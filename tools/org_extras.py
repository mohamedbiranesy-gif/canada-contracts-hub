#!/usr/bin/env python3
"""Extra facts an organisation prints on its own site (buyers and vendors), evidence or nothing:
  - legal name as printed in the copyright / footer line ("© 2026 Acme Holdings Inc.", "Tous droits réservés Ville de X");
  - Business Number / GST-HST / charity registration number as printed ("GST/HST # 123456789 RT0001", "BN 12345 6789 RR0001",
    "Numéro d'entreprise du Québec 1234567890" → NEQ); the GST/HST account is derived from a BN9 and always labelled so;
  - logo image URL (og:image or an <img> whose src / alt says logo);
  - language of the site (fr / en / fr-en from the html lang attribute and stopwords);
  - whether the site answers (status).
  v3 (2026-11-10, the bill-to legal name of 160,000 rows): the name printed WITH its legal form anywhere on the organisation's pages that its
    own domain name spells ("Credit Lift Inc." on creditlift.ca); the legal person a page puts behind the site's name ("Majid Enterprises Inc.,
    operating as Lawn Lovers", "Solaris (1457570 Alberta Ltd.)", "Legal Entity : …"); the operator a page names; the home page's title and
    og:site_name; a Shopify store's fixed policy pages; the five pages are chosen among ALL the links of the home page.
  v2 (2026-11-08, downstream coverage targets): schema.org JSON-LD Organization facts (legalName, address, telephone, logo, taxID,
    foundingDate, numberOfEmployees, sameAs); the legal name stated on Terms / Privacy / Legal pages ("operated by X Inc.",
    "X Inc. ("we")", "The Corporation of the City of X", "Centre de services scolaire de X"); logo from the header or the
    site icon when no og:image; links to supplier / e-tendering / e-invoicing / e-signature portals (ap_system_hint);
    payment-method, tax-exempt and e-signature mentions; LinkedIn page. Shared hosts (canada.ca, gov.bc.ca, ontario.ca …)
    are read from the organisation's own start URL, not the host root.
Reads the home page and up to five "about / legal / privacy / terms / contact" pages. Polite: robots.txt, 1 request / second / host,
identified UA. Output: ~/cch-crawler-state/org_extras.jsonl (resume) and <repo>/data/incoming/claude/claude_org_extras.jsonl.gz
(read by contrib/claude/rank_buyers/rank.py), one JSON per registrable domain (per start URL on shared hosts) with the page URL
and a ≤300-char quote per fact.
  python3 tools/org_extras.py --tasks tasks.csv [--workers 48] [--repo ~/cch-crawler] [--refresh] [--test URL ...]
  --refresh re-reads domains whose record predates v2 or failed on a redirect / network error (old facts are kept when the new read fails).
"""
V = 3
import argparse, csv, gzip, html, json, os, re, sys, threading, time, unicodedata, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C
from org_contacts import strip_long, visible_keep_lines, flat

STATE = os.path.expanduser("~/cch-crawler-state")
RESUME = os.path.join(STATE, "org_extras.jsonl")
TODAY = time.strftime("%Y-%m-%d")
lock = threading.Lock()
COPY = re.compile(r"(?:©|&copy;|\(c\)|copyright|tous droits r[ée]serv[ée]s|all rights reserved)[\s,.]*(?:copyright\s*)?(?:(?:19|20)\d\d(?:\s*[-–]\s*(?:19|20)?\d\d)?)?[\s,.]*"
                  r"(?:by\s+|par\s+)?([A-Z0-9][^|•\n©]{2,90}?)(?=\s*(?:\.|\||•|all rights|tous droits|\s[-–—]\s|$|\n|privacy|confidentialit|terms|conditions|site|powered|design|web|\d{4}))", re.I)
COPY2 = re.compile(r"([A-Z0-9][^|•\n©]{2,90}?)\s*(?:©|&copy;)\s*(?:19|20)\d\d", re.I)
LEGAL_TAIL = re.compile(r"\b(inc|incorporated|ltd|limited|lt[ée]e|llc|llp|lp|corp|corporation|co|company|s\.?e\.?n\.?c|s\.?a|plc|gmbh|ag|srl|ulc|society|association|foundation|fondation|"
                        r"university|universit[ée]|college|coll[èe]ge|c[ée]gep|city of|town of|village of|municipality of|ville de|municipalit[ée] de|county of|district of|"
                        r"regional district of|township of|first nation|nation|band|school board|school division|school district|conseil scolaire|centre de services scolaire|"
                        r"commission scolaire|hospital|health|sant[ée]|authority|board|commission|agency|office|ministry|department|government|gouvernement|library|biblioth[èe]que|"
                        r"church|[ée]glise|parish|paroisse|trust|group|groupe|holdings|partners|partnership|cooperative|co-op|coop|credit union|caisse)\b", re.I)
BN = re.compile(r"(?:(?:GST|HST|GST/HST|TPS|TVH|TPS/TVH|business\s*number|numéro\s*d['’]entreprise(?:\s*(?:f[ée]d[ée]ral|du\s*Canada))?|\bBN\b|charitable\s*registration|registration\s*(?:no|number|#)|"
                r"num[ée]ro\s*d['’]enregistrement|num[ée]ro\s*d['’]organisme\s*de\s*bienfaisance|charity\s*(?:no|number|#)|RR\s*0001|RT\s*0001)[^\d/A-Za-z]{0,12}(?:[A-Za-z]{0,3}[^\d/A-Za-z]{0,6})?)"
                r"(?<![\dA-Za-z/])(\d{5}\s?\d{4}|\d{9})(?!\d)\s*((?:RT|RR|RP|RC)\s?\d{4})?", re.I)
NEQ = re.compile(r"(?:NEQ|num[ée]ro\s*d['’]entreprise\s*du\s*Qu[ée]bec)[^\d]{0,20}(\d{10})\b", re.I)
QST = re.compile(r"(?:TVQ|QST)[^\d]{0,15}(\d{10})\s*(TQ\s?\d{4})", re.I)
LOGO = re.compile(r"(?is)<img[^>]+(?:src|data-src)\s*=\s*[\"']([^\"']+)[\"'][^>]*>")
OG = re.compile(r"(?is)<meta[^>]+property\s*=\s*[\"']og:image[\"'][^>]+content\s*=\s*[\"']([^\"']+)")
OG2 = re.compile(r"(?is)<meta[^>]+content\s*=\s*[\"']([^\"']+)[\"'][^>]+property\s*=\s*[\"']og:image[\"']")
LANG = re.compile(r"(?is)<html[^>]+lang\s*=\s*[\"']([a-zA-Z]{2})")
FRW = re.compile(r"\b(de la|des|les|pour|avec|nous|vous|notre|votre|est|sont|une|dans|sur|à propos|accueil|nous joindre|services)\b", re.I)
ENW = re.compile(r"\b(the|and|for|with|our|your|about|home|contact|services|from|this|that|are|is|more)\b", re.I)
PAGE_LINK = re.compile(r"about|a-propos|apropos|legal|mentions|privacy|confidentialit|terms|conditions|contact|nous-joindre|donate|don\b|faire-un-don|give|charitable|tax-receipt|re[cç]u|accessibilit|disclaimer|avis", re.I)
LEGAL_PAGE = re.compile(r"legal|mentions|privacy|confidentialit|terms|conditions|disclaimer|avis|accessibilit|about|a-propos|apropos", re.I)
# shared hosts: many organisations publish under one registrable domain; each is read from its own start URL
SHARED_HOSTS = re.compile(r"(?:^|\.)(canada\.ca|gc\.ca|gov\.bc\.ca|ontario\.ca|gouv\.qc\.ca|quebec\.ca|alberta\.ca|gov\.ab\.ca|novascotia\.ca|gnb\.ca|gov\.mb\.ca|"
                          r"saskatchewan\.ca|gov\.sk\.ca|gov\.nl\.ca|gov\.pe\.ca|yukon\.ca|gov\.nt\.ca|gov\.nu\.ca|gov\.au|gov\.uk|nhs\.uk|[a-z]{2}\.gov|[a-z]{2}\.us|wordpress\.com|wixsite\.com|squarespace\.com|weebly\.com|godaddysites\.com|google\.com|sites\.google\.com)$", re.I)
ORG_TYPES = re.compile(r"Organization|Corporation|GovernmentOrganization|EducationalOrganization|CollegeOrUniversity|School|Hospital|MedicalOrganization|NGO|LocalBusiness|"
                       r"Library|Airport|SportsOrganization|Consortium|FundingAgency|ResearchOrganization|WorkersUnion|PerformingGroup|MedicalClinic|Dentist|Physician|"
                       r"ProfessionalService|Store|FinancialService|InsuranceAgency|BankOrCreditUnion|Service|Place|CivicStructure|GovernmentOffice|Museum|Church|PublicSwimmingPool", re.I)
NOT_ORG_TYPES = re.compile(r"^(?:Person|Article|NewsArticle|BlogPosting|WebPage|WebSite|BreadcrumbList|ItemList|Event|Product|Offer|Review|ImageObject|VideoObject|SearchAction|"
                           r"FAQPage|Question|Answer|JobPosting|Recipe|Course|CreativeWork|ListItem|SiteNavigationElement|WPHeader|WPFooter|Thing)$", re.I)
CAPW = r"(?:[A-Z0-9][A-Za-z0-9ÀÉÈÊÎÔÛàâçéèêëîïôöûüÿ'’.\-]*(?: (?:of|de|du|des|the|and|&|la|le|les|d['’]|et|en|pour|for|à|au|aux|sur|sous))? ){1,6}"
PUBLIC_BODY = re.compile(r"\b((?:The )?Corporation of the (?:City|Town|Township|Village|Municipality|County|District|Regional Municipality|United Counties|Municipal District|Norfolk County|Haldimand County)"
                         r"(?: of)? [A-Z][A-Za-zÀ-ÿ'’.\- ]{2,60}?|(?:Ville|Municipalit[ée]|Municipalit[ée] r[ée]gionale de comt[ée]|MRC|Paroisse|Canton|Village|Cit[ée]) (?:de |du |des |d['’])[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,60}?|"
                         r"Centre de services scolaire (?:de |du |des |d['’])[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,60}?|Commission scolaire (?:de |du |des |d['’])[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,60}?|"
                         r"Conseil scolaire [A-Za-zÀ-ÿ'’\- ]{3,70}?|C[IU]?SSS (?:de |du |des |d['’])[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,70}?|" + CAPW + r"(?:District |Regional |Catholic |Public |Francophone )*School (?:Board|Division|District)(?: No\.? ?\d+)?|"
                         r"Regional District of [A-Z][A-Za-z'’\- ]{2,50}?|(?:Regional Municipality|County|Municipal District|Township|Town|City|Village|District|Rural Municipality|Resort Municipality) of [A-Z][A-Za-zÀ-ÿ'’.\- ]{2,50}?|"
                         r"Universit[ée] (?:de |du |d['’])[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,50}?|University of [A-Z][A-Za-z'’\- ]{2,50}?|" + CAPW + r"(?:University|Polytechnic|College|Health (?:Authority|Services|Sciences Centre|Sciences)|Hospital|Library Board|Police Services? Board|Conservation Authority|Transit Commission|Housing Corporation)"
                         r")(?=[\s,.;:)(\]|\"“”«»]|$)")
LEGAL_FORM_NAME = re.compile(r"\b(" + CAPW + r"(?:Inc\.?|Incorporated|Ltd\.?|Limited|Lt[ée]e\.?|LLC|L\.L\.C\.|LLP|L\.L\.P\.|LP|L\.P\.|Corp\.?|Corporation|Co\.|Company|S\.?E\.?N\.?C\.?|s\.e\.c\.|S\.A\.|S\.A\.R\.L\.|SARL|GmbH|AG|plc|ULC|"
                             r"Society|Trust|Credit Union|Co-?operative|Cooperative|Group|Groupe|Holdings|Partners|Partnership|Authority|Commission|Agency|Board|Institute|Institut|Foundation|Association)|"
                             r"(?:Soci[ée]t[ée]|Association|Fondation|Caisse(?: populaire| Desjardins)?|Coop[ée]rative|Groupe|Institut|Centre|Office|Conseil|F[ée]d[ée]ration|Ordre|Corporation|R[ée]gie|Agence|Commission|Minist[èe]re) (?:[a-zà-ÿ'’\-]+ ){0,4}[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\- ]{2,60}?)"
                             r"(?=[\s,.;:)(\]|\"“”«»]|$)")
ABBR_DEF = re.compile(r"((?:[A-Z0-9][A-Za-z0-9ÀÉÈÊÎÔÛàâçéèêëîïôöûüÿ'’.\-]*|of|de|du|des|the|and|&|la|le|les|d['’]|et|en|pour|for|à|au|aux)(?: (?:[A-Z0-9][A-Za-z0-9ÀÉÈÊÎÔÛàâçéèêëîïôöûüÿ'’.\-]*|of|de|du|des|the|and|&|la|le|les|d['’]|et|en|pour|for|à|au|aux|[a-zà-ÿ]{2,12})){0,8})"
                      r"\s*\(\s*(?:(?:hereinafter|ci-apr[èe]s|the|la|le|l['’])\s*)?[\"“«']?\s*([A-Z][A-Za-z]{1,7})\s*[\"”»']?\s*\)")
CONNECT = {"of", "de", "du", "des", "the", "and", "&", "la", "le", "les", "d'", "d’", "et", "en", "pour", "for", "à", "au", "aux"}
OPERATED_BY = re.compile(r"(?:(?:is |are |website |site |web ?site |ce site (?:web )?(?:est |a été )?)(?:owned|operated|run|maintained|published|provided|managed|exploit[ée]|g[ée]r[ée]|administr[ée]|publi[ée]|[ée]dit[ée])(?: and (?:operated|maintained|managed))? (?:by|par) |"
                         r"(?:a (?:web ?site|site) of|un site (?:web )?de) |(?:property of|propri[ée]t[ée] de) |(?:entre vous et|between you and) |(?:la pr[ée]sente politique|this (?:privacy )?policy) (?:describes|explains|s'applique|applies to) (?:how |the way |la fa[çc]on dont )?)"
                         r"([A-Z][A-Za-z0-9&'’.,\-ÀÉÈÊÎÔÛàâçéèêëîïôöûüÿ ]{2,90}?)(?=\s*(?:[(,.;:]|\(|«|\"|“|'|and its|et ses| is | a | the | which | who |$))", re.M)
WE_DEF = re.compile(r"([A-Z][A-Za-z0-9&'’.,\-ÀÉÈÊÎÔÛàâçéèêëîïôöûüÿ ]{2,90}?)\s*\((?:\s*(?:hereinafter|ci-apr[èe]s|collectively|together|referred to as|the|la|le|l['’]|also|or|ou)\s*)*[\"“«']?\s*(?:we|us|our|the Company|the Corporation|the City|the Town|the Municipality|the University|the College|the Hospital|the Board|the Society|the Organization|the Organisation|"
                    r"nous|notre|la Ville|la Municipalit[ée]|la Soci[ée]t[ée]|l['’]Organisme|l['’]Universit[ée]|le Coll[èe]ge|le Centre|the Authority|the Agency)\b", re.I)
PORTALS = [("ariba.com", "SAP Ariba", "e-procurement / e-invoicing"), ("coupa.com", "Coupa", "e-procurement / e-invoicing"), ("coupahost", "Coupa", "e-procurement / e-invoicing"), ("jaggaer", "Jaggaer", "e-procurement"), ("sciquest", "Jaggaer (SciQuest)", "e-procurement"),
           ("bidsandtenders", "bids&tenders", "e-tendering"), ("bonfirehub", "Bonfire", "e-tendering"), ("biddingo", "Biddingo", "e-tendering"), ("merx.com", "MERX", "e-tendering"), ("seao.ca", "SEAO", "e-tendering"), ("seao.gouv.qc.ca", "SEAO", "e-tendering"),
           ("bcbid", "BC Bid", "e-tendering"), ("purchasingconnection", "Alberta Purchasing Connection", "e-tendering"), ("sasktenders", "SaskTenders", "e-tendering"), ("nbon.gnb.ca", "NBON", "e-tendering"), ("publicpurchase.com", "Public Purchase", "e-tendering"),
           ("demandstar", "DemandStar", "e-tendering"), ("bidnetdirect", "BidNet Direct", "e-tendering"), ("bidsync", "Periscope / BidSync", "e-tendering"), ("periscopeholdings", "Periscope", "e-tendering"), ("ionwave", "IonWave", "e-tendering"), ("opengov.com", "OpenGov Procurement", "e-tendering"),
           ("vendorregistry", "Vendor Registry", "e-tendering"), ("planetbids", "PlanetBids", "e-tendering"), ("bidexpress", "Bid Express", "e-tendering"), ("canadabuys", "CanadaBuys", "e-tendering"), ("buyandsell.gc.ca", "CanadaBuys", "e-tendering"), ("tendersnb", "NBON", "e-tendering"),
           ("tungsten-network", "Tungsten Network", "e-invoicing"), ("tungsten.", "Tungsten Network", "e-invoicing"), ("taulia", "Taulia", "e-invoicing / supplier payments"), ("basware", "Basware", "e-invoicing"), ("esker", "Esker", "e-invoicing"), ("paymentworks", "PaymentWorks", "supplier onboarding / payments"),
           ("billtrust", "Billtrust", "e-invoicing"), ("tipalti", "Tipalti", "supplier payments"), ("oraclecloud.com", "Oracle Fusion Cloud (supplier portal)", "e-procurement"), ("myworkday.com", "Workday", "e-procurement / supplier portal"), ("workday.com", "Workday", "e-procurement / supplier portal"), ("sap.com/business-network", "SAP Business Network", "e-invoicing"),
           ("peoplesoft", "PeopleSoft", "finance system"), ("unit4", "Unit4", "finance system"), ("bidsandtenders.ca", "bids&tenders", "e-tendering"), ("docusign", "DocuSign", "e-signature"), ("adobesign", "Adobe Sign", "e-signature"), ("echosign", "Adobe Sign", "e-signature"), ("hellosign", "Dropbox Sign", "e-signature"), ("consigno", "ConsignO", "e-signature"),
           ("yardi", "Yardi", "finance system"), ("vendorcafe", "Yardi VendorCafe", "supplier portal"), ("nexonia", "Nexonia", "finance system"), ("supplier.", "supplier portal", "supplier portal"), ("vendorportal", "vendor portal", "supplier portal"), ("fournisseurs.", "portail fournisseurs", "supplier portal")]
MENTIONS = {"payment_method": re.compile(r"((?:direct deposit|d[ée]p[ôo]t direct|electronic funds transfer|\bEFT\b|\bACH\b|virement(?: bancaire| [ée]lectronique)?|e-?transfer|\bInterac\b(?!t)|paid by cheque|payment by cheque|par ch[èe]que|credit card payments?|\bP-?card\b|wire transfer)[^.\n]{0,80})", re.I),
            "tax_exempt": re.compile(r"((?:tax[- ]exempt(?:ion)?|exempt from (?:GST|HST|PST|sales tax|the goods and services tax)|exon[ée]r[ée]e?s? de (?:la )?(?:TPS|TVQ|TVH|taxe)|HST rebate|GST rebate|PST exempt|exemption de taxe|municipal rebate)[^.\n]{0,80})", re.I),
            "esignature": re.compile(r"((?:DocuSign|Adobe Sign|AdobeSign|electronic signatures?|digital signatures?|signatures? [ée]lectroniques?|signatures? num[ée]riques?|e-?signatures?)[^.\n]{0,80})", re.I),
            "ap_cycle": re.compile(r"((?:cheque runs?|payment runs?|payments? (?:are|is) (?:issued|processed|made|released) (?:weekly|bi-?weekly|every|on|twice|once|within)|paiements? (?:sont )?(?:[ée]mis|effectu[ée]s|trait[ée]s) (?:chaque|toutes? les|le|hebdomadaire)|cycle de paiement|invoices? (?:are|is) paid (?:within|net|on|in))[^.\n]{0,80})", re.I)}
# a mention counts only in an accounts-payable / supplier context, never in site boilerplate (cookies, DMCA, donations, newsletters)
MENTION_CONTEXT = re.compile(r"invoice|factur|supplier|vendor|fournisseur|payable|payment to|paiement|purchase order|bon de commande|accounts payable|comptes [àa] payer|remit|remise|procurement|approvisionnement|purchasing|achats", re.I)
MENTION_NOISE = re.compile(r"copyright|dmca|infring|cookie|newsletter|donat|don\b|tax receipt|re[çc]u|charitable|patient|student|[ée]tudiant|tuition|membership|adh[ée]sion|property tax|taxes fonci|parking|stationnement|utility bill|water bill|facture d['’]eau|compte de taxes", re.I)
TEL_HREF = re.compile(r"(?i)href\s*=\s*[\"']tel:([^\"']{7,30})[\"']")
ICON = re.compile(r"(?is)<link[^>]+rel\s*=\s*[\"'](?:apple-touch-icon(?:-precomposed)?|icon|shortcut icon)[\"'][^>]*>")
HREF = re.compile(r"(?is)href\s*=\s*[\"']([^\"']+)[\"']")
LINKEDIN = re.compile(r"https?://(?:[a-z]{2,3}\.)?linkedin\.com/(?:company|school|showcase)/[A-Za-z0-9_%.\-]+/?", re.I)
HEADER_IMG = re.compile(r"(?is)<(?:header|nav|div)[^>]*(?:class|id)\s*=\s*[\"'][^\"']*(?:header|navbar|brand|logo|masthead|site-title|banner)[^\"']*[\"'][^>]*>(.*?)</(?:header|nav|div)>")


def quote_at(text, needle, n=300):
    i = text.find(needle)
    if i < 0:
        return flat(needle)[:n]
    return flat(text[max(0, i - 100):i + len(needle) + 100])[:n]


def legal_name(text, host):
    """the organisation's legal name as printed in the copyright line, if it looks like a legal name"""
    cands = []
    for rx in (COPY, COPY2):
        for m in rx.finditer(text):
            c = flat(m.group(1))
            c = re.sub(r"^(?:by|par)\s+", "", c, flags=re.I).strip(" .,-–—|")
            c = re.split(r"\s+(?:registered charity|charitable registration|accessibilit|privacy|confidentialit|terms|conditions|sitemap|plan du site|contact|"
                         r"disclaimer|avis|legal|mentions l[ée]gales|login|connexion|back to top|retour|website|site web|powered|design)\b", c, 1, flags=re.I)[0].strip(" .,-–—|:")
            if 3 <= len(c) <= 90 and LEGAL_TAIL.search(c) and not re.search(r"\b(?:website|site web|design|powered|theme|wordpress|squarespace|wix|shopify|developed|développ|réalis|created|made with|hosting)\b", c, re.I):
                cands.append(c)
    if not cands:
        return ""
    # prefer the shortest candidate that still ends with / contains a legal form word near its end
    cands.sort(key=lambda c: (not re.search(r"\b(inc|ltd|limited|lt[ée]e|llc|llp|corp|corporation|co|society|association|foundation|fondation)\.?$", c, re.I), len(c)))
    return cands[0]


def _walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from _walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from _walk(v)


def _types(o):
    t = o.get("@type") or o.get("type") or ""
    return [t] if isinstance(t, str) else [x for x in t if isinstance(x, str)] if isinstance(t, list) else []


def _str(v):
    if isinstance(v, str):
        return flat(html.unescape(v))
    if isinstance(v, dict):
        return _str(v.get("name") or v.get("url") or v.get("@id") or v.get("value") or "")
    if isinstance(v, list):
        return "; ".join(x for x in (_str(i) for i in v[:3]) if x)
    return flat(str(v)) if v not in (None, "", 0) else ""


def _addr(a):
    if isinstance(a, list):
        a = next((x for x in a if isinstance(x, dict)), a[0] if a else None)
    if isinstance(a, dict):
        parts = [_str(a.get(k)) for k in ("streetAddress", "addressLocality", "addressRegion", "postalCode", "addressCountry")]
        if parts[0] and (parts[1] or parts[3]):
            return ", ".join(p for p in parts if p)[:200]
        return ""
    if isinstance(a, str) and re.search(r"\d", a) and 10 < len(a) < 200:
        return flat(a)
    return ""


def jsonld_org(raw, host, name):
    """schema.org Organization (or subtype) facts from the page's JSON-LD; the object whose url / @id is on this host or whose
    name shares the organisation's core tokens wins; Person / Article / WebPage objects are ignored"""
    best, best_score = None, -1
    core = {t for t in re.findall(r"[a-z0-9]{3,}", (name or "").lower()) if t not in ("the", "and", "inc", "ltd", "city", "town", "ville", "corporation", "limited", "des", "les")}
    for m in re.finditer(r"(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>", raw):
        txt = m.group(1).strip()
        try:
            data = json.loads(txt)
        except Exception:
            try:
                data = json.loads(re.sub(r",\s*([}\]])", r"\1", txt))
            except Exception:
                continue
        for o in _walk(data):
            if not isinstance(o, dict):
                continue
            ts = _types(o)
            if not ts or any(NOT_ORG_TYPES.match(t) for t in ts) or not any(ORG_TYPES.search(t) for t in ts):
                if not o.get("legalName"):
                    continue
            nm = _str(o.get("legalName") or o.get("name"))
            if not nm or len(nm) < 3:
                continue
            url = _str(o.get("url") or o.get("@id"))
            uh = (urllib.parse.urlparse(url).hostname or "").lower().removeprefix("www.") if "//" in url else ""
            score = 0
            if uh and (uh == host or uh.endswith("." + host) or host.endswith("." + uh)):
                score += 3
            toks = set(re.findall(r"[a-z0-9]{3,}", nm.lower()))
            if core and core & toks:
                score += 2
            if o.get("legalName"):
                score += 1
            if any(t in ("Organization", "GovernmentOrganization", "EducationalOrganization", "Corporation", "CollegeOrUniversity", "Hospital", "NGO") for t in ts):
                score += 1
            if score > best_score:
                best, best_score = o, score
    if best is None or best_score < 2:
        return {}
    o = best
    out = {"jsonld_type": "/".join(_types(o))[:60], "jsonld_name": _str(o.get("name"))[:120], "jsonld_legal_name": _str(o.get("legalName"))[:120],
           "jsonld_alternate_name": _str(o.get("alternateName"))[:120], "jsonld_address": _addr(o.get("address")), "jsonld_phone": _str(o.get("telephone"))[:40],
           "jsonld_email": _str(o.get("email")).replace("mailto:", "")[:80], "jsonld_logo": _str(o.get("logo"))[:300], "jsonld_url": _str(o.get("url"))[:200],
           "jsonld_founding_date": _str(o.get("foundingDate"))[:20], "jsonld_tax_id": _str(o.get("taxID") or o.get("vatID"))[:40], "jsonld_duns": _str(o.get("duns"))[:20],
           "jsonld_lei": _str(o.get("leiCode"))[:30], "jsonld_naics": _str(o.get("naics"))[:40], "jsonld_employees": _str(o.get("numberOfEmployees"))[:40],
           "jsonld_parent": _str(o.get("parentOrganization"))[:120], "jsonld_same_as": "; ".join(x for x in (_str(u) for u in (o.get("sameAs") if isinstance(o.get("sameAs"), list) else [o.get("sameAs")])) if x)[:400]}
    out = {k: v for k, v in out.items() if v}
    if out:
        out["jsonld_quote"] = flat(txt)[:300]
    return out


def legal_name_text(text, host, name):
    """the legal name a Terms / Privacy / Legal page states: "operated by X Inc.", "X Inc. ("we", "us")", a public body's full style"""
    cands = []
    def anchored(seg, pos=None):
        """the legal-form / public-body name inside a captured segment (the capture may start a few words early: "Welcome to X University");
        the longer of the two patterns' matches wins ("Hamilton Health Sciences Corporation" over "Hamilton Health Sciences")"""
        ms = []
        if pos is not None:
            ms += [m.group(1) for m in (PUBLIC_BODY.match(text, pos), LEGAL_FORM_NAME.match(text, pos)) if m]
        if not ms:
            ms += [m.group(1) for m in (PUBLIC_BODY.search(seg), LEGAL_FORM_NAME.search(seg)) if m]
        return max(ms, key=len) if ms else seg
    def initials_ok(seg, abbr):
        words = [w for w in re.findall(r"[A-Za-zÀ-ÿ0-9'’]+", seg) if w.lower() not in CONNECT]
        ini = "".join(w[0] for w in words).upper()
        return len(words) >= 2 and (ini == abbr.upper() or ini.endswith(abbr.upper()) and len(abbr) >= 3)
    for m in OPERATED_BY.finditer(text):
        cands.append((0, anchored(m.group(1), m.start(1))))
    for m in WE_DEF.finditer(text):
        cands.append((1, anchored(m.group(1))))
    for m in ABBR_DEF.finditer(text):
        seg, abbr = m.group(1).strip(), m.group(2)
        if PUBLIC_BODY.search(seg) or LEGAL_FORM_NAME.search(seg):
            cands.append((1, anchored(seg)))
        elif initials_ok(seg, abbr):
            words = [w for w in re.findall(r"[A-Za-zÀ-ÿ0-9'’]+", seg) if w.lower() not in CONNECT]
            k = len(abbr)  # the name is the last k significant words (plus connectors between them)
            start = seg.rfind(words[-k]) if k <= len(words) else 0
            cands.append((1, seg[start:].strip()))
    for m in PUBLIC_BODY.finditer(text):
        cands.append((2, m.group(1)))
    core = {t for t in re.findall(r"[a-z0-9]{3,}", unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()) if t not in ("the", "and", "inc", "ltd", "city", "town", "ville", "corporation", "limited", "des", "les", "municipality", "county", "canada", "group", "groupe", "ltee", "corp", "company")}
    out = []
    for rank, c in cands:
        c = flat(c).strip(" .,;:-–—|«»\"“”'")
        c = re.sub(r"^(?:by|par|the|la|le|l['’])\s+", lambda m: m.group(0) if re.match(r"(?i)the corporation", c) else "", c, flags=re.I).strip()
        if not (3 <= len(c) <= 90) or re.search(r"\b(?:website|site web|cookies?|browser|google|facebook|wordpress|privacy policy|politique)\b", c, re.I):
            continue
        if rank < 2 and not (LEGAL_FORM_NAME.search(c + " ") or PUBLIC_BODY.search(c) or LEGAL_TAIL.search(c) or (len(c.split()) >= 2 and c[0].isupper() and sum(w[0].isupper() for w in c.split()) >= 2)):
            continue  # "operated by our team" / "between you and us"
        toks = set(re.findall(r"[a-z0-9]{3,}", unicodedata.normalize("NFKD", c).encode("ascii", "ignore").decode().lower()))
        hostc = unicodedata.normalize("NFKD", host or "").encode("ascii", "ignore").decode().lower().replace("-", "").replace("www.", "")
        hit = bool(core & toks) or (hostc and any(t in hostc for t in toks if len(t) >= 4 and t not in ("city", "town", "ville", "county", "canada", "ontario", "quebec", "group", "groupe")))
        if not hit:
            continue  # a defined term, another body named on the page ("Ville de Granby" on Waterloo's site), a law ("PIPEDA"): not this organisation
        out.append((0, rank, len(c), c))
    if not out:
        return ""
    out.sort()
    return out[0][3]


# ---- v3 (2026-11-10): the name an organisation prints WITH its legal form, tied to the site by what its own address spells ----
# Measured on 317 sites whose record held no legal name: 31 print a name with a legal form whose words spell their domain name ("Credit Lift Inc."
# on creditlift.ca, "Autoénergie Canada inc." on autoenergie.com, "M.A.C. Trucking Ltd" on mactrucking.ca), 17 of them on the home page itself,
# outside any copyright line or "operated by" sentence. On 324 sites that had a legal name the rule agreed with it 81 times, and of the 15 times it
# differed it was right 14 times ("Liberty Security Systems Inc." where the record held "Canadian Security Association", "Spurrell Professional
# Corporation" where it held "Secure Sockets Layer").
SUF3 = re.compile(r"(?<![\w.\-/])(Inc|Incorporated|Incorpor[ée]e|Ltd|Limited|Limit[ée]e|Lt[ée]e|Corp|Corporation|LLP|L\.L\.P|LLC|L\.L\.C|PLC|GmbH|S\.E\.N\.C\.R\.L|S\.E\.N\.C|SENCRL|SENC|ULC|U\.L\.C)(?![\w\-])\.?", re.I)
_W3 = re.compile(r"^(?:[A-Z0-9À-Ý][\w'’.+\-À-ÿ&]*|[a-z]{1,3}[A-Z][\w'’.+\-À-ÿ]*|[dDlL]['’][A-ZÀ-Ý][\w'’\-À-ÿ]*|&|\+)$")  # a capitalised word, a number, "eBay", "d'Amour", & or +
_J3 = {"and", "et", "of", "de", "du", "des", "la", "le", "les", "the", "for", "pour", "à", "au", "aux", "en", "sur", "&", "+"}
CHROME3 = set("""privacy policy policies politique politiques confidentialité confidentialite terms conditions modalités modalites copyright rights reserved droits réservés reserves
home accueil contact contactez about menu search recherche login connexion cart panier skip content contenu welcome bienvenue notice statement agreement disclaimer legal
mentions légales legales introduction overview website site page section article effective date updated last version english français francais follow suivez subscribe
january february march april may june july august september october november december janvier février mars avril mai juin juillet août septembre octobre novembre décembre
monday tuesday wednesday thursday friday saturday sunday lundi mardi mercredi jeudi vendredi samedi dimanche phone tel téléphone email courriel fax address adresse hours heures
facebook instagram twitter linkedin youtube tiktok pinterest shop boutique checkout account compte cookies cookie sitemap careers carrières faq blog news nouvelles
by par with avec from our notre nos your votre vos this these that those ce cette ces all tous toutes and/or""".split())
# companies a site names because it uses them, never because it is them (platforms, payment and advertising services, franchisors, carriers)
THIRD3 = re.compile(r"\b(?:shopify|google|alphabet|meta platforms|facebook|instagram|whatsapp|stripe|paypal|houzz|wix|squarespace|godaddy|weebly|webflow|interac|apple|microsoft|amazon|mailchimp|"
                    r"intuit|hubspot|cloudflare|automattic|wordpress|lightspeed|block|square|moneris|visa|mastercard|american express|amex|klarna|afterpay|affirm|sezzle|paybright|re/?max|"
                    r"royal lepage|century 21|sotheby|keller williams|coldwell|canada post|postes canada|united parcel|ups|fedex|federal express|purolator|dhl|youtube|linkedin|twitter|"
                    r"tiktok|pinterest|yelp|tripadvisor|adobe|oracle|salesforce|zoom video|calendly|eventbrite|ticketmaster|booking|expedia|airbnb|uber|doordash|skipthedishes|jane software|"
                    r"mindbody|vagaro|constant contact|sendgrid|twilio|zendesk|atlassian|slack|dropbox|vimeo|network advertising|digital advertising|odoo|bigcommerce|ecwid|jimdo|duda|"
                    r"wordfence|growthzone|civicplus|granicus|esolutions|blackbaud|global payments|elavon|chase|clover|toast|opentable|resy|yext|trustpilot|birdeye|podium|klaviyo|"
                    r"cookiebot|onetrust|termly|iubenda|termsfeed|freeprivacypolicy|privacypolicies|getterms|cookieyes|complianz|osano|usercentrics|web\.com|bluehost|hostgator|ionos|ovh)\b", re.I)
NUMBERED3 = re.compile(r"^\d[\d\-]{3,9}$")
_ART3 = re.compile(r"^(?:The|Les|Le|La|THE|LES|LE|LA)$")
ABBR3 = re.compile(r"(?:[A-Za-zÀ-ÿ]\.)+|(?:St|Ste|Mt|Dr|Jr|Sr|Bros|Mfg|Intl|Assoc|Wm|Geo|Co|No|Pvt|Pty)\.")
ENDINGS3 = set("canada ca inc ltd corp co online store shop boutique group groupe qc quebec web site services service solutions official usa us na".split())
PROV3 = re.compile(r"(?i)(?:qu[ée]bec|canada|ontario|alberta|manitoba|saskatchewan|b\.?c\.?|british|nova|n\.?[bs]\.?|new|yukon|newfoundland|nunavut|p\.?e\.?i\.?)\b")
DBA3 = re.compile(r"\s*[,(]?\s*(?:operating as|doing business as|carrying on business as|trading as|o/a|d/b/a|d\.b\.a\.?|dba|faisant affaires? sous(?: le nom| la raison sociale| la d[ée]nomination(?: sociale)?)?(?: de)?|"
                  r"op[ée]rant sous le nom(?: de)?|exploitant l['’]entreprise)\s*[:\-–]?\s*[\"“«‘']?\s*", re.I)
ALIAS3 = re.compile(r"\s*,?\s*\(\s*(?:hereinafter|hereafter|ci-apr[èe]s|collectively|together|referred to as|d[ée]sign[ée]e? (?:comme|par)|the|la|le|l['’]|,|\s)*[\"“«‘']\s*([^\"”»’'()]{2,40}?)\s*,?\s*[\"”»’'](?=[^()]{0,70}\b(?:we|us|our|nous|notre|nos)\b)", re.I)
LABELLED3 = re.compile(r"(?:Legal (?:Entity|Name)|Registered (?:Company |Business )?Name|Company Legal Name|Raison sociale|D[ée]nomination sociale|Nom l[ée]gal(?: de l['’]entreprise)?)\s*[:：]\s*", re.I)
OPER3 = re.compile(r"(?:(?:owned and )?operated|published|(?:d[ée]tenue?s? et )?exploit[ée]e?s?|[ée]dit[ée]e?s?)\s+(?:by|par)\s*:?\s*(?:the\s+|la\s+|le\s+|l['’]\s*)?[\"“«]?\s*", re.I)
SHOPIFY3 = re.compile(r"cdn\.shopify\.com|Shopify\.(?:shop|theme|routes)\b|\.myshopify\.com", re.I)
STORE_POLICIES = ("/policies/legal-notice", "/policies/contact-information", "/policies/terms-of-service", "/policies/privacy-policy")
TITLE3 = re.compile(r"(?is)<title[^>]*>(.*?)</title>")
OGSN3 = re.compile(r"(?is)<meta[^>]+property\s*=\s*[\"']og:site_name[\"'][^>]+content\s*=\s*[\"']([^\"']{2,120})|<meta[^>]+content\s*=\s*[\"']([^\"']{2,120})[\"'][^>]+property\s*=\s*[\"']og:site_name[\"']")


def letters3(s):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())


def host_label(host):
    """the first label of the site's registrable domain, letters and digits only ("" on a host many organisations share)"""
    h = (host or "").lower().removeprefix("www.")
    dom = C.registrable(h) or h
    if not dom or SHARED_HOSTS.search(h) or SHARED_HOSTS.search(dom) or re.search(r"(?:^|\.)(?:myshopify\.com|wixsite\.com|webflow\.io|github\.io|netlify\.app|square\.site|business\.site|"
                                                                                 r"blogspot\.com|strikingly\.com|carrd\.co|facebook\.com|linktr\.ee|jimdofree\.com|webnode\.\w+|site123\.me)$", dom):
        return ""
    return re.sub(r"[^a-z0-9]", "", dom.split(".")[0])


def _name_runs(text, loose=False):
    """every name printed with a legal form: (words before the form, the form as printed, start of the first word, end of the form, cut) — the words
    are read backwards from the form while they look like the words of a name; `cut` says the reading stopped at its limit, not at the name's start.
    loose: words written small are read too ("Centre dentaire Ahuntsic inc."); the caller then takes only what the site's own address spells."""
    for m in SUF3.finditer(text):
        if re.match(r"\s+(?:of|de|du|des|d['’])\s", text[m.end():m.end() + 6]):
            continue  # "The Corporation of the Town of …", "Limited edition"
        if m.group(1).islower() and m.group(1) not in ("inc", "ltée", "ltee", "senc", "ltd", "limitée", "limitee"):
            continue  # "a limited number", "the corporation": the French forms are written small ("Autoénergie Canada inc."), the English ones are not
        j = m.start()
        if j == 0 or text[j - 1] not in "  ":
            continue
        head = text[max(0, j - 140):j].rstrip("  ")
        if head.endswith(","):
            head = head[:-1]
        toks = head.split(" ")
        words, cut = [], False
        for t in reversed(toks):
            t0 = t.rstrip(",")
            if not t0 or len(words) >= 8:
                cut = len(words) >= 8
                break
            paren = t0.startswith("(") and len(t0) > 1  # "Solaris (1457570 Alberta Ltd.)": the bracket opens the name
            core = t0[1:] if paren else t0
            if core.lower().strip(".:") in CHROME3 or not (_W3.match(core) or core.lower() in _J3 or (loose and re.fullmatch(r"[a-zà-ÿ][a-zà-ÿ'’\-]{1,20}", core))):
                break
            if core[-1] in ".:;!?)|" and not ABBR3.fullmatch(core):
                break  # the end of the sentence before the name ("… in our store. Acme Inc.", "Yes. Felicita Holdings Ltd."); "J.", "M.A.C.", "St." are parts of names
            words.insert(0, core)
            if paren:
                break
        while words and ((words[0].lower() in _J3 and not _ART3.match(words[0])) or not (_W3.match(words[0]) or _ART3.match(words[0]))):
            words.pop(0)  # a connector or a small word left at the front; an article written with a capital opens a name ("The Brick Ltd.")
        if not words:
            continue
        w0 = max(0, j - 150)
        mm = re.search(r"[ ,\u00a0]+".join(map(re.escape, words)) + r",?[ \u00a0]+$", text[w0:j])
        if not mm:
            continue
        form = text[m.start():m.end()]
        if form.endswith(".") and re.fullmatch(r"(?i)limited|limit[ée]e|corporation|incorporated|incorpor[ée]e|llp|llc|ulc|plc|gmbh|senc|sencrl", form[:-1]):
            form = form[:-1]
        yield words, form, w0 + mm.start(), m.start() + len(form), cut


def _variants3(words):
    out = set()
    for amp in ("", "and", "et", "n"):
        out.add(letters3(" ".join(amp if w in ("&", "+") else w for w in words)))
    return out


OPENING3 = set("""les le la the services service entreprises entreprise groupe group gestion société societe compagnie clinique centre constructions construction distributions
distribution transports transport industries équipements equipements aliments produits placements investissements immeubles productions éditions editions consultants solutions technologies
laboratoires pharmacie restaurant boutique atelier garage ferme excavation excavations plomberie toitures toiture rénovations renovations rénovation renovation électrique electrique
entrepreneur entrepreneurs assurances assurance courtage transport location locations ventes importations exportations meubles pavage paysagement paysagiste""".split())


def _opening3(text, nm):
    """the name with the opening word(s) the site prints before it EVERY time ("Services Mobile Mediq inc.", "Les Entreprises Tremblay inc.",
    "Alliance to End Plastic Waste, Inc." on endplasticwaste.org), or the name as it is. Only words written with a capital, right before the name,
    with no comma between. They are part of the name when they stand inside a sentence (a word written small comes before them: "… the policies
    of ALLIANCE TO END PLASTIC WASTE, INC."), or — for the usual opening words of company names — whenever every printing has them. A word that
    stands before the name only now and then, or the same word after the same word every time ("Shop Now" above a footer), is the page's furniture."""
    small = re.compile(r"[a-zà-ÿ'’]{1,14}$")
    chains = []
    for m in re.finditer(r",?[ \u00a0]+".join(map(re.escape, nm.split(" "))), text):  # "… PLASTIC WASTE, INC.": the comma before the form is not in the name as kept
        head = text[max(0, m.start() - 90):m.start()]
        ws = head[:-1].split(" ") if head.endswith(" ") else []
        ch = []
        while ws and len(ch) < 4:
            w = ws[-1]
            if not w or w.lower().strip(".:") in CHROME3 or not _W3.match(w) or w in ("&", "+") or not w[0].isalpha() or (w[-1] in ".,:;!?)|" and not ABBR3.fullmatch(w)):
                break  # a year, a number: "© 2026 Sécurité Métalgard Inc."
            ch.insert(0, w)
            ws.pop()
        chains.append((ch, ws[-1] if ws else ""))
    if not chains:
        return nm
    tail = list(chains[0][0])  # the words every printing shares, counted from the name backwards ("Les Entreprises" and "les Entreprises": "Entreprises")
    for ch, _ in chains[1:]:
        k = 0
        while k < len(tail) and k < len(ch) and tail[-1 - k] == ch[-1 - k]:
            k += 1
        tail = tail[len(tail) - k:]
    if not tail:
        return nm
    if {letters3(w) for w in tail} & {letters3(w) for w in nm.split(" ")}:
        return nm  # the site's short name printed right before its legal name ("Selkirk Security Selkirk Security Services Ltd."): not an opening
    usual = all(w.lower() in OPENING3 for w in tail)
    in_sentence = all(len(ch) == len(tail) and small.match(b or "") for ch, b in chains)  # every printing: a small word, then exactly these words, then the name
    if len(chains) == 1:
        ok = in_sentence
    else:
        ok = usual or in_sentence or len({b for ch, b in chains if len(ch) == len(tail)}) >= 2 and all(len(ch) == len(tail) for ch, b in chains)
    return (" ".join(tail) + " " + nm) if ok else nm


def spelled_name(text, host):
    """(name with its legal form, basis, times printed, position) for the name whose words spell the site's own domain name — the whole of it
    ("Credit Lift Inc." on creditlift.ca, "Strato Inc." on stratoinc.com), its beginning ("AZON Bookkeeping Services Inc." on azonbookkeeping.ca; the
    domain must have six letters), or the whole of it with the first words by their initials ("Case Grypma Mechanical Ltd." on cgmechanical.ca)."""
    lab = host_label(host)
    if len(lab) < 4:
        return None
    found = {}
    for words, suf, s, e, cut in _name_runs(text):
        sl = letters3(suf)
        best = None
        for k in range(1, len(words) + 1):
            run = words[-k:]
            if run[0].lower() in _J3 and not _ART3.match(run[0]):
                continue
            vs = _variants3(run)
            if lab in vs or any(v + sl == lab for v in vs):
                best = (run, "its words spell the site's own domain name"); break
            if len(lab) >= 6 and any(v.startswith(lab) for v in vs):
                best = (run, "its words begin with the site's own domain name"); break
            sig = [w for w in run if w.lower() not in _J3]
            if len(sig) >= 3:
                for j in range(2, len(sig)):
                    if "".join(letters3(w)[:1] for w in sig[:j]) + letters3(" ".join(sig[j:])) == lab:
                        best = (run, "its words spell the site's own domain name, the first ones by their initials"); break
                if best:
                    break
                ini = "".join(letters3(w)[:1] for w in sig)
                if (len(ini) >= 4 and ini == lab) or (len(ini) >= 3 and ini + sl == lab):
                    best = (run, "its initials are the site's own domain name"); break  # "Global Institute of Forensic Research Inc." on gifrinc.com
        if not best:
            continue
        nm = " ".join(best[0]) + " " + suf
        if THIRD3.search(nm) or len(nm) > 90:
            continue
        key = letters3(nm)
        if key not in found:
            found[key] = [nm, best[1], 0, e - len(nm)]
        found[key][2] += 1
    if not found:
        # names with words written small inside them ("Centre dentaire Ahuntsic inc."): only the name that spells the whole domain name
        for words, suf, s, e, cut in _name_runs(text, loose=True):
            for k in range(2, len(words) + 1):
                run = words[-k:]
                if not _W3.match(run[0]) or run[0].lower() in _J3:
                    continue
                if lab in _variants3(run):
                    nm = " ".join(run) + " " + suf
                    if not THIRD3.search(nm) and len(nm) <= 90:
                        key = letters3(nm)
                        found.setdefault(key, [nm, "its words spell the site's own domain name", 0, text.rfind(nm, 0, e + 1)])
                        found[key][2] += 1
                    break
        if not found:
            return None
    best = sorted(found.values(), key=lambda v: (0 if v[1].startswith("its words spell") else 1 if v[1].startswith("its words begin") else 2, -v[2], v[3]))[0]
    full = _opening3(text, best[0])
    if full != best[0]:
        best = [full, best[1] + ", after the opening “%s” it is always printed with" % full[:len(full) - len(best[0])].strip(), best[2], max(0, text.find(full))]
    return best


def _trim_form3(cand):
    """a full stop after a whole word or an acronym ends the sentence, not the name ("… operated by Adaria Vending Services Limited.")"""
    return cand[:-1] if re.search(r"(?i)\b(?:limited|limit[ée]e|corporation|incorporated|incorpor[ée]e|llp|llc|ulc|plc|gmbh|senc|sencrl)\.$", cand) else cand


def _fits3(trade, lab):
    t = letters3(trade)
    # "Genesis" is not the name of genesiskw.ca (a dealer's site carrying the maker's privacy notice: "… a division of Hyundai Auto Canada Corp. (“Genesis”)")
    return bool(t) and bool(lab) and (t == lab or (len(lab) >= 5 and t.startswith(lab)) or (len(t) >= 5 and lab.startswith(t) and lab[len(t):] in ENDINGS3))


def _lead_words3(s, n=6):
    """the capitalised words a text starts with (a trade name after "operating as")"""
    out = []
    for t in s.split(" ")[:n + 2]:
        if out and t[:1] in "(\"“«‘[":
            break  # "… sous la dénomination sociale StreamScan (“StreamScan”)": the bracket after the name opens something else
        t0 = t.strip("\"“”«»‘’'(),")
        if not t0 or not (_W3.match(t0) or (out and t0.lower() in _J3)) or t0.lower() in CHROME3:
            break
        out.append(t0)
        if t and t[-1] in ".,;:)\"”»" or len(out) >= n:
            break
    while out and out[-1].lower() in _J3:
        out.pop()
    return " ".join(out).rstrip(".")


def party_name(text, host):
    """(legal person, the site's name it stands behind, how the page puts it, position) — "Majid Enterprises Inc., operating as Lawn Lovers",
    "1234567 Ontario Inc. ("Acme", "we", "us")", "Solaris (1457570 Alberta Ltd.)", "Legal Entity : Sleepera Mattress Wholesale Ltd.". The name the
    legal person stands behind must be the site's own (it spells its domain name); a labelled legal entity needs no such name."""
    lab = host_label(host)
    if not lab:
        return None
    for words, suf, s, e, cut in _name_runs(text):
        if cut:
            continue
        # the day and year of a date before the name ("January 13, 2026 Majid Enterprises Inc."); a numbered company keeps its number ("1457570 Alberta Ltd.")
        while len(words) > 1 and re.fullmatch(r"\d{1,4}(?:st|nd|rd|th|e|er)?", words[0]) and not PROV3.match(words[1]):
            s = text.find(words[1], text.find(words[0], s) + len(words[0]))
            words = words[1:]
        while len(words) > 2 and words[0].lower() in ("web", "site", "website") and words[1].lower() in _J3:
            s = text.find(words[2], text.find(words[1], s) + len(words[1]))  # "… le site Web de Auto-Chem inc."
            words = words[2:]
        name = " ".join(words) + " " + suf
        if THIRD3.search(name) or len(name) > 90 or (len(words) == 1 and NUMBERED3.match(words[0])):
            continue
        tail = text[e:e + 160]
        m = DBA3.match(tail)
        if m and m.end() > 2:
            trade = _lead_words3(tail[m.end():])
            if _fits3(trade, lab):
                return name, trade, "doing business as", s
        m = ALIAS3.match(tail)
        if m and _fits3(m.group(1), lab):
            return name, m.group(1).strip(), "defined on the page as", s
        if s >= 2 and text[s - 1] == "(" and tail[:1] == ")":
            before = text[max(0, s - 90):s - 1].rstrip().split(" ")
            tw = []
            for t in reversed(before):
                if not t or not _W3.match(t.rstrip(",")) or t.lower().strip(".:,") in CHROME3 or len(tw) >= 5:
                    break
                tw.insert(0, t.rstrip(","))
            if tw and SUF3.fullmatch(tw[-1]):
                continue
            for k in range(1, len(tw) + 1):
                if _fits3(" ".join(tw[-k:]), lab):
                    return name, " ".join(tw[-k:]), "in brackets after the site's name", s
    for m in LABELLED3.finditer(text):
        seg = text[m.end():m.end() + 120]
        mm = SUF3.search(seg)
        if not mm:
            continue
        cand = seg[:mm.end()].strip()
        ws = cand.split(" ")
        if 2 <= len(ws) <= 9 and all(_W3.match(w.rstrip(",")) or w.lower() in _J3 or SUF3.fullmatch(w) for w in ws) and not THIRD3.search(cand):
            return _trim_form3(cand), "", "labelled as the legal entity", m.end()
    return None


def operator_name(text):
    """(legal person, position) a page names as the one that operates / owns / publishes the site, whatever its name ("exploité par Société Groupe
    Panican inc."): a name with a legal form right after the words; the ranker checks the sentence again in the quote before it prints the name"""
    for m in OPER3.finditer(text):
        seg = text[m.end():m.end() + 120]
        mm = SUF3.search(seg)
        if not mm:
            continue
        cand = seg[:mm.end()].strip()
        ws = cand.split(" ")
        if 2 <= len(ws) <= 9 and all(_W3.match(w.rstrip(",")) or w.lower() in _J3 or SUF3.fullmatch(w) for w in ws) and not THIRD3.search(cand) and not any(w.lower().strip(".,") in CHROME3 for w in ws):
            return _trim_form3(cand), m.end()
    return None


def quote_pos(text, pos, name, n=300):
    return flat(text[max(0, pos - 110):pos + len(name) + 110])[:n]


def logo_from(raw, url):
    """logo: header <img> whose src / alt / class says logo, else og:image, else the site icon (apple-touch-icon / icon)"""
    for hm in HEADER_IMG.finditer(raw[:200_000]):
        for im in LOGO.finditer(hm.group(1)):
            src = re.sub(r"\s+", "", im.group(1))
            if re.search(r"logo|brand|wordmark|armoiries|embl", src + " " + im.group(0), re.I) and not re.search(r"partner|sponsor|client|award|badge|payment|visa|mastercard|facebook|twitter|linkedin|instagram|youtube|flag", src, re.I):
                return urllib.parse.urljoin(url, html.unescape(src)), "logo image in the site header"
    for im in LOGO.finditer(raw):
        src = re.sub(r"\s+", "", im.group(1))
        if re.search(r"logo", src + " " + im.group(0), re.I) and not re.search(r"partner|sponsor|client|award|badge|icon-|payment|visa|mastercard|facebook|twitter|linkedin|instagram|youtube", src, re.I):
            return urllib.parse.urljoin(url, html.unescape(src)), "logo image on the site"
    for lm in ICON.finditer(raw):  # the site's own icon is the logo mark; og:image is often a photo (checked last, labelled)
        h = HREF.search(lm.group(0))
        if h and not h.group(1).lower().endswith(".ico") and "apple-touch" in lm.group(0).lower():
            return urllib.parse.urljoin(url, html.unescape(h.group(1))), "site icon (apple-touch-icon)"
    m = OG.search(raw) or OG2.search(raw)
    if m:
        og = html.unescape(m.group(1))
        photo = bool(re.search(r"hero|banner|slide|photo|snow|aerial|skyline|campus|building|homepage|home-page|\.jpe?g(\?|$)", og, re.I))
        return urllib.parse.urljoin(url, og), "og:image of the home page" + (" (looks like a photo, not a logo: check before use)" if photo else "")
    for lm in ICON.finditer(raw):
        h = HREF.search(lm.group(0))
        if h and not h.group(1).lower().endswith(".ico"):
            return urllib.parse.urljoin(url, html.unescape(h.group(1))), "site icon (icon link)"
    return "", ""


def portals_from(pages):
    found = {}
    for url, raw in pages:
        for m in HREF.finditer(raw):
            h = html.unescape(m.group(1)).strip()
            if not h.startswith("http"):
                continue
            hl = h.lower()
            for pat, nm, kind in PORTALS:
                if pat in hl and nm not in found:
                    found[nm] = {"name": nm, "kind": kind, "url": h[:200], "on_page": url}
                    break
    return list(found.values())[:8]


def mentions_from(pages):
    out = {}
    for url, raw in pages:
        text = re.sub(r"\s+", " ", visible_keep_lines(raw))
        for key, rx in MENTIONS.items():
            if key in out:
                continue
            for m in rx.finditer(text):
                ctx = text[max(0, m.start() - 250):m.end() + 250]
                if MENTION_CONTEXT.search(ctx) and not MENTION_NOISE.search(ctx):
                    out[key] = {"text": flat(m.group(1))[:160], "url": url, "quote": quote_at(text, m.group(1)[:60])}
                    break
    return out


def read_site(site, kind, name="", start_url=""):
    res = {"status": "no_page"}
    if not C.allowed(site):
        res["status"] = "robots"; return res
    st, ct, data, final = C.fetch(start_url or site, 3_000_000)
    if st in (401, 403, 429):
        res["status"] = "blocked"; return res
    if st != 200 or not data or "html" not in (ct or "").lower():
        res["status"] = "http_%s" % st; return res
    raw0 = strip_long(data.decode("utf-8", "replace"))
    if C.BLOCK_RX.search(raw0[:5000]) or (len(raw0) < 2500 and re.search(r"incapsula|imperva|datadome|perimeterx", raw0, re.I)):
        res["status"] = "blocked"; return res
    host = (urllib.parse.urlparse(final).hostname or "").lower().removeprefix("www.")
    pages = [(final, raw0)]
    seen = []
    for u, label in C.links(raw0, final):
        p = urllib.parse.urlparse(u)
        u0 = u.split("#")[0]
        if (p.hostname or "").lower().removeprefix("www.") != host or C.SKIP_EXT.search(p.path or "") or u0 in seen or u0.rstrip("/") == final.rstrip("/"):
            continue
        if PAGE_LINK.search(p.path or "") or PAGE_LINK.search(label or ""):
            seen.append(u0)  # v3: every such link is seen before five are chosen (a menu's five "about" pages came before the footer's Privacy / Terms links)
            if len(seen) >= 60:
                break
    picked = sorted(seen, key=lambda u: (not LEGAL_PAGE.search(u), len(u)))[:5]
    if SHOPIFY3.search(raw0):
        # v3: a store on Shopify keeps its policies at fixed addresses, linked from the home page or not; the legal notice and the contact
        # information policy print the legal entity, its address and its business number (the store's robots.txt opens its policy pages)
        base = "%s://%s" % (urllib.parse.urlparse(final).scheme, urllib.parse.urlparse(final).netloc)
        have = {urllib.parse.urlparse(u).path.rstrip("/") for u in picked}
        picked += [base + pth for pth in STORE_POLICIES if pth not in have][:max(0, 8 - len(picked))]
    for u in picked:
        if not C.allowed(u):
            continue
        st, ct, data, fin = C.fetch(u, 3_000_000)
        if st == 200 and data and "html" in (ct or "").lower():
            pages.append((fin, strip_long(data.decode("utf-8", "replace"))))
    res["status"] = "ok"
    res["pages"] = len(pages)
    res["v"] = V
    res["pages_read"] = "; ".join(u for u, _ in pages)[:600]
    # v3: the name printed with its legal form that the site's own address spells; the legal person a page puts behind the site's name; the
    # operator a page names. Every one with its page and its words; the ranker decides which one a row prints.
    m = TITLE3.search(raw0)
    title0 = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else ""
    if title0:
        res["title"] = title0[:150]
    m = OGSN3.search(raw0)
    if m:
        res["og_site_name"] = html.unescape(m.group(1) or m.group(2) or "").strip()[:100]
    sp, party, oper = {}, None, None
    for url, raw in pages:
        m = TITLE3.search(raw)
        ft = (html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() + " \n " if m else "") + re.sub(r"\s+", " ", visible_keep_lines(raw))
        ft = re.sub(r"\s*[®™℠]", "", ft)  # "Pangaea® Natural Stone Inc."
        phost = (urllib.parse.urlparse(url).hostname or "").lower().removeprefix("www.")
        if C.registrable(phost) != C.registrable(host):
            continue  # a page that left the site says nothing about the site
        r = spelled_name(ft, host)
        if r:
            k = letters3(r[0])
            if k not in sp:
                sp[k] = [r[0], r[1], 0, url, quote_pos(ft, r[3], r[0])]
            sp[k][2] += r[2]
        if not party:
            r = party_name(ft, host)
            if r:
                party = (r, url, quote_pos(ft, r[3], r[0]))
        if not oper:
            r = operator_name(ft)
            if r:
                oper = (r, url, quote_pos(ft, r[1], r[0]))
    if sp:
        b = sorted(sp.values(), key=lambda v: (not v[1].startswith("its words spell"), -v[2]))[0]
        res.update({"legal_name_spelled": b[0], "legal_name_spelled_basis": b[1], "legal_name_spelled_times": b[2], "legal_name_spelled_url": b[3], "legal_name_spelled_quote": b[4]})
    if party:
        res.update({"legal_name_party": party[0][0], "legal_name_party_trade": party[0][1], "legal_name_party_how": party[0][2], "legal_name_party_url": party[1], "legal_name_party_quote": party[2]})
    if oper:
        res.update({"legal_name_operator": oper[0][0], "legal_name_operator_url": oper[1], "legal_name_operator_quote": oper[2]})
    # v2: structured and stated facts first (JSON-LD Organization, Terms / Privacy / Legal page statements), then the copyright line
    for url, raw in pages:
        jl_ = jsonld_org(raw, host, name)
        if jl_:
            jl_["jsonld_page"] = url
            res.update(jl_)
            break
    for url, raw in sorted(pages, key=lambda p: (not LEGAL_PAGE.search(p[0]), p[0] != pages[0][0])):
        ln = legal_name_text(re.sub(r"\s+", " ", visible_keep_lines(raw)), host, name)
        if ln:
            res.update({"legal_name_stated": ln, "legal_name_stated_url": url, "legal_name_stated_quote": quote_at(re.sub(r"\s+", " ", visible_keep_lines(raw)), ln)})
            break
    pf = portals_from(pages)
    if pf:
        res["portals"] = pf
    mm = mentions_from(pages)
    if mm:
        res["mentions"] = mm
    li = next((m.group(0) for _, raw in pages for m in LINKEDIN.finditer(raw)), "")
    if li:
        res["linkedin_url"] = li[:160]
    tels = [(html.unescape(urllib.parse.unquote(m.group(1))).strip(), u) for u, raw in pages for m in TEL_HREF.finditer(raw)]
    tels = [(t, u) for t, u in tels if len(re.sub(r"\D", "", t)) >= 10]
    if tels:
        res["tel_links"] = "; ".join(dict.fromkeys(t for t, _ in tels))[:120]
        res["tel_links_url"] = tels[0][1]
    m = LANG.search(raw0)
    lang = (m.group(1).lower() if m else "")
    t0 = visible_keep_lines(raw0)
    fr, en = len(FRW.findall(t0)), len(ENW.findall(t0))
    res["language"] = "fr-en" if (fr and en and 0.5 <= fr / max(en, 1) <= 2) else ("fr" if (lang == "fr" or fr > en) else "en" if (lang == "en" or en > fr) else lang)
    for url, raw in pages:
        text = visible_keep_lines(raw)
        ftext = re.sub(r"\s+", " ", text)
        if not res.get("legal_name"):
            ln = legal_name(ftext, host)
            if ln:
                res.update({"legal_name": ln, "legal_name_url": url, "legal_name_quote": quote_at(ftext, ln)})
        if not res.get("bn"):
            for m in BN.finditer(ftext):
                digits = re.sub(r"\D", "", m.group(1))
                if len(digits) == 9 and digits != "000000000" and not re.fullmatch(r"(\d)\1{8}", digits):
                    prog = (m.group(2) or "").replace(" ", "").upper()
                    label = m.group(0)[:40]
                    res.update({"bn": digits, "bn_program": prog, "bn_label": flat(label), "bn_url": url, "bn_quote": quote_at(ftext, m.group(0))})
                    break
        if not res.get("neq"):
            m = NEQ.search(ftext)
            if m:
                res.update({"neq": m.group(1), "neq_url": url, "neq_quote": quote_at(ftext, m.group(0))})
        if not res.get("qst"):
            m = QST.search(ftext)
            if m:
                res.update({"qst": (m.group(1) + " " + m.group(2).replace(" ", "")).strip(), "qst_url": url, "qst_quote": quote_at(ftext, m.group(0))})
        if not res.get("logo_url"):
            lu, lb = logo_from(raw, url)
            if lu:
                res.update({"logo_url": lu, "logo_basis": lb})
    if not res.get("logo_url") and res.get("jsonld_logo"):
        res.update({"logo_url": res["jsonld_logo"], "logo_basis": "schema.org JSON-LD logo"})
    return res


RETRY_STATUS = ("http_308", "http_307", "http_301", "http_302", "http_0", "error")


def task_key(h, w):
    """the site's host (www. dropped), or domain + path on shared hosts (canada.ca/en/environment-climate-change → one record per organisation).
    Until 2026-11-10 the key was the registrable domain, so one record served every host of a domain: the record read on tdi.texas.gov was
    handed to five other Texas agencies, one municipality's to the sixteen others on ao.ca, one church's to another on churchcenter.com. Each
    host is read for itself now; a record made before that day stays the record of the host it was read on (done_for)."""
    dom = C.registrable(h)
    if SHARED_HOSTS.search(h) or SHARED_HOSTS.search(dom):
        p = urllib.parse.urlparse(w if "//" in w else "https://" + w).path.rstrip("/")
        seg = "/".join(p.split("/")[:3]) if p else ""
        return (dom + seg) if seg else (h if h != dom else dom), h + seg
    return h, ""


def _host_of_site(w):
    w = w or ""
    return (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")


def done_for(done, key, h):
    """the record of this site, if this very host was read: under its own key, or — read before 2026-11-10 — under its registrable domain.
    A record kept under the host's name but read on another host of the domain (the domain's record, read on bookstore.upei.ca, is not
    upei.ca's) does not count: the host is read for itself and its record takes the key."""
    old = done.get(key)
    if key == h:
        if old is not None and _host_of_site(old.get("website")) not in ("", h):
            old = None
        if old is None:
            o2 = done.get(C.registrable(h))
            if o2 is not None and _host_of_site(o2.get("website")) == h:
                return o2
    return old


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--tasks", default="")
    a.add_argument("--workers", type=int, default=48)
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--refresh", action="store_true", help="re-read domains read by an older version of this reader (v < V) or that failed on a redirect / network error")
    a.add_argument("--older-only", action="store_true", help="with --refresh: only the sites that have a record of an older version (the sites never read are another run's)")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--test", nargs="*", default=None, help="read these sites once and print the facts (no files written)")
    a.add_argument("--shard", default="", help="K/N: only domains that hash to shard K of N (parallel runners never share a host)")
    a.add_argument("--seed-resume", default="", help="a jsonl(.gz) of organisations already read (the repo copy): skipped as if in the resume file")
    a = a.parse_args()
    if a.test is not None:
        for u in a.test:
            u = u if u.startswith("http") else "https://" + u
            res = read_site("https://%s/" % (urllib.parse.urlparse(u).hostname or ""), "buyer", name="", start_url=u)
            print(json.dumps(res, ensure_ascii=False, indent=1)[:4000], flush=True)
        return
    os.makedirs(STATE, exist_ok=True)
    done = {}
    if os.path.exists(RESUME):
        for l in open(RESUME, encoding="utf-8"):
            try:
                d = json.loads(l); done[d["domain"]] = d
            except Exception:
                pass
    if a.seed_resume and os.path.exists(a.seed_resume):
        import hashlib  # noqa: F811
        with (gzip.open if a.seed_resume.endswith(".gz") else open)(a.seed_resume, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    d = json.loads(l)
                    if d.get("domain") and d["domain"] not in done:
                        done[d["domain"]] = d
                except Exception:
                    pass
    import hashlib
    shard_k, shard_n = (int(a.shard.split("/")[0]), int(a.shard.split("/")[1])) if a.shard else (0, 1)
    tasks, seen, again = [], set(), set()
    for r in csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")):
        w = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
        if not h or "." not in h:
            continue
        dom, start_path = task_key(h, w)
        if dom in seen:
            continue
        old = done_for(done, dom, h)
        if old is not None and not (a.refresh and ((int(old.get("v") or 1) < V and int(old.get("v_tried") or 0) < V) or (old.get("status") in RETRY_STATUS and not a.older_only))):
            continue
        if old is None and a.older_only:
            continue
        if shard_n > 1 and int(hashlib.md5((C.registrable(h) or h).encode()).hexdigest(), 16) % shard_n != shard_k:  # every host of a domain on one runner
            continue
        seen.add(dom); tasks.append((dom, r.get("key", ""), r.get("name", ""), "https://%s/" % h, r.get("kind", ""), ("https://%s/" % start_path) if start_path else ""))
        if old is not None:
            again.add(dom)
    tasks.sort(key=lambda t: t[0] in again)  # the sites never read come first; the ones read by an older reader fill what is left of the time box
    if a.limit:
        tasks = tasks[:a.limit]
    print("tasks: %d domains to read, %d of them read before by an older reader (%d in resume file; refresh=%s)" % (len(tasks), len(again), len(done), a.refresh), flush=True)
    out_gz = os.path.join(a.repo, "data/incoming/claude/claude_org_extras.jsonl.gz")
    stats, last = {}, [time.time()]

    def dump():
        with lock:
            rows = [d for d in done.values() if d.get("status") == "ok" and any(d.get(k) for k in ("legal_name", "legal_name_stated", "legal_name_spelled", "legal_name_party", "legal_name_operator", "title", "jsonld_legal_name", "jsonld_name", "bn", "neq", "qst", "logo_url", "language", "portals", "mentions", "tel_links", "jsonld_address", "jsonld_phone", "linkedin_url"))]
        for attempt in range(3):
            try:
                tmp = out_gz + ".%d.tmp" % os.getpid()
                with gzip.open(tmp, "wt", encoding="utf-8") as f:
                    for d in sorted(rows, key=lambda d: d["domain"]):
                        f.write(json.dumps(d, ensure_ascii=False) + "\n")
                os.replace(tmp, out_gz); break
            except Exception as e:
                print(time.strftime("%H:%M"), "dump failed (%s), retrying" % e, flush=True); time.sleep(20)
        print(time.strftime("%H:%M"), "wrote", out_gz, len(rows), "organisations", dict(stats), flush=True)

    def one(t):
        dom, key, name, site, kind, start = t
        try:
            res = read_site(site, kind, name=name, start_url=start)
        except Exception as e:
            res = {"status": "error", "error": str(e)[:100]}
        res.update({"domain": dom, "key": key, "name": name, "website": start or site, "kind": kind, "date": TODAY})
        with lock:
            old = done.get(dom)
            if old and _host_of_site(old.get("website")) not in ("", _host_of_site(res.get("website"))):
                old = None  # the record under this key was read on another host of the domain: this host's own record replaces it, facts are not mixed
            if old and old.get("status") == "ok" and res.get("status") != "ok":
                res = dict(old, last_recheck=TODAY, last_recheck_status=res.get("status"), v_tried=V)  # keep yesterday's facts when today's read fails; this version of the reader has had its try
            elif old and old.get("status") == "ok":
                merged = dict(old); merged.update({k: v for k, v in res.items() if v not in ("", None, [], {})}); res = merged
            done[dom] = res
            stats[res["status"]] = stats.get(res["status"], 0) + 1
            with open(RESUME, "a", encoding="utf-8") as f:
                f.write(json.dumps(res, ensure_ascii=False) + "\n")
            due = time.time() - last[0] > 300
            if due:
                last[0] = time.time()
        if due:
            try:
                dump()
            except Exception as e:
                print("dump error", e, flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    dump()
    print("finished", dict(stats), flush=True)


if __name__ == "__main__":
    main()

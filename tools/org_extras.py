#!/usr/bin/env python3
"""Extra facts an organisation prints on its own site (buyers and vendors), evidence or nothing:
  - legal name as printed in the copyright / footer line ("© 2026 Acme Holdings Inc.", "Tous droits réservés Ville de X");
  - Business Number / GST-HST / charity registration number as printed ("GST/HST # 123456789 RT0001", "BN 12345 6789 RR0001",
    "Numéro d'entreprise du Québec 1234567890" → NEQ); the GST/HST account is derived from a BN9 and always labelled so;
  - logo image URL (og:image or an <img> whose src / alt says logo);
  - language of the site (fr / en / fr-en from the html lang attribute and stopwords);
  - whether the site answers (status).
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
V = 2
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
    seen = set()
    for u, label in C.links(raw0, final):
        p = urllib.parse.urlparse(u)
        if (p.hostname or "").lower().removeprefix("www.") != host or C.SKIP_EXT.search(p.path or "") or u.split("#")[0] in seen:
            continue
        if PAGE_LINK.search(p.path or "") or PAGE_LINK.search(label or ""):
            seen.add(u.split("#")[0])
            if len(seen) >= 5:
                break
    for u in sorted(seen, key=lambda u: (not LEGAL_PAGE.search(u), len(u)))[:5]:
        if not C.allowed(u):
            continue
        st, ct, data, fin = C.fetch(u, 3_000_000)
        if st == 200 and data and "html" in (ct or "").lower():
            pages.append((fin, strip_long(data.decode("utf-8", "replace"))))
    res["status"] = "ok"
    res["pages"] = len(pages)
    res["v"] = V
    res["pages_read"] = "; ".join(u for u, _ in pages)[:600]
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
    """registrable domain, or domain + path for shared hosts (canada.ca/en/environment-climate-change → one record per organisation)"""
    dom = C.registrable(h)
    if SHARED_HOSTS.search(h) or SHARED_HOSTS.search(dom):
        p = urllib.parse.urlparse(w if "//" in w else "https://" + w).path.rstrip("/")
        seg = "/".join(p.split("/")[:3]) if p else ""
        return (dom + seg) if seg else (h if h != dom else dom), h + seg
    return dom, ""


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--tasks", default="")
    a.add_argument("--workers", type=int, default=48)
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--refresh", action="store_true", help="re-read domains read before v2 or that failed on a redirect / network error")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--test", nargs="*", default=None, help="read these sites once and print the facts (no files written)")
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
    tasks, seen = [], set()
    for r in csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")):
        w = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower().removeprefix("www.")
        if not h or "." not in h:
            continue
        dom, start_path = task_key(h, w)
        if dom in seen:
            continue
        old = done.get(dom)
        if old is not None and not (a.refresh and (int(old.get("v") or 1) < V or old.get("status") in RETRY_STATUS)):
            continue
        seen.add(dom); tasks.append((dom, r.get("key", ""), r.get("name", ""), "https://%s/" % h, r.get("kind", ""), ("https://%s/" % start_path) if start_path else ""))
    if a.limit:
        tasks = tasks[:a.limit]
    print("tasks: %d domains to read (%d in resume file; refresh=%s)" % (len(tasks), len(done), a.refresh), flush=True)
    out_gz = os.path.join(a.repo, "data/incoming/claude/claude_org_extras.jsonl.gz")
    stats, last = {}, [time.time()]

    def dump():
        with lock:
            rows = [d for d in done.values() if d.get("status") == "ok" and any(d.get(k) for k in ("legal_name", "legal_name_stated", "jsonld_legal_name", "jsonld_name", "bn", "neq", "qst", "logo_url", "language", "portals", "mentions", "tel_links", "jsonld_address", "jsonld_phone", "linkedin_url"))]
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
            if old and old.get("status") == "ok" and res.get("status") != "ok":
                res = dict(old, last_recheck=TODAY, last_recheck_status=res.get("status"))  # keep yesterday's facts when today's read fails
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

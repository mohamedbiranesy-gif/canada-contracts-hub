#!/usr/bin/env python3
"""Invoicing terms, PO requirement, portal, AP phone / address / contact name and the buyer's own GST number, read from the
evidence pages of the delivered mailboxes (owner 2026-11-06, D4 / D5 / D6 / D11: lift payment_terms, invoice_portal_url,
ap_contact_name coverage without search credits).

The ranking kept a 300-character quote per mailbox; the page usually says more (terms, "PO number required", portal, phone,
mailing address, the AP clerk's printed name, the buyer's GST/HST number). This re-reads each evidence page once — politely
(tools/ap_crawler.fetch: 1 request/second/host, identified user agent, robots.txt honoured; 401/403/429/CAPTCHA = blocked,
never worked around) — and writes every fact with the URL actually opened, the retrieval date and a quote of at most 300
characters that contains it. No search, no AI, no inference: a regex either finds the printed value or the cell stays empty.
rank.py merges the file by mailbox (contrib/claude/rank_buyers/rank.py, "ap_terms").
  python3 tools/ap_terms.py [--repo ~/cch-crawler] [--ranked path.csv.gz] [--tiers A,B,T,M,L,C,D,E,F] [--workers 24] [--limit N]
Output: <repo>/data/incoming/claude/claude_ap_terms.csv (resumable: pages already read within --recheck-days are skipped).
"""
import argparse, hashlib, csv, datetime, gzip, html, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
try:
    from buyer_pages import FIRST_NAMES as _FIRST
except Exception:
    _FIRST = set()
TODAY = datetime.date.today().isoformat()
lock = threading.Lock()
COLS = ["email", "evidence_url", "final_url", "retrieved_date", "status", "payment_terms", "payment_terms_quote", "po_required", "po_quote",
        "portal_name", "portal_url", "portal_quote", "ap_phone", "ap_phone_quote", "invoice_mailing_address", "address_quote",
        "ap_contact_name", "contact_quote", "invoice_format", "format_quote", "buyer_bn", "bn_quote", "mailbox_still_on_page", "mailbox_context", "payment_method", "payment_method_quote", "ap_cycle", "ap_cycle_quote", "tax_exempt", "tax_exempt_quote", "esignature", "esignature_quote", "ap_system", "ap_system_quote", "setup_url", "setup_quote"]
TERMS = re.compile(r"\b(?:net\s?(?:30|45|60|90|15|10)\b(?:\s?(?:days|jours))?|(?:payment|paid|payable|paiement|pay[ée]e?s?)\b[^.;]{0,60}?\b(?:within|dans les|dans un d[ée]lai de|sous|in)\s(?:\d{2}|thirty|forty-five|sixty|trente|quarante-cinq|soixante)\s?(?:calendar |business |working |ouvrables? )?(?:days?|jours)\b|"
                   r"(?:payment )?terms?(?: of payment| are| is|:)?\s?(?:are |is |:)?\s?net\s?\d{2}|conditions? de paiement\s?:?\s?[^.;]{0,40}?\d{2}\s?jours|"
                   r"\b\d{2}\s?(?:calendar |business |working )?days? (?:from|after|of|following) (?:the )?(?:receipt|invoice date|date of invoice|approval)|"
                   r"\b\d{2}\s?jours (?:suivant|apr[èe]s|de) (?:la )?(?:r[ée]ception|date de (?:la )?facture)|2\s?%\s?(?:10|15)\s?,?\s?net\s?\d{2})", re.I)
PO_REQ = re.compile(r"(?:(?:valid |authorized |official )?purchase[- ]order(?: number| no\.?| #)?|\bP\.?O\.?(?: number| no\.?| #)\b|bon de commande|num[ée]ro de (?:bon de )?commande|\bBC\b num[ée]ro)[^.;]{0,100}?\b(?:required|must|needs?|shall|mandatory|doit|doivent|obligatoire|requis|exig|include|indiqu|mention|quote|quoted|reference|référenc|appear|appara)|"
                    r"\b(?:required|must|needs?|shall|mandatory|doit|doivent|obligatoire|requis|exig|include|indiqu|mention|quote|reference|référenc)[^.;]{0,100}?(?:purchase[- ]order(?: number| no\.?| #)?|\bP\.?O\.?(?: number| no\.?| #)\b|bon de commande|num[ée]ro de (?:bon de )?commande)", re.I)
NO_PO_NO_PAY = re.compile(r"no (?:purchase order|PO)[, ]+no pay(?:ment)?|pas de (?:bon de commande|BC)[, ]+pas de paiement", re.I)
PORTALS = [("SAP Ariba", r"ariba"), ("Coupa", r"coupa"), ("Jaggaer", r"jaggaer|sciquest"), ("Tungsten / Kofax", r"tungsten"), ("Basware", r"basware"), ("SAP Business Network", r"sap business network"),
           ("Esker", r"\besker\b"), ("Taulia", r"taulia"), ("Tradeshift", r"tradeshift"), ("Oracle iSupplier / Supplier Portal", r"isupplier|oracle supplier portal|oracle fusion supplier"), ("Workday supplier portal", r"workday[^.]{0,30}supplier"),
           ("Bonfire", r"bonfirehub|gobonfire"), ("bids&tenders", r"bidsandtenders|bids ?& ?tenders"), ("MERX", r"\bmerx\b"), ("SEAO", r"\bseao\b"), ("Transcepta", r"transcepta"), ("OpenInvoice / Enverus", r"openinvoice"), ("Cortex", r"\bcortex\b[^.]{0,30}invoice"),
           ("GHX", r"\bghx\b"), ("PaymentWorks", r"paymentworks"), ("Zycus", r"zycus"), ("Ivalua", r"ivalua"), ("GEP SMART", r"gep smart|smart by gep"), ("Medius", r"\bmedius\b"), ("Yooz", r"\byooz\b"), ("Procurify", r"procurify"),
           ("supplier / vendor portal", r"(?:supplier|vendor|fournisseurs?) (?:self[- ]service )?portal|portail (?:des )?fournisseurs?|e-?invoicing portal|invoice portal|portail de facturation")]
PORTAL_HREF = re.compile(r"href=[\"']([^\"']+)[\"']", re.I)
# new-supplier setup: the forms AP teams require before a first payment (vendor registration, direct-deposit / EFT enrolment) — owner 2026-11-08 14:53 EST
SETUP_LINK = re.compile(r"<a\s[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.{0,160}?)</a>", re.I | re.S)
SETUP_TXT = re.compile(r"vendor registration|supplier registration|become a (?:supplier|vendor)|new (?:vendor|supplier) (?:form|setup|set-up|registration|application)|vendor (?:setup|set-up|onboarding|information) form|supplier (?:setup|set-up|onboarding|information) form|direct deposit (?:form|enrol|authori[sz]ation|application|request)|EFT (?:form|enrol|authori[sz]ation|request|application)|electronic funds transfer (?:form|enrol|authori[sz]ation)|inscription des fournisseurs|devenir fournisseur|formulaire (?:de |d')(?:inscription|d[ée]p[ôo]t direct|paiement [ée]lectronique|fournisseur)|d[ée]p[ôo]t direct", re.I)
PHONE = re.compile(r"(?:\+?1[\s.-]?)?\(?\b[2-9]\d{2}\)?[\s.-]\d{3}[\s.-]\d{4}\b(?:\s?(?:x|ext\.?|poste|p\.)\s?\d{1,6})?", re.I)
PC_CA = r"[A-Z]\d[A-Z]\s?\d[A-Z]\d"
ADDR = re.compile(r"(?:(?:P\.?\s?O\.?\s?Box|C\.?P\.?|Case postale|Boîte postale|Bo[iî]te postale)\s?\d+[^,\n]{0,40}|\b\d{1,6}[A-Za-z]?(?:[-–]\d{1,6})?\s(?:[A-Za-zÀ-ÿ'.-]+\s){1,6}(?:Street|St\.?|Avenue|Ave\.?|Road|Rd\.?|Boulevard|Blvd\.?|Drive|Dr\.?|Way|Place|Crescent|Court|Highway|Hwy|Parkway|Trail|Lane|Square|Rue|Boul\.?|Chemin|Ch\.|Route|Avenue|Montée|Rang|Promenade)[^,\n]{0,40})"
                  r"[,\s]+(?:(?:Suite|Unit|Bureau|Floor|#)\s?[\w-]+[,\s]+)?[A-Za-zÀ-ÿ'. -]{2,40}[,\s]+(?:[A-Z]{2}|Ontario|Québec|Quebec|Alberta|Manitoba|Saskatchewan|British Columbia|Nova Scotia|New Brunswick|Newfoundland and Labrador|Prince Edward Island|Yukon|Nunavut|Northwest Territories)[,\s]+(?:" + PC_CA + r"|\d{5}(?:-\d{4})?)", re.I)
BN = re.compile(r"\b(\d{9})\s?(?:RT|RT\s?0001|RT0001)\b|\b(\d{9})\s?RT\s?0+1\b")
BN_WORDS = re.compile(r"\bGST\b|\bHST\b|\bTPS\b|\bTVH\b|business number|num[ée]ro d'entreprise|registration (?:no|number)|BN\b", re.I)
FORMAT = re.compile(r"(?:(?:one|single|1|une seule|une) (?:invoice|facture)s? per (?:e-?mail|courriel|attachment|PDF)|(?:invoices?|factures?)[^.;]{0,80}?\b(?:PDF|TIFF|TIF)\b[^.;]{0,60}|\b(?:PDF|TIFF)\b[^.;]{0,30}?(?:format|only|seulement|uniquement|attachments?|pi[èe]ces? jointes?)|"
                    r"(?:do not|ne pas|n'envoyez pas)[^.;]{0,30}?(?:send|submit|envoyer)[^.;]{0,30}?(?:paper|duplicate|copies?|papier)[^.;]{0,60}|(?:maximum|max\.?|limit(?:ed)? to)[^.;]{0,20}?\d+\s?(?:MB|Mo|pages?|attachments?)[^.;]{0,40})", re.I)
PAYMETHOD = re.compile(r"(?:direct deposit|electronic funds transfer|\bEFT\b|\bACH\b|e-?transfer|d[ée]p[ôo]t direct|virement(?: bancaire)?|transfert [ée]lectronique de fonds|\bTEF\b)[^.;]{0,80}(?:preferred|encourag|required|mandatory|only|no longer|default|standard|privil[ée]gi|obligatoire|requis|exig|available|offered|enrol|sign[- ]?up|register|authori[sz]ation|formulaire|inscri)|"
                       r"(?:preferred|encourag|required|mandatory|no longer issue|will not issue|discontinu|privil[ée]gi|obligatoire|ne (?:sera|seront) plus [ée]mis)[^.;]{0,80}(?:direct deposit|electronic funds transfer|\bEFT\b|\bACH\b|cheques?|checks?|d[ée]p[ôo]t direct|virement|ch[èe]ques?)|"
                       r"(?:payments? (?:is|are|will be|shall be) (?:made|issued|processed|sent|remitted)|we pay|pays? (?:our |its )?(?:suppliers|vendors)|paiements?(?: aux fournisseurs| des fournisseurs| des factures)? (?:sont|est|seront) (?:effectu[ée]s?|[ée]mis|vers[ée]s?|faits?)|nous payons|r[èe]glement des factures)[^.;]{0,40}?(?:by|via|through|par|en)\s(?:direct deposit|electronic funds transfer|\bEFT\b|\bACH\b|e-?transfer|cheque|check|wire|d[ée]p[ôo]t direct|virement|ch[èe]que|carte de cr[ée]dit|credit card|p-?card|purchasing card)[^.;]{0,80}|"
                       r"(?:direct deposit|\bEFT\b|\bACH\b|d[ée]p[ôo]t direct|virement)\s(?:form|enrol?l?ment|authori[sz]ation|request|application|sign[- ]?up|registration|formulaire|inscription|adh[ée]sion)[^.;]{0,80}|(?:formulaire|form)[^.;]{0,25}?(?:d'?inscription au |de |for |pour le )?(?:d[ée]p[ôo]t direct|direct deposit|\bEFT\b|virement)[^.;]{0,60}|"
                       r"(?:supplier|vendor|fournisseur)s?[^.;]{0,40}?(?:paid|pay[ée]s?)[^.;]{0,20}?(?:by|par)\s(?:direct deposit|EFT|electronic funds transfer|cheque|check|d[ée]p[ôo]t direct|virement|ch[èe]que)[^.;]{0,60}", re.I)
APCYCLE = re.compile(r"(?:cheque|check|payment|EFT|direct deposit|paiement|ch[èe]que|accounts? payable|AP)s?\s(?:runs?|cycles?|are (?:issued|processed|released|made|mailed|generated|disbursed)|is (?:issued|processed|released|made|generated)|will be (?:issued|processed|released|made)|sont (?:[ée]mis|trait[ée]s|effectu[ée]s|g[ée]n[ée]r[ée]s)|processing)[^.;]{0,100}?(?:weekly|bi-?weekly|every (?:second |other |two )?(?:week|monday|tuesday|wednesday|thursday|friday|\d+ (?:days|weeks))|twice (?:a|per) month|once (?:a|per) (?:week|month)|monthly|semi-?monthly|on (?:monday|tuesday|wednesday|thursday|friday)s?|(?:each|every) (?:monday|tuesday|wednesday|thursday|friday)|hebdomadaire|aux deux semaines|toutes les deux semaines|chaque (?:semaine|jeudi|vendredi|mardi|mercredi|lundi)|mensuel|deux fois par mois|les (?:lundis|mardis|mercredis|jeudis|vendredis))[^.;]{0,60}|"
                     r"(?:weekly|bi-?weekly|twice[- ]monthly|semi-?monthly|monthly|hebdomadaire|aux deux semaines)\s(?:cheque|check|payment|EFT|paiement|AP|accounts payable)\s(?:runs?|cycles?|processing|[ée]mission)[^.;]{0,60}|"
                     r"(?:payment|cheque|check|EFT) (?:run|cycle|processing) (?:dates?|schedule|calendar)[^.;]{0,100}|invoices? (?:received|approved|submitted|dated) (?:by|before|on or before)[^.;]{0,60}?(?:paid|processed|payment|issued)[^.;]{0,80}|(?:calendrier|dates?) (?:des )?(?:paiements?|d'[ée]mission des ch[èe]ques)[^.;]{0,80}", re.I)
TAXEX = re.compile(r"(?:tax[- ]exempt(?:ion)?(?: status| certificate| number)?|exempt from (?:GST|HST|PST|QST|sales tax)|GST(?:/HST)? exempt|exemption (?:de|des) taxes?|exon[ée]r[ée]e? (?:de la |des )?(?:TPS|TVQ|TVH|taxes?)|do not charge (?:GST|HST|PST|tax)|ne pas (?:facturer|charger) (?:la |les )?(?:TPS|TVQ|taxes?)|status indian|first nation[^.;]{0,30}exempt|diplomatic (?:tax )?exempt)[^.;]{0,100}|"
                   r"(?:GST|HST|GST/HST|PST|QST|TPS|TVQ|TVH)(?: registration| account)? (?:number|no\.?|#|num[ée]ro)s?[^.;]{0,40}?(?:must|should|shall|is required|are required|doit|doivent|required|requis|obligatoire)[^.;]{0,70}|"
                   r"(?:show|indicate|itemi[sz]e|list|display|include|break out|state|identify)[^.;]{0,40}?(?:GST|HST|PST|QST|sales tax|taxes)[^.;]{0,30}?separately[^.;]{0,60}|(?:GST|HST|GST/HST|PST|QST|TPS|TVQ|TVH|sales taxes?|taxes)[^.;]{0,30}?(?:must|should|shall|is to|are to) (?:be )?(?:shown|indicated|itemi[sz]ed|listed|identified|stated|appear|broken out|charged|added|included)[^.;]{0,80}|(?:taxes?|TPS|TVQ|TVH)[^.;]{0,30}?(?:doivent|doit) (?:être )?(?:indiqu[ée]e?s?|pr[ée]sent[ée]e?s?|d[ée]taill[ée]e?s?|ventil[ée]e?s?|inscrite?s?) s[ée]par[ée]ment[^.;]{0,60}|"
                   r"(?:applicable|all) (?:sales )?taxes? (?:must|should|shall|are to|will) be (?:shown|identified|itemi[sz]ed|listed|indicated|included|added|charged|extra)[^.;]{0,80}|(?:prices?|amounts?|pricing|montants?|prix)[^.;]{0,30}?(?:exclusive|inclusive|exclud|includ|incluent|excluent|avant|plus)[^.;]{0,20}?(?:of )?(?:applicable |les )?(?:GST|HST|taxes)[^.;]{0,60}|"
                   r"(?:our|the (?:city|town|township|village|municipality|county|region|district|board|university|college|hospital|authority|agency|corporation|commission|school|centre)'s|notre|la ville|le centre)[^.;]{0,30}?(?:GST|HST|GST/HST|TPS|TVQ|TVH|business|tax) (?:registration |account )?(?:number|no\.?|#|num[ée]ro)[^.;]{0,20}?(?:is|:|est)\s?[^.;]{0,40}\d{9}[^.;]{0,30}|"
                   r"(?:public service bod(?:y|ies)|PSB|municipal|municipalit[ée]s?) (?:rebate|remboursement)[^.;]{0,80}|(?:GST|HST|TPS|TVH)[^.;]{0,20}?(?:applies|is applicable|s'applique|is charged|will be added)[^.;]{0,60}|(?:PST|QST|TVQ)[^.;]{0,20}?(?:does not apply|not applicable|ne s'applique pas|exempt)[^.;]{0,60}|(?:zero[- ]rated|d[ée]tax[ée]e?s?)[^.;]{0,60}", re.I)
ESIGN = re.compile(r"(?:DocuSign|Adobe Sign|Adobe Acrobat Sign|HelloSign|Dropbox Sign|PandaDoc|OneSpan|ConsignO|Notarius|signature[s]? (?:[ée]lectronique|num[ée]rique)s?|e-?signatures?|digital(?:ly)? sign(?:ed|ature)s?|electronic(?:ally)? sign(?:ed|ature)s?(?: (?:are |is )?(?:accepted|required|preferred|not accepted))?)[^.;]{0,80}", re.I)
ESIGN_CTX = re.compile(r"contract|agreement|purchase order|\bPO\b|bon de commande|contrat|entente|invoice|factur|supplier|vendor|fournisseur|document", re.I)
# AP / ERP / e-procurement systems the organisation names on its payables, supplier or purchasing pages (the AP system hint of the invoice card)
SYSTEMS = re.compile(r"\b(SAP Ariba|Ariba|Coupa|Jaggaer|Workday|Oracle (?:E-Business Suite|EBS|ERP Cloud|Fusion|iSupplier|PeopleSoft|NetSuite)|PeopleSoft|SAP S/4 ?HANA|SAP Business Network|\bSAP\b|Esker|Kofax|Tipalti|Bill\.com|AvidXchange|Basware|Tungsten|Taulia|Tradeshift|Unit4|Agresso|Dynamics ?365|Dynamics GP|Great Plains|"
                     r"Sage Intacct|Sage 300|Sage 50|Munis|Tyler Technologies|Yardi|JD Edwards|Infor|Lawson|NetSuite|Ellucian|Colleague|Acomba|Avantage|SOFE|Virtuo|PG Solutions|M[ée]gagest|Unicit[ée]|Paymode-?X|Bottomline|Telpay|Plooto|Versapay|Kyriba|Medius|Yooz|Procurify|Bonfire|Ivalua|Zycus|GEP SMART|OpenInvoice|Transcepta|PaymentWorks|Cortex|GHX|Vendorlink|"
                     r"Paramount WorkPlace|Emburse|Blackbaud|Financial Edge|CaseWare|QuickBooks|Xero|FreshBooks|Wave Accounting|Microsoft Dynamics|Dynamics NAV|Business Central|Birchstreet|Determine|Periscope|Euna|eSolutions|Biddingo|MERX|SEAO|Ariba Network|Dayforce|Ceridian)\b", re.I)
SYS_CTX = re.compile(r"invoice|factur|supplier|vendor|fournisseur|payable|paiement|payment|purchase order|bon de commande|procurement|approvisionnement|e-?procurement|portal|portail|\bAP\b|\bERP\b|accounting system|financial system|syst[èe]me (?:comptable|financier|de gestion)|e-?tendering|bid|soumission|appel d'offres", re.I)
PAY_CTX = re.compile(r"invoice|factur|supplier|vendor|fournisseur|payable|payment to|paiements? (?:aux|des) fournisseurs|purchase order|bon de commande|remittance|accounts payable|comptes (?:à|a) payer|contractor|entrepreneur", re.I)
PAY_NOISE = re.compile(r"property tax|taxes fonci|utility bill|water bill|parking|ticket|fine|permit fee|dog licen|tuition|pay your|payez votre|donation|\bdon\b|membership|registration fee|frais d'inscription|camp|program fee|rent payment|tenant", re.I)
# the AP contact rule of rank.py (conservative; business contact information the organisation prints itself, never a mailbox)
_cands = [os.path.join(d, "contrib/claude/rank_buyers/rank.py") for d in (os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.getcwd(), os.path.expanduser("~/cch-crawler"))]
_src = open(next(p for p in _cands if os.path.exists(p)), encoding="utf-8").read()
_ns = {"re": re, "_FIRST": _FIRST}
exec(_src[_src.index("AP_TITLE = re.compile("):_src.index("NOT_NAME = re.compile(")], _ns)
exec(_src[_src.index("HONORIFIC = re.compile("):_src.index("FR = re.compile(")], _ns)
ap_contact_name = _ns["ap_contact_name"]
_AP_TITLE, _NAME_RX, _NOT_NAME2, _HONORIFIC = _ns["AP_TITLE"], _ns["NAME_RX"], _ns["NOT_NAME2"], _ns["HONORIFIC"]
AP_ROLE_PHRASE = re.compile(r"(?:(?:senior |junior |chief |assistant |associate )?(?:accounts? payable|payables?|comptes? (?:à|a) payer|comptes payables|finance|financial|accounting|comptabilit[ée]|treasury|tr[ée]sorerie|AP)"
                            r"[\w /&'’-]{0,30}?(?:clerk|supervisor|manager|coordinator|coordinatrice|coordonnat\w+|technician|technicienne?|specialist|officer|administrator|analyst|lead|assistant|agente?|commis|adjointe?|directeur|directrice|director|controller|contr[ôo]leur|treasurer|tr[ée]sori[èe]re?|accountant|comptable)|"
                            r"(?:commis|technicienne?|agente?|adjointe?|coordonnat\w+|pr[ée]pos[ée]e?|analyste|conseill[èe]re?|chef|directeur|directrice|responsable|superviseure?|clerk|technician|coordinator|supervisor|manager|specialist|officer)"
                            r"(?: (?:en|de|des|du|à la|aux|of|for|,|-|–))? (?:la )?(?:comptabilit[ée]|comptes? (?:à|a) payer|comptes payables|accounts? payable|payables|finances?|paie|facturation|invoic\w+|accounting))", re.I)


def ap_contact_name_any(text, buyer=""):
    """owner 2026-11-08 ("person is allowed for AP"): the AP contact person the organisation itself prints on its AP / finance / staff
    page — a proper name (known given name or honorific) within 80 characters of an accounts-payable role phrase; the role phrase is kept
    with the name. Still only what the organisation publishes about itself; the mailbox columns stay organisational."""
    btoks = set(re.findall(r"[a-zà-ÿ]{3,}", (buyer or "").lower()))
    for m in AP_ROLE_PHRASE.finditer(text[:200_000]):
        win = text[max(0, m.start() - 80):m.end() + 80]
        for nmm in _NAME_RX.finditer(win):
            nm = nmm.group(1)
            toks = nm.split()
            hon = bool(_HONORIFIC.search(win[max(0, nmm.start() - 12):nmm.start()]))
            if toks[0] in ("Mme", "Madame", "Monsieur", "Mr", "Mrs", "Ms", "Dr"):
                hon, toks = True, toks[1:]
                nm = " ".join(toks)
            if len(toks) < 2 or len(toks) > 3 or _NOT_NAME2.search(nm) or re.search(r"\d", nm) or set(t.lower() for t in toks) & btoks:
                continue
            if not (toks[0].lower() in _FIRST or hon):
                continue
            role = re.sub(r"\s+", " ", m.group(0)).strip()
            return "%s (%s)" % (nm, role), win
    return "", ""


def q300(text, start, end):
    """a quote of at most 300 characters around text[start:end], cut at word boundaries"""
    if end - start >= 290:
        return text[start:start + 300].strip()
    pad = (300 - (end - start)) // 2
    a, b = max(0, start - pad), min(len(text), end + pad)
    q = text[a:b]
    if a > 0:
        q = q.split(" ", 1)[-1]
    if b < len(text):
        q = q.rsplit(" ", 1)[0]
    return q.strip()[:300]


def near(text, i, span=600):
    return text[max(0, i - span):i + span], max(0, i - span)


def read_page(url):
    if not C.allowed(url):
        return "robots", url, "", ""
    try:
        status, ctype, data, final = C.fetch(url)
    except Exception:
        return "error", url, "", ""
    if status in (401, 403, 429):
        return "blocked", final, "", ""
    if status != 200 or not data:
        return "http_%s" % status, final, "", ""
    is_pdf = "pdf" in (ctype or "").lower() or data[:5] == b"%PDF-"
    if is_pdf:
        text = re.sub(r"\s+", " ", C.pdf_text(data) or "")
        return "ok", final, text, ""
    raw = html.unescape(data.decode("utf-8", "replace"))
    if C.BLOCK_RX.search(raw[:20000]) and len(raw) < 60000:
        return "blocked", final, "", ""
    raw = re.sub(r"data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+", " ", raw[:3_000_000])
    return "ok", final, C.visible(raw), raw


def extract(email, buyer, text, raw, final):
    out = {}
    low = text.lower()
    i = low.find(email.lower())
    out["mailbox_still_on_page"] = "yes" if i >= 0 or (raw and email.lower() in raw.lower()) else "no"
    if i >= 0:  # O1.2: the page's own text around the mailbox (500 characters), verbatim, for disambiguation — the 300-character quote stays the verified value
        out["mailbox_context"] = re.sub(r"\s+", " ", text[max(0, i - 250):i + len(email) + 250]).strip()[:600]
    # windows: around the mailbox when it is on the page, else around invoice words
    anchors = [i] if i >= 0 else [m.start() for m in re.finditer(r"invoice|factur|accounts? payable|comptes? (?:à|a) payer|comptes payables|payables", low)][:6]
    win_txt = ""
    for a in anchors:
        w, _ = near(text, a, 700)
        win_txt += " " + w
    win_txt = win_txt.strip() or text[:4000]
    m = TERMS.search(win_txt) or TERMS.search(text)
    if m and not re.search(r"days? (?:a week|per week|of operation|notice)|opening hours", m.group(0), re.I):
        src = win_txt if m.re.search(win_txt) and m.string is win_txt else text
        out["payment_terms"] = re.sub(r"\s+", " ", m.group(0)).strip()[:100]
        out["payment_terms_quote"] = q300(src, m.start(), m.end())
    m = NO_PO_NO_PAY.search(text) or PO_REQ.search(win_txt) or PO_REQ.search(text)
    if m:
        src = m.string
        frag = re.sub(r"\s+", " ", m.group(0)).strip()[:120]
        out["po_quote"] = q300(src, m.start(), m.end())
        out["po_required"] = ("yes (as published: %s)" if re.search(r"invoice|factur", out["po_quote"], re.I) else "purchase-order terms published (as published: %s)") % frag
    for name, rx in PORTALS:
        m = re.search(rx, win_txt, re.I) or re.search(rx, text, re.I)
        if m:
            src = m.string
            out["portal_name"] = name
            out["portal_quote"] = q300(src, m.start(), m.end())
            if raw:
                for h in PORTAL_HREF.findall(raw):
                    if re.search(rx, h, re.I) and not h.startswith(("mailto:", "#", "javascript")):
                        out["portal_url"] = urllib.parse.urljoin(final, h)[:300]
                        break
            break
    if i >= 0:
        w, off = near(text, i, 250)
        m = PHONE.search(w)
        if m and not re.search(r"fax|t[ée]l[ée]copieur", w[max(0, m.start() - 25):m.start()], re.I):
            out["ap_phone"] = re.sub(r"\s+", " ", m.group(0)).strip()
            out["ap_phone_quote"] = q300(text, off + m.start(), off + m.end())
        w, off = near(text, i, 450)
        m = ADDR.search(w)
        if m:
            out["invoice_mailing_address"] = re.sub(r"\s+", " ", m.group(0)).strip()[:200]
            out["address_quote"] = q300(text, off + m.start(), off + m.end())
        w, off = near(text, i, 90)
        nm = ap_contact_name(w, email, buyer)
        if nm:
            out["ap_contact_name"] = nm
            out["contact_quote"] = q300(text, off, off + len(w))
    if not out.get("ap_contact_name"):  # owner 2026-11-08: the AP person the page names with an AP role phrase, anywhere on the AP page
        nm, win = ap_contact_name_any(text, buyer)
        if nm:
            j = text.find(win)
            out["ap_contact_name"] = nm
            out["contact_quote"] = q300(text, j, j + len(win)) if j >= 0 else win[:300]
    m = FORMAT.search(win_txt)
    if m:
        out["invoice_format"] = re.sub(r"\s+", " ", m.group(0)).strip()[:160]
        out["invoice_format_quote"] = q300(win_txt, m.start(), m.end())
    for m in BN.finditer(text):
        w = text[max(0, m.start() - 120):m.end() + 40]
        if BN_WORDS.search(w):
            out["buyer_bn"] = (m.group(1) or m.group(2)) + "RT0001"
            out["bn_quote"] = q300(text, m.start() - 0, m.end())
            break
    for col, rx in (("payment_method", PAYMETHOD), ("ap_cycle", APCYCLE), ("tax_exempt", TAXEX), ("esignature", ESIGN)):
        for src in (win_txt, text):
            for m in rx.finditer(src):
                ctx = src[max(0, m.start() - 300):m.end() + 300]
                if PAY_NOISE.search(ctx) and not re.search(r"supplier|vendor|fournisseur|payable|invoice|factur", ctx, re.I):
                    continue  # a citizen-payment page (property taxes, tickets), not payables
                if col == "esignature" and not ESIGN_CTX.search(ctx):
                    continue
                if col in ("payment_method", "tax_exempt", "ap_cycle") and not PAY_CTX.search(ctx):
                    continue
                out[col] = re.sub(r"\s+", " ", m.group(0)).strip()[:160]
                out[col + "_quote"] = q300(src, m.start(), m.end())
                break
            if out.get(col):
                break
    names = []
    for m in SYSTEMS.finditer(text):
        ctx = text[max(0, m.start() - 160):m.end() + 160]
        if SYS_CTX.search(ctx) and not PAY_NOISE.search(ctx):
            nm = m.group(1)
            if nm.lower() not in [n.lower() for n in names]:
                names.append(nm)
                if "ap_system_quote" not in out:
                    out["ap_system_quote"] = q300(text, m.start(), m.end())
        if len(names) >= 3:
            break
    if names:
        out["ap_system"] = ", ".join(names)[:160]
    if "invoice_format_quote" in out:
        out["format_quote"] = out.pop("invoice_format_quote")
    for m in SETUP_LINK.finditer(raw):
        href, label = m.group(1), re.sub(r"<[^>]+>|\s+", " ", m.group(2)).strip()
        if href.startswith(("mailto:", "#", "javascript", "tel:")):
            continue
        if SETUP_TXT.search(label) or SETUP_TXT.search(urllib.parse.unquote(href).replace("-", " ").replace("_", " ")):
            out["setup_url"] = urllib.parse.urljoin(final, href)[:300]
            out["setup_quote"] = ("link text: %s" % label)[:300]
            break
    return out


QMAP = {"invoice_mailing_address": "address_quote", "ap_contact_name": "contact_quote", "invoice_format": "format_quote", "po_required": "po_quote", "buyer_bn": "bn_quote", "portal_name": "portal_quote", "setup_url": "setup_quote"}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--ranked", default="")
    a.add_argument("--tiers", default="A,B,T,M,L,C,D,E,F")
    a.add_argument("--workers", type=int, default=24)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--recheck-days", type=int, default=45)
    a.add_argument("--grades", default="invoicing,finance,purchasing", help="email_type prefixes to read (general pages rarely carry terms)")
    a.add_argument("--force", action="store_true", help="re-read pages already read (new columns)")
    a.add_argument("--urls", default="", help="CSV buyer_key,buyer_name,website,official_site,url (search results): read these pages, keyed by buyer_key instead of mailbox")
    a.add_argument("--reread-known", action="store_true", help="re-read every page already in the output files (new extraction patterns); a page that no longer answers keeps its old row")
    a.add_argument("--shard", default="", help="K/N: only pages whose host hashes to shard K of N (parallel runners)")
    a = a.parse_args()
    shard_k, shard_n = (int(a.shard.split("/")[0]), int(a.shard.split("/")[1])) if a.shard else (0, 1)
    def in_shard(url):
        h = (urllib.parse.urlparse(url).hostname or "").lower()
        return shard_n == 1 or int(hashlib.md5(h.encode()).hexdigest(), 16) % shard_n == shard_k
    out = os.path.join(a.repo, "data/incoming/claude/claude_ap_terms.csv")
    prev = {}
    for r in read_rows(out) + read_rows(pages_file(out)):
        prev[(r["email"], r["evidence_url"])] = r
    ranked = a.ranked or os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv.gz")
    opener = gzip.open if ranked.endswith(".gz") else open
    tiers = set(a.tiers.split(","))
    grades = tuple(a.grades.split(","))
    todo, seen = [], set()
    cutoff = (datetime.date.today() - datetime.timedelta(days=a.recheck_days)).isoformat()
    with opener(ranked, "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("tier") or "") not in tiers or not (r.get("email") or "") or not (r.get("email_evidence_url") or "").startswith("http"):
                continue
            if not (r.get("email_type") or "").startswith(grades):
                continue
            k = (r["email"].lower(), r["email_evidence_url"])
            if k in seen:
                continue
            seen.add(k)
            p = prev.get(k)
            if p and not a.force and p.get("retrieved_date", "") >= cutoff and p.get("status") not in ("error", "http_0"):
                continue
            todo.append((r["email"].lower(), r["email_evidence_url"], r.get("buyer") or "", r.get("rank_group") or ""))
    if a.urls:
        todo = []
        for r in csv.DictReader(open(a.urls, encoding="utf-8")):
            k = (r.get("buyer_key") or "").strip(); u = (r.get("url") or "").strip()
            if k and u.startswith("http") and (k, u) not in seen and (a.force or (k, u) not in prev):
                seen.add((k, u)); todo.append((k, u, r.get("buyer_name") or "", "URLS"))
    if a.reread_known:
        todo = [(k[0], k[1], "", "REREAD") for k, r in prev.items() if r.get("status") == "ok" and k[1].startswith("http")]
    todo = [t for t in todo if in_shard(t[1])]
    todo.sort(key=lambda t: (t[3] != "GOLD", t[3][:1] not in ("A", "B"), t[3]))
    if a.limit:
        todo = todo[:a.limit]
    print("pages to read: %d (known: %d)" % (len(todo), len(prev)), flush=True)
    stats = {}
    n_done = [0]

    def one(t):
        email, url, buyer, grp = t
        st, final, text, raw = read_page(url)
        row = {c: "" for c in COLS}
        row.update(email=email, evidence_url=url, final_url=final, retrieved_date=TODAY, status=st)  # in --urls mode the "email" column carries the buyer_key
        if st == "ok":
            try:
                row.update(extract(email, buyer, text, raw, final))
            except Exception as e:
                row["status"] = "extract_error:" + type(e).__name__
        old = prev.get((email, url))
        if old and old.get("status") == "ok":
            if row["status"] != "ok":
                return  # a page that no longer answers (timeout, 403 today) keeps the row read earlier: nothing verified is thrown away
            for c in COLS:  # a value read earlier whose quote is still on the page stays when the new read left the column empty (pattern order, page layout)
                if c.endswith("_quote") or c in ("email", "evidence_url", "final_url", "retrieved_date", "status", "mailbox_still_on_page", "mailbox_context"):
                    continue
                if old.get(c) and not row.get(c):
                    oq = old.get(c + "_quote") or old.get(QMAP.get(c, ""), "")
                    probe = re.sub(r"\s+", " ", (oq or old[c]))[:120].lower()
                    if probe and probe in re.sub(r"\s+", " ", text).lower():
                        row[c] = old[c]
                        if oq:
                            row[QMAP.get(c, c + "_quote")] = oq
        with lock:
            prev[(email, url)] = row
            stats[row["status"][:12]] = stats.get(row["status"][:12], 0) + 1
            n_done[0] += 1
            if n_done[0] % 200 == 0:
                print(n_done[0], stats, "terms:%d po:%d portal:%d phone:%d addr:%d name:%d bn:%d" % tuple(sum(1 for v in prev.values() if v.get(c)) for c in ("payment_terms", "po_required", "portal_name", "ap_phone", "invoice_mailing_address", "ap_contact_name", "buyer_bn")), flush=True)
            if n_done[0] % 1000 == 0:
                write(out, prev)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    write(out, prev)
    print("wrote", out, len(prev), stats, flush=True)
    print("filled:", {c: sum(1 for v in prev.values() if v.get(c)) for c in ("payment_terms", "po_required", "portal_name", "portal_url", "ap_phone", "invoice_mailing_address", "ap_contact_name", "invoice_format", "buyer_bn", "setup_url")}, flush=True)


def pages_file(out):
    """the walker / search page rows (keyed by buyer_key, no '@') live in a gzipped companion: the single CSV passed 50 MB on 2026-11-08 and GitHub refuses 100 MB"""
    return out[:-4] + "_pages.csv.gz" if out.endswith(".csv") else out + "_pages.csv.gz"


def read_rows(path):
    if not os.path.exists(path):
        return []
    import io as _io
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8", errors="replace") as f:
        txt = f.read().replace("\0", "")  # a page text once carried a NUL byte
    return list(csv.DictReader(_io.StringIO(txt)))


def write(out, prev):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rows = dict(prev)
    for path in (out, pages_file(out)):  # rows another runner (GitHub Actions shard, synced into this clone) wrote meanwhile are kept: union by key, this process's rows win
        try:
            for r_ in read_rows(path):
                k_ = (r_.get("email") or "", r_.get("evidence_url") or "")
                if all(k_) and k_ not in rows:
                    rows[k_] = r_
        except Exception as e_:
            print("union with the on-disk file failed:", path, type(e_).__name__, e_, flush=True)
    mail = {k: v for k, v in rows.items() if "@" in k[0]}
    pages = {k: v for k, v in rows.items() if "@" not in k[0]}
    for path, part in ((out, mail), (pages_file(out), pages)):
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path + ".tmp", "wt", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
            w.writeheader()
            for k in sorted(part):
                w.writerow({c: str(part[k].get(c, "") or "").replace("\0", "").replace("\r", " ") for c in COLS})
        os.replace(path + ".tmp", path)


if __name__ == "__main__":
    main()

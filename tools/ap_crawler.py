#!/usr/bin/env python3
"""No-AI crawler for buyers' invoicing / accounts-payable mailboxes. Built to run for days on the owner's Mac.

For every buyer in the research queues that has a known website (largest buyers first) it reads the buyer's own site
the way a visitor would: robots.txt respected, at most one request per second per site, a page budget per site, and
only links about invoicing, accounts payable, suppliers, purchasing, finance or contact. Role mailboxes for invoicing,
AP, supplier payment or purchasing found on those pages (HTML and PDF) are saved as buyer_ap rows with the page URL
and a quote, and pushed to GitHub, where the referee re-opens every page before anything enters the dataset.
No AI, no search engine. Blocked sites (401/403/429, CAPTCHA, bot checks) are skipped, never worked around.
Protected (obfuscated) e-mails are never decoded. Named people's mailboxes are dropped (same rule as the referee).

Run it in its own clone:  python3 tools/ap_crawler.py [--days 7] [--workers 8] [--limit N] [--max-seconds S]
State and log: ~/cch-crawler-state/.  Output: data/incoming/claude/claude_buyer_ap_results_crawl01.csv
Pass 1 reads up to 25 pages per site; pass 2 re-reads sites with nothing found, up to 60 pages. Then it checks for new
queue batches every 6 hours until --days is over.
"""
import gzip, argparse, csv, datetime, glob, heapq, html, io, json, os, re, shutil, subprocess, sys, threading, time, unicodedata
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import EMAIL, PERSONAL, ROLE_HINT, TLDS  # same mailbox rules as the referee

STATE = os.path.expanduser("~/cch-crawler-state")
OUT = "data/incoming/claude/claude_buyer_ap_results_crawl01.csv"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
COLS = ["task_id", "buyer_key", "org_name_as_found", "ap_email", "ap_email_type", "invoice_portal_url", "ap_phone",
        "invoice_mailing_address", "invoicing_requirements_summary", "applies_to", "evidence_url", "evidence_quote",
        "retrieved_date", "status", "queries_tried", "notes"]
LINK_KW = [(re.compile(r"(?<!manu)factur|invoice|payable|comptes?[-_ ]?(a|à)[-_ ]?payer|accounts?[-_ ]?pay|e-?invoic", re.I), 10),
           (re.compile(r"fournisseur|supplier|vendor|approvisionnement|purchas|procure|achats?\b|faire[-_ ]affaire|"
                       r"doing[-_ ]business|business[-_ ]with|appels?[-_ ]d|tender|bid", re.I), 6),
           (re.compile(r"financ|tr[ée]sor|treasur|comptab|accounting|paiement|payment", re.I), 5),
           (re.compile(r"terms[-_ ](?:and|&)[-_ ]conditions|conditions[-_ ]g[ée]n[ée]rales|modalit[ée]s|terms[-_ ]of|e-?procurement|ariba|coupa|portal|portail|"
                       r"bylaw|by-law|r[èe]glement|policy|policies|politique", re.I), 5),  # 2026-11-08: PO terms and conditions, purchasing bylaws and AP policies (PO rule, payment terms, cheque runs)
           (re.compile(r"nous[-_ ]joindre|contact|coordonn|directory|bottin|annuaire|services", re.I), 2)]
SKIP_EXT = re.compile(r"\.(jpe?g|png|gif|svg|webp|ico|mp4|mov|mp3|zip|doc|xls|pptx?|ics|css|js|xml|rss)(\?|$)", re.I)
OFFICE = re.compile(r"\.(docx|xlsx)(\?|$)", re.I)
EMAIL_RX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
AP_LOCAL = re.compile(r"(?<!manu)factur|invoice|payable|compt|account|^ap$|^ap[._-]|[._-]ap$|[._-]cap$|financ|fourniss|"
                      r"supplier|vendor|approv|achat|purchas|procure|paiement|payment|tresor|treasur|acquisition", re.I)
NOT_AP = re.compile(r"plainte|complaint|recevable|receivable|billing|patient|usager|emploi|career|job|media|presse|press|"
                    r"benevol|volunteer|fondation|foundation|donat|webmaster|privacy|confidential|rh[._-]|^rh$|hr[._-]|^hr$", re.I)
CONTEXT_AP = re.compile(r"(?<!manu)factur|invoice|payable|comptes? (à|a) payer|paiement|payment|fournisseur|supplier|vendor", re.I)
BLOCK_RX = re.compile(r"captcha|cf-challenge|challenge-platform|attention required|access denied|are you a robot", re.I)
FIN_NOT = re.compile(r"aid|bourse|scholar|tuition|student|etudiant|soutien|financement|funding|grant|subvention|invest|sustainab|"
                     r"bank|loan|pret|credit|donat|fondation|foundation|japan|china|europe|client", re.I)  # not the buyer's payables
RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "finance": 3, "procurement": 4, "general": 5, "role": 6}
# owner rule 2026-10-28: "not_published only when the organisation publishes no role mailbox at all". 2026-11-10: two thirds of the lead sites read in
# the cloud gave "nothing found" because small organisations publish sales@ / service@ / orders@ / team@ instead of info@. Those front-office role
# mailboxes count as the last resort (opt-in: general="any"; kept only when the site has no invoicing, AP, purchasing, finance or general mailbox;
# written as ap_email_type=general with a note). An explicit list: a single first name (john@) is never a role.
OTHER_ROLE = re.compile(r"^(sales|ventes?|service|services|serviceclient|service-client|service\.client|serviceclientele|sac|customerservice|customer-service|customer\.service|customercare|"
                        r"customer|clients?|clientele|support|soutien|help|aide|team|equipe|mail|email|e-mail|courriel|courrier|hi|bonjour|allo|salut|welcome|bienvenue|connect|enquiry|inquiry|"
                        r"inquire|ask|questions?|demandes?|requests?|orders?|commandes?|bookings?|reservations?|reserve|frontdesk|front-desk|front\.desk|main|mainoffice|headoffice|head-office|"
                        r"head\.office|siege|corporate|management|direction|dg|gm|operations|ops|shop|store|boutique|magasin|estimates?|quotes?|soumissions?|devis|rentals?|parts|pieces|"
                        # 2026-11-11 (240 sites that had given nothing were read again; 1 in 30 prints only a role word that was not on this list):
                        # the desk a small organisation answers from, named after what it does. Words only — a first name is never a role.
                        r"gestion|gerance|manager|leasing|locations?|admissions?|registrar|registraire|registration|inscriptions?|membership|members|membres|adhesion|adhesions|"
                        r"events?|evenements?|claims?|reclamations?|dispatch|repartition|shipping|expedition|livraison|delivery|warehouse|entrepot|intake|referrals?|appointments?|"
                        r"rendezvous|rdv|tickets?|billetterie|boxoffice|guestservices?|concierge|clinic|clinique|pharmacy|pharmacie|garage|atelier|studio|hotel|motel|camping|"
                        r"ecole|school|eglise|church|paroisse|parish|quoteme|getaquote|getquote|requestaquote|catering|traiteur|groups?|groupes?|tours?|voyages?|travel|production|"
                        r"projects?|projets?|communications?|marketing|bookstore|librairie|cityclerk|townclerk|townoffice|cityoffice|villageoffice|municipaloffice)"
                        r"(\d{0,2})([._-](info|general|office|team|ca|canada|qc|on|bc|ab|mtl|montreal|toronto|ottawa|quebec|vancouver|calgary|edmonton|winnipeg|halifax))?$", re.I)
_PLACE = (r"canada|ca|qc|on|bc|ab|mb|sk|ns|nb|nl|pei|mtl|montreal|toronto|ottawa|quebec|vancouver|calgary|edmonton|winnipeg|halifax|saskatoon|regina|victoria|laval|gatineau|"
          r"sherbrooke|kelowna|london|hamilton|kitchener|waterloo|mississauga|brampton|surrey|burnaby|moncton|fredericton|stjohns|charlottetown|sudbury|barrie|kingston|windsor|"
          r"oshawa|guelph|niagara|trois-?rivieres|saguenay|levis|longueuil|rimouski|drummondville|granby|whitehorse|yellowknife")
GENERAL = re.compile(r"^(?:(?:info|contact|contactus|reception|admin|administration|general|greffe|mairie|municipalite|townhall|cityhall|clerk|office|bureau|secretariat|accueil|hello|inquiries|"
                     r"enquiries|renseignements|information|informations|infos)(?:[._-]|$)|(?:info|contact|office|bureau)(?:%s)$)" % _PLACE, re.I)
TODAY = datetime.date.today().isoformat()

host_lock, host_next, robots = threading.Lock(), {}, {}
dom_next, _dom_of_host = {}, {}
DOMAIN_INTERVAL = 0.5  # seconds between two requests to the hosts of one registrable domain in this process (see fetch)
HOST_INTERVAL = 1.0  # seconds between two requests to one host in this process (other engines may read the same host: ap_walk uses 2.0)
out_lock, state_lock = threading.Lock(), threading.Lock()
stats = {"sites": 0, "pages": 0, "found_sites": 0, "rows": 0, "blocked": 0}
# 2026-11-08 (downstream §4): the AP / supplier / purchasing pages (and PDFs) a crawl reads are kept per buyer, so tools/ap_terms.py --urls
# can extract payment terms, PO rules, portals, invoice addresses from them even when the page shows no mailbox
AP_PAGES = {}
AP_PAGE_RX = re.compile(r"(?<!manu)factur|invoice|payable|comptes?[-_ ]?(a|à)[-_ ]?payer|accounts?[-_ ]?pay|e-?invoic|fournisseur|supplier|vendor|approvisionnement|purchasing|procurement|achats?\b|"
                        r"doing[-_ ]business|business[-_ ]with|terms[-_ ]and[-_ ]conditions|conditions[-_ ]g[ée]n[ée]rales|appels?[-_ ]d[-_ ]?offres|soumissions|tenders?\b|bids?\b|rfp|rfq|"
                        r"purchasing[-_ ](?:policy|bylaw|by-law|procedure)|procurement[-_ ](?:policy|bylaw|by-law|procedure)|accounts?[-_ ]payable[-_ ]policy|payment[-_ ]polic|politique[-_ ]d[-_ ]?(?:achat|approvisionnement)|r[èe]glement[-_ ]de[-_ ]gestion[-_ ]contractuelle|finance[-_ ]polic|bylaws?/|by-laws?/|policies/|politiques/", re.I)  # 2026-11-08: purchasing bylaws and AP policies carry the PO rule, payment terms and cheque-run cadence
AP_PAGE_WEAK = re.compile(r"/news/|/nouvelles/|/blog/|/events?/|cemetery|cimeti|parking|stationnement|real-?estate|land|property-tax|taxes?-fonci|recreation|loisirs|permit|licen[cs]e|transit|library|biblioth", re.I)
AP_TEXT_RX = re.compile(r"payment terms|net \d{2}|within \d{2} days|purchase order|bon de commande|conditions de paiement|modalit[ée]s de paiement|accounts payable|comptes [àa] payer|submit (?:your )?invoices?|"
                        r"soumettre (?:vos |les )?factures?|invoice[s]? (?:must|should|are to)|supplier portal|portail (?:des )?fournisseurs|vendor registration|inscription des fournisseurs|direct deposit|d[ée]p[ôo]t direct", re.I)
AP_PAGES_FILE = os.path.join(STATE, "ap_pages_seen.csv")


def note_ap_page(buyer_key, buyer_name, site, url, text, is_doc):
    """remember an AP-relevant page of this buyer's site (URL words or page text), at most 10 per site"""
    if not buyer_key:
        return
    path = urllib.parse.urlparse(url).path
    if AP_PAGE_WEAK.search(path) and not AP_TEXT_RX.search(text[:60000]):
        return  # news, cemetery lots, land purchases, parking payments: not the payables pages
    if not (AP_PAGE_RX.search(path) or AP_TEXT_RX.search(text[:60000])):
        return
    with out_lock:
        lst = AP_PAGES.setdefault(buyer_key, [])
        if len(lst) < 12 and url not in [u for u, _ in lst]:
            lst.append((url, "document" if is_doc else "page"))


def flush_ap_pages(buyer_key, buyer_name, site):
    with out_lock:
        lst = AP_PAGES.pop(buyer_key, [])
        if not lst:
            return
        new = not os.path.exists(AP_PAGES_FILE)
        with open(AP_PAGES_FILE, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["buyer_key", "buyer_name", "website", "official_site", "url", "kind", "date"])
            for u, k in lst:
                w.writerow([buyer_key, buyer_name, site, site, u, k, TODAY])


def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)


# 2026-11-11: sites of different organisations that live on one platform's servers (Wix: 185.230.60-63.x, Shopify: 23.227.38.x, a web
# host's shared machines) are one "host" for that platform. The site-facts readers, given a task list that was half Wix and Shopify sites,
# were refused (403 / 429) by 28 to 45 % of the sites — sites that answer a single reader without trouble. A reader that sets NET_INTERVAL
# waits that long between two requests to the same /24 of addresses, whatever the site names (0 = off: the mailbox crawl and the scan,
# whose lists are a few per cent platform sites, are not refused). Resolving a name is not a page request.
NET_INTERVAL = 0.0
_net_of_host, net_next = {}, {}


def net_of(host):
    """the /24 of the address a host name resolves to ("" when it does not resolve)"""
    n = _net_of_host.get(host)
    if n is None:
        try:
            import socket
            n = ".".join(socket.gethostbyname(host).split(".")[:3])
        except Exception:
            n = ""
        _net_of_host[host] = n
    return n


def fetch(url, limit=6_000_000, _hops=0):
    """(status, content_type, bytes, final_url); one request per second per host across all threads, two per registrable domain."""
    host = urllib.parse.urlparse(url).hostname or ""
    net = net_of(host) if NET_INTERVAL and host else ""
    # 2026-11-10: the hosts of one registrable domain are often one platform's servers (500 congregations on churchcenter.com, the municipalities
    # hosted on ao.ca) and each is read for itself now: together they get at most two requests a second, whatever the number of threads.
    dom = _dom_of_host.get(host)
    if dom is None:
        dom = _dom_of_host[host] = (registrable(host) if host else "") or host
    while True:
        with host_lock:
            now = time.time()
            wait = max(host_next.get(host, 0), dom_next.get(dom, 0), net_next.get(net, 0) if net else 0) - now
            if wait <= 0:
                host_next[host] = now + HOST_INTERVAL
                dom_next[dom] = now + DOMAIN_INTERVAL
                if net:
                    net_next[net] = now + NET_INTERVAL
                break
        time.sleep(min(wait, 1.0))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl()
    except urllib.error.HTTPError as e:
        # 2026-11-08: Python 3.9's urllib does not follow 308 (and some 301/307 with odd Location headers): 55 of the Gold buyers'
        # sites answered http_308 and were never read. Follow up to 5 redirects by hand.
        loc = e.headers.get("Location") if e.headers else None
        if e.code in (301, 302, 303, 307, 308) and loc and _hops < 5:
            nxt = urllib.parse.urljoin(url, loc.strip())
            if nxt != url:
                if (urllib.parse.urlparse(nxt).hostname or "") != host and not allowed(nxt):
                    return 403, "", b"", nxt  # the redirect target's robots.txt disallows us: treated like a block (reviewer 2026-11-08)
                return fetch(nxt, limit, _hops + 1)
        return e.code, "", b"", url
    except Exception as ex:
        msg = str(ex).lower()
        p = urllib.parse.urlparse(url)
        if _hops == 0 and p.scheme == "https" and ("ssl" in msg or "certificate" in msg or "handshake" in msg or "eof" in msg):
            return fetch("http://" + url[8:], limit, 1)  # broken TLS on a small municipal site: the plain-http copy is the same public page
        if _hops == 0 and ("nodename" in msg or "name or service" in msg or "getaddrinfo" in msg or "no address" in msg) and p.hostname and not p.hostname.startswith("www."):
            return fetch(url.replace("://" + p.hostname, "://www." + p.hostname, 1), limit, 1)  # bare host without a DNS record, www. has one
        return 0, "", b"", url


# A document behind a storage redirect (a link on the site answers with a pre-signed S3 / Azure / Google Storage address: access-key id, signature,
# valid a few minutes) — 2026-11-10: a row carried such an address as its evidence; it cannot be opened again, and GitHub's push protection
# refused the whole merge of a crawl run because of the key id in it. The address that was ASKED is the stable one: it is the evidence.
SIGNED_URL = re.compile(r"[?&](?:X-Amz-Signature|X-Amz-Credential|X-Amz-Security-Token|AWSAccessKeyId|Signature|X-Goog-Signature|X-Goog-Credential|GoogleAccessId|sig|Key-Pair-Id|Policy)=", re.I)


def stable_url(asked, final):
    return asked if (final and SIGNED_URL.search(final) and not SIGNED_URL.search(asked or "")) else (final or asked)


def allowed(url):
    p = urllib.parse.urlparse(url)
    if p.scheme not in ("http", "https") or not p.netloc:
        return False  # a relative or malformed URL (a sitemap entry without a host, "mailto:", "tel:"): nothing to fetch — walker 2026-11-08: 36 sites ended in ValueError ':///robots.txt'
    key = "%s://%s" % (p.scheme, p.netloc)
    if key not in robots:
        rp = urllib.robotparser.RobotFileParser()
        status, _, data, _ = fetch(key + "/robots.txt", 500_000)
        if status in (401, 403):
            rp.disallow_all = True
        elif status == 200:
            rp.parse(data.decode("utf-8", "replace").splitlines())
        else:
            rp.allow_all = True
        robots[key] = rp
    return robots[key].can_fetch(UA, url)


PDFTOTEXT = shutil.which("pdftotext") or next((p for p in ("/opt/homebrew/bin/pdftotext", "/usr/local/bin/pdftotext") if os.path.exists(p)), None)


def pdf_text(data):
    if PDFTOTEXT:  # poppler reads far more PDFs than pypdf (fonts, encodings)
        try:
            r = subprocess.run([PDFTOTEXT, "-layout", "-", "-"], input=data, capture_output=True, timeout=60)
            if r.stdout.strip():
                return r.stdout.decode("utf-8", "replace")
        except Exception:
            pass
    try:
        import pypdf
        return "\n".join((pg.extract_text() or "") for pg in pypdf.PdfReader(io.BytesIO(data)).pages[:40])
    except Exception:
        return ""


def office_text(data):
    """Text of a .docx / .xlsx file (zip of XML), for supplier forms and invoicing guides."""
    import zipfile
    try:
        z = zipfile.ZipFile(io.BytesIO(data))
        parts = [n for n in z.namelist() if n in ("word/document.xml", "xl/sharedStrings.xml") or n.startswith(("word/header", "word/footer"))]
        return " ".join(re.sub(r"<[^>]+>", " ", z.read(n).decode("utf-8", "replace")) for n in parts)
    except Exception:
        return ""


_COMMON_TLD = {"ca", "com", "org", "net", "edu", "gov", "info", "biz", "coop", "quebec", "us", "uk", "io", "co", "fr", "de", "au", "nz", "ie", "eu", "int", "mil"}


def page_emails(src):
    """the addresses in a page's source: lower case, a top-level domain that exists, and never an address plus the word that follows it.
    2026-11-10: descriptions and search indexes made by stripping tags without spaces print "info@site.caPhone", "ap@town.caDevelopment" next to
    the real address; 125 such strings had been taken for mailboxes (the last label is no TLD) — and "info@site.ca" + "re" would even be one."""
    es = {re.sub(r"^(?:u003e|u003c|u00a0|u0026|u0022|u0027|%[0-9a-f]{2})+", "", x.lower().rstrip(".")) for x in EMAIL_RX.findall(src)}  # "\u003ebilling@", "%20payments@": escape debris in front
    es = {e for e in es if "@" in e and not e.startswith("@")}
    if TLDS:
        es = {e for e in es if e.rsplit(".", 1)[-1] in TLDS}
    glued = {e for e in es if e.rsplit(".", 1)[-1] not in _COMMON_TLD
             and any(o != e and e.startswith(o) and o.rsplit(".", 1)[-1] in _COMMON_TLD for o in es)}
    return es - glued


# Minified pages write their attributes without quotes (<a href=https://example.org/contact>): 3 of 1,450 home pages sampled 2026-11-10 do
# it for most of their links, and every link expression of the readers expects quotes. The page is given its quotes back before it is read.
_UNQUOTED = re.compile(r"""(?i)(<(?:a|link|script|iframe|img|form|area|source|embed|frame)\b[^>]*?\s(?:href|src|action)\s*=\s*)([^\s"'>][^\s>]*)""")
_UNQUOTED_ANY = re.compile(r"""(?i)\s(?:href|src)=[^\s"'>]""")


def quote_attrs(raw):
    if not raw or not _UNQUOTED_ANY.search(raw[:600_000]):
        return raw
    for _ in range(4):  # a tag may carry several unquoted attributes: one is quoted per pass
        fixed = _UNQUOTED.sub(lambda m: '%s"%s"' % (m.group(1), m.group(2)), raw)
        if fixed == raw:
            break
        raw = fixed
    return raw


def visible(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


_A_PHONE = re.compile(r"(?:\+?1[\s.\-]?)?\(?\b\d{3}\)?[\s.\-]{1,2}\d{3}[\s.\-]\d{4}\b(?:\s*(?:ext|poste|x)\.?\s*\d{1,5})?", re.I)
_A_YEAR = re.compile(r"(?:©|\(c\)|copyright)\s*(?:19|20)\d{2}(?:\s*[-–]\s*(?:19|20)\d{2})?|\b(?:19|20)\d{2}\b(?=\s+(?:by|par|all rights|tous droits)\b|\s*[©|])", re.I)
_A_RIGHTS = re.compile(r"all rights reserved\.?|tous droits r[ée]serv[ée]s\.?", re.I)
_A_START = re.compile(r"(?<![\w-])(?:[A-Za-z]?\d{1,5}[A-Za-z]?\s?[-–]\s?)?\d{1,6}(?:[A-Za-z]|-[A-Za-z](?![A-Za-z]))?,?\s+(?:[–-]\s+)?(?:[a-zà-ÿ]+\.?\s+){0,2}[A-ZÀ-Ý0-9]")
# a floor or a unit written out in front of the street number belongs to the address: "3rd Floor, 1250 Dewdney Avenue", "Unit E5, 487 Cornwall Rd"
_A_UNIT = re.compile(r"(?:\b\d{1,3}(?:st|nd|rd|th|e|er|i[èe]me)\s+(?:floor|[ée]tage)|\b(?:suite|unit|unit[ée]|bureau|local|apt\.?|apartment|app\.?)\s*#?\s*[A-Za-z]?\d{1,5}[A-Za-z]?)\s*[,–-]?\s*$", re.I)
_A_BOX = re.compile(r"(?:P\.?\s?O\.?\s*Box|C\.?\s?P\.?|Case postale|B\.?\s?P\.?|Box|Suite|Unit|Unité|Bureau)\s*#?\s*$", re.I)
_A_TIME = re.compile(r"\b\d{1,2}\s?[:h]\s?\d{2}\b(?:\s*[ap]\.?\s?m\b\.?)?|\b\d{1,2}\s*[ap]\.?\s?m\b\.?", re.I)
# words of a page, not of an address: when they stand between a number and the street, the number is not the street number
_A_LABEL = re.compile(r"(?i)\b(?:address|adresse|location|located|hours|heures|contact|contactez|phone|t[ée]l[ée]phone|tel|email|e-mail|courriel|menu|cart|panier|shop|store|boutique|magasin|visit|find us|"
                      r"get in touch|subscribe|follow|copyright|rights|search|login|log in|account|accueil|about|services|products|produits|quantity|details|share|closed|ferm[ée]|"
                      r"monday|tuesday|wednesday|thursday|friday|saturday|sunday|lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche|welcome|bienvenue|head office|si[èe]ge social|"
                      r"mailing|showroom|warehouse|sponsors?|coordonn[ée]es|message|guarantee|training|courses|navigation|gallery|items?|usd|cad|information|info|comments?|download|map|browse|brands?)\b")
_A_STREET = re.compile(r"(?i)\b(?:street|st|avenue|ave|av|road|rd|drive|dr|boulevard|blvd|boul|rue|chemin|ch|chem|route|rte|highway|hwy|way|court|crt|ct|crescent|cres|lane|ln|place|pl|square|sq|trail|tr|terrace|"
                       r"parkway|pkwy|circle|cir|close|gate|grove|line|sideroad|concession|rang|mont[ée]e|c[ôo]te|all[ée]e|promenade|quai|plaza|centre|center|park|crossing|row|wharf|esplanade|po box|"
                       r"p\.o\. box|box|c\.p\.|case postale|rr|r\.r\.)\b\.?")
_A_DATE = re.compile(r"\d{1,2},\s+(?:19|20)\d{2}\b")


# 2026-11-12 (test set of the day: "dans la conception … à haute performance énergétique. Pont-Rouge, QC G3H2P9", "… Email info@x.ca
# Pointe-Claire, QC H9R 5N3"): with no street number in the quote, the address is the place in front of the province and postal code — not
# the page's sentence, label, mailbox or person before it. The place words are taken back from the province: capitalised words (and the
# small words of place names: de, du, la, sur …), at most four, stopping at a sentence's end, a label of the page, a mailbox or a number.
_PLACE_END = re.compile(r"[\s,(]*(?:A[BL]|BC|MB|N[BLSTU]|ON|PE|QC|Q[Cc]|SK|YT|Alberta|British Columbia|Colombie-Britannique|Manitoba|New Brunswick|Nouveau-Brunswick|"
                        r"Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Nova Scotia|Nouvelle-[ÉE]cosse|Ontario|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|"
                        r"Qu[ée]bec|Qc|Saskatchewan|Yukon|Northwest Territories|Nunavut)\.?\)?[\s,]*(?:(?:Canada|CAN)[\s,]+)?(?:[A-Za-z]\d[A-Za-z][\s-]?\d[A-Za-z]\d)?\s*(?:,?\s*(?:Canada|CA|CAN))?\s*$")
_PROV_WORD = {"ab": "AB", "alberta": "AB", "bc": "BC", "british columbia": "BC", "colombie britannique": "BC", "mb": "MB", "manitoba": "MB", "nb": "NB", "new brunswick": "NB",
              "nouveau brunswick": "NB", "nl": "NL", "newfoundland": "NL", "newfoundland and labrador": "NL", "terre neuve": "NL", "terre neuve et labrador": "NL", "ns": "NS",
              "nova scotia": "NS", "nouvelle ecosse": "NS", "on": "ON", "ontario": "ON", "pe": "PE", "prince edward island": "PE", "ile du prince edouard": "PE", "qc": "QC",
              "quebec": "QC", "sk": "SK", "saskatchewan": "SK", "yt": "YT", "yukon": "YT", "nt": "NT", "northwest territories": "NT", "nu": "NU", "nunavut": "NU"}
_PC_PROV = {"A": "NL", "B": "NS", "C": "PE", "E": "NB", "G": "QC", "H": "QC", "J": "QC", "K": "ON", "L": "ON", "M": "ON", "N": "ON", "P": "ON", "R": "MB", "S": "SK", "T": "AB", "V": "BC", "Y": "YT"}
_PLACE_SMALL = {"de", "du", "des", "la", "le", "les", "sur", "en", "lès", "d'", "of", "the", "and", "et", "upon", "on", "in", "-"}


def _place_only(t):
    m = _PLACE_END.search(t)
    if not m or m.start() == 0:
        return t
    head = t[:m.start()]
    # only when what stands in front of the place is the page's text — a mailbox, a label of the page, the end of a sentence — and no street
    # follows the last number (a street the first rule could not cut: "27 chemin des neiges", "B-245 McDermot Avenue (corner of …) Winnipeg",
    # "25, ch. de la Québécoise Saint-Adolphe-d'Howard"), nor does a number stand right before the place ("Box 61, Burwash Landing")
    if not ("@" in head or _A_LABEL.search(head) or re.search(r"[a-zà-ÿ]{2,}[.!?]\s+[A-ZÀ-Ý]", head)):
        return t
    ld = [m_.end() for m_ in re.finditer(r"\d", head)]
    if ld and (_A_STREET.search(head[ld[-1]:]) or re.search(r"\d", head[-25:]) or re.search(r"(?i)\b(?:P\.?\s?O\.?\s*Box|C\.?\s?P\.?|Case postale|Box)\s*#?\s*\d", head)):
        return t
    words, out = re.split(r"[\s,]+", head.strip()), []
    for w_ in reversed(words):
        abbr = w_.rstrip(".").lower() in ("st", "ste", "mt", "ft", "pt")
        if len(out) >= 4 or "@" in w_ or re.search(r"\d", w_) or _A_LABEL.fullmatch(w_.strip(",.:;()")) or (out and w_.endswith((".", ":", ";", "!", "?")) and not abbr):
            break
        if not (w_[:1].isupper() or w_.lower() in _PLACE_SMALL or re.fullmatch(r"[A-ZÀ-Ý][\w'’.-]*", w_.strip(",()"))):
            break
        out.insert(0, w_)
    while out and out[0].lower() in _PLACE_SMALL:
        out.pop(0)
    if not out:
        return t
    # the longest run of those words that is a place of the province (the GeoNames place names of tools/data/city_biller.tsv.gz): "Harry Walsh
    # WPM Novar" is Novar; a place the table does not know keeps at most its last two words
    import unicodedata as _ud
    tailtxt = t[m.start():]
    key = re.sub(r"[^a-z ]+", " ", _ud.normalize("NFKD", tailtxt).encode("ascii", "ignore").decode().lower())
    prov = next((v for k_, v in sorted(_PROV_WORD.items(), key=lambda kv: -len(kv[0])) if re.search(r"\b%s\b" % k_, key)), "")
    pcm = re.search(r"([A-Za-z])\d[A-Za-z][\s-]?\d[A-Za-z]\d", tailtxt)
    prov = prov or (_PC_PROV.get(pcm.group(1).upper(), "") if pcm else "")
    try:
        import by_location as _BL
        tab = _BL._cities()
        known = next((out[i:] for i in range(len(out)) if (prov, _BL.norm_city(" ".join(out[i:]).strip(",()"))) in tab), None) if prov else None
    except Exception:
        known = None
    out = known or out[-2:]
    return (" ".join(out) + tailtxt).strip(" ,.-–|:")


def address_from(quote):
    """the address part of a quote that ends at the postal code: from the street number on.
    2026-11-10 (first rule): a telephone number or a copyright year in front of the address was taken for the street number ("403.686.6444 1677 –
    93 Street SW" gave "6444 1677 – 93 Street SW"): the address starts after the last telephone number / copyright year of the quote, and a
    "P.O. Box" stays.
    2026-11-10 (second rule, measured on 82,492 printed buyer addresses: 3,792 carried words of the page in front — "00 Shop Made in KY Location &
    Hours Store Address 318 Monument Square …", "00 pm Friday 8:00 am - 3:00 pm Contact us Laird Orthodontics 62 Laird Dr. …"): opening hours are
    skipped like telephone numbers; of the numbers left, the street number is the first one that is followed by its street within a few words
    with no word of the page in between (Address, Hours, Contact, Shop …) — a price, a date, a count is not; "1585-M De Coulomb" starts at 1585."""
    q = quote or ""
    cut = max([m.end() for m in _A_PHONE.finditer(q)] + [m.end() for m in _A_YEAR.finditer(q)] + [m.end() for m in _A_RIGHTS.finditer(q)] + [m.end() for m in _A_TIME.finditer(q)] + [0])
    tail = q[cut:]
    ms = list(_A_START.finditer(tail))
    if not ms:
        return _place_only((tail if cut else q).strip(" ,.-–|:"))
    start = ms[-1].start()
    for i, m in enumerate(ms):
        nxt = ms[i + 1].start() if i + 1 < len(ms) else len(tail)
        rest = tail[m.start():]
        sw = _A_STREET.search(rest)
        near = bool(sw) and sw.start() <= 45
        if _A_DATE.match(rest) or (re.match(r"(?:19|20)\d{2}\b", rest) and not (sw and sw.start() <= 30)):
            continue  # "15, 2026 …", "2027 Sponsors …": a date or a year, unless a street follows it at once ("2026 Main Street")
        if near:
            between = rest[m.end() - m.start() - 1:sw.start()]  # the words between the number and the street word
            lab = _A_LABEL.search(between)
            # a page word standing right in front of the street word, with nothing after it, is the street's name: "450 N BRAND BLVD", "12 Park Lane"
            if not lab or (not between[lab.end():].strip(" .") and len(between.split()) <= 3 and not re.search(r"\d", between)):
                start = m.start()
                break
            continue
        if not _A_LABEL.search(tail[m.start():nxt]):
            start = m.start()
            break
    b = _A_BOX.search(tail[:start]) or _A_UNIT.search(tail[:start])
    if b:
        start = b.start()
    return tail[start:].strip(" ,.-–|:")


def find_tok(src, email):
    """Position of the address as a whole token (not the tail of a longer address such as rap@x for ap@x), else -1."""
    m = re.search(r"(?<![A-Za-z0-9._%+-])" + re.escape(email) + r"(?![A-Za-z0-9-]|\.[A-Za-z0-9])", src, re.I)
    return m.start() if m else -1


def quote_for(email, text, raw):
    for src in (text, re.sub(r"\s+", " ", raw)):
        i = find_tok(src, email)
        if i < 0:
            continue
        a = max(0, i - 140)
        q = src[a:a + 290]
        j, lo, hi = i - a, 0, len(q)
        for m in EMAIL_RX.finditer(q):  # keep other people's addresses out of the quote
            if m.start() == j:
                continue
            if m.end() <= j:
                lo = m.end()
            elif m.start() >= j + len(email):
                hi = m.start()
                break
        q = q[lo:hi].strip()
        if find_tok(q, email) >= 0:
            return q
    return ""


def classify(email, context, general=False):
    local = email.split("@")[0]
    if NOT_AP.search(local):
        return None
    if not AP_LOCAL.search(local):  # owner rule (2026-10-28): a general role mailbox only when no AP/procurement one
        if general and GENERAL.search(local) and EMAIL.match(email):
            return "general"
        return "role" if general == "any" and OTHER_ROLE.search(local) and EMAIL.match(email) else None
    if not EMAIL.match(email) or (PERSONAL.match(local) and not ROLE_HINT.search(local)):
        return None
    if re.search(r"(?<!manu)factur|invoice", local, re.I):
        return "invoice_submission"
    if re.search(r"payable|compt.*pay|^ap$|^ap[._-]|[._-]ap$|[._-]cap$", local, re.I):
        return "accounts_payable"
    if re.search(r"paiement|payment", local, re.I):
        return "supplier_payment"
    if re.search(r"fourniss|supplier|vendor|approv|achat|purchas|procure|acquisition", local, re.I):
        return "procurement"
    if CONTEXT_AP.search(context):  # finance@, comptabilite@, tresorerie@ ... when the page talks about invoicing
        return "accounts_payable"
    if re.search(r"compt|financ|tresor|tr[ée]sor|treasur|account", local, re.I) and not FIN_NOT.search(local):
        return "finance"  # finance / accounting department mailbox: written as general, ranked above other general mailboxes
    return None


AFF_STOP = {"www", "info", "ville", "city", "town", "county", "comte", "municipalite", "municipality", "canton", "paroisse", "village",
            "gouv", "gov", "quebec", "canada", "ontario", "alberta", "org", "com", "net", "mail", "email", "courriel", "the", "and",
            "des", "les", "del", "saint", "sainte", "regional", "district", "school", "board", "college", "university", "centre",
            "center", "service", "services", "public", "region", "nord", "sud", "est", "ouest", "north", "south", "east", "west"}
GENERIC_WORDS = {"municipalite", "municipality", "ville", "city", "town", "township", "county", "canton", "paroisse", "village",
                 "mrc", "regie", "de", "du", "des", "la", "le", "les", "of", "the", "and", "et", "d", "l"}
ABBR = {"st", "ste", "mun", "muni", "my", "ville", "city", "town", "villede", "cityof", "townof", "info", "mail",
        "qc", "on", "ab", "bc", "mb", "sk", "ns", "nb", "nl", "pe", "nt", "nu", "yk"}
GENERIC_MAIL = re.compile(r"(^|\.)(videotron|axion|bellnet|sympatico|globetrotter|cgocable|cooptel|xplornet|gmail|hotmail|outlook|live|"
                          r"yahoo|telus|shaw|eastlink|tellambton|derytele|b2b2c|icloud|bell|rogers|cogeco|xittel|sogetel|ccapcable|"
                          r"telupton|maskatel|tlb|tbaytel|execulink|wightman|persona|netcom)\.", re.I)
SAAS_AP = re.compile(r"(^|\.)(concursolutions|coupahost|basware|tungsten-network|esker|ariba|kofax|readsoft|invoicecapture)\.", re.I)
SHARED_SUFFIX = re.compile(r"\.(gouv\.qc|gov\.(ab|bc|mb|sk|nl|nt|nu|pe|yk|on)|gc|qc|on|ab|bc|mb|sk|ns|nb|nl|pe|nt|nu|yk)\.ca$|"
                           r"\.(ac|gov|co|org|nhs|police|ltd|plc|sch)\.uk$|\.(gov|edu|com|org|net)\.au$|\.gouv\.fr$|\.(k12|state)\.[a-z]{2}\.us$")


PORTAL_MAIL = {"canada.ca", "gc.ca", "gov.bc.ca", "alberta.ca", "gov.ab.ca", "quebec.ca", "gouv.qc.ca", "ontario.ca", "gov.on.ca",
               "gov.sk.ca", "saskatchewan.ca", "gov.mb.ca", "gov.nt.ca", "gov.nl.ca", "novascotia.ca", "gnb.ca", "gov.yk.ca", "yukon.ca",
               "gov.nu.ca", "gov.pe.ca", "gov.uk", "usa.gov"}
PORTAL_WORDS = {"canada", "canadian", "government", "gouvernement", "ministry", "ministere", "department", "affairs", "office",
                "services", "service", "agency", "agence", "national", "federal"}


def ascii_low(x):
    return unicodedata.normalize("NFKD", x or "").encode("ascii", "ignore").decode().lower()


def tokens(s):
    return {t for t in re.split(r"[^a-z0-9]+", ascii_low(s)) if len(t) >= 4 and t not in AFF_STOP}


GENERIC_SLD = set("gov govt gob gouv go gv gc ac edu sch school org or co com net nhs mil police ltd plc k12 state asn id health cri "
                  "parliament iwi nic res ernet muni info biz web me ne gen".split())  # second-level labels shared by many bodies
AU_STATE = {"vic", "nsw", "qld", "wa", "sa", "tas", "nt", "act"}
US_TYPE = {"ci", "co", "town", "vil", "twp", "k12", "state", "lib", "cc", "tec", "boro", "cog", "dst", "pvt"}
US_STATE = set("al ak az ar ca co ct de dc fl ga hi id il in ia ks ky la me md ma mi mn ms mo mt ne nv nh nj nm ny nc nd oh ok or pa ri "
               "sc sd tn tx ut vt va wa wv wi wy pr gu vi as mp".split())


def registrable(host):
    """the organisation's own domain: one label above a public / shared suffix (x.gouv.qc.ca, x.qc.ca, x.ac.uk, x.govt.nz,
    x.vic.gov.au, ci.x.co.us), else the last two labels"""
    host = host.lower().strip(".")
    host = host[4:] if host.startswith("www.") else host
    labels = host.split(".")
    if len(labels) >= 3:
        tld, sld = labels[-1], labels[-2]
        if tld == "us" and sld in US_STATE:  # ci.boulder.co.us, co.boulder.co.us, boulder.co.us, x.k12.ca.us
            return ".".join(labels[-4:] if len(labels) >= 4 and (labels[-3] in US_TYPE or labels[-4] in US_TYPE) else labels[-3:])
        if tld == "au" and len(labels) >= 4 and labels[-3] in AU_STATE and sld in ("gov", "edu"):
            return ".".join(labels[-4:])
    m = SHARED_SUFFIX.search(host)
    if m:  # one label above a shared suffix: x.gouv.qc.ca, x.ac.uk, x.qc.ca
        head = host[:m.start()].rsplit(".", 1)[-1]
        return head + m.group(0)
    if len(labels) >= 3 and len(labels[-1]) == 2 and labels[-2] in GENERIC_SLD:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


def same_org(email, site, org_name):
    """A mailbox of the buyer itself, not of a contractor, partner or another body named on its pages: same registrable
    domain as the site; a domain or mailbox name that spells the buyer's name, a distinctive word of it or its acronym
    (@saint-x.ca for saint-x.qc.ca, villagestpierre@videotron.ca, @mgerc-ceegm.gc.ca); or the Québec health network's
    shared mail domain."""
    local, _, d = ascii_low(email).partition("@")
    host = ascii_low(urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "")
    host = host[4:] if host.startswith("www.") else host
    if not d or not host:
        return True
    if d in PORTAL_MAIL:  # one mail domain for a whole government: only a mailbox named after this body counts
        loc, words = re.sub(r"[^a-z0-9]", "", local), [w for w in re.split(r"[^a-z0-9]+", ascii_low(org_name)) if w]
        acr = {"".join(w[0] for w in words if w not in GENERIC_WORDS),
               "".join(w[0] for w in words if w not in GENERIC_WORDS and w not in ("canada", "government", "gouvernement", "ministry", "ministere"))}
        return any(len(x) >= 3 and x in loc for x in acr) or any(t in loc for t in tokens(org_name) if len(t) >= 5 and t not in PORTAL_WORDS)
    if d == host or d.endswith("." + host) or host.endswith("." + d) or d.endswith("ssss.gouv.qc.ca"):
        return True
    if registrable(d) == registrable(host) and not SHARED_SUFFIX.fullmatch("." + registrable(d)):
        return True
    flat = lambda x: re.sub(r"[^a-z0-9]", "", ascii_low(x))
    strip = lambda x: re.sub(r"\.(gouv\.qc|gov\.[a-z]{2}|[a-z]{2})\.ca$|\.(ac|edu|gov|co|org|net|com)\.[a-z]{2}$|\.[a-z]+$", "", x)
    core, bcore, org = flat(strip(d)), flat(strip(host)), flat(org_name)
    pre = re.compile(r"^(townof|cityof|countyof|villede|municipalitede|municipalite|ville|city|town|county|mun|cegep|college|universite|regie|mrcde|mrc|css|cs)")
    core2 = pre.sub("", core)
    affix = {"", "ville", "villede", "cityof", "townof", "city", "town", "mun", "municipalite", "mrc", "cs", "css", "cegep", "college", "info"}
    if len(core2) >= 4 and (core2 in org or core2 in bcore or (len(bcore) >= 4 and bcore in core and core.replace(bcore, "", 1) in affix)):
        return True
    if len(core2) >= 3 and bcore.startswith(core2):
        return True
    words = [w for w in re.split(r"[^a-z0-9]+", ascii_low(org_name)) if w]
    small = {"de", "du", "des", "la", "le", "les", "of", "the", "and", "et", "d", "l"}
    acr = set()
    for ws in (words, [w for w in re.split(r"[^a-z0-9]+", ascii_low(re.split(r"\s[-–—(,]|\(", org_name)[0])) if w]):  # whole name, and its first part
        acr |= {"".join(w[0] for w in ws), "".join(w[0] for w in ws if w not in small), "".join(w[0] for w in ws if w not in GENERIC_WORDS)}
    acr.discard("")
    if any(len(w) >= 3 and core == w for w in words):  # the domain is one of the name's words, e.g. @olg.ca for "... (OLG)"
        return True
    if len(bcore) >= 2 and core != bcore and core.startswith(bcore) and len(core) - len(bcore) <= 2:
        return False  # a sibling body of the same system: @tamuk.edu (Kingsville) for tamu.edu, @uncc.edu for unc.edu
    for x in acr:
        if (len(x) >= 3 and (core == x or core.startswith(x) or (len(x) >= 4 and x in core))) or (len(x) >= 2 and core2 != core and core2 == x) \
                or (len(core) >= 4 and x.startswith(core)):
            return True
        if len(x) >= 3 and re.fullmatch(r"(qc|on|ab|bc|mb|sk|ns|nb|nl|pe|nt|nu|yk)" + re.escape(x), core):  # @bcldb.com
            return True
    orgwords = {w for w in words if len(w) >= 3}

    def explained(rem):  # what is left of a name once a distinctive word is removed must also come from the name
        for _ in range(12):
            if not rem:
                return True
            for w in sorted(orgwords | ABBR | small, key=len, reverse=True):
                if (len(w) >= 2 or w in ("d", "l")) and rem.startswith(w):
                    rem = rem[len(w):]
                    break
            else:
                return any(len(rem) >= 4 and w.startswith(rem) for w in orgwords) or any(len(rem) >= 1 and a.startswith(rem) for a in acr if a)
        return not rem
    loc = flat(local)
    distinct = {t for t in tokens(org_name) if len(t) >= 5}
    if re.search(r"invoic|(?<!manu)factur|payable|^ap[._-]|[._-]ap([._-]|$)", local) and (any(len(x) >= 3 and x in loc for x in acr) or any(t in loc for t in distinct)):
        return True  # e.g. cityofx_invoicecapture@<invoice service>.com named on the buyer's own page
    for t in distinct:
        if t in core and explained(core.replace(t, "", 1)):
            return True
        if t in loc and (GENERIC_MAIL.search(d) or SAAS_AP.search(d) or explained(loc.replace(t, "", 1))):
            return True
    return False


def links(raw, base):
    for m in re.finditer(r"(?is)<a\s[^>]*?href\s*=\s*[\"']([^\"'#>]+)[\"'][^>]*>(.*?)</a>", raw[:2_000_000]):
        href, label = m.group(1).strip(), visible(m.group(2))[:120]
        if href.lower().startswith(("mailto:", "tel:", "javascript:")):
            continue
        yield urllib.parse.urljoin(base, href), label



SITEMAP_AP = re.compile(r"factur|invoic|payable|comptes|fournisseur|supplier|vendor|purchas|procure|approvisionnement|achats|"
                        r"faire-affaire|doing-business|finance|accounting|comptab|paiement|payment|contact|nous-joindre", re.I)


def sitemap_urls(root, limit=15):
    """Pages about invoicing / suppliers / contact listed in the site's own sitemap (deep pages a home page never links)."""
    import gzip as _gz
    host = urllib.parse.urlparse(root).netloc
    rp = robots.get("%s://%s" % (urllib.parse.urlparse(root).scheme, host))
    maps = list((rp.site_maps() if rp and hasattr(rp, "site_maps") else None) or []) or [root.rstrip("/") + "/sitemap.xml", root.rstrip("/") + "/sitemap_index.xml"]
    seen_maps, found = set(), []
    while maps and len(seen_maps) < 6 and len(found) < limit:
        m = maps.pop(0)
        if m in seen_maps or not allowed(m):
            continue
        seen_maps.add(m)
        status, _, data, _ = fetch(m, 8_000_000)
        if status != 200 or not data:
            continue
        if data[:2] == b"\x1f\x8b":
            try:
                data = _gz.decompress(data)
            except Exception:
                continue
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace"))[:50000]:
            loc = html.unescape(loc)
            if loc.lower().split("?")[0].endswith((".xml", ".xml.gz")):
                if SITEMAP_AP.search(loc) or "page" in loc.lower() or len(maps) < 3:
                    maps.append(loc)
            elif SITEMAP_AP.search(urllib.parse.urlparse(loc).path):
                found.append(loc)
                if len(found) >= limit:
                    break
    # invoicing pages first, then supplier pages, then contact pages
    order = lambda u: (0 if re.search(r"factur|invoic|payable|comptes", u, re.I) else 1 if re.search(r"fournisseur|supplier|vendor|purchas|procure|approvisionnement|achats", u, re.I) else 2)
    return sorted(dict.fromkeys(found), key=order)


def crawl(task, max_pages, general=False):
    start = task["known_website"].strip()
    if not start.startswith("http"):
        start = "https://" + start
    host0 = (urllib.parse.urlparse(start).hostname or "").lower()
    if not host0:
        return "no_website", 0, []
    base = host0[4:] if host0.startswith("www.") else host0
    site = task["known_website"]  # the address a mailbox is judged against (same_org): the site as on file, or the site the organisation's home page lives on
    origin, pre, moved = "%s://%s" % (urllib.parse.urlparse(start).scheme, urllib.parse.urlparse(start).netloc), {}, ""
    if not task.get("_only_paths"):
        # 2026-11-11 — where the site answers, asked once before anything else (240 sites that had given "nothing_found" were read again):
        #  - 1 lead site in 9 never answered at the address on file and the seeded pages were asked of the same dead address one by one. fetch()
        #    turns to www. only when the bare name has no DNS record, and to plain http only after a TLS error: a bare name that resolves and
        #    refuses the connection (rbcbank.com) was never read. Its www. twin is asked once; a site with no answer at all ends here as
        #    "unreachable" (one or two requests instead of eight).
        #  - the pages that follow are asked of the address that answered (scheme and host of the home page's final URL), not of the one on file.
        #  - 1 site in 7 of the .ca registry class is a second name of an organisation whose site lives under another domain (osfs.ca ->
        #    flyos.ca, feuer.ca -> valenciarisk.com): the home page answers there, the mailbox printed there is that domain's, and same_org()
        #    refused it against the name on file. A caller that can tell an organisation's own second site from a platform or a parking page
        #    passes task["_moved_ok"](asked, final): when it says yes the site read is the one that answers, and task["_moved"] names it.
        res = fetch(start) if allowed(start) else None
        if res is not None and res[0] == 0 and not host0.startswith("www."):
            alt = "https://www.%s/" % base
            r2 = fetch(alt) if allowed(alt) else None
            if r2 is not None and r2[0] == 200:
                res, start = r2, alt
        if res is not None and res[0] == 0:
            root0 = origin + "/"
            r3 = fetch(root0) if (root0 != start and allowed(root0)) else None  # the address on file was a page inside the site: its home page
            if r3 is None or r3[0] == 0:
                return "unreachable", 1, []
            res, start = r3, root0
        if res is not None:
            pre[start.split("#")[0]] = res
            pf = urllib.parse.urlparse(res[3] or start)
            fb = (pf.hostname or "").lower()
            fb = fb[4:] if fb.startswith("www.") else fb
            if res[0] == 200 and fb and pf.scheme in ("http", "https"):
                if registrable(fb) == registrable(base):
                    origin = "%s://%s" % (pf.scheme, pf.netloc)
                elif task.get("_moved_ok") and task["_moved_ok"](start, res[3]):
                    origin, base, site, moved = "%s://%s" % (pf.scheme, pf.netloc), fb, "%s://%s/" % (pf.scheme, pf.netloc), res[3]
                    task["_moved"] = moved
    same = lambda h: bool(h) and (h.lower() == base or h.lower().endswith("." + base))
    heap, seen, pages, found = [(-100, 0, start), (-90, 0, origin + "/")], set(), 0, {}
    for i, path in enumerate(("contact", "contact-us", "nous-joindre", "suppliers", "fournisseurs")):  # common pages, often unlinked from home
        heap.append((-60 + i, 1, "%s/%s" % (origin, path)))
    for i, path in enumerate(task.get("_extra_paths") or ()):  # pages a caller knows this kind of site has (a Shopify store's /policies/contact-information)
        heap.append((-95 + i, 1, "%s/%s" % (origin, path.lstrip("/"))))
    if task.get("_only_paths"):  # a second look at a site already read: these pages and nothing else (depth 9: their links are not followed)
        heap = [(-95 + i, 9, "https://%s/%s" % (host0, path.lstrip("/"))) for i, path in enumerate(task["_only_paths"])]
    stop_found = task.get("_stop_found") or 0  # a caller that pays for every request: stop once this many pages are read and a mailbox better than a front-office role is on file
    root = origin + "/"
    if allowed(root) and not task.get("_no_sitemap") and not task.get("_only_paths"):  # the sitemap reveals deep invoicing / supplier pages (a store's sitemap lists products: a caller may skip it)
        for i, u in enumerate(sitemap_urls(root)):
            if (urllib.parse.urlparse(u).hostname or "").lower().endswith(base):
                heap.append((-98 + i, 1, u))
    heapq.heapify(heap)
    t_end = task.get("_deadline") or 0  # optional wall-clock budget for one site (tools/lead_crawl.py: a slow site must not hold a cloud runner)
    while heap and pages < max_pages and not (t_end and time.time() > t_end):
        if stop_found and pages >= stop_found and any(v[1] != "role" for v in found.values()):
            break
        neg, depth, url = heapq.heappop(heap)
        url = url.split("#")[0]
        if url in seen:
            continue
        seen.add(url)
        if not allowed(url):
            continue
        status, ctype, data, final = pre.pop(url, None) or fetch(url)
        page = stable_url(url, final)  # what a row and the page memory name; `final` still resolves the page's own links
        pages += 1
        stats["pages"] += 1
        head = data[:20000].decode("utf-8", "replace")
        if status in (401, 403, 429) or (status == 503 and BLOCK_RX.search(head)) or (pages <= 2 and BLOCK_RX.search(head) and len(data) < 30000):
            if pages <= 2:
                return "blocked", pages, []
            continue
        if status != 200 or not data:
            continue
        is_pdf = "pdf" in ctype.lower() or data[:5] == b"%PDF-"
        is_office = data[:2] == b"PK" and (OFFICE.search(url) or "officedocument" in ctype.lower())
        raw = pdf_text(data) if is_pdf else office_text(data) if is_office else quote_attrs(html.unescape(data.decode("utf-8", "replace")))
        is_pdf = is_pdf or is_office  # documents: no links to follow
        text = re.sub(r"\s+", " ", raw) if is_pdf else visible(raw)
        note_ap_page(task.get("buyer_key", ""), task.get("buyer_name", ""), task["known_website"], page, text, is_pdf)
        vis = page_emails(text)
        for e in page_emails(raw):
            if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or e in found:
                continue
            if e not in vis and any(v != e and v.endswith(e) for v in vis):
                continue  # only in a link target while the page shows a longer address (typo'd mailto: ccountspayable@ for accountspayable@)
            if not same_org(e, site, task.get("buyer_name", "")):
                continue
            q = quote_for(e, text, raw)
            i = find_tok(text, e)
            kind = classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, general)
            if kind and q:
                found[e] = (RANK[kind] * 100 + neg, kind, page, q)
        if is_pdf or depth >= (4 if max_pages > 30 else 3):  # the deeper pass (max_pages > 30) follows one more level: policies and bylaws sit behind an index page
            continue
        for link, label in links(raw, final):
            p = urllib.parse.urlparse(link)
            if p.scheme not in ("http", "https") or not same(p.hostname) or link in seen or SKIP_EXT.search(p.path):
                continue
            score = sum(w for rx, w in LINK_KW if rx.search(p.path + " " + p.query + " " + label))
            if (p.path.lower().endswith(".pdf") or OFFICE.search(p.path)) and score < 5:
                continue
            if score > 0:
                heapq.heappush(heap, (-score * 10 + depth, depth + 1, link))
    if any(v[1] != "role" for v in found.values()):  # a front-office role mailbox only when the site publishes nothing better
        found = {e: v for e, v in found.items() if v[1] != "role"}
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    if best and best[0][1][1] == "role":
        best = best[:1]
    rows = [{"task_id": task["task_id"], "buyer_key": task["buyer_key"], "org_name_as_found": task["buyer_name"],
             "ap_email": e, "ap_email_type": "general" if kind in ("finance", "role") else kind, "invoice_portal_url": "", "ap_phone": "", "invoice_mailing_address": "",
             "invoicing_requirements_summary": "", "applies_to": "whole_organisation", "evidence_url": url,
             "evidence_quote": q, "retrieved_date": TODAY, "status": "found",
             "queries_tried": "site crawl of %s (%d pages, robots.txt respected), no AI, no search engine" % (urllib.parse.urlparse(origin).hostname or host0, pages),
             "notes": "found on the buyer's own site by tools/ap_crawler.py" + (("; the organisation's site: https://%s/ answers at %s (redirect followed %s)" % (host0, moved, TODAY)) if moved else "") + ("; general role mailbox: no invoicing, AP or purchasing mailbox found on the site" if kind == "general" else
                                                                                "; front-office role mailbox (sales / service / orders / team): the site publishes no invoicing, AP, purchasing or general mailbox" if kind == "role" else
                                                                                "; finance / accounting department mailbox: no invoicing or AP mailbox published on the site" if kind == "finance" else "")} for e, (_, kind, url, q) in best]
    return ("found" if rows else "nothing_found"), pages, rows


def load_tasks():
    tasks, sites = {}, {}
    p = os.path.join(STATE, "websites.tsv")  # written by tools/site_finder.py for buyers without a known website
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            k, _, url = line.rstrip("\n").partition("\t")
            sites[k] = url.split("\t")[0]
    for f in sorted(glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv")):
        if "_verify_" in f:
            continue
        for r in csv.DictReader(open(f, encoding="utf-8-sig")):
            if not (r.get("known_website") or "").strip() and sites.get(r.get("buyer_key")):
                r["known_website"] = sites[r["buyer_key"]]
            if (r.get("known_website") or "").strip() and r.get("buyer_key") and r["buyer_key"] not in tasks:
                tasks[r["buyer_key"]] = r
    verified = set()  # buyers that already have a verified invoicing / AP mailbox (a general or purchasing one is not enough)
    try:  # 2026-11-10: team_buyers.jsonl.gz is a release asset (tools/state_io.py); a fresh checkout fetches the current version
        import state_io
        state_io.ensure("coord/results/team_buyers.jsonl.gz")
    except Exception:
        pass
    _tb = next((q for q in ("coord/results/team_buyers.jsonl.gz", "coord/results/team_buyers.jsonl") if os.path.exists(q)), None)
    if _tb:
        for line in (gzip.open(_tb, "rt", encoding="utf-8") if _tb.endswith(".gz") else open(_tb, encoding="utf-8")):
            o = json.loads(line)
            for e in (o.get("ap_contact_team") or {}).get("evidence") or []:
                if (e.get("verification") in ("verified", "cross_verified") and e.get("type") in ("invoice_submission", "accounts_payable", "supplier_payment")
                        and re.search(r"(?<!manu)factur|invoic|payable|compt\w*pay|^ap$|^ap[._-]|[._-]ap$|paiement|payment", (e.get("email") or "").split("@")[0], re.I)):
                    verified.add(o["buyer_key"])
                    break
    def size(r):
        try:
            return -int(float(r.get("contracts_in_dataset") or 0))
        except ValueError:
            return 0
    return sorted((t for k, t in tasks.items() if k not in verified), key=size)


def general_only():
    """Contract buyers (b:) and relationship buyers (lead:) for which every row found so far is a general mailbox."""
    best = {}
    if os.path.exists(OUT):
        for r in csv.DictReader(io.StringIO(open(OUT, encoding="utf-8", errors="replace").read().replace("\0", ""))):
            k = r.get("buyer_key") or ""
            if k.startswith(("b:", "lead:")) and r.get("ap_email"):
                g = r.get("ap_email_type") == "general" and "finance / accounting" not in (r.get("notes") or "")
                best[k] = best.get(k, True) and g
    return {k for k, g in best.items() if g}


def load_done():
    done = {}
    p = os.path.join(STATE, "done.tsv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 3:
                done[parts[0]] = (int(parts[1]), parts[2])
    return done


def save(task, pass_no, result, pages, rows):
    flush_ap_pages(task.get("buyer_key", ""), task.get("buyer_name", ""), task.get("known_website", ""))
    with out_lock:
        new = not os.path.exists(OUT)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            if new:
                w.writeheader()
            w.writerows(rows)
        with open(os.path.join(STATE, "done.tsv"), "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%s\t%d\t%s\n" % (task["buyer_key"], pass_no, result, pages, task["known_website"]))
        stats["sites"] += 1
        stats["rows"] += len(rows)
        stats["found_sites"] += bool(rows)
        stats["blocked"] += result == "blocked"


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True, timeout=300)


def sync(final=False):
    """Commit new rows and push to main (rebased on the latest main); retried on the next cycle when it fails."""
    with out_lock:
        if not git("status", "--porcelain", "data/incoming/claude").stdout.strip():
            return
        git("add", "data/incoming/claude")
        git("commit", "-q", "-m", "[claude] ap_crawler: buyer invoicing contacts (%d sites read, %d rows so far)"
            % (stats["sites"], stats["rows"]))
    for attempt in range(3):
        git("pull", "-q", "--rebase", "origin", "main")
        if git("push", "-q", "origin", "HEAD:main").returncode == 0:
            log("pushed", stats)
            return
        time.sleep(20 * (attempt + 1))
    log("push failed, will retry", stats)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=7)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-seconds", type=float, default=0)
    a = ap.parse_args()
    os.makedirs(STATE, exist_ok=True)
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    deadline = time.time() + (a.max_seconds or a.days * 86400)
    stop = threading.Event()

    def syncer():
        while not stop.wait(900):
            sync()
    threading.Thread(target=syncer, daemon=True).start()
    log("start", {"days": a.days, "workers": a.workers, "pdf": bool(shutil.which("pdftotext")) or "pypdf"})
    while time.time() < deadline:
        git("pull", "-q", "--rebase", "origin", "main")
        tasks, done = load_tasks(), load_done()
        if a.limit:
            tasks = tasks[:a.limit]
        upgrade = general_only()
        for pass_no, max_pages in ((4, 60), (1, 25), (2, 60), (3, 40)):  # pass 4 first: few sites, all contract / relationship buyers
            if pass_no == 4:  # buyers we only have a general mailbox for: read deeper for an invoicing / finance / purchasing one
                todo = [t for t in tasks if t["buyer_key"] in upgrade and done.get(t["buyer_key"], (0, ""))[0] < 4]
            else:
                todo = [t for t in tasks if (pass_no == 1 and t["buyer_key"] not in done) or
                        (pass_no > 1 and not t["buyer_key"].startswith(("wd:", "v:", "osm:", "lead:")) and done.get(t["buyer_key"], (0, ""))[0] < pass_no and done.get(t["buyer_key"], (0, ""))[1] == "nothing_found")]
            log("pass %d: %d sites" % (pass_no, len(todo)))

            def one(t, pass_no=pass_no, max_pages=max_pages):
                if time.time() >= deadline:
                    return
                try:
                    result, pages, rows = crawl(t, max_pages, general=(pass_no == 3 or (pass_no != 4 and t["buyer_key"].startswith(("wd:", "v:", "osm:", "lead:")))))
                except Exception as e:
                    result, pages, rows = "error:%s" % type(e).__name__, 0, []
                save(t, pass_no, result, pages, rows)
                done[t["buyer_key"]] = (pass_no, result)
                if stats["sites"] % 50 == 0:
                    log(stats)
            with ThreadPoolExecutor(a.workers) as ex:
                list(ex.map(one, todo))
            sync()
        if a.limit or a.max_seconds:
            break
        log("queue done; checking for new buyers in 1 hour", stats)
        stop.wait(min(3600, max(0, deadline - time.time())))
    stop.set()
    sync(final=True)
    log("finished", stats)


if __name__ == "__main__":
    main()

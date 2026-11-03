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
import argparse, csv, datetime, glob, heapq, html, io, json, os, re, shutil, subprocess, sys, threading, time, unicodedata
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import EMAIL, PERSONAL, ROLE_HINT  # same mailbox rules as the referee

STATE = os.path.expanduser("~/cch-crawler-state")
OUT = "data/incoming/claude/claude_buyer_ap_results_crawl01.csv"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
COLS = ["task_id", "buyer_key", "org_name_as_found", "ap_email", "ap_email_type", "invoice_portal_url", "ap_phone",
        "invoice_mailing_address", "invoicing_requirements_summary", "applies_to", "evidence_url", "evidence_quote",
        "retrieved_date", "status", "queries_tried", "notes"]
LINK_KW = [(re.compile(r"factur|invoice|payable|comptes?[-_ ]?(a|à)[-_ ]?payer|accounts?[-_ ]?pay|e-?invoic", re.I), 10),
           (re.compile(r"fournisseur|supplier|vendor|approvisionnement|purchas|procure|achats?\b|faire[-_ ]affaire|"
                       r"doing[-_ ]business|business[-_ ]with|appels?[-_ ]d|tender|bid", re.I), 6),
           (re.compile(r"financ|tr[ée]sor|treasur|comptab|accounting|paiement|payment", re.I), 5),
           (re.compile(r"nous[-_ ]joindre|contact|coordonn|directory|bottin|annuaire|services", re.I), 2)]
SKIP_EXT = re.compile(r"\.(jpe?g|png|gif|svg|webp|ico|mp4|mov|mp3|zip|doc|xls|pptx?|ics|css|js|xml|rss)(\?|$)", re.I)
OFFICE = re.compile(r"\.(docx|xlsx)(\?|$)", re.I)
EMAIL_RX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
AP_LOCAL = re.compile(r"factur|invoice|payable|compt|account|^ap$|^ap[._-]|[._-]ap$|[._-]cap$|financ|fourniss|"
                      r"supplier|vendor|approv|achat|purchas|procure|paiement|payment|tresor|treasur|acquisition", re.I)
NOT_AP = re.compile(r"plainte|complaint|recevable|receivable|billing|patient|usager|emploi|career|job|media|presse|press|"
                    r"benevol|volunteer|fondation|foundation|donat|webmaster|privacy|confidential|rh[._-]|^rh$|hr[._-]|^hr$", re.I)
CONTEXT_AP = re.compile(r"factur|invoice|payable|comptes? (à|a) payer|paiement|payment|fournisseur|supplier|vendor", re.I)
BLOCK_RX = re.compile(r"captcha|cf-challenge|challenge-platform|attention required|access denied|are you a robot", re.I)
FIN_NOT = re.compile(r"aid|bourse|scholar|tuition|student|etudiant|soutien|financement|funding|grant|subvention|invest|sustainab|"
                     r"bank|loan|pret|credit|donat|fondation|foundation|japan|china|europe|client", re.I)  # not the buyer's payables
RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "finance": 3, "procurement": 4, "general": 5}
GENERAL = re.compile(r"^(info|contact|contactus|reception|admin|administration|general|greffe|mairie|municipalite|townhall|cityhall|clerk|office|bureau|secretariat|accueil|hello|inquiries|enquiries|renseignements)([._-]|$)", re.I)
TODAY = datetime.date.today().isoformat()

host_lock, host_next, robots = threading.Lock(), {}, {}
out_lock, state_lock = threading.Lock(), threading.Lock()
stats = {"sites": 0, "pages": 0, "found_sites": 0, "rows": 0, "blocked": 0}


def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)


def fetch(url, limit=6_000_000):
    """(status, content_type, bytes, final_url); one request per second per host across all threads."""
    host = urllib.parse.urlparse(url).hostname or ""
    while True:
        with host_lock:
            wait = host_next.get(host, 0) - time.time()
            if wait <= 0:
                host_next[host] = time.time() + 1.0
                break
        time.sleep(min(wait, 1.0))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", b"", url
    except Exception:
        return 0, "", b"", url


def allowed(url):
    p = urllib.parse.urlparse(url)
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


def visible(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


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
        return "general" if general and GENERAL.search(local) and EMAIL.match(email) else None
    if not EMAIL.match(email) or (PERSONAL.match(local) and not ROLE_HINT.search(local)):
        return None
    if re.search(r"factur|invoice", local, re.I):
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


def registrable(host):
    m = SHARED_SUFFIX.search(host)
    if m:  # one label above a shared suffix: x.gouv.qc.ca, x.ac.uk, x.qc.ca
        head = host[:m.start()].rsplit(".", 1)[-1]
        return head + m.group(0)
    return ".".join(host.split(".")[-2:])


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
    if re.search(r"invoic|factur|payable|^ap[._-]|[._-]ap([._-]|$)", local) and (any(len(x) >= 3 and x in loc for x in acr) or any(t in loc for t in distinct)):
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
    same = lambda h: bool(h) and (h.lower() == base or h.lower().endswith("." + base))
    heap, seen, pages, found = [(-100, 0, start), (-90, 0, "https://%s/" % host0)], set(), 0, {}
    for i, path in enumerate(("contact", "contact-us", "nous-joindre", "suppliers", "fournisseurs")):  # common pages, often unlinked from home
        heap.append((-60 + i, 1, "https://%s/%s" % (host0, path)))
    root = "%s://%s/" % (urllib.parse.urlparse(start).scheme, urllib.parse.urlparse(start).netloc)
    if allowed(root):  # the sitemap reveals deep invoicing / supplier pages
        for i, u in enumerate(sitemap_urls(root)):
            if (urllib.parse.urlparse(u).hostname or "").lower().endswith(base):
                heap.append((-98 + i, 1, u))
    heapq.heapify(heap)
    while heap and pages < max_pages:
        neg, depth, url = heapq.heappop(heap)
        url = url.split("#")[0]
        if url in seen:
            continue
        seen.add(url)
        if not allowed(url):
            continue
        status, ctype, data, final = fetch(url)
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
        raw = pdf_text(data) if is_pdf else office_text(data) if is_office else html.unescape(data.decode("utf-8", "replace"))
        is_pdf = is_pdf or is_office  # documents: no links to follow
        text = re.sub(r"\s+", " ", raw) if is_pdf else visible(raw)
        vis = set(x.lower().rstrip(".") for x in EMAIL_RX.findall(text))
        for e in set(x.lower().rstrip(".") for x in EMAIL_RX.findall(raw)):
            if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or e in found:
                continue
            if e not in vis and any(v != e and v.endswith(e) for v in vis):
                continue  # only in a link target while the page shows a longer address (typo'd mailto: ccountspayable@ for accountspayable@)
            if not same_org(e, task["known_website"], task.get("buyer_name", "")):
                continue
            q = quote_for(e, text, raw)
            i = find_tok(text, e)
            kind = classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, general)
            if kind and q:
                found[e] = (RANK[kind] * 100 + neg, kind, final, q)
        if is_pdf or depth >= 3:
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
    best = sorted(found.items(), key=lambda kv: kv[1][0])[:3]
    rows = [{"task_id": task["task_id"], "buyer_key": task["buyer_key"], "org_name_as_found": task["buyer_name"],
             "ap_email": e, "ap_email_type": "general" if kind == "finance" else kind, "invoice_portal_url": "", "ap_phone": "", "invoice_mailing_address": "",
             "invoicing_requirements_summary": "", "applies_to": "whole_organisation", "evidence_url": url,
             "evidence_quote": q, "retrieved_date": TODAY, "status": "found",
             "queries_tried": "site crawl of %s (%d pages, robots.txt respected), no AI, no search engine" % (host0, pages),
             "notes": "found on the buyer's own site by tools/ap_crawler.py" + ("; general role mailbox: no invoicing, AP or purchasing mailbox found on the site" if kind == "general" else
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
    if os.path.exists("coord/results/team_buyers.jsonl"):
        for line in open("coord/results/team_buyers.jsonl", encoding="utf-8"):
            o = json.loads(line)
            for e in (o.get("ap_contact_team") or {}).get("evidence") or []:
                if (e.get("verification") in ("verified", "cross_verified") and e.get("type") in ("invoice_submission", "accounts_payable", "supplier_payment")
                        and re.search(r"factur|invoic|payable|compt\w*pay|^ap$|^ap[._-]|[._-]ap$|paiement|payment", (e.get("email") or "").split("@")[0], re.I)):
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

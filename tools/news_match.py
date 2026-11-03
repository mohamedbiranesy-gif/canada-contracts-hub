#!/usr/bin/env python3
"""Organisations WE ALREADY KNOW (buyers of the dataset, crawled organisations, lead buyers) named as customers in a
Canada-located vendor's own dated news release. No AI: dictionary matching.

tools/vendor_news.py parsed release TITLES for "<Buyer> selects <Vendor>" shapes: 51,000 releases gave 22 leads. Most
releases name the customer in a different shape ("<Vendor> announces X as new customer", "… awarded by the City of Y",
"<Vendor> to deliver Z for <Buyer>"). This tool instead looks for the names (or linked websites) of organisations we
already have — ~60,000 of them, with their websites and often their confirmed invoicing mailbox — in the title and the
first paragraphs of each release, next to a buying cue (selected, awarded, contract, deploys, customer, renews, …) and
away from the dropped cues (financing, acquisition, prize, partnership, donation, grant received …).

A match is emitted as a lead (tools/lead_scanner.py --bridge picks it up): buyer = the known organisation (its own name
and website, so rank.py attaches its confirmed mailbox and upgrades its row to a dated relationship), vendor = the
release's publisher, record date = the release date, evidence = the release URL + the sentence naming the buyer.
Vendor in Canada: the vendor list's own basis (contract data country field, Wikidata country, Canada-HQ list) AND, for
sites that are not .ca / not on the HQ list, a Canadian place line in the release itself (dateline or "headquartered in").

Vendors: the newsrooms that tools/vendor_news.py found releases on (its *.done files), Canadian listed companies from
Wikidata (TSX / TSXV / CSE / NEO), the Canada-HQ list. Polite: robots.txt, 1 request / second / site, identified UA.
  python3 tools/news_match.py [--workers 24] [--per-vendor 60] [--limit N] [--min-urls 3] [--only tsx|done|hq]
Output ~/cch-leads/socrata_news_match.jsonl (+ .done progress, .stats).
"""
import argparse, collections, csv, datetime, glob, hashlib, html, json, os, re, sys, threading, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL
import vendor_news as VN
from customer_stories import VENDORS as HQ_VENDORS

TODAY = datetime.date.today()
OLDEST = (TODAY - datetime.timedelta(days=3 * 365)).isoformat()
RECENT = (TODAY - datetime.timedelta(days=365)).isoformat()
LEADS = os.path.expanduser("~/cch-leads")
STATE = os.path.expanduser("~/cch-crawler-state")
REPO = os.path.expanduser("~/cch-crawler")
OUT = os.path.join(LEADS, "socrata_news_match.jsonl")
UA = CL.UA if hasattr(CL, "UA") else "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
lock = threading.Lock()

BUY = re.compile(r"\b(select(?:s|ed)|chose|chooses|chosen|picks|picked|taps|tapped|awarded|awards|contract(?:ed)?\s+(?:to|with|by|from)|"
                 r"purchase\s+order|orders?\s+(?:from|of|for)|ordered|renew(?:s|ed|al)|standardi[sz]e[sd]\s+on|goes\s+live|went\s+live|go\s+live|"
                 r"roll(?:s|ed)?\s+out|rollout|deploy(?:s|ed|ment|ing)|implement(?:s|ed|ation|ing)|adopt(?:s|ed|ion)|licen[cs]e[sd]|"
                 r"subscri(?:bed|ption)|(?:new|latest|newest|first)\s+(?:customer|client)|as\s+(?:a\s+)?(?:new\s+)?(?:customer|client)|"
                 r"customer\s+(?:win|agreement|contract)|to\s+(?:provide|supply|deliver|deploy|implement|equip|power|support|serve|build|"
                 r"design|modernize|modernise|digitize|digitise|operate|manage)|will\s+(?:provide|supply|deliver|deploy|implement|equip|build|"
                 r"design|operate)|has\s+(?:been\s+)?(?:selected|chosen|awarded|contracted|engaged|retained)|mandat[ée]?e?|choisi\w*|retenu\w*|"
                 r"octroy\w*|adjug\w*|attribu\w*|d[ée]ploie\w*|renouvel\w*|commande|livrera|fournira|r[ée]alisera|nouveau\s+client|"
                 r"nouvelle\s+cliente|contrat\s+(?:avec|de|du|pour|octroy|attribu|accord))\b", re.I)
DROP_T = re.compile(r"financ|credit facilit|\bloan|\bprêt|invest(?!igat)|raises?\b|funding|\bfund\b|grant(?!ed a contract)|subvention|"
                    r"acqui|merger|\bmerge|fusion|\bmou\b|memorand|letter of intent|\bloi\b|lettre d.intention|distribut|reseller|"
                    r"resell|revendeur|dealer|franchis|\bprize|\bprix\b|laur[ée]at|finalist|ranked|ranking|\btop \d|recogni|"
                    r"named (a|one|to)|appoint|nomm|hires|\bceo\b|\bcfo\b|board of directors|dividend|earnings|results|quarter|"
                    r"trimestr|webinar|conference|congr[èe]s|\bipo\b|shares|sponsor|donat|\bdon\b|charit|scholarship|bourse|"
                    r"internship|career fair|job fair|hackathon|study|survey|report finds|research shows|white ?paper|podcast|"
                    r"opinion|editorial|holiday|season.s greetings|notes\b|debenture|maturity|interest rate|offering|private placement|"
                    r"bought deal|warrant|prospectus|buyback|issuer bid|\bncib\b|annual meeting|\bagm\b|voting results|retire|passing|"
                    r"obituary|certification|\biso\b|arbitration|collective agreement|strike|union|lockout|layoff|guidance|outlook|"
                    r"fiscal|revenue|profit|loss|production|reserves|drill|assay|resource estimate|feasibility|permit|exploration|"
                    r"mineral|ounces|tonnes|wells?\b|pipeline capacity|open season|rate case|tariff|conversion|redemption|"
                    r"normal course|\bexchange\b|listing|delist|halt|material change|insider|governance|sustainability report|"
                    r"esg report|climate|emissions target|anniversary|celebrat|welcomes? (?:the )?(?:new )?(?:vice|president|chief|director|"
                    r"officer|members?)|joins? (?:the )?(?:board|team)|statement on|statement regarding|responds? to|update on", re.I)
GENERIC = {"the", "of", "and", "de", "du", "des", "la", "le", "les", "et", "l", "d", "for", "in", "a", "an", "inc", "ltd", "llc",
           "corp", "corporation", "co", "company", "limited", "ltee", "group", "groupe", "holdings", "international", "canada",
           "city", "town", "village", "county", "district", "municipality", "township", "region", "regional", "university",
           "college", "school", "schools", "board", "hospital", "health", "services", "service", "authority", "association",
           "society", "foundation", "centre", "center", "department", "ministry", "office", "government", "state", "county",
           "public", "national", "general", "community", "institute", "ville", "municipalite", "commission", "agency", "bank",
           "credit", "union", "federal", "province", "provincial", "council", "system", "systems", "solutions", "technologies"}
TYPE_WORD = re.compile(r"^(city|town|village|county|district|municipality|township|region|regional|ville|municipalite|rm|"
                       r"comte|mrc|conseil|county|parish|borough|hamlet|cree|first|nation)$")
PLATFORM_DOM = re.compile(r"(^|\.)(linkedin|facebook|twitter|x|instagram|youtube|vimeo|wikipedia|google|apple|amazon|bit|t|"
                          r"newswire|prnewswire|globenewswire|businesswire|cision|accesswire|marketwatch|yahoo|bloomberg|"
                          r"reuters|cnw|newsfilecorp|sedarplus|sec|tsx|nasdaq|nyse|crunchbase|zoominfo|glassdoor|indeed|"
                          r"wordpress|wix|squarespace|shopify|hubspot|mailchimp|eventbrite|zoom|microsoft|adobe|gov|canada|"
                          r"gc|quebec|ontario|alberta|bcgov|europa|un|who|w3|github|medium|substack|spotify|soundcloud)\.[a-z.]+$|"
                          r"^(gov\.uk|canada\.ca|gc\.ca|quebec\.ca|ontario\.ca|alberta\.ca|gov\.bc\.ca|europa\.eu|un\.org|who\.int)$")
norm = VN.norm


from ap_crawler import registrable as _reg


def registrable(host):
    h = CL.base(host) if host else ""
    return _reg(h) if h and "." in h else h


STOP = {"the", "of", "and", "de", "du", "des", "la", "le", "les", "et", "l", "d", "for", "in", "a", "an", "inc", "ltd", "llc", "corp",
        "corporation", "co", "company", "limited", "ltee", "plc", "sa", "ulc", "lp", "llp", "the"}
_COMMON = set()
for _wf in ("/usr/share/dict/words", "/usr/dict/words"):
    if os.path.exists(_wf):
        _COMMON = {w.strip().lower() for w in open(_wf, encoding="utf-8", errors="replace") if w.strip()}
        break


def sig_tokens(name):
    """the name's words without articles / legal suffixes (type words such as city, hospital, university stay)"""
    return [t for t in norm(name).split() if t not in STOP and len(t) > 1]


def distinctive(toks):
    """a phrase worth matching in running text: 2+ words with one that is not an everyday word, or 3+ words"""
    if len(toks) < 2:
        return False
    return len(toks) >= 3 or any(t not in _COMMON and not t.isdigit() for t in toks)


# ----------------------------------------------------------------------------------------------------------------
# the dictionary of organisations we know
def load_orgs():
    """name tokens -> org; registrable domain -> org. org = {name, website, key, grade}"""
    orgs, by_dom = {}, {}
    def add(name, website, key, grade=""):
        name = (name or "").strip()
        h = registrable((urllib.parse.urlparse(website if "//" in (website or "") else "https://" + (website or "")).hostname or "").lower().removeprefix("www."))
        if not name and not h:
            return
        o = orgs.get(key) or {"name": name, "website": website, "key": key, "grade": grade, "dom": h}
        if grade and (not o["grade"] or grade > o["grade"]):
            o["grade"] = grade
        orgs[key] = o
        if h and not PLATFORM_DOM.search(h) and not re.search(r"^(gmail|hotmail|outlook|yahoo|live|icloud)\.", h):
            by_dom.setdefault(h, o)
    rb = os.path.join(REPO, "coord/results/ranked/ranked_buyers.csv")
    if os.path.exists(rb):
        for r in csv.DictReader(open(rb, encoding="utf-8", errors="replace")):
            add(r["buyer"], r["buyer_website"], (r["keys"] or "").split("|")[0] or "rb:" + hashlib.sha1(r["buyer"].encode()).hexdigest()[:12], r.get("grade") or "")
    lf = os.path.join(REPO, "data/incoming/claude/claude_buyer_leads.csv")
    if os.path.exists(lf):
        for r in csv.DictReader(open(lf, encoding="utf-8", errors="replace")):
            add(r["buyer_name"], r.get("website") or "", r["buyer_key"])
    for f in sorted(glob.glob(os.path.join(REPO, "coord/tasks/claude/claude_buyer_ap_batch9*.csv"))) + \
             sorted(glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch9*.csv"))):
        try:
            for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
                if r.get("buyer_key", "").startswith(("v:", "osm:")):
                    continue  # vendors and shops: not buyers we target
                add(r.get("buyer_name") or "", r.get("known_website") or "", r.get("buyer_key") or "")
        except Exception:
            pass
    # name index: first significant token -> [(token tuple, org)]
    index = collections.defaultdict(list)
    for o in orgs.values():
        n = o["name"]
        if not n or re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", n.lower()):
            continue  # a bare domain is matched through links, not words
        toks = sig_tokens(n)
        if not distinctive(toks) or len(toks) > 9:
            continue  # one word, or only everyday words: not a name match
        index[toks[0]].append((tuple(toks), o, False))
    return orgs, by_dom, index


def find_names(text, index, limit=6):
    """organisations whose name phrase occurs in text: [(org, start, end)] on the normalised token stream"""
    toks, pos = [], []
    for m in re.finditer(r"[a-z0-9]+", text.lower()):
        toks.append(m.group(0)); pos.append((m.start(), m.end()))
    hits = {}
    for i, t in enumerate(toks):
        for phrase, o, typed in index.get(t, ()):
            n = len(phrase)
            if typed:
                if tuple(toks[i:i + n]) == phrase:
                    hits.setdefault(o["key"], (o, pos[i][0], pos[i + n - 1][1]))
            else:  # the significant words, in order, within a window that allows the generic words between them
                j, k, ok = i, 0, True
                while k < n and ok:
                    if j < len(toks) and toks[j] == phrase[k]:
                        k += 1; j += 1
                    elif j < len(toks) and toks[j] in STOP and j - i < n + 4:
                        j += 1
                    else:
                        ok = False
                if ok and k == n:
                    hits.setdefault(o["key"], (o, pos[i][0], pos[j - 1][1]))
        if len(hits) >= limit:
            break
    return list(hits.values())


def sentence_at(text, a, b):
    s = max(text.rfind(". ", 0, a), text.rfind("! ", 0, a), text.rfind("? ", 0, a), text.rfind("\n", 0, a)) + 1
    e = min(x for x in (text.find(". ", b), text.find("! ", b), text.find("? ", b), len(text)) if x >= 0)
    sent = text[s:e + 1].strip()
    if len(sent) > 300:
        lo = max(0, a - s - 120)
        sent = sent[lo:lo + 300]
    return sent


# ----------------------------------------------------------------------------------------------------------------
def wikidata_listed():
    """Canadian companies listed on TSX / TSXV / CSE / NEO (or 300+ employees) with a website, cached for a week."""
    cp = os.path.join(STATE, "wikidata_listed.json")
    if os.path.exists(cp) and time.time() - os.path.getmtime(cp) < 7 * 86400:
        return json.load(open(cp))
    q = """SELECT DISTINCT ?c ?cLabel ?web ?exLabel WHERE {
      ?c wdt:P17 wd:Q16 ; wdt:P856 ?web .
      { ?c wdt:P414 ?ex . } UNION { ?c wdt:P1128 ?emp . FILTER(?emp >= 300) }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr". }
    } LIMIT 25000"""
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.loads(r.read().decode("utf-8"))
    out = {}
    for b in data["results"]["bindings"]:
        web, name = b["web"]["value"], b["cLabel"]["value"]
        ex = (b.get("exLabel") or {}).get("value", "")
        if ex and not re.search(r"Toronto|TSX|Venture|Canadian Securities|NEO|Aequitas|Cboe Canada|Montreal", ex):
            continue
        h = registrable((urllib.parse.urlparse(web).hostname or "").lower().removeprefix("www."))
        if h and h not in out:
            out[h] = {"buyer_key": "wd:" + b["c"]["value"].rsplit("/", 1)[-1], "buyer_name": name, "known_website": "https://%s/" % h,
                      "basis": "wd", "exchange": ex}
    os.makedirs(STATE, exist_ok=True)
    json.dump(list(out.values()), open(cp, "w"))
    return list(out.values())


def vendors_from_done(min_urls):
    """vendor sites whose newsroom tools/vendor_news.py found releases on (site, urls, rows)"""
    seen, out = set(), []
    names = {}
    for f in glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90[234].csv")):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
            h = registrable((urllib.parse.urlparse(r.get("known_website") or "").hostname or "").lower().removeprefix("www."))
            if h:
                names.setdefault(h, (r.get("buyer_name") or "", r.get("buyer_key") or ""))
    for f in glob.glob(os.path.join(LEADS, "socrata_vnews_*.jsonl.done")):
        for line in open(f, encoding="utf-8", errors="replace"):
            p = line.rstrip("\n").split("\t")
            if len(p) < 2 or not p[1].isdigit() or int(p[1]) < min_urls:
                continue
            site = p[0]
            h = registrable((urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www."))
            if h in seen or not h:
                continue
            seen.add(h)
            nm, key = names.get(h, ("", ""))
            out.append({"buyer_key": key or "site:" + h, "buyer_name": nm, "known_website": site, "basis": (key.split(":")[0] if key else "site"), "urls": int(p[1])})
    out.sort(key=lambda v: -v["urls"])
    return out


NEWS_INDEX = ("news", "newsroom", "news-releases", "press", "press-releases", "media", "media-centre", "media-center", "blog",
              "nouvelles", "salle-de-presse", "communiques", "actualites", "investors/news", "about/news", "company/news", "en/news")
RSS_LINK = re.compile(r"(?is)<link[^>]+type\s*=\s*[\"']application/(?:rss|atom)\+xml[\"'][^>]*>")


def release_urls(site, cap):
    """Every release-looking URL of the site's newsroom (sitemaps, RSS, newsroom index pages), newest first.
    Unlike tools/vendor_news.py, the slug need not carry a deal word: the dictionary does the selecting."""
    from customer_stories import fetch_xml
    found = {}
    def keep(u, d=""):
        u = html.unescape(u).split("#")[0]
        p = urllib.parse.urlparse(u)
        if p.scheme not in ("http", "https") or CL.base(p.hostname) != CL.base(urllib.parse.urlparse(site).hostname):
            return
        if VN.NEWS_PATH.search(p.path) and not VN.NOT_SLUG.search(p.path) and len(p.path.strip("/").split("/")) >= 2:
            if not d:
                m = re.search(r"/(20\d\d)/(\d\d)/", p.path)
                d = "%s-%s-01" % m.groups() if m else ""
            if d and d < OLDEST:
                return
            if u not in found or (d and d > found[u]):
                found[u] = d
    robots = fetch_xml(urllib.parse.urljoin(site, "/robots.txt"), 300_000) or ""
    queue = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots) + [urllib.parse.urljoin(site, p) for p in
            ("/sitemap.xml", "/sitemap_index.xml", "/news-sitemap.xml", "/post-sitemap.xml", "/sitemap/sitemap.xml")]
    seen = set()
    while queue and len(seen) < 30 and len(found) < cap * 3:
        sm = queue.pop(0)
        if sm in seen or not CL.allowed(sm):
            continue
        seen.add(sm)
        txt = fetch_xml(sm)
        if not txt or "<" not in txt[:500]:
            continue
        index = "<sitemapindex" in txt[:3000].lower()
        for blk in re.findall(r"(?is)<(?:url|sitemap)>(.*?)</(?:url|sitemap)>", txt):
            loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", blk)
            if not loc:
                continue
            loc = html.unescape(loc.group(1))
            lm = re.search(r"<(?:lastmod|news:publication_date)>\s*(20\d\d-\d\d-\d\d)", blk)
            if index or loc.endswith((".xml", ".xml.gz")) or ".xml?" in loc:
                if lm and lm.group(1) < OLDEST:
                    continue
                if re.search(r"news|press|post|media|blog|actualit|nouvell|communiq|release|article|stor", loc, re.I):
                    queue.insert(0, loc)
                elif len(queue) < 40 and not re.search(r"product|produit|image|video|categor|tag|author|page-sitemap|attachment", loc, re.I):
                    queue.append(loc)
                continue
            keep(loc, lm.group(1) if lm else "")
    if len(found) < 10:  # RSS feed(s) and the newsroom index pages
        home, hfinal = CL.fetch(site) if CL.allowed(site) else ("", site)
        feeds = [urllib.parse.urljoin(hfinal, m.group(1)) for m in re.finditer(r"href\s*=\s*[\"']([^\"']+)", " ".join(RSS_LINK.findall(home or "")))]
        feeds += [urllib.parse.urljoin(site, p) for p in ("/feed", "/rss", "/rss.xml", "/news/rss", "/news/feed", "/feed/", "/blog/feed")]
        for fu in feeds[:6]:
            if not CL.allowed(fu):
                continue
            txt = fetch_xml(fu, 3_000_000)
            if not txt or "<item" not in txt and "<entry" not in txt:
                continue
            for blk in re.findall(r"(?is)<(?:item|entry)>(.*?)</(?:item|entry)>", txt):
                lk = re.search(r"<link>\s*([^<\s]+)", blk) or re.search(r"<link[^>]+href\s*=\s*[\"']([^\"']+)", blk)
                dt = re.search(r"(20\d\d)-(\d\d)-(\d\d)", blk) or None
                pd = re.search(r"(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+(20\d\d)", blk)
                d = "-".join(dt.groups()) if dt else ("%s-%02d-%02d" % (pd.group(3), ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"].index(pd.group(2).lower()[:3]) + 1, int(pd.group(1)))) if pd else ""
                if lk:
                    u = html.unescape(lk.group(1)).strip()
                    p = urllib.parse.urlparse(u)
                    if CL.base(p.hostname) == CL.base(urllib.parse.urlparse(site).hostname) and not VN.NOT_SLUG.search(p.path) and (not d or d >= OLDEST):
                        found.setdefault(u.split("#")[0], d)
            if len(found) >= 10:
                break
        tried = 0
        for pth in NEWS_INDEX:
            if len(found) >= 10 or tried >= 4:
                break
            u = urllib.parse.urljoin(site, "/" + pth)
            if not CL.allowed(u):
                continue
            page, final = CL.fetch(u)
            tried += 1
            if not page or len(page) < 2000:
                continue
            for href, label in CL.anchors(page, final):
                keep(href)
            for href in re.findall(r"href\s*=\s*[\"']([^\"']+)[\"'][^>]*>\s*(?:next|older|more|suivant|\d+)\s*<", page, re.I)[:2]:
                p2, f2 = CL.fetch(urllib.parse.urljoin(final, href)) if CL.allowed(urllib.parse.urljoin(final, href)) else ("", "")
                for h2, l2 in CL.anchors(p2 or "", f2 or final):
                    keep(h2)
    best = {}
    for u, d in found.items():  # one URL per release across language copies, English first
        p = urllib.parse.urlparse(u).path
        m = re.match(r"^/([a-z]{2}(?:[-_][a-zA-Z]{2})?)(/.*)$", p)
        loc, rest = (m.group(1).lower(), m.group(2)) if m else ("", p)
        rank = 0 if loc in ("", "en", "en-us", "en-ca") else 1
        k = rest.rstrip("/").lower()
        if k not in best or rank < best[k][0]:
            best[k] = (rank, d, u)
    return [u for _, d, u in sorted(best.values(), key=lambda x: x[1], reverse=True)][:cap]


def one(v, orgs, by_dom, index, cap, stats, done):
    site = v["known_website"]
    vhost = registrable((urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www."))
    if not vhost or vhost in done or vhost in by_dom and v["basis"] not in ("v", "wd", "hq"):
        return
    basis = v.get("basis") or "site"
    vname = v.get("buyer_name") or vhost
    try:
        urls = release_urls(site, cap) if CL.allowed(site) else []
    except Exception:
        urls = []
    rows, n_read = {}, 0
    for u in urls:
        if not CL.allowed(u):
            continue
        page, final = CL.fetch(u)
        if not page:
            continue
        n_read += 1
        title = VN.page_title(page)
        if not title or DROP_T.search(title):
            continue
        d = VN.page_date(page, final)
        if not d or d < OLDEST or d > TODAY.isoformat():
            continue
        text = VN.body_text(page)
        head = title + ". " + text[:2500]
        place = VN.CANADA_LINE.search(text[:4000]) or VN.CANADA_HQ.search(text)
        place = re.sub(r"\s+", " ", text[max(0, place.start() - 40):place.end() + 40]).strip()[:200] if place else ""
        if basis != "hq" and not vhost.endswith(".ca") and not place:
            stats["no_canada_line"] += 1
            continue
        linked = set()
        for href, label in CL.anchors(page, final):  # organisations linked from the release (confirms a name match)
            h = registrable((urllib.parse.urlparse(href).hostname or "").lower().removeprefix("www."))
            if h and h != vhost and not h.endswith("." + vhost) and h in by_dom:
                linked.add(by_dom[h]["key"])
        for o, a, b in find_names(head, index):
            how = "name+link" if o["key"] in linked else "name"
            od = o.get("dom") or ""
            if od and (od == vhost or od.endswith("." + vhost) or vhost.endswith("." + od)):
                continue  # the vendor itself
            ot, vt = set(sig_tokens(o["name"])), set(sig_tokens(vname)) | set(sig_tokens(vhost.split(".")[0]))
            if ot and vt and (ot <= vt or vt <= ot or (len(ot & vt) >= 2)):
                continue  # the vendor itself (or its own group company)
            if a < 160 and re.match(r"\s*,\s*(?:ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|Ont|Que|Alta|Canada|[A-Z]{2})\b", head[b:b + 12]):
                continue  # the dateline (MISSISSAUGA, ON, …) names the vendor's city, not a buyer
            sent = sentence_at(head, a, b)
            cue = BUY.search(sent)
            if not cue or abs(cue.start() - (a - max(0, head.rfind(sent, 0, a + 1)))) > 220:
                stats["no_buy_cue"] += 1
                with lock, open(OUT + ".nearmiss", "a", encoding="utf-8") as nf:
                    nf.write("%s\t%s\t%s\t%s\t%s\n" % (d, o["name"][:40], vname[:30], title[:90].replace("\t", " "), sent[:220].replace("\t", " ")))
                continue
            if DROP_T.search(sent):
                continue
            if norm(o["name"]) not in norm(sent) and not all(t in norm(sent) for t in sig_tokens(o["name"])):
                sent = head[max(0, a - 120):b + 160]
            k = o["key"]
            if k in rows and rows[k]["row"]["record_date"] >= d:
                continue
            rows[k] = {"platform": "news_match", "domain": od or registrable((urllib.parse.urlparse(final).hostname or "")), "dataset_id": final,
                       "dataset": "named as a customer in a Canada-located vendor's own news release (%s)" % d, "dataset_url": final,
                       "publisher": o["name"] or od, "buyer_unit": "", "website": o["website"] or ("https://%s/" % od if od else ""),
                       "vendor": vname, "canada_field": "own news release of the vendor (%s)" % VN.BASIS.get(basis, basis),
                       "canada_value": place or vhost,
                       "row": {"record_date": d, "news_date": d, "title": title[:300], "quote": sent[:300], "match": how,
                               "org_key": k, "org_grade": o.get("grade", ""), "vendor_key": v["buyer_key"], "vendor_site": site,
                               "retrieved": TODAY.isoformat()}}
            stats["recent" if d >= RECENT else "older"] += 1
            if o.get("grade") == "4":
                stats["ap_grade_org"] += 1
    with lock:
        if rows:
            with open(OUT, "a", encoding="utf-8") as f:
                for r in rows.values():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(OUT + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\t%d\n" % (site, len(urls), n_read, len(rows)))
        stats["vendors"] += 1; stats["releases"] += n_read; stats["leads"] += len(rows)
        if stats["vendors"] % 50 == 0:
            print("%s %s" % (datetime.datetime.now().strftime("%H:%M"), dict(stats)), flush=True)
            json.dump(dict(stats), open(OUT + ".stats", "w"))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--workers", type=int, default=24)
    a.add_argument("--per-vendor", type=int, default=60)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--min-urls", type=int, default=3)
    a.add_argument("--only", default="")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    orgs, by_dom, index = load_orgs()
    print("organisations: %d (domains %d, name phrases %d)" % (len(orgs), len(by_dom), sum(len(v) for v in index.values())), flush=True)
    done = set()
    if os.path.exists(OUT + ".done"):
        for l in open(OUT + ".done", encoding="utf-8"):
            done.add(registrable((urllib.parse.urlparse(l.split("\t")[0]).hostname or "").lower().removeprefix("www.")))
    vendors, seen = [], set()
    groups = []
    if a.only in ("", "tsx"):
        try:
            groups.append(wikidata_listed())
        except Exception as ex:
            print("wikidata: %s" % ex, flush=True)
    if a.only in ("", "hq"):
        groups.append([{"buyer_key": "hq:" + h, "buyer_name": "", "known_website": "https://www.%s/" % h, "basis": "hq"} for h in dict.fromkeys(HQ_VENDORS)])
    if a.only in ("", "done"):
        groups.append(vendors_from_done(a.min_urls))
    for g in groups:
        for v in g:
            h = registrable((urllib.parse.urlparse(v["known_website"]).hostname or "").lower().removeprefix("www."))
            if h and h not in seen:
                seen.add(h); vendors.append(v)
    if a.limit:
        vendors = vendors[:a.limit]
    print("vendors: %d (%d done before)" % (len(vendors), len(done)), flush=True)
    stats = collections.Counter()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, orgs, by_dom, index, a.per_vendor, stats, done), vendors))
    json.dump(dict(stats), open(OUT + ".stats", "w"))
    print("finished %s" % dict(stats), flush=True)


if __name__ == "__main__":
    main()

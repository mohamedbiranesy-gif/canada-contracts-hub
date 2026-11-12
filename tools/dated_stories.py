#!/usr/bin/env python3
"""Dated private buyers from the customer stories that Canada-located vendors publish on their own sites. No AI.

Source: each vendor's own customer-story / case-study pages (paths /customers/<slug>, /case-studies/<slug>,
/customer-stories/<slug>, /success-stories/<slug>, /clients/<slug>, /etudes-de-cas/<slug>, ... as in
tools/customer_stories.py), found in the vendor's sitemaps (robots.txt Sitemap lines, else /sitemap.xml,
/sitemap_index.xml, /wp-sitemap.xml; indexes and gzip followed, story sitemaps first) or, without a readable sitemap, on
the customers listing page linked from the home page.
Vendors: the crawler's local lists on the Mac, ~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch903.csv (verified
contract vendors), batch904 (OpenStreetMap), batch902 (Wikidata), column known_website, plus customer_stories.VENDORS
(Canada-HQ list). One worker per vendor site; sharded by sha1(host) % --of.
Canada filter, required per vendor before any story page is read (the proof text is kept as canada_value):
  the story site is .ca  ->  ".ca site";  OR the vendor is in customer_stories.VENDORS  ->  "Canada-HQ list";
  OR its home page or contact page shows a Canadian postal code in the visible text (with a province / "Canada" next to
  it unless written "A1A 1A1") and no more distinct US ZIP addresses than Canadian postal codes  ->  that address line.
Fields used per story page: og:title / <title> / <h1> (customer name, customer_stories.name_from, checked against a list
of generic words); the page's OWN published date, in this order: meta article:published_time / og:published_time /
datePublished / pubdate / publish_date / publication_date / dc.date(.issued) / name="date", JSON-LD "datePublished",
a <time> marked published / entry-date, a /YYYY/MM/ URL, a visible "Published on ..." / "Publié le ..." line, the first
<time> tag that is not an "updated" / "modified" one. Never a modified date; the sitemap lastmod is only used to read the
newest stories first and to skip stories whose lastmod is older than the cutoff (published <= last modified).
The customer's website: an external link in the story's main content whose domain spells the customer's name (prefix,
non-generic word, acronym) or whose label is in both the title and the URL slug; else Wikidata (exact label / alias,
official website P856; a cross-process lock keeps it at most 1 request/second for all shards together).
Kept: stories dated on or after 2023-11-02 (--since), one line per (customer website, vendor), the newest story kept.
Customers named but without a website are logged to ~/cch-leads/dstories_nosite_<I>.jsonl, not kept.
Output (picked up by tools/lead_scanner.py --bridge; row.record_date = row.story_date):
  ~/cch-leads/socrata_dstories_<I>.jsonl ; progress <same>.done (vendor site, story URLs, pages read, rows, proof).
Polite: robots.txt obeyed (401/403 on robots.txt = disallow all), one request per second per host, identified user
agent, 401/403/429 or a bot-check page stops that vendor.
  python3 tools/dated_stories.py --shard I --of N [--workers 32] [--per-vendor 40] [--limit N] [--fresh]
  python3 tools/dated_stories.py --test 60     (20 Canada-HQ vendors + 40 sampled from the lists -> ~/cch-leads/dstories_test/)
Counts seen: see notes in the log ~/cch-crawler-state/dstories_<I>.log (final "finished" line per shard).
"""
import argparse, collections, csv, datetime, fcntl, gzip, hashlib, html, json, os, random, re, sys, threading, time
import urllib.error, urllib.parse, urllib.request, urllib.robotparser
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL
from customer_stories import STORY, NOT_STORY, VENDORS as HQ_VENDORS, name_from

UA = CL.UA
LEADS = CL.LEADS
TODAY = datetime.date.today().isoformat()
LAST12 = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
WD_API = "https://www.wikidata.org/w/api.php?"
HQ = set(HQ_VENDORS)

# ---------------------------------------------------------------- polite fetching (1 request / second / host)
_guard = threading.Lock()
_host_locks, _last, _robots, _robots_txt = {}, {}, {}, {}


def _wait(host):
    with _guard:
        lk = _host_locks.get(host)
        if lk is None:
            lk = _host_locks[host] = threading.Lock()
    with lk:
        w = _last.get(host, 0) + 1.0 - time.time()
        if w > 0:
            time.sleep(w)
        _last[host] = time.time()


def get(url, limit=3_000_000, want_html=True):
    """(text, final url, status). status 0 = network error; text None when not HTML (want_html) or on error."""
    _wait((urllib.parse.urlparse(url).hostname or "").lower())
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-CA,en;q=0.8,fr-CA;q=0.6"})
        with urllib.request.urlopen(req, timeout=20) as r:
            ct = (r.headers.get("content-type") or "").lower()
            final = r.geturl()
            if want_html and ct and "html" not in ct:
                return None, final, r.status
            data = r.read(limit)
        if data[:2] == b"\x1f\x8b":
            try:
                data = gzip.decompress(data)
            except Exception:
                return None, final, 0
        return data.decode("utf-8", "replace"), final, 200
    except urllib.error.HTTPError as e:
        return None, url, e.code
    except Exception:
        return None, url, 0


def robots_text(url):
    p = urllib.parse.urlparse(url)
    key = "%s://%s" % (p.scheme, p.netloc)
    with _guard:
        if key in _robots:
            return _robots_txt.get(key, "")
    txt, _, code = get(key + "/robots.txt", 300_000, want_html=False)
    rp = urllib.robotparser.RobotFileParser()
    if code in (401, 403):
        rp.disallow_all = True
        txt = ""
    else:
        txt = txt if txt and "<html" not in txt[:600].lower() else ""
        rp.parse(txt.lstrip("\ufeff").splitlines())
    with _guard:
        _robots[key], _robots_txt[key] = rp, txt
    return txt


def allowed(url):
    robots_text(url)
    p = urllib.parse.urlparse(url)
    try:
        return _robots["%s://%s" % (p.scheme, p.netloc)].can_fetch(UA, url)
    except Exception:
        return True


# ---------------------------------------------------------------- text helpers
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
squash = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
LEGAL = re.compile(r"\b(inc|incorporated|ltd|limited|ltee|ltée|corp|corporation|co|company|llc|plc|sa|gmbh|ag|holdings?|"
                   r"the|of|and|for|de|du|des|la|le|les|et)\b\.?", re.I)
GENERIC_WORDS = set("""city town county state province health healthcare hospital hospitals university college school
schools district region regional services service group global national international canada canadian america american
north south east west united general public community foundation society association council department ministry
government solutions systems technologies technology partners capital energy power bank insurance financial finance
network digital media marketing retail foods food brands company consulting management medical care home homes club
sports credit union trust realty properties group world best first new""".split())
BAD_NAME = re.compile(r"^(home|blog|news|resources?|customers?|clients?|case|success|stories|story|testimonials?|references?|"
                      r"about|contact|products?|solutions?|services?|industr\w*|page|404|not found|error|access denied|"
                      r"just a moment|attention required|welcome|overview|introduction|watch|video|webinar|download|read|"
                      r"learn|discover|get|see|meet|inside|behind|from|with|by|for|in|on|at|to|a|an|this|these|that|how|"
                      r"why|what|when|where|who|reducing|increasing|improving|building|transforming|scaling|driving|saving|"
                      r"streamlining|automating|boosting|growing|creating|delivering|enabling|empowering|modernizing|"
                      r"modernising|accelerating|helping|making|bringing|turning|unlocking|powering|optimizing|"
                      r"optimising|maximizing|simplifying|supporting|achieving|leveraging|using|elevating|"
                      r"revolutionizing|enhancing|cutting|managing|digital|data|cloud|ai|seamless|smarter|better|faster|"
                      r"\d)\b", re.I)
BLOCKED_TITLE = re.compile(r"just a moment|attention required|access denied|are you a robot|captcha|security check|"
                           r"request rejected|403 forbidden|bot verification|pardon our interruption", re.I)
SKIP = re.compile(r"facebook|linkedin|twitter|x\.com$|instagram|youtube|youtu\.be|tiktok|pinterest|google|goo\.gl|"
                  r"apple\.com|microsoft|wordpress|wix|squarespace|shopify|godaddy|w3\.org|schema\.org|bbb\.org|iso\.org|"
                  r"adobe|mailchimp|hubspot|hs-sites|hsforms|vimeo|vidyard|wistia|flickr|yelp|tripadvisor|amazon|gstatic|"
                  r"cloudflare|cloudfront|akamai|azureedge|jquery|bootstrap|fontawesome|gravatar|wikipedia|wikimedia|"
                  r"creativecommons|github|zoom\.us|calendly|bit\.ly|addthis|sharethis|marketo|pardot|force\.com|"
                  r"typeform|g2\.com|capterra|getapp|trustradius|softwareadvice|gartner|forrester|medium\.com|substack|"
                  r"newswire|businesswire|cision|issuu|scribd|slideshare|dropbox|box\.com|sharepoint|office\.com|"
                  r"imgix|cloudinary|unsplash|gettyimages|shutterstock|zendesk|intercom|drift\.com|6sense|bing\.com|"
                  r"t\.co$|lnkd\.in|feedburner|disqus|eventbrite|on24|zoominfo|crunchbase|bloomberg|reuters|forbes|"
                  r"techcrunch|cnn\.com|cbc\.ca|theglobeandmail|financialpost|nationalpost|ctvnews|wsj\.com|nytimes|"
                  r"onetrust|cookiebot|cookielaw|trustarc|openstreetmap|archive\.org|ytimg|spotify|podcasts|"
                  r"statuspage|sentry|segment|optimizely|doubleclick|clarity\.ms|hotjar|cdn\.", re.I)
MULTI_SLD = {"co", "com", "org", "gov", "ac", "net", "edu", "gc", "qc", "on", "bc", "ab", "mb", "sk", "ns", "nb", "nl", "pe"}


def sld(host):
    parts = CL.base(host).split(".")
    if len(parts) >= 3 and parts[-2] in MULTI_SLD:
        return parts[-3]
    return parts[-2] if len(parts) >= 2 else parts[0]


CDN_SUB = re.compile(r"^(static\w*|cdn\d*|assets?\d*|media|images?|img\d*|files?|content|uploads?|s3|downloads?|go|info|lp|"
                     r"pages|email|click|links?)$", re.I)


def site_host(h):
    """The organisation's own host for a link on a CDN-like subdomain (staticctf.ubisoft.com -> ubisoft.com)."""
    parts = h.split(".")
    n = 3 if len(parts) >= 3 and parts[-2] in MULTI_SLD else 2
    return ".".join(parts[-n:]) if len(parts) > n and CDN_SUB.match(parts[0]) else h


def name_in_title(lab, title):
    """The words of the title that spell the domain label ("Ubisoft" for ubisoft.com), else ''."""
    toks = re.findall(r"[A-Za-zÀ-ÿ0-9&'’.-]+", title or "")
    for i in range(len(toks)):
        for j in range(i + 1, min(i + 5, len(toks)) + 1):
            if squash(" ".join(toks[i:j])) == lab:
                return " ".join(toks[i:j]).strip(".-'’")
    return ""


def visible(page):
    page = re.sub(r"(?is)<(script|style|noscript|svg|template|head)\b[^>]*>.*?</\1>", " ", page[:2_000_000])
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", page)))


def name_words(name):
    return [w for w in norm(LEGAL.sub(" ", name or "")).split() if w]


def name_match(host, name):
    """The domain spells the name: its label is a prefix of the squashed name (>= 4), a non-generic word of it (>= 5),
    its acronym (>= 3), or contains the whole squashed name (>= 4)."""
    words = name_words(name)
    if not words:
        return False
    sq, acr, lab = "".join(words), "".join(w[0] for w in words), squash(sld(host))
    if len(lab) < 3:
        return False
    return (lab == sq or (len(lab) >= 4 and sq.startswith(lab)) or (len(lab) >= 5 and lab in words and lab not in GENERIC_WORDS)
            or (len(acr) >= 3 and lab == acr) or (len(sq) >= 4 and sq in lab))


# ---------------------------------------------------------------- Canada proof of the vendor
PROV = (r"(?:ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU|Ont\.?|Qu[ée]\.?|B\.C\.|Alta\.?|Man\.?|Sask\.?|N\.S\.|N\.B\.|"
        r"Ontario|Qu[ée]bec|British Columbia|Colombie[- ]Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|"
        r"Nouvelle[- ][ÉE]cosse|New Brunswick|Nouveau[- ]Brunswick|Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|"
        r"Prince Edward Island|[ÎI]le[- ]du[- ]Prince[- ][ÉE]douard|Yukon|Northwest Territories|Nunavut|Canada)")
POSTAL = re.compile(r"\b([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z])([ \u00a0-]?)(\d[ABCEGHJ-NPRSTV-Z]\d)\b")
PROV_BEFORE = re.compile(r"\b" + PROV + r"\b[\s,.)]*$")
US_ZIP = re.compile(r"\b(?:A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|"
                    r"T[NX]|UT|V[AT]|W[AIVY]|Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|"
                    r"Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|"
                    r"Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|"
                    r"New Jersey|New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|"
                    r"Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|"
                    r"West Virginia|Wisconsin|Wyoming)\.?,?\s+(\d{5})(?:-\d{4})?\b")
CONTACT_PATH = re.compile(r"contact|nous-joindre|joindre|contactez|coordonn|locations?\b|offices?\b|bureaux|find-us|"
                          r"nous-trouver|about|a-propos|qui-sommes", re.I)
CONTACT_LABEL = re.compile(r"\b(contact|nous joindre|joignez|contactez|locations|our offices|nos bureaux|find us)", re.I)


def canada_postal(text):
    """(address line with the first Canadian postal code, distinct Canadian codes, distinct US ZIP addresses)."""
    ca, line = set(), ""
    for m in POSTAL.finditer(text):
        before, after = text[max(0, m.start() - 60):m.start()], text[m.end():m.end() + 25]
        context = PROV_BEFORE.search(before) or re.match(r"[\s,.]*Canada\b", after)
        if m.group(2) != " " and m.group(2) != "\u00a0" and not context:
            continue  # "A1A1A1" / "A1A-1A1" only next to a province or "Canada"
        ca.add(m.group(1) + m.group(3))
        if not line:
            line = re.sub(r"\s+", " ", text[max(0, m.start() - 80):m.end() + 20]).strip()
    us = set(m.group(1) for m in US_ZIP.finditer(text))
    return line[:220], len(ca), len(us)


def canada_proof(vkey, vhost, story_host, cache, stats):
    """(proof type, canada_value, proof page) or None."""
    if vkey.startswith("hq:") or vhost in HQ:
        return "hq", "Canada-HQ list", ""
    if CL.base(story_host).endswith(".ca"):
        return "ca", ".ca site", ""
    root = "https://%s/" % story_host
    page, final = cached(root, cache)
    if not page:
        return None
    pages = [(page, final)]
    links = []
    for href, label in CL.anchors(page, final):
        pu = urllib.parse.urlparse(href)
        if pu.scheme not in ("http", "https") or sld(pu.hostname or "") != sld(story_host) or pu.path in ("", "/"):
            continue
        if CONTACT_PATH.search(pu.path) or (len(label) < 40 and CONTACT_LABEL.search(label)):
            score = 0 if re.search(r"contact|joindre|contactez", pu.path + " " + label, re.I) else 1
            links.append((score, href.split("#")[0]))
    links = [u for _, u in sorted(dict.fromkeys(links), key=lambda x: x[0])]
    if not links:
        links = [urllib.parse.urljoin(root, "/contact"), urllib.parse.urljoin(root, "/contact-us")]
    for page_, url in pages + [(None, u) for u in list(dict.fromkeys(links))[:2]]:
        if page_ is None:
            if not allowed(url):
                continue
            page_, url = cached(url, cache)
            if not page_:
                continue
        line, nca, nus = canada_postal(visible(page_))
        if nca and nus <= nca:
            return "postal", line, url
        if nus > nca:
            stats["us_zip_majority_pages"] += 1
    return None


def cached(url, cache):
    if url not in cache:
        page, final, code = get(url)
        cache[url] = (html.unescape(page) if page else None, final, code)
    return cache[url][0], cache[url][1]


# ---------------------------------------------------------------- story URLs
STORY_SM = re.compile(r"custom|case|stor|client|success|temoign|etude|reference|portfolio", re.I)
LISTING = re.compile(r"^/(?:[a-z]{2}(?:[-_][a-z]{2})?/)?(?:resources/|ressources/)?(customers?|customer-stories|case-studies|"
                     r"casestudies|success-stories|clients?|client-stories|etudes-de-cas|temoignages|references)/?$", re.I)


def story_urls(root, vhost, since, cache):
    """[(url, sitemap lastmod or '')], one per story across language copies, newest lastmod first."""
    found = {}
    robots = robots_text(root)
    listed = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots)
    defaults = [] if listed else [urllib.parse.urljoin(root, p) for p in ("/sitemap.xml", "/sitemap_index.xml", "/wp-sitemap.xml")]
    queue, seen, readable = listed + defaults, set(), 0
    while queue and len(seen) < 40 and len(found) < 5000:
        sm = queue.pop(0)
        if sm in seen:
            continue
        seen.add(sm)
        if not allowed(sm):
            continue
        txt, _, _ = get(sm, 8_000_000, want_html=False)
        if not txt or "<loc" not in txt[:50_000].lower():
            continue
        readable += 1
        if sm in defaults:
            queue = [q for q in queue if q not in defaults]
        index = "<sitemapindex" in txt[:3000].lower()
        for blk in re.findall(r"(?is)<(?:\w+:)?(?:url|sitemap)>(.*?)</(?:\w+:)?(?:url|sitemap)>", txt):
            loc = re.search(r"(?is)<(?:\w+:)?loc>\s*(?:<!\[CDATA\[)?\s*([^<\s\]]+)", blk)
            if not loc:
                continue
            loc = html.unescape(loc.group(1)).strip()
            lm = re.search(r"<(?:\w+:)?lastmod>\s*(20\d\d-\d\d-\d\d)", blk)
            lm = lm.group(1) if lm else ""
            if index or re.search(r"\.xml(\.gz)?($|\?)", loc):
                if lm and lm < since:
                    continue  # nothing in it changed since the cutoff
                if STORY_SM.search(loc):
                    queue.insert(0, loc)
                elif len(queue) < 60 and not re.search(r"product|produit|image|video|tag|author|categor", loc, re.I):
                    queue.append(loc)
                continue
            pu = urllib.parse.urlparse(loc)
            if sld(pu.hostname or "") != sld(vhost) or not STORY.search(pu.path) or NOT_STORY.search(loc):
                continue
            if lm and lm < since:
                continue  # published <= last modified < cutoff
            found[loc.split("#")[0]] = lm
    if not readable:  # no sitemap: story links on the home page and on the customers listing page it links to
        page, final = cached(root, cache)
        if page:
            listings = []
            for href, label in CL.anchors(page, final):
                pu = urllib.parse.urlparse(href)
                if sld(pu.hostname or "") != sld(vhost):
                    continue
                if STORY.search(pu.path) and not NOT_STORY.search(href):
                    found.setdefault(href.split("#")[0], "")
                elif LISTING.match(pu.path):
                    listings.append(href.split("#")[0])
            for lu in list(dict.fromkeys(listings))[:2]:
                if not allowed(lu):
                    continue
                lp, lf = cached(lu, cache)
                for href, label in CL.anchors(lp or "", lf):
                    pu = urllib.parse.urlparse(href)
                    if sld(pu.hostname or "") == sld(vhost) and STORY.search(pu.path) and not NOT_STORY.search(href) \
                            and pu.path.rstrip("/") != urllib.parse.urlparse(lu).path.rstrip("/"):
                        found.setdefault(href.split("#")[0], "")
    best = {}
    for u, lm in found.items():
        p = urllib.parse.urlparse(u).path
        m = re.match(r"^/([a-z]{2}(?:[-_][a-zA-Z]{2})?)(/.*)$", p)
        lang, rest = (m.group(1).lower(), m.group(2)) if m else ("", p)
        rank = 0 if lang in ("", "en", "en-us", "en-ca", "en_ca", "en-gb") else 1
        k = rest.rstrip("/").lower()
        if k not in best or rank < best[k][0]:
            best[k] = (rank, lm, u)
    return [(u, lm) for _, lm, u in sorted(best.values(), key=lambda x: x[1], reverse=True)]


# ---------------------------------------------------------------- the page's own published date
MON = {"january": 1, "jan": 1, "february": 2, "feb": 2, "march": 3, "mar": 3, "april": 4, "apr": 4, "may": 5, "june": 6,
       "jun": 6, "july": 7, "jul": 7, "august": 8, "aug": 8, "september": 9, "sept": 9, "sep": 9, "october": 10,
       "oct": 10, "november": 11, "nov": 11, "december": 12, "dec": 12, "janvier": 1, "février": 2, "fevrier": 2,
       "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7, "août": 8, "aout": 8, "septembre": 9, "octobre": 10,
       "novembre": 11, "décembre": 12, "decembre": 12}
_MONALT = "|".join(sorted(MON, key=len, reverse=True))
HUMAN = re.compile(r"(?i)\b(?:(\d{1,2})(?:er|st|nd|rd|th)?\s+(%s)\.?,?\s+(20\d\d)|(%s)\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(20\d\d))\b"
                   % (_MONALT, _MONALT))
META_KEYS = (r"article:published_time|og:published_time|datePublished|pubdate|publish[-_]?date|publication[-_]?date|"
             r"published[-_]?date|sailthru\.date|parsely-pub-date|dc\.date\.issued|dcterms\.issued|dc\.date|dcterms\.date|date")
META_A = re.compile(r"(?is)<meta[^>]+(?:property|name|itemprop)\s*=\s*[\"'](?:%s)[\"'][^>]*?content\s*=\s*[\"']([^\"']+)" % META_KEYS)
META_B = re.compile(r"(?is)<meta[^>]+content\s*=\s*[\"']([^\"']+)[\"'][^>]+(?:property|name|itemprop)\s*=\s*[\"'](?:%s)[\"']" % META_KEYS)
PUBLISHED_TEXT = re.compile(r"(?i)\b(?:published|posted|date published|publication date|publi[ée]e?|date de publication|"
                            r"mis en ligne)\b\s*(?:on|le|:)?\s*:?\s*(.{6,40})")


def as_date(s):
    s = s or ""
    m = re.search(r"(20\d\d)[-/.](\d{1,2})[-/.](\d{1,2})", s)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = HUMAN.search(s)
        if not m:
            return ""
        if m.group(1):
            y, mo, d = int(m.group(3)), MON[m.group(2).lower()], int(m.group(1))
        else:
            y, mo, d = int(m.group(6)), MON[m.group(4).lower()], int(m.group(5))
    try:
        out = datetime.date(y, mo, d).isoformat()
    except ValueError:
        return ""
    return out if "2000-01-01" <= out <= TODAY else ""


def published_date(page, url):
    """(YYYY-MM-DD, source) from the page itself; never a modified date."""
    head = page[:800_000]
    for rx, src in ((META_A, "meta published"), (META_B, "meta published"),
                    (re.compile(r"(?is)\"datePublished\"\s*:\s*\"([^\"]+)\""), "JSON-LD datePublished")):
        for m in rx.finditer(head):
            d = as_date(m.group(1))
            if d:
                return d, src
    times = []
    for m in re.finditer(r"(?is)<time\b([^>]*)>(.{0,80}?)</time>", head):
        attrs, inner = m.group(1), m.group(2)
        before = re.sub(r"(?s)<[^>]+>", " ", head[max(0, m.start() - 200):m.start()])
        if re.search(r"modif|updat", attrs, re.I) or re.search(r"(?i)(updated|modified|mis\s+[àa]\s+jour|modifi[ée])\W{0,15}$", before):
            continue
        dt = re.search(r"(?i)datetime\s*=\s*[\"']([^\"']+)", attrs)
        d = as_date(dt.group(1) if dt else re.sub(r"<[^>]+>", " ", inner))
        if d:
            times.append((bool(re.search(r"publish|entry-date|post-date|pubdate", attrs, re.I)), d))
    for marked, d in times:
        if marked:
            return d, "time tag (published)"
    m = re.search(r"/(20\d\d)/(\d\d)/(?:(\d\d)/)?", urllib.parse.urlparse(url).path)
    if m:
        d = as_date("%s-%s-%s" % (m.group(1), m.group(2), m.group(3) or "01"))
        if d:
            return d, "URL /YYYY/MM/"
    for m in PUBLISHED_TEXT.finditer(visible(page)[:40_000]):
        d = as_date(m.group(1))
        if d:
            return d, "visible 'published' line"
    if times:
        return times[0][1], "time tag"
    return "", ""


# ---------------------------------------------------------------- customer name and website
def page_bits(page):
    def grab(rx):
        m = re.search(rx, page[:600_000])
        return re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", m.group(1))).strip() if m else ""
    return (grab(r"(?is)<title[^>]*>(.*?)</title>"), grab(r"(?is)<h1[^>]*>(.*?)</h1>"),
            grab(r"(?is)<meta[^>]+property\s*=\s*[\"']og:title[\"'][^>]+content\s*=\s*[\"']([^\"']+)"))


def good_name(n):
    n = (n or "").strip(" .,:;|-–—\"'“”")
    if not (2 <= len(n) <= 70) or len(n.split()) > 8 or BAD_NAME.match(n) or re.search(r"[%$?!]|\d{2,}", n):
        return ""
    if not re.search(r"[A-ZÀ-Ý]", n[:1] + "".join(w[:1] for w in n.split())):
        return ""  # a proper name has a capital
    return n


def customer_site(page, final, vhost, name, title, h1):
    """(host, link label, basis) of the customer's site among the story's external links, else ('', '', '')."""
    body = re.sub(r"(?is)<(header|nav|footer|aside)\b.*?</\1>", " ", page)
    m = re.search(r"(?is)<main\b[^>]*>(.*?)</main>", body) or re.search(r"(?is)<article\b[^>]*>(.*?)</article>", body)
    body = m.group(1) if m and len(m.group(1)) > 2000 else body
    doms, labels = collections.Counter(), {}
    for href, label in CL.anchors(body, final):
        pu = urllib.parse.urlparse(href)
        h = site_host(CL.base(pu.hostname))
        if pu.scheme not in ("http", "https") or not h or "." not in h or SKIP.search(h) or sld(h) == sld(vhost):
            continue
        doms[h] += 1
        labels.setdefault(h, label)
    slug = squash(urllib.parse.urlparse(final).path.rstrip("/").rsplit("/", 1)[-1])
    tsq = squash(title + " " + h1)
    for h, _ in doms.most_common():
        if name and name_match(h, name):
            return h, labels[h], "link whose domain spells the customer name"
    for h, _ in doms.most_common():
        lab = squash(sld(h))
        if len(lab) >= 5 and lab not in GENERIC_WORDS and lab in tsq and lab in slug:
            return h, labels[h], "link whose domain is in the page title and URL slug"
    return "", "", ""


_wd_cache = {}


def wd_get(params):
    """Wikidata API call; a lock file shared by all shards keeps it at most one request per second in total."""
    with open(os.path.join(LEADS, ".wikidata_rate"), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read().strip() or 0)
        except ValueError:
            last = 0
        w = last + 1.05 - time.time()
        if w > 0:
            time.sleep(w)
        f.seek(0)
        f.truncate()
        f.write("%.3f" % time.time())
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)
    params = dict(params, format="json")
    req = urllib.request.Request(WD_API + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def wikidata_site(name):
    """Official website of the item whose label or alias is exactly the name (one-word names: the domain must spell it)."""
    n = norm(name)
    if len(n) < 4:
        return None
    if n in _wd_cache:
        return _wd_cache[n]
    hit = None
    try:
        res = wd_get({"action": "wbsearchentities", "search": name, "language": "en", "limit": 7, "type": "item"}).get("search", [])
        ids = [x["id"] for x in res if norm(x.get("label")) == n or norm((x.get("match") or {}).get("text")) == n]
        if ids:
            ents = wd_get({"action": "wbgetentities", "ids": "|".join(ids[:5]), "props": "claims"}).get("entities", {})
            for qid in ids:
                c = (ents.get(qid) or {}).get("claims", {})
                sites = [(x["mainsnak"].get("datavalue") or {}).get("value") for x in c.get("P856", [])]
                if not sites or not sites[0]:
                    continue
                host = (urllib.parse.urlparse(sites[0]).hostname or "").lower()
                if len(n.split()) >= 2 or n.replace(" ", "") in host.replace("-", ""):
                    hit = (sites[0], qid)
                    break
    except Exception:
        hit = None
    _wd_cache[n] = hit
    return hit


# ---------------------------------------------------------------- one vendor
lock = threading.Lock()


def one(v, a, out, nosite, done, stats):
    site = (v.get("known_website") or "").strip()
    if not site.startswith("http"):
        return
    p = urllib.parse.urlparse(site)
    host = (p.hostname or "").lower()
    vhost = CL.base(host)
    root = "https://%s/" % host
    if vhost in done:
        return
    vkey = v.get("buyer_key") or ""
    vname = v.get("buyer_name") or ""
    vendor = vname if vname and name_match(vhost, vname) else vhost
    vwords = [w for w in re.split(r"[^a-z]+", sld(vhost)) if len(w) >= 4] + ([squash(vname)] if vendor == vname and len(squash(vname)) >= 4 else [])
    cache, rows, nos, info = {}, {}, [], collections.Counter()
    proof = None
    urls = []
    try:
        if allowed(root):
            urls = story_urls(root, vhost, a.since, cache)
        if urls:
            story_host = collections.Counter(urllib.parse.urlparse(u).hostname for u, _ in urls).most_common(1)[0][0]
            proof = canada_proof(vkey, vhost, story_host, cache, stats)
        useless = blocked = 0
        for u, lm in (urls[:a.per_vendor] if proof else []):
            if useless >= 12 or blocked >= 3:
                break
            if not allowed(u):
                continue
            page, final, code = get(u)
            if code in (401, 403, 429):
                blocked += 1
                info["blocked"] += 1
                continue
            if not page:
                continue
            page = html.unescape(page)
            info["read"] += 1
            title, h1, og = page_bits(page)
            if BLOCKED_TITLE.search(title + " " + h1):
                blocked += 1
                info["blocked"] += 1
                continue
            d, dsrc = published_date(page, final)
            if d:
                info["dated"] += 1
            if not d or d < a.since:
                useless += 1
                continue
            useless = 0
            info["dated_since"] += 1
            if d >= LAST12:
                info["dated_12m"] += 1
            name = good_name(name_from(title, h1, vwords) or name_from(og, "", vwords))
            text = visible(page)
            if name and len(re.findall(re.escape(name.lower()), text.lower())) < 2:
                name_checked = False
            else:
                name_checked = bool(name)
            ch, label, basis = customer_site(page, final, vhost, name, title, h1)
            web = "https://%s/" % ch if ch else ""
            if not web and name and name_checked and (len(name.split()) >= 2 or len(name) >= 5) and \
                    squash(name) not in GENERIC_WORDS:
                hit = wikidata_site(name)
                if hit:
                    wh = CL.base(urllib.parse.urlparse(hit[0]).hostname)
                    if wh and sld(wh) != sld(vhost) and not SKIP.search(wh):
                        ch, web, basis = wh, "https://%s/" % wh, "Wikidata %s (exact label)" % hit[1]
            publisher = name if name and (name_checked or (ch and name_match(ch, name))) else ""
            if not publisher and ch:
                lab = re.sub(r"\s+", " ", label or "").strip()
                publisher = name_in_title(squash(sld(ch)), title + " | " + h1) or (
                    lab if good_name(lab) and not re.search(r"www|http|website|visit|learn|read|click|here|site", lab, re.I) else ch)
            canada_type, canada_value, proof_page = proof
            row = {"title": (og or title or h1)[:300], "page_title": title[:300], "h1": h1[:300], "story_date": d,
                   "record_date": d, "date_source": dsrc, "sitemap_lastmod": lm, "customer_label": name,
                   "customer_link_label": (label or "")[:120], "customer_site_basis": basis, "vendor_site": root,
                   "vendor_key": vkey, "vendor_list_name": vname, "vendor_canada_proof": canada_type,
                   "canada_proof_page": proof_page, "quote": (og or title or h1)[:300], "retrieved": TODAY}
            if not web:
                if name:
                    nos.append({"buyer": name, "vendor": vendor, "page": final, "row": row})
                continue
            if sld(ch) == sld(vhost):
                continue
            r = {"platform": "vendor_story_dated", "domain": ch, "dataset_id": final,
                 "dataset": "customer story published by a Canada-located vendor (dated)", "dataset_url": final,
                 "publisher": publisher or ch, "buyer_unit": "", "website": web, "vendor": vendor,
                 "canada_field": "customer story published by the vendor (dated)", "canada_value": canada_value, "row": row}
            if ch not in rows or d > rows[ch]["row"]["story_date"]:
                rows[ch] = r
    except Exception as e:
        info["error"] += 1
        print("error %s: %r" % (vhost, e), flush=True)
    with lock:
        if rows:
            with open(out, "a", encoding="utf-8") as f:
                for r in rows.values():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if nos:
            with open(nosite, "a", encoding="utf-8") as f:
                for r in nos:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(out + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\t%d\t%s\n" % (vhost, len(urls), info["read"], len(rows), proof[0] if proof else ("none" if urls else "")))
        stats["vendors"] += 1
        stats["with_story_urls"] += bool(urls)
        stats["story_urls"] += len(urls)
        stats["no_canada_proof"] += bool(urls) and not proof
        if proof:
            stats["proof_" + proof[0]] += 1
        for k in ("read", "dated", "dated_since", "dated_12m", "blocked", "error"):
            stats[k] += info[k]
        stats["rows"] += len(rows)
        stats["rows_12m"] += sum(1 for r in rows.values() if r["row"]["story_date"] >= LAST12)
        stats["nosite"] += len(nos)
        if stats["vendors"] % 100 == 0:
            print("%s %s" % (datetime.datetime.now().strftime("%H:%M"), dict(stats)), flush=True)


def load_vendors():
    vendors, seen = [], set()
    hq = [{"buyer_key": "hq:" + h, "buyer_name": "", "known_website": "https://www.%s/" % h if h.count(".") == 1 else "https://%s/" % h}
          for h in dict.fromkeys(HQ_VENDORS)]
    lists = [os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90%d.csv" % n) for n in (3, 4, 2)]
    for rows in [hq] + [csv.DictReader(open(f, encoding="utf-8-sig")) for f in lists if os.path.exists(f)]:
        for r in rows:
            h = CL.base(urllib.parse.urlparse((r.get("known_website") or "").strip()).hostname)
            if h and h not in seen:
                seen.add(h)
                vendors.append(r)
    return vendors


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--shard", type=int, default=0)
    a.add_argument("--of", type=int, default=1)
    a.add_argument("--workers", type=int, default=32)
    a.add_argument("--per-vendor", type=int, default=40)
    a.add_argument("--since", default="2023-11-02")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--test", type=int, default=0, help="N vendors: 1/3 Canada-HQ list, 2/3 sampled from the lists")
    a.add_argument("--fresh", action="store_true", help="overwrite this shard's output instead of resuming")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    allv = load_vendors()
    if a.test:
        d = os.path.join(LEADS, "dstories_test")
        os.makedirs(d, exist_ok=True)
        out, nosite = os.path.join(d, "socrata_dstories_test.jsonl"), os.path.join(d, "dstories_nosite_test.jsonl")
        hq = [v for v in allv if (v.get("buyer_key") or "").startswith("hq:")]
        rest = [v for v in allv if not (v.get("buyer_key") or "").startswith("hq:")]
        vendors = hq[:a.test // 3] + random.Random(7).sample(rest, a.test - a.test // 3)
    else:
        out = os.path.join(LEADS, "socrata_dstories_%02d.jsonl" % a.shard)
        nosite = os.path.join(LEADS, "dstories_nosite_%02d.jsonl" % a.shard)
        vendors = [v for v in allv if int(hashlib.sha1(CL.base(urllib.parse.urlparse(v["known_website"].strip()).hostname)
                                                       .encode()).hexdigest(), 16) % a.of == a.shard]
        if a.limit:
            vendors = vendors[:a.limit]
    if a.fresh or a.test:
        for f in (out, nosite, out + ".done"):
            if os.path.exists(f):
                os.remove(f)
    done = set(l.split("\t")[0] for l in open(out + ".done", encoding="utf-8")) if os.path.exists(out + ".done") else set()
    print("%s shard %d/%d: %d vendor sites (%d done before), since %s" % (
        datetime.datetime.now().strftime("%H:%M"), a.shard, a.of, len(vendors), len(done), a.since), flush=True)
    stats = collections.Counter()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, a, out, nosite, done, stats), vendors))
    print("%s shard %d finished %s" % (datetime.datetime.now().strftime("%H:%M"), a.shard, dict(stats)), flush=True)


if __name__ == "__main__":
    main()

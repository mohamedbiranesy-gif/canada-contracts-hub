#!/usr/bin/env python3
"""Credit scan (cloud): the relationship an organisation prints on its OWN home page — "Website by <agency>", "Site web réalisé par …",
"Hébergé par …", "Powered by …" — with a link to the vendor. When the vendor's own site prints a Canadian postal address, that is a
Canada-located vendor that was paid by the organisation, stated by the paying party itself, read live and dated.

Why (owner 2026-11-09 20:48 EST: "a Canadian entity gets paid because it provided a service … establish that relationship, get the other
party's contact"): 50,355 of the 64,539 delivered rows are tier I — an organisation with a confirmed mailbox and only an INFERRED
relationship. One request to each organisation's home page turns many of them into a relationship with evidence, and the same scan over
every .ca site in Common Crawl's index finds new buyers. Nothing here uses AI or a search engine.

  universe --shard K/N        every .ca registered domain with a captured page (Common Crawl columnar index) -> out/ca_domains_<K>.csv
  merge-universe DIR          -> data/incoming/claude/credit_scan/ca_domains.csv.gz
  scan --shard K/N            one polite read of each site's home page (robots.txt respected, identified user agent): credit links and the
                              vetted Canada-HQ software services (tools/tech_relationships.py) -> out/credit_seen_<K>.jsonl, out/credit_done_<K>.tsv
  vendors --shard K/N         each credited vendor's own home / contact page: its postal address (the Canada proof), its own name
                              -> out/credit_vendors_<K>.jsonl
  merge DIR --stamp S         shard outputs -> append-only files in data/incoming/claude/credit_scan/ (done_, seen_, vendors_<S>), then
                              leads: every sighting whose vendor is proven in Canada -> claude_buyer_leads_cc.csv + claude_lead_details_cc.jsonl.gz
                              (tools/lead_crawl.py then reads the buyer's site for its role mailbox; the referee re-fetches that page), and the
                              vetted-service sightings -> claude_tenant_candidates.csv.gz (tools/lead_crawl.py --candidates accepts or rejects)
Scan order: delivered rows (their relationship is upgraded), then leads, then the .ca universe (sites with the most captured pages first).

What counts as a credit (find_credits): an <a> to another organisation's domain whose own text, or the text right before it, is a service
credit. Three classes — W: a web noun is in the phrase ("website by", "site web par", "hébergé par", "web design by"): accepted anywhere on
the page; D: a design verb alone ("designed by", "conception :", "une réalisation de"): only in the footer zone; P: "powered by" /
"propulsé par": only in the footer zone, vendors with a free plan excluded. Sponsors, donors, hosts of events, themes, photo credits,
"developed by" / "built by" without a web noun (real-estate developers, builders) are not credits.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, random, re, sys, threading, time, urllib.parse, urllib.robotparser

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "credit_scan")
UNIVERSE = os.path.join(DIR, "ca_domains.csv.gz")
TODAY = time.strftime("%Y-%m-%d")
CF_CREDIT = "service of a Canada-located vendor credited on the buyer's own site (tech)"  # "(tech)": rank.py files it as a service seen on the buyer's own site
PLATFORM = re.compile(r"(^|\.)(blogspot|wordpress|wixsite|weebly|squarespace|myshopify|godaddysites|webflow|github|tumblr|substack|jimdo|site123|webself|wix|godaddy|google|facebook|"
                      r"instagram|twitter|linkedin|youtube|pinterest|tiktok|apple|microsoft|amazon|cloudflare|shopify|w3|gravatar|automattic|woocommerce|elementor|bootstrap|jquery|"
                      r"mailchimp|hubspot|paypal|stripe|yelp|tripadvisor|eventbrite|vimeo|flickr|whatsapp|adobe|bit|goo|t|x|canada|gc)\.[a-z.]{2,8}$", re.I)
# Canada-based services with a free plan or no charge to the organisation: a "powered by" line is not proof of a payment
FREE_PLAN = re.compile(r"(^|\.)(webself\.net|zeffy\.com|thinkific\.com|vidyard\.com|wattpad\.com|fundrazr\.com|hootsuite\.com|wealthsimple\.com|canva\.com|linktr\.ee|carrd\.co|"
                       r"wildapricot\.(com|org)|cyberimpact\.com|canadahelps\.org|gofundme\.com|tithe\.ly)$", re.I)

# ------------------------------------------------------------------------------------------------------------------- credit phrases
_WEBN = (r"(?:web\s?sites?|web\s?pages?|sites?\s?web|sites?\s+internet|pages?\s+web|web\s?design|web\s?development|web\s?hosting|web\s?marketing|design\s+web|"
         r"d[ée]veloppement\s+web|conception\s+web|h[ée]bergement(?:\s+web)?|h[ée]berg[ée]e?s?|r[ée]f[ée]rencement|seo|webmaster|webmestre|sites?|web)")
_DESN = (r"(?:design(?:ed)?|crafted|handcrafted|hand-crafted|coded|programmed|engineered|con[çc]u(?:e|s|es)?|conception|r[ée]alis[ée](?:e|s|es)?|r[ée]alisation|cr[ée]ation|"
         r"programmation|programm[ée](?:e|s|es)?|marketing|branding)")
_WEAK = (r"(?:develop(?:ed|ment)|built|created?|made|hosted|hosting|maintained|maintenance|cr[ée][ée](?:e|s|es)?|d[ée]velopp[ée](?:e|s|es)?|d[ée]veloppement|fait)")
_POW = r"(?:powered|propuls[ée](?:e|s|es)?)"
_HEAD = "(?:%s|%s|%s|%s)" % (_WEBN, _DESN, _WEAK, _POW)
_JOIN = r"(?:\s*(?:and|&|\+|et|,|/|-|–)\s*|\s+)"
_FILL = r"(?:graphique|internet|num[ée]rique|digital|du\s+site|de\s+site|de\s+ce\s+site|of\s+this\s+site|this\s+site|ce\s+site|is|was|est|a\s+[ée]t[ée])"
_WITH = (r"(?:(?:with|avec)\s+[^\s<>]{1,14}(?:\s+(?:and|&|et)\s+[^\s<>]{1,14})?\s+|proudly\s+|lovingly\s+|fi[èe]rement\s+|in\s+[A-Z][A-Za-zÀ-ÿ.\-]{2,20}(?:,?\s+[A-Z][A-Za-zÀ-ÿ.\-]{1,20})?\s+)")
_PH_BY = _HEAD + "(?:" + _JOIN + "(?:" + _HEAD + "|" + _FILL + "))*" + r"\s*(?:" + _WITH + r"){0,2}(?:by|par)(?![A-Za-zÀ-ÿ])"
_PH_COLON = (r"(?:web\s?design|design|conception|r[ée]alisation|cr[ée]ation|d[ée]veloppement|development|h[ée]bergement|hosting|programmation|webmaster|webmestre|site\s?web|web\s?site)"
             + "(?:" + _JOIN + "(?:" + _HEAD + "|" + _FILL + "))*" + r"\s*:")
_PH_DE = r"(?:une\s+)?(?:r[ée]alisation|cr[ée]ation|conception)(?:\s+web)?\s+(?:de\s+l['’][ée]quipe(?:\s+de)?|de|d['’]|sign[ée]e(?:\s+par)?)(?![A-Za-zÀ-ÿ])"
_PHRASE = "(?:" + _PH_BY + "|" + _PH_COLON + "|" + _PH_DE + ")"
BEFORE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PHRASE + r")[\s:\-–—|»›>]{0,6}(?:(?:the\s+(?:team|folks)\s+at|l['’][ée]quipe\s+(?:de|chez)|our\s+friends\s+at)[\s|]*)?$", re.I)
INNER_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PHRASE + r")\s*(?!e-?mail|courriel|courrier|email|sms|t[ée]l[ée]phone)\S", re.I)  # not "marketing par e-mail" (a newsletter badge)
WEBN_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _WEBN + r"(?![A-Za-zÀ-ÿ])", re.I)
DESN_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _DESN + r"(?![A-Za-zÀ-ÿ])", re.I)
POW_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])" + _POW + r"(?![A-Za-zÀ-ÿ])", re.I)
WITH_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(?:with|avec)\s+\S", re.I)
MAKE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(?:made|built|created|fait|cr[ée][ée]e?)(?![A-Za-zÀ-ÿ])", re.I)
# words right before / inside the phrase that make it something else than a service the organisation paid for
NEG_RX = re.compile(r"donat|sponsor|courtesy|gracieuset|offert|commandit|pro\s?bono|volunteer|b[ée]n[ée]vol|themes?\b|th[èe]mes?\b|templates?|gabarit|plugin|ic[oô]n|fonts?\b|polices?\b|photo|image|"
                    r"illustrat|vid[ée]o|map\b|carte\b|musi[cq]|recipe|recette|article|post\b|billet|written|[ée]crit|review|produit|product|collection|furniture|meuble|homes?\b|maisons?\b|condos?|"
                    r"project|projet|communit|communaut|building|immeuble|tower|tour\b|event|[ée]v[èé]nement|festival|concert|show|spectacle|tournament|tournoi|award|prix|study|[ée]tude|report|rapport", re.I)
A_RX = re.compile(r"<a\b([^>]*)>(.*?)</a\s*>", re.I | re.S)
HREF_RX = re.compile(r"""\bhref\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+))""", re.I)
ATTR_RX = re.compile(r"""\b(?:alt|title|aria-label)\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.I)
DROP_RX = re.compile(r"<(script|style|noscript)\b.*?</\1\s*>|<!--.*?-->", re.I | re.S)
TAG_RX = re.compile(r"<[^>]*>")


BLOCK_RX = re.compile(r"</?(?:p|div|li|ul|ol|td|tr|th|table|section|footer|header|nav|aside|h[1-6]|br|hr|form|address|small)\b[^>]*>", re.I)


def vis(s, sep=False):
    """visible text of a piece of HTML that may start or end in the middle of a tag or a script; sep: block boundaries become " | " """
    for end in ("</script>", "</style>", "</noscript>", "-->"):
        i = s.lower().rfind(end)
        if i >= 0 and "<script" not in s[i:].lower() and "<style" not in s[i:].lower():
            s = s[i + len(end):]
    i, j = s.find(">"), s.find("<")
    if i >= 0 and (j < 0 or i < j):
        s = s[i + 1:]
    i, j = s.rfind("<"), s.rfind(">")
    if i >= 0 and i > j:
        s = s[:i]
    s = DROP_RX.sub(" ", s)
    if sep:
        s = BLOCK_RX.sub(" | ", s)
    s = TAG_RX.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


CLAUSE_RX = re.compile(r"[|·•.©®™–—:;,()!?\[\]/]|\s-\s|\d{4}")


def phrase_class(ph, ctx):
    """W / D / P ('' = not a service credit). ctx: the text before the phrase; only the clause the phrase belongs to is tested
    ("Theme designed by", "This project was built by"), never the organisation's own name in the copyright line before it."""
    clause = CLAUSE_RX.split(ctx)[-1][-40:]
    if NEG_RX.search(clause + " " + ph):
        return ""
    if WEBN_RX.search(ph):
        return "W"
    if DESN_RX.search(ph):
        return "D"
    if POW_RX.search(ph):
        return "P"
    return "D" if WITH_RX.search(ph) and MAKE_RX.search(ph) else ""  # "made with love by", "built with care by" (an agency's signature), never "hosted with … by"


def find_credits(raw, page_url):
    """[{v: vendor registrable domain, vh: vendor host, k: W|D|P, q: quote (<= 300 chars), t: the link's own text}] — one per vendor domain"""
    site = C.registrable((urllib.parse.urlparse(page_url).hostname or "").lower())
    raw = raw[:1_500_000]
    low = raw.lower()
    foot = low.rfind("<footer")
    zone = min(foot if foot >= len(raw) * 0.5 else len(raw), int(len(raw) * 0.8))  # the footer zone: from the last <footer> (when it sits in the second half), at most the last 20 %
    out = {}
    for m in A_RX.finditer(raw):
        h = HREF_RX.search(m.group(1))
        if not h:
            continue
        href = (h.group(1) or h.group(2) or h.group(3) or "").strip()
        if not href.lower().startswith(("http://", "https://", "//")):
            continue
        try:
            host = (urllib.parse.urlparse(urllib.parse.urljoin(page_url, href)).hostname or "").lower()
        except ValueError:
            continue
        host = host[4:] if host.startswith("www.") else host
        if not host or "." not in host:
            continue
        v = C.registrable(host)
        if v == site or PLATFORM.search(v):
            continue
        inner = m.group(2)
        attrs = " ".join(a or b for a, b in ATTR_RX.findall(m.group(1) + " " + inner))
        itxt = vis(inner)
        label = (itxt or attrs).strip()[:120]
        before = vis(raw[max(0, m.start() - 700):m.start()], sep=True)[-200:]
        ph, cls, where = "", "", ""
        mb = BEFORE_RX.search(before)
        if mb:
            ph, cls, where = mb.group(1), phrase_class(mb.group(1), before[:mb.start()]), "before"
        if not cls:
            for cand in (itxt, attrs):
                mi = INNER_RX.search(cand or "")
                if mi:
                    ph, cls, where = mi.group(1), phrase_class(mi.group(1), (cand or "")[:mi.start()]), "inner"
                    if cls:
                        label = (cand or "").strip()[:120]
                        break
        if not cls:
            continue
        label = label or "[link to %s]" % host  # a logo without alt text: the link target names the vendor
        if cls in ("D", "P") and m.start() < zone:
            continue  # a bare "designed by" / "powered by" outside the footer zone is usually about a product, not about the site
        q = (before[-150:] + " " + label) if where == "before" else label
        q = re.sub(r"\s+", " ", re.sub(r"(?:\s*\|\s*)+", " | ", q)).strip(" |")[-300:]
        cur = out.get(v)
        if cur is None or "WDP".index(cls) < "WDP".index(cur["k"]):
            out[v] = {"v": v, "vh": host, "k": cls, "q": q, "t": label, "p": re.sub(r"\s+", " ", ph).strip()[:80]}
    return list(out.values())


# ------------------------------------------------------------------------------------------------------------------- fetching
def decode(data, ctype):
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I)
    enc = m.group(1) if m else ""
    if not enc:
        mb = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", data[:4000], re.I)
        enc = mb.group(1).decode("ascii", "replace") if mb else "utf-8"
    try:
        return data.decode(enc, "replace")
    except LookupError:
        return data.decode("utf-8", "replace")


def robots_ok(root, url):
    """(allowed, reachable). No shared cache: a scan meets each host once."""
    st, _, data, _ = C.fetch(root + "robots.txt", 300_000)
    if st in (401, 403):
        return False, True
    if st == 0:
        return True, False
    if st == 200 and data:
        rp = urllib.robotparser.RobotFileParser()
        try:
            rp.parse(data.decode("utf-8", "replace").splitlines())
            return rp.can_fetch(C.UA, url), True
        except Exception:
            return True, True
    return True, True


def get_page(url, check_robots=True):
    """(status word, final url, html) — status: ok | robots | unreachable | blocked | http_<code> | not_html"""
    p = urllib.parse.urlparse(url)
    root = "%s://%s/" % (p.scheme, p.netloc)
    if check_robots:
        ok, reach = robots_ok(root, url)
        if not reach:
            return "unreachable", url, ""
        if not ok:
            return "robots", url, ""
    st, ctype, data, final = C.fetch(url, 1_500_000)
    if st == 0:
        return "unreachable", final, ""
    head = data[:20000].decode("utf-8", "replace") if data else ""
    if st in (401, 403, 429) or (st == 503 and C.BLOCK_RX.search(head)) or (C.BLOCK_RX.search(head) and len(data) < 30000):
        return "blocked", final, ""
    if st != 200 or not data:
        return "http_%s" % st, final, ""
    if data[:5] == b"%PDF-" or "pdf" in (ctype or "").lower() or ("html" not in (ctype or "html").lower() and b"<html" not in data[:3000].lower() and b"<a " not in data[:20000].lower()):
        return "not_html", final, ""
    fh = (urllib.parse.urlparse(final).hostname or "").lower()
    if C.registrable(fh) != C.registrable(p.hostname or "") and check_robots:  # redirected to another organisation's domain: its robots.txt decides
        fp = urllib.parse.urlparse(final)
        ok, _ = robots_ok("%s://%s/" % (fp.scheme, fp.netloc), final)
        if not ok:
            return "robots", final, ""
    return "ok", final, html.unescape(decode(data, ctype))


def host_of(site):
    site = (site or "").strip()
    h = (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower() if site else ""
    return h[4:] if h.startswith("www.") else h


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def state_lines(prefix):
    """every line of the append-only state files data/incoming/claude/credit_scan/<prefix>_*.gz"""
    for p in sorted(glob.glob(os.path.join(DIR, prefix + "_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                if l.strip():
                    yield l.rstrip("\n")


# ------------------------------------------------------------------------------------------------------------------- universe
def universe(a):
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    con = CCL._duck()
    out = collections.Counter()
    for spec in CCL.crawl_ids(a.crawl):
        cid, paths = CCL.newest_crawl(spec)
        queue, t0 = list(enumerate(paths[k::n])), time.time()
        for rnd in range(5):
            if not queue:
                break
            if rnd:
                print("round %d: %d index parts to read again after a pause" % (rnd + 1, len(queue)), flush=True)
                time.sleep(60 * rnd + random.uniform(0, 30))
            nxt = []
            for i, p in queue:
                q = ("SELECT url_host_registered_domain, count(*) FROM read_parquet('%s') WHERE url_host_tld IN ('ca', 'quebec') AND fetch_status = 200 "
                     "AND content_mime_detected = 'text/html' GROUP BY 1") % (CCL.CC + p)
                try:
                    got = con.execute(q).fetchall()
                except Exception as e:
                    print("part %d failed (round %d): %s" % (i, rnd + 1, str(e)[:160]), flush=True)
                    nxt.append((i, p))
                    time.sleep(10)
                    continue
                for d, c in got:
                    if d:
                        out[d.lower()] += c
                if got or i % 25 == 0:
                    print("%s %s part %d: %d .ca domains (total %d, %.0f s)" % (time.strftime("%H:%M:%S"), cid, i, len(got), len(out), time.time() - t0), flush=True)
            queue = nxt
        if queue:
            print("UNREAD index parts of %s after 5 rounds: %s" % (cid, ", ".join(str(i) for i, p in queue)), flush=True)
    with open("out/ca_domains_%d.csv" % k, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "pages"])
        for d, c in sorted(out.items()):
            w.writerow([d, c])
    print("shard %d: %d .ca registered domains with a captured page" % (k, len(out)), flush=True)


def merge_universe(a):
    doms = collections.Counter()
    if os.path.exists(UNIVERSE):
        with gzip.open(UNIVERSE, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                doms[r["dom"]] = int(r["pages"] or 0)
    n0 = len(doms)
    for f in sorted(glob.glob(os.path.join(a.dir, "ca_domains_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("dom") and not PLATFORM.search(r["dom"]):
                doms[r["dom"]] = max(doms[r["dom"]], int(r["pages"] or 0))
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(UNIVERSE, "wt", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["dom", "pages"])
        for d in sorted(doms):
            w.writerow([d, doms[d]])
    print(".ca universe: %d registered domains with a captured page (+%d this run)" % (len(doms), len(doms) - n0))


# ------------------------------------------------------------------------------------------------------------------- scan
def scan_queue(k, n, limit=0):
    done = {l.split("\t")[0] for l in state_lines("done")}
    seen, tasks = set(), []

    def add(host, pri, extra=0):
        if not host or "." not in host or host in seen or host in done or PLATFORM.search(host) or not shard_ok(host, k, n):
            return
        seen.add(host)
        tasks.append((pri, -extra, host))
    rp = os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz")
    if os.path.exists(rp):  # 1. delivered rows: the inferred-relationship rows first (a credit gives them a relationship with evidence)
        with gzip.open(rp, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(host_of(r.get("buyer_website")), 0 if r.get("tier") == "I" else 1)
    for p in (CCL.LEADS_CC, os.path.join(INC, "claude_buyer_leads.csv")):  # 2. leads (a credit is a second, first-party relationship)
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
                add(host_of(r.get("website")), 2)
    if os.path.exists(UNIVERSE):  # 3. every .ca site of the archive, the sites with the most captured pages first
        with gzip.open(UNIVERSE, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 3, min(int(r.get("pages") or 0), 500))
    tasks.sort()
    if limit:
        tasks = tasks[:limit]
    return [{"dom": h, "pri": pri} for pri, _, h in tasks], len(done)


def scan(a):
    import lead_crawl as LC
    import tech_relationships as T
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    tasks, n_done = scan_queue(k, n, a.limit)
    print("shard %d/%d: %d sites to read (%d read before): %s" % (k, n, len(tasks), n_done, dict(collections.Counter(t["pri"] for t in tasks))), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fs = open("out/credit_seen_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/credit_done_%d.tsv" % k, "a", encoding="utf-8")
    assets_of = lambda b: " ".join(T.SRC_RE.findall(b) + T.LINKTAG_RE.findall(b) + T.INLINE_RE.findall(b)[:40])

    def one(t):
        if time.time() > deadline:
            return
        dom = t["dom"]
        try:
            res, final, raw = get_page("https://%s/" % dom)
        except Exception as e:
            res, final, raw = "error:" + type(e).__name__, "", ""
        rec = None
        if res == "ok":
            try:
                fhost = host_of(final) or dom
                credits = find_credits(raw, final)
                tech = []
                for u in T.all_urls(raw, final)[:3000]:
                    for vk, slug, purl in T.portal_hits(u):
                        if not any(x["v"] == vk and x["slug"] == slug for x in tech):
                            tech.append({"v": vk, "slug": slug, "purl": purl, "via": u[:200], "how": "link / embed on the organisation's own page"})
                if C.registrable(fhost) == C.registrable(dom) or not PLATFORM.search(fhost):
                    assets = assets_of(raw)
                    for vk, v in T.VENDORS.items():
                        if v["kind"] == "asset" and v.get("asset_re_c"):
                            ma = v["asset_re_c"].search(assets)
                            if ma:
                                x = {"v": vk, "slug": "asset", "purl": "", "via": re.sub(r"\s+", " ", assets[max(0, ma.start() - 40):ma.end() + 60])[:160], "how": "asset loaded by the organisation's own page"}
                                if vk == "shopify":
                                    mc = re.search(r'Shopify\.country\s*=\s*"([A-Z]{2})"', raw)
                                    x["country"] = mc.group(1) if mc else ""
                                tech.append(x)
                if credits or tech:
                    title, meta = T.page_meta(raw)
                    rec = {"dom": dom, "site": fhost, "page": final, "date": TODAY, "name": LC.site_name_for(fhost, meta.get("og:site_name"), title, T), "title": (title or "")[:160],
                           "credits": credits, "tech": tech}
            except Exception as e:
                res = "error:" + type(e).__name__
        with lock:
            stats["sites"] += 1
            stats[res.split(":")[0] if not res.startswith("http_") else "http_error"] += 1
            if rec:
                stats["with_credit"] += bool(rec["credits"])
                stats["with_vetted_service"] += bool(rec["tech"])
                fs.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fd.write("%s\t%s\t%s\t%d\t%d\n" % (dom, TODAY, res, len(rec["credits"]) if rec else 0, len(rec["tech"]) if rec else 0))
            if stats["sites"] % 2000 == 0:
                fs.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\n" % (t["dom"], TODAY))
            stats["timeout"] += 1
    left = LC.run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fs.close(); fd.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


# ------------------------------------------------------------------------------------------------------------------- vendors
CONTACT_RX = re.compile(r"contact|joindre|coordonn|about|propos|qui-sommes|nous-trouver|find-us|location|bureaux|offices?|impressum|legal|mentions", re.I)
SERVICE_RX = re.compile(r"web|site|design|digital|num[ée]rique|marketing|agenc[ey]|studio|cr[ée]ati|d[ée]velop|software|logiciel|h[ée]berg|hosting|seo|r[ée]f[ée]rencement|branding|"
                        r"graphi|communication|m[ée]dia|informati|\bIT\b|\bTI\b|technolog|app|cloud|e-?commerce|consult", re.I)


def proven_elsewhere():
    """vendor domains whose Canadian postal address the row factory already read on the vendor's own page: {domain: (address text, url, name)}"""
    out = {}
    if os.path.exists(CCL.DETAILS_CC):
        for l in gzip.open(CCL.DETAILS_CC, "rt", encoding="utf-8"):
            try:
                d = json.loads(l)
            except ValueError:
                continue
            if d.get("platform") == "vendor_site_cc" and d.get("vendor_address") and d.get("vendor_site"):
                dom = C.registrable(host_of(d["vendor_site"]))
                nm = d.get("vendor") or ""
                out.setdefault(dom, (d["vendor_address"], d.get("vendor_address_url") or d.get("record_url") or "", "" if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", nm.lower()) else nm))
    for dom, o in CCL._vendor_addrs().items():
        out.setdefault(C.registrable(dom), ("%s (as printed on %s, archive capture %s)" % (CCL.address_from(o.get("quote") or ""), o.get("url") or "", (o.get("capture") or "")[:10]), o.get("url") or "", ""))
    return out


def vendor_state():
    """latest live check per vendor domain"""
    out = {}
    for l in state_lines("vendors"):
        try:
            o = json.loads(l)
            out[o["dom"]] = o
        except (ValueError, KeyError):
            pass
    return out


def sightings():
    """latest sighting record per site"""
    out = {}
    for l in state_lines("seen"):
        try:
            o = json.loads(l)
            out[o["dom"]] = o
        except (ValueError, KeyError):
            pass
    return out


def vendors(a):
    import lead_crawl as LC
    import tech_relationships as T
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    have, known = vendor_state(), proven_elsewhere()
    cnt = collections.Counter()
    for o in sightings().values():
        for c in o.get("credits") or []:
            cnt[c["v"]] += 1
    tasks = [{"dom": v, "n": c} for v, c in cnt.most_common() if v not in have and v not in known and shard_ok(v, k, n) and not PLATFORM.search(v)]
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d credited vendor domains to check (%d checked before, %d proven by the row factory)" % (k, n, len(tasks), len(have), len(known)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fv = open("out/credit_vendors_%d.jsonl" % k, "a", encoding="utf-8")
    ADDRS = (("CA", CCL.ADDR), ("US", LC.US_ADDR), ("GB", LC.GB_ADDR), ("AU", LC.AU_ADDR))

    def address_in(text):
        for cc, rx in ADDRS:
            m = rx.search(text)
            if m:
                return cc, re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:]
        return "", ""

    def one(t):
        if time.time() > deadline:
            return
        dom = t["dom"]
        rec = {"dom": dom, "date": TODAY, "seen_on": t["n"], "status": "", "quote": "", "url": "", "name": "", "title": "", "desc": "", "service_words": ""}
        try:
            res, final, raw = get_page("https://%s/" % dom)
            if res != "ok":
                rec["status"] = res
            else:
                fhost = host_of(final) or dom
                title, meta = T.page_meta(raw)
                rec["name"] = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
                rec["title"], rec["desc"] = (title or "")[:160], (meta.get("description") or meta.get("og:description") or "")[:240]
                sw = SERVICE_RX.search(rec["title"] + " " + rec["desc"])
                rec["service_words"] = sw.group(0) if sw else ""
                found = {}  # country -> (quote, url); a Canadian address anywhere on the pages read wins
                cc, q = address_in(C.visible(raw))
                if cc:
                    found[cc] = (q, final)
                if "CA" not in found:
                    links, seen_l = [], set()
                    for link, label in C.links(raw, final):
                        p = urllib.parse.urlparse(link)
                        if p.scheme in ("http", "https") and C.registrable((p.hostname or "").lower()) == C.registrable(fhost) and not C.SKIP_EXT.search(p.path) \
                                and CONTACT_RX.search(p.path + " " + label) and link.split("#")[0] not in seen_l and link.split("#")[0].rstrip("/") != final.rstrip("/"):
                            seen_l.add(link.split("#")[0])
                            links.append((0 if re.search(r"contact|joindre|coordonn", p.path + " " + label, re.I) else 1, len(p.path), link.split("#")[0]))
                    todo = [u for _, _, u in sorted(links)[:3]] or ["https://%s/contact" % fhost, "https://%s/contact-us" % fhost, "https://%s/nous-joindre" % fhost]
                    for u in todo:
                        if time.time() > deadline + 120:
                            break
                        r2, f2, raw2 = get_page(u, check_robots=False) if C.allowed(u) else ("robots", u, "")
                        if r2 != "ok":
                            continue
                        cc, q = address_in(C.visible(raw2))
                        if cc and cc not in found:
                            found[cc] = (q, f2)
                        if "CA" in found:
                            break
                if found:
                    cc = "CA" if "CA" in found else sorted(found)[0]
                    rec["status"], rec["quote"], rec["url"] = cc, found[cc][0], found[cc][1]
                else:
                    rec["status"] = "no_address"
        except Exception as e:
            rec["status"] = "error:" + type(e).__name__
        with lock:
            stats["vendors"] += 1
            stats[rec["status"].split(":")[0] if not rec["status"].startswith("http_") else "http_error"] += 1
            fv.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if stats["vendors"] % 500 == 0:
                fv.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fv.write(json.dumps({"dom": t["dom"], "date": TODAY, "seen_on": t["n"], "status": "timeout"}) + "\n")
            stats["timeout"] += 1
    left = LC.run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fv.close()
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


# ------------------------------------------------------------------------------------------------------------------- merge
def credit_key(dom):
    """its own key: the same organisation may also be a client-listing lead (key of the linked domain); rank.py keeps one row per website domain"""
    return "lead:" + hashlib.sha1(("%s|credit:%s" % (dom, dom)).encode()).hexdigest()[:16]


def _append_state(prefix, stamp, lines):
    lines = [l for l in lines if l.strip()]
    if not lines:
        return 0
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(os.path.join(DIR, "%s_%s.gz" % (prefix, stamp)), "wt", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(lines)


def merge(a):
    d, stamp = a.dir, a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    done_before = {l.split("\t")[0] for l in state_lines("done")}
    new_done, st_count = {}, collections.Counter()
    for f in sorted(glob.glob(os.path.join(d, "credit_done_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and q[0] not in done_before and len(q) >= 3:
                new_done[q[0]] = l.rstrip("\n")
                st_count[q[2].split(":")[0] if not q[2].startswith("http_") else "http_error"] += 1
    n_done = _append_state("done", stamp, [new_done[k] for k in sorted(new_done)])
    new_seen = {}
    for f in sorted(glob.glob(os.path.join(d, "credit_seen_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                new_seen[o["dom"]] = json.dumps(o, ensure_ascii=False)
            except (ValueError, KeyError):
                pass
    n_seen = _append_state("seen", stamp, [new_seen[k] for k in sorted(new_seen)])
    vstate, new_v = vendor_state(), {}
    for f in sorted(glob.glob(os.path.join(d, "credit_vendors_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            try:
                o = json.loads(l)
                if o["dom"] not in vstate:
                    new_v[o["dom"]] = json.dumps(o, ensure_ascii=False)
            except (ValueError, KeyError):
                pass
    n_v = _append_state("vendors", stamp, [new_v[k] for k in sorted(new_v)])
    if n_done or n_seen:
        print("credit scan: %d sites read this run (%s); %d with a credit or a vetted service" % (n_done, ", ".join("%s %d" % kv for kv in st_count.most_common(8)), n_seen))
    # ---- leads: sightings whose vendor is proven in Canada
    vstate, known_v, seen = vendor_state(), proven_elsewhere(), sightings()
    def proof(v):
        o = vstate.get(v)
        if o and o.get("status") == "CA" and o.get("quote"):
            return ("%s (as printed on %s, read %s)" % (CCL.address_from(o["quote"]), o.get("url") or "", o.get("date") or ""), o.get("url") or "", o.get("name") or "", bool(o.get("service_words")))
        if v in known_v:
            return known_v[v] + (True,)  # the row factory read its client / portfolio page: a firm that sells services
        return None
    main_keys = set()
    mp = os.path.join(INC, "claude_buyer_leads.csv")
    if os.path.exists(mp):
        main_keys = {r["buyer_key"] for r in csv.DictReader(open(mp, encoding="utf-8", errors="replace"))}
    prev, pdet = {}, {}
    if os.path.exists(CCL.LEADS_CC):
        prev = {r["buyer_key"]: r for r in csv.DictReader(open(CCL.LEADS_CC, encoding="utf-8"))}
    if os.path.exists(CCL.DETAILS_CC):
        for l in gzip.open(CCL.DETAILS_CC, "rt", encoding="utf-8"):
            try:
                o = json.loads(l)
                pdet[o["key"]] = o
            except (ValueError, KeyError):
                pass
    stats = collections.Counter()
    vend_n = collections.Counter(c["v"] for o in seen.values() for c in (o.get("credits") or []))
    for dom in sorted(seen):
        o = seen[dom]
        site = o.get("site") or dom
        best = None
        for c in o.get("credits") or []:
            stats["credit links seen"] += 1
            v = c["v"]
            if v == C.registrable(site) or (c["k"] == "P" and FREE_PLAN.search(v)) or vend_n[v] > 20000:
                continue
            pr = proof(v)
            if not pr:
                stats["vendor not proven in Canada (yet)"] += 1
                continue
            if c["k"] in ("D", "P") and vend_n[v] < 2 and not pr[3]:
                stats["design / powered-by credit of a vendor seen once whose own site names no web / design / software service (kept out)"] += 1
                continue
            if best is None or "WDP".index(c["k"]) < "WDP".index(best[0]["k"]):
                best = (c, pr)
        if not best:
            continue
        c, pr = best
        key = credit_key(site)
        if key in main_keys:
            continue
        vname = pr[2] or c["v"]
        what = {"W": "website / web services", "D": "design / web services", "P": "software / platform"}[c["k"]]
        if key not in prev:
            stats["new leads"] += 1
        stats["leads (%s)" % what] += 1
        prev[key] = {"buyer_key": key, "buyer_name": o.get("name") or site, "website": "https://%s/" % site, "canadian_vendor_rows": 1, "example_vendor": vname,
                     "canada_field_value": "%s=%s; the vendor's own site prints its Canadian postal address: %s" % (CF_CREDIT, c["v"], pr[0][:260]),
                     "evidence_dataset": o.get("page") or "https://%s/" % site, "latest_record_date": o.get("date") or TODAY}
        pdet[key] = {"key": key, "platform": "site_credit_cc", "record_url": o.get("page") or "", "vendor": vname, "record_date": o.get("date") or "",
                     "title": "%s by %s — credit printed on the buyer's own site: “%s”" % (what, vname, c["q"][-180:]),
                     "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % c["v"], "credit_quote": c["q"], "credit_class": c["k"], "credit_phrase": c.get("p") or "",
                     "credit_link_text": c.get("t") or "", "credit_link_host": c.get("vh") or c["v"], "vendor_seen_on_sites": vend_n[c["v"]], "page_title": o.get("title") or ""}
    with open(CCL.LEADS_CC, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CCL.LEAD_COLS)
        w.writeheader()
        for k in sorted(prev):
            w.writerow({c: prev[k].get(c, "") for c in CCL.LEAD_COLS})
    with gzip.open(CCL.DETAILS_CC, "wt", encoding="utf-8") as f:
        for k in sorted(pdet):
            f.write(json.dumps(pdet[k], ensure_ascii=False) + "\n")
    # ---- vetted Canada-HQ software services seen on the site -> candidates (accepted only with a role mailbox + an address in the vendor's scope)
    n_c = 0
    try:
        import cc_tenants as CT
        cands = {}
        if os.path.exists(CT.CANDS):
            with gzip.open(CT.CANDS, "rt", encoding="utf-8", newline="") as fh:
                cands = {r["cand_key"]: r for r in csv.DictReader(fh)}
        by_host = {CCL.base((urllib.parse.urlparse(r["website"]).hostname or "").lower()) for r in cands.values()}
        n_shop = 0
        lead_hosts = {host_of(r.get("website")) for r in prev.values() if "(tech)" in (r.get("canada_field_value") or "") and "credited" not in (r.get("canada_field_value") or "")}
        for dom in sorted(seen):
            o = seen[dom]
            site = o.get("site") or dom
            for x in o.get("tech") or []:
                vk = x["v"]
                if vk == "shopify" and (x.get("country") or "") not in ("", "CA", "US"):
                    continue
                ck = "t:%s:%s" % (vk, site if x["slug"] == "asset" else x["slug"])
                if ck in cands or site in by_host or site in lead_hosts or (vk == "shopify" and n_shop >= a.max_shopify):
                    continue
                n_shop += vk == "shopify"
                cands[ck] = {"cand_key": ck, "vendor_key": vk, "name": o.get("name") or "", "website": "https://%s/" % site, "evidence_url": o.get("page") or "", "capture": o.get("date") or "",
                             "name_basis": "og:site_name / title of the organisation's own home page" if o.get("name") else "",
                             "website_basis": "%s (%s, read %s)" % (x.get("how") or "seen on the organisation's own page", o.get("page") or "", o.get("date") or ""),
                             "slug": x["slug"], "extra": json.dumps({"seen_on": o.get("page"), "via": x.get("via"), "portal": x.get("purl"), "portal_check": 1 if vk == "jane" else 0,
                                                                     "shopify_country": x.get("country") or ""}, ensure_ascii=False)}
                by_host.add(site)
                n_c += 1
                stats["vetted service candidates: " + vk] += 1
        if n_c:
            with gzip.open(CT.CANDS, "wt", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=CT.CAND_COLS)
                w.writeheader()
                for k in sorted(cands):
                    w.writerow({c: cands[k].get(c, "") for c in CT.CAND_COLS})
    except Exception as e:  # the credit leads must land even when the candidates file cannot be read
        print("vetted-service candidates skipped: %s" % e)
    vs = collections.Counter((o.get("status") or "?").split(":")[0] for o in vstate.values())
    todo_v = sum(1 for v in vend_n if v not in vstate and v not in known_v)
    print("credit leads: %s" % dict(stats))
    print("credit scan totals: sites read %d, sites with a credit or vetted service %d, credited vendor domains %d (checked live %d: %s; proven by the row factory %d; waiting %d), %d (+%d new) vendor checks this run; "
          "credit leads in %s: %d" % (len(done_before) + n_done, len(seen), len(vend_n), len(vstate), dict(vs.most_common(6)), sum(1 for v in vend_n if v in known_v), todo_v, n_v, n_v,
                                      os.path.basename(CCL.LEADS_CC), sum(1 for r in prev.values() if "credited on the buyer's own site" in (r.get("canada_field_value") or ""))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["universe", "merge-universe", "scan", "vendors", "merge"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--crawl", default="auto")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--max-shopify", type=int, default=15000, help="merge: at most this many new Shopify-store candidates per run (owner 2026-11-09: no lane may crowd out the others)")
    ap.add_argument("--straggler-seconds", type=float, default=180)
    ap.add_argument("--site-seconds", type=float, default=150)
    a = ap.parse_args()
    if a.cmd in ("scan", "vendors"):
        os.makedirs(C.STATE, exist_ok=True)
        {"scan": scan, "vendors": vendors}[a.cmd](a)
        sys.stdout.flush()
        os._exit(0)  # do not wait for straggler threads
    {"universe": universe, "merge-universe": merge_universe, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()

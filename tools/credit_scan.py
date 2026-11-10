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
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, random, re, sys, threading, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser

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
_PH_COLON = (r"(?:web\s?design|design|conception|r[ée]alisation|cr[ée]ation|d[ée]veloppement|development|h[ée]bergement|hosting|programmation|webmaster|webmestre)"
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
# membership stated by the member itself: "Proud member of the Calgary Chamber of Commerce" (text or the alt text of a badge) linked to the body.
# Class M. Not: team / board / staff members of …, "a member of the X group of companies" (the body must be a chamber, association, federation …).
MEM_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])((?:(?:proud(?:ly)?|fi[èe]re?s?|active|actif|accredited|accr[ée]dit[ée]e?|certified|registered|corporate|business)\s+){0,2}(?:members?|membres?)\s+"
                    r"(?:of|de|du|des|de\s+la|de\s+l['’]|d['’])\s*(?:(?:the|la|le|les|l['’]|your|our|votre|notre)\s*)?)", re.I)
MEM_NEG = re.compile(r"team|board|staff|family|famil|crew|band|cast|faculty|committee|comit[ée]|council\s+member|conseil\s+d|founding|honorary|community\s+member|"
                     r"parliament|parlement|legislat|assembl[ée]e\s+nationale|\bMPP?\b|\bMLA\b|\bMNA\b|d[ée]put[ée]|[ée]quipe|personnel|group\s+of\s+companies|groupe\s+d['’]entreprises", re.I)
BODY_RX = re.compile(r"chamber|chambre|board\s+of\s+trade|association|alliance|federation|f[ée]d[ée]ration|institute|institut\b|guild|\bordre\b|corporation\s+des|regroupement|r[ée]seau|"
                     r"society\s+of|soci[ée]t[ée]\s+(?:de|des|canadienne|qu[ée]b[ée]coise)|business\s+improvement|\bBIA\b|\bSDC\b|tourism|tourisme|\bCHBA\b|\bAPCHQ\b|\bACQ\b|\bCFIB\b|\bFCEI\b|"
                     r"home\s+builders|landscape\s+(?:ontario|alberta|nova)|destination\s+\w+|\bcouncil\s+of\b|conseil\s+(?:du|de\s+la|des|canadien|qu[ée]b[ée]cois)|coalition|consortium|co-?op[ée]rative\s+de|union\s+des", re.I)
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
        if not cls:  # no service credit: a membership statement?
            mm = re.search(MEM_RX.pattern + r"[\s|]*$", before, re.I)
            if mm and not MEM_NEG.search(before[max(0, mm.start() - 30):] + " " + label) and BODY_RX.search(label):
                ph, cls, where = mm.group(1), "M", "before"
            else:
                for cand in (attrs, itxt):
                    mi = MEM_RX.search(cand or "")
                    if mi and not MEM_NEG.search(cand) and BODY_RX.search(cand[mi.end():]):
                        ph, cls, where, label = mi.group(1), "M", "inner", cand.strip()[:160]
                        break
        if not cls:
            continue
        if ph.rstrip().endswith(":") and re.fullmatch(r"(?:https?://)?(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)+/?\S*", label.strip().lower()):
            continue  # "Design: https://…" in a list of resources is an address, not a credit
        label = label or "[link to %s]" % host  # a logo without alt text: the link target names the vendor
        if cls in ("D", "P") and m.start() < zone:
            continue  # a bare "designed by" / "powered by" outside the footer zone is usually about a product, not about the site
        q = (before[-150:] + " " + label) if where == "before" else label
        q = re.sub(r"\s+", " ", re.sub(r"(?:\s*\|\s*)+", " | ", q)).strip(" |")[-300:]
        cur = out.get(v)
        if cur is None or "WDPM".index(cls) < "WDPM".index(cur["k"]):
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


FAST_TIMEOUT = 10


def fast_fetch(url, limit=1_500_000, _hops=0):
    """(status, content type, bytes, final url) for the scan: each site is met once, so no per-host waiting list; a 10-second timeout, because
    a list of a million domains holds many that no longer answer (ap_crawler.fetch waits 20 s and keeps a growing table of hosts)"""
    req = urllib.request.Request(url, headers={"User-Agent": C.UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=FAST_TIMEOUT) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", b"", url
    except Exception as ex:
        msg, p = str(ex).lower(), urllib.parse.urlparse(url)
        if _hops == 0 and p.scheme == "https" and ("ssl" in msg or "certificate" in msg or "handshake" in msg or "eof" in msg):
            return fast_fetch("http://" + url[8:], limit, 1)  # broken TLS on a small site: the plain-http copy is the same public page
        if _hops == 0 and ("nodename" in msg or "name or service" in msg or "getaddrinfo" in msg or "no address" in msg) and p.hostname and not p.hostname.startswith("www."):
            return fast_fetch(url.replace("://" + p.hostname, "://www." + p.hostname, 1), limit, 1)  # bare host without a DNS record, www. has one
        return 0, "", b"", url


_fetch = C.fetch  # the vendor step reads several pages of one site: ap_crawler's polite fetch (one request per second per host); the scan switches to fast_fetch


def robots_ok(root, url):
    """(allowed, reachable). No shared cache: a scan meets each host once."""
    st, _, data, _ = _fetch(root + "robots.txt", 300_000)
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
    st, ctype, data, final = _fetch(url, 1_500_000)
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


# ------------------------------------------------------------------------------------------------------------------- web graph
GRAPH_CA = os.path.join(DIR, "graph_ca_domains.csv.gz")      # .ca / .quebec domains the web graph knows (linked from somewhere), beyond the crawled ones
GRAPH_IN = os.path.join(DIR, "graph_inlinks.csv.gz")         # domains that link to a vendor proven in Canada (most footer credits are such links)


def newest_graph():
    try:
        for g in json.loads(CCL.http_get("https://index.commoncrawl.org/graphinfo.json", tries=3)):
            if g.get("id"):
                return g["id"]
    except Exception as e:
        print("graphinfo not reachable (%s): falling back to the last release we read" % type(e).__name__, flush=True)
    return "cc-main-2026-may-jun-jul"


def graph(a):
    """Common Crawl's domain-level web graph (one vertices file, one edges file; 118 M domains, 2.8 G links):
    (1) every .ca / .quebec domain it knows; (2) every domain that links to a vendor already proven in Canada. Both only say which home pages
    are worth one read — a lead still needs the credit line seen live on the site and the vendor's own address."""
    import shutil, subprocess
    rel = a.release if a.release and a.release != "auto" else newest_graph()
    base = a.base or "%sprojects/hyperlinkgraph/%s/domain/%s-domain-" % (CCL.CC, rel, rel)
    cands = [d for d in (a.work, "/mnt/cs", os.environ.get("RUNNER_TEMP") or "", ".") if d]
    work, free = ".", 0
    for d in cands:
        try:
            os.makedirs(d, exist_ok=True)
            st = os.statvfs(d)
            if os.access(d, os.W_OK) and st.f_bavail * st.f_frsize > free:
                work, free = d, st.f_bavail * st.f_frsize
        except OSError:
            pass
    print("web graph %s; work dir %s (%.1f GiB free)" % (rel, work, free / 2 ** 30), flush=True)
    os.makedirs("out", exist_ok=True)
    awk = shutil.which("mawk") or "awk"
    unz = (shutil.which("pigz") or "gzip") + " -dc"
    W = lambda name: os.path.join(work, name)
    sh = lambda cmd: subprocess.run(["bash", "-o", "pipefail", "-c", cmd], check=True)
    curl = "curl -sS -L --fail --retry 10 --retry-delay 10 --retry-all-errors -C - -A '%s'" % CCL.UA

    targets = set(proven_elsewhere()) | {d for d, o in vendor_state().items() if o.get("status") in ("CA", "CA-loc")}
    targets = {d for d in targets if d and not PLATFORM.search(d)}
    tech_t = set()
    try:  # the customer-portal domains of the vetted Canada-HQ software vendors (<clinic>.janeapp.com …): a site that links to its portal is a customer
        import cc_tenants as CT
        tech_t = set(CT.portal_domains())
    except Exception as e:
        print("portal domains not loaded: %s" % e, flush=True)
    targets |= tech_t
    rev = lambda d: ".".join(reversed(d.split(".")))
    with open(W("targets.txt"), "w") as f:
        f.write("\n".join(sorted(rev(d) for d in targets)) + "\n")
    print("targets: %d vendor domains proven in Canada" % len(targets), flush=True)
    t0 = time.time()
    sh("%s -o %s %svertices.txt.gz" % (curl, W("v.gz"), base))
    print("vertices downloaded: %.0f MiB in %.0f s" % (os.path.getsize(W("v.gz")) / 2 ** 20, time.time() - t0), flush=True)
    # one pass over the vertices: ids of the targets; every .ca / .quebec domain
    sh("%s %s | %s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} {if ($2 in t) print $1\"\\t\"$2 > \"%s\"; if (substr($2,1,3)==\"ca.\" || substr($2,1,7)==\"quebec.\") print $2\"\\t\"$3 > \"%s\"}'"
       % (unz, W("v.gz"), awk, W("targets.txt"), W("tv.txt"), W("ca.txt")))
    tid = {}
    if os.path.exists(W("tv.txt")):
        for l in open(W("tv.txt")):
            q = l.split()
            if len(q) >= 2:
                tid[q[0]] = rev(q[1])
    n_ca = 0
    with open("out/graph_ca_domains.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "hosts"])
        if os.path.exists(W("ca.txt")):
            for l in open(W("ca.txt"), encoding="utf-8", errors="replace"):
                q = l.split()
                if q and re.fullmatch(r"[a-z0-9.-]+", q[0]) and q[0].count(".") <= 3:
                    d = rev(q[0])
                    if not PLATFORM.search(d):
                        w.writerow([d, q[1] if len(q) > 1 else ""])
                        n_ca += 1
    print("vertices read in %.0f s: %d of %d targets are in the graph; %d .ca / .quebec domains" % (time.time() - t0, len(tid), len(targets), n_ca), flush=True)
    with open(W("tid.txt"), "w") as f:
        f.write("\n".join(sorted(tid)) + "\n")
    # the edges: links INTO a target
    t0 = time.time()
    flt = "%s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} ($2 in t)' > %s" % (awk, W("tid.txt"), W("hits.txt"))
    if free > 14 * 2 ** 30:
        sh("%s -o %s %sedges.txt.gz" % (curl, W("e.gz"), base))
        print("edges downloaded: %.1f GiB in %.0f s" % (os.path.getsize(W("e.gz")) / 2 ** 30, time.time() - t0), flush=True)
        sh("%s %s | %s" % (unz, W("e.gz"), flt))
        os.remove(W("e.gz"))
    else:  # not enough disk for the 10 GiB file: stream it (a broken stream is started again, at most 3 times)
        for attempt in range(3):
            try:
                sh("curl -sS -L --fail -A '%s' %sedges.txt.gz | %s | %s" % (CCL.UA, base, unz, flt))
                break
            except subprocess.CalledProcessError as e:
                print("edge stream attempt %d failed (%s)" % (attempt + 1, e.returncode), flush=True)
                if attempt == 2:
                    raise
                time.sleep(60)
    print("edges read in %.0f s" % (time.time() - t0), flush=True)
    indeg = collections.Counter()
    for l in open(W("hits.txt")):
        q = l.split()
        if len(q) == 2:
            indeg[q[1]] += 1
    ok_t = {t for t, c in indeg.items() if c <= a.max_indegree or tid.get(t) in tech_t}  # no cap for the vetted portals: their in-links ARE customers
    print("links into targets: %d; targets linked: %d; targets with more than %d linking domains (platform-like, left out): %d — %s"
          % (sum(indeg.values()), len(indeg), a.max_indegree, len(indeg) - len(ok_t), ", ".join("%s %d" % (tid.get(t, t), c) for t, c in indeg.most_common(12))), flush=True)
    src, src_tech = collections.Counter(), collections.defaultdict(set)
    try:
        vkey_of = CT.portal_domains()
    except Exception:
        vkey_of = {}
    for l in open(W("hits.txt")):
        q = l.split()
        if len(q) == 2 and q[1] in ok_t and q[0] not in tid:
            src[q[0]] += 1
            if tid.get(q[1]) in tech_t:
                src_tech[q[0]].add(vkey_of.get(tid[q[1]], tid[q[1]]))
    src = {f: c for f, c in src.items() if c <= 5 or f in src_tech}  # a domain linking to many vendors is a directory, not a client
    with open(W("fid.txt"), "w") as f:
        f.write("\n".join(src) + "\n")
    sh("%s %s | %s 'BEGIN{while((getline l < \"%s\") > 0) t[l]=1} ($1 in t){print $1\"\\t\"$2\"\\t\"$3}' > %s" % (unz, W("v.gz"), awk, W("fid.txt"), W("fv.txt")))
    n_in = 0
    with open("out/graph_inlinks.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "targets", "hosts", "tech"])
        for l in open(W("fv.txt"), encoding="utf-8", errors="replace"):
            q = l.split()
            if len(q) < 2 or not re.fullmatch(r"[a-z0-9.-]+", q[1]) or q[1].count(".") > 3:
                continue
            d = rev(q[1])
            try:
                hosts = int(q[2]) if len(q) > 2 else 1
            except ValueError:
                hosts = 1
            if hosts > 30 or PLATFORM.search(d):
                continue
            w.writerow([d, src.get(q[0], 1), hosts, ",".join(sorted(src_tech.get(q[0], ())))])
            n_in += 1
    print("graph %s: %d domains link to a vendor proven in Canada (1-5 such vendors each); %d of them link to a vetted customer portal: %s"
          % (rel, n_in, len(src_tech), dict(collections.Counter(v for vs in src_tech.values() for v in vs))), flush=True)


OSM_SITES = os.path.join(DIR, "osm_sites.csv.gz")  # websites of OpenStreetMap objects in Canada (shops, offices, clinics, restaurants …), any TLD


def osm(a):
    """OpenStreetMap, Canada extract (Geofabrik): every object with a website tag -> its host, name and place. Organisations located in
    Canada whose site is on .com / .org as well as .ca: more home pages worth one read (the credit line and the mailbox come from the site)."""
    import shutil, subprocess
    work = a.work or os.environ.get("RUNNER_TEMP") or "."
    for d in (a.work, "/mnt/cs"):
        if d and os.path.isdir(d) and os.access(d, os.W_OK):
            work = d
            break
    os.makedirs("out", exist_ok=True)
    if not shutil.which("osmium"):
        sys.exit("osmium-tool is not installed (apt-get install osmium-tool)")
    W = lambda name: os.path.join(work, name)
    sh = lambda cmd: subprocess.run(["bash", "-o", "pipefail", "-c", cmd], check=True)
    url = a.base or "https://download.geofabrik.de/north-america/canada-latest.osm.pbf"
    t0 = time.time()
    sh("curl -sS -L --fail --retry 8 --retry-delay 10 --retry-all-errors -C - -A '%s' -o %s %s" % (CCL.UA, W("canada.osm.pbf"), url))
    print("extract downloaded: %.1f GiB in %.0f s" % (os.path.getsize(W("canada.osm.pbf")) / 2 ** 30, time.time() - t0), flush=True)
    sh("osmium tags-filter %s nwr/website nwr/contact:website nwr/url -o %s --overwrite" % (W("canada.osm.pbf"), W("sites.osm.pbf")))
    sh("osmium cat %s -f opl -o %s --overwrite" % (W("sites.osm.pbf"), W("sites.opl")))
    print("objects with a website tag extracted in %.0f s" % (time.time() - t0), flush=True)
    unq = lambda v: re.sub(r"%([0-9a-fA-F]+)%", lambda m: chr(int(m.group(1), 16)), v)
    KIND = ("shop", "amenity", "office", "craft", "tourism", "healthcare", "leisure", "club", "industrial", "man_made", "emergency", "landuse", "building")
    sites, n_obj = {}, 0
    for l in open(W("sites.opl"), encoding="utf-8", errors="replace"):
        m = re.search(r" T(\S*)", l)
        if not m:
            continue
        tags = {}
        for kv in m.group(1).split(","):
            k, _, v = kv.partition("=")
            tags[unq(k)] = unq(v)
        w = tags.get("website") or tags.get("contact:website") or tags.get("url") or ""
        h = host_of(w.split(";")[0].strip())
        if not h or "." not in h or PLATFORM.search(h) or not re.fullmatch(r"[a-z0-9.-]+", h):
            continue
        n_obj += 1
        kind = next(("%s=%s" % (k, tags[k]) for k in KIND if tags.get(k) and tags[k] != "yes"), "")
        o = sites.get(h)
        if o is None:
            sites[h] = [h, (tags.get("name") or tags.get("operator") or "")[:100], tags.get("addr:city") or "", tags.get("addr:province") or tags.get("addr:state") or "", tags.get("addr:postcode") or "", kind, 1]
        else:
            o[6] += 1
    with open("out/osm_sites.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dom", "name", "city", "province", "postcode", "kind", "objects"])
        for h in sorted(sites):
            w.writerow(sites[h])
    tl = collections.Counter(h.rsplit(".", 1)[-1] for h in sites)
    print("OpenStreetMap Canada: %d objects with a website, %d distinct hosts (%s)" % (n_obj, len(sites), ", ".join("%s %d" % kv for kv in tl.most_common(6))), flush=True)


def merge_graph(a):
    os.makedirs(DIR, exist_ok=True)
    for name, path, cols in (("graph_ca_domains.csv", GRAPH_CA, ["dom", "hosts"]), ("graph_inlinks.csv", GRAPH_IN, ["dom", "targets", "hosts", "tech"]),
                             ("osm_sites.csv", OSM_SITES, ["dom", "name", "city", "province", "postcode", "kind", "objects"])):
        rows = {}
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                rows = {r["dom"]: r for r in csv.DictReader(fh)}
        n0 = len(rows)
        for f in sorted(glob.glob(os.path.join(a.dir, name))):
            for r in csv.DictReader(open(f, encoding="utf-8")):
                if r.get("dom"):
                    rows[r["dom"]] = r
        if rows:
            with gzip.open(path, "wt", encoding="utf-8", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
                w.writeheader()
                for d in sorted(rows):
                    w.writerow(rows[d])
        print("%s: %d domains (+%d this run)" % (os.path.basename(path), len(rows), len(rows) - n0))


# ------------------------------------------------------------------------------------------------------------------- scan
DETECTOR = 3  # 1: credit lines + the vendor table of 2026-11-02; 2 ("t2"): + Jobber; 3 ("t3"): + membership statements (class M)


def done_versions():
    """{site: detector version of its latest read} from the append-only done files"""
    ver = {}
    for l in state_lines("done"):
        q = l.split("\t")
        v = 3 if "t3" in q[5:] else 2 if "t2" in q[5:] else 1
        if v > ver.get(q[0], 0):
            ver[q[0]] = v
    return ver


def scan_queue(k, n, limit=0):
    ver = done_versions()
    seen, tasks = set(), []

    def add(host, pri, extra=0, again=False):
        """a site read by an older detector (done line without the current mark) is read once more: right away when the web graph says it
        links to a vetted portal (again), otherwise after every site that was never read"""
        if not host or "." not in host or host in seen or PLATFORM.search(host) or not shard_ok(host, k, n):
            return
        v = ver.get(host)
        if v is not None:
            if v >= DETECTOR:
                return
            pri = pri if again else pri + 10
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
    if os.path.exists(GRAPH_IN):  # 3. sites that link to a vendor proven in Canada (web graph): most footer credits are such links
        with gzip.open(GRAPH_IN, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 2 if r.get("tech") else 3, int(r.get("targets") or 1), again=bool(r.get("tech")))
    if os.path.exists(OSM_SITES):  # 3. organisations OpenStreetMap places in Canada (any TLD); chains with hundreds of branches last
        with gzip.open(OSM_SITES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 3, -min(int(r.get("objects") or 1), 400))
    if os.path.exists(UNIVERSE):  # 4. every .ca site of the archive, the sites with the most captured pages first
        with gzip.open(UNIVERSE, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 4, min(int(r.get("pages") or 0), 500))
    if os.path.exists(GRAPH_CA):  # 5. .ca domains the web graph knows only as link targets (many are gone: one failed request each)
        with gzip.open(GRAPH_CA, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                add(r["dom"], 5)
    tasks.sort()
    if limit:
        tasks = tasks[:limit]
    return [{"dom": h, "pri": pri} for pri, _, h in tasks], len(ver)


def scan(a):
    import lead_crawl as LC
    import tech_relationships as T
    global _fetch
    _fetch = fast_fetch
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    tasks, n_done = scan_queue(k, n, a.limit)
    print("shard %d/%d: %d sites to read (%d read before): %s" % (k, n, len(tasks), n_done, dict(collections.Counter(t["pri"] for t in tasks))), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fs = open("out/credit_seen_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/credit_done_%d.tsv" % k, "a", encoding="utf-8")
    assets_of = lambda b: " ".join(T.SRC_RE.findall(b) + T.LINKTAG_RE.findall(b) + T.INLINE_RE.findall(b)[:40])
    # which outside services do these sites load or post to? (script / iframe / form targets, counted per registrable domain) — the frequency
    # table shows which Canada-based platforms are worth vetting for the vendor table of tools/tech_relationships.py
    ext = collections.Counter()

    def embedded(raw, final, site_dom):
        out = set()
        for rx in (T.SRC_RE, T.FORM_RE):
            for x in rx.findall(raw)[:400]:
                try:
                    h = (urllib.parse.urlparse(urllib.parse.urljoin(final, html.unescape(x).strip())).hostname or "").lower()
                except ValueError:
                    continue
                d = C.registrable(h) if h and "." in h else ""
                if d and d != site_dom:
                    out.add(d)
        return out

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
                emb = embedded(raw, final, C.registrable(fhost))
                with lock:
                    ext.update(emb)
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
            fd.write("%s\t%s\t%s\t%d\t%d\tt3\n" % (dom, TODAY, res, len(rec["credits"]) if rec else 0, len(rec["tech"]) if rec else 0))
            if stats["sites"] % 2000 == 0:
                fs.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    def on_timeout(t):
        with lock:
            fd.write("%s\t%s\ttimeout\t0\t0\tt3\n" % (t["dom"], TODAY))
            stats["timeout"] += 1
    left = LC.run_pool(tasks, one, a, deadline, on_timeout)
    with lock:
        fs.close(); fd.close()
        with open("out/credit_ext_%d.tsv" % k, "w", encoding="utf-8") as f:
            for d, c in ext.most_common(30000):
                if c >= 2:
                    f.write("%s\t%d\n" % (d, c))
    print("finished", dict(stats), "(stragglers left: %d)" % left, flush=True)


# ------------------------------------------------------------------------------------------------------------------- vendors
CONTACT_RX = re.compile(r"contact|joindre|coordonn|about|propos|qui-sommes|nous-trouver|find-us|location|bureaux|offices?|impressum|legal|mentions|privacy|confidentialit|terms|conditions|politique", re.I)
_PROVN = (r"Qu[ée]bec|Ontario|British Columbia|Colombie-Britannique|Alberta|Manitoba|Saskatchewan|Nova Scotia|Nouvelle-[ÉE]cosse|New Brunswick|Nouveau-Brunswick|"
          r"Newfoundland(?: and Labrador)?|Terre-Neuve(?:-et-Labrador)?|Prince Edward Island|[ÎI]le-du-Prince-[ÉE]douard|Yukon|Nunavut|Northwest Territories")
# "Halifax, Nova Scotia" · "Montréal (Québec)" · "Toronto, ON" · "Saskatchewan, Canada": the vendor's own statement of where it is (no postal code)
LOC_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])([A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+(?:[ \-][A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+){0,3})\s*(?:,\s*|\(\s*)(?:(" + _PROVN + r")|(QC|Qc|ON|BC|AB|MB|SK|NS|NB|NL|PE|PEI|YT|NT|NU))\)?"
                    r"(?:,?\s*Canada)?(?![A-Za-zÀ-ÿ])(?!,?\s*(?:CA|California|USA?)\b)(?!\s+\d{5})")
CANADA_LINE_RX = re.compile(r"(?<![A-Za-zÀ-ÿ])(" + _PROVN + r"),?\s+Canada(?![A-Za-zÀ-ÿ])")
CA_PHONE_RX = re.compile(r"(?<![\d.])(?:\+?1[\s.\-]?)?\(?(204|226|236|249|250|263|289|306|343|354|365|367|368|382|403|416|418|428|431|437|438|450|468|474|506|514|519|548|579|581|584|587|604|613|639|"
                         r"647|672|683|705|709|742|753|778|780|782|807|819|825|867|873|879|902|905)\)?[\s.\-]{0,2}\d{3}[\s.\-]?\d{4}(?![\d.])")
LD_PC_RX = re.compile(r'"postalCode"\s*:\s*"\s*([ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ \-]?\d[ABCEGHJ-NPRSTV-Z]\d)\s*"', re.I)
LD_FIELD_RX = re.compile(r'"(streetAddress|addressLocality|addressRegion|postalCode|addressCountry)"\s*:\s*"([^"]{1,90})"')


def jsonld_address(raw):
    """a schema.org PostalAddress with a Canadian postal code in the page source: 'streetAddress: …, addressLocality: …, postalCode: …'"""
    m = LD_PC_RX.search(raw)
    if not m:
        return ""
    seg, got = raw[max(0, m.start() - 500):m.end() + 300], {}
    for k, v in LD_FIELD_RX.findall(seg):
        got.setdefault(k, v.strip())
    return ", ".join("%s: %s" % (k, got[k]) for k in ("streetAddress", "addressLocality", "addressRegion", "postalCode", "addressCountry") if got.get(k))[:220]


def location_line(text):
    """(quote, phone) when the page states a Canadian province next to a place name AND prints a telephone number with a Canadian area code"""
    ph = CA_PHONE_RX.search(text)
    if not ph:
        return "", ""
    m = CANADA_LINE_RX.search(text) or LOC_RX.search(text)
    if not m:
        return "", ""
    return re.sub(r"\s+", " ", text[max(0, m.start() - 40):m.end()]).strip(), ph.group(0).strip()
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
    """one record per site: the latest read, plus what an earlier read saw and the latest did not (a site read again by a newer detector)"""
    out = {}
    for l in state_lines("seen"):
        try:
            o = json.loads(l)
        except ValueError:
            continue
        if not o.get("dom"):
            continue
        old = out.get(o["dom"])
        if old:
            have = {c["v"] for c in o.get("credits") or []}
            o["credits"] = (o.get("credits") or []) + [c for c in old.get("credits") or [] if c["v"] not in have]
            havet = {(t["v"], t["slug"]) for t in o.get("tech") or []}
            o["tech"] = (o.get("tech") or []) + [t for t in old.get("tech") or [] if (t["v"], t["slug"]) not in havet]
        out[o["dom"]] = o
    return out


def vendors(a):
    import lead_crawl as LC
    import tech_relationships as T
    k, n = CCL.shard_of(a)
    os.makedirs("out", exist_ok=True)
    # rule 2 (2026-11-10): schema.org address data, privacy / terms pages, the location line. Vendors that gave "no_address" under rule 1 are read again
    have, known = {d: o for d, o in vendor_state().items() if not (o.get("status") == "no_address" and (o.get("rule") or 1) < 2)}, proven_elsewhere()
    cnt = collections.Counter()
    for o in sightings().values():
        for c in o.get("credits") or []:
            cnt[c["v"]] += 1
    tasks = [{"dom": v, "n": c} for v, c in cnt.most_common() if v not in have and v not in known and shard_ok(v, k, n) and not PLATFORM.search(v)]
    # the row factory's vendors whose client page (and archived contact page) printed no address: 11,096 domains, 39,313 buyer domains wait on them.
    # Their live home / contact / legal page is read the same way; tools/cc_clients.py merge promotes their client links when the proof is found.
    rf = collections.Counter()
    for o in CCL._side_records():
        vd = ((o.get("row") or {}).get("vendor_key") or "")[3:]
        if vd:
            rf[vd] += 1
    queued = {t["dom"] for t in tasks}
    arch = CCL._vendor_addrs()
    tasks += [{"dom": v, "n": c} for v, c in rf.most_common() if v not in have and v not in arch and v not in queued and shard_ok(v, k, n) and not PLATFORM.search(v)]
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d credited vendor domains to check (%d checked before, %d proven by the row factory)" % (k, n, len(tasks), len(have), len(known)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fv = open("out/credit_vendors_%d.jsonl" % k, "a", encoding="utf-8")
    ADDRS = (("CA", CCL.ADDR), ("US", LC.US_ADDR), ("GB", LC.GB_ADDR), ("AU", LC.AU_ADDR))

    def addresses_in(raw):
        """{country: quote} for every postal address form found on one page (visible text, then schema.org data in the source), + the location line"""
        text, out = C.visible(raw), {}
        for cc, rx in ADDRS:
            m = rx.search(text)
            if m:
                out[cc] = re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:]
        if "CA" not in out:
            j = jsonld_address(raw)
            if j:
                out["CA"] = "%s (schema.org PostalAddress in the page source)" % j
        loc, phone = location_line(text)
        if loc:
            out["loc"] = "%s … tel. %s" % (loc, phone)
        return out

    def one(t):
        if time.time() > deadline:
            return
        dom = t["dom"]
        rec = {"dom": dom, "date": TODAY, "seen_on": t["n"], "status": "", "quote": "", "url": "", "name": "", "title": "", "desc": "", "service_words": "", "also_prints": "", "rule": 2}
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
                found = {}  # country (or "loc") -> (quote, url); a Canadian postal address anywhere on the pages read wins
                for cc, q in addresses_in(raw).items():
                    found[cc] = (q, final)
                if "CA" not in found:
                    links, seen_l = [], set()
                    for link, label in C.links(raw, final):
                        p = urllib.parse.urlparse(link)
                        if p.scheme in ("http", "https") and C.registrable((p.hostname or "").lower()) == C.registrable(fhost) and not C.SKIP_EXT.search(p.path) \
                                and CONTACT_RX.search(p.path + " " + label) and link.split("#")[0] not in seen_l and link.split("#")[0].rstrip("/") != final.rstrip("/"):
                            seen_l.add(link.split("#")[0])
                            links.append((0 if re.search(r"contact|joindre|coordonn", p.path + " " + label, re.I) else 1, len(p.path), link.split("#")[0]))
                    todo = [u for _, _, u in sorted(links)[:4]] or ["https://%s/contact" % fhost, "https://%s/contact-us" % fhost, "https://%s/nous-joindre" % fhost]
                    for u in todo:
                        if time.time() > deadline + 120:
                            break
                        r2, f2, raw2 = get_page(u, check_robots=False) if C.allowed(u) else ("robots", u, "")
                        if r2 != "ok":
                            continue
                        for cc, q in addresses_in(raw2).items():
                            found.setdefault(cc, (q, f2))
                        if "CA" in found:
                            break
                other = sorted(c for c in found if c not in ("CA", "loc"))
                rec["also_prints"] = ",".join(other)
                if "CA" in found:
                    rec["status"], rec["quote"], rec["url"] = "CA", found["CA"][0], found["CA"][1]
                elif other:  # a postal address elsewhere and none in Canada: located there
                    rec["status"], rec["quote"], rec["url"] = other[0], found[other[0]][0], found[other[0]][1]
                elif "loc" in found:  # no postal code anywhere: the site's own location line (a Canadian province) + a Canadian telephone number
                    rec["status"], rec["quote"], rec["url"] = "CA-loc", found["loc"][0], found["loc"][1]
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
    ver_before = done_versions()
    done_before = set(ver_before)
    new_done, st_count = {}, collections.Counter()
    for f in sorted(glob.glob(os.path.join(d, "credit_done_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and len(q) >= 3 and (3 if "t3" in q[5:] else 2 if "t2" in q[5:] else 1) > ver_before.get(q[0], 0):
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
                old = vstate.get(o["dom"])
                if old is None or (old.get("status") == "no_address" and (old.get("rule") or 1) < 2 and (o.get("rule") or 1) >= 2):
                    new_v[o["dom"]] = json.dumps(o, ensure_ascii=False)
            except (ValueError, KeyError):
                pass
    n_v = _append_state("vendors", stamp, [new_v[k] for k in sorted(new_v)])
    extc = collections.Counter()
    for f in sorted(glob.glob(os.path.join(d, "credit_ext_*.tsv"))):
        for l in open(f, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) == 2 and q[1].isdigit():
                extc[q[0]] += int(q[1])
    if extc:  # outside services loaded by the sites read in this run (top 20,000): a table to vet new Canada-based platforms from
        _append_state("ext", stamp, ["%s\t%d" % kv for kv in extc.most_common(20000)])
    if n_done or n_seen:
        print("credit scan: %d sites read this run (%s); %d with a credit or a vetted service" % (n_done, ", ".join("%s %d" % kv for kv in st_count.most_common(8)), n_seen))
    # ---- leads: sightings whose vendor is proven in Canada
    vstate, known_v, seen = vendor_state(), proven_elsewhere(), sightings()
    def proof(v):
        o = vstate.get(v)
        if o and o.get("status") == "CA" and o.get("quote"):
            return ("%s (as printed on %s, read %s)" % (CCL.address_from(o["quote"]) if "schema.org" not in o["quote"] else o["quote"], o.get("url") or "", o.get("date") or ""), o.get("url") or "", o.get("name") or "",
                    bool(o.get("service_words")), "the vendor's own site prints its Canadian postal address")
        if o and o.get("status") == "CA-loc" and o.get("quote"):
            return ("“%s” (as printed on %s, read %s)" % (o["quote"], o.get("url") or "", o.get("date") or ""), o.get("url") or "", o.get("name") or "",
                    bool(o.get("service_words")), "the vendor's own site gives its location in Canada and a Canadian telephone number (no postal code printed)")
        if v in known_v:
            return known_v[v] + (True, "the vendor's own site prints its Canadian postal address")  # the row factory read its client / portfolio page: a firm that sells services
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
    try:
        import tech_relationships as T
        VETTED = set(T.VENDOR_BASES)
    except Exception:
        VETTED = set()
    vend_n = collections.Counter(c["v"] for o in seen.values() for c in (o.get("credits") or []))
    for dom in sorted(seen):
        o = seen[dom]
        site = o.get("site") or dom
        best = None
        for c in o.get("credits") or []:
            if c["k"] == "M":
                stats["membership statements seen"] += 1
                continue
            stats["credit links seen"] += 1
            v = c["v"]
            if v == C.registrable(site) or (c["k"] == "P" and FREE_PLAN.search(v)) or vend_n[v] > 20000 or v in VETTED:
                continue  # the vetted software vendors have their own acceptance rules (tools/tech_relationships.py): never through a credit line
            pr = proof(v)
            if not pr:
                stats["vendor not proven in Canada (yet)"] += 1
                continue
            if c["k"] in ("D", "P") and vend_n[v] < 2 and not pr[3]:
                stats["design / powered-by credit of a vendor seen once whose own site names no web / design / software service (kept out)"] += 1
                continue
            if best is None or "WDP".index(c["k"]) < "WDP".index(best[0]["k"]):
                best = (c, pr)
        # membership stated on the member's own site -> its own lead (dues: the member pays the body), when the body is proven in Canada
        for c in o.get("credits") or []:
            if c["k"] != "M" or c["v"] == C.registrable(site) or c["v"] in VETTED:
                continue
            pr = proof(c["v"])
            if not pr:
                continue
            bname = pr[2] or re.sub(r"^.*?(?:members?|membres?)\s+(?:of|de|du|des|de\s+la|de\s+l['’]|d['’])\s*(?:(?:the|la|le|les|l['’])\s*)?", "", c.get("t") or "", flags=re.I).strip()[:90] or c["v"]
            if not BODY_RX.search(bname + " " + (c.get("t") or "")):
                continue
            mkey = "lead:" + hashlib.sha1(("%s|member:%s" % (site, c["v"])).encode()).hexdigest()[:16]
            if mkey in main_keys:
                continue
            stats["new member leads" if mkey not in prev else "member leads kept"] += 1
            prev[mkey] = {"buyer_key": mkey, "buyer_name": o.get("name") or site, "website": "https://%s/" % site, "canadian_vendor_rows": 1, "example_vendor": bname,
                          "canada_field_value": "membership / statutory fee relationship (member badge on the buyer's own site)=%s; %s: %s" % (c["v"], pr[4], pr[0][:240]),
                          "evidence_dataset": o.get("page") or "https://%s/" % site, "latest_record_date": o.get("date") or TODAY}
            pdet[mkey] = {"key": mkey, "platform": "site_member_cc", "record_url": o.get("page") or "", "vendor": bname, "record_date": o.get("date") or "",
                          "title": "membership of %s — stated on the member's own site: “%s”" % (bname, c["q"][-180:]),
                          "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % c["v"], "credit_quote": c["q"], "credit_class": "M",
                          "credit_link_text": c.get("t") or "", "vendor_location_basis": pr[4], "page_title": o.get("title") or ""}
            break
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
                     "canada_field_value": "%s=%s; %s: %s" % (CF_CREDIT, c["v"], pr[4], pr[0][:260]),
                     "evidence_dataset": o.get("page") or "https://%s/" % site, "latest_record_date": o.get("date") or TODAY}
        pdet[key] = {"key": key, "platform": "site_credit_cc", "record_url": o.get("page") or "", "vendor": vname, "record_date": o.get("date") or "",
                     "title": "%s by %s — credit printed on the buyer's own site: “%s”" % (what, vname, c["q"][-180:]),
                     "vendor_address": pr[0], "vendor_address_url": pr[1], "vendor_site": "https://%s/" % c["v"], "credit_quote": c["q"], "credit_class": c["k"], "credit_phrase": c.get("p") or "",
                     "credit_link_text": c.get("t") or "", "credit_link_host": c.get("vh") or c["v"], "vendor_seen_on_sites": vend_n[c["v"]], "page_title": o.get("title") or "",
                     "vendor_location_basis": pr[4], "vendor_also_prints_addresses_in": (vstate.get(c["v"]) or {}).get("also_prints") or ""}
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
    ap.add_argument("cmd", choices=["universe", "merge-universe", "graph", "osm", "merge-graph", "scan", "vendors", "merge"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--crawl", default="auto")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=120)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--release", default="auto", help="graph: web-graph release id (auto = newest)")
    ap.add_argument("--work", default="", help="graph: directory for the downloaded files")
    ap.add_argument("--base", default="", help="graph: URL prefix of the vertices / edges files (tests)")
    ap.add_argument("--max-indegree", type=int, default=5000, help="graph: a vendor linked from more domains than this is platform-like (its links are not credits)")
    ap.add_argument("--max-shopify", type=int, default=15000, help="merge: at most this many new Shopify-store candidates per run (owner 2026-11-09: no lane may crowd out the others)")
    ap.add_argument("--straggler-seconds", type=float, default=180)
    ap.add_argument("--site-seconds", type=float, default=150)
    a = ap.parse_args()
    if a.cmd in ("scan", "vendors"):
        os.makedirs(C.STATE, exist_ok=True)
        {"scan": scan, "vendors": vendors}[a.cmd](a)
        sys.stdout.flush()
        os._exit(0)  # do not wait for straggler threads
    {"universe": universe, "merge-universe": merge_universe, "graph": graph, "osm": osm, "merge-graph": merge_graph, "merge": merge}[a.cmd](a)


if __name__ == "__main__":
    main()

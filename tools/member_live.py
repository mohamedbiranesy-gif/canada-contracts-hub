#!/usr/bin/env python3
"""Member directories, read live (cloud): the members of a Canadian chamber of commerce, board of trade or trade association pay it dues, and
the body's own directory names each member with its address, telephone and website. The row factory already reads the member pages the
Common Crawl archive happens to hold (40,484 pages on 71 directory hosts); this engine reads the directories themselves, complete and current.

Directories of the GrowthZone / ChamberMaster family have one structure everywhere: /list/searchalpha/<letter> lists the members by initial,
/list/member/<name>-<id> is one member. The member page is parsed by the same code as the archived ones (tools/cc_clients.py leads_of): the
member's own website is the single link labelled as a website; the member's printed address is kept; the body is proven to be in Canada by
its own printed postal address (on the member page when it prints one, otherwise by the address pass / the live vendor check).

  hosts                      list the directory hosts known (archive index + hosts found by `discover`)
  discover --shard K/N       probe the .ca domains whose name says chamber / chambre / board of trade (and their business. / members. / web.
                             hosts) for a /list/ directory of this family -> out/member_hosts_<K>.csv
  index-hosts [--crawl ID]   every host with /list/member/ pages in the Common Crawl index, on any domain (one scan of the index, ~10 minutes)
                             -> data/incoming/claude/claude_member_index_hosts.csv (host, member_pages, crawl)
  discover-index --shard K/N each of those hosts not judged before is read once: its /list/ page (is it a directory of this family, whose is
                             it), then the body's own home page when the directory prints no postal address. Kept: a body whose own page
                             prints a Canadian postal address -> out/member_hosts_<K>.csv + out/cc_vendor_addr_<K>.jsonl (the address, quoted)
                             + out/member_judged_<K>.tsv (every host with its outcome: a directory abroad is not asked again)
  crawl --shard K/N          read each directory's alphabetical lists, then each member page not read before (archive or live)
                             -> out/cc_leads_<K>.jsonl, out/cc_leads_noaddr_<K>.jsonl, out/cc_extract_done_<K>.tsv  (the files `cc_clients.py merge` takes)
  merge-hosts DIR            -> data/incoming/claude/claude_member_hosts.csv
Politeness: every directory of the family is served by the same platform, so ALL requests of a runner share one queue: 2 requests per
second towards the platform, whatever the number of chambers. robots.txt respected, identified user agent. No AI, no search engine.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402

INC = CCL.INC
HOSTS = os.path.join(INC, "claude_member_hosts.csv")
HOST_COLS = ["host", "dom", "basis", "found", "how", "name"]
INDEX_HOSTS = os.path.join(INC, "claude_member_index_hosts.csv")   # host, member_pages, crawl — every host with /list/member/ pages in the archive index
JUDGED = os.path.join(INC, "claude_member_hosts_judged.tsv")        # host, date, outcome, body's domain — one line per index host read by discover-index
# the platform's own domains: a directory there is one tenant among thousands (the body's own domain is found on the page, not in the host name)
PLATFORM_DOM = re.compile(r"(^|\.)(chambermaster\.com|chambermasterdev\.com|growthzoneapp\.com|growthzonesites\.com|growthzonecms\.com|growthzone\.com|micronetonline\.com|memberzone\.org)$", re.I)
NOT_OWN = re.compile(r"(^|\.)(facebook|fb|twitter|x|linkedin|instagram|youtube|youtu|pinterest|tiktok|google|goo|apple|microsoft|flickr|vimeo|constantcontact|mailchimp|list-manage|eventbrite|paypal|issuu|"
                     r"threads|whatsapp|yelp|tripadvisor|adobe|bit|t|wa|linktr|zoom|canada|gc)\.[a-z.]{2,6}$", re.I)
US_ZIP = re.compile(r"\b(?:A[LKZR]|C[AOT]|DE|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY]|DC)\.?,?\s+\d{5}(?:-\d{4})?\b")
TODAY = time.strftime("%Y-%m-%d")
MEMBER_HREF = re.compile(r"""href\s*=\s*["']([^"'#?]*/list/member/[^"'#?/]+)/?["'#?]""", re.I)
FAMILY = re.compile(r"chambermaster|growthzone|micronet|mn-directory|gz-directory|gz-list|mn-listing|/list/(?:member|category|ql|searchalpha)/", re.I)
CHAMBER = re.compile(r"chamber|chambre|cham\b|boardoftrade|board-of-trade|\bbot\b|cci[a-z]|ccq|commerce|bia\b|association|assoc|builders|tourism|tourisme|\bhba\b", re.I)
ALPHA = list("abcdefghijklmnopqrstuvwxyz") + ["0-9"]

_gate, _next = threading.Lock(), [0.0]
_fetch0 = C.fetch


def fetch(url, limit=3_000_000):
    """one queue per runner: the directories of this family sit on one platform"""
    with _gate:
        t = max(time.time(), _next[0])
        _next[0] = t + 0.5
    w = t - time.time()
    if w > 0:
        time.sleep(w)
    return _fetch0(url, limit)


def known_hosts():
    """{host: (dom, basis, name)}: directory hosts of the archive index (.ca), then the hosts found by `discover` / `discover-index`"""
    out = {}
    if os.path.exists(CCL.PAGES):
        with gzip.open(CCL.PAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r.get("cls") == "member" and CCL._M1_RX.search((r.get("path") or "").lower()):
                    out.setdefault(r["host"], (r.get("dom") or C.registrable(r["host"]), r.get("basis") or "", ""))
    if os.path.exists(HOSTS):
        for r in csv.DictReader(open(HOSTS, encoding="utf-8")):
            out.setdefault(r["host"], (r.get("dom") or C.registrable(r["host"]), r.get("basis") or "", r.get("name") or ""))
    # a directory under the platform's own domain (xyz.chambermaster.com) is one tenant among thousands, most of them abroad: it is read only
    # when discover-index found whose it is (the body's own domain, never the platform's)
    return {h: v for h, v in out.items() if not CCL.MULTI_TENANT.search(v[0]) and (not CCL.MULTI_TENANT.search(h) or C.registrable(h) != v[0])}


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def discover(a):
    import credit_scan as CS
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    n = max(1, n)
    os.makedirs("out", exist_ok=True)
    known = known_hosts()
    known_dom = {v[0] for v in known.values()}
    probed = set()
    if os.path.exists(HOSTS + ".probed"):
        probed = {l.strip() for l in open(HOSTS + ".probed", encoding="utf-8")}
    doms = []
    for path in (CS.UNIVERSE, CS.GRAPH_CA, CS.OSM_SITES):
        if os.path.exists(path):
            with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    d = C.registrable(r["dom"])
                    if d.endswith(".ca") and CHAMBER.search(d.split(".")[0]) and d not in known_dom and d not in probed and shard_ok(d, k, n):
                        doms.append(d)
    doms = sorted(set(doms))
    if a.limit:
        doms = doms[:a.limit]
    print("shard %d/%d: %d .ca domains with a chamber / association name to probe (%d directory hosts known)" % (k, n, len(doms), len(known)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/member_hosts_%d.csv" % k, "w", newline="", encoding="utf-8")
    w = csv.writer(fo)
    w.writerow(HOST_COLS)
    fp = open("out/member_probed_%d.txt" % k, "w", encoding="utf-8")

    def one(d):
        if time.time() > deadline:
            return
        hit = None
        try:
            # the home page says where the directory is (a link to business.<domain>/list/ or /list/ on the site itself)
            st, ct, data, final = _fetch0("https://%s/" % d, 800_000)
            if st == 200 and data:
                raw = data.decode("utf-8", "replace")
                cands = set()
                for m in re.finditer(r"""href\s*=\s*["'](https?://[^"'#?\s]+?)/list(?:/[^"']*)?["']""", raw, re.I):
                    h = (urllib.parse.urlparse(m.group(1)).hostname or "").lower()
                    if h and C.registrable(h) == d:
                        cands.add(h)
                if re.search(r"""href\s*=\s*["']/list(?:/[^"']*)?["']""", raw, re.I):
                    cands.add((urllib.parse.urlparse(final).hostname or d).lower())
                for h in sorted(cands)[:3]:
                    u = "https://%s/list/" % h
                    if not C.allowed(u):
                        continue
                    s2, _, d2, _ = fetch(u, 800_000)
                    if s2 == 200 and d2 and FAMILY.search(d2.decode("utf-8", "replace")):
                        hit = h
                        break
        except Exception:
            stats["errors"] += 1
        with lock:
            stats["probed"] += 1
            fp.write(d + "\n")
            if hit:
                stats["directories_found"] += 1
                w.writerow([hit, d, "", TODAY, "its /list/ page carries the directory family's markers"])
            if stats["probed"] % 200 == 0:
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, doms))
    fo.close(); fp.close()
    print("finished", dict(stats), flush=True)


def merge_hosts(a):
    rows = {}
    if os.path.exists(HOSTS):
        rows = {r["host"]: r for r in csv.DictReader(open(HOSTS, encoding="utf-8"))}
    n0 = len(rows)
    for f in sorted(glob.glob(os.path.join(a.dir, "member_hosts_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("host"):
                rows.setdefault(r["host"], r)
    with open(HOSTS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HOST_COLS)
        w.writeheader()
        for h in sorted(rows):
            w.writerow({c: rows[h].get(c, "") for c in HOST_COLS})
    probed = set()
    if os.path.exists(HOSTS + ".probed"):
        probed = {l.strip() for l in open(HOSTS + ".probed", encoding="utf-8")}
    for f in sorted(glob.glob(os.path.join(a.dir, "member_probed_*.txt"))):
        probed |= {l.strip() for l in open(f, encoding="utf-8")}
    with open(HOSTS + ".probed", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(x for x in probed if x)) + "\n")
    judged = {}
    for f in [JUDGED] + sorted(glob.glob(os.path.join(a.dir, "member_judged_*.tsv"))):
        if os.path.exists(f):
            for l in open(f, encoding="utf-8"):
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    judged[q[0]] = l.rstrip("\n")
    if judged:
        with open(JUDGED, "w", encoding="utf-8") as f:
            f.write("\n".join(judged[h] for h in sorted(judged)) + "\n")
    oc = collections.Counter((l.split("\t") + ["", "", ""])[2].split(":")[0] for l in judged.values())
    print("index hosts judged so far: %d %s" % (len(judged), dict(oc.most_common())))
    print("member directory hosts found by probing: %d (+%d this run); domains probed so far: %d; with the archive's hosts: %d" % (len(rows), len(rows) - n0, len(probed), len(known_hosts())))


def crawl(a):
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    n = max(1, n)
    os.makedirs("out", exist_ok=True)
    os.makedirs(C.STATE, exist_ok=True)
    done = set()
    if os.path.exists(CCL.EXDONE):
        for l in open(CCL.EXDONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if q and q[0] and "/list/member/" in q[0] and (len(q) < 5 or q[4] == "ok"):
                done.add(re.sub(r"^https?://", "", q[0]).rstrip("/").lower())
    hosts = sorted(h for h in known_hosts() if shard_ok(h, k, n))
    if a.limit:
        hosts = hosts[:a.limit]
    kh = known_hosts()
    print("shard %d/%d: %d directory hosts; %d member pages read before (archive or live)" % (k, n, len(hosts), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fl = open("out/cc_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fn = open("out/cc_leads_noaddr_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/cc_extract_done_%d.tsv" % k, "a", encoding="utf-8")

    def member_urls(host):
        urls = {}
        misses = 0
        # 1. the directory's own sitemap (named in its robots.txt: "Sitemap: https://<host>/SiteMap.xml") lists every member page. The platform's
        #    robots.txt disallows /list/search — which covers the alphabetical lists (/list/searchalpha/…) — so on most hosts the sitemap is the
        #    only list a crawler may read (2026-11-10: business.ykchamber.com, 443 member pages in the sitemap, 115 in the archive).
        for sm in ("https://%s/SiteMap.xml" % host,):
            if time.time() > deadline or not C.allowed(sm):
                continue
            try:
                st, ct, data, final = fetch(sm, 20_000_000)
            except Exception:
                st, data = 0, b""
            if st == 200 and data:
                for loc in re.findall(r"(?is)<loc>\s*([^<\s]+)\s*</loc>", data.decode("utf-8", "replace")):
                    loc = html.unescape(loc)
                    pu = urllib.parse.urlparse(loc)
                    if (pu.hostname or "").lower() == host and re.match(r"(?i)/list/member/[^/?#]+/?$", pu.path or ""):
                        urls.setdefault(re.sub(r"^https?://", "", loc).rstrip("/").lower(), loc)
                with lock:
                    stats["sitemaps_read"] += 1
                    stats["member_pages_in_sitemaps"] += len(urls)
        if urls:
            return urls
        for c in ALPHA:
            if time.time() > deadline or misses >= 4:
                break
            u = "https://%s/list/searchalpha/%s" % (host, c)
            if not C.allowed(u):
                stats["robots"] += 1
                break
            st, ct, data, final = fetch(u)
            if st != 200 or not data:
                misses += 1
                continue
            raw = html.unescape(data.decode("utf-8", "replace"))
            found = 0
            for m in MEMBER_HREF.finditer(raw):
                full = urllib.parse.urljoin(final, m.group(1))
                if (urllib.parse.urlparse(full).hostname or "").lower() == host:
                    urls.setdefault(re.sub(r"^https?://", "", full).rstrip("/").lower(), full)
                    found += 1
            misses = 0 if found else misses + (1 if c in "abc" else 0)
        return urls

    def one(host):
        if time.time() > deadline:
            return
        dom, basis, body = kh[host]
        try:
            urls = member_urls(host)
        except Exception as e:
            urls = {}
            with lock:
                stats["host_errors"] += 1
        todo = [(key, u) for key, u in sorted(urls.items()) if key not in done]
        with lock:
            stats["hosts"] += 1
            stats["hosts_with_members"] += bool(urls)
            stats["member_pages_listed"] += len(urls)
            stats["member_pages_new"] += len(todo)
        for key, u in todo:
            if time.time() > deadline:
                break
            page, why = None, ""
            try:
                if not C.allowed(u):
                    why = "robots"
                else:
                    st, ct, data, final = fetch(u)
                    if st == 200 and data:
                        page = data.decode("utf-8", "replace")  # as the archive reader hands it over: markup untouched
                    else:
                        why = "http_%s" % st
                row = {"url": u, "host": host, "dom": dom, "path": urllib.parse.urlparse(u).path, "cls": "member", "basis": basis, "fetch_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                       "warc_filename": "live", "warc_record_offset": 0, "warc_record_length": 0}
                hits, quote = CCL.leads_of(page, row) if page else ([], "")
            except Exception as e:
                page, why, hits, quote = None, "error:" + type(e).__name__, [], ""
            for h in hits:
                h["dataset"] = h["dataset"].replace("(Common Crawl capture)", "(the directory read live)")
                h["row"]["pass"] = "live"
                if C.registrable(host) != dom:  # the directory sits on the platform's domain: the body is named by its own site, not by the tenant host
                    h["row"]["vendor_site"] = "https://%s/" % dom
                    h["canada_value"] = dom
                if (h.get("vendor") or "").lower() in ("", host.lower(), CCL.base(host)):  # the member page carries no site name: the body's name as its
                    nm = body or body_name(page)                                           # directory front page gave it, else the page's own title
                    if nm:
                        h["vendor"] = nm
            with lock:
                stats["pages"] += 1
                stats["unreadable"] += page is None
                stats["with_member_site"] += bool(hits)
                stats["leads" if quote else "leads_noaddr"] += len(hits)
                out = fl if quote else fn
                for h in hits:
                    out.write(json.dumps(h, ensure_ascii=False) + "\n")
                fd.write("%s\t%s\t%d\t%d\t%s\t%d\n" % (u, TODAY, len(hits), 1 if quote else 0, "ok" if page is not None else "unreadable:" + why, 1))
                if stats["pages"] % 500 == 0:
                    for f in (fl, fn, fd):
                        f.flush()
                    print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, hosts))
    for f in (fl, fn, fd):
        f.close()
    print("finished", dict(stats), flush=True)


def index_hosts(a):
    """every host that holds /list/member/<name>-<id> pages in the Common Crawl columnar index, on any domain: the directories of this family the
    archive has seen (the row factory's own index only looked at .ca hosts). One query per index part, ~2 seconds each."""
    import duckdb
    cid, paths = CCL.newest_crawl(a.crawl or "auto")
    con = duckdb.connect()
    for st in ("INSTALL httpfs", "LOAD httpfs", "SET threads=4", "SET http_retries=8", "SET http_retry_wait_ms=2000", "SET enable_progress_bar=false"):
        try:
            con.execute(st)
        except Exception as e:
            print("duckdb setting skipped: %s (%s)" % (st, str(e)[:80]), flush=True)
    tot, failed, t0 = collections.Counter(), [], time.time()
    for i, p in enumerate(paths):
        for attempt in range(3):
            try:
                for h, n in con.execute("SELECT url_host_name, count(*) FROM read_parquet('%s') WHERE starts_with(url_path, '/list/member/') GROUP BY 1" % (CCL.CC + p)).fetchall():
                    tot[(h or "").lower()] += n
                break
            except Exception as e:
                if attempt == 2:
                    failed.append(i)
                    print("part %d not read: %s" % (i, str(e)[:120]), flush=True)
                time.sleep(10 * (attempt + 1))
        if i % 50 == 0:
            print("%s part %d/%d: %d hosts, %d member pages (%.0f s)" % (cid, i + 1, len(paths), len(tot), sum(tot.values()), time.time() - t0), flush=True)
    have = {}
    if os.path.exists(INDEX_HOSTS):
        have = {r["host"]: r for r in csv.DictReader(open(INDEX_HOSTS, encoding="utf-8"))}
    n0 = len(have)
    for h, n in tot.items():
        if h and (h not in have or int(have[h].get("member_pages") or 0) < n):
            have[h] = {"host": h, "member_pages": n, "crawl": cid}
    with open(INDEX_HOSTS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["host", "member_pages", "crawl"])
        w.writeheader()
        for h in sorted(have, key=lambda h: (-int(have[h]["member_pages"]), h)):
            w.writerow(have[h])
    print("index hosts: %d with /list/member/ pages in %s (%d member pages; index parts not read: %d); on file %d (+%d)" % (
        len(tot), cid, sum(tot.values()), len(failed), len(have), len(have) - n0))


def own_site(raw, host):
    """the body's own website as its directory page links it: the outside domain most of the page's menu links go to (a body's directory wears
    the body's menu), else the link labelled Home"""
    cnt, home = collections.Counter(), ""
    me = C.registrable(host)
    for m in re.finditer(r"(?is)<a\b([^>]*)>(.*?)</a>", raw[:800_000]):
        hm = re.search(r"""href\s*=\s*["'](https?://[^"'#\s]+)""", m.group(1))
        if not hm:
            continue
        h = (urllib.parse.urlparse(hm.group(1)).hostname or "").lower()
        if not h or "." not in h:
            continue
        d = C.registrable(h[4:] if h.startswith("www.") else h)
        if not d or d == me or PLATFORM_DOM.search(d) or NOT_OWN.search(d):
            continue
        cnt[d] += 1
        label = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", m.group(2))).strip()
        if not home and re.fullmatch(r"(?i)home|accueil|main (?:web)?site|chamber home|back to (?:the )?(?:main )?(?:web)?site", label):
            home = d
    if cnt:
        d, n = cnt.most_common(1)[0]
        if n >= 4 and n >= 2 * (cnt.most_common(2)[1][1] if len(cnt) > 1 else 0):
            return d
    return home


def body_name(raw):
    """the body's name as its directory page states it: og:site_name, else the last part of the <title> ("Business Directory Search - Yellowknife
    Chamber of Commerce") when that part reads as an organisation's name"""
    t = re.search(r"""(?is)<meta[^>]+property=["']og:site_name["'][^>]+content=["']([^"']{2,90})["']""", raw[:200_000])
    if t and t.group(1).strip():
        return html.unescape(t.group(1)).strip()
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw[:200_000])
    if t:
        parts = [x.strip() for x in re.split(r"\s+[|–—-]\s+", html.unescape(re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", t.group(1)))).strip()) if x.strip()]
        if len(parts) >= 2 and 4 <= len(parts[-1]) <= 90 and re.search(r"(?i)chamber|chambre|board of trade|association|council|conseil|alliance|society|soci[ée]t[ée]|federation|f[ée]d[ée]ration|"
                                                                        r"institute|institut|bureau|commerce|tourism|tourisme|network|r[ée]seau|partnership|corporation|club|guild|league", parts[-1]):
            return parts[-1]
    return ""


def body_address(text):
    """(country, quote): the LAST postal address the page prints — a directory page prints its members' addresses first and the body's own in its
    footer. 'CA' with the quote, 'US' when the last address is a US state + ZIP code, '' when the page prints neither."""
    ms = list(CCL.ADDR.finditer(text))
    us = list(US_ZIP.finditer(text))
    if ms and (not us or ms[-1].end() >= us[-1].end()):
        m = ms[-1]
        return "CA", re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:]
    if us:
        return "US", ""
    return "", ""


def discover_index(a):
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    n = max(1, n)
    os.makedirs("out", exist_ok=True)
    known = known_hosts()
    judged = set()
    if os.path.exists(JUDGED):
        judged = {l.split("\t")[0] for l in open(JUDGED, encoding="utf-8") if l.strip()}
    todo = []
    if os.path.exists(INDEX_HOSTS):
        for r in csv.DictReader(open(INDEX_HOSTS, encoding="utf-8")):
            h = (r.get("host") or "").lower()
            if h and h not in known and h not in judged and shard_ok(h, k, n) and int(r.get("member_pages") or 0) >= a.min_pages:
                todo.append(h)
    if a.limit:
        todo = todo[:a.limit]
    print("shard %d/%d: %d index hosts to judge (%d directory hosts known, %d judged before)" % (k, n, len(todo), len(known), len(judged)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/member_hosts_%d.csv" % k, "w", newline="", encoding="utf-8")
    w = csv.writer(fo)
    w.writerow(HOST_COLS)
    fa = open("out/cc_vendor_addr_%d.jsonl" % k, "a", encoding="utf-8")
    fj = open("out/member_judged_%d.tsv" % k, "a", encoding="utf-8")

    def one(h0):
        if time.time() > deadline:
            return
        outcome, host, dom, name, quote, qurl = "", h0, "", "", "", ""
        try:
            u = "https://%s/list/" % h0
            if not C.allowed(u):
                outcome = "robots"
            else:
                st, ct, data, final = fetch(u, 1_500_000)  # the platform's queue: 2 requests a second for the whole runner
                raw = data.decode("utf-8", "replace") if data else ""
                if st in (401, 403, 429) or (st == 503 and C.BLOCK_RX.search(raw[:3000])) or (raw and len(raw) < 30000 and C.BLOCK_RX.search(raw[:3000])):
                    outcome = "blocked"  # CAPTCHA, bot check, access denied: recorded and left alone
                elif st != 200 or not raw:
                    outcome = "http_%s" % st
                elif not FAMILY.search(raw) or not re.search(r"/list/(?:member|category|ql|searchalpha)/", raw, re.I):
                    outcome = "not_a_directory"
                else:
                    host = (urllib.parse.urlparse(final).hostname or h0).lower()
                    dom = C.registrable(host[4:] if host.startswith("www.") else host)
                    if PLATFORM_DOM.search(dom):
                        dom = own_site(raw, host)  # a tenant of the platform: whose directory it is
                    name = body_name(raw)
                    cc, quote = body_address(CCL.visible(raw))
                    qurl = final
                    if not dom:
                        outcome = "body_not_identified"
                    elif cc == "US":
                        outcome = "abroad:US"
                    elif cc != "CA":
                        # the directory prints no postal address: the body's own home page (its own site, not the platform's queue)
                        hu = "https://%s/" % dom
                        cc2, q2, raw2 = "", "", ""
                        if C.allowed(hu):
                            s2, _, d2, f2 = _fetch0(hu, 1_500_000)
                            raw2 = d2.decode("utf-8", "replace") if (s2 == 200 and d2) else ""
                            if raw2:
                                cc2, q2 = body_address(CCL.visible(raw2))
                                if cc2 == "CA":
                                    quote, qurl = q2, f2
                                if not name:
                                    name = body_name(raw2)
                        outcome = "CA" if cc2 == "CA" else "abroad:US" if cc2 == "US" else "no_address" if raw2 else "body_site_unreadable"
                    else:
                        outcome = "CA"
        except Exception as e:
            outcome = "error:" + type(e).__name__
        with lock:
            stats[outcome.split(":")[0] if not outcome.startswith("abroad") else outcome] += 1
            if outcome == "CA" and dom and quote:
                w.writerow([host, dom, "a body whose member directory was read live", TODAY,
                            "host with /list/member/ pages in the archive index; its /list/ page carries the directory family's markers", name])
                fa.write(json.dumps({"dom": dom, "host": (urllib.parse.urlparse(qurl).hostname or host).lower(), "url": qurl, "capture": time.strftime("%Y-%m-%d %H:%M:%S"), "crawl": "live",
                                     "quote": quote, "warc": "live"}, ensure_ascii=False) + "\n")
            if not outcome.startswith(("error", "http_5", "http_None", "http_0")):  # a host that did not answer is asked again by a later run
                fj.write("%s\t%s\t%s\t%s\n" % (h0, TODAY, outcome, dom))
            if sum(stats.values()) % 100 == 0:
                fo.flush(); fa.flush(); fj.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    for f in (fo, fa, fj):
        f.close()
    print("finished", dict(stats), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["hosts", "discover", "crawl", "merge-hosts", "index-hosts", "discover-index"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--crawl", default="auto", help="index-hosts: the Common Crawl id (default: the newest whose index is published)")
    ap.add_argument("--min-pages", type=int, default=1, help="discover-index: only hosts with at least this many member pages in the index")
    a = ap.parse_args()
    if a.cmd == "hosts":
        kh = known_hosts()
        print("%d directory hosts" % len(kh))
        for h in sorted(kh):
            print(h, kh[h][0], kh[h][1][:60])
    elif a.cmd == "discover":
        os.makedirs(C.STATE, exist_ok=True)
        discover(a)
        sys.stdout.flush()
        os._exit(0)
    elif a.cmd == "index-hosts":
        index_hosts(a)
    elif a.cmd == "discover-index":
        os.makedirs(C.STATE, exist_ok=True)
        discover_index(a)
        sys.stdout.flush()
        os._exit(0)
    elif a.cmd == "merge-hosts":
        merge_hosts(a)
    else:
        crawl(a)
        sys.stdout.flush()
        os._exit(0)


if __name__ == "__main__":
    main()

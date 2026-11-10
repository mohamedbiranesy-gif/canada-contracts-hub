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
HOST_COLS = ["host", "dom", "basis", "found", "how"]
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
    """{host: (dom, basis)}: directory hosts of the archive index, then the hosts found by `discover`"""
    out = {}
    if os.path.exists(CCL.PAGES):
        with gzip.open(CCL.PAGES, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r.get("cls") == "member" and CCL._M1_RX.search((r.get("path") or "").lower()):
                    out.setdefault(r["host"], (r.get("dom") or C.registrable(r["host"]), r.get("basis") or ""))
    if os.path.exists(HOSTS):
        for r in csv.DictReader(open(HOSTS, encoding="utf-8")):
            out.setdefault(r["host"], (r.get("dom") or C.registrable(r["host"]), r.get("basis") or ""))
    # a directory under the platform's own domain (xyz.chambermaster.com) is one tenant among thousands, most of them abroad: only directories on
    # the body's own domain are read
    return {h: v for h, v in out.items() if not CCL.MULTI_TENANT.search(h) and not CCL.MULTI_TENANT.search(v[0])}


def shard_ok(h, k, n):
    return int(hashlib.sha1(h.encode()).hexdigest(), 16) % n == k


def discover(a):
    import credit_scan as CS
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    n = max(1, n)
    os.makedirs("out", exist_ok=True)
    known = known_hosts()
    known_dom = {d for d, _ in known.values()}
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
        dom, basis = kh[host]
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["hosts", "discover", "crawl", "merge-hosts"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=150)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
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
    elif a.cmd == "merge-hosts":
        merge_hosts(a)
    else:
        crawl(a)
        sys.stdout.flush()
        os._exit(0)


if __name__ == "__main__":
    main()

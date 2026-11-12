#!/usr/bin/env python3
"""Client / dealer / sponsor / tenant / member pages of Canada-located organisations, read LIVE on their own sites (2026-11-10).

Why. The row factory (tools/cc_clients.py) reads such pages from the Common Crawl archive: 66,000 pages of .ca hosts, the pages the archive
happens to hold. The archive keeps a few pages of a small site, and the page that names its clients is often not one of them. The home-page scan
(tools/credit_scan.py) has since read 1.3 million home pages: 169,000 .ca sites print a Canadian postal address there, and 14,500 vendors were
checked live (address in Canada). Each of those sites is asked for its home page once more; the links of its own menu whose PATH is a client /
case-study / portfolio / dealer / sponsor / tenant / member page — the same path rule as the archive engine and as rank.py — are read (four pages
at most) with the archive engine's own extractor (cc_clients.leads_of). The records have the archive engine's format, so its merge takes them:
same rules (vendor's Canadian postal address quoted from its own page; a domain named by more than 15 vendors is a platform; spam, credits,
country selectors, menu links out), same lead keys, same withdrawals.

  scan   --shard K/N [--minutes 100] [--workers 100] [--limit N]   -> out/cc_leads_<K>.jsonl, out/cc_leads_noaddr_<K>.jsonl,
                                                                      out/cc_extract_done_<K>.tsv, out/live_done_<K>.tsv
  merge  DIR --stamp S                                             -> data/incoming/claude/client_live/done_<S>.gz (append-only state);
                                                                      then: python3 tools/cc_clients.py merge DIR --stamp S --engine lc

Polite: robots.txt of every site is read first and obeyed, one request per second per host (ap_crawler.fetch), identified user agent, a site
that refuses is noted as blocked and left alone. No AI, no search engine, no archive.
"""
import argparse, collections, glob, gzip, hashlib, json, os, random, re, sys, threading, time, urllib.parse, urllib.robotparser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402
import credit_scan as CS  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
STATE = os.path.join(INC, "client_live")
TODAY = time.strftime("%Y-%m-%d")
MAX_PAGES = 4
CLASS_RANK = {"client": 0, "dealer": 1, "sponsor": 2, "tenant": 3, "member": 4}
LIVE_TEXT = {k: v.replace("(Common Crawl capture)", "(read live on its own site)") for k, v in CCL.CLASS_TEXT.items()}
NOT_PAGE = re.compile(r"\.(?:pdf|jpe?g|png|gif|webp|svg|zip|docx?|xlsx?|pptx?|mp4|mp3|ics)(?:$|\?)", re.I)


def done_sites():
    out = {}
    for p in sorted(glob.glob(os.path.join(STATE, "done_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            for l in fh:
                q = l.rstrip("\n").split("\t")
                if q and q[0]:
                    out[q[0]] = q
    return out


def pages_read():
    """page URLs the archive engine or an earlier live run already read (http / https / www / trailing slash alike)"""
    out = set()
    if os.path.exists(CCL.EXDONE):
        with open(CCL.EXDONE, encoding="utf-8") as fh:
            for l in fh:
                q = l.split("\t", 5)
                if len(q) > 4 and q[4].startswith("ok"):
                    out.add(norm_url(q[0]))
    return out


def norm_url(u):
    p = urllib.parse.urlparse(u)
    h = (p.hostname or "").lower()
    return (h[4:] if h.startswith("www.") else h) + (p.path.rstrip("/") or "/") + (("?" + p.query) if p.query else "")


def queue(k, n, limit=0):
    """sites to read: vendors whose own site was checked live and prints its address in Canada (most are web / design / IT firms: their portfolio
    pages name clients), then .ca sites whose home page prints a Canadian postal address. Governments, marketplaces, media and site builders are
    left out by the archive engine's own lists."""
    done = done_sites()
    seen, tasks = set(), []

    def add(dom, pri):
        dom = (dom or "").lower().strip()
        if not dom or "." not in dom or dom in seen or dom in done or CCL.VENDOR_SKIP.search(dom) or CCL.MULTI_TENANT.search(dom) or CS.PLATFORM.search(dom):
            return
        if int(hashlib.sha1(dom.encode()).hexdigest(), 16) % n != k:
            return
        seen.add(dom)
        tasks.append((pri, dom))
    for dom, o in CS.vendor_state().items():
        if o.get("status") in ("CA", "CA-loc") and (dom.endswith(".ca") or not o.get("also_prints")):
            add(dom, 0 if dom.endswith(".ca") else 2)
    for l in CS.state_lines("done"):
        q = l.split("\t")
        if len(q) > 6 and q[2] == "ok" and "cc=CA" in q[6:]:
            add(q[0], 1 if q[0].endswith(".ca") else 2)  # 2: a site on another ending (.com, .org …) whose home page prints a Canadian postal address
    rnd = random.Random(11)
    tasks.sort(key=lambda t: (t[0], rnd.random()))
    return (tasks[:limit] if limit else tasks), len(done)


def robots_of(root):
    """(parser or None, reachable, refused): robots.txt read once per site"""
    st, _, data, _ = C.fetch(root + "robots.txt", 300_000)
    if st in (401, 403):
        return None, True, True
    if st == 0:
        return None, False, False
    if st == 200 and data:
        rp = urllib.robotparser.RobotFileParser()
        try:
            rp.parse(data.decode("utf-8-sig", "replace").splitlines())
            return rp, True, False
        except Exception:
            return None, True, False
    return None, True, False


def site(dom, known_pages):
    """(status, pages found, pages read, hits with an address, hits without, done lines for the pages)"""
    root = "https://%s/" % dom
    rp, reach, refused = robots_of(root)
    if refused:
        return "blocked", 0, 0, [], [], []
    allowed = lambda u: True if rp is None else rp.can_fetch(C.UA, u)
    if not allowed(root):
        return "robots", 0, 0, [], [], []
    st, final, home = CS.get_page(root, check_robots=False)
    if st != "ok":
        return st, 0, 0, [], [], []
    fhost = CCL.base((urllib.parse.urlparse(final).hostname or "").lower())
    if C.registrable(fhost) != C.registrable(dom):
        return "redirected_elsewhere", 0, 0, [], [], []
    text = CCL.visible(home)
    m = CCL.ADDR.search(text)
    home_quote = re.sub(r"^\S*\s", "", text[max(0, m.start() - 110):m.end()].strip())[-200:] if m else ""
    basis = ""
    if not dom.endswith(".ca"):
        # a site on another ending counts as a Canada-located organisation only on its own word: its home page prints a Canadian postal address
        # and no postal address abroad (a multinational's site lists its offices in several countries: left out)
        import lead_crawl as LC
        if not home_quote:
            return "no_canadian_address", 0, 0, [], [], []
        if any(rx.search(text) for rx in (LC.US_ADDR, LC.GB_ADDR, LC.AU_ADDR)):
            return "also_prints_an_address_abroad", 0, 0, [], [], []
        basis = "a site whose home page prints no postal address outside Canada"
    cand = {}
    for href, label in CCL.anchors(home, final):
        try:
            p = urllib.parse.urlparse(href)
        except ValueError:
            continue
        h = CCL.base((p.hostname or "").lower())
        if p.scheme not in ("http", "https") or not h or C.registrable(h) != C.registrable(dom) or NOT_PAGE.search(p.path or ""):
            continue
        cls = CCL.page_class(p.path)
        if not cls or (cls == "member" and CCL._M1_RX.search((p.path or "").lower())):
            continue  # one-member pages of a directory are the member-directory engine's work
        u = href.split("#")[0]
        if norm_url(u) in known_pages:
            continue
        cand.setdefault(norm_url(u), (CLASS_RANK.get(cls, 9), len(p.path), u, cls))
    pages = [(u, cls) for _, _, u, cls in sorted(cand.values())[:MAX_PAGES]]
    with_addr, without, lines, n_read = [], [], [], 0
    for u, cls in pages:
        if not allowed(u):
            lines.append("%s\t%s\t0\t0\trobots\t1\n" % (u, TODAY))
            continue
        st, pfinal, page = CS.get_page(u, check_robots=False)
        if st != "ok":
            lines.append("%s\t%s\t0\t0\tunreadable:%s\t1\n" % (u, TODAY, st))
            continue
        n_read += 1
        pp = urllib.parse.urlparse(pfinal)
        if C.registrable(CCL.base((pp.hostname or "").lower())) != C.registrable(dom):
            lines.append("%s\t%s\t0\t0\tok\t1\n" % (u, TODAY))
            continue
        row = {"url": pfinal, "host": (pp.hostname or "").lower(), "dom": C.registrable(dom), "path": pp.path, "cls": CCL.page_class(pp.path) or cls, "basis": basis,
               "fetch_time": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()), "warc_filename": "live", "warc_record_offset": 0, "warc_record_length": 0}
        try:
            hits, quote = CCL.leads_of(page, row)
        except Exception:
            hits, quote = [], ""
        for hrec in hits:
            r = hrec["row"]
            r["pass"], r["warc"], r["vendor_address_how"] = "live", "", "live"
            hrec["dataset"] = LIVE_TEXT.get(r.get("page_class") or "client", LIVE_TEXT["client"])
            if home_quote and (not quote or basis):  # the client page prints no address — or the site is not a .ca one, where the home page's address is the test
                r["vendor_address_quote"], r["vendor_address_url"] = home_quote, final
        addr = quote or home_quote
        (with_addr if addr else without).extend(hits)
        lines.append("%s\t%s\t%d\t%d\tok\t1\n" % (u, TODAY, len(hits), 1 if addr else 0))
    return "ok", len(cand), n_read, with_addr, without, lines


def scan(a):
    k, n = (int(x) for x in a.shard.split("/"))
    os.makedirs("out", exist_ok=True)
    tasks, n_done = queue(k, n, a.limit)
    known = pages_read()
    print("shard %d/%d: %d sites to read (%d read before; %d pages already read by the archive engine): %s" % (
        k, n, len(tasks), n_done, len(known), dict(collections.Counter({0: "vendor checked live", 1: ".ca site printing a Canadian address", 2: "other ending, Canadian address"}[p] for p, _ in tasks))), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats = threading.Lock(), collections.Counter()
    fl = open("out/cc_leads_%d.jsonl" % k, "a", encoding="utf-8")
    fn = open("out/cc_leads_noaddr_%d.jsonl" % k, "a", encoding="utf-8")
    fd = open("out/cc_extract_done_%d.tsv" % k, "a", encoding="utf-8")
    fs = open("out/live_done_%d.tsv" % k, "a", encoding="utf-8")
    it = iter(tasks)

    def work():
        while time.time() < deadline:
            with lock:
                t = next(it, None)
            if t is None:
                return
            pri, dom = t
            try:
                st, n_found, n_read, wa, wo, lines = site(dom, known)
            except Exception as e:
                st, n_found, n_read, wa, wo, lines = "error:%s" % type(e).__name__, 0, 0, [], [], []
            with lock:
                stats["sites"] += 1
                stats[st.split(":")[0]] += 1
                stats["sites with a client-type page"] += bool(n_found)
                stats["pages read"] += n_read
                stats["sites with links"] += bool(wa or wo)
                stats["leads"] += len(wa)
                stats["leads_noaddr"] += len(wo)
                for h in wa:
                    fl.write(json.dumps(h, ensure_ascii=False) + "\n")
                for h in wo:
                    fn.write(json.dumps(h, ensure_ascii=False) + "\n")
                for l in lines:
                    fd.write(l)
                fs.write("%s\t%s\t%s\t%d\t%d\t%d\n" % (dom, TODAY, st, n_found, n_read, len(wa) + len(wo)))
                if stats["sites"] % 500 == 0:
                    for f in (fl, fn, fd, fs):
                        f.flush()
                    print(time.strftime("%H:%M:%S"), dict(stats), flush=True)
    th = [threading.Thread(target=work, daemon=True) for _ in range(a.workers)]
    for t in th:
        t.start()
    end = deadline + a.straggler_seconds
    for t in th:
        t.join(max(0.0, end - time.time()))
    with lock:
        for f in (fl, fn, fd, fs):
            f.flush()
        print("finished", dict(stats), "(stragglers left: %d)" % sum(1 for t in th if t.is_alive()), flush=True)
    sys.stdout.flush()
    os._exit(0)  # do not wait for straggler threads


def merge(a):
    os.makedirs(STATE, exist_ok=True)
    lines = []
    for f in sorted(glob.glob(os.path.join(a.dir, "live_done_*.tsv"))):
        with open(f, encoding="utf-8") as fh:
            lines += [l for l in fh if l.strip()]
    if lines:
        with gzip.open(os.path.join(STATE, "done_%s.gz" % (a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime()))), "wt", encoding="utf-8") as fh:
            fh.writelines(lines)
    st = collections.Counter(l.split("\t")[2].split(":")[0] for l in lines if l.count("\t") >= 5)
    tot = done_sites()
    print("client pages read live: %d sites this run (%s); with a client-type page %d; pages read %d; links %d; sites read so far %d" % (
        len(lines), ", ".join("%s %d" % kv for kv in st.most_common(6)), sum(1 for l in lines if l.count("\t") >= 5 and l.split("\t")[3] != "0"),
        sum(int(l.split("\t")[4]) for l in lines if l.count("\t") >= 5), sum(int(l.split("\t")[5]) for l in lines if l.count("\t") >= 5), len(tot)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["scan", "merge"])
    ap.add_argument("dir", nargs="?", default="out")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=100)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stamp", default="")
    ap.add_argument("--straggler-seconds", type=float, default=120)
    a = ap.parse_args()
    if a.cmd == "scan":
        os.makedirs(C.STATE, exist_ok=True)
        scan(a)
    else:
        merge(a)


if __name__ == "__main__":
    main()

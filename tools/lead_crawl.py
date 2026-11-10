#!/usr/bin/env python3
"""Row factory, step 2 (cloud): the role mailbox of every NEW lead buyer, read on the buyer's own site.

tools/cc_clients.py finds new buyers (organisations named and linked on the client pages of Canada-located vendors). A buyer becomes a
delivered row only with a mailbox the organisation publishes itself. This runs tools/ap_crawler.crawl() — the same no-AI reader that ran on
the owner's Mac — over the new leads, from GitHub runners: robots.txt respected, at most one request per second per site, a small page budget,
invoicing / AP / supplier / purchasing / finance mailboxes first and, when the site publishes none, its general role mailbox (owner rule
2026-10-28). Never a named person, never a pattern-built address, blocked sites are recorded as blocked and left alone.
  python3 tools/lead_crawl.py --shard K/N [--minutes 150] [--max-pages 15] [--workers 40] [--limit N]
In : data/incoming/claude/claude_buyer_leads_cc.csv  (buyer_key, buyer_name, website, …)
     data/incoming/claude/claude_lead_crawl_done.tsv  (buyer_key, date, result, pages, rows)      — resume
Out: out/lead_rows_<K>.csv   buyer_ap rows (docs/RETURN_FORMATS.md) — appended by the workflow to claude_buyer_ap_results_cccrawl01.csv,
                             where the referee re-fetches every evidence page before a mailbox counts
     out/lead_done_<K>.tsv
"""
import argparse, csv, hashlib, os, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DONE = os.path.join(INC, "claude_lead_crawl_done.tsv")
TODAY = time.strftime("%Y-%m-%d")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--leads", default=os.path.join(INC, "claude_buyer_leads_cc.csv"))
    a.add_argument("--shard", default="0/1")
    a.add_argument("--minutes", type=float, default=150)
    a.add_argument("--max-pages", type=int, default=15)
    a.add_argument("--workers", type=int, default=40)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--straggler-seconds", type=float, default=240, help="when only slow sites are left and nothing finished for this long, stop")
    a = a.parse_args()
    k, n = int(a.shard.split("/")[0]), max(1, int(a.shard.split("/")[1]))
    os.makedirs(C.STATE, exist_ok=True)
    os.makedirs("out", exist_ok=True)
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t")[0] for l in open(DONE, encoding="utf-8")}
    tasks, hosts = [], set()
    for r in csv.DictReader(open(a.leads, encoding="utf-8")):
        site = (r.get("website") or "").strip()
        h = (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower() if site else ""
        if not h or "." not in h or r["buyer_key"] in done or h in hosts:
            continue
        if int(hashlib.sha1(h.encode()).hexdigest(), 16) % n != k:  # sharded by host: two runners never read the same site
            continue
        hosts.add(h)
        tasks.append({"task_id": "CC-" + r["buyer_key"].split(":")[-1][:10], "buyer_key": r["buyer_key"], "buyer_name": r.get("buyer_name") or h, "known_website": "https://%s/" % h,
                      "_n": int(r.get("canadian_vendor_rows") or 1)})
    tasks.sort(key=lambda t: -t["_n"])  # buyers named by several Canadian vendors first
    if a.limit:
        tasks = tasks[:a.limit]
    print("shard %d/%d: %d new lead sites to read (%d done before)" % (k, n, len(tasks), len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock = threading.Lock()
    stats = {"sites": 0, "with_mailbox": 0, "rows": 0, "blocked": 0, "errors": 0}
    fr = open("out/lead_rows_%d.csv" % k, "a", newline="", encoding="utf-8")
    w = csv.DictWriter(fr, fieldnames=C.COLS, extrasaction="ignore")
    w.writeheader()
    fd = open("out/lead_done_%d.tsv" % k, "a", encoding="utf-8")

    def one(t):
        if time.time() > deadline:
            return
        try:
            result, pages, rows = C.crawl(t, a.max_pages, general=True)
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        try:
            C.AP_PAGES.pop(t["buyer_key"], None)  # the walker's page memory is not needed here
        except Exception:
            pass
        # the validator's own rule (tools/validate_returns.py): a first.last-shaped local part without a role word is treated as a person and dropped
        rows = [r for r in rows if C.EMAIL.match(r.get("ap_email") or "") and not (C.PERSONAL.match(r["ap_email"].split("@")[0]) and not C.ROLE_HINT.search(r["ap_email"].split("@")[0]))]
        with lock:
            stats["sites"] += 1
            stats["with_mailbox"] += bool(rows)
            stats["rows"] += len(rows)
            stats["blocked"] += result == "blocked"
            stats["errors"] += str(result).startswith("error")
            w.writerows(rows)
            fd.write("%s\t%s\t%s\t%d\t%d\n" % (t["buyer_key"], TODAY, result, pages, len(rows)))
            if stats["sites"] % 200 == 0:
                fr.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), stats, flush=True)
    # a few sites answer so slowly that one thread can hold a runner for an hour (first cycle, 2026-11-10: two of eight shards were still
    # running 20 minutes after the others). When only stragglers are left and nothing finished for 4 minutes, they are recorded as "timeout"
    # (not read again) and the run ends; sites not started by the deadline stay in the queue for the next cycle.
    from concurrent.futures import wait
    ex = ThreadPoolExecutor(a.workers)
    futs = {ex.submit(one, t): t for t in tasks}
    pending, last = set(futs), time.time()
    while pending:
        fin, pending = wait(pending, timeout=min(30, max(1, a.straggler_seconds / 3)))
        if fin:
            last = time.time()
        if (len(pending) <= a.workers and time.time() - last > a.straggler_seconds) or time.time() > deadline + 300:
            with lock:
                for f in pending:
                    if f.running():
                        fd.write("%s\t%s\ttimeout\t0\t0\n" % (futs[f]["buyer_key"], TODAY))
                        stats["errors"] += 1
            break
    with lock:
        fr.close(); fd.close()
    print("finished", stats, "(stragglers left: %d)" % len(pending), flush=True)
    sys.stdout.flush()
    os._exit(0)  # do not wait for the straggler threads


if __name__ == "__main__":
    main()

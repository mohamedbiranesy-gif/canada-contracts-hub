#!/usr/bin/env python3
"""The $5,000+ rows held back for want of a mailbox: read their own sites for a role mailbox (tools/ap_crawler.py crawl, the same reader,
robots and rules as the crawler that runs on the owner's Mac), so the referee can re-read them.

Owner 2026-11-13 13:20 EST: "add as much over 5000 as possible". The table of 22:10Z held 1,824 rows marked $5,000+ out of the ready set;
956 of them for no mailbox, 900-odd of those with the organisation's own website on file. The Mac crawler is the one that reads contract
buyers' sites; it is not running in the cloud. This reads those sites once, here.

  python3 contrib/claude/c5k_mailboxes.py ranked_buyers.csv.gz [--workers 12] [--minutes 50] [--out data/incoming/claude/claude_buyer_ap_results_c5k01.csv]
"""
import argparse, csv, gzip, os, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ap_crawler as A  # noqa: E402

csv.field_size_limit(1 << 30)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ranked")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--minutes", type=float, default=50)
    ap.add_argument("--out", default="data/incoming/claude/claude_buyer_ap_results_c5k01.csv")
    ap.add_argument("--sites", default="", help="read the sites of this file (key, name, site) instead of the table's")
    ap.add_argument("--skip", type=int, default=0, help="leave the first N sites of the table's order (read by an earlier run that stopped at its time limit)")
    a = ap.parse_args()
    os.chdir(ROOT)
    tasks, seen = [], set()
    if a.sites:
        for r in csv.DictReader(open(a.sites, encoding="utf-8")):
            if r.get("site") and r["site"] not in seen:
                seen.add(r["site"])
                tasks.append({"task_id": "C5S-%04d" % (len(tasks) + 1), "buyer_key": r["key"], "buyer_name": r["name"][:200], "known_website": r["site"]})
        a.ranked = None
    with (gzip.open(a.ranked, "rt", encoding="utf-8", errors="replace") if a.ranked else open(os.devnull)) as fh:
        for x in (csv.DictReader(fh) if a.ranked else ()):
            if (x.get("amount_mark") or "5")[:1] not in "12" or (x.get("ship_ready") or "").startswith("yes"):
                continue
            miss = x.get("ship_ready_missing") or ""
            if "no mailbox" not in miss and "not re-read" not in miss:
                continue
            site = (x.get("buyer_website") or "").strip()
            key = next((k for k in (x.get("keys") or "").split("|") if k.startswith(("b:", "lead:"))), "")
            if not site or not key or site in seen:
                continue
            seen.add(site)
            tasks.append({"task_id": "C5K-%04d" % (len(tasks) + 1), "buyer_key": key, "buyer_name": (x.get("buyer") or "")[:200], "known_website": site})
    print("%d sites of $5,000+ rows with no mailbox" % len(tasks), flush=True)
    if a.skip:
        tasks = tasks[a.skip:]
        print("left the first %d (read before); %d to read" % (a.skip, len(tasks)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, out_rows, stats = threading.Lock(), [], {"sites": 0, "found": 0}

    def one(t):
        if time.time() >= deadline:
            return
        t["_deadline"] = deadline
        try:
            result, pages, rows = A.crawl(t, 25, general=True)
        except Exception as e:  # a site that breaks the reader is left, never retried here
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        with lock:
            stats["sites"] += 1
            stats["found"] += bool(rows)
            out_rows.extend(rows)
            if stats["sites"] % 50 == 0:
                print(stats, flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    new = not os.path.exists(a.out)
    with open(a.out, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=A.COLS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerows(out_rows)
    print("done:", stats, "rows written:", len(out_rows), "->", a.out, flush=True)


if __name__ == "__main__":
    main()

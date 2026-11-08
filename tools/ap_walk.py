#!/usr/bin/env python3
"""AP site walker (downstream §4: payment terms, PO rules, invoice addresses, portals, e-invoicing systems): for every delivered buyer,
follow the buyer's OWN links to its accounts-payable / supplier / purchasing / finance pages and documents (ap_crawler.crawl: link
words, sitemap, PDFs; robots.txt respected, 1 request / second / host), remember those pages, then hand them to tools/ap_terms.py
--urls, which extracts the terms with quotes. No search engine, no AI: the site's own navigation is the source, so it scales to every
buyer. Gold buyers first, then P02–P05, then the rest.
  python3 tools/ap_walk.py --ranked ~/cch-tasks/ranked_latest.csv.gz [--workers 40] [--max-pages 40] [--limit N]
Output: ~/cch-crawler-state/ap_pages_seen.csv (buyer_key,buyer_name,website,official_site,url,kind,date) — the input of
  python3 tools/ap_terms.py --urls ~/cch-crawler-state/ap_pages_seen.csv --ranked ~/cch-tasks/ranked_latest.csv.gz
Resume: ~/cch-crawler-state/ap_walk_done.tsv (buyer_key, date, pages, ap_pages).
"""
import argparse, hashlib, csv, gzip, os, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

STATE = os.path.expanduser("~/cch-crawler-state")
DONE = os.path.join(STATE, "ap_walk_done.tsv")
TODAY = time.strftime("%Y-%m-%d")
lock = threading.Lock()


def prio(r):
    rg, t, g = r.get("rank_group") or "", r.get("tier") or "", r.get("grade") or ""
    if rg == "GOLD":
        return 0
    if t in ("A", "B") and g in ("3", "2"):
        return 1
    if rg in ("GOLD-T", "GOLD-M"):
        return 2
    if t in ("A", "B", "L"):
        return 3
    if t in ("T", "M", "C", "D", "E"):
        return 4
    if t == "I":
        return 6
    return 5


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.expanduser("~/cch-tasks/ranked_latest.csv.gz"))
    a.add_argument("--workers", type=int, default=40)
    a.add_argument("--max-pages", type=int, default=40)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--redo-days", type=int, default=60)
    a.add_argument("--tiers", default="", help="only rows of these tiers (e.g. I for the inferred-relationship package), so a second walker can start on the long tail")
    a.add_argument("--skip-tiers", default="", help="skip rows of these tiers (the first walker keeps the stronger packages)")
    a.add_argument("--shard", default="", help="K/N: only buyers whose key hashes to shard K of N (parallel runners never share a host: one buyer = one site)")
    a = a.parse_args()
    shard_k, shard_n = (int(a.shard.split("/")[0]), int(a.shard.split("/")[1])) if a.shard else (0, 1)
    os.makedirs(STATE, exist_ok=True)
    C.HOST_INTERVAL = 2.0  # the site readers may be on the same host at the same time: stay well under 2 requests / second per host overall
    done = {}
    if os.path.exists(DONE):
        for l in open(DONE, encoding="utf-8"):
            p = l.rstrip("\n").split("\t")
            if len(p) >= 2:
                done[p[0]] = p[1]
    cutoff = time.strftime("%Y-%m-%d", time.localtime(time.time() - a.redo_days * 86400))
    op = gzip.open if a.ranked.endswith(".gz") else open
    tasks, seen = [], set()
    with op(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if not r.get("email"):
                continue
            if a.tiers and (r.get("tier") or "") not in a.tiers.split(","):
                continue
            if a.skip_tiers and (r.get("tier") or "") in a.skip_tiers.split(","):
                continue
            key = (r.get("keys") or "").split("|")[0]
            w = (r.get("buyer_website") or "").strip()
            h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower() if w else ""
            if not key or not h or "." not in h or key in seen:
                continue
            if done.get(key, "") >= cutoff:
                continue
            if shard_n > 1 and int(hashlib.md5(h.encode()).hexdigest(), 16) % shard_n != shard_k:
                continue  # sharded by host, so two runners never crawl the same site
            seen.add(key)
            tasks.append((prio(r), {"task_id": "", "buyer_key": key, "buyer_name": r.get("buyer") or "", "known_website": "https://%s/" % h}))
    tasks.sort(key=lambda t: t[0])
    if a.limit:
        tasks = tasks[:a.limit]
    print("sites to walk: %d (%d walked within %d days)" % (len(tasks), len(done), a.redo_days), flush=True)
    stats = {"sites": 0, "pages": 0, "ap_pages": 0, "blocked": 0}

    def one(t):
        pr, task = t
        try:
            result, pages, rows = C.crawl(task, a.max_pages, general=True)
        except Exception as e:
            result, pages = "error:%s" % type(e).__name__, 0
        n_ap = len(C.AP_PAGES.get(task["buyer_key"], []))
        C.flush_ap_pages(task["buyer_key"], task["buyer_name"], task["known_website"])
        with lock:
            stats["sites"] += 1; stats["pages"] += pages; stats["ap_pages"] += n_ap; stats["blocked"] += result == "blocked"
            with open(DONE, "a", encoding="utf-8") as f:
                f.write("%s\t%s\t%d\t%d\t%s\n" % (task["buyer_key"], TODAY, pages, n_ap, result))
            if stats["sites"] % 100 == 0:
                print(time.strftime("%H:%M"), stats, flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    print("finished", stats, flush=True)


if __name__ == "__main__":
    main()

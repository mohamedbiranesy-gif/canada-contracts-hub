#!/usr/bin/env python3
"""Read the sites of one task list now, with the crawler's rules, instead of waiting for its next cycle. No AI.

    python3 tools/crawl_some.py coord/tasks/claude/claude_buyer_ap_batch907.csv [--workers 16]

Each buyer's site is read for an invoicing / AP / finance / purchasing mailbox (60 pages); when none is found, again
for a general role mailbox (40 pages). Rows go to the crawler's results file and its done list, so the long-running
crawler skips these buyers afterwards. Same politeness: robots.txt, one request per second per site.
"""
import argparse, csv, os, sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C


def main():
    a = argparse.ArgumentParser()
    a.add_argument("tasks")
    a.add_argument("--workers", type=int, default=16)
    a = a.parse_args()
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    done = C.load_done()
    tasks = [t for t in csv.DictReader(open(a.tasks, encoding="utf-8-sig"))
             if (t.get("known_website") or "").startswith("http") and done.get(t["buyer_key"], (0, ""))[0] < 4]
    C.log("crawl_some: %d sites from %s" % (len(tasks), a.tasks))

    def one(t):
        try:
            result, pages, rows = C.crawl(t, 60, general=False)
            if not rows and result != "blocked":
                result, more, rows = C.crawl(t, 40, general=True)
                pages += more
        except Exception as e:
            result, pages, rows = "error:%s" % type(e).__name__, 0, []
        C.save(t, 4, result, pages, rows)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tasks))
    C.log("crawl_some finished", C.stats)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extend Biddingo awarded-bid list.jsonl further back in time (resume paging after the last saved page).
Usage: python3 -I crawl_list_more.py <outdir> <min_posted YYYY-MM-DD>
Then run crawl.py <outdir> <min_posted> to fetch the details of the new rows (it skips done ids)."""
import sys, os, json, time, datetime, re
import requests

outdir, min_posted = sys.argv[1], sys.argv[2]
API = "https://api.biddingo.com/restapi"
list_path = os.path.join(outdir, "list.jsonl")
log_path = os.path.join(outdir, "crawl.log")
sess = requests.Session()
sess.headers.update({"User-Agent": "contracts-research/1.0", "Accept": "application/json"})


def log(m):
    with open(log_path, "a") as f:
        f.write(f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} [list_more] {m}\n")


def to_iso(mdy):
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", mdy or "")
    return f"{m.group(3)}-{m.group(1)}-{m.group(2)}" if m else None


last = -1
ids = set()
for line in open(list_path):
    try:
        r = json.loads(line); last = max(last, r.get("_list_page", -1)); ids.add(r["biddingoTenderId"])
    except Exception:
        pass
page = last + 1
log(f"resume at page {page}, have {len(ids)}")
with open(list_path, "a") as f:
    while True:
        r = None
        for attempt in range(5):
            try:
                r = sess.get(f"{API}/v2/noauthorize/bids?offset={page}&limit=50&statuses=5&sort=postedDate%3Adesc", timeout=90)
                if r.status_code == 200:
                    break
                log(f"page {page} HTTP {r.status_code}")
            except Exception as e:
                log(f"page {page} error {e!r}")
            time.sleep(3 + 4 * attempt)
        if r is None or r.status_code != 200:
            log(f"page {page} FAILED; stop")
            break
        rows = r.json().get("bidInfoList", [])
        if not rows:
            log(f"page {page} empty; done")
            break
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        for x in rows:
            if x["biddingoTenderId"] in ids:
                continue
            ids.add(x["biddingoTenderId"])
            x["_retrieved_at"] = now; x["_list_page"] = page
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
        f.flush()
        dates = [to_iso(x.get("publishedDate")) for x in rows if to_iso(x.get("publishedDate"))]
        if page % 20 == 0:
            log(f"page {page}: last posted {dates[-1] if dates else None}")
        if dates and max(dates) < min_posted:
            log(f"page {page}: reached {min_posted}; stop")
            break
        page += 1
        time.sleep(0.4)
log("done")

#!/usr/bin/env python3
"""Biddingo (biddingo.com) public API - awarded bids.

List : GET https://api.biddingo.com/restapi/v2/noauthorize/bids?offset=<page>&limit=50&statuses=5&sort=postedDate:desc
       (statuses: 1 Open, 2 Cancelled, 4 Closed, 5 Awarded, 6 Suspended). Newest posted first.
Detail: GET https://api.biddingo.com/restapi/bidding/noauthorize/<buyerSysId>/<buyerOrgId>/<biddingoTenderId>
       -> bidInfo incl. bidAwardInfoList[].successfulBidderInfoList[] (bidderName, city, province, country, totalPrice...)
Writes <outdir>/list.jsonl (one row per bid) and <outdir>/details.jsonl (resumable), stops when posted date < min_posted.
Usage: python3 -I crawl.py <outdir> <min_posted YYYY-MM-DD> [max_details]
"""
import sys, os, json, time, datetime, re
import requests

UA = "contracts-research/1.0"
API = "https://api.biddingo.com/restapi"
outdir = sys.argv[1]
min_posted = sys.argv[2]
max_details = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
os.makedirs(outdir, exist_ok=True)
list_path = os.path.join(outdir, "list.jsonl")
details_path = os.path.join(outdir, "details.jsonl")
log_path = os.path.join(outdir, "crawl.log")
sess = requests.Session()
sess.headers.update({"User-Agent": UA, "Accept": "application/json"})


def log(msg):
    with open(log_path, "a") as f:
        f.write(f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} {msg}\n")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def to_iso(mdy):
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", mdy or "")
    return f"{m.group(3)}-{m.group(1)}-{m.group(2)}" if m else None


def get(url, tries=5):
    for attempt in range(tries):
        try:
            r = sess.get(url, timeout=90)
            if r.status_code == 200:
                return r
            log(f"{url} HTTP {r.status_code} attempt {attempt}")
            if r.status_code in (404, 410):
                return r
        except Exception as e:
            log(f"{url} error {e!r} attempt {attempt}")
        time.sleep(3 + 4 * attempt)
    return None


# ---- list
listed = {}
if os.path.exists(list_path):
    for line in open(list_path):
        try:
            r = json.loads(line)
            listed[r["biddingoTenderId"]] = r
        except Exception:
            pass
if not listed:
    page = 0
    with open(list_path, "a") as f:
        while True:
            r = get(f"{API}/v2/noauthorize/bids?offset={page}&limit=50&statuses=5&sort=postedDate%3Adesc")
            if r is None or r.status_code != 200:
                log(f"list page {page} FAILED")
                break
            d = r.json()
            rows = d.get("bidInfoList", [])
            if page == 0:
                log(f"list: bidCount {d.get('bidCount')}")
            for x in rows:
                x["_retrieved_at"] = now()
                x["_list_page"] = page
                f.write(json.dumps(x, ensure_ascii=False) + "\n")
                listed[x["biddingoTenderId"]] = x
            f.flush()
            if not rows:
                log(f"list page {page}: no rows; done")
                break
            dates = [to_iso(x.get("publishedDate")) for x in rows if to_iso(x.get("publishedDate"))]
            if page % 20 == 0:
                log(f"list page {page}: {len(rows)} rows, last posted {dates[-1] if dates else None}")
            if dates and max(dates) < min_posted:
                log(f"list page {page}: reached min posted date {min_posted}; stopping")
                break
            page += 1
            time.sleep(0.4)
log(f"list rows: {len(listed)}")

# ---- details (newest posted first)
done = set()
if os.path.exists(details_path):
    for line in open(details_path):
        try:
            done.add(json.loads(line)["biddingoTenderId"])
        except Exception:
            pass
order = sorted(listed.values(), key=lambda x: to_iso(x.get("publishedDate")) or "", reverse=True)
n = 0
with open(details_path, "a") as f:
    for x in order:
        tid = x["biddingoTenderId"]
        if tid in done:
            continue
        if (to_iso(x.get("publishedDate")) or "9999") < min_posted:
            continue
        url = f"{API}/bidding/noauthorize/{x['buyerSysId']}/{x['buyerOrgId']}/{tid}"
        r = get(url)
        rec = {"biddingoTenderId": tid, "list_row": x, "detail_url": url, "retrieved_at": now()}
        if r is None:
            rec["http_status"] = None
            rec["failed"] = True
        else:
            rec["http_status"] = r.status_code
            if r.status_code == 200:
                try:
                    rec["detail"] = r.json()
                except Exception as e:
                    rec["parse_error"] = str(e)
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        f.flush()
        done.add(tid)
        n += 1
        if n % 200 == 0:
            log(f"details written {n} (posted {x.get('publishedDate')})")
        if n >= max_details:
            break
        time.sleep(0.35)
log(f"details done: wrote {n}")
log("done")

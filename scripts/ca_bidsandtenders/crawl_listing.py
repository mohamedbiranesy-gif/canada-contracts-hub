#!/usr/bin/env python3
"""Crawl the bids&tenders aggregator listing of Awarded bids.

https://opportunities.bidsandtenders.com/bid-opportunities/Embed?status=Awarded&page=N&pageSize=50&sort=UtcClosingDate&dir=DESC

Saves each page's HTML under <outdir>/pages/page_NNNNN.html and appends parsed rows to
<outdir>/listing.jsonl (one JSON per bid row). Resumable: existing page files are skipped.
Usage: python3 -I crawl_listing.py <outdir> [max_pages]
"""
import sys, os, re, json, time, html, datetime
import requests

UA = "contracts-research/1.0"
BASE = "https://opportunities.bidsandtenders.com/bid-opportunities/Embed"
RATE_SLEEP = 0.3  # ~3 req/s

outdir = sys.argv[1]
max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
pages_dir = os.path.join(outdir, "pages")
os.makedirs(pages_dir, exist_ok=True)
listing_path = os.path.join(outdir, "listing.jsonl")
log_path = os.path.join(outdir, "crawl_listing.log")

ROW_RE = re.compile(r'<tr class="bt-row">(.*?)</tr>', re.S)
TD_RE = re.compile(r'<td class="([^"]*)">(.*?)</td>', re.S)


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_page(h, page_no):
    rows = []
    for m in ROW_RE.finditer(h):
        seg = m.group(1)
        rec = {"_listing_page": page_no}
        for cm in TD_RE.finditer(seg):
            cls, inner = cm.group(1), cm.group(2)
            if "bt-bid-name" in cls:
                rec["bid_name"] = clean(inner)
            elif "bt-cell--status" in cls:
                rec["status"] = clean(inner)
            elif "bt-date-cell" in cls:
                du = re.search(r'data-utc="([^"]+)"', inner)
                tz = re.search(r'data-source-tz="([^"]+)"', inner)
                key = "published_utc" if "published_utc" not in rec else "closing_utc"
                rec[key] = du.group(1) if du else clean(inner)
                rec[key + "_source_tz"] = tz.group(1) if tz else None
            elif "bt-cell--org" in cls:
                rec["organization"] = clean(inner)
            elif "bt-cell--fees" in cls:
                rec["document_fees"] = clean(inner)
            elif "bt-cell--bid-type" in cls:
                rec["bid_type"] = clean(inner)
            elif "bt-cell--view" in cls:
                u = re.search(r'href="([^"]+)"', inner)
                rec["detail_url"] = html.unescape(u.group(1)) if u else None
        if rec.get("detail_url"):
            mm = re.search(r"https://([A-Za-z0-9.-]+)/Module/Tenders/(en|fr)/Tender/Detail/([0-9a-fA-F-]+)", rec["detail_url"])
            if mm:
                rec["portal"] = mm.group(1).lower().replace(".bidsandtenders.ca", "")
                rec["portal_host"] = mm.group(1)
                rec["tender_id"] = mm.group(3).lower()
        rows.append(rec)
    return rows


def log(msg):
    with open(log_path, "a") as f:
        f.write(f"{datetime.datetime.utcnow().isoformat()}Z {msg}\n")


sess = requests.Session()
sess.headers["User-Agent"] = UA
total_results = None
page = 0
seen_pages = set()
if os.path.exists(listing_path):
    with open(listing_path) as f:
        for line in f:
            try:
                seen_pages.add(json.loads(line)["_listing_page"])
            except Exception:
                pass

with open(listing_path, "a") as out:
    while page < max_pages:
        fn = os.path.join(pages_dir, f"page_{page:05d}.html")
        if page in seen_pages and os.path.exists(fn):
            page += 1
            continue
        url = f"{BASE}?status=Awarded&page={page}&pageSize=50&sort=UtcClosingDate&dir=DESC"
        h = None
        for attempt in range(4):
            try:
                r = sess.get(url, timeout=60)
                if r.status_code == 200:
                    h = r.text
                    break
                log(f"page {page} HTTP {r.status_code} attempt {attempt}")
            except Exception as e:
                log(f"page {page} error {e!r} attempt {attempt}")
            time.sleep(2 + 3 * attempt)
        if h is None:
            log(f"page {page} FAILED, stopping")
            break
        with open(fn, "w", encoding="utf-8") as f:
            f.write(h)
        m = re.search(r"Showing ([\d,]+) to ([\d,]+) of ([\d,]+) results", h)
        if m:
            total_results = int(m.group(3).replace(",", ""))
        rows = parse_page(h, page)
        for rec in rows:
            rec["_retrieved_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        out.flush()
        if page % 50 == 0:
            log(f"page {page} rows {len(rows)} total_results {total_results}")
        if not rows:
            log(f"page {page} had no rows; stopping (total_results={total_results})")
            break
        if total_results is not None and (page + 1) * 50 >= total_results:
            log(f"reached end at page {page} (total_results={total_results})")
            break
        page += 1
        time.sleep(RATE_SLEEP)
log("done")

#!/usr/bin/env python3
"""Crawl the public MERX "Awarded Solicitations" listing, newest award first.

https://www.merx.com/public/solicitations/awarded?keywords=&sortBy=awardedDate&sortDirection=DESC&pageNumber=N
(25 rows per page). Saves pages under <outdir>/pages and parsed rows to <outdir>/listing.jsonl.
Stops when the award date drops below <min_award_date> (YYYY/MM/DD) or pages run out.
Usage: python3 -I crawl_listing.py <outdir> <min_award_date YYYY-MM-DD> [max_pages] [partitions]
  partitions: comma-separated list of extra query strings, e.g. "location=355,location=373&category=10004";
  MERX caps any listing at 1,000 results (40 pages x 25), so partitions (location/category) are
  crawled one after another (newest award first) and rows are de-duplicated later by merx_id.
"""
import sys, os, re, json, time, html, datetime
import requests

UA = "contracts-research/1.0"
BASE = "https://www.merx.com/public/solicitations/awarded"
outdir = sys.argv[1]
min_award = sys.argv[2]
max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
partitions = sys.argv[4].split(",") if len(sys.argv) > 4 and sys.argv[4] else [""]
pages_dir = os.path.join(outdir, "pages")
os.makedirs(pages_dir, exist_ok=True)
listing_path = os.path.join(outdir, "listing.jsonl")
log_path = os.path.join(outdir, "crawl_listing.log")

ROW_RE = re.compile(r'<tr\s+data-index="\d+"\s+class="mets-table-row[^"]*">(.*?)</tr>', re.S)


def log(msg):
    with open(log_path, "a") as f:
        f.write(f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} {msg}\n")


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_rows(h, page):
    out = []
    for m in ROW_RE.finditer(h):
        r = m.group(1)
        idm = re.search(r'id="searchResultSol_(solicitation|notice)_(\d+)"', r)
        href = re.search(r'href="([^"]+)"', r)
        title = re.search(r'class="rowTitle">\s*(.*?)</span>', r, re.S)
        buyer = re.search(r'class="buyer-name">\s*(.*?)</span>', r, re.S)
        loc = re.search(r'class="location">\s*(.*?)</span>', r, re.S)
        pub = re.search(r'class="publicationDate">.*?<span class="dateValue">([^<]+)</span>', r, re.S)
        aw = re.search(r'class="awardDate">.*?<span class="dateValue">([^<]+)</span>', r, re.S)
        icon = re.search(r'data-mets-tooltip="([^"]+)"', r)
        rec = {
            "_listing_page": page,
            "row_type": idm.group(1) if idm else None,
            "merx_id": idm.group(2) if idm else None,
            "href": html.unescape(href.group(1)) if href else None,
            "title": clean(title.group(1)) if title else None,
            "buyer": clean(buyer.group(1)) if buyer else None,
            "location": clean(loc.group(1)) if loc else None,
            "publication_date": pub.group(1).strip() if pub else None,
            "award_date": aw.group(1).strip() if aw else None,
            "icon_tooltip": icon.group(1) if icon else None,
            "_retrieved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        out.append(rec)
    return out


sess = requests.Session()
sess.headers["User-Agent"] = UA
min_award_slash = min_award.replace("-", "/")


FINISHED_TAGS = set()
if os.path.exists(log_path):
    for _l in open(log_path):
        _m = re.search(r"\[([A-Za-z0-9_]+)\] page \d+ (?:reached|no rows)", _l)
        if _m:
            FINISHED_TAGS.add(_m.group(1))


def crawl_partition(part):
    tag = re.sub(r"[^A-Za-z0-9]+", "_", part) or "all"
    if tag in FINISHED_TAGS:
        return
    done_pages = set()
    known_total = None
    if os.path.exists(listing_path):
        with open(listing_path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    if r.get("_partition", "") == part:
                        done_pages.add(r["_listing_page"])
                        if r.get("_partition_total_results") is not None:
                            known_total = r["_partition_total_results"]
                except Exception:
                    pass
    if done_pages and known_total is not None and max(done_pages) * 25 >= known_total:
        return
    if done_pages and known_total is not None and max(done_pages) >= 40:
        return
    page = 1
    with open(listing_path, "a") as out:
        while page <= max_pages:
            if page in done_pages:
                page += 1
                continue
            url = f"{BASE}?keywords=&{part + '&' if part else ''}sortBy=awardedDate&sortDirection=DESC&pageNumber={page}"
            h = None
            for attempt in range(8):
                try:
                    r = sess.get(url, timeout=60)
                    if r.status_code == 200 and ('searchResultSol_' in r.text or re.search(r"\(\s*0 results?\)", r.text) or 'No Results' in r.text or 'returned no results' in r.text):
                        h = r.text
                        break
                    log(f"[{tag}] page {page} HTTP {r.status_code} len {len(r.text)} attempt {attempt}")
                except Exception as e:
                    log(f"[{tag}] page {page} error {e!r} attempt {attempt}")
                time.sleep(5 + 10 * attempt)
            if h is None:
                log(f"[{tag}] page {page} FAILED; stopping partition")
                return
            with open(os.path.join(pages_dir, f"{tag}_page_{page:05d}.html"), "w", encoding="utf-8") as f:
                f.write(h)
            rows = parse_rows(h, page)
            tot = re.search(r"\(\s*([\d,]+) results?\s*\)", h)
            total = int(tot.group(1).replace(",", "")) if tot else None
            for rec in rows:
                rec["_partition"] = part
                rec["_partition_total_results"] = total
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush()
            if page % 10 == 0 or page == 1:
                log(f"[{tag}] page {page} rows {len(rows)} last award {rows[-1]['award_date'] if rows else None} total {total}")
            if not rows:
                log(f"[{tag}] page {page} no rows; stopping partition")
                return
            dates = [r["award_date"] for r in rows if r.get("award_date") and r["award_date"][:4].isdigit() and int(r["award_date"][:4]) < 2100]
            if dates and max(dates) < min_award_slash:
                log(f"[{tag}] page {page} reached min award date ({max(dates)} < {min_award_slash}); stopping partition")
                return
            if total is not None and page * 25 >= total:
                log(f"[{tag}] page {page} reached end of partition (total {total})")
                return
            if page >= 40:
                log(f"[{tag}] page {page} reached MERX 1000-result cap (total {total})")
                return
            page += 1
            time.sleep(1.0)


for part in partitions:
    crawl_partition(part)
log("done")

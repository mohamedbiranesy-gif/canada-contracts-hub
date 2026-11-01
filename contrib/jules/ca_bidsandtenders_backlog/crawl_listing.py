#!/usr/bin/env python3
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

def log(msg):
    print(msg)
    with open(log_path, "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()} {msg}\n")

# From notes/ca_bidsandtenders.md, pages 0-2046 were crawled.
# We want to crawl 2047 onwards
start_page = 2047

def crawl():
    s = requests.Session()
    s.headers.update({"User-Agent": UA})
    for page in range(start_page, start_page + max_pages):
        page_file = os.path.join(pages_dir, f"page_{page:05d}.html")
        if os.path.exists(page_file):
            continue

        url = f"{BASE}?status=Awarded&page={page}&pageSize=50&sort=UtcClosingDate&dir=DESC"
        log(f"Fetching page {page} {url}")
        resp = s.get(url, timeout=15)
        if resp.status_code != 200:
            log(f"Error {resp.status_code}")
            time.sleep(5)
            continue

        html_txt = resp.text
        with open(page_file, "w") as f:
            f.write(html_txt)

        rows = ROW_RE.findall(html_txt)
        if not rows:
            log("No more rows")
            break

        with open(listing_path, "a") as f:
            for row in rows:
                cols = TD_RE.findall(row)
                d = {k.strip(): clean(v) for k, v in cols}
                if 'data-title' in row:
                    m = re.search(r'data-title="([^"]+)"', row)
                    if m: d['title'] = clean(m.group(1))
                if 'href' in row:
                    m = re.search(r'href="([^"]+)"', row)
                    if m: d['href'] = clean(m.group(1))
                f.write(json.dumps(d) + "\n")

        time.sleep(RATE_SLEEP)

if __name__ == "__main__":
    crawl()

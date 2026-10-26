#!/usr/bin/env python3
"""Crawl SaskTenders awarded competitions listing pages.
https://www.sasktenders.ca/Search?statusId=83773de3-960f-416f-a511-bbd76ff1812f&pageSize=100&pageNumber=N
(statusId = "Awarded" option value). Each page embeds full competition cards incl. "Award Details"
(vendor name, "City, REGION", amount, award date). Pages saved verbatim; resumable.
Usage: python3 -I crawl_sasktenders.py <download_dir> [sortField] [sortDirection]
"""
import os, sys, time, re, datetime as dt
import requests

OUT = sys.argv[1]
SORT = sys.argv[2] if len(sys.argv) > 2 else "closedate"
DIR = sys.argv[3] if len(sys.argv) > 3 else "desc"
os.makedirs(os.path.join(OUT, "pages"), exist_ok=True)
UA = {"User-Agent": "contracts-research/1.0"}
STATUS_AWARDED = "83773de3-960f-416f-a511-bbd76ff1812f"
LOG = open(os.path.join(OUT, "crawl.log"), "a")


def log(m):
    line = f"{dt.datetime.utcnow().isoformat()}Z {m}"
    LOG.write(line + "\n"); LOG.flush(); print(line, flush=True)


def fetch(page):
    url = (f"https://www.sasktenders.ca/Search?statusId={STATUS_AWARDED}&sortField={SORT}"
           f"&sortDirection={DIR}&pageSize=100&pageNumber={page}")
    for attempt in range(6):
        try:
            r = requests.get(url, headers=UA, timeout=120)
            if r.status_code == 200 and "Competition #" in r.text:
                return r.text
            log(f"page {page} HTTP {r.status_code} len={len(r.text)}")
        except Exception as e:
            log(f"page {page} EXC {e}")
        time.sleep(3 + 4 * attempt)
    return None


first = fetch(1)
if first is None:
    log("cannot fetch page 1"); sys.exit(1)
m = re.search(r'(\d[\d,]*)\s*results', first)
total = int(m.group(1).replace(",", "")) if m else None
pages = (total + 99) // 100 if total else None
log(f"total results={total} pages={pages}")
open(os.path.join(OUT, "pages", "page_0001.html"), "w").write(first)
p = 2
while pages is None or p <= pages:
    path = os.path.join(OUT, "pages", f"page_{p:04d}.html")
    if os.path.exists(path) and os.path.getsize(path) > 50000:
        p += 1; continue
    t = fetch(p)
    if t is None:
        log(f"GIVE UP page {p}"); p += 1; continue
    open(path, "w").write(t)
    n = len(re.findall(r'/Competitions/Print\?id=', t))
    if p % 10 == 0:
        log(f"page {p}/{pages} print-links={n}")
    if n == 0:
        log(f"page {p} has no competitions; stopping"); break
    p += 1
    time.sleep(0.4)
log("DONE")

"""Stage A: crawl Cision 'Contracts' category listings (newswire.ca + prnewswire.com)
and write candidate rows to downloads/private_press/candidates_<site>.jsonl"""
import requests, re, time, json, sys, datetime
from bs4 import BeautifulSoup
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
OUT = "downloads/private_press"
site = sys.argv[1]  # newswire or prnewswire
start = int(sys.argv[2]); end = int(sys.argv[3])
base = {"newswire": "https://www.newswire.ca", "prnewswire": "https://www.prnewswire.com"}[site]
path = "/news-releases/financial-services-latest-news/contracts-list/"
out = open(f"{OUT}/candidates_{site}.jsonl", "a", encoding="utf-8")
log = open(f"{OUT}/crawl_{site}.log", "a")
empty_streak = 0
for page in range(start, end+1):
    u = f"{base}{path}?page={page}&pagesize=100"
    for attempt in range(4):
        try:
            r = requests.get(u, headers=UA, timeout=40)
            if r.status_code == 200: break
            log.write(f"{datetime.datetime.utcnow().isoformat()} page {page} status {r.status_code} attempt {attempt}\n"); log.flush()
            time.sleep(5*(attempt+1))
        except Exception as e:
            log.write(f"page {page} error {e}\n"); log.flush(); time.sleep(5)
    else:
        print("giving up page", page); continue
    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.select("div.card.col-view")
    n = 0
    for c in cards:
        a = c.select_one("a.newsreleaseconsolidatelink")
        if not a: continue
        h3 = c.select_one("h3"); small = c.select_one("h3 small"); p = c.select_one("p")
        dt = small.get_text(strip=True) if small else None
        title = h3.get_text(" ", strip=True).replace(dt or "", "").strip() if h3 else None
        row = {"site": site, "page": page, "url": base + a.get("href"), "title": title, "list_date": dt,
               "summary": p.get_text(" ", strip=True) if p else None,
               "retrieved_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"}
        out.write(json.dumps(row, ensure_ascii=False)+"\n"); n += 1
    out.flush()
    print(f"page {page}: {n} cards; last date {dt}", flush=True)
    log.write(f"{datetime.datetime.utcnow().isoformat()} {u} status {r.status_code} bytes {len(r.content)} cards {n}\n"); log.flush()
    if n == 0:
        empty_streak += 1
        if empty_streak >= 2: break
    else: empty_streak = 0
    time.sleep(2.5)

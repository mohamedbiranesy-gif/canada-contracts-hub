"""Stage A2: newswire.ca keyword search (recent-first, ~25-30 results/query) + company pages.
Appends to candidates_search.jsonl (dedupe later)."""
import requests, re, time, json, sys, datetime, os
from bs4 import BeautifulSoup
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
OUT = "downloads/private_press"
base = "https://www.newswire.ca"
seen = set()
for f in ["candidates_newswire.jsonl","candidates_search.jsonl"]:
    p = f"{OUT}/{f}"
    if os.path.exists(p):
        for l in open(p):
            try: seen.add(json.loads(l)["url"])
            except: pass
out = open(f"{OUT}/candidates_search.jsonl","a",encoding="utf-8")
log = open(f"{OUT}/crawl_search.log","a")
def get(u):
    for attempt in range(4):
        try:
            r = requests.get(u, headers=UA, timeout=45)
            if r.status_code == 200: return r
            time.sleep(5*(attempt+1))
        except Exception: time.sleep(5)
    return None
def parse(r, label, page):
    soup = BeautifulSoup(r.text, "lxml")
    n=0; new=0
    for c in soup.select("div.row.newsCards > div.card, div.card.col-view"):
        a = c.select_one("a.newsreleaseconsolidatelink") or c.select_one("h3 a") or c.find("a", href=re.compile(r'/news-releases/.*\d{6,}\.html'))
        if not a: continue
        h3 = c.select_one("h3"); small = c.select_one("h3 small"); p = c.select_one("p")
        if p and p.find("em"): p = None
        dt = small.get_text(strip=True) if small else None
        title = h3.get_text(" ", strip=True).replace(dt or "", "").strip() if h3 else None
        url = base + a.get("href") if a.get("href","").startswith("/") else a.get("href")
        n+=1
        if url in seen: continue
        seen.add(url); new+=1
        out.write(json.dumps({"site":"newswire","query":label,"page":page,"url":url,"title":title,"list_date":dt,
            "summary": p.get_text(" ", strip=True) if p else None,
            "retrieved_at": datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")}, ensure_ascii=False)+"\n")
    out.flush()
    return n, new
mode = sys.argv[1]
if mode == "keywords":
    KW = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
    for kw in KW:
        u = f"{base}/search/news/?keyword={requests.utils.quote(kw)}&page=1&pagesize=100"
        r = get(u)
        if not r: log.write(f"FAIL {u}\n"); continue
        n,new = parse(r, "kw:"+kw, 1)
        log.write(f"{datetime.datetime.now(datetime.UTC).isoformat()} {u} cards={n} new={new}\n"); log.flush()
        print(f"{kw!r}: {n} cards, {new} new", flush=True)
        time.sleep(2.5)
elif mode == "companies":
    slugs = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
    for slug in slugs:
        for page in range(1, 6):
            u = f"{base}/news/{slug}/?page={page}&pagesize=100"
            r = get(u)
            if not r: log.write(f"FAIL {u}\n"); break
            n,new = parse(r, "co:"+slug, page)
            log.write(f"{datetime.datetime.now(datetime.UTC).isoformat()} {u} cards={n} new={new}\n"); log.flush()
            print(f"{slug} p{page}: {n} cards, {new} new", flush=True)
            # stop when oldest date on page < 2023
            dates = re.findall(r'(\w{3} \d{2}, (\d{4})), \d{2}:\d{2} ET', r.text)
            if n < 100 or (dates and int(dates[-1][1]) < 2023): break
            time.sleep(2.5)
        time.sleep(2)
elif mode == "categories":
    cats = [l.strip() for l in open(sys.argv[2]) if l.strip() and not l.startswith("#")]
    for cat in cats:
        empty=0
        for page in range(1, 40):
            u = f"{base}/news-releases/{cat}/?page={page}&pagesize=100"
            r = get(u)
            if not r: log.write(f"FAIL {u}\n"); break
            n,new = parse(r, "cat:"+cat, page)
            dates = re.findall(r'(\w{3} \d{2}, (\d{4})), \d{2}:\d{2} ET', r.text)
            log.write(f"{datetime.datetime.now(datetime.UTC).isoformat()} {u} cards={n} new={new} last={dates[-1][0] if dates else None}\n"); log.flush()
            print(f"{cat} p{page}: {n} cards, {new} new, last={dates[-1][0] if dates else None}", flush=True)
            if n == 0:
                empty+=1
                if empty>=2: break
            else: empty=0
            if dates and int(dates[-1][1]) < 2024: break
            time.sleep(2.5)

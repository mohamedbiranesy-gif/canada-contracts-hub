"""Fetch selected Irving Shipbuilding (shipsforcanada.ca) supplier-award stories and extract text + date.
Output: downloads/private_press/fetched_isi.jsonl, HTML saved under downloads/private_press/html/<sha1>.html"""
import requests, re, json, time, hashlib, datetime, os, sys
from bs4 import BeautifulSoup
OUT = "downloads/private_press"
slugs = [l.strip() for l in open(sys.argv[1]) if l.strip()]
done = set()
p = f"{OUT}/fetched_isi.jsonl"
if os.path.exists(p):
    for l in open(p): done.add(json.loads(l)["url"])
out = open(p, "a", encoding="utf-8")
for slug in slugs:
    url = f"https://shipsforcanada.ca/our-stories/{slug}"
    if url in done: continue
    try:
        r = requests.get(url, timeout=40)
    except Exception as e:
        print("ERR", slug, e); continue
    if r.status_code != 200:
        print("HTTP", r.status_code, slug); continue
    sha = hashlib.sha1(url.encode()).hexdigest()
    open(f"{OUT}/html/{sha}.html", "w", encoding="utf-8").write(r.text)
    s = BeautifulSoup(r.text, "lxml")
    title = (s.find("h1").get_text(" ", strip=True) if s.find("h1") else "")
    meta = {}
    for m in s.find_all("meta"):
        n = m.get("name") or m.get("property")
        if n in ("article:published_time", "og:title", "description", "date"): meta[n] = m.get("content")
    tm = s.find("time")
    date_txt = tm.get("datetime") if tm and tm.get("datetime") else (tm.get_text(strip=True) if tm else "")
    body = s.select_one("article") or s.select_one("main") or s
    text = body.get_text("\n", strip=True)
    out.write(json.dumps({"url": url, "sha1": sha, "title": title, "date_txt": date_txt, "meta": meta, "text": text[:20000],
                          "retrieved_at": datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")}, ensure_ascii=False) + "\n")
    out.flush()
    print("ok", slug, date_txt, len(text))
    time.sleep(1.5)

"""Stage B: fetch each candidate release (Cision newswire.ca / prnewswire.com), save HTML,
and write an extracted-facts row to downloads/private_press/fetched_<site>.jsonl"""
import requests, re, time, json, sys, datetime, hashlib, os
from bs4 import BeautifulSoup
UA = {"User-Agent": "contracts-research/1.0", "Accept-Language":"en-CA,en;q=0.9"}
OUT = "downloads/private_press"
HTML_DIR = f"{OUT}/html"; os.makedirs(HTML_DIR, exist_ok=True)
src = sys.argv[1]           # candidates file
outname = sys.argv[2]       # fetched_<x>.jsonl
done = set()
if os.path.exists(f"{OUT}/{outname}"):
    for l in open(f"{OUT}/{outname}"):
        try: done.add(json.loads(l)["url"])
        except: pass
out = open(f"{OUT}/{outname}", "a", encoding="utf-8")
rows = [json.loads(l) for l in open(src)]
def body_soup(html):
    """Cision pages with image galleries contain self-closing <div .../> tags that make lxml close the
    release-body section early (body text after the gallery is lost). Slice the raw section first, fix the
    self-closing divs, then parse the slice."""
    i = html.find('<section class="release-body')
    if i < 0: return None
    j = html.find('</section>', i)
    seg = html[i:j if j > 0 else None]
    seg = re.sub(r'(<div\b[^>]*?)/>', r'\1></div>', seg)
    return BeautifulSoup(seg, "lxml")
def extract(url, html):
    soup = BeautifulSoup(html, "lxml")
    meta = {}
    for m in soup.find_all("meta"):
        n = m.get("name") or m.get("property")
        if n in ("date","keywords","og:title","description","og:url"): meta[n] = m.get("content")
    body = body_soup(html) or soup.select_one("section.release-body") or soup.select_one(".release-body") or soup.find("article")
    text = body.get_text("\n", strip=True) if body else soup.get_text("\n", strip=True)
    # dateline: first paragraph
    first_p = body.find("p") if body else None
    dateline = first_p.get_text(" ", strip=True)[:300] if first_p else ""
    tickers = sorted(set(re.findall(r"\((?:TSX|TSXV|TSX-V|CSE|NYSE|NASDAQ|Nasdaq|NEO|Cboe CA|OTCQX|OTCQB|OTC)[^)]{0,40}\)", text)))
    company_links = sorted(set(a.get_text(" ", strip=True) for a in soup.select("a[href^='/news/']") if a.get_text(strip=True)))
    return {"meta": meta, "dateline": dateline, "tickers": tickers[:8], "company_links": company_links[:5], "text": text}
n=0
for r in rows:
    u = r["url"]
    if u in done: continue
    h = hashlib.sha1(u.encode()).hexdigest()
    for attempt in range(3):
        try:
            resp = requests.get(u, headers=UA, timeout=45)
            if resp.status_code == 200: break
            time.sleep(2.5)
        except Exception as e:
            time.sleep(3)
    else:
        out.write(json.dumps({"url": u, "error": "fetch_failed"})+"\n"); out.flush(); continue
    open(f"{HTML_DIR}/{h}.html","w",encoding="utf-8").write(resp.text)
    try:
        ex = extract(u, resp.text)
    except Exception as e:
        ex = {"error": str(e)}
    row = {"url": u, "sha1": h, "title": r.get("title"), "list_date": r.get("list_date"), "site": r.get("site"),
           "retrieved_at": datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z"),
           "bytes": len(resp.content), **ex}
    out.write(json.dumps(row, ensure_ascii=False)+"\n"); out.flush(); n+=1
    if n % 25 == 0: print(n, "fetched", flush=True)
    time.sleep(0.6)
print("done", n)

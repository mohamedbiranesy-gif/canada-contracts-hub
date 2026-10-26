"""sec_edgar round 2: fetch 6-K/8-K EX-99.x press-release exhibits of Canadian-located filers (EFTS hits not yet
fetched), save text under downloads/sec_edgar/docs/, append rows to docs_index.jsonl (same layout as fetch_docs.py).
usage: fetch_ex99.py <labels comma-separated> [max]"""
import requests, json, time, os, re, datetime, sys
from bs4 import BeautifulSoup
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
OUT = "downloads/sec_edgar"
DOCS = f"{OUT}/docs"
labels = set(sys.argv[1].split(","))
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9
shard, nshards = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, 1)
hits = [json.loads(l) for l in open(f"{OUT}/hits.jsonl")]
done = set(json.loads(l)["_id"] for l in open(f"{OUT}/docs_index.jsonl"))
sel = []
for h in hits:
    s = h["_source"]; ft = (s.get("file_type") or "").upper()
    if s["form"] in ("6-K", "8-K", "6-K/A", "8-K/A") and ft.startswith("EX-99") and h["_id"] not in done and h.get("_query") in labels:
        sel.append(h)
sel.sort(key=lambda h: h["_source"]["file_date"], reverse=True)
sel = sel[shard::nshards]
print("to fetch", len(sel), flush=True)
idx = open(f"{OUT}/docs_index.jsonl", "a", encoding="utf-8")
n = 0
for h in sel[:mx]:
    s = h["_source"]; adsh = s["adsh"]; cik = s["ciks"][0].lstrip("0"); fn = h["_id"].split(":", 1)[1]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
    index_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{adsh}-index.htm"
    txt = None; status = None
    for attempt in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=60); status = r.status_code
            if r.status_code == 200:
                if fn.lower().endswith((".htm", ".html")) or "html" in r.headers.get("content-type", ""):
                    soup = BeautifulSoup(r.content, "lxml")
                    for t in soup(["script", "style"]): t.decompose()
                    txt = soup.get_text("\n", strip=True)
                else:
                    txt = r.text
                break
            time.sleep(1.5 * (attempt + 1))
        except Exception:
            time.sleep(2)
    fname = f"{adsh}__{re.sub(r'[^A-Za-z0-9._-]','_',fn)}.txt"
    if txt is not None:
        open(f"{DOCS}/{fname}", "w", encoding="utf-8").write(txt[:40000])
    idx.write(json.dumps({"_id": h["_id"], "kind": "ex99_pr", "adsh": adsh, "cik": cik, "fn": fn, "url": url, "index_url": index_url,
        "status": status, "chars": len(txt) if txt else 0, "file": fname if txt else None,
        "display_name": s["display_names"][0], "file_date": s["file_date"], "form": s["form"], "file_type": s["file_type"],
        "file_description": s.get("file_description"), "biz_locations": s.get("biz_locations"), "biz_states": s.get("biz_states"),
        "items": s.get("items"), "period_ending": s.get("period_ending"), "query": h.get("_query"),
        "retrieved_at": datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")}, ensure_ascii=False) + "\n")
    idx.flush(); n += 1
    if n % 100 == 0: print(n, flush=True)
    time.sleep(0.25)
print("done", n, flush=True)

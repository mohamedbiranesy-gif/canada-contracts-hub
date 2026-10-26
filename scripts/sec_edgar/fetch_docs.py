"""Stage B (sec_edgar): download EX-10.* exhibits and 8-K main docs (Item 1.01) for Canadian filers;
convert to text; save under downloads/sec_edgar/docs/<adsh>__<fn>.txt; write docs_index.jsonl"""
import requests, json, time, os, re, datetime, sys
from bs4 import BeautifulSoup
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
OUT = "downloads/sec_edgar"
DOCS = f"{OUT}/docs"; os.makedirs(DOCS, exist_ok=True)
hits = [json.loads(l) for l in open(f"{OUT}/hits.jsonl")]
def want(h):
    s = h["_source"]; ft = (s["file_type"] or "").upper()
    if ft.startswith("EX-10"): return "ex10"
    if s["form"] in ("8-K","8-K/A") and ft in ("8-K","8-K/A") and "1.01" in (s.get("items") or []): return "8k_101"
    return None
sel = [(h, want(h)) for h in hits]
sel = [(h,k) for h,k in sel if k]
print("to fetch:", len(sel), {k: sum(1 for _,kk in sel if kk==k) for k in ("ex10","8k_101")})
done = set()
idx_path = f"{OUT}/docs_index.jsonl"
if os.path.exists(idx_path):
    for l in open(idx_path):
        try: done.add(json.loads(l)["_id"])
        except: pass
idx = open(idx_path, "a", encoding="utf-8")
n=0
for h,kind in sel:
    if h["_id"] in done: continue
    s = h["_source"]; adsh = s["adsh"]; cik = s["ciks"][0].lstrip("0"); fn = h["_id"].split(":",1)[1]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
    index_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{adsh}-index.htm"
    txt=None; status=None
    for attempt in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=60); status=r.status_code
            if r.status_code==200:
                ct = r.headers.get("content-type","")
                if fn.lower().endswith((".htm",".html")) or "html" in ct:
                    soup = BeautifulSoup(r.content, "lxml")
                    for t in soup(["script","style"]): t.decompose()
                    txt = soup.get_text("\n", strip=True)
                else:
                    txt = r.text
                break
            time.sleep(1.5*(attempt+1))
        except Exception as e:
            time.sleep(2)
    fname = f"{adsh}__{re.sub(r'[^A-Za-z0-9._-]','_',fn)}.txt"
    if txt is not None:
        open(f"{DOCS}/{fname}","w",encoding="utf-8").write(txt)
    idx.write(json.dumps({"_id": h["_id"], "kind": kind, "adsh": adsh, "cik": cik, "fn": fn, "url": url, "index_url": index_url,
        "status": status, "chars": len(txt) if txt else 0, "file": fname if txt else None,
        "display_name": s["display_names"][0], "file_date": s["file_date"], "form": s["form"], "file_type": s["file_type"],
        "file_description": s.get("file_description"), "biz_locations": s.get("biz_locations"), "biz_states": s.get("biz_states"),
        "items": s.get("items"), "period_ending": s.get("period_ending"), "query": h.get("_query"),
        "retrieved_at": datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")}, ensure_ascii=False)+"\n")
    idx.flush(); n+=1
    if n%50==0: print(n, flush=True)
    time.sleep(0.12)
print("done", n)

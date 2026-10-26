import requests, json, time, re, datetime, sys, warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
OUT="downloads/sec_edgar"; DOCS=f"{OUT}/docs"
hits = {json.loads(l)["_id"]: json.loads(l) for l in open(f"{OUT}/hits.jsonl")}
have = set(json.loads(l)["_id"] for l in open(f"{OUT}/docs_index.jsonl"))
idx = open(f"{OUT}/docs_index.jsonl","a",encoding="utf-8")
def want(h):
    s=h["_source"]; n=s["display_names"][0]; ft=s["file_type"]; d=s["file_date"]
    rules = [("Theratechnologies", ("EX-4.27","EX-4.28")), ("Milestone Pharmaceuticals", ("EX-10.24",)), ("MERCER", ("EX-10.1",)), ("Loop Industries", ("EX-10.1",)),
             ("Profound Medical", ("EX-10.7","EX-10.8","EX-99.1")), ("Lexaria", ("EX-10.6","EX-10.2","EX-10.4")), ("INTERMAP", ("EX-99.1",)), ("Largo", ("EX-99.1",)),
             ("KELSO", ("EX-99.3",)), ("Electra Battery", ("EX-99.1",)), ("Algoma", ("EX-99.1",)), ("Zentek", ("EX-99.1",)), ("Satellos", ("EX-99.1",)), ("Karbon-X", ("EX-10.9",)),
             ("Above Food", ("EX-10.29","EX-10.15")), ("Canopy Growth", ("EX-10.3",)), ("EVOME", ("EX-99.1",)), ("POET", ("EX-99.1",)), ("GREENPOWER", ("EX-99.2",)), ("Bragg Gaming", ("EX-99.1",)),
             ("Atlas Corp", ("EX-4.19",)), ("ENBRIDGE", ("EX-10.1","EX-10.4"))]
    for name, fts in rules:
        if name in n and ft in fts and h["_id"] not in have and s["form"] not in ("40FR12B",): return True
    return False
sel=[h for h in hits.values() if want(h)]
print(len(sel))
for h in sel:
    s=h["_source"]; adsh=s["adsh"]; cik=s["ciks"][0].lstrip("0"); fn=h["_id"].split(":",1)[1]
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
    try:
        r=requests.get(url, headers=UA, timeout=60)
    except Exception as e:
        print("ERR", url, e); continue
    if r.status_code!=200: print("fail", url, r.status_code); continue
    soup=BeautifulSoup(r.content,"lxml"); [t.decompose() for t in soup(["script","style"])]
    txt=soup.get_text("\n", strip=True)
    fname=f"{adsh}__{re.sub(r'[^A-Za-z0-9._-]','_',fn)}.txt"; open(f"{DOCS}/{fname}","w",encoding="utf-8").write(txt)
    idx.write(json.dumps({"_id":h["_id"],"kind":"extra","adsh":adsh,"cik":cik,"fn":fn,"url":url,"index_url":f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{adsh}-index.htm","status":200,"chars":len(txt),"file":fname,"display_name":s["display_names"][0],"file_date":s["file_date"],"form":s["form"],"file_type":s["file_type"],"file_description":s.get("file_description"),"biz_locations":s.get("biz_locations"),"biz_states":s.get("biz_states"),"items":s.get("items"),"period_ending":s.get("period_ending"),"query":h.get("_query"),"retrieved_at":datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")}, ensure_ascii=False)+"\n"); idx.flush()
    flat=re.sub(r"\s+"," ",txt)
    print("="*90); print(s["display_names"][0][:50], s["file_date"], s["form"], s["file_type"], url); print(flat[:700])
    for p in [r"(?:Initial Term|initial term)[^.]{0,250}\.", r"(?:expire|terminate)s? (?:on|upon) [^.]{0,120}\.", r"[Tt]erm of (?:this|the) Agreement[^.]{0,200}\."]:
        m=re.search(p, flat)
        if m: print("  >>", flat[max(0,m.start()-100):m.end()+60])
    time.sleep(0.2)

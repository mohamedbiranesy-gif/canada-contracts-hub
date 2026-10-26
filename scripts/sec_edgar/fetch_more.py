import requests, json, time, re, datetime, os
from bs4 import BeautifulSoup
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
OUT="downloads/sec_edgar"; DOCS=f"{OUT}/docs"
hits = {json.loads(l)["_id"]: json.loads(l) for l in open(f"{OUT}/hits.jsonl")}
idx = open(f"{OUT}/docs_index.jsonl","a",encoding="utf-8")
have = set(json.loads(l)["_id"] for l in open(f"{OUT}/docs_index.jsonl"))
want = [k for k,h in hits.items() if any(x in k for x in ["0001213900-25", "0001104659-25"]) and "PSYENCE" in h["_source"]["display_names"][0] and h["_source"]["file_date"]=="2025-06-11"]
want += [k for k,h in hits.items() if "CANNAPHARMARX" in h["_source"]["display_names"][0] and h["_source"]["file_type"]=="EX-1.1"]
want += [k for k,h in hits.items() if "Intellipharmaceutics" in h["_source"]["display_names"][0] and h["_source"]["file_type"]=="EX-4.87"]
want += [k for k,h in hits.items() if "Bitfarms" in h["_source"]["display_names"][0] and h["_source"]["file_date"]=="2024-11-04" and h["_source"]["file_type"]=="EX-99.2"]
want += [k for k,h in hits.items() if "Clearmind" in h["_source"]["display_names"][0] and h["_source"]["file_type"] in ("EX-4.31","EX-4.19","EX-4.20","EX-99.1")]
want += [k for k,h in hits.items() if "FSD Pharma" in h["_source"]["display_names"][0] and h["_source"]["file_type"]=="EX-4.3"]
want += [k for k,h in hits.items() if "Pinnacle Food" in h["_source"]["display_names"][0] and h["_source"]["file_type"]=="EX-4.17"]
print(len(want))
for k in want:
    if k in have: continue
    h=hits[k]; s=h["_source"]; adsh=s["adsh"]; cik=s["ciks"][0].lstrip("0"); fn=k.split(":",1)[1]
    url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
    r=requests.get(url, headers=UA, timeout=60)
    if r.status_code!=200: print("fail", url, r.status_code); continue
    soup=BeautifulSoup(r.content,"lxml"); [t.decompose() for t in soup(["script","style"])]
    txt=soup.get_text("\n", strip=True)
    fname=f"{adsh}__{re.sub(r'[^A-Za-z0-9._-]','_',fn)}.txt"; open(f"{DOCS}/{fname}","w",encoding="utf-8").write(txt)
    idx.write(json.dumps({"_id":k,"kind":"extra","adsh":adsh,"cik":cik,"fn":fn,"url":url,"index_url":f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{adsh}-index.htm","status":200,"chars":len(txt),"file":fname,"display_name":s["display_names"][0],"file_date":s["file_date"],"form":s["form"],"file_type":s["file_type"],"file_description":s.get("file_description"),"biz_locations":s.get("biz_locations"),"biz_states":s.get("biz_states"),"items":s.get("items"),"period_ending":s.get("period_ending"),"query":h.get("_query"),"retrieved_at":datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")}, ensure_ascii=False)+"\n"); idx.flush()
    flat=re.sub(r"\s+"," ",txt)
    print("="*90); print(s["display_names"][0], s["file_date"], s["file_type"], url); print(flat[:900])
    for p in [r"(?:Term|TERM)\s*[\.:]\s*(?:This|The)[^.]{0,300}\.", r"(?:initial term|Initial Term)[^.]{0,250}\.", r"(?:expire|terminate)s? on [^.]{0,120}\."]:
        m=re.search(p, flat)
        if m: print("  >>", flat[m.start():m.end()+100])
    time.sleep(0.2)

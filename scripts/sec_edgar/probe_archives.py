import requests, json, time
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate", "Host": "www.sec.gov"}
hits = [json.loads(l) for l in open("downloads/sec_edgar/hits.jsonl")]
ex10 = [h for h in hits if h["_source"]["file_type"].upper().startswith("EX-10")][:3]
for h in ex10:
    adsh = h["_source"]["adsh"]; cik = h["_source"]["ciks"][0].lstrip("0"); fn = h["_id"].split(":")[1]
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
    idx = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{adsh}-index.htm"
    for u in (url, idx):
        r = requests.get(u, headers={"User-Agent": "contracts-research research@example.com"}, timeout=60)
        print(r.status_code, len(r.content), u)
        time.sleep(0.2)
# data.sec.gov submissions
r = requests.get("https://data.sec.gov/submissions/CIK0001860742.json", headers={"User-Agent": "contracts-research research@example.com"}, timeout=60)
print(r.status_code, len(r.content), "data.sec.gov submissions")
if r.status_code==200:
    j=r.json(); print(j.get("name"), j.get("stateOfIncorporation"), j.get("addresses",{}).get("business"))

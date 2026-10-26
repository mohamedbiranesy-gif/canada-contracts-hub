import requests, json, sys, time
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
d = json.load(open("downloads/sec_edgar/probe1.json"))
print("top-level keys:", list(d.keys()))
print("aggregations keys:", list(d.get("aggregations",{}).keys()))
for k,v in d.get("aggregations",{}).items():
    print(k, json.dumps(v)[:600])
# test location filter
for param in ["locationCodes", "locationCode", "biz_states"]:
    url = f"https://efts.sec.gov/LATEST/search-index?q=%22agreement%22&forms=8-K&dateRange=custom&startdt=2024-01-01&enddt=2026-10-25&{param}=A6"
    r = requests.get(url, headers=UA, timeout=60)
    j = r.json()
    hits = j["hits"]["hits"]
    states = set()
    for h in hits:
        states.update(h["_source"].get("biz_states",[]))
    print(param, r.status_code, "total:", j["hits"]["total"], "states in first page:", states)
    time.sleep(0.3)

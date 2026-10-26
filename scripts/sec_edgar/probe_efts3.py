import requests, json, time, urllib.parse
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
CA_CODES = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","B0","Z4"]  # AB, BC, MB, NB, NL, NS, ON, PE, QC, SK, YT, CANADA (federal)
def q(params):
    url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode(params)
    r = requests.get(url, headers=UA, timeout=60)
    return r.json()
# Which codes are valid? Test counts.
for code in CA_CODES:
    j = q({"q": "agreement", "forms": "8-K", "dateRange":"custom","startdt":"2024-01-01","enddt":"2026-10-25","locationCodes": code})
    print(code, j["hits"]["total"])
    time.sleep(0.2)
# Combined codes?
j = q({"q": "agreement", "forms": "8-K", "dateRange":"custom","startdt":"2024-01-01","enddt":"2026-10-25","locationCodes": "A6,A8"})
print("A6,A8 combined:", j["hits"]["total"])
# file_type filter? e.g. EX-10
j = q({"q": "agreement", "forms": "EX-10", "dateRange":"custom","startdt":"2024-01-01","enddt":"2026-10-25","locationCodes": "A6"})
print("forms=EX-10:", j["hits"]["total"], [h["_source"]["file_type"] for h in j["hits"]["hits"][:10]])
# pagination param
j2 = q({"q": "agreement", "forms": "8-K", "dateRange":"custom","startdt":"2024-01-01","enddt":"2026-10-25","locationCodes": "A6", "page": "2", "from": "100"})
print("page2 first id:", j2["hits"]["hits"][0]["_id"], "vs page1:", j["hits"]["hits"][0]["_id"] if j["hits"]["hits"] else None)
print(json.dumps(j2["query"], indent=1)[:800])

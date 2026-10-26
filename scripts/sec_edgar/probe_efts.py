import requests, json, sys
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
url = "https://efts.sec.gov/LATEST/search-index?q=%22material%20contract%22&forms=8-K"
r = requests.get(url, headers=UA, timeout=60)
print(r.status_code, r.headers.get("content-type"))
txt = r.text
print(txt[:3000])
open("downloads/sec_edgar/probe1.json","w").write(txt)

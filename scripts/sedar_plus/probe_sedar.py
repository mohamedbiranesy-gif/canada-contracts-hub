import requests, re, json
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
s = requests.Session()
r = s.get("https://www.sedarplus.ca/csa-party/service/create.html", headers=UA, timeout=30)
print(r.status_code, len(r.text))
html = r.text
open("downloads/sedar_plus/landing.html","w").write(html)
print(re.findall(r'<script[^>]+src="([^"]+)"', html)[:20])
print(re.findall(r'(https?://[^"\' ]+)', html)[:30])
print(html[:1500])
# try a known search endpoint pattern used by SEDAR+ (Liferay / csa-party)
for u in ["https://www.sedarplus.ca/csa-party/records/document.html",
          "https://www.sedarplus.ca/onlinesubmissions/search/searchDocuments",
          "https://www.sedarplus.ca/csa-party/api/searchDocuments",
          "https://www.sedarplus.ca/csa-party/rest/documentSearch"]:
    try:
        rr = s.get(u, headers=UA, timeout=30)
        print(rr.status_code, len(rr.content), rr.headers.get("content-type"), u)
    except Exception as e:
        print("ERR", u, e)

import requests, time, re, json
from bs4 import BeautifulSoup
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
u = "https://www.newswire.ca/news-releases/corby-announces-extension-of-hiram-walker-agreements-868806490.html"
r = requests.get(u, headers=UA, timeout=30)
print(r.status_code, len(r.content))
html = r.text
open("downloads/private_press/sample_release.html","w").write(html)
soup = BeautifulSoup(html, "lxml")
# metadata
for m in soup.find_all("meta"):
    n = m.get("name") or m.get("property")
    if n and any(k in n.lower() for k in ["date","title","description","og:","article","dc.","keywords","location","ticker","company"]):
        print("META", n, "=", (m.get("content") or "")[:150])
# JSON-LD
for s in soup.find_all("script", type="application/ld+json"):
    print("LD+JSON:", s.string[:1500] if s.string else "")
# body
body = soup.select_one(".release-body") or soup.select_one("section.release-body") or soup.find("article")
print("BODY FOUND:", bool(body))
if body:
    txt = body.get_text("\n", strip=True)
    print(txt[:1500])
# dateline
dl = soup.select_one(".release-body p") 
print("first p:", dl.get_text(" ", strip=True)[:200] if dl else None)
# tickers / company links
for a in soup.select("a[href*='/news/']")[:5]:
    print("company link:", a.get("href"), a.get_text(strip=True))

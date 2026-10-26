import requests, re
from bs4 import BeautifulSoup
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
u = "https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/?page=3&pagesize=100"
r = requests.get(u, headers=UA, timeout=40)
soup = BeautifulSoup(r.text, "lxml")
links = set(re.findall(r'href="(/news-releases/[^"]+\d{6,}\.html)"', r.text))
cards = soup.select("div.card.col-view")
card_links = set(c.select_one("a.newsreleaseconsolidatelink").get("href") for c in cards if c.select_one("a.newsreleaseconsolidatelink"))
print(len(links), len(cards), len(card_links))
missing = links - card_links
print("missing sample:", list(missing)[:5])
for m in list(missing)[:2]:
    a = soup.find("a", href=m)
    print(a.find_parent().find_parent().prettify()[:800])

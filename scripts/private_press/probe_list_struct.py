import requests, re, time
from bs4 import BeautifulSoup
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
for page in [30, 5]:
    u = f"https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/?page={page}&pagesize=100"
    r = requests.get(u, headers=UA, timeout=30)
    print(r.status_code, len(r.text), u)
    links = re.findall(r'href="(/news-releases/[^"]+\d{6,}\.html)"', r.text)
    print(" links:", len(set(links)))
    dates = re.findall(r'(\w{3} \d{1,2}, \d{4})', r.text)
    print(" dates:", dates[:3], dates[-3:] if dates else None)
    soup = BeautifulSoup(r.text, "lxml")
    a = soup.find("a", href=re.compile(r'/news-releases/.*\d{6,}\.html'))
    if a:
        container = a.find_parent(["div","li","article"])
        print(container.find_parent().prettify()[:2000])
    time.sleep(2)

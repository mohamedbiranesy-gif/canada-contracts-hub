import requests, re, time
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
for page in [10, 15, 20, 25]:
    u = f"https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/?page={page}&pagesize=100"
    r = requests.get(u, headers=UA, timeout=30)
    links = re.findall(r'href="(/news-releases/[^"]+\d{6,}\.html)"', r.text)
    dates = re.findall(r'(\w{3} \d{2}, \d{4}), \d{2}:\d{2} ET', r.text)
    print(page, r.status_code, "links:", len(set(links)), "dates:", dates[:1], dates[-1:])
    time.sleep(1.5)

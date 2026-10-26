import requests, time, re
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
urls = [
 "https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/",
 "https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/?page=2&pagesize=100",
 "https://www.prnewswire.com/news-releases/financial-services-latest-news/contracts-list/?page=1&pagesize=100",
 "https://www.newswire.ca/rss/financial-services-latest-news/contracts-list.rss",
]
for u in urls:
    try:
        r = requests.get(u, headers=UA, timeout=30, allow_redirects=True)
        print(r.status_code, len(r.content), u)
        if r.status_code==200:
            links = re.findall(r'href="(/news-releases/[^"]+\d{6,}\.html)"', r.text)
            print("  release links:", len(set(links)))
            for l in list(dict.fromkeys(links))[:5]: print("   ", l)
            # look for dates
            dates = re.findall(r'(\d{1,2} \w{3}, \d{4}|\w{3} \d{1,2}, \d{4})', r.text)
            print("  dates sample:", dates[:5])
    except Exception as e:
        print("ERR", u, str(e)[:150])
    time.sleep(1)

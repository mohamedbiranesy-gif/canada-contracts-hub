import requests, time
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
urls = [
 "https://www.newswire.ca/news-releases/business-latest-news/",
 "https://www.globenewswire.com/search/keyword/awarded%20contract",
 "https://www.businesswire.com/newsroom",
 "https://www.prnewswire.com/news-releases/",
 "https://www.accesswire.com/newsroom",
 "https://www.newsfilecorp.com/",
 "https://www.defense.gov/News/Contracts/",
 "https://www.sedarplus.ca/",
 "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&State=A6&type=8-K&count=10&output=atom",
 "https://www.cae.com/news-events/press-releases/",
 "https://feeds.feedburner.com/",
]
for u in urls:
    try:
        r = requests.get(u, headers=UA, timeout=30, allow_redirects=True)
        print(r.status_code, len(r.content), u)
    except Exception as e:
        print("ERR", u, str(e)[:150])
    time.sleep(0.5)

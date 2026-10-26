import requests, time
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
urls = [
 "https://www.globenewswire.com/news-release/2025/04/07/3056644/0/en/telesat-secures-substantial-multi-year-contract-with-viasat-for-telesat-lightspeed-services.html",
 "https://www.globenewswire.com/en/search/keyword/awarded%20contract?pageSize=50",
 "https://www.globenewswire.com/RssFeed/orgclass/1/feedTitle/GlobeNewswire%20-%20News%20about%20Public%20Companies",
 "https://www.globenewswire.com/search/organization/Telesat",
 "https://www.businesswire.com/news/home/20250610925216/en/SEKO-Logistics-Taps-Kinaxis-to-Modernize-its-End-to-End-Supply-Chain",
 "https://www.war.gov/News/Contracts/",
 "https://www.defense.gov/News/Contracts/Contract/Article/3656651/",
 "https://www.telesat.com/press/press-releases/",
 "https://mda.space/news",
 "https://www.stantec.com/en/news",
 "https://www.aecon.com/press-room",
 "https://www.bird.ca/news/",
 "https://investors.herouxdevtek.com/news-releases",
 "https://www.ballard.com/about-ballard/newsroom/news-releases",
 "https://www.davie.ca/en/posts/",
 "https://www.seaspan.com/stories-press-releases/",
 "https://bombardier.com/en/media/news",
 "https://www.newsfilecorp.com/newsroom",
 "https://api.newsfilecorp.com/",
 "https://www.accesswire.com/newsroom/company/",
 "https://www.tmxmoney.com/en/index.html",
 "https://www.sedarplus.ca/csa-party/service/create.html",
]
for u in urls:
    try:
        r = requests.get(u, headers=UA, timeout=30, allow_redirects=True)
        print(r.status_code, len(r.content), u)
    except Exception as e:
        print("ERR", u, str(e)[:120])
    time.sleep(0.7)

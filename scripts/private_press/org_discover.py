import requests, re, time, json, sys
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language":"en-CA,en;q=0.9"}
names = [l.strip() for l in open(sys.argv[1]) if l.strip()]
out = open("downloads/private_press/org_slugs.jsonl","a")
for n in names:
    u = f"https://www.newswire.ca/search/organization/?keyword={requests.utils.quote(n)}&pagesize=25"
    try:
        r = requests.get(u, headers=UA, timeout=45)
        orgs = re.findall(r'href="(/news/[^"/]+/)"[^>]*>([^<]{2,80})<', r.text)
        orgs = list(dict.fromkeys(orgs))[:8]
        out.write(json.dumps({"name": n, "orgs": orgs}, ensure_ascii=False)+"\n"); out.flush()
        print(n, "->", orgs[:4], flush=True)
    except Exception as e:
        print(n, "ERR", str(e)[:60], flush=True)
    time.sleep(1.5)

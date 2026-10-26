"""Single-request existence check for company slugs not yet crawled; writes company_slugs_remaining_ok.txt"""
import requests, time, re, sys
src=open('scripts/private_press/crawl_search.py').read()
UA=eval(re.search(r'UA\s*=\s*(\{.*?\})', src, re.S).group(1))
slugs=[l.strip() for l in open('scripts/private_press/company_slugs.txt') if l.strip()]
done=set()
for l in open('downloads/private_press/crawl_search.log'):
    m=re.search(r'/news/([^/]+)/\?page=1', l)
    if m: done.add(m.group(1))
remaining=[s for s in slugs if s not in done]
out=open('scripts/private_press/precheck.out','w')
ok=[]
for s in remaining:
    try:
        r=requests.get(f"https://www.newswire.ca/news/{s}/?page=1&pagesize=100", headers=UA, timeout=20)
        code=r.status_code
    except Exception:
        code='ERR'
    out.write(f"{s} {code}\n"); out.flush()
    if code==200: ok.append(s)
    time.sleep(1.0)
open('scripts/private_press/company_slugs_remaining_ok.txt','w').write('\n'.join(ok)+'\n')
out.write(f"DONE ok={len(ok)} of {len(remaining)}\n")

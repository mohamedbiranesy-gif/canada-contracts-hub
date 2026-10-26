#!/usr/bin/env python3 -I
"""Probe a list of URLs (one per line in the file given as argv[1]); save bodies to argv[2]/<md5>.html
and print status, size, final URL, <title>, and a short text excerpt."""
import sys, os, re, hashlib, concurrent.futures, datetime, json
import requests

urls = [u.strip() for u in open(sys.argv[1]) if u.strip() and not u.startswith('#')]
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
H = {"User-Agent": "contracts-research/1.0 (Mozilla/5.0 compatible)"}

def fetch(u):
    t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    try:
        r = requests.get(u, headers=H, timeout=60, allow_redirects=True)
        body = r.content
        fn = os.path.join(out, hashlib.md5(u.encode()).hexdigest()[:10] + '.html')
        with open(fn, 'wb') as f:
            f.write(body)
        txt = r.text if 'html' in r.headers.get('content-type', '') or body[:30].lower().lstrip().startswith(b'<') else ''
        title = re.search(r'<title[^>]*>(.*?)</title>', txt, re.S | re.I)
        title = re.sub(r'\s+', ' ', title.group(1)).strip()[:120] if title else ''
        waf = r.headers.get('x-amzn-waf-action', '') or ('cf-mitigated' if 'cf-mitigated' in r.headers else '') or ('server=' + r.headers.get('server', ''))
        return {"url": u, "status": r.status_code, "bytes": len(body), "final": r.url, "title": title, "ctype": r.headers.get('content-type', ''), "waf": waf, "file": fn, "retrieved_at": t}
    except Exception as e:
        return {"url": u, "status": "ERR", "error": str(e)[:200], "retrieved_at": t}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    res = list(ex.map(fetch, urls))
with open(os.path.join(out, 'probe_results.json'), 'a') as f:
    for r in res:
        f.write(json.dumps(r) + '\n')
for r in res:
    print(r.get('status'), r.get('bytes', ''), r.get('waf', ''), r['url'], '->', r.get('final', '') if r.get('final') != r['url'] else '', '|', r.get('title', ''), r.get('error', ''))

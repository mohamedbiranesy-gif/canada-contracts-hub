"""Pick crawled sites (status ok) still lacking an AP mailbox, by priority, for the sitemap pass. usage: prep_deep.py <n> <out.json>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
n, outp = int(sys.argv[1]), sys.argv[2]
prio = {s['site'].rstrip('/'): s for s in json.load(open(WORK + '/sites_main.json'))}
done_deep = set()
for f in ('deep.jsonl', 'deep2.jsonl'):
    if os.path.exists(WORK + '/' + f):
        done_deep |= {json.loads(l)['site'] for l in open(WORK + '/' + f)}
cand = []
for l in open(WORK + '/crawl.jsonl'):
    r = json.loads(l)
    s = r['site'].rstrip('/')
    if r['status'] not in ('ok',) or s in done_deep:
        continue
    if any(e['class'] in ('ap',) for e in r.get('emails', [])):
        continue
    p = prio.get(s, {'prio': 0, 'buyer_keys': r.get('buyer_keys', [])})
    cand.append({'site': r.get('final_url') or r['site'], 'buyer_keys': p['buyer_keys'], 'prio': p['prio'], 'orig_site': r['site']})
cand.sort(key=lambda x: -x['prio'])
json.dump(cand[:n], open(outp, 'w'), indent=0)
print(len(cand), 'candidates; wrote', min(n, len(cand)))

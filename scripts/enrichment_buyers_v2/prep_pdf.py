"""Sites (crawl ok) still lacking an AP mailbox -> up to 3 supplier/finance pages each for the PDF pass. usage: prep_pdf.py <n> <out.json>"""
import sys, os, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
n, outp = int(sys.argv[1]), sys.argv[2]
prio = {s['site'].rstrip('/'): s for s in json.load(open(WORK + '/sites_main.json'))}
agg = {}
for f in sorted(glob.glob(WORK + '/crawl*.jsonl')) + sorted(glob.glob(WORK + '/deep*.jsonl')):
    for l in open(f):
        r = json.loads(l); k = r['site'].rstrip('/')
        a = agg.setdefault(k, {'site': r['site'], 'ap': False, 'pages': [], 'ok': False})
        a['ok'] |= r['status'] == 'ok'
        a['ap'] |= any(e['class'] == 'ap' for e in r.get('emails', []))
        for p in r.get('pages', []):
            t = norm(p['url'] + ' ' + p.get('title', ''))
            if re.search(r'(supplier|vendor|fournisseur|invoice|factur|payable|accounts payable|finance|doing business|purchasing|procurement|bids|tender)', t):
                a['pages'].append(p['url'])
done = {json.loads(l)['site'] for l in open(WORK + '/pdf.jsonl')} if os.path.exists(WORK + '/pdf.jsonl') else set()
out = []
for k, a in agg.items():
    if a['ap'] or not a['ok'] or not a['pages'] or a['site'] in done or k not in prio:
        continue
    pg = list(dict.fromkeys(a['pages']))
    pg.sort(key=lambda u: (not re.search(r'(invoice|payable|supplier|vendor)', u, re.I), len(u)))
    out.append({'site': a['site'], 'buyer_keys': prio[k]['buyer_keys'], 'pages': pg[:3], 'prio': prio[k]['prio']})
out.sort(key=lambda x: -x['prio'])
json.dump(out[:n], open(outp, 'w'), indent=0)
print(len(out), 'candidates; wrote', min(n, len(out)))

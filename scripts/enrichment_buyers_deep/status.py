"""top groups and whether the assembled output gives them an AP mailbox/portal now. usage: status.py [N] [offset]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
OFF = int(sys.argv[2]) if len(sys.argv) > 2 else 0
G = json.load(open(WORK + '/groups.json'))
out = {}
for l in open(OUT_ENRICHED):
    r = json.loads(l); out[r['buyer_key']] = r
for g in G[OFF:OFF + N]:
    ap = any((out.get(k) or {}).get('ap_contact', {}).get('emails') or (out.get(k) or {}).get('ap_contact', {}).get('invoice_portal') for k in g['keys'])
    w = next(((out.get(k) or {}).get('official_website') for k in g['keys'] if (out.get(k) or {}).get('official_website')), g['website'])
    print(g['rank'], g['records'], 'AP' if ap else '--', g['gid'][:48], '|', (w or '')[:45], '|', ','.join(g['site_status'])[:30])

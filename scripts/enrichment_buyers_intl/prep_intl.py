"""Build WORK/sites_intl.json for deep_intl.py: the own websites of in-scope groups (WORK/groups.json), largest groups first.
Skipped: shared government portals (gov.uk, europa.eu commission pages), organisations researched by hand (WHO, UNDP, FAO ...), third-party
e-procurement platforms recorded as 'websites' in the notices, and sites that answered with a block/challenge in an earlier pass."""
import sys, os, json, re, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

G = json.load(open(WORK + '/groups.json'))
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r
SKIP_HOST = re.compile(r'(^|\.)(gov\.uk|who\.int|undp\.org|fao\.org|commission\.europa\.eu|ec\.europa\.eu|deutsche-evergabe\.de|evergabe-online\.de|ethics\.dk|'
                       r'riik\.ee|ariba\.com|multiquote\.com|publicprocurement\.be|gencat\.cat|vhodne-uverejneni\.cz|vemap\.com|schramm-oehler\.at|rtx\.com|leidos\.com|'
                       r'coal\.gov\.uk|mercell|tendsign|doffin|tenderned)$', re.I)
sites = []
seen = set()
for g in G:
    if g['category'] == 'borrower_or_foreign_government':
        continue
    for w in g['websites']:
        u = w if w.startswith('http') else 'https://' + w
        sp = urllib.parse.urlsplit(u)
        host = sp.netloc.lower()
        if not host or SKIP_HOST.search(host):
            continue
        blocked = False
        for k in g['keys']:
            st = str(((prev.get(k) or {}).get('extras') or {}).get('website_check', {}).get('status', ''))
            if 'block' in st or 'challeng' in st:
                blocked = True
        if blocked:
            continue
        home = sp.scheme + '://' + sp.netloc + '/'
        seeds = [u] if sp.path not in ('', '/') else []
        key = host.replace('www.', '')
        if key in seen:
            for s in sites:
                if s['host'] == key:
                    s['buyer_keys'] = sorted(set(s['buyer_keys']) | set(g['keys']))
            continue
        seen.add(key)
        sites.append({'site': home, 'host': key, 'buyer_keys': g['keys'], 'gid': g['gid'], 'seeds': seeds, 'records': g['records']})
json.dump(sites, open(WORK + '/sites_intl.json', 'w'), indent=0)
print(len(sites), 'sites;', sum(1 for s in sites if s['records'] >= 2), 'with >=2 records')

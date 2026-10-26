"""Build the site list for deep2.py from WORK/groups.json: organisation websites (largest groups first), excluding shared government portals
(www.quebec.ca, www2.gov.bc.ca, saskatchewan.ca, novascotia.ca, canada.ca, gov.uk ...) and sites that answered with a block/challenge before."""
import sys, os, json, urllib.parse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
G = json.load(open(WORK + '/groups.json'))
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r
SHARED = {'www.quebec.ca', 'quebec.ca', 'www2.gov.bc.ca', 'www.saskatchewan.ca', 'novascotia.ca', 'www.novascotia.ca', 'www.canada.ca', 'canada.ca', 'www.gov.uk',
          'www.gov.mb.ca', 'gov.mb.ca', 'www.alberta.ca', 'www.ontario.ca', 'ontario.ca', 'www.gov.nl.ca', 'yukon.ca', 'www.mass.gov', 'vermont.gov', 'www.nyc.gov',
          'www.oregon.gov', 'www.who.int', 'www.undp.org', 'europa.eu', 'ec.europa.eu', 'www.worldbank.org', 'www.usa.gov', 'alaska.gov', 'www.virginia.gov'}
sites = collections.OrderedDict()
skipped = collections.Counter()
for g in G:
    if g['records'] < int(os.environ.get('MINREC', '15')):
        continue
    for k in g['keys']:
        p = prev.get(k) or {}
        w = (p.get('official_website') or '').strip()
        if not w:
            continue
        if not w.startswith('http'):
            w = 'https://' + w
        h = urllib.parse.urlsplit(w).netloc.lower()
        st = (p.get('extras') or {}).get('website_check', {}).get('status', '')
        if h in SHARED or h.endswith('.gc.ca') or 'gov.uk' in h:
            skipped['shared'] += 1; continue
        if st == 'blocked_or_challenged':
            skipped['blocked_before'] += 1; continue
        home = urllib.parse.urlsplit(w).scheme + '://' + h + '/'
        s = sites.setdefault(home, {'site': home, 'buyer_keys': [], 'gid': g['gid'], 'records': 0})
        s['buyer_keys'].append(k); s['records'] += 0
    for s in sites.values():
        pass
out = list(sites.values())
json.dump(out, open(WORK + '/sites_deep2.json', 'w'), indent=0)
print(len(out), dict(skipped))

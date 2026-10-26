"""Site list for deep3.py: own websites of the largest groups (records >= MINREC), seeds = supplier/finance/procurement pages seen by earlier passes
(v1/v2 crawl + deep, deep2 pages and sitemap candidates). Skips shared government portals, sites that answered with a block/challenge before
(any pass), and sites deep2 has not finished yet. usage: MINREC=80 python3 -I prep_deep3.py <out.json>"""
import sys, os, json, glob, re, urllib.parse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
outp = sys.argv[1]
G = json.load(open(WORK + '/groups.json'))
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r
SHARED = {'www.quebec.ca', 'quebec.ca', 'www2.gov.bc.ca', 'www.saskatchewan.ca', 'novascotia.ca', 'www.novascotia.ca', 'www.canada.ca', 'canada.ca', 'www.gov.uk',
          'www.gov.mb.ca', 'gov.mb.ca', 'www.alberta.ca', 'www.ontario.ca', 'ontario.ca', 'www.gov.nl.ca', 'yukon.ca', 'www.mass.gov', 'vermont.gov', 'www.nyc.gov',
          'www.oregon.gov', 'www.who.int', 'www.undp.org', 'europa.eu', 'ec.europa.eu', 'www.worldbank.org', 'www.usa.gov', 'alaska.gov', 'www.virginia.gov'}
KW = re.compile(r'(factur|invoice|payable|comptes|fournisseur|supplier|vendor|faire-affaire|faire-des-affaires|doing-business|approvisionnement|procurement|'
                r'purchasing|achats|depot-direct|direct-deposit|conditions|terms|finance|comptabilit|nous-joindre|contact)', re.I)
pages_by_host = collections.defaultdict(set)
blocked = set()
deep2_done = set()
files = sorted(glob.glob(OLD_WORK + '/crawl*.jsonl')) + sorted(glob.glob(OLD_WORK + '/deep*.jsonl')) + sorted(glob.glob(V2_WORK + '/crawl*.jsonl')) + \
    sorted(glob.glob(V2_WORK + '/deep*.jsonl')) + [WORK + '/deep2.jsonl']
for f in files:
    if not os.path.exists(f):
        continue
    for l in open(f):
        try:
            r = json.loads(l)
        except Exception:
            continue
        h = urllib.parse.urlsplit(r['site'] if r['site'].startswith('http') else 'https://' + r['site']).netloc.lower()
        if r.get('status') in ('blocked_or_challenged', 'partially_blocked'):
            blocked.add(h)
        if f.endswith('deep2.jsonl'):
            deep2_done.add(r['site'])
        for p in r.get('pages', []):
            if KW.search(urllib.parse.unquote(p.get('url', ''))):
                pages_by_host[h].add(p['url'])
        for u in r.get('candidates', []) or []:
            pages_by_host[h].add(u)
deep2_all = {s['site'] for s in json.load(open(WORK + '/sites_deep2.json'))}
sites = collections.OrderedDict()
sk = collections.Counter()
for g in G:
    if g['records'] < int(os.environ.get('MINREC', '80')):
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
            sk['shared'] += 1; continue
        if st in ('blocked_or_challenged',) or h in blocked:
            sk['blocked_before'] += 1; continue
        home = urllib.parse.urlsplit(w).scheme + '://' + h + '/'
        if home in deep2_all and home not in deep2_done:
            sk['deep2_pending'] += 1; continue
        s = sites.setdefault(home, {'site': home, 'buyer_keys': [], 'gid': g['gid'], 'records': g['records'], 'seeds': []})
        if k not in s['buyer_keys']:
            s['buyer_keys'].append(k)
for s in sites.values():
    h = urllib.parse.urlsplit(s['site']).netloc.lower()
    seeds = sorted(pages_by_host.get(h, ()), key=lambda u: (not re.search('factur|invoice|payable|comptes|fournisseur|supplier|vendor', u, re.I), len(u)))
    s['seeds'] = seeds[:25]
out = list(sites.values())
json.dump(out, open(outp, 'w'), indent=0)
print(len(out), 'sites', dict(sk))

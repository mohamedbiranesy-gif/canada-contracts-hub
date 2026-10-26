"""Group the deep-input buyer keys into organisations (canonical name from the previous enrichment, else normalized name; plus explicit
merge rules for historical/variant names) and rank by total record_count. Writes WORK/groups.json and WORK/worklist.tsv."""
import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

rows = load_buyers()
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r

# explicit merges for keys without canonical name (historical CSSS names, variants) -> canonical label of the organisation that now holds them
MERGE = [
    (r'\bcisss\b.*\blaurentides\b|\bcsss\b.*\blaurentides\b', 'Santé Québec – Laurentides'),
    (r'^csss de laval|centre de sante et de services sociaux de laval|^cisss de laval', 'Santé Québec – Laval'),
    (r'sud de lanaudiere|nord de lanaudiere|\bcisss\b.*lanaudiere', 'Santé Québec – Lanaudière'),
    (r'centre de sante et de services sociaux de trois rivieres|csss de trois rivieres', 'Santé Québec – Mauricie-et-Centre-du-Québec – Universitaire'),
    (r'champlain charles le moyne|haut richelieu rouville', 'Santé Québec – Montérégie-Centre'),
    (r'jardins roussillon|csss du suroit|vaudreuil soulanges', 'Santé Québec – Montérégie-Ouest'),
    (r'ouest de l ile \(?ciusss odim|centre de sante et de services sociaux de l ouest de l ile', 'Santé Québec – Ouest-de-l’Île-de-Montréal – Universitaire'),
    (r'centre hospitalier affilie universitaire de quebec', 'Santé Québec – CHU de Québec – Université Laval'),
    (r'institut universitaire en sante mentale de montreal', 'Santé Québec – Est-de-l’Île-de-Montréal – Universitaire'),
    (r'bas st laurent|bas saint laurent', 'Santé Québec – Bas-Saint-Laurent'),
    (r'sante et de services sociaux des iles', 'Santé Québec – Îles'),
]


def canon(r):
    k = r['buyer_key']
    p = prev.get(k) or {}
    cn = p.get('canonical_name') or (r.get('_known') or {}).get('canonical_name') or ''
    if cn:
        return cn, 'canonical_name'
    n = norm(r['name'])
    for rx, lab in MERGE:
        if re.search(rx, n):
            return lab, 'merge_rule'
    return r['name'].strip().rstrip('.').strip(), 'name'


G = collections.OrderedDict()
for r in rows:
    lab, basis = canon(r)
    gk = norm(lab)
    g = G.setdefault(gk, {'gid': re.sub(r'\s+', '_', gk)[:60], 'label': lab, 'keys': [], 'records': 0, 'names': [], 'websites': collections.Counter(),
                          'countries': collections.Counter(), 'sources': collections.Counter(), 'tasks': collections.Counter(), 'site_status': collections.Counter(), 'basis': set()})
    g['keys'].append(r['buyer_key']); g['records'] += r['record_count']; g['basis'].add(basis)
    if len(g['names']) < 6:
        g['names'].append(r['name'])
    p = prev.get(r['buyer_key']) or {}
    w = p.get('official_website') or (r.get('_known') or {}).get('official_website') or ''
    if w:
        g['websites'][w] += r['record_count']
    g['countries'][r['country']] += 1
    g['sources'][(r['sources'][0]['value'] if r['sources'] else '')] += r['record_count']
    g['tasks'][r['_task']] += 1
    g['site_status'][(p.get('extras') or {}).get('website_check', {}).get('status', 'none')] += 1
out = []
for gk, g in G.items():
    out.append({'gid': g['gid'], 'label': g['label'], 'records': g['records'], 'n_keys': len(g['keys']), 'keys': g['keys'], 'names': g['names'],
                'website': g['websites'].most_common(1)[0][0] if g['websites'] else '', 'country': g['countries'].most_common(1)[0][0],
                'source': g['sources'].most_common(1)[0][0], 'tasks': dict(g['tasks']), 'site_status': dict(g['site_status']), 'basis': sorted(g['basis'])})
# second step: union groups that share the same official website URL (exact URL incl. path; shared government portals excluded) or an explicit equivalence
SHARED_W = re.compile(r'^https?://(www\.)?(quebec\.ca|canada\.ca|www2\.gov\.bc\.ca|gov\.bc\.ca|saskatchewan\.ca|novascotia\.ca|gov\.mb\.ca|alberta\.ca|ontario\.ca|gov\.nl\.ca|yukon\.ca|gov\.uk|mass\.gov|nyc\.gov|oregon\.gov|who\.int|undp\.org|europa\.eu|worldbank\.org|usa\.gov|alaska\.gov|virginia\.gov|vermont\.gov|gov\.nt\.ca|gov\.pe\.ca|gnb\.ca|gov\.yk\.ca)(/|$)', re.I)
EQUIV = [(r'^newfoundland (and )?labrador hydro$|^nl hydro$', 'newfoundland and labrador hydro'),
         (r'^halifax transit halifax regional municipality$', 'halifax regional municipality')]
DESIG = {'city', 'county', 'town', 'village', 'township', 'ville', 'municipalite', 'paroisse', 'canton', 'mrc', 'cite'}
GEN = {'municipality', 'district', 'regional', 'region', 'the', 'of', 'de', 'du', 'des', 'la', 'le', 'and', 'et', 'inc', 'ltd', 'limited', 'corporation',
       'company', 'department', 'government', 'ministry', 'services', 'service', 'centre', 'center', 'board', 'school', 'university', 'college',
       'commonwealth', 'national', 'societe', 'office', 'authority', 'health'}
def compatible(a, b):
    ta, tb = set(norm(a).split()), set(norm(b).split())
    da, db = ta & DESIG, tb & DESIG
    if da and db and not (da & db):
        return False
    for w in ('village', 'town', 'city', 'township', 'ville', 'county'):
        if (w in ta) != (w in tb) and not (w == 'county' and 'municipality' in ta | tb):
            return False
    if norm(a) in norm(b) or norm(b) in norm(a):
        return True
    xa = {t for t in ta if len(t) >= 4 and t not in GEN and t not in DESIG}
    xb = {t for t in tb if len(t) >= 4 and t not in GEN and t not in DESIG}
    return bool(xa & xb)
parent = {i: i for i in range(len(out))}
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]; i = parent[i]
    return i
byw = {}
bylab = {norm(g['label']): i for i, g in enumerate(out)}
for i, g in enumerate(out):
    w = (g['website'] or '').strip().rstrip('/').lower().replace('http://', 'https://').replace('https://www.', 'https://')
    if w and not SHARED_W.search(w):
        if w in byw and compatible(out[byw[w]]['label'], g['label']):
            parent[find(i)] = find(byw[w])
        else:
            byw[w] = i
    for rx, target in EQUIV:
        if re.search(rx, norm(g['label'])) and target in bylab and bylab[target] != i:
            parent[find(i)] = find(bylab[target])
merged = collections.OrderedDict()
for i, g in enumerate(out):
    r = find(i)
    m = merged.setdefault(r, None)
    if m is None:
        merged[r] = dict(g, member_gids=[g['gid']], member_labels=[g['label']])
    else:
        big, small = (m, g) if m['records'] >= g['records'] else (g, m)
        nm = dict(big)
        nm['keys'] = big['keys'] + small['keys']; nm['records'] = m['records'] + g['records']; nm['n_keys'] = len(nm['keys'])
        nm['names'] = (big['names'] + small['names'])[:8]
        nm['member_gids'] = m['member_gids'] + [g['gid']]; nm['member_labels'] = m['member_labels'] + [g['label']]
        nm['website'] = big['website'] or small['website']
        merged[r] = nm
out = list(merged.values())
out.sort(key=lambda g: -g['records'])
for i, g in enumerate(out):
    g['rank'] = i
json.dump(out, open(WORK + '/groups.json', 'w'), ensure_ascii=False, indent=0)
with open(WORK + '/worklist.tsv', 'w') as f:
    cum = 0
    for g in out:
        cum += g['records']
        f.write('\t'.join(map(str, [g['rank'], g['records'], cum, g['n_keys'], g['label'], g['website'], g['country'], g['source'], ','.join(g['site_status']), ' || '.join(g['names'][:3])])) + '\n')
print(len(out), 'groups;', sum(g['records'] for g in out), 'records')

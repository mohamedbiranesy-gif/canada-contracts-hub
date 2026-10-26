"""Build WORK/groups.json for the international scope: one group per org_group of hub/claude_buyer_ap_scope.json
(gid = slug of the org_group label), with the union of its buyer keys, record counts, websites already known (_known / previous record)
and a coarse category used to pick research methods. Sorted by contract records (descending)."""
import sys, os, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

scope = json.load(open(SCOPE))
B = {b['buyer_key']: b for b in load_buyers()}
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l)
        if r['buyer_key'] in B:
            prev[r['buyer_key']] = r

IGO = re.compile(r'(united nations|^un |unops|undp|unicef|unesco|unhcr|unrwa|unido|unfpa|unitaid|world health|world meteorological|international (civil aviation|atomic|labour|telecommunication|fund for agric)|'
                 r'food and agriculture|world trade|world intellectual|preparatory commission|european (commission|investment bank|central bank|maritime|food safety|aviation|securities)|europol|'
                 r'joint undertaking|sesar|nato|caribbean development bank|niger basin|intergovernmental authority)', re.I)
WB_GOV = re.compile(r'^(the )?(republic|islamic republic|federal republic|federal democratic republic|kingdom|commonwealth|co operative republic|united republic|'
                    r'democratic republic|repubic|federated states|government of|federal government|independent state|state of)\b|^[a-z ]{3,40}$', re.I)
out = []
seen_gid = collections.Counter()
for g in scope:
    keys = g['buyer_keys']
    recs = sum(B[k]['record_count'] for k in keys)
    hm = sum(B[k]['record_count_high_or_medium'] for k in keys)
    sites = []
    for k in keys:
        w = (B[k].get('_known') or {}).get('official_website') or prev.get(k, {}).get('official_website') or ''
        if w and w not in sites:
            sites.append(w)
    srcs = collections.Counter(s['value'] for k in keys for s in B[k]['sources'])
    types = collections.Counter(t['value'] for k in keys for t in B[k]['types'])
    lab = g['org_group']
    gid = re.sub(r'[^a-z0-9]+', '_', norm(lab)).strip('_')[:70]
    seen_gid[gid] += 1
    if seen_gid[gid] > 1:
        gid += '_%d' % seen_gid[gid]
    tp = ' '.join(types)
    if IGO.search(lab) or 'IGO' in tp or 'international organization' in tp.lower():
        cat = 'igo'
    elif set(srcs) <= {'worldbank', 'other_igo', 'cdb', 'ccc_canada'} and (WB_GOV.search(lab) or 'ministry' in lab or 'government' in lab):
        cat = 'borrower_or_foreign_government'
    elif set(srcs) <= {'private_press', 'sec_edgar'}:
        cat = 'company_or_private_press'
    else:
        cat = 'public_body'
    out.append({'gid': gid, 'label': lab, 'country': g['country'], 'keys': keys, 'records': recs, 'records_hm': hm, 'websites': sites,
                'sources': dict(srcs), 'types': dict(types), 'category': cat,
                'names': list(dict.fromkeys(n for k in keys for n in B[k]['name_variants']))[:6]})
out.sort(key=lambda g: (-g['records'], g['gid']))
json.dump(out, open(WORK + '/groups.json', 'w'), ensure_ascii=False, indent=0)
print(len(out), 'groups', sum(len(g['keys']) for g in out), 'keys')
print(collections.Counter(g['category'] for g in out))
print('records by category', {c: sum(g['records'] for g in out if g['category'] == c) for c in set(g['category'] for g in out)})

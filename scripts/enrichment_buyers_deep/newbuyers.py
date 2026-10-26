"""Full enrichment base for the 104 `full_enrichment_new_buyer` keys -> WORK/new_buyers.json
1) same organisation already enriched under another key (buyers_enriched.jsonl / buyers_enriched_v2.jsonl): normalized-name equality
   (legal suffixes, 'the corporation of', parenthesised acronyms, '&'/'and' removed) -> copy website, identifiers, address, AP / procurement /
   general contacts with their evidence, parent organisation; basis recorded;
2) CRA registered-charity list (downloads/cra_charities/ident_2024.csv + weburl_2024.csv, T3010 open data 2024, fetched by the vendor worker
   2026-10-26T02:46Z): exact normalized legal/operating name, province must agree with the notice location when one is published -> BN (RR
   program account), registered address, website as filed (website asserted only after this pass fetched it, see assemble_deep.py);
3) website candidates (well-known official domains) -> crawled by deep3.py (sites_deep3c.json) and asserted by assemble_deep.py only when
   the homepage loads and its title/domain matches."""
import sys, os, json, re, csv, collections, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

rows = [r for r in load_buyers() if r['_task'] == 'full_enrichment_new_buyer']
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r
SUFFIX = re.compile(r'\b(inc|ltd|limited|corp|corporation|incorporated|llc|lp|ltee|the)\b')


def nm(s):
    s = re.sub(r'\([^)]*\)', ' ', s or '')
    s = norm(s.replace('&', ' and '))
    s = re.sub(r'^the corporation of (the )?', '', s)
    s = SUFFIX.sub(' ', s)
    return re.sub(r'\s+', ' ', s).strip()


idx = collections.defaultdict(list)
for k, r in prev.items():
    if (r.get('extras') or {}).get('jurisdiction_candidates'):
        continue
    for n in {nm(r.get('name')), nm(r.get('canonical_name'))}:
        if n:
            idx[n].append(k)
    n2 = nm(r.get('name')).replace(' and ', ' ')
    if n2:
        idx[n2].append(k)


def score(k):
    r = prev[k]
    return (bool(r['ap_contact']['emails']) or bool(r['ap_contact']['invoice_portal'])) * 4 + bool(r.get('official_website')) * 2 + bool(r['procurement_contact']['emails'])


# CRA charities
CH = collections.defaultdict(list)
web = {}
try:
    for row in csv.DictReader(open(BASE + '/downloads/cra_charities/weburl_2024.csv', encoding='utf-8', errors='replace')):
        web.setdefault(row['BN/NE'], row['Contact URL'])
    for row in csv.DictReader(open(BASE + '/downloads/cra_charities/ident_2024.csv', encoding='utf-8', errors='replace')):
        for n in {nm(row['Legal Name']), nm(row['Account Name'])}:
            if n:
                CH[n].append(row)
except Exception as e:
    print('charities not loaded', e)
PROV = {'ON': 'ON', 'MB': 'MB', 'NL': 'NL', 'SK': 'SK', 'AB': 'AB', 'BC': 'BC', 'NS': 'NS', 'NB': 'NB', 'QC': 'QC', 'PE': 'PE', 'NT': 'NT', 'YT': 'YT', 'NU': 'NU'}
REGION_PROV = {'Ontario': 'ON', 'Manitoba': 'MB', 'Saskatchewan': 'SK'}

out = {}
stats = collections.Counter()
for b in rows:
    k = b['buyer_key']
    n = nm(b['name'])
    loc = ' '.join(a['value'].get('location_as_published', '') for a in b['addresses'])
    prov = ''
    m = re.search(r',\s*([A-Z]{2}),\s*CAN', loc)
    if m:
        prov = m.group(1)
    else:
        for w, p in REGION_PROV.items():
            if w in loc:
                prov = p
    e = {'notes': [], 'extras': {}}
    cands = [c for c in dict.fromkeys(idx.get(n, []) + idx.get(n.replace(' and ', ' '), [])) if c != k]
    if cands:
        best = sorted(cands, key=lambda c: -score(c))[0]
        r = prev[best]
        for f in ('official_website', 'canonical_name', 'organisation_type', 'address', 'ap_contact', 'procurement_contact', 'general_contact'):
            if r.get(f):
                e[f] = copy.deepcopy(r[f])
        e['identifiers'] = {kk: vv for kk, vv in (r.get('identifiers') or {}).items() if kk != 'from_dataset'}
        for kk in ('parent_organisation', 'website_check', 'finance_role_mailboxes', 'targeted_sources', 'directory_sources'):
            if (r.get('extras') or {}).get(kk):
                e['extras'][kk] = copy.deepcopy(r['extras'][kk])
        e['extras']['same_organisation_as'] = {'buyer_key': best, 'name': r['name'], 'basis': 'normalized name equality ("%s")' % n,
                                               'source_file': 'buyers_enriched.jsonl / buyers_enriched_v2.jsonl', 'match_confidence': 'strong'}
        e['notes'].append('facts copied from the existing record of the same organisation (%s, "%s")' % (best, r['name']))
        stats['same_org'] += 1
    # charities
    ch = [c for c in CH.get(n, []) if (not prov or c['Province'] == prov) and (nm(c['Account Name']) == n or nm(c['Account Name']) == nm(c['Legal Name']))]
    if len(ch) == 1:
        c = ch[0]
        e.setdefault('identifiers', {})['cra_charity_bn'] = c['BN']
        e['identifiers']['business_number_bn9'] = c['BN'][:9]
        e['extras']['cra_charity'] = {'bn': c['BN'], 'legal_name': c['Legal Name'], 'account_name': c['Account Name'], 'category': c['Category'],
                                      'designation': c['Designation'], 'address': ' '.join(x for x in (c['Address Line 1'], c['Address Line 2']) if x),
                                      'city': c['City'], 'province': c['Province'], 'postal_code': c['Postal Code'], 'website_as_filed': web.get(c['BN'], ''),
                                      'source': 'CRA list of registered charities (T3010 open data, 2024) downloads/cra_charities/ident_2024.csv',
                                      'match_basis': 'exact normalized name "%s"%s' % (n, (' + province ' + prov) if prov else ''), 'match_confidence': 'exact' if prov else 'strong'}
        if not (e.get('address') or {}).get('line1'):
            e['address'] = {'line1': ' '.join(x for x in (c['Address Line 1'], c['Address Line 2']) if x).title(), 'city': c['City'].title(), 'region': c['Province'],
                            'postal_code': c['Postal Code'], 'country': 'CA', 'source': 'CRA registered charity record (BN %s)' % c['BN']}
        stats['charity'] += 1
    elif len(ch) > 1:
        e['notes'].append('CRA charities: %d registrations share the name (not resolved)' % len(ch))
    out[k] = e
json.dump(out, open(WORK + '/new_buyers.json', 'w'), ensure_ascii=False, indent=0)
print(len(out), dict(stats))
for k, e in out.items():
    b = next(x for x in rows if x['buyer_key'] == k)
    print(b['record_count'], b['name'][:50], '|', (e.get('extras', {}).get('same_organisation_as') or {}).get('name', '')[:40], '|', e.get('identifiers', {}).get('cra_charity_bn', ''), '|', e.get('official_website', ''))

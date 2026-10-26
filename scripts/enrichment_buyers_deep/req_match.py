"""Match Quebec buyers to the Registraire des entreprises du Québec bulk file (downloads/quebec_req/JeuDonnees.zip, fetched 18:56 UTC by the
vendor worker) by exact normalized name -> NEQ, legal form, status, address. Output WORK/req_matches.json. Reads the zip in place (no extraction)."""
import sys, os, json, re, zipfile, io, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
csv.field_size_limit(10**8)
ZIP = BASE + '/downloads/quebec_req/JeuDonnees.zip'
buyers = load_buyers()
bulk = json.load(open(WORK + '/bulk.json'))
targets = collections.defaultdict(set)


def n2(s):
    s = re.sub(r'\(.*?\)', ' ', s or '')
    s = s.split(' - ')[0].split(' / ')[0]
    return norm(s.rstrip(' .'))


for b in buyers:
    if b['country'] != 'CA':
        continue
    srcs = {s['value'] for s in b['sources']}
    r = bulk.get(b['buyer_key'], {})
    if 'seao_quebec' not in srcs and not str(r.get('organisation_type', '')).startswith('Quebec'):
        continue
    for c in {n2(b['name']), n2(r.get('canonical_name', ''))}:
        if c and len(c) > 5:
            targets[c].add(b['buyer_key'])
print('targets', len(targets), flush=True)
z = zipfile.ZipFile(ZIP)
hits = collections.defaultdict(set)
f = io.TextIOWrapper(z.open('Nom.csv'), encoding='utf-8-sig', errors='replace')
for row in csv.DictReader(f):
    if row.get('DAT_FIN_NOM_ASSUJ'):
        continue
    for k in (norm(row['NOM_ASSUJ']), norm(row.get('NOM_ASSUJ_LANG_ETRNG') or '')):
        if k and k in targets:
            hits[k].add(row['NEQ'])
print('name hits', len(hits), flush=True)
neqs = set().union(*hits.values()) if hits else set()
ent = {}
f = io.TextIOWrapper(z.open('Entreprise.csv'), encoding='utf-8-sig', errors='replace')
rd = csv.reader(f)
hdr = next(rd)
for row in rd:
    if row and row[0] in neqs:
        ent[row[0]] = dict(zip(hdr, row))
dom = {}
f = io.TextIOWrapper(z.open('DomaineValeur.csv'), encoding='utf-8-sig', errors='replace')
for row in csv.DictReader(f):
    dom[(row['TYP_DOM_VAL'], row['COD_DOM_VAL'])] = row['VAL_DOM_FRAN']
out = {}
for k, ns in hits.items():
    recs = []
    for n in sorted(ns):
        e = ent.get(n, {})
        recs.append({'neq': n, 'legal_form': '%s (%s)' % (e.get('COD_FORME_JURI', ''), dom.get(('FORM_JURI', e.get('COD_FORME_JURI', '')), '')),
                     'status': dom.get(('STAT_IMMAT', e.get('COD_STAT_IMMAT', '')), e.get('COD_STAT_IMMAT', '')),
                     'registration_date': e.get('DAT_IMMAT', ''), 'legal_regime': dom.get(('REGIM_JURI', e.get('COD_REGIM_JURI', '')), e.get('COD_REGIM_JURI', '')),
                     'constituted': e.get('DAT_CONSTI', ''),
                     'address': ', '.join(x for x in [e.get(c, '') for c in hdr[-4:]] if x)})
    for bk in targets[k]:
        out.setdefault(bk, {'name_matched': k, 'records': recs, 'match_confidence': 'exact' if len(recs) == 1 else 'weak'})
json.dump({'source': 'Registraire des entreprises du Québec bulk extract JeuDonnees.zip (downloads/quebec_req/, fetched 2026-10-25T18:56Z by the vendor worker)',
           'matches': out}, open(WORK + '/req_matches.json', 'w'), ensure_ascii=False)
print('buyers matched', len(out))

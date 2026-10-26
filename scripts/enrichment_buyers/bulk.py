"""Stage 1: match buyers to bulk directories. Output WORK/bulk.json {buyer_key: partial record}."""
import csv, json, re, sys, collections, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

buyers = load_buyers()
out = {}
MT = {  # file mtimes as retrieval times of directory files
}


def mtime(p):
    import datetime
    return datetime.datetime.utcfromtimestamp(os.path.getmtime(p)).replace(microsecond=0).isoformat() + 'Z'


def rec(b):
    k = b['buyer_key']
    if k not in out:
        out[k] = {'identifiers': {}, 'address': {}, 'general_contact': {'emails': [], 'phone': ''},
                  'official_website': '', 'canonical_name': '', 'organisation_type': '', 'sources': [], 'notes': []}
    return out[k]


def url(w):
    w = (w or '').strip()
    if not w:
        return ''
    if not w.startswith('http'):
        w = 'https://' + w
    return w

# ---------------- Quebec municipal directory (MAMH) ----------------
mun_p = DL + '/mamh/MUN.csv'
MUN = list(csv.DictReader(open(mun_p, encoding='utf-8-sig')))
MRC = list(csv.DictReader(open(DL + '/mamh/MRC_CM_Arg.csv', encoding='utf-8-sig')))
ARR = list(csv.DictReader(open(DL + '/mamh/ARR.csv', encoding='utf-8-sig')))
mun_by = collections.defaultdict(list)
for m in MUN:
    mun_by[norm(m['munnom'])].append(m)
mrc_by = collections.defaultdict(list)
for m in MRC:
    mrc_by[norm(m['mrcnom'])].append(m)
def strip_art(x):
    return re.sub(r'^(?:la|le|les|l|de la|de l|des|du|de|d)\s+', '', x)
mun_by2 = collections.defaultdict(list)
for m in MUN:
    mun_by2[strip_art(norm(m['munnom']))].append(m)
mrc_by2 = collections.defaultdict(list)
for m in MRC:
    mrc_by2[strip_art(norm(m['mrcnom']))].append(m)
arr_by = collections.defaultdict(list)
for a in ARR:
    arr_by[norm(a['arrnom'])].append(a)

PFX = [('municipalite regionale de comte', 'MRC'), ('mrc', 'MRC'),
       ('municipalite du canton', 'Canton'), ('canton', 'Canton'), ('cantons unis', 'Cantons unis'),
       ('municipalite de la paroisse', 'Paroisse'), ('paroisse', 'Paroisse'),
       ('municipalite du village', 'Village'), ('village', 'Village'),
       ('municipalite', 'Municipalité'), ('ville', 'Ville'), ('city', 'Ville'), ('town', 'Ville'), ('township', 'Canton'),
       ('cite', 'Ville')]
ART = r'(?:de la|de l|des|du|de|d|of the|of|la|le|les|l)'


def parse_muni(name):
    n = name.split(' - ')[0].split(' – ')[0]
    n = re.sub(r'\(.*?\)', ' ', n)
    nn = norm(n)
    for p, des in PFX:
        m = re.match(r'^%s\s+(?:%s\s+)?(.*)$' % (p, ART), nn)
        if m and m.group(1):
            return des, m.group(1).strip(), (des in ('Municipalité',) and False)
    return None, nn, False


def put_mun(r, m, basis, conf):
    r['canonical_name'] = r['canonical_name'] or ('%s de %s' % (m['mdes'], m['munnom']))
    r['organisation_type'] = r['organisation_type'] or 'Quebec local municipality (%s)' % m['mdes']
    r['identifiers']['mamh_municipal_code'] = m['mcode']
    r['identifiers']['quebec_admin_region'] = m['regadm']
    r['identifiers']['mrc'] = m.get('mrc', '')
    r['address'] = {'line1': m['madr1'], 'city': m['madr2'], 'region': 'QC', 'postal_code': m['mcodpos'], 'country': 'CA'}
    if m['mweb']:
        r['official_website'] = url(m['mweb'])
    if m['mcourriel']:
        r['general_contact']['emails'] = [m['mcourriel'].strip()]
    r['general_contact']['phone'] = m['mtel']
    r['extras_mamh'] = {'fax': m['mfax'], 'population': m['mpopul']}
    r['sources'].append({'source': 'MAMH Répertoire des municipalités MUN.csv', 'url': 'https://donneesouvertes.affmunqc.net/repertoire/MUN.csv',
                         'retrieved_at': mtime(mun_p), 'match_basis': basis, 'match_confidence': conf})


def put_mrc(r, m, basis, conf):
    r['canonical_name'] = r['canonical_name'] or m['mrcdescdesi'].strip() + ' ' + m['mrcnom']
    r['organisation_type'] = r['organisation_type'] or m['mrcdescdesi'].strip()
    r['identifiers']['mamh_mrc_code'] = m['mrccod']
    r['address'] = {'line1': m['mrcadr1'], 'city': m['mrcadr2'], 'region': 'QC', 'postal_code': m['mrccodp'], 'country': 'CA'}
    if m['mrcweb']:
        r['official_website'] = url(m['mrcweb'])
    if m['mrccourriel']:
        r['general_contact']['emails'] = [m['mrccourriel'].strip()]
    r['general_contact']['phone'] = m['mrctel']
    r['sources'].append({'source': 'MAMH Répertoire MRC_CM_Arg.csv', 'url': 'https://donneesouvertes.affmunqc.net/repertoire/MRC_CM_Arg.csv',
                         'retrieved_at': mtime(DL + '/mamh/MRC_CM_Arg.csv'), 'match_basis': basis, 'match_confidence': conf})


QC_MUNI_TYPES = {'municipality', 'city', 'regional county municipality (MRC)', ''}
stats = collections.Counter()
for b in buyers:
    if b['country'] != 'CA':
        continue
    t = b['types'][0]['value'] if b['types'] else ''
    srcs = {s['value'] for s in b['sources']}
    if 'seao_quebec' not in srcs and t not in ('municipality', 'city'):
        continue
    des, core, _ = parse_muni(b['name'])
    if des is None:
        continue
    if des == 'MRC':
        c = mrc_by.get(core, []) or mrc_by2.get(strip_art(core), [])
        c = [m for m in c if 'comt' in norm(m['mrcdescdesi']) or m['mrccod'].startswith('MR') or True]
        if len(c) == 1:
            put_mrc(rec(b), c[0], 'normalized name "%s" == MRC name' % core, 'exact'); stats['mrc'] += 1
        elif len(c) > 1:
            cc = [m for m in c if 'comt' in norm(m['mrcdescdesi'])]
            if len(cc) == 1:
                put_mrc(rec(b), cc[0], 'name == MRC name (designation MRC)', 'exact'); stats['mrc'] += 1
        continue
    c = mun_by.get(core, [])
    if not c:
        # try with "saint" <-> "st"
        core2 = re.sub(r'\bst\b', 'saint', re.sub(r'\bste\b', 'sainte', core))
        c = mun_by.get(core2, [])
    if not c:
        c = mun_by2.get(strip_art(core), [])
    if len(c) == 1:
        m = c[0]
        conf = 'exact' if (des == m['mdes'] or (des == 'Ville' and m['mdes'] == 'Ville')) else 'strong'
        put_mun(rec(b), m, 'normalized name "%s" == munnom; buyer designation %s, directory designation %s' % (core, des, m['mdes']), conf)
        stats['mun_' + conf] += 1
    elif len(c) > 1:
        cc = [m for m in c if m['mdes'] == des]
        if len(cc) == 1:
            put_mun(rec(b), cc[0], 'name "%s" + designation %s disambiguated among %d homonyms' % (core, des, len(c)), 'strong')
            stats['mun_disamb'] += 1
        else:
            r = rec(b); r['notes'].append('MAMH: %d municipalities named "%s" (%s); not resolved' % (len(c), core, ', '.join(m['mcode'] + ' ' + m['mdes'] for m in c)))
            stats['mun_ambig'] += 1
    else:
        stats['mun_none'] += 1

# ---------------- Quebec school service centres ----------------
css = json.load(open(DL + '/qc/meq_css_directory.json'))
css_by = {}
for c in css:
    css_by[norm(re.sub(r'^Centre de services scolaires? ', '', c['name']).replace('Commission scolaire ', ''))] = c


def css_core(n):
    n = n.split(' / ')[0].split(' - ')[0]
    n = re.sub(r'\(.*?\)', ' ', n)
    nn = norm(n)
    m = re.match(r'^(?:centre de services scolaires?|commission scolaire|school board|css)\s+(.*)$', nn)
    return m.group(1).strip() if m else None


for b in buyers:
    if b['country'] != 'CA':
        continue
    core = css_core(b['name'])
    if not core:
        continue
    hit = css_by.get(core)
    if not hit:
        for k, v in css_by.items():
            kk = re.sub(r'^(?:de la|de l|des|du|de|d)\s+', '', k)
            cc = re.sub(r'^(?:de la|de l|des|du|de|d)\s+', '', core)
            if kk == cc:
                hit = v; break
    if hit:
        r = rec(b)
        r['canonical_name'] = hit['name']; r['organisation_type'] = 'Quebec school service centre / school board'
        r['official_website'] = r['official_website'] or hit['website']
        r['general_contact']['phone'] = r['general_contact']['phone'] or hit.get('phone', '')
        r['sources'].append({'source': 'MEQ coordonnées des centres de services scolaires (meq_css_coord.html)', 'url': hit.get('page_url'),
                             'retrieved_at': mtime(DL + '/qc/meq_css_directory.json'), 'match_basis': 'normalized CSS name == "%s"' % core, 'match_confidence': 'exact'})
        stats['css'] += 1

# ---------------- Quebec health establishments ----------------
sq = json.load(open(DL + '/qc/sante_quebec_etablissements.json'))


def hcore(n):
    nn = norm(n)
    nn = re.sub(r'^(?:sante quebec)\s*', '', nn)
    nn = re.sub(r'^(?:centre integre(?: universitaire)? de sante et de services sociaux|ciusss|cisss)\s+(?:(?:de la|de l|des|du|de|d)\s+)?', '', nn)
    nn = nn.replace(' et du ', ' et ').replace(' st ', ' saint ')
    nn = re.sub(r'\b(?:universitaire|ciusss|cisss|[a-z]{2,4})$', lambda m: '' if m.group(0) in ('universitaire', 'ciusss', 'cisss', 'mcq', 'cn') else m.group(0), nn).strip()
    nn = re.sub(r'\buniversitaire\b', '', nn)
    return re.sub(r'\s+', ' ', nn).strip()


sq_by = {}
for e in sq:
    sq_by[hcore(e['region_title'])] = e
for b in buyers:
    if b['country'] != 'CA':
        continue
    nn = norm(b['name'])
    if not any(w in nn for w in ('sante quebec', 'cisss', 'ciusss', 'centre integre', 'chu ', 'centre hospitalier', 'institut', 'centre universitaire de sante')):
        continue
    core = hcore(b['name'])
    hit = sq_by.get(core)
    if not hit:
        for k, v in sq_by.items():
            if k and (core == k or (len(k) > 8 and core.startswith(k)) or (len(core) > 8 and k.startswith(core))):
                hit = v; break
    if hit:
        r = rec(b)
        r['canonical_name'] = r['canonical_name'] or 'Santé Québec – ' + hit['region_title'].replace('​', '').replace('\xa0', ' ')
        r['organisation_type'] = 'Quebec health and social services establishment (Santé Québec)'
        r['official_website'] = r['official_website'] or hit.get('website', '')
        a = hit.get('address', '')
        parts = [p.strip() for p in a.split(',')]
        if len(parts) >= 5:
            r['address'] = {'line1': parts[0], 'city': parts[1], 'region': 'QC', 'postal_code': parts[3], 'country': 'CA'}
        r['general_contact']['phone'] = hit.get('phone', '')
        r['sources'].append({'source': 'Santé Québec - trouver un établissement', 'url': 'https://www.santequebec.ca/trouver-un-etablissement',
                             'retrieved_at': mtime(DL + '/qc/sante_quebec_etablissements.json'), 'match_basis': 'health region core "%s"' % core, 'match_confidence': 'strong'})
        stats['health'] += 1

# ---------------- Government of Canada ----------------
gc = json.load(open(DL + '/gc/organization_list.json'))['result']
gc_by = {o['name']: o for o in gc}
links = json.load(open(DL + '/gc/dept_links.json'))
link_by = {}
for t, u in links:
    link_by[norm(t)] = u
gc_title = {}
for o in gc:
    for lang in ('en', 'fr'):
        t = (o.get('title_translated') or {}).get(lang)
        if t:
            gc_title[norm(t)] = o


def gc_site(o):
    en = norm(o['title_translated']['en'])
    if en in link_by:
        return link_by[en]
    for k, u in link_by.items():
        if len(k) > 10 and (k in en or en in k):
            return u
    return ''


for b in buyers:
    if b['country'] != 'CA':
        continue
    oo = b['identifiers'].get('owner_org', [])
    o = None; basis = ''
    if oo:
        o = gc_by.get(oo[0]['value']); basis = 'owner_org code %s' % oo[0]['value']
    else:
        srcs = {s['value'] for s in b['sources']}
        if 'canada_federal' in srcs:
            n = norm(re.sub(r'\(.*?\)', '', b['name']))
            o = gc_title.get(n)
            if not o:
                n2 = re.sub(r'^(?:department of|ministere de la|ministere des|ministere de l|ministere du)\s+', '', n)
                o = gc_title.get(n2)
            basis = 'name == GC registry title'
    if not o:
        continue
    r = rec(b)
    r['canonical_name'] = o['title_translated']['en'].strip()
    r['organisation_type'] = r['organisation_type'] or 'Government of Canada organization (FAA schedule %s)' % o.get('faa_schedule', '')
    r['identifiers']['owner_org'] = o['name']
    r['identifiers']['gc_org_title'] = o['title']
    if o.get('department_number'):
        r['identifiers']['department_number'] = o['department_number']
    if o.get('faa_schedule'):
        r['identifiers']['faa_schedule'] = o['faa_schedule']
    s = gc_site(o)
    if s:
        r['official_website'] = s
    r['sources'].append({'source': 'open.canada.ca organization_list (CKAN)', 'url': 'https://open.canada.ca/data/api/3/action/organization_list?all_fields=true',
                         'retrieved_at': mtime(DL + '/gc/organization_list.json'), 'match_basis': basis, 'match_confidence': 'exact' if oo else 'strong'})
    if s:
        r['sources'].append({'source': 'canada.ca departments and agencies list', 'url': 'https://www.canada.ca/en/government/dept.html',
                             'retrieved_at': mtime(DL + '/gc/dept.html'), 'match_basis': 'English title match', 'match_confidence': 'strong'})
    stats['gc'] += 1

# ---------------- UK gov.uk organisations ----------------
uk = json.load(open(DL + '/uk/govuk_organisations.json'))
uk_by = collections.defaultdict(list)
for o in uk:
    uk_by[norm(o['title'])].append(o)
for b in buyers:
    if b['country'] != 'GB':
        continue
    n = norm(b['name'].replace('Foreign Commonwealth', 'Foreign, Commonwealth'))
    c = [o for o in uk_by.get(n, []) if o['details'].get('govuk_status') == 'live'] or uk_by.get(n, [])
    if len(c) >= 1:
        o = c[0]; r = rec(b)
        r['canonical_name'] = o['title']; r['organisation_type'] = 'UK public body (%s)' % o.get('format')
        r['official_website'] = o['web_url'] if o['details'].get('govuk_status') == 'live' else (o['details'].get('url') or o['web_url'])
        r['identifiers']['govuk_slug'] = o['details']['slug']
        r['sources'].append({'source': 'GOV.UK organisations API', 'url': 'https://www.gov.uk/api/organisations', 'retrieved_at': mtime(DL + '/uk/govuk_organisations.json'),
                             'match_basis': 'normalized title equality', 'match_confidence': 'exact'})
        stats['uk'] += 1

# carry input addresses/identifiers when directory missing
for b in buyers:
    r = out.get(b['buyer_key'])
    if r is None:
        continue
json.dump(out, open(WORK + '/bulk.json', 'w'), ensure_ascii=False, indent=0)
print(stats, len(out))

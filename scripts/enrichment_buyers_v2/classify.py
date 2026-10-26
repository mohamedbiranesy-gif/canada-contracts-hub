"""Stage 0 (v2): classify each new buyer: jurisdiction (province/state), parent organisation for divisions and provincial/state
government units, municipal designation + core name, and candidate labels for directory lookups.
Output: WORK/classify.json {buyer_key: {...}}"""
import sys, os, json, re, collections, gzip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

SRC_PROV = {'ca_alberta_apc': 'AB', 'ca_alberta_sole_source': 'AB', 'ca_city_edmonton': 'AB', 'ca_bc_ministry_awards': 'BC',
            'ca_nova_scotia': 'NS', 'ca_saskatchewan': 'SK', 'ca_newfoundland': 'NL', 'ca_nwt': 'NT', 'ca_city_toronto': 'ON',
            'ca_city_ottawa': 'ON', 'ca_ontario_vor': 'ON',
            'us_state_virginia': 'VA', 'us_state_texas_lbb': 'TX', 'us_state_texas_dir': 'TX', 'us_state_massachusetts': 'MA',
            'us_state_ny_abo': 'NY', 'us_ny_mta': 'NY', 'us_state_vermont': 'VT', 'us_state_alaska': 'AK', 'us_state_oregon': 'OR',
            'us_county_montgomery_md': 'MD', 'us_county_montgomery_md_spending': 'MD', 'us_county_miami_dade': 'FL', 'us_city_mesa_az': 'AZ',
            'us_county_fulton_ga': 'GA', 'us_city_la': 'CA', 'us_city_mesquite_tx': 'TX', 'us_city_baton_rouge': 'LA', 'us_city_corona_ca': 'CA',
            'us_city_indio_ca': 'CA', 'us_city_richmond_ca': 'CA', 'us_city_nyc': 'NY', 'us_city_providence': 'RI', 'us_state_oklahoma': 'OK',
            'us_state_delaware': 'DE', 'us_city_austin': 'TX'}
# provincial/territorial government sources whose "department-like" buyers are units of that government
GOV_SRC = {'ca_alberta_apc': 'AB', 'ca_alberta_sole_source': 'AB', 'ca_bc_ministry_awards': 'BC', 'ca_nova_scotia': 'NS',
           'ca_saskatchewan': 'SK', 'ca_newfoundland': 'NL', 'ca_nwt': 'NT'}
GOV_NAME = {'AB': 'Government of Alberta', 'BC': 'Government of British Columbia', 'NS': 'Government of Nova Scotia',
            'SK': 'Government of Saskatchewan', 'NL': 'Government of Newfoundland and Labrador', 'NT': 'Government of the Northwest Territories',
            'ON': 'Government of Ontario', 'YT': 'Government of Yukon', 'MB': 'Government of Manitoba'}
REG = {'ab': 'AB', 'alberta': 'AB', 'ca ab': 'AB', 'on': 'ON', 'ontario': 'ON', 'ca on': 'ON', 'bc': 'BC', 'british columbia': 'BC',
       'ns': 'NS', 'nova scotia': 'NS', 'sk': 'SK', 'saskatchewan': 'SK', 'nl': 'NL', 'mb': 'MB', 'manitoba': 'MB', 'nb': 'NB',
       'nt': 'NT', 'yt': 'YT', 'pe': 'PE', 'qc': 'QC', 'va': 'VA', 'ny': 'NY', 'tx': 'TX'}
TZ_PROV = {'America/Denver': {'AB'}, 'America/Edmonton': {'AB'}, 'America/Toronto': {'ON'}, 'America/New_York': {'ON'},
           'America/Los_Angeles': {'BC'}, 'America/Vancouver': {'BC'}, 'America/Halifax': {'NS', 'NB', 'PE'}, 'America/Moncton': {'NB'},
           'America/Regina': {'SK'}, 'America/St_Johns': {'NL'}, 'America/Winnipeg': {'MB'}, 'America/Chicago': {'MB'},
           'America/Whitehorse': {'YT'}, 'America/Yellowknife': {'NT'}}

PARENTS = [  # (regex on name, parent canonical name, parent key, jurisdiction)
    (r'^city of toronto\b', 'City of Toronto', 'city_of_toronto', 'ON'),
    (r'^city of ottawa\b', 'City of Ottawa', 'city_of_ottawa', 'ON'),
    (r'^commonwealth of massachusetts\b', 'Commonwealth of Massachusetts', 'state_ma', 'MA'),
    (r'^state of vermont\b', 'State of Vermont', 'state_vt', 'VT'),
    (r'^state of alaska\b', 'State of Alaska', 'state_ak', 'AK'),
    (r'^state of oklahoma\b', 'State of Oklahoma', 'state_ok', 'OK'),
    (r'^state of delaware\b', 'State of Delaware', 'state_de', 'DE'),
    (r'^montgomery county (md|maryland)\b', 'Montgomery County, Maryland', 'montgomery_md', 'MD'),
    (r'^miami dade county\b', 'Miami-Dade County', 'miami_dade', 'FL'),
    (r'^city of mesa\b', 'City of Mesa, Arizona', 'mesa_az', 'AZ'),
    (r'^fulton county georgia\b', 'Fulton County, Georgia', 'fulton_ga', 'GA'),
    (r'^city of los angeles\b', 'City of Los Angeles', 'city_la', 'CA'),
    (r'^city of mesquite\b', 'City of Mesquite, Texas', 'mesquite_tx', 'TX'),
    (r'^city of baton rouge\b', 'City of Baton Rouge / Parish of East Baton Rouge', 'baton_rouge', 'LA'),
    (r'^city of corona\b', 'City of Corona, California', 'corona_ca', 'CA'),
    (r'^city of indio\b', 'City of Indio, California', 'indio_ca', 'CA'),
    (r'^city of richmond california\b', 'City of Richmond, California', 'richmond_ca', 'CA'),
    (r'^city of new york\b', 'City of New York', 'nyc', 'NY'),
    (r'^city of san jose\b', 'City of San José, California', 'san_jose', 'CA'),
    (r'^undp\b', 'United Nations Development Programme (UNDP)', 'undp', ''),
    (r'^world health organization\b|^unitaid\b', 'World Health Organization (WHO)', 'who', ''),
    (r'^european commission\b', 'European Commission', 'eu_commission', ''),
    (r'^university of toronto\b', 'University of Toronto', 'uoft', 'ON'),
    (r'^toronto transit commission\b', 'Toronto Transit Commission', 'ttc', 'ON'),
    (r'^nl heal?th services?\b|^nl heath services\b', 'Newfoundland and Labrador Health Services', 'nlhs', 'NL'),
    (r'^government of newfoundland and labrador gnl\b', 'Government of Newfoundland and Labrador', 'gov_NL', 'NL'),
    (r'^ministerie van defensie\b|^commando materieel', 'Ministerie van Defensie (Netherlands)', 'nl_mod', ''),
    (r'^eidgenossische technische hochschule zurich|^eidgenossisch technische hochschule zurich', 'ETH Zürich', 'ethz', ''),
    (r'^ecole polytechnique federale de lausanne', 'EPFL', 'epfl', ''),
    (r'^the geological survey of norway|^geological survey of norway', 'Geological Survey of Norway (NGU)', 'ngu', ''),
    (r'^government of ontario\b', 'Government of Ontario', 'gov_ON', 'ON'),
    (r'^government of yukon\b', 'Government of Yukon', 'gov_YT', 'YT'),
    (r'^province of nova scotia\b', 'Government of Nova Scotia', 'gov_NS', 'NS'),
    (r'^all government ministries and agencies\b', 'Government of Saskatchewan', 'gov_SK', 'SK'),
    (r'^manitoba (transportation and infrastructure|environment and climate change)\b', 'Government of Manitoba', 'gov_MB', 'MB'),
]

DESIG = r'(city|town|township|village|summer villages?|county|municipality|municipal district|district municipality|district|region|regional municipality|regional district|rural municipality|rm|md|united counties|resort municipality|county of|corporation of the (?:city|town|county|township|municipality))'
ORG_WORDS = re.compile(r'\b(universit\w*|college\w*|school\w*|board|authority|corporation|commission|hospital\w*|health|housing|foundation|librar\w*|police|society|inc|ltd|agency|institute|polytechnic|council|centre|center|crown|liquor|lottery|hydro|power|insurance|association|nation|airport|bank|corp|company|group|limited|museum|zoo|press|enterprises|regional office|sask[a-z]+|telecommunications|research council|conseil\w*|incorporated|federation|confederacy|gallery|trust|society|museum|transit)\b')


# separate legal entities (crown corporations, legislative offices, municipal bodies, associations) named like departments
NOT_DEPT = re.compile(r'(^halifax water$|\bwaste\b|\bgpo\b|enterprise network|\brda\b|^ceed$|acadien|innovacorp|miscellaneous|mash sector|'
                      r'^(build|develop|invest|link|tourism|conserve|elections) nova scotia$|^nova scotia (lands|federation|e911|education common services)|'
                      r'^hearing and speech nova scotia$|^nlc$|muskrat falls|workplace ?nl|house of assembly|auditor general|chief electoral|\bsask\b|gaming|'
                      r'irrigation district|rcssd|school division|provincial health services|destination bc|emergency health services|'
                      r'housing management commission|assessment authority|islands trust|pavco|pavilion|games society|worksafe|royal roads|'
                      r'licensing board|3shealth|office of the speaker|legislative services|liquor distribution branch|bc liquor|product distribution centre)')


def province_of(b, tz_by_portal):
    provs = collections.Counter()
    for s in b['sources']:
        if s['value'] in SRC_PROV:
            provs[SRC_PROV[s['value']]] += s['count']
    for a in b['addresses']:
        v = a['value']
        r = norm(v.get('region') or v.get('stateProvince') or '')
        if r in REG:
            provs[REG[r]] += a['count']
        lp = v.get('location_as_published') or ''
        m = re.search(r',\s*([A-Z]{2}),\s*CAN', lp)
        if m:
            provs[m.group(1)] += a['count']
    tzp = set()
    for p in b['identifiers'].get('bidsandtenders_portal', []):
        portal = p['value'].split('.')[0]
        for tz in tz_by_portal.get(portal, []):
            tzp |= TZ_PROV.get(tz, set())
    return provs, tzp


def municipal_parts(name):
    n = re.sub(r'\(.*?\)', ' ', name)
    n = re.sub(r'^the corporation of (the )?', '', n, flags=re.I)
    nn = norm(n)
    nn = re.sub(r'^the ', '', nn)
    m = re.match(r'^%s\s+of\s+(?:the\s+)?(.+)$' % DESIG, nn)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r'^(.+?)\s+(county|township|region|regional district|regional municipality)$', nn)
    if m:
        return m.group(2), m.group(1)
    m = re.match(r'^(rm|md) of (.+)$', nn)
    if m:
        return m.group(1), m.group(2)
    return None, nn


GENERIC = {'finance', 'justice', 'education', 'infrastructure', 'agriculture', 'health', 'energy', 'highways', 'environment', 'transportation',
           'housing', 'tourism', 'labour', 'seniors', 'corrections', 'lands', 'mines', 'fisheries', 'forestry', 'culture', 'immigration',
           'undp', 'confidential', 'various', 'procurement', 'purchasing', 'administration', 'operations', 'facilities'}
RAW_DESIG = re.compile(r'^(?:The Corporation of (?:the )?)?(?:City|Town|Township|Village|County|Municipality|Municipal District|District|Region|Regional Municipality|Regional District|Rural Municipality|United Counties|District Municipality)\s+of\s+(?:the\s+)?(.+)$', re.I)


def labels_for(name, desig, core):
    n = re.sub(r'\s*\(.*?\)\s*', ' ', name).strip()
    n = re.sub(r'^The Corporation of (the )?', '', n, flags=re.I).strip()
    out = {n, re.sub(r'^The ', '', n)}
    mraw = RAW_DESIG.match(n)
    if mraw:
        out.add(mraw.group(1).strip())
    if ' - ' in n:
        out.add(n.split(' - ')[0].strip())
    if desig:
        C = ' '.join(w.capitalize() if w not in ('of', 'and', 'the', 'de', 'la', 'du', 'des') else w for w in core.split())
        C2 = re.sub(r'\bSt\b', 'St.', C)
        for c in {C, C2}:
            out.add(c)
            if desig in ('county', 'county of', 'united counties'):
                out |= {c + ' County', 'County of ' + c, 'United Counties of ' + c}
            if desig in ('region', 'regional municipality'):
                out |= {'Regional Municipality of ' + c, c + ' Region', 'Region of ' + c}
            if desig in ('district', 'district municipality'):
                out |= {'District of ' + c, 'District Municipality of ' + c}
            if desig == 'regional district':
                out |= {'Regional District of ' + c}
            if desig in ('municipal district', 'md'):
                out |= {'Municipal District of ' + c}
            if desig in ('township',):
                out |= {'Township of ' + c, c + ' Township'}
            if desig in ('municipality',):
                out |= {'Municipality of ' + c}
            if desig in ('rural municipality', 'rm'):
                out |= {'Rural Municipality of ' + c}
    return sorted(x for x in out if x and len(x) >= 3)


def main():
    buyers = load_buyers()
    tz_by_portal = collections.defaultdict(set)
    lp = BASE + '/downloads/ca_bidsandtenders/listing.jsonl'
    if os.path.exists(lp):
        for l in open(lp):
            try:
                r = json.loads(l)
            except Exception:
                continue
            if r.get('portal') and r.get('closing_utc_source_tz'):
                tz_by_portal[r['portal']].add(r['closing_utc_source_tz'])
    # names of Alberta ministries as published in the sole-source disclosure (ministry-only dataset) and APC type
    ab_min = set()
    for b in buyers:
        srcs = {s['value'] for s in b['sources']}
        t = b['types'][0]['value'] if b['types'] else ''
        if 'ca_alberta_sole_source' in srcs or 'Alberta provincial government department' in t:
            ab_min.add(norm(b['name']))
    out = {}
    stats = collections.Counter()
    for b in buyers:
        k = b['buyer_key']; name = b['name']; nn = norm(name)
        srcs = {s['value']: s['count'] for s in b['sources']}
        t = b['types'][0]['value'] if b['types'] else ''
        provs, tzp = province_of(b, tz_by_portal)
        rec = {'name': name, 'country': b['country'], 'provinces': dict(provs), 'tz_provinces': sorted(tzp), 'type': t}
        prov = provs.most_common(1)[0][0] if provs else (list(tzp)[0] if len(tzp) == 1 else '')
        rec['province'] = prov
        # parents for divisions / named governments
        for rx, pn, pk, jur in PARENTS:
            if re.search(rx, nn):
                rec['parent'] = {'name': pn, 'key': pk, 'jurisdiction': jur, 'basis': 'name pattern /%s/' % rx}
                break
        if 'parent' not in rec and 'ca_newfoundland' in srcs and re.search(r'^(eastern|western|central)( regional)? health( authority)?$|^labrador grenfell( regional)? health( authority)?$|^nl centre for health information$|^newfoundland and labrador centre for health information$', nn):
            rec['parent'] = {'name': 'Newfoundland and Labrador Health Services', 'key': 'nlhs', 'jurisdiction': 'NL',
                             'basis': 'legacy NL regional health authority / NLCHI, integrated into Newfoundland and Labrador Health Services (provincial health authority since 2023)'}
        m = re.match(r'^government of (.+?) (?:–|-) executing agency', name.lower())
        if m and 'parent' not in rec:
            rec['parent'] = {'name': 'Government of ' + name[14:14 + len(m.group(1))], 'key': 'gov_' + norm(m.group(1)).replace(' ', '_'), 'jurisdiction': '',
                             'basis': 'CDB executing agency = national government'}
        desig, core = municipal_parts(name)
        rec['designation'] = desig; rec['core'] = core
        # provincial government units
        gov_juris = collections.Counter()
        if 'parent' not in rec and b['country'] == 'CA':
            for s, c in srcs.items():
                if s not in GOV_SRC:
                    continue
                pj = GOV_SRC[s]
                deptlike = (desig is None and not ORG_WORDS.search(nn)) or nn.startswith(('ministry of', 'department of', 'office of the'))
                if s == 'ca_alberta_sole_source':
                    deptlike = True
                if s == 'ca_alberta_apc':
                    deptlike = nn in ab_min or nn.startswith('ministry of')
                if s == 'ca_bc_ministry_awards':
                    deptlike = nn.startswith('ministry of') or (desig is None and not re.search(r'\b(universit\w*|college|school district|health authority|city of|town of|district of|regional district|corporation|commission|society|authority)\b', nn))
                if s == 'ca_nwt':
                    deptlike = ('GNWT' in t or deptlike) and not re.search(r'authority|corporation|\bnwt\b health', nn)
                    if nn in ('housing nwt', 'nwt housing corporation'):
                        deptlike = True
                if s in ('ca_newfoundland', 'ca_nova_scotia', 'ca_saskatchewan'):
                    deptlike = deptlike or bool(re.match(r'^(department|ministry|office) of', nn))
                    if re.search(r'\b(health authority|regional health|liquor|housing corporation|hydro|oilco|oil co|bull arm|nalcor|constabulary|workplacenl|centre for health)\b', nn):
                        deptlike = nn in ('royal newfoundland constabulary',) and False
                if s == 'ca_saskatchewan' and nn.startswith('saskbuilds and procurement'):
                    deptlike = True  # Ministry of SaskBuilds and Procurement
                if deptlike and NOT_DEPT.search(nn):
                    deptlike = False
                if deptlike:
                    gov_juris[pj] += c
        if gov_juris:
            rec['gov_units'] = dict(gov_juris)
            if len(gov_juris) == 1:
                pj = list(gov_juris)[0]
                rec['parent'] = {'name': GOV_NAME[pj], 'key': 'gov_' + pj, 'jurisdiction': pj,
                                 'basis': 'department/ministry/branch name published by the %s government source (%s)' % (pj, ', '.join(s for s in srcs if GOV_SRC.get(s) == pj))}
                stats['gov_unit_' + pj] += 1
            else:
                rec['ambiguous_jurisdictions'] = dict(gov_juris)
                stats['gov_unit_multi'] += 1
        rec['labels'] = labels_for(name, desig, core) if ('parent' not in rec and 'ambiguous_jurisdictions' not in rec) else []
        if rec['labels'] and desig is None and len(core.split()) < 2 and (core in GENERIC or len(core) < 4):
            rec['labels'] = []  # too generic for label lookup
        if rec.get('parent', {}).get('jurisdiction'):
            rec['province'] = rec['parent']['jurisdiction']
        out[k] = rec
        stats['parent' if 'parent' in rec else ('ambig' if 'ambiguous_jurisdictions' in rec else 'standalone')] += 1
    json.dump(out, open(WORK + '/classify.json', 'w'), ensure_ascii=False, indent=0)
    print(dict(stats))


main()

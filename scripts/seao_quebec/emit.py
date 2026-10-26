"""Merge SEAO XML + JSON staging into normalized records (one per numeroseao x awarded supplier).

Usage: python3 -I emit.py <xml_sqlite> <json_sqlite> <out_jsonl> <stats_json> <logfile> [--limit N]

Status logic (reference date 2026-10-25):
  excluded : vendor not Canadian / closure (information finale) matched / OCDS contract terminated or cancelled /
             planned end date (OCDS contracts[].period.endDate on an open contract) < 2026-10-25 / award or tender cancelled /
             contract concluded after 2026-10-25 / superseded by a later OCDS award to other suppliers
  ongoing  : open OCDS contract with period.endDate >= 2026-10-25 and dateSigned <= 2026-10-25
  ongoing_inferred : contract concluded <= 2026-10-25, no end date anywhere, no closure record in either feed
"""
import sys, os, re, json, sqlite3, datetime, unicodedata, collections, hashlib

TODAY = '2026-10-25'
RETRIEVED_AT = '2026-10-25T12:28:30Z'   # end of the JSON download window; per-file timestamps in logs/
DATASET_URL = 'https://www.donneesquebec.ca/recherche/dataset/systeme-electronique-dappel-doffres-seao'
NEW_PORTAL = 'https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId={}'

xml_db, json_db, out_path, stats_path, log_path = sys.argv[1:6]
limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
log = open(log_path, 'a', encoding='utf-8')


def L(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    log.write(f'{ts}\t{msg}\n'); log.flush(); print(msg, flush=True)


# ----------------------------------------------------------------------------- code tables (from the format spec PDFs + JSON equivalents)
TYPE_LABELS = {
    '3': "Contrat adjugé suite à un appel d'offres public",
    '9': 'Contrat octroyé de gré à gré',
    '10': "Contrat adjugé suite à un appel d'offres sur invitations",
    '11': "Contrat à la suite d'un achat mandaté ou d'un regroupement d'organismes",   # not in the 2021 spec; label taken from the JSON feed's procurementMethodDetails
    '14': "Contrat suite à un appel d'offres sur invitation publié au SEAO",
    '16': 'Contrat conclu relatif aux infrastructures de transport',
    '17': "Contrat conclu - Appel d'offres public non publié au SEAO",
}
TYPE_METHOD = {'3': 'open', '9': 'direct', '10': 'limited', '11': 'open', '14': 'limited', '16': 'open', '17': 'open'}
NATURE_LABELS = {'1': 'Approvisionnement (biens)', '2': 'Services', '3': 'Travaux de construction', '5': 'Autre', '6': 'Concession',
                 '7': 'Vente de biens immeubles', '8': 'Vente de biens meubles', '0': None}
PRECISION_LABELS = {'1': 'Services professionnels', '2': 'Services de nature technique'}
REGION_LABELS = {'1': 'Bas-Saint-Laurent', '2': 'Saguenay-Lac-Saint-Jean', '3': 'Capitale-Nationale', '4': 'Mauricie', '5': 'Estrie', '6': 'Montréal',
                 '7': 'Outaouais', '8': 'Abitibi-Témiscamingue', '9': 'Côte-Nord', '11': 'Nord-du-Québec', '12': 'Chaudière-Appalaches', '13': 'Laval',
                 '14': 'Laurentides', '15': 'Montérégie', '16': 'Lanaudière', '17': 'Centre-du-Québec', '18': 'Gaspésie-Îles-de-la-Madeleine', '19': 'Hors Québec'}
CAPROV = {'AB', 'BC', 'PE', 'MB', 'NB', 'NS', 'ON', 'QC', 'SK', 'NF', 'NL', 'NT', 'YT', 'NU', 'PQ'}
CA_POSTAL = re.compile(r'^[A-Z]\d[A-Z]\s?\d[A-Z]\d$')
COUNTRY_ISO2 = {'CAN': 'CA', 'CA': 'CA', 'CANADA': 'CA', 'USA': 'US', 'US': 'US', 'GBR': 'GB', 'FRA': 'FR', 'DEU': 'DE', 'NLD': 'NL', 'CHE': 'CH', 'AUS': 'AU', 'NZL': 'NZ', 'ESP': 'ES'}

LEGAL_TOKENS = {'inc', 'ltee', 'ltd', 'limitee', 'limited', 'enr', 'senc', 'sencrl', 'llp', 'corp', 'corporation', 'co', 'cie', 'compagnie', 'lp', 'sec', 'llc', 'plc', 'ulc', 'gp'}


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def norm_name(s):
    s = strip_accents((s or '').lower())
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    toks = [t for t in s.split() if t not in LEGAL_TOKENS]
    return ' '.join(toks)


def norm_neq(s):
    d = re.sub(r'\D', '', s or '')
    return d if len(d) == 10 else ''


def slugify(s, maxlen=60):
    s = strip_accents((s or '').lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:maxlen].strip('-') or 'unknown'


def num(s):
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    s = str(s).strip().replace(' ', '').replace(',', '.')
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def iso_date(s):
    """'aaaa-mm-jj hh:MM' / ISO datetime -> 'YYYY-MM-DD' or None."""
    if not s:
        return None
    m = re.match(r'^(\d{4}-\d{2}-\d{2})', str(s).strip())
    return m.group(1) if m else None


def item_id_from_url(url):
    m = re.search(r'ItemId=([0-9a-fA-F-]{36})', url or '')
    return m.group(1).lower() if m else None


def vendor_country(pays, province, postal):
    """Returns (iso2_or_raw, basis_text, is_canada)."""
    p = (pays or '').strip().upper()
    if p in ('CAN', 'CA', 'CANADA'):
        return 'CA', f'supplier country field = "{pays}" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)', True
    if p == '':
        prov = (province or '').strip().upper()
        cp = (postal or '').strip().upper()
        if prov in CAPROV:
            return 'CA', f'supplier country field blank; supplier province field = "{province}" is a Canadian province code', True
        if CA_POSTAL.match(cp):
            return 'CA', f'supplier country field blank; supplier postal code "{postal}" matches the Canadian postal-code pattern', True
        return None, 'supplier country field blank and no province/postal-code evidence', False
    return COUNTRY_ISO2.get(p, p), f'supplier country field = "{pays}" (not Canada)', False


def buyer_type(name, municipal):
    n = strip_accents((name or '').lower())
    if str(municipal).strip() == '1':
        if re.search(r'\bmrc\b|municipalite regionale de comte', n): return 'regional county municipality (MRC)'
        if re.search(r'\bville\b|\bcite\b', n): return 'city'
        if re.search(r'regie|societe de transport|reseau de transport|communaute metropolitaine|office municipal|office d.habitation', n): return 'municipal agency'
        return 'municipality'
    if re.search(r'^ministere|\bministere\b', n): return 'provincial ministry'
    if re.search(r'cisss|ciusss|centre integre|\bchu\b|centre hospitalier|hopital|institut universitaire|institut de cardiologie|institut national de sante|\bclsc\b|chsld|centre de readaptation|institut philippe|institut nazareth|centre jeunesse|agence de la sante|sante et services sociaux', n): return 'hospital / health and social services institution'
    if re.search(r'universite|ecole de technologie|\bhec\b|polytechnique|\benap\b|\binrs\b|teluq|ecole nationale', n): return 'university'
    if re.search(r'cegep|college|commission scolaire|centre de services scolaire|school board|conservatoire|institut de technologie|ecole', n): return 'school board / college'
    if re.search(r'hydro.quebec|loto.quebec|societe des alcools|\bsaq\b|investissement quebec|caisse de depot|societe quebecoise|societe de developpement|societe d.habitation|societe des traversiers|societe des etablissements|societe de l.assurance|societe du plan nord|societe de financement|societe immobiliere|societe quebecoise des infrastructures|\bsqi\b|revenu quebec|retraite quebec|autorite des marches|commission de la construction|\bcnesst\b|\bcsst\b|\bsaaq\b', n): return 'crown corporation / state enterprise'
    if re.search(r'surete du quebec|regie|commission|office|autorite|agence|centre d.acquisitions|centre de services partages|tribunal|curateur|protecteur|institut|conseil|fonds|bureau|secretariat|assemblee nationale|directeur general des elections|verificateur general|directeur des poursuites|bibliotheque|musee|centre de la francophonie|ecole nationale de police|corporation d.urgences|urgences.sante|heritage|societe', n): return 'provincial agency'
    return 'quebec public body'


# ----------------------------------------------------------------------------- open DBs
xc = sqlite3.connect(xml_db); xc.execute('PRAGMA cache_size=-300000')
jc = sqlite3.connect(json_db); jc.execute('PRAGMA cache_size=-300000')

# iterate numeroseao in string order across both feeds (merge join)
xml_cur = xc.execute('SELECT numeroseao, ord, src, kind, json FROM avis_rows ORDER BY numeroseao, ord')
clo_cur = xc.execute('SELECT numeroseao, ord, src, kind, json FROM contrat_rows ORDER BY numeroseao, ord')
dep_cur = xc.execute('SELECT numeroseao, ord, src, kind, json FROM depense_rows ORDER BY numeroseao, ord')
jl_cur = jc.execute('SELECT numeroseao, ocid, release_id, release_date, file_order, src, tags, json FROM latest ORDER BY numeroseao')


class Grouper:
    """Pull consecutive rows with the same key from an ordered cursor."""
    def __init__(self, cur):
        self.cur = cur; self.pending = next(cur, None)

    def key(self):
        return self.pending[0] if self.pending else None

    def take(self, key):
        out = []
        while self.pending is not None and self.pending[0] == key:
            out.append(self.pending); self.pending = next(self.cur, None)
        return out


G_avis, G_clo, G_dep, G_jl = Grouper(xml_cur), Grouper(clo_cur), Grouper(dep_cur), Grouper(jl_cur)

stats = collections.Counter()
by_year = collections.defaultdict(collections.Counter)
excl_year = collections.defaultdict(collections.Counter)
pays_values = collections.Counter()
buyer_types = collections.Counter()
closure_pub_years = collections.Counter()
samples = []
out = open(out_path, 'w', encoding='utf-8')
n_written = 0


def json_history(ocid):
    rows = jc.execute('SELECT release_id, release_date, tags, src, file_order FROM json_releases WHERE ocid=? ORDER BY file_order, release_id', (ocid,)).fetchall()
    return [{'release_id': r[0], 'release_date': r[1], 'tag': r[2].split(',') if r[2] else [], 'source_file': r[3]} for r in rows]


def json_latest_with_contracts(ocid):
    """Latest release that still lists contracts (fallback when the very latest snapshot dropped them)."""
    for (js,) in jc.execute('SELECT json FROM json_releases WHERE ocid=? ORDER BY file_order DESC, release_id DESC', (ocid,)):
        r = json.loads(js)
        if r.get('contracts'):
            return r
    return None


def supplier_key(neq, name):
    n = norm_neq(neq)
    return ('neq', n) if n else ('name', norm_name(name))


def build_json_view(rel):
    """From an OCDS release: parties by id, awards by id, per-supplier contract lines."""
    parties = {p.get('id'): p for p in rel.get('parties') or []}
    awards = {a.get('id'): a for a in rel.get('awards') or []}
    per_sup = collections.OrderedDict()   # key -> dict(party, supplier_ref, awards, contracts)
    contracts_by_award = collections.defaultdict(list)
    for c in rel.get('contracts') or []:
        contracts_by_award[c.get('awardID')].append(c)
    orphan = [c for c in rel.get('contracts') or [] if c.get('awardID') not in awards]
    for aid, a in awards.items():
        sups = a.get('suppliers') or []
        if not sups:
            sups = [{'id': None, 'name': None}]
        for s in sups:
            p = parties.get(s.get('id')) or {}
            det = p.get('details') or {}
            neq = det.get('neq') or det.get('NEQ') or ''
            if not neq and (s.get('id') or '').startswith('FO-'):
                cand = s['id'][3:]
                if norm_neq(cand):
                    neq = cand
            key = supplier_key(neq, s.get('name') or p.get('name'))
            e = per_sup.setdefault(key, {'party': p, 'supplier_ref': s, 'neq': norm_neq(neq) or None, 'name': s.get('name') or p.get('name'), 'awards': [], 'contracts': []})
            if a not in e['awards']:
                e['awards'].append(a)
            for c in contracts_by_award.get(aid, []):
                if c not in e['contracts']:
                    e['contracts'].append(c)
    if orphan:
        key = ('name', '__orphan_contracts__')
        per_sup[key] = {'party': {}, 'supplier_ref': {}, 'neq': None, 'name': None, 'awards': [], 'contracts': orphan}
    return parties, awards, per_sup


def classify_json_contracts(contracts, awards=()):
    """Return (cls, planned_end, details) for a supplier's OCDS contract lines (or award-only lines)."""
    classes = []
    if not contracts:
        if awards and all((a.get('status') or '').lower() == 'cancelled' for a in awards):
            return 'closed', None, []
        return 'award_only', None, []
    for c in contracts:
        st = (c.get('status') or '').lower()
        ed = iso_date((c.get('period') or {}).get('endDate'))
        if st in ('terminated', 'cancelled'):
            classes.append(('closed', ed, c))
        elif ed and ed >= TODAY:
            classes.append(('planned_end_future', ed, c))
        elif ed:
            classes.append(('planned_end_past', ed, c))
        else:
            classes.append(('open_no_end', None, c))
    kinds = {k for k, _, _ in classes}
    if 'planned_end_future' in kinds:
        return 'planned_end_future', max(e for k, e, _ in classes if k == 'planned_end_future'), classes
    if 'open_no_end' in kinds:
        return 'open_no_end', None, classes
    if 'planned_end_past' in kinds:
        return 'planned_end_past', max(e for k, e, _ in classes if k == 'planned_end_past'), classes
    return 'closed', max((e or '') for k, e, _ in classes) or None, classes


def emit(rec):
    global n_written
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
    n_written += 1
    if n_written % 1000 == 0:
        out.flush()
    if len(samples) < 40 and (n_written % 997 == 0):
        samples.append(rec)


def process(ns):
    avis_rows = G_avis.take(ns); clo_rows = G_clo.take(ns); dep_rows = G_dep.take(ns); jl_rows = G_jl.take(ns)
    stats['notices_total'] += 1
    # ---------------- XML side
    xml_versions = [dict(ord=r[1], src=r[2], kind=r[3], obj=json.loads(r[4])) for r in avis_rows]
    avis = xml_versions[-1]['obj'] if xml_versions else None
    # supplementary expenses: Depenses appends, DepensesRevisions replaces the full list
    depenses = []
    for r in dep_rows:
        o = json.loads(r[4])
        items = []
        for d in o.get('depenses') or []:
            if isinstance(d, dict):
                d = dict(d); d['_source_file'] = r[2]; d['_export_period'] = o.get('_export_period'); items.append(d)
        if r[3] == 'DepensesRevisions':
            depenses = items
        else:
            depenses.extend(items)
    closures = [json.loads(r[4]) for r in clo_rows]
    # ---------------- JSON side
    rel = None; rel_hist = []; rel_caveat = None; ocid = None
    if jl_rows:
        jr = jl_rows[0]
        ocid = jr[1]
        rel = json.loads(jr[7])
        rel_hist = json_history(ocid)
        if not rel.get('contracts'):
            alt = json_latest_with_contracts(ocid)
            if alt is not None:
                rel_caveat = (f"most recent OCDS release ({rel.get('id')} from {rel.get('_source_file')}, tag {rel.get('tag')}) no longer lists any contract; "
                              f"contract data taken from the latest contract-bearing release {alt.get('id')} ({alt.get('_source_file')})")
                rel = alt
    j_parties, j_awards, j_per_sup = build_json_view(rel) if rel else ({}, {}, collections.OrderedDict())
    tender = (rel or {}).get('tender') or {}
    tender_cancelled = (tender.get('status') == 'cancelled')

    # ---------------- supplier universe
    suppliers = collections.OrderedDict()   # key -> dict
    if avis:
        for f in avis.get('fournisseurs') or []:
            if not isinstance(f, dict) or f.get('adjudicataire') != '1':
                continue
            key = supplier_key(f.get('neq'), f.get('nomorganisation'))
            e = suppliers.setdefault(key, {'xml_lines': [], 'json': None, 'name': f.get('nomorganisation'), 'neq': norm_neq(f.get('neq')) or None})
            e['xml_lines'].append(f)
    for key, e in j_per_sup.items():
        s = suppliers.get(key)
        if s is None:
            # try name match against XML suppliers when NEQ differs/missing
            alt = None
            if key[0] == 'neq':
                nn = norm_name(e['name'])
                for k2, s2 in suppliers.items():
                    if k2[0] == 'name' and k2[1] == nn:
                        alt = k2; break
            else:
                for k2, s2 in suppliers.items():
                    if norm_name(s2['name']) == key[1]:
                        alt = k2; break
            if alt is not None:
                suppliers[alt]['json'] = e
            else:
                suppliers[key] = {'xml_lines': [], 'json': e, 'name': e['name'], 'neq': e['neq']}
        else:
            s['json'] = e
    # pair leftover XML-only and JSON-only suppliers (supplier renamed / NEQ corrected in SEAO): same amount, else 1:1 leftover
    xml_only = [k for k, e in suppliers.items() if e['xml_lines'] and not e['json']]
    json_only = [k for k, e in suppliers.items() if e['json'] and not e['xml_lines'] and k[1] != '__orphan_contracts__']
    if xml_only and json_only:
        def jamt(e):
            return round(sum((num((c.get('value') or {}).get('amount')) or 0) for c in e['json']['contracts']) or sum((num((a.get('value') or {}).get('amount')) or 0) for a in e['json']['awards']), 2)
        def xamt(e):
            return round(sum((num(f.get('montantcontrat')) or 0) for f in e['xml_lines']), 2)
        pairs = []
        used = set()
        for kx in xml_only:
            for kj in json_only:
                if kj in used:
                    continue
                if xamt(suppliers[kx]) == jamt(suppliers[kj]):
                    pairs.append((kx, kj)); used.add(kj); break
        if not pairs and len(xml_only) == 1 and len(json_only) == 1:
            pairs.append((xml_only[0], json_only[0]))
        for kx, kj in pairs:
            suppliers[kx]['json'] = suppliers[kj]['json']
            suppliers[kx]['paired_note'] = f"OCDS feed lists this contract under supplier '{suppliers[kj]['name']}' (NEQ {suppliers[kj]['neq']}) while the XML notice lists '{suppliers[kx]['name']}' (NEQ {suppliers[kx]['neq']}); paired by contract amount / single leftover"
            del suppliers[kj]
            stats['supplier_paired_xml_json_rename'] += 1
    if not suppliers:
        stats['notices_without_awarded_supplier'] += 1
        return
    # XML suppliers that the JSON (when it carries awards) no longer lists -> superseded
    json_has_awards = bool(rel and (rel.get('contracts') or rel.get('awards')))

    # ---------------- closures -> suppliers (NEQ, then name, then single-supplier fallback)
    unmatched_closures = []
    closure_by_sup = collections.defaultdict(list)
    for c in closures:
        k = supplier_key(c.get('neqcontractant'), c.get('nomcontractant'))
        target = None
        if k in suppliers:
            target = k
        else:
            nn = norm_name(c.get('nomcontractant'))
            for k2, s2 in suppliers.items():
                if nn and norm_name(s2['name']) == nn:
                    target = k2; break
        if target is None and len(suppliers) == 1:
            target = next(iter(suppliers)); stats['closure_matched_by_single_supplier_fallback'] += 1
        if target is None:
            unmatched_closures.append(c); stats['closure_unmatched'] += 1
        else:
            closure_by_sup[target].append(c)
    dep_by_sup = collections.defaultdict(list); unmatched_dep = []
    for d in depenses:
        k = supplier_key(d.get('neqcontractant'), d.get('nomcontractant'))
        target = None
        if k in suppliers:
            target = k
        else:
            nn = norm_name(d.get('nomcontractant'))
            for k2, s2 in suppliers.items():
                if nn and norm_name(s2['name']) == nn:
                    target = k2; break
        if target is None and len(suppliers) == 1:
            target = next(iter(suppliers))
        if target is None:
            unmatched_dep.append(d)
        else:
            dep_by_sup[target].append(d)

    # ---------------- notice-level normalized fields
    item_id = None; hyperlien = None
    if avis:
        hyperlien = avis.get('hyperlienseao') or None
        item_id = item_id_from_url(hyperlien)
    if not item_id:
        for d in tender.get('documents') or []:
            item_id = item_id_from_url(d.get('url'))
            if item_id:
                break
    record_url = NEW_PORTAL.format(item_id) if item_id else None
    buyer_party = None
    if rel:
        bid = ((rel.get('buyer') or {}).get('id'))
        buyer_party = j_parties.get(bid)
    if avis:
        b_name = avis.get('organisme'); municipal = avis.get('municipal')
        b_addr = {'line1': avis.get('adresse1') or None, 'line2': avis.get('adresse2') or None, 'city': avis.get('ville') or None,
                  'region': avis.get('province') or None, 'postal_code': avis.get('codepostal') or None, 'country': avis.get('pays') or None}
        b_country = COUNTRY_ISO2.get((avis.get('pays') or '').strip().upper(), (avis.get('pays') or None))
    else:
        b_name = (rel.get('buyer') or {}).get('name') or (buyer_party or {}).get('name')
        municipal = ((buyer_party or {}).get('details') or {}).get('municipal') or ((buyer_party or {}).get('details') or {}).get('Municipal')
        ad = (buyer_party or {}).get('address') or {}
        b_addr = {'line1': ad.get('streetAddress'), 'line2': None, 'city': ad.get('locality'), 'region': ad.get('region'), 'postal_code': ad.get('postalCode'), 'country': ad.get('countryName')}
        b_country = COUNTRY_ISO2.get((ad.get('countryName') or '').strip().upper(), ad.get('countryName') or ('CA' if b_name else None))
    b_ids = {}
    if rel and (rel.get('buyer') or {}).get('id'):
        b_ids['seao_organisation_id'] = rel['buyer']['id']
    btype = buyer_type(b_name, municipal)
    buyer_types[btype] += 1

    if avis:
        title = avis.get('titre'); tcode = avis.get('type'); ncode = avis.get('nature'); prec = avis.get('precision')
        proc_method = TYPE_METHOD.get(tcode); proc_detail = TYPE_LABELS.get(tcode, f'type code {tcode}')
        nature_label = NATURE_LABELS.get(ncode)
        if ncode == '2' and prec in PRECISION_LABELS:
            nature_label = f'{nature_label} - {PRECISION_LABELS[prec]}'
        elif ncode == '5' and prec:
            nature_label = f'Autre - {prec}'
        commodity = {'unspsc': avis.get('unspscprincipale') or None, 'seao_category': avis.get('categorieseao') or None}
        if tender.get('items'):
            cl = (tender['items'][0].get('classification') or {})
            commodity['unspsc_description'] = cl.get('description')
            if not commodity['unspsc']:
                commodity['unspsc'] = cl.get('id')
        description = nature_label
        published = iso_date(avis.get('datesaisieadjudication')) or iso_date(avis.get('datepublication'))
        tender_pub = iso_date(avis.get('datepublication')); tender_close = iso_date(avis.get('datefermeture'))
        disposition = avis.get('disposition') or None
        regions = [REGION_LABELS.get(x.strip(), x.strip()) for x in (avis.get('regionlivraison') or '').split(',') if x.strip()]
    else:
        title = tender.get('title'); tcode = None; ncode = None
        proc_method = tender.get('procurementMethod'); proc_detail = tender.get('procurementMethodDetails')
        cats = tender.get('additionalProcurementCategories') or []
        description = '; '.join([x for x in [tender.get('mainProcurementCategory')] + cats if x]) or None
        items = tender.get('items') or []
        cl = (items[0].get('classification') or {}) if items else {}
        commodity = {'unspsc': cl.get('id'), 'unspsc_description': cl.get('description'), 'seao_category': (items[0].get('description') if items else None)}
        published = None   # set per supplier from release history below
        tender_pub = iso_date((tender.get('tenderPeriod') or {}).get('startDate')); tender_close = iso_date((tender.get('tenderPeriod') or {}).get('endDate'))
        disposition = tender.get('procurementMethodRationale')
        regions = []
    commodity = {k: v for k, v in commodity.items() if v}

    # ---------------- per supplier
    for key, s in suppliers.items():
        stats['supplier_lines_total'] += 1
        xml_lines = s['xml_lines']; jv = s['json']
        # vendor country
        if xml_lines:
            f0 = xml_lines[-1]
            pays_values[(f0.get('pays') or '')] += 1
            iso, basis, is_ca = vendor_country(f0.get('pays'), f0.get('province'), f0.get('codepostal'))
            basis = 'XML fournisseur/pays: ' + basis
            v_addr = {'line1': f0.get('adresse1') or None, 'line2': f0.get('adresse2') or None, 'city': f0.get('ville') or None, 'region': f0.get('province') or None,
                      'postal_code': f0.get('codepostal') or None, 'country': f0.get('pays') or None}
        else:
            ad = (jv['party'].get('address') or {}) if jv else {}
            pays_values[('JSON:' + str(ad.get('countryName')))] += 1
            iso, basis, is_ca = vendor_country(ad.get('countryName'), ad.get('region'), ad.get('postalCode'))
            basis = 'OCDS parties[role=supplier].address.countryName: ' + basis
            v_addr = {'line1': ad.get('streetAddress'), 'line2': None, 'city': ad.get('locality'), 'region': ad.get('region'), 'postal_code': ad.get('postalCode'), 'country': ad.get('countryName')}
        if not is_ca:
            stats['excluded_vendor_not_canada'] += 1
            continue
        # conclusion date
        signed = None
        if xml_lines and avis:
            signed = iso_date(avis.get('dateadjudication'))
        if jv:
            ds = [iso_date(c.get('dateSigned')) for c in jv['contracts']] + ([iso_date(a.get('date')) for a in jv['awards']] if not jv['contracts'] else [])
            ds = [d for d in ds if d]
            if ds and not signed:
                signed = min(ds)
            elif ds and signed and min(ds) != signed:
                pass  # keep XML conclusion date; JSON dates kept in raw
        year = (signed or '')[:4] or 'unknown'
        # closure / status
        xml_closed = bool(closure_by_sup.get(key))
        j_cls, planned_end, j_classes = (None, None, [])
        if jv:
            j_cls, planned_end, j_classes = classify_json_contracts(jv['contracts'], jv['awards'])
            if any(a.get('status') == 'cancelled' for a in jv['awards']) and all((c.get('status') in ('cancelled', 'terminated')) for c in jv['contracts']):
                j_cls = 'closed'
        superseded = (not jv) and json_has_awards and bool(xml_lines)
        if superseded:
            stats['excluded_superseded_by_json_awards'] += 1; excl_year[year]['superseded'] += 1
            continue
        if tender_cancelled and not xml_lines:
            stats['excluded_tender_cancelled'] += 1; excl_year[year]['tender_cancelled'] += 1
            continue
        if xml_closed:
            stats['excluded_closure_xml'] += 1; excl_year[year]['closure_xml'] += 1
            for c in closure_by_sup[key]:
                closure_pub_years[(c.get('datepublicationfinale') or '')[:4]] += 1
            continue
        if j_cls == 'closed':
            stats['excluded_closure_json'] += 1; excl_year[year]['closure_json'] += 1
            continue
        if j_cls == 'planned_end_past':
            stats['excluded_planned_end_past'] += 1; excl_year[year]['planned_end_past'] += 1
            continue
        if signed and signed > TODAY:
            stats['excluded_future_start'] += 1; excl_year[year]['future_start'] += 1
            continue
        # XML multi-line partial closure cannot occur here (xml_closed handled); count lines
        if j_cls == 'planned_end_future':
            status = 'ongoing'
            open_c = [c for k_, e_, c in j_classes if k_ == 'planned_end_future']
            status_basis = (f"OCDS contracts[].period.endDate = {planned_end} (planned end date; contract status '{open_c[0].get('status')}') is on/after {TODAY}; "
                            f"contract concluded (dateSigned) {signed or 'n/a'} on/before {TODAY}; no final-information (closure) record in XML Contrats files nor 'terminated' status in OCDS as of retrieval")
        else:
            status = 'ongoing_inferred'
            if jv and jv['contracts']:
                jnote = f"OCDS contract status '{jv['contracts'][-1].get('status')}' with no period.endDate in latest release {rel.get('id')} from {rel.get('_source_file')}"
            elif jv:
                jnote = f"OCDS release {rel.get('id')} from {rel.get('_source_file')} carries only an award (status '{jv['awards'][-1].get('status')}') for this supplier, no contracts[] entry and no termination"
            else:
                jnote = 'notice absent from the OCDS JSON feed 2021-03..2026-10-18, so no post-May-2024 closure could be detected'
            status_basis = (f"contract concluded on {signed or 'unknown date'}; no final-information (closure) record published as of retrieval "
                            f"(no matching record in XML Contrats/ContratsRevisions files 2009-01..2024-05; {jnote})")
        if rel_caveat and jv:
            status_basis += '; CAVEAT: ' + rel_caveat
        if s.get('paired_note'):
            status_basis += '; NOTE: ' + s['paired_note']
        if unmatched_closures:
            status_basis += f'; CAVEAT: {len(unmatched_closures)} final-information record(s) exist for this notice under contractor name(s) that match none of the awarded suppliers (kept in raw.information_finale_unmatched)'
        if xml_lines and len(xml_lines) > 1:
            status_basis += f'; supplier has {len(xml_lines)} awarded lines in the notice (amounts summed)'
        closed_lines = [c for k_, e_, c in j_classes if k_ == 'closed']
        if closed_lines and jv and jv['contracts']:
            status_basis += f"; NOTE: {len(closed_lines)} of {len(jv['contracts'])} OCDS contract lines for this supplier are terminated/cancelled (ids {[c.get('id') for c in closed_lines]}); the open line(s) drive the status"
        stats[f'status_{status}'] += 1; by_year[year][status] += 1
        stats[f'status_{status}_' + ('json_backed' if jv else 'xml_only')] += 1

        # values
        if xml_lines:
            amounts = [num(f.get('montantcontrat')) for f in xml_lines]
            value = sum(a for a in amounts if a is not None) if any(a is not None for a in amounts) else None
            vd = {'montantcontrat': value}
            tot = [num(f.get('montanttotalcontrat')) for f in xml_lines]
            tot = [t for t in tot if t]
            if tot:
                vd['montanttotalcontrat'] = sum(tot)
            sub = [num(f.get('montantsoumis')) for f in xml_lines]
            sub = [t for t in sub if t is not None]
            if sub:
                vd['montantsoumis'] = sum(sub)
            unit = xml_lines[-1].get('montantssoumisunite')
        else:
            if jv['contracts']:
                amounts = [num((c.get('value') or {}).get('amount')) for c in jv['contracts']]
                value = sum(a for a in amounts if a is not None) if any(a is not None for a in amounts) else None
                vd = {'ocds_contract_value_amount': value}
            else:
                amounts = [num((a.get('value') or {}).get('amount')) for a in jv['awards']]
                value = sum(a for a in amounts if a is not None) if any(a is not None for a in amounts) else None
                vd = {'ocds_award_value_amount': value}
            ta = [num((a.get('value') or {}).get('totalAmount')) for a in jv['awards']]
            ta = [t for t in ta if t is not None]
            if ta:
                vd['ocds_award_totalAmount'] = sum(ta)
            unit = None
        if jv and xml_lines:
            jam = [num((c.get('value') or {}).get('amount')) for c in jv['contracts']]
            jam = [a for a in jam if a is not None]
            if jam:
                vd['ocds_contract_value_amount'] = sum(jam)
        deps = dep_by_sup.get(key, [])
        if deps:
            vd['supplementary_expenses_total'] = sum((num(d.get('montantdepense')) or 0) for d in deps)
            vd['supplementary_expenses_count'] = len(deps)
        amendments = []
        if jv:
            for c in jv['contracts']:
                amendments.extend(c.get('amendments') or [])
        amended_last = None
        cands = [iso_date(d.get('datepublicationdepense')) or iso_date(d.get('datedepense')) for d in deps] + [iso_date(a.get('date')) for a in amendments]
        cands = [c for c in cands if c]
        if cands:
            amended_last = max(cands)
        # published date
        pub = published
        if not pub and jv and rel_hist:
            cids = {c.get('id') for c in jv['contracts']}
            first = None
            for h in rel_hist:
                if 'contract' in h['tag'] or 'contractUpdate' in h['tag'] or 'awardUpdate' in h['tag'] or 'contractTermination' in h['tag']:
                    first = h; break
            if first is None:
                first = rel_hist[0]
            rid = first.get('release_id') or ''
            if re.match(r'^\d{14}$', rid):
                pub = f'{rid[:4]}-{rid[4:6]}-{rid[6:8]}'
            else:
                pub = iso_date(first.get('release_date'))
        # identifiers
        ids = {'numeroseao': ns}
        if avis and avis.get('numero'):
            ids['numero'] = avis.get('numero')
        elif tender.get('id'):
            ids['numero'] = tender.get('id')
        if ocid:
            ids['ocid'] = ocid
        if jv:
            ids['ocds_contract_ids'] = [c.get('id') for c in jv['contracts']]
            ids['ocds_award_ids'] = [a.get('id') for a in jv['awards']]
        if item_id:
            ids['seao_item_id'] = item_id
        related = {}
        if hyperlien:
            related['hyperlienseao_original'] = hyperlien
        if record_url:
            related['notice_url'] = record_url
        if tender.get('documents'):
            related['ocds_tender_document_url'] = tender['documents'][0].get('url')
        if rel and rel.get('relatedProcesses'):
            related['ocds_relatedProcesses'] = rel['relatedProcesses']
        if regions:
            related['delivery_regions'] = regions
        if disposition:
            related['disposition_or_rationale'] = disposition
        if unit and unit != '1':
            related['montantssoumisunite_code'] = unit
        v_ids = {}
        if s['neq']:
            v_ids['neq'] = s['neq']
        if jv and (jv['supplier_ref'] or {}).get('id'):
            v_ids['seao_supplier_id'] = jv['supplier_ref']['id']
        v_contact = {}
        slug = slugify(s['name'])
        rec_id = f"seao_quebec:{ns}:{slug}"
        if sum(1 for k2 in suppliers if slugify(suppliers[k2]['name']) == slug) > 1:
            # several awarded suppliers of this notice share the (truncated) slug: disambiguate with NEQ or a hash of the full name
            rec_id += '-' + (key[1] if key[0] == 'neq' else hashlib.sha1((s['name'] or '').encode('utf-8')).hexdigest()[:8])
        raw = {
            'avis': avis,
            'avis_appearances': [{'source_file': v['src'], 'kind': v['kind'], 'export_period': v['obj'].get('_export_period')} for v in xml_versions] or None,
            'fournisseur_lines': xml_lines or None,
            'depenses_supplementaires': deps,
            'depenses_supplementaires_unmatched': unmatched_dep or None,
            'information_finale': None,
            'information_finale_unmatched': unmatched_closures or None,
            'ocds_release': rel,
            'ocds_release_history': rel_hist or None,
            'ocds_supplier_contracts': (jv['contracts'] if jv else None),
            'ocds_supplier_awards': (jv['awards'] if jv else None),
            'ocds_supplier_party': (jv['party'] if jv else None),
            'code_labels': {'type': TYPE_LABELS.get(tcode) if tcode else None, 'nature': NATURE_LABELS.get(ncode) if ncode else None,
                            'precision': PRECISION_LABELS.get(avis.get('precision')) if avis else None} if avis else None,
        }
        rec = {
            'record_id': rec_id,
            'source': {'key': 'seao_quebec', 'name': "Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes",
                       'publisher': 'Secrétariat du Conseil du trésor (Québec) via Données Québec', 'dataset_url': DATASET_URL,
                       'record_url': record_url, 'retrieved_at': RETRIEVED_AT},
            'status': status, 'status_basis': status_basis,
            'contract': {
                'identifiers': ids, 'title': title, 'description': description, 'instrument_type': 'contract',
                'procurement_method': proc_method, 'solicitation_procedure': proc_detail, 'commodity': commodity,
                'value': value, 'currency': 'CAD', 'value_detail': vd,
                'dates': {'published': pub, 'signed': signed, 'start': signed, 'end': planned_end if status == 'ongoing' else None, 'amended_last': amended_last,
                          'tender_published': tender_pub, 'tender_closing': tender_close},
                'related': related,
            },
            'buyer': {'name': b_name, 'country': b_country, 'type': btype, 'identifiers': b_ids, 'address': b_addr,
                      'contact': {}, 'municipal_flag': str(municipal) if municipal is not None else None},
            'vendor': {'name': s['name'], 'country': 'CA', 'country_basis': basis, 'identifiers': v_ids, 'address': v_addr, 'contact': v_contact},
            'raw': raw,
        }
        emit(rec)


# ----------------------------------------------------------------------------- main loop (merge join over 4 ordered cursors)
L('START emit')
count = 0
while True:
    keys = [k for k in (G_avis.key(), G_clo.key(), G_dep.key(), G_jl.key()) if k is not None]
    if not keys:
        break
    ns = min(keys)
    try:
        process(ns)
    except Exception as e:
        stats['errors'] += 1
        L(f'ERROR numeroseao={ns}: {e!r}')
        # make sure cursors advance past this key
        G_avis.take(ns); G_clo.take(ns); G_dep.take(ns); G_jl.take(ns)
    count += 1
    if count % 50000 == 0:
        L(f'... {count} notices processed, {n_written} records written, stats={dict(stats)}')
    if limit and count >= limit:
        break
out.close()
L(f'DONE notices={count} written={n_written}')
with open(stats_path, 'w', encoding='utf-8') as f:
    json.dump({'stats': dict(stats), 'by_conclusion_year': {y: dict(c) for y, c in sorted(by_year.items())},
               'excluded_by_conclusion_year': {y: dict(c) for y, c in sorted(excl_year.items())},
               'pays_values': dict(pays_values.most_common()), 'buyer_types': dict(buyer_types.most_common()),
               'closure_publication_years': dict(sorted(closure_pub_years.items())),
               'samples': [s['record_id'] for s in samples]}, f, ensure_ascii=False, indent=1)
L(json.dumps(dict(stats)))

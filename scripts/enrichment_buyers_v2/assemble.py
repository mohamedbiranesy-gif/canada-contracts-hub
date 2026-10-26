"""Stage 3 (v2): merge directory/parent data + crawl results (v2 crawl + reused v1 crawl results) + targeted findings into
enrichment/v2/buyers_enriched_v2.jsonl (atomic rewrite, one line per input buyer)."""
import sys, os, json, re, glob, collections, urllib.parse, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

OUT = OUT_ENRICHED
buyers = load_buyers()
bulk = json.load(open(WORK + '/bulk.json'))
crawl = {}
reuse_sites = {x['site'].rstrip('/') for x in json.load(open(WORK + '/sites_reused_v1.json'))} if os.path.exists(WORK + '/sites_reused_v1.json') else set()
files = [(f, True) for f in sorted(glob.glob(OLD_WORK + '/crawl*.jsonl')) + sorted(glob.glob(OLD_WORK + '/deep*.jsonl'))] + \
        [(f, False) for f in sorted(glob.glob(WORK + '/crawl*.jsonl')) + sorted(glob.glob(WORK + '/deep*.jsonl')) + sorted(glob.glob(WORK + '/pdf*.jsonl'))]
for f, is_old in files:
    if 'test' in f:
        continue
    for l in open(f):
        if is_old and not any(rs in l[:600] for rs in reuse_sites):
            continue
        try:
            r = json.loads(l)
        except Exception:
            continue
        key = r['site'].rstrip('/')
        if is_old and key not in reuse_sites:
            continue
        if is_old:
            r['reused_from_v1'] = True
        if key in crawl:
            o = crawl[key]
            for fld in ('pages', 'emails', 'invoice_snippets', 'portal_links', 'errors'):
                o[fld] = (o.get(fld) or []) + (r.get(fld) or [])
            if r.get('status') == 'ok' and o.get('status') != 'ok' and r.get('pages'):
                o['status'] = 'ok'
            o.setdefault('modes', []).append(r.get('mode', 'crawl'))
        else:
            crawl[key] = r
reqm = json.load(open(WORK + '/req_matches.json'))['matches'] if os.path.exists(WORK + '/req_matches.json') else {}
manual = [json.loads(l) for l in open(WORK + '/manual_ap.jsonl')] if os.path.exists(WORK + '/manual_ap.jsonl') else []
CLS = json.load(open(WORK + '/classify.json'))
PROV_OF = {}
for _k, _c in CLS.items():
    PROV_OF[_c['name']] = _c.get('province', '')
    _bk = bulk.get(_k) or {}
    if _bk.get('canonical_name'):
        PROV_OF.setdefault(_bk['canonical_name'], _c.get('province', ''))
SHARED_HOSTS = {'www.canada.ca', 'www.quebec.ca', 'canada.ca', 'www.gov.uk', 'www.oregon.gov', 'oregon.gov', 'www.gov.mb.ca', 'www2.gov.bc.ca', 'www.alberta.ca', 'novascotia.ca', 'www.saskatchewan.ca', 'www.gov.nl.ca', 'www.ontario.ca', 'www.mass.gov', 'www.nyc.gov'}
GOV_SUFFIX = ('gc.ca', 'canada.ca', 'gouv.qc.ca', 'gov', 'gov.uk', 'gov.au', 'quebec')
APKW = ['factur', 'invoice', 'payable', 'fournisseur', 'supplier', 'vendor', 'comptes', 'paiement', 'payment', 'affaire', 'business']


def regdom(h):
    h = h.lower().split(':')[0]
    p = h.split('.')
    if len(p) >= 3 and p[-1] == 'ca' and p[-2] in ('qc', 'on', 'gc', 'gouv'):
        return '.'.join(p[-3:]) if p[-2] != 'gouv' else '.'.join(p[-4:])
    return '.'.join(p[-2:])


GENERIC_TOK = {'county', 'town', 'city', 'municipality', 'district', 'region', 'regional', 'township', 'village', 'school', 'board', 'catholic',
               'public', 'services', 'service', 'university', 'college', 'division', 'corporation', 'authority', 'rural', 'health', 'alberta',
               'ontario', 'national', 'canada', 'north', 'south', 'east', 'west', 'government', 'department', 'ministry', 'separate', 'roman',
               'commission', 'housing', 'foundation', 'saint', 'sainte', 'greater', 'united', 'counties'}
DIRECTORY_PAGE = re.compile(r'(business[-_ ]?directory|businessdirectory|/directory/|local[-_]business|business[-_]listing|/listings?/|member[-_]directory|chamber)', re.I)


def own_domain(email, site, orgname, page_url=None):
    """True when the mailbox belongs to the organisation itself: same registrable domain as its website, a government domain,
    or a domain label containing a distinctive token of the organisation's name (e.g. edenwold-sk.ca for RM of Edenwold)."""
    ed = email.split('@')[1].lower()
    if site and regdom(ed) == regdom(urllib.parse.urlsplit(site).netloc):
        return True
    if page_url and regdom(ed) == regdom(urllib.parse.urlsplit(page_url).netloc):
        return True  # same domain as the organisation page it was published on (site moved to a new domain)
    if ed.endswith(('gc.ca', 'canada.ca', 'gouv.qc.ca', 'gov.uk', 'gov.au')):
        return True
    prov = PROV_OF.get(orgname, '')
    for suf, pj in (('gov.ab.ca', 'AB'), ('alberta.ca', 'AB'), ('gov.bc.ca', 'BC'), ('gov.sk.ca', 'SK'), ('gov.nl.ca', 'NL'), ('gov.nt.ca', 'NT'),
                    ('gov.ns.ca', 'NS'), ('novascotia.ca', 'NS'), ('gov.mb.ca', 'MB'), ('ontario.ca', 'ON'), ('gov.yk.ca', 'YT'), ('yukon.ca', 'YT'),
                    ('state.ma.us', 'MA'), ('texas.gov', 'TX'), ('virginia.gov', 'VA'), ('oregon.gov', 'OR'), ('ny.gov', 'NY'), ('vermont.gov', 'VT'),
                    ('alaska.gov', 'AK'), ('delaware.gov', 'DE')):
        if ed.endswith(suf):
            return prov == pj
    lab = regdom(ed).split('.')[0].replace('-', '')
    toks = [t for t in norm(orgname).split() if len(t) >= 5 and t not in GENERIC_TOK]
    return any(t in lab for t in toks)


def path_ok(site, page):
    s = urllib.parse.urlsplit(site); p = urllib.parse.urlsplit(page)
    if s.netloc.lower() not in SHARED_HOSTS:
        return True
    segs = [x for x in s.path.split('/') if x][:2]
    pre = '/' + '/'.join(segs)
    pre = re.sub(r'\.html$', '', pre)
    return p.netloc.lower() == s.netloc.lower() and p.path.startswith(pre)


def blank():
    return {'emails': [], 'phone': '', 'fax': '', 'mailing_address': '', 'invoice_portal': '', 'invoicing_requirements': '', 'instructions_url': '',
            'evidence_snippet': '', 'retrieved_at': '', 'evidence': []}


PROBE_CTX = {}
if os.path.exists(WORK + '/probe_log.jsonl'):
    for _l in open(WORK + '/probe_log.jsonl'):
        _p = json.loads(_l)
        for _e, _ctx in (_p.get('emails') or {}).items():
            if _ctx:
                PROBE_CTX.setdefault((_p['url'], _e), _ctx); PROBE_CTX.setdefault((_p.get('final_url'), _e), _ctx)
KEEP = set()
for _m in ([json.loads(l) for l in open(WORK + '/manual_ap.jsonl')] if os.path.exists(WORK + '/manual_ap.jsonl') else []):
    for _f in ('ap_emails', 'proc_emails', 'general_emails'):
        KEEP.update(e.lower() for e in _m.get(_f, []))
    KEEP.update(e.lower() for e in C.EMAIL_RE.findall(_m.get('invoicing_requirements', '') or ''))  # curated text: role mailboxes copied from the cited page


def redact(t):
    if not t:
        return t
    return C.EMAIL_RE.sub(lambda m: m.group(0) if (m.group(0).lower() in KEEP or C.localpart_class(m.group(0).lower(), '') is not None) else '[personal e-mail removed]', t)


stats = collections.Counter()
tmp = OUT + '.tmp'
fo = open(tmp, 'w')
for b in buyers:
    k = b['buyer_key']
    r = bulk.get(k, {})
    site = (r.get('official_website') or '').rstrip('/')
    cr = crawl.get(site)
    rec = {'buyer_key': k, 'name': b['name'], 'country': b['country'],
           'official_website': '', 'canonical_name': r.get('canonical_name', ''), 'organisation_type': r.get('organisation_type', '') or (b['types'][0]['value'] if b['types'] else ''),
           'identifiers': {}, 'address': r.get('address') or {}, 'ap_contact': blank(), 'procurement_contact': {'emails': [], 'phone': '', 'url': '', 'evidence': []},
           'general_contact': {'emails': [], 'phone': '', 'evidence': []}, 'extras': {}, 'notes': ''}
    notes = list(r.get('notes', []))
    # identifiers: directory first, then dataset-published ones
    rec['identifiers'].update(r.get('identifiers', {}))
    ds = {}
    for idk, vals in b['identifiers'].items():
        if idk in ('contracting_entity', 'ministers_office', 'contracting_entity_code', 'canadabuys_end_user_office'):
            continue
        ds[idk] = [v['value'] for v in vals][:5]
    if ds:
        rec['identifiers']['from_dataset'] = ds
    rec['extras']['directory_sources'] = r.get('sources', [])
    if r.get('parent'):
        rec['extras']['parent_organisation'] = {'name': r['parent']['name'], 'key': r['parent']['key'], 'jurisdiction': r['parent'].get('jurisdiction', ''),
                                                'basis': r['parent']['basis'], 'website': r.get('official_website', '')}
    if r.get('extras_dir'):
        rec['extras'].update(r['extras_dir'])
    if r.get('ambiguous_jurisdictions'):
        rec['extras']['jurisdiction_candidates'] = [{'jurisdiction': j, 'records_in_source_data': n} for j, n in sorted(r['ambiguous_jurisdictions'].items(), key=lambda t: -t[1])]
    rq = reqm.get(k)
    if rq:
        rec['extras']['quebec_req'] = dict(rq, source='Registraire des entreprises du Québec bulk extract (Données Québec JeuDonnees.zip, fetched 2026-10-25T18:56Z)',
                                           match_basis='exact normalized current name (incl. other names) == "%s"' % rq['name_matched'])
        if rq['match_confidence'] == 'exact':
            rec['identifiers']['neq'] = rq['records'][0]['neq']
            ra = rq['records'][0].get('address', '')
            if ra and not (rec['address'] and rec['address'].get('line1')):
                m = re.match(r'^(.*?),\s*([^,]+?)\s*\((?:Québec|QUÉBEC)\)(?:,\s*)?(?:,?\s*([A-Z]\d[A-Z]\s?\d[A-Z]\d))?', ra)
                if m:
                    rec['address'] = {'line1': m.group(1), 'city': m.group(2), 'region': 'QC', 'postal_code': (m.group(3) or '').replace(' ', ''),
                                      'country': 'CA', 'source': 'Registraire des entreprises du Québec (domicile), NEQ %s' % rq['records'][0]['neq']}
                else:
                    rec['address'] = {'line1': ra, 'city': '', 'region': 'QC', 'postal_code': '', 'country': 'CA',
                                      'source': 'Registraire des entreprises du Québec (domicile), NEQ %s' % rq['records'][0]['neq']}
        else:
            notes.append('REQ: %d entities share the name "%s" (not resolved)' % (len(rq['records']), rq['name_matched']))
    # address fallback: dataset address with most fields
    if not rec['address'] and b['addresses']:
        best = max(b['addresses'], key=lambda a: sum(1 for v in a['value'].values() if v))['value']
        if any(best.values()):
            rec['address'] = {'line1': best.get('line1') or best.get('streetAddress') or '', 'city': best.get('city') or best.get('locality') or '',
                              'region': best.get('region') or '', 'postal_code': best.get('postal_code') or best.get('postalCode') or '',
                              'country': best.get('country') or best.get('countryName') or b['country'], 'source': 'contract dataset (buyer address as published in notices)'}
    # general contact from directory
    gcd = r.get('general_contact') or {}
    def org_box(e):
        lp2 = re.sub(r'[^a-z]', '', unaccent(e.split('@')[0].lower()))
        key = re.sub(r'[^a-z]', '', unaccent((r.get('canonical_name') or b['name']).lower()))
        key2 = key.replace('sainte', 'ste').replace('saint', 'st')
        return lp2.startswith('mun') or (len(lp2) >= 4 and (lp2 in key or lp2 in key2))
    gem = [e.strip() for e in gcd.get('emails', []) if e and (C.localpart_class(e.strip().lower(), '') is not None or org_box(e.strip()))]
    if len(gem) < len(gcd.get('emails', [])):
        notes.append('directory e-mail withheld (looks like a personal mailbox)')
    if gem:
        rec['general_contact']['emails'] = gem
        rec['general_contact']['evidence'].append({'source': (r.get('sources') or [{}])[0].get('url', ''), 'note': 'directory listing'})
    rec['general_contact']['phone'] = gcd.get('phone', '')
    # dataset role mailboxes (published in notices), e.g. AusTender
    for c in b.get('contacts', []):
        v = c['value'] or {}
        for fld, val in v.items():
            if not isinstance(val, str):
                continue
            for e in C.EMAIL_RE.findall(val):
                cl = C.localpart_class(e.lower(), val)
                if cl and (r.get('official_website') or '') and not own_domain(e.lower(), r.get('official_website'), (r.get('canonical_name') or b['name'])):
                    stats['dropped_dataset_third_party'] += 1
                    continue
                if cl in ('procurement', 'general', 'ap'):
                    tgt = rec['procurement_contact']
                    if e.lower() not in tgt['emails']:
                        tgt['emails'].append(e.lower()); tgt['evidence'].append({'email': e.lower(), 'source': 'contract dataset contact field (%s)' % fld})
    # crawl
    if site:
        if cr and cr.get('status') == 'ok' or (cr and cr.get('pages')):
            rec['official_website'] = site
            rec['extras']['website_check'] = {'status': cr['status'], 'final_url': cr.get('final_url'), 'checked_at': cr.get('started_at'), 'pages_fetched': len(cr.get('pages', []))}
        elif cr:
            rec['official_website'] = site
            rec['extras']['website_check'] = {'status': cr['status'], 'errors': (cr.get('errors') or [])[:2], 'checked_at': cr.get('started_at')}
            notes.append('website not crawlable: %s' % cr['status'])
        else:
            rec['official_website'] = site
            rec['extras']['website_check'] = {'status': 'not_crawled (parent government portal; see parent_organisation and targeted sources)' if r.get('website_is_parent') else 'not_crawled_yet'}
    src0 = ' '.join(x.get('source', '') for x in (r.get('sources') or []))
    if site and cr and cr.get('status') in ('unreachable', 'http_404', 'http_410') and not cr.get('pages') and ('Wikidata' in src0 or 'alias rule' in src0) \
            and not r.get('website_is_parent'):
        rec['extras']['website_candidates'] = [{'url': site, 'source': 'Wikidata' if 'Wikidata' in src0 else 'alias rule', 'check': cr.get('status'), 'checked_at': cr.get('started_at')}]
        rec['official_website'] = ''
        notes = [n for n in notes if not n.startswith('website not crawlable')]
        notes.append('candidate website %s did not load (%s); not asserted as official website' % (site, cr.get('status')))
        cr = None
    if cr:
        host = urllib.parse.urlsplit(site).netloc.lower()
        for e in cr.get('emails', []):
            if not path_ok(site, e['page_url']):
                continue
            cl = C.localpart_class(e['email'], e['snippet'] + ' ' + e.get('page_title', '') + ' ' + e['page_url'])
            if cl is None:
                continue
            if DIRECTORY_PAGE.search(e['page_url']) or not own_domain(e['email'], site, (r.get('canonical_name') or b['name']), e['page_url']):
                stats['dropped_third_party_or_directory'] += 1
                continue
            snl = norm(e['snippet'])
            if cl in ('ap', 'ap_context') and 'receivable' in snl and 'payable' not in snl and not any(w in snl for w in ('invoice', 'supplier', 'vendor')):
                cl = 'general'
            pg = norm(e['page_url'] + ' ' + e.get('page_title', ''))
            ev = {'email': e['email'], 'page_url': e['page_url'], 'retrieved_at': e['retrieved_at'], 'snippet': fixmojibake(e['snippet'][:300])}
            same = regdom(e['email'].split('@')[1]) == regdom(host) or e['email'].split('@')[1].endswith(GOV_SUFFIX)
            lpe = e['email'].split('@')[0]
            if cl in ('general', 'ap_context') and re.match(r'(financ|tresor|comptab|compta|accounting|fin$|finance)', lpe):
                fr = rec['extras'].setdefault('finance_role_mailboxes', [])
                if e['email'] not in [x['email'] for x in fr] and len(fr) < 4:
                    fr.append(dict(ev, note='finance/treasury role mailbox published by the organisation; not explicitly designated for invoices'))
            if cl == 'ap' or (cl == 'ap_context' and any(w in pg for w in ['factur', 'invoice', 'payable', 'comptes a payer', 'paiement'])):
                if e['email'] not in rec['ap_contact']['emails']:
                    rec['ap_contact']['emails'].append(e['email']); rec['ap_contact']['evidence'].append(ev)
            elif cl == 'procurement':
                if e['email'] not in rec['procurement_contact']['emails']:
                    rec['procurement_contact']['emails'].append(e['email']); rec['procurement_contact']['evidence'].append(ev)
            else:
                if same and e['email'] not in rec['general_contact']['emails'] and len(rec['general_contact']['emails']) < 4:
                    rec['general_contact']['emails'].append(e['email']); rec['general_contact']['evidence'].append(ev)
        ap = rec['ap_contact']
        if ap['evidence']:
            ap['instructions_url'] = ap['evidence'][0]['page_url']; ap['retrieved_at'] = ap['evidence'][0]['retrieved_at']
            ap['evidence_snippet'] = ap['evidence'][0]['snippet']
        def snippet_ok(sn):
            pt = norm(sn['page_url'] + ' ' + sn.get('title', ''))
            tx = norm(sn['snippet'])
            if not any(w in pt for w in ['invoice', 'factur', 'payable', 'supplier', 'vendor', 'fournisseur', 'doing business', 'faire affaire', 'purchasing', 'procurement']):
                return False
            if any(w in pt for w in ['pay an invoice', 'invoice payment', 'online payment', 'pay online', 'property tax', 'water', 'parking', 'ar invoice',
                                      'receivable', 'food', 'real estate', 'land development', 'permit', 'manufactur', 'business count', 'miscellaneous']):
                return False
            return any(w in tx for w in ['supplier', 'vendor', 'fournisseur', 'contractor']) and any(w in tx for w in ['invoice', 'factur'])
        for s in cr.get('invoice_snippets', []):
            if path_ok(site, s['page_url']) and snippet_ok(s):
                ap['invoicing_requirements'] = ap['invoicing_requirements'] or ('[page excerpt] ' + fixmojibake(s['snippet'][:800]))
                ap['instructions_url'] = ap['instructions_url'] or s['page_url']
                ap['retrieved_at'] = ap['retrieved_at'] or cr.get('started_at')
                break
        for p in cr.get('portal_links', []):
            t = norm(p['anchor'] + ' ' + p['url'])
            if path_ok(site, p['page_url']) and any(w in t for w in ['fournisseur', 'supplier', 'vendor', 'factur', 'invoice']) and any(w in t for w in ['portail', 'portal', 'plateforme', 'platform', 'ariba', 'coupa', 'jaggaer', 'basware', 'tungsten', 'ipp gov', 'electronique', 'electronic']):
                if any(w in t for w in ['factur', 'invoice', 'ipp gov']):
                    if not ap['invoice_portal']:
                        ap['invoice_portal'] = p['url']; ap['portal_evidence'] = {'anchor': p['anchor'], 'found_on': p['page_url']}
                elif not rec['procurement_contact'].get('supplier_portal'):
                    rec['procurement_contact']['supplier_portal'] = p['url']
                    rec['procurement_contact']['supplier_portal_evidence'] = {'anchor': p['anchor'], 'found_on': p['page_url']}
        for pgx in cr.get('pages', []):
            t = norm(pgx['url'] + ' ' + pgx.get('title', ''))
            if any(w in t for w in ['approvisionnement', 'procurement', 'appels d offres', 'appel d offres', 'fournisseur', 'supplier', 'purchasing', 'achats', 'doing business', 'faire affaire']) and path_ok(site, pgx['url']):
                rec['procurement_contact']['url'] = rec['procurement_contact']['url'] or pgx['url']
    # targeted findings
    for m in manual:
        mt = m['match']; hit = False
        if 'owner_org' in mt and rec['identifiers'].get('owner_org') == mt['owner_org']:
            hit = True
        if 'mamh_municipal_code' in mt and rec['identifiers'].get('mamh_municipal_code') == mt['mamh_municipal_code']:
            hit = True
        if 'canonical_name' in mt and rec['canonical_name'] == mt['canonical_name']:
            hit = True
        if 'website_host' in mt and site and urllib.parse.urlsplit(site).netloc.lower().replace('www.', '') == mt['website_host'].replace('www.', ''):
            hit = True
        if 'buyer_keys' in mt and k in mt['buyer_keys']:
            hit = True
        if 'parent_key' in mt and (r.get('parent') or {}).get('key') == mt['parent_key']:
            hit = True
        if 'name_regex' in mt and re.search(mt['name_regex'], norm(b['name'])) and b['country'] == mt.get('country', b['country']):
            hit = True
        if not hit:
            continue
        ap = rec['ap_contact']
        for e in reversed(m.get('ap_emails', [])):
            if e.lower() in ap['emails']:
                ap['emails'].remove(e.lower())
            ap['emails'].insert(0, e.lower())
            ap['evidence'].insert(0, {'email': e.lower(), 'page_url': m['url'], 'retrieved_at': m['retrieved_at'],
                                      'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e.lower())) or m.get('evidence_snippet') or '(targeted search)')[:400]})
        if (m.get('ap_emails') or m.get('invoicing_requirements') or m.get('invoice_portal')) and not ap.get('_manual'):
            ap['instructions_url'] = m['url']; ap['retrieved_at'] = m['retrieved_at']
            ap['evidence_snippet'] = m.get('evidence_snippet') or ap['evidence_snippet']
            if m.get('invoicing_requirements'):
                ap['invoicing_requirements'] = m['invoicing_requirements']
            ap['_manual'] = True
        elif m.get('invoicing_requirements') and ap.get('_manual'):
            ap['invoicing_requirements'] += ' | ' + m['invoicing_requirements']
        for f in ('invoice_portal', 'mailing_address', 'phone', 'fax'):
            if m.get(f):
                ap[f] = m[f]
        for e in reversed(m.get('proc_emails', [])):
            if e.lower() not in rec['procurement_contact']['emails']:
                rec['procurement_contact']['emails'].insert(0, e.lower())
                rec['procurement_contact']['evidence'].insert(0, {'email': e.lower(), 'page_url': m['url'], 'retrieved_at': m['retrieved_at'],
                                                                  'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e.lower())) or '')[:400]})
        if m.get('proc_url'):
            rec['procurement_contact']['url'] = m['proc_url']
        for e in reversed(m.get('general_emails', [])):
            if e.lower() not in rec['general_contact']['emails']:
                rec['general_contact']['emails'].insert(0, e.lower())
                rec['general_contact']['evidence'].insert(0, {'email': e.lower(), 'page_url': m['url'], 'retrieved_at': m['retrieved_at'],
                                                               'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e.lower())) or '')[:400]})
        if m.get('official_website') and not rec['official_website']:
            rec['official_website'] = m['official_website']
        if m.get('notes'):
            notes.append(m['notes'])
        rec['extras'].setdefault('targeted_sources', []).append(m['url'])
    for jc in rec['extras'].get('jurisdiction_candidates', []):
        for m in manual:
            if m['match'].get('parent_key') == 'gov_' + jc['jurisdiction']:
                jc.setdefault('government', m['match']['parent_key'])
                jc.setdefault('ap_emails', []).extend(e for e in m.get('ap_emails', []) if e not in jc.get('ap_emails', []))
                jc['instructions_url'] = m['url']; jc['retrieved_at'] = m['retrieved_at']
                if m.get('invoicing_requirements'):
                    jc['invoicing_requirements'] = m['invoicing_requirements'][:600]
    # final personal-mailbox guard: <name>.<short role token> where <name> is not part of the organisation's name
    okey = re.sub(r'[^a-z]', '', unaccent((rec['canonical_name'] or b['name']).lower()))
    okey2 = okey.replace('sainte', 'ste').replace('saint', 'st')
    def personal_like(e):
        toks = [t for t in re.split(r'[._\-]', e.split('@')[0].lower()) if t]
        if len(toks) == 2:
            for i in (0, 1):
                a1, a2 = toks[i], toks[1 - i]
                if a2 in ('dg', 'dga', 'adj', 'sec', 'dir') and a1.isalpha() and len(a1) >= 4 and a1 not in okey and a1 not in okey2 \
                        and not any(a1.startswith(st) for st in C.STEMS):
                    return True
        return False
    for fld in ('procurement_contact', 'general_contact'):
        bad = [e for e in rec[fld]['emails'] if personal_like(e)]
        if bad:
            rec[fld]['emails'] = [e for e in rec[fld]['emails'] if e not in bad]
            rec[fld]['evidence'] = [ev for ev in rec[fld]['evidence'] if ev.get('email') not in bad]
    for fld in ('ap_contact', 'procurement_contact', 'general_contact'):
        for ev in rec[fld].get('evidence', []):
            if ev.get('snippet'):
                ev['snippet'] = redact(ev['snippet'])
    rec['ap_contact']['evidence_snippet'] = redact(rec['ap_contact']['evidence_snippet'])
    rec['ap_contact']['invoicing_requirements'] = redact(rec['ap_contact']['invoicing_requirements'])
    for ev in rec['extras'].get('finance_role_mailboxes', []):
        ev['snippet'] = redact(ev.get('snippet', ''))
    rec['ap_contact'].pop('_manual', None)
    if not rec['official_website'] and not r.get('ambiguous_jurisdictions'):
        notes.append('no directory match; website not identified')
    rec['notes'] = '; '.join(dict.fromkeys(notes))
    for fld, cond in [('website', rec['official_website']), ('ap_email', rec['ap_contact']['emails']), ('invoice_portal', rec['ap_contact']['invoice_portal']),
                      ('invoicing_requirements', rec['ap_contact']['invoicing_requirements']), ('procurement_email', rec['procurement_contact']['emails']),
                      ('procurement_url', rec['procurement_contact']['url']), ('general_email', rec['general_contact']['emails']), ('address', rec['address'].get('line1') if rec['address'] else ''),
                      ('identifiers_directory', any(x != 'from_dataset' for x in rec['identifiers'])), ('neq', rec['identifiers'].get('neq'))]:
        if cond:
            stats[fld] += 1
            if b['record_count_high_or_medium'] > 0:
                stats['hm_' + fld] += 1
    fo.write(json.dumps(rec, ensure_ascii=False) + '\n')
fo.close()
os.replace(tmp, OUT)
json.dump(dict(stats), open(WORK + '/assemble_stats.json', 'w'), indent=1)
print(dict(sorted(stats.items())))

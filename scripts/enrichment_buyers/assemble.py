"""Stage 3: merge bulk/alias directory data + crawl results + targeted findings into enrichment/buyers_enriched.jsonl (atomic rewrite)."""
import sys, os, json, re, glob, collections, urllib.parse, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

OUT = BASE + '/enrichment/buyers_enriched.jsonl'
buyers = load_buyers()
bulk = json.load(open(WORK + '/bulk.json'))
crawl = {}
for f in sorted(glob.glob(WORK + '/crawl*.jsonl')) + sorted(glob.glob(WORK + '/deep*.jsonl')):
    if 'test' in f:
        continue
    for l in open(f):
        try:
            r = json.loads(l)
        except Exception:
            continue
        key = r['site'].rstrip('/')
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
SHARED_HOSTS = {'www.canada.ca', 'www.quebec.ca', 'canada.ca', 'www.gov.uk'}
GOV_SUFFIX = ('gc.ca', 'canada.ca', 'gouv.qc.ca', 'gov', 'gov.uk', 'gov.au', 'quebec')
APKW = ['factur', 'invoice', 'payable', 'fournisseur', 'supplier', 'vendor', 'comptes', 'paiement', 'payment', 'affaire', 'business']


def regdom(h):
    h = h.lower().split(':')[0]
    p = h.split('.')
    if len(p) >= 3 and p[-1] == 'ca' and p[-2] in ('qc', 'on', 'gc', 'gouv'):
        return '.'.join(p[-3:]) if p[-2] != 'gouv' else '.'.join(p[-4:])
    return '.'.join(p[-2:])


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


def redact(t):
    if not t:
        return t
    return C.EMAIL_RE.sub(lambda m: m.group(0) if C.localpart_class(m.group(0).lower(), '') is not None else '[personal e-mail removed]', t)


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
            rec['extras']['website_check'] = {'status': 'not_crawled_yet'}
    if cr:
        host = urllib.parse.urlsplit(site).netloc.lower()
        for e in cr.get('emails', []):
            if not path_ok(site, e['page_url']):
                continue
            cl = C.localpart_class(e['email'], e['snippet'] + ' ' + e.get('page_title', '') + ' ' + e['page_url'])
            if cl is None:
                continue
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
        for s in cr.get('invoice_snippets', []):
            if path_ok(site, s['page_url']):
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
        if 'name_regex' in mt and re.search(mt['name_regex'], norm(b['name'])) and b['country'] == mt.get('country', b['country']):
            hit = True
        if not hit:
            continue
        ap = rec['ap_contact']
        for e in m.get('ap_emails', []):
            if e.lower() not in ap['emails']:
                ap['emails'].insert(0, e.lower())
            ap['evidence'].insert(0, {'email': e.lower(), 'page_url': m['url'], 'retrieved_at': m['retrieved_at'], 'snippet': '(targeted search)'})
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
        for e in m.get('proc_emails', []):
            if e.lower() not in rec['procurement_contact']['emails']:
                rec['procurement_contact']['emails'].insert(0, e.lower())
                rec['procurement_contact']['evidence'].insert(0, {'email': e.lower(), 'page_url': m['url'], 'retrieved_at': m['retrieved_at']})
        if m.get('proc_url'):
            rec['procurement_contact']['url'] = m['proc_url']
        for e in m.get('general_emails', []):
            if e.lower() not in rec['general_contact']['emails']:
                rec['general_contact']['emails'].insert(0, e.lower())
        if m.get('official_website') and not rec['official_website']:
            rec['official_website'] = m['official_website']
        if m.get('notes'):
            notes.append(m['notes'])
        rec['extras'].setdefault('targeted_sources', []).append(m['url'])
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
    if not r and not rec['official_website']:
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

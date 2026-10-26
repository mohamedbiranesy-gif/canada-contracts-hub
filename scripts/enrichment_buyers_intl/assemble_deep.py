"""W3 deep pass — assemble enrichment/v2/buyers_deep.jsonl (atomic rewrite).
One line per buyer_key with something new:
  * ap_deep buyers: the FULL merged record = previous record (buyers_enriched.jsonl / buyers_enriched_v2.jsonl, which holds the `_known` facts) + new
    findings of this pass (deep2/deep3 crawler results, targeted findings in WORK/manual_ap.jsonl, parent-organisation inheritance);
  * full_enrichment_new_buyer buyers: a full record built in WORK/new_buyers.json (+ crawl/targeted findings), always written.
Findings are applied per ORGANISATION (WORK/groups.json: spelling variants / sub-units of one organisation share one group), so one finding
fills every key of the group. extras.deep_pass lists what this pass added and from where."""
import sys, os, json, re, glob, copy, collections, urllib.parse, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.argv = [sys.argv[0], '/dev/null', '/dev/null']
spec = importlib.util.spec_from_file_location('crawlmod', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawl.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)

RUN = 'buyers_deep (W3) 2026-10-26'
buyers = load_buyers()
prev = {}
for f in PREV_ENRICHED:
    for l in open(f):
        r = json.loads(l); prev[r['buyer_key']] = r
G = json.load(open(WORK + '/groups.json'))
key2g = {}
for g in G:
    for k in g['keys']:
        key2g[k] = g
NEWB = json.load(open(WORK + '/new_buyers.json')) if os.path.exists(WORK + '/new_buyers.json') else {}
manual = [json.loads(l) for l in open(WORK + '/manual_ap.jsonl')] if os.path.exists(WORK + '/manual_ap.jsonl') else []
PROBE_CTX = {}
if os.path.exists(WORK + '/probe_log.jsonl'):
    for _l in open(WORK + '/probe_log.jsonl'):
        _p = json.loads(_l)
        for _e, _ctx in (_p.get('emails') or {}).items():
            if _ctx:
                PROBE_CTX.setdefault((_p['url'], _e), _ctx); PROBE_CTX.setdefault((_p.get('final_url'), _e), _ctx)

# ---------- crawl results of this pass ----------
crawl_by_key = collections.defaultdict(list)
crawl_status = {}
for f in sorted(glob.glob(WORK + '/deep*.jsonl')) + sorted(glob.glob(WORK + '/crawl*.jsonl')):
    for l in open(f):
        try:
            r = json.loads(l)
        except Exception:
            continue
        r['_file'] = os.path.basename(f)
        crawl_status.setdefault(r['site'], []).append((r.get('mode', os.path.basename(f)), r.get('status'), len(r.get('pages', []))))
        for k in r.get('buyer_keys', []):
            crawl_by_key[k].append(r)

MOVED = {}
if os.path.exists(WORK + '/sites_deep3m2.json'):
    for _s in json.load(open(WORK + '/sites_deep3m2.json')):
        MOVED[_s['site']] = _s['moved_from']
SHARED_HOSTS = {'www.canada.ca', 'www.quebec.ca', 'canada.ca', 'www.gov.uk', 'www.oregon.gov', 'oregon.gov', 'www.gov.mb.ca', 'www2.gov.bc.ca', 'www.alberta.ca',
                'novascotia.ca', 'www.saskatchewan.ca', 'www.gov.nl.ca', 'www.ontario.ca', 'www.mass.gov', 'www.nyc.gov'}
GOV_SUFFIX = ('gc.ca', 'canada.ca', 'gouv.qc.ca', 'gov', 'gov.uk', 'gov.au', 'quebec')
GENERIC_TOK = {'county', 'town', 'city', 'municipality', 'district', 'region', 'regional', 'township', 'village', 'school', 'board', 'catholic',
               'public', 'services', 'service', 'university', 'college', 'division', 'corporation', 'authority', 'rural', 'health', 'alberta',
               'ontario', 'national', 'canada', 'north', 'south', 'east', 'west', 'government', 'department', 'ministry', 'separate', 'roman',
               'commission', 'housing', 'foundation', 'saint', 'sainte', 'greater', 'united', 'counties', 'centre', 'center', 'quebec', 'montreal',
               'sante', 'services', 'sociaux', 'integre', 'universitaire', 'scolaire', 'ville', 'municipalite', 'societe', 'transport', 'reseau'}
DIRECTORY_PAGE = re.compile(r'(business[-_ ]?directory|businessdirectory|/directory/|local[-_]business|business[-_]listing|/listings?/|member[-_]directory|chamber|bottin)', re.I)
RECEIVABLE = ('recevoir', 'recevable', 'receivable', 'client', 'debiteur', 'billing', 'taxation', 'perception', 'customer', 'collection', 'revenu', 'revenue',
              'utility', 'utilities', 'water', 'taxes', 'cashmgmt', 'cash')


def regdom(h):
    h = h.lower().split(':')[0]
    p = h.split('.')
    if len(p) >= 3 and p[-1] == 'ca' and p[-2] in ('qc', 'on', 'gc', 'gouv', 'ns', 'nb', 'ab', 'bc', 'mb', 'sk', 'nl', 'pe'):
        return '.'.join(p[-3:]) if p[-2] != 'gouv' else '.'.join(p[-4:])
    return '.'.join(p[-2:])


def prov_of(rec, b):
    a = rec.get('address') or {}
    pr = (a.get('region') or '').upper()
    if not pr:
        pr = ((rec.get('extras') or {}).get('parent_organisation') or {}).get('jurisdiction', '')
    return pr


def own_domain(email, site, orgname, prov, page_url=None):
    ed = email.split('@')[1].lower()
    if site and regdom(ed) == regdom(urllib.parse.urlsplit(site).netloc):
        return True
    if page_url and regdom(ed) == regdom(urllib.parse.urlsplit(page_url).netloc) and urllib.parse.urlsplit(page_url).netloc.lower() not in SHARED_HOSTS:
        return True
    if ed.endswith(('gc.ca', 'canada.ca', 'gov.uk', 'gov.au')):
        return True
    if ed.endswith(('gouv.qc.ca', '.quebec')):
        return prov in ('QC', '')
    for suf, pj in (('gov.ab.ca', 'AB'), ('alberta.ca', 'AB'), ('gov.bc.ca', 'BC'), ('gov.sk.ca', 'SK'), ('gov.nl.ca', 'NL'), ('gov.nt.ca', 'NT'),
                    ('gov.ns.ca', 'NS'), ('novascotia.ca', 'NS'), ('gov.mb.ca', 'MB'), ('ontario.ca', 'ON'), ('gov.yk.ca', 'YT'), ('yukon.ca', 'YT'),
                    ('gnb.ca', 'NB'), ('gov.pe.ca', 'PE'), ('state.ma.us', 'MA'), ('texas.gov', 'TX'), ('virginia.gov', 'VA')):
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
    pre = re.sub(r'\.html$', '', '/' + '/'.join(segs))
    return p.netloc.lower() == s.netloc.lower() and p.path.startswith(pre)


def ap_class(e, snippet, page_url, title):
    """precision-first classification of a crawled mailbox: ap | procurement | general | None"""
    cl = C.localpart_class(e, snippet + ' ' + title + ' ' + page_url)
    if cl is None:
        return None
    lp = e.split('@')[0].lower()
    lpn = re.sub(r'[^a-z]', '', unaccent(lp))
    if any(x in lpn for x in RECEIVABLE):
        return 'general'
    snl = norm(snippet)
    pg = norm(page_url + ' ' + title)
    if re.search(r'(crediteur|creditor)', lpn):  # "comptes créditeurs" = accounts payable (Canadian federal French usage)
        return 'ap'
    if cl in ('general', 'ap_context') and re.match(r'(financ|comptab|compta|tresor|accounting|fin$)', lpn) and \
            any(w in pg for w in ['payments vendors', 'vendor payments', 'payment vendors', 'supplier payments', 'paiements fournisseurs', 'paiement des fournisseurs',
                                  'paiement fournisseurs', 'accounts payable', 'comptes a payer', 'comptes payables', 'comptes fournisseurs']):
        return 'ap'
    if cl in ('ap', 'ap_context') and 'receivable' in snl and 'payable' not in snl and not any(w in snl for w in ('invoice', 'supplier', 'vendor', 'fournisseur', 'factur')):
        return 'general'
    if cl == 'ap':
        strong = re.search(r'(factur|invoice|payable|payables|comptes?a?payer|cptespay|comptespay|apinv|accountspay|acctspay|acctpay|^ap$|^cp$|^cap$|(^|[._-])(ap|cp)([._-]|$))', lp)
        if not strong:  # signal only from payment/paiement/billing tokens -> require supplier context
            if not any(w in snl + ' ' + pg for w in ('supplier', 'vendor', 'fournisseur', 'factur', 'invoice', 'payable', 'comptes a payer')):
                return 'general'
        return 'ap'
    if cl == 'ap_context':
        if any(w in pg for w in ['factur', 'invoice', 'payable', 'comptes a payer', 'comptes payables', 'comptes fournisseurs', 'paiement des fournisseurs',
                                 'depot direct', 'direct deposit', 'supplier payment', 'vendor payment']) or \
                any(w in snl for w in ['transmettre vos factures', 'transmettre les factures', 'send invoices', 'submit invoices', 'invoices should be', 'invoices must be',
                                       'factures doivent', 'factures a l adresse', 'invoices to', 'factures par courriel', 'facture par courriel', 'invoice to']):
            return 'ap'
        return 'general'
    return cl


def blank_ap():
    return {'emails': [], 'phone': '', 'fax': '', 'mailing_address': '', 'invoice_portal': '', 'invoicing_requirements': '', 'instructions_url': '',
            'evidence_snippet': '', 'retrieved_at': '', 'evidence': []}


KEEP = set()
for _m in manual:
    for _f in ('ap_emails', 'proc_emails', 'general_emails'):
        KEEP.update(e.lower() for e in _m.get(_f, []))
    KEEP.update(e.lower() for e in C.EMAIL_RE.findall(_m.get('invoicing_requirements', '') or ''))


def redact(t):
    if not t:
        return t
    return C.EMAIL_RE.sub(lambda m: m.group(0) if (m.group(0).lower() in KEEP or C.localpart_class(m.group(0).lower(), '') is not None) else '[personal e-mail removed]', t)


def snippet_ok(sn):
    pt = norm(sn['page_url'] + ' ' + sn.get('title', ''))
    tx = norm(sn['snippet'])
    if not any(w in pt for w in ['invoice', 'factur', 'payable', 'supplier', 'vendor', 'fournisseur', 'doing business', 'faire affaire', 'purchasing',
                                 'procurement', 'approvisionnement', 'conditions', 'terms', 'bon de commande', 'purchase order', 'comptes']):
        return False
    if any(w in pt for w in ['pay an invoice', 'invoice payment', 'online payment', 'pay online', 'property tax', 'water', 'parking', 'ar invoice', 'receivable',
                             'food', 'real estate', 'land development', 'permit', 'manufactur', 'business count', 'miscellaneous', 'taxe', 'compte de taxes', 'usager',
                             'frais d hospitalisation', 'hydro jonquiere', 'electricite']):
        return False
    return any(w in tx for w in ['supplier', 'vendor', 'fournisseur', 'contractor', 'entrepreneur', 'adjudicataire', 'prestataire']) and any(w in tx for w in ['invoice', 'factur'])


def group_findings(g, orgname, site, prov):
    """findings of this pass' crawler for the organisation (all sites crawled for any key of the group)"""
    out = {'ap': [], 'proc': [], 'gen': [], 'fin': [], 'snip': None, 'portal': None, 'supplier_portal': None, 'phone': None, 'proc_url': '', 'sites': set()}
    seen = set()
    rs = []
    for k in g['keys']:
        rs.extend(crawl_by_key.get(k, []))
    for r in rs:
        csite = r['site']
        out['sites'].add(csite)
        for e in r.get('emails', []):
            if (e['email'], e['page_url']) in seen:
                continue
            seen.add((e['email'], e['page_url']))
            if not path_ok(csite, e['page_url']) or DIRECTORY_PAGE.search(e['page_url']):
                continue
            cl = ap_class(e['email'], e.get('snippet', ''), e['page_url'], e.get('page_title', ''))
            if cl is None:
                continue
            dnote = ''
            if not own_domain(e['email'], site or csite, orgname, prov, e['page_url']):
                # exception: an invoice mailbox on another domain (legacy domain of the organisation, or an e-invoicing capture service such as
                # Basware / Concur) that the organisation itself publishes on its own invoicing page
                ph = urllib.parse.urlsplit(e['page_url']).netloc.lower()
                own_page = any(regdom(ph) == regdom(urllib.parse.urlsplit(x).netloc) for x in (site, csite) if x)
                inv_page = re.search(r'(factur|invoice|payable|comptes?[ -]a[ -]payer|accounts payable)', norm(e['page_url'] + ' ' + e.get('page_title', '') + ' ' + e.get('snippet', '')))
                if cl == 'ap' and own_page and inv_page:
                    dnote = 'mailbox domain differs from the organisation website; published by the organisation on its own invoicing page'
                else:
                    continue
            ev = {'email': e['email'], 'page_url': e['page_url'], 'retrieved_at': e['retrieved_at'], 'snippet': fixmojibake(e.get('snippet', '')[:300]),
                  'source': 'crawler (%s)' % r.get('mode', r['_file'])}
            if dnote:
                ev['note'] = dnote
            lpe = e['email'].split('@')[0]
            if cl == 'ap':
                out['ap'].append(ev)
            elif cl == 'procurement':
                out['proc'].append(ev)
            else:
                if re.match(r'(financ|tresor|comptab|compta|accounting|fin$)', lpe):
                    out['fin'].append(ev)
                ed = e['email'].split('@')[1]
                if regdom(ed) == regdom(urllib.parse.urlsplit(site or csite).netloc) or ed.endswith(GOV_SUFFIX):
                    out['gen'].append(ev)
        if not out['snip']:
            for s in r.get('invoice_snippets', []):
                if path_ok(csite, s['page_url']) and snippet_ok(s):
                    out['snip'] = dict(s, retrieved_at=r.get('started_at')); break
        for p in r.get('portal_links', []):
            t = norm(p['anchor'] + ' ' + p['url'])
            if path_ok(csite, p['page_url']) and any(w in t for w in ['fournisseur', 'supplier', 'vendor', 'factur', 'invoice']) and \
                    any(w in t for w in ['portail', 'portal', 'plateforme', 'platform', 'ariba', 'coupa', 'jaggaer', 'basware', 'tungsten', 'ipp gov', 'electronique', 'electronic']):
                if any(w in t for w in ['factur', 'invoice', 'ipp gov']):
                    out['portal'] = out['portal'] or {'url': p['url'], 'anchor': p['anchor'], 'found_on': p['page_url']}
                else:
                    out['supplier_portal'] = out['supplier_portal'] or {'url': p['url'], 'anchor': p['anchor'], 'found_on': p['page_url']}
        for ph in r.get('ap_phone_snippets', []):
            if not out['phone'] and path_ok(csite, ph['page_url']):
                sn = norm(ph['snippet'])
                if not any(w in sn for w in ('receivable', 'recevoir', 'recevable', 'taxe', 'tax ', 'client')):
                    out['phone'] = dict(ph, retrieved_at=r.get('started_at'))
        for pgx in r.get('pages', []):
            t = norm(pgx['url'] + ' ' + pgx.get('title', ''))
            if any(w in t for w in ['approvisionnement', 'procurement', 'appels d offres', 'appel d offres', 'fournisseur', 'supplier', 'purchasing', 'achats',
                                    'doing business', 'faire affaire']) and path_ok(csite, pgx['url']) and not out['proc_url']:
                out['proc_url'] = pgx['url']
    return out


def manual_hits(rec, b, g):
    k = b['buyer_key']
    site = rec.get('official_website') or ''
    for m in manual:
        mt = m['match']; hit = False
        gids = set(g.get('member_gids') or [g['gid']]) | {g['gid']} if g else set()
        if 'group' in mt and mt['group'] in gids:
            hit = True
        if 'groups' in mt and gids & set(mt['groups']):
            hit = True
        if 'buyer_keys' in mt and k in mt['buyer_keys']:
            hit = True
        if 'canonical_name' in mt and rec.get('canonical_name') == mt['canonical_name']:
            hit = True
        if 'website_host' in mt and site and urllib.parse.urlsplit(site).netloc.lower().replace('www.', '') == mt['website_host'].replace('www.', ''):
            hit = True
        if 'parent_key' in mt and ((rec.get('extras') or {}).get('parent_organisation') or {}).get('key') == mt['parent_key']:
            hit = True
        if 'name_regex' in mt and (re.search(mt['name_regex'], norm(b['name'])) or re.search(mt['name_regex'], norm(rec.get('canonical_name') or ''))) \
                and b['country'] == mt.get('country', b['country']):
            hit = True
        if 'exclude_regex' in mt and re.search(mt['exclude_regex'], norm(b['name'])):
            hit = False
        if hit:
            yield m


def build_new(b):
    nb = NEWB.get(b['buyer_key'], {})
    rec = {'buyer_key': b['buyer_key'], 'name': b['name'], 'country': nb.get('country') or b['country'],
           'official_website': nb.get('official_website', ''), 'canonical_name': nb.get('canonical_name', '') or b['name'],
           'organisation_type': nb.get('organisation_type') or (b['types'][0]['value'] if b['types'] else ''),
           'identifiers': dict(nb.get('identifiers', {})), 'address': nb.get('address') or {}, 'ap_contact': blank_ap(),
           'procurement_contact': {'emails': [], 'phone': '', 'url': '', 'evidence': []}, 'general_contact': {'emails': [], 'phone': '', 'evidence': []},
           'extras': dict(nb.get('extras', {})), 'notes': ''}
    for fld in ('ap_contact', 'procurement_contact', 'general_contact'):
        if nb.get(fld):
            rec[fld] = copy.deepcopy(nb[fld])
            for kk, vv in (blank_ap() if fld == 'ap_contact' else {'emails': [], 'evidence': []}).items():
                rec[fld].setdefault(kk, vv)
    ds = {}
    for idk, vals in b['identifiers'].items():
        ds[idk] = [v['value'] for v in vals][:5]
    if ds:
        rec['identifiers']['from_dataset'] = ds
    if not rec['address'] and b['addresses']:
        best = max(b['addresses'], key=lambda a: sum(1 for v in a['value'].values() if v))['value']
        if best.get('location_as_published'):
            parts = [x.strip() for x in best['location_as_published'].split(',')]
            reg = next((p for p in parts if re.fullmatch(r'[A-Z]{2}', p)), '')
            rec['address'] = {'line1': '', 'city': parts[0] if len(parts) >= 3 else '', 'region': reg, 'postal_code': '', 'country': 'CA' if 'CAN' in parts or 'Canada' in parts else b['country'],
                              'location_as_published': best['location_as_published'], 'source': 'contract dataset (buyer location as published in the notice)'}
        elif any(best.values()):
            rec['address'] = {'line1': best.get('line1') or '', 'city': best.get('city') or '', 'region': best.get('region') or '', 'postal_code': best.get('postal_code') or '',
                              'country': best.get('country') or b['country'], 'source': 'contract dataset (buyer address as published in notices)'}
    rec['_notes'] = list(nb.get('notes', []))
    return rec


stats = collections.Counter()
gstats = collections.Counter()
tmp = OUT_ENRICHED + '.tmp'
fo = open(tmp, 'w')
GF = {}
for b in buyers:
    k = b['buyer_key']
    g = key2g.get(k)
    is_new = b['_task'] == 'full_enrichment_new_buyer'
    if is_new:
        rec = build_new(b)
        notes = rec.pop('_notes')
    else:
        rec = copy.deepcopy(prev[k])
        notes = [n for n in (rec.get('notes') or '').split('; ') if n]
    for fld in ('ap_contact',):
        for kk, vv in blank_ap().items():
            rec[fld].setdefault(kk, vv)
    rec['procurement_contact'].setdefault('evidence', []); rec['general_contact'].setdefault('evidence', [])
    new_fields = []
    srcs = []
    before = json.dumps({x: rec.get(x) for x in ('official_website', 'ap_contact', 'procurement_contact', 'general_contact', 'address', 'identifiers')}, sort_keys=True)
    ap = rec['ap_contact']
    site = rec.get('official_website') or ''
    orgname = rec.get('canonical_name') or b['name']
    prov = prov_of(rec, b)
    # ---- organisation site moved to a new hostname (old site redirects there; observed by deep3, re-crawled in deep3m)
    if site and g:
        oh = urllib.parse.urlsplit(site if site.startswith('http') else 'https://' + site).netloc.lower()
        for r in crawl_by_key.get(k, []):
            mf = MOVED.get(r['site'])
            if mf and mf.lower() == oh and r.get('pages'):
                rec['extras']['website_moved'] = {'from': site, 'to': r['site'].rstrip('/'), 'observed_at': r.get('started_at'), 'basis': 'HTTP redirect of the former homepage'}
                rec['official_website'] = r['site'].rstrip('/'); site = rec['official_website']
                new_fields.append('official_website'); srcs.append(r['site'])
                break
    # ---- website for organisations that had none: knowledge-based candidate (site_alias_candidates.json) asserted only when this pass
    #      fetched its homepage (HTTP 200) and the page title or domain carries a distinctive token of the organisation's name
    if not site and g:
        for r in crawl_by_key.get(k, []):
            if r.get('mode') != 'deep3' or not r.get('pages'):
                continue
            home = r['pages'][0]
            toks = [t for t in norm(orgname).split() if len(t) >= 4 and t not in GENERIC_TOK and t not in ('cegep', 'college', 'du', 'de', 'la', 'des')]
            ttl = norm(home.get('title', '')); dom = urllib.parse.urlsplit(r['site']).netloc.lower().replace('-', '')
            if home.get('status') == 200 and (any(t in ttl for t in toks) or any(t[:6] in dom for t in toks)):
                rec['official_website'] = r['site'].rstrip('/'); site = rec['official_website']
                rec['extras'].setdefault('directory_sources', []).append({'source': 'site alias (well-known official domain, scripts/enrichment_buyers_deep site_alias_candidates.json) verified by homepage fetch',
                                                                         'url': home['url'], 'retrieved_at': home.get('retrieved_at'), 'match_basis': 'homepage title "%s"' % home.get('title', '')[:120],
                                                                         'match_confidence': 'strong'})
                rec['extras']['website_check'] = {'status': r.get('status'), 'checked_at': r.get('started_at'), 'pages_fetched': len(r.get('pages', []))}
                new_fields.append('official_website'); srcs.append(home['url'])
                notes = [n for n in notes if 'website not identified' not in n]
                break
    # ---- crawler findings (group level)
    if g:
        if g['gid'] not in GF:
            GF[g['gid']] = group_findings(g, orgname, site, prov)
        F = GF[g['gid']]
        for ev in F['ap']:
            if ev['email'] not in ap['emails']:
                ap['emails'].append(ev['email']); ap['evidence'].append(ev); new_fields.append('ap_contact.emails'); srcs.append(ev['page_url'])
        for ev in F['proc']:
            if ev['email'] not in rec['procurement_contact']['emails']:
                rec['procurement_contact']['emails'].append(ev['email']); rec['procurement_contact']['evidence'].append(ev); new_fields.append('procurement_contact.emails'); srcs.append(ev['page_url'])
        for ev in F['gen']:
            if ev['email'] not in rec['general_contact']['emails'] and len(rec['general_contact']['emails']) < 4:
                rec['general_contact']['emails'].append(ev['email']); rec['general_contact']['evidence'].append(ev); new_fields.append('general_contact.emails'); srcs.append(ev['page_url'])
        for ev in F['fin']:
            fr = rec['extras'].setdefault('finance_role_mailboxes', [])
            if ev['email'] not in [x['email'] for x in fr] and len(fr) < 4:
                fr.append(dict(ev, note='finance/treasury role mailbox published by the organisation; not explicitly designated for invoices'))
                new_fields.append('extras.finance_role_mailboxes')
        if F['snip'] and not ap['invoicing_requirements']:
            ap['invoicing_requirements'] = '[page excerpt] ' + fixmojibake(F['snip']['snippet'][:800])
            ap['instructions_url'] = ap['instructions_url'] or F['snip']['page_url']; ap['retrieved_at'] = ap['retrieved_at'] or F['snip'].get('retrieved_at') or ''
            new_fields.append('ap_contact.invoicing_requirements'); srcs.append(F['snip']['page_url'])
        if F['portal'] and not ap['invoice_portal']:
            ap['invoice_portal'] = F['portal']['url']; ap['portal_evidence'] = {'anchor': F['portal']['anchor'], 'found_on': F['portal']['found_on']}
            new_fields.append('ap_contact.invoice_portal'); srcs.append(F['portal']['found_on'])
        if F['supplier_portal'] and not rec['procurement_contact'].get('supplier_portal'):
            rec['procurement_contact']['supplier_portal'] = F['supplier_portal']['url']
            rec['procurement_contact']['supplier_portal_evidence'] = {'anchor': F['supplier_portal']['anchor'], 'found_on': F['supplier_portal']['found_on']}
            new_fields.append('procurement_contact.supplier_portal')
        if F['phone'] and not ap['phone']:
            ap['phone'] = F['phone']['phone']; ap['phone_evidence'] = {'page_url': F['phone']['page_url'], 'snippet': F['phone']['snippet'][:300], 'retrieved_at': F['phone'].get('retrieved_at')}
            new_fields.append('ap_contact.phone'); srcs.append(F['phone']['page_url'])
        if F['proc_url'] and not rec['procurement_contact'].get('url'):
            rec['procurement_contact']['url'] = F['proc_url']; new_fields.append('procurement_contact.url')
    if ap['evidence'] and not ap['instructions_url']:
        ap['instructions_url'] = ap['evidence'][0]['page_url']; ap['retrieved_at'] = ap['evidence'][0]['retrieved_at']; ap['evidence_snippet'] = ap['evidence'][0].get('snippet', '')
    # ---- targeted findings
    for m in manual_hits(rec, b, g):
        srcs.append(m['url'])
        basis = m.get('basis', 'own')
        for e in reversed(m.get('ap_emails', [])):
            e = e.lower()
            if e in ap['emails']:
                ap['emails'].remove(e); ap['evidence'] = [x for x in ap['evidence'] if x.get('email') != e]
            else:
                new_fields.append('ap_contact.emails')
            ap['emails'].insert(0, e)
            ap['evidence'].insert(0, {'email': e, 'page_url': m['url'], 'retrieved_at': m['retrieved_at'], 'source': 'targeted search (%s)' % basis,
                                      'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e)) or m.get('evidence_snippet') or '(targeted search)')[:400]})
        if m.get('ap_emails') or m.get('invoicing_requirements') or m.get('invoice_portal'):
            if not ap.get('_manual'):
                ap['instructions_url'] = m['url']; ap['retrieved_at'] = m['retrieved_at']
                ap['evidence_snippet'] = m.get('evidence_snippet') or ap['evidence_snippet']
                if m.get('invoicing_requirements'):
                    if ap['invoicing_requirements'] != m['invoicing_requirements']:
                        new_fields.append('ap_contact.invoicing_requirements')
                    ap['invoicing_requirements'] = m['invoicing_requirements']
                ap['_manual'] = True
            elif m.get('invoicing_requirements') and m['invoicing_requirements'] not in ap['invoicing_requirements']:
                ap['invoicing_requirements'] += ' | ' + m['invoicing_requirements']
        for f in ('invoice_portal', 'mailing_address', 'phone', 'fax'):
            if m.get(f) and ap.get(f) != m[f]:
                ap[f] = m[f]; new_fields.append('ap_contact.' + f)
        for e in reversed(m.get('proc_emails', [])):
            e = e.lower()
            if e not in rec['procurement_contact']['emails']:
                rec['procurement_contact']['emails'].insert(0, e); new_fields.append('procurement_contact.emails')
                rec['procurement_contact']['evidence'].insert(0, {'email': e, 'page_url': m['url'], 'retrieved_at': m['retrieved_at'], 'source': 'targeted search (%s)' % basis,
                                                                  'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e)) or '')[:400]})
        if m.get('proc_url') and rec['procurement_contact'].get('url') != m['proc_url']:
            rec['procurement_contact']['url'] = m['proc_url']; new_fields.append('procurement_contact.url')
        if m.get('proc_phone') and not rec['procurement_contact'].get('phone'):
            rec['procurement_contact']['phone'] = m['proc_phone']; new_fields.append('procurement_contact.phone')
        for e in reversed(m.get('general_emails', [])):
            e = e.lower()
            if e not in rec['general_contact']['emails']:
                rec['general_contact']['emails'].insert(0, e); new_fields.append('general_contact.emails')
                rec['general_contact']['evidence'].insert(0, {'email': e, 'page_url': m['url'], 'retrieved_at': m['retrieved_at'], 'source': 'targeted search (%s)' % basis,
                                                               'snippet': re.sub(r'\s+', ' ', PROBE_CTX.get((m['url'], e)) or '')[:400]})
        if m.get('general_phone') and not rec['general_contact'].get('phone'):
            rec['general_contact']['phone'] = m['general_phone']; new_fields.append('general_contact.phone')
        if m.get('official_website') and not rec.get('official_website'):
            rec['official_website'] = m['official_website']; new_fields.append('official_website')
        if m.get('address') and not (rec.get('address') or {}).get('line1'):
            rec['address'] = m['address']; new_fields.append('address')
        if m.get('notes'):
            notes.append(m['notes'])
        if basis != 'own':
            rec['extras'].setdefault('ap_inherited_from', [])
            inh = {'organisation': m.get('parent_name', ''), 'basis': basis, 'url': m['url']}
            if inh not in rec['extras']['ap_inherited_from']:
                rec['extras']['ap_inherited_from'].append(inh)
        rec['extras'].setdefault('targeted_sources', [])
        if m['url'] not in rec['extras']['targeted_sources']:
            rec['extras']['targeted_sources'].append(m['url'])
    ap.pop('_manual', None)
    # ---- multi-government bare names (e.g. "Infrastructure"): add each government's central facts to its jurisdiction candidate entry
    for jc in rec['extras'].get('jurisdiction_candidates', []):
        for m in manual:
            if m['match'].get('parent_key') == 'gov_' + jc.get('jurisdiction', ''):
                newe = [e for e in m.get('ap_emails', []) if e not in jc.get('ap_emails', [])]
                if newe or not jc.get('instructions_url'):
                    jc.setdefault('government', m['match']['parent_key'])
                    jc.setdefault('ap_emails', []).extend(newe)
                    jc['instructions_url'] = jc.get('instructions_url') or m['url']; jc['retrieved_at'] = jc.get('retrieved_at') or m['retrieved_at']
                    if m.get('invoicing_requirements') and not jc.get('invoicing_requirements'):
                        jc['invoicing_requirements'] = m['invoicing_requirements'][:600]
                    if newe:
                        new_fields.append('extras.jurisdiction_candidates.ap_emails'); srcs.append(m['url'])
    # ---- personal-data guards (same as v1/v2)
    okey = re.sub(r'[^a-z]', '', unaccent(orgname.lower()))
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
    for fld in ('ap_contact', 'procurement_contact', 'general_contact'):
        bad = [e for e in rec[fld]['emails'] if personal_like(e) or (C.localpart_class(e, 'invoice supplier') is None and e not in KEEP and fld != 'general_contact')]
        if bad:
            rec[fld]['emails'] = [e for e in rec[fld]['emails'] if e not in bad]
            rec[fld]['evidence'] = [ev for ev in rec[fld]['evidence'] if ev.get('email') not in bad]
        for ev in rec[fld].get('evidence', []):
            if ev.get('snippet'):
                ev['snippet'] = redact(ev['snippet'])
    ap['evidence_snippet'] = redact(ap['evidence_snippet'])
    ap['invoicing_requirements'] = redact(ap['invoicing_requirements'])
    for ev in rec['extras'].get('finance_role_mailboxes', []):
        ev['snippet'] = redact(ev.get('snippet', ''))
    after = json.dumps({x: rec.get(x) for x in ('official_website', 'ap_contact', 'procurement_contact', 'general_contact', 'address', 'identifiers')}, sort_keys=True)
    new_fields = list(dict.fromkeys(new_fields))
    if not is_new and (before == after and not new_fields):
        continue
    rec['notes'] = '; '.join(dict.fromkeys(n for n in notes if n))
    rec['extras']['deep_pass'] = {'run': RUN, 'task': b['_task'], 'group': g['gid'] if g else '', 'group_label': g['label'] if g else '',
                                  'new_fields': new_fields, 'sources': list(dict.fromkeys(srcs))[:12]}
    fo.write(json.dumps(rec, ensure_ascii=False) + '\n')
    stats['written'] += 1
    stats['written_' + b['_task']] += 1
    has_ap = bool(ap['emails']); has_portal = bool(ap['invoice_portal'])
    if 'ap_contact.emails' in new_fields:
        stats['gained_ap_email'] += 1; stats['gained_ap_email_records'] += b['record_count']
    if 'ap_contact.invoice_portal' in new_fields:
        stats['gained_portal'] += 1; stats['gained_portal_records'] += b['record_count']
    if ('ap_contact.emails' in new_fields or 'ap_contact.invoice_portal' in new_fields):
        stats['gained_ap_email_or_portal'] += 1; stats['gained_ap_email_or_portal_records'] += b['record_count']
    for f in new_fields:
        stats['new:' + f] += 1
    if is_new:
        for f, cond in [('website', rec['official_website']), ('ap_email', has_ap), ('portal', has_portal), ('invoicing_requirements', ap['invoicing_requirements']),
                        ('procurement_email', rec['procurement_contact']['emails']), ('procurement_url', rec['procurement_contact'].get('url')),
                        ('general_email', rec['general_contact']['emails']), ('address', (rec['address'] or {}).get('line1') or (rec['address'] or {}).get('city')),
                        ('identifiers', any(x != 'from_dataset' for x in rec['identifiers']))]:
            if cond:
                stats['newbuyer_has_' + f] += 1
fo.close()
os.replace(tmp, OUT_ENRICHED)
stats['assembled_at'] = now()
json.dump(dict(stats), open(WORK + '/assemble_stats.json', 'w'), indent=1)
print(json.dumps(dict(sorted(stats.items(), key=lambda t: str(t[0]))), indent=0))

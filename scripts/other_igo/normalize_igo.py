#!/usr/bin/env python3
"""Normalize other-IGO contract awards to Canadian suppliers into other_igo.jsonl.

Feeds:
  IDB:  <dl>/idb/idb_contract_awards_canada.json  (CKAN datastore_search, awarded_firm_country_name='CANADA')
  EBRD: <dl>/ebrd/award_list.json + <dl>/ebrd/notices/<id>.html (ECEPP Contract Award Notices; contracting party address country)

Usage: python3 -I normalize_igo.py <dl> <out_jsonl> <stats_json>
"""
import datetime as dt, html, json, os, re, sys
from collections import defaultdict

TODAY = dt.date(2026, 10, 25)


def num(s):
    if s in (None, ''):
        return None
    try:
        return float(str(s).replace(',', '').replace('€', '').strip())
    except ValueError:
        return None


def d_idb(s):
    if not s:
        return None
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


def d_dmy(s):
    if not s:
        return None
    m = re.search(r'(\d{2})/(\d{2})/(\d{4})', s)
    return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


IDB_COUNTRY = {'AR': 'AR', 'BA': 'BS', 'BR': 'BR', 'BL': 'BZ', 'BO': 'BO', 'BH': 'BB', 'CH': 'CL', 'CO': 'CO', 'CR': 'CR', 'DR': 'DO', 'EC': 'EC', 'ES': 'SV', 'GU': 'GT', 'GY': 'GY', 'HA': 'HT', 'HO': 'HN', 'JA': 'JM', 'ME': 'MX', 'NI': 'NI', 'PN': 'PA', 'PR': 'PY', 'PE': 'PE', 'SU': 'SR', 'TT': 'TT', 'UR': 'UY', 'VE': 'VE', 'RG': None, 'CA': None}
IDB_NAME = {'ARGENTINA': 'AR', 'BAHAMAS': 'BS', 'BARBADOS': 'BB', 'BELIZE': 'BZ', 'BOLIVIA': 'BO', 'BRAZIL': 'BR', 'CHILE': 'CL', 'COLOMBIA': 'CO', 'COSTA RICA': 'CR', 'DOMINICAN REPUBLIC': 'DO', 'ECUADOR': 'EC', 'EL SALVADOR': 'SV', 'GUATEMALA': 'GT', 'GUYANA': 'GY', 'HAITI': 'HT', 'HONDURAS': 'HN', 'JAMAICA': 'JM', 'MEXICO': 'MX', 'NICARAGUA': 'NI', 'PANAMA': 'PA', 'PARAGUAY': 'PY', 'PERU': 'PE', 'SURINAME': 'SR', 'TRINIDAD AND TOBAGO': 'TT', 'URUGUAY': 'UY', 'VENEZUELA': 'VE'}


def idb(dl, emit, excl, stats):
    d = json.load(open(os.path.join(dl, 'idb', 'idb_contract_awards_canada.json')))
    retrieved = d.get('_retrieved_at') or dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    for r in d['result']['records']:
        stats['idb_rows'] += 1
        start = d_idb(r.get('start_date')) or d_idb(r.get('signature_date'))
        stop = d_idb(r.get('stop_date'))
        st = r.get('status')
        if stop:
            if stop >= TODAY and (start is None or start <= TODAY):
                status, basis = 'ongoing', f"IDB feed: start_date {start.isoformat() if start else 'n/a'} <= 2026-10-25 and stop_date {stop.isoformat()} >= 2026-10-25 (status={st})."
            else:
                excl.append({'record_id': f"other_igo:idb:{r['contract_id']}", 'reason': f"stop_date {stop.isoformat()} < 2026-10-25 (status={st})"})
                stats['idb_excluded_stop_passed'] += 1
                continue
        else:
            if st == 'ACTIVE':
                status, basis = 'ongoing_inferred', "IDB feed: no stop_date; contract status = ACTIVE in the IDB procurement system."
            else:
                excl.append({'record_id': f"other_igo:idb:{r['contract_id']}", 'reason': f"no stop_date and status={st} (not active)"})
                stats['idb_excluded_exited_no_stop'] += 1
                continue
        emit({
            'record_id': f"other_igo:idb:{r['contract_id']}",
            'source': {'key': 'other_igo', 'name': 'Inter-American Development Bank - IDB Project Procurement Contract Awards Data', 'publisher': 'Inter-American Development Bank (IDB Open Data)',
                       'dataset_url': 'https://data.iadb.org/dataset/idb-project-procurement-contract-awards-data', 'record_url': None, 'retrieved_at': retrieved},
            'status': status, 'status_basis': basis,
            'contract': {
                'identifiers': {'contract_id': r.get('contract_id'), 'project_number': r.get('project_number'), 'operation_number': r.get('operation_number'), 'borrower_cd': r.get('borrower_cd'), 'executor_cd': r.get('executor_cd'), 'datastore_id': r.get('_id')},
                'title': r.get('project_name'), 'description': None, 'instrument_type': 'contract',
                'procurement_method': r.get('procurement_type'), 'solicitation_procedure': r.get('contract_type'),
                'commodity': {'contract_type': r.get('contract_type'), 'economic_sector': r.get('economic_sector_name')},
                'value': num(r.get('total_amount')), 'currency': 'USD',
                'value_detail': {'total_amount': num(r.get('total_amount')), 'idb_amount': num(r.get('idb_amount'))},
                'dates': {'published': None, 'signed': d_idb(r.get('signature_date')).isoformat() if d_idb(r.get('signature_date')) else None,
                          'start': d_idb(r.get('start_date')).isoformat() if d_idb(r.get('start_date')) else None, 'end': stop.isoformat() if stop else None,
                          'entry_date': r.get('entry_date'), 'last_modification_date': r.get('last_modification_date'), 'contract_year': r.get('contract_year'), 'amended_last': None},
                'related': {'project_url': f"https://www.iadb.org/en/project/{r.get('project_number')}", 'dataset_api': 'https://data.iadb.org/api/3/action/datastore_search?resource_id=dd09c605-9cd8-49c5-92dc-191ff6ecdd58&filters={"awarded_firm_country_name":"CANADA"}'},
            },
            'buyer': {'name': ' / '.join(x for x in [r.get('borrower_name'), r.get('executing_agency')] if x), 'country': IDB_NAME.get((r.get('operation_country_name') or '').upper()) or IDB_COUNTRY.get(r.get('operation_country_code')),
                      'type': 'government (IDB borrower / executing agency)', 'identifiers': {'borrower_cd': r.get('borrower_cd'), 'executor_cd': r.get('executor_cd'), 'operation_country_code': r.get('operation_country_code'), 'operation_country_name': r.get('operation_country_name')},
                      'address': {'country': r.get('operation_country_name')}, 'contact': {}, 'borrower': r.get('borrower_name'), 'executing_agency': r.get('executing_agency'), 'financier': f"IDB {r.get('operation_type_name')} {r.get('operation_number')}"},
            'vendor': {'name': r.get('awarded_firm_name'), 'country': 'CA', 'country_basis': "awarded_firm_country_name = 'CANADA' (IDB's own code awarded_firm_country_code = 'CD'; note IDB code 'CA' means Central American sub-region)",
                       'identifiers': {}, 'address': {'line1': r.get('awarded_firm_address') if r.get('awarded_firm_address') not in ('Not Available', '') else None, 'city': r.get('awarded_firm_city') if r.get('awarded_firm_city') not in ('N/A', '') else None, 'country': 'Canada'}, 'contact': {}},
            'raw': {'idb_row': r, 'dataset': {'ckan_package': 'idb-project-procurement-contract-awards-data', 'resource_id': 'dd09c605-9cd8-49c5-92dc-191ff6ecdd58', 'doi': 'https://doi.org/10.60966/coo0rbyd'}},
        })
        stats[f'idb_{status}'] += 1


def clean(s):
    if s is None:
        return None
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '\n', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip() or None


def parse_ebrd(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    body = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    txt = clean(body) or ''
    out = {'text': txt}

    def grab(label, multiline=False):
        m = re.search(re.escape(label) + r'\s*\n\s*(.+?)(?:\n|$)', txt)
        return m.group(1).strip() if m else None
    for lab, key in [('Project Name:', 'project_name'), ('EBRD Project ID:', 'project_id'), ('Country:', 'country'), ('Client Name:', 'client_name'), ('ECEPP ID:', 'ecepp_id'),
                     ('Procurement Exercise Name:', 'exercise_name'), ('Type of Procurement:', 'procurement_type'), ('Procurement Method:', 'procurement_method'),
                     ('Business Sector:', 'business_sector'), ('Publication Date:', 'publication_date'), ('Contract Title:', 'contract_title'), ('Contract Description:', 'contract_description'),
                     ('Contract Scheduled Completion Date:', 'scheduled_completion'), ('Date of Contract Signature:', 'signature_date'), ('Signed Contract Value:', 'signed_value'),
                     ('Lot(s):', 'lots'), ('Notice Type:', 'notice_type')]:
        out[key] = grab(lab)
    # contracting parties: blocks after "2. Contracting Party" up to "JVCA Partners:" / "Contract Price" / "3. Other Information"
    parties = []
    for m in re.finditer(r'2\. Contracting Party\s*\n(.*?)(?=\n\s*(?:JVCA Partners:|Contract Price:|2\. Contracting Party|3\. Other Information|$))', txt, re.S):
        lines = [l.strip() for l in m.group(1).split('\n') if l.strip()]
        if lines:
            parties.append({'name': lines[0], 'address_lines': lines[1:], 'country': lines[-1] if len(lines) > 1 else None})
    # older layout: "Awarded Tenderer(s):" block (name, address lines, country, proposal price, JVCA flag)
    m = re.search(r'Awarded Tenderer\(s\):\s*\n(.*?)(?=\n\s*Evaluated Tenderer\(s\):|\n\s*Rejected Tenderer\(s\):|\n\s*Access Opportunity)', txt, re.S)
    if m:
        block = m.group(1)
        # segments end at the "Is this a JVCA: ..." line; a JVCA "Yes" segment continues with "JVCA Details:" partner lines until the next segment start
        lines_b = [l.strip() for l in block.split('\n') if l.strip()]
        segs, cur = [], []
        for l in lines_b:
            cur.append(l)
            if l.startswith('Is this a JVCA'):
                segs.append(cur)
                cur = []
        if cur:
            if segs and any(x.startswith('JVCA Details') for x in cur):
                segs[-1].extend(cur)
            else:
                segs.append(cur)
        # attach "JVCA Details" trailing partner lines (which appear AFTER the Is-this-a-JVCA line) to the preceding segment
        merged = []
        for s in segs:
            if merged and (s[0].startswith('JVCA Details') or s[0].startswith('Lead partner')):
                merged[-1].extend(s)
            else:
                merged.append(s)
        for lines in merged:
            if not lines:
                continue
            head = []
            for l in lines:
                if re.match(r'(Proposal Price|Tender price|Evaluated Tender Price|Is this a JVCA|JVCA Details|Lead partner)', l):
                    break
                head.append(l)
            if not head:
                continue
            addr = head[1:]
            country = addr[-1] if addr else None
            if country and ',' in country and not re.search(r'\bCanada\b$', country):
                country = country.split(',')[-1].strip()
            jv_lines = []
            seen_details = False
            for l in lines:
                if l.startswith('JVCA Details'):
                    seen_details = True
                    continue
                if seen_details:
                    jv_lines.append(l)
            price = next((l for l in lines if l.startswith('Proposal Price (in evaluation currency)') or l.startswith('Evaluated Tender Price')), None)
            price_eur = next((l for l in lines if 'Euro Equivalent' in l), None)
            parties.append({'name': head[0], 'address_lines': addr, 'country': country, 'proposal_price': price, 'proposal_price_eur': price_eur,
                            'jvca': next((l.split(':', 1)[1].strip() for l in lines if l.startswith('Is this a JVCA')), None),
                            'jvca_partner_lines': jv_lines or None, 'layout': 'awarded_tenderers'})
        m2 = re.search(r'Duration of Contract:\s*([^\n]*)', txt)
        out['duration_of_contract'] = m2.group(1).strip() if m2 else None
        m2 = re.search(r'Contract Award Date:\s*([^\n]*)', txt)
        out['contract_award_date'] = m2.group(1).strip() if m2 else None
        m2 = re.search(r'Scope Of Contract:\s*([^\n]*)', txt)
        out['scope_of_contract'] = m2.group(1).strip() if m2 else None
        m2 = re.search(r'Tender/Contract Reference No:\s*([^\n]*)', txt)
        out['tender_contract_reference'] = m2.group(1).strip() if m2 else None
    out['contracting_parties'] = parties
    m = re.search(r'Evaluated Tenderer\(s\):\s*\n(.*?)(?=\n\s*Rejected Tenderer\(s\):|\n\s*Access Opportunity)', txt, re.S)
    out['evaluated_tenderers_text'] = m.group(1).strip() if m else None
    m = re.search(r'JVCA Partners:\s*\n(.*?)(?=\n\s*2\. Contracting Party|\n\s*3\. Other Information)', txt, re.S)
    out['jvca_partners_text'] = m.group(1).strip() if m else None
    m = re.search(r'Contract Price:\s*([^\n]+)', txt)
    out['contract_price'] = m.group(1).strip() if m else None
    m = re.search(r'Contract Price \(Euro Equivalent\):\s*([^\n]+)', txt)
    out['contract_price_eur'] = m.group(1).strip() if m else None
    m = re.search(r'JVCA\?\s*([^\n]+)', txt)
    out['jvca'] = m.group(1).strip() if m else None
    m = re.search(r'3\. Other Information\s*\n(.*?)(?=\n\s*4\. Client Address)', txt, re.S)
    out['other_information'] = m.group(1).strip() if m else None
    m = re.search(r'4\. Client Address\s*\n(.*?)(?=\n\s*Access Opportunity|\n\s*Terms and Conditions)', txt, re.S)
    out['client_address'] = [l.strip() for l in m.group(1).split('\n') if l.strip()] if m else []
    # lots with their own contracting parties (multi-lot notices)
    out['lot_blocks'] = re.findall(r'(Lot\s*\d+[^\n]*\n(?:(?!Lot\s*\d+)[^\n]*\n){0,25})', txt)
    return out


def ebrd(dl, emit, excl, stats):
    lst = json.load(open(os.path.join(dl, 'ebrd', 'award_list.json')))
    retrieved = lst['retrieved_at']
    for a in lst['award_notices']:
        nid = a['notice_id']
        path = os.path.join(dl, 'ebrd', 'notices', f'{nid}.html')
        if not os.path.exists(path):
            stats['ebrd_missing_detail'] += 1
            continue
        stats['ebrd_award_notices'] += 1
        p = parse_ebrd(path)
        def is_ca(x):
            if (x.get('country') or '').strip().lower() == 'canada':
                return True
            return any(re.search(r'(^|,\s*)canada\s*(,\s*[A-Z0-9 ]{6,7})?$', l.strip(), re.I) for l in x.get('address_lines', []))
        ca_parties = [x for x in p['contracting_parties'] if is_ca(x)]
        jv_ca = bool(p.get('jvca_partners_text') and re.search(r'\n\s*Canada\s*(\n|$)', '\n' + p['jvca_partners_text'] + '\n'))
        if not ca_parties:
            # JV partner lines in the older layout
            for x in p['contracting_parties']:
                if any(re.search(r',\s*Canada\b', l) for l in (x.get('jvca_partner_lines') or [])):
                    jv_ca = True
                    p['jvca_partners_text'] = (p.get('jvca_partners_text') or '') + '\n' + '\n'.join(x['jvca_partner_lines'])
        if not ca_parties and jv_ca:
            # Canadian firm is a JV/consortium partner of the awarded contracting party
            lead = p['contracting_parties'][0] if p['contracting_parties'] else {'name': None, 'address_lines': []}
            ca_parties = [{'name': lead.get('name'), 'address_lines': lead.get('address_lines'), 'country': lead.get('country'), 'canadian_jv_partner': True}]
            stats['ebrd_canada_as_jv_partner'] += 1
        if not ca_parties:
            continue
        stats['ebrd_canada_awards'] += 1
        signed = d_dmy(p.get('signature_date')) or d_dmy(p.get('contract_award_date'))
        end = d_dmy(p.get('scheduled_completion'))
        computed_end = None
        if end:
            if end >= TODAY and (signed is None or signed <= TODAY):
                status, basis = 'ongoing', f"ECEPP notice: 'Contract Scheduled Completion Date' {end.isoformat()} >= 2026-10-25; 'Date of Contract Signature' {signed.isoformat() if signed else 'n/a'}."
            else:
                excl.append({'record_id': f'other_igo:ebrd:{nid}', 'reason': f"scheduled completion {end.isoformat()} < 2026-10-25"})
                stats['ebrd_excluded_completed'] += 1
                continue
        else:
            dur_txt = (p.get('duration_of_contract') or '').strip()
            md = re.match(r'(\d+)\s*(month|year|week|day)', dur_txt, re.I)
            if not md and re.fullmatch(r'\d{1,3}', dur_txt):
                md = re.match(r'(\d+)()', dur_txt)  # bare number: ECEPP 'Duration of Contract' is expressed in months
            if md and signed:
                v, u = int(md.group(1)), (md.group(2) or 'month').lower()
                computed_end = signed + dt.timedelta(days=round(v * {'month': 30.44, 'year': 365.25, 'week': 7, 'day': 1}[u]))
                if computed_end >= TODAY and signed <= TODAY:
                    status, basis = 'ongoing_inferred', f"ECEPP notice: 'Duration of Contract' {p['duration_of_contract']} (months assumed when no unit given); computed end = Contract Award Date {signed.isoformat()} + duration = {computed_end.isoformat()} >= 2026-10-25."
                else:
                    excl.append({'record_id': f'other_igo:ebrd:{nid}', 'reason': f"duration {p['duration_of_contract']} from {signed.isoformat()} -> computed end {computed_end.isoformat()} < 2026-10-25"})
                    stats['ebrd_excluded_completed'] += 1
                    continue
            else:
                status, basis = 'end_date_unknown', 'ECEPP notice has no scheduled completion date or duration.'
        val = p.get('signed_value') or ''
        mv = re.match(r'([\d,\.]+)\s*([A-Z]{3})', val)
        party = ca_parties[0]
        emit({
            'record_id': f'other_igo:ebrd:{nid}',
            'source': {'key': 'other_igo', 'name': 'European Bank for Reconstruction and Development - ECEPP Contract Award Notices', 'publisher': 'EBRD (ECEPP - EBRD Client E-Procurement Portal)',
                       'dataset_url': 'https://ecepp.ebrd.com/delta/noticeSearch.html', 'record_url': a['url'], 'retrieved_at': retrieved},
            'status': status, 'status_basis': basis,
            'contract': {
                'identifiers': {'ecepp_notice_id': nid, 'ecepp_id': p.get('ecepp_id'), 'ebrd_project_id': p.get('project_id')},
                'title': p.get('contract_title') or a.get('title'), 'description': p.get('contract_description'), 'instrument_type': 'contract',
                'procurement_method': p.get('procurement_method'), 'solicitation_procedure': p.get('procurement_type'),
                'commodity': {'business_sector': p.get('business_sector'), 'procurement_type': p.get('procurement_type')},
                'value': num(mv.group(1)) if mv else None, 'currency': mv.group(2) if mv else None,
                'value_detail': {'signed_contract_value': p.get('signed_value'), 'contract_price_party': p.get('contract_price'), 'contract_price_eur_equivalent': p.get('contract_price_eur')},
                'dates': {'published': d_dmy(p.get('publication_date')).isoformat() if d_dmy(p.get('publication_date')) else None, 'signed': signed.isoformat() if signed else None, 'start': None,
                          'end': end.isoformat() if end else None, 'end_computed': computed_end.isoformat() if computed_end else None, 'duration': p.get('duration_of_contract'), 'amended_last': None},
                'related': {'notice_url': a['url'], 'ebrd_project_url': f"https://www.ebrd.com/work-with-us/projects/psd/{p.get('project_id')}" if p.get('project_id') else None, 'project_name': p.get('project_name'), 'procurement_exercise': p.get('exercise_name')},
            },
            'buyer': {'name': p.get('client_name'), 'country': None, 'type': 'EBRD client (public entity / borrower)', 'identifiers': {'ebrd_project_id': p.get('project_id')},
                      'address': {'lines': p.get('client_address'), 'country': p.get('country')}, 'contact': {}, 'country_name': p.get('country'), 'financier': 'EBRD'},
            'vendor': {'name': party['name'], 'country': 'CA' if not party.get('canadian_jv_partner') else party.get('country'),
                       'country_basis': ("'2. Contracting Party' / 'Awarded Tenderer(s)' address block in the ECEPP contract award notice ends with 'Canada'" if not party.get('canadian_jv_partner') else "awarded party is a JV whose partner list ('JVCA Partners') includes a member with address country Canada; lead party country shown"),
                       'identifiers': {}, 'address': {'lines': party.get('address_lines'), 'country': 'Canada'}, 'contact': {}, 'jvca': p.get('jvca'), 'jvca_partners': p.get('jvca_partners_text'),
                       'all_contracting_parties': p['contracting_parties']},
            'raw': {'list_row': a, 'notice_parsed': p, 'notice_html_path': path},
        })
        stats[f'ebrd_{status}'] += 1


def main():
    dl, out_path, stats_path = sys.argv[1:4]
    stats = defaultdict(int)
    excl = []
    out = open(out_path, 'w', encoding='utf-8')

    def emit(rec):
        out.write(json.dumps(rec, ensure_ascii=False) + '\n')
    idb(dl, emit, excl, stats)
    ebrd(dl, emit, excl, stats)
    out.close()
    with open(stats_path, 'w') as f:
        json.dump({'stats': dict(stats), 'excluded': excl}, f, indent=1, ensure_ascii=False)
    print(json.dumps(dict(stats), indent=1))


if __name__ == '__main__':
    main()

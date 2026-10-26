#!/usr/bin/env python3
"""Normalize World Bank contract awards to Canadian suppliers.

Feeds (downloads/worldbank):
  fone_DS01004_RS00934_canada.json  IPF contract awards FY2001-2016 (supplier_country='Canada')
  fone_DS04691_RS03933_canada.json  IPF contract awards FY2017-2019
  fone_DS00005_RS00005_canada.json  IPF contract awards FY2020+   (these three = successor of Socrata kdui-wcs3 "Major Contract Awards")
  fone_DS00028_RS00025_canada.json  Corporate Procurement Contract Awards (World Bank Group itself is the buyer)
  projects.json                     Projects API records keyed by project_id
  procnotices_canada.json           Procurement "Contract Award" notices whose text contains "Country: Canada"

Status logic:
  IPF awards: no end date in the feed. If a matching procnotice gives "Duration of Contract" -> compute end from
  award/signing date (ongoing_inferred or exclude). Else project status Active and closing date >= today -> ongoing_inferred
  (project closing date is the latest the contract can be disbursed). Project Closed/Dropped with closing < today -> exclude.
  Project record missing/empty -> end_date_unknown. Pipeline/Active without closing date -> end_date_unknown.
  Procnotices awards with Canadian awarded firm not present in the IPF feed -> own records (duration-based status).
  Corporate procurement: award_date only -> end_date_unknown.

Usage: python3 -I normalize_wb.py <downloads_dir> <out_jsonl> <stats_json>
"""
import datetime as dt, html, json, os, re, sys
from collections import defaultdict

TODAY = dt.date(2026, 10, 25)


def parse_date(s):
    if not s:
        return None
    s = str(s).strip()
    for fmt in ('%d-%b-%Y', '%Y-%m-%dT%H:%M:%SZ', '%m/%d/%Y %I:%M:%S %p', '%Y/%m/%d', '%Y-%m-%d', '%d-%b-%y', '%m/%d/%Y'):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def add_months(d, months):
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return dt.date(y, m, day)


def add_duration(d, value, unit):
    u = unit.lower()
    v = float(value)
    if u.startswith('month'):
        whole = int(v)
        return add_months(d, whole) + dt.timedelta(days=round((v - whole) * 30.4))
    if u.startswith('year'):
        return add_months(d, int(round(v * 12)))
    if u.startswith('week'):
        return d + dt.timedelta(days=int(round(v * 7)))
    if u.startswith('day'):
        return d + dt.timedelta(days=int(round(v)))
    return None


def num(s):
    if s is None or s == '':
        return None
    try:
        return float(str(s).replace(',', ''))
    except ValueError:
        return None


# ------------------------------------------------------------------ procnotice parsing
def html_to_text(t):
    txt = re.sub(r'<br\s*/?>', '\n', t, flags=re.I)
    txt = re.sub(r'</(p|div|tr|h\d|li|table)>', '\n', txt, flags=re.I)
    txt = re.sub(r'<td[^>]*>', ' | ', txt, flags=re.I)
    txt = re.sub(r'<[^>]+>', '', txt)
    txt = html.unescape(txt)
    txt = re.sub(r'[ \t]+', ' ', txt)
    txt = re.sub(r'\n\s*\n+', '\n', txt)
    return txt.strip()


def parse_procnotice(n):
    """Extract structured fields from a Contract Award notice (STEP format or 'Small Contract Award Notice')."""
    txt = html_to_text(n.get('notice_text') or '')
    out = {'text': txt, 'kind': None, 'awarded_firms': [], 'duration': None, 'award_date': None, 'signed_price': None, 'loan_info': None}
    if txt.startswith('Small Contract Award Notice'):
        out['kind'] = 'small_contract_award_notice'
        # repeated blocks
        blocks = re.split(r'\n(?=Awarded Firm/Indv\. ?:)', txt)
        for b in blocks[1:]:
            firm = {}
            m = re.search(r'Awarded Firm/Indv\. ?:\s*(.*)', b)
            firm['name'] = m.group(1).strip() if m else None
            m = re.search(r'Address:\s*(.*)', b)
            firm['address'] = m.group(1).strip() if m else None
            m = re.search(r'Country:\s*(.*)', b)
            firm['country'] = m.group(1).strip() if m else None
            m = re.search(r'Contract Signature Date:\s*(.*)', b)
            firm['signature_date'] = m.group(1).strip() if m else None
            m = re.search(r'Method of Procurement:\s*(.*)', b)
            firm['method'] = m.group(1).strip() if m else None
            m = re.search(r'Price:\s*(.*)', b)
            firm['price'] = m.group(1).strip() if m else None
            m = re.search(r'Duration:\s*(.*)', b)
            firm['duration'] = m.group(1).strip() if m else None
            m = re.search(r'Summary Scope of Contract:\s*(.*)', b)
            firm['scope'] = m.group(1).strip() if m else None
            out['awarded_firms'].append(firm)
        return out
    out['kind'] = 'step_contract_award'
    m = re.search(r'Loan/Credit/TF Info:\s*(.*)', txt)
    out['loan_info'] = m.group(1).strip() if m else None
    m = re.search(r'Date Notification of Award Issued\s*\(YYYY/MM/DD\)\s*(\d{4}/\d{2}/\d{2})', txt)
    out['award_date'] = m.group(1) if m else None
    m = re.search(r'Duration of Contract\s*\n?\s*([\d.,]+)\s*(Month|Week|Day|Year)\(s\)', txt)
    out['duration'] = {'value': m.group(1).replace(',', ''), 'unit': m.group(2)} if m else None
    m = re.search(r'Signed Contract [Pp]rice\s*\n?\s*(.*)', txt)
    out['signed_price'] = m.group(1).strip() if m else None
    m = re.search(r'Scope of Contract:\s*(.*)', txt)
    out['scope'] = m.group(1).strip() if m else None
    m = re.search(r'Procurement Method:\s*(.*)', txt)
    out['method'] = m.group(1).strip() if m else None
    m = re.search(r'Notice Version No:\s*(\d+)', txt)
    out['version'] = m.group(1) if m else None
    m = re.search(r'Minimum Qualifying Score\s*\n?\s*([\d.]+)', txt)
    out['min_qualifying_score'] = m.group(1) if m else None
    # awarded section
    m = re.search(r'Awarded (?:Firm|Bidder)\(s\):(.*?)(?:Evaluated (?:Firm|Bidder)\(s\):|Rejected (?:Firm|Bidder)\(s\):|$)', txt, re.S)
    if m:
        sec = m.group(1)
        # firms: "NAME (id)\n[address]\nCountry: X"
        for fm in re.finditer(r'(?:^|\n)\s*([^\n]+?)\s*\((\d+)\)\s*\n((?:(?!Country:)[^\n]*\n){0,8}?)Country:\s*([^\n|]+)', sec):
            addr = ' '.join(l.strip() for l in fm.group(3).split('\n') if l.strip()) if fm.group(3) else None
            out['awarded_firms'].append({'name': fm.group(1).strip(), 'supplier_id': fm.group(2), 'address': addr or None, 'country': fm.group(4).strip()})
        if not out['awarded_firms']:
            # individual consultants are anonymised: "Individual Consultant\nCountry: X"
            for fm in re.finditer(r'(?:^|\n)\s*(Individual Consultant[^\n(]*)\n(?:Registry ID:[^\n]*\n)?Country:\s*([^\n|]+)', sec):
                out['awarded_firms'].append({'name': fm.group(1).strip(), 'supplier_id': None, 'address': None, 'country': fm.group(2).strip(), 'anonymised_individual': True})
            if not out['awarded_firms']:
                for fm in re.finditer(r'(?:^|\n)\s*([^\n]+)\n(?:(?!Country:)[^\n]*\n){0,6}?Country:\s*([^\n|]+)', sec):
                    out['awarded_firms'].append({'name': fm.group(1).strip(), 'supplier_id': None, 'address': None, 'country': fm.group(2).strip()})
        # beneficial owners
        bo = []
        for bm in re.finditer(r'\n\s*\|?\s*([^|\n]+?)\s*\|\s*([A-Z]{2})\s*\|\s*([^|\n]+?)\s*\|\s*([^\n]+)', sec):
            if bm.group(1).strip() in ('Name',):
                continue
            bo.append({'name': bm.group(1).strip(), 'nationality': bm.group(2), 'residence_country': bm.group(3).strip(), 'conditions_met': bm.group(4).strip()})
        out['beneficial_owners'] = bo
        sm = re.search(r'Final Evaluation Price\s*\n?\s*([^\n]+)', sec)
        out['final_evaluation_price'] = sm.group(1).strip() if sm else None
        pm = re.search(r'Bid Price at Opening\s*\n?\s*([^\n]+)', sec)
        out['bid_price_at_opening'] = pm.group(1).strip() if pm else None
        em = re.search(r'Evaluated Bid Price\s*\n?\s*([^\n]+)', sec)
        out['evaluated_bid_price'] = em.group(1).strip() if em else None
        out['awarded_section'] = sec.strip()
    return out


def parse_price(s):
    """'MGA 1392300000.00; EUR 355000.00' -> list of {currency, amount}"""
    if not s:
        return []
    res = []
    for part in re.split(r';', s):
        m = re.match(r'\s*([A-Z]{3})\s*([\d,]+(?:\.\d+)?)', part.strip())
        if m:
            res.append({'currency': m.group(1), 'amount': num(m.group(2))})
    return res


WB_NAME_TO_ISO2 = {
    'Belize': 'BZ', 'Haiti': 'HT', 'Congo, Democratic Republic of': 'CD', 'Madagascar': 'MG', 'Bosnia and Herzegovina': 'BA', 'Nepal': 'NP', "Cote d'Ivoire": 'CI',
    'Cameroon': 'CM', 'Guinea': 'GN', 'Congo, Republic of': 'CG', 'Dominica': 'DM', 'Sao Tome and Principe': 'ST', 'Jamaica': 'JM', 'Sri Lanka': 'LK', 'Lesotho': 'LS',
    'Burkina Faso': 'BF', 'Burundi': 'BI', 'Guyana': 'GY', 'Senegal': 'SN', 'Cabo Verde': 'CV', 'Morocco': 'MA', 'Somalia, Federal Republic of': 'SO', 'Somalia': 'SO',
    'Uzbekistan': 'UZ', 'Tonga': 'TO', 'Gambia, The': 'GM', 'Solomon Islands': 'SB', 'Tuvalu': 'TV', 'Myanmar': 'MM', 'Gabon': 'GA', 'Mauritania': 'MR', 'India': 'IN',
    'Chad': 'TD', 'Viet Nam': 'VN', 'Vietnam': 'VN', "Lao People's Democratic Republic": 'LA', 'Angola': 'AO', 'Comoros': 'KM', 'Mongolia': 'MN', 'Vanuatu': 'VU',
    'Maldives': 'MV', 'St Maarten': 'SX', 'Kyrgyz Republic': 'KG', 'Nigeria': 'NG', 'Tanzania': 'TZ', 'Tajikistan': 'TJ', 'Georgia': 'GE', 'Marshall Islands': 'MH',
    'Pakistan': 'PK', 'St. Lucia': 'LC', 'Ukraine': 'UA', 'Cambodia': 'KH', 'Ethiopia': 'ET', 'Turkiye': 'TR', 'Turkey': 'TR', 'Ghana': 'GH', 'Liberia': 'LR', 'Kenya': 'KE',
    'Djibouti': 'DJ', 'Kosovo': 'XK', 'Togo': 'TG', 'St. Vincent and the Grenadines': 'VC', 'Mali': 'ML', 'Bangladesh': 'BD', 'Rwanda': 'RW', 'Central African Republic': 'CF',
    'Kiribati': 'KI', 'Serbia': 'RS', 'Niger': 'NE', 'Benin': 'BJ', 'Papua New Guinea': 'PG', 'Malawi': 'MW', 'Philippines': 'PH', 'Guatemala': 'GT',
    'Egypt, Arab Republic of': 'EG', 'Mozambique': 'MZ', 'Iraq': 'IQ', 'Guinea-Bissau': 'GW', 'Bhutan': 'BT', 'Azerbaijan': 'AZ', 'Costa Rica': 'CR',
    'Micronesia, Federated States of': 'FM', 'South Sudan': 'SS', 'Sierra Leone': 'SL', 'Fiji': 'FJ', 'Panama': 'PA', 'Uganda': 'UG', 'West Bank and Gaza': 'PS', 'Peru': 'PE',
    'Yemen, Republic of': 'YE', 'Barbados': 'BB', 'Poland': 'PL', 'Uruguay': 'UY', 'Dominican Republic': 'DO', 'Armenia': 'AM', 'Afghanistan': 'AF', 'Sudan': 'SD',
    'Colombia': 'CO', 'Tunisia': 'TN', 'Kazakhstan': 'KZ', 'Botswana': 'BW', 'Albania': 'AL', 'Algeria': 'DZ', 'Argentina': 'AR', 'Belarus': 'BY', 'Brazil': 'BR',
    'Bulgaria': 'BG', 'China': 'CN', 'Croatia': 'HR', 'El Salvador': 'SV', 'Eswatini': 'SZ', 'Grenada': 'GD', 'Honduras': 'HN', 'Indonesia': 'ID',
    'Iran, Islamic Republic of': 'IR', 'Jordan': 'JO', 'Latvia': 'LV', 'Lebanon': 'LB', 'Mauritius': 'MU', 'Mexico': 'MX', 'Moldova': 'MD', 'Montenegro': 'ME',
    'Nicaragua': 'NI', 'North Macedonia': 'MK', 'Romania': 'RO', 'Russian Federation': 'RU', 'Samoa': 'WS', 'Slovenia': 'SI', 'South Africa': 'ZA',
    'St. Kitts and Nevis': 'KN', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Trinidad and Tobago': 'TT', 'Venezuela, Republica Bolivariana de': 'VE', 'Zambia': 'ZM',
    'Ecuador': 'EC', 'Bolivia': 'BO', 'Paraguay': 'PY', 'Chile': 'CL', 'Zimbabwe': 'ZW', 'Namibia': 'NA', 'Eritrea': 'ER', 'Libya': 'LY', 'Syrian Arab Republic': 'SY',
    'Turkmenistan': 'TM', 'Hungary': 'HU', 'Lithuania': 'LT', 'Estonia': 'EE', 'Slovak Republic': 'SK', 'Czech Republic': 'CZ', 'Korea, Republic of': 'KR', 'Malaysia': 'MY',
    'Equatorial Guinea': 'GQ', 'Seychelles': 'SC', 'Nauru': 'NR', 'Palau': 'PW', 'Suriname': 'SR', 'Antigua and Barbuda': 'AG', 'Bahamas, The': 'BS',
}


def iso2_for(name, wb_code):
    """ISO-3166 alpha-2 for a borrower country; regional/multi-country programmes -> None (kept in identifiers)."""
    if name in WB_NAME_TO_ISO2:
        return WB_NAME_TO_ISO2[name]
    if wb_code and len(wb_code) == 2 and wb_code.isalpha() and wb_code not in ('ZR', 'YF', 'RY', 'GZ', 'CB'):
        return wb_code
    return None


# ------------------------------------------------------------------ status
def status_from_project(proj):
    """returns (status or None (=exclude), basis, end_date_iso)"""
    if not proj or not proj.get('_found') or not proj.get('record') or proj['record'].get('status') is None:
        return 'end_date_unknown', 'Contract feed has no end date; World Bank Projects API returned no status/closing date for the project (project record not found or empty).', None
    r = proj['record']
    st = r.get('status')
    cd = parse_date(r.get('closingdate'))
    if st == 'Active' and cd and cd >= TODAY:
        return 'ongoing_inferred', f"Contract feed has no end date; Projects API: project {r['id']} status=Active, closingdate={cd.isoformat()} >= 2026-10-25 (project closing date bounds the contract).", cd.isoformat()
    if st == 'Active' and cd and cd < TODAY:
        return None, f"Projects API: project status=Active but closingdate {cd.isoformat()} < 2026-10-25 (closing passed; treated as ended).", cd.isoformat()
    if st == 'Active' and not cd:
        return 'end_date_unknown', f"Contract feed has no end date; Projects API: project {r['id']} status=Active but no closing date published.", None
    if st in ('Closed', 'Dropped'):
        if cd and cd >= TODAY:
            return 'ongoing_inferred', f"Projects API: project status={st} but closingdate {cd.isoformat()} >= 2026-10-25.", cd.isoformat()
        return None, f"Projects API: project {r['id']} status={st}, closingdate={cd.isoformat() if cd else 'n/a'} < 2026-10-25 -> contract ended.", cd.isoformat() if cd else None
    if st == 'Pipeline':
        return 'end_date_unknown', f"Contract feed has no end date; Projects API: project status=Pipeline (closing date {cd.isoformat() if cd else 'n/a'}).", cd.isoformat() if cd else None
    return 'end_date_unknown', f"Contract feed has no end date; Projects API status={st}, closing={cd.isoformat() if cd else 'n/a'}.", cd.isoformat() if cd else None


def main():
    dl, out_path, stats_path = sys.argv[1:4]
    projects = json.load(open(os.path.join(dl, 'projects.json')))
    pn = json.load(open(os.path.join(dl, 'procnotices_canada.json')))
    pn_rows = pn['rows']
    parsed = {}
    pn_by_project = defaultdict(list)
    for n in pn_rows:
        p = parse_procnotice(n)
        parsed[n['id']] = p
        pn_by_project[n.get('project_id')].append(n)
    stats = defaultdict(int)
    excluded = []
    out = open(out_path, 'w', encoding='utf-8')

    def emit(rec):
        out.write(json.dumps(rec, ensure_ascii=False) + '\n')
        stats[rec['status']] += 1

    matched_notice_ids = set()
    # ---------------- IPF contract awards
    for ds, rs, title in [('DS01004', 'RS00934', 'Contract Awards in Investment Project Financing (since FY 2001 - FY 2016)'),
                          ('DS04691', 'RS03933', 'Contract Awards in Investment Project Financing (since FY 2017 - FY 2019)'),
                          ('DS00005', 'RS00005', 'Contract Awards in Investment Project Financing (Since FY 2020)')]:
        d = json.load(open(os.path.join(dl, f'fone_{ds}_{rs}_canada.json')))
        retrieved = d['retrieved_at']
        for row in d['rows']:
            try:
                stats['ipf_rows'] += 1
                pid = row.get('project_id')
                proj = projects.get(pid)
                prec = (proj or {}).get('record') or {}
                signed = parse_date(row.get('contract_signing_date'))
                cno = row.get('wb_contract_number') or row.get('contract_number')
                # match procnotice: same project and same borrower reference number
                ref = (row.get('borrower_contract_reference_number') or '').strip()
                match = None
                for n in pn_by_project.get(pid, []):
                    if ref and (n.get('bid_reference_no') or '').strip().lower() == ref.lower():
                        p = parsed[n['id']]
                        if any((f.get('country') or '').lower() == 'canada' for f in p['awarded_firms']):
                            match = n
                            break
                dur = None
                award_date = None
                if match:
                    matched_notice_ids.add(match['id'])
                    p = parsed[match['id']]
                    dur = p.get('duration')
                    award_date = parse_date(p.get('award_date'))
                status = basis = end_iso = None
                computed_end = None
                if dur and (signed or award_date):
                    base = signed or award_date
                    computed_end = add_duration(base, dur['value'], dur['unit'])
                    if computed_end:
                        if computed_end >= TODAY and base <= TODAY:
                            status = 'ongoing_inferred'
                            basis = f"Finances One feed has no end date; matching procurement notice {match['id']} states 'Duration of Contract' {dur['value']} {dur['unit']}(s); computed end = contract_signing_date {base.isoformat()} + duration = {computed_end.isoformat()} >= 2026-10-25."
                        else:
                            basis = f"Matching procurement notice {match['id']} duration {dur['value']} {dur['unit']}(s): computed end {computed_end.isoformat()} = signing {base.isoformat()} + duration < 2026-10-25 -> ended."
                            excluded.append({'record_id': f"worldbank:{ds}:{cno}", 'reason': basis})
                            stats['excluded_duration_ended'] += 1
                            continue
                if status is None:
                    status, basis, end_iso = status_from_project(proj)
                    if status is None:
                        excluded.append({'record_id': f"worldbank:{ds}:{cno}", 'reason': basis})
                        stats['excluded_project_closed'] += 1
                        continue
                    if signed and signed > TODAY:
                        status = 'end_date_unknown'
                        basis += ' Signing date is after the reference date (future-dated row).'
                amount = row.get('supplier_contract_amount_usd', row.get('supplier_contract_amount'))
                sid = row.get('supplier_id')
                rec_id = f"worldbank:{ds}:{cno}" + (f":{sid}" if sid else '')
                rec = {
                    'record_id': rec_id,
                    'source': {
                        'key': 'worldbank',
                        'name': f"World Bank Finances One - {title} (successor of Socrata 'Major Contract Awards' kdui-wcs3)",
                        'publisher': 'World Bank Group (Procurement / STEP data via Finances One)',
                        'dataset_url': f"https://financesone.worldbank.org/d/{ds}",
                        'record_url': None,
                        'retrieved_at': retrieved,
                    },
                    'status': status,
                    'status_basis': basis,
                    'contract': {
                        'identifiers': {'wb_contract_number': cno, 'borrower_contract_reference_number': row.get('borrower_contract_reference_number'), 'project_id': pid,
                                        'supplier_id': sid, 'procurement_notice_id': match['id'] if match else None, 'loan_credit_tf': parsed[match['id']].get('loan_info') if match else None},
                        'title': row.get('contract_description'),
                        'description': (parsed[match['id']].get('scope') if match else None),
                        'instrument_type': 'contract',
                        'procurement_method': row.get('procurement_method'),
                        'solicitation_procedure': row.get('procurement_category'),
                        'commodity': {'procurement_category': row.get('procurement_category'), 'project_global_practice': row.get('project_global_practice')},
                        'value': num(amount),
                        'currency': 'USD',
                        'value_detail': {'supplier_contract_amount_usd': num(amount), 'note': 'USD equivalent; joint-venture totals are split equally among members per dataset description',
                                         'signed_contract_price_notice': parse_price(parsed[match['id']].get('signed_price')) if match else None},
                        'dates': {'published': parse_date(match['noticedate']).isoformat() if match and parse_date(match.get('noticedate')) else None,
                                  'signed': signed.isoformat() if signed else None, 'start': None, 'end': None,
                                  'end_computed': computed_end.isoformat() if computed_end else None,
                                  'duration': dur, 'award_notification': award_date.isoformat() if award_date else None,
                                  'project_closing_date': end_iso, 'fiscal_year': row.get('fiscal_year'), 'amended_last': None},
                        'related': {'project_url': f"https://projects.worldbank.org/en/projects-operations/project-detail/{pid}",
                                    'project_api_url': f"https://search.worldbank.org/api/v2/projects?format=json&id={pid}",
                                    'procurement_notice_url': f"https://projects.worldbank.org/en/projects-operations/procurement-detail/{match['id']}" if match else None,
                                    'dataset_api': f"https://datacatalogapi.worldbank.org/dexapps/fone/api/apiservice?datasetId={ds}&resourceId={rs}&type=json&filter=supplier_country%3D%27Canada%27"},
                    },
                    'buyer': {
                        'name': ' / '.join([x for x in [prec.get('borrower'), prec.get('impagency')] if x]) or (row.get('borrower_country') + ' (borrower; implementing agency not published)'),
                        'country': iso2_for(row.get('borrower_country'), row.get('borrower_country_code') or ((prec.get('countrycode') or [None])[0] if isinstance(prec.get('countrycode'), list) else None)),
                        'type': 'government (World Bank borrower / implementing agency)',
                        'identifiers': {'project_id': pid, 'borrower_country': row.get('borrower_country'), 'wb_borrower_country_code': row.get('borrower_country_code'), 'region': row.get('region')},
                        'address': {'country': row.get('borrower_country')},
                        'contact': {},
                        'borrower': prec.get('borrower'), 'implementing_agency': prec.get('impagency'), 'project_name': row.get('project_name'),
                        'financier': 'World Bank (IBRD/IDA) Investment Project Financing',
                    },
                    'vendor': {
                        'name': row.get('supplier'), 'country': 'CA',
                        'country_basis': "supplier_country = 'Canada' (place of supplier registration per dataset description); supplier_country_code = CA",
                        'identifiers': {'supplier_id': sid},
                        'address': {'line1': None, 'city': None, 'region': None, 'postal_code': None, 'country': 'Canada',
                                    'notice_address': next((f.get('address') for f in parsed[match['id']]['awarded_firms'] if (f.get('country') or '').lower() == 'canada'), None) if match else None},
                        'contact': {},
                    },
                    'raw': {'finances_one_row': row, 'finances_one_dataset': {'datasetId': ds, 'resourceId': rs, 'title': title, 'as_of': row.get('as_of_date')},
                            'project': proj, 'procurement_notice': match, 'procurement_notice_parsed': parsed[match['id']] if match else None},
                }
                emit(rec)
            except Exception as e:
                stats['errors'] += 1
                print('ERROR ipf', row.get('wb_contract_number'), repr(e), file=sys.stderr)
    # ---------------- procnotices not matched to the feed, with a Canadian awarded firm
    for n in pn_rows:
        try:
            if n['id'] in matched_notice_ids:
                continue
            p = parsed[n['id']]
            ca_firms = [f for f in p['awarded_firms'] if (f.get('country') or '').strip().lower() == 'canada']
            if not ca_firms:
                stats['procnotice_canada_only_evaluated'] += 1
                continue
            stats['procnotice_canada_awarded_unmatched'] += 1
            pid = n.get('project_id')
            proj = projects.get(pid)
            if proj is None:
                proj = None
            prec = (proj or {}).get('record') or {}
            for fi, f in enumerate(ca_firms):
                if p['kind'] == 'small_contract_award_notice':
                    signed = parse_date(f.get('signature_date'))
                    dm = re.match(r'([\d.]+)\s*(Month|Week|Day|Year)', f.get('duration') or '')
                    dur = {'value': dm.group(1), 'unit': dm.group(2)} if dm else None
                    base = signed
                    price = parse_price(f.get('price').replace(',', '')) if f.get('price') else []
                    title = f.get('scope')
                    method = f.get('method')
                else:
                    signed = None
                    dur = p.get('duration')
                    base = parse_date(p.get('award_date')) or parse_date(n.get('noticedate'))
                    price = parse_price(p.get('signed_price'))
                    title = n.get('bid_description') or p.get('scope')
                    method = n.get('procurement_method_name') or p.get('method')
                computed_end = add_duration(base, dur['value'], dur['unit']) if dur and base else None
                if computed_end:
                    if computed_end >= TODAY and base <= TODAY:
                        status = 'ongoing_inferred'
                        basis = f"Procurement notice states 'Duration of Contract' {dur['value']} {dur['unit']}(s); computed end = {'contract signature' if signed else 'award notification/notice'} date {base.isoformat()} + duration = {computed_end.isoformat()} >= 2026-10-25."
                    else:
                        excluded.append({'record_id': f"worldbank:procnotice:{n['id']}:{fi}", 'reason': f"notice duration {dur['value']} {dur['unit']}(s) from {base.isoformat()} -> computed end {computed_end.isoformat()} < 2026-10-25."})
                        stats['excluded_duration_ended'] += 1
                        continue
                else:
                    status, basis, _ = status_from_project(proj) if proj else ('end_date_unknown', 'No duration in notice; project not looked up.', None)
                    if status is None:
                        excluded.append({'record_id': f"worldbank:procnotice:{n['id']}:{fi}", 'reason': basis})
                        stats['excluded_project_closed'] += 1
                        continue
                    basis = 'No usable duration in the procurement notice. ' + basis
                rec = {
                    'record_id': f"worldbank:procnotice:{n['id']}" + (f":{fi}" if len(ca_firms) > 1 else ''),
                    'source': {'key': 'worldbank', 'name': 'World Bank Procurement Notices - Contract Award notices (STEP)', 'publisher': 'World Bank Group',
                               'dataset_url': 'https://projects.worldbank.org/en/projects-operations/procurement (API https://search.worldbank.org/api/v2/procnotices)',
                               'record_url': f"https://projects.worldbank.org/en/projects-operations/procurement-detail/{n['id']}", 'retrieved_at': pn['retrieved_at']},
                    'status': status, 'status_basis': basis,
                    'contract': {
                        'identifiers': {'procurement_notice_id': n['id'], 'bid_reference_no': n.get('bid_reference_no'), 'project_id': pid, 'supplier_id': f.get('supplier_id'), 'loan_credit_tf': p.get('loan_info'), 'notice_version': p.get('version')},
                        'title': title, 'description': p.get('scope') if p['kind'] != 'small_contract_award_notice' else None,
                        'instrument_type': 'contract', 'procurement_method': method, 'solicitation_procedure': n.get('procurement_method_code'),
                        'commodity': {'procurement_group': n.get('procurement_group')},
                        'value': price[0]['amount'] if price else None, 'currency': price[0]['currency'] if price else None,
                        'value_detail': {'signed_contract_price': price, 'final_evaluation_price': p.get('final_evaluation_price'), 'bid_price_at_opening': p.get('bid_price_at_opening'), 'evaluated_bid_price': p.get('evaluated_bid_price')},
                        'dates': {'published': parse_date(n.get('noticedate')).isoformat() if parse_date(n.get('noticedate')) else None, 'signed': signed.isoformat() if signed else None,
                                  'start': None, 'end': None, 'end_computed': computed_end.isoformat() if computed_end else None, 'duration': dur,
                                  'award_notification': p.get('award_date'), 'amended_last': None},
                        'related': {'project_url': f"https://projects.worldbank.org/en/projects-operations/project-detail/{pid}" if pid else None},
                    },
                    'buyer': {'name': ' / '.join([x for x in [prec.get('borrower'), prec.get('impagency')] if x]) or f"{n.get('project_ctry_name')} (borrower; implementing agency not published)",
                              'country': iso2_for(n.get('project_ctry_name'), (prec.get('countrycode') or [None])[0] if isinstance(prec.get('countrycode'), list) else None), 'type': 'government (World Bank borrower / implementing agency)',
                              'identifiers': {'project_id': pid, 'project_country': n.get('project_ctry_name')}, 'address': {'country': n.get('project_ctry_name')}, 'contact': {},
                              'borrower': prec.get('borrower'), 'implementing_agency': prec.get('impagency'), 'project_name': n.get('project_name'), 'financier': 'World Bank (IBRD/IDA/TF)'},
                    'vendor': {'name': f.get('name'), 'country': 'CA', 'country_basis': "'Country: Canada' line under Awarded Firm(s)/Bidder(s) in the contract award notice text",
                               'identifiers': {'supplier_id': f.get('supplier_id')}, 'address': {'line1': f.get('address'), 'country': 'Canada'}, 'contact': {},
                               'beneficial_owners': p.get('beneficial_owners')},
                    'raw': {'procurement_notice': n, 'procurement_notice_parsed': p, 'project': proj},
                }
                emit(rec)
        except Exception as e:
            stats['errors'] += 1
            print('ERROR procnotice', n.get('id'), repr(e), file=sys.stderr)
    # ---------------- corporate procurement
    d = json.load(open(os.path.join(dl, 'fone_DS00028_RS00025_canada.json')))
    for i, row in enumerate(d['rows']):
        try:
            stats['corporate_rows'] += 1
            ad = parse_date(row.get('award_date'))
            rec = {
                'record_id': f"worldbank:corporate:{row.get('selection_number')}:{i}",
                'source': {'key': 'worldbank', 'name': 'World Bank Finances One - Corporate Procurement Contract Awards', 'publisher': 'World Bank Group (Corporate Procurement)',
                           'dataset_url': 'https://financesone.worldbank.org/corporate-procurement-contract-awards/DS00028', 'record_url': None, 'retrieved_at': d['retrieved_at']},
                'status': 'end_date_unknown',
                'status_basis': 'Corporate procurement feed publishes award_date and amount only; no end date or duration.',
                'contract': {'identifiers': {'selection_number': row.get('selection_number')}, 'title': row.get('contract_description'), 'description': None, 'instrument_type': 'contract',
                             'procurement_method': None, 'solicitation_procedure': None, 'commodity': {'commodity_category': row.get('commodity_category')},
                             'value': num(row.get('contract_award_amount')), 'currency': 'USD', 'value_detail': {'contract_award_amount': num(row.get('contract_award_amount')), 'fund_source': row.get('fund_source')},
                             'dates': {'published': None, 'signed': ad.isoformat() if ad else None, 'start': None, 'end': None, 'fiscal_quarter': row.get('quarter_and_fiscal_year'), 'amended_last': None},
                             'related': {'dataset_api': 'https://datacatalogapi.worldbank.org/dexapps/fone/api/apiservice?datasetId=DS00028&resourceId=RS00025&type=json&filter=supplier_country%3D%27Canada%27'}},
                'buyer': {'name': f"World Bank Group - {row.get('wbg_organization')} - {row.get('vpu_description')}", 'country': 'US', 'type': 'IGO',
                          'identifiers': {'wbg_organization': row.get('wbg_organization'), 'vpu': row.get('vpu_description')}, 'address': {'city': 'Washington, DC', 'country': 'US'}, 'contact': {}},
                'vendor': {'name': row.get('supplier'), 'country': 'CA', 'country_basis': "supplier_country = 'Canada'; supplier_country_code = CA", 'identifiers': {}, 'address': {'country': 'Canada'}, 'contact': {}},
                'raw': {'finances_one_row': row, 'finances_one_dataset': {'datasetId': 'DS00028', 'resourceId': 'RS00025'}},
            }
            emit(rec)
        except Exception as e:
            stats['errors'] += 1
            print('ERROR corporate', repr(e), file=sys.stderr)
    out.close()
    with open(stats_path, 'w') as f:
        json.dump({'stats': dict(stats), 'excluded': excluded}, f, indent=1, ensure_ascii=False)
    print(json.dumps(dict(stats), indent=1))


if __name__ == '__main__':
    main()

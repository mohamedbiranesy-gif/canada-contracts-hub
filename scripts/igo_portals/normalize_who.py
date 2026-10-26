#!/usr/bin/env python3 -I
"""Normalize WHO awarded-contract rows (output of parse_who.py) for suppliers located in Canada.
Usage: python3 -I normalize_who.py <parsed_rows.json> <who_download_dir> <out_jsonl> <stats_json> <ungm_index_json>
"""
import sys, os, re, json, datetime, collections

rows_fn, dl_dir, out_fn, stats_fn, ungm_fn = sys.argv[1:6]
REF = datetime.date(2026, 10, 25)
data = json.load(open(rows_fn))
rows = data['rows']
ungm = [u for u in json.load(open(ungm_fn)) if u.get('agency') == 'WHO']

# source URLs per file (from the WHO contract-awards page, retrieved 2026-10-25)
SRC = {
 '2015-goods-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2015-goods-awarded-contracts.pdf?sfvrsn=c4b96b6f_3&ua=1',
 '2015-service-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2015-service-awarded-contracts.pdf?sfvrsn=f4f6e4ac_5&ua=1',
 '2016-goods-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2016-goods-awarded-contracts.pdf?sfvrsn=47764014_3&ua=1',
 '2016-service-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2016-service-awarded-contracts.pdf?sfvrsn=4c6f3ace_5&ua=1',
 'goods-awarded-contracts-2017-who.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/goods-awarded-contracts-2017-who.pdf?sfvrsn=cd0f38c2_3&ua=1',
 'service-awarded-contracts-2017.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/service-awarded-contracts-2017.pdf?sfvrsn=a61cb608_5&ua=1',
 '2018-goods-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2018-goods-awarded-contracts.pdf?sfvrsn=37723c38_3&ua=1',
 '2018-service-awarded-contracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2018-service-awarded-contracts.pdf?sfvrsn=aa4f8722_5&ua=1',
 '2019goodsawardedcontracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2019goodsawardedcontracts.pdf?sfvrsn=5d1da887_5&ua=1',
 '2019servicesawardedcontracts.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2019servicesawardedcontracts.pdf?sfvrsn=9d5bdd9a_5&ua=1',
 '2020_contract_awards_goods.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2020_contract_awards_goods.pdf?sfvrsn=50bb0c6f_5',
 '2020_contract_awards_services.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2020_contract_awards_services.pdf?sfvrsn=415befcc_5',
 '2021_contract_awards_goods.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2021_contract_awards_goods.pdf?sfvrsn=9840cf24_5',
 '2021_contract_awards_services.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2021_contract_awards_services.pdf?sfvrsn=79df0a71_5',
 '2022_contract_awards_goods.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2022_contract_awards_goods.pdf?sfvrsn=b806f1d4_3',
 '2022_contract_awards_services.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2022_contract_awards_services.pdf?sfvrsn=24e05aec_3',
 '2023-contract-awards-goods.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2023-contract-awards-goods.pdf?sfvrsn=ee4efa8e_2',
 '2023-contract-award-services.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2023-contract-award-services.pdf?sfvrsn=efd26a52_2',
 '2024-contract-awards-goods-who-unitaid.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2024-contract-awards-goods-who-unitaid.pdf?sfvrsn=d938652c_4',
 '2024-contract-awards-services-who-unitaid.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2024-contract-awards-services-who-unitaid.pdf?sfvrsn=8ebb26cc_4',
 'who-2025_contract_awards_goods.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/who-2025_contract_awards_goods.pdf?sfvrsn=704327e4_1',
 '2025_contract_awards_services_who_unitaid.pdf': 'https://cdn.who.int/media/docs/default-source/procurement/2025_contract_awards_services_who_unitaid.pdf?sfvrsn=306e8f8d_1',
}
RETRIEVED = {}
for fn in SRC:
    p = os.path.join(dl_dir, fn)
    if os.path.exists(p):
        RETRIEVED[fn] = datetime.datetime.fromtimestamp(os.path.getmtime(p), datetime.timezone.utc).isoformat(timespec='seconds')

MON = {m: i for i, m in enumerate(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], 1)}

# per-file day-first / month-first detection for purely numeric dates
def numeric_order(file_rows):
    first_gt = second_gt = 0
    for r in file_rows:
        dt = (r['cells'].get('date_of_contract') or '').strip()
        m = re.match(r'^(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})$', dt)
        if m:
            if int(m.group(1)) > 12: first_gt += 1
            if int(m.group(2)) > 12: second_gt += 1
    if first_gt and not second_gt: return 'DMY'
    if second_gt and not first_gt: return 'MDY'
    return 'DMY' if first_gt >= second_gt else 'MDY'

by_file = collections.defaultdict(list)
for r in rows: by_file[r['file']].append(r)
ORDER = {f: numeric_order(rs) for f, rs in by_file.items()}
year_of_file = {f: int(re.search(r'(20\d\d)', f).group(1)) for f in by_file}

def parse_date(s, fn):
    s = (s or '').strip()
    s = re.sub(r'\s*\$$', '', s)
    m = re.match(r'^(\d{1,2})-([A-Za-z]{3})-(\d{2,4})$', s)
    if m:
        d, mo, y = int(m.group(1)), MON.get(m.group(2).lower()), int(m.group(3))
        if y < 100: y += 2000
        try: return datetime.date(y, mo, d).isoformat()
        except Exception: return None
    m = re.match(r'^(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})$', s)
    if m:
        a, b, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if y < 100: y += 2000
        d, mo = (a, b) if ORDER[fn] == 'DMY' else (b, a)
        if mo > 12 and d <= 12: d, mo = mo, d
        try: return datetime.date(y, mo, d).isoformat()
        except Exception: return None
    return None

def parse_amount(s):
    if not s: return None
    t = s.replace('$', '').replace(' ', '').strip()
    if re.match(r'^\d{1,3}(\.\d{3})+$', t):          # 2020/2021 files use '.' as thousands separator
        t = t.replace('.', '')
    elif re.match(r'^\d{1,3}(,\d{3})*(\.\d+)?$', t):
        t = t.replace(',', '')
    else:
        t = re.sub(r'[^0-9.]', '', t)
    try: return float(t)
    except Exception: return None

stats = collections.Counter()
out = open(out_fn, 'w', encoding='utf-8')
seen_ids = {}
possible_ungm = []
for r in rows:
    c = r['cells']
    fn = r['file']
    cc = (c.get('supplier_country') or '').strip()
    basis = None
    if cc.lower() == 'canada':
        basis = "'Supplier Country' column of the WHO awarded-contracts PDF = 'Canada'"
    elif cc.lower().endswith(' canada') and re.match(r'^(northern ireland|great britain and northern ireland)\s+canada$', cc.lower()):
        basis = f"'Supplier Country' column = 'Canada' (cell text '{cc}': the first words are the wrapped tail of the previous row's country)"
    elif not cc and re.match(r'^Canada\s+\d', (c.get('date_of_contract') or '').strip()):
        basis = "'Supplier Country' value 'Canada' was pushed into the date column by a long supplier name (date cell: '%s')" % c.get('date_of_contract')
    if not basis:
        continue
    stats['canada_rows'] += 1
    ref = (c.get('contract_reference_number') or '').strip()
    mref = re.search(r'\b(\d{9})\b', ref) or re.search(r'\b(\d{9})\b', c.get('purchase_order_for_the_supply_of') or '')
    ref9 = mref.group(1) if mref else r.get('anchor_ref')
    date_raw = c.get('date_of_contract')
    if date_raw and date_raw.strip().startswith('Canada'):
        date_raw_clean = date_raw.strip()[6:].strip()
    else:
        date_raw_clean = date_raw
    signed = parse_date(date_raw_clean, fn)
    if not signed:
        stats['date_unparsed'] += 1
    amount = parse_amount(c.get('contract_amount_usd'))
    name = (c.get('supplier_name') or '').strip() or None
    withheld = bool(name and re.search(r'withheld|witheld', name, re.I))
    is_service = 'service' in fn.lower()
    rid = f"who:{ref9}"
    if rid in seen_ids:
        n = 2
        while f"{rid}-{n}" in seen_ids: n += 1
        rid = f"{rid}-{n}"
        stats['duplicate_reference_numbers'] += 1
    seen_ids[rid] = 1
    office = (c.get('who_office') or '').strip() or None
    buyer_name = 'World Health Organization' + (f' - {office}' if office else '')
    if office and office.upper() == 'UNITAID':
        buyer_name = 'Unitaid (hosted by WHO)'
    desc = c.get('purchase_order_for_the_supply_of') or c.get('service_category')
    # strip a leading 9-digit ref that leaked into the description cell
    if desc: desc = re.sub(r'^\d{9}\s*', '', desc).strip() or None
    title = desc
    for u in ungm:
        if name and u['vendor'] and re.sub(r'[^a-z0-9]', '', u['vendor'].lower())[:8] == re.sub(r'[^a-z0-9]', '', name.lower())[:8]:
            possible_ungm.append({'who_ref': ref9, 'who_name': name, 'who_date': signed, 'ungm': u})
    status = 'end_date_unknown'
    basis_status = "WHO publishes contract reference, date of contract signature/approval and amount only; no end date, term or duration."
    stats[status] += 1
    rec = {
        'record_id': rid,
        'source': {
            'key': 'who',
            'name': 'WHO - Awarded contracts (annual lists of contracts for goods and services)',
            'publisher': 'World Health Organization, Contracting and Procurement Services',
            'dataset_url': 'https://www.who.int/about/accountability/procurement/contract-awards',
            'record_url': None,
            'retrieved_at': RETRIEVED.get(fn),
        },
        'status': status,
        'status_basis': basis_status,
        'contract': {
            'identifiers': {'who_contract_reference_number': ref9, 'purchase_order_number': ref9},
            'title': title,
            'description': desc,
            'instrument_type': (c.get('service_contract_type') or ('service contract / purchase order' if is_service else 'purchase order (goods)')),
            'procurement_method': None,
            'solicitation_procedure': None,
            'commodity': {'who_category': c.get('service_category') or c.get('purchase_order_for_the_supply_of')},
            'value': amount,
            'currency': 'USD' if amount is not None else None,
            'value_detail': {'contract_amount_usd': amount},
            'dates': {'published': None, 'signed': signed, 'start': None, 'end': None, 'end_computed': None, 'amended_last': None},
            'related': {'source_pdf_url': SRC.get(fn), 'source_pdf_file': fn, 'source_pdf_page': r['page']},
        },
        'buyer': {
            'name': buyer_name,
            'country': None,
            'type': 'IGO (UN specialized agency)',
            'identifiers': {'who_office': office},
            'address': {},
            'contact': {},
        },
        'vendor': {
            'name': None if withheld else name,
            'name_withheld': withheld,
            'name_as_published': name,
            'country': 'CA',
            'country_basis': basis,
            'identifiers': {},
            'address': {'country': 'Canada'},
            'contact': {},
        },
        'raw': {
            'pdf_file': fn, 'pdf_page': r['page'], 'row_anchor_top_pt': r['anchor_top'], 'anchor_reference': r.get('anchor_ref'),
            'cells': c, 'header_text': r.get('header_text'), 'columns_detected': r.get('columns'),
            'date_order_assumed_for_numeric_dates': ORDER[fn],
        },
    }
    if withheld: stats['vendor_name_withheld'] += 1
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
out.close()
json.dump({'stats': stats, 'date_order_by_file': ORDER, 'possible_ungm_overlap': possible_ungm, 'per_file_rows': {f: len(rs) for f, rs in by_file.items()}}, open(stats_fn, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(stats, indent=1)); print(ORDER); print('possible ungm overlap', len(possible_ungm))

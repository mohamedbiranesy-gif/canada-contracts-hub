#!/usr/bin/env python3 -I
"""Parse FAO quarterly 'Vendors with total procurement actions over USD 100 000' PDFs and emit
normalized records for POs whose 'Vendor Country' column is Canada.
Usage: python3 -I parse_fao.py <fao_dir> <out_jsonl> <stats_json>
Columns (PO Number | Project Symbol | Project Title | Vendor Name | Vendor Country | General Description | USD Net
Ordered Value) are located from the header words (first page that has them; positions are constant within a
file); words are assigned to columns by x and to PO lines by the nearest line that starts with a PO number.
"""
import sys, os, re, json, glob, datetime, collections, bisect
import pdfplumber

fao_dir, out_fn, stats_fn = sys.argv[1:4]
log = {e['file']: e for e in json.load(open(os.path.join(fao_dir, 'fetch_log.json')))}
PO_RE = re.compile(r'^\d{5,8}$')
ORDER = ['po', 'project_symbol', 'project_title', 'vendor_name', 'vendor_country', 'description', 'usd']

def header_cols(words):
    """Header labels may wrap ('Vendor' / 'Country' on two lines, 'USD' / 'Net' ...). Use the header line that
    holds 'Project Symbol' and read all label positions from it."""
    hw = sorted(words, key=lambda w: (w['top'], w['x0']))
    anchor = None
    for w in hw:
        nxt = [v for v in hw if abs(v['top'] - w['top']) < 3 and 0 <= v['x0'] - w['x1'] < 8]
        if w['text'] == 'Project' and nxt and nxt[0]['text'] == 'Symbol':
            anchor = w; break
    if not anchor: return None
    line = [w for w in hw if abs(w['top'] - anchor['top']) < 3]
    cols = {}
    for w in line:
        t = w['text']
        nxt = [v for v in line if 0 <= v['x0'] - w['x1'] < 8]
        nt = nxt[0]['text'] if nxt else ''
        if t == 'PO': cols['po'] = w['x0']
        elif t == 'Project' and nt == 'Symbol': cols['project_symbol'] = w['x0']
        elif t == 'Project' and nt == 'Title': cols['project_title'] = w['x0']
        elif t == 'Vendor' and nt == 'Name': cols['vendor_name'] = w['x0']
        elif t == 'Vendor' and nt != 'Name': cols['vendor_country'] = w['x0']
        elif t == 'General': cols['description'] = w['x0']
        elif t == 'USD': cols['usd'] = w['x0']
    if 'usd' not in cols:
        # 'USD Net' may sit on the line above/below; take the right-most 'USD' word near the header
        us = [w for w in hw if w['text'] == 'USD' and abs(w['top'] - anchor['top']) < 16 and w['x0'] > cols.get('description', 0)]
        if us: cols['usd'] = us[0]['x0']
    if len([k for k in cols if k in ('project_symbol', 'project_title', 'vendor_name', 'vendor_country', 'description', 'usd')]) >= 6:
        cols.setdefault('po', 0)
        return cols
    return None

def parse_file(fn):
    groups = []
    cur = None
    cols = None
    with pdfplumber.open(fn) as pdf:
        for pno, page in enumerate(pdf.pages):
            words = page.extract_words(x_tolerance=1.5, y_tolerance=2)
            if not words: continue
            hc = header_cols(words)
            if hc: cols = hc
            if not cols: continue
            names = [k for k in ORDER if k in cols]
            bounds = [cols[k] - 2.5 for k in names]
            def col_of(x):
                return names[max(bisect.bisect_right(bounds, x) - 1, 0)]
            # group words into lines by top
            lines = []
            for w in sorted(words, key=lambda w: (round(w['top']), w['x0'])):
                if lines and abs(lines[-1]['top'] - w['top']) < 3: lines[-1]['words'].append(w)
                else: lines.append({'top': w['top'], 'words': [w]})
            hdr_top = None
            if hc:
                hts = [w['top'] for w in words if w['text'] in ('Number', 'Symbol', 'Title', 'Name', 'Country', 'Description', 'Net', 'Vendor', 'Project') and w['top'] < 200]
                hdr_top = max(hts) if hts else None
            for ln in lines:
                if hdr_top is not None and ln['top'] <= hdr_top + 2: continue
                ws = sorted(ln['words'], key=lambda w: w['x0'])
                first = ws[0]
                if first['x0'] < cols['project_symbol'] - 5 and PO_RE.match(first['text']):
                    po = first['text']
                    if len(ws) >= 2 and ws[1]['text'] == 'Total':
                        amt = ws[-1]['text'] if len(ws) >= 3 else None
                        if cur and cur['po'] == po:
                            cur['total'] = amt; groups.append(cur); cur = None
                        continue
                    if cur and cur['po'] != po:
                        groups.append(cur); cur = None
                    if cur is None: cur = {'po': po, 'rows': [], 'page': pno + 1}
                    row = collections.defaultdict(list)
                    for w in ws[1:]: row[col_of(w['x0'])].append(w['text'])
                    cur['rows'].append({'cells': {k: ' '.join(v) for k, v in row.items()}, 'line_text': ' '.join(w['text'] for w in ws), 'top': round(ln['top'], 1), 'page': pno + 1, 'continuation': []})
                elif cur and cur['rows'] and first['x0'] >= cols['project_symbol'] - 5:
                    txt = ' '.join(w['text'] for w in ws)
                    if txt.startswith('This report') or txt.startswith('VENDORS WITH') or 'knowledge as correct' in txt or txt.startswith('presented to the best'):
                        continue
                    row = collections.defaultdict(list)
                    for w in ws: row[col_of(w['x0'])].append(w['text'])
                    cur['rows'][-1]['continuation'].append({'cells': {k: ' '.join(v) for k, v in row.items()}, 'line_text': txt, 'top': round(ln['top'], 1), 'page': pno + 1})
    if cur: groups.append(cur)
    return groups, cols

stats = collections.Counter()
records = []
excluded = []
for fn in sorted(glob.glob(os.path.join(fao_dir, 'fao_*.pdf'))):
    base = os.path.basename(fn)
    m = re.match(r'fao_(\d{4})_(q\d|qx)_(502_vendor|507_service_provider)_', base)
    year, quarter, kind = m.group(1), m.group(2), m.group(3)
    groups, cols = parse_file(fn)
    stats['po_groups_total'] += len(groups)
    for g in groups:
        rows = []
        for r in g['rows']:
            cell = dict(r['cells'])
            for cnt in r['continuation']:
                for k, v in cnt['cells'].items():
                    if v and k != 'po': cell[k] = (cell.get(k, '') + ' ' + v).strip()
            rows.append(cell)
        countries = {re.sub(r'\s+', ' ', r.get('vendor_country', '')).strip() for r in rows}
        vendor_country = ' | '.join(sorted(x for x in countries if x))
        if not re.search(r'\bcanada\b', vendor_country, re.I):
            continue
        stats['po_groups_canada'] += 1
        vendor_name = re.sub(r'\s+', ' ', rows[0].get('vendor_name', '')).strip()
        amounts = []
        for r in rows:
            a = re.sub(r'[^0-9]', '', r.get('usd', ''))
            amounts.append(float(a) if a else None)
        total = float(g['total'].replace(',', '')) if g.get('total') and re.sub(r'[^0-9]', '', g['total']) else (sum(a for a in amounts if a) or None)
        desc = ' || '.join(dict.fromkeys(re.sub(r'\s+', ' ', r.get('description', '')).strip() for r in rows if r.get('description')))
        projects = [{'project_symbol': re.sub(r'\s+', ' ', r.get('project_symbol', '')).strip() or None,
                     'project_title': re.sub(r'\s+', ' ', r.get('project_title', '')).strip() or None,
                     'usd_net_ordered_value': a} for r, a in zip(rows, amounts)]
        q_end = {'q1': '03-31', 'q2': '06-30', 'q3': '09-30', 'q4': '12-31'}.get(quarter)
        stats_page = 'https://www.fao.org/unfao/procurement/statistics/2025statistics/en' if year == '2025' else f'https://www.fao.org/unfao/procurement/statistics/{year}-statistics/en'
        # explicit service period in the description -> ongoing / excluded; 'for <year>' alone -> calendar year
        status, basis_status, end_computed, start_stated = 'end_date_unknown', f"FAO lists PO number, project, vendor, description and USD value for POs issued in {year} {quarter.upper()}; no PO date, start or end date is published.", None, None
        REFD = datetime.date(2026, 10, 25)
        mper = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})\s+to\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})', desc or '')
        myear = re.search(r'\b(?:for|Services for)\s+(20\d\d)\b', desc or '')
        MONS = {m: i for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], 1)}
        if mper:
            start_stated = datetime.date(int(mper.group(3)), MONS[mper.group(1)], int(mper.group(2))).isoformat()
            end_computed = datetime.date(int(mper.group(6)), MONS[mper.group(4)], int(mper.group(5))).isoformat()
            if datetime.date.fromisoformat(end_computed) >= REFD and datetime.date.fromisoformat(start_stated) <= REFD:
                status = 'ongoing'; basis_status = f"Description states the service period '{mper.group(0)}'; {start_stated} <= 2026-10-25 <= {end_computed}."
            else:
                status = 'excluded_ended'; basis_status = f"Description states the service period '{mper.group(0)}' which ends {end_computed} < 2026-10-25."
        elif myear:
            y = int(myear.group(1)); start_stated = f'{y}-01-01'; end_computed = f'{y}-12-31'
            if y == 2026:
                status = 'ongoing_inferred'; basis_status = f"Description says the software/services are 'for {y}' (annual subscription): inferred term {start_stated} to {end_computed}, which contains 2026-10-25."
            elif y < 2026:
                status = 'excluded_ended'; basis_status = f"Description says services are 'for {y}': inferred term ends {end_computed} < 2026-10-25."
        if status == 'excluded_ended':
            stats['excluded_ended_by_stated_period'] += 1
            excluded.append({'po': g['po'], 'vendor': vendor_name, 'desc': desc, 'basis': basis_status})
            continue
        stats[status] += 1
        rec = {
            'record_id': f"fao:{g['po']}",
            'source': {
                'key': 'fao',
                'name': 'FAO Procurement statistics - Vendors with total procurement actions over USD 100 000 (quarterly PO lists)',
                'publisher': 'Food and Agriculture Organization of the United Nations (FAO), Procurement Service (CSDA)',
                'dataset_url': stats_page,
                'record_url': None,
                'retrieved_at': log.get(fn, {}).get('retrieved_at'),
            },
            'status': status,
            'status_basis': basis_status,
            'contract': {
                'identifiers': {'fao_po_number': g['po'], 'project_symbols': [p['project_symbol'] for p in projects if p['project_symbol']]},
                'title': desc[:300] if desc else None,
                'description': desc or None,
                'instrument_type': 'purchase order',
                'procurement_method': None,
                'solicitation_procedure': None,
                'commodity': {},
                'value': total,
                'currency': 'USD',
                'value_detail': {'usd_net_ordered_value_total': total, 'per_project': amounts},
                'dates': {'published': None, 'signed': None, 'start': start_stated, 'end': end_computed if status == 'ongoing' else None, 'end_computed': end_computed, 'reporting_period': f'{year}-{quarter.upper()}', 'reporting_quarter_end': f'{year}-{q_end}' if q_end else None, 'amended_last': None},
                'related': {'source_pdf_url': log.get(fn, {}).get('url'), 'source_pdf_file': base, 'source_pdf_page': g['page'], 'projects': projects},
            },
            'buyer': {'name': 'Food and Agriculture Organization of the United Nations (FAO)', 'country': None, 'type': 'IGO (UN specialized agency)', 'identifiers': {}, 'address': {}, 'contact': {}},
            'vendor': {'name': vendor_name or None, 'country': 'CA', 'country_basis': f"'Vendor Country' column of the FAO PO list = '{vendor_country}'", 'identifiers': {}, 'address': {'country': 'Canada'}, 'contact': {}},
            'raw': {'pdf_file': base, 'year': year, 'quarter': quarter, 'list_kind': kind, 'po_number': g['po'], 'rows': g['rows'], 'merged_rows': rows, 'po_total_line_amount': g.get('total'), 'header_columns_x': cols},
        }
        records.append(rec)
seen = {}
with open(out_fn, 'w', encoding='utf-8') as f:
    for r in records:
        k = r['record_id']
        if k in seen:
            seen[k]['raw'].setdefault('also_listed_in', []).append({'pdf_file': r['raw']['pdf_file'], 'merged_rows': r['raw']['merged_rows'], 'po_total_line_amount': r['raw']['po_total_line_amount']})
            stats['duplicate_po_listings'] += 1
            continue
        seen[k] = r
    for r in seen.values():
        f.write(json.dumps(r, ensure_ascii=False) + '\n'); stats['written'] += 1
json.dump({'stats': stats, 'excluded': excluded}, open(stats_fn, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(stats, indent=1))
for r in seen.values():
    print(r['record_id'], r['raw']['year'], r['raw']['quarter'], '|', r['vendor']['name'], '|', r['contract']['value'], '|', (r['contract']['description'] or '')[:70])

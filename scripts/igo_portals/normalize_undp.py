#!/usr/bin/env python3 -I
"""Parse UNDP contract-award listings (view_awards.cfm HTML, one file per half-year) and emit
normalized records for awards whose 'Country of Contractor' is Canada.
Usage: python3 -I normalize_undp.py <download_dir> <out_jsonl> <stats_json> <ungm_index_json>
"""
import sys, os, re, glob, json, html, datetime, collections

dl, out_fn, stats_fn, ungm_idx_fn = sys.argv[1:5]
REF = datetime.date(2026, 10, 25)
fetch_log = {}
try:
    for e in json.load(open(os.path.join(dl, 'fetch_log.json'))):
        fetch_log[os.path.basename(e['file'])] = e
except Exception:
    pass

ungm = json.load(open(ungm_idx_fn))
ungm_undp = [u for u in ungm if u.get('agency') == 'UNDP']

MON = {m: i for i, m in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 1)}

def parse_date(s):
    """'17-Dec-08' -> 2008-12-17 ; returns ISO string or None"""
    if not s:
        return None
    m = re.match(r'\s*(\d{1,2})-([A-Za-z]{3})-(\d{2,4})\s*$', s)
    if not m:
        return None
    d, mo, y = int(m.group(1)), MON.get(m.group(2).title()), int(m.group(3))
    if not mo:
        return None
    if y < 100:
        y += 2000 if y < 70 else 1900
    try:
        return datetime.date(y, mo, d).isoformat()
    except ValueError:
        return None

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def parse_amount(s):
    if s is None:
        return None
    t = re.sub(r'[^0-9.\-]', '', s.replace(',', ''))
    if t in ('', '-', '.'):
        return None
    try:
        return float(t)
    except ValueError:
        return None

def parse_block(b):
    rec = {}
    m = re.search(r'<h3>(.*?)</h3>', b, re.S)
    rec['title_html'] = m.group(1).strip() if m else None
    rec['title'] = clean(m.group(1)) if m else None
    m = re.search(r'Posted on:</span><br>\s*([^<\n]+)', b)
    rec['posted_on'] = m.group(1).strip() if m else None
    fields = {}
    fields_html = {}
    for cat in re.findall(r'<div class="contractsTable__category">(.*?)</div>\s*(?=<div class="contractsTable__category">|</div>|$)', b, re.S):
        m = re.match(r'\s*<span class="contractsTable__category__title">([^<]*)</span>(.*)', cat, re.S)
        if not m:
            continue
        label = m.group(1).strip().rstrip(':').strip()
        val_html = m.group(2).strip()
        fields_html[label] = val_html
        fields[label] = clean(val_html)
    rec['fields'] = fields
    rec['fields_html'] = fields_html
    links = re.findall(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', b, re.S)
    rec['links'] = [{'href': html.unescape(h), 'text': clean(t)} for h, t in links]
    return rec

# duration / end-date heuristics (conservative; only explicit statements)
DUR_RE = re.compile(r'(?:for a (?:period|duration) of|duration of|period of|term of|valid for|for)\s+(\d{1,2})\s*(year|month)s?', re.I)
UNTIL_RE = re.compile(r'(?:until|till|through|to)\s+(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{4}-\d{2}-\d{2}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})', re.I)

def add_months(d, n):
    y, m = d.year + (d.month - 1 + n) // 12, (d.month - 1 + n) % 12 + 1
    import calendar
    return datetime.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))

def status_for(signed, posted, text):
    base = signed or posted
    if base:
        bd = datetime.date.fromisoformat(base)
        m = DUR_RE.search(text)
        if m:
            n, unit = int(m.group(1)), m.group(2).lower()
            end = add_months(bd, n * (12 if unit == 'year' else 1))
            if end >= REF:
                return 'ongoing_inferred', end.isoformat(), f"No end date published; text states a {n}-{unit} term ('{m.group(0)}'): {'signature' if signed else 'posting'} date {base} + {n} {unit}(s) = {end.isoformat()} >= 2026-10-25."
            return 'excluded_ended', end.isoformat(), f"Text states a {n}-{unit} term ('{m.group(0)}'): {base} + {n} {unit}(s) = {end.isoformat()} < 2026-10-25."
    return 'end_date_unknown', None, "UNDP award listing publishes posting date, signature date and amount only; no end date or term stated."

stats = collections.Counter()
seen = {}
out = open(out_fn, 'w', encoding='utf-8')
excluded = []
dup_ungm = []
for fn in sorted(glob.glob(os.path.join(dl, 'awards_*.html'))):
    h = open(fn, encoding='utf-8', errors='replace').read()
    base = os.path.basename(fn)
    mrange = re.match(r'awards_(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})\.html', base)
    blocks = [b for b in re.split(r'<div class="contractsTable">', h)[1:] if 'contractsTable__row' in b]
    for b in blocks:
        stats['rows_total'] += 1
        rec = parse_block(b)
        f = rec['fields']
        cc = f.get('Country of Contractor')
        if cc is None:
            stats['rows_without_contractor_country'] += 1
            continue
        stats['rows_with_contractor_country'] += 1
        if cc.strip().upper() != 'CANADA':
            continue
        stats['rows_canada'] += 1
        ref = f.get('Contract Reference Number') or ''
        contractor = f.get('Name of Contractor') or ''
        signed = parse_date(f.get('Date of Contract Signature'))
        posted = parse_date(rec['posted_on'])
        key = '|'.join([ref.strip(), contractor.strip().lower(), rec['title'] or '', signed or '', posted or ''])
        if key in seen:
            stats['duplicates_within_source'] += 1
            seen[key]['raw']['duplicate_listing_rows'].append({'file': base, 'block': rec})
            continue
        # UNGM dedup: same agency + same reference, or same vendor + same title
        dup = None
        for u in ungm_undp:
            if (u['ref'] and ref and u['ref'].strip().lower() == ref.strip().lower()) or \
               (u['vendor'].strip().lower() == contractor.strip().lower() and u['title'].strip().lower() == (rec['title'] or '').strip().lower()):
                dup = u
        if dup:
            dup_ungm.append({'undp_ref': ref, 'contractor': contractor, 'title': rec['title'], 'ungm': dup})
            stats['already_covered_by_ungm'] += 1
            continue
        text = ' '.join([rec['title'] or '', f.get('Description of Contract') or ''])
        status, end_computed, basis = status_for(signed, posted, text)
        if status == 'excluded_ended':
            stats['excluded_ended_by_stated_term'] += 1
            excluded.append({'ref': ref, 'contractor': contractor, 'title': rec['title'], 'signed': signed, 'posted': posted, 'end_computed': end_computed, 'basis': basis})
            continue
        stats[status] += 1
        amount_str = f.get('Contract Amount in US') or f.get('Contract Amount in USD')
        amount = parse_amount(amount_str)
        office = f.get('UNDP Office')
        notice = next((l for l in rec['links'] if 'view_notice' in l['href']), None)
        notice_url = ('https://procurement-notices.undp.org/' + notice['href']) if notice else None
        rid_core = re.sub(r'[^A-Za-z0-9]+', '-', ref.strip()).strip('-') if ref.strip() else None
        if not rid_core:
            rid_core = 'noref-' + (signed or posted or 'nodate') + '-' + re.sub(r'[^A-Za-z0-9]+', '-', contractor.lower())[:40].strip('-')
        rid = f"undp:{rid_core}"
        n = 1
        base_rid = rid
        while any(r['record_id'] == rid for r in seen.values()):
            n += 1
            rid = f"{base_rid}-{n}"
        pm = f.get('Procurement Method')
        instrument = 'LTA / framework agreement' if re.search(r'\b(LTA|long[- ]term agreement|framework agreement|acuerdo de larga)', text, re.I) else 'contract'
        record = {
            'record_id': rid,
            'source': {
                'key': 'undp',
                'name': 'UNDP Procurement Notices - Contract Awards',
                'publisher': 'United Nations Development Programme (UNDP)',
                'dataset_url': 'https://procurement-notices.undp.org/view_awards.cfm',
                'record_url': None,
                'retrieved_at': fetch_log.get(base, {}).get('retrieved_at'),
            },
            'status': status,
            'status_basis': basis,
            'contract': {
                'identifiers': {'contract_reference_number': ref or None},
                'title': rec['title'],
                'description': f.get('Description of Contract'),
                'instrument_type': instrument,
                'procurement_method': pm,
                'solicitation_procedure': pm,
                'commodity': {},
                'value': amount,
                'currency': 'USD' if amount is not None else None,
                'value_detail': {'contract_amount_usd': amount},
                'dates': {'published': posted, 'signed': signed, 'start': None, 'end': None, 'end_computed': end_computed, 'amended_last': None},
                'related': {'linked_procurement_notice_url': notice_url, 'linked_procurement_notice_text': notice['text'] if notice else None,
                            'search_query': {'url': 'https://procurement-notices.undp.org/view_awards.cfm', 'method': 'POST',
                                             'date_from1': mrange.group(1) if mrange else None, 'date_to1': mrange.group(2) if mrange else None}},
                'beneficiary_country': f.get('Beneficiary Country'),
            },
            'buyer': {
                'name': ('UNDP - ' + office) if office else 'United Nations Development Programme (UNDP)',
                'country': None,
                'type': 'IGO (UN system organization)',
                'identifiers': {'undp_office': office},
                'address': {},
                'contact': {},
            },
            'vendor': {
                'name': contractor or None,
                'country': 'CA',
                'country_basis': f"'Country of Contractor' field on the UNDP award listing = '{cc.strip()}'",
                'identifiers': {},
                'address': {'country': cc.strip()},
                'contact': {},
            },
            'raw': {
                'listing_file': base,
                'listing_html_block': b.strip(),
                'parsed': rec,
                'duplicate_listing_rows': [],
            },
        }
        seen[key] = record

for r in seen.values():
    out.write(json.dumps(r, ensure_ascii=False) + '\n')
out.close()
json.dump({'stats': stats, 'excluded': excluded, 'already_covered_by_ungm': dup_ungm}, open(stats_fn, 'w'), indent=1, ensure_ascii=False)
print(json.dumps(stats, indent=1))
print('written', len(seen))

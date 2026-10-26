#!/usr/bin/env python3
"""Normalize NZ GETS awarded-tender detail records (details_*.jsonl from crawl_gets.py; raw HTML in
detail/<rfx_id>.html) into the shared record shape: one record per (RFx, awarded supplier located in
Canada). GETS publishes no contract end date, so status is end_date_unknown unless the overview /
title documents a term.

Usage: python3 -I normalize_gets.py <crawl_dir> <out.jsonl> <review.tsv>
"""
import json, glob, os, re, sys, collections, datetime as dt, html

TODAY = dt.date(2026, 10, 25)
SOURCE = {
    'key': 'nz_gets',
    'name': 'GETS - Government Electronic Tenders Service (New Zealand), awarded tender notices',
    'publisher': 'New Zealand Government Procurement (MBIE)',
    'dataset_url': 'https://www.gets.govt.nz/ExternalAwardedTenderList.htm (public Advanced Search, Status=Awarded; detail pages ExternalTenderDetails.htm?id=<RFx ID>)',
}
MONTHS = {m: i for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], 1)}
CA_POSTAL = re.compile(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d\b', re.I)
PROV = re.compile(r'\b(ontario|quebec|qu[ée]bec|british columbia|alberta|manitoba|saskatchewan|nova scotia|new brunswick|'
                  r'newfoundland|prince edward island|yukon|nunavut|northwest territories|ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|YT|NU|NT)\b', re.I)
UK_CANADA_PLACE = re.compile(r'canada\W{0,3}(sq|square|water|house|place|wharf|street|st|road|rd|gate|life|court|lane|way|close|avenue|ave|dock|tower|yard|row|drive|walk|building|wood|quay|hill|works|farm|highway)\b', re.I)

def parse_nz_date(s):
    """'Thursday, 19 November 2026 (Pacific/Auckland UTC+13:00)' or '... 2:33 PM (...)' -> date"""
    if not s: return None
    m = re.search(r'(\d{1,2}) ([A-Z][a-z]+) (\d{4})', s)
    if not m or m.group(2) not in MONTHS: return None
    try:
        return dt.date(int(m.group(3)), MONTHS[m.group(2)], int(m.group(1)))
    except ValueError:
        return None

def split_supplier(entry):
    """'Name - line, line, City, Postcode, COUNTRY' -> (name, address_text, country)"""
    entry = entry.strip()
    name, addr = entry, ''
    m = re.match(r'^(.*?)\s+-\s+(.*)$', entry, flags=re.S)
    if m:
        name, addr = m.group(1).strip(), m.group(2).strip()
    parts = [p.strip() for p in addr.split(',') if p.strip()]
    country = parts[-1] if parts and re.fullmatch(r'[A-Z][A-Z .\'-]{2,}', parts[-1]) else None
    return name, addr, country, parts

def is_canadian(addr, country, parts):
    if country and re.fullmatch(r'CANADA', country.strip(), re.I):
        return True, 'RFx Outcome awarded-supplier address, last (country) token = CANADA', False
    if country:
        # another country named explicitly; override only on hard evidence
        body = ', '.join(parts[:-1])
        if CA_POSTAL.search(body) and PROV.search(body):
            return True, f'awarded-supplier address has Canadian postal code + province but country token = {country!r} (CONFLICT)', True
        return False, '', False
    stripped = UK_CANADA_PLACE.sub('', addr)
    if re.search(r'\bcanada\b', stripped, re.I):
        return True, 'awarded-supplier address text contains "Canada" (no country token)', False
    if CA_POSTAL.search(addr) and PROV.search(addr):
        return True, 'awarded-supplier address has Canadian postal code pattern + province (no country token)', False
    return False, '', False

def term_from_text(*texts):
    """Look for an explicit contract term in free text. Returns (years_or_None, matched_phrase)."""
    t = ' '.join(x for x in texts if x)
    m = re.search(r'(?:initial|contract|agreement)?\s*(?:term|period|duration)\s+(?:of|is|will be)?\s*(?:up to\s*)?(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)\s*(?:\(\d+\)\s*)?(years?|months?)', t, re.I)
    if not m: return None, None
    words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
    n = words.get(m.group(1).lower()) or int(m.group(1))
    months = n * 12 if m.group(2).lower().startswith('year') else n
    return months, m.group(0)

def main():
    crawl_dir, out, review = sys.argv[1], sys.argv[2], sys.argv[3]
    lst = json.load(open(os.path.join(crawl_dir, 'list.json')))
    counts = collections.Counter(); seen = set()
    with open(out, 'w', encoding='utf-8') as o, open(review, 'w', encoding='utf-8') as rv:
        rv.write('decision\tstatus\trfx_id\tsupplier\tcountry_token\taddress\taward_date\torg\ttitle\turl\n')
        for p in sorted(glob.glob(os.path.join(crawl_dir, 'details*.jsonl'))):
            for line in open(p, encoding='utf-8'):
                try:
                    d = json.loads(line)
                except Exception:
                    counts['bad_line'] += 1; continue
                counts['details'] += 1
                det = d.get('detail') or {}
                outcome = det.get('RFx Outcome') or {}
                awarded = outcome.get('awarded_to') or []
                if not awarded:
                    counts['no_awarded_supplier_listed'] += 1; continue
                counts['with_awarded_supplier'] += 1
                row = d.get('list_row') or {}
                cells = row.get('cells') or []
                org = None
                m = re.search(r'\((Pacific/Auckland[^)]*)\)\s*(.*)$', cells[4] if len(cells) > 4 else '')
                if m: org = m.group(2).strip()
                title_tag = det.get('page_title')
                for entry in awarded:
                    name, addr, country, parts = split_supplier(entry)
                    ok, basis, conflict = is_canadian(addr, country, parts)
                    if not ok:
                        continue
                    counts['canadian_supplier_entries'] += 1
                    award_date = parse_nz_date(outcome.get('award_date'))
                    completed = parse_nz_date(outcome.get('completed_updated'))
                    open_date = parse_nz_date(det.get('Open Date'))
                    close_date = parse_nz_date(det.get('Close Date'))
                    anchor = award_date or completed
                    if anchor and anchor > TODAY:
                        counts['excluded_award_date_after_today'] += 1
                        rv.write('\t'.join(['EXCLUDED_future_award', '', d['rfx_id'], name, country or '', addr, str(award_date), org or '', det.get('Tender Name', ''), d['url']]) + '\n')
                        continue
                    months, phrase = term_from_text(det.get('Tender Name'), det.get('Overview'))
                    if months and anchor:
                        y, mo = divmod(anchor.month - 1 + months, 12)
                        inferred_end = dt.date(anchor.year + y, mo + 1, min(anchor.day, 28))
                        if inferred_end < TODAY:
                            counts['excluded_inferred_term_ended'] += 1
                            rv.write('\t'.join(['EXCLUDED_inferred_ended', '', d['rfx_id'], name, country or '', addr, str(award_date), org or '', det.get('Tender Name', ''), d['url']]) + '\n')
                            continue
                        status = 'ongoing_inferred'
                        status_basis = (f'GETS publishes no contract end date; notice text states a term ("{phrase}") = {months} months from award date '
                                        f'{anchor} -> inferred end ~{inferred_end} >= 2026-10-25')
                    else:
                        inferred_end = None
                        status = 'end_date_unknown'
                        status_basis = (f'GETS award notices carry no contract start/end date or value; award date {award_date} '
                                        f'(RFx Outcome "Award Date"), notice completed/updated {completed}; no term stated in the notice text')
                    rid = f"nz_gets:{d['rfx_id']}"
                    if rid in seen:
                        rid = f"{rid}:{re.sub(r'[^A-Za-z0-9]', '', name)[:30]}"
                    seen.add(rid)
                    cats = det.get('Categories_list') or ([det['Categories']] if det.get('Categories') else [])
                    codes = [(c.split(' - ', 1)[0].strip(), c.split(' - ', 1)[1].strip() if ' - ' in c else None) for c in cats if re.match(r'\d{8}', c)]
                    commodity = {}
                    if codes:
                        commodity['unspsc'] = codes[0][0]; commodity['unspsc_description'] = codes[0][1]
                        if len(codes) > 1: commodity['unspsc_additional'] = [c[0] for c in codes[1:]]
                    city = parts[-3] if len(parts) >= 3 else (parts[-2] if len(parts) == 2 else None)
                    postal = next((pp for pp in parts if CA_POSTAL.fullmatch(pp.strip())), None)
                    ttype = det.get('Tender Type') or (cells[3] if len(cells) > 3 else None)
                    rec = {
                        'record_id': rid,
                        'source': dict(SOURCE, record_url=d['url'], retrieved_at=d.get('fetched_at')),
                        'status': status, 'status_basis': status_basis,
                        'contract': {
                            'identifiers': {'rfx_id': d['rfx_id'], 'reference_number': det.get('Reference #'),
                                            'agency_code_in_url': re.search(r'gets\.govt\.nz/([^/]+)/ExternalTenderDetails', d['url']).group(1) if re.search(r'gets\.govt\.nz/([^/]+)/ExternalTenderDetails', d['url']) else None},
                            'title': det.get('Tender Name') or title_tag, 'description': det.get('Overview'),
                            'instrument_type': 'award notice (GETS RFx outcome)' if 'Award Notice' in (ttype or '') else f'awarded tender ({ttype})',
                            'procurement_method': ttype, 'solicitation_procedure': det.get('Exemption Reason'),
                            'commodity': commodity,
                            'value': None, 'currency': 'NZD', 'value_detail': {},
                            'dates': {'published': open_date.isoformat() if open_date else None,
                                      'signed': award_date.isoformat() if award_date else None,
                                      'start': None, 'end': inferred_end.isoformat() if inferred_end else None,
                                      'amended_last': completed.isoformat() if completed else None},
                            'related': {'close_date': close_date.isoformat() if close_date else None, 'regions': det.get('Regions'),
                                        'tender_coverage': det.get('Tender Coverage'), 'required_prequalifications': det.get('Required Pre-qualifications'),
                                        'all_awarded_suppliers': awarded, 'award_window_month': row.get('award_window')},
                        },
                        'buyer': {'name': org, 'country': 'NZ', 'type': 'New Zealand public sector agency (GETS purchaser)',
                                  'identifiers': {}, 'address': {'country': det.get('Agency Address')},
                                  'contact': {'raw': det.get('Contact'), 'department_business_unit': det.get('Department/Business Unit')}},
                        'vendor': {'name': name, 'country': 'CA', 'country_basis': basis, 'country_conflict': conflict,
                                   'identifiers': {},
                                   'address': {'line1': ', '.join(parts[:-3]) if len(parts) > 3 else (parts[0] if parts else None),
                                               'city': city, 'region': None, 'postal_code': postal, 'country': country},
                                   'contact': {}},
                        'raw': {'detail_fields': det, 'list_row': row, 'awarded_supplier_entry': entry,
                                'html_file': f"downloads/nz_gets/crawl/detail/{d['rfx_id']}.html"},
                    }
                    o.write(json.dumps(rec, ensure_ascii=False) + '\n')
                    counts[f'emitted_{status}'] += 1
                    rv.write('\t'.join(['INCLUDED', status, d['rfx_id'], name, country or '', addr, str(award_date), org or '', (det.get('Tender Name') or '')[:80], d['url']]) + '\n')
    counts['list_rows_total'] = len(lst['rows'])
    print(json.dumps(counts, indent=1))

if __name__ == '__main__':
    main()

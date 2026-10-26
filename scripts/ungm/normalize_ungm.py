#!/usr/bin/env python3
"""Normalize UNGM contract awards (supplier country = Canada) to the shared record shape.

Inputs: <dl>/search_summary.json (list rows), <dl>/details/<id>.html (award detail pages).
Usage: python3 -I normalize_ungm.py <dl> <out_jsonl> <stats_json>
"""
import datetime as dt, html, json, os, re, sys
from collections import defaultdict

TODAY = dt.date(2026, 10, 25)
AGENCY_FULL = {}


def clean(s):
    if s is None:
        return None
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s).replace('\xa0', ' ')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip() or None


def parse_date(s):
    if not s:
        return None
    try:
        return dt.datetime.strptime(s.strip(), '%d-%b-%Y').date()
    except ValueError:
        return None


def num(s):
    if not s:
        return None
    try:
        return float(s.replace(',', ''))
    except ValueError:
        return None


DUR_RE = re.compile(r'(?:duration|period|term)\s*(?:of\s*(?:the\s*)?(?:contract|agreement|LTA|assignment))?\s*(?:is|:|of|will be|shall be)?\s*(?:up to\s*|approximately\s*|approx\.\s*)?(\d{1,3})\s*(?:\(\w+\)\s*)?(months?|years?|weeks?|days?)', re.I)
UNTIL_RE = re.compile(r'(?:until|through|up to|valid to|ending|end date[: ]+|expires? (?:on)?)\s*(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4})', re.I)


def parse_detail(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    out = {'fields': {}, 'contacts': [], 'vendors': [], 'countries': [], 'description_html': None, 'unspsc': []}
    # General tab: reportRows before the Contacts tab
    gen_end = t.find('id="Contacts-tab"')
    gen = t[:gen_end] if gen_end > 0 else t
    for lab, val in re.findall(r'<div class="reportRow">\s*<label[^>]*>(.*?)</label>\s*(?:<span[^>]*class="value"[^>]*>(.*?)</span>)?', gen, re.S):
        lab = clean(lab)
        if lab:
            out['fields'][lab] = clean(val)
    m = re.search(r'<div class="raw clear">(.*?)</div>\s*</fieldset>', gen, re.S)
    if m:
        out['description_html'] = m.group(1).strip()
        out['fields']['Description'] = clean(m.group(1))
    m = re.search(r'<legend>Countries or territories</legend>(.*?)</fieldset>', gen, re.S)
    if m:
        out['countries'] = [clean(x) for x in re.findall(r'<div class="formRow clear">\s*(.*?)\s*</div>', m.group(1), re.S) if clean(x)]
    m = re.search(r'id="contractAwardVendorsContainer">(.*?)</div>\s*</p>', t, re.S)
    if m:
        out['vendors'] = [clean(x) for x in re.findall(r'<label>\s*(.*?)\s*</label>', m.group(1), re.S) if clean(x)]
        out['vendors_html'] = m.group(1).strip()
    # contacts
    c_start = t.find('id="Contacts-tab"')
    c_end = t.find('id="UNSPSC-tab"')
    if c_start > 0:
        csec = t[c_start:c_end if c_end > 0 else None]
        for item in re.findall(r'<div class="editableListItem">(.*?)</div>\s*</div>\s*</div>', csec, re.S) or [csec]:
            d = {}
            for lab, val in re.findall(r'<div class="reportRow">\s*<label[^>]*>(.*?)</label>\s*(?:<span[^>]*class="value"[^>]*>(.*?)</span>)?', item, re.S):
                lab = clean(lab)
                if lab:
                    d[lab] = clean(val)
            hd = re.search(r'<strong>\s*(.*?)\s*</strong>', item, re.S)
            if hd:
                d['heading'] = clean(hd.group(1))
            if d:
                out['contacts'].append(d)
    u_start = t.find('id="UNSPSC-tab"')
    if u_start > 0:
        usec = t[u_start:]
        out['unspsc'] = [clean(x) for x in re.findall(r'class="nodeName[^"]*"[^>]*>(.*?)</', usec, re.S) if clean(x)]
    title = re.search(r'<span id="awardTitle" class="value">(.*?)</span>', t, re.S)
    out['title'] = clean(title.group(1)) if title else out['fields'].get('Title')
    return out


def main():
    dl, out_path, stats_path = sys.argv[1:4]
    summ = json.load(open(os.path.join(dl, 'search_summary.json')))
    retrieved = summ['retrieved_at']
    stats = defaultdict(int)
    excluded = []
    with open(out_path, 'w', encoding='utf-8') as out:
        for aid in summ['ids']:
            try:
                path = os.path.join(dl, 'details', f'{aid}.html')
                row = summ['rows'].get(aid) or {}
                cells = [clean(c) for c in row.get('cells_html', [])]
                # list cells: [supplier, award date, agency abbrev, reference, destination(s)]
                list_supplier = cells[0] if len(cells) > 0 else None
                list_award_date = cells[1] if len(cells) > 1 else None
                list_agency = cells[2] if len(cells) > 2 else None
                list_ref = cells[3] if len(cells) > 3 else None
                list_dest = cells[4] if len(cells) > 4 else None
                det = parse_detail(path) if os.path.exists(path) else None
                f = (det or {}).get('fields', {})
                award_date = parse_date(f.get('Award date') or list_award_date)
                desc = f.get('Description')
                title = (det or {}).get('title') or clean(row.get('title_html'))
                # duration heuristics from description text
                status = 'end_date_unknown'
                basis = "UNGM publishes award date and contract value only; no end date or duration field."
                end_computed = None
                text = ' '.join(x for x in [title, desc] if x)
                mu = UNTIL_RE.search(text) if text else None
                md = DUR_RE.search(text) if text else None
                if mu:
                    s = mu.group(1)
                    end = None
                    for fmt in ('%d %B %Y', '%d %b %Y', '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y'):
                        try:
                            end = dt.datetime.strptime(re.sub(r'(\d)(st|nd|rd|th)', r'\1', s), fmt).date()
                            break
                        except ValueError:
                            pass
                    if end:
                        if end >= TODAY and award_date and award_date <= TODAY:
                            status, basis = 'ongoing_inferred', f"Free-text description states the contract runs until {end.isoformat()} (>= 2026-10-25); award date {award_date.isoformat()}. Not a structured field."
                            end_computed = end
                        elif end < TODAY:
                            excluded.append({'id': aid, 'reason': f"description states end {end.isoformat()} < 2026-10-25 (free text)"})
                            stats['excluded_text_end'] += 1
                            continue
                elif md and award_date:
                    v, u = int(md.group(1)), md.group(2).lower()
                    days = {'month': 30.44, 'year': 365.25, 'week': 7, 'day': 1}[u.rstrip('s')]
                    end_computed = award_date + dt.timedelta(days=round(v * days))
                    if end_computed >= TODAY and award_date <= TODAY:
                        status, basis = 'ongoing_inferred', f"Free-text description mentions a duration of {v} {u} ('{md.group(0).strip()}'); computed end = award date {award_date.isoformat()} + duration = {end_computed.isoformat()} >= 2026-10-25. Not a structured field."
                    else:
                        excluded.append({'id': aid, 'reason': f"description duration {v} {u} from award date {award_date.isoformat()} -> computed end {end_computed.isoformat()} < 2026-10-25 (free text)"})
                        stats['excluded_text_duration'] += 1
                        continue
                org_full = f.get('Organization')
                vendors = (det or {}).get('vendors') or ([list_supplier] if list_supplier else [])
                rec = {
                    'record_id': f'ungm:{aid}',
                    'source': {'key': 'ungm', 'name': 'United Nations Global Marketplace (UNGM) - Contract awards', 'publisher': 'UNGM / UN Procurement Division (on behalf of UN organizations)',
                               'dataset_url': 'https://www.ungm.org/Public/ContractAward', 'record_url': f'https://www.ungm.org/Public/ContractAward/{aid}', 'retrieved_at': retrieved},
                    'status': status, 'status_basis': basis,
                    'contract': {
                        'identifiers': {'ungm_contract_award_id': aid, 'reference': f.get('Reference') or list_ref},
                        'title': title, 'description': desc, 'instrument_type': 'contract', 'procurement_method': None, 'solicitation_procedure': None,
                        'commodity': {'unspsc': (det or {}).get('unspsc') or None},
                        'value': num(f.get('Contract value (USD)')), 'currency': 'USD' if f.get('Contract value (USD)') else None,
                        'value_detail': {'contract_value_usd': num(f.get('Contract value (USD)'))},
                        'dates': {'published': None, 'signed': award_date.isoformat() if award_date else None, 'start': None, 'end': None,
                                  'end_computed': end_computed.isoformat() if end_computed else None, 'amended_last': None},
                        'related': {'award_detail_url': f'https://www.ungm.org/Public/ContractAward/{aid}', 'popup_url': f'https://www.ungm.org/Public/ContractAward/Popup/{aid}'},
                        'beneficiary_countries': (det or {}).get('countries') or ([list_dest] if list_dest else []),
                    },
                    'buyer': {'name': org_full or list_agency, 'country': None, 'type': 'IGO (UN system organization)',
                              'identifiers': {'ungm_agency_abbreviation': list_agency}, 'address': {}, 'contact': ((det or {}).get('contacts') or [{}])[0] if det else {}},
                    'vendor': {'name': vendors[0] if vendors else None, 'country': 'CA',
                               'country_basis': 'UNGM contract-award search filter SupplierCountries=[2328] (option value of "Canada" in #selContractAwardSupplierCountry); the detail page itself does not display the vendor country',
                               'identifiers': {}, 'address': {'country': 'Canada'}, 'contact': {}, 'all_vendors': vendors},
                    'raw': {'search_list_row': row, 'search_list_cells': cells, 'detail_parsed': det, 'detail_html_path': path if os.path.exists(path) else None},
                }
                # include full detail HTML main section (trimmed to <main>) so nothing is lost
                if det is not None:
                    t = open(path, encoding='utf-8', errors='replace').read()
                    m = re.search(r'<main.*?</main>', t, re.S)
                    rec['raw']['detail_main_html'] = m.group(0) if m else t
                out.write(json.dumps(rec, ensure_ascii=False) + '\n')
                stats[status] += 1
            except Exception as e:
                stats['errors'] += 1
                print('ERROR', aid, repr(e), file=sys.stderr)
    with open(stats_path, 'w') as fh:
        json.dump({'stats': dict(stats), 'excluded': excluded}, fh, indent=1, ensure_ascii=False)
    print(json.dumps(dict(stats), indent=1))


if __name__ == '__main__':
    main()

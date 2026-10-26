#!/usr/bin/env python3
"""Normalize Canadian Commercial Corporation (CCC) 'Disclosure Report of Signed Transactions'
quarterly PDF tables (transcribed to transactions_transcribed.psv) into the shared record shape.

CCC is Canada's government-to-government contracting agency: the foreign government buyer contracts
with CCC, CCC contracts with the Canadian exporter. The reports give Exporter, Destination (buyer
country), Description (sector) and a CAD amount range; no buyer name, no dates beyond the quarter.

Usage: python3 -I normalize_ccc.py <psv> <out_jsonl> <stats_json>
"""
import datetime as dt, json, re, sys
from collections import defaultdict

TODAY = dt.date(2026, 10, 25)
RETRIEVED = '2026-10-25T14:05:00Z'

DEST_ISO2 = {'United States': 'US', 'Canada': 'CA', 'Germany': 'DE', 'Montenegro': 'ME', 'Dominican Republic': 'DO', 'Portugal': 'PT', 'Netherlands': 'NL',
             'Austria': 'AT', 'Bangladesh': 'BD', 'Belgium': 'BE', 'Romania': 'RO', 'Ecuador': 'EC', 'Italy': 'IT', 'Greece': 'GR', 'Spain': 'ES', 'France': 'FR',
             'Croatia': 'HR', 'Sierra Leone': 'SL', 'South Africa': 'ZA', 'Peru': 'PE', 'Australia': 'AU', 'Chile': 'CL', 'Ukraine': 'UA', 'Colombia': 'CO',
             'Argentina': 'AR', 'Malaysia': 'MY', 'Caribbean': None}
# Destination 'Canada' = the end customer is a foreign government but the goods are delivered in Canada (e.g. US DoD DPSA
# contracts executed in Canada, or sales to foreign governments via Canadian delivery) OR a Government of Canada department
# (CCC also serves as contracting agent for GAC/DND aid procurements). CCC does not say which; buyer name is not disclosed.
BUYER_HINT = {
    'United States': 'U.S. Department of Defense / U.S. federal agencies (via the Canada-U.S. Defence Production Sharing Agreement, DPSA) - buyer identity not disclosed in the report',
    'Caribbean': 'Caribbean government buyer(s) (CCC Caribbean tourism-sector programme) - identity not disclosed',
}


def parse_range(s):
    s = s.replace('–', '-').replace(' to ', ' - ').replace(',', '').replace('$', '')
    m = re.match(r'^\s*<\s*([\d.]+)', s)
    if m:
        return None, float(m.group(1))
    m = re.match(r'^\s*(?:Less than)\s*([\d.]+)', s, re.I)
    if m:
        return None, float(m.group(1))
    m = re.match(r'^\s*>\s*([\d.]+)', s)
    if m:
        return float(m.group(1)), None
    m = re.match(r'^\s*([\d.]+)\s*-\s*([\d.]+)', s)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None


def fiscal_label(start):
    y = start.year if start.month >= 4 else start.year - 1
    q = {4: 1, 7: 2, 10: 3, 1: 4}[start.month]
    return f"FY{y}-{str(y + 1)[-2:]} Q{q}"


def main():
    psv, out_path, stats_path = sys.argv[1:4]
    stats = defaultdict(int)
    excluded = []
    seen = set()
    with open(psv, encoding='utf-8') as fh, open(out_path, 'w', encoding='utf-8') as out:
        header = fh.readline().rstrip('\n').split('|')
        for line in fh:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            parts = line.split('|')
            if len(parts) != 8:
                stats['bad_rows'] += 1
                print('bad row', line[:120], file=sys.stderr)
                continue
            row = dict(zip(header, parts))
            try:
                stats['rows'] += 1
                ps = dt.date.fromisoformat(row['period_start'])
                pe = dt.date.fromisoformat(row['period_end'])
                lo, hi = parse_range(row['amount_range_cad'])
                dest = row['destination'].strip()
                exporter = row['exporter'].strip()
                anonymised = exporter.lower().startswith('canadian exporter')
                rid = f"ccc_canada:{row['period_start']}:{row['row']}"
                if rid in seen:
                    stats['dup_ids'] += 1
                    continue
                seen.add(rid)
                if anonymised:
                    stats['anonymised_exporter'] += 1
                status = 'end_date_unknown'
                basis = f"CCC quarterly disclosure lists transactions signed between {ps.isoformat()} and {pe.isoformat()}; no start/end date, duration or contract number is published."
                if dest == 'Canada':
                    buyer_name = 'Foreign government buyer contracting through CCC, or Government of Canada client department (destination shown as Canada; buyer identity not disclosed)'
                    buyer_country = None
                    buyer_type = 'government (undisclosed)'
                else:
                    buyer_name = BUYER_HINT.get(dest, f"Government of {dest} (buyer identity not disclosed; CCC government-to-government contract)")
                    buyer_country = DEST_ISO2.get(dest)
                    buyer_type = 'foreign government (via CCC government-to-government contract)'
                rec = {
                    'record_id': rid,
                    'source': {'key': 'ccc_canada', 'name': 'Canadian Commercial Corporation - Disclosure Report of Signed Transactions (quarterly)', 'publisher': 'Canadian Commercial Corporation (CCC), Government of Canada Crown corporation',
                               'dataset_url': 'https://www.ccc.ca/en/about/corporate-reports/#transactions', 'record_url': row['report_url'], 'retrieved_at': RETRIEVED},
                    'status': status, 'status_basis': basis,
                    'contract': {
                        'identifiers': {'report_row': int(row['row']), 'report_period': f"{ps.isoformat()}/{pe.isoformat()}", 'fiscal_quarter': fiscal_label(ps)},
                        'title': f"{row['description_en'].strip()} - {exporter} - {dest}",
                        'description': row['description_en'].strip(),
                        'instrument_type': 'contract (CCC government-to-government prime contract with back-to-back domestic contract to the Canadian exporter)',
                        'procurement_method': None, 'solicitation_procedure': None,
                        'commodity': {'ccc_sector_description': row['description_en'].strip()},
                        'value': None, 'currency': 'CAD',
                        'value_detail': {'amount_range_cad': row['amount_range_cad'].strip(), 'range_low_cad': lo, 'range_high_cad': hi},
                        'dates': {'published': None, 'signed': None, 'signed_between': [ps.isoformat(), pe.isoformat()], 'start': None, 'end': None, 'amended_last': None},
                        'related': {'report_pdf': row['report_url'], 'corporate_reports_page': 'https://www.ccc.ca/en/about/corporate-reports/'},
                    },
                    'buyer': {'name': buyer_name, 'country': buyer_country, 'type': buyer_type, 'identifiers': {}, 'address': {'country': dest}, 'contact': {},
                              'destination_as_published': dest, 'contracting_agent': 'Canadian Commercial Corporation (CCC)'},
                    'vendor': {'name': None if anonymised else exporter, 'country': 'CA',
                               'country_basis': "CCC reports list the Canadian exporter party to each government-to-government transaction (CCC contracts only with Canadian exporters; report column 'Exporter / Exportateur'); anonymised rows show 'Canadian Exporter'",
                               'identifiers': {}, 'address': {'country': 'CA'}, 'contact': {}, 'name_as_published': exporter, 'anonymised': anonymised},
                    'raw': row,
                }
                out.write(json.dumps(rec, ensure_ascii=False) + '\n')
                stats[status] += 1
            except Exception as e:
                stats['errors'] += 1
                print('ERROR', line[:100], repr(e), file=sys.stderr)
    with open(stats_path, 'w') as f:
        json.dump({'stats': dict(stats), 'excluded': excluded}, f, indent=1)
    print(json.dumps(dict(stats), indent=1))


if __name__ == '__main__':
    main()

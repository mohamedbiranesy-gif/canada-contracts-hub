import urllib.request
import urllib.parse
import json
import gzip
import datetime
from datetime import datetime as dt, timezone
import time
import sys
import os

def load_config():
    with open('coord/config.json') as f:
        return json.load(f)

config = load_config()
ref_date_str = config['reference_date']
ref_date = dt.strptime(ref_date_str, '%Y-%m-%d').date()

def is_ongoing(start, end, ref_date):
    if not start and not end:
        return 'end_date_unknown', 'No start or end date provided.'

    start_d = None
    if start:
        start_d = dt.strptime(start[:10], '%Y-%m-%d').date()

    end_d = None
    if end:
        end_d = dt.strptime(end[:10], '%Y-%m-%d').date()

    if not end_d:
        if start_d and start_d <= ref_date:
            return 'end_date_unknown', 'No end date provided, but started on or before reference date.'
        else:
            return 'end_date_unknown', 'No end date provided, and started after reference date.'

    if start_d:
        if start_d <= ref_date and end_d >= ref_date:
            return 'ongoing', f'Start date ({start_d}) <= reference date and end date ({end_d}) >= reference date.'
    else:
        if end_d >= ref_date:
            return 'ongoing', f'End date ({end_d}) >= reference date.'

    return None, None

def fetch_data(dataset_id):
    query = urllib.parse.urlencode({
        "$where": "upper(vendor_country) = 'CANADA'",
        "$limit": "100000"
    })
    url = f"https://data.ny.gov/resource/{dataset_id}.json?{query}"
    req = urllib.request.Request(url, headers={'User-Agent': 'contracts-research/1.0'})
    print(f"Fetching {url}")
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

datasets = {
    'ehig-g5x3': 'Procurement Report for State Authorities',
    '8w5p-k45m': 'Procurement Report for Local Authorities',
    'd84c-dk28': 'Procurement Report for Local Development Corporations',
    'p3p6-xqr5': 'Procurement Report for Industrial Development Agencies'
}

def parse_money(s):
    if not s:
        return None
    try:
        return float(s.replace('$', '').replace(',', '').strip())
    except ValueError:
        return None

records = []
seen_ids = set()
for ds_id, ds_name in datasets.items():
    data = fetch_data(ds_id)
    print(f"Found {len(data)} records for {ds_id}")
    for idx, row in enumerate(data):
        # Check ongoing
        start = row.get('begin_date') or row.get('award_date')
        end = row.get('end_date')

        status, status_basis = is_ongoing(start, end, ref_date)
        if not status:
            continue

        record_id = f"ny_procurement_{ds_id}:{row.get('transaction_number', '')}_{row.get('authority_name', '')}_{row.get('vendor_name', '')}_{idx}".replace(' ', '_').lower()
        if record_id in seen_ids:
            continue
        seen_ids.add(record_id)

        record = {
            "record_id": record_id,
            "source": {
                "key": "us_ny_state_authorities_procurement",
                "name": ds_name,
                "publisher": "New York State",
                "dataset_url": f"https://data.ny.gov/dataset/{ds_id}",
                "record_url": None,
                "retrieved_at": dt.now(timezone.utc).isoformat().replace('+00:00', 'Z')
            },
            "status": status,
            "status_basis": status_basis,
            "contract": {
                "identifiers": {"transaction_number": row.get('transaction_number')} if row.get('transaction_number') else {},
                "title": row.get('procurement_description', ''),
                "description": row.get('procurement_description', ''),
                "instrument_type": row.get('type_of_procurement', ''),
                "procurement_method": row.get('award_process', ''),
                "solicitation_procedure": "",
                "commodity": {},
                "value": parse_money(row.get('contract_amount')),
                "currency": "USD",
                "value_detail": {
                    "expended_to_date": parse_money(row.get('amount_expended_to_date')),
                    "fair_market_value": parse_money(row.get('fair_market_value'))
                },
                "dates": {
                    "published": row.get('award_date', '')[:10] if row.get('award_date') else "",
                    "signed": row.get('award_date', '')[:10] if row.get('award_date') else "",
                    "start": row.get('begin_date', '')[:10] if row.get('begin_date') else "",
                    "end": row.get('end_date', '')[:10] if row.get('end_date') else "",
                    "amended_last": ""
                },
                "related": {}
            },
            "buyer": {
                "name": row.get('authority_name', ''),
                "country": "US",
                "type": "state authority",
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "vendor": {
                "name": row.get('vendor_name', ''),
                "country": "CA",
                "country_basis": "vendor_country",
                "identifiers": {},
                "address": {
                    "line1": row.get('vendor_address_1', ''),
                    "city": row.get('vendor_city', ''),
                    "region": row.get('vendor_state', '') or row.get('vendor_province_region', ''),
                    "postal_code": row.get('vendor_postal_code', ''),
                    "country": "CA"
                },
                "contact": {}
            },
            "raw": row,
            "link": f"https://data.ny.gov/dataset/{ds_id}",
            "link_type": "dataset"
        }
        records.append(record)
    time.sleep(1)

out_file = "data/incoming/jules/records_us_ny_state_authorities_procurement.jsonl.gz"
with gzip.open(out_file, "wt", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

print(f"Wrote {len(records)} records to {out_file}")

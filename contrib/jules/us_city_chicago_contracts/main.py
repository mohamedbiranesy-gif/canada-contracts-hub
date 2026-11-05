import urllib.request
import json
import gzip
import os
from datetime import datetime, timezone
import urllib.parse

def get_ref_date():
    try:
        with open('coord/config.json', 'r') as f:
            return json.load(f).get('reference_date', datetime.now(timezone.utc).isoformat()[:10])
    except:
        return datetime.now(timezone.utc).isoformat()[:10]

def fetch_chicago_contracts():
    base_url = "https://data.cityofchicago.org/resource/rsxa-ify5.json"
    where_clause = "state = 'CAN' OR state = 'ON' OR state = 'QC' OR state = 'BC' OR state = 'AB' OR state = 'MB' OR state = 'SK' OR state = 'NS' OR state = 'NB' OR state = 'NL' OR state = 'PE' OR state = 'YT' OR state = 'NT' OR state = 'NU'"

    url = f"{base_url}?$where={urllib.parse.quote(where_clause)}&$limit=50000"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def process_contracts(data, ref_date):
    records = []
    retrieved_at = datetime.now(timezone.utc).isoformat()

    for row in data:
        # Determine status
        start = row.get('start_date', '')
        end = row.get('end_date', '')
        status = 'end_date_unknown'
        status_basis = 'No explicit end date'

        if start and end:
            try:
                # As Chicago dates are like 2015-11-12T00:00:00.000
                if start[:10] <= ref_date and end[:10] >= ref_date:
                    status = 'ongoing'
                    status_basis = f'start ({start[:10]}) <= ref <= end ({end[:10]})'
                elif end[:10] < ref_date:
                    status = 'ended'
                    status_basis = f'end ({end[:10]}) < ref'
                elif start[:10] > ref_date:
                    # Future contract is not ongoing per strict rule 3, but rule says "Exclude: end date < ref_date, cancelled...".
                    # We will drop future contracts as they are not currently ongoing per "ongoing = start <= reference date".
                    status = 'future'
                    status_basis = f'start ({start[:10]}) > ref'
            except Exception:
                pass

        # Exclude ended or future
        if status in ['ended', 'future']:
            continue

        record_id = f"us_city_chicago_contracts:{row.get('purchase_order_contract_number', '')}_{row.get('revision_number', '')}"

        # Amount formatting
        try:
            val = float(row.get('award_amount', 0))
        except:
            val = None

        # Build normalized record
        rec = {
            "record_id": record_id,
            "source": {
                "key": "us_city_chicago_contracts",
                "name": "City of Chicago Contracts",
                "publisher": "City of Chicago",
                "dataset_url": "https://data.cityofchicago.org/d/rsxa-ify5",
                "record_url": None,
                "retrieved_at": retrieved_at
            },
            "status": status,
            "status_basis": status_basis,
            "contract": {
                "identifiers": {
                    "purchase_order": row.get('purchase_order_contract_number'),
                    "specification_number": row.get('specification_number')
                },
                "title": row.get('purchase_order_description', ''),
                "description": "",
                "instrument_type": row.get('contract_type', ''),
                "procurement_method": "",
                "solicitation_procedure": "",
                "commodity": {},
                "value": val,
                "currency": "USD",
                "value_detail": {},
                "dates": {
                    "published": "",
                    "signed": row.get('approval_date', '')[:10] if row.get('approval_date') else "",
                    "start": start[:10] if start else "",
                    "end": end[:10] if end else "",
                    "amended_last": ""
                },
                "related": {}
            },
            "buyer": {
                "name": row.get('department', 'City of Chicago'),
                "country": "US",
                "type": "city",
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "vendor": {
                "name": row.get('vendor_name', ''),
                "country": "CA",
                "country_basis": "state column",
                "identifiers": {
                    "vendor_id": row.get('vendor_id', '')
                },
                "address": {
                    "line1": row.get('address_1', ''),
                    "city": row.get('city', ''),
                    "region": row.get('state', ''),
                    "postal_code": row.get('zip', ''),
                    "country": "CA"
                },
                "contact": {}
            },
            "raw": row,
            "link": "https://data.cityofchicago.org/d/rsxa-ify5",
            "link_type": "dataset"
        }

        # Clean up None/empty values in identifiers
        rec['contract']['identifiers'] = {k: v for k, v in rec['contract']['identifiers'].items() if v}
        rec['vendor']['identifiers'] = {k: v for k, v in rec['vendor']['identifiers'].items() if v}

        records.append(rec)

    return records

def main():
    ref_date = get_ref_date()
    print(f"Fetching Chicago contracts with reference date {ref_date}...")
    data = fetch_chicago_contracts()
    print(f"Total Canada records found: {len(data)}")

    records = process_contracts(data, ref_date)
    print(f"Ongoing/Unknown-end records: {len(records)}")

    out_dir = "data/incoming/jules"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "records_us_city_chicago_contracts.jsonl.gz")

    with gzip.open(out_path, 'wt', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r) + '\n')

    print(f"Wrote {len(records)} records to {out_path}")

if __name__ == "__main__":
    main()

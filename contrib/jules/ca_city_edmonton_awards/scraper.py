import urllib.request
import json
import gzip
import datetime
from pathlib import Path

def fetch_data():
    all_data = []
    limit = 50000
    offset = 0
    while True:
        url = f"https://data.edmonton.ca/resource/gnse-cass.json?$limit={limit}&$offset={offset}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            batch = json.loads(response.read().decode())
            if not batch:
                break
            all_data.extend(batch)
            if len(batch) < limit:
                break
            offset += limit
    return all_data

def is_canada_vendor(vendor_name):
    if not vendor_name:
        return False
    name = str(vendor_name).lower()
    return any(kw in name for kw in ['canada', 'edmonton', 'calgary', 'alberta', ' ab.'])

def parse_date(date_str):
    if not date_str:
        return None
    try:
        return date_str.split('T')[0]
    except:
        return None

def main():
    out_dir = Path("data/incoming/jules")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "records_ca_city_edmonton_awards.jsonl.gz"

    reference_date = "2026-10-25"
    with open("coord/config.json", "r") as f:
        config = json.load(f)
        reference_date = config.get("reference_date", reference_date)

    data = fetch_data()

    records = []
    for i, row in enumerate(data):
        vendor_name = row.get("supplier_name", "")
        if not is_canada_vendor(vendor_name):
            continue

        end_date = parse_date(row.get("validity_period_end"))
        if not end_date:
            status = "end_date_unknown"
        elif end_date >= reference_date:
            status = "ongoing"
        else:
            status = "end_date_unknown"

        start_date = parse_date(row.get("validity_period_start"))
        record_id = f"ca_city_edmonton_awards:{row.get('outline_agreement', f'row-{i}')}"

        records.append({
            "record_id": record_id,
            "source_url": "https://data.edmonton.ca/api/views/gnse-cass/rows.json?accessType=DOWNLOAD",
            "source": {
                "key": "ca_city_edmonton_awards",
                "name": "City of Edmonton Hired Equipment Contracts",
                "publisher": "City of Edmonton",
                "dataset_url": "https://data.edmonton.ca/Purchasing/Hired-Equipment-Contracts-over-10-000/gnse-cass",
                "record_url": "https://data.edmonton.ca/resource/gnse-cass.json",
                "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            },
            "buyer": {
                "name": "City of Edmonton",
                "country": "CA",
                "type": "city"
            },
            "vendor": {
                "name": vendor_name,
                "country": "CA",
                "country_basis": "Derived from supplier_name matching local Canada/Alberta keyword"
            },
            "contract": {
                "identifiers": {
                    "outline_agreement": row.get("outline_agreement")
                },
                "title": row.get("purchasing_document_description") or "Hired Equipment Contract",
                "description": row.get("purchasing_document_description") or "",
                "instrument_type": "contract",
                "procurement_method": "",
                "solicitation_procedure": "",
                "commodity": {},
                "value": None,
                "currency": "CAD",
                "value_detail": {},
                "dates": {
                    "published": "",
                    "signed": "",
                    "start": start_date or "",
                    "end": end_date or "",
                    "amended_last": ""
                },
                "related": {}
            },
            "title": row.get("purchasing_document_description") or "Hired Equipment Contract",
            "description": row.get("purchasing_document_description") or "",
            "status": status,
            "status_basis": "ongoing" if status == "ongoing" else "unknown or historical end date",
            "reference_number": row.get("outline_agreement"),
            "start_date": start_date,
            "end_date": end_date,
            "link": "https://data.edmonton.ca/resource/gnse-cass.json",
            "link_type": "source",
            "raw": row
        })

    print(f"Extracted {len(records)} records")

    with gzip.open(out_file, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    main()

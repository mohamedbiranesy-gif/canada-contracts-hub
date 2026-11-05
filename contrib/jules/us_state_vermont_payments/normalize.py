import json
import gzip
import os
import urllib.request
import urllib.parse
from datetime import datetime, timezone

URL = "https://data.vermont.gov/resource/786x-sbp3.json"
PROVINCES = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'YT', 'NT', 'NU']
LIMIT = 50000

def main():
    records = []

    where_clause = " OR ".join([f"state='{p}'" for p in PROVINCES])
    query = f"?$where={urllib.parse.quote(where_clause)}&$limit={LIMIT}&$offset=0"
    req_url = URL + query

    req = urllib.request.Request(req_url, headers={'User-Agent': 'CanadaContractsHub/1.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))

    for idx, row in enumerate(data):
        buyer_name = row.get("govtunit", "").strip()
        if buyer_name and not buyer_name.upper().startswith("STATE OF VERMONT"):
             buyer_name = "State of Vermont - " + buyer_name
        elif not buyer_name:
             buyer_name = "State of Vermont"

        vendor_name = row.get("vendor", "").strip()
        if not vendor_name:
            continue

        qtrending = row.get("qtrending", "")
        end_date = qtrending.split("T")[0] if qtrending else ""

        amt = row.get("amt", "")
        vno = row.get("vno", "")
        record_id = f"VT-PAY-{vno}-{qtrending}-{amt}-{idx}"

        record = {
            "record_id": record_id,
            "title": row.get("description", "Vendor Payment"),
            "description": row.get("account", ""),
            "source": {
                "key": "us_state_vermont_payments",
                "name": "Vermont Vendor Payments",
                "publisher": "State of Vermont",
                "dataset_url": "https://data.vermont.gov/d/786x-sbp3",
                "record_url": None,
                "retrieved_at": datetime.now(timezone.utc).isoformat()
            },
            "buyer": {
                "name": buyer_name
            },
            "vendor": {
                "name": vendor_name,
                "city": row.get("city", ""),
                "state_or_province": row.get("state", ""),
                "country": "CA",
                "country_basis": "vendor_state"
            },
            "value": {
                "amount": amt,
                "currency": "USD"
            },
            "start_date": "",
            "end_date": end_date,
            "status": "end_date_unknown",
            "status_basis": "payment_date",
            "link": "https://data.vermont.gov/d/786x-sbp3",
            "link_type": "dataset",
            "raw": row,
            "cross_source_matches": []
        }
        records.append(record)

    out_dir = "data/incoming/jules"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "records_us_state_vermont_payments.jsonl.gz")

    with gzip.open(out_path, 'wt', encoding='utf-8') as f:
        for rec in records:
            f.write(json.dumps(rec) + '\n')

    print(f"Wrote {len(records)} records to {out_path}")

if __name__ == '__main__':
    main()

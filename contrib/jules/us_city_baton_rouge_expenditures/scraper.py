import urllib.request
import json
import gzip
import os
import hashlib

from datetime import datetime, timezone

ds = "vwa8-ps2a"
url = f"https://data.brla.gov/resource/{ds}.json?$where=vendor_state%20in%20('ON',%20'QC',%20'BC',%20'AB',%20'MB',%20'SK',%20'NS',%20'NB',%20'NL',%20'PE',%20'YT',%20'NT',%20'NU')&$limit=50000"

records = []
try:
    with urllib.request.urlopen(url) as response:
        records = json.loads(response.read().decode())
except Exception as e:
    print("Error", e)

print(f"Found {len(records)} potential Canadian records.")

out_dir = "data/incoming/jules"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "records_us_city_baton_rouge_expenditures.jsonl.gz")

processed_records = []
for row in records:
    date_str = row.get("check_date", "")[:10] if row.get("check_date") else None
    val = float(row.get("invoice_line_item_amount", "0"))

    buyer_name = "City of Baton Rouge"
    dept = row.get("department", "").strip()
    if dept:
        buyer_name += f" - {dept}"

    row_hash = hashlib.md5(json.dumps(row, sort_keys=True).encode("utf-8")).hexdigest()[:10]

    rec = {
        "record_id": f"us_city_baton_rouge_expenditures:{row.get('check_number', '')}-{row.get('invoice_number', '')}-{row.get('line_number', '')}-{row_hash}",
        "link": f"https://data.brla.gov/d/{ds}",
        "link_type": "source",
        "source": {
            "key": "us_city_baton_rouge_expenditures",
            "name": "City-Parish Expenditures",
            "publisher": "City of Baton Rouge / Parish of East Baton Rouge",
            "dataset_url": "https://data.brla.gov/",
            "record_url": None,
            "retrieved_at": datetime.now(timezone.utc).isoformat()
        },
        "contract": {
            "title": f"Payment to {row.get('vendor_name_1', '')} for {row.get('expense_category', '')}",
            "description": f"Fund: {row.get('fund', '')}",
            "value": val,
            "currency": "USD",
            "dates": {
                "start": date_str,
                "end": date_str
            },
            "identifiers": {
                "check_number": row.get('check_number', ''),
                "invoice_number": row.get('invoice_number', ''),
                "source_document_number": row.get("source_document_number", "")
            }
        },
        "buyer": {
            "name": buyer_name,
            "country": "US"
        },
        "vendor": {
            "name": row.get("vendor_name_1", "").strip(),
            "country": "CA",
            "country_basis": f"vendor_state is {row.get('vendor_state')}"
        },
        "status": "end_date_unknown",
        "status_basis": "Checkbook payment line with no contract end date specified.",
        "raw": row
    }
    processed_records.append(rec)

with gzip.open(out_path, "wt", encoding="utf-8") as f:
    for rec in processed_records:
        f.write(json.dumps(rec) + "\n")

print(f"Wrote {len(processed_records)} records to {out_path}")

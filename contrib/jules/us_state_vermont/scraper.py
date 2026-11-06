import urllib.request
import json
import gzip
import os
import hashlib

from datetime import datetime, timezone

datasets = ["786x-sbp3", "w4us-y6js", "kngi-j45t", "e7ne-x7k2", "9t8z-fmfj", "i558-vamq"]

records = []
for ds in datasets:
    url = f"https://data.vermont.gov/resource/{ds}.json?$where=state%20in%20('ON',%20'QC',%20'BC',%20'AB',%20'MB',%20'SK',%20'NS',%20'NB',%20'NL',%20'PE',%20'YT',%20'NT',%20'NU')&$limit=50000"

    try:
        with urllib.request.urlopen(url) as response:
            ds_records = json.loads(response.read().decode())
            for row in ds_records:
                row["_dataset_id"] = ds
            records.extend(ds_records)
    except Exception as e:
        print("Error fetching", ds, e)

print(f"Found {len(records)} potential Canadian records.")

out_dir = "data/incoming/jules"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "records_us_state_vermont.jsonl.gz")

processed_records = []
for row in records:
    date_str = row.get("qtrending", "")[:10] if row.get("qtrending") else None
    val = float(row.get("amt", "0"))

    buyer_name = "State of Vermont"
    dept = row.get("govtunit", "").strip()
    if dept:
        buyer_name += f" - {dept}"

    row_hash = hashlib.md5(json.dumps(row, sort_keys=True).encode("utf-8")).hexdigest()[:10]

    rec = {
        "record_id": f"us_state_vermont:{row.get('qtrending', '')[:10]}-{row.get('vno', '')}-{row.get('account', '')}-{row.get('objcode', '')}-{row_hash}",
        "link": f"https://data.vermont.gov/d/{row.get('_dataset_id')}",
        "link_type": "source",
        "source": {
            "key": "us_state_vermont",
            "name": "Vermont Vendor Payments",
            "publisher": "State of Vermont",
            "dataset_url": "https://data.vermont.gov/",
            "record_url": None,
            "retrieved_at": datetime.now(timezone.utc).isoformat()
        },
        "contract": {
            "title": f"Payment to {row.get('vendor', '')} for {row.get('account', '')}",
            "description": f"Fund: {row.get('fund_description', '')} / Dept: {row.get('description', '')}",
            "value": val,
            "currency": "USD",
            "dates": {
                "start": date_str,
                "end": date_str
            },
            "identifiers": {}
        },
        "buyer": {
            "name": buyer_name,
            "country": "US"
        },
        "vendor": {
            "name": row.get("vendor", "").strip(),
            "country": "CA",
            "country_basis": f"state is {row.get('state')}"
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

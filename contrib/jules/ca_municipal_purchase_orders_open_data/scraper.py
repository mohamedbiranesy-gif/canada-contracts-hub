import requests
import json
import gzip
import csv
import os
import hashlib
from datetime import datetime, timezone
import sys

# Reference date for ongoing calculation
with open("coord/config.json", "r") as f:
    config = json.load(f)
ref_date_str = config.get("reference_date", "2026-10-25")
ref_date = datetime.strptime(ref_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)

# Load verified Canadian vendor dictionary
def load_vendors():
    vendors = set()
    with gzip.open("contrib/claude/buyer_pages/vendors_ca.tsv.gz", "rt", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if row:
                vendors.add(row[0].lower().strip())
    return vendors

ca_vendors = load_vendors()

datasets = [
    ("y9rm-5xha", "Purchase Orders Over $10,000", "create_date", "dollar_value_category"),
    ("ydv5-y4pu", "Outline Agreements over $10,000", "validity_period_end", "dollar_value_category"),
    ("gnse-cass", "Hired Equipment Contracts over $10,000", "validity_period_end", "dollar_value_category")
]

out_dir = "data/incoming/jules"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "records_ca_municipal_purchase_orders_open_data.jsonl.gz")

total_rows = 0
canadian_rows = 0
ongoing_rows = 0

with gzip.open(out_file, "wt", encoding="utf-8") as out:
    for dataset_id, dataset_name, date_col, val_col in datasets:
        offset = 0
        limit = 5000
        while True:
            # $select=* to get all fields, plus :id for the unique row ID
            url = f"https://data.edmonton.ca/resource/{dataset_id}.json?$limit={limit}&$offset={offset}&$order=:id&$select=*,:id"
            try:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                print(f"Error fetching {url}: {e}", file=sys.stderr)
                break

            if not data:
                break

            for row in data:
                total_rows += 1
                supplier = row.get("supplier_name", "")
                if not supplier:
                    continue

                # Check vendor
                if supplier.lower().strip() not in ca_vendors:
                    continue

                canadian_rows += 1

                # Check status
                date_val = row.get(date_col)
                status = "end_date_unknown"
                status_basis = f"published {date_col} provided but no explicit end date for PO"
                if date_val:
                    try:
                        d = datetime.strptime(date_val[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
                        if "end" in date_col.lower():
                            if d >= ref_date:
                                status = "ongoing"
                                status_basis = f"{date_col} >= {ref_date_str}"
                            else:
                                status = "end_date_unknown"
                                status_basis = f"{date_col} < {ref_date_str}"
                    except ValueError:
                        pass

                if status == "ongoing":
                     ongoing_rows += 1

                po_number = row.get(":id")

                record = {
                    "record_id": f"ca_municipal_purchase_orders_open_data:{dataset_id}:{po_number}",
                    "source": {
                        "key": "ca_municipal_purchase_orders_open_data",
                        "name": f"Edmonton {dataset_name}",
                        "publisher": "City of Edmonton",
                        "dataset_url": f"https://data.edmonton.ca/d/{dataset_id}",
                        "record_url": None,
                        "retrieved_at": datetime.now(timezone.utc).isoformat()
                    },
                    "status": status,
                    "status_basis": status_basis,
                    "contract": {
                        "identifiers": {"po_number": po_number},
                        "title": row.get("description", ""),
                        "description": row.get("description", ""),
                        "instrument_type": row.get("purchase_order_type", "purchase order"),
                        "procurement_method": None,
                        "solicitation_procedure": None,
                        "commodity": {},
                        "value": None,
                        "currency": "CAD",
                        "value_detail": {},
                        "dates": {
                            "start": date_val[:10] if date_val and "end" not in date_col.lower() else None,
                            "end": date_val[:10] if date_val and "end" in date_col.lower() else None
                        },
                        "related": {}
                    },
                    "buyer": {
                        "name": "City of Edmonton",
                        "country": "CA",
                        "type": "city",
                        "identifiers": {},
                        "address": {},
                        "contact": {}
                    },
                    "vendor": {
                        "name": supplier,
                        "country": "CA",
                        "country_basis": "matched to verified Canadian vendor dictionary contrib/claude/buyer_pages/vendors_ca.tsv.gz",
                        "identifiers": {},
                        "address": {},
                        "contact": {}
                    },
                    "raw": row,
                    "link": f"https://data.edmonton.ca/d/{dataset_id}",
                    "link_type": "dataset"
                }

                val_str = row.get(val_col)
                if val_str:
                    record["raw"][val_col] = val_str

                out.write(json.dumps(record) + "\n")

            offset += limit

print(f"Total rows: {total_rows}")
print(f"Canadian rows: {canadian_rows}")
print(f"Ongoing rows: {ongoing_rows}")

# Save counts to a file for easy reading later
with open("contrib/jules/ca_municipal_purchase_orders_open_data/counts.json", "w") as f:
    json.dump({"total_rows": total_rows, "canadian_rows": canadian_rows, "ongoing_rows": ongoing_rows}, f)

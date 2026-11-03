#!/usr/bin/env python3
import sys
import os
import csv
import json
import hashlib
import urllib.request
import urllib.parse
from datetime import datetime
import gzip

sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_state_portals"

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

def normalize_w64c_ndf7(row):
    # Determine canadian
    state = row.get("vendor_state", "")
    country = row.get("vendor_country", "")  # May not exist, but let's be safe

    prov = norm_prov(state)
    basis = None
    is_ca = False

    if country.upper() in COUNTRY_CA:
        is_ca = True
        basis = f"Vendor Country = '{country}'"
    elif state.upper() == "CAN" or state.upper() == "CANADA":
        is_ca = True
        basis = f"Vendor State = '{state}'"
    elif prov:
        is_ca = True
        basis = f"Vendor State is Canadian province '{state}'"
    elif is_ca_postal(row.get("vendor_zip")):
        is_ca = True
        basis = f"Vendor Zip is Canadian format '{row.get('vendor_zip')}'"

    if not is_ca:
        return None

    # Status
    start = parse_date(row.get("contract_start_date"))
    end = parse_date(row.get("contract_end_date")) or parse_date(row.get("contract_termination_date"))

    status, status_basis = status_from_dates(start, end, future_start_ok=True)
    if not status:
        return None

    rid = row.get("sales_fact_number", "")
    if not rid:
        # Fallback
        rid = hashlib.sha1(str(row).encode('utf-8')).hexdigest()[:16]

    amt = parse_amount(row.get("purchase_amount"))

    contract = contract_block(
        identifiers={"sales_fact_number": row.get("sales_fact_number"), "contract_number": row.get("contract_number")},
        title=row.get("rfo_description"),
        description=row.get("rfo_description"),
        instrument_type=row.get("contract_type"),
        commodity={"brand_name": row.get("brand_name"), "staffing_technology": row.get("staffing_technology")},
        value=amt,
        dates={"start": start, "end": end}
    )

    buyer = buyer_block(
        name=row.get("customer_name"),
        btype=row.get("customer_type"),
        country="US",
        address={"city": row.get("customer_city"), "region": row.get("customer_state"), "postal_code": row.get("customer_zip")}
    )

    vendor = vendor_block(
        name=row.get("vendor_name"),
        basis=basis,
        address={"city": row.get("vendor_city"), "region": state, "postal_code": row.get("vendor_zip"), "line1": row.get("vendor_address")}
    )

    rec = record(
        source_key=SOURCE_KEY,
        source_name="ARCHIVE DIR Cooperative Contract Sales Data Fiscal 2010 To 2025",
        publisher="Texas Department of Information Resources",
        dataset_url="https://data.texas.gov/d/w64c-ndf7",
        record_url=None,
        retrieved_at=now_iso(),
        rid=f"w64c-ndf7-{rid}",
        status=status,
        basis=status_basis,
        contract=contract,
        buyer=buyer,
        vendor=vendor,
        raw=row
    )

    # Missing link required by SCHEMA.md validator
    rec['link'] = f"https://data.texas.gov/d/w64c-ndf7"
    rec['link_type'] = "dataset"
    return rec

def fetch_socrata_with_soql(dataset_id, domain, normalize_fn, out_path, limit=50000):
    print(f"Processing {dataset_id}")
    provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT", "CAN", "CANADA"]

    with gzip.open(out_path, "at", encoding="utf-8") as f:
        for prov in provinces:
            offset = 0
            while True:
                # Proper encoding of URL parameters, avoiding escape issues
                query = urllib.parse.urlencode({
                    "$where": f"vendor_state='{prov}'",
                    "$limit": limit,
                    "$offset": offset
                })
                url = f"https://{domain}/resource/{dataset_id}.json?{query}"
                print(f"Fetching {prov} offset {offset}...")
                try:
                    data = fetch_json(url)
                    for row in data:
                        rec = normalize_fn(row)
                        if rec:
                            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    if len(data) < limit:
                        break
                    offset += limit
                except Exception as e:
                    print(f"Error fetching {prov}: {e}")
                    break

def main():
    out_file = "data/incoming/jules/records_us_state_portals.jsonl.gz"
    if os.path.exists(out_file):
        os.remove(out_file)

    fetch_socrata_with_soql("w64c-ndf7", "data.texas.gov", normalize_w64c_ndf7, out_file)

if __name__ == "__main__":
    main()

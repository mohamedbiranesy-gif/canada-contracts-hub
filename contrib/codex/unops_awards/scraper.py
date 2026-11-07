import urllib.request
import urllib.error
import urllib.parse
import gzip
import json
import time
from datetime import datetime, timezone
import sys

BASE_URL = "https://api.data.dev.unops.org/api/v1/unops-data-dev/journey_project_contract_table_001"
LIMIT = 10000

def fetch_page(offset):
    # Sort by Approval_Date or Contract so we can actually page through
    url = f"{BASE_URL}?_limit={LIMIT}&_offset={offset}&_sort=Contract"
    req = urllib.request.Request(url, headers={
        "Accept-Encoding": "gzip",
        "User-Agent": "Mozilla/5.0"
    })

    for attempt in range(3):
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            if resp.info().get('Content-Encoding') == 'gzip':
                data = gzip.decompress(resp.read())
            else:
                data = resp.read()
            # Be polite to the server on success as well
            time.sleep(0.5)
            return json.loads(data)
        except Exception as e:
            print(f"Error fetching offset {offset} (attempt {attempt+1}): {e}")
            time.sleep(2)
    return None

def normalize(item):
    # Determine vendor country
    country = item.get("Supplier_Country")
    if not country:
        country_desc = item.get("Supplier_Country_Description", "").upper()
        if country_desc == "CANADA":
            country = "CA"

    # Filter for Canada
    if country != "CA" and item.get("Supplier_Country_Description", "").upper() != "CANADA":
        return None

    # Determine status (end_date_unknown since no end date provided)
    status = "end_date_unknown"
    status_basis = "Source publishes awards but no end date."

    # Dates
    start_date = item.get("Approval_Date", "")

    # Clean amount
    amount_str = str(item.get("Procurement_Amount", ""))
    amount = None
    if amount_str:
        try:
            amount = float(amount_str)
        except ValueError:
            pass

    # Clean timestamp
    retrieved_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    record = {
        "record_id": f"unops_awards:{item.get('Contract')}",
        "source": {
            "key": "unops_awards",
            "name": "UNOPS contract awards",
            "publisher": "UNOPS",
            "dataset_url": "https://data.unops.org",
            "record_url": None,
            "retrieved_at": retrieved_at
        },
        "status": status,
        "status_basis": status_basis,
        "contract": {
            "identifiers": {
                "contract_id": item.get("Contract")
            },
            "title": item.get("Product", ""),
            "description": "",
            "instrument_type": "contract",
            "value": amount,
            "currency": "USD", # UNOPS amounts typically in USD
            "value_detail": {},
            "dates": {
                "published": start_date,
                "signed": start_date,
                "start": start_date,
                "end": "",
                "amended_last": ""
            },
            "related": {
                "source_url": "https://data.unops.org"
            }
        },
        "buyer": {
            "name": "UNOPS",
            "type": "IGO",
            "country": "DK", # Headquarters
            "identifiers": {},
            "address": {},
            "contact": {}
        },
        "vendor": {
            "name": item.get("Supplier", ""),
            "country": "CA",
            "country_basis": "Supplier_Country / Supplier_Country_Description",
            "identifiers": {},
            "address": {},
            "contact": {}
        },
        "link": "https://data.unops.org",
        "link_type": "dataset",
        "raw": item
    }

    return record

def main():
    out_path = "data/incoming/codex/records_unops_awards.jsonl.gz"

    offset = 0
    total_records = 0
    canadian_records = 0

    # We found earlier that offset doesn't actually work without sorting (or maybe it loops?).
    # So we will track seen ids.
    seen = set()

    with gzip.open(out_path, "wt", encoding="utf-8") as out:
        while True:
            print(f"Fetching from offset {offset}...", flush=True)
            page = fetch_page(offset)
            if not page or not page.get("success"):
                print("Failed to fetch or unsuccessful response.", flush=True)
                break

            data = page.get("data", [])
            if not data:
                break

            new_records = 0
            for row in data:
                contract_id = row.get('Contract')
                if contract_id in seen:
                    continue
                seen.add(contract_id)
                new_records += 1
                total_records += 1
                rec = normalize(row)
                if rec:
                    out.write(json.dumps(rec) + "\n")
                    canadian_records += 1

            if new_records == 0:
                print("No new records found in this page. Stopping.")
                break

            if len(data) < LIMIT:
                break

            offset += LIMIT

    print(f"Total records processed: {total_records}", flush=True)
    print(f"Canadian records found: {canadian_records}", flush=True)

if __name__ == "__main__":
    main()

import json
import gzip
import os
import sys

# Get config
try:
    with open("coord/config.json", "r") as f:
        config = json.load(f)
        ref_date = config["reference_date"]
except Exception as e:
    print(f"Warning: could not load config.json, using 2026-11-02: {e}")
    ref_date = "2026-11-02"

print(f"Reference date: {ref_date}")

# Output structure
import hashlib

def make_id(row):
    # Include amount expended for fiscal year and end date to make it more unique as some records are updated per fiscal year
    key = f"{row.get('_source_dataset', '')}|{row.get('authority_name', '')}|{row.get('vendor_name', '')}|{row.get('award_date', '')}|{row.get('begin_date', '')}|{row.get('end_date', '')}|{row.get('contract_amount', '')}|{row.get('amount_expended_for_fiscal_year', '')}|{row.get('transaction_number', '')}|{row.get('fiscal_year_end_date', '')}"
    return hashlib.sha256(key.encode('utf-8')).hexdigest()[:16]

def parse_float(val):
    if not val:
        return None
    val = str(val).replace('$', '').replace(',', '').strip()
    try:
        return float(val)
    except ValueError:
        return None

def run(raw_file):
    with open(raw_file, "r") as f:
        data = json.load(f)

    print(f"Loaded {len(data)} raw records")

    records = []
    seen_ids = set()

    DATASETS_META = {
        "state_authorities": {
            "name": "Procurement Report for State Authorities",
            "url": "https://data.ny.gov/dataset/Procurement-Report-for-State-Authorities/ehig-g5x3"
        },
        "local_authorities": {
            "name": "Procurement Report for Local Authorities",
            "url": "https://data.ny.gov/dataset/Procurement-Report-for-Local-Authorities/8w5p-k45m"
        },
        "local_development_corps": {
            "name": "Procurement Report for Local Development Corporations",
            "url": "https://data.ny.gov/dataset/Procurement-Report-for-Local-Development-Corporations/d84c-dk28"
        },
        "industrial_development_agencies": {
            "name": "Procurement Report for Industrial Development Agencies",
            "url": "https://data.ny.gov/dataset/Procurement-Report-for-Industrial-Development-Agencies/p3p6-xqr5"
        }
    }

    for row in data:
        if "vendor_country" not in row:
            continue
        country = row["vendor_country"].upper()
        if country not in ["CAN", "CANADA", "CA", "ONTARIO, CANADA"]:
            continue

        # Determine status
        status = "end_date_unknown"
        status_basis = "No end date provided"

        start_dt = row.get("begin_date", row.get("award_date", ""))
        end_dt = row.get("end_date", "")

        if start_dt and end_dt:
            start_dt_short = start_dt[:10]
            end_dt_short = end_dt[:10]
            if start_dt_short <= ref_date and end_dt_short >= ref_date:
                status = "ongoing"
                status_basis = f"start date {start_dt_short} <= {ref_date} and end date {end_dt_short} >= {ref_date}"
            elif end_dt_short < ref_date:
                 # Exclude ended
                 continue
            elif start_dt_short > ref_date:
                 # exclude future starting contracts to be safe
                 continue
        elif start_dt:
            start_dt_short = start_dt[:10]
            if start_dt_short <= ref_date:
                status = "end_date_unknown"
                status_basis = f"start date {start_dt_short} <= {ref_date} but no end date published"
            else:
                continue
        elif end_dt:
            end_dt_short = end_dt[:10]
            if end_dt_short < ref_date:
                continue
            else:
                status = "end_date_unknown"
                status_basis = f"no start date published but end date {end_dt_short} >= {ref_date}"

        # Process location
        v_postal = row.get("vendor_postal_code", "")
        if len(v_postal) == 7 and v_postal[3] == '-':
            v_postal = v_postal.replace('-', ' ')

        rec_id = f"us_ny_state_authorities_procurement:{make_id(row)}"
        if rec_id in seen_ids:
            # Avoid duplicate ids across the dataset
            # Append a number
            counter = 1
            while f"{rec_id}_{counter}" in seen_ids:
                counter += 1
            rec_id = f"{rec_id}_{counter}"
        seen_ids.add(rec_id)

        dataset_key = row.get("_source_dataset", "state_authorities")
        meta = DATASETS_META.get(dataset_key, DATASETS_META["state_authorities"])

        rec = {
            "record_id": rec_id,
            "source": {
                "key": "us_ny_state_authorities_procurement",
                "name": meta["name"],
                "publisher": "New York State",
                "dataset_url": meta["url"],
                "record_url": None,
                "retrieved_at": "2026-11-03T00:00:00Z"
            },
            "status": status,
            "status_basis": status_basis,
            "link": meta["url"],
            "link_type": "dataset",
            "contract": {
                "identifiers": {},
                "title": row.get("procurement_description", ""),
                "description": row.get("procurement_description", ""),
                "instrument_type": row.get("type_of_procurement", ""),
                "procurement_method": row.get("award_process", ""),
                "solicitation_procedure": None,
                "commodity": {},
                "value": parse_float(row.get("contract_amount")),
                "currency": "USD",
                "value_detail": {
                    "amount_expended_to_date": parse_float(row.get("amount_expended_to_date")),
                    "amount_expended_for_fiscal_year": parse_float(row.get("amount_expended_for_fiscal_year"))
                },
                "dates": {
                    "published": None,
                    "signed": row.get("award_date", "")[:10] if "award_date" in row else None,
                    "start": row.get("begin_date", "")[:10] if "begin_date" in row else None,
                    "end": row.get("end_date", "")[:10] if "end_date" in row else None,
                    "amended_last": row.get("renewal_date", "")[:10] if "renewal_date" in row else None
                },
                "related": {}
            },
            "buyer": {
                "name": row.get("authority_name", ""),
                "country": "US",
                "type": "New York State Authority",
                "identifiers": {},
                "address": {},
                "contact": {}
            },
            "vendor": {
                "name": row.get("vendor_name", ""),
                "country": "CA",
                "country_basis": "vendor_country",
                "identifiers": {},
                "address": {
                    "line1": row.get("vendor_address_1", ""),
                    "city": row.get("vendor_city", ""),
                    "region": row.get("vendor_province_region", ""),
                    "postal_code": v_postal,
                    "country": "CA"
                },
                "contact": {}
            },
            "raw": row
        }

        if "transaction_number" in row and row["transaction_number"] != "NONE":
            rec["contract"]["identifiers"]["transaction_number"] = row["transaction_number"]

        records.append(rec)

    print(f"Kept {len(records)} valid ongoing/unknown records")

    # ensure directory exists
    os.makedirs("data/incoming/jules", exist_ok=True)

    with gzip.open("data/incoming/jules/records_us_ny_state_authorities_procurement.jsonl.gz", "wt", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

    print("Done")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Provide path to raw.json")

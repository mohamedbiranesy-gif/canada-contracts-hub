#!/usr/bin/env python3
import sys
import os
import json
import gzip
import urllib.request
import urllib.parse
import urllib.error
import re
import datetime
import time
import hashlib
from collections import defaultdict

# Add W1c sweep normalizers to path
sys.path.insert(0, "scripts/us_discovery_sweep")
import sweeplib

# Load reference date
config = json.load(open("coord/config.json"))
REF_DATE = config["reference_date"]
sweeplib.REF_S = REF_DATE

# Set up output path
OUT_PATH = "data/incoming/jules/records_us_socrata_sweep_continue.jsonl.gz"
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

UA = "contracts-research/1.0"

# Dataset identification logic
def identify_datasets(out_file="out.jsonl"):
    FP = re.compile(r"LA CANADA|CANADA ST|CANADA AVE|CANADA RD|CANADA RAOD|CANADA WAY|CANADA DR|CANADAIGUA|CANADA BLVD|CANADA LN|CANADA CT|CANADA GOOSE|CANADAWAY|CANADA HOLLOW|TRANS.CANADA|CANADA TRUST|CANADAY|LITTLE CANADA|BOCA CANADA|CANADA HILL|CANADA RIDGE", re.I)
    datasets = []

    if not os.path.exists(out_file):
        raise FileNotFoundError(f"Missing dependency: {out_file} is required to run the scraper.")

    with open(out_file, "r") as f:
        for line in f:
            j = json.loads(line)
            if j.get("total_hits", 0) == 0:
                continue

            good_cols = []
            has_canadian = False
            for c in j.get("cols", []):
                vals = [(v, n) for v, n in (c.get("values") or []) if v and not FP.search(str(v))]
                if vals:
                    good_cols.append(c)
                    has_canadian = True

            if has_canadian:
                # Add good_cols to the dataset object to know which columns to query
                j["good_cols"] = good_cols
                datasets.append(j)

    return datasets


def fetch_socrata_data(domain, dataset_id, cols):
    """Fetch rows from Socrata where Canadian vendor logic might hit."""

    # Try to construct a WHERE clause to reduce download size based on the good_cols
    where_parts = []
    for c in cols:
        col_name = c["col"]
        kind = c["kind"]
        if kind == "country":
            where_parts.append(f"upper(`{col_name}`) in ('CA','CAN','CANADA','CDN') OR upper(`{col_name}`) like '%CANADA%'")
        elif kind == "state":
            provs = ",".join(f"'{p}'" for p in ["ON", "ONT", "ONTARIO", "QC", "PQ", "QUE", "QUEBEC", "BC", "AB", "ALBERTA", "MB", "MANITOBA", "SK", "SASKATCHEWAN", "NS", "NOVA SCOTIA", "NB", "NEW BRUNSWICK", "NL", "NEWFOUNDLAND", "PE", "PEI", "YT", "YUKON", "NT", "NU", "CANADA", "CAN", "CDN"])
            where_parts.append(f"upper(`{col_name}`) in ({provs}) OR upper(`{col_name}`) like '%CANADA%'")
        elif kind == "zip":
             where_parts.append(f"upper(`{col_name}`) >= 'A' AND upper(`{col_name}`) < '['")
        elif kind in ("address", "city"):
             where_parts.append(f"upper(`{col_name}`) like '%CANADA%'")

    where_clause = " OR ".join(where_parts)

    url = f"https://{domain}/resource/{dataset_id}.json"
    params = {"$limit": 50000}
    if where_clause:
        params["$where"] = where_clause

    url += "?" + urllib.parse.urlencode(params)

    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404):
                print(f"HTTP {e.code} for {domain}/{dataset_id}")
                return []
            time.sleep(3 * (attempt + 1))
        except Exception as e:
            print(f"Error fetching {domain}/{dataset_id}: {e}")
            time.sleep(3 * (attempt + 1))
    return []


def process_dataset(ds, fo):
    domain = ds["domain"]
    ds_id = ds["id"]
    name = ds.get("name", "Unknown Socrata Dataset")

    print(f"Processing {domain}/{ds_id}...")

    rows = fetch_socrata_data(domain, ds_id, ds.get("good_cols", []))
    if not rows:
        print(f"No rows returned for {domain}/{ds_id}")
        return

    # Analyze the schema dynamically based on common Socrata column names
    keys = set()
    for row in rows[:50]:
        keys.update(row.keys())
    keys = list(keys)

    # Try to find relevant columns
    date_cols = [k for k in keys if "date" in k.lower() or "time" in k.lower()]
    start_col = next((k for k in date_cols if "start" in k.lower() or "begin" in k.lower() or "effective" in k.lower()), None)
    end_col = next((k for k in date_cols if "end" in k.lower() or "expir" in k.lower() or "close" in k.lower()), None)
    award_col = next((k for k in date_cols if "award" in k.lower() or "issue" in k.lower() or "exec" in k.lower() or "creat" in k.lower()), None)
    if not award_col and not start_col and date_cols:
         award_col = date_cols[0] # Fallback

    val_col = next((k for k in keys if "amount" in k.lower() or "value" in k.lower() or "cost" in k.lower() or "price" in k.lower() or "total" in k.lower()), None)
    desc_col = next((k for k in keys if "desc" in k.lower() or "title" in k.lower() or "purp" in k.lower() or "comm" in k.lower()), None)
    id_col = next((k for k in keys if "id" in k.lower() or "num" in k.lower() or "po" in k.lower() or "contract" in k.lower()), None)

    buyer_name_col = next((k for k in keys if ("dept" in k.lower() or "agency" in k.lower() or "buyer" in k.lower() or "purch" in k.lower()) and "name" in k.lower()), None)
    if not buyer_name_col:
        buyer_name_col = next((k for k in keys if ("dept" in k.lower() or "agency" in k.lower())), None)

    vendor_name_col = next((k for k in keys if "vendor" in k.lower() or "supp" in k.lower() or "payee" in k.lower() or "contractor" in k.lower()), None)
    if not vendor_name_col:
        # fallback to any 'name' col that isn't buyer
        vendor_name_col = next((k for k in keys if "name" in k.lower() and k != buyer_name_col), None)

    # Use the discovered good_cols for location mapping
    loc_cols = ds.get("good_cols", [])
    country_col = next((c["col"] for c in loc_cols if c["kind"] == "country"), None)
    state_col = next((c["col"] for c in loc_cols if c["kind"] == "state"), None)
    zip_col = next((c["col"] for c in loc_cols if c["kind"] == "zip"), None)
    city_col = next((c["col"] for c in loc_cols if c["kind"] == "city"), None)
    addr_col = next((c["col"] for c in loc_cols if c["kind"] == "address"), None)

    # Website col
    website_col = next((k for k in keys if "url" in k.lower() or "website" in k.lower() or "web" in k.lower()), None)

    for i, row in enumerate(rows):
        is_canadian, basis = sweeplib.canadian(
            region=row.get(state_col) if state_col else None,
            postal=row.get(zip_col) if zip_col else None,
            country=row.get(country_col) if country_col else None,
            text=row.get(addr_col) if addr_col else None,
            region_field=state_col or "state",
            postal_field=zip_col or "zip",
            country_field=country_col or "country"
        )

        if not is_canadian:
            continue

        buyer_name = row.get(buyer_name_col) if buyer_name_col else None
        # Default buyer to the dataset publisher or domain if no explicit column is found
        if not buyer_name:
            buyer_name = domain.split(".")[0].capitalize()

        if not buyer_name or str(buyer_name).strip() == "":
            continue # Must have named buyer

        # Try to infer dates
        d_start = sweeplib.d(row.get(start_col)) if start_col else None
        d_end = sweeplib.d(row.get(end_col)) if end_col else None
        d_award = sweeplib.d(row.get(award_col)) if award_col else None

        # Calculate status
        # If it's a payments dataset (no end date, high volume), use activity status
        if not end_col and ("payment" in name.lower() or "checkbook" in name.lower() or "expenditure" in name.lower()):
            status, status_basis = sweeplib.status_activity(d_award or d_start)
        else:
            status, status_basis = sweeplib.status_contract(d_start, d_end, award=d_award)

        if not status:
            continue # Skip ended/not started

        # Identifiers
        c_ids = {}
        if id_col and row.get(id_col):
             c_ids["contract_id"] = str(row.get(id_col))

        v_name = row.get(vendor_name_col) if vendor_name_col else None
        if not v_name or str(v_name).strip() == "" or str(v_name).strip().upper() == "UNKNOWN":
            continue

        b_contact = {}
        if website_col and row.get(website_col):
             # Try to parse if it's a dict (Socrata url fields can be dicts)
             v = row.get(website_col)
             if isinstance(v, dict) and "url" in v:
                 b_contact["website"] = v["url"]
             elif isinstance(v, str):
                 b_contact["website"] = v

        rec_id = row.get("id") or str(i)

        # Make deterministic dedupe suffix based on row content
        row_hash = hashlib.sha1(json.dumps(row, sort_keys=True).encode()).hexdigest()[:8]
        if id_col and row.get(id_col):
            rec_id = f"{row.get(id_col)}_{row_hash}"
        else:
            rec_id = f"{i}_{row_hash}"

        record_url = f"https://{domain}/d/{ds_id}"

        source = {
            "key": "us_socrata_sweep_continue",
            "name": name,
            "publisher": domain,
            "dataset_url": f"https://{domain}/d/{ds_id}",
            "record_url": record_url, # Best guess
            "retrieved_at": sweeplib.now_iso()
        }

        contract = sweeplib.contract(
            identifiers=c_ids,
            title=sweeplib.s(row.get(desc_col)) if desc_col else None,
            value=sweeplib.amt(row.get(val_col)) if val_col else None,
            dates={"start": d_start, "end": d_end, "published": d_award},
            related={"link": record_url}
        )

        # ensure there is a single link in the main object if expected
        buyer = sweeplib.buyer(
            name=sweeplib.s(buyer_name),
            btype=None,
            contact=b_contact
        )

        vendor = sweeplib.vendor(
            name=v_name,
            basis=basis,
            line1=row.get(addr_col) if addr_col else None,
            city=row.get(city_col) if city_col else None,
            region=row.get(state_col) if state_col else None,
            postal=row.get(zip_col) if zip_col else None,
            country=row.get(country_col) if country_col else None
        )

        # Build the final record
        rec = sweeplib.rec(source, f"{domain}~{ds_id}~{rec_id}", status, status_basis, contract, buyer, vendor, raw=row)
        rec["link"] = record_url
        rec["link_type"] = "dataset"

        fo.write(json.dumps(rec, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    datasets = identify_datasets()
    print(f"Identified {len(datasets)} candidate datasets.")

    with gzip.open(OUT_PATH, "wt", encoding="utf-8") as fo:
        for ds in datasets:
            process_dataset(ds, fo)

    print(f"Sweep complete. Wrote {OUT_PATH}")

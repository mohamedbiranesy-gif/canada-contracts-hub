import sys, os, csv, json, hashlib, collections, gzip, re
from datetime import datetime, date, timezone

dl = 'data/incoming/jules/downloads/ca_municipal_purchase_orders_open_data'
outdir = 'data/incoming/jules'
os.makedirs(dl, exist_ok=True)
os.makedirs(outdir, exist_ok=True)

REF_DATE = json.load(open("coord/config.json"))["reference_date"]

print("Loading vendor dictionary...", file=sys.stderr)
VENDORS_LOWER = set()
with gzip.open('contrib/claude/buyer_pages/vendors_ca.tsv.gz', 'rt') as f:
    r = csv.reader(f, delimiter='\t')
    next(r)
    for row in r:
        if len(row) > 0:
            VENDORS_LOWER.add(row[0].strip().lower())

def is_canada_vendor(name):
    if not name: return False
    if name.lower() in VENDORS_LOWER: return True
    clean = re.sub(r'(?i)\b(inc|ltd|corp|llc|incorporated|limited|corporation)\b\.?', '', name).strip().lower()
    if clean in VENDORS_LOWER: return True
    return False

def parse_edmonton():
    path = f"{dl}/data.edmonton.ca_y9rm-5xha.csv"
    if not os.path.exists(path):
        return []
    records = []
    seen = set()
    RET = datetime.now(timezone.utc).isoformat()
    for row_idx, row in enumerate(csv.DictReader(open(path, encoding="utf-8-sig"))):
        sup = (row.get("Supplier Name") or "").strip()
        if not sup: continue
        if not is_canada_vendor(sup): continue

        start_date = None
        try:
            start_date = datetime.strptime(row["Create Date"].strip(), "%B %d %Y").date()
        except:
            pass

        is_ongoing = False
        if start_date:
            if start_date.isoformat() <= REF_DATE:
                is_ongoing = True

        h = hashlib.sha1(json.dumps(row, sort_keys=True).encode()).hexdigest()[:10]
        rec_id = f"ca_municipal_purchase_orders_open_data:edmonton:{h}"

        # Avoid duplicate ids
        if rec_id in seen:
            rec_id = f"{rec_id}_{row_idx}"
        seen.add(rec_id)

        rec = {
            "record_id": rec_id,
            "source": {
                "key": "ca_municipal_purchase_orders_open_data",
                "name": "City of Edmonton - Purchase Orders Over $10,000",
                "publisher": "City of Edmonton",
                "dataset_url": "https://data.edmonton.ca/d/y9rm-5xha",
                "record_url": None,
                "retrieved_at": RET
            },
            "link": "https://data.edmonton.ca/d/y9rm-5xha",
            "link_type": "dataset",
            "status": "end_date_unknown" if is_ongoing else "end_date_unknown",
            "status_basis": "No end date published; kept as end_date_unknown.",
            "contract": {
                "identifiers": {},
                "title": row.get("Description"),
                "description": row.get("Description"),
                "instrument_type": row.get("Purchase Order Type"),
                "procurement_method": None,
                "solicitation_procedure": None,
                "commodity": {},
                "value": None,
                "currency": None,
                "value_detail": {"dollar_value_category": row.get(" Dollar Value Category ")},
                "dates": {
                    "published": None,
                    "signed": None,
                    "start": start_date.isoformat() if start_date else None,
                    "end": None,
                    "amended_last": None,
                },
                "related": {}
            },
            "buyer": {
                "name": "City of Edmonton",
                "country": "CA",
                "type": "city",
                "identifiers": {},
                "address": {"city": "Edmonton", "region": "AB"},
                "contact": {}
            },
            "vendor": {
                "name": sup,
                "country": "CA",
                "country_basis": "Matched vendor name against contrib/claude/buyer_pages/vendors_ca.tsv.gz",
                "identifiers": {},
                "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": "CA"},
                "contact": {}
            },
            "raw": row,
        }
        records.append(rec)
    return records

all_records = parse_edmonton()
with gzip.open(f"{outdir}/records_ca_municipal_purchase_orders_open_data.jsonl.gz", "wt") as f:
    for r in all_records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"Saved {len(all_records)} records.", file=sys.stderr)

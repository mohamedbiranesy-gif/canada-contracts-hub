#!/usr/bin/env python3
"""Ontario Enterprise Vendor of Record (VOR) arrangements (data.ontario.ca / Supply Ontario VOR database CSV).
Columns: VOR Number, VOR Name, Qualified Vendor, Start Date, End Date. No vendor address -> unverified-country file only.
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, csv, json, hashlib, collections
from datetime import date

dl, outdir = sys.argv[1], sys.argv[2]
REF = date(2026, 10, 25)
RET = open(os.path.join(dl, "retrieved_at.txt")).read().strip()
out = open(os.path.join(outdir, "ca_ontario_vor_unverified_country.jsonl"), "w")
stats = collections.Counter()
lines = list(csv.reader(open(os.path.join(dl, "enterprise_vor_program.csv"), encoding="utf-8", errors="replace"), skipinitialspace=True))
extract_tag = lines[0][0] if lines and lines[0] else None
hdr = None
for i, r in enumerate(lines):
    if r and r[0].startswith("Vendor of Record (VOR) Number"):
        hdr = [h.strip() for h in r]
        start_i = i + 1
        break
seen = collections.Counter()
for r in lines[start_i:]:
    if len(r) != len(hdr):
        continue
    row = dict(zip(hdr, [x.strip() for x in r]))
    stats["rows"] += 1
    try:
        st = date.fromisoformat(row["Start Date"]); en = date.fromisoformat(row["End Date"])
    except Exception:
        stats["bad_dates"] += 1
        continue
    if en < REF:
        stats["excluded_ended"] += 1; continue
    if st > REF:
        stats["excluded_not_started"] += 1; continue
    vor = row["Vendor of Record (VOR) Number"]
    seen[vor] += 1
    h = hashlib.sha1(row["Qualified Vendor"].encode()).hexdigest()[:8]
    rec = {
        "record_id": f"ca_ontario_vor:{vor}:{h}",
        "source": {"key": "ca_ontario_vor", "name": "Enterprise Vendor of Record Arrangements (Ontario)",
                   "publisher": "Government of Ontario - Supply Ontario / Ministry of Public and Business Service Delivery and Procurement (data.ontario.ca)",
                   "dataset_url": "https://data.ontario.ca/dataset/enterprise-vendor-of-record-arrangements", "record_url": None, "retrieved_at": RET},
        "status": "ongoing",
        "status_basis": f"Start Date {st.isoformat()} <= 2026-10-25 <= End Date {en.isoformat()} (VOR arrangement term).",
        "contract": {"identifiers": {"vor_number": vor}, "title": row["Vendor of Record (VOR) Name"], "description": row["Vendor of Record (VOR) Name"],
                     "instrument_type": "vendor of record arrangement (standing agreement)", "procurement_method": "competitive (enterprise VOR)",
                     "solicitation_procedure": None, "commodity": {}, "value": None, "currency": None, "value_detail": {},
                     "dates": {"published": None, "signed": None, "start": st.isoformat(), "end": en.isoformat(), "amended_last": None}, "related": {"extract": extract_tag}},
        "buyer": {"name": "Government of Ontario (Ontario Public Service ministries; enterprise VOR administered by Supply Ontario)", "country": "CA", "type": "province",
                  "identifiers": {}, "address": {"region": "ON"}, "contact": {}},
        "vendor": {"name": row["Qualified Vendor"], "country": None, "country_basis": "not published (dataset has no vendor address)",
                   "identifiers": {}, "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": None}, "contact": {}},
        "raw": row,
    }
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    stats["emitted_ongoing"] += 1
out.close()
stats["distinct_vor"] = len(seen)
print(json.dumps(dict(stats), indent=1))

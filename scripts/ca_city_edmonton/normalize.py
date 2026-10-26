#!/usr/bin/env python3
"""City of Edmonton open data: Outline Agreements over $10,000 (ydv5-y4pu) and Hired Equipment Contracts over
$10,000 (gnse-cass). No supplier address -> unverified-country file only. Only rows whose 'Validity Period End'
>= 2026-10-25 are emitted (status ongoing); Purchase Orders over $10,000 (y9rm-5xha) are one-off straight POs
(2012-2019) with no term and are not emitted.
Usage: python3 -I normalize.py <downloads_dir> <normalized_dir>
"""
import sys, os, csv, json, hashlib, collections
from datetime import datetime, date

dl, outdir = sys.argv[1], sys.argv[2]
REF = date(2026, 10, 25)
RET = open(os.path.join(dl, "retrieved_at.txt")).read().strip()
out = open(os.path.join(outdir, "ca_city_edmonton_unverified_country.jsonl"), "w")
stats = collections.Counter()
DS = {"ydv5-y4pu": "Outline Agreements over $10,000", "gnse-cass": "Hired Equipment Contracts over $10,000"}
for did, name in DS.items():
    for row in csv.DictReader(open(os.path.join(dl, did + ".csv"), encoding="utf-8")):
        row = {k.strip(): v for k, v in row.items()}
        stats[did + "_rows"] += 1
        try:
            end = datetime.strptime(row["Validity Period End"].strip(), "%b %d, %Y").date()
        except Exception:
            stats[did + "_bad_end"] += 1
            continue
        if end < REF:
            stats[did + "_ended"] += 1
            continue
        sup = (row.get("Supplier Name") or "").strip()
        if not sup:
            continue
        yr = row.get("Year") or row.get("Year of Contract")
        h = hashlib.sha1(json.dumps(row, sort_keys=True).encode()).hexdigest()[:10]
        rec = {
            "record_id": f"ca_city_edmonton:{did}:{h}",
            "source": {"key": "ca_city_edmonton", "name": f"City of Edmonton - {name}", "publisher": "City of Edmonton (Open Data Portal)",
                       "dataset_url": f"https://data.edmonton.ca/d/{did}", "record_url": None, "retrieved_at": RET},
            "status": "ongoing",
            "status_basis": f"'Year' {yr} (agreement year, <= 2026) and 'Validity Period End' {row['Validity Period End']!r} = {end.isoformat()} >= 2026-10-25.",
            "contract": {"identifiers": {}, "title": row.get("Description"), "description": row.get("Description"),
                         "instrument_type": row.get("Purchase Order Type") or "outline agreement", "procurement_method": None, "solicitation_procedure": None,
                         "commodity": {}, "value": None, "currency": None, "value_detail": {"dollar_value_category": row.get("Dollar Value Category")},
                         "dates": {"published": None, "signed": None, "start": None, "end": end.isoformat(), "amended_last": None, "agreement_year": yr},
                         "related": {}},
            "buyer": {"name": "City of Edmonton", "country": "CA", "type": "city", "identifiers": {}, "address": {"city": "Edmonton", "region": "AB"}, "contact": {}},
            "vendor": {"name": sup, "country": None, "country_basis": "not published (dataset has no supplier address)", "identifiers": {},
                       "address": {"line1": None, "city": None, "region": None, "postal_code": None, "country": None}, "contact": {}},
            "raw": row,
        }
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        stats["emitted_ongoing"] += 1
out.close()
print(json.dumps(dict(stats), indent=1))

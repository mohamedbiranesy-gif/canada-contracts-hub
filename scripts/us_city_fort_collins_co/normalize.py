#!/usr/bin/env python3
"""City of Fort Collins (CO) OpenBook: Detailed Expenses joined to Detailed Vendors on vendor id; Canadian vendor address.
usage: python3 -I normalize.py <vendors_ca.jsonl> <expenses_ca.jsonl> <out.jsonl>"""
import sys, json, collections
sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *
vp, ep, op = sys.argv[1:4]
B = "https://services1.arcgis.com/dLpFH5mwVvxSN4OE/arcgis/rest/services"
SRC = {"key": "us_city_fort_collins_co", "name": "Fort Collins Detailed OpenBook Expenses + Fort Collins Detailed OpenBook Vendors (ArcGIS Online)",
       "publisher": "City of Fort Collins, Colorado (OpenData_fcgov)", "dataset_url": f"{B}/Fort_Collins_Detailed_OpenBook_Expenses/FeatureServer/0",
       "record_url": None, "retrieved_at": "2026-10-26T03:51:37Z"}
V = collections.defaultdict(list)
for v in read_jsonl(vp): V[str(v.get("vendor_id"))].append(v)
G = collections.defaultdict(list)
for e in read_jsonl(ep): G[(str(e.get("Vendor_ID")), s(e.get("Department")))].append(e)
out = Out(op)
for (vid, dept), rows in G.items():
    vm = V.get(vid, [])
    if not vm: out.exclude("no_vendor_master"); continue
    v0 = vm[0]
    ok, basis = canadian(region=v0.get("state"), postal=v0.get("zip"), country=None, region_field="vendor master state", postal_field="vendor master zip", country_field=None)
    if not ok: out.exclude("not_canadian " + basis); continue
    basis += " (vendor master 'country' column reads 'US' for every row, a system default; province + postal code govern)"
    rows.sort(key=lambda e: e.get("Date") or 0)
    last = d(rows[-1].get("Date")); first = d(rows[0].get("Date"))
    st, sb = status_activity(last, "expense")
    if not st: out.exclude("stale"); continue
    val = round(sum(amt(e.get("Actual_Amount")) or 0 for e in rows), 2)
    pc = sum(1 for e in rows if str(e.get("Purchasing_Card_Expense")).lower() == "true")
    c = contract({"vendor_id": vid}, title="; ".join(dict.fromkeys(s(e.get("Description")) or "" for e in rows))[:300],
                 description="; ".join(dict.fromkeys(s(e.get("Expense_Category")) or "" for e in rows))[:500],
                 instrument_type="expense payments" + (" (incl. purchasing-card expenses)" if pc else ""),
                 value=val, value_detail={"sum_actual_amount": val, "rows": len(rows), "purchasing_card_rows": pc},
                 dates={"start": first, "amended_last": last}, related={"first_expense": first, "last_expense": last})
    b = buyer(f"City of Fort Collins, Colorado - {dept}", "city department", identifiers={"service_area": s(rows[0].get("Service_Area"))})
    v = vendor(v0.get("vendor_name"), basis, identifiers={"fort_collins_vendor_id": vid}, line1=v0.get("address_1"), line2=v0.get("address_2"),
               city=v0.get("city"), region=v0.get("state"), postal=v0.get("zip"))
    out.write(rec(SRC, sid(vid, dept), st, sb, c, b, v, {"rows": rows, "vendor_master": vm,
                  "layers": [f"{B}/Fort_Collins_Detailed_OpenBook_Expenses/FeatureServer/0", f"{B}/Fort_Collins_Detailed_OpenBook_Vendors/FeatureServer/0"]}))
print(json.dumps(out.close()))

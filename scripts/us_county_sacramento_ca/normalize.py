#!/usr/bin/env python3
"""Sacramento County (CA) 'County Contracts' ArcGIS layer (SAP outline agreements), Canadian vendor address.
usage: python3 -I normalize.py <county_contracts_ca.jsonl> <out.jsonl> [<purchase_orders_ca.jsonl>]"""
import sys, json, collections
sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *
ip, op = sys.argv[1:3]
LAYER = "https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/services/County_Contracts/FeatureServer/1"
SRC = {"key": "us_county_sacramento_ca", "name": "County Contracts (Sacramento County, California) - ArcGIS Online item d9e90b479cda4576a8ee393a3e9ac17c",
       "publisher": "County of Sacramento, California (Sacramento County GIS, ArcGIS Online)",
       "dataset_url": "https://www.arcgis.com/home/item.html?id=d9e90b479cda4576a8ee393a3e9ac17c", "record_url": None,
       "retrieved_at": "2026-10-26T03:42:35Z"}
TYPES = {"MK": "contract (SAP quantity outline agreement 'MK')", "WK": "contract (SAP value outline agreement 'WK')"}
G = collections.defaultdict(list)
for r in read_jsonl(ip):
    G[(s(r.get("ContractNo")), s(r.get("VendorName")))].append(r)
out = Out(op)
for (cn, vn), rows in G.items():
    r0 = rows[0]
    ok, basis = canadian(region=r0.get("VendorState"), postal=r0.get("VendorZip"), text=" ".join(str(r0.get(k) or "") for k in ("VendorAddress", "VendorCity")),
                         region_field="VendorState", postal_field="VendorZip", country_field=None)
    if not ok: out.exclude("not_canadian " + basis); continue
    rows.sort(key=lambda r: (s(r.get("ContractItemNo")) or ""))
    starts = [d(r.get("ContractDate")) for r in rows if r.get("ContractDate")]; ends = [d(r.get("ContractEndDate")) for r in rows if r.get("ContractEndDate")]
    start = min(starts) if starts else None; end = max(ends) if ends else None
    st, sb = status_contract(start, end)
    if not st: out.exclude(sb); continue
    sb = "ContractDate/ContractEndDate of the outline agreement items: " + sb
    val = round(sum(amt(r.get("EffectivePrice")) or 0 for r in rows), 2)
    c = contract({"contract_number": cn, "contract_items": ";".join(s(r.get("ContractItemNo")) or "" for r in rows)},
                 title="; ".join(dict.fromkeys(s(r.get("MaterialDescription")) or "" for r in rows))[:300],
                 description="; ".join(s(r.get("MaterialDescription")) or "" for r in rows)[:1500],
                 instrument_type=TYPES.get(s(r0.get("ContractType")), f"contract (type {s(r0.get('ContractType'))})"),
                 value=val, value_detail={"sum_item_effective_price": val, "items": len(rows)},
                 dates={"signed": start, "start": start, "end": end})
    b = buyer("County of Sacramento, California", "county")
    v = vendor(vn, basis, line1=r0.get("VendorAddress"), city=r0.get("VendorCity"), region=r0.get("VendorState"), postal=r0.get("VendorZip"))
    out.write(rec(SRC, sid(cn), st, sb, c, b, v, {"rows": rows, "layer": LAYER}))
# --- purchase orders (Purchase_Orders/FeatureServer/1): no term -> 12-month PO-date window
POL = "https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/services/Purchase_Orders/FeatureServer/1"
vend_contracts = collections.defaultdict(list)
for (cn, vn), rows in G.items():
    vend_contracts[vn].append(cn)
if len(sys.argv) > 3:
    SRC2 = dict(SRC, name="Purchase Orders (Sacramento County, California) - ArcGIS Online Purchase_Orders FeatureServer/1",
                dataset_url="https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/services/Purchase_Orders/FeatureServer/1",
                retrieved_at="2026-10-26T03:48:20Z")
    P = collections.defaultdict(list)
    for r in read_jsonl(sys.argv[3]):
        P[(s(r.get("PO_No")), s(r.get("VendorName")))].append(r)
    for (po, vn), rows in P.items():
        r0 = rows[0]
        ok, basis = canadian(region=r0.get("VendorState"), postal=r0.get("VendorZip"), text=" ".join(str(r0.get(k) or "") for k in ("VendorAddress", "VendorCity")),
                             region_field="VendorState", postal_field="VendorZip", country_field=None)
        if not ok: out.exclude("not_canadian " + basis); continue
        pdate = max(d(r.get("PO_Date")) or "" for r in rows) or None
        st, sb = status_activity(pdate, "purchase order")
        if not st: out.exclude("stale_po"); continue
        rows.sort(key=lambda r: s(r.get("PO_ItemNo")) or "")
        val = round(sum((amt(r.get("Qty")) or 0) * (amt(r.get("UnitPrice")) or 0) for r in rows), 2)
        c = contract({"po_number": po, "po_items": ";".join(s(r.get("PO_ItemNo")) or "" for r in rows)},
                     title="; ".join(dict.fromkeys(s(r.get("MaterialDescription")) or "" for r in rows))[:300],
                     description="; ".join(s(r.get("MaterialDescription")) or "" for r in rows)[:1500],
                     instrument_type="purchase order", value=val, value_detail={"sum_qty_x_unit_price": val, "items": len(rows)},
                     dates={"signed": pdate, "start": pdate},
                     related={"same_vendor_outline_agreements_in_county_contracts": vend_contracts.get(vn, [])})
        b = buyer("County of Sacramento, California", "county")
        v = vendor(vn, basis, line1=r0.get("VendorAddress"), city=r0.get("VendorCity"), region=r0.get("VendorState"), postal=r0.get("VendorZip"))
        out.write(rec(SRC2, sid("PO", po), st, sb, c, b, v, {"rows": rows, "layer": POL}))
print(json.dumps(out.close()))

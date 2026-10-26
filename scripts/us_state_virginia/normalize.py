#!/usr/bin/env python3
"""Normalize Virginia eVA Procurement Data (data.virginia.gov) -> Canadian-vendor purchase orders.
usage: python3 -I normalize.py <eva_2026_canada.csv> <eva_2025_canada.jsonl> <out.jsonl>
Source is line-level purchase-order data (no end dates). One record per Order # (all lines in raw.rows).
Only orders dated within the last 12 months before the reference date are kept as end_date_unknown.
"""
import sys, csv, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

csv.field_size_limit(10**9)
SOURCE_KEY = "us_state_virginia"
RECENT_CUTOFF = "2025-10-25"  # 12 months before reference date
FY_META = {
    "2026": ("e6f7f6ba-23a1-4423-93cd-31697b89a26f", "76f6831d-fac7-4c1f-8313-cc7ff238ddca", "https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia"),
    "2025": ("8edfcb13-f18f-4bdf-be87-2484838348e2", "b8dc22a8-e96e-460f-9d5c-8dede67fddda", "https://data.virginia.gov/dataset/eva-procurement-data-2025-virginia"),
}


def norm_key(k):
    return k.replace(" ", "_")


def main():
    csv26, js25, out = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = []
    with open(csv26, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["_fy"] = "2026"; r["_retrieved"] = file_mtime_iso(csv26)
            rows.append(r)
    with open(js25, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            r = {norm_key(k): (v if v is not None else "") for k, v in r.items() if k not in ("_full_text",)}
            r["_fy"] = "2025"; r["_retrieved"] = file_mtime_iso(js25)
            rows.append(r)
    w = Writer(out)
    stats = collections.Counter()
    stats["rows"] = len(rows)
    orders = collections.OrderedDict()
    for r in rows:
        st = (r.get("Vendor_Address_State") or "").strip()
        if not norm_prov(st):
            stats["not_canadian_state_value"] += 1
            continue
        orders.setdefault((r["Order_#"], r["eVA_ID"]), []).append(r)
    stats["orders"] = len(orders)
    for (onum, evaid), lines in orders.items():
        lines.sort(key=lambda x: int(x.get("Order_Line_Number") or 0))
        hdr = lines[0]
        statuses = set((l.get("Order_Status") or "").strip() for l in lines)
        if statuses and statuses <= {"Canceled", "Denied"}:
            stats["excluded_cancelled_denied"] += 1
            continue
        odate = parse_date(hdr.get("Ordered_Date"))
        if not odate or odate < RECENT_CUTOFF:
            stats["excluded_older_than_12m"] += 1
            continue
        if odate > REF_S:
            stats["excluded_future"] += 1
            continue
        status = "end_date_unknown"
        basis = f"eVA publishes purchase orders without end dates; Ordered Date {odate} within 12 months before {REF_S}; Order Status {sorted(statuses)}"
        total = sum((parse_amount(l.get("Line_Total")) or 0) for l in lines if (l.get("Order_Status") or "") not in ("Canceled", "Denied"))
        fy = hdr["_fy"]
        pkg, res, landing = FY_META[fy]
        contract = contract_block(
            identifiers={"order_number": onum, "contract_number": hdr.get("Contract_Number") or None, "requisition_dates": None,
                         "eva_vendor_id": evaid, "vlin_id": hdr.get("VLIN_ID") or None, "entity_code": hdr.get("Entity_Code"),
                         "order_line_numbers": [l.get("Order_Line_Number") for l in lines]},
            title=(hdr.get("Item_Description") or hdr.get("NIGP_Description") or None),
            description="; ".join(sorted(set((l.get("Item_Description") or "").strip() for l in lines if l.get("Item_Description")))) [:2000] or None,
            instrument_type=f"purchase order ({hdr.get('Order_Type')})" + (f" under contract {hdr.get('Contract_Number')}" if hdr.get("Contract_Number") else ""),
            procurement_method=hdr.get("PO_Category_Description") or None,
            commodity={"nigp": hdr.get("NIGP_#"), "nigp_description": hdr.get("NIGP_Description"),
                       "nigp_all_lines": sorted(set(l.get("NIGP_#") for l in lines if l.get("NIGP_#")))},
            value=round(total, 2), currency="USD",
            value_detail={"sum_line_total_non_cancelled": round(total, 2), "line_totals": [parse_amount(l.get("Line_Total")) for l in lines]},
            dates={"published": odate, "signed": odate, "start": odate,
                   "amended_last": None},
            related={"contract_type": hdr.get("Contract_Type") or None, "procurement_transaction_desc": hdr.get("Procurement_Transaction_Desc"),
                     "dataset_fiscal_year": fy, "ckan_package_id": pkg, "ckan_resource_id": res},
        )
        buyer = buyer_block(hdr.get("Entity_Description"), "Virginia state agency / public body / institution", "US",
                            identifiers={"eva_entity_code": hdr.get("Entity_Code")},
                            address={"line1": hdr.get("Shipping_Lines") or None, "city": hdr.get("Shipping_City") or None,
                                     "region": hdr.get("Shipping_State") or None, "postal_code": hdr.get("Shipping_Postal") or None, "name": hdr.get("Shipping_Name") or None})
        vendor = vendor_block(hdr.get("Vendor_Name"), f"Vendor Address State = '{hdr.get('Vendor_Address_State')}' (Canadian province code)",
                              identifiers={"eva_id": evaid, "vlin_id": hdr.get("VLIN_ID") or None},
                              address={"line1": hdr.get("Vendor_Address_Lines") or None, "city": hdr.get("Vendor_Address_City") or None,
                                       "region": hdr.get("Vendor_Address_State"), "postal_code": hdr.get("Vendor_Address_Postal") or None,
                                       "country": None, "location_name": hdr.get("Vendor_Location_Name") or None,
                                       "geolocation": hdr.get("Vendor_Address_Geolocation") or None})
        raw = {"dataset": f"eVA Procurement Data {fy} - Virginia", "rows": [{k: v for k, v in l.items() if not k.startswith("_")} for l in lines]}
        rec = record(SOURCE_KEY, f"eVA Procurement Data (Virginia Open Data Portal, FY{fy} file)", "Virginia Department of General Services (eVA) via data.virginia.gov",
                     landing, None, hdr["_retrieved"], f"{fy}:{onum}:{evaid}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

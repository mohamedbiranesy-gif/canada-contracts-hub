#!/usr/bin/env python3
"""Miami-Dade County 'Purchase Orders (INFORMS)' 2025 + 2026 layers (ArcGIS, MDPublisher); Canadian vendor = COUNTRY = 'CAN'
(supplier address country). One record per (PO_YEAR, PO_NUMBER, BUSINESS_UNIT); end_date_unknown iff PO_DATE within 12 months.
usage: python3 -I normalize.py <out.jsonl> <layer_jsonl>..."""
import sys, datetime
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_county_miami_dade"; RET = "2026-10-25T19:29:33Z"
LAYERS = {"po_informs_2026_ca": "https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/services/miamidade_procurement_data_informs_2026/FeatureServer/0",
          "po_informs_2025_ca": "https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/services/miamidade_procurement_data_informs_2025/FeatureServer/0"}


def pdate(v):
    if isinstance(v, (int, float)):
        return datetime.datetime.fromtimestamp(v / 1000, datetime.timezone.utc).date().isoformat()
    return parse_date(v)


def build(k, rs, first, last):
    h = rs[0]
    if (h.get("COUNTRY") or "").upper() != "CAN":
        return None
    lines = {}
    for r in rs:
        lines.setdefault((r.get("PO_LINE_NUMBER"), r.get("INVOICE_ITEM_ID")), r)
    amt = sum(parse_amount(r.get("PO_AMOUNT")) or 0 for r in lines.values())
    desc = "; ".join(dict.fromkeys((r.get("LONG_ITEM_DESCRIPTION") or r.get("ITEM_DESCRIPTION") or "").strip() for r in rs))[:2000]
    c = contract_block({"po_number": h.get("PO_NUMBER"), "po_year": h.get("PO_YEAR"), "business_unit": h.get("BUSINESS_UNIT"),
                        "supplier_contract_id": h.get("SUPPLIER_CONTRACT_ID"), "supplier_po_type": h.get("SUPPLIER_PO_TYPE")},
                       title=(h.get("ITEM_DESCRIPTION") or "")[:200] or None, description=desc or None,
                       instrument_type="purchase order" + (f" (release against contract {h.get('SUPPLIER_CONTRACT_ID')})" if h.get("SUPPLIER_CONTRACT_ID") else ""),
                       commodity={"miami_dade_item_category": "; ".join(sorted({str(r.get('ITEM_CATEGORY')) for r in rs if r.get('ITEM_CATEGORY')}))},
                       value=amt or None, value_detail={"sum_po_amount_distinct_lines": amt},
                       dates={"published": first, "signed": first, "start": first},
                       related={"supplier_contract_id": h.get("SUPPLIER_CONTRACT_ID"), "layer_url": h["_layer_url"]})
    b = buyer_block(f"Miami-Dade County (business unit {h.get('BUSINESS_UNIT')})", "county department", identifiers={"business_unit": h.get("BUSINESS_UNIT")})
    v = vendor_block(h.get("SUPPLIER_NAME"), f"COUNTRY = 'CAN' (supplier address country); STATE '{h.get('STATE')}', POSTAL '{h.get('POSTAL')}'",
                     identifiers={"supplier_short_name": h.get("SUPPLIER_SHORT_NAME")},
                     address={"line1": h.get("SUPPLIER_ADDRESS"), "line2": h.get("SUPPLIER_ADDRESS2"), "city": h.get("CITY"), "region": h.get("STATE"),
                              "postal_code": h.get("POSTAL"), "country": h.get("COUNTRY")},
                     contact={"phone": " ".join(filter(None, [str(h.get("PHONE_AREA_INTL_CODE") or ""), str(h.get("PHONE_NUMBER") or ""), str(h.get("PHONE_EXTENSION") or "")])).strip() or None})
    basis = f"purchase order (no term published); PO_DATE {last} within 12 months before {REF_S}"
    return record(SK, "Miami-Dade County — Purchase Orders (INFORMS)", "Miami-Dade County (ArcGIS Open Data, MDPublisher)",
                  "https://gis-mdc.opendata.arcgis.com/", None, RET, f"{h.get('PO_YEAR')}-{h.get('BUSINESS_UNIT')}-{h.get('PO_NUMBER')}", "end_date_unknown", basis, c, b, v, {"rows": rs})


if __name__ == "__main__":
    rows = []
    for p in sys.argv[2:]:
        key = p.rsplit("/", 1)[-1].replace(".jsonl", "")
        for r in load_jsonl(p):
            r["_layer_url"] = LAYERS.get(key); r["_po_date_iso"] = pdate(r.get("PO_DATE")); rows.append(r)
    run(rows, lambda r: (r.get("PO_YEAR"), r.get("PO_NUMBER"), r.get("BUSINESS_UNIT")), lambda r: r["_po_date_iso"], build, sys.argv[1])

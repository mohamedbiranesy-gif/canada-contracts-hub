#!/usr/bin/env python3
"""Fulton County GA 'Vendor Payments' (data.fultoncountyga.gov mxhc-krcg) joined on vendor_code = vendor_id to 'Fulton County
Vendors' (2jx8-2ffx) whose address is Canadian (state = province code with non-US zip, or zip in Canadian postal format).
One record per (vendor_code, department). usage: python3 -I normalize.py <vendors_ca.json> <payments_ca.jsonl> <out.jsonl>"""
import sys, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_county_fulton_ga"; RET = "2026-10-25T19:24:03Z"
V = {}


def basis(v):
    st = (v.get("state") or "").strip(); z = (v.get("zip") or "").strip()
    parts = []
    if norm_prov(st): parts.append(f"state = '{st}' (Canadian province code)")
    if is_ca_postal(z): parts.append(f"zip = '{z}' (Canadian postal-code format)")
    return "Fulton County Vendors (2jx8-2ffx) address: " + " and ".join(parts) + f"; city '{v.get('city')}'"


def build(k, rs, first, last):
    h = rs[0]; v = V[h["vendor_code"]]
    good = [r for r in rs if (r.get("check_status") or "").lower() not in ("cancelled", "void", "voided")]
    if not good:
        return None
    amt = sum(filter(None, (parse_amount(r.get("amount")) for r in good)))
    objs = "; ".join(dict.fromkeys(r.get("object_name") or "" for r in rs))
    c = contract_block({"payment_documents": sorted({r.get("payment_document") for r in rs if r.get("payment_document")}),
                        "dis_doc_ids": sorted({r.get("dis_doc_id") for r in rs if r.get("dis_doc_id")}),
                        "vendor_invoice_nos": sorted({r.get("vendor_invoice_no") for r in rs if r.get("vendor_invoice_no")})},
                       title=objs[:200], description=objs, instrument_type="vendor payments (no contract published)",
                       commodity={"fulton_object": "; ".join(sorted({r.get('object') or '' for r in rs}))},
                       value=amt, value_detail={"sum_payments": amt, "n_payments": len(rs)},
                       dates={"start": first, "amended_last": last}, related={"first_payment": first, "last_payment": last})
    b = buyer_block(f"Fulton County, Georgia — {h['department_name']}", "county department", identifiers={"dept": h.get("dept")})
    vend = vendor_block(v.get("vendor_name") or h.get("vendor_legal_name"), basis(v), identifiers={"fulton_vendor_id": v["vendor_id"]},
                        address={"line1": None, "city": v.get("city"), "region": norm_prov(v.get("state")) or v.get("state"), "postal_code": v.get("zip"), "country": None})
    bas = f"payment-level data, no contract term published; latest disb_date {last} within 12 months before {REF_S}"
    return record(SK, "Fulton County Vendor Payments + Fulton County Vendors", "Fulton County, Georgia (data.fultoncountyga.gov)",
                  "https://data.fultoncountyga.gov/d/mxhc-krcg", None, RET, f"{h['vendor_code']}-{h.get('dept')}", "end_date_unknown", bas, c, b, vend,
                  {"rows": rs, "vendor_master": v})


if __name__ == "__main__":
    for v in json.load(open(sys.argv[1])):
        V[v["vendor_id"]] = v
    run(load_jsonl(sys.argv[2]), lambda r: (r["vendor_code"], r.get("dept")), lambda r: r.get("disb_date"), build, sys.argv[3])

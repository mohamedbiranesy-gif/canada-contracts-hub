#!/usr/bin/env python3
"""City of Richmond, California 'Expenditures' (transparentrichmond.org 86qj-wgke) joined on vendorid to 'Vendors' (5mrn-7gkk)
whose state is a Canadian province code. One record per (vendorid, organizationcode); end_date_unknown iff latest date within
12 months. usage: python3 -I normalize.py <vendors_ca.jsonl> <expenditures_ca.jsonl> <out.jsonl>"""
import sys
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_city_richmond_ca"; RET = "2026-10-25T19:45:20Z"; V = {}


def build(k, rs, first, last):
    h = rs[-1]; v = V[h["vendorid"]]
    prov = norm_prov(v.get("state"))
    if not prov or v.get("employee"):
        return None
    paid = [r for r in rs if (r.get("invoicestatus") or "") != "Void"]
    amt = sum(filter(None, (parse_amount(r.get("actual")) for r in paid)))
    desc = "; ".join(dict.fromkeys((r.get("description") or "").strip() for r in rs if r.get("description")))
    c = contract_block({"invoice_ids": sorted({r.get("invoiceid") for r in rs if r.get("invoiceid")}),
                        "payment_check_numbers": sorted({r.get("paymentchecknumber") for r in rs if r.get("paymentchecknumber")}),
                        "unique_ids": [r.get("uniqueid") for r in rs]},
                       title=desc[:200] or None, description=desc or None, instrument_type="vendor payments (no contract published)",
                       commodity={"richmond_object": "; ".join(sorted({f"{r.get('objectcode')} {r.get('object')}" for r in rs}))},
                       value=amt, value_detail={"sum_actual_non_void": amt, "n_rows": len(rs)},
                       dates={"start": first, "amended_last": last}, related={"first_payment": first, "last_payment": last,
                                                                              "projects": sorted({r.get("project") for r in rs if r.get("project")})})
    b = buyer_block(f"City of Richmond, California — {h.get('organization')}", "city department",
                    identifiers={"organizationcode": h.get("organizationcode"), "entity": h.get("entity")})
    ven = vendor_block(v.get("vendorname"), f"Vendors dataset (5mrn-7gkk) state = '{v.get('state')}' (Canadian province code), zip '{v.get('zip')}', city '{v.get('city')}'",
                       identifiers={"richmond_vendor_id": v.get("vendorid")},
                       address={"line1": None, "city": v.get("city"), "region": prov, "postal_code": v.get("zip"), "country": v.get("country")},
                       contact={"phone": v.get("phone"), "web": v.get("webaddress")})
    bas = f"payment-level data, no contract term published; latest expenditure date {last} within 12 months before {REF_S}"
    return record(SK, "Transparent Richmond — Expenditures + Vendors", "City of Richmond, California (transparentrichmond.org)",
                  "https://www.transparentrichmond.org/d/86qj-wgke", None, RET, f"{v.get('vendorid')}-{h.get('organizationcode')}", "end_date_unknown", bas, c, b, ven,
                  {"rows": rs, "vendor_master": v})


if __name__ == "__main__":
    for v in load_jsonl(sys.argv[1]):
        V[v["vendorid"]] = v
    run(load_jsonl(sys.argv[2]), lambda r: (r["vendorid"], r.get("organizationcode")), lambda r: r.get("date"), build, sys.argv[3])

#!/usr/bin/env python3
"""Providence RI 'City and School Department Purchase Orders' (data.providenceri.gov 425y-pm5m); Canadian vendor = state is a
province code and postal_code is not a US ZIP. usage: python3 -I normalize.py <po_ca.jsonl> <out.jsonl>"""
import sys, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_city_providence"; RET = "2026-10-25T19:20:05Z"


def build(k, rs, first, last):
    h = rs[0]
    prov = norm_prov(h.get("state")); pc = (h.get("postal_code") or "").strip()
    if not prov or re.fullmatch(r"\d{5}(-?\d{4})?", pc):
        return None
    amt = sum((parse_amount(r.get("quantity")) or 0) * (parse_amount(r.get("unit_price")) or 0) for r in rs)
    desc = "; ".join(dict.fromkeys((r.get("line_description") or "").strip() for r in rs if r.get("line_description")))
    c = contract_block({"po_number": h["po_number"], "district": h["district"]}, title=desc[:200] or None, description=desc or None,
                       instrument_type="purchase order", value=amt or None, value_detail={"sum_quantity_x_unit_price": amt},
                       dates={"published": first, "signed": first, "start": first})
    bname = "City of Providence" if h["district"] == "CITY" else "Providence Public School Department"
    b = buyer_block(bname, "city" if h["district"] == "CITY" else "school district", identifiers={"district": h["district"]})
    v = vendor_block(h["vendor_name"], f"state = '{h['state']}' (Canadian province code), postal_code '{pc}'" + (" (Canadian format)" if is_ca_postal(pc) else ""),
                     identifiers={"providence_vendor_id": h.get("vendor")},
                     address={"line1": h.get("address1"), "line2": h.get("address2"), "city": h.get("city"), "region": prov, "postal_code": pc, "country": None},
                     contact={"name": h.get("vendor_contct"), "email": h.get("e_mail_address")})
    basis = f"purchase order (no term published); po_date {last} within 12 months before {REF_S}"
    return record(SK, "Providence — City and School Department Purchase Orders", "City of Providence (data.providenceri.gov)",
                  "https://data.providenceri.gov/d/425y-pm5m", None, RET, f"{h['district']}-{h['po_number']}", "end_date_unknown", basis, c, b, v, {"rows": rs})


if __name__ == "__main__":
    run(load_jsonl(sys.argv[1]), lambda r: (r["district"], r["po_number"]), lambda r: r.get("po_date"), build, sys.argv[2])

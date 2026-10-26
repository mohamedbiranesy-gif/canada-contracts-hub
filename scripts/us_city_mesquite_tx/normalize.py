#!/usr/bin/env python3
"""City of Mesquite TX 'Check Register for Open Checkbook' (opendata.cityofmesquite.com 6tva-azs5) joined on vendor_no =
vendor_num to 'Vendor' (qnqi-i9bs) whose state is a Canadian province code AND whose zip starts with a Canadian FSA (letter-
digit-letter; excludes e.g. 'NL' = Netherlands '1841HA'). One record per (vendor_no, org); end_date_unknown iff latest
check_date within 12 months. usage: python3 -I normalize.py <vendors_ca.jsonl> <checks_ca.jsonl> <out.jsonl>"""
import sys, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_city_mesquite_tx"; RET = "2026-10-25T19:47:27Z"; V = {}


def build(k, rs, first, last):
    h = rs[-1]; v = V[h["vendor_no"]]
    prov = norm_prov(v.get("state")); z = (v.get("zip") or "").strip()
    if not prov or not re.match(r"(?i)[A-Z]\d[A-Z]", z):
        return None
    good = [r for r in rs if "VOID" not in (r.get("check_status") or "").upper()]
    amt = sum(filter(None, (parse_amount(r.get("amount")) for r in good)))
    objs = "; ".join(dict.fromkeys(r.get("object_desc") or "" for r in rs))
    c = contract_block({"payment_ids": sorted({r.get("payment_id") for r in rs if r.get("payment_id")}),
                        "inv_numbers": sorted({r.get("inv_number") for r in rs if r.get("inv_number")})},
                       title=objs[:200], description=objs, instrument_type="vendor payments (no contract published)",
                       commodity={"mesquite_object": "; ".join(sorted({f"{r.get('object')} {r.get('object_desc')}" for r in rs}))},
                       value=amt, value_detail={"sum_amount_non_void": amt, "n_payments": len(rs)},
                       dates={"start": first, "amended_last": last}, related={"first_payment": first, "last_payment": last})
    b = buyer_block(f"City of Mesquite, Texas — {h.get('org_desc')}", "city department", identifiers={"org": h.get("org"), "fund": h.get("fund")})
    ven = vendor_block(v.get("vendor_name"), f"Vendor dataset (qnqi-i9bs) state = '{v.get('state')}' (Canadian province code), zip '{z}' (Canadian FSA), city '{v.get('city')}'",
                       identifiers={"mesquite_vendor_num": v.get("vendor_num"), "dba": v.get("dba")},
                       address={"line1": v.get("street_1"), "line2": v.get("street_2"), "city": v.get("city"), "region": prov, "postal_code": z, "country": None})
    bas = f"payment-level data, no contract term published; latest check_date {last} within 12 months before {REF_S}"
    return record(SK, "City of Mesquite Open Checkbook — Check Register + Vendor", "City of Mesquite, Texas (opendata.cityofmesquite.com)",
                  "https://opendata.cityofmesquite.com/d/6tva-azs5", None, RET, f"{v.get('vendor_num')}-{h.get('org')}", "end_date_unknown", bas, c, b, ven,
                  {"rows": rs, "vendor_master": v})


if __name__ == "__main__":
    for v in load_jsonl(sys.argv[1]):
        V[v["vendor_num"]] = v
    run(load_jsonl(sys.argv[2]), lambda r: (r["vendor_no"], r.get("org")), lambda r: r.get("check_date"), build, sys.argv[3])

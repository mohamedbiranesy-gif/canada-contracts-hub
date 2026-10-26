#!/usr/bin/env python3
"""City of Corona CA 'CorStat - Corona Open Expenditures' (corstat.coronaca.gov mdmf-aswt); Canadian vendor = vendor_st is a
province code and vendor_zip is not a 5-digit US ZIP. Individuals ('SURNAME, GIVEN' payees: refunds/reimbursements) skipped.
One record per (vendor_id, department). usage: python3 -I normalize.py <expenditures_ca.jsonl> <out.jsonl>"""
import sys, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_city_corona_ca"; RET = "2026-10-25T19:24:04Z"


def build(k, rs, first, last):
    h = rs[-1]
    prov = norm_prov(h.get("vendor_st")); z = (h.get("vendor_zip") or "").strip()
    if not prov or re.fullmatch(r"\d{5}(-?\d{4})?", z):
        return None
    if re.fullmatch(r"[A-Z'\- ]+, [A-Z'\- ]+", h.get("vendor") or ""):
        return None
    if not h.get("department"):  # deposit refunds / non-departmental disbursements, not purchases
        return None
    amt = sum(filter(None, (parse_amount(r.get("amount")) for r in rs)))
    desc = "; ".join(dict.fromkeys((r.get("description") or "").strip() for r in rs if r.get("description")))[:1500]
    c = contract_block({"payment_ids": sorted({r.get("payment_id") for r in rs if r.get("payment_id")}),
                        "invoice_ids": sorted({r.get("invoice_id") for r in rs if r.get("invoice_id")})},
                       title=desc[:200] or None, description=desc or None, instrument_type="vendor payments (no contract published)",
                       commodity={"corona_expense_category": "; ".join(sorted({r.get('expense_category') or '' for r in rs}))},
                       value=amt, value_detail={"sum_payments": amt, "n_payments": len(rs)},
                       dates={"start": first, "amended_last": last}, related={"first_payment": first, "last_payment": last})
    b = buyer_block(f"City of Corona, California — {h.get('department')}", "city department", identifiers={"department_code": h.get("department_code")})
    v = vendor_block(h.get("vendor"), f"vendor_st = '{h.get('vendor_st')}' (Canadian province code)" + (f", vendor_zip '{z}' (Canadian postal-code format)" if is_ca_postal(z) else (f", vendor_zip '{z}'" if z else "")) + f"; vendor_city '{h.get('vendor_city')}'",
                     identifiers={"corona_vendor_id": h.get("vendor_id")},
                     address={"line1": None, "city": h.get("vendor_city"), "region": prov, "postal_code": z or None, "country": None})
    bas = f"payment-level data, no contract term published; latest payment_date {last} within 12 months before {REF_S}"
    return record(SK, "CorStat - Corona Open Expenditures", "City of Corona, California (corstat.coronaca.gov)",
                  "https://corstat.coronaca.gov/d/mdmf-aswt", None, RET, f"{h.get('vendor_id')}-{h.get('department_code')}", "end_date_unknown", bas, c, b, v, {"rows": rs})


if __name__ == "__main__":
    run(load_jsonl(sys.argv[1]), lambda r: (r.get("vendor_id") or r.get("vendor"), r.get("department_code")), lambda r: r.get("payment_date"), build, sys.argv[2])

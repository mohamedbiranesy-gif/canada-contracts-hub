#!/usr/bin/env python3
"""Alaska Checkbook 'Expense Details Updated' (stateofalaska.data.socrata.com qdjq-crxc); payment-level. Canadian vendor = state
is a province code. One record per (vendor_name, state, dept, division). usage: python3 -I normalize.py <expenses_ca.jsonl> <out.jsonl>"""
import sys
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_state_alaska"; RET = "2026-10-25T19:20:04Z"


def build(k, rs, first, last):
    h = rs[0]
    prov = norm_prov(h.get("state"))
    if not prov:
        return None
    paid = [r for r in rs if (r.get("payment_status") or "").lower() not in ("void", "voided", "cancelled")]
    amt = sum(filter(None, (parse_amount(r.get("amount")) for r in paid)))
    types = "; ".join(dict.fromkeys(r.get("expense_type") or "" for r in rs))
    c = contract_block({"invoice_numbers": sorted({r.get("invoice_number") for r in rs if r.get("invoice_number")}),
                        "transactions": sorted({r.get("transaction") for r in rs if r.get("transaction")})},
                       title=types[:200], description=types, instrument_type="vendor payments (no contract published)",
                       commodity={"alaska_expense_codes": "; ".join(sorted({r.get('expense') or '' for r in rs}))},
                       value=amt, value_detail={"sum_payments": amt, "n_payments": len(rs)},
                       dates={"start": first, "amended_last": last},
                       related={"first_payment": first, "last_payment": last})
    b = buyer_block(f"State of Alaska — {h['department_name']} ({h.get('division_name')})", "state agency",
                    identifiers={"dept": h.get("dept"), "division": h.get("division")})
    v = vendor_block(h["vendor_name"], f"state = '{h['state']}' (Canadian province code in the checkbook vendor state field)",
                     identifiers={"alias_dba": h.get("alias_dba")}, address={"line1": None, "city": None, "region": prov, "postal_code": None, "country": None})
    basis = f"payment-level data, no contract term published; latest transaction_date {last} within 12 months before {REF_S}"
    rid = f"{h.get('dept')}-{h.get('division')}-{h['vendor_name']}".replace(" ", "_")
    return record(SK, "Alaska Checkbook — Expense Details", "State of Alaska, Division of Finance (Alaska Checkbook Online, stateofalaska.data.socrata.com)",
                  "https://stateofalaska.data.socrata.com/d/qdjq-crxc", None, RET, rid, "end_date_unknown", basis, c, b, v, {"rows": rs})


if __name__ == "__main__":
    run(load_jsonl(sys.argv[1]), lambda r: (r["vendor_name"], r["state"], r.get("dept"), r.get("division")), lambda r: r.get("transaction_date"), build, sys.argv[2])

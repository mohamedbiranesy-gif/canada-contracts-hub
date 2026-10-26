#!/usr/bin/env python3
"""Montgomery County MD 'County Spending' (data.montgomerycountymd.gov vpf9-6irq), payments 2025-10-25..2026-10-25 whose vendor_zip
is a Canadian postal code. Grouped per (vendor_id, contract_num | po_num | department). When contract_num is in the active
'Contracts' list (vmu2-pnrc CSV), status/dates come from Execution/Expiration Date (ongoing); contracts already emitted by
us_county_montgomery_md are skipped (dedupe). usage: python3 -I normalize.py <spending.jsonl> <contracts_vmu2-pnrc.csv> <us_county_montgomery_md.jsonl> <out.jsonl>"""
import sys, csv, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_county_montgomery_md_spending"; RET = "2026-10-25T20:01:57Z"
C = {}; DONE = set()


def key(r):
    if r.get("contract_num"):
        return (r["vendor_id"], "C" + r["contract_num"])
    if r.get("po_num"):
        return (r["vendor_id"], "P" + r["po_num"])
    return (r["vendor_id"], "D" + (r.get("department") or ""))


def build(k, rs, first, last):
    h = rs[-1]; z = (h.get("vendor_zip") or "").strip()
    if not is_ca_postal(z) or not PC_RE.fullmatch(z.upper().replace(" ", "")[:3] + " " + z.upper().replace(" ", "")[3:]):
        return None
    cn = h.get("contract_num")
    if cn and cn in DONE:
        return None
    amt = sum(filter(None, (parse_amount(r.get("amount")) for r in rs)))
    desc = "; ".join(dict.fromkeys(f"{r.get('expense_category')} / {r.get('description')}" for r in rs))
    con = C.get(cn) if cn else None
    if con:
        start, end = parse_date(con.get("Execution Date")), parse_date(con.get("Expiration Date"))
        status, basis = status_from_dates(start, end)
        if not status:
            return None
        basis = f"active Contracts list (vmu2-pnrc) contract {cn}: Execution Date {start} <= {REF_S} <= Expiration Date {end}; payments to {last}"
        title = con.get("ContractDesc")
    else:
        start, end, status = None, None, "end_date_unknown"
        basis = (f"payments under contract {cn} (not in the active Contracts list, no term published); " if cn else "payment-level data, no contract term published; ") + f"latest payment_date {last} within 12 months before {REF_S}"
        title = desc[:200]
    ids = {"contract_num": cn, "po_nums": sorted({r.get("po_num") for r in rs if r.get("po_num")}),
           "invoice_ids": sorted({r.get("invoice_id") for r in rs if r.get("invoice_id")}), "payment_ids": sorted({r.get("payment_id") for r in rs if r.get("payment_id")})}
    if con:
        ids["solicitation_number"] = con.get("SolicitationNumber")
    c = contract_block(ids, title=title, description=desc, instrument_type=(con.get("ContractType") if con else None) or ("contract (payments)" if cn else "purchase order / payments"),
                       commodity={"mc_account_code": "; ".join(sorted({f"{r.get('account_code')} {r.get('description')}" for r in rs}))},
                       value=amt, value_detail={"sum_payments_12m": amt, "n_payment_rows": len(rs)},
                       dates={"signed": start, "start": start or first, "end": end, "amended_last": last},
                       related={"first_payment_in_window": first, "last_payment": last, "extend_date": parse_date(con.get("Extend Date")) if con else None})
    dept = (con.get("DeptName") if con else None) or h.get("department")
    b = buyer_block(f"Montgomery County, Maryland — {dept}", "county department",
                    contact=({"buyer": f"{con.get('Buyer First Name')} {con.get('Buyer Last Name')}", "email": con.get("BuyerEmail"), "phone": con.get("BuyerPhone")} if con else {}))
    addr = {"line1": None, "city": None, "region": None, "postal_code": z, "country": None}
    if con:
        addr = {"line1": con.get("Vendor Address Line 1"), "line2": con.get("Vendor Address Line 2"), "city": con.get("Vendor City"),
                "region": con.get("Vendor State"), "postal_code": con.get("Vendor Zip Code") or z, "country": None}
    v = vendor_block(h.get("vendor"), f"County Spending vendor_zip = '{z}' (Canadian postal-code format)" + (f"; Contracts list address: {con.get('Vendor City')}, {con.get('Vendor State')} {con.get('Vendor Zip Code')}" if con else ""),
                     identifiers={"mc_vendor_id": h.get("vendor_id")}, address=addr,
                     contact=({"name": con.get("Vendor Contact"), "email": con.get("Vendor Email"), "phone": con.get("Vendor Phone Number")} if con else {}))
    return record(SK, "Montgomery County MD — County Spending (+ active Contracts list)", "Montgomery County, Maryland (dataMontgomery)",
                  "https://data.montgomerycountymd.gov/d/vpf9-6irq", None, RET, re.sub(r"[^A-Za-z0-9-]+", "_", f"{k[0]}-{k[1]}"), status, basis, c, b, v,
                  {"rows": rs, "contract_row": con})


if __name__ == "__main__":
    for r in csv.DictReader(open(sys.argv[2], encoding="utf-8", errors="replace", newline="")):
        C[r["Contract Number"].strip()] = r
    for l in open(sys.argv[3]):
        j = json.loads(l); DONE.add(j["record_id"].split(":", 1)[1])
    run(load_jsonl(sys.argv[1]), key, lambda r: r.get("payment_date"), build, sys.argv[4])

#!/usr/bin/env python3
"""Vermont 'Purchase Orders with Vendor Information' (data.vermont.gov 8ewu-igdm), Canadian vendor = st is a province code.
usage: python3 -I normalize.py <po_ca_8ewu-igdm.jsonl> <out.jsonl>"""
import sys
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_state_vermont"; RET = "2026-10-25T19:20:04Z"


def build(k, rs, first, last):
    h = rs[0]
    prov = norm_prov(h.get("st"))
    if not prov:
        return None
    amt = sum(filter(None, (parse_amount(r.get("merchandise_amt")) for r in rs)))
    desc = "; ".join(dict.fromkeys((r.get("item_long_descr") or "").strip() for r in rs if r.get("item_long_descr")))[:2000]
    c = contract_block({"po_id": h["po_id"], "business_unit": h["business_unit"], "items": sorted({r["item"] for r in rs if r.get("item")}) or None},
                       title=desc[:200] or None, description=desc or None, instrument_type="purchase order",
                       value=amt, value_detail={"sum_merchandise_amt": amt},
                       dates={"published": first, "signed": first, "start": first, "amended_last": last if last != first else None})
    b = buyer_block(f"State of Vermont — {h['business_unit_descr']}", "state agency", identifiers={"business_unit": h["business_unit"]})
    v = vendor_block(h["vendor_name"], f"st = '{h['st']}' (Canadian province code; city '{h.get('city')}')",
                     identifiers={"vermont_supplier_id": h["supplier"]}, address={"line1": None, "city": h.get("city"), "region": prov, "postal_code": None, "country": None})
    basis = f"purchase order (no term published); po_date {last} within 12 months before {REF_S}"
    return record(SK, "State of Vermont — Purchase Orders with Vendor Information", "State of Vermont, Department of Finance & Management (data.vermont.gov)",
                  "https://data.vermont.gov/d/8ewu-igdm", None, RET, f"{h['business_unit']}-{h['po_id']}", "end_date_unknown", basis, c, b, v, {"rows": rs})




# ---- added on resume: payment-derived records for (vendor, agency) pairs without a PO in 8ewu-igdm ----
# usage: python3 -I normalize.py <po_ca_8ewu-igdm.jsonl> <out.jsonl> <payments_ca_786x-sbp3.jsonl>
import re as _re


def pay_records(pay_path, po_rows, w):
    popairs = {((p.get("supplier") or "").lstrip("0"), p.get("business_unit")) for p in po_rows}
    g = {}
    for p in load_jsonl(pay_path):
        g.setdefault((p.get("vno"), p.get("unitno")), []).append(p)
    st = {}
    for (vno, unit), rs in g.items():
        q = sorted(filter(None, (parse_date(r.get("qtrending")) for r in rs)))
        last = q[-1] if q else None
        if not last or last < WIN or last > REF_S:
            continue
        rs = [r for r in rs if (parse_date(r.get("qtrending")) or "") >= WIN]
        h = rs[0]
        if vno == "SINGLE" or _re.fullmatch(r"[A-Za-z'\- ]+,[A-Za-z'\- ]+(,[A-Za-z ]*)?", h.get("vendor") or ""):
            st["skip_single_or_individual"] = st.get("skip_single_or_individual", 0) + 1; continue
        if ((vno or "").lstrip("0"), unit) in popairs:
            st["skip_has_po"] = st.get("skip_has_po", 0) + 1; continue
        prov = norm_prov(h.get("state"))
        amt = sum(filter(None, (parse_amount(r.get("amt")) for r in rs)))
        desc = "; ".join(dict.fromkeys(f"{r.get('description')} / {r.get('account')}" for r in rs))
        c = contract_block({"vermont_vendor_no": vno, "unitno": unit, "quarters": sorted({r.get('qtrending')[:10] for r in rs})},
                           title=desc[:200], description=desc, instrument_type="vendor payments (quarterly totals; no PO/contract published)",
                           commodity={"vermont_account": "; ".join(sorted({f"{r.get('acctno')} {r.get('account')}" for r in rs}))},
                           value=amt, value_detail={"sum_amt_quarters_in_window": amt},
                           dates={"start": q[0], "amended_last": last}, related={"first_quarter_end": q[0], "last_quarter_end": last})
        b = buyer_block(f"State of Vermont — {h.get('govtunit')}", "state agency", identifiers={"unitno": unit})
        v = vendor_block(h.get("vendor"), f"Vermont Vendor Payments (786x-sbp3) state = '{h.get('state')}' (Canadian province code); city '{h.get('city')}'",
                         identifiers={"vermont_vendor_no": vno}, address={"line1": None, "city": h.get("city"), "region": prov, "postal_code": None, "country": None})
        bas = f"quarterly payment totals, no contract term published; latest quarter ending {last} within 12 months before {REF_S}; no PO for this vendor/agency in 8ewu-igdm"
        w.write(record(SK, "State of Vermont — Vermont Vendor Payments (quarterly)", "State of Vermont, Department of Finance & Management (data.vermont.gov)",
                       "https://data.vermont.gov/d/786x-sbp3", None, "2026-10-25T19:20:07Z", f"PAY-{unit}-{vno}", "end_date_unknown", bas, c, b, v, {"rows": rs}))
        st["written"] = st.get("written", 0) + 1
    print("payments:", st)


if __name__ == "__main__":
    po_rows = load_jsonl(sys.argv[1])
    run(po_rows, lambda r: (r["business_unit"], r["po_id"]), lambda r: r.get("po_date"), build, sys.argv[2])
    if len(sys.argv) > 3:
        w = open(sys.argv[2], "a", encoding="utf-8")
        class _W:
            def write(self, rec):
                w.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        pay_records(sys.argv[3], po_rows, _W()); w.close()

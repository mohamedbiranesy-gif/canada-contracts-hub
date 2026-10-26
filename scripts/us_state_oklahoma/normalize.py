#!/usr/bin/env python3
"""State of Oklahoma 'Vendor Payments' monthly files (data.ok.gov CKAN datastore, FY2026 + FY2027 packages), rows whose STATE is a
Canadian province code. One record per (AGENCYNBR, VENDOR_NAME); end_date_unknown iff latest EFFDT within 12 months.
usage: python3 -I normalize.py <out.jsonl> <vendor_payments_ca_YYYYMM.jsonl>..."""
import sys, re
sys.path.insert(0, "scripts/us_common")
from po_group import *

SK = "us_state_oklahoma"; RET = "2026-10-25T19:52:25Z"
uq = lambda s: (s or "").strip().strip('"').strip() or None


def build(k, rs, first, last):
    h = rs[0]
    prov = norm_prov(h.get("STATE"))
    if not prov:
        return None
    amt = sum(filter(None, (parse_amount(r.get("PYMNT_AMT")) for r in rs)))
    accts = "; ".join(dict.fromkeys(uq(r.get("ACCTDESCR")) or "" for r in rs))
    c = contract_block({"voucher_ids": sorted({r.get("VOUCHER_ID") for r in rs}), "related_voucher_ids": sorted({r.get("VOUCHER_ID_RELATED") for r in rs if (r.get("VOUCHER_ID_RELATED") or "").strip()})},
                       title=accts[:200], description=accts, instrument_type="vendor payment vouchers (no contract published)",
                       commodity={"ok_account": "; ".join(sorted({f"{r.get('ACCOUNT')} {uq(r.get('ACCTDESCR'))}" for r in rs}))},
                       value=amt, value_detail={"sum_pymnt_amt": amt, "n_rows": len(rs)},
                       dates={"start": first, "amended_last": last}, related={"voucher_styles": sorted({r.get('VOUCHER_STYLE') for r in rs})})
    b = buyer_block(f"State of Oklahoma — {uq(h.get('AGENCYNAME'))}", "state agency / institution", identifiers={"agency_nbr": h.get("AGENCYNBR")})
    v = vendor_block(uq(h.get("VENDOR_NAME")), f"STATE = '{h.get('STATE')}' (Canadian province code), POSTAL '{h.get('POSTAL')}', CITY '{h.get('CITY')}'",
                     address={"line1": None, "city": h.get("CITY"), "region": prov, "postal_code": h.get("POSTAL"), "country": None})
    zero = " All rows are JRNL-style vouchers with PYMNT_AMT 0 (accounting entries tied to earlier vouchers VOUCHER_ID_RELATED)." if amt == 0 else ""
    bas = f"payment-voucher data, no contract term published; latest EFFDT {last} within 12 months before {REF_S}.{zero}"
    rec = record(SK, "State of Oklahoma Vendor Payments (monthly)", "Oklahoma Office of Management and Enterprise Services (data.ok.gov)",
                 "https://data.ok.gov/dataset/state-of-oklahoma-vendor-payments-fiscal-year-2026", None, RET,
                 f"{h.get('AGENCYNBR')}-{re.sub(r'[^A-Za-z0-9]+', '_', uq(h.get('VENDOR_NAME')) or '')}", "end_date_unknown", bas, c, b, v, {"rows": rs})
    return rec


if __name__ == "__main__":
    rows = []
    for p in sys.argv[2:]:
        for r in load_jsonl(p):
            r.pop("_full_text", None); r["_source_file"] = p.rsplit("/", 1)[-1]; rows.append(r)
    run(rows, lambda r: (r.get("AGENCYNBR"), uq(r.get("VENDOR_NAME"))), lambda r: (r.get("EFFDT") or "").split(" ")[0].replace("-", "/"), build, sys.argv[1])

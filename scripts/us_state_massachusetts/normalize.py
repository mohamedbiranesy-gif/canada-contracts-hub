#!/usr/bin/env python3
"""Normalize Massachusetts CTHRU 'Comptroller of the Commonwealth Spending' (cthru.data.socrata.com pegc-naaa) payment
rows whose vendor state is a Canadian province -> one record per encumbrance (contract/PO document id) with a payment in
the 12 months before the reference date. Payment-level data: no end dates -> end_date_unknown.
usage: python3 -I normalize.py <jsonl> <out.jsonl>
"""
import sys, json, re, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_state_massachusetts"
DSID = "pegc-naaa"
RECENT_CUTOFF = "2025-10-25"


def main():
    path, out = sys.argv[1], sys.argv[2]
    retrieved = file_mtime_iso(path)
    w = Writer(out)
    stats = collections.Counter()
    g = collections.OrderedDict()
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        stats["rows"] += 1
        if not norm_prov((r.get("state") or "").strip()):
            continue
        stats["canadian_rows"] += 1
        enc = (r.get("encumbrance_id") or "").strip()
        key = (enc, (r.get("vendor") or "").strip().upper(), r.get("department_code"))
        g.setdefault(key, []).append(r)
    stats["encumbrances"] = len(g)
    for (enc, vname, dept), rows in g.items():
        rows.sort(key=lambda x: (x.get("date") or "", x.get("payment_id") or ""))
        last = rows[-1]
        last_pay = parse_date(last.get("date"))
        if not last_pay or last_pay < RECENT_CUTOFF:
            stats["excluded_no_recent_payment"] += 1
            continue
        status = "end_date_unknown"
        basis = f"payment-level data (encumbrance {enc}) without contract dates; latest payment {last_pay} within 12 months before {REF_S}"
        m = re.match(r"\((\w+)\)\s*(.*)", enc)
        doc_type, doc_id = (m.group(1), m.group(2)) if m else (None, enc)
        tot = round(sum(parse_amount(x.get("amount")) or 0 for x in rows), 2)
        contract = contract_block(
            identifiers={"encumbrance_id": enc, "encumbrance_document_type": doc_type, "encumbrance_document_id": doc_id, "payment_ids": [x.get("payment_id") for x in rows],
                         "base_ids": [x.get("base_id") for x in rows]},
            title=f"{last.get('object_code')} - {last.get('appropriation_name')}", description=f"{last.get('object_class')}; {last.get('object_code')}; appropriation {last.get('appropriation_name')}",
            instrument_type=f"encumbrance ({doc_type})" if doc_type else "encumbrance", commodity={"mmars_object_code": last.get("object"), "object_code_description": last.get("object_code")},
            value=tot, currency="USD", value_detail={"sum_of_payments_fy2025_onward": tot, "payments": len(rows), "fiscal_years": sorted(set(x.get("budget_fiscal_year") for x in rows))},
            dates={"start": parse_date(rows[0].get("date")), "amended_last": last_pay},
            related={"first_payment": parse_date(rows[0].get("date")), "last_payment": last_pay, "fund": last.get("fund"), "appropriation_code": last.get("appropriation_code")},
        )
        buyer = buyer_block(f"Commonwealth of Massachusetts - {last.get('department')}", "state department", "US",
                            identifiers={"department_code": dept, "cabinet_secretariat": last.get("cabinet_secretariat")})
        vendor = vendor_block(last.get("vendor"), f"state = '{last.get('state')}' (Canadian province code) in CTHRU vendor address", identifiers={"cthru_vendor_id": last.get("vendor_id")},
                              address={"city": last.get("city"), "region": last.get("state"), "postal_code": last.get("zip_code"), "country": None})
        rid = re.sub(r"[^A-Za-z0-9]+", "_", f"{enc}:{vname}:{dept}")
        rec = record(SOURCE_KEY, "CTHRU - Comptroller of the Commonwealth Spending (Massachusetts)", "Office of the Comptroller of the Commonwealth of Massachusetts",
                     f"https://cthru.data.socrata.com/d/{DSID}", None, retrieved, rid, status, basis, contract, buyer, vendor, {"dataset_id": DSID, "rows": rows})
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

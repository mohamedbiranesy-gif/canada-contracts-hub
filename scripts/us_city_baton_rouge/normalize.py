#!/usr/bin/env python3
"""Normalize Baton Rouge / East Baton Rouge Parish 'Purchase Orders and Contracts' (data.brla.gov 2ung-w7t4) for vendors
whose VENDOR STATE is a Canadian province code (or blank state + Canadian postal code in VENDOR ZIP).
One record per DOCUMENT NUMBER (all rows in raw.rows). Kept as end_date_unknown iff latest INPUT DATE is within the
12 months before the reference date and no START/EXPIRATION date says otherwise; ongoing if EXPIRATION/EXTENSION >= ref.
usage: python3 -I normalize.py <po_contracts_2ung-w7t4.csv> <out.jsonl>
"""
import sys, csv, collections, datetime
sys.path.insert(0, "scripts/us_common")
from common import *

SK = "us_city_baton_rouge"
WIN = "2025-10-25"


def ca_basis(r):
    s = r["VENDOR STATE"].strip().upper()
    if norm_prov(s):
        return f"VENDOR STATE = '{s}' (Canadian province code); VENDOR ZIP '{r['VENDOR ZIP'].strip()}'"
    if not s and is_ca_postal(r["VENDOR ZIP"]):
        return f"VENDOR STATE blank; VENDOR ZIP '{r['VENDOR ZIP'].strip()}' is a Canadian postal code (VENDOR CITY '{r['VENDOR CITY'].strip()}')"
    return None


def main():
    src, out = sys.argv[1], sys.argv[2]
    ret = "2026-10-25T17:26:12Z"
    docs = collections.OrderedDict()
    for r in csv.DictReader(open(src, encoding="utf-8", errors="replace", newline="")):
        if ca_basis(r):
            docs.setdefault(r["DOCUMENT NUMBER"], []).append(r)
    w = Writer(out); st = collections.Counter()
    for dn, rows in docs.items():
        st["docs"] += 1
        inputs = sorted(filter(None, (parse_date(x["INPUT DATE"]) for x in rows)))
        last = inputs[-1] if inputs else None
        hdr = next((x for x in rows if x["RECORD TYPE"] == "H"), rows[0])
        stat_desc = {x["DOCUMENT STATUS DESCRIPTION"] for x in rows}
        if any("cancel" in s.lower() for s in stat_desc):
            st["excl_cancelled"] += 1; continue
        start = next(filter(None, (parse_date(x["START DATE"]) for x in rows)), None)
        exp = max(filter(None, [parse_date(x["EXPIRATION DATE"]) for x in rows] + [parse_date(x["EXTENSION DATE"]) for x in rows]), default=None)
        if exp:
            status, basis = status_from_dates(start or last, exp)
            if not status:
                st["excl_dates"] += 1; continue
            basis = f"START DATE {start} / EXPIRATION-EXTENSION DATE {exp}: " + basis
        else:
            if not last or last < WIN or last > REF_S:
                st["excl_older_than_12m"] += 1; continue
            status = "end_date_unknown"
            basis = f"purchase order without START/EXPIRATION date; latest INPUT DATE {last} within 12 months before {REF_S}"
        total = parse_amount(hdr["TOTAL AMOUNT"])
        items = sum(filter(None, (parse_amount(x["ITEM TOTAL COST"]) for x in rows if x["RECORD TYPE"] == "D")))
        desc = "; ".join(dict.fromkeys(x["ITEM DESCRIPTION"].strip() for x in rows if x["ITEM DESCRIPTION"].strip()))[:2000]
        comm = {"brla_commodity": "; ".join(dict.fromkeys(x["COMMODITY CODE"] for x in rows if x["COMMODITY CODE"])),
                "brla_commodity_description": "; ".join(dict.fromkeys(x["COMMODITY DESCRIPTION"] for x in rows if x["COMMODITY DESCRIPTION"]))}
        contract = contract_block(
            identifiers={"document_number": dn, "requisition_number": hdr["REQUISITION NUMBER"] or None,
                         "source_document_type": hdr["SOURCE DOCUMENT TYPE"], "document_type_code": hdr["DOCUMENT TYPE CODE"]},
            title=hdr["DOCUMENT DESCRIPTION"], description=desc or hdr["DOCUMENT DESCRIPTION"],
            instrument_type="purchase order" + (" (annual contract)" if hdr["ANNUAL CONTRACT"].strip() else ""),
            commodity=comm, value=total if total else (items or None), currency="USD",
            value_detail={"total_amount": total, "vouched_amount": parse_amount(hdr["VOUCHED AMOUNT"]), "sum_item_total_cost": items},
            dates={"published": inputs[0] if inputs else None, "signed": inputs[0] if inputs else None, "start": start, "end": exp, "amended_last": last})
        buyer = buyer_block(f"City of Baton Rouge / Parish of East Baton Rouge — {hdr['DEPARTMENT NAME'].strip()}", "city-parish department",
                            identifiers={"department_number": hdr["DEPARTMENT NUMBER"], "cost_center": hdr["COST CENTER"], "cost_center_name": hdr["COST CENTER NAME"]})
        vendor = vendor_block(" ".join(filter(None, [hdr["VENDOR NAME 1"].strip(), hdr["VENDOR NAME 2"].strip()])), ca_basis(hdr),
                              address={"line1": None, "city": hdr["VENDOR CITY"].strip(), "region": norm_prov(hdr["VENDOR STATE"]) or hdr["VENDOR STATE"].strip() or None,
                                       "postal_code": hdr["VENDOR ZIP"].strip(), "country": None})
        raw = {"rows": rows}
        rec = record(SK, "City of Baton Rouge / East Baton Rouge Parish — Purchase Orders and Contracts", "City of Baton Rouge / Parish of East Baton Rouge (data.brla.gov)",
                     "https://data.brla.gov/d/2ung-w7t4", None, ret, dn, status, basis, contract, buyer, vendor, raw)
        w.write(rec); st[status] += 1
    print(w.close(), dict(st))


if __name__ == "__main__":
    main()

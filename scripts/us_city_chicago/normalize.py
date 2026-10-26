#!/usr/bin/env python3
"""Normalize City of Chicago 'Contracts' (data.cityofchicago.org rsxa-ify5) -> Canadian-vendor ongoing contracts.
usage: python3 -I normalize.py <jsonl> <out.jsonl>
One record per (Purchase Order (Contract) Number, Vendor ID); all revision rows kept in raw.rows; latest revision drives dates/amount.
"""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_city_chicago"
DSID = "rsxa-ify5"
RECENT_CUTOFF = "2024-01-01"  # for rows without an end date: approval date must be on/after this


def canadian(r):
    st = (r.get("state") or "").strip()
    stu = st.upper()
    z = (r.get("zip") or "").strip()
    if stu in ("CAN", "CANADA"):
        return True, f"State field = '{st}' (Canada)"
    p = norm_prov(stu.split(",")[0].strip())
    if p:
        return True, f"State field = '{st}' (Canadian province)"
    if is_ca_postal(z) and not stu:
        return True, f"Canadian-format Zip '{z}' with empty State"
    return False, None


def main():
    path, out = sys.argv[1], sys.argv[2]
    retrieved = file_mtime_iso(path)
    w = Writer(out)
    stats = collections.Counter()
    groups = collections.OrderedDict()
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            stats["rows"] += 1
            ok, basis = canadian(r)
            if not ok:
                continue
            stats["canadian_rows"] += 1
            r["_basis"] = basis
            groups.setdefault((r.get("purchase_order_contract_number"), r.get("vendor_id")), []).append(r)
    stats["canadian_contracts"] = len(groups)
    for (po, vid), rows in groups.items():
        rows.sort(key=lambda x: int(x.get("revision_number") or 0))
        latest = rows[-1]
        start = parse_date(latest.get("start_date"))
        end = parse_date(latest.get("end_date"))
        appr = parse_date(latest.get("approval_date"))
        if end:
            status, basis = status_from_dates(start or appr, end)
            if not status:
                stats["excluded_ended" if "ended" in basis else "excluded_future"] += 1
                continue
            basis = f"Start Date {start} <= {REF_S} <= End Date {end} (revision {latest.get('revision_number')})"
        else:
            if not appr or appr < RECENT_CUTOFF:
                stats["excluded_stale_no_end"] += 1
                continue
            status = "end_date_unknown"
            basis = f"no Start/End Date published; Approval Date {appr} >= {RECENT_CUTOFF}"
        amt = parse_amount(latest.get("award_amount"))
        pdf = latest.get("contract_pdf")
        pdf_url = pdf.get("url") if isinstance(pdf, dict) else pdf
        contract = contract_block(
            identifiers={"purchase_order_contract_number": po, "specification_number": latest.get("specification_number"),
                         "revision_numbers": [x.get("revision_number") for x in rows], "vendor_id": vid},
            title=latest.get("purchase_order_description"), description=latest.get("purchase_order_description"),
            instrument_type=latest.get("contract_type"), procurement_method=latest.get("procurement_type"),
            value=amt, currency="USD",
            value_detail={"award_amount_latest_revision": amt,
                          "award_amount_by_revision": {x.get("revision_number"): parse_amount(x.get("award_amount")) for x in rows}},
            dates={"signed": appr, "start": start, "end": end,
                   "amended_last": parse_date(latest.get("approval_date")) if len(rows) > 1 else None},
            related={"contract_pdf": pdf_url},
        )
        buyer = buyer_block(f"City of Chicago - {latest.get('department')}" if latest.get("department") else "City of Chicago", "city department", "US",
                            identifiers={"department": latest.get("department")})
        addr = {"line1": latest.get("address_1"), "line2": latest.get("address_2"), "city": latest.get("city"),
                "region": latest.get("state"), "postal_code": latest.get("zip"), "country": None}
        vendor = vendor_block(latest.get("vendor_name"), latest["_basis"], identifiers={"chicago_vendor_id": vid}, address=addr)
        raw = {"dataset_id": DSID, "rows": [{k: v for k, v in x.items() if not k.startswith("_")} for x in rows]}
        rec = record(SOURCE_KEY, "City of Chicago Contracts (Chicago Data Portal)", "City of Chicago Department of Procurement Services",
                     f"https://data.cityofchicago.org/d/{DSID}", pdf_url, retrieved, f"{po}:{vid}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

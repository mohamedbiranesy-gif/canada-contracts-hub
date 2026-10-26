#!/usr/bin/env python3
"""Normalize data.ny.gov twsw-2mqa 'MTA Procurements: Beginning 2018' -> Canadian-vendor ongoing contracts.
usage: python3 -I normalize.py <csv> <out.jsonl>
"""
import sys, csv, re, collections, hashlib
sys.path.insert(0, "scripts/us_common")
from common import *

csv.field_size_limit(10**9)
SOURCE_KEY = "us_ny_mta"
DSID = "twsw-2mqa"
STALE_FY_CUTOFF = "2024-01-01"


def canadian(row):
    co = (row.get("Country") or "").strip().upper()
    reg = (row.get("Region") or "").strip()
    st = (row.get("State") or "").strip()
    pc = row.get("Postal Code") or ""
    if co == "CAN":
        return True, "Country = 'CAN'"
    if co == "OTHER":
        if norm_prov(reg):
            return True, f"Country = 'OTHER' (non-US) with Region = '{reg}' (Canadian province code)"
        if norm_prov(st):
            return True, f"Country = 'OTHER' (non-US) with State = '{st}' (Canadian province code)"
        if is_ca_postal(pc):
            return True, f"Country = 'OTHER' (non-US) with Canadian-format Postal Code '{pc}'"
    return False, None


def key_of(row):
    tn = (row.get("Transaction Number") or "").strip()
    v = row["Vendor Name"].strip().upper()
    if tn and not re.match(r"^\d(\.\d+)?E\+\d+$", tn):
        return ("TN", tn, v)
    return (v, (row.get("Procurement Description") or "").strip().upper(), (row.get("Award Date") or "").strip(),
            (row.get("Begin Date") or "").strip())


def main():
    path, out = sys.argv[1], sys.argv[2]
    retrieved = file_mtime_iso(path)
    w = Writer(out)
    stats = collections.Counter()
    groups = collections.OrderedDict()
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            stats["rows"] += 1
            ok, basis = canadian(row)
            if not ok:
                continue
            stats["canadian_rows"] += 1
            row["_country_basis"] = basis
            groups.setdefault(key_of(row), []).append(row)
    stats["canadian_contracts"] = len(groups)
    for k, rows in groups.items():
        rows.sort(key=lambda r: parse_date(r["Fiscal Year End Date"]) or "")
        latest = rows[-1]
        last_fy = parse_date(latest["Fiscal Year End Date"])
        st = (latest.get("Status") or "").strip()
        award = parse_date(latest.get("Award Date"))
        start = parse_date(latest.get("Begin Date")) or award
        end = parse_date(latest.get("End Date"))
        if st.upper() == "COMPLETED":
            stats["excluded_completed"] += 1
            continue
        if end:
            status, basis = status_from_dates(start, end)
            if not status:
                stats["excluded_ended" if "ended" in basis else "excluded_future"] += 1
                continue
            basis = f"Begin Date {start} <= {REF_S} <= End Date {end}; Status='{st}' in latest report (FY ending {last_fy})"
        else:
            if start and start > REF_S:
                stats["excluded_future"] += 1
                continue
            if not last_fy or last_fy < STALE_FY_CUTOFF:
                stats["excluded_stale_no_end"] += 1
                continue
            status = "end_date_unknown"
            basis = f"no End Date published; Status='{st}'; Award Date {award or 'n/a'}; last reported FY ending {last_fy}"
        rid = hashlib.sha1("|".join(k).encode("utf-8")).hexdigest()[:16]
        tn = (latest.get("Transaction Number") or "").strip()
        amt = parse_amount(latest.get("Contract Amount"))
        vd = {"contract_amount": amt, "fair_market_value": parse_amount(latest.get("Fair Market Value")),
              "amount_expended_for_fiscal_year_latest": parse_amount(latest.get("Amount Expended For Fiscal Year")),
              "amount_expended_to_date": parse_amount(latest.get("Amount Expended to Date")),
              "current_or_outstanding_balance": parse_amount(latest.get("Current or Outstanding Balance"))}
        contract = contract_block(
            identifiers={"transaction_number": tn or None, "dataset_id": DSID},
            title=latest.get("Procurement Description") or None, description=latest.get("Procurement Description") or None,
            instrument_type=latest.get("Award Process") or None, procurement_method=latest.get("Award Process") or None,
            commodity={"mta_type_of_procurement": latest.get("Type of Procurement") or None},
            value=amt, currency="USD", value_detail={a: b for a, b in vd.items() if b is not None},
            dates={"signed": award, "start": start, "end": end, "amended_last": parse_date(latest.get("Renewal Date"))},
            related={"fiscal_years_reported": [parse_date(r["Fiscal Year End Date"]) for r in rows],
                     "status_in_latest_report": st or None,
                     "number_of_bids_or_proposals_received": latest.get("Number of Bids or Proposals Received") or None,
                     "vendor_is_nys_or_fbe": latest.get("Vendor is NYS or FBE") or None,
                     "exempt_from_article_4c": latest.get("Exempt from Article 4c") or None},
        )
        buyer = buyer_block("Metropolitan Transportation Authority", "NY state public authority (transit)", "US",
                            identifiers={"abo_authority_name": "Metropolitan Transportation Authority"})
        addr = {"line1": latest.get("Address Line 1") or None, "line2": latest.get("Address Line 2") or None,
                "city": latest.get("City") or None, "region": latest.get("Region") or latest.get("State") or None,
                "postal_code": latest.get("Postal Code") or None, "country": latest.get("Country") or None}
        vendor = vendor_block(latest["Vendor Name"].strip(), latest["_country_basis"], address=addr)
        raw = {"dataset_id": DSID, "rows": [{kk: vv for kk, vv in r.items() if not kk.startswith("_")} for r in rows]}
        rec = record(SOURCE_KEY, "MTA Procurements: Beginning 2018 (Open Data NY)", "Metropolitan Transportation Authority via data.ny.gov",
                     f"https://data.ny.gov/d/{DSID}", None, retrieved, rid, status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

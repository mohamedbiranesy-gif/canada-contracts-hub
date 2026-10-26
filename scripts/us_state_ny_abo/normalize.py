#!/usr/bin/env python3
"""Normalize NY Authorities Budget Office (ABO) procurement reports (data.ny.gov) -> Canadian-vendor ongoing contracts.
usage: python3 -I normalize.py <downloads_dir> <out.jsonl>
Datasets (CSV exports): ehig-g5x3 State Authorities, 8w5p-k45m Local Authorities, d84c-dk28 LDCs, p3p6-xqr5 IDAs.
"""
import sys, os, csv, re, collections
sys.path.insert(0, "scripts/us_common")
from common import *

csv.field_size_limit(10**9)
SOURCE_KEY = "us_state_ny_abo"
DATASETS = [
    ("state_authorities_ehig-g5x3.csv", "ehig-g5x3", "Procurement Report for State Authorities", "state authority"),
    ("local_authorities_8w5p-k45m.csv", "8w5p-k45m", "Procurement Report for Local Authorities", "local authority"),
    ("ldc_d84c-dk28.csv", "d84c-dk28", "Procurement Report for Local Development Corporations", "local development corporation"),
    ("ida_p3p6-xqr5.csv", "p3p6-xqr5", "Procurement Report for Industrial Development Agencies", "industrial development agency"),
]
STALE_FY_CUTOFF = "2024-01-01"  # rows without an end date are kept only if last reported in a fiscal year ending on/after this


def canadian(row):
    """Return (True, basis) if the vendor is in Canada per structured fields, else (False, None)."""
    vc = (row.get("Vendor Country") or "").strip()
    vcu = vc.upper()
    pr = (row.get("Vendor Province/Region") or "").strip()
    prov = norm_prov(pr)
    pc = row.get("Vendor Postal Code") or ""
    if vcu in ("CAN", "CANADA"):
        return True, f"Vendor Country = '{vc}'"
    if vcu == "CA":
        # 'CA' is ambiguous (California); accept only with a Canadian province or postal code
        if prov:
            return True, f"Vendor Country = 'CA' with Vendor Province/Region = '{pr}'"
        if is_ca_postal(pc):
            return True, f"Vendor Country = 'CA' with Canadian-format Vendor Postal Code '{pc}'"
        return False, None
    if norm_prov(vcu):
        return True, f"Vendor Country field holds a Canadian province name '{vc}'"
    if prov and re.fullmatch(r"\d[A-Z]\d", vcu) and (row.get("Vendor State") or "").strip() == "":
        return True, f"Vendor Province/Region = '{pr}' (Vendor Country field '{vc}' is a Canadian postal-code fragment)"
    return False, None


def key_of(row):
    tn = (row.get("Transaction Number") or "").strip()
    base = (row["Authority Name"].strip(), row["Vendor Name"].strip())
    if tn:
        return base + ("TN", tn)
    return base + ((row.get("Procurement Description") or "").strip(), (row.get("Award Date") or "").strip(),
                   (row.get("Begin Date") or "").strip(), (row.get("Type of Procurement") or "").strip())


def main():
    ddir, out = sys.argv[1], sys.argv[2]
    w = Writer(out)
    stats = collections.Counter()
    for fn, dsid, dsname, btype in DATASETS:
        path = os.path.join(ddir, fn)
        retrieved = file_mtime_iso(path)
        groups = collections.OrderedDict()
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                stats[(dsid, "rows")] += 1
                ok, basis = canadian(row)
                if not ok:
                    continue
                stats[(dsid, "canadian_rows")] += 1
                row["_country_basis"] = basis
                groups.setdefault(key_of(row), []).append(row)
        stats[(dsid, "canadian_contracts")] = len(groups)
        for k, rows in groups.items():
            rows.sort(key=lambda r: parse_date(r["Fiscal Year End Date"]) or "")
            latest = rows[-1]
            last_fy = parse_date(latest["Fiscal Year End Date"])
            st = (latest.get("Status") or "").strip().upper()
            start = parse_date(latest.get("Begin Date")) or parse_date(latest.get("Award Date"))
            end = parse_date(latest.get("End Date"))
            award = parse_date(latest.get("Award Date"))
            if st == "COMPLETED":
                stats[(dsid, "excluded_completed")] += 1
                continue
            if end:
                status, basis = status_from_dates(start, end)
                if not status:
                    stats[(dsid, "excluded_" + ("ended" if "ended" in basis else "future"))] += 1
                    continue
                basis = f"Begin Date/Award Date {start} <= {REF_S} <= End Date {end}" + (f"; Status={st}" if st else "") + f"; last reported FY ending {last_fy}"
            else:
                if start and start > REF_S:
                    stats[(dsid, "excluded_future")] += 1
                    continue
                if not last_fy or last_fy < STALE_FY_CUTOFF:
                    stats[(dsid, "excluded_stale_no_end")] += 1
                    continue
                status = "end_date_unknown"
                basis = (f"no End Date published; " + (f"Status={st}; " if st else "") +
                         f"Award Date {award or 'n/a'}, Begin Date {parse_date(latest.get('Begin Date')) or 'n/a'}; last reported in fiscal year ending {last_fy} (>= {STALE_FY_CUTOFF})")
            # record
            tn = (latest.get("Transaction Number") or "").strip()
            rid_src = "|".join(k)
            import hashlib
            rid = dsid + ":" + hashlib.sha1(rid_src.encode("utf-8")).hexdigest()[:16]
            ids = {"abo_dataset_id": dsid, "transaction_number": tn or None, "authority_name": latest["Authority Name"]}
            amt = parse_amount(latest.get("Contract Amount"))
            vd = {
                "contract_amount": amt,
                "fair_market_value": parse_amount(latest.get("Fair Market Value")),
                "amount_expended_for_fiscal_year_latest": parse_amount(latest.get("Amount Expended for Fiscal Year")),
                "amount_expended_to_date": parse_amount(latest.get("Amount Expended to Date")),
                "current_or_outstanding_balance": parse_amount(latest.get("Current or Outstanding Balance")),
            }
            contract = contract_block(
                identifiers=ids, title=(latest.get("Procurement Description") or None),
                description=(latest.get("Procurement Description") or None),
                instrument_type=(latest.get("Award Process") or None),
                procurement_method=(latest.get("Award Process") or None),
                commodity={"abo_type_of_procurement": latest.get("Type of Procurement") or None},
                value=amt, currency="USD", value_detail={k2: v for k2, v in vd.items() if v is not None},
                dates={"signed": award, "start": parse_date(latest.get("Begin Date")) or award, "end": end,
                       "amended_last": parse_date(latest.get("Renewal Date"))},
                related={"fiscal_years_reported": [parse_date(r["Fiscal Year End Date"]) for r in rows],
                         "status_in_latest_report": st or None,
                         "number_of_bids_or_proposals_received": latest.get("Number of Bids or Proposals Received") or None,
                         "nys_or_foreign_business_enterprise": latest.get("NYS or Foreign Business Enterprise") or None},
            )
            buyer = buyer_block(latest["Authority Name"].strip(), f"NY public authority ({btype})", "US",
                                identifiers={"abo_authority_name": latest["Authority Name"].strip()})
            addr = {"line1": latest.get("Vendor Address 1") or None, "line2": latest.get("Vendor Address 2") or None,
                    "city": latest.get("Vendor City") or None,
                    "region": latest.get("Vendor Province/Region") or latest.get("Vendor State") or None,
                    "postal_code": latest.get("Vendor Postal Code") or None, "country": latest.get("Vendor Country") or None}
            vendor = vendor_block(latest["Vendor Name"].strip(), latest["_country_basis"], identifiers={}, address=addr)
            raw_rows = [{kk: vv for kk, vv in r.items() if not kk.startswith("_")} for r in rows]
            raw = {"dataset_id": dsid, "dataset_name": dsname, "rows": raw_rows}
            rec = record(SOURCE_KEY, "New York State Authorities Budget Office (ABO) procurement reports (data.ny.gov)",
                         "New York State Authorities Budget Office via Open Data NY", f"https://data.ny.gov/d/{dsid}",
                         None, retrieved, rid, status, basis, contract, buyer, vendor, raw)
            w.write(rec)
            stats[(dsid, status)] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

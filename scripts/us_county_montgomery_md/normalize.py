#!/usr/bin/env python3
"""Normalize Montgomery County, MD 'Contracts' (data.montgomerycountymd.gov vmu2-pnrc; all ACTIVE county contracts).
usage: python3 -I normalize.py <csv> <out.jsonl>
"""
import sys, csv, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_county_montgomery_md"
DSID = "vmu2-pnrc"


def main():
    path, out = sys.argv[1], sys.argv[2]
    retrieved = file_mtime_iso(path)
    w = Writer(out)
    stats = collections.Counter()
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            stats["rows"] += 1
            st = (r.get("Vendor State") or "").strip()
            z = (r.get("Vendor Zip Code") or "").strip()
            prov = norm_prov(st)
            if prov:
                basis = f"Vendor State = '{st}' (Canadian province code)"
            elif is_ca_postal(z) and not st:
                basis = f"Canadian-format Vendor Zip Code '{z}' with empty Vendor State"
            else:
                continue
            stats["canadian_rows"] += 1
            start = parse_date(r.get("Execution Date"))
            end = parse_date(r.get("Expiration Date"))
            ext = parse_date(r.get("Extend Date"))
            status, b2 = status_from_dates(start, end or ext)
            if not status:
                stats["excluded_" + ("ended" if "ended" in b2 else "future")] += 1
                continue
            basis = (f"Execution Date {start} <= {REF_S} <= Expiration Date {end}" if end else b2) + "; dataset lists only active County contracts (updated daily)"
            if end and ext and ext > end:
                basis += f"; Extend Date (option limit) {ext}"
            contract = contract_block(
                identifiers={"contract_number": r.get("Contract Number"), "solicitation_number": r.get("SolicitationNumber") or None},
                title=r.get("ContractDesc"), description=r.get("ContractDesc"), instrument_type="county contract",
                procurement_method=r.get("ContractType"), value=None, currency="USD",
                dates={"signed": start, "start": start, "end": end},
                related={"extend_date": ext, "prevailing_wage_contract": r.get("Prevailing Wage Contracts"), "living_wage_contract": r.get("Living Wage Contracts"),
                         "non_profit_vendor": r.get("Non-Profit")},
            )
            buyer = buyer_block(f"Montgomery County, MD - {r.get('DeptName')}" if r.get("DeptName") else "Montgomery County, MD", "county department", "US",
                                identifiers={"department": r.get("DeptName"), "division": r.get("Division") or None},
                                contact={"buyer_name": f"{r.get('Buyer First Name','')} {r.get('Buyer Last Name','')}".strip() or None, "buyer_title": r.get("BuyerTitle") or None,
                                         "buyer_phone": r.get("BuyerPhone") or None, "buyer_email": r.get("BuyerEmail") or None,
                                         "contract_administrator": r.get("Contract Administrator") or None, "contract_administrator_phone": r.get("Contract Administrator Phone") or None,
                                         "contract_administrator_email": r.get("Contract Administrator Email") or None})
            vendor = vendor_block(r.get("Vendor"), basis,
                                  address={"line1": r.get("Vendor Address Line 1") or None, "line2": r.get("Vendor Address Line 2") or None, "city": r.get("Vendor City") or None,
                                           "region": st or None, "postal_code": z or None, "country": None},
                                  contact={"name": r.get("Vendor Contact") or None, "email": r.get("Vendor Email") or None, "phone": r.get("Vendor Phone Number") or None})
            rec = record(SOURCE_KEY, "Montgomery County (Maryland) Contracts - dataMontgomery", "Montgomery County Office of Procurement via dataMontgomery",
                         f"https://data.montgomerycountymd.gov/d/{DSID}", None, retrieved, r.get("Contract Number"), status, basis, contract, buyer, vendor,
                         {"dataset_id": DSID, "row": dict(r)})
            w.write(rec)
            stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

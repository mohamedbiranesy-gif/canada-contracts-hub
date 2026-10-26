#!/usr/bin/env python3
"""Normalize Texas DIR cooperative contracts with a Canadian primary vendor.
Inputs: data.texas.gov vipt-h4ye 'Official - DIR Current Active Cooperative Contracts' (no vendor address) joined on
contract_number with w64c-ndf7 'ARCHIVE DIR Cooperative Contract Sales Data FY2010-FY2025' rows (vendor_address/city/state/zip)
whose vendor_state is a Canadian province. Only contracts present in the ACTIVE list are emitted.
usage: python3 -I normalize.py <active.jsonl> <sales_ca.jsonl> <out.jsonl>
"""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_state_texas_dir"


def main():
    act_p, sales_p, out = sys.argv[1], sys.argv[2], sys.argv[3]
    act = collections.defaultdict(list)
    for line in open(act_p, encoding="utf-8"):
        r = json.loads(line)
        act[r.get("contract_number")].append(r)
    sales = collections.defaultdict(list)
    for line in open(sales_p, encoding="utf-8"):
        r = json.loads(line)
        if norm_prov((r.get("vendor_state") or "").strip()):
            sales[r.get("contract_number")].append(r)
    w = Writer(out)
    stats = collections.Counter()
    stats["active_contracts"] = sum(len(v) for v in act.values())
    stats["canadian_vendor_contract_numbers_in_sales"] = len(sales)
    retrieved = file_mtime_iso(act_p)
    for cn, srows in sales.items():
        if cn not in act:
            stats["excluded_not_in_active_list"] += 1
            continue
        arows = act[cn]
        prim = [a for a in arows if not a.get("reseller_name")] or arows
        a = prim[0]
        # vendor address: sales rows whose vendor_name matches the active primary vendor name (same contract)
        vs = [s for s in srows if (s.get("vendor_name") or "").strip().upper() == (a.get("primary_vendor_name") or "").strip().upper()] or srows
        s = sorted(vs, key=lambda x: x.get("order_date") or "")[-1]
        start = parse_date(a.get("contract_start"))
        end = parse_date(a.get("contract_termination_date"))
        status, basis = status_from_dates(start, end)
        if not status:
            stats["excluded_" + ("ended" if "ended" in basis else "future")] += 1
            continue
        basis = f"active list: contract_start {start} <= {REF_S} <= contract_termination_date {end}"
        contract = contract_block(
            identifiers={"contract_number": cn, "rfo_number": a.get("rfo_number")},
            title=a.get("rfo_description"), description=a.get("rfo_description"), instrument_type="DIR cooperative contract (statewide IT contract)",
            commodity={"dir_contract_type": a.get("contract_type"), "dir_contract_subtype": a.get("contract_subtype")},
            value=None, currency="USD",
            value_detail={"reported_sales_by_canadian_vendor_in_archive": round(sum(parse_amount(x.get("purchase_amount")) or 0 for x in srows), 2)},
            dates={"start": start, "end": end},
            related={"resellers_on_contract": sorted(set(x.get("reseller_name") for x in arows if x.get("reseller_name"))),
                     "contract_end_date_in_sales_archive": parse_date(s.get("contract_end_date")), "contract_termination_date_in_sales_archive": parse_date(s.get("contract_termination_date")),
                     "contract_page": f"https://dir.texas.gov/contracts/{cn.lower()}"},
        )
        buyer = buyer_block("Texas Department of Information Resources (DIR)", "state agency (cooperative contracts program)", "US",
                            contact={"contract_manager": a.get("contract_manager"), "contract_manager_email": a.get("contract_manager_email")})
        vendor = vendor_block(a.get("primary_vendor_name"), f"vendor_state = '{s.get('vendor_state')}' in DIR sales archive (w64c-ndf7) for the same contract_number",
                              address={"line1": s.get("vendor_address"), "city": s.get("vendor_city"), "region": s.get("vendor_state"), "postal_code": s.get("vendor_zip"), "country": None},
                              contact={"name": a.get("vendor_contact"), "email": a.get("vendor_contact_email"), "phone": a.get("vendor_contact_phone_number"), "hub_status": a.get("primary_vendor_hub_status")})
        raw = {"active_rows_vipt-h4ye": arows, "sales_archive_rows_w64c-ndf7": srows}
        rec = record(SOURCE_KEY, "Texas DIR Current Active Cooperative Contracts (data.texas.gov) + DIR sales archive", "Texas Department of Information Resources via Texas Open Data Portal",
                     "https://data.texas.gov/d/vipt-h4ye", f"https://dir.texas.gov/contracts/{cn.lower()}", retrieved, cn, status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

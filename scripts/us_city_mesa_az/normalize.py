#!/usr/bin/env python3
"""Normalize City of Mesa, AZ 'Business Services - Purchases' (citydata.mesaaz.gov u5x3-dvhs) rows with a Canadian
vendor_state -> one record per award document (award_document_code+dept+id); end_date_unknown (no term dates), kept only
if the accounting period is within 12 months before the reference date.
usage: python3 -I normalize.py <jsonl> <out.jsonl>
"""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_city_mesa_az"
DSID = "u5x3-dvhs"
RECENT_CUTOFF = "2025-10-01"  # accounting periods are month starts


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
            st = (r.get("vendor_state") or "").strip()
            if not norm_prov(st):
                continue
            stats["canadian_rows"] += 1
            groups.setdefault(r.get("concatenated_award_document"), []).append(r)
    stats["documents"] = len(groups)
    for doc, rows in groups.items():
        rows.sort(key=lambda x: (x.get("accounting_period_date_format") or "", int(x.get("award_document_version_number") or 0)))
        last = rows[-1]
        period = parse_date(last.get("accounting_period_date_format"))
        if not period or period < RECENT_CUTOFF:
            stats["excluded_older_than_12m"] += 1
            continue
        status = "end_date_unknown"
        basis = f"purchase document without term dates; latest accounting period {period} (FY{last.get('award_header_fiscal_year')} period {last.get('award_header_accounting_period')}) within 12 months before {REF_S}"
        amt = parse_amount(last.get("award_header_actual_amount"))
        contract = contract_block(
            identifiers={"award_document_code": last.get("award_document_code"), "award_department_code": last.get("award_department_code"),
                         "award_document_id": last.get("award_document_id"), "award_document_version_number": last.get("award_document_version_number"),
                         "concatenated_award_document": doc, "cited_authority": last.get("award_header_citied_authority")},
            title=last.get("award_document_name") or last.get("award_document_procurement_1"), description=last.get("award_document_name") or None,
            instrument_type=last.get("award_document_procurement_1"), procurement_method=last.get("award_header_citied_authority"),
            commodity={"reporting_code": last.get("award_header_reporting_code"), "reporting_code_description": last.get("award_header_reporting_code_1")},
            value=amt, currency="USD",
            value_detail={"award_header_actual_amount": amt, "versions": [{"version": x.get("award_document_version_number"), "amount": parse_amount(x.get("award_header_actual_amount")), "period": x.get("accounting_period_date_format")} for x in rows]},
            dates={"published": period},
            related={"purchase_under_25000_flag": last.get("purchase_under_25000_flag"), "purchase_under_100000_flag": last.get("purchase_under_100000_flag")},
        )
        buyer = buyer_block(f"City of Mesa, AZ - {last.get('award_department_name')}", "city department", "US",
                            identifiers={"award_department_code": last.get("award_department_code")})
        vendor = vendor_block(None, f"vendor_state = '{last.get('vendor_state')}' (Canadian province code); dataset publishes vendor city/state but not vendor name",
                              address={"city": last.get("vendor_city"), "region": last.get("vendor_state"), "country": None})
        raw = {"dataset_id": DSID, "rows": rows}
        rec = record(SOURCE_KEY, "City of Mesa Business Services - Purchases (Mesa Open Data)", "City of Mesa, Arizona", f"https://citydata.mesaaz.gov/d/{DSID}",
                     None, retrieved, doc, status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

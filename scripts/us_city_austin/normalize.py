#!/usr/bin/env python3
"""Normalize City of Austin 'Purchase Order Quantity Price detail for Commodity/Goods procurements'
(datahub.austintexas.gov 3ebq-e9iz) rows with ctry = 'CA' -> one record per purchase_order; end_date_unknown (no term
dates), kept if award_date within 12 months before the reference date. (The 'Contracts' dataset 84ih-p28j has no vendor
address; checked for vendor codes seen in CA rows: none matched.)
usage: python3 -I normalize.py <po_detail_ca.jsonl> <out.jsonl>
"""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_city_austin"
DSID = "3ebq-e9iz"
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
        if (r.get("ctry") or "").strip().upper() != "CA":
            continue
        stats["canadian_rows"] += 1
        g.setdefault((r.get("purchase_order"), r.get("vendor_code")), []).append(r)
    stats["pos"] = len(g)
    for (po, vc), rows in g.items():
        last = sorted(rows, key=lambda x: x.get("award_date") or "")[-1]
        award = parse_date(last.get("award_date"))
        if not award or award < RECENT_CUTOFF or award > REF_S:
            stats["excluded_older_than_12m_or_future"] += 1
            continue
        status = "end_date_unknown"
        basis = f"purchase-order line data without term dates; award_date {award} within 12 months before {REF_S}"
        tot = round(sum(parse_amount(x.get("itm_tot_am")) or 0 for x in rows), 2)
        contract = contract_block(
            identifiers={"purchase_order": po, "master_agreement": last.get("master_agreement") or None, "vendor_code": vc},
            title=last.get("contract_name") or last.get("commodity_description"), description="; ".join(sorted(set((x.get("extended_description") or x.get("commodity_description") or "") for x in rows)))[:2000],
            instrument_type="purchase order" + (f" under master agreement {last.get('master_agreement')}" if last.get("master_agreement") else ""),
            commodity={"austin_commodity_code": last.get("commodity"), "commodity_description": last.get("commodity_description"),
                       "all_commodity_codes": sorted(set(x.get("commodity") for x in rows if x.get("commodity")))},
            value=tot, currency="USD", value_detail={"sum_itm_tot_am": tot, "lines": len(rows)},
            dates={"signed": award, "start": award}, related={"data_build_date": last.get("data_build_date")},
        )
        buyer = buyer_block("City of Austin, Texas", "city", "US")
        vendor = vendor_block(last.get("lgl_nm"), "ctry = 'CA' (vendor address country code)", identifiers={"austin_vendor_code": vc},
                              address={"line1": last.get("ad_ln_1"), "line2": last.get("ad_ln_2"), "city": last.get("city"), "region": last.get("st"), "postal_code": last.get("zip"), "country": last.get("ctry")})
        rec = record(SOURCE_KEY, "City of Austin Purchase Order Quantity Price detail (Austin Open Data)", "City of Austin Financial Services - Purchasing Office",
                     f"https://datahub.austintexas.gov/d/{DSID}", None, retrieved, f"{po}:{vc}", status, basis, contract, buyer, vendor, {"dataset_id": DSID, "rows": rows})
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

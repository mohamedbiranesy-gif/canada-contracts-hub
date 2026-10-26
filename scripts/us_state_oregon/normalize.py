#!/usr/bin/env python3
"""Normalize Oregon 'OregonBuys Purchases and Contracts - Multi-Year Report' (data.oregon.gov qyug-f2km)
and 'Historical - ORPIN - Contracts Issued' (6e9e-sfc4) -> Canadian-vendor ongoing contracts.
usage: python3 -I normalize.py <oregonbuys.jsonl> <orpin.csv> <out.jsonl> [lottery.jsonl treasury.jsonl judicial.jsonl]
"""
import sys, json, csv, collections
sys.path.insert(0, "scripts/us_common")
from common import *

csv.field_size_limit(10**9)
SOURCE_KEY = "us_state_oregon"
RECENT_CUTOFF = "2025-01-01"


def main():
    ob_path, orpin_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    w = Writer(out)
    stats = collections.Counter()
    # --- OregonBuys ---
    retrieved = file_mtime_iso(ob_path)
    groups = collections.OrderedDict()
    with open(ob_path, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            stats["ob_rows"] += 1
            if (r.get("vendor_country") or "").strip().upper() != "CAN":
                continue
            stats["ob_canadian_rows"] += 1
            groups.setdefault((r.get("po_nbr"), r.get("vendor_nbr")), []).append(r)
    stats["ob_canadian_pos"] = len(groups)
    for (po, vn), rows in groups.items():
        rows.sort(key=lambda x: (int(x.get("release_nbr") or 0), x.get("sent_date") or ""))
        # prefer the blanket (term-bearing) row as master; releases against it share the po_nbr
        blankets = [x for x in rows if x.get("blanket_end_date")]
        latest = max(blankets, key=lambda x: x.get("blanket_end_date")) if blankets else rows[-1]
        start = parse_date(latest.get("blanket_begin_date"))
        end = parse_date(latest.get("blanket_end_date"))
        sent = parse_date(max(x.get("sent_date") or "" for x in rows)) or parse_date(latest.get("sent_date"))
        ptype = latest.get("po_type")
        if end:
            status, basis = status_from_dates(start or sent, end)
            if not status:
                stats["ob_excluded_ended" if "ended" in basis else "ob_excluded_future"] += 1
                continue
            basis = f"blanket_begin_date {start} <= {REF_S} <= blanket_end_date {end} (po_type {ptype}; {len(rows)} row(s) incl. releases)"
        else:
            # one-off purchase orders (RPA / OPEN MARKET / releases) carry no term; keep only recent ones
            if not sent or sent < RECENT_CUTOFF:
                stats["ob_excluded_stale_no_end"] += 1
                continue
            status = "end_date_unknown"
            basis = f"po_type {ptype} has no blanket begin/end dates; sent_date {sent} >= {RECENT_CUTOFF}"
        tot = parse_amount(latest.get("purchase_order_total_amount"))
        lim = parse_amount(latest.get("blanket_dollar_limit"))
        value = lim if (lim and lim > 0) else tot
        contract = contract_block(
            identifiers={"po_nbr": po, "release_nbr": latest.get("release_nbr"), "record_ids": [x.get("record_id") for x in rows],
                         "org_id": latest.get("org_id"), "vendor_nbr": vn},
            title=latest.get("short_description"), description=latest.get("blanket_description") or latest.get("short_description"),
            instrument_type=ptype, commodity={"oregonbuys_discipline_type": latest.get("discipline_type")},
            value=value, currency="USD",
            value_detail={"purchase_order_total_amount": tot, "blanket_dollar_limit": lim},
            dates={"published": sent, "start": start, "end": end},
            related={"date_retrieved_by_publisher": latest.get("date_retrieved")},
        )
        buyer = buyer_block(latest.get("org_name"), "Oregon state agency", "US", identifiers={"org_id": latest.get("org_id")})
        vendor = vendor_block(latest.get("vendor_name"), "vendor_country = 'CAN'", identifiers={"oregonbuys_vendor_nbr": vn},
                              address={"line1": None, "city": None, "region": None, "postal_code": latest.get("vendor_zipcode"), "country": latest.get("vendor_country")})
        raw = {"dataset_id": "qyug-f2km", "rows": rows}
        rec = record(SOURCE_KEY, "OregonBuys Purchases and Contracts - Multi-Year Report (data.oregon.gov)", "Oregon Department of Administrative Services",
                     "https://data.oregon.gov/d/qyug-f2km", None, retrieved, f"qyug-f2km:{po}:{vn}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats["ob_" + status] += 1
    # --- ORPIN historical ---
    retrieved2 = file_mtime_iso(orpin_path)
    g2 = collections.OrderedDict()
    with open(orpin_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            stats["orpin_rows"] += 1
            st = (row.get("State") or "").strip()
            if norm_prov(st):
                stats["orpin_canadian_rows"] += 1
                row["_basis"] = f"State = '{st}' (Canadian province code)"
                g2.setdefault(row.get("Document #"), []).append(row)
    stats["orpin_canadian_contracts"] = len(g2)
    for doc, rows in g2.items():
        rows.sort(key=lambda x: int(x.get("Amendment #") or 0))
        latest = rows[-1]
        start = parse_date(latest.get("Original Start Date"))
        end = parse_date(latest.get("Expiration Date"))
        if not end:
            stats["orpin_excluded_no_end"] += 1  # historical system (retired 2021): no-end rows are not current
            continue
        status, basis = status_from_dates(start, end)
        if not status:
            stats["orpin_excluded_ended" if "ended" in basis else "orpin_excluded_future"] += 1
            continue
        basis = f"Original Start Date {start} <= {REF_S} <= Expiration Date {end} (amendment {latest.get('Amendment #')})"
        tot = parse_amount(latest.get("Total Award Value"))
        contract = contract_block(
            identifiers={"document_number": doc, "amendment_numbers": [x.get("Amendment #") for x in rows], "agency_number": latest.get("Agency #")},
            title=latest.get("Award Title"), instrument_type=latest.get("Award Type"), value=tot, currency="USD",
            value_detail={"original_award_value": parse_amount(latest.get("Original Award Value")), "total_award_value_w_amendments": tot},
            dates={"start": start, "end": end, "amended_last": parse_date(latest.get("Amendment Date"))},
        )
        buyer = buyer_block(latest.get("Agency Name"), "Oregon state agency", "US", identifiers={"agency_number": latest.get("Agency #")})
        vendor = vendor_block((latest.get("Contractor  ") or latest.get("Contractor") or "").strip(), latest["_basis"],
                              address={"line1": latest.get("Street Address"), "line2": latest.get("Address Line 2"), "city": latest.get("City"),
                                       "region": latest.get("State"), "postal_code": latest.get("Zip Code"), "country": None})
        raw = {"dataset_id": "6e9e-sfc4", "rows": [{k: v for k, v in x.items() if not k.startswith("_")} for x in rows]}
        rec = record(SOURCE_KEY, "Historical - ORPIN - Contracts Issued - Multi-Year Report (data.oregon.gov)", "Oregon Department of Administrative Services",
                     "https://data.oregon.gov/d/6e9e-sfc4", None, retrieved2, f"6e9e-sfc4:{doc}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats["orpin_" + status] += 1
    # --- Oregon Lottery purchase orders (rkhh-35im), Treasury contracts (4iz8-xm93), Judicial Dept contracts (3wxk-gaen) ---
    if len(sys.argv) > 6:
        lot, tre, jud = sys.argv[4], sys.argv[5], sys.argv[6]
        PO_CUTOFF = "2025-10-25"
        # Lottery: line-level POs; group by purchase_order; keep if created within 12 months
        g = collections.OrderedDict()
        for line in open(lot, encoding="utf-8"):
            r = json.loads(line)
            stats["lottery_rows"] += 1
            if not norm_prov((r.get("state") or "").strip()):
                continue
            stats["lottery_canadian_rows"] += 1
            g.setdefault(r.get("purchase_order"), []).append(r)
        stats["lottery_canadian_pos"] = len(g)
        rt = file_mtime_iso(lot)
        for po, rows in g.items():
            rows.sort(key=lambda x: (x.get("created") or "", float(x.get("line_no") or 0)))
            last = rows[-1]
            created = parse_date(last.get("created"))
            if not created or created < PO_CUTOFF:
                stats["lottery_excluded_older_than_12m"] += 1
                continue
            status = "end_date_unknown"
            basis = f"purchase order line items without term dates; latest line created {created} within 12 months before {REF_S}"
            tot = round(sum(parse_amount(x.get("net_amount")) or 0 for x in rows), 2)
            contract = contract_block(
                identifiers={"purchase_order": po, "line_numbers": [x.get("line_no") for x in rows]},
                title=last.get("contract_description"), description="; ".join(sorted(set((x.get("line_item_description") or "").replace("\n", " / ") for x in rows)))[:2000],
                instrument_type="purchase order", value=tot, currency="USD", value_detail={"sum_net_amount": tot, "fiscal_years": sorted(set(x.get("fiscal_year") for x in rows))},
                dates={"published": created, "start": parse_date(rows[0].get("created"))})
            buyer = buyer_block("Oregon State Lottery", "Oregon state agency (lottery)", "US")
            vendor = vendor_block(last.get("vendor"), f"state = '{last.get('state')}' (Canadian province code)",
                                  address={"line1": last.get("address_line"), "city": last.get("city"), "region": last.get("state"), "postal_code": None, "country": None})
            rec = record(SOURCE_KEY, "Lottery Contracts - Multi-Year Report (data.oregon.gov)", "Oregon State Lottery", "https://data.oregon.gov/d/rkhh-35im", None, rt,
                         f"rkhh-35im:{po}", status, basis, contract, buyer, vendor, {"dataset_id": "rkhh-35im", "rows": rows})
            w.write(rec); stats["lottery_" + status] += 1
        # Treasury
        rt = file_mtime_iso(tre)
        for line in open(tre, encoding="utf-8"):
            r = json.loads(line)
            stats["treasury_rows"] += 1
            if not norm_prov((r.get("state_province") or "").strip()):
                continue
            stats["treasury_canadian_rows"] += 1
            start, end = parse_date(r.get("effective_date")), parse_date(r.get("expiration_date"))
            status, basis = status_from_dates(start, end)
            if not status:
                stats["treasury_excluded_ended" if "ended" in basis else "treasury_excluded_future"] += 1
                continue
            basis = f"effective_date {start} <= {REF_S} <= expiration_date {end}" if end else basis
            amt = parse_amount(r.get("contract_nte_amount"))
            contract = contract_block(identifiers={"contract_id": r.get("contract_id")}, title=r.get("award_title"), instrument_type=r.get("contract_classification"),
                                      value=amt, currency="USD", value_detail={"contract_nte_amount": amt}, dates={"start": start, "end": end})
            buyer = buyer_block("Oregon State Treasury", "Oregon state agency", "US")
            vendor = vendor_block(r.get("contractor_name"), f"state_province = '{r.get('state_province')}' (Canadian province)",
                                  address={"line1": r.get("street1"), "city": r.get("city"), "region": r.get("state_province"), "postal_code": r.get("postal_code"), "country": None})
            rec = record(SOURCE_KEY, "Treasury Contracts - Multi-Year Report (data.oregon.gov)", "Oregon State Treasury", "https://data.oregon.gov/d/4iz8-xm93", None, rt,
                         f"4iz8-xm93:{r.get('contract_id')}", status, basis, contract, buyer, vendor, {"dataset_id": "4iz8-xm93", "row": r})
            w.write(rec); stats["treasury_" + status] += 1
        # Judicial
        rt = file_mtime_iso(jud)
        g = collections.OrderedDict()
        for line in open(jud, encoding="utf-8"):
            r = json.loads(line)
            stats["judicial_rows"] += 1
            if not norm_prov((r.get("state") or "").strip()):
                continue
            stats["judicial_canadian_rows"] += 1
            g.setdefault(r.get("award_number"), []).append(r)
        for an, rows in g.items():
            rows.sort(key=lambda x: x.get("fiscal_year") or "")
            last = rows[-1]
            start, end = parse_date(last.get("contract_effective_date")), parse_date(last.get("contract_expiration_date"))
            if end:
                status, basis = status_from_dates(start, end)
                if not status:
                    stats["judicial_excluded_ended" if "ended" in basis else "judicial_excluded_future"] += 1
                    continue
                basis = f"contract_effective_date {start} <= {REF_S} <= contract_expiration_date {end}"
            else:
                if not start or start < "2025-01-01" or start > REF_S:
                    stats["judicial_excluded_stale_or_future"] += 1
                    continue
                status = "end_date_unknown"
                basis = f"no contract_expiration_date published; contract_effective_date {start} (reported FY{last.get('fiscal_year')})"
            amt = parse_amount(last.get("total_contract_value")) or parse_amount(last.get("original_contract_value"))
            contract = contract_block(identifiers={"award_number": an}, title=last.get("award_title"), instrument_type=last.get("award_type"),
                                      value=amt, currency="USD", value_detail={"original_contract_value": parse_amount(last.get("original_contract_value")), "total_contract_value": parse_amount(last.get("total_contract_value")), "total_amendments": last.get("total_amendments")},
                                      dates={"start": start, "end": end}, related={"fiscal_years_reported": [x.get("fiscal_year") for x in rows]})
            buyer = buyer_block("Oregon Judicial Department", "Oregon state judicial branch", "US")
            vendor = vendor_block(last.get("company_name"), f"state = '{last.get('state')}' (Canadian province)",
                                  address={"line1": last.get("company_address"), "city": last.get("city"), "region": last.get("state"), "country": None}, contact={"phone": last.get("company_phone")})
            rec = record(SOURCE_KEY, "Judicial Dept. Contracts - Multi-Year Report (data.oregon.gov)", "Oregon Judicial Department", "https://data.oregon.gov/d/3wxk-gaen", None, rt,
                         f"3wxk-gaen:{an}", status, basis, contract, buyer, vendor, {"dataset_id": "3wxk-gaen", "rows": rows})
            w.write(rec); stats["judicial_" + status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

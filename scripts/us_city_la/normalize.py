#!/usr/bin/env python3
"""Normalize Checkbook L.A. (controllerdata.lacity.org pggv-e4fn) rows with supplier_country = 'CA' -> one record per
purchase order (po_num + vendor_id) that had a payment in the 12 months before the reference date. Payment-level data:
no contract end dates -> end_date_unknown.
usage: python3 -I normalize.py <jsonl> <out.jsonl>
"""
import sys, json, collections
sys.path.insert(0, "scripts/us_common")
from common import *

SOURCE_KEY = "us_city_la"
DSID = "pggv-e4fn"
RECENT_CUTOFF = "2025-10-25"


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
            if (r.get("supplier_country") or "").strip().upper() != "CA":
                continue
            stats["canadian_rows"] += 1
            po = (r.get("po_num") or "").strip()
            if not po:
                stats["rows_without_po"] += 1
                continue
            groups.setdefault((po, r.get("vendor_id")), []).append(r)
    stats["pos"] = len(groups)
    for (po, vid), rows in groups.items():
        rows.sort(key=lambda x: (x.get("transaction_date") or "", x.get("transaction_id") or ""))
        last = rows[-1]
        last_tx = parse_date(last.get("transaction_date"))
        po_date = parse_date(last.get("po_date"))
        if not last_tx or last_tx < RECENT_CUTOFF:
            stats["excluded_no_recent_payment"] += 1
            continue
        status = "end_date_unknown"
        basis = f"payment-level data without contract end dates; latest payment {last_tx} within 12 months before {REF_S}; PO date {po_date or 'n/a'}"
        total = round(sum(parse_amount(x.get("dollar_amount")) or 0 for x in rows), 2)
        descs = sorted(set((x.get("description") or "").strip() for x in rows if x.get("description")))
        contract = contract_block(
            identifiers={"po_num": po, "vendor_id": vid, "transaction_ids": [x.get("transaction_id") for x in rows], "invoice_numbers": sorted(set(x.get("inv_num") for x in rows if x.get("inv_num"))),
                         "authority": last.get("authority"), "btrc": last.get("btrc")},
            title=descs[0] if descs else (last.get("account_name") or None), description="; ".join(descs)[:2000] or None,
            instrument_type=f"purchase order ({'blanket' if po.startswith('BPO') else 'contract' if po.startswith('C') else 'open'})",
            commodity={"item_code": last.get("item_code"), "item_code_name": last.get("item_code_name"), "account_code": last.get("account_code"), "account_name": last.get("account_name")},
            value=total, currency=last.get("currency") or "USD",
            value_detail={"sum_of_payments_all_years": total, "payments_in_dataset": len(rows), "fiscal_years": sorted(set(x.get("fiscal_year") for x in rows))},
            dates={"start": po_date, "amended_last": last_tx},
            related={"first_payment": parse_date(rows[0].get("transaction_date")), "last_payment": last_tx, "procurement_organization": last.get("procurement_organization"),
                     "buyer_name": last.get("buyer_name"), "data_source": last.get("data_source"), "authority_name": last.get("authority_name"),
                     "authority_link": (last.get("authority_link") or {}).get("url") if isinstance(last.get("authority_link"), dict) else last.get("authority_link")},
        )
        buyer = buyer_block(f"City of Los Angeles - {last.get('department_name')}", "city department", "US",
                            identifiers={"department_number": last.get("department_number"), "department_name": last.get("department_name"), "site_location": last.get("site_location")})
        vendor = vendor_block(last.get("vendor_name"), "supplier_country = 'CA' (Checkbook L.A. supplier country code)",
                              identifiers={"la_vendor_id": vid, "vendor_num": last.get("vendor_num")},
                              address={"line1": None, "city": last.get("supplier_city"), "region": None, "postal_code": last.get("zip"), "country": last.get("supplier_country")})
        raw = {"dataset_id": DSID, "rows": rows}
        rec = record(SOURCE_KEY, "Checkbook L.A. Data (Los Angeles City Controller)", "Office of the Los Angeles City Controller",
                     f"https://controllerdata.lacity.org/d/{DSID}", None, retrieved, f"{po}:{vid}", status, basis, contract, buyer, vendor, raw)
        w.write(rec)
        stats[status] += 1
    n, bs = w.close()
    print("written", n, bs)
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()

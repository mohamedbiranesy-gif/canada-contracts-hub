#!/usr/bin/env python3
"""City of Vancouver open data 'Awarded contracts' -> normalized/ca_city_vancouver_unverified_country.jsonl
(no vendor address published; no contract end date published). Usage: python3 -I normalize.py <csv> <download.log> <out_unverified.jsonl> <stats.json>"""
import sys, json, re, collections, datetime
import pandas as pd
src, dlog, outu, stp = sys.argv[1:5]
ret = [l.split()[0] for l in open(dlog) if " ok " in l and "exports/csv" in l][-1]
df = pd.read_csv(src, dtype=str, keep_default_na=False, encoding="utf-8-sig")
st = collections.Counter(); bys = collections.Counter()
by_bid = collections.defaultdict(list)
for r in df.to_dict(orient="records"):
    by_bid[r["bid_number"]].append(r)
fo = open(outu, "w")
for bid, rows in by_bid.items():
    win = [r for r in rows if r["awarded"].strip().lower() == "yes"]
    for i, r in enumerate(win, 1):
        st["awarded_rows"] += 1
        if r["award_date"][:10] < "2015-01-01":
            st["excluded_award_before_2015"] += 1; continue
        if r["award_date"][:10] > "2026-10-25":
            st["excluded_future_award"] += 1; continue
        amt = float(r["bid_amount"]) if r["bid_amount"].strip() else None
        rec = {"record_id": f"ca_city_vancouver:{bid}:{i}",
               "source": {"key": "ca_city_vancouver", "name": "City of Vancouver Open Data - Awarded contracts", "publisher": "City of Vancouver",
                          "dataset_url": "https://opendata.vancouver.ca/explore/dataset/awarded-contracts/", "record_url": None, "retrieved_at": ret},
               "status": "end_date_unknown",
               "status_basis": f"end_date_unknown: dataset publishes Award Date {r['award_date']} and bid amount but no contract term or end date",
               "contract": {"identifiers": {"bid_number": bid, "awarded_vendor_index": i}, "title": r["bid_description"] or None, "description": None,
                            "instrument_type": r["bid_type"] or None, "procurement_method": f"Open public competitive bid ({r['bid_type']})" if r["bid_type"] else None,
                            "solicitation_procedure": r["bid_type"] or None, "commodity": {}, "value": amt, "currency": "CAD" if amt is not None else None,
                            "value_detail": {"bid_amount": amt}, "dates": {"published": None, "signed": r["award_date"][:10] or None, "start": None, "end": None, "amended_last": None},
                            "related": {}},
               "buyer": {"name": "City of Vancouver", "country": "CA", "type": "city",
                         "identifiers": {"note": "Vancouver Group: City of Vancouver, Vancouver Park Board, Vancouver Police Board, Vancouver Public Library"},
                         "address": {"city": "Vancouver", "region": "BC", "country": "CA"}, "contact": {}},
               "vendor": {"name": r["vendor_name"] or None, "country": None, "country_basis": "not published: dataset has vendor name only",
                          "identifiers": {}, "address": {}, "contact": {}},
               "raw": {"row": r, "all_bid_rows": rows}}
        fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); bys["end_date_unknown"] += 1
fo.close()
json.dump({"stats": st, "by_status_unverified": bys}, open(stp, "w"), indent=1); print(dict(st), dict(bys))

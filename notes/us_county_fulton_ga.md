# us_county_fulton_ga — Fulton County, Georgia "Vendor Payments" joined to "Fulton County Vendors" (data.fultoncountyga.gov)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_county_fulton_ga.jsonl` (**7 records**, all `end_date_unknown`). Script: `scripts/us_county_fulton_ga/normalize.py` (`python3 -I normalize.py <vendors_ca.json> <payments_ca.jsonl> <out.jsonl>`).

## What was downloaded (2026-10-25 19:23:49–19:24:03 UTC, SODA)
- `2jx8-2ffx` "Fulton County Vendors" (43,541 rows: vendor_id (hashed), vendor_name, vendor_status, city, **state**, **zip**) → `downloads/us_county_fulton_ga/vendors_all_2jx8-2ffx.json`; Canadian subset (101) → `vendors_ca_2jx8-2ffx.json`.
- `mxhc-krcg` "Vendor Payments" (229,092 rows, disb_date 2022-01-07…2026-10-09; vendor_code, vendor_legal_name, department, object, amount, check_status, payment_document, dis_doc_id, vendor_invoice_no/date, …): per-vendor summary → `payments_vendor_summary.json`; full rows for the 101 Canadian vendor codes → `payments_ca_mxhc-krcg.jsonl` (68 rows). Landing https://data.fultoncountyga.gov/d/mxhc-krcg.

## Canadian vendor
Vendor master address: zip in Canadian postal format, and/or state = province code with a non-US zip (the state field is unreliable, e.g. Domainpeople "Vancouver, Bc" state ON zip V6C 2B5 — the postal code governs). Join payments.vendor_code = vendors.vendor_id (5,373 of 6,105 payment vendor codes match the master).

## Ongoing
Payment-level, no contract terms: one record per (vendor_code, dept) with all payments in `raw.rows` (+ `raw.vendor_master`); kept iff latest disb_date within the 12 months before the reference date: 7 of 25 groups. value = Σ amount (non-cancelled). `record_url` null.

## Result: 7 end_date_unknown (USD 2.13 M)
Bibliocommons Inc. (Toronto; Library, USD 1.04 M), Advanced Utility Systems Corp (Toronto; Finance, utility billing support, USD 885 k), 14 Oranges Software (Richmond BC; IT), Real Time Networks (Port Coquitlam; Sheriff), Tradogram (Ottawa; Superior Court), Krug Inc (Kitchener; Superior Court Clerk), FanFit Gaming (Barrie; Police).

## Samples
- `us_county_fulton_ga:81357d5a48e75900-650` Bibliocommons Inc. (Toronto ON M5W 2C5) — Library — USD 1,042,857 — payments 2022-11-04…2026-09-11
- `us_county_fulton_ga:3cdaf16ad9467d40-210` Advanced Utility Systems Corporation (Toronto M2J 5B5) — Finance — USD 884,746 — last 2026-09-25
- `us_county_fulton_ga:65600b00a3f68391-330` Real Time Networks Inc. (Port Coquitlam BC V3C6G5) — Sheriff's Office — USD 66,931 — last 2026-06-17
- `us_county_fulton_ga:6adee1e7d0419756-450` Tradogram Inc. (Ottawa K2H 9E8) — Superior Court-General — USD 9,360 — last 2026-04-03
- `us_county_fulton_ga:b6197bdf0ec1f0cb-220` 14 Oranges Software Inc (Richmond BC V7C 5A7) — Information Technology — USD 103,262 — last 2026-03-13

## Gaps
Payments only; value is cumulative 2022–2026 payments for the vendor/department pair.

# us_city_mesquite_tx — City of Mesquite, Texas "Check Register for Open Checkbook" + "Vendor" (opendata.cityofmesquite.com)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_mesquite_tx.jsonl` (**6 records**, all `end_date_unknown`). Script: `scripts/us_city_mesquite_tx/normalize.py`.

## What was downloaded (SODA, 2026-10-25T19:47:26Z–19:47:27Z UTC)
- `qnqi-i9bs` "Vendor" (vendor_num, vendor_name, dba, street_1, street_2, city, **state**, zip) filtered `state in (province codes)` → `downloads/us_city_mesquite_tx/vendors_ca_qnqi-i9bs.jsonl` (27 rows).
- `6tva-azs5` "Check Register for Open Checkbook" (fiscal_year/month, check_date, org(+desc), object(+desc), fund, payee, amount, payment_id, check_status, check_number, inv_number, payment_type, vendor_no) filtered on those vendor numbers → `checks_ca_6tva-azs5.jsonl` (48 rows; register current to 2026-10-21).

## Canadian vendor
Vendor state = province code AND zip starting with a Canadian FSA (letter-digit-letter). This excludes "Beton Block Global, Stompetoren, NL 1841HA" (Netherlands). Typos kept as published (e.g. "WINNIPEC", "V6Z 0CB").

## Ongoing
Payments only: one record per (vendor_no, org) with all checks in `raw.rows` (+ `raw.vendor_master`); kept iff latest check_date within 12 months before 2026-10-25: 6 of 15 groups (NewspaperDirect/PressReader last paid 2025-10-21, just outside). `record_url` null.

## Result: 6 end_date_unknown (USD 190,677)
- `us_city_mesquite_tx:10584-407000` Consortech Solutions Inc. (Brossard QC J4Y 0B6) — GIS Operations — software licences — USD 117,500 (last 2026-08-26)
- `us_city_mesquite_tx:13350-150000` F.H. Black & Company (Winnipeg MB R2C4H4) — Finance Administration — professional services — USD 26,000
- `us_city_mesquite_tx:6969-2107060` WhiteWater West Industries (Richmond BC V6W1J7) — 4B Capital PARD — USD 11,497 — 2026-06-10
- `us_city_mesquite_tx:4828-401500` Transoft Solutions (Richmond BC V6V 2L1) — Traffic Engineering — software licences — USD 10,210
- `us_city_mesquite_tx:5931-500000` Tumbleweed Press (Toronto M5M 3Z4) — Library — periodicals/subscriptions — USD 7,830 (last 2026-10-14)
- `us_city_mesquite_tx:10430-2802121` Sparta 2002 Designs & Promotions Inc. — Police Contributions/Donations — USD 17,640

## Gaps
Payments only; no contract terms.

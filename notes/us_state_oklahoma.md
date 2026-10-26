# us_state_oklahoma — State of Oklahoma "Vendor Payments" monthly files (data.ok.gov, OMES)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_oklahoma.jsonl` (**2 records**, both `end_date_unknown`). Script: `scripts/us_state_oklahoma/normalize.py`; puller `scripts/us_common/ckan_ds_pull.py`.

## What was downloaded (CKAN datastore_search_sql, 2026-10-25T19:52:25Z–19:52:33Z UTC)
Packages `state-of-oklahoma-vendor-payments-fiscal-year-2026` (resources Vendors_Public_202507…202606) and `…-fiscal-year-2027` (202607…202609); the 12 monthly resources covering 2025-10 … 2026-09 were queried with `"STATE" IN (province codes)` → `downloads/us_state_oklahoma/vendor_payments_ca_YYYYMM.jsonl`. Monthly datastore totals are only 2,198–9,996 rows (e.g. 2025-12: 8,767). Columns: AGENCYNBR, AGENCYNAME, CALENDAR_YEAR/MONTH, VENDOR_NAME, **CITY, STATE, POSTAL**, EFFDT, VOUCHER_ID, VOUCHER_STYLE, VOUCHER_ID_RELATED, INVOICE_DT, TRANSACTION_TYPE, PYMNT_AMT, PYMNT_DT, CANCEL_DT, FUND, CLASS, DEPT, ACCOUNT, OPERATING_UNIT, PRODUCT, PROGRAM, BUDGET_REF…
Also listed on the portal: "Direct purchase order lines / sole-source / ratification" spend files (vendor name only, no address) — not used.

## Canadian vendor / ongoing
STATE = Canadian province code (with Canadian POSTAL). Only 6 rows in 12 months, all in 2025-11. One record per (AGENCYNBR, VENDOR_NAME); latest EFFDT within 12 months → `end_date_unknown`. **All 6 rows are JRNL vouchers with PYMNT_AMT 0** (accounting entries referencing earlier vouchers in VOUCHER_ID_RELATED), so value = 0; this is said in `status_basis`. `record_url` null.

## Result: 2 end_date_unknown
- `us_state_oklahoma:77300-PROFIT_SYSTEMS_INC` Profit Systems Inc (Saskatoon SK S7N 2X8) — OSU College of Osteopathic Medicine — other services / data-processing software rent — EFFDT 2025-11-25
- `us_state_oklahoma:56600-LIGHTSPEED_COMMERCE_INC` Lightspeed Commerce Inc (Montréal QC H2Y 1A6) — Department of Tourism and Recreation — data-processing software rent — EFFDT 2025-11-06

## Gaps
The public monthly files appear to be a small subset of state disbursements; earlier fiscal years were not pulled (outside the 12-month window).

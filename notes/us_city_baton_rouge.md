# us_city_baton_rouge — City of Baton Rouge / East Baton Rouge Parish "Purchase Orders and Contracts" (data.brla.gov)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_baton_rouge.jsonl` (**10 records**, all `end_date_unknown`). Script: `scripts/us_city_baton_rouge/normalize.py` (`python3 -I normalize.py <po_contracts_2ung-w7t4.csv> <out.jsonl>`). (An earlier pass had rejected this source; on resume it was normalized under the shared 12-month `end_date_unknown` convention used for us_state_virginia / us_city_la / us_state_massachusetts.)

## What was downloaded
- 2026-10-25T17:25:47Z–17:26:12Z UTC: https://data.brla.gov/api/views/2ung-w7t4/rows.csv?accessType=DOWNLOAD → `downloads/us_city_baton_rouge/po_contracts_2ung-w7t4.csv` (131.5 MB, 344,208 rows; landing https://data.brla.gov/d/2ung-w7t4). Columns: RECORD TYPE (H header / D detail line), DOCUMENT NUMBER, SOURCE DOCUMENT TYPE, DOCUMENT DESCRIPTION, REQUISITION NUMBER, INPUT DATE, TOTAL AMOUNT, DEPARTMENT NUMBER/NAME, COST CENTER(+NAME), DOCUMENT TYPE CODE/DESCRIPTION, DOCUMENT STATUS CODE/DESCRIPTION, VOUCHED AMOUNT, START DATE, EXPIRATION DATE, EXTENSION DATE, ANNUAL CONTRACT, VENDOR NAME 1/2, VENDOR CITY, **VENDOR STATE**, **VENDOR ZIP**, vendor certification flags, ITEM NUMBER/DESCRIPTION/QUANTITY/UOM/UNIT COST/TOTAL COST, COMMODITY CODE/DESCRIPTION, EXPENSE TYPE.
- Same time: `syff-bi5d` "Annual Contracts" (71 rows) → `annual_contracts_syff-bi5d.csv`; no Canadian vendors.

## Canadian vendor
`VENDOR STATE` is a Canadian province code (ON 335 rows, QC 9, BC 7) or VENDOR STATE blank and VENDOR ZIP a Canadian postal code (10 rows: EDTEK Services Toronto `m5a 1v5`; Busch Systems, Barrie ONT `L4N 6E5`). Note: `CA` (5,108 rows) is California and is NOT treated as Canada. 136 Canadian-vendor documents in total.

## Ongoing
None of the Canadian-vendor documents carries START/EXPIRATION/EXTENSION dates (one-off POs). One record per DOCUMENT NUMBER with all H/D rows in `raw.rows`; kept as `end_date_unknown` iff the latest INPUT DATE is within 2025-10-25…2026-10-25 and no row is cancelled: 10 kept, 126 older. Value = header TOTAL AMOUNT (falls back to sum of ITEM TOTAL COST); `value_detail` has both plus VOUCHED AMOUNT. No per-record page exists (`record_url` null).

## Result: 10 end_date_unknown (USD 142,370)
ABBA Pump Parts & Service (Burlington ON; sewer pump-station parts for Environmental Services) 7; EDTEK Services (Toronto; HR, USD 32,500); Busch Systems International (Barrie; Library); AG-NAV Inc (Barrie; Mosquito & Rodent Control).

## Samples
- `us_city_baton_rouge:26002433` ABBA Pump Parts & Service (Burlington ON L7L 5N8) — ENV SERV — PS 359 pump parts — USD 20,243 — 2026-04-01
- `us_city_baton_rouge:26003865` ABBA Pump Parts & Service — ENV SERV — PS 26 replacement bare pump FMN0432/3 — USD 33,976 — 2026-06-04
- `us_city_baton_rouge:26006686` ABBA Pump Parts & Service — ENV SERV — USD 19,586 — 2026-10-08
- `us_city_baton_rouge:800007712` EDTEK Services Inc (Toronto m5a 1v5) — H R — USD 32,500 — 2026-04-08
- `us_city_baton_rouge:26005574` Busch Systems International (Barrie ONT L4N 6E5) — LIBRARY — USD 3,917 — 2026-08-20

## Gaps
PO-level only; no contract terms. Vendor address is city/state/zip only (no street).

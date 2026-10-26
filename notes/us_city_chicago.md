# us_city_chicago — City of Chicago Contracts (data.cityofchicago.org rsxa-ify5): checked, pulled in full, 0 ongoing Canadian-vendor contracts

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_chicago.jsonl` (**0 records**). Script: `scripts/us_city_chicago/normalize.py`.

## What was downloaded
- "Contracts" dataset `rsxa-ify5` (landing https://data.cityofchicago.org/d/rsxa-ify5; all City contracts/POs since 1993 with revisions; columns: Purchase Order Description, Purchase Order (Contract) Number, Revision Number, Specification Number, Contract Type, Start Date, End Date, Approval Date, Department, Vendor Name, Vendor ID, Address 1/2, City, **State**, Zip, Award Amount, Procurement Type, Contract PDF). The CSV export was cut off by the server (23 MB, curl error 18), so the data were pulled via SODA JSON paginated 50k (`scripts/us_common/soda_pull.py`, 2026-10-25 17:28:33–17:29:09 UTC) → `downloads/us_city_chicago/contracts_rsxa-ify5.jsonl`, **186,024 rows**.

## Canadian vendor
`State` field values for Canada: `CAN` 33, `BC` 13, `ONTARIO` 7, `ON` 3, `QC` 1, `QC, H2T 1X3` 1 (58 rows → 28 contract/vendor groups; 4,139 rows in the whole dataset have End Date ≥ reference, so the dataset is current). No rows with a Canadian postal code and a blank state.

## Result
Of the 28 Canadian-vendor contracts, 15 have End Dates all before the reference date (latest: Arconas PO 98464, airport seating, ended 2025-12-28; Normal Studio Inc. PO 267323 ended 2024-12-31; Universal Boot/Sabodoin PO 11856 ended 2022-10-31) and 13 have no dates at all and approval dates ≤ 2016 (small EXHIBIT-A/B purchases from BSM Technologies, Intelex, Canada Ticket). None qualifies as ongoing or as a recent `end_date_unknown` award, so the file is empty. The normalizer and raw data are kept so the source can be refreshed.

## Resume check (2026-10-25 ≈19:17 UTC)
The normalizer was re-run on the existing 186,024-row download (`scripts/us_city_chicago/normalize.py downloads/us_city_chicago/contracts_rsxa-ify5.jsonl …`): canadian_rows 58, canadian_contracts 28, excluded_ended 15, excluded_stale_no_end 13 → **0 records**, confirming the result above. `normalized/us_city_chicago.jsonl` stays empty (final).

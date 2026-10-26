# us_city_fort_collins_co — City of Fort Collins (Colorado) OpenBook Detailed Expenses joined to Detailed Vendors (ArcGIS Online), vendor address in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_fort_collins_co.jsonl` (**5 records**, all `end_date_unknown`). Script: `scripts/us_city_fort_collins_co/normalize.py` (`python3 -I normalize.py <vendors_ca.jsonl> <expenses_ca.jsonl> <out.jsonl>`). Found by the W1c ArcGIS Online sweep (owner OpenData_fcgov).

## What was downloaded (ArcGIS REST, `scripts/us_common/arcgis_pull.py`)
- "Fort Collins Detailed OpenBook Vendors" https://services1.arcgis.com/dLpFH5mwVvxSN4OE/arcgis/rest/services/Fort_Collins_Detailed_OpenBook_Vendors/FeatureServer/0 (fields vendor_name, vendor_id, vendor_description, address_1, address_2, city, **state**, zip, country), where `UPPER(state) IN (<province codes>) OR UPPER(country) IN ('CA','CAN','CANADA')`, 2026-10-26T03:51:19Z–03:51:21Z → `downloads/us_city_fort_collins_co/vendors_ca.jsonl` (122 rows, 61 vendor ids; ON 54, BC 39, AB 16, MB 5, NS 4, NF 4).
- "Fort Collins Detailed OpenBook Expenses" (item title "… Expenses DEPR") https://services1.arcgis.com/dLpFH5mwVvxSN4OE/arcgis/rest/services/Fort_Collins_Detailed_OpenBook_Expenses/FeatureServer/0 (801,134 rows to 2026-04-29; fields Fiscal_Year, Fiscal_Period, Date, Service_Area, Department, Expense_Category, Description, Fund, Actual_Amount, Vendor_Name, Vendor_ID, Purchasing_Card_Expense), where `Vendor_ID IN (<61 Canadian vendor ids>)`, 2026-10-26T03:51:34Z–03:51:37Z → `expenses_ca.jsonl` (54 rows).

## Canadian vendor
Vendor master `state` = Canadian province code with a Canadian postal code in `zip` (e.g. CALGARY AB T3H 3C8). The master's `country` column reads `US` for every row (a system default), so it is not used; 3 groups were rejected by the strict test (province code but non-Canadian postal code). Names never used.

## Ongoing
Expense rows only (no contract term): one record per (vendor id, department); `end_date_unknown` iff the latest expense date is within 2025-10-25…2026-10-25 (5 of 18 groups; 13 older). value = Σ Actual_Amount; purchasing-card rows are counted in `value_detail.purchasing_card_rows` (none among the 5). `record_url` null.

## Result: 5 end_date_unknown (USD 135,999)
- `us_city_fort_collins_co:583422:SAFETY_RISK_MANAGEMENT` CLEAR RISK INC (St. John's NL) — Safety & Risk Management — USD 134,467 — last 2026-04-21
- `us_city_fort_collins_co:697594:RECREATION` EPACT NETWORK LTD (North Vancouver BC) — Recreation — USD 1,422 — 2026-01-29
- `us_city_fort_collins_co:577443:EMERGENCY_PREP_SECURITY` EVENT APPROVALS INC (Vancouver BC) — Emergency Prep & Security — USD 70 — 2026-01-28
- `us_city_fort_collins_co:533376:PARKS` NORATEK SOLUTIONS INC (Prince George BC) — Parks — USD 9.61 — 2025-11-18
- `us_city_fort_collins_co:884589:POUDRE_FIRE_AUTHORITY` VODASAFE INC (Vancouver BC) — Poudre Fire Authority (as a department in the City's books) — USD 30.33 — 2025-11-17
(all five records listed; they double as samples)

## Gaps
The expense layer is marked deprecated ("DEPR") and ends 2026-04-29; amounts are allocated expense lines (some very small). Payments only, no contract terms.

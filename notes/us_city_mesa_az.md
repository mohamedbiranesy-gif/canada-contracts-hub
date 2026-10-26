# us_city_mesa_az — City of Mesa (Arizona) Business Services - Purchases, vendor_state = Canadian province

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_mesa_az.jsonl` (**56 records**, all `end_date_unknown`). Script: `scripts/us_city_mesa_az/normalize.py`.

## What was downloaded
- Dataset `u5x3-dvhs` "Business Services - Purchases" on citydata.mesaaz.gov (landing https://citydata.mesaaz.gov/d/u5x3-dvhs → /Business-Services/Business-Services-Purchases/u5x3-dvhs): award documents from the Advantage financial system. Columns: award_document_code (DO/PO/…), concatenated_award_document, award_department_code/name, award_document_id, award_document_version_number, award_document_procurement(_1) (Delivery Order / Decentralized Purchase / Purchase Order / Professional Services), award_header_reporting_code(_1), fiscal year / accounting period / accounting_period_date_format, award_document_name, award_header_citied_authority (cited procurement authority), **vendor_city, vendor_state**, purchase_under_25000_flag, award_header_actual_amount, departmental YTD totals.
- Pulled via SODA `$where=vendor_state in (provinces)` 2026-10-25 18:04:22 UTC → `downloads/us_city_mesa_az/purchases_ca_u5x3-dvhs.jsonl`, 732 rows (FY2017–FY2027). Province values: ON 428, QC 147, AB 81, BC 73, MB 2, NS 1.

## How "Canadian vendor" was determined
Structured `vendor_state` ∈ Canadian province codes, with `vendor_city` (Toronto, Maple, Baie D'Urfé, Calgary, Ottawa, Blainville, Vancouver, Mississauga, Montreal, Thunder Bay). **The dataset does not publish the vendor name** (`vendor.name` = null; basis recorded in `vendor.country_basis`).

## How "ongoing" was determined
Award documents carry no term dates; one record per concatenated award document (versions in `raw.rows`), kept as `end_date_unknown` iff the latest accounting period is ≥ 2025-10-01 (56 of 732; 676 older excluded).

## Record construction
`record_id` = `us_city_mesa_az:<concatenated_award_document>` (e.g. `DO,F400,24011627`). Buyer = "City of Mesa, AZ - <department>". Value = award_header_actual_amount (per-version amounts in value_detail.versions). No per-document URL (`record_url` null).

## Counts
56 end_date_unknown. Departments: Arts and Culture 20 (Toronto vendor; monthly subscription fees + fraud-prevention service — ticketing platform), Innovation and Technology 12 (Maple ON), Water Resources 9 (Baie D'Urfé QC), Economic Development 5 (Calgary), Police 4 (Ottawa, Thunder Bay), Energy Resources 3, Transportation 3. Sum USD 769,556.

## 5 samples
- us_city_mesa_az:DO,F400,26003508 | vendor in Toronto ON (name not published) | Arts and Culture | inv#67622 10/1/25 October subscription fees | USD 12,454.50 | period 2025-10
- us_city_mesa_az:DO,F155,26003546 | Maple ON | Innovation and Technology | Delivery Order | USD 3,162.36 | 2025-10
- us_city_mesa_az:PO,F310,GK260033 | Baie D'Urfé QC | Water Resources | Decentralized Purchase | USD 384.83 | 2025-10
- us_city_mesa_az:PO,F400,26001054 | Toronto ON | Arts and Culture | inv#67743 Fraud prevention Sept 2025 | USD 1,226.40 | 2025-10
- us_city_mesa_az:… | Ottawa ON | Police | Sole Source | 2026

## Known gaps / limits
- Vendor name is withheld by the publisher; only city/state are given. Records identify the buyer, document id, amount and the vendor's Canadian city/province.
- Purchase-level only; no contract terms.

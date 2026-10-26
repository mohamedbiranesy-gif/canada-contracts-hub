# us_state_alaska — Alaska Checkbook Online "Expense Details" (stateofalaska.data.socrata.com)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_alaska.jsonl` (**17 records**, all `end_date_unknown`). Script: `scripts/us_state_alaska/normalize.py`. (Earlier note rejected Alaska because the procurement public-notice site has no structured vendor address; on resume the Checkbook expense data — which has a vendor state field — was used.)

## What was downloaded (2026-10-25T19:20:03Z UTC, SODA)
- `qdjq-crxc` "Expense Details Updated" (65,573 payment rows, transaction_date 2026-07-01…2026-09-30 = FY2027 Q1; columns fy, period, transaction_date, dept, department_name, division, division_name, expense_category, expense_type, description, fund, fund_name, vendor_name, alias_dba, **state**, issue_date, check_number, payment_method, payment_status, transaction, invoice_number, invoice_date, amount, expense, expense_name, expense_description), filter `state in (province codes)` → `downloads/us_state_alaska/expenses_ca_qdjq-crxc.jsonl` (133 rows: NS 79, BC 41, ON …).
- Public-corporation expense sets (`shmc-7nyi` AEA, `k7w4-d9y9` AIDEA, `8hab-zxq2` AHFC, `9kvf-evu3` APFC, `esij-6ma5` AMBBA) queried with the same filter: 0 Canadian rows.
- `46bc-ekd3` "Vendor Dataset" (96,682 vendors with street/city/state/zip) exists but has no key shared with the expense rows (vendor_code vs vendor_name) and was not used.

## Canadian vendor / ongoing
`state` = Canadian province code. Payment-level data, no contract term: one record per (vendor_name, state, dept, division) with all payments in `raw.rows`; all 17 groups have payments within the 12 months before the reference date → `end_date_unknown`. value = Σ amount. `record_url` null.

## Result: 17 end_date_unknown (USD 6.58 M)
Conair Group Inc (BC; air-tanker leases, DNR Forestry, USD 6.01 M), Metocean Telematics (NS; satellite telemetry, Fish & Game, 79 payments), Prime Mover Controls (BC; DOT&PF), Artcraft Display Graphics (BC; Parks), Skretting (BC), Sky Mobile Corp (ON), Thinkific Labs (BC; USD 90,000), Consulab Educatech (QC), Latitude Technologies, Trent University, Deep Trekker, Vancouver Petrographics, Customer Expressions (Legislature), Biodiversity Pathways, Griffin Chapman Environmental, Ferroque Systems (Law), Canada Ticket.

## Samples
- `us_state_alaska:10-4390-Conair_Group_Inc` Conair Group Inc (BC) — DNR Forestry — equipment rentals/leases — USD 6,014,147 — 2026-07-07…
- `us_state_alaska:11-50WC-Metocean_Telematics` Metocean Telematics (NS) — Fish and Game, Wildlife Conservation — wireless charges — USD 24,618
- `us_state_alaska:10-4790-Artcraft_Display_Graphics` Artcraft Display Graphics (BC) — DNR Parks — print/graphics — USD 18,155
- `us_state_alaska:26-0003-Thinkific_Labs_Inc.` Thinkific Labs Inc. (BC) — Family and Community Services — software licensing — USD 90,000
- `us_state_alaska:16-0007-Griffin_Chapman_Environmental_Inc` Griffin Chapman Environmental (ON) — Health — lab supplies — USD 17,397

## Gaps
Only the current quarter is published in this dataset; vendor address = province only. The state procurement notice site (aws.state.ak.us/OnlinePublicNotices) has no structured vendor address.

# us_city_baton_rouge_expenditures — City of Baton Rouge / Parish of East Baton Rouge "City-Parish Expenditures" (data.brla.gov vwa8-ps2a), vendor address in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_baton_rouge_expenditures.jsonl` (**8 records**, all `end_date_unknown`). Script: `scripts/us_city_baton_rouge_expenditures/normalize.py` (`python3 -I normalize.py <expenditures_ca.jsonl> <normalized/us_city_baton_rouge.jsonl> <out.jsonl>`). Complements `us_city_baton_rouge` (POs, dataset 2ung-w7t4, earlier worker), which it de-duplicates against (read-only).

## What was downloaded
SODA `vwa8-ps2a` "City-Parish Expenditures" (department-level spending 2018-01-01 → present; landing https://data.brla.gov/d/vwa8-ps2a), 2026-10-26T03:40:57Z–03:40:59Z, `$where=upper(vendor_state) in (<province codes>,'ONTARIO','QUEBEC','CANADA') OR (upper(vendor_zip) >= 'A' AND upper(vendor_zip) < '[')` → `downloads/us_city_baton_rouge_expenditures/expenditures_ca_vwa8-ps2a.jsonl` (203 rows, 0.29 MB; ON 159, BC 30, PE 7, QC 5, AB 2; check dates 2018-02-06 … 2026-09-22). Columns: year, fund, department(_id), function, division, program, subprogram, journal_entry_period, invoice_status, check_number, check_date, invoice_number/line/date, invoice_line_item_amount/description, source_document_number/type/description (P = purchase order), expense_category, purchasing_department, commodity_code/description, payment_type/status, vendor_name_1/2, vendor_city, **vendor_state**, vendor_zip, vendor_type and certification flags.

## Canadian vendor
`vendor_state` is a Canadian province code with a Canadian postal code in `vendor_zip` (or zip blank: Tumbleweed Press, ON). `CA` (California) is never treated as Canada. Names never used.

## Ongoing
Payment data without contract term: grouped per (vendor, department, source document number or "NODOC"); `end_date_unknown` iff the latest check date is within 2025-10-25…2026-10-25 (12-month convention shared with the other US payment sources). 124 groups older → excluded; 4 groups whose purchase-order number is already a record in `us_city_baton_rouge` (ABBA Pump Parts POs 26002433, 26004943, 26004944, AG-NAV 26004113) → skipped as duplicates. value = Σ invoice_line_item_amount over all rows of the group (first/last payment dates in `contract.related`). `record_url` null.

## Result: 8 end_date_unknown (USD 380,604 of payments in the groups)
Library Board of Control: PressReader Inc (Richmond BC V6V 2J1; USD 146,550, last 2026-07-23), Artefactual Systems (New Westminster BC; USD 112,814), Tumbleweed Press (ON; USD 40,095), iWave Information Systems (Charlottetown PE; USD 30,330), Xello Inc (Toronto; USD 30,135), Jandi Enterprises (Vancouver; USD 12,300); Environmental Services: ABBA Pump Parts & Service (Burlington ON; PO 25006263, USD 4,922); Mosquito & Rodent Control: AG-NAV Inc (Barrie ON; USD 3,458).

## Samples
- `us_city_baton_rouge_expenditures:NODOC:PRESSREADER_INC:1200` PRESSREADER INC (Richmond BC V6V 2J1) — Library Board of Control — USD 146,549.74 — last payment 2026-07-23
- `us_city_baton_rouge_expenditures:NODOC:ARTEFACTUAL_SYSTEMS_INC:1200` ARTEFACTUAL SYSTEMS INC (V3M 1S3) — Library Board of Control — USD 112,814 — 2026-07-23
- `us_city_baton_rouge_expenditures:NODOC:IWAVE_INFORMATION_SYSTEMS_INC:1200` IWAVE INFORMATION SYSTEMS INC (C1A 8R8) — Library — USD 30,330 — 2025-11-20
- `us_city_baton_rouge_expenditures:25006263:ABBA_PUMP_PARTS_SERVICE:7700` ABBA PUMP PARTS & SERVICE (Burlington ON L7L 5N8) — Environmental Services — PO 25006263 — USD 4,922 — 2025-11-20
- `us_city_baton_rouge_expenditures:NODOC:AG-NAV_INC:1100` AG-NAV INC (L4N8ZS) — Mosquito & Rodent Control — USD 3,458 — 2026-08-28

## Gaps
Payments only; vendor address = city/state/zip. Values are cumulative for the group since 2018.

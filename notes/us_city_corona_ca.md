# us_city_corona_ca — City of Corona, California "CorStat - Corona Open Expenditures" (corstat.coronaca.gov)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_corona_ca.jsonl` (**10 records**, all `end_date_unknown`). Script: `scripts/us_city_corona_ca/normalize.py`.

## What was downloaded
SODA `mdmf-aswt` (payments FY2016–FY2027; columns fiscal_year, fiscal_year_period, fund_name, department_code, department, department_activity, vendor_id, vendor, vendor_city, **vendor_st**, vendor_zip, payment_id, payment_date, invoice_id, expense_category, description, amount), filter `vendor_st in (province codes)`, 2026-10-25T19:24:04Z → `downloads/us_city_corona_ca/expenditures_ca_mdmf-aswt.jsonl` (383 rows). Found via a Socrata catalog sweep (`scripts/us_discovery/catalog_sweep.py`, output `downloads/us_discovery/catalog_sweep_resume.txt`).

## Canadian vendor
vendor_st = province code and vendor_zip not a 5-digit US ZIP (several card-merchant rows carry fake 5-digit zips such as Unsplash "00221" and are therefore excluded). Individuals ("SURNAME, GIVEN" payees — refunds/reimbursements) and rows without a department (deposit refunds) are skipped.

## Ongoing
Payment-level: one record per (vendor_id, department_code) with all payments in `raw.rows`; kept iff latest payment_date within the 12 months before 2026-10-25: 10 of 65 groups (52 older, 3 excluded by the rules above). `record_url` null.

## Result: 10 end_date_unknown (USD 29.6 M)
Arantine Hills Holding LP (Toronto; CFD 2018-1 acquisition/bond payments, USD 29.2 M), N. Harris Computer Corp (Ottawa; IT, USD 396,749), Digital Water Solutions (Guelph; hydrant AI lease), Midpoint International (Aurora ON; Utilities), Safe Software (Surrey), Workleap (Montréal), Castr.io, Nova Maps, Epiphan, Action First Aid.

## Samples
- `us_city_corona_ca:146552-23` Arantine Hills Holding LP (Toronto ON M5S2B7) — GENL RESP-NON-CITY DEBT SVC — CFD2018-1 payments — last 2026-04-30
- `us_city_corona_ca:149973-17` N Harris Computer Corporation (Ottawa ON K2E 8C4) — Information Technology — USD 396,749 — last 2026-05-07
- `us_city_corona_ca:150161-17` Digital Water Solutions Inc (Guelph ON N1K1B8) — Information Technology — hydrant AI unit lease / annual DaaS fees — USD 47,428 — last 2025-12-11
- `us_city_corona_ca:PC006881-17` Workleap (Montreal QC) — Information Technology — Officevibe + Pingboard — USD 480 — 2025-12-15
- `us_city_corona_ca:PC007055-17` Nova Maps (Victoria BC) — Information Technology — Nova Pro — USD 1,235 — 2026-03-15

## Gaps
Payments only; many small card purchases; no contract terms.

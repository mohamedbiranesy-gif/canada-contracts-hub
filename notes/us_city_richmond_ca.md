# us_city_richmond_ca — City of Richmond, California "Expenditures" + "Vendors" (transparentrichmond.org)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_richmond_ca.jsonl` (**3 records**, all `end_date_unknown`). Script: `scripts/us_city_richmond_ca/normalize.py`.

## What was downloaded (SODA, 2026-10-25T19:45:19Z–19:45:20Z UTC)
- `5mrn-7gkk` "Vendors" (12,621 rows: vendorid, vendorname, city, **state**, zip, country (empty), phone, webaddress, vendortype, employee), filter `state in (province codes)` → `downloads/us_city_richmond_ca/vendors_ca_5mrn-7gkk.jsonl` (12 vendors).
- `86qj-wgke` "Expenditures" (608,228 GL rows to 2026-10-20: date, fiscalyear/period, entity, fund, organization(+code), object(+code), project, description, actual, invoiceid, invoicestatus, paymentchecknumber, vendorid, vendorname, uniqueid, segment codes…), filter `vendorid in (12 Canadian ids)` → `expenditures_ca_86qj-wgke.jsonl` (39 rows). Landing https://www.transparentrichmond.org/d/86qj-wgke.

## Canadian vendor / ongoing
Vendor master state = Canadian province code (BC 5, ON 5, AB 1, QC 1). One record per (vendorid, organizationcode) with all rows in `raw.rows` (+ `raw.vendor_master`); kept iff latest expenditure date within the 12 months before 2026-10-25: 3 of 15 groups. value = Σ actual excluding Void invoices. `record_url` null.

## Result: 3 end_date_unknown (USD 422,678)
- `us_city_richmond_ca:13164-01191021` InTime Services, Inc. (Vancouver BC V6E 0C5) — Police Admin — SaaS timesheet/inventory — USD 302,581 (2018-06-30 … 2026-07-14)
- `us_city_richmond_ca:17057-01141013` eScribe Software Ltd (Toronto ON M5L1B9) — City Clerk — agenda management — USD 119,597 (… 2026-08-04)
- `us_city_richmond_ca:17579-13564065` Drift Mural Corporation (Ottawa ON K1S 2A2) — Econ Dev / Public Art 1.5% — USD 500 — 2026-08-04
(only three records exist, so these are also the samples). Excluded: Bibliocommons (last 2025-08-06), Active Network, Visible Strategies, Userful, Pioneering Technology (2009–2021).

## Gaps
GL-level expenditure rows, no contract terms.

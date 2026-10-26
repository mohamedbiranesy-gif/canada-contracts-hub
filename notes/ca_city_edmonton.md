# ca_city_edmonton — City of Edmonton open data (SAP outline agreements / hired equipment / POs)

Status: COMPLETE (small). Output only `normalized/ca_city_edmonton_unverified_country.jsonl` (16 records, all `ongoing`).

## Source (data.edmonton.ca, Socrata; datasets last updated 2019-12-18)
Downloaded 2026-10-25T19:26:21Z via `https://data.edmonton.ca/api/views/<id>/rows.csv?accessType=DOWNLOAD`
(+ `<id>_metadata.json`) into `downloads/ca_city_edmonton/`:
- `ydv5-y4pu` Outline Agreements over $10,000 — 5,309 rows (Year 2012–2019, Supplier Name, Description, Purchase Order Type,
  Dollar Value Category, Validity Period End).
- `gnse-cass` Hired Equipment Contracts over $10,000 — 747 rows (Year of Contract, …, Validity Period End); none ends
  on/after 2026-10-25 (SoQL `validity_period_end>='2026-10-25'` count = 0).
- `y9rm-5xha` Purchase Orders over $10,000 — 4,518 rows (Create Date 2012–2019, straight one-off POs, no term) — not emitted.
Script `scripts/ca_city_edmonton/normalize.py`.

## Canadian vendor
No supplier address/country field -> vendor.country null, country_basis "not published".

## Ongoing logic
`Validity Period End` ≥ 2026-10-25 (agreement Year ≤ 2019 is the start anchor) -> `ongoing` (16); 5,293 ended rows excluded.
Amounts only as a value band (`Dollar Value Category`), so contract.value is null.

## record_url
None (no per-row page). record_id = `ca_city_edmonton:<dataset id>:<sha1(row)[:10]>`.

## Samples
- SUREWAY CONSTRUCTION | LAUREL STAGE 22 SERVICING | 2017 -> 2028-12-31
- VIX TECHNOLOGY(USA)INC. | REGIONAL SMART FARE SOLUTION | 2017 -> 2032-06-30
- EPCOR | GRC STAGE 1 - WATER FLUSH SERVICE | 2018 -> 2027-12-31
- ESC AUTOMATION INC | ENERGY MANAGEMENT MONITORING SUPPORT | 2018 -> 2028-03-31
- 812244 ALBERTA LTD | MASTER FIBRE LEASE AGREEMENT | 2017 -> 2026-12-31

## Known gaps
Datasets frozen since 2019; current City of Edmonton awards are on APC (`ca_alberta_apc`, buyer "City of Edmonton").

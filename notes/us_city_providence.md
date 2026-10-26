# us_city_providence — Providence RI "City and School Department Purchase Orders" (data.providenceri.gov)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_city_providence.jsonl` (**6 records**, all `end_date_unknown`). Script: `scripts/us_city_providence/normalize.py`.

## What was downloaded
SODA `425y-pm5m` (240,845 PO lines; columns district (CITY/SCHOOL), po_number, po_line_nbr, po_date, line_description, quantity, unit_price, vendor, vendor_name, address1, address2, city, **state**, **postal_code**, vendor_contct, e_mail_address), filter `state in (province codes) OR upper(state)='CANADA'`, 2026-10-25T19:20:03Z → `downloads/us_city_providence/po_ca_425y-pm5m.jsonl` (90 rows). Landing https://data.providenceri.gov/d/425y-pm5m.

## Canadian vendor
state = province code AND postal_code not a US ZIP (excludes "JULIE LIPSON, Philadelphia, PE 19139"). Values: MB 44 (AmbuTech, Winnipeg), ON 35, QC 4, BC 3, AB 2, NS 1.

## Ongoing
POs only; one record per (district, po_number); kept iff po_date within 12 months before 2026-10-25: 6 of 46 POs. value = Σ quantity × unit_price. `record_url` null (no record page).

## Result: 6 end_date_unknown (USD 90,078)
Gary Jonas Computing Ltd. (dba LilyPad POS, Markham ON) 4 (City of Providence — park/museum POS licences); Hootsuite Inc (Vancouver) 1; Xello Inc (Toronto; Providence Public School Department, 2026-07-01, 10 lines).

## Samples
- `us_city_providence:CITY-588024` Gary Jonas Computing Ltd. (8133 Warden Ave, Markham ON L6G 1B3) — City of Providence — annual software licences — USD 6,273 — 2026-01-23
- `us_city_providence:CITY-587795` Hootsuite Inc (Vancouver BC V5T 4L1) — yearly subscription — USD 1,188 — 2025-12-23
- `us_city_providence:SCHOOL-1042414` Xello Inc (Toronto ON) — Providence Public School Department — 2026-07-01
- `us_city_providence:CITY-587860` Gary Jonas Computing — RWP Museum POS upgrade — USD 815 — 2026-01-07
- `us_city_providence:CITY-587348` Gary Jonas Computing — Botanical Center POS upgrade — USD 2,398 — 2025-11-05

## Gaps
No contract terms; line descriptions truncated at 30 characters by the publisher.

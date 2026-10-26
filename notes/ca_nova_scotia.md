# ca_nova_scotia — Nova Scotia (REJECTED: no supplier location in any accessible source)

Checked 2026-10-25 17:18–17:25 UTC.

1. **Open data "Awarded Public Tenders"** — Socrata `https://data.novascotia.ca/resource/m6ps-8j6u.json` (dataset id `m6ps-8j6u`; 33,670 rows, awarded_date 2010-04-06 … 2026-10-13, metadata via `https://data.novascotia.ca/api/views/m6ps-8j6u.json`). Columns are only: `tender_id, entity, goods, service, construction, tender_start_date, tender_close_date, tender_description, awarded_date, awarded_amount, vendor`. **No vendor address/city/province/country column** and no contract start/end dates (tender_start/close are the posting window). Rejected under the rule "vendor country never from the name". The companion view `rjg2-93i9` is an aggregate chart of the same data. A metadata scan of all 1,278 datasets on data.novascotia.ca (`/api/views/metadata/v1?search=contract`) found no other procurement/award dataset.
2. **Nova Scotia Procurement Portal** (`https://procurement-portal.novascotia.ca/tenders`, React SPA; API base `https://procurement-portal.novascotia.ca/procurementui`). The bundle shows award rows carry `supplier`, `supplierLocation`, `supplierLocationCountry`, `supplierLocationProvince`, `awardAmount`, `awardDate` — i.e. the portal *does* hold supplier country — but every API call (`POST /procurementui/tenders`, `GET /procurementui/tenders?tenderId=…`, `/altps`, `/standingoffers`) returns an F5/ASM-style **"Request Rejected … support ID"** block page (HTTP 200 with WAF body) for non-browser clients. Not bypassed, per the brief. The old `procurement.novascotia.ca/ns-tenders.aspx` URL redirects to this portal.
3. `https://novascotia.ca/tenders/tenders/tender-awards.aspx` also redirects to the portal.

Result: 0 records. Re-check if the portal publishes a CSV/open-data export of award details in future.

## UPDATE 2026-10-25T19:24Z — unverified-country output produced
Per the coordinator's revised rule (records without published vendor location go to a separate file), the
Socrata dataset was normalized after all:
- Downloaded `https://data.novascotia.ca/api/views/m6ps-8j6u/rows.csv?accessType=DOWNLOAD` at 2026-10-25T19:23:07Z
  -> `downloads/ca_nova_scotia/m6ps-8j6u.csv` (6.0 MB, 33,670 rows; awarded_date 2010–2026) + metadata
  `m6ps-8j6u_metadata.json`. Script `scripts/ca_nova_scotia/normalize.py` (shared parser `scripts/_muni/terms.py`).
- Output: `normalized/ca_nova_scotia_unverified_country.jsonl` — vendor.country null, country_basis
  "not published (dataset has no vendor address/country column)". No main `ca_nova_scotia.jsonl` (no location data).
- Status: explicit period / stated term in TENDER_DESCRIPTION anchored on AWARDED_DATE -> ongoing / ongoing_inferred
  (ended -> excluded, 100 rows); otherwise end_date_unknown. Placeholder vendors (N/A, VARIOUS, …) skipped (310).
- Counts: **end_date_unknown 33,259; ongoing_inferred 1**. Most end_date_unknown rows are old awards (2010–2020)
  that have probably ended; filter on contract.dates.awarded downstream.
- record_id `ca_nova_scotia:<TENDER_ID>:<sha1(row)[:10]>`; record_url = Socrata row filter, e.g.
  `https://data.novascotia.ca/resource/m6ps-8j6u.json?tender_id=DAL2023-001` (verified HTTP 200, 2026-10-25).
- Samples: TOA-2025-02-07 | Town of Antigonish | MNP | 233,421 | "5 Year Period" from 2025-03-20 -> ongoing_inferred 2030-03-20;
  DAL2023-001 | Dalhousie University | Avondale Construction Limited | 431,915 | end_date_unknown.

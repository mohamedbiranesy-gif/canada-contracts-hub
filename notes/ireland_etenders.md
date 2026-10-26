# ireland_etenders — Ireland eTenders / OGP open data (SKIPPED: no supplier-country field)

Reference date: 2026-10-25. Worker decision: **no records emitted** (`/home/claude/contracts/normalized/ireland_etenders.jsonl` not created).

## What was checked (2026-10-25, ~12:55 UTC)

| Source | URL | Result |
|---|---|---|
| eTenders portal | https://www.etenders.gov.ie/ → redirects to https://www.etenders.gov.ie/epps/home.do | HTTP 200 but page is an F5 "TSPD" bot-challenge shell (first request returned "Request Rejected … support ID"); `epps/quickSearchAction.do?searchSelect=1&latest=true` returns 0 bytes to a non-browser client. No public awards API or export is advertised on the site. Not attempted further (would require bot-check circumvention, which is out of scope). |
| data.gov.ie CKAN | `https://data.gov.ie/api/3/action/package_search?q=etenders+award` | 6 datasets, all from the Office of Government Procurement (OGP). |
| OGP "Contract Notices Published on eTenders" | https://assets.gov.ie/static/documents/edf2df28/Public_Procurement_Opendata_Dataset.csv (35.8 MB, metadata modified 2026-10-16; saved to `/home/claude/contracts/downloads/ireland_etenders/Public_Procurement_Opendata_Dataset.csv`) | 89,734 rows, 31 columns, notice dates 2013-01-02 → 2026-09-30. 46,217 rows have `Awarded Suppliers`. **Columns are notice-level only**: Tender ID, Contracting Authority, title, CPV, procedure, estimated value, `Sum of Contract Duration (Months)`, `Award Published`, `Sum of Awarded Value (€)`, `Awarded Suppliers` (names, `|`/`;` separated), `TED Notice Link`, `TED CAN Link`. **There is no supplier address or supplier country column**, so the schema's rule ("vendor country per the source's vendor-country/address field — never by name alone") cannot be satisfied from this file. |
| OGP "Contracts for Mini-Competitions and Standalone Awards" (2023, 2024 Q1–Q4) | e.g. https://assets.gov.ie/320030/f49a3061-40a7-40b7-8d79-39c97cc2b768.csv | Columns: contracting authority, client CA, title, Suppliers (names only), award confirmed/start/end dates, CPV. Again **no supplier address/country**. |
| OCP Data Registry | https://data.open-contracting.org/en/search/?q=ireland | Only "Ireland: OpenTender" (Government Transparency Institute aggregation of TED data, Jan 2004 – Dec 2024, refreshed every 6 months) — a TED-derived third-party dataset, not an eTenders export; stale by ~2 years relative to the reference date. |

## Name-only signal (NOT used for records)
Exactly one `Awarded Suppliers` value in the OGP dataset contains the word "Canada": Tender ID 4332606, Teagasc, "3B Scientific Canada Inc", award published 13/12/2024, TED CAN link https://ted.europa.eu/en/notice/-/detail/766822-2024. Supplier location would have to be confirmed from the TED contract award notice (section V.2.3 gives supplier country); that belongs to the TED worker, not to this sub-source.

## Recommendation / gap
Irish above-threshold awards (with supplier country in V.2.3) are published on TED; Irish below-threshold awards on eTenders carry supplier names only in the open exports. If Irish coverage is required, use the TED source for Ireland (buyer country IE, supplier country CA) rather than eTenders.

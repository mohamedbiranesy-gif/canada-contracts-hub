# ca_bc_ministry_awards — "Ministry Contract Awards - Province of British Columbia" (BC Data Catalogue), Canadian vendors

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ca_bc_ministry_awards.jsonl` — **12,871 records, all `end_date_unknown`**.

## What was downloaded
- Dataset page: https://catalogue.data.gov.bc.ca/dataset/ministry-contract-awards-province-of-british-columbia (CKAN id `9bff5da9-fced-4671-8ff3-f6117e5c8266`; metadata saved as `downloads/ca_bc_ministry_awards/package_show.json`). Description: "B.C. government ministries post contract award summaries for each competitive opportunity published on BC Bid … Award summaries are posted after the contract is signed. Contract award summaries include the successful supplier name, location and award total."
- All 29 resources (one file per period, 2012-2018 combined, 2019 annual, then quarterly to Jul–Sep 2026; 25 CSV + 4 XLSX) downloaded 2026-10-25 17:24:27–17:25:05 UTC into `downloads/ca_bc_ministry_awards/` (URL list in `urls.txt`; e.g. `…/resource/1ec7799d-d9fc-499f-b313-41bebf0d81b0/download/ministry-contract-awards-jul-to-sep-2026.csv`). Total 49 MB; three CSVs are padded with ~1.05 M empty rows (Excel export artefact) — 16,038 non-empty data rows in all.
- Script: `scripts/ca_bc_ministry_awards/normalize_bc.py`; stats in `downloads/ca_bc_ministry_awards/normalize_stats.json`.

## Columns (three generations)
1. 2012–2022: `Issued by Organization, Issued for Organization, Title, Tender No, Procurement Method, Issued Date, Amendments, Closing Date, Successful Vendor, Successful Vendor City, Province (/ State), Country, Award Total, Date Awarded`.
2. 2023–2024: `… Opportunity ID … Successful Vendor, Successful Vendor Address, Award Total, Date Awarded` (free-text address, no country column).
3. 2025–2026: adds `Successful Vendor Country` and the address ends with the ISO token `CA` (e.g. "4601 Canada Wy Burnaby British Columbia CA").

## How "Canadian vendor" was determined (`vendor.country_basis`)
- `Country` / `Successful Vendor Country` column == "Canada" (11,417 records);
- else `Province` column is a Canadian province name (59 records; used only when Country was blank);
- else the free-text `Successful Vendor Address` contains a Canadian province name or a province abbreviation adjacent to a Canadian postal code (1,394 records; the regex requires a province token — city alone is never enough).
- Rows with a foreign country/province (262 + 6), with vendor "N/A"/blank (850 — unawarded/cancelled), or with no usable location at all (1,673, mostly 2023-24 rows whose address cell is blank or just a town name) were skipped. The Jan–Mar 2022 file has 146 rows with shifted columns (a date in the Country column); those rows fall into the no-location bucket unless the Province column carries a Canadian province.
- Known caveat: a handful of rows have "Country=Canada" with a US-looking address (data entry by ministry staff); the field value was trusted as the brief requires.

## How "ongoing" was determined
The dataset has no contract start, end, term or duration field in any generation (only Issued Date, Closing Date, Date Awarded). Every record is therefore `end_date_unknown`, with `status_basis` quoting Date Awarded. Rows with Date Awarded after 2026-10-25: none. Awards from 2012-2019 (≈6,700) are very probably finished, but nothing in the source says so; they are kept as the schema requires (consumers can filter on `contract.dates.awarded`).

## Record construction
- `record_id` = `ca_bc_ministry_awards:` + sha1(file|tender no|vendor|awarded|total|title)[:16]; 376 exact duplicate rows (same file, all fields equal) collapsed.
- `record_url` = null (BC Bid opportunity pages require the reCAPTCHA browser check; see `notes/ca_bc_bid.md`). `contract.related.source_file_url` gives the exact CSV/XLSX the row came from; `contract.identifiers.tender_no` / `opportunity_id` is the BC Bid number.
- Buyer = `Issued for Organization` (fallback `Issued by Organization`), e.g. "Ministry of Forests", "Ministry of Transportation and Infrastructure - Construction"; some rows name BC Timber Sales regions or other public-sector entities that posted on BC Bid.
- `raw` holds every column of the row verbatim plus `_source_file`.

## Counts
- Rows 16,038 → emitted 12,871 (by award year: 2012 479, 2013 390, 2014 786, 2015 1,089, 2016 1,042, 2017 858, 2018 988, 2019 1,056, 2020 1,000, 2021 1,024, 2022 1,158, 2023 606, 2024 788, 2025 830, 2026 777). Vendor region: BC 11,409, ON 824, AB 346, QC 101, MB 45, NS 35, SK 21, NB 10, YT 7, NL 3, PE 1, NT 1, unknown 68.
- Status: `end_date_unknown` 12,871; `ongoing` 0; `ongoing_inferred` 0. Total award value CAD 11.46 B (dominated by a few large health/IT contracts).

## 5 samples
- ca_bc_ministry_awards:5bdc968bc3c71771 | Rhino Motorcycles (Cowichan Bay, BC) | Ministry of Forests | Req 63629 - 5 ATVs | CAD 84,000 | awarded 2025-01-28 | ministry-contract-awards-jan-mar-2025.xlsx
- ca_bc_ministry_awards:340cf3d9609b947c | Institute of Health Economics (Victoria, BC) | Ministry of Forests | Life Prevention Schedule Economic Modelling | CAD 120,000 | awarded 2026-04-20 | apr-to-jun-2026.csv
- ca_bc_ministry_awards:5e1b4b606c75406c | Jeratec Forestry Contracting (150 Mile House, BC) | Cariboo-Chilcotin (BC Timber Sales) | SU26TLH008 Silviculture Surveys | CAD 172,182 | awarded 2025-03-19
- ca_bc_ministry_awards:26e70fc81794a44b | TRAFX Research Ltd. (Canmore, AB) | Southern Engineering Group | Vehicle Traffic Counters | CAD 16,700 | awarded 2026-07-21
- ca_bc_ministry_awards:56d8f8fcd8d7805d | TRUTEST MEDICAL INDUSTRIES (London, ON) | Product Distribution Centre | Smith Medical/ICU Products | CAD 645,879 | awarded 2026-09-30 | jul-to-sep-2026.csv

## Known gaps / limits
- Only *ministry* (core government + BC Timber Sales + a few agencies) award summaries; Crown corporations, health authorities and municipalities that post on BC Bid are not in this extract.
- No end dates anywhere → everything flagged `end_date_unknown`.
- 2023–2024 files lost the structured city/province/country columns; ~1,600 rows of that period could not be assigned a country and were dropped.
- Award totals are as published (some "$0.00" for standing arrangements / rate-based contracts).

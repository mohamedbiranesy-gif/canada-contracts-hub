# ca_city_ottawa — City of Ottawa, contracts awarded under delegation of authority (open data)

Status: COMPLETE. Output ONLY `normalized/ca_city_ottawa_unverified_country.jsonl` (5,220 records); no main file,
because the City publishes no vendor address or country.

## Source
- Publisher: City of Ottawa, Open Ottawa (ArcGIS Hub) — semi-annual "Contracts awarded under delegation of authority"
  reports (> $25,000), all departments plus separate Transit Commission tables.
- Downloaded 2026-10-25T17:57:33Z–17:57:39Z (EDT 13:57) from ArcGIS feature services
  `https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/<service>/FeatureServer/0/query?where=1=1&outFields=*&f=json`
  into `downloads/ca_city_ottawa/<service>.json` (9 files, 35–426 KB). Hub items (dataset_url
  `https://open.ottawa.ca/datasets/<item_id>`):
  - 2025 H2 6d5248355ab64d49a3222f512710ebb7; 2025 H1 14cca5b087f74d2d9eadc018c261d1b3;
    2024 H2 31cafa0179134a859d57f1c14f516fe3; 2024 H1 64dfc00c6fab486eb0a45d6fe36efe51;
    2023 H2 bd7380d28f7d4857a5d51cda4e752d61; 2023 H1 d0c227869bb84d6999abb24eadb069c5;
    Transit 2024 H1 ab9cb1e837b342ec917c7bf6351333af; Transit 2023 H2 ef5c0369926a49c48c8330d4627cde28;
    Transit 2022 H2 1063c22c959849008645b0b5c0c0b235.
- Fields: Item, Contract (number), Department, [Service], Description, Professional/Consulting Services designation,
  Contract Approval Request Type (Initial / Amendment / Extension …), Amount, Vendor, Non-Competitive Rationale.
- Script: `scripts/ca_city_ottawa/normalize.py`; stats `downloads/ca_city_ottawa/normalize_stats.json`.

## Canadian vendor
Not determinable: no vendor address/country field. All rows -> unverified file with `vendor.country = null`,
`country_basis = "not published"`. (Many vendors are obviously local but name-based inference is not allowed.)

## Ongoing logic
- The award date is not published; each table covers approvals in a half-year (approval_period_start/end kept in
  `contract.dates`).
- `ongoing_inferred`: Description states a term ("for a period of two years", "three-year contract" …); inferred end
  = approval period start + term ≥ 2026-10-25 (arithmetic in status_basis); rows whose term ended even from the
  period end are excluded (442).
- `end_date_unknown`: no term stated.

## Counts
5,663 rows -> ongoing_inferred 240; end_date_unknown 4,980; excluded ended-by-duration 442; no vendor 1.

## record_url
ArcGIS per-feature query, e.g.
`https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/Contracts_25000_Awarded_DOA_Jul_Dec_2025/FeatureServer/0/query?where=OBJECTID%3D4&outFields=*&f=json`.

## Samples
- ca_city_ottawa:Contracts_25000_Awarded_DOA_Jul_Dec_2025:4 | ongoing_inferred | City of Ottawa - Finance and Corporate Services | GILMORE DOCULINK | 313,423.60 | "for a period of two years"
- ca_city_ottawa:2025_Contracts_Awarded_greater_than_25000_Jan_-_Jun:221 | end_date_unknown | City of Ottawa - Transit Services | SOLUTIONS SERAFIN INC | 27,500
- ca_city_ottawa:Contracts_awarded_for_Q3_Q4_2024:445 | end_date_unknown | City of Ottawa - Infrastructure & Water Services | WESTERN CANADA HEAT EXCHANGER LTD | 41,201
- ca_city_ottawa:Contracts_awarded_under_delegation_of_authority_for_Jan_June_2024_AODA_All_Departments:743 | end_date_unknown | Infrastructure & Water Services | EGIS CANADA LTD | 58,632
- ca_city_ottawa:Ottawa_and_Open_data_Contracts_awarded_under_DA_January_1_2023_to_June_30_2023_AODA:202 | end_date_unknown | Public Works | J W BASTIAN CONTRACTING INC | 2,784,652.82

## Known gaps
- 2022 H1 and earlier, and Transit tables for 2024 H2+ not found as feature services.
- City of Ottawa bid awards also appear in `ca_merx` (City of Ottawa posts on MERX) with vendor addresses.

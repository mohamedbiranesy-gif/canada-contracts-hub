# ca_alberta_sole_source — Alberta "Sole-source service contracts" disclosure, Canadian vendors, ongoing

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ca_alberta_sole_source.jsonl` — **949 records, all `ongoing`** (explicit start and end dates).

## What was downloaded
- Dataset: https://open.alberta.ca/opendata/sole-source-service-contracts ("sole-source contracts of $10,000 or more for services purchased by Alberta government departments … for government business and for direct human services and supports; updated quarterly"). Disclosure table: https://www.alberta.ca/sole-source-contracts-disclosure-table (JS front-end over the same OData service).
- Resource used: the CSV export `https://sole-source.dataservices.alberta.ca/SoleSourceDataService.svc/file.exportcsv` (5.8 MB, 16,579 data rows, 22 columns), retrieved 2026-10-25 18:12:49 UTC (took ~48 s to generate) → `downloads/ca_alberta_sole_source/sole_source_contracts_file.exportcsv.csv`. The OData service (`…/SoleSourceDataService.svc/`; collections `DisplayContracts` (6,210 rows, `$count` saved) and `DisplaySpecialContracts` (10,369 rows); `$metadata` saved) was verified to carry the identical schema but pages 25 rows/request at ~10 s each, so the CSV was used. The CSV's `permittedSituations` column is the OData `exception` field.
- Script: `scripts/ca_alberta_sole_source/normalize_ab_sole_source.py`; stats `downloads/ca_alberta_sole_source/normalize_stats.json`.

## Columns
`department, departmentStreet, departmentStreet2, departmentCity, departmentProvince, departmentPostalCode, departmentCountry, vendor, vendorStreet, vendorStreet2, vendorCity, vendorProvince, vendorPostalCode, vendorCountry, startDate, endDate, contractAmount, contractNumber, contractServices, permittedSituations, fiscalYear, special` — all kept verbatim in `raw`.

## How "Canadian vendor" was determined
`vendorCountry == "Canada"` (values seen: Canada 16,116; United States 325; United Kingdom 25; Australia 15; … 40 other countries). 462 non-Canadian rows skipped. Vendor address (street, city, province code, postal code) copied to `vendor.address`; 27 ongoing rows have placeholder province "XX"/"N/A" (individuals whose address is withheld) but still `vendorCountry = Canada`.

## How "ongoing" was determined
`startDate ≤ 2026-10-25 ≤ endDate` using the two explicit date columns (US-format `m/d/yyyy 12:00:00 AM`, never blank). Excluded: 15,167 ended (endDate < reference), 0 not-yet-started, 1 exact duplicate. `status_basis` quotes both dates. Four records carry obviously mistyped end dates (2424-03-31, 3031-03-31, 3033-03-31, two 2050-01-01); kept and visible in `contract.dates.end`.

## Record construction
- `record_id` = `ca_alberta_sole_source:` + sha1(contractNumber|department|vendor|start|end|amount|fiscalYear|special)[:16].
- `record_url` = null (the disclosure table is a JS grid without per-row URLs; `contract.related.odata_service` names the collection and `contract.identifiers.contract_number` the GoA contract number).
- `contract.related.special_direct_human_services` = true for the "direct human services and supports" table (397 of 949; e.g. PDD / children's services agency contracts), false for "government business" (552).
- `solicitation_procedure` records the permitted-situation exception letter (`d` 588, `g` 154, `b` 142, `j` 26, `z` 21 …) as published; the legend is on the alberta.ca disclosure page (JS-rendered, not captured).

## Counts
- Rows 16,579 → Canadian 16,116 → ongoing 949 (end year: 2026 52, 2027 640, 2028 98, 2029 113, 2030 27, 2031 11, later 8). Total contract amount CAD 2.78 B.
- Top buyers: Assisted Living and Social Services 252, Children and Family Services 176, Education and Childcare 155, Environment and Protected Areas 62, Forestry and Parks 61. Vendor region: AB 818, ON 77, BC 19, QC 5, SK 2, NS 1, placeholder 27.
- Status: `ongoing` 949; `ongoing_inferred` 0; `end_date_unknown` 0.

## 5 samples
- ca_alberta_sole_source:9fca0b5cbf739d6f | EDENBRIDGE FAMILY SERVICES INC. (Lethbridge AB T1J 2V6) | Assisted Living and Social Services | PDD support | CAD 6,344,966.82 | 2026-04-01 → 2027-03-31 | #EE0621-615
- ca_alberta_sole_source:3f9773bcd0ea0eec | Northern Alberta Institute of Technology (Edmonton AB) | Environment and Protected Areas | Wetland Replacement Program | CAD 315,330.40 | 2025-07-30 → 2030-03-31 | #26WCE814
- ca_alberta_sole_source:d0a7fe5ccba6a3f3 | ESRI CANADA LIMITED (Toronto ON M3C 3R8) | Technology and Innovation | Esri Canada Enterprise Agreement Renewal | CAD 5,700,000 | 2026-01-01 → 2027-12-31 | #C7095A
- ca_alberta_sole_source:344bcfc690498c3c | YWCA of Edmonton (Edmonton AB) | Assisted Living and Social Services | PDD support | CAD 7,740,591.24 | 2026-04-01 → 2027-03-31 | #EF0133-326
- ca_alberta_sole_source:f0402da5914f9786 | Receiver General of Canada Eastgate Offices (Edmonton AB) | Environment and Parks | Canada-Alberta Agreement on Hydrometric Monitoring | CAD 3,190,547 | 1975-04-01 → 2050-01-01 | #80088508(a)

## Known gaps / limits
- Sole-source *service* contracts ≥ $10k of GoA departments only (competitive awards are on APC — see `ca_alberta_apc`); goods and construction are out of scope of this disclosure.
- `contractAmount` is the contract value as disclosed (may be an annual amount for multi-year human-services agreements).
- Department names are as of the contract (ministry renamings not harmonised).

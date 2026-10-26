# ca_nwt — Government of the Northwest Territories "Contract Report" (contracts over $5,000), Canadian vendors, ongoing

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ca_nwt.jsonl` — **797 records: 795 `ongoing`, 2 `end_date_unknown`**.

## What was downloaded
- Listing: https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582 (Department of Finance → Resources → category "Contracts Reporting", 38 resources). Each report is a node page (e.g. https://www.fin.gov.nt.ca/node/11994 → `…/sites/fin/files/resources/government_of_northwest_territories_contract_report_apr_1_2026_to_june_30_2026_reporting_period.xlsx`).
- 29 XLSX files downloaded 2026-10-25 17:50–17:53 UTC (`scripts/ca_nwt/fetch_nwt.sh`, log `downloads/ca_nwt/fetch.log`) covering reporting periods FY2015-16 … Apr 1 2026–Jun 30 2026 (quarterly cumulative files: Q1, Q1–Q2, Q1–Q3, full year). PDF-only summaries (infographics) ignored. The Yukon-style "Contract Registry" page (`/en/services/contract-registry`) is only a service description.
- Script: `scripts/ca_nwt/normalize_nwt.py`; stats `downloads/ca_nwt/normalize_stats.json`.

## Columns (standard "Contract Data" sheet, FY2021-22 → present; 24,976 rows across 23 files)
`Contracting Department, SetID, Contract ID Number, Contract Title, Contract Region, Contract BIP Community, Contract BIP Category, Contract Type, Contract Sub-type, Contract Method, Contract Request Format, Competition ID number, Contractor Name, NWT Business Status, Contractor City, Contractor Prov./Terr., Contractor BIP Status, Contract Original Start Date, Expiry Date, Contract Amount / Change Orders / Change Order Amount / Revised Amount (all "for fiscal reporting period")`. Older files (FY2015-16 … FY2020-21) use an unlabeled legacy layout without an "Expiry Date" header and were not parsed (all their contracts started ≥ 5 years ago; any still-running multi-year contract reappears in the later standard-layout reports because every report lists all contracts active in the period).

## How "Canadian vendor" was determined
`Contractor Prov./Terr.` is a Canadian province/territory code (NT, ON, AB, BC, QC, MB, SK, YT, NS, NB, PE, NL, NU); `Contractor City` kept. No country column exists; the province code is the structured location field (no name-based inference). Skipped: 97 contracts whose code is a US state / UK county / other (MA, PA, MN, TX, CA, GT LON, QLD, …).

## How "ongoing" was determined
One record per `Contract ID Number` (7,474 distinct), taking the row from the most recent report (highest node id) as the normalized layer and keeping every row from every report under `raw.rows`. `Contract Original Start Date ≤ 2026-10-25 ≤ Expiry Date` → `ongoing` (795); Expiry blank → `end_date_unknown` (2); Expiry < reference → excluded (6,580). `status_basis` quotes both dates and the report used.

## Record construction
- `record_id` = `ca_nwt:<Contract ID Number>`; `record_url` = null (reports are spreadsheets); `contract.related.reports_containing_contract` lists the reporting periods in which the contract appears.
- Amounts are **per fiscal reporting period** (the GNWT reports spend/commitment within the period, with change orders), not the total contract value; `contract.value` = latest period's Revised Amount, detail fields kept in `value_detail`.
- Buyer = `Contracting Department` (GNWT departments, NWT Health and Social Services Authority, Housing NWT, etc.); `vendor.nwt_business_status` / `contractor_bip_status` (Business Incentive Policy) kept (the status column is an Excel formula in the source; it is resolved from the BIP status).

## Counts
- Standard-layout rows 24,976 → distinct contracts 7,474 → Canadian & ongoing 795 + 2 unknown end (end year: 2026 86, 2027 431, 2028 139, 2029 65, 2030 40, 2031 15, 2032-2037 19).
- Top buyers: Infrastructure 258, NWT Health and Social Services Authority 157, Finance 105, Environment and Climate Change 65, Health and Social Services 44. Vendor region: NT 489, ON 127, AB 81, BC 51, QC 15, MB 11, SK 5, YT 5, others 13.

## 5 samples
- ca_nwt:0000008168 | Beaver Enterprises Limited Partnership (Fort Liard, NT) | Infrastructure | Fort Liard Highway Maintenance | CAD 4,041,842.25 (period) | 2026-05-07 → 2029-03-31 | Comp - Public
- ca_nwt:0000001454 | Quest Software Canada Inc. (Vaughan, ON) | Finance | 5-Year Foglight for SQL Server Performance Investigator | CAD 277,133 | 2025-04-01 → 2030-03-31 | Non-Competitive
- ca_nwt:0000005644 | The Northern Document Company Limited (Yellowknife, NT) | Health and Social Services | Multifunction Photocopier | CAD 21,838.47 | 2022-12-01 → 2026-11-30 | Comp - Public
- ca_nwt:0000058504 | Aklavik Housing Association (Aklavik, NT) | NWT Health and Social Services Authority | Accommodation Staff | CAD 14,640 | 2026-04-01 → 2027-03-31 | Non-Competitive
- ca_nwt:0000010350 | Jean Marie River First Nation (Jean Marie River, NT) | Education, Culture and Employment | Office Lease | CAD 22,560 | 2023-04-01 → 2028-03-31 | Sole Source

## Known gaps / limits
- Legacy-layout files (FY2015-16 to FY2020-21) not parsed (no expiry column header); contracts that started then and are still running appear in later reports anyway only if they had activity in a later period.
- Street address / postal code of contractors are not published (city + province only).
- Reports are cumulative within a fiscal year and overlap; amounts are period amounts.

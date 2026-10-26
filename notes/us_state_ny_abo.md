# us_state_ny_abo — New York State Authorities Budget Office (ABO) procurement reports, vendor in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_ny_abo.jsonl` (**74 records**: 44 `ongoing`, 30 `end_date_unknown`).

## What was downloaded (Open Data NY, Socrata CSV export `https://data.ny.gov/api/views/<id>/rows.csv?accessType=DOWNLOAD`, retrieved 2026-10-25 17:25–17:26 UTC)
| Dataset | id | file | rows |
|---|---|---|---|
| Procurement Report for State Authorities | ehig-g5x3 | `downloads/us_state_ny_abo/state_authorities_ehig-g5x3.csv` (89.5 MB) | 275,763 |
| Procurement Report for Local Authorities | 8w5p-k45m | `local_authorities_8w5p-k45m.csv` (15.8 MB) | 65,467 |
| Procurement Report for Local Development Corporations | d84c-dk28 | `ldc_d84c-dk28.csv` (7.1 MB) | 24,331 |
| Procurement Report for Industrial Development Agencies | p3p6-xqr5 | `ida_p3p6-xqr5.csv` (1.8 MB) | 6,448 |

Landing pages: https://data.ny.gov/d/ehig-g5x3 (→ /Transparency/Procurement-Report-for-State-Authorities/ehig-g5x3), /d/8w5p-k45m, /d/d84c-dk28, /d/p3p6-xqr5. These are the annual PARIS procurement reports public authorities file under Public Authorities Law §2800; one row per procurement per fiscal year (so a multi-year contract appears in several fiscal years). Fiscal years covered: FY ending 2017 … 2024 (latest report year available at retrieval; the 2025 reports were not yet loaded).

Columns (state authorities): Authority Name, Fiscal Year End Date, Procurements, Vendor Name, Vendor Address 1/2, Vendor City, Vendor State, Vendor Postal Code, Vendor Province/Region, **Vendor Country**, Procurement Description, Type of Procurement, Award Process, Award Date, Begin Date, Renewal Date, End Date, Contract Amount, Fair Market Value, FMV Explanation, Amount Expended for Fiscal Year, Amount Expended to Date, Current or Outstanding Balance, Number of Bids or Proposals Received, NYS or Foreign Business Enterprise, Vendor is a MWBE, Solicited MWBE, Number of MWBE Proposals, Exempt From Publishing, Reason for Publishing Exemption, Status, Transaction Number. The local-authority/LDC/IDA files have the same vendor block but fewer contract columns (no Begin Date, Status, Transaction Number, expended-to-date).

## How "Canadian vendor" was determined (script `scripts/us_state_ny_abo/normalize.py`, function `canadian`)
Structured `Vendor Country` field: values seen for Canada = `CAN` (2,534 state-authority rows), `CANADA` (411), `Canada` (362), `CA` (210). `CA` is ambiguous (California), so it is accepted only when `Vendor Province/Region` normalises to a Canadian province (ON/QC/BC/… or full name) or `Vendor Postal Code` matches the Canadian A1A 1A1 pattern; 'CA' rows without either are dropped. Also accepted: `Vendor Country` holding a province name (`Ontario`/`ONTARIO`, 3 rows) and 3 Ogdensburg Bridge & Port Authority rows where the country column holds the second half of a Canadian postal code and Province/Region = Ontario. Names were never used. Counts: state authorities 3,521 Canadian rows → 1,930 distinct contracts; local authorities 297 → 204; LDCs 27 → 25; IDAs 2 → 2.

Grouping: rows with a `Transaction Number` are grouped by (Authority, Vendor, Transaction Number); otherwise by (Authority, Vendor, Procurement Description, Award Date, Begin Date, Type of Procurement). Each record keeps **all fiscal-year rows under `raw.rows`**; the normalized layer uses the latest fiscal-year row.

## How "ongoing" was determined
- Latest-year row with `Status = COMPLETED` → excluded (882 state-authority contracts).
- `End Date` present: `ongoing` iff Begin Date (or Award Date) ≤ 2026-10-25 ≤ End Date (44). End Date < reference → excluded (1,013 across files).
- No End Date: kept as `end_date_unknown` only if the contract was still reported in a fiscal year ending ≥ 2024-01-01 (i.e. appears in the most recent report cycles) and not COMPLETED (30 records); older no-end-date rows are treated as stale (192 excluded, `excluded_stale_no_end`). `status_basis` states the dates and the last fiscal year reported.
- No `ongoing_inferred` cases.

## Record construction
`record_id` = `us_state_ny_abo:<dataset id>:<sha1(group key)[:16]>`. No per-record page exists on data.ny.gov (`record_url` = null; dataset_url points at the dataset). Buyer = Authority Name (type: state authority / local authority / LDC / IDA). Value = `Contract Amount` (latest row); `value_detail` carries FMV, expended-for-FY, expended-to-date, balance. `contract.related.fiscal_years_reported` lists every fiscal year the contract appeared in.

## Counts
By status: ongoing 44 (ehig-g5x3 only; the local/LDC/IDA files have no still-open dated contracts), end_date_unknown 30 (ehig 12, local 12, LDC 6). End years of ongoing: 2026: 4, 2027: 19, 2028: 3, 2029: 3, 2030–2036: 13, 2051: 1 (Roswell Park / Gevity, as reported). Buyers: MTA 31, NYPA 10, NYC Health + Hospitals 10, Roswell Park 4, RGRTA 3, NYCEDC 3, others. Sum of latest Contract Amount: USD 2.50 B (dominated by MTA bus purchases from New Flyer of America, Winnipeg MB).

## 5 samples
- us_state_ny_abo:ehig-g5x3:ba400ed06b413809 | HYPERCARE (ON M5G 1L7) | Erie County Medical Center Corporation | Technology - Software | USD 92,561.03 | 2024-01-17 → 2027-02-28 | ongoing
- us_state_ny_abo (MTA, TN B406562) | NEW FLYER OF AMERICA INC (711 Kernaghan Ave, MB R2C 3TR) | 276 low floor 40-ft Buses | USD 388.7 M | 2014-01-14 → 2031-12-31 | ongoing
- us_state_ny_abo (NYPA) | REEL COH INC (QC J7G 2J2) | NGN 630 TON GANTRY CRANE REPLACEMENT | USD 37.8 M | 2022-07-27 → 2027-07-26 | ongoing
- us_state_ny_abo (Roswell Park) | Inspirata Canada Inc (Ontario M2N 6N5) | E-Path Lite Annual | USD 230,020 | 2021-07-21 → 2027-03-31 | ongoing
- us_state_ny_abo (RGRTA) | New Flyer Industries Ltd. (MB R2C 3T4) | Purchase Order 1 - (2) Hydrogen Buses | USD 2.88 M | 2023-03-01 → (none) | end_date_unknown

## Known gaps / limits
- Reports lag: latest fiscal year loaded is FY2024 (ending 03/31/2024, 06/30/2024, 12/31/2024). Contracts awarded in 2025–2026 are not yet in these files (the MTA's own 2025 data is in `us_ny_mta`).
- Vendor City / Vendor State are almost always blank for foreign vendors; province is in `Vendor Province/Region` (free text: `QC`, `PQ`, `Ontario`, `QU`, street addresses…). Kept verbatim in `vendor.address.region`.
- MTA contracts appear both here (FY2017–2022 rows) and in `us_ny_mta` (FY2018–2025); the two sources overlap for 2018–2022 and record_ids differ. Dedup downstream on (buyer=MTA, Transaction Number).
- `end_date_unknown` rows from "Non Contract Procurement/Purchase Order" award processes are one-off purchases reported for the year; they are kept only when reported in FY2024 (the most recent cycle).

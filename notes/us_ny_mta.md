# us_ny_mta — MTA Procurements: Beginning 2018 (Open Data NY), vendor in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_ny_mta.jsonl` (**52 records**: 45 `ongoing`, 7 `end_date_unknown`).

## What was downloaded
- `https://data.ny.gov/api/views/twsw-2mqa/rows.csv?accessType=DOWNLOAD` → `downloads/us_ny_mta/mta_procurements_twsw-2mqa.csv` (31.2 MB, 107,503 rows), retrieved 2026-10-25 17:25:47–17:26 UTC. Landing: https://data.ny.gov/d/twsw-2mqa (→ /Transportation/MTA-Procurements-Beginning-2018/twsw-2mqa). Fiscal years (12/31) 2018 … 2025, ~12–15k rows each; one row per procurement per fiscal year.
- Columns: Fiscal Year End Date, Vendor Name, Transaction Number, Procurement Description, Status, Type of Procurement, Award Process, Award Date, Begin Date, Renewal Date, End Date, Contract Amount, Amount Expended For Fiscal Year, Amount Expended to Date, Current or Outstanding Balance, Number of Bids or Proposals Received, Vendor is NYS or FBE, Vendor is a MWBE, Solicited MWBE, Number of MWBE Proposals, Exempt from Article 4c, Basis for exemption, Fair Market Value, Fair Market Value Explanation, Address Line 1/2, City, State, Postal Code, Zip Code plus 4, Region, **Country**.

## How "Canadian vendor" was determined (`scripts/us_ny_mta/normalize.py`)
- FY2018–2022 rows: `Country = 'CAN'` (1,644 rows).
- FY2023–2025 rows: the MTA stopped coding countries (only `USA` / `OTHER`). For `Country = 'OTHER'` rows, Canada is accepted when `Region` or `State` is a Canadian province code (QC/ON/MB/BC/AB…) or `Postal Code` matches the Canadian A1A 1A1 pattern (546 rows). `vendor.country_basis` records which rule fired. Names never used. Total 2,190 Canadian rows → 1,642 contract groups (grouped by Transaction Number + vendor; rows whose Transaction Number was mangled to scientific notation like `6E+14` are grouped by vendor + description + award date + begin date instead).

## How "ongoing" was determined
Latest fiscal-year row per group. `Status = Completed` → excluded (477). End Date present → `ongoing` iff Begin Date ≤ 2026-10-25 ≤ End Date (45); End Date < reference → excluded (1,091). No End Date → `end_date_unknown` only if still reported in FY2024+ and Status Open (7, all "Multiple PO" blanket rows like `BACH-SIMPSON A DIV OF WABTEC CANADA — Various items`); 22 stale excluded.

## Record construction
`record_id` = `us_ny_mta:<sha1(group key)[:16]>`; all fiscal-year rows in `raw.rows`; normalized values from latest row; `contract.related.fiscal_years_reported`. No per-record URL (`record_url` null). Buyer = Metropolitan Transportation Authority (type NY state public authority (transit)).

## Counts
ongoing 45, end_date_unknown 7. End years: 2026: 11, 2027: 16, 2028: 5, 2029: 2, 2030–2038: 11. Sum of latest Contract Amount USD 2.74 B (New Flyer of America bus contracts: 205 BEBs USD 680 M, 110 hybrid buses USD 594 M, 276 buses USD 389 M …). Vendors: New Flyer of America (Winnipeg MB), Vapor Stone Rail Systems (Ville St-Laurent QC), GIRO Inc (Montreal), Sherwood Electromotion (Concord ON), RideCo US Inc (Waterloo ON, paratransit tech, USD 72 M to 2035), Cority Software (Toronto), ARVA Industries, CAD Railway Industries, Roctest, EHC Canada, TDG Transit Design Group, Enertec Rail, Mark David Canada, EPP Track Equipment.

## 5 samples
- us_ny_mta:8985a02868ad442f | NEW FLYER OF AMERICA INC (Winnipeg MB R2C 3T4) | 276 low floor 40-ft Buses (B406562) | USD 388,670,407 | 2014-01-14 → 2031-12-31 | ongoing (8 FY rows)
- us_ny_mta (B40706) | NEW FLYER OF AMERICA INC | Furnish and Deliver 205 BEBs | USD 679,914,717 | 2024-02-14 → 2036-12-31 | ongoing
- us_ny_mta (R34257) | CAD RAILWAY INDUSTRIES LTD (Lachine QC H8S 1B4) | Conversion and Upgrade of R77E | USD 27,957,413 | 2020-09-30 → 2030-09-30 | ongoing
- us_ny_mta | RIDECO US INC (Waterloo ON N2L 6C2) | PARATRANSIT TECHNOLOGY SOLUTION | USD 71,951,069 | 2025-08-18 → 2035-08-17 | ongoing (FY2025 row, Country=OTHER, Region=ON)
- us_ny_mta | AIRPLUS INDUSTRIAL CORP (Langley BC V4W 1S3) | Various Items, Multiple PO - NYCTA | (no amount) | end_date_unknown

## Known gaps / limits
- Country coding stops after FY2022; detection for FY2023–2025 relies on province code / postal code in the address block (documented per record).
- Transaction Numbers for many 2023–2025 rows are corrupted in the source (`4.00E+14`, `6E+14`) — stored verbatim; grouping falls back to vendor+description+dates, so a renewal with the same description could be merged with its predecessor (checked: the normalized `dates`/`value` come from the latest row, and all rows remain in `raw.rows`).
- Overlaps with `us_state_ny_abo` (MTA FY2017–2022 rows filed with the ABO).

# us_state_oregon — Oregon (data.oregon.gov) contracts/purchase datasets with vendor state/country, vendor in Canada

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_state_oregon.jsonl` (**74 records**: 12 `ongoing`, 62 `end_date_unknown`). Script: `scripts/us_state_oregon/normalize.py`.

## What was downloaded (all Socrata, retrieved 2026-10-25)
| Dataset | id | pull | rows (Canadian) |
|---|---|---|---|
| OregonBuys Purchases and Contracts - Multi-Year Report | qyug-f2km | SODA JSON, paginated 50k (`scripts/us_common/soda_pull.py`) 17:28 UTC → `downloads/us_state_oregon/oregonbuys_qyug-f2km.jsonl` | 109,119 rows; `vendor_country = CAN` 207 rows → 152 PO/vendor groups |
| Historical - ORPIN - Contracts Issued - Multi-Year Report | 6e9e-sfc4 | CSV export 17:26 UTC → `orpin_issued_6e9e-sfc4.csv` (24.5 MB) | 93,846 rows; `State` ∈ Canadian province codes 242 rows → 82 documents |
| Lottery Contracts - Multi-Year Report | rkhh-35im | SODA JSON filtered `state in (provinces)` 18:04 UTC → `lottery_contracts_ca_rkhh-35im.jsonl` | 1,329 line rows → 645 purchase orders |
| Treasury Contracts - Multi-Year Report | 4iz8-xm93 | SODA filtered `state_province in (...)` → `treasury_contracts_ca_4iz8-xm93.jsonl` | 35 |
| Judicial Dept. Contracts - Multi-Year Report | 3wxk-gaen | SODA filtered `state in (...)` → `judicial_contracts_ca_3wxk-gaen.jsonl` | 5 |
Landing pages: https://data.oregon.gov/d/qyug-f2km (→ /Revenue-Expense/OregonBuys-Purchases-and-Contracts-Multi-Year-Repo/qyug-f2km), /d/6e9e-sfc4, /d/rkhh-35im, /d/4iz8-xm93, /d/3wxk-gaen. Also checked and not used: ODOT Highway Contracts fdus-r2ei (no Canadian state values), Historical ORPIN Contracts Expired 8izy-bwhd (expired by definition), Statewide Price Agreement Spend gart-52me (no vendor address).

OregonBuys columns: record_id, date_retrieved, sent_date, po_nbr, release_nbr, po_type (MASTER BLANKET / STANDARD RELEASE / DIRECT RELEASE / RPA / OPEN MARKET / DIRECT OPEN MARKET), blanket_begin_date, blanket_end_date, org_id, org_name, discipline_type, short_description, blanket_description, purchase_order_total_amount, blanket_dollar_limit, vendor_nbr, vendor_name, vendor_zipcode, **vendor_country**. ORPIN columns: Agency #, Agency Name, Document #, Amendment #, Award Title, Award Type, Contractor, Street Address, Address Line 2, City, **State**, Zip Code, Original Start Date, Amendment Date, Expiration Date, Original/Amendment/Total Award Value.

## How "Canadian vendor" was determined
- OregonBuys: structured `vendor_country = 'CAN'` (values seen: US 108,405; blank 481; CAN 207; GBR 17 …). vendor_zipcode is a Canadian postal code in all CAN rows; no row with a Canadian postal code had another country.
- ORPIN / Lottery / Judicial: `State` field is a Canadian province code (BC 102, ON 96, NS 21, QC 13, AB 6, MB 4 in ORPIN; NB 1,050 (IGT Canada, Moncton), MB, ON, AB, BC, QC in Lottery). Treasury: `state_province` (ON/Ontario/Alberta/BC).
- Names never used; basis stored per record in `vendor.country_basis`.

## How "ongoing" was determined
- OregonBuys: grouped by (po_nbr, vendor_nbr); the MASTER BLANKET row (with blanket_begin/end dates) is the master and its releases are kept in `raw.rows`. `ongoing` iff blanket_begin_date ≤ 2026-10-25 ≤ blanket_end_date (12 — e.g. GoFleet telematics for ODOT to 2030-12-18 with USD 10 M limit; Niche Technology RMS for Oregon State Police to 2032-04-28; RLDatix for OHA to 2028). Ended blankets excluded (10). One-off orders (RPA/OPEN MARKET/releases) have no term: kept as `end_date_unknown` only if sent_date ≥ 2025-01-01 (17); older excluded (111).
- ORPIN: all 82 Canadian documents expired before the reference date (ORPIN was retired in 2021) → 0 records.
- Lottery: line-level POs with no dates other than `created`; kept as `end_date_unknown` if the latest line was created within 12 months before the reference date (44 POs, mostly IGT Canada Solutions ULC VLT spare parts and Carmanah Signs); 601 older excluded.
- Treasury: all 35 contracts (ICPM dues, Rosenberg Research, Hootsuite…) expired ≤ 2026-01-10 → 0.
- Judicial: 1 kept (`B3794` Archon Systems Inc., effective 2025-05-23, no expiration published → end_date_unknown); 2 expired, 1 stale.

## Record construction
`record_id` = `us_state_oregon:<dataset id>:<po_nbr>:<vendor_nbr>` (OregonBuys), `:<Document #>` (ORPIN), `:<purchase_order>` (Lottery), `:<contract_id>` (Treasury), `:<award_number>` (Judicial). No per-record page on data.oregon.gov; the OregonBuys public portal (oregonbuys.gov/bso) requires a JS session for blanket lookups, so `record_url` = null. Value = blanket_dollar_limit if > 0 else purchase_order_total_amount (both in value_detail).

## Counts
ongoing 12 (all OregonBuys master blankets; end years 2026: 1, 2027: 5, 2028: 2, 2029: 1, 2030: 1, 2031: 1, 2032: 1); end_date_unknown 62 (OregonBuys 17, Lottery 44, Judicial 1). Buyers: Oregon State Lottery 44, Dept of Forestry 12, ODOT 5, OHCS 4, OHA 3, OSP 2 … Sum of value fields USD 46.7 M.

## 5 samples
- us_state_oregon:qyug-f2km:730-B37903-21:V00005197 | GOFLEET CORPORATION (L4W 5B2) | ODOT | AUTOMATIC VEHICLE LOCATION/TELEMATICS SYSTEM | limit USD 10,000,000 | 2020-12-18 → 2030-12-18 | ongoing (16 rows incl. releases)
- us_state_oregon:qyug-f2km:PO-DASOBO-00006779:V00004661 | NICHE TECHNOLOGY INC. (R3A 1P6) | Oregon State Police | NICHE OSP RECORDS MANAGEMENT | USD 3,515,960 | 2012-01-01 → 2032-04-28 | ongoing
- us_state_oregon:qyug-f2km:730-B32105-14:… | INTERTALK CRITICAL INFORMATION SYSTEMS (B3B 0J5) | ODOT | limit USD 8,854,505 | 2014-05-02 → 2029-05-02 | ongoing
- us_state_oregon:qyug-f2km:PO-73000-00040465:… | DRIVEWYZE LTD. (T6H 4J9) | ODOT | 2021-09-10 → 2031-09-09 | ongoing
- us_state_oregon:rkhh-35im:<po> | IGT CANADA SOLUTIONS ULC (Moncton NB E1H 2R6) | Oregon State Lottery | Inventory Replenishment - VLT Spare Parts | created 2026-06 | end_date_unknown

## Known gaps / limits
- OregonBuys extract is dated 2025-11-14 (`date_retrieved`), so blankets started after that date are missing; vendor address is postal code + country only.
- OregonBuys `blanket_dollar_limit` / `purchase_order_total_amount` are often 0.00 for services blankets (value reported as 0).
- Lottery/Judicial records have no end dates by design.

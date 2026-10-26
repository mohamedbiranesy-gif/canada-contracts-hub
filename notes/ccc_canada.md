# ccc_canada — Canadian Commercial Corporation (CCC) government-to-government transactions

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/ccc_canada.jsonl` (663 records). Script: `/home/claude/contracts/scripts/ccc_canada/normalize_ccc.py`. Downloads: `/home/claude/contracts/downloads/ccc_canada/`.

## What CCC publishes
CCC (Crown corporation) is the Government of Canada's government-to-government contracting agency: a foreign government buys from CCC, which signs a back-to-back contract with the Canadian exporter. CCC does **not** report under the federal proactive-disclosure contracts dataset (checked: `owner_org` list of open.canada.ca `contracts.csv`, 99 organizations, no `ccc`; open.canada.ca organization `ccc` has 0 datasets). Its only transaction-level publication is the quarterly **"Disclosure Report of Signed Transactions"** (PDF, bilingual, marked Protected B) linked from https://www.ccc.ca/en/about/corporate-reports/ ("Quarterly transactional reports"). Columns: **Exporter** (Canadian exporter; sometimes anonymised as "Canadian Exporter"), **Destination** (country of the buyer / delivery), **Description** (sector), **Amount of the transaction (CAD)** as a band (<$100k … >$500M). No buyer name, no contract number, no signing date beyond the quarter, no duration.

## What was downloaded / transcribed (2026-10-25, 13:50–14:05 UTC)
www.ccc.ca sits behind Cloudflare bot protection (HTTP 403 for scripted clients), so the 20 PDFs were read through the web-fetch tool and their tables transcribed row by row into `downloads/ccc_canada/transactions_transcribed.psv` (663 rows; header `report_url|period_start|period_end|row|exporter|destination|description_en|amount_range_cad`; French halves of bilingual cells dropped, English kept verbatim incl. source typos such as "Maagement"). Reports covered (all that are listed on the page):

| Fiscal quarter | Period | Rows | PDF |
|---|---|---|---|
| FY2026-27 Q1 | 2026-04-01 → 2026-06-30 | 37 | https://www.ccc.ca/wp-content/uploads/2026/07/TD-2026-2027-Q1.pdf |
| FY2025-26 Q4 | 2026-01-01 → 2026-03-31 | 55 | https://www.ccc.ca/wp-content/uploads/2026/06/TD-2025-2026-Q4.pdf |
| FY2025-26 Q3 | 2025-10-01 → 2025-12-31 | 53 | https://www.ccc.ca/wp-content/uploads/2026/02/TD-2025-2026-Q3.pdf |
| FY2025-26 Q2 | 2025-07-01 → 2025-09-30 | 38 | https://www.ccc.ca/wp-content/uploads/2025/11/TD-2025-2026-Q2.pdf |
| FY2025-26 Q1 | 2025-04-01 → 2025-06-30 | 49 | https://www.ccc.ca/wp-content/uploads/2025/07/TD-2025-2026-Q1.pdf |
| FY2024-25 Q4 | 2025-01-01 → 2025-03-31 | 42 | https://www.ccc.ca/wp-content/uploads/2025/05/TD-2024-2025-Q4.pdf |
| FY2024-25 Q3 | 2024-10-01 → 2024-12-31 | 43 | https://www.ccc.ca/wp-content/uploads/2025/02/TD-2024-2025-Q3.pdf |
| FY2024-25 Q2 | 2024-07-01 → 2024-09-30 | 54 | https://www.ccc.ca/wp-content/uploads/2024/11/TD-2024-2025-Q2.pdf |
| FY2024-25 Q1 | 2024-04-01 → 2024-06-30 | 44 | https://www.ccc.ca/wp-content/uploads/2024/08/TD-2024-2025-Q1-FINAL.pdf |
| FY2023-24 Q4 | 2024-01-01 → 2024-03-31 | 32 | https://www.ccc.ca/wp-content/uploads/2024/05/TD-2023-2024-Q4-FINAL.pdf |
| FY2023-24 Q3 | 2023-10-01 → 2023-12-31 | 42 | https://www.ccc.ca/wp-content/uploads/2024/02/TD-2023-2024-Q3-FINAL.pdf |
| FY2023-24 Q2 | 2023-07-01 → 2023-09-30 | 20 | https://www.ccc.ca/wp-content/uploads/2023/11/TD-2023-2024-Q2-FINAL-1.pdf |
| FY2023-24 Q1 | 2023-04-01 → 2023-06-30 | 21 | https://www.ccc.ca/wp-content/uploads/2023/08/TD-2023-2024-Q1-FINAL-.pdf |
| FY2022-23 Q4 | 2023-01-01 → 2023-03-31 | 30 | https://www.ccc.ca/wp-content/uploads/2023/06/TD-2022-2023-Q4-FINAL2.pdf |
| FY2022-23 Q3 | 2022-10-01 → 2022-12-31 | 33 | https://www.ccc.ca/wp-content/uploads/2023/03/TD-Q3-V2.pdf |
| FY2022-23 Q2 | 2022-07-01 → 2022-09-30 | 16 | https://www.ccc.ca/wp-content/uploads/2022/11/Q2-2022-2023.pdf |
| FY2022-23 Q1 | 2022-04-01 → 2022-06-30 | 21 | https://www.ccc.ca/wp-content/uploads/pdfs/Disclosure-Report-of-Signed-Transactrion-Q1-FY-22-23-protected.pdf |
| FY2021-22 Q4 | 2022-01-01 → 2022-03-31 | 22 | https://www.ccc.ca/wp-content/uploads/pdfs/Disclosure-Report-of-Signed-Transactions-Q4-2022.pdf |
| FY2021-22 Q3 | 2021-10-01 → 2021-12-31 | 7 | https://www.ccc.ca/wp-content/uploads/pdfs/Canadian-Commercial-Corporation-Disclosure-Report-of-Signed-Transactions-Q3.pdf |
| FY2021-22 Q2 | 2021-07-01 → 2021-09-30 | 4 | https://www.ccc.ca/wp-content/uploads/pdfs/Canadian-Commercial-Corporation-Disclosure-Report-of-Signed-Transactions-Q2.pdf |

The original PDFs could not be stored locally (403); `raw` holds the transcribed row and `source.record_url` points at the PDF. Row numbering follows the order in each PDF.

## How "Canadian vendor" was determined
By construction: CCC only contracts with Canadian exporters, and the report column is "Exporter / Exportateur canadien". 123 rows are anonymised ("Canadian Exporter") → `vendor.name = null`, `vendor.anonymised = true`, `vendor.name_as_published` kept. Note three rows name foreign entities as "exporter" (International Civil Aviation Organization, New Zealand Defence Force, Air Filter Maintenance Services International (PTY) Ltd, Global Clearance Solutions AG) — kept as published; the user may wish to review them.

## Buyer
The buyer government is never named; `buyer.name` is derived from the Destination ("Government of <country> … identity not disclosed"), `buyer.country` = ISO2 of the destination. Destination **United States** (388 rows) = U.S. DoD/federal agencies under the Canada–US Defence Production Sharing Agreement; **Canada** (149 rows) = CCC records the destination as Canada when goods are delivered in Canada or the client is a Government of Canada department (e.g. GAC aid procurement, DND) — buyer country left null; **Caribbean** (25) = regional tourism programme, country null; **Ukraine** (48) = Government of Ukraine military-aid procurements executed by CCC for Canada.

## How "ongoing" was determined
Not determinable: the reports give only the signing quarter and an amount band. All 663 records are `end_date_unknown` (`status_basis` states the signing window). No records excluded.

## Counts
| status | records |
|---|---|
| end_date_unknown | 663 |
| ongoing / ongoing_inferred | 0 |

By destination: US 388, Canada 149, Ukraine 48, Caribbean 25, Chile 9, Germany 5, Portugal 5, Bangladesh 5, Malaysia 5, Montenegro 3, Romania 2, Netherlands 2, Dominican Republic 2, Argentina 2, 13 others × 1.

## record_url
`source.record_url` = the quarterly PDF; `contract.identifiers.report_row` locates the row. Verified: https://www.ccc.ca/wp-content/uploads/2026/07/TD-2026-2027-Q1.pdf is the "Disclosure Report of Signed Transactions 2026-04-01 to 2026-06-30" (37 rows; row 1 Bell Textron Canada Limited / Montenegro / Aerospace / $100,000–$1,000,000).

## Known gaps / limits
* Values are bands (`value_detail.range_low_cad/range_high_cad`), `contract.value` null.
* Reports before FY2021-22 Q2 are not listed on the CCC site; CCC annual reports give only aggregates.
* Transcription via the fetch tool: cells were reproduced as returned; one report (FY2025-26 Q3) had to be extracted in three slices (rows 1-27, 26-32, 32-53) and the slices were reconciled (rows 26, 27 and 32 overlap and match).
* CCC's own site also hosts a "Business Activity Report"/annual report naming large G2G contracts (e.g. Candu Energy – Romania Cernavoda refurbishment, GDLS-C – Saudi LAVs); those appear here only as anonymised or named rows without buyer names.

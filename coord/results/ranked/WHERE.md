# Where the deliverable is

Build **2026-11-10T08:43:34Z-db5c5f9** — 76935 rows, 73589 with a mailbox. Tiers (rows with a mailbox): A 1279, B 1623, C 368, D 12310, E 2746, F 8, I 11305, L 390, M 4432, R 27574, T 11554.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 83.5 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 105.8 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 89.6 MB | every package as CSV (38 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.7 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 3.1 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 44 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 139 |
| P01_GOLD_active_relationship_invoicing_AP_email | 626 |
| P02_active_relationship_finance_accounting_email | 403 |
| P03_active_relationship_purchasing_email | 209 |
| P04_active_relationship_general_email | 1570 |
| P05_likely_active_awarded_12_36_months_any_email | 377 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 4314 |
| P06T_active_service_seen_on_buyer_site_other_email | 9559 |
| P06_client_listing_invoicing_AP_email | 276 |
| P07_client_listing_finance_or_purchasing_email | 529 |
| P08_client_listing_general_email | 11055 |
| P09_older_contract_or_payment_any_email | 348 |
| P10R_ca_domain_registration_contract_own_email | 27005 |
| P10_linked_from_vendor_site_any_email | 2580 |
| P11_any_relationship_email_not_yet_confirmed | 3168 |
| P12_weaker_relationship_within_5_years_own_email | 8 |
| P13_inferred_relationship_no_record_own_email | 11305 |
| Z_no_email_yet_not_delivered | 3420 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

# Where the deliverable is

Build **2026-11-12T14:57:13Z-a7cfa01** — 264965 rows, 259912 with a mailbox. Tiers (rows with a mailbox): A 1241, B 1738, C 300, D 22950, E 4416, F 16, I 164561, L 433, M 19589, T 44668.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 453.5 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 522.3 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 472.1 MB | every package as CSV (126 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.7 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 15.0 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 196 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 198 |
| P01_GOLD_active_relationship_invoicing_AP_email | 625 |
| P02_active_relationship_finance_accounting_email | 463 |
| P03_active_relationship_purchasing_email | 260 |
| P04_active_relationship_general_email | 3558 |
| P05_likely_active_awarded_12_36_months_any_email | 419 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 19102 |
| P06T_active_service_seen_on_buyer_site_other_email | 43728 |
| P06_client_listing_invoicing_AP_email | 254 |
| P07_client_listing_finance_or_purchasing_email | 666 |
| P08_client_listing_general_email | 21518 |
| P09_older_contract_or_payment_any_email | 278 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2146 |
| P11_any_relationship_email_not_yet_confirmed | 1633 |
| P12_weaker_relationship_within_5_years_own_email | 16 |
| P13_inferred_relationship_no_record_own_email | 164561 |
| Z_no_email_yet_not_delivered | 5344 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

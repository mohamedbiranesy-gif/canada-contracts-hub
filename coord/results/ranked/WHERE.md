# Where the deliverable is

Build **2026-11-10T09:29:09Z-16ba0e7** — 77055 rows, 73672 with a mailbox. Tiers (rows with a mailbox): A 1279, B 1622, C 331, D 11534, E 2563, F 7, I 10644, L 378, M 4221, R 26037, T 15056.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 84.8 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 107.6 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 90.8 MB | every package as CSV (37 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.6 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 3.1 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 47 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 173 |
| P01_GOLD_active_relationship_invoicing_AP_email | 626 |
| P02_active_relationship_finance_accounting_email | 403 |
| P03_active_relationship_purchasing_email | 209 |
| P04_active_relationship_general_email | 1569 |
| P05_likely_active_awarded_12_36_months_any_email | 365 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 4103 |
| P06T_active_service_seen_on_buyer_site_other_email | 12949 |
| P06_client_listing_invoicing_AP_email | 263 |
| P07_client_listing_finance_or_purchasing_email | 501 |
| P08_client_listing_general_email | 10340 |
| P09_older_contract_or_payment_any_email | 312 |
| P10R_ca_domain_registration_contract_own_email | 25497 |
| P10_linked_from_vendor_site_any_email | 2406 |
| P11_any_relationship_email_not_yet_confirmed | 3187 |
| P12_weaker_relationship_within_5_years_own_email | 7 |
| P13_inferred_relationship_no_record_own_email | 10644 |
| Z_no_email_yet_not_delivered | 3454 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

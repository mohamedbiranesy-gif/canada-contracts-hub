# Where the deliverable is

Build **2026-11-11T19:36:57Z-324ccea** — 300708 rows, 292548 with a mailbox. Tiers (rows with a mailbox): A 1275, B 1729, C 314, D 27036, E 5457, F 7, I 17451, L 433, M 13462, R 106584, T 118800.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 347.8 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 423.8 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 369.5 MB | every package as CSV (131 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.5 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 19.5 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 123 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 446 |
| P01_GOLD_active_relationship_invoicing_AP_email | 625 |
| P02_active_relationship_finance_accounting_email | 486 |
| P03_active_relationship_purchasing_email | 264 |
| P04_active_relationship_general_email | 4132 |
| P05_likely_active_awarded_12_36_months_any_email | 420 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 13240 |
| P06T_active_service_seen_on_buyer_site_other_email | 95584 |
| P06_client_listing_invoicing_AP_email | 297 |
| P07_client_listing_finance_or_purchasing_email | 788 |
| P08_client_listing_general_email | 25442 |
| P09_older_contract_or_payment_any_email | 294 |
| P10R_ca_domain_registration_contract_own_email | 105619 |
| P10_linked_from_vendor_site_any_email | 2652 |
| P11_any_relationship_email_not_yet_confirmed | 24579 |
| P12_weaker_relationship_within_5_years_own_email | 7 |
| P13_inferred_relationship_no_record_own_email | 17451 |
| Z_no_email_yet_not_delivered | 8259 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

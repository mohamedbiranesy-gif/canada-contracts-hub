# Where the deliverable is

Build **2026-11-13T16:22:19Z-a1d369c** — 341713 rows, 335743 with a mailbox. Tiers (rows with a mailbox): A 1256, B 2322, C 105, D 30860, E 4098, F 10, I 207861, L 722, M 32387, T 56122.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 605.6 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 693.0 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 629.4 MB | every package as CSV (161 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.4 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 20.3 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 429 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 207 |
| P01_GOLD_active_relationship_invoicing_AP_email | 657 |
| P02_active_relationship_finance_accounting_email | 485 |
| P03_active_relationship_purchasing_email | 274 |
| P04_active_relationship_general_email | 4772 |
| P05_likely_active_awarded_12_36_months_any_email | 428 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 31427 |
| P06T_active_service_seen_on_buyer_site_other_email | 55074 |
| P06_client_listing_invoicing_AP_email | 243 |
| P07_client_listing_finance_or_purchasing_email | 758 |
| P08_client_listing_general_email | 28702 |
| P09_older_contract_or_payment_any_email | 71 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2008 |
| P11_any_relationship_email_not_yet_confirmed | 1806 |
| P12_weaker_relationship_within_5_years_own_email | 10 |
| P13_inferred_relationship_no_record_own_email | 207861 |
| Z_no_email_yet_not_delivered | 6501 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

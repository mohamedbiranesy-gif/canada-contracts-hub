# Where the deliverable is

Build **2026-11-12T07:45:01Z-3a45807** — 236452 rows, 230133 with a mailbox. Tiers (rows with a mailbox): A 1309, B 1771, C 336, D 23079, E 4446, F 16, I 144433, L 441, M 16287, T 38015.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 408.3 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 471.1 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 424.2 MB | every package as CSV (113 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 45.8 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 13.8 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 146 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 185 |
| P01_GOLD_active_relationship_invoicing_AP_email | 641 |
| P02_active_relationship_finance_accounting_email | 471 |
| P03_active_relationship_purchasing_email | 271 |
| P04_active_relationship_general_email | 3629 |
| P05_likely_active_awarded_12_36_months_any_email | 427 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 15872 |
| P06T_active_service_seen_on_buyer_site_other_email | 37219 |
| P06_client_listing_invoicing_AP_email | 257 |
| P07_client_listing_finance_or_purchasing_email | 677 |
| P08_client_listing_general_email | 21626 |
| P09_older_contract_or_payment_any_email | 314 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2168 |
| P11_any_relationship_email_not_yet_confirmed | 1512 |
| P12_weaker_relationship_within_5_years_own_email | 16 |
| P13_inferred_relationship_no_record_own_email | 144433 |
| Z_no_email_yet_not_delivered | 6588 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

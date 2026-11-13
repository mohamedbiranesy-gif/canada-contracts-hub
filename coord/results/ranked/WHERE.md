# Where the deliverable is

Build **2026-11-13T13:06:47Z-7b56b70** — 336619 rows, 330668 with a mailbox. Tiers (rows with a mailbox): A 1256, B 2322, C 312, D 31506, E 4180, F 10, I 202744, L 721, M 31428, T 56189.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 594.8 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 681.3 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 618.3 MB | every package as CSV (158 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 45.0 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 19.4 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 420 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 206 |
| P01_GOLD_active_relationship_invoicing_AP_email | 657 |
| P02_active_relationship_finance_accounting_email | 486 |
| P03_active_relationship_purchasing_email | 275 |
| P04_active_relationship_general_email | 4816 |
| P05_likely_active_awarded_12_36_months_any_email | 428 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 30514 |
| P06T_active_service_seen_on_buyer_site_other_email | 55144 |
| P06_client_listing_invoicing_AP_email | 249 |
| P07_client_listing_finance_or_purchasing_email | 780 |
| P08_client_listing_general_email | 29302 |
| P09_older_contract_or_payment_any_email | 278 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2052 |
| P11_any_relationship_email_not_yet_confirmed | 1813 |
| P12_weaker_relationship_within_5_years_own_email | 10 |
| P13_inferred_relationship_no_record_own_email | 202744 |
| Z_no_email_yet_not_delivered | 6445 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

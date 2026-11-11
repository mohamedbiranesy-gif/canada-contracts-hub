# Where the deliverable is

Build **2026-11-11T20:21:52Z-091c3f5** — 153127 rows, 147473 with a mailbox. Tiers (rows with a mailbox): A 1275, B 1727, C 320, D 26717, E 7104, F 15, I 33504, L 435, M 14830, T 61546.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 195.4 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 246.1 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 210.9 MB | every package as CSV (70 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.5 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 13.3 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 132 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 334 |
| P01_GOLD_active_relationship_invoicing_AP_email | 626 |
| P02_active_relationship_finance_accounting_email | 488 |
| P03_active_relationship_purchasing_email | 264 |
| P04_active_relationship_general_email | 4694 |
| P05_likely_active_awarded_12_36_months_any_email | 422 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 14527 |
| P06T_active_service_seen_on_buyer_site_other_email | 60669 |
| P06_client_listing_invoicing_AP_email | 295 |
| P07_client_listing_finance_or_purchasing_email | 774 |
| P08_client_listing_general_email | 25137 |
| P09_older_contract_or_payment_any_email | 298 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 3662 |
| P11_any_relationship_email_not_yet_confirmed | 1461 |
| P12_weaker_relationship_within_5_years_own_email | 15 |
| P13_inferred_relationship_no_record_own_email | 33504 |
| Z_no_email_yet_not_delivered | 5825 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

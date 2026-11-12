# Where the deliverable is

Build **2026-11-12T00:14:07Z-445acd8** — 186576 rows, 180937 with a mailbox. Tiers (rows with a mailbox): A 1274, B 1727, C 329, D 23373, E 4729, F 15, I 97406, L 435, M 14993, T 36656.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 278.9 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 335.8 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 296.3 MB | every package as CSV (85 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 44.5 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 10.3 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 129 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 189 |
| P01_GOLD_active_relationship_invoicing_AP_email | 626 |
| P02_active_relationship_finance_accounting_email | 464 |
| P03_active_relationship_purchasing_email | 263 |
| P04_active_relationship_general_email | 3678 |
| P05_likely_active_awarded_12_36_months_any_email | 422 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 14663 |
| P06T_active_service_seen_on_buyer_site_other_email | 35923 |
| P06_client_listing_invoicing_AP_email | 271 |
| P07_client_listing_finance_or_purchasing_email | 691 |
| P08_client_listing_general_email | 21900 |
| P09_older_contract_or_payment_any_email | 307 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2334 |
| P11_any_relationship_email_not_yet_confirmed | 1455 |
| P12_weaker_relationship_within_5_years_own_email | 15 |
| P13_inferred_relationship_no_record_own_email | 97406 |
| Z_no_email_yet_not_delivered | 5840 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

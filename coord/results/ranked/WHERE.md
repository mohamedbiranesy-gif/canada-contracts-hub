# Where the deliverable is

Build **2026-11-13T14:21:45Z-ffde0bb** — 338136 rows, 332186 with a mailbox. Tiers (rows with a mailbox): A 1256, B 2321, C 310, D 31421, E 4121, F 11, I 204826, L 722, M 31400, T 55798.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 599.1 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 685.9 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 622.7 MB | every package as CSV (159 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 45.1 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 18.7 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 420 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 203 |
| P01_GOLD_active_relationship_invoicing_AP_email | 653 |
| P02_active_relationship_finance_accounting_email | 489 |
| P03_active_relationship_purchasing_email | 276 |
| P04_active_relationship_general_email | 4792 |
| P05_likely_active_awarded_12_36_months_any_email | 429 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 30486 |
| P06T_active_service_seen_on_buyer_site_other_email | 54756 |
| P06_client_listing_invoicing_AP_email | 246 |
| P07_client_listing_finance_or_purchasing_email | 775 |
| P08_client_listing_general_email | 29228 |
| P09_older_contract_or_payment_any_email | 276 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2018 |
| P11_any_relationship_email_not_yet_confirmed | 1808 |
| P12_weaker_relationship_within_5_years_own_email | 11 |
| P13_inferred_relationship_no_record_own_email | 204826 |
| Z_no_email_yet_not_delivered | 6444 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

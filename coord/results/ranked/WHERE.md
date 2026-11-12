# Where the deliverable is

Build **2026-11-12T10:45:44Z-b218a97** — 265631 rows, 258878 with a mailbox. Tiers (rows with a mailbox): A 1321, B 1773, C 336, D 23085, E 4437, F 16, I 163822, L 440, M 18846, T 44802.

The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):

**https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/tag/ranked-latest**

| File | Size | What |
|---|---|---|
| [ranked_buyers.csv.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.csv.gz) | 454.2 MB | the whole table, one row per buyer |
| [ranked_buyers.jsonl.gz](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_buyers.jsonl.gz) | 524.3 MB | the same rows as JSON lines |
| [ranked_batches.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_batches.zip) | 472.0 MB | every package as CSV (124 files) |
| [ranked_contracts.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_contracts.zip) | 46.2 MB | contracts of the delivered buyers |
| [ranked_extras.zip](https://github.com/mohamedbiranesy-gif/canada-contracts-hub/releases/download/ranked-latest/ranked_extras.zip) | 13.6 MB | audit flags, DMARC list, rows changed since the last build |

## Packages in `ranked_batches.zip`

| Package | Rows |
|---|---|
| P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email | 195 |
| P01T_active_service_seen_on_buyer_site_invoicing_AP_email | 199 |
| P01_GOLD_active_relationship_invoicing_AP_email | 644 |
| P02_active_relationship_finance_accounting_email | 472 |
| P03_active_relationship_purchasing_email | 271 |
| P04_active_relationship_general_email | 3641 |
| P05_likely_active_awarded_12_36_months_any_email | 426 |
| P06M_member_or_regulated_payer_of_canadian_body_other_email | 18370 |
| P06T_active_service_seen_on_buyer_site_other_email | 43858 |
| P06_client_listing_invoicing_AP_email | 256 |
| P07_client_listing_finance_or_purchasing_email | 677 |
| P08_client_listing_general_email | 21636 |
| P09_older_contract_or_payment_any_email | 314 |
| P10R_ca_domain_registration_contract_own_email | 0 |
| P10_linked_from_vendor_site_any_email | 2160 |
| P11_any_relationship_email_not_yet_confirmed | 1640 |
| P12_weaker_relationship_within_5_years_own_email | 16 |
| P13_inferred_relationship_no_record_own_email | 163822 |
| Z_no_email_yet_not_delivered | 7034 |

`batches_head/` in this folder holds the first 10 rows of each package, to look at a package without downloading it. Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.
Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build).

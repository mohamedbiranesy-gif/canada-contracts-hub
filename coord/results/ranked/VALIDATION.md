# Integrity gates — 39682 delivered rows in 17 packages

- **1 mailbox present, valid, domain with a mail server**: PASS (0)
- **2 role mailbox (no person-like local part, no freemail)**: PASS (0)
- **3 mailbox evidence url + quote containing the address**: PASS (0)
- **4 relationship evidence (contract_status + vendor_country_basis + vendor)**: PASS (0)
- **5 one row per mailbox across packages**: PASS (0)
- **6 no blank cell**: PASS (0)
- **7 receivables mailbox graded as invoicing (heuristic, review)**: PASS (0)

Informational: 54 rows whose quote shows the label next to the address rather than the address itself (the address sits in a mailto link; the referee re-fetched the page and saw it).

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 16
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 90
- P01_GOLD_active_relationship_invoicing_AP_email: 560
- P02_active_relationship_finance_accounting_email: 261
- P03_active_relationship_purchasing_email: 236
- P04_active_relationship_general_email: 1600
- P05_likely_active_awarded_12_36_months_any_email: 374
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 168
- P06T_active_service_seen_on_buyer_site_other_email: 2422
- P06_client_listing_invoicing_AP_email: 137
- P07_client_listing_finance_or_purchasing_email: 196
- P08_client_listing_general_email: 2717
- P09_older_contract_or_payment_any_email: 364
- P10_linked_from_vendor_site_any_email: 2603
- P11_any_relationship_email_not_yet_confirmed: 476
- P12_weaker_relationship_within_5_years_own_email: 23
- P13_inferred_relationship_no_record_own_email: 27439

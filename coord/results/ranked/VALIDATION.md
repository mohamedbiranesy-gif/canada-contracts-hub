# Integrity gates — 180736 delivered rows in 18 packages (83 files)

- **1 mailbox present, valid, domain with a mail server**: PASS (0)
- **2 role mailbox (no person-like local part, no freemail)**: PASS (0)
- **3 mailbox evidence url + quote containing the address, referee-confirmed (all packages but P11)**: PASS (0)
- **4 relationship evidence (contract_status + vendor_country_basis + vendor)**: PASS (0)
- **5 one row per mailbox across packages**: PASS (0)
- **6 no blank cell**: PASS (0)
- **7 receivables mailbox graded as invoicing (heuristic, review)**: PASS (0)

Informational: 2 rows whose quote shows the label next to the address rather than the address itself (the address sits in a mailto link; the referee re-fetched the page and saw it).

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 129
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 189
- P01_GOLD_active_relationship_invoicing_AP_email: 626
- P02_active_relationship_finance_accounting_email: 464
- P03_active_relationship_purchasing_email: 263
- P04_active_relationship_general_email: 3678
- P05_likely_active_awarded_12_36_months_any_email: 422
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 14663
- P06T_active_service_seen_on_buyer_site_other_email: 35923
- P06_client_listing_invoicing_AP_email: 271
- P07_client_listing_finance_or_purchasing_email: 691
- P08_client_listing_general_email: 21900
- P09_older_contract_or_payment_any_email: 307
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2334
- P11_any_relationship_email_not_yet_confirmed: 1455
- P12_weaker_relationship_within_5_years_own_email: 15
- P13_inferred_relationship_no_record_own_email: 97406

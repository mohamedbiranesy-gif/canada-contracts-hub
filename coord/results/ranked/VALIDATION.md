# Integrity gates — 356279 delivered rows in 18 packages (169 files)

- **1 mailbox present, valid, domain with a mail server**: PASS (0)
- **2 role mailbox (no person-like local part, no freemail)**: PASS (0)
- **3 mailbox evidence url + quote containing the address, referee-confirmed (all packages but P11)**: PASS (0)
- **4 relationship evidence (contract_status + vendor_country_basis + vendor)**: FAIL (65)
    - P01_GOLD_active_relationship_invoicing_AP_email:627 GIW INDUSTRIES, INC.
    - P01_GOLD_active_relationship_invoicing_AP_email:630 The Kraft Heinz Company
    - P02_active_relationship_finance_accounting_email:408 Sherwin-Williams Paints, Stains, Supplie
    - P03_active_relationship_purchasing_email:221 multipleline.americannational.com
    - P03_active_relationship_purchasing_email:222 Elevance Health
    - P03_active_relationship_purchasing_email:223 American Family Insurance
    - P03_active_relationship_purchasing_email:224 DZYNE TECHNOLOGIES INCORPORATED
    - P03_active_relationship_purchasing_email:225 Quad/Graphics, Inc.
    - P03_active_relationship_purchasing_email:226 ultimatemedical.edu
    - P04_active_relationship_general_email:2190 wildthymegroup.com
    - P04_active_relationship_general_email:2191 Quisitive
    - P04_active_relationship_general_email:2192 Get More with Kliken
    - P04_active_relationship_general_email:2193 HearUSA
    - P04_active_relationship_general_email:2194 learn.e4l.com
    - P04_active_relationship_general_email:2195 Stand Up Guys Junk Removal
    - P04_active_relationship_general_email:2196 LifeSafer
    - P04_active_relationship_general_email:2197 O'Brien Brothers
    - P04_active_relationship_general_email:2198 Proforma Canada
    - P04_active_relationship_general_email:2199 Wally's Natural
    - P04_active_relationship_general_email:2200 Centered Health and Aesthetics
- **5 one row per mailbox across packages**: PASS (0)
- **6 no blank cell**: PASS (0)
- **7 receivables mailbox graded as invoicing (heuristic, review)**: PASS (0)

Informational: 3 rows whose quote shows the label next to the address rather than the address itself (the address sits in a mailto link; the referee re-fetched the page and saw it).

## Rows per package
- P01M_member_or_regulated_payer_of_canadian_body_invoicing_AP_email: 435
- P01T_active_service_seen_on_buyer_site_invoicing_AP_email: 201
- P01_GOLD_active_relationship_invoicing_AP_email: 629
- P02_active_relationship_finance_accounting_email: 474
- P03_active_relationship_purchasing_email: 275
- P04_active_relationship_general_email: 4816
- P05_likely_active_awarded_12_36_months_any_email: 443
- P06M_member_or_regulated_payer_of_canadian_body_other_email: 32303
- P06T_active_service_seen_on_buyer_site_other_email: 53176
- P06_client_listing_invoicing_AP_email: 242
- P07_client_listing_finance_or_purchasing_email: 759
- P08_client_listing_general_email: 28712
- P09_older_contract_or_payment_any_email: 71
- P10R_ca_domain_registration_contract_own_email: 0
- P10_linked_from_vendor_site_any_email: 2004
- P11_any_relationship_email_not_yet_confirmed: 1809
- P12_weaker_relationship_within_5_years_own_email: 11
- P13_inferred_relationship_no_record_own_email: 229919

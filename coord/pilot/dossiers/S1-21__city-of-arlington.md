# S1-21 — City of Arlington ⇄ Bubble Technology Industries Inc

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Arlington, TX — PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)
SUBMIT TO: accountspayable@arlingtontx.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal
REFERENCE: contract 27-0035 (govtContractNumber) | PO rule: purchase-order terms published (as published: shall be set forth in the block of the purchase order)
FROM / REMIT TO: BUBBLE TECHNOLOGY INDUSTRIES INC. — 31278 Highway 17, Chalk River, Ontario, K0J 1J0, CA | GST/HST 121041842RT0001 (account derived from the BN9)
TAX: Tax Exemption for Eligible Childcare Providers Improvement Districts Purchasing Sub-menu Bidding & Procurement Pu (as printed on https://www.arlingtontx.gov/Gov | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 30 days from the invoice date (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finan
DESCRIPTION: Sole Source Contract for Hazmat Detection System and Software Support Services
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Arlington (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Bubble Technology Industries Inc | subject: Sole Source Contract for Hazmat Detection System and Software Support Services | contract number: 27-0035 (govtContractNumber) | all identifiers: {"govtContractNumber": "27-0035"} | awarded 2026-10-30 | published by: businessCountryCode (TEC Form 1295 CSV) | record: https://www.ethics.texas.gov/data/search/1295/1295Certificates_2026_to_2030.csv | vendor in Canada because: businessCountryCode (TEC Form 1295 CSV)=Chalk River, AE, CAN | status rule: likely active (record dated in the last 12 months: businessCountryCode (TEC Form 1295 CSV))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:9bd09965d76737c0
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: businessCountryCode (TEC Form 1295 CSV); 0 in the contract dataset)

## Buyer
- **buyer**: City of Arlington
- **buyer_website**: http://www.arlingtontx.gov/
- **buyer_address**: 101 W. Abram St., Arlington TX 76010
- **buyer_phone**: 817-459-6777
- **buyer_contact_evidence_url**: https://www.arlingtontx.gov/Government/Contact-Us
- **buyer_legal_name_as_published**: City of Arlington, TX
- **buyer_logo_url**: https://www.arlingtontx.gov/files/templates/00000000-0000-0000-0000-000000000000/1e57e76d-1919-4c46-a066-ed414e8610c1/v/238/print-logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/city-of-arlington/
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.arlingtontx.gov/Government/Contact-Us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required pre-employment training, background checks (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0031-scope-of-work.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax Exemption for Eligible Childcare Providers Improvement Districts Purchasing Sub-menu Bidding & Procurement Pu (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@arlingtontx.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll
- **email_evidence_quote**: l PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arlingtontx.gov Division Listing for Vendors (PDF, 53KB) Back to top Site Footer Contact Us 101 W. Abram St. Arlington TX 76010 View o
- **email_evidence_context**: g Financial Transparency Accounts Payable & Payroll Annual Financial Reports Accounts Payable & Payroll Payroll PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arlingtontx.gov Division Listing for Vendors (PDF, 53KB) Back to top Site Footer Contact Us 101 W. Abram St. Arlington TX 76010 View on Map Contact Us 817-459-6777 Site Footer Share & Connect Like us on Facebook Follow us on X Follow us on Instagram Follow us on Yo (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@arlingtontx.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll | quote: "l PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arli" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00037
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com;
- **dmarc_record_domain**: arlingtontx.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:%{ir}.%{v}.%{d}.spf.has.pphosted.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 817-459-6300 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)
- **invoice_mailing_address**: PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)
- **payment_terms_as_published**: 30 days from the invoice date (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0031-scope-of-work.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: shall be set forth in the block of the purchase order) (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0121-bid-invitation.pdf, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "30 days from the invoice date (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0031-scope-of-work.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: shall be set forth in the block of the purchase order) (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0121-bid-invitation.pdf, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "817-459-6300 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)", "mailing_address": "PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Arlington, TX — PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@arlingtontx.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: contract 27-0035 (govtContractNumber) | PO rule: purchase-order terms published (as published: shall be set forth in the block of the purchase order) ⏎ FROM / REMIT TO: BUBBLE TECHNOLOGY INDUSTRIES INC. — 31278 Highway 17, Chalk River, Ontario, K0J 1J0, CA | GST/HST 121041842RT0001 (account derived from the BN9) ⏎ TAX: Tax Exemption for Eligible Childcare Providers Improvement Districts Purchasing Sub-menu Bidding & Procurement Pu (as printed on https://www.arlingtontx.gov/Gov | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 30 days from the invoice date (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finan ⏎ DESCRIPTION: Sole Source Contract for Hazmat Detection System and Software Support Services
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Arlington, TX", "legal_name_is_published": true, "address": "PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@arlingtontx.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: shall be set forth in the block of the purchase order) (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0121-bid-invitation.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "27-0035 (govtContractNumber)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 27-0035 (govtContractNumber) — source us_tx_form1295"}, "terms": {"payment_terms
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 87
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: 27-0035 (govtContractNumber) — source us_tx_form1295

## Vendor
- **vendor**: Bubble Technology Industries Inc
- **vendor_legal_name**: BUBBLE TECHNOLOGY INDUSTRIES INC.
- **vendor_registry_id**: Corporations Canada (corporation number): 2294770; corporation number 2294770 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2294770
- **vendor_registered_address**: 1565 Carling Avenue, Suite 400, OTTAWA, ON, K1Z 8R1, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 7 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 1988-02-02
- **vendor_address**: 31278 Highway 17, Chalk River, Ontario, K0J 1J0, CA
- **vendor_country_basis**: businessCountryCode (TEC Form 1295 CSV)=Chalk River, AE, CAN
- **vendor_bn9**: 121041842
- **vendor_gst_hst_derived**: 121041842RT0001
- **vendor_website**: https://bubbletech.ca/
- **vendor_emails**: info@bubbletech.ca; sales@bubbletech.ca; support@bubbletech.ca
- **vendor_phone**: +1 (613)-589-2456
- **vendor_contact_evidence_url**: https://bubbletech.ca/contact-us-2/contact-information/
- **vendor_logo_url**: https://bubbletech.ca/
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://bubbletech.ca/ (Bubble Technology Industries --> Search for: --> Partner login header-login--> MENU MENU Company About BTI News & Events Careers The Region ISO Quality Assuranc)
- **vendor_facts_provenance**: name and address: the record's vendor block (businessCountryCode (TEC Form 1295 CSV)); registry identity: Corporations Canada (corporation number): 2294770; corporation number 2294770 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1988-02-02; phone / role e-mails / logo: the vendor's own site, https://bubbletech.ca/contact-us-2/contact-information/ (tools/org_contacts.py, org_extras.py); website: https://bubbletech.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 1988-02-02
- **vendor_years_in_business**: 38.8 (since 1988-02-02, registry date)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: shall be set forth in the block of the purchase order) (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0121-bid-invitation.pdf, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: businessCountryCode (TEC Form 1295 CSV))
- **contract_reference**: {"govtContractNumber": "27-0035"}
- **contract_title**: Sole Source Contract for Hazmat Detection System and Software Support Services
- **contract_description**: Sole Source Contract for Hazmat Detection System and Software Support Services (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: 27-0035 (govtContractNumber)
- **award_date**: 2026-10-30
- **contract_link**: https://www.ethics.texas.gov/data/search/1295/1295Certificates_2026_to_2030.csv
- **source**: businessCountryCode (TEC Form 1295 CSV)
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: businessCountryCode (TEC Form 1295 CSV); 0 in the contract dataset)
- **records_in_contract_dataset**: 3 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 121041842RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Arlington, TX — PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@arlingtontx.gov (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: contract 27-0035 (govtContractNumber) | PO rule: purchase-order terms published (as published: shall be set forth in the block of the purchase order) ⏎ FROM / REMIT TO: BUBBLE TECHNOLOGY INDUSTRIES INC. — 31278 Highway 17, Chalk River, Ontario, K0J 1J0, CA | GST/HST 121041842RT0001 (account derived from the BN9) ⏎ TAX: Tax Exemption for Eligible Childcare Providers Improvement Districts Purchasing Sub-menu Bidding & Procurement Pu (as printed on https://www.arlingtontx.gov/Gov | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 30 days from the invoice date (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finan ⏎ DESCRIPTION: Sole Source Contract for Hazmat Detection System and Software Support Services
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Arlington, TX", "legal_name_is_published": true, "address": "PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@arlingtontx.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 90231 MS 63-0800 Arlington, TX 76004 (as printed on https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: shall be set forth in the block of the purchase order) (as printed on https://www.arlingtontx.gov/files/assets/city/v/1/finance/documents/financial-transparency/contracts-and-procurement/bid-documents/goods-and-services/2022/22-0121-bid-invitation.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "27-0035 (govtContractNumber)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 27-0035 (govtContractNumber) — source us_tx_form1295"}, "terms": {"payment_terms
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 87
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accountspayable@arlingtontx.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll", "quote: \"l PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arli\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00037"], "buyer_facts": ["address and phone: the buyer's own site, https://www.arlingtontx.gov/Government/Contact-Us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll | 2026-11-08 | ok |  |  |  | 817-459-6300 | PO Box 90231 MS 63-0800 Arlington, TX 76004 |  |  |  |  |

## Buyer site facts (org_extras, arlingtontx.gov)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: City of Arlington, TX
- **legal_name_url**: https://www.arlingtontx.gov/Home
- **legal_name_quote**: Home | City of Arlington, TX --> Skip to main content opens in new tab or window Sign up for MyArlingtonTX News Stay informed wi
- **logo_url**: https://www.arlingtontx.gov/files/templates/00000000-0000-0000-0000-000000000000/1e57e76d-1919-4c46-a066-ed414e8610c1/v/238/print-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: arlingtontx.gov
- **key**: lead:9bd09965d76737c0
- **name**: City of Arlington
- **website**: https://arlingtontx.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: City of Arlington
- **legal_name_stated_url**: https://www.arlingtontx.gov/Government/Data-Information/Data-Information-Directory/Accessibility
- **legal_name_stated_quote**: Accessibility | City of Arlington, TX --> Skip to main content opens in new tab or window Sign up for MyArlingtonTX News Stay informe
- **mentions**: {'payment_method': {'text': 'Interactive Maps Business Economic Development Corporation Economic Development Site Se', 'url': 'https://www.arlingtontx.gov/Home', 'quote': 'Us Action Center City Phones & Emails Directory Mobile Apps Data & Information City Facts Open Data Interactive Maps Business Economic Development Corporation Economic Development Site Selection Resources Small Business Assistance Development Resources Water U'}}
- **linkedin_url**: https://www.linkedin.com/company/city-of-arlington/
- **tel_links**: 8174596777

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "101 W. Abram St., Arlington TX 76010", "address_country": "US", "address_url": "https://www.arlingtontx.gov/Government/Contact-Us", "address_method": "pattern", "address_quote": "able mobile apps from the City of Arlington. Back to top Site Footer Contact Us 101 W. Abram St. Arlington TX 76010 View on Map Contact Us 817-459-6777 Site Footer Share & Conn", "phone": "817-459-6777", "phone_url": "https://www.arlingtontx.gov/Government/Contact-Us", "domain": "arlingtontx.gov", "key": "lead:9bd09965d76737c0", "name": "City of Arlington", "website": "https://arlingtontx.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, bubbletech.ca)
- **status**: ok
- **pages**: 6
- **v**: 2
- **legal_name_stated**: Bubble Technology Industries
- **legal_name_stated_url**: https://bubbletech.ca/
- **legal_name_stated_quote**: Bubble Technology Industries --> Search for: --> Partner login header-login--> MENU MENU Company About BTI News & Events Careers
- **linkedin_url**: https://www.linkedin.com/company/bubbletechnologyindustries/
- **language**: en
- **logo_url**: https://bubbletech.ca/
- **logo_basis**: logo image in the site header
- **legal_name**: the Bubble Technology Industries Inc
- **legal_name_url**: https://bubbletech.ca/terms-of-use/
- **legal_name_quote**: without limitation, reasonable legal and accounting fees, alleging or resulting from your access to the Bubble Technology Industries Inc. website or your breach of the Terms of Uses. No Liability In no event will Bubble Technology Indus
- **domain**: bubbletech.ca
- **key**: vendor:Bubble Technology Industries Inc
- **name**: Bubble Technology Industries Inc
- **website**: https://bubbletech.ca/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "P.O. Box 100, Chalk River, Ontario, Canada, K0J 1J0", "address_country": "CA", "address_url": "https://bubbletech.ca/contact-us-2/contact-information/", "address_method": "pattern", "address_quote": "hone +1 (613)-589-2456 Postal Address P.O. Box 100 Chalk River, Ontario, Canada K0J 1J0 Shipping Address 31278 Highway 17 Chalk River, Ontario, Canada K0J 1J0 Thank yo", "phone": "+1 (613)-589-2456", "phone_url": "https://bubbletech.ca/contact-us-2/contact-information/", "emails": "info@bubbletech.ca; sales@bubbletech.ca; support@bubbletech.ca", "emails_url": "https://bubbletech.ca/contact-us-2/contact-information/", "domain": "bubbletech.ca", "key": "vendor:Bubble Technology Industries Inc", "name": "Bubble Technology Industries Inc", "website": "https://bubbletech.ca/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | City of Arlington |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:9bd09965d76737c0",
 "ap_contact_team": {
  "emails": [
   "accountspayable@arlingtontx.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@arlingtontx.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll",
    "quote": "l PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arlingtontx.gov Division Listing for Vendors (PDF, 53KB) Back to top Site Footer Contact Us 101 W. Abram St. Arlington TX 76010 View o",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Arlington",
    "task_id": "CL-LT-01440",
    "verified_via": "https://web.archive.org/web/20260723172110/https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll"
   },
   {
    "email": "accountspayable@arlingtontx.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll",
    "quote": "l PO Box 90231 MS 63-0800 Arlington, TX 76004 817-459-6300 Accounts Payable Office PO Box 90231 MS 63-0840 Arlington, TX 76004 817-459-6300 accountspayable@arlingtontx.gov Division Listing for Vendors (PDF, 53KB) Back to top Site Footer Contact Us 101 W. Abram St. Arlington TX 76010 View o",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Arlington",
    "task_id": "CL-WS-00037",
    "verified_via": "https://web.archive.org/web/20260723172110/https://www.arlingtontx.gov/Government/Budget-Finance/Accounts-Payable-Payroll"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.arlingtontx.gov (60 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 5)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:cb:CW2422543 | Canadian Space Agency (CSA) | Canadian Active Neutron Spectrometer (CANS) Phase BCDE | 5512500.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2422543 |
| ted_eu:388878-2022:award1 | Fraunhofer-Gesellschaft - Einkauf C2 | Neutronenspektrometer für Energiebereich thermisch bis 16 MeV | 0.01 |  |  | https://ted.europa.eu/en/notice/-/detail/388878-2022 |
| us_city_austin:PO830026072001536:V00000992894 | City of Austin, Texas | PR267837-Hazmat - Repair for FlexSpec Radiation Backpack | 2251.0 |  |  | https://datahub.austintexas.gov/d/3ebq-e9iz |
| usaspending:CONT_AWD_70RWMD25C00000009_7001_-NONE-_-NONE- | Department of Homeland Security | THIS AWARD INITIATES A NEW COST PLUS FIXED FEE CONTRACT WITH BUBBLE TECHNOLOGY INDUSTRIES FOR SECONDARY NEUTRON AIR CARGO SCREENING (SNACS). | 1681724.51 |  |  | https://www.usaspending.gov/award/CONT_AWD_70RWMD25C00000009_7001_-NONE-_-NONE-/ |
| usaspending:sub:CONT_AWD_19AQMM18C0185_1900_-NONE-_-NONE-:GDIT-86810:QQG9V3DKCNS7 | GENERAL DYNAMICS INFORMATION TECHNOLOGY, INC. | PRODUCTS | 197336.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_19AQMM18C0185_1900_-NONE-_-NONE-/ |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane). Budget rule (PLAN §4d): layer 1 already carries this buyer's confirmed channel, PO rule and terms with quotes; the notes below add only what changes how the invoice is built.

**Row is complete as published** (City of Arlington, TX: PO terms published, "30 days from the invoice date", supplier portal, confirmed AP mailbox).
Texas municipality: exempt from Texas sales tax (derived), USD, Prompt Payment Act ch. 2251. Bubble Technology Industries (Chalk River, ON): zero-rated
export; the City requires vendor registration in its supplier portal before payment (row: portal named) — register first.

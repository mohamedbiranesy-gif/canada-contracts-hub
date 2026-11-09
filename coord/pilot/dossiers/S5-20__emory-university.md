# S5-20 — Emory University ⇄ THE UNIVERSITY OF BRITISH COLUMBIA

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Emory University — Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557 — buyer tax no. 580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: invoices@emory.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)
REFERENCE: contract {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 (reference) | PO rule: yes (as published: must match the purchase order)
FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public
TAX: Tax-Exempt Authorization letter (PDF) (regarding tangible property and service) tions (PDF) (as printed on https://finance.emory.edu/home/procurement/sourcing/s | CURRENCY: USD (derived fr
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Emory University (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): THE UNIVERSITY OF BRITISH COLUMBIA | subject: IMPACT-ADRD: INVESTIGATING THE MULTI-OMICS PERTURBATIONS ASSOCIATED WITH COMPLEX E | contract number: {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_gene | all identifiers: {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 | value: 99867.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2026-06-26 | published by: subawardee country | record: https://www.usaspending.gov/award/U01AG088425 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:2feb523fd776ea8c
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: Emory University
- **buyer_website**: https://emory.edu/
- **buyer_address**: Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557
- **buyer_phone**: 470-268-3610
- **buyer_contact_evidence_url**: https://obs.emory.edu/relocation-services/index.html
- **buyer_legal_name_as_published**: Emory University
- **buyer_bn_as_published**: 580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 580566256RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.emory.edu/sites/emorymain/files/logos/logo-dark.svg?1785786799
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/emory-university/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q621043; private university; private not-for-profit educational institution
- **buyer_founded**: 1836-00-00 (Wikidata Q621043, official website on the organisation's domain (https://emory.edu) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 3084868216 Q4917; 3145500356 Q4917; 3275702848 Q4917; 3504618972 Q4917; 3525925969 Q4917; 3589561177 Q4917; 4065819568 Q (Wikidata Q621043, official website on the organisation's domain (https://emory.edu) + name; 2026-11-08)
- **buyer_employees**: 12953 (Wikidata Q621043, official website on the organisation's domain (https://emory.edu) + name; 2026-11-08)
- **buyer_legal_form**: Georgia non-profit corporation (Wikidata Q621043, official website on the organisation's domain (https://emory.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://obs.emory.edu/relocation-services/index.html (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: preferred methods of supplier payments, Single Use Account (SUA) and ACH Direct Deposit (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax-Exempt Authorization letter (PDF) (regarding tangible property and service) tions (PDF) (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoices@emory.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html
- **email_evidence_quote**: t possible, email all Emory University invoices containing Purchase Orders numbers beginning with A, CH, S, T or W followed by 6 numbers to Invoices@emory.edu. Step 4: Submit the Invoice for Payment The University will pay all valid invoices and/or undisputed amounts of an invoice within t
- **email_evidence_context**: owledge receipt (based on dollar threshold) through electronic receiving. Email If the electronic option is not possible, email all Emory University invoices containing Purchase Orders numbers beginning with A, CH, S, T or W followed by 6 numbers to Invoices@emory.edu. Step 4: Submit the Invoice for Payment The University will pay all valid invoices and/or undisputed amounts of an invoice within the negotiation payments terms after receipt of invoice or goods or services. See Payment Methods and Payment Terms for (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoices@emory.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html | quote: "t possible, email all Emory University invoices containing Purchase Orders numbers beginning with A, CH, S, T or W followed by 6 numbers to Invoices@emory.edu. " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00033
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; fo=1; pct=100; ri=3600; rua=mailto:dmarc.aggrep@emory.edu,mailto:dmarc_agg@vali.email
- **dmarc_record_domain**: emory.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:170.140.0.0/16 ip4:163.246.0.0/16 include:spf.protection.outlook.com include:technolutions.net include:cust-spf.exacttarget.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)
- **payment_terms_as_published**: payment terms are Net 60 (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: must match the purchase order) (as printed on https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment terms are Net 60 (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)", "po_required": "yes (as published: must match the purchase order) (as printed on https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)", "requirements_text": "invoice format as published: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Emory University — Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557 — buyer tax no. 580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: invoices@emory.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08) ⏎ REFERENCE: contract {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 (reference) | PO rule: yes (as published: must match the purchase order) ⏎ FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public ⏎ TAX: Tax-Exempt Authorization letter (PDF) (regarding tangible property and service) tions (PDF) (as printed on https://finance.emory.edu/home/procurement/sourcing/s | CURRENCY: USD (
- **invoice_card_json**: {"bill_to": {"legal_name": "Emory University", "legal_name_is_published": true, "address": "Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557", "address_is_the_invoice_address": false, "tax_number": "580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "invoices@emory.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: must match the purchase order) (as printed on https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"90511-75581-UBC\", \"prime_award_internal_id\": \"2716723
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 (reference) — source usaspending

## Vendor
- **vendor**: THE UNIVERSITY OF BRITISH COLUMBIA
- **vendor_address**: Vancouver, BC
- **vendor_country_basis**: subawardee country=CAN
- **vendor_website**: https://www.ubc.ca/
- **vendor_contact_evidence_url**: https://blogs.ubc.ca/about/
- **vendor_logo_url**: https://cdn.ubc.ca/clf/7.0.5/img/touch-icon-iphone.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.ubc.ca/ (The University of British Columbia Skip to main content Search UBC Search The University of British Columbia The University of British Columbia UBC Search About)
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); phone / role e-mails / logo: the vendor's own site, https://blogs.ubc.ca/about/ (tools/org_contacts.py, org_extras.py); website: https://www.ubc.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: must match the purchase order) (as printed on https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842
- **contract_title**: IMPACT-ADRD: INVESTIGATING THE MULTI-OMICS PERTURBATIONS ASSOCIATED WITH COMPLEX E
- **contract_description**: IMPACT-ADRD: INVESTIGATING THE MULTI-OMICS PERTURBATIONS ASSOCIATED WITH COMPLEX E (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 (reference)
- **contract_value**: 99867.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2026-06-26
- **contract_link**: https://www.usaspending.gov/award/U01AG088425
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 6
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 6 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 580566256RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Emory University — Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557 — buyer tax no. 580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: invoices@emory.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08) ⏎ REFERENCE: contract {"internal_id": "90511-75581-UBC", "prime_award_internal_id": "271672361", "Sub-Award ID": "90511-75581-UBC", "Prime Award ID": "U01AG088425", "prime_award_generated_internal_id": "ASST_NON_U01AG08842 (reference) | PO rule: yes (as published: must match the purchase order) ⏎ FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public ⏎ TAX: Tax-Exempt Authorization letter (PDF) (regarding tangible property and service) tions (PDF) (as printed on https://finance.emory.edu/home/procurement/sourcing/s | CURRENCY: USD (
- **invoice_card_json**: {"bill_to": {"legal_name": "Emory University", "legal_name_is_published": true, "address": "Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557", "address_is_the_invoice_address": false, "tax_number": "580566256 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2022-05-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "invoices@emory.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory University (as printed on https://finance.emory.edu/home/procurement/sourcing/supplier-management.html, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: must match the purchase order) (as printed on https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"90511-75581-UBC\", \"prime_award_internal_id\": \"2716723
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["invoices@emory.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html", "quote: \"t possible, email all Emory University invoices containing Purchase Orders numbers beginning with A, CH, S, T or W followed by 6 numbers to Invoices@emory.edu. \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00033"], "buyer_facts": ["address and phone: the buyer's own site, https://obs.emory.edu/relocation-services/index.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and d

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html | 2026-11-08 | ok |  | yes (as published: must match the purchase order) | supplier / vendor portal |  |  |  |  |  | assumed to indicate the immediate remittance of payment. In order for a payment to process, the PO invoice quantity and dollar amount must match the purchase order and the department must acknowledge receipt (based on do |

## Buyer site facts (org_extras, emory.edu)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Emory University
- **legal_name_url**: https://www.emory.edu/
- **legal_name_quote**: Home | Emory University Skip to main content { const url = 'https://template.aws.emory.edu/shared-assets/emergency/alert-fe
- **logo_url**: https://www.emory.edu/sites/emorymain/files/logos/logo-dark.svg?1785786799
- **logo_basis**: logo image in the site header
- **domain**: emory.edu
- **key**: lead:2feb523fd776ea8c
- **name**: Emory University
- **website**: https://emory.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Emory University
- **legal_name_stated_url**: https://www.emory.edu/about
- **legal_name_stated_quote**: About | Emory University Skip to main content { const url = 'https://template.aws.emory.edu/shared-assets/emergency/alert-fe
- **linkedin_url**: https://www.linkedin.com/school/emory-university/
- **tel_links**: 404.727.6069; 404.727.6036; 770.784.8888; 770.784.8328; 404.727.6270; 404.727.8106; 404.727.6311; 404.727.6028; 404.727.

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "Ace/Atlas , Name:, Mike McGill , Title:, Vice President, Work:, 216-290-3390 , Cell:, 216-403-2557", "address_country": "", "address_url": "https://obs.emory.edu/relocation-services/index.html", "address_method": "address-tag", "address_quote": "l Title: Account Manager Phone: 470-268-3610 Email: Jeralyn.Howell@CorpRelo.com Ace/Atlas Name: Mike McGill Title: Vice President Work: 216-290-3390 Cell: 216-403-2557 Em", "phone": "470-268-3610", "phone_url": "https://obs.emory.edu/relocation-services/index.html", "domain": "emory.edu", "key": "lead:2feb523fd776ea8c", "name": "Emory University", "website": "https://finance.emory.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, ubc.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **domain**: ubc.ca
- **key**: lead:7d16facc909dded1
- **name**: The University Of British Columbia
- **website**: https://ubc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University
- **legal_name_stated_url**: https://www.ubc.ca:443/about/
- **legal_name_stated_quote**: About UBC | The University of British Columbia Skip to main content Search UBC Search The University of British Columbia The U
- **linkedin_url**: https://www.linkedin.com/school/universityofbc
- **logo_url**: https://cdn.ubc.ca/clf/7.0.5/img/touch-icon-iphone.png
- **logo_basis**: site icon (apple-touch-icon)

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "1234 Street, Vancouver, BC, Canada, V0V 0V0", "address_country": "CA", "address_url": "https://blogs.ubc.ca/about/", "address_method": "pattern", "address_quote": "iki for sharing your UBC resources. Unit Name 1234 Street Vancouver , BC Canada V0V 0V0 Back to top The University of British Columbia Emergency Procedures | Terms of", "domain": "ubc.ca", "key": "vd:ubc.ca", "name": "Institute for Critical Education Studies", "website": "https://blogs.ubc.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Emory University | Q621043 | official website on the organisation's domain (https://emory.edu) + name |  | Emory University | Université Emory | private university; private not-for-profit educational institution | Georgia non-profit corporation | United States | 1836-00-00 | Atlanta |
| b | The University Of British Columbia | Q391028 | official website on the organisation's domain (https://www.ubc.ca/) + name | The University of British Columbia [en] | University of British Columbia | Université de la Colombie-Britannique | public research university; open-access publisher; university in British Columbia; charitable organization | educational institution | Canada | 1908-01-01 | Vancouver |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:2feb523fd776ea8c",
 "ap_contact_team": {
  "emails": [
   "invoices@emory.edu",
   "invoice@emory.edu",
   "suapayments@emory.edu",
   "sourcingandprocurement@emory.edu",
   "finance@emory.edu",
   "ofaaccounting@emory.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoices@emory.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/paying/vendor-mgmt/invoicing/payment-process.html",
    "quote": "t possible, email all Emory University invoices containing Purchase Orders numbers beginning with A, CH, S, T or W followed by 6 numbers to Invoices@emory.edu. Step 4: Submit the Invoice for Payment The University will pay all valid invoices and/or undisputed amounts of an invoice within t",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Emory University",
    "task_id": "CL-WS-00033"
   },
   {
    "email": "invoice@emory.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/sourcing/supplier-management.html",
    "quote": "ongly encouraged for suppliers to utilize Emory's Supplier Portal or via EDI interface. IF this is not possible, invoices can be emailed to invoice@emory.edu . Please ensure that each: Invoice contains a valid Emory University PO number PDF file contains only one invoice Use of the Emory U",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Emory University",
    "task_id": "CL-WS-00033"
   },
   {
    "email": "invoice@emory.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/_includes/documents/sections/sourcing/procurement-process-guide.pdf",
    "quote": "PO has been received. 3. Once veriﬁed, please be sure to advise the supplier to send the invoice DIRECTLY to you all for processing and NOT invoice@emory.edu once the order has been fulﬁlled. Procurement and Support Services Process Guide | Version 1.1 | Effective: 2026-08| Page 36 4. Once",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Emory University",
    "task_id": "CL-WS-00024"
   },
   {
    "email": "invoice@emory.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/_includes/documents/sections/sourcing/best-procurement-practices-presentation-110125.pdf",
    "quote": "er submits an invoice per a preferred method listed on the PO, which includes via electronically cXML; via supplier portal; or via email to invoice@emory.edu for shipped goods and/or delivered services. • If submitted via email, these invoices will be scanned into the system by our third-p",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Emory University",
    "task_id": "CL-WS-00387"
   },
   {
    "email": "suapayments@emory.edu",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/sourcing/supplier-management.html",
    "quote": "ayment option where suppliers can elect to participate and get paid immediately upon invoice approval.</p><p>If interested, <a href=\"http://suapayments@emory.edu\" rel=\"noopener\" target=\"_blank\">enroll today</a>!</p><h4>Automated Clearing House (ACH)</h4><p><span>Emory offers ACH as a payme",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Emory University",
    "task_id": "CL-WS-00033"
   },
   {
    "email": "sourcingandprocurement@emory.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/sourcing/vendor-selection.html",
    "quote": "nd some purchases paid by federal grant funding, a formal solicitation process is required. In this case, please contact Strategic Sourcing sourcingandprocurement@emory.edu and the assigned Sourcing Manager will work with you. Note: A contract form request within Emory Express will likely",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Emory University",
    "task_id": "CL-SQ-00837"
   },
   {
    "email": "sourcingandprocurement@emory.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.emory.edu/home/procurement/_includes/documents/sections/sourcing/procurement-process-guide.pdf",
    "quote": "th institutional and regulatory requirements. To request Procurement’s support in managing your sourcing event or for any a
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 40)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_sole_source:a75c6b2f7294f7c1 | Environment and Protected Areas | BlueSky Wildfire Smoke Forecasting 2025-2026 | 100000.0 |  |  | https://www.alberta.ca/sole-source-contracts-disclosure-table |
| ca_bc_ministry_awards:d4e81e445205eaaa | Ministry of Health | Health Technology Assessment Resources | 270000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:66ce180545931f02 | Ministry of Forests, Lands, Natural Resource Operations and R.D. | Dothistroma Septosporum DNA Detection | 2500.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_newfoundland:a74d672ade81d78a | Department of Energy and Mines | Dissolution, Trace Elements | 21480.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-September-16-30-Contract-Awards-Report.pdf |
| ca_newfoundland:6b4d0d8d0a4d629d | Industry, Energy and Technology | Analytical Request of Isotopic Chemistry and Interpretation | 77600.0 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2025-01-16-To-2025-01-31-KD-Edits.pdf |
| ca_newfoundland:eace72cee528c032 | Industry, Energy and Technology | Analytical Request for Isotopic Chemistry and Interpretation | 56315.0 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2025-01-16-To-2025-01-31-KD-Edits.pdf |
| ca_newfoundland:b50cf3f0d5d79bb1 | Department of Industry, Energy and Technology | Sample Analysis | 109800.0 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2025-02-01-To-2025-02-15-KD-Edits.pdf |
| ca_newfoundland:a00049082be3e936 | Department of Industry, Energy and Technology | Trace Element Analyses | 72625.0 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2025-03-16-To-2025-03-31.pdf |
| ca_nwt:0000010678 | Education, Culture and Employment | Middle Year Child Development Research and  Reporting | 124025.81 |  |  | https://www.fin.gov.nt.ca/en/resources/contracts-over-5000-report?f%5B0%5D=field_resource_category_legacy%3A582 |
| canada_federal:aafc-aac:3000816405 | Agriculture and Agri-Food Canada | Scientific services | 18367.65 |  |  | https://search.open.canada.ca/contracts/record/aafc-aac,C-2026-2027-Q1-00260 |
| canada_federal:ec:3000804377 | Environment and Climate Change Canada | Scientific consultants | 23000.0 |  |  | https://search.open.canada.ca/contracts/record/ec,C-2025-2026-Q2-00579 |
| canada_federal:dnd-mdn:CW2411943 | National Defence | Engineering consultants-Other | 833060.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q3-06276 |
| canada_federal:dnd-mdn:W6369-27-A058 | National Defence | Tuition fees and costs of attending courses including seminars not elsewhere specified | 85000.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-06870 |
| canada_federal:dnd-mdn:W7707-4503097690 | National Defence | Engineering consultants-Other | 168618.75 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-08019 |
| canada_federal:nrc-cnrc:1025434 | National Research Council Canada | Scientific services | 100000.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2024-2025-Q4-00145 |
| canada_federal:nrc-cnrc:1031816 | National Research Council Canada | Scientific services | 59946.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2025-2026-Q1-00623 |
| canada_federal:nrc-cnrc:1039293 | National Research Council Canada | Scientific services | 50000.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2025-2026-Q4-00590 |
| canada_federal:nrc-cnrc:1040217 | National Research Council Canada | Other business services not elsewhere specified | 75000.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2025-2026-Q4-00784 |
| canada_federal:nrc-cnrc:1040739 | National Research Council Canada | Scientific services | 199450.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2025-2026-Q4-00849 |
| canada_federal:nrc-cnrc:1040840 | National Research Council Canada | Other business services not elsewhere specified | 85000.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2025-2026-Q4-00862 |
| canada_federal:nrc-cnrc:1043026 | National Research Council Canada | Scientific services | 63000.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2026-2027-Q1-00421 |
| canada_federal:nrcan-rncan:3000798187 | Natural Resources Canada | Scientific services | 19550.0 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2025-2026-Q2-00189 |
| canada_federal:nrcan-rncan:3000804543 | Natural Resources Canada | Scientific consultants | 40000.0 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2025-2026-Q2-00179 |
| canada_federal:nrcan-rncan:3000813879 | Natural Resources Canada | Scientific consultants | 25000.0 |  |  | https://search.open.canada.ca/contracts/record/nrcan-rncan,C-2026-2027-Q1-00085 |
| canada_federal:phac-aspc:6D03747461 | Public Health Agency of Canada | Scientific consultants | 267772.33 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2025-2026-Q4-00418 |
| canada_federal:cb:CW2396987 | Department of National Defence (DND) | PGME W6369-22A044-002-ZH |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2396987 |
| canada_federal:cb:CW2437576 | Department of Public Works and Government Services (PSPC) | IDEaS-Contract-CP6-1a-691268 | 168618.75 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2437576 |
| canada_federal:cb:PW-23-01029721 | Natural Resources Canada | Nationwide burn probability mapping, forecasting and inventory polygon segmentation | 75000.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-23-01029721 |
| seao_quebec:686353:university-of-british-columbia | Université McGill | P0003616 | 36015.91 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=07602c8a-fda3-49ed-b79c-445d251cea65 |
| usaspending:CONT_AWD_140G0324P0384_1434_-NONE-_-NONE- | Department of the Interior | SAMPLE PROCESSING RADIOGENIC ISOTOPES | 24930.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_140G0324P0384_1434_-NONE-_-NONE-/ |
| who:202198223 | World Health Organization - Headquarters | Services.Implementation of programmes. | 42667.0 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2019servicesawardedcontracts.pdf?sfvrsn=9d5bdd9a_5&ua=1 |
| worldbank:DS00005:1783076:843314 | Republic of Cabo Verde / Ministry of Culture and Creative Industries and Ministry of the Sea, Ministry of Finance and Business Development, Ministry of Infrastructure,Territorial Planning and Housing, Ministry of Tourism | Consulting Service to the Ministry of the Sea on Climate Change and Marine Fisheries | 215000.0 |  |  | https://projects.worldbank.org/en/projects-operations/project-detail/P176981 |
| ca_canadabuys_contract_history:W7714-217539/001/SV1 | Department of National Defence | UNIVERSITY-INDUSTRY LIAISON OFFICE (W7714-217539/001/SV1~000) | 229080.0 |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:an:PW-15-00710950 | Canadian Space Agency | SPACE EXPLORATION TOPICAL TEAMS | 15000.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-15-00710950 |
| ca_canadabuys_contract_history:an:PW-18-00856769-860387 | Natural Resources Canada | Forest Monitoring and Land Use | 131250.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-18-00856769-860387 |
| ca_canadabuys_contract_history:an:PW-19-00890916-901116 | Fisheries and Oceans Canada | Blue carbon storage capacity of Canada’s eelgrass | 151903.5 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-19-00890916-901116 |
| ca_canadabuys_contract_history:an:PW-21-00970836-980975 | Natural Resources Canada | National Forest Age and Species Products | 94500.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-21-00970836-980975 |
| ca_canadabuys_contract_history:an:PW-22-00996031 | Public Works and Government Services Canada | Product/Material - Design, Development, Formulation, Modification: Science and Technology Related (R&D) (CW2233469)(W7714-228359) | 1150000.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-00996031 |
| ca_canadabuys_contract_history:an:PW-22-00997193 | Public Works and Government Services Canada | Product/Material - Design, Development, Formulation, Modification: Science and Technology Related (R&D) (CW2233794) (W7714-238376) | 1103080.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-00997193 |
| canada_sosa:CW2396987 | Department of National Defence | PGME W6369-22A044-002-ZH |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2396987 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

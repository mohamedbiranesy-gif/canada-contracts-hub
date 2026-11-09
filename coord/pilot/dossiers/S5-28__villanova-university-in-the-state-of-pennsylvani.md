# S5-28 — Villanova University In The State Of Pennsylvania ⇄ THE UNIVERSITY OF BRITISH COLUMBIA

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Villanova University In The State Of Pennsylvania — 789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)
SUBMIT TO: procurement@villanova.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.paymentworks.com/ — PaymentWorks
REFERENCE: contract {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 (reference) | PO rule: purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an
FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public
TAX: tax exempt form, to communicate with the Procurement Department Send check to ____ department, Send check to a (as printed on https://www.villanova.edu/content/ | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Villanova University In The State Of Pennsylvania (government ministry / agency, jurisdiction not stated) — public contract / purchase award | AMOUNT: 8000.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 88
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Villanova University In The State Of Pennsylvania (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): THE UNIVERSITY OF BRITISH COLUMBIA | contract number: {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_in | all identifiers: {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 | value: 8000.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2026-09-14 | published by: subawardee country | record: https://www.usaspending.gov/award/24DG11094200305 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:61b179048aa614fe
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: Villanova University In The State Of Pennsylvania
- **buyer_website**: https://villanova.edu
- **buyer_address**: 299 North Spring Mill Road, Villanova, PA 19085
- **buyer_phone**: 610-519-4500
- **buyer_contact_evidence_url**: https://www.villanova.edu/university/contact-us.html
- **buyer_logo_url**: https://www.villanova.edu/content/dam/villanova/logos/university-main-logo-1.png
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.villanova.edu/university/contact-us.html (tools/org_contacts.py: JSON-LD / contact page; no AI); logo: og:image / logo image of the buyer's site; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the lane's AP page (https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required for Automatic Clearing House (ACH (as printed on https://www.villanova.edu/university/financial-affairs/vendors/vitual-card-program.html, re-read 2026-11-08)
- **buyer_tax_exempt_status**: tax exempt form, to communicate with the Procurement Department Send check to ____ department, Send check to a (as printed on https://www.villanova.edu/content/dam/villanova/finance/documents/procurement/novabuy/NovaPayInvoiceGuideSection123.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: procurement@villanova.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf
- **email_evidence_quote**: All invoices must be sent to the following email address: procurement@villanova.edu
- **email_evidence_context**: or you can contact the PA Department of Revenue. 1099-MISC/REV-1832 The 1099-MISC Withholding Exemption Certificate should be filled out if you are EXEMPT from Pennsylvania's 1099-MISC withholding. Once the form has been completed, please send it to procurement@villanova.edu . Or mail to: Villanova University Procurement Office 789 E. Lancaster Ave. Villanova, PA 19085 Villanova FEIN: 23-1352688 Notices Reporting and Clearance Amendment If any of your employees will be on Villanova campus and have direct contact with mi (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: procurement@villanova.edu (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08 | page: https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf | quote: "All invoices must be sent to the following email address: procurement@villanova.edu" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50078
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=quarantine; rua=mailto:dmarc_agg@vali.email; ruf=mailto:MTE3MDE3@ruf.vali.email
- **dmarc_record_domain**: villanova.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:%{i}._ip.%{h}._ehlo.%{d}._spf.vali.email ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)
- **invoicing_requirements**: Email one invoice copy to procurement@villanova.edu, Adobe or Microsoft Word format, with a minimum 300 DPI for scans. Include unique number, date and supplier remittance address. Match PO invoices line by line. Payment follows agreed terms. Vendors may select virtual card via PaymentWorks.
- **po_required_as_published**: purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)
- **invoice_portal_url**: https://www.paymentworks.com/ — PaymentWorks
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: PaymentWorks (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "portal_url": "https://www.paymentworks.com/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "requirements_text": "Email one invoice copy to procurement@villanova.edu, Adobe or Microsoft Word format, with a minimum 300 DPI for scans. Include unique number, date and supplier remittance address. Match PO invoices line by line. Payment follows agreed terms. Vendors may select virtual card via PaymentWorks."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Villanova University In The State Of Pennsylvania — 789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08) ⏎ SUBMIT TO: procurement@villanova.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.paymentworks.com/ — PaymentWorks ⏎ REFERENCE: contract {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 (reference) | PO rule: purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an ⏎ FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public ⏎ TAX: tax exempt form, to communicate with the Procurement Department Send check to ____ department, Send check to a (as printed on https://www.villanova.edu/content/ | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Villanova University In The State Of Pennsylvania (government ministry / agency, jurisdiction not stated) — public contract / purchase award | AMOUNT: 8000.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Villanova University In The State Of Pennsylvania", "legal_name_is_published": false, "address": "789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "procurement@villanova.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.paymentworks.com/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: PaymentWorks (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"530228UBC\", \"prime_award_internal_id\": \"236495367\", \"Sub-Award ID\": \"530228UBC\
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 74
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published bill-to legal name; published payment terms
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 (reference) — source usaspending

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
- **po_required_as_published**: purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01
- **contract_or_agreement_number**: {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 (reference)
- **contract_value**: 8000.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2026-09-14
- **contract_link**: https://www.usaspending.gov/award/24DG11094200305
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Villanova University In The State Of Pennsylvania — 789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08) ⏎ SUBMIT TO: procurement@villanova.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.paymentworks.com/ — PaymentWorks ⏎ REFERENCE: contract {"internal_id": "530228UBC", "prime_award_internal_id": "236495367", "Sub-Award ID": "530228UBC", "Prime Award ID": "24DG11094200305", "prime_award_generated_internal_id": "ASST_NON_24DG11094200305_01 (reference) | PO rule: purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an ⏎ FROM / REMIT TO: THE UNIVERSITY OF BRITISH COLUMBIA — Vancouver, BC | GST/HST number not public ⏎ TAX: tax exempt form, to communicate with the Procurement Department Send check to ____ department, Send check to a (as printed on https://www.villanova.edu/content/ | CURRENCY: USD (derived from the source's government) | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Villanova University In The State Of Pennsylvania (government ministry / agency, jurisdiction not stated) — public contract / purchase award | AMOUNT: 8000.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Villanova University In The State Of Pennsylvania", "legal_name_is_published": false, "address": "789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "procurement@villanova.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.paymentworks.com/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "789 E. Lancaster Ave. Villanova, PA 19085 (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: PaymentWorks (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) (as printed on https://www.villanova.edu/university/financial-affairs/vendors.html, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"530228UBC\", \"prime_award_internal_id\": \"236495367\", \"Sub-Award ID\": \"530228UBC\
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 74
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published bill-to legal name; published payment terms
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **facts_provenance_json**: {"mailbox": ["procurement@villanova.edu (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08", "page: https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf", "quote: \"All invoices must be sent to the following email address: procurement@villanova.edu\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50078"], "buyer_facts": ["address and phone: the buyer's own site, https://www.villanova.edu/university/contact-us.html (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "logo: og:image / logo image of the buyer's site", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the lane's AP page (https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (subawardee country)"

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.villanova.edu/university/financial-affairs/vendors.html | 2026-11-08 | ok |  | purchase-order terms published (as published: must receive an invitation from Villanova University in order to become an approved Payee within our purchase order) | PaymentWorks |  | 789 E. Lancaster Ave. Villanova, PA 19085 |  |  |  | and companies that already use this system for their vendor management. Payees must receive an invitation from Villanova University in order to become an approved Payee within our purchase order and payment system. This  |

## Buyer site facts (org_extras, villanova.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.villanova.edu/content/dam/villanova/logos/university-main-logo-1.png
- **logo_basis**: logo image in the site header
- **domain**: villanova.edu
- **key**: lead:61b179048aa614fe
- **name**: Villanova University In The State Of Pennsylvania
- **website**: https://villanova.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Villanova University
- **legal_name_stated_url**: https://www.villanova.edu/university/law/about/library.html
- **legal_name_stated_quote**: Library | Charles Widger School of Law | Villanova University Skip to main content VISIT / APPLY / GIVE / X VISIT / APPLY / GIVE / MAIN MENU ABOUT UNIVERSITY LEA
- **mentions**: {'payment_method': {'text': 'interact inside every cell', 'url': 'https://www.villanova.edu/university/engineering/about-us/news-events/villanova-engineer-2026/artificial-made-real.html', 'quote': 'body contains more than 20,000 genes, thousands of proteins and intricate biochemical pathways that interact inside every cell. Any of them can play a role in Alzheimer’s disease. “Our job is to use AI to study how those prote'}}
- **linkedin_url**: https://www.linkedin.com/company/villanovaengineering/
- **tel_links**: 6105194500

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "299 North Spring Mill Road, Villanova, PA 19085", "address_country": "US", "address_url": "https://www.villanova.edu/university/contact-us.html", "address_method": "pattern", "address_quote": "Room 117 Phone: 610-519-4060 Colleges and Schools Charles Widger School of Law 299 North Spring Mill Road Villanova, PA 19085 Phone: 610-519-7000 Email the Law School College of Liberal", "phone": "610-519-4500", "phone_url": "https://www.villanova.edu/university/contact-us.html", "emails": "international@villanova.edu; support@villanova.edu", "emails_url": "https://www.villanova.edu/university/contact-us.html", "domain": "villanova.edu", "key": "lead:61b179048aa614fe", "name": "Villanova University In The State Of Pennsylvania", "website": "https://villanova.edu/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Villanova University In The State Of Pennsylvania |  |  |  |  |  |  |  |  |  |  |
| b | The University Of British Columbia | Q391028 | official website on the organisation's domain (https://www.ubc.ca/) + name | The University of British Columbia [en] | University of British Columbia | Université de la Colombie-Britannique | public research university; open-access publisher; university in British Columbia; charitable organization | educational institution | Canada | 1908-01-01 | Vancouver |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:61b179048aa614fe",
 "ap_contact_team": {
  "emails": [
   "procurement@villanova.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "Email one invoice copy to procurement@villanova.edu, Adobe or Microsoft Word format, with a minimum 300 DPI for scans. Include unique number, date and supplier remittance address. Match PO invoices line by line. Payment follows agreed terms. Vendors may select virtual card via PaymentWorks.",
  "evidence": [
   {
    "email": "procurement@villanova.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Email one invoice copy to procurement@villanova.edu, Adobe or Microsoft Word format, with a minimum 300 DPI for scans. Include unique number, date and supplier remittance address. Match PO invoices line by line. Payment follows agreed terms. Vendors may select virtual card via PaymentWorks.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.villanova.edu/dam/villanova/finance/documents/procurement/Vendors/concur_inv_ltr.pdf",
    "quote": "All invoices must be sent to the following email address: procurement@villanova.edu",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "Villanova University",
    "task_id": "CH-AP-50078"
   },
   {
    "email": "procurement@villanova.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.villanova.edu/university/financial-affairs/vendors.html",
    "quote": "icate should be filled out if you are EXEMPT from Pennsylvania's 1099-MISC withholding. Once the form has been completed, please send it to procurement@villanova.edu . Or mail to: Villanova University Procurement Office 789 E. Lancaster Ave. Villanova, PA 19085 Villanova FEIN: 23-1352688 N",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Villanova University In The State Of Pennsylvania",
    "task_id": "CL-WS-00008"
   },
   {
    "email": "procurement@villanova.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.villanova.edu/university/financial-affairs/procurement.html",
    "quote": "arch Accounting Office Our Staff CONTACT US Visit the Financial Affairs Staff page to meet our Procurement team. Phone: 610-519-4231 Email: procurement@villanova.edu POLICIES & PROCEDURES FORMS YEAR-END GUIDE PLACE A HELP TICKET TRAINING RESOURCES NovaPay (Concur) System Status Updated Vil",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Villanova University In The State Of Pennsylvania",
    "task_id": "CL-WS-00115"
   },
   {
    "email": "procurement@villanova.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.villanova.edu/university/financial-affairs/vendors/honorariums.html",
    "quote": "icate should be filled out if you are EXEMPT from Pennsylvania's 1099-MISC withholding. Once the form has been completed, please send it to procurement@villanova.edu . Or mail to: Villanova University Procurement Office 789 E. Lancaster Ave. Villanova, PA 19085 Villanova FEIN: 23-1352688 N",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Villanova University In The State Of Pennsylvania",
    "task_id": "CL-WS-00128"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site:villanova.edu \"accounts payable\" vendor invoice Villanova University | site:villanova.edu \"invoice\" \"procurement@villanova.edu\" invoices Accounts Payable",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

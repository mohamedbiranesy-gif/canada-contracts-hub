# S5-50 — University Of Florida ⇄ THE GOVERNORS OF THE UNIVERSITY OF CALGARY

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Florida State University Tallahassee, FL — 1400 University Center, Tallahassee, FL 32306-2370
SUBMIT TO: invoices@admin.fsu.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks | format: Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)
REFERENCE: contract {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ (reference) | PO rule: purchase-order terms published (as published: Must Show: The purchase order number)
FROM / REMIT TO: THE GOVERNORS OF THE UNIVERSITY OF CALGARY — 2500 University Dr NW, Calgary, Alberta, T2N 1N4, CA | GST/HST number not public
TAX: Tax-Exempt Status FSU is tax exempt from the payment of all sales, use or excise taxes (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2 | CURRENCY: USD (derived from the source's government) | TERMS: payment terms are net 40 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 202
DESCRIPTION: University Of Florida (org
```

## Relationship
- **rank_group**: L4
- **data_quality_score**: 80
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University Of Florida (organisation (type not stated in the record), jurisdiction not stated) — dated deal or payment 12 to 36 months ago: THE GOVERNORS OF THE UNIVERSITY OF CALGARY | contract number: {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_genera | all identifiers: {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ | value: 165500.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2025-07-07 | published by: subawardee country | record: https://www.usaspending.gov/award/P41HD095831 | vendor in Canada because: subawardee country=CAN | status rule: likely active (awarded 12-36 months ago; record dated 12-36 months ago: subawardee country)
- **how_relationship_was_found**: a dated public record (payment register, subaward, vendor news release or EDC transaction) 12 to 36 months old, harvested by the lead scanners
- **keys**: lead:b34484acf6b4f0c0
- **tier**: L
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: University Of Florida
- **buyer_website**: https://fsu.edu
- **buyer_address**: 1400 University Center, Tallahassee, FL 32306-2370
- **buyer_phone**: 850-644-6850
- **buyer_contact_evidence_url**: https://procurement.fsu.edu/contact-us
- **buyer_legal_name_as_published**: Florida State University Tallahassee, FL
- **buyer_logo_url**: https://www.fsu.edu/themes/custom/fsu_strata/strata-3.3.14/_/s3/img/175/FSU175-logo-horizontal-on-garnet.svg
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q861548; public university; public educational institution of the United States
- **buyer_founded**: 1851-00-00 (Wikidata Q861548, official website on the organisation's domain (https://fsu.edu) + name; 2026-11-08)
- **buyer_employees**: 7273 (Wikidata Q861548, official website on the organisation's domain (https://fsu.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://procurement.fsu.edu/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Preferred) Net 40 via ACH NET 40 via check (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax-Exempt Status FSU is tax exempt from the payment of all sales, use or excise taxes (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoices@admin.fsu.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://procurement.fsu.edu/suppliers-resources
- **email_evidence_quote**: ed otherwise on the purchase order, address all invoices to: Florida State University UCA 5607 University Center Tallahassee, FL 32306-2391 invoices@admin.fsu.edu 850-644-8137 (Fax) Invoices that do not correspond to the purchase order's specifications, that are out of the ordinary, or req
- **email_evidence_context**: to submit a purchase order invoice directly to an individual or the ordering department. Except where stipulated otherwise on the purchase order, address all invoices to: Florida State University UCA 5607 University Center Tallahassee, FL 32306-2391 invoices@admin.fsu.edu 850-644-8137 (Fax) Invoices that do not correspond to the purchase order's specifications, that are out of the ordinary, or require contract interpretation should be referred to the appropriate Procurement Specialist in Procurement Services. Supplie (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoices@admin.fsu.edu (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://procurement.fsu.edu/suppliers-resources | quote: "ed otherwise on the purchase order, address all invoices to: Florida State University UCA 5607 University Center Tallahassee, FL 32306-2391 invoices@admin.fsu.e" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-00554
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:70pgwimc@ag.us.dmarcian.com; ruf=mailto:70pgwimc@fr.us.dmarcian.com
- **dmarc_record_domain**: admin.fsu.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:148.163.149.175 ip4:148.163.152.135 ip4:148.163.145.201 ip4:148.163.141.201 ip4:146.201.107.145 ip4:146.201.107.249 ip4:192.135.64.34 include:spf.protection.outlook.com include:mailgun.org ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 850-644-8137 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **invoicing_requirements**: invoice format as published: Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)
- **payment_terms_as_published**: payment terms are net 40 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: Must Show: The purchase order number) (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **invoice_portal_url**: https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: PaymentWorks (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment terms are net 40 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: Must Show: The purchase order number) (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "portal_url": "https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)", "ap_phone": "850-644-8137 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "requirements_text": "invoice format as published: Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Florida State University Tallahassee, FL — 1400 University Center, Tallahassee, FL 32306-2370 ⏎ SUBMIT TO: invoices@admin.fsu.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks | format: Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08) ⏎ REFERENCE: contract {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ (reference) | PO rule: purchase-order terms published (as published: Must Show: The purchase order number) ⏎ FROM / REMIT TO: THE GOVERNORS OF THE UNIVERSITY OF CALGARY — 2500 University Dr NW, Calgary, Alberta, T2N 1N4, CA | GST/HST number not public ⏎ TAX: Tax-Exempt Status FSU is tax exempt from the payment of all sales, use or excise taxes (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2 | CURRENCY: USD (derived from the source's government) | TERMS: payment terms are net 40 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 202 ⏎ DESCRIPTION: University Of 
- **invoice_card_json**: {"bill_to": {"legal_name": "Florida State University Tallahassee, FL", "legal_name_is_published": true, "address": "1400 University Center, Tallahassee, FL 32306-2370", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@admin.fsu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)", "system": "named on the buyer's page: PaymentWorks (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: Must Show: The purchase order number) (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"SUB00004819-01\", \"prime_award_internal_id\": \"269997601\", \"Sub-Award ID\": \"SUB00004819-01\", \"Prime Award ID\": \"P41HD095831\", \"prime_award_generated_internal_id\": \"ASST_
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ (reference) — source usaspending

## Vendor
- **vendor**: THE GOVERNORS OF THE UNIVERSITY OF CALGARY
- **vendor_address**: 2500 University Dr NW, Calgary, Alberta, T2N 1N4, CA
- **vendor_country_basis**: subawardee country=CAN
- **vendor_website**: https://www.ucalgary.ca/
- **vendor_phone**: 403.220.5460
- **vendor_contact_evidence_url**: https://research.ucalgary.ca/contact
- **vendor_logo_url**: https://ucalgary.ca/themes/ucalgary/ucws_theme/apple-touch-icon.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://ucalgary.ca/about-ucalgary/our-organization/governance-and-leadership (a of oversight, and collaboration, consultation and cooperation are hallmarks of university decision-making. The Board of Governors, General Faculties Council a)
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); phone / role e-mails / logo: the vendor's own site, https://research.ucalgary.ca/contact (tools/org_contacts.py, org_extras.py); website: https://www.ucalgary.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: purchase-order terms published (as published: Must Show: The purchase order number) (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)
- **contract_status**: likely active (awarded 12-36 months ago; record dated 12-36 months ago: subawardee country)
- **contract_reference**: {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_
- **contract_or_agreement_number**: {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ (reference)
- **contract_value**: 165500.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2025-07-07
- **contract_link**: https://www.usaspending.gov/award/P41HD095831
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Florida State University Tallahassee, FL — 1400 University Center, Tallahassee, FL 32306-2370 ⏎ SUBMIT TO: invoices@admin.fsu.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks | format: Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08) ⏎ REFERENCE: contract {"internal_id": "SUB00004819-01", "prime_award_internal_id": "269997601", "Sub-Award ID": "SUB00004819-01", "Prime Award ID": "P41HD095831", "prime_award_generated_internal_id": "ASST_NON_P41HD095831_ (reference) | PO rule: purchase-order terms published (as published: Must Show: The purchase order number) ⏎ FROM / REMIT TO: THE GOVERNORS OF THE UNIVERSITY OF CALGARY — 2500 University Dr NW, Calgary, Alberta, T2N 1N4, CA | GST/HST number not public ⏎ TAX: Tax-Exempt Status FSU is tax exempt from the payment of all sales, use or excise taxes (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2 | CURRENCY: USD (derived from the source's government) | TERMS: payment terms are net 40 (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 202 ⏎ DESCRIPTION: University Of 
- **invoice_card_json**: {"bill_to": {"legal_name": "Florida State University Tallahassee, FL", "legal_name_is_published": true, "address": "1400 University Center, Tallahassee, FL 32306-2370", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@admin.fsu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://procurement.fsu.edu/procurement-resources/frequently-asked-questions/paymentworks-faqs — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "Invoice Generate Invoice You can generate your own PDF invoice on the fly using our Generate Invoice function (as printed on https://studentfinance.fsu.edu/current-students/generate-invoice, re-read 2026-11-08)", "system": "named on the buyer's page: PaymentWorks (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: Must Show: The purchase order number) (as printed on https://procurement.fsu.edu/suppliers-resources, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"SUB00004819-01\", \"prime_award_internal_id\": \"269997601\", \"Sub-Award ID\": \"SUB00004819-01\", \"Prime Award ID\": \"P41HD095831\", \"prime_award_generated_internal_id\": \"ASST_
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["invoices@admin.fsu.edu (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://procurement.fsu.edu/suppliers-resources", "quote: \"ed otherwise on the purchase order, address all invoices to: Florida State University UCA 5607 University Center Tallahassee, FL 32306-2391 invoices@admin.fsu.e\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-00554"], "buyer_facts": ["address and phone: the buyer's own site, https://procurement.fsu.edu/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://procurement.fsu.edu/suppliers-resources | 2026-11-08 | ok | payment terms are net 40 | purchase-order terms published (as published: Must Show: The purchase order number) | PaymentWorks | 850-644-8137 |  |  |  | University Billing amount Payment Terms Unless otherwise noted in the solicitation document, contract, or purchase order, FSU’s standard payment terms are net 40 from receipt of the invoice, goods received, or services p | between the hours of 8:00 and 4:30 p.m., Monday through Friday (except University holidays). All Packages Must Show: The purchase order number. The department name/"attention to" name. Room number/location if stated on t |

## Buyer site facts (org_extras, fsu.edu)
- **status**: ok
- **pages**: 3
- **language**: en
- **legal_name**: Florida State University Tallahassee, FL
- **legal_name_url**: https://www.fsu.edu/
- **legal_name_quote**: ccurately reflect the current status of all programs. We intend to have websites updated shortly. © Florida State University Tallahassee, FL 32306 FSU Directory Assistance Questions or Comments Privacy Policy Copyright Like Florida State on
- **logo_url**: https://www.fsu.edu/themes/custom/fsu_strata/strata-3.3.14/_/s3/img/175/FSU175-logo-horizontal-on-garnet.svg
- **logo_basis**: logo image in the site header
- **domain**: fsu.edu
- **key**: lead:b34484acf6b4f0c0
- **name**: University Of Florida
- **website**: https://fsu.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: State University
- **legal_name_stated_url**: https://www.fsu.edu/about
- **legal_name_stated_quote**: About FSU | Florida State University Skip to main content FSU | Florida State University Webmail Search FSU Navigation FSU Sites Faculty

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1400 University Center, Tallahassee, FL 32306-2370", "address_country": "US", "address_url": "https://procurement.fsu.edu/contact-us", "address_method": "pattern", "address_quote": "e: https://procurement.fsu.edu/how/buy/contacts-commodity Procurement Services A1400 University Center Tallahassee, FL 32306-2370 Location Map Email: procurement@fsu.edu Phone: 850-6", "phone": "850-644-6850", "phone_url": "https://procurement.fsu.edu/contact-us", "emails": "procurement@fsu.edu", "emails_url": "https://procurement.fsu.edu/contact-us", "domain": "fsu.edu", "key": "lead:b34484acf6b4f0c0", "name": "University Of Florida", "website": "https://procurement.fsu.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, ucalgary.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **domain**: ucalgary.ca
- **key**: b:7c93f114a648ffff
- **name**: University of Calgary
- **website**: https://ucalgary.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University
- **legal_name_stated_url**: https://ucalgary.ca/
- **legal_name_stated_quote**: University of Calgary Skip to main content Search Toggle Toolbox Search My UCalgary Webmail UCalgary Support D
- **linkedin_url**: https://www.linkedin.com/company/university-of-calgary
- **tel_links**: 403.220.8261
- **logo_url**: https://ucalgary.ca/themes/ucalgary/ucws_theme/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **bn**: 108102864
- **bn_program**: RR0001
- **bn_label**: Charitable registration #: 10810 2864 RR
- **bn_url**: https://www.ucalgary.ca/giving/ways-give
- **bn_quote**: raise a dollar well below the industry standard at $0.12 for every dollar raised. Giving Contact us Charitable registration #: 10810 2864 RR0001 403.220.8261 give@ucalgary.ca Website Terms & Conditions Privacy Policy Website feedback University

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "2500 University Drive NW, Calgary, AB, T2N 1N4", "address_country": "CA", "address_url": "https://research.ucalgary.ca/contact", "address_method": "pattern", "address_quote": "ing Address A100, Administration Building 2500 University Drive NW Calgary, AB, T2N 1N4 View location on campus map UCalgary parking information Participate in Researc", "phone": "403.220.5460", "phone_url": "https://research.ucalgary.ca/contact", "domain": "ucalgary.ca", "key": "vd:ucalgary.ca", "name": "Alberta Gambling Research Institute", "website": "https://research.ucalgary.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of Calgary | Q1067471 | official website on the organisation's domain (http://www.ucalgary.ca/) + name |  | University of Calgary | Université de Calgary | autonomous university; comprehensive academic and research university; open-access publisher; public research university; charitable organization |  | Canada | 1966-00-00 | Calgary |
| b | University Of Florida | Q861548 | official website on the organisation's domain (https://fsu.edu) + name |  | Florida State University | Université d'État de Floride | public university; public educational institution of the United States |  | United States | 1851-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b34484acf6b4f0c0",
 "ap_contact_team": {
  "emails": [
   "invoices@admin.fsu.edu",
   "financialaid@fsu.edu",
   "procurement@fsu.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoices@admin.fsu.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://procurement.fsu.edu/suppliers-resources",
    "quote": "ed otherwise on the purchase order, address all invoices to: Florida State University UCA 5607 University Center Tallahassee, FL 32306-2391 invoices@admin.fsu.edu 850-644-8137 (Fax) Invoices that do not correspond to the purchase order's specifications, that are out of the ordinary, or req",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of Florida",
    "task_id": "CL-LD-00554"
   },
   {
    "email": "financialaid@fsu.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://financialaid.fsu.edu/office-financial-aid-staff",
    "quote": "539 Fax: (850) 644-6404 Address: Office of Financial Aid Suite 4400A University Center Tallahassee, FL 32306-2430 Email: General questions: financialaid@fsu.edu Work Study questions:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of Florida",
    "task_id": "CL-LD-00554"
   },
   {
    "email": "procurement@fsu.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://procurement.fsu.edu/",
    "quote": "related to fiscal close transactions. View all Procurement Services A1400 University Center Tallahassee, FL 32306-2370 Location Map Email: procurement@fsu.edu Phone: 850-644-6850 Fax: 850-644-8921 M-F, 8am-5pm © Florida State University Tallahassee, FL 32306 FSU Directory Assistance Quest",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of Florida",
    "task_id": "CL-LD-00554"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of fsu.edu (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of fsu.edu (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of fsu.edu (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 16)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_sole_source:bf3e561d161b0283 | Environment and Protected Areas | Laboratory Analysis of Algal Toxins | 24000.0 |  |  | https://www.alberta.ca/sole-source-contracts-disclosure-table |
| ca_alberta_sole_source:5a1ea443db7f4ad2 | Primary and Preventative Health Services | To contribute to the fulfillment of the stewardship priority area for action under the Antimicrobial Resistance (AMR) Framework. | 730000.0 |  |  | https://www.alberta.ca/sole-source-contracts-disclosure-table |
| canada_federal:csa-asc:CW2376400 | Canadian Space Agency | Scientific consultants | 562559.2 |  |  | https://search.open.canada.ca/contracts/record/csa-asc,C-2024-2025-Q3-00081 |
| canada_federal:phac-aspc:4600002583 | Public Health Agency of Canada | Scientific consultants | 20803694.51 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2024-2025-Q2-00490 |
| canada_federal:phac-aspc:4500487851 | Public Health Agency of Canada | Other professional services not otherwise specified | 20051.6 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2025-2026-Q4-00589 |
| canada_federal:phac-aspc:6D0378131B | Public Health Agency of Canada | Other business services not elsewhere specified | 86635.65 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2026-2027-Q1-00366 |
| canada_federal:cb:CW2438611 | Public Health Agency of Canada (PHAC) | 6D037-248131-002-SL - CANADIAN NOSOCOMIAL INFECTION SURVEILLANCE PROGRAM (CNISP) | 86635.65 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2438611 |
| canada_federal:cb:CW2439246 | Department of National Defence (DND) | IDEaS-Contract-CP6-1a-691064 | 284050.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2439246 |
| canada_federal:cb:CW2452824 | Defence Research and Development Canada (DRDC) | W7707-267416-Development of a Color Change-based Chemical Agent Disclosure System | 74779.74 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2452824 |
| canada_federal:cb:CW2467297 | Department of National Defence (DND) | W8703-270055 Defence Drone Initiative (DDI) Marketplace SA 391 | 1.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2467297 |
| canada_federal:cb:PW-22-01008386 | Public Works and Government Services Canada | Product/Material - Design, Development, Formulation, Modification: Science and Technology Related (R&D) (CW2238737)(W7714-238436) | 1133612.5 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-01008386 |
| usaspending:CONT_AWD_75F40126C00212_7524_-NONE-_-NONE- | Department of Health and Human Services | EO 14398 - REGULATORY SCIENCE TOOL FOR TRANSCRANIAL ULTRASOUND MODELING | 345837.15 |  |  | https://www.usaspending.gov/award/CONT_AWD_75F40126C00212_7524_-NONE-_-NONE-/ |
| usaspending:sub:CONT_AWD_75N93022C00035_7529_-NONE-_-NONE-:60062907 CAL BASE OP3:XC87G4J7F7M8 | NORTHWESTERN UNIVERSITY | CENTERS FOR RESEARCH ON STRUCTURAL BIOLOGY OF INFECTIOUS DISEASES | 305437.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_75N93022C00035_7529_-NONE-_-NONE-/ |
| usaspending:sub:CONT_AWD_75N93022C00035_7529_-NONE-_-NONE-:60062907 CAL BASE OP4 (SP0071158:XC87G4J7F7M8 | NORTHWESTERN UNIVERSITY | CENTERS FOR RESEARCH ON STRUCTURAL BIOLOGY OF INFECTIOUS DISEASES | 313806.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_75N93022C00035_7529_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:W7714-196729/001/SV | Department of National Defence | RESEARCH SERVICES (W7714-196729/001/SV~000) | 199925.0 |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:an:PW-15-00710953 | Canadian Space Agency | SPACE EXPLORATION TOPICAL TEAMS | 14990.1 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-15-00710953 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

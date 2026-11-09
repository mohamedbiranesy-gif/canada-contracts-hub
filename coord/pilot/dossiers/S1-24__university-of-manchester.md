# S1-24 — University of Manchester ⇄ Droplet Lab

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/) — The University of Manchester, Oxford Road, Manchester, M13 9PL, UK
SUBMIT TO: supplier.invoices@manchester.ac.uk (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: yes (as published: no purchase order, no pay)
FROM / REMIT TO: Droplet Smart Tech Inc. (Wikidata Q141630318, exact name match + country + organisation claims; 2026-11-08) — Brampton (headquarters per Wikidata Q141630318; not the registered address) | GST/HST 781803929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2025-04-21; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/su
DESCRIPTION: University of Manchester: Titaniu
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University of Manchester (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Droplet Lab | subject: University of Manchester: Titanium Implant Contact Angle | awarded 2026-10-28 | published by: customer story published by the vendor (dated) | record: https://dropletlab.com/validation/case-studies/university-of-manchester-titanium-implant-contact-angle/ | vendor in Canada because: customer story published by the vendor (dated)=es Buying Guides Company About Us Contact Us 98 Major Wm Sharpe Dr Brampton, ON L6X 3V1 VISIT US 647-490-46 | status rule: likely active (record dated in the last 12 months: customer story published by the vendor (dated))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:164c3407fe4619bb
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: customer story published by the vendor (dated); 0 in the contract dataset)

## Buyer
- **buyer**: University of Manchester
- **buyer_website**: https://manchester.ac.uk/
- **buyer_address**: The University of Manchester, Oxford Road, Manchester, M13 9PL, UK
- **buyer_phone**: +44 (0) 161 306 6000
- **buyer_contact_evidence_url**: https://www.manchester.ac.uk/connect/contact-us/
- **buyer_legal_name_as_published**: University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/)
- **buyer_logo_url**: https://assets.manchester.ac.uk/corporate/images/design/logo-university-of-manchester.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/university-of-manchester/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q230899; university; open-access publisher; educational organization
- **buyer_founded**: 1824-00-00; 2004-00-00 (Wikidata Q230899, official website on the organisation's domain (https://manchester.ac.uk) + name; 2026-11-08)
- **buyer_legal_form**: royal charter company (Wikidata Q230899, official website on the organisation's domain (https://manchester.ac.uk) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.manchester.ac.uk/connect/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the lane's AP page (https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: supplier.invoices@manchester.ac.uk
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/
- **email_evidence_quote**: order is at your own risk. Prior to dispatching goods please check that an order is legitimate . Invoices must be send in a .pdf format to supplier.invoices@manchester.ac.uk or to The University of Manchester, Accounts Payable Office, John Owens Building, Oxford Road, Manchester, M13 9PL.
- **email_evidence_context**: The University operates a ‘no purchase order, no pay’ system and any work undertaken without a valid purchase order is at your own risk. Prior to dispatching goods please check that an order is legitimate . Invoices must be send in a .pdf format to supplier.invoices@manchester.ac.uk or to The University of Manchester, Accounts Payable Office, John Owens Building, Oxford Road, Manchester, M13 9PL. Our standard payment terms are within 30 days of receipt of a valid invoice (quoting a legitimate University purchase order number) w (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: supplier.invoices@manchester.ac.uk (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02 | page: https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/ | quote: "order is at your own risk. Prior to dispatching goods please check that an order is legitimate . Invoices must be send in a .pdf format to supplier.invoices@man" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00013
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com,mailto:dmarc-rua@dmarc.service.gov.uk; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com;
- **dmarc_record_domain**: manchester.ac.uk
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:%{ir}.%{v}.%{d}.spf.has.pphosted.com include:servers.ebsnd.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: John Owe (as printed by the organisation next to its invoicing mailbox)
- **invoicing_requirements**: invoice format as published: pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)
- **payment_terms_as_published**: payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "po_required": "yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "invoice_format": "pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "requirements_text": "invoice format as published: pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)"}
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/) — The University of Manchester, Oxford Road, Manchester, M13 9PL, UK ⏎ SUBMIT TO: supplier.invoices@manchester.ac.uk (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: no purchase order, no pay) ⏎ FROM / REMIT TO: Droplet Smart Tech Inc. (Wikidata Q141630318, exact name match + country + organisation claims; 2026-11-08) — Brampton (headquarters per Wikidata Q141630318; not the registered address) | GST/HST 781803929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2025-04-21; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/su ⏎ DESCRIPTION: University of Manches
- **invoice_card_json**: {"bill_to": {"legal_name": "University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/)", "legal_name_is_published": true, "address": "The University of Manchester, Oxford Road, Manchester, M13 9PL, UK", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "supplier.invoices@manchester.ac.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08))"}, "terms": {"payment_terms": "payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "payment_method": "", 
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08))

## Vendor
- **vendor**: Droplet Lab
- **vendor_legal_name**: Droplet Smart Tech Inc. (Wikidata Q141630318, exact name match + country + organisation claims; 2026-11-08)
- **vendor_address**: Brampton (headquarters per Wikidata Q141630318; not the registered address)
- **vendor_country_basis**: customer story published by the vendor (dated)=es Buying Guides Company About Us Contact Us 98 Major Wm Sharpe Dr Brampton, ON L6X 3V1 VISIT US 647-490-46
- **vendor_bn9**: 781803929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2025-04-21; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 781803929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://dropletlab.com
- **vendor_emails**: info@dropletlab.com; support@dropletlab.com
- **vendor_phone**: +1-647-490-4644
- **vendor_contact_evidence_url**: https://dropletlab.com/company/contact/
- **vendor_logo_url**: https://dropletlab.com/wp-content/uploads/2025/05/Droplet-Lab3-1.png
- **vendor_facts_provenance**: name and address: the record's vendor block (customer story published by the vendor (dated)); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://dropletlab.com/company/contact/ (tools/org_contacts.py, org_extras.py); website: https://dropletlab.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q141630318; business
- **vendor_founded**: 2016-00-00 (Wikidata Q141630318, exact name match + country + organisation claims; 2026-11-08)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **po_required_as_published**: yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: customer story published by the vendor (dated))
- **contract_title**: University of Manchester: Titanium Implant Contact Angle
- **contract_description**: University of Manchester: Titanium Implant Contact Angle (the record's title; the source publishes no separate description)
- **award_date**: 2026-10-28
- **contract_link**: https://dropletlab.com/validation/case-studies/university-of-manchester-titanium-implant-contact-angle/
- **source**: customer story published by the vendor (dated)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: customer story published by the vendor (dated); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: GBP (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 781803929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/) — The University of Manchester, Oxford Road, Manchester, M13 9PL, UK ⏎ SUBMIT TO: supplier.invoices@manchester.ac.uk (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: no purchase order, no pay) ⏎ FROM / REMIT TO: Droplet Smart Tech Inc. (Wikidata Q141630318, exact name match + country + organisation claims; 2026-11-08) — Brampton (headquarters per Wikidata Q141630318; not the registered address) | GST/HST 781803929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2025-04-21; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: DERIVED: GBP (derived from the buyer's country; C | TERMS: payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/su ⏎ DESCRIPTION: University of Manches
- **invoice_card_json**: {"bill_to": {"legal_name": "University (stated on https://www.manchester.ac.uk/study/student-terms-and-conditions/)", "legal_name_is_published": true, "address": "The University of Manchester, Oxford Road, Manchester, M13 9PL, UK", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "supplier.invoices@manchester.ac.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "pdf format (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: no purchase order, no pay) (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08))"}, "terms": {"payment_terms": "payment terms are within 30 days (as printed on https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/, re-read 2026-11-08)", "payment_method": "", 
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["supplier.invoices@manchester.ac.uk (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02", "page: https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/", "quote: \"order is at your own risk. Prior to dispatching goods please check that an order is legitimate . Invoices must be send in a .pdf format to supplier.invoices@man\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00013"], "buyer_facts": ["address and phone: the buyer's own site, https://www.manchester.ac.uk/connect/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the lane's AP page (http

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/ | 2026-11-08 | ok | payment terms are within 30 days | yes (as published: no purchase order, no pay) |  |  |  | pdf format |  | or to The University of Manchester, Accounts Payable Office, John Owens Building, Oxford Road, Manchester, M13 9PL. Our standard payment terms are within 30 days of receipt of a valid invoice (quoting a legitimate Univer | is committed to dealing fairly and equitably with its suppliers including payment of valid invoices. The University operates a ‘no purchase order, no pay’ system and any work undertaken without a valid purchase order is  |

## Buyer site facts (org_extras, manchester.ac.uk)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://assets.manchester.ac.uk/corporate/images/design/logo-university-of-manchester.png
- **logo_basis**: logo image in the site header
- **domain**: manchester.ac.uk
- **key**: lead:164c3407fe4619bb
- **name**: University of Manchester
- **website**: https://manchester.ac.uk/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University
- **legal_name_stated_url**: https://www.manchester.ac.uk/study/student-terms-and-conditions/
- **legal_name_stated_quote**: Student terms and conditions | The University of Manchester Skip to navigation | Skip to main content | Skip to footer Home Study Undergraduate U
- **mentions**: {'payment_method': {'text': 'interaction with children and working with adults in regulated activity (courses where', 'url': 'https://www.manchester.ac.uk/study/student-terms-and-conditions/', 'quote': 'courses, for example, teaching, health, social work, pharmacy and others where studies necessitate interaction with children and working with adults in regulated activity (courses where a Disclosure and Barring Service (DBS) record check is required), applica'}}
- **linkedin_url**: https://www.linkedin.com/school/university-of-manchester/
- **tel_links**: +441613066000

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "The University of Manchester, Oxford Road, Manchester, M13 9PL, UK", "address_country": "GB", "address_url": "https://www.manchester.ac.uk/connect/contact-us/", "address_method": "address-tag", "address_quote": "Contact The University of Manchester Skip to navigation | Skip to main content | Skip to footer Home Study Undergrad", "phone": "+44 (0) 161 306 6000", "phone_url": "https://www.manchester.ac.uk/connect/contact-us/", "emails": "international@manchester.ac.uk", "emails_url": "https://www.manchester.ac.uk/study/postgraduate-research/contact/", "domain": "manchester.ac.uk", "key": "lead:164c3407fe4619bb", "name": "University of Manchester", "website": "https://manchester.ac.uk/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, dropletlab.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://dropletlab.com/wp-content/uploads/2025/05/Droplet-Lab3-1.png
- **logo_basis**: logo image in the site header
- **domain**: dropletlab.com
- **key**: wd:Q141630318
- **name**: Droplet Lab
- **website**: https://dropletlab.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Droplet Lab
- **jsonld_legal_name**: Droplet Smart Tech Inc.
- **jsonld_alternate_name**: Droplet Smart Tech Inc.; DropletLab
- **jsonld_address**: 98 Major Wm Sharpe Dr, Brampton, ON, L6X 3V1, CA
- **jsonld_phone**: +1-647-490-4644
- **jsonld_email**: info@dropletlab.com
- **jsonld_url**: https://dropletlab.com/
- **jsonld_founding_date**: 2016-02-25
- **jsonld_naics**: 334516
- **jsonld_employees**: 6
- **jsonld_same_as**: https://www.linkedin.com/company/droplet-lab; https://www.youtube.com/@dropletlab; https://twitter.com/dropletlab
- **jsonld_quote**: {"@context":"https://schema.org","@type":"Review","reviewBody":"We’re in the 21st century. 3D printing, excellent digital microscopes, fast control software and mobile computing make it possible to combine precision with affordability. It’s great that Droplet Labs have transformed this important tec
- **jsonld_page**: https://dropletlab.com/
- **legal_name_stated**: York University
- **legal_name_stated_url**: https://dropletlab.com/company/about/
- **legal_name_stated_quote**: eep Saini MSc Chief Of Operations Holds a BASc in Mechanical Engineering (Ryerson) and an MASc from York University. He develops the automatic edge and baseline detection behind the Dropometer's analysis. Pratik Saw
- **mentions**: {'payment_method': {'text': 'interactions or contractual relationship with us', 'url': 'https://dropletlab.com/legal/privacy-policy/', 'quote': 'k your permission to send you marketing information, or sometimes your consent is implied from your interactions or contractual relationship with us. Where your consent is implied, it is on the basis that you would have a reasonable expectation of'}}
- **linkedin_url**: https://www.linkedin.com/company/droplet-lab
- **tel_links**: 647-490-4644

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "98 Major Wm Sharpe Dr, Brampton, ON, L6X 3V1", "address_country": "CA", "address_url": "https://dropletlab.com/company/contact/", "address_method": "json-ld", "address_quote": "es Buying Guides Company About Us Contact Us 98 Major Wm Sharpe Dr Brampton, ON L6X 3V1 VISIT US 647-490-4644 Call Us [email protected] Email Us Working Hours Working", "phone": "+1-647-490-4644", "phone_url": "https://dropletlab.com/company/contact/", "emails": "info@dropletlab.com; support@dropletlab.com", "emails_url": "https://dropletlab.com/company/contact/", "domain": "dropletlab.com", "key": "vd:dropletlab.com", "name": "Droplet Lab", "website": "https://dropletlab.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of Manchester | Q230899 | official website on the organisation's domain (https://manchester.ac.uk) + name |  | University of Manchester | Université de Manchester | university; open-access publisher; educational organization | royal charter company | United Kingdom | 1824-00-00; 2004-00-00 | Manchester |
| b | Droplet Lab | Q141630318 | official website on the organisation's domain (https://dropletlab.com) + name | Droplet Smart Tech Inc. [en] | Droplet Lab |  | business |  | Canada | 2016-00-00 | Brampton |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:164c3407fe4619bb",
 "ap_contact_team": {
  "emails": [
   "supplier.invoices@manchester.ac.uk",
   "ap-helpdesk@manchester.ac.uk",
   "humanities.finance@manchester.ac.uk"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "supplier.invoices@manchester.ac.uk",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/",
    "quote": "order is at your own risk. Prior to dispatching goods please check that an order is legitimate . Invoices must be send in a .pdf format to supplier.invoices@manchester.ac.uk or to The University of Manchester, Accounts Payable Office, John Owens Building, Oxford Road, Manchester, M13 9PL.",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Manchester",
    "task_id": "CL-WS-00013"
   },
   {
    "email": "ap-helpdesk@manchester.ac.uk",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://documents.manchester.ac.uk/DocuInfo.aspx?DocID=37938",
    "quote": "ue and the form will adjust automatically Type: Form Owner: Directorate of Finance This document requires CAS authentication Contact email: ap-helpdesk@manchester.ac.uk Last modified: 12/08/2026 Link to this document: https://documents.manchester.ac.uk/display.aspx?DocID=37938 Edit (only A",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Manchester",
    "task_id": "CL-WS-00013"
   },
   {
    "email": "humanities.finance@manchester.ac.uk",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.staffnet.manchester.ac.uk/seed/resources/finance-faqs/",
    "quote": ". For all other school budget codes (including task codes associated with budgets beginning with P) please contact humanities.finance@manchester.ac.uk . For budgets outside SEED contact finance.helpdesk@manches",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Manchester",
    "task_id": "CL-WS-00013"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**The buyer's invoicing rule, in full.** "Payment and invoicing", https://www.staffnet.manchester.ac.uk/procurement/supplying/payment-and-invoicing/:
"no purchase order, no pay" system (work without a valid PO at the supplier's own risk); invoices as PDF to supplier.invoices@manchester.ac.uk; postal
option "The University of Manchester, Accounts Payable Office", John Owens Building, Oxford Road, Manchester, M13 9PL; invoice must quote "a legitimate
University purchase order number"; terms "within 30 days of receipt of a valid invoice"; "payment usually made through the BACS system". Terms and
Conditions of Purchase (April 2024): https://documents.manchester.ac.uk/display.aspx?DocID=15179; Procurement Policy (July 2026):
https://documents.manchester.ac.uk/display.aspx?DocID=79637; Supplier Set-Up Form: https://documents.manchester.ac.uk/display.aspx?DocID=3998 (the vendor
must be set up — bank details — before the first payment). → Droplet Lab: GBP invoice, PO number mandatory, zero-rated for Canadian GST (export).

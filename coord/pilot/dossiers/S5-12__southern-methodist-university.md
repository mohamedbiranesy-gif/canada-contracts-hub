# S5-12 — Southern Methodist University ⇄ Evertz

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps) — 6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/)
SUBMIT TO: invoices@smu.edu (invoicing/AP mailbox, confirmed by the referee) | format: PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required to have an approved contract or purchase order)
FROM / REMIT TO: Evertz — 5292 John Lucas Dr, Burlington, Ontario, L7L 5Z9, CA | GST/HST number not public
TAX: Tax Exemption Certificates should be completed and submitted for in-state hotel accommodations (as printed on https://www.smu.edu/businessfinance/officeoffinanc | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: Net30 (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/
DESCRIPTION: Southern Methodist University Case Study | Solutions by Application
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 73
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Southern Methodist University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Evertz | subject: Southern Methodist University Case Study | Solutions by Application | published by: the Canada-located vendor's own website | record: https://evertz.com/applications/sdvn/case-studies/southern-methodist-university/ | vendor in Canada because: vendor located in Canada (stories; v)=evertz.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:626f4f8d08c6d427
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Southern Methodist University
- **buyer_website**: https://www.smu.edu/
- **buyer_address**: 6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/)
- **buyer_phone**: 214-768-2000
- **buyer_contact_evidence_url**: https://www.smu.edu/aboutsmu/contactsmu
- **buyer_legal_name_as_published**: Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps)
- **buyer_logo_url**: https://www.smu.edu/-/media/Site/DevelopmentExternalAffairs/MarketingCommunications/digital-marketing/dallas-hall-sunset.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/smudallas/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1536258; private university; private not-for-profit educational institution
- **buyer_founded**: 1911-00-00 (Wikidata Q1536258, official website on the organisation's domain (https://www.smu.edu/) + name; 2026-11-08)
- **buyer_employees**: 2831 (Wikidata Q1536258, official website on the organisation's domain (https://www.smu.edu/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.smu.edu/aboutsmu/contactsmu (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Direct deposit is the mandatory (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/general-policies, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax Exemption Certificates should be completed and submitted for in-state hotel accommodations (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: Docusign for approval (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoices@smu.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions
- **email_evidence_quote**: e fully approved, it will be processed for payment. If you receive a vendor’s invoice within the department, please forward that invoice to invoices@smu.edu . Please ask the vendor to send directly to Accounts Payable going forward. Any non-invoice should be accompanied by a payment reques
- **email_evidence_context**: e to be processed through Docusign for approval. Vendors should include this information on their invoice. Once fully approved, it will be processed for payment. If you receive a vendor’s invoice within the department, please forward that invoice to invoices@smu.edu . Please ask the vendor to send directly to Accounts Payable going forward. Any non-invoice should be accompanied by a payment request form . It should also be sent to invoices@smu.edu for approval routing and processing. It may be sent to the appro (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoices@smu.edu (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions | quote: "e fully approved, it will be processed for payment. If you receive a vendor’s invoice within the department, please forward that invoice to invoices@smu.edu . P" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-47058
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; fo=1; ri=3600; rua=mailto:postmaster@smu.edu; ruf=mailto:postmaster@smu.edu
- **dmarc_record_domain**: smu.edu
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Elizabeth Reyes Lead (Accounts Payable Team Lead) (as printed by the organisation on its own accounts-payable page (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable, re-read 2026-11-08))
- **invoicing_requirements**: invoice format as published: PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)
- **payment_terms_as_published**: Net30 (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/other-relevant-policies, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "Net30 (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/other-relevant-policies, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)", "invoice_format": "PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)", "requirements_text": "invoice format as published: PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps) — 6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/) ⏎ SUBMIT TO: invoices@smu.edu (invoicing/AP mailbox, confirmed by the referee) | format: PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required to have an approved contract or purchase order) ⏎ FROM / REMIT TO: Evertz — 5292 John Lucas Dr, Burlington, Ontario, L7L 5Z9, CA | GST/HST number not public ⏎ TAX: Tax Exemption Certificates should be completed and submitted for in-state hotel accommodations (as printed on https://www.smu.edu/businessfinance/officeoffinanc | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: Net30 (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/ ⏎ DESCRIPTION: Southern Methodist University Case Study | Solutions by Application
- **invoice_card_json**: {"bill_to": {"legal_name": "Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps)", "legal_name_is_published": true, "address": "6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@smu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "https://www.smu.edu/-/media/site/businessfinance/controllers/ap-forms/direct-deposit-form-for-smu-employees-may-2025.pdf", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required to have an approved contract or purchase order) (as pr
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **supplier_setup_url**: https://www.smu.edu/-/media/site/businessfinance/controllers/ap-forms/direct-deposit-form-for-smu-employees-may-2025.pdf (linked as "direct deposit form" (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/payment-processing, re-read 2026-11-08))
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/fre)

## Vendor
- **vendor**: Evertz
- **vendor_address**: 5292 John Lucas Dr, Burlington, Ontario, L7L 5Z9, CA
- **vendor_country_basis**: vendor located in Canada (stories; v)=evertz.com
- **vendor_website**: https://evertz.com/
- **vendor_phone**: +1 905-335-3700
- **vendor_contact_evidence_url**: https://evertz.com/contact/
- **vendor_logo_url**: https://evertz.com/img/evertz/evertz.logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/evertz
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://evertz.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://evertz.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q5417421; business; public company
- **vendor_founded**: 1996-00-00; 1966-00-00 (Wikidata Q5417421, official website on the organisation's domain (http://www.evertz.com) + name; 2026-11-08)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Southern Methodist University Case Study | Solutions by Application
- **contract_description**: Southern Methodist University Case Study | Solutions by Application (the record's title; the source publishes no separate description)
- **contract_link**: https://evertz.com/applications/sdvn/case-studies/southern-methodist-university/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps) — 6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/) ⏎ SUBMIT TO: invoices@smu.edu (invoicing/AP mailbox, confirmed by the referee) | format: PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required to have an approved contract or purchase order) ⏎ FROM / REMIT TO: Evertz — 5292 John Lucas Dr, Burlington, Ontario, L7L 5Z9, CA | GST/HST number not public ⏎ TAX: Tax Exemption Certificates should be completed and submitted for in-state hotel accommodations (as printed on https://www.smu.edu/businessfinance/officeoffinanc | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: Net30 (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/ ⏎ DESCRIPTION: Southern Methodist University Case Study | Solutions by Application
- **invoice_card_json**: {"bill_to": {"legal_name": "Southern Methodist University (stated on https://www.smu.edu/aboutsmu/maps)", "legal_name_is_published": true, "address": "6425 Boaz Lane, Dallas, TX, 75205, US (schema.org JSON-LD PostalAddress on https://www.smu.edu/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@smu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "https://www.smu.edu/-/media/site/businessfinance/controllers/ap-forms/direct-deposit-form-for-smu-employees-may-2025.pdf", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF attachment (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/appoliciesprocedures/invoice-handling, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: required to have an approved contract or purchase order) (as printed on https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required to have an approved contract or purchase order) (as pr
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["invoices@smu.edu (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions", "quote: \"e fully approved, it will be processed for payment. If you receive a vendor’s invoice within the department, please forward that invoice to invoices@smu.edu . P\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-47058"], "buyer_facts": ["address and phone: the buyer's own site, https://www.smu.edu/aboutsmu/contactsmu (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions | 2026-11-08 | ok |  | purchase-order terms published (as published: required to have an approved contract or purchase order) |  |  |  |  |  |  | on file. If not, payment will be delayed until that approval is obtained. Requests for payments greater than $5000 are required to have an approved contract or purchase order. When payment requests are not submitted with |

## Buyer site facts (org_extras, smu.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.smu.edu/-/media/Site/DevelopmentExternalAffairs/MarketingCommunications/digital-marketing/dallas-hall-sunset.png
- **logo_basis**: og:image of the home page
- **domain**: smu.edu
- **key**: lead:626f4f8d08c6d427
- **name**: Southern Methodist University
- **website**: https://smu.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: CollegeOrUniversity
- **jsonld_name**: Southern Methodist University
- **jsonld_alternate_name**: SMU
- **jsonld_address**: 6425 Boaz Lane, Dallas, TX, 75205, US
- **jsonld_logo**: https://www.smu.edu/assets/images/smu-logo.png
- **jsonld_url**: https://www.smu.edu/
- **jsonld_same_as**: https://www.facebook.com/smudallas/; https://x.com/SMU; https://www.instagram.com/smudallas/; https://www.linkedin.com/school/smudallas/; https://www.youtube.com/@SMUdallas
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "WebPage", "url": "https://www.smu.edu/", "name": "Southern Methodist University", "description": "Discover world-class education at SMU in Dallas. Explore diverse programs, cutting-edge research, and vibrant campus life. World changers shap
- **jsonld_page**: https://www.smu.edu/
- **legal_name_stated**: Southern Methodist University
- **legal_name_stated_url**: https://www.smu.edu/aboutsmu/maps
- **legal_name_stated_quote**: Preparedness Follow Us Facebook Instagram LinkedIn YouTube X Link Menu Item (nested) --> SMU Home © Southern Methodist University Primary navigation menu Close Menu Search About SMU Office of the President Administration Presiden
- **mentions**: {'payment_method': {'text': 'interactive campus map enables you to search for specific buildings and includes street', 'url': 'https://www.smu.edu/aboutsmu/maps', 'quote': "ty's official address is 6425 Boaz Lane, Dallas TX 75205. Get directions to campus . Campus Map Our interactive campus map enables you to search for specific buildings and includes street addresses, building photos and descriptions. A printable campus map acce"}}
- **linkedin_url**: https://www.linkedin.com/school/smudallas/
- **tel_links**: 214-768-2000; 214-768-3333; 214-768-7650; 214-768-7660; 2147685555

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "6425 Boaz Lane, Dallas TX 75205", "address_country": "US", "address_url": "https://www.smu.edu/aboutsmu/contactsmu", "address_method": "pattern", "address_quote": "ndar Email Broken links on the SMU Web site Email Write to SMU Physical address 6425 Boaz Lane Dallas TX 75205 Format for All P.O. Box addresses SMU P.O. Box 75xxxx Dallas TX", "phone": "214-768-2000", "phone_url": "https://www.smu.edu/aboutsmu/contactsmu", "emails": "help@smu.edu", "emails_url": "https://www.smu.edu/aboutsmu/contactsmu", "domain": "smu.edu", "key": "lead:626f4f8d08c6d427", "name": "Southern Methodist University", "website": "https://smu.edu/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, evertz.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://evertz.com/img/evertz/evertz.logo.svg
- **logo_basis**: logo image in the site header
- **domain**: evertz.com
- **key**: vendor:Evertz
- **name**: Evertz
- **website**: https://evertz.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: End User License Agreement
- **legal_name_stated_url**: https://evertz.com/contact/about/
- **legal_name_stated_quote**: solutions. See also... Privacy Policy AODA Customer Service Policy Global Hardware Warranty Patents End User License Agreement (EULA) Solutions by Application Solutions by Platform Solutions by Product Type Contact Us Find a S
- **linkedin_url**: https://www.linkedin.com/company/evertz
- **tel_links**: 19053353700; 18779953700; 19053357570; 19054077570; 18185583910; 14808448501; 17243491412; 18008393658; 912227811124; 91

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "5292 John Lucas Dr, Burlington, Ontario, Canada, L7L 5Z9", "address_country": "CA", "address_url": "https://evertz.com/contact/", "address_method": "address-tag", "address_quote": "Americas Corporate HQ - Canada 5292 John Lucas Dr, Burlington, Ontario, Canada, L7L 5Z9 Phone: +1 905-335-3700 Toll Free: +1 877-995-3700 Email: [email protected] Cust", "phone": "+1 905-335-3700", "phone_url": "https://evertz.com/contact/", "domain": "evertz.com", "key": "vd:evertz.com", "name": "Evertz", "website": "https://evertz.com/", "kind": "vendor", "date": "2026-11-06"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Southern Methodist University | Q1536258 | official website on the organisation's domain (https://www.smu.edu/) + name |  | Southern Methodist University | Université méthodiste du Sud | private university; private not-for-profit educational institution |  | United States | 1911-00-00 |  |
| v | Evertz | Q5417421 | official website on the organisation's domain (http://www.evertz.com) + name |  | Evertz Microsystems | Evertz Technologies | business; public company |  | Canada | 1996-00-00; 1966-00-00 | Burlington |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:626f4f8d08c6d427",
 "ap_contact_team": {
  "emails": [
   "invoices@smu.edu",
   "ap_simmons@smu.edu",
   "ap_dea@smu.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoices@smu.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable/frequentlyaskedquestions",
    "quote": "e fully approved, it will be processed for payment. If you receive a vendor’s invoice within the department, please forward that invoice to invoices@smu.edu . Please ask the vendor to send directly to Accounts Payable going forward. Any non-invoice should be accompanied by a payment reques",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Southern Methodist University",
    "task_id": "CL-LD-47058"
   },
   {
    "email": "ap_simmons@smu.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable",
    "quote": "ap_simmons@smu.edu ap_theology@smu.edu 214-768-2016 ryeoman@smu.edu Mary Martinez Accounts Payable Specialist Athletics Stude",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Southern Methodist University",
    "task_id": "CL-LD-47058"
   },
   {
    "email": "ap_dea@smu.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.smu.edu/businessfinance/officeoffinanceandplanning/accountspayable",
    "quote": "\">ap_business_finance@smu.edu</a><br /> <a href=\"mailto:ap_dea@smu.edu\">ap_dea@smu.edu",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Southern Methodist University",
    "task_id": "CL-LD-47058"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of www.smu.edu (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.smu.edu (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.smu.edu (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 2)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:cb:CW2440469 | Department of Public Works and Government Services (PSPC) | Evertz Microsystems Ltd |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2440469 |
| canada_sosa:CW2440469 | Public Works and Government Services Canada | Evertz Microsystems Ltd:  Mandatory Commodity  Commercial-grade Audio Visual, Conferencing and Collaboration equipment E60HN-25AVSA |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2440469 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

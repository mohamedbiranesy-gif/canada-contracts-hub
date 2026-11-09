# S1-23 — East Sussex County Council ⇄ Spare Labs Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08) — ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England
SUBMIT TO: apinvoices@eastsussex.gov.uk (invoicing/AP mailbox, confirmed by the referee) | format: PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)
REFERENCE: contract 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender 14201 (tender_id) | PO rule: purchase-order terms published (as published: includes sending purchase order)
FROM / REMIT TO: SPARE LABS INC. — 810-815 W Hastings St, Vancouver, British Columbia, V6C 1B4, Canada | GST/HST 798511291RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: 30 days from receipt (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regu
DESCRIPTION: ESCC -DE- DDRT Digital Platform (a.k.a. Management System) | AMOUNT: 223,200.00 GBP
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 93
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: East Sussex County Council (non-profit / association / cultural body, UK) — public contract / purchase award with a published end date (dated record): Spare Labs Inc. | subject: ESCC -DE- DDRT Digital Platform (a.k.a. Management System) | instrument: contract | contract number: 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference | solicitation: 14201 (tender_id) | all identifiers: {"ocid": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013", "award_id": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-1", "notice_guid": "2d17136a-ef96-4739-bdfc-b79ffd9932f0", "tender_id": "14201", "compiled_release_id": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-2026-03-20T11:27:45Z"} | value: 223200.0 GBP | awarded 2026-02-27, start 2026-02-05, end 2029-02-04 | published by: Contracts Finder (UK) - OCDS award notices | record: https://www.contractsfinder.service.gov.uk/Notice/2d17136a-ef96-4739-bdfc-b79ffd9932f0 | vendor in Canada because: address.streetAddress text contains country "Canada" | status rule: active (published end date today or later) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 1 in the last 12 months; latest 2026-02-27)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:d7b1bc9df61219dc
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: East Sussex County Council
- **buyer_website**: https://eastsussex.gov.uk
- **buyer_address**: ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England
- **buyer_contact_evidence_url**: https://www.eastsussex.gov.uk/libraries/local/locations
- **buyer_legal_name_as_published**: East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08)
- **buyer_logo_url**: https://www.eastsussex.gov.uk/media/mepbxm1y/decoupled-escc-logo-for-website-test-version-large.png?width=250&height=55&rmode=pad&bgcolor=&format=webp&quality=100&autoorient=true
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q5329458; non-metropolitan county council
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.eastsussex.gov.uk/libraries/local/locations (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: apinvoices@eastsussex.gov.uk
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods
- **email_evidence_quote**: ness name and address; and 5.1.9 the name and address of the Council. 5.2 The Supplier must submit all invoices electronically via email to APInvoices@eastsussex.gov.uk and shall: 5.2.1 add the word ‘Invoice’ in the email subject field; 5.2.2 make sure it contains a valid Purchase Order nu
- **mailbox_provenance**: apinvoices@eastsussex.gov.uk (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods | quote: "ness name and address; and 5.1.9 the name and address of the Council. 5.2 The Supplier must submit all invoices electronically via email to APInvoices@eastsusse" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mailhost.eastsussex.gov.uk) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00139
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mailhost.eastsussex.gov.uk)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;rua=mailto:dmarc@eastsussex.gov.uk, mailto:dmarc-rua@dmarc.service.gov.uk
- **dmarc_record_domain**: eastsussex.gov.uk
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx include:spf4.eastsussex.gov.uk include:spf.occsites.co.uk include:spf_c.oraclecloud.com include:_spf.salesforce.com include:spf.recruitmail.com include:eu.rp.oracleemaildelivery.com ip4:194.140.226.250 -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)
- **payment_terms_as_published**: 30 days from receipt (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: includes sending purchase order) (as printed on https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "30 days from receipt (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: includes sending purchase order) (as printed on https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement, re-read 2026-11-08)", "invoice_format": "PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)", "requirements_text": "invoice format as published: PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08) — ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England ⏎ SUBMIT TO: apinvoices@eastsussex.gov.uk (invoicing/AP mailbox, confirmed by the referee) | format: PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08) ⏎ REFERENCE: contract 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender 14201 (tender_id) | PO rule: purchase-order terms published (as published: includes sending purchase order) ⏎ FROM / REMIT TO: SPARE LABS INC. — 810-815 W Hastings St, Vancouver, British Columbia, V6C 1B4, Canada | GST/HST 798511291RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: 30 days from receipt (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regu ⏎ DESCRIPTION: ESCC -DE- DDRT Digital Platform (a.k.a. Management System) | AMOUNT: 223,200.00 GBP
- **invoice_card_json**: {"bill_to": {"legal_name": "East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08)", "legal_name_is_published": true, "address": "ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "apinvoices@eastsussex.gov.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: includes sending purchase order) (as printed on https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_cont
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_contracts_finder

## Vendor
- **vendor**: Spare Labs Inc.
- **vendor_legal_name**: SPARE LABS INC.
- **vendor_registry_id**: Corporations Canada (corporation number): 9498877; corporation number 9498877 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=9498877
- **vendor_registered_address**: Suite 300 - 601 Hastings St W, Vancouver, BC, V6B 1M8, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2015-11-03
- **vendor_address**: 810-815 W Hastings St, Vancouver, British Columbia, V6C 1B4, Canada
- **vendor_country_basis**: address.streetAddress text contains country "Canada"
- **vendor_bn9**: 798511291
- **vendor_gst_hst_derived**: 798511291RT0001
- **vendor_website**: https://spare.com/
- **vendor_logo_url**: https://cdn.prod.website-files.com/66738eaed2726c155169f677/6ac7be737e828c37c290b048_JTA.svg
- **vendor_linkedin_url**: https://ca.linkedin.com/company/spare
- **vendor_facts_provenance**: name and address: the record's vendor block (Contracts Finder (UK) - OCDS award notices); registry identity: Corporations Canada (corporation number): 9498877; corporation number 9498877 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active; BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 9498877 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2015-12-09; website: https://spare.com/
- **vendor_concentration_top_share**: Spare Labs Inc.: 100% of 1 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; BC OrgBook (BC registration): Active
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2015-12-09
- **vendor_years_in_business**: 10.9 (since 2015-12-09, registry date)
- **vendor_bn_source**: corporations_canada 9498877 (exact match)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: includes sending purchase order) (as printed on https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"ocid": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013", "award_id": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-1", "notice_guid": "2d17136a-ef96-4739-bdfc-b79ffd9932f0", "tender_id": "14201", "compiled_release_id": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-2026-03-20T11:27:45Z"}
- **contract_title**: ESCC -DE- DDRT Digital Platform (a.k.a. Management System)
- **contract_description**: The digital platform element is being procured here which provides the 'Digital' element of the DDRT service. The digital platform will provide the passenger booking app, the driver app (for pick and drop off of passengers) and the backend management of the service including the algorithms that …
- **contract_or_agreement_number**: 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: 14201 (tender_id)
- **award_or_notice_id**: ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-1 (award_id); ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-2026-03-20T11:27:45Z (compiled_release_id); ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013 (ocid); 2d17136a-ef96-4739-bdfc-b79ffd9932f0 (notice_guid)
- **commodity_codes**: CPV 48000000 (Software package and information systems)
- **contract_value**: 223200.0
- **currency**: GBP
- **award_date**: 2026-02-27
- **start_date**: 2026-02-05
- **end_date**: 2029-02-04
- **contract_link**: https://www.contractsfinder.service.gov.uk/Notice/2d17136a-ef96-4739-bdfc-b79ffd9932f0
- **source**: Contracts Finder (UK) - OCDS award notices
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: Contracts Finder (UK) - OCDS award notices (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is accounted for by the buyer under the reverse charge where applicable
- **vendor_gst_hst_derived**: 798511291RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08) — ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England ⏎ SUBMIT TO: apinvoices@eastsussex.gov.uk (invoicing/AP mailbox, confirmed by the referee) | format: PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08) ⏎ REFERENCE: contract 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; tender 14201 (tender_id) | PO rule: purchase-order terms published (as published: includes sending purchase order) ⏎ FROM / REMIT TO: SPARE LABS INC. — 810-815 W Hastings St, Vancouver, British Columbia, V6C 1B4, Canada | GST/HST 798511291RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); UK VAT is | CURRENCY: GBP | TERMS: 30 days from receipt (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regu ⏎ DESCRIPTION: ESCC -DE- DDRT Digital Platform (a.k.a. Management System) | AMOUNT: 223,200.00 GBP
- **invoice_card_json**: {"bill_to": {"legal_name": "East Sussex County Council (label per Wikidata Q5329458, official website on the organisation's domain (https://www.eastsussex.gov.uk) + name; 2026-11-08)", "legal_name_is_published": true, "address": "ICT SERVICES, COUNTY HALL, LEWES, BN71SG, England", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "apinvoices@eastsussex.gov.uk", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "PDF or TIFF format (as printed on https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: includes sending purchase order) (as printed on https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 14201 (tender_id) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source uk_cont
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["apinvoices@eastsussex.gov.uk (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods", "quote: \"ness name and address; and 5.1.9 the name and address of the Council. 5.2 The Supplier must submit all invoices electronically via email to APInvoices@eastsusse\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mailhost.eastsussex.gov.uk)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00139"], "buyer_facts": ["address and phone: the buyer's own site, https://www.eastsussex.gov.uk/libraries/local/locations (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.eastsussex.gov.uk/social-care/paying-for-care/types-of-direct-payment-account | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, eastsussex.gov.uk)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.eastsussex.gov.uk/media/mepbxm1y/decoupled-escc-logo-for-website-test-version-large.png?width=250&height=55&rmode=pad&bgcolor=&format=webp&quality=100&autoorient=true
- **logo_basis**: logo image in the site header
- **domain**: eastsussex.gov.uk
- **key**: b:d7b1bc9df61219dc
- **name**: East Sussex County Council
- **website**: https://eastsussex.gov.uk/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: British Sign Language
- **legal_name_stated_url**: https://www.eastsussex.gov.uk/about-this-site
- **legal_name_stated_quote**: ds Community Environment Business in East Sussex Contact us About this site Accessibility statement British Sign Language (BSL) introduction to our website Cookies Privacy Search Engine Site Map Modern Slavery Statements
- **portals**: [{'name': 'Oracle Fusion Cloud (supplier portal)', 'kind': 'e-procurement', 'url': 'https://fa-euru-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/External/', 'on_page': 'https://www.eastsussex.gov.uk/'}]
- **mentions**: {'payment_method': {'text': 'interact with carousel replies, they may experience focus visibility issues and navigat', 'url': 'https://www.eastsussex.gov.uk/about-this-site/accessibility-statement', 'quote': 'e escalated it to the product engineering team for resolution. When keyboard or screen reader users interact with carousel replies, they may experience focus visibility issues and navigational issues. Focus visibility may not move new messages completely into'}}
- **linkedin_url**: https://www.linkedin.com/company/east-sussex-county-council/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "7 Market Square, Battle, East Sussex, TN33 0XB", "address_country": "GB", "address_url": "https://www.eastsussex.gov.uk/libraries/local/locations", "address_method": "pattern", "address_quote": "View map of results Battle Library Today's hours Open today 10am to 1pm Address 7 Market Square, Battle, East Sussex, TN33 0XB Facilities Disabled access, Display facilities", "domain": "eastsussex.gov.uk", "key": "b:d7b1bc9df61219dc", "name": "East Sussex County Council", "website": "https://eastsussex.gov.uk/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, spare.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Spare Labs Inc
- **legal_name_url**: https://spare.com/
- **legal_name_quote**: tomer Stories Blog eBooks Connect Upcoming Webinars Tradeshows Privacy Terms of Use Security © 2026 Spare Labs Inc
- **logo_url**: https://cdn.prod.website-files.com/66738eaed2726c155169f677/6ac7be737e828c37c290b048_JTA.svg
- **logo_basis**: logo image in the site header
- **domain**: spare.com
- **key**: vendor:Spare Labs Inc.
- **name**: Spare Labs Inc.
- **website**: https://spare.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: California Privacy Rights Act
- **legal_name_stated_url**: https://spare.com/privacy-policy
- **legal_name_stated_quote**: nia and is provided in accordance with the California Consumer Privacy Act (CCPA) as amended by the California Privacy Rights Act (CPRA). The tables below describe the categories of personal information Spare may collect, the sou
- **mentions**: {'payment_method': {'text': 'interact with Spare through: our websites and online services marketing and communicati', 'url': 'https://spare.com/privacy-policy', 'quote': 'describes how Spare collects, uses, discloses, and safeguards personal information when individuals interact with Spare through: our websites and online services marketing and communications recruiting and hiring processes customer and business relationships s'}}
- **linkedin_url**: https://ca.linkedin.com/company/spare

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | East Sussex County Council | Q5329458 | official website on the organisation's domain (https://www.eastsussex.gov.uk) + name |  | East Sussex County Council |  | non-metropolitan county council |  | United Kingdom |  |  |
| v | SPARE LABS INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:d7b1bc9df61219dc",
 "ap_contact_team": {
  "emails": [
   "direct.payments.invoices@eastsussex.gov.uk",
   "apinvoices@eastsussex.gov.uk",
   "direct.payments@eastsussex.gov.uk",
   "providerpayments@eastsussex.gov.uk",
   "purchasing.queries@eastsussex.gov.uk",
   "procurementpmo@eastsussex.gov.uk"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "Oracle Fusion Purchase-to-Pay covers most council orders, with exceptions including schooldirectorders. ElectronicPOs, BACS and electroniccatalogues. PutPO number and contactdetails on invoice; resolvePO price/errors withnamedbuyer before supply. Check specificPO invoicing address; SAP-originPO providesaddress, deliverylocation is distinct. MasterCard purchasingcards offer payment within4workingdays ifsupplierparticipates. No universalAPmailbox, netdays, invoiceformat or universalpostaladdress on checkedguide.",
  "evidence": [
   {
    "email": "direct.payments.invoices@eastsussex.gov.uk",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/social-care/paying-for-care/types-of-direct-payment-account",
    "quote": "account statement at any time. Things to note To pay the bills for your care, ask the care provider to: send a copy of the 4-weekly bill to direct.payments.invoices@eastsussex.gov.uk for the Direct Payments team to pay send you a copy of the bill to check it is correct. Let the Direct Paym",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "East Sussex County Council",
    "task_id": "CL-DT04-00024"
   },
   {
    "email": "apinvoices@eastsussex.gov.uk",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders/purchase-orders-goods",
    "quote": "ness name and address; and 5.1.9 the name and address of the Council. 5.2 The Supplier must submit all invoices electronically via email to APInvoices@eastsussex.gov.uk and shall: 5.2.1 add the word ‘Invoice’ in the email subject field; 5.2.2 make sure it contains a valid Purchase Order nu",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "East Sussex County Council",
    "task_id": "CL-WS-00139"
   },
   {
    "email": "direct.payments@eastsussex.gov.uk",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/social-care/providers/contracts-purchasing-support/extra-information-for-direct-payment-support-services",
    "quote": "aining all the information that the support service has, to enable them to look into the account. The email address for these referrals is: direct.payments@eastsussex.gov.uk Back to top Support service managed account referrals As the support service is managing the account, it is essentia",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "East Sussex County Council",
    "task_id": "CL-DT04-00024"
   },
   {
    "email": "providerpayments@eastsussex.gov.uk",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/social-care/providers/contracts-purchasing-support/payments",
    "quote": "an adult social care provider with a payment query, please contact us:</p> <p class=\"govuk-body\">Email: <a class=\"govuk-link\" href=\"mailto:providerpayments@eastsussex.gov.uk\" style=\"\">ContrOCC Payments Team<i class=\"fa-regular fa-envelope govuk-!-margin-left-1\"></i></a></p> <p class=\"govu",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "East Sussex County Council",
    "task_id": "CL-DT04-00024"
   },
   {
    "email": "purchasing.queries@eastsussex.gov.uk",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/business/doing-business/electronic-procurement",
    "quote": "Council member of staff quoted on the purchase order. If no name is listed on your invoice, please email <a class=\"govuk-link\" href=\"mailto:purchasing.queries@eastsussex.gov.uk\" style=\"\">Purchasing queries<i class=\"fa-regular fa-envelope govuk-!-margin-left-1\"></i></a>. </li> <li>Make sure",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "East Sussex County Council",
    "task_id": "CL-WS-00066"
   },
   {
    "email": "procurementpmo@eastsussex.gov.uk",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastsussex.gov.uk/business/doing-business/rules-regulations-policies/purchase-orders",
    "quote": "<div > <p class=\"govuk-body\">Examples of our standard contracts are available on request by emailing our <a class=\"govuk-link\" href=\"mailto:procurementpmo@eastsussex.gov.uk\" style=\"\">Procurement team<i class=\"fa-regular f
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| uk_contracts_finder:ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-1 | uk_contracts_finder | ongoing | ESCC -DE- DDRT Digital Platform (a.k.a. Management System) | 223200.0 | GBP |  |  | {"ocid": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013", "award_id": "ocds-b5fd17-1ffabd15-6280-4646-8b2d-d07e96045013-1", "notice_guid": "2d17136a-ef96-4739-bdfc-b79ffd9932f0", "tender_id": "1420 | https://www.contractsfinder.service.gov.uk/Notice/2d17136a-ef96-4739-bdfc-b79ffd9932f0 |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 11)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:9e6f1e34-be1a-4685-beb7-ae6dd04c0e75:1 | City of Cornwall | Specialized Transit/On Demand Scheduling Software | 440700.0 |  |  | https://cornwall.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9e6f1e34-be1a-4685-beb7-ae6dd04c0e75 |
| ca_bidsandtenders:bb300062-f2c7-44c3-8057-adca6044ec16:1 | City of Timmins | Para-Transit/On-Demand Scheduling Software RFP |  |  |  | https://timmins.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bb300062-f2c7-44c3-8057-adca6044ec16 |
| ca_bidsandtenders:18c812fd-8853-4133-b4aa-6d8166be756b:1 | City of Brampton | Cloud Based on-demand Transit Technology Solution for Brampton Transit for a Three (3) Year Period |  |  |  | https://brampton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/18c812fd-8853-4133-b4aa-6d8166be756b |
| ca_bidsandtenders:b9f962e6-c555-49b4-905a-79b6327efcdb:1 | Town of Oakville | On-Demand Scheduling Software and Ride-hailing App |  |  |  | https://oakville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b9f962e6-c555-49b4-905a-79b6327efcdb |
| ca_bidsandtenders:dc4b433f-325e-45af-a590-d692d65104a3:1 | Region of Waterloo | Software and Related Technology and Services for On-Demand Transit Service Delivery |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dc4b433f-325e-45af-a590-d692d65104a3 |
| ca_bidsandtenders:0131c587-a834-43d9-98c3-f2673f5fce5f:1 | City of Stratford | Southwest Community Transit Association: Digital Ride Booking Application |  |  |  | https://stratford.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0131c587-a834-43d9-98c3-f2673f5fce5f |
| ca_bidsandtenders:dd6c32a4-ce83-4006-af31-e60ffeb82d69:1 | City of Hamilton | Proposal for Demand Responsive Transit Pilot | 23100.0 |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dd6c32a4-ce83-4006-af31-e60ffeb82d69 |
| ca_bidsandtenders:d0a7b537-e286-40c7-9987-fb99d1ca4124:1 | City of Burlington | On-Demand Transit Technology Solution | 481719.0 |  |  | https://burlington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d0a7b537-e286-40c7-9987-fb99d1ca4124 |
| ca_saskatchewan:236f778e-27f0-48aa-9eba-e81dd8aa6b58:0 | City of Regina | On Request Transit Software | 574430.04 |  |  | https://www.sasktenders.ca/Competitions/Print?id=236f778e-27f0-48aa-9eba-e81dd8aa6b58 |
| uk_contracts_finder:ocds-b5fd17-994dac90-50a3-4a4c-8c72-1406706234e2-1 | CAMBRIDGESHIRE AND PETERBOROUGH BUSINESS GROWTH COMPANY LIMITED | Tiger on Demand Booking & Customer App Services | 113400.0 |  |  | https://www.contractsfinder.service.gov.uk/Notice/741fb1de-9e7c-4ede-a4b6-2ccb7e420cc5 |
| uk_find_a_tender:ocds-h6vhtk-0504a3:4:GB-PPON-PBCR-8647-WWTV | Foreign Commonwealth and Development Office | Lot 2b Software as a Service (Saas) | 14000000000.0 |  |  | https://www.find-tender.service.gov.uk/Notice/070505-2026 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

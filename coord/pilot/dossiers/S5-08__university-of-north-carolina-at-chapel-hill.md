# S5-08 — University Of North Carolina At Chapel Hill ⇄ THE UNIVERSITY OF MANITOBA

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: University of North Carolina at Chapel Hill — 104 Airport Drive, Chapel Hill, NC 27599
SUBMIT TO: pastdueinvoices@unc.edu (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: contract 847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: "S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123") | PO rule: yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense co
FROM / REMIT TO: THE UNIVERSITY OF MANITOBA — Winnipeg, MB, Canada | GST/HST number not public
TAX: Tax-Exempt Status Letter Vendor Management Wire Fund Transfers Contact Vacant Director, Accounts Payable and Vendor S (as printed on https://finance.unc.edu/dep | CURRENCY: USD (derived from the source's government) | TERMS: payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary
DESCRIPTION: University Of North Carolina At Chapel Hill (organisation (type not stated in the record), jurisdiction not stated) — public contract / purc | AMOUNT: 48531.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University Of North Carolina At Chapel Hill (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): THE UNIVERSITY OF MANITOBA | contract number: 847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: "S NIMH grant (R01 MH123724) and the European Un | all identifiers: {"internal_id": "5137923", "prime_award_internal_id": "270351532", "Sub-Award ID": "5137923", "Prime Award ID": "R37CA306827", "prime_award_generated_internal_id": "ASST_NON_R37CA306827_075"} | value: 48531.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2026-08-19 | published by: subawardee country | record: https://www.usaspending.gov/award/R37CA306827 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:5f1ad32e75b74dc0
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: University Of North Carolina At Chapel Hill
- **buyer_website**: https://unc.edu
- **buyer_address**: 104 Airport Drive, Chapel Hill, NC 27599
- **buyer_phone**: 919-962-7242
- **buyer_contact_evidence_url**: https://finance.unc.edu/about/
- **buyer_legal_name_as_published**: University of North Carolina at Chapel Hill
- **buyer_logo_url**: https://www.unc.edu/wp-content/uploads/2025/11/University_Signature_White_Navy_rgb_h.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/university-of-north-carolina-at-chapel-hill/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q192334; public research university; public educational institution of the United States
- **buyer_founded**: 1789-12-11 (Wikidata Q192334, official website on the organisation's domain (https://unc.edu) + name; 2026-11-08)
- **buyer_employees**: 14404 (Wikidata Q192334, official website on the organisation's domain (https://unc.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://finance.unc.edu/about/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax-Exempt Status Letter Vendor Management Wire Fund Transfers Contact Vacant Director, Accounts Payable and Vendor S (as printed on https://finance.unc.edu/departments/accounts-payable-and-vendor-services/, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: pastdueinvoices@unc.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://finance.unc.edu/departments/accounts-payable-and-vendor-services/
- **email_evidence_quote**: Department Phone 919-962-0213 Past Due Invoice Inquiries pastdueinvoices@unc.edu News Updates to Card Infraction Policies 1253 and 1506 August 31, 2026 Effective Sept. 1, 2026, updates to Policy 1253 on Purc
- **email_evidence_context**: Fund Transfers Contact Vacant Director, Accounts Payable and Vendor Services 104 Airport Drive, Suite 3200 Campus Box 1220 Departmental Staff Directory Department Email accountspayable@unc.edu Department Phone 919-962-0213 Past Due Invoice Inquiries pastdueinvoices@unc.edu News Updates to Card Infraction Policies 1253 and 1506 August 31, 2026 Effective Sept. 1, 2026, updates to Policy 1253 on Purchase Card (P-Card) Infractions and Policy 1506 on Travel & Expense Card (T&E Card) Infractions will take effect. Categories (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: pastdueinvoices@unc.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://finance.unc.edu/departments/accounts-payable-and-vendor-services/ | quote: "Department Phone 919-962-0213 Past Due Invoice Inquiries pastdueinvoices@unc.edu News Updates to Card Infraction Policies 1253 and 1506 August 31, 2026 Effectiv" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00019
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:DmarcAggregate@office.unc.edu,mailto:dmarc_agg@vali.email; ruf=mailto:DmarcForensic@office.unc.edu; fo=1;
- **dmarc_record_domain**: unc.edu
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:152.2.79.86 ip4:152.2.79.87 ip4:152.2.79.94 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 919-962-0213 (as printed on https://finance.unc.edu/departments/accounts-payable-and-vendor-services/, re-read 2026-11-08)
- **payment_terms_as_published**: payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary/, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense code Purchase order n) (as printed on https://fo.unc.edu/sce/finance/pay-invoice/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary/, re-read 2026-11-08)", "po_required": "yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense code Purchase order n) (as printed on https://fo.unc.edu/sce/finance/pay-invoice/, re-read 2026-11-08)", "ap_phone": "919-962-0213 (as printed on https://finance.unc.edu/departments/accounts-payable-and-vendor-services/, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of North Carolina at Chapel Hill — 104 Airport Drive, Chapel Hill, NC 27599 ⏎ SUBMIT TO: pastdueinvoices@unc.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract 847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: "S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123") | PO rule: yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense co ⏎ FROM / REMIT TO: THE UNIVERSITY OF MANITOBA — Winnipeg, MB, Canada | GST/HST number not public ⏎ TAX: Tax-Exempt Status Letter Vendor Management Wire Fund Transfers Contact Vacant Director, Accounts Payable and Vendor S (as printed on https://finance.unc.edu/dep | CURRENCY: USD (derived from the source's government) | TERMS: payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary ⏎ DESCRIPTION: University Of North Carolina At Chapel Hill (organisation (type not stated in the record), jurisdiction not stated) — public contract / purc | AMOUNT: 48531.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "University of North Carolina at Chapel Hill", "legal_name_is_published": true, "address": "104 Airport Drive, Chapel Hill, NC 27599", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "pastdueinvoices@unc.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense code Purchase order n) (as printed on https://fo.unc.edu/sce/finance/pay-invoice/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: \"S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123\")", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 5137923 (internal_id) — source usaspending"}, "terms": {"payment_terms": "payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_st
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: award or notice id: 5137923 (internal_id) — source usaspending

## Vendor
- **vendor**: THE UNIVERSITY OF MANITOBA
- **vendor_address**: Winnipeg, MB, Canada
- **vendor_country_basis**: subawardee country=CAN
- **vendor_website**: https://umanitoba.ca/
- **vendor_phone**: 1-800-432-1960 (North America)
- **vendor_contact_evidence_url**: https://umanitoba.ca/about-um/our-campuses
- **vendor_logo_url**: https://umanitoba.ca/themes/custom/umanitoba/images/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://umanitoba.ca/ (University of Manitoba Skip to main content The University of Manitoba campuses and research spaces are located on original lands of Anishinaabeg, Ininiwak, Ani)
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); phone / role e-mails / logo: the vendor's own site, https://umanitoba.ca/about-um/our-campuses (tools/org_contacts.py, org_extras.py); website: https://umanitoba.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense code Purchase order n) (as printed on https://fo.unc.edu/sce/finance/pay-invoice/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "5137923", "prime_award_internal_id": "270351532", "Sub-Award ID": "5137923", "Prime Award ID": "R37CA306827", "prime_award_generated_internal_id": "ASST_NON_R37CA306827_075"}
- **contract_or_agreement_number**: 847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: "S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123")
- **award_or_notice_id**: 5137923 (internal_id); 5137923 (Sub-Award ID); R37CA306827 (Prime Award ID); 270351532 (prime_award_internal_id); ASST_NON_R37CA306827_075 (prime_award_generated_internal_id)
- **contract_value**: 48531.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2026-08-19
- **contract_link**: https://www.usaspending.gov/award/R37CA306827
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 12
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 12 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of North Carolina at Chapel Hill — 104 Airport Drive, Chapel Hill, NC 27599 ⏎ SUBMIT TO: pastdueinvoices@unc.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract 847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: "S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123") | PO rule: yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense co ⏎ FROM / REMIT TO: THE UNIVERSITY OF MANITOBA — Winnipeg, MB, Canada | GST/HST number not public ⏎ TAX: Tax-Exempt Status Letter Vendor Management Wire Fund Transfers Contact Vacant Director, Accounts Payable and Vendor S (as printed on https://finance.unc.edu/dep | CURRENCY: USD (derived from the source's government) | TERMS: payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary ⏎ DESCRIPTION: University Of North Carolina At Chapel Hill (organisation (type not stated in the record), jurisdiction not stated) — public contract / purc | AMOUNT: 48531.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "University of North Carolina at Chapel Hill", "legal_name_is_published": true, "address": "104 Airport Drive, Chapel Hill, NC 27599", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "pastdueinvoices@unc.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: reference (if applicable) Subsystem information: work order, material request, CIP ID, CIP expense code Purchase order n) (as printed on https://fo.unc.edu/sce/finance/pay-invoice/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "847776 (as printed in the buyer's own buyer page: https://cdr.lib.unc.edu/downloads/wm118038p, read 2026-11-08: \"S NIMH grant (R01 MH123724) and the European Union’s Horizon 2020 research and innovation program under grant agreement No 847776. KK was supported by the University of Manitoba and US NIMH (R01 MH123\")", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 5137923 (internal_id) — source usaspending"}, "terms": {"payment_terms": "payment within 30 days (as printed on https://finance.unc.edu/policies-procedures-and-forms/glossary/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_st
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["pastdueinvoices@unc.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://finance.unc.edu/departments/accounts-payable-and-vendor-services/", "quote: \"Department Phone 919-962-0213 Past Due Invoice Inquiries pastdueinvoices@unc.edu News Updates to Card Infraction Policies 1253 and 1506 August 31, 2026 Effectiv\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00019"], "buyer_facts": ["address and phone: the buyer's own site, https://finance.unc.edu/about/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (subawardee country)", "phon

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://finance.unc.edu/departments/accounts-payable-and-vendor-services/ | 2026-11-08 | ok |  |  |  | 919-962-0213 |  |  |  |  |  |

## Buyer site facts (org_extras, unc.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: University of North Carolina at Chapel Hill
- **legal_name_url**: https://finance.unc.edu/
- **legal_name_quote**: Home - Finance skip to the end of the global utility bar The University of North Carolina at Chapel Hill Accessibility Events Libraries Maps Departments ConnectCarolina UNC Search Skip to main content You
- **logo_url**: https://www.unc.edu/wp-content/uploads/2025/11/University_Signature_White_Navy_rgb_h.svg
- **logo_basis**: logo image in the site header
- **domain**: unc.edu
- **key**: lead:5f1ad32e75b74dc0
- **name**: University Of North Carolina At Chapel Hill
- **website**: https://unc.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: The University of North Carolina at Chapel Hill
- **jsonld_logo**: https://www.unc.edu/wp-content/uploads/2025/11/University_Signature_White_Navy_rgb_h.svg
- **jsonld_url**: https://www.unc.edu/
- **jsonld_same_as**: https://www.facebook.com/uncchapelhill/; https://x.com/unc; https://www.instagram.com/uncchapelhill/; https://www.linkedin.com/school/university-of-north-carolina-at-chapel-hill/; https://pinterest.com/uncchapelhill/; https://www.youtube.com/user/UNCChapelHill
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://www.unc.edu/","url":"https://www.unc.edu/","name":"The University of North Carolina at Chapel Hill","isPartOf":{"@id":"https://www.unc.edu/#website"},"about":{"@id":"https://www.unc.edu/#organization"},"primaryImageOfPage":
- **jsonld_page**: https://www.unc.edu/
- **legal_name_stated**: University
- **legal_name_stated_url**: https://www.unc.edu/about/
- **legal_name_stated_quote**: About the University - The University of North Carolina at Chapel Hill Close Alert Message Alert Carolina! Normal The Un
- **linkedin_url**: https://www.linkedin.com/school/university-of-north-carolina-at-chapel-hill/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "104 Airport Drive, Chapel Hill, NC 27599", "address_country": "US", "address_url": "https://finance.unc.edu/about/", "address_method": "pattern", "address_quote": "f Finance and Operations . Locations Main Office Administrative Office Building 104 Airport Drive Chapel Hill, NC 27599 ( Map ) Phone: 919-962-7242 Fax: 919-962-4140 Cashier’s O", "phone": "919-962-7242", "phone_url": "https://finance.unc.edu/about/", "domain": "unc.edu", "key": "lead:5f1ad32e75b74dc0", "name": "University Of North Carolina At Chapel Hill", "website": "https://finance.unc.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, umanitoba.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: University of Manitoba
- **legal_name_url**: https://umanitoba.ca/
- **legal_name_quote**: University of Manitoba Skip to main content The University of Manitoba campuses and research spaces are located on origina
- **logo_url**: https://umanitoba.ca/themes/custom/umanitoba/images/logo.svg
- **logo_basis**: logo image on the site
- **domain**: umanitoba.ca
- **key**: b:697d047e9f2d7d76
- **name**: University of Manitoba
- **website**: https://umanitoba.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: University
- **legal_name_stated_url**: https://umanitoba.ca/about-um
- **legal_name_stated_quote**: About UM | University of Manitoba Skip to main content The University of Manitoba campuses and research spaces are locate
- **mentions**: {'payment_method': {'text': 'interactive way to identify reasonable accommodations that support equal access to educ', 'url': 'https://umanitoba.ca/student-supports/accessibility', 'quote': 's are shared. How academic accommodations are determined SAS works with students in a personalized, interactive way to identify reasonable accommodations that support equal access to education. The focus is on addressing barriers in the environment that may li'}}
- **linkedin_url**: https://www.linkedin.com/school/umanitoba/
- **tel_links**: +1800-432-1960; +1204-474-9341

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "University of Manitoba , Winnipeg, Manitoba Canada, R3T 2N2, Maps and directions", "address_country": "CA", "address_url": "https://umanitoba.ca/about-um/our-campuses", "address_method": "address-tag", "address_quote": "of the Red River Métis. More University of Manitoba Winnipeg, Manitoba Canada, R3T 2N2 Maps and directions 1-800-432-1960 (North America) Emergency: 204-474-9341 Emer", "phone": "1-800-432-1960 (North America)", "phone_url": "https://umanitoba.ca/about-um/our-campuses", "domain": "umanitoba.ca", "key": "b:697d047e9f2d7d76", "name": "University of Manitoba", "website": "https://umanitoba.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of Manitoba | Q1191833 | official website on the organisation's domain (https://umanitoba.ca/) + name |  | University of Manitoba | Université du Manitoba | university in Manitoba; public research university; charitable organization |  | Canada | 1877-00-00 | Winnipeg |
| b | University Of North Carolina At Chapel Hill | Q192334 | official website on the organisation's domain (https://unc.edu) + name |  | University of North Carolina at Chapel Hill | Université de Caroline du Nord à Chapel Hill | public research university; public educational institution of the United States |  | United States | 1789-12-11 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:5f1ad32e75b74dc0",
 "ap_contact_team": {
  "emails": [
   "pastdueinvoices@unc.edu",
   "accountspayable@unc.edu",
   "accounting@unc.edu",
   "financialreporting@unc.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "pastdueinvoices@unc.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.unc.edu/departments/accounts-payable-and-vendor-services/",
    "quote": "Department Phone 919-962-0213 Past Due Invoice Inquiries pastdueinvoices@unc.edu News Updates to Card Infraction Policies 1253 and 1506 August 31, 2026 Effective Sept. 1, 2026, updates to Policy 1253 on Purc",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-WS-00019"
   },
   {
    "email": "accountspayable@unc.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://fo.unc.edu/about/contact/",
    "quote": "Accounts Payable and Vendor Services Finance 919-962-0213 accountspayable@unc.edu Benefits Human Resources 919-962-3071 benefits@unc.edu Budget and Data Analysis Budget and Data Analysis 919-966-3251 9",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-SQ-00894"
   },
   {
    "email": "accounting@unc.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://fo.unc.edu/about/contact/",
    "quote": "rations Departmental Contact Information Unit Department Phone Fax Email Social Media Accounting Services Finance 919-962-0036 919-962-3306 accounting@unc.edu Accounts Payable and Vendor Services Finance 919-962-0213",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-SQ-00894"
   },
   {
    "email": "accountspayable@unc.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://finance.unc.edu/departments/accounts-payable-and-vendor-services/",
    "quote": "Director, Accounts Payable and Vendor Services 104 Airport Drive, Suite 3200 Campus Box 1220 Departmental Staff Directory Department Email accountspayable@unc.edu Department Phone 919-962-0213 Past Due Invoice Inquiries",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-WS-00019"
   },
   {
    "email": "accountspayable@unc.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://policies.unc.edu/TDClient/2833/Portal/KB/Article/131540/707-1-Procedure-for-Payments-for-Personal-Services-of-a-Non-North-Carolina-Resident",
    "quote": "Policy Contact Subject Contact Telephone Fax E-Mail Non-resident withholding Accounts Payable and Vendor Services 919-843-5098 919-962-2356 accountspayable@unc.edu Sign in to leave feedback 100% helpful - 1 review Blank Blank Blank Blank Print Article Deleting... © 2026 University of North",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-WS-00413"
   },
   {
    "email": "financialreporting@unc.edu",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://fo.unc.edu/about/contact/",
    "quote": "Facilities Technology Group Facilities Services 919-843-3617 Financial Reporting and Management Services Finance 919-843-2694 919-962-4140 financialreporting@unc.edu Fleet Services Facilities Services 919-966-2967 Granville Towers Real Estate Operations 919-370-4500 Grounds Services Facil",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "University Of North Carolina At Chapel Hill",
    "task_id": "CL-SQ-00894"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of unc.edu (33 pages, robots.txt respected), no AI, no search engine",
  "site crawl of unc.edu (33 pages, robots.txt respected), no AI, no search engine",
  "site crawl of unc.edu (33 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 12)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bc_ministry_awards:e0adfd6b10310506 | Ministry of Health | Interprofessional Competency Tools for International Health Prof | 311644.66 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| canada_federal:cgc-ccg:6054859 | Canadian Grain Commission | Research contracts | 63000.0 |  |  | https://search.open.canada.ca/contracts/record/cgc-ccg,C-2026-2027-Q1-00008 |
| canada_federal:pch:45450253 | Canadian Heritage | Management Consulting | 172733.75 |  |  | https://search.open.canada.ca/contracts/record/pch,C-2024-2025-Q2-00002 |
| canada_federal:pch:45471501 | Canadian Heritage | Other Business Services not Elsewhere Specified | 1021636.0 |  |  | https://search.open.canada.ca/contracts/record/pch,C-2024-2025-Q2-00026 |
| canada_federal:dfo-mpo:4500106747 | Fisheries and Oceans Canada | Scientific services | 19873.0 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2026-2027-Q1-00830 |
| canada_federal:hc-sc:4500486622 | Health Canada | Other health services not elsewhere specified | 10739.52 |  |  | https://search.open.canada.ca/contracts/record/hc-sc,C-2025-2026-Q3-00054 |
| canada_federal:dnd-mdn:CW2428868 | National Defence | Engineering consultants-Other | 500227.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-04186 |
| canada_federal:nrc-cnrc:1025568 | National Research Council Canada | Scientific services | 119880.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2024-2025-Q4-00147 |
| canada_federal:phac-aspc:6D06346871 | Public Health Agency of Canada | Other business services not elsewhere specified | 360000.0 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2025-2026-Q1-00287 |
| canada_federal:cb:CW2380381 | Public Health Agency of Canada (PHAC) | 6D063-246871 Breeding Services for National Microbiology Laboratory | 360000.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2380381 |
| who:202014669 | World Health Organization - Headquarters | Services.Implementation of programmes. | 41250.01 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2018-service-awarded-contracts.pdf?sfvrsn=aa4f8722_5&ua=1 |
| who:201915864 | World Health Organization - Headquarters | Services.Implementation of programmes. | 40000.0 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2018-service-awarded-contracts.pdf?sfvrsn=aa4f8722_5&ua=1 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

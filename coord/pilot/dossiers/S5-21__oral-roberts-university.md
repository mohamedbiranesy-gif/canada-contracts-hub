# S5-21 — Oral Roberts University ⇄ d2l.com

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Oral Roberts University — 7777 South Lewis Ave, Tulsa, OK, 74171
SUBMIT TO: invoices@oru.edu (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: include, but are not limited to, purchase order)
FROM / REMIT TO: D2L Corporation (as printed on the vendor's site: https://www.d2l.com/) — 137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8 | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Oral Roberts University | Customer Success | D2L
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 72
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Oral Roberts University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: d2l.com | subject: Oral Roberts University | Customer Success | D2L | published by: the Canada-located vendor's own website | record: https://www.d2l.com/why-d2l/customers/oral-roberts-university/ | vendor in Canada because: vendor located in Canada (stories)=d2l.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:dfc738eca5033171
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Oral Roberts University
- **buyer_website**: https://oru.edu/
- **buyer_address**: 7777 South Lewis Ave, Tulsa, OK, 74171
- **buyer_phone**: 1.800.678.8876
- **buyer_contact_evidence_url**: https://oru.edu/campus-visitation/
- **buyer_legal_name_as_published**: Oral Roberts University
- **buyer_logo_url**: https://xab3h1j8dc.cloudimg.io/oru.edu/_resources/images/Oral-Roberts-University-Logo-Tan-udpated.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/oral-roberts-university/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q3121493; university; private not-for-profit educational institution; church college
- **buyer_founded**: 1963-00-00 (Wikidata Q3121493, official website on the organisation's domain (http://oru.edu) + name; 2026-11-08)
- **buyer_employees**: 820 (Wikidata Q3121493, official website on the organisation's domain (http://oru.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://oru.edu/campus-visitation/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoices@oru.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf
- **email_evidence_quote**: ormed on University premises/grounds. Invoices are a request for payment from a Vendor to University. All invoices must be sent directly to invoices@oru.edu. Purchase Requisitions are internal forms used to request permission to buy Goods and/or Services. They are used to identify the Good
- **email_evidence_context**: ntractual document that Vendors must sign before performing Services which specifically includes Services performed on University premises/grounds. Invoices are a request for payment from a Vendor to University. All invoices must be sent directly to invoices@oru.edu. Purchase Requisitions are internal forms used to request permission to buy Goods and/or Services. They are used to identify the Goods and/or Services to be purchased and any necessary approvals. All purchase requisitions are required to have the pr (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoices@oru.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf | quote: "ormed on University premises/grounds. Invoices are a request for payment from a Vendor to University. All invoices must be sent directly to invoices@oru.edu. Pu" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Mimecast | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00188
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Mimecast
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100; rua=mailto:re+gxt3w08la4v@dmarc.postmarkapp.com; sp=none; aspf=r;
- **dmarc_record_domain**: oru.edu
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:us._netblocks.mimecast.com ip4:205.143.139.214 ip4:205.143.139.217 ip4:63.101.54.51 ip4:66.151.109.0/24 include:spf.protection.outlook.com ip4:205.143.139.224 include:aspmx.pardot.com include:servers.mcsv.net ip4:165.193.85.0/24 include:spf.dynect.net ip4:198.187.196.100 ip4:198.187.1
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **po_required_as_published**: purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Oral Roberts University — 7777 South Lewis Ave, Tulsa, OK, 74171 ⏎ SUBMIT TO: invoices@oru.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: include, but are not limited to, purchase order) ⏎ FROM / REMIT TO: D2L Corporation (as printed on the vendor's site: https://www.d2l.com/) — 137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Oral Roberts University | Customer Success | D2L
- **invoice_card_json**: {"bill_to": {"legal_name": "Oral Roberts University", "legal_name_is_published": true, "address": "7777 South Lewis Ave, Tulsa, OK, 74171", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@oru.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%2020)"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%2020)

## Vendor
- **vendor**: d2l.com
- **vendor_legal_name**: D2L Corporation (as printed on the vendor's site: https://www.d2l.com/)
- **vendor_trading_name**: d2l.com
- **vendor_address**: 137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8
- **vendor_country_basis**: vendor located in Canada (stories)=d2l.com
- **vendor_website**: https://d2l.com
- **vendor_phone**: 1-519-772-0325
- **vendor_contact_evidence_url**: https://www.d2l.com/about/locations/
- **vendor_logo_url**: https://www.d2l.com/wp-content/uploads/2022/08/logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/d2l/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://www.d2l.com/about/locations/ (tools/org_contacts.py, org_extras.py); website: https://d2l.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_founded**: 1999-04-01 (schema.org JSON-LD foundingDate on https://www.d2l.com/)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf, re-read 2026-11-08)
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Oral Roberts University | Customer Success | D2L
- **contract_description**: Oral Roberts University | Customer Success | D2L (the record's title; the source publishes no separate description)
- **contract_link**: https://www.d2l.com/why-d2l/customers/oral-roberts-university/
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
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Oral Roberts University — 7777 South Lewis Ave, Tulsa, OK, 74171 ⏎ SUBMIT TO: invoices@oru.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: include, but are not limited to, purchase order) ⏎ FROM / REMIT TO: D2L Corporation (as printed on the vendor's site: https://www.d2l.com/) — 137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Oral Roberts University | Customer Success | D2L
- **invoice_card_json**: {"bill_to": {"legal_name": "Oral Roberts University", "legal_name_is_published": true, "address": "7777 South Lewis Ave, Tulsa, OK, 74171", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@oru.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: include, but are not limited to, purchase order) (as printed on https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%2020)"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["invoices@oru.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf", "quote: \"ormed on University premises/grounds. Invoices are a request for payment from a Vendor to University. All invoices must be sent directly to invoices@oru.edu. Pu\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Mimecast", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00188"], "buyer_facts": ["address and phone: the buyer's own site, https://oru.edu/campus-visitation/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://www.d2l.com/about/locations/ (tools/org_contacts.py, org_extras.py)", "website: https://d2

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf | 2026-11-08 | ok |  | purchase-order terms published (as published: include, but are not limited to, purchase order) |  |  |  |  |  |  | o parties (buyer and seller/provider) which defines the rights and obligations of both parties.. Contracts include, but are not limited to, purchase orders, grants, sub- contracts, licenses, leases, Independent Contracto |

## Buyer site facts (org_extras, oru.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Oral Roberts University
- **legal_name_url**: https://oru.edu/
- **legal_name_quote**: Oral Roberts University | Spirit-Empowered Christian Education --> Skip to content --> Visit Request Info Student Stories N
- **logo_url**: https://xab3h1j8dc.cloudimg.io/oru.edu/_resources/images/Oral-Roberts-University-Logo-Tan-udpated.png
- **logo_basis**: logo image on the site
- **domain**: oru.edu
- **key**: lead:dfc738eca5033171
- **name**: Oral Roberts University
- **website**: https://oru.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: President University
- **legal_name_stated_url**: https://oru.edu/about-oru/index.php
- **legal_name_stated_quote**: Newsroom Pres Wilson Give Close About ORU Overview Vision & Mission Board of Trustees Office of the President University Administration Visit Information Virtual Tour Accreditation Unprecedented Growth Academics Overview
- **mentions**: {'payment_method': {'text': 'interactive virtual tour or schedule a visit today to step inside our 200-foot-tall Pra', 'url': 'https://oru.edu/about-oru/index.php', 'quote': 'tic, art-deco buildings, each of which symbolizes an element of our Christian faith. Experience our interactive virtual tour or schedule a visit today to step inside our 200-foot-tall Prayer Tower, take a stroll around the massive columns surrounding our Learn'}, 'tax_exempt': {'text': 'Tax-exempt Status Oral Roberts University is a Section 501(c)(3) tax exempt entity', 'url': 'https://oru.edu/alumni-and-friends/developme
- **linkedin_url**: https://www.linkedin.com/school/oral-roberts-university/
- **tel_links**: 1-800-678-8876; 1-9184956161

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "1.800.678.8876", "phone_url": "https://oru.edu/admissions/visit-campus/contact-us.php", "address": "7777 South Lewis Ave, Tulsa, OK, 74171", "address_country": "US", "address_url": "https://oru.edu/campus-visitation/", "address_method": "json-ld", "address_quote": "rved. Oral Roberts University Accreditations and Memberships Legal Disclosures* 7777 South Lewis Ave. Tulsa, Oklahoma 74171 (918) 495-6161 NOTICE OF NONDISCRIMINATORY POLICY AS TO", "domain": "oru.edu", "key": "lead:dfc738eca5033171", "name": "oru.edu", "website": "https://oru.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, d2l.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: D2L Corporation
- **legal_name_url**: https://www.d2l.com/
- **legal_name_quote**: hat is an LMS? What is Asynchronous Learning? What’s new at D2L Best Corporate LMS Copyright © 2026 D2L Corporation. All rights reserved. Status Privacy Notice Do Not Sell My PI Terms of Use Accessibility Conformanc
- **logo_url**: https://www.d2l.com/wp-content/uploads/2022/08/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: d2l.com
- **key**: vendor:d2l.com
- **name**: d2l.com
- **website**: https://d2l.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: D2L
- **jsonld_legal_name**: D2L Inc.
- **jsonld_alternate_name**: Desire2Learn
- **jsonld_phone**: 1-888-772-0325
- **jsonld_logo**: https://www.d2l.com/wp-content/uploads/2026/04/img-logo-D2L_author.png
- **jsonld_url**: https://www.d2l.com/
- **jsonld_founding_date**: 1999-04-01
- **jsonld_same_as**: https://www.facebook.com/D2Linc; https://x.com/D2L; https://www.linkedin.com/company/d2l/; https://www.youtube.com/user/desire2learninc; https://www.instagram.com/d2l/; https://en.wikipedia.org/wiki/D2L; https://www.wikidata.org/wiki/Q5264469; https://www.crunchbase.com/organization/desire2learn
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.d2l.com\/","url":"https:\/\/www.d2l.com\/","name":"D2L Brightspace Learning Platform With Built-In AI","isPartOf":{"@id":"https:\/\/www.d2l.com\/#website"},"about":{"@id":"https:\/\/www.d2l.com\/#organization"},"pri
- **jsonld_page**: https://www.d2l.com/
- **legal_name_stated**: Rideau Hall Foundation
- **legal_name_stated_url**: https://www.d2l.com/about/leadership/
- **legal_name_stated_quote**: Director David Johnston was Canada’s 28th governor general. During his mandate, he established the Rideau Hall Foundation (RHF), a registered charity that supports and amplifies the Office of the Governor General in its w
- **mentions**: {'payment_method': {'text': 'interactive learning experiences', 'url': 'https://www.d2l.com/', 'quote': 'nuing Education Faculty Burn Out Streamline Workflows D2L for K-12 Engage and inspire students with interactive learning experiences. Learn More use case Personalized and Engaged Learning Professional Learning for Educators Reduce T'}}
- **linkedin_url**: https://www.linkedin.com/company/d2l/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "137 Glasgow Street Suite 560, Kitchener, ON, N2G 4X8", "address_country": "CA", "address_url": "https://www.d2l.com/about/locations/", "address_method": "address-tag", "address_quote": "D2L Corporation Global Headquarters 137 Glasgow Street Suite 560 Kitchener, ON N2G 4X8 1-519-772-0325 (Local) 1-888-772-0325 (Toll Free, North America) 1-519-772-0324", "phone": "1-519-772-0325", "phone_url": "https://www.d2l.com/about/locations/", "domain": "d2l.com", "key": "vd:d2l.com", "name": "d2l.com", "website": "https://d2l.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Oral Roberts University | Q3121493 | official website on the organisation's domain (http://oru.edu) + name |  | Oral Roberts University | Université Oral Roberts | university; private not-for-profit educational institution; church college |  | United States | 1963-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:dfc738eca5033171",
 "ap_contact_team": {
  "emails": [
   "invoices@oru.edu",
   "studentaccounts@oru.edu",
   "vendors@oru.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoices@oru.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://oru.edu/pdfs/finance/Purchasing%20Policy%20-%20Final%20-%20Appoved%20Aug%2028%202023.pdf",
    "quote": "ormed on University premises/grounds. Invoices are a request for payment from a Vendor to University. All invoices must be sent directly to invoices@oru.edu. Purchase Requisitions are internal forms used to request permission to buy Goods and/or Services. They are used to identify the Good",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Oral Roberts University",
    "task_id": "CL-WS-00188"
   },
   {
    "email": "studentaccounts@oru.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://oru.edu/tuition-and-financial-aid/online/index.php",
    "quote": "​​ Contact Us For any questions or assistance, please call Nelnet at (800) 609-8056 or the Student Accounts Office at 918.495.6370 or email studentaccounts@oru.edu . Scholarship Opportunities Degree Completer Scholarship Students who previously left ORU and have since applied to return in",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "oru.edu",
    "task_id": "CL-LD-11997"
   },
   {
    "email": "vendors@oru.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://oru.edu/chapel/Intl%20Supplier%20Registration%20Form%202019-2020.pdf",
    "quote": "____________________ VENDOR/SUPPLIER E-Mail/Fax completed form to: Oral Roberts University REGISTRATION FORM Fax: 918-495-6985 E-mail form: vendors@oru.edu Phone: 918-495-7531/7549 Company/Individual Name Phone Fax Company DBA name - Payments will be made to this name Phone Fax Contact Nam",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "oru.edu",
    "task_id": "CL-LD-11997"
   },
   {
    "email": "vendors@oru.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://oru.edu/pdfs/finance/Vendor%20Registration%20Form%20Rev%2031120.pdf",
    "quote": "Requesting Form ____________________ REGISTRATION FORM E-Mail/Fax completed form to: Oral Roberts University Fax: 918-495-6985 E-mail form: vendors@oru.edu Phone: 918-495-7531 Company/Individual Name on IRS Record Phone Fax Company DBA name - Payments will be made to this name Phone Fax Co",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Oral Roberts University",
    "task_id": "CL-WS-00188"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of oru.edu (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of oru.edu (60 pages, robots.txt respected), no AI, no search engine",
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

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

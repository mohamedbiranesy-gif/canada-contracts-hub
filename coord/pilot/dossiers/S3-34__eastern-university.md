# S3-34 — Eastern University ⇄ D2L Corporation

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Eastern University — 1300 Eagle Road, St. Davids, PA 19087-3696
SUBMIT TO: student.accounts@eastern.edu (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Login - Eastern University
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 56
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Eastern University (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: D2L Corporation | subject: Login - Eastern University | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://eastern.brightspace.com/d2l/login | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=You can find us at our headquarters in Kitchener, Ontario and in satellite offices across the globe. | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor D2L Corporation
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:52de48902e881250
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Eastern University
- **buyer_website**: http://www.eastern.edu/
- **buyer_address**: 1300 Eagle Road, St. Davids, PA 19087-3696
- **buyer_phone**: 1-800-732-7669
- **buyer_contact_evidence_url**: https://eastern.edu/about/contact-eastern-university
- **buyer_legal_name_as_published**: Eastern University
- **buyer_logo_url**: https://eastern.edu/sites/default/files/EU2017_original_logo.svg
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q5330550; university; private not-for-profit educational institution; church college; Christian educational institution
- **buyer_founded**: 1925-01-01 (Wikidata Q5330550, official website on the organisation's domain (http://www.eastern.edu) + name; 2026-11-08)
- **buyer_employees**: 663 (Wikidata Q5330550, official website on the organisation's domain (http://www.eastern.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://eastern.edu/about/contact-eastern-university (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: student.accounts@eastern.edu
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.eastern.edu/sites/default/files/inline-files/2024-2025%20Financial%20Aid%20Facts-%20UNDG%20NT%207.pdf
- **email_evidence_quote**: tern student account, sending refunds, and helping to set-up payment plans. Student Accounts can be reached at 610-341-5831 or via email at student.accounts@eastern.edu. Questions? Contact the Financial Aid Office at 610-225-5102 or by email at
- **email_evidence_context**: and University aid based on the date the withdrawal takes place. If financial aid funding is returned, the student may owe a balance to the University. Students owing a balance should contact the Student Accounts Office to make payment arrangements- student.accounts@eastern.edu or 610-341-5831. Additionally, students who withdraw from the University are not considered registered students. Therefore: Enrollment verification will be reported as “not enrolled” to lenders and loan servicing agencies. Students may need to conta (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: student.accounts@eastern.edu (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.eastern.edu/sites/default/files/inline-files/2024-2025%20Financial%20Aid%20Facts-%20UNDG%20NT%207.pdf | quote: "tern student account, sending refunds, and helping to set-up payment plans. Student Accounts can be reached at 610-341-5831 or via email at student.accounts@eas" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00165
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; adkim=r; aspf=r; rua=mailto:bounce@eastern.edu
- **dmarc_record_domain**: eastern.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.google.com include:a._spf.brightspace.com include:et._spf.pardot.com include:secure.giftlegacy.com include:emailers.eastern.edu include:mail.zendesk.com  ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Eastern University — 1300 Eagle Road, St. Davids, PA 19087-3696 ⏎ SUBMIT TO: student.accounts@eastern.edu (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Login - Eastern University
- **invoice_card_json**: {"bill_to": {"legal_name": "Eastern University", "legal_name_is_published": true, "address": "1300 Eagle Road, St. Davids, PA 19087-3696", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "student.accounts@eastern.edu", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "812930345RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "D2L Corporation", "bn9": "812930345", "neq": "1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)", "remit_address": "137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8, CA"}, "follow_up": {"ap_phone": 
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: D2L Corporation
- **vendor_legal_name**: D2L Corporation
- **vendor_trading_name**: D2L® (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1177781433
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8, CA
- **vendor_neq**: 1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — ONTARIO : Loi sur les sociétés par actions, L.R.O. 1990, c. B.16
- **vendor_activity_code**: CAE 9999 — Systèmes de logiciels d'apprentissage
- **vendor_employees_quebec**: De 11 à 25
- **vendor_directors_range**: 3 to 15 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2014-06-20
- **vendor_address**: Kitchener, ON, CA
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=You can find us at our headquarters in Kitchener, Ontario and in satellite offices across the globe.
- **vendor_bn9**: 812930345
- **vendor_gst_hst_derived**: 812930345RT0001
- **vendor_website**: https://www.d2l.com/
- **vendor_phone**: 1-519-772-0325
- **vendor_contact_evidence_url**: https://www.d2l.com/about/locations/
- **vendor_logo_url**: https://www.d2l.com/wp-content/uploads/2022/08/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.d2l.com/ (D2L Brightspace Learning Platform With Built-In AI Skip to main content English English English (APAC) English (IN) Spanish (EU) Español (LATAM) Français (CA) N)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: Québec REQ (NEQ): 1177781433 status Québec REQ (NEQ): Immatriculée (2022-07-05); Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-01-01; phone / role e-mails / logo: the vendor's own site, https://www.d2l.com/about/locations/ (tools/org_contacts.py, org_extras.py); website: https://www.d2l.com/; NEQ: 1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2022-07-05); Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 2014-01-01
- **vendor_years_in_business**: 12.9 (since 2014-01-01, registry date)

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor D2L Corporation
- **contract_title**: Login - Eastern University
- **contract_description**: Login - Eastern University (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-03
- **contract_link**: https://eastern.brightspace.com/d2l/login
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 812930345RT0001

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Eastern University — 1300 Eagle Road, St. Davids, PA 19087-3696 ⏎ SUBMIT TO: student.accounts@eastern.edu (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: D2L Corporation — Kitchener, ON, CA | GST/HST 812930345RT0001 (account derived from the BN9) | NEQ 1177781433 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Login - Eastern University
- **invoice_card_json**: {"bill_to": {"legal_name": "Eastern University", "legal_name_is_published": true, "address": "1300 Eagle Road, St. Davids, PA 19087-3696", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "student.accounts@eastern.edu", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "812930345RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "D2L Corporation", "bn9": "812930345", "neq": "1177781433 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)", "remit_address": "137 Glasgow Street, Suite 560, Kitchener, ON, N2G 4X8, CA"}, "follow_up": {"ap_phone": 
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["student.accounts@eastern.edu (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.eastern.edu/sites/default/files/inline-files/2024-2025%20Financial%20Aid%20Facts-%20UNDG%20NT%207.pdf", "quote: \"tern student account, sending refunds, and helping to set-up payment plans. Student Accounts can be reached at 610-341-5831 or via email at student.accounts@eas\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00165"], "buyer_facts": ["address and phone: the buyer's own site, https://eastern.edu/about/contact-eastern-university (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: Québec REQ (NEQ): 1177781433 status Québec REQ (NEQ): Immatriculée (2022-07-05)", "Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / R

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.eastern.edu/admissions-financial-aid/financial-aid-office/eligibility-and-forms/satisfactory-academic-progress | 2026-11-08 | ok |  |  |  | 610-341-5831 |  |  |  |  |  |

## Buyer site facts (org_extras, eastern.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Eastern University
- **legal_name_url**: https://eastern.edu/
- **legal_name_quote**: Eastern University | Christian University in Philadelphia | Undergraduate, Graduate and Online Degrees Skip to main co
- **logo_url**: https://eastern.edu/sites/default/files/EU2017_original_logo.svg
- **logo_basis**: logo image in the site header
- **domain**: eastern.edu
- **key**: lead:52de48902e881250
- **name**: Eastern University
- **website**: https://eastern.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Eastern University's College
- **legal_name_stated_url**: https://eastern.edu/about
- **legal_name_stated_quote**: n student body, faculty, and administration. Colleges & Schools The College of Arts and Humanities: Eastern University's College of Arts and Humanities (CAH) houses majors and minors in the humanities and performing arts. The Co

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1300 Eagle Road, St. Davids, PA 19087-3696", "address_country": "US", "address_url": "https://eastern.edu/about/contact-eastern-university", "address_method": "pattern", "address_quote": "tact Eastern University Contact Eastern University Campus Operator 610-341-5800 1300 Eagle Road St. Davids, PA 19087-3696 You may also directly contact the various departments", "phone": "1-800-732-7669", "phone_url": "https://eastern.edu/admissions-financial-aid/graduate-online-undergraduate-admissions/contact-graduate-and-online", "domain": "eastern.edu", "key": "lead:52de48902e881250", "name": "Eastern University", "website": "https://eastern.edu/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Eastern University | Q5330550 | official website on the organisation's domain (http://www.eastern.edu) + name |  | Eastern University | Université de l'Est | university; private not-for-profit educational institution; church college; Christian educational institution |  | United States | 1925-01-01 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:52de48902e881250",
 "ap_contact_team": {
  "emails": [
   "student.accounts@eastern.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "student.accounts@eastern.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastern.edu/admissions-financial-aid/financial-aid-office/eligibility-and-forms/satisfactory-academic-progress",
    "quote": "dent may owe a balance to the University. Students owing a balance should contact the Student Accounts Office to make payment arrangements- student.accounts@eastern.edu or 610-341-5831. Additionally, students who withdraw from the University are not considered registered students. Therefor",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Eastern University",
    "task_id": "CL-LT-00010"
   },
   {
    "email": "student.accounts@eastern.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.eastern.edu/sites/default/files/inline-files/2024-2025%20Financial%20Aid%20Facts-%20UNDG%20NT%207.pdf",
    "quote": "tern student account, sending refunds, and helping to set-up payment plans. Student Accounts can be reached at 610-341-5831 or via email at student.accounts@eastern.edu. Questions? Contact the Financial Aid Office at 610-225-5102 or by email at",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Eastern University",
    "task_id": "CL-WS-00165"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.eastern.edu (60 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 19)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-01951:e8fa37de-e5b3-4690-9330-afe42c0586e6 | Red Deer Polytechnic | Red Deer Polytechnic - Negotiated Request for Proposal - Learning Management System (LMS ) | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01951 |
| ca_bidsandtenders:852b0bf1-b12e-4541-8487-7045b6dacafa:1 | Municipality of Clarington | Learning Management System |  |  |  | https://clarington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/852b0bf1-b12e-4541-8487-7045b6dacafa |
| ca_bidsandtenders:156b602d-cf79-4b84-a630-c854f0f21834:1 | City of Waterloo | Learning Management System |  |  |  | https://waterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/156b602d-cf79-4b84-a630-c854f0f21834 |
| ca_merx:2486883468:1 | University Of Calgary | Learning Management System (LMS) |  |  |  | https://www.merx.com/universityofcalgary/solicitations/Learning-Management-System-LMS/0000246846?origin=0 |
| ca_merx:2165019645:1 | George Brown College | Learning Management System | 1.0 |  |  | https://www.merx.com/oupma/georgebrown/solicitations/Learning-Management-System/0000221122?origin=0 |
| ca_merx:2006612454:1 | Brock University | Modern Cloud-Based Learning Management System |  |  |  | https://www.merx.com/oupma/brocku/solicitations/Modern-Cloud-Based-Learning-Management-System/0000211285?origin=0 |
| canada_federal:cb:CW2355334 | Department of Public Works and Government Services (PSPC) | ProServices SA – D2L Corporation |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2355334 |
| canada_federal:cb:CW2441855 | Department of Public Works and Government Services (PSPC) | TSPS SA (Task Based) – D2L Corporation |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2441855 |
| private_press:794233bb4145c8e7cdf17b99547974a1e07a80c6 | Van Lang Investment and Education Management Group Corporation (Van Lang Education Group) | D2L Signs First Strategic Vietnam Customer as Van Lang Education Group Adopts D2L Brightspace |  |  |  | https://www.newswire.ca/news-releases/d2l-signs-first-strategic-vietnam-customer-as-van-lang-education-group-adopts-d2l-brightspace-812975353.html |
| private_press:0c3794d5505bc42d10b62c4866618e482928a3a5 | University of Ottawa | University of Ottawa Deepens Strategic Relationship with a 12-Year Renewal of D2L Brightspace |  |  |  | https://www.newswire.ca/news-releases/university-of-ottawa-deepens-strategic-relationship-with-a-12-year-renewal-of-d2l-brightspace-873135986.html |
| private_press:ddd6a291a865fced13db2a5d62c5291716fcca43 | Loyola University Chicago | Loyola University Chicago Selects D2L Brightspace as Its Next-Generation Learning Platform |  |  |  | https://www.newswire.ca/news-releases/loyola-university-chicago-selects-d2l-brightspace-as-its-next-generation-learning-platform-836650163.html |
| private_press:db2e14eb0dcc26197c337d59e67ead66646bf28b | Midwestern University | Midwestern University Selects D2L to Support AI Innovation in Teaching and Learning |  |  |  | https://www.newswire.ca/news-releases/midwestern-university-selects-d2l-to-support-ai-innovation-in-teaching-and-learning-868245884.html |
| private_press:a36d3c0f4638d63ef4ccc49d981ccecd62100b0b | Rasmussen University (American Public Education, Inc.) | Rasmussen University Selects D2L Brightspace to Deliver Inclusive AI in Education |  |  |  | https://www.newswire.ca/news-releases/rasmussen-university-selects-d2l-brightspace-to-deliver-inclusive-ai-in-education-894898316.html |
| seao_quebec:1222576:d2l-corporation | Université McGill | Learning Management System | 3373502.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d760a2a3-1284-4bfd-bfa3-c7e409c63390 |
| seao_quebec:1250822:d2l-corporation | CEGEP de Saint-Hyacinthe | Plateforme de formation en ligne | 69548.81 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cee99611-3295-40db-9ca4-6af2373e2033 |
| us_state_delaware:5775:D2L_Ltd | State of Delaware - Government Support Services (Contracting) | DTCC Learning Management System |  |  |  | http://mmp.delaware.gov/Contracts/Details/5775 |
| usaspending:CONT_AWD_140A2325P0187_1450_-NONE-_-NONE- | Department of the Interior | SIPI BRIGHTSPACE LICENSING | 247223.01 |  |  | https://www.usaspending.gov/award/CONT_AWD_140A2325P0187_1450_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:an:E60ZH-1700LS:034:ZH | Public Works and Government Services Canada | End-to-End Learning Services (Excludes COTS Training) |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| canada_sosa:CW2382809 | Public Works and Government Services Canada | PSPC Cloud Method of Supply ? D2L Corporation |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2382809 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

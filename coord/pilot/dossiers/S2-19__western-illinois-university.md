# S2-19 — Western Illinois University ⇄ Modern Campus

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade B · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Western Illinois University — 1 University Circle, Macomb, IL 61455
SUBMIT TO: accounts-payable@wiu.edu (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: MODERN CAMPUS INC. — 40 Holly Street, Suite 800, Toronto, ON, M4S 3C3, Canada | GST/HST 897424255 (Canada's Business Registries, ON 1000790550, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1179600292
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/bu
DESCRIPTION: Western Illinois University Boosts Student Engagement with Points
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 73
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Western Illinois University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Modern Campus | subject: Western Illinois University Boosts Student Engagement with Points | published by: the Canada-located vendor's own website | record: https://moderncampus.com/success-stories/western-illinois-university-boosts-student-engagement-with-points | vendor in Canada because: vendor located in Canada (stories; contract data vendor country)=moderncampus.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:fd994df9d3b74588
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Western Illinois University
- **buyer_website**: https://wiu.edu/
- **buyer_address**: 1 University Circle, Macomb, IL 61455
- **buyer_contact_evidence_url**: https://www.wiu.edu/visit/
- **buyer_legal_name_as_published**: Western Illinois University
- **buyer_logo_url**: https://www.wiu.edu/_resources/_redesign/images/wlogo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/western-illinois-university/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1474005; university; public educational institution of the United States
- **buyer_founded**: 1899-00-00 (Wikidata Q1474005, official website on the organisation's domain (http://www.wiu.edu) + name; 2026-11-08)
- **buyer_employees**: 1280 (Wikidata Q1474005, official website on the organisation's domain (http://www.wiu.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.wiu.edu/visit/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts-payable@wiu.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.wiu.edu/business_services/accounting/acctpay.php
- **email_evidence_quote**: nts Payable division is located in Sherman Hall 220. Accounts Payable can be contacted by phone at 309-298-1811; fax 309-298-2811; or email accounts-payable@wiu.edu . Accounts Payable processes Direct Pay Authorizations and Travel Vouchers among many other things. Please allow 3 to 5 busin
- **email_evidence_context**: Services ≡ Section Menu WIU Home > Business Services > Accounting Accounts Payable The Business Services Accounts Payable division is located in Sherman Hall 220. Accounts Payable can be contacted by phone at 309-298-1811; fax 309-298-2811; or email accounts-payable@wiu.edu . Accounts Payable processes Direct Pay Authorizations and Travel Vouchers among many other things. Please allow 3 to 5 business days for payment processing once documents are received in Business Services. Incomplete or incorrect documentation will (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts-payable@wiu.edu (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.wiu.edu/business_services/accounting/acctpay.php | quote: "nts Payable division is located in Sherman Hall 220. Accounts Payable can be contacted by phone at 309-298-1811; fax 309-298-2811; or email accounts-payable@wiu" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-22165
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Google Workspace
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:sysops@wiu.edu; pct=1; adkim=r; aspf=r
- **dmarc_record_domain**: wiu.edu
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:143.43.222.19 ip4:143.43.248.75 ip4:143.43.193.0/24 a:smtp.wiu.edu include:_spf.google.com include:_spf.regroupcloud.com include:a._spf.brightspace.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 309-298-1811 (as printed on https://www.wiu.edu/business_services/accounting/acctpay.php, re-read 2026-11-08)
- **payment_terms_as_published**: paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/business_services/billing/payments.php, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/business_services/billing/payments.php, re-read 2026-11-08)", "ap_phone": "309-298-1811 (as printed on https://www.wiu.edu/business_services/accounting/acctpay.php, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Western Illinois University — 1 University Circle, Macomb, IL 61455 ⏎ SUBMIT TO: accounts-payable@wiu.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MODERN CAMPUS INC. — 40 Holly Street, Suite 800, Toronto, ON, M4S 3C3, Canada | GST/HST 897424255 (Canada's Business Registries, ON 1000790550, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1179600292 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/bu ⏎ DESCRIPTION: Western Illinois University Boosts Student Engagement with Points
- **invoice_card_json**: {"bill_to": {"legal_name": "Western Illinois University", "legal_name_is_published": true, "address": "1 University Circle, Macomb, IL 61455", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts-payable@wiu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/business_services/billing/payments.php, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "897424255RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MODERN CAMPUS INC.", "bn9": "897424255 (Canada's Business Registries, ON 1000790550, 2026-1
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Modern Campus
- **vendor_legal_name**: MODERN CAMPUS INC.
- **vendor_trading_name**: Modern Campus
- **vendor_registry_id**: Québec REQ (NEQ): 1179600292; 1000790550 (ON)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 2482 Yonge Street #1366, Toronto (Ontario), M4P2H5
- **vendor_neq**: 1179600292 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — ONTARIO : Loi sur les sociétés par actions, L.R.O. 1990, c. B.16
- **vendor_activity_code**: CAE 9999 — Société de développement de logiciels
- **vendor_employees_quebec**: De 1 à 5
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 40 Holly Street, Suite 800, Toronto, ON, M4S 3C3, Canada
- **vendor_country_basis**: vendor located in Canada (stories; contract data vendor country)=moderncampus.com
- **vendor_bn9**: 897424255 (Canada's Business Registries, ON 1000790550, 2026-11-08)
- **vendor_gst_hst_derived**: 897424255RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://moderncampus.com/
- **vendor_emails**: sales@moderncampus.com; support@moderncampus.com; marketing@moderncampus.com
- **vendor_phone**: +14164800500 (tel: link on https://moderncampus.com/)
- **vendor_contact_evidence_url**: https://moderncampus.com/contact-us
- **vendor_logo_url**: https://moderncampus.com/hubfs/logo-school-1.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/moderncampus/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Québec REQ (NEQ): 1179600292; 1000790550 (ON) status Québec REQ (NEQ): Immatriculée (2024-03-06) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1000790550, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2018-05-16; phone / role e-mails / logo: the vendor's own site, https://moderncampus.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://moderncampus.com/ (site answers); NEQ: 1179600292 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2024-03-06)
- **vendor_incorporation_date**: 2018-05-16
- **vendor_years_in_business**: 8.5 (since 2018-05-16, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1000790550, 2026-11-08

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Western Illinois University Boosts Student Engagement with Points
- **contract_description**: Western Illinois University Boosts Student Engagement with Points (the record's title; the source publishes no separate description)
- **contract_link**: https://moderncampus.com/success-stories/western-illinois-university-boosts-student-engagement-with-points
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 897424255RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Western Illinois University — 1 University Circle, Macomb, IL 61455 ⏎ SUBMIT TO: accounts-payable@wiu.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: MODERN CAMPUS INC. — 40 Holly Street, Suite 800, Toronto, ON, M4S 3C3, Canada | GST/HST 897424255 (Canada's Business Registries, ON 1000790550, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1179600292 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/bu ⏎ DESCRIPTION: Western Illinois University Boosts Student Engagement with Points
- **invoice_card_json**: {"bill_to": {"legal_name": "Western Illinois University", "legal_name_is_published": true, "address": "1 University Circle, Macomb, IL 61455", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts-payable@wiu.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "paid in full or a payment agreement is not made within 90 days (as printed on https://www.wiu.edu/business_services/billing/payments.php, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: USD (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "897424255RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "MODERN CAMPUS INC.", "bn9": "897424255 (Canada's Business Registries, ON 1000790550, 2026-1
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounts-payable@wiu.edu (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.wiu.edu/business_services/accounting/acctpay.php", "quote: \"nts Payable division is located in Sherman Hall 220. Accounts Payable can be contacted by phone at 309-298-1811; fax 309-298-2811; or email accounts-payable@wiu\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-22165"], "buyer_facts": ["address and phone: the buyer's own site, https://www.wiu.edu/visit/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Québec REQ (NEQ): 1179600292", "1000790550 (ON) status Québec REQ (NEQ): Immatriculée (

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.wiu.edu/business_services/accounting/acctpay.php | 2026-11-08 | ok |  |  |  | 309-298-1811 |  |  |  |  |  |

## Buyer site facts (org_extras, wiu.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Western Illinois University
- **legal_name_url**: https://www.wiu.edu/
- **legal_name_quote**: Western Illinois University - Your potential. Our purpose. Mental Health Resources --> Skip to main content Parents & Families
- **logo_url**: https://www.wiu.edu/_resources/_redesign/images/wlogo.png
- **logo_basis**: logo image in the site header
- **domain**: wiu.edu
- **key**: lead:fd994df9d3b74588
- **name**: Western Illinois University
- **website**: https://wiu.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Western Illinois University
- **legal_name_stated_url**: https://www.wiu.edu/about/
- **legal_name_stated_quote**: About Western Illinois University - WIU Skip to main content Parents & Families Visitors International Students Libraries Course Offe
- **mentions**: {'payment_method': {'text': 'interact', 'url': 'https://www.wiu.edu/fortheW/', 'quote': 'hancing technology, laboratory settings, and classrooms where students discover, learn, create, and interact. Growing endowed support for future enhancements and opportunities so Western can continue to evolv'}}
- **linkedin_url**: https://www.linkedin.com/school/western-illinois-university/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "1 University Circle, Macomb, IL 61455", "address_country": "US", "address_url": "https://www.wiu.edu/visit/", "address_method": "pattern", "address_quote": "s: Accessibility Employment Sustainability Veterans Western Illinois University 1 University Circle Macomb, IL 61455 USA Phone: (309) 298-1414 info@wiu.edu © 2026 Western Illinois", "emails": "info@wiu.edu", "emails_url": "https://www.wiu.edu/visit/", "domain": "wiu.edu", "key": "lead:fd994df9d3b74588", "name": "wiu.edu", "website": "https://wiu.edu/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, moderncampus.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Modern Campus is a registered trademark of Modern Campus USA Inc
- **legal_name_url**: https://moderncampus.com/
- **legal_name_quote**: hat's happening around campus. Join Our Mailing List Get the latest delivered to your inbox! © 2026 Modern Campus is a registered trademark of Modern Campus USA Inc. All rights reserved. Privacy Policy | Accessibility
- **logo_url**: https://moderncampus.com/hubfs/logo-school-1.svg
- **logo_basis**: logo image in the site header
- **domain**: moderncampus.com
- **key**: vendor:moderncampus.com
- **name**: moderncampus.com
- **website**: https://moderncampus.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Success Story Ferris State University
- **legal_name_stated_url**: https://moderncampus.com/
- **legal_name_stated_quote**: tion Discover how workforce pell is expanding access to short-term workforce programs. Learn More → Success Story Ferris State University Increased Website Clickthrough by 2800% Using Personalization How a top-ranked national university
- **mentions**: {'payment_method': {'text': 'interaction with the institution—improving their likelihood to succeed within their pro', 'url': 'https://moderncampus.com/', 'quote': 'leges and universities can ensure they’re delivering a high-quality experience with every student’s interaction with the institution—improving their likelihood to succeed within their program, increasing their openness to return for ongoing learning and to con'}}
- **linkedin_url**: https://www.linkedin.com/company/moderncampus/
- **tel_links**: +14164800500; +18664030500

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2482 Yonge Street #1366 Toronto, Ontario M4P 2H5", "address_country": "CA", "address_url": "https://moderncampus.com/contact-us", "address_method": "pattern", "address_quote": "rt The EvoLLLution Contact Information 2482 Yonge Street #1366 Toronto, Ontario M4P 2H5 330 N Lantana St Suite 28 PMB 1014 Camarillo, CA 93010 (416) 480-0500 (866) 403", "emails": "sales@moderncampus.com; support@moderncampus.com", "emails_url": "https://moderncampus.com/contact-us", "domain": "moderncampus.com", "key": "vd:moderncampus.com", "name": "moderncampus.com", "website": "https://moderncampus.com/", "kind": "vendor", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Western Illinois University | Q1474005 | official website on the organisation's domain (http://www.wiu.edu) + name |  | Western Illinois University | Western Illinois University | university; public educational institution of the United States |  | United States | 1899-00-00 |  |
| v | MODERN CAMPUS INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:fd994df9d3b74588",
 "ap_contact_team": {
  "emails": [
   "accounts-payable@wiu.edu",
   "info@wiu.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounts-payable@wiu.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wiu.edu/business_services/accounting/acctpay.php",
    "quote": "nts Payable division is located in Sherman Hall 220. Accounts Payable can be contacted by phone at 309-298-1811; fax 309-298-2811; or email accounts-payable@wiu.edu . Accounts Payable processes Direct Pay Authorizations and Travel Vouchers among many other things. Please allow 3 to 5 busin",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "wiu.edu",
    "task_id": "CL-LD-22165"
   },
   {
    "email": "info@wiu.edu",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wiu.edu/",
    "quote": "Accessibility Employment Sustainability Veterans Western Illinois University 1 University Circle Macomb, IL 61455 USA Phone: (309) 298-1414 info@wiu.edu © 2026 Western Illinois University. All Rights Reserved. | Web Privacy Policy",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "wiu.edu",
    "task_id": "CL-LD-22165"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of wiu.edu (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of wiu.edu (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 6)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-08194:faac7d84-90c4-4246-b47d-2259c97d731b | Northern Alberta Institute of Technology (NAIT) | Northern Alberta Institute of Technology (NAIT) - Negotiated Request for Proposal - Enrolment Management Software | 1201139.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-08194 |
| ca_merx:2553739575:1 | University Of Calgary | Student Registration System |  |  |  | https://www.merx.com/universityofcalgary/solicitations/Student-Registration-System/0000252247?origin=0 |
| ca_merx:2295098937:1 | University of Toronto – St. George Campus – Procurement Services | Continuing Education Enrolment Management System | 309120.0 |  |  | https://www.merx.com/uoft/uoft-stgeorge-procurement/solicitations/Continuing-Education-Enrolment-Management-System/0000232112?origin=0 |
| ca_saskatchewan:eab3c7d0-08be-4817-9714-4d2b3057bbc1:0 | University of Saskatchewan | Continuing Education Registration System | 1532000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=eab3c7d0-08be-4817-9714-4d2b3057bbc1 |
| us_state_virginia:2026:PO05257535:SUP250539 | James Madison University | Modern Campus, Extended Education ********* 2027  Subscription Fee, YR 2 per Supplemental Agreement to VIT-200-2016. | 63062.0 |  |  | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:PO05387923:SUP250539 | George Mason University | Year 1: May 1, 2026-April 30, 2027: Lifelong Learning Extended Education Subscription: $59,671.50 / year for up to $2,100,000 in Revenue per year (“Revenue Limi | 224386.66 |  |  | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

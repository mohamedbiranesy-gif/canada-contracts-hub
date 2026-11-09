# S2-30 — Douglas College ⇄ Colleges and Institutes Canada

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Douglas College — 700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/) — buyer tax no. 118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name)
SUBMIT TO: ap@douglascollege.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Colleges and Institutes Canada — 1 Rideau Street,701, ON, K1N8S7, CAN | GST/HST 133165225RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Douglas College (university / college, jurisdiction not stated) — member or regulated payer of a Canadian body (current list): Colleges and 
```

## Relationship
- **rank_group**: GOLD-M
- **data_quality_score**: 80
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Douglas College (university / college, jurisdiction not stated) — member or regulated payer of a Canadian body (current list): Colleges and Institutes Canada | awarded 2026-11-03 | published by: the Canadian body's own current member / participant list | record: https://www.collegesinstitutes.ca/colleges-and-institutes-in-your-community/our-members/ | vendor in Canada because: membership / statutory fee relationship: current list published by the Canadian body (Colleges and Institutes Canada)=Colleges and Institutes Canada, Ottawa, Ontario | status rule: member / regulated payer of a Canadian body (current list read 2026-11-03): Colleges and Institutes Canada
- **how_relationship_was_found**: tools/member_lists.py read the Canadian body's current member / regulated-payer list and matched the buyer by name
- **keys**: lead:3432f27fb425b421
- **tier**: M
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canadian body's own current member / participant list; 0 in the contract dataset)

## Buyer
- **buyer**: Douglas College
- **buyer_website**: https://douglascollege.ca/
- **buyer_address**: 700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/)
- **buyer_phone**: 604 527 5400
- **buyer_contact_evidence_url**: https://www.douglascollege.ca/about-douglas/contacts
- **buyer_legal_name_as_published**: Douglas College
- **buyer_bn_as_published**: 118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 118887579RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.douglascollege.ca/sites/default/files/styles/medium_auto/public/images/EQA-logo-small.gif
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/douglas-college/
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q5301348; college; public university; charitable organization
- **buyer_founded**: 1970-00-00 (Wikidata Q5301348, official website on the organisation's domain (https://www.douglascollege.ca/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 72364863 Q1104069; 77909892 Q1104069; 78236278 Q1104069; 82013598 Q1104069; 93027561 Q1104069; 94843006 Q1104069; 104520 (Wikidata Q5301348, official website on the organisation's domain (https://www.douglascollege.ca/) + name; 2026-11-08)
- **buyer_employees**: 815; 1128; 1193; 1160; 1117; 1227; 677; 698; 757; 729; 774; 746; 766; 800; 784; 830; 923; 956; 946; 1046; 1059; 1077; 10 (Wikidata Q5301348, official website on the organisation's domain (https://www.douglascollege.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.douglascollege.ca/about-douglas/contacts (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap@douglascollege.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance
- **email_evidence_quote**: ance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca NW4740 Accounts Receivable
- **email_evidence_context**: developing financial policies and procedures are also the department's area of responsibility. Contact the Finance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca NW4740 Accounts Receivable accounts@douglascollege.ca NW4740 Get in touch Contact us Addresses and maps Hours of operation Emergency contacts Other Douglas digital properties Bookstore Library and Learning Centre Continuing Education IT Services Por (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap@douglascollege.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance | quote: "ance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00085
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:cybersecalerts@douglascollege.ca; ruf=mailto:cybersecalerts@douglascollege.ca; sp=none; ri=604800
- **dmarc_record_domain**: douglascollege.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:_spf1.douglascollege.ca include:_spf2.douglascollege.ca include:_spf3.douglascollege.ca include:_spf.messagegears.net include:mh.blackboard.com include:_spf.salesforce.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Douglas College — 700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/) — buyer tax no. 118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name) ⏎ SUBMIT TO: ap@douglascollege.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Colleges and Institutes Canada — 1 Rideau Street,701, ON, K1N8S7, CAN | GST/HST 133165225RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Douglas College (university / college, jurisdiction not stated) — member or regulated payer of a Canadian body (current list): Colleges and 
- **invoice_card_json**: {"bill_to": {"legal_name": "Douglas College", "legal_name_is_published": true, "address": "700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/)", "address_is_the_invoice_address": false, "tax_number": "118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name)", "language": "en"}, "submit_to": {"email": "ap@douglascollege.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "v
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Colleges and Institutes Canada
- **vendor_legal_name**: Colleges and Institutes Canada
- **vendor_trading_name**: Collèges et Instituts Canada (other names in the registry)
- **vendor_registry_id**: Corporations Canada (corporation number): 315702; corporation number 315702 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=315702
- **vendor_registered_address**: 350 Sparks St, Ottawa, ON, K1R 7S8, CA
- **vendor_legal_form**: Canada Not-for-profit Corporations Act (Canada (federal))
- **vendor_directors_range**: 14 to 18 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2013-06-26
- **vendor_address**: 1 Rideau Street,701, ON, K1N8S7, CAN
- **vendor_country_basis**: membership / statutory fee relationship: current list published by the Canadian body (Colleges and Institutes Canada)=Colleges and Institutes Canada, Ottawa, Ontario
- **vendor_bn9**: 133165225
- **vendor_gst_hst_derived**: 133165225RT0001
- **vendor_website**: https://www.collegesinstitutes.ca/
- **vendor_emails**: info@cican.org
- **vendor_phone**: 613-746-2222
- **vendor_contact_evidence_url**: https://www.collegesinstitutes.ca/about/contact-us/
- **vendor_logo_url**: https://www.collegesinstitutes.ca/wp-content/themes/cicancorp/assets/images/logo-en.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: http://linkedin.com/company/collegecan
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canadian body's own current member / participant list); registry identity: Corporations Canada (corporation number): 315702; corporation number 315702 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2013-06-26; phone / role e-mails / logo: the vendor's own site, https://www.collegesinstitutes.ca/about/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.collegesinstitutes.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 2013-06-26
- **vendor_years_in_business**: 13.4 (since 2013-06-26, registry date)

## Contract
- **contract_status**: member / regulated payer of a Canadian body (current list read 2026-11-03): Colleges and Institutes Canada
- **award_date**: 2026-11-03
- **contract_link**: https://www.collegesinstitutes.ca/colleges-and-institutes-in-your-community/our-members/
- **source**: the Canadian body's own current member / participant list
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canadian body's own current member / participant list; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 118887579RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 133165225RT0001

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Douglas College — 700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/) — buyer tax no. 118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name) ⏎ SUBMIT TO: ap@douglascollege.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Colleges and Institutes Canada — 1 Rideau Street,701, ON, K1N8S7, CAN | GST/HST 133165225RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Douglas College (university / college, jurisdiction not stated) — member or regulated payer of a Canadian body (current list): Colleges and 
- **invoice_card_json**: {"bill_to": {"legal_name": "Douglas College", "legal_name_is_published": true, "address": "700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada (schema.org JSON-LD PostalAddress on https://www.douglascollege.ca/)", "address_is_the_invoice_address": false, "tax_number": "118887579RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (douglascollege.ca) + name)", "language": "en"}, "submit_to": {"email": "ap@douglascollege.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "v
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["ap@douglascollege.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance", "quote: \"ance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00085"], "buyer_facts": ["address and phone: the buyer's own site, https://www.douglascollege.ca/about-douglas/contacts (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canadian body's own current member / participant list)", "registry identity: Corporations Canada (corporation number): 315702", "corporation number 315702 (

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, douglascollege.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Douglas College
- **legal_name_url**: https://www.douglascollege.ca/
- **legal_name_quote**: Douglas College Skip to main content Skip to footer Douglas College Logins International students Future students C
- **logo_url**: https://www.douglascollege.ca/sites/default/files/styles/medium_auto/public/images/EQA-logo-small.gif
- **logo_basis**: logo image on the site
- **domain**: douglascollege.ca
- **key**: lead:3432f27fb425b421
- **name**: Douglas College
- **website**: https://douglascollege.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: CollegeOrUniversity
- **jsonld_name**: Douglas College
- **jsonld_address**: 700 Royal Ave, New Westminster, BC, V3M 5Z5, Canada
- **jsonld_phone**: 6045275400
- **jsonld_url**: https://www.douglascollege.ca/
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "CollegeOrUniversity", "additionalType": "EducationalOrganization", "description": "Founded in 1970, Douglas College is the largest college in British Columbia, Canada,", "name": "Douglas College", "url": "https://www.douglascollege.ca/", "t
- **jsonld_page**: https://www.douglascollege.ca/
- **legal_name_stated**: 2030 College
- **legal_name_stated_url**: https://www.douglascollege.ca/about-douglas
- **legal_name_stated_quote**: enu President's Office open/close menu Senior Management Team Strategic planning - Looking ahead to 2030 College Board open/close menu Board members Board members' biographies Meeting schedule Committees, Liaison
- **linkedin_url**: https://www.linkedin.com/school/douglas-college/
- **tel_links**: 6045275520; 6045275222; 6045275491; 6045275004; 6045275538; 6047776251; 6047776252; 1 844 515 4352

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "PO Box 2503 , New Westminster, B.C., V3L 5B2", "address_country": "CA", "address_url": "https://www.douglascollege.ca/about-douglas/contacts", "address_method": "pattern", "address_quote": "glas College. Mailing Address Douglas College PO Box 2503 New Westminster, B.C. V3L 5B2 Main Switchboard Phone: 604 527 5400 Legal Documents fax 604 527 5311 Campuses", "phone": "604 527 5400", "phone_url": "https://www.douglascollege.ca/about-douglas/contacts", "emails": "procurement@douglascollege.ca", "emails_url": "https://www.douglascollege.ca/about-douglas/contacts", "domain": "douglascollege.ca", "key": "lead:7cd31a2b33656537", "name": "Douglas College HCI VX RAIL", "website": "https://douglascollege.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, collegesinstitutes.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.collegesinstitutes.ca/wp-content/themes/cicancorp/assets/images/logo-en.png
- **logo_basis**: logo image in the site header
- **domain**: collegesinstitutes.ca
- **key**: vendor:Colleges and Institutes Canada
- **name**: Colleges and Institutes Canada
- **website**: https://collegesinstitutes.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Colleges and Institutes Canada
- **jsonld_logo**: https://www.collegesinstitutes.ca/wp-content/uploads/2025/06/logo-en.png
- **jsonld_url**: https://www.collegesinstitutes.ca/fr/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.collegesinstitutes.ca\/","url":"https:\/\/www.collegesinstitutes.ca\/","name":"Home - Colleges and Institutes Canada","isPartOf":{"@id":"https:\/\/www.collegesinstitutes.ca\/fr\/#website"},"about":{"@id":"https:\/\/
- **jsonld_page**: https://www.collegesinstitutes.ca/
- **legal_name_stated**: Carleton University
- **legal_name_stated_url**: https://www.collegesinstitutes.ca/about/president-ceo/
- **legal_name_stated_quote**: anization for academic journalism. Fluently bilingual, Pari has an MA in international affairs from Carleton University and a BA in French literature from the University of Regina. Related Content October 2, 2026 The Qu
- **linkedin_url**: http://linkedin.com/company/collegecan

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "350 Sparks Street, Suite 301, Ottawa, Ontario K1R 7S8", "address_country": "CA", "address_url": "https://www.collegesinstitutes.ca/about/contact-us/", "address_method": "pattern", "address_quote": "/ Contact Us Contact Us Address: 350 Sparks Street, Suite 301, Ottawa, Ontario K1R 7S8 Telephone: 613-746-2222 Fax: 613-746-6721 Email: info@cican.org Media Contact F", "phone": "613-746-2222", "phone_url": "https://www.collegesinstitutes.ca/about/contact-us/", "emails": "info@cican.org", "emails_url": "https://www.collegesinstitutes.ca/about/contact-us/", "domain": "collegesinstitutes.ca", "key": "vd:collegesinstitutes.ca", "name": "Collèges and Instituts Canada", "website": "https://collegesinstitutes.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Douglas College | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Douglas%20College | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Douglas College | Q5301348 | official website on the organisation's domain (https://www.douglascollege.ca/) + name |  | Douglas College |  | college; public university; charitable organization |  | Canada | 1970-00-00 |  |
| b | Collèges and Instituts Canada |  |  |  |  |  |  |  |  |  |  |
| v | Colleges and Institutes Canada | Q4809677 | official website on the organisation's domain (http://www.collegesinstitutes.ca) + name |  | Colleges and Institutes Canada | Collèges et instituts Canada | nonprofit organization |  | Canada | 1972-00-00 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:3432f27fb425b421",
 "ap_contact_team": {
  "emails": [
   "ap@douglascollege.ca",
   "accounts@douglascollege.ca",
   "procurement@douglascollege.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "ap@douglascollege.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance",
    "quote": "ance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca NW4740 Accounts Receivable",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Douglas College",
    "task_id": "CL-LD-15649"
   },
   {
    "email": "accounts@douglascollege.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance",
    "quote": "NW4740 Accounts Receivable accounts@douglascollege.ca NW4740 Get in touch Contact us Addresses and maps Hours of operation Emergency contacts Other Douglas digital properties Bo",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Douglas College",
    "task_id": "CL-LD-15649"
   },
   {
    "email": "ap@douglascollege.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance",
    "quote": "ance department Enrolment Services is the primary point of contact for all student inquiries. General Inquiries Email Room Accounts Payable ap@douglascollege.ca NW4740 Accounts Receivable",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Douglas College",
    "task_id": "CL-WS-00085"
   },
   {
    "email": "accounts@douglascollege.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/finance",
    "quote": "NW4740 Accounts Receivable accounts@douglascollege.ca NW4740 Get in touch Contact us Addresses and maps Hours of operation Emergency contacts Other Douglas digital properties Bo",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Douglas College",
    "task_id": "CL-WS-00085"
   },
   {
    "email": "procurement@douglascollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.douglascollege.ca/about-douglas/campus-information/finance-and-procurement/procurement",
    "quote": "ew Douglas College and other BC public sector bid opportunities posted, visit the BC Bid . Procurement contacts General Procurement Queries procurement@douglascollege.ca Imran Saeed, Manager, Procurement 604 527 5682",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Douglas College",
    "task_id": "CL-LD-15649"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of douglascollege.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of douglascollege.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of douglascollege.ca (25 pages, robots.txt respected), no AI, no search engine",
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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

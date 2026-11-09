# S5-19 — Catfish Creek Conservation Authority ⇄ Graham Scott Enns LLP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: 2026 · Catfish Creek Conservation Authority — 8079 Springwater Road, Aylmer, Ontario N5H 2R4 — buyer tax no. 106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/)
SUBMIT TO: finance@catfishcreek.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: purchase order must)
FROM / REMIT TO: Graham Scott Enns LLP — 450 Sunset Drive, St Thomas, ON, N5R 5V1, Canada | GST/HST number not public
TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Catfish Creek Conservation Authority (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 78
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Catfish Creek Conservation Authority (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Graham Scott Enns LLP | awarded 2026-02-05, end 2020-12-31 (as printed in the buyer's own council / committee report or minutes: https://www.catfishcreek.ca/wp-content/uploads/2021/03/FA-Agenda-March-2021-min.pdf, read 2026-11-08: "s LLP Chartered Professional Accountants Ms. Buchanan presented the Audited Financial Statements for the year ending December 31, 2020. She informed the members that the statements presented include a") | published by: auditor of record (own audited financial statements, auditor's report signed in St. Thomas | record: https://www.catfishcreek.ca/wp-content/uploads/2026/03/Catfish-Creek-Conservation-Authority-2025-Financial-Statements.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in St. Thomas, Ontario)=hority by Graham Scott Enns LLP in accordance with Canadian public sector accounting standards. | _____________________ | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in St. Thomas)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:a20d716e3b5bce18
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in St. Thomas; 0 in the contract dataset)

## Buyer
- **buyer**: Catfish Creek Conservation Authority
- **buyer_website**: https://catfishcreek.ca/
- **buyer_address**: 8079 Springwater Road, Aylmer, Ontario N5H 2R4
- **buyer_phone**: 519-773-9037
- **buyer_contact_evidence_url**: https://www.catfishcreek.ca/contact-us/
- **buyer_legal_name_as_published**: 2026 · Catfish Creek Conservation Authority
- **buyer_bn_as_published**: 106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/)
- **buyer_bn_program**: RR (registered charity program account)
- **buyer_gst_hst_derived**: 106879240RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.catfishcreek.ca/wp-content/uploads/2016/09/Header-Logo-Main.png
- **buyer_website_status**: site answers
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (catfishcreek.ca) + name)
- **buyer_charity_designation**: C; 0200
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q106289329; conservation authority; charitable organization
- **buyer_budget_or_revenue**: revenue 935904 Q1104069; 901863 Q1104069; 1032103 Q1104069; 969159 Q1104069; 1089666 Q1104069; 1060327 Q1104069; 1093699 Q110406 (Wikidata Q106289329, official website on the organisation's domain (https://www.catfishcreek.ca/) + name; 2026-11-08)
- **buyer_employees**: 25; 62; 22; 40; 39; 35; 27; 36; 33; 37; 38; 43; 28; 34 (Wikidata Q106289329, official website on the organisation's domain (https://www.catfishcreek.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.catfishcreek.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@catfishcreek.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.catfishcreek.ca/wp-content/uploads/2024/12/Seasonal-Camper-Handbook-2025.pdf
- **email_evidence_quote**: al Fees by April 30th and receive a 1% discount on your fee. Increment patments do not qualify for the 1% discount.Transfers can be sent to finance@catfishcreek.ca. Make sure to include your Name (Primary Occupant), Site Number and that the email transfer is for your site fees in your mess
- **mailbox_provenance**: finance@catfishcreek.ca (finance/accounting dept or supplier-payment office) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.catfishcreek.ca/wp-content/uploads/2024/12/Seasonal-Camper-Handbook-2025.pdf | quote: "al Fees by April 30th and receive a 1% discount on your fee. Increment patments do not qualify for the 1% discount.Transfers can be sent to finance@catfishcreek" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00432
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: catfishcreek.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf.hornetsecurity.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **po_required_as_published**: yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 2026 · Catfish Creek Conservation Authority — 8079 Springwater Road, Aylmer, Ontario N5H 2R4 — buyer tax no. 106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/) ⏎ SUBMIT TO: finance@catfishcreek.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order must) ⏎ FROM / REMIT TO: Graham Scott Enns LLP — 450 Sunset Drive, St Thomas, ON, N5R 5V1, Canada | GST/HST number not public ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Catfish Creek Conservation Authority (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 
- **invoice_card_json**: {"bill_to": {"legal_name": "2026 · Catfish Creek Conservation Authority", "legal_name_is_published": true, "address": "8079 Springwater Road, Aylmer, Ontario N5H 2R4", "address_is_the_invoice_address": false, "tax_number": "106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/)", "language": "en"}, "submit_to": {"email": "finance@catfishcreek.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (ht
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08))

## Vendor
- **vendor**: Graham Scott Enns LLP
- **vendor_address**: 450 Sunset Drive, St Thomas, ON, N5R 5V1, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in St. Thomas, Ontario)=hority by Graham Scott Enns LLP in accordance with Canadian public sector accounting standards. | _______________________________ Dustin Underhill General Manager/Secretary-Treasurer | St. Thomas, Ontario February 5, 2026
- **vendor_website**: https://grahamscottenns.com/
- **vendor_emails**: info@grahamscottenns.com
- **vendor_phone**: 519-773-9265
- **vendor_contact_evidence_url**: https://grahamscottenns.com/contact/
- **vendor_logo_url**: https://grahamscottenns.com/wp-content/uploads/2019/01/logo-grahamscottenns.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://grahamscottenns.com/ (Accountants in St. Thomas & Aylmer Ontario | Graham Scott Enns LLP Skip to content Graham Scott Enns LLP Chartered Professional Accountants in St. Thomas & Aylm)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in St. Thomas); phone / role e-mails / logo: the vendor's own site, https://grahamscottenns.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://grahamscottenns.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in St. Thomas)
- **award_date**: 2026-02-05
- **end_date**: 2020-12-31 (as printed in the buyer's own council / committee report or minutes: https://www.catfishcreek.ca/wp-content/uploads/2021/03/FA-Agenda-March-2021-min.pdf, read 2026-11-08: "s LLP Chartered Professional Accountants Ms. Buchanan presented the Audited Financial Statements for the year ending December 31, 2020. She informed the members that the statements presented include a")
- **contract_link**: https://www.catfishcreek.ca/wp-content/uploads/2026/03/Catfish-Creek-Conservation-Authority-2025-Financial-Statements.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in St. Thomas
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in St. Thomas; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 106879240RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 2026 · Catfish Creek Conservation Authority — 8079 Springwater Road, Aylmer, Ontario N5H 2R4 — buyer tax no. 106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/) ⏎ SUBMIT TO: finance@catfishcreek.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order must) ⏎ FROM / REMIT TO: Graham Scott Enns LLP — 450 Sunset Drive, St Thomas, ON, N5R 5V1, Canada | GST/HST number not public ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Catfish Creek Conservation Authority (government ministry / agency, jurisdiction not stated) — public contract / purchase award in the last 
- **invoice_card_json**: {"bill_to": {"legal_name": "2026 · Catfish Creek Conservation Authority", "legal_name_is_published": true, "address": "8079 Springwater Road, Aylmer, Ontario N5H 2R4", "address_is_the_invoice_address": false, "tax_number": "106879240 RR0001 (as printed: Registration Number 10687 9240 RR0001; https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/)", "language": "en"}, "submit_to": {"email": "finance@catfishcreek.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order must) (as printed on https://www.catfishcreek.ca/wp-content/uploads/2016/10/Purchasing-Policy.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (ht
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["finance@catfishcreek.ca (finance/accounting dept or supplier-payment office)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.catfishcreek.ca/wp-content/uploads/2024/12/Seasonal-Camper-Handbook-2025.pdf", "quote: \"al Fees by April 30th and receive a 1% discount on your fee. Increment patments do not qualify for the 1% discount.Transfers can be sent to finance@catfishcreek\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by self-hosted or other (mx-cluster-ca-fallback.hornetsecurity.com)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00432"], "buyer_facts": ["address and phone: the buyer's own site, https://www.catfishcreek.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and add

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.catfishcreek.ca/ | 2026-11-06 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, catfishcreek.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: 2026 · Catfish Creek Conservation Authority
- **legal_name_url**: https://www.catfishcreek.ca/
- **legal_name_quote**: ETY WATERSHED CONDITIONS STATEMENT – March 2, 2026 Catfish Creek CA Facebook Springwater Facebook © 2026 · Catfish Creek Conservation Authority. Home Site Map Privacy Contact Us
- **logo_url**: https://www.catfishcreek.ca/wp-content/uploads/2016/09/Header-Logo-Main.png
- **logo_basis**: logo image in the site header
- **bn**: 106879240
- **bn_program**: RR0001
- **bn_label**: Registration Number 10687 9240 RR0001
- **bn_url**: https://www.catfishcreek.ca/about-us/mandate-objectives-mission-statement/
- **bn_quote**: ue in the future. An official tax receipt can be issued for minimum donations of $50.00. Charitable Registration Number 10687 9240 RR0001. Our Mission Statement To communicate and deliver resource management services and programs in orde
- **domain**: catfishcreek.ca
- **key**: lead:a20d716e3b5bce18
- **name**: Catfish Creek Conservation Authority
- **website**: https://catfishcreek.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: 2026 Conservation Authority
- **legal_name_stated_url**: https://www.catfishcreek.ca/about-us/board-of-directors/
- **legal_name_stated_quote**: icy Programs and Services Booklet Recent Updates WATER SAFETY WATER CONDITIONS STATEMENT – July 27, 2026 Conservation Authority Amalgamation WATER SAFETY WATERSHED CONDITIONS STATEMENT – March 2, 2026 Catfish Creek CA Facebook

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "8079 Springwater Road, Aylmer, Ontario N5H 2R4", "address_country": "CA", "address_url": "https://www.catfishcreek.ca/contact-us/", "address_method": "pattern", "address_quote": "t Us Catfish Creek Conservation Authority 8079 Springwater Road Aylmer, Ontario N5H 2R4 Tel: 519-773-9037 Fax: 519-765-1489 Staff Directory Recent News WATER SAFETY WA", "phone": "519-773-9037", "phone_url": "https://www.catfishcreek.ca/contact-us/", "emails": "admin@catfishcreek.ca", "emails_url": "https://www.catfishcreek.ca/contact-us/", "domain": "catfishcreek.ca", "key": "wd:Q106289329", "name": "Catfish Creek Conservation Authority", "website": "https://catfishcreek.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, grahamscottenns.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Graham Scott Enns LLP
- **legal_name_url**: https://grahamscottenns.com/
- **legal_name_quote**: Accountants in St. Thomas & Aylmer Ontario | Graham Scott Enns LLP Skip to content Graham Scott Enns LLP Chartered Professional Accountants in St. Thomas & Aylmer Ont
- **logo_url**: https://grahamscottenns.com/wp-content/uploads/2019/01/logo-grahamscottenns.svg
- **logo_basis**: logo image in the site header
- **domain**: grahamscottenns.com
- **key**: vendor:Graham Scott Enns LLP
- **name**: Graham Scott Enns LLP
- **website**: https://grahamscottenns.com/
- **kind**: vendor
- **date**: 2026-11-09
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Graham Scott Enns LLP
- **jsonld_logo**: https://grahamscottenns.com/wp-content/uploads/2019/01/cropped-icon-grahamscottenns.png
- **jsonld_url**: https://grahamscottenns.com/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://grahamscottenns.com/#/schema/WebSite","url":"https://grahamscottenns.com/","name":"Graham Scott Enns LLP","description":"Chartered Professional Accountants in St. Thomas & Aylmer Ontario","inLanguage":"en-CA","potentialActi
- **jsonld_page**: https://grahamscottenns.com/
- **linkedin_url**: https://www.linkedin.com/company/graham-scott-enns-llp/
- **tel_links**: +1-519-773-9265; +1-519-773-9683; +1-519-633-0700; +1-519-633-7009
- **tel_links_url**: https://grahamscottenns.com/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "25 John Street South, Suite 208, Aylmer, Ontario N5H 2C1", "address_country": "CA", "address_url": "https://grahamscottenns.com/contact/", "address_method": "pattern", "address_quote": "519-773-9265 Fax: 519-773-9683 25 John Street South, Suite 208 Aylmer, Ontario N5H 2C1 View on Google Maps St. Thomas Office Phone: 519-633-0700 Fax: 519-633-7009 450", "phone": "519-773-9265", "phone_url": "https://grahamscottenns.com/contact/", "emails": "info@grahamscottenns.com", "emails_url": "https://grahamscottenns.com/contact/", "domain": "grahamscottenns.com", "key": "vd:grahamscottenns.com", "name": "Graham Scott Enns LLP", "website": "https://grahamscottenns.com/", "kind": "vendor", "date": "2026-11-07"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Catfish Creek Conservation Authority | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Catfish%20Creek%20Conservation%20Authority | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Catfish Creek Conservation Authority | Q106289329 | official website on the organisation's domain (https://www.catfishcreek.ca/) + name |  | Catfish Creek Conservation Authority |  | conservation authority; charitable organization |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:a20d716e3b5bce18",
 "ap_contact_team": {
  "emails": [
   "finance@catfishcreek.ca",
   "admin@catfishcreek.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@catfishcreek.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.catfishcreek.ca/wp-content/uploads/2024/12/Seasonal-Camper-Handbook-2025.pdf",
    "quote": "al Fees by April 30th and receive a 1% discount on your fee. Increment patments do not qualify for the 1% discount.Transfers can be sent to finance@catfishcreek.ca. Make sure to include your Name (Primary Occupant), Site Number and that the email transfer is for your site fees in your mess",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Catfish Creek Conservation Authority",
    "task_id": "CL-WS-00432"
   },
   {
    "email": "admin@catfishcreek.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.catfishcreek.ca/",
    "quote": "\"lng\":\"-81.0344\",\"ibx\":\"8079 Springwater Rd, \\u003C/br\\u003E\\r\\nAylmer, ON N5H 2R4 \\u003C/br\\u003E\\r\\n519-773-9037\\r\\n\\u003Ca href=\\\"mailto:admin@catfishcreek.ca\\\"\\",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Catfish Creek Conservation Authority",
    "task_id": "CL-LD-45691"
   },
   {
    "email": "admin@catfishcreek.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.catfishcreek.ca/wp-content/uploads/2024/10/CCCA-Low-Water-Response-Manual.pdf",
    "quote": "ATFISH CREEK CONSERVATION AUTHORITY 8079 Springwater Road, RR# 5, Aylmer, Ontario N5H 2R4 PHONE: (519) 773-9037 • FAX: 519-765-1489 e-mail: admin@catfishcreek.ca • www.catfishcreek.ca May 28, 2012 Dear Landowner: RE: Water Taking During Low Water Periods 34 The Catfish Creek Water Response",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Catfish Creek Conservation Authority",
    "task_id": "CL-WS-00017"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of catfishcreek.ca (11 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 2)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:ba6fdf9b-4a98-4e72-a3db-be6fe795b22b:1 | Perth County | External Audit Services |  |  |  | https://perthcounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ba6fdf9b-4a98-4e72-a3db-be6fe795b22b |
| ca_bidsandtenders:85ef4eb2-ce73-4e48-93f0-50fb4f7e18e4:1 | County of Elgin | External Audit Services |  |  |  | https://elgincounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/85ef4eb2-ce73-4e48-93f0-50fb4f7e18e4 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

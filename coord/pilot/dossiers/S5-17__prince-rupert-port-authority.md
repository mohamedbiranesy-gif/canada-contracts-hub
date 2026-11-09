# S5-17 — Prince Rupert Port Authority ⇄ Crestview Strategy

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Prince Rupert Port Authority — 200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2
SUBMIT TO: finance@rupertport.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: requisitioning, approvals, purchase order)
FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, r
DESCRIPTION: null
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 80
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Prince Rupert Port Authority (transport / transit authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Crestview Strategy | subject: null | awarded 2026-10-31, start 2026-03-31, end 2026-10-31 | published by: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv) | record: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6414&regId=56582714 | vendor in Canada because: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=555 Burrard St #1795, Vancouver, BC, V7X 1M8, CAN | status rule: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:b02056afccb3069f
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)

## Buyer
- **buyer**: Prince Rupert Port Authority
- **buyer_website**: https://rupertport.com/
- **buyer_address**: 200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2
- **buyer_contact_evidence_url**: https://www.rupertport.com/contact-us/
- **buyer_legal_name_as_published**: Prince Rupert Port Authority
- **buyer_logo_url**: https://www.rupertport.com/wp-content/themes/rupert/assets/images/rupert-logo-color.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/prince-rupert-port-authority/
- **buyer_type**: transport / transit authority
- **buyer_sector**: transport / transit
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.rupertport.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_esignature_preference**: Docusign Envelope ID: 4EF8BE28-ECBE-45AD-AEC7-F651D42B9E3F  Purchase of goods where raw (as printed on https://www.rupertport.com/wp-content/uploads/2025/05/2025-REPORT-ON-FORCED-AND-CHILD-LABOUR-IN-SUPPLY-CHAINS-ID-26757.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@rupertport.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.rupertport.com/financial-statements/
- **email_evidence_quote**: the region as a whole.</p> <p class="wp-block-paragraph">If you have questions concerning our financial statements, please <a href="mailto:finance@rupertport.com">contact our finance department</a>.</p> <div class="wp-block-file"><a id="wp-block-file--media-cd752f68-e205-432c-8a54-0628750
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@rupertport.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-02 | page: https://www.rupertport.com/financial-statements/ | quote: "the region as a whole.</p> <p class="wp-block-paragraph">If you have questions concerning our financial statements, please <a href="mailto:finance@rupertport.co" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-SN-02585
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:dmarcreports@rupertport.com,mailto:dmarc_agg@vali.email;
- **dmarc_record_domain**: rupertport.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com ip4:209.145.102.0/24 include:amazonses.com include:servers.mcsv.net include:cmail1.com include:_spf.psm.knowbe4.com ip4:52.60.59.231 include:_spf.ultipro.com ip4:15.222.212.123 -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, re-read 2026-11-08)", "po_required": "yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prince Rupert Port Authority — 200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2 ⏎ SUBMIT TO: finance@rupertport.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: requisitioning, approvals, purchase order) ⏎ FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, r ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Prince Rupert Port Authority", "legal_name_is_published": true, "address": "200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rupertport.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08))"}, "terms": {"payment_terms": "payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 4EF8BE28-ECBE-45AD-AEC7-F651D42B9E3F  Purchase of goods where raw (as printed on https://www.rupertport.com/wp-content/uploads/2025/05/2025-REPORT-ON-FORCED-AND-CHILD-LABOUR-IN-SUPPLY-CHAINS-ID-26757.pdf,
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 73
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08))

## Vendor
- **vendor**: Crestview Strategy
- **vendor_legal_name**: Crestview Strategy Inc.
- **vendor_trading_name**: Crestview Strategy
- **vendor_registry_id**: Québec REQ (NEQ): 1181904914
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 330 Bay Street, Unit 10, Toronto (Ontario), M5H2S8
- **vendor_neq**: 1181904914 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Agence internationale d'affaires publiques
- **vendor_employees_quebec**: De 1 à 5
- **vendor_establishments_quebec**: Agence Stratégie Crestview: 2200-1250 boul. René-Lévesque O, Montréal (Québec), H3B4W8
- **vendor_address**: 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA
- **vendor_country_basis**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=555 Burrard St #1795, Vancouver, BC, V7X 1M8, CAN
- **vendor_website**: https://www.crestviewstrategy.com/
- **vendor_emails**: contactus@crestviewstrategy.com
- **vendor_phone**: +1 416.645.2912
- **vendor_contact_evidence_url**: https://www.crestviewstrategy.com/contact/
- **vendor_logo_url**: https://www.crestviewstrategy.com/wp-content/uploads/2025/02/logo.svg
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)); registry identity: Québec REQ (NEQ): 1181904914 status Québec REQ (NEQ): Immatriculée (2026-03-12) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2025-12-09; phone / role e-mails / logo: the vendor's own site, https://www.crestviewstrategy.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.crestviewstrategy.com/ (site answers); NEQ: 1181904914 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2026-03-12)
- **vendor_incorporation_date**: 2025-12-09
- **vendor_years_in_business**: 0.9 (since 2025-12-09, registry date)

## Contract
- **po_required_as_published**: yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **contract_title**: null
- **contract_description**: null (the record's title; the source publishes no separate description)
- **award_date**: 2026-10-31
- **start_date**: 2026-03-31
- **end_date**: 2026-10-31
- **contract_link**: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6414&regId=56582714
- **source**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prince Rupert Port Authority — 200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2 ⏎ SUBMIT TO: finance@rupertport.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: requisitioning, approvals, purchase order) ⏎ FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, r ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Prince Rupert Port Authority", "legal_name_is_published": true, "address": "200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "finance@rupertport.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: requisitioning, approvals, purchase order) (as printed on https://www.rupertport.com/transparency/, re-read 2026-11-08))"}, "terms": {"payment_terms": "payable within thirty days (as printed on https://www.rupertport.com/port_tariffs/fees-generally/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": "Docusign Envelope ID: 4EF8BE28-ECBE-45AD-AEC7-F651D42B9E3F  Purchase of goods where raw (as printed on https://www.rupertport.com/wp-content/uploads/2025/05/2025-REPORT-ON-FORCED-AND-CHILD-LABOUR-IN-SUPPLY-CHAINS-ID-26757.pdf,
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 73
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["finance@rupertport.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-02", "page: https://www.rupertport.com/financial-statements/", "quote: \"the region as a whole.</p> <p class=\"wp-block-paragraph\">If you have questions concerning our financial statements, please <a href=\"mailto:finance@rupertport.co\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-SN-02585"], "buyer_facts": ["address and phone: the buyer's own site, https://www.rupertport.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))", "registry identity: Québe

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.rupertport.com/financial-statements/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, rupertport.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Copyright Prince Rupert Port Authority
- **legal_name_url**: https://www.rupertport.com/
- **legal_name_quote**: ting Events Gateway Workforce Network Email Address * First Name Last Name * Required Fields © 2026 Copyright Prince Rupert Port Authority. All rights reserved. Address Prince Rupert Port Authority 200 - 215 Cow Bay Rd. Prince Rupert, BC
- **logo_url**: https://www.rupertport.com/wp-content/themes/rupert/assets/images/rupert-logo-color.svg
- **logo_basis**: logo image in the site header
- **domain**: rupertport.com
- **key**: lead:b02056afccb3069f
- **name**: Prince Rupert Port Authority
- **website**: https://rupertport.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Ridley Energy Export Facility
- **legal_name_stated_url**: https://www.rupertport.com/about/
- **legal_name_stated_quote**: t Port Authority congratulates Vopak and AltaGas on their positive final investment decision on the Ridley Energy Export Facility (REEF). This is an incredible milestone for the Port of Prince Rupert as it marks the largest inves
- **linkedin_url**: https://www.linkedin.com/company/prince-rupert-port-authority/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "200 – 215 Cow Bay Rd. , Prince Rupert, BC V8J 1A2", "address_country": "CA", "address_url": "https://www.rupertport.com/contact-us/", "address_method": "pattern", "address_quote": "om ADDRESS Prince Rupert Port Authority 200 – 215 Cow Bay Rd. Prince Rupert, BC V8J 1A2 © 2026 Copyright Prince Rupert Port Authority. All rights reserved. Address Pri", "emails": "info@rupertport.com", "emails_url": "https://www.rupertport.com/contact-us/", "domain": "rupertport.com", "key": "lead:b02056afccb3069f", "name": "Prince Rupert Port Authority", "website": "https://rupertport.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, crestviewstrategy.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.crestviewstrategy.com/wp-content/uploads/2025/02/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: crestviewstrategy.com
- **key**: vendor:Crestview Strategy
- **name**: Crestview Strategy
- **website**: https://crestviewstrategy.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Crestview Strategy
- **jsonld_logo**: https://www.crestviewstrategy.com/wp-content/uploads/2025/03/Favicon.svg
- **jsonld_url**: https://www.crestviewstrategy.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.crestviewstrategy.com\/","url":"https:\/\/www.crestviewstrategy.com\/","name":"Top Public Affairs Agency | Crestview Strategy","isPartOf":{"@id":"https:\/\/www.crestviewstrategy.com\/#website"},"about":{"@id":"https
- **jsonld_page**: https://www.crestviewstrategy.com/
- **legal_name_stated**: Crestview Strategy and are
- **legal_name_stated_url**: https://www.crestviewstrategy.com/terms-and-conditions/
- **legal_name_stated_quote**: of Service. Intellectual Property The Site and all of its original content are the sole property of Crestview Strategy and are, as such, fully protected by the appropriate international copyright and other intellectual propert
- **mentions**: {'payment_method': {'text': 'interaction information (such as scrolling, clicks, and mouse-overs), and methods used', 'url': 'https://www.crestviewstrategy.com/privacy-policy/', 'quote': 'clicked), page response times, download errors, length of visits to certain pages on the Site, page interaction information (such as scrolling, clicks, and mouse-overs), and methods used to browse away from the Site) We do not collect any Special Categories of'}}
- **tel_links**: 14166452912; +61.2.8580.5467; 971585868730; 16132323192; 61.2.8580.5467; 416-645-2912 x1

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "330 Bay St, Suite 1000, Toronto ON, Canada , M5H 2S8", "address_country": "CA", "address_url": "https://www.crestviewstrategy.com/contact/", "address_method": "pattern", "address_quote": ".2.8580.5467 Location Details Toronto 330 Bay St, Suite 1000 Toronto ON, Canada M5H 2S8 Email +1 416.645.2912 Location Details Vancouver 555 Burrard Street, Floor 17", "phone": "+1 416.645.2912", "phone_url": "https://www.crestviewstrategy.com/contact/", "emails": "contactus@crestviewstrategy.com", "emails_url": "https://www.crestviewstrategy.com/contact/", "domain": "crestviewstrategy.com", "key": "vd:crestviewstrategy.com", "name": "Crestview Strategy", "website": "https://crestviewstrategy.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Prince Rupert Port Authority | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Prince%20Rupert%20Port%20Authority | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Crestview Strategy | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Prince Rupert Port Authority |  |  |  |  |  |  |  |  |  |  |
| b | Crestview Strategy |  |  |  |  |  |  |  |  |  |  |
| v | Crestview Strategy Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b02056afccb3069f",
 "ap_contact_team": {
  "emails": [
   "info@rupertport.com",
   "finance@rupertport.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "The Port Authority describes a cloud procure-to-pay system for PO management and invoice processing. Its public notice gives no supplier submission URL.",
  "evidence": [
   {
    "email": "info@rupertport.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "The Port Authority describes a cloud procure-to-pay system for PO management and invoice processing. Its public notice gives no supplier submission URL.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.rupertport.com/contact-us/",
    "quote": "info@rupertport.com",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "Prince Rupert Port Authority",
    "task_id": "CH-AP-50020"
   },
   {
    "email": "finance@rupertport.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rupertport.com/financial-statements/",
    "quote": "the region as a whole.</p> <p class=\"wp-block-paragraph\">If you have questions concerning our financial statements, please <a href=\"mailto:finance@rupertport.com\">contact our finance department</a>.</p> <div class=\"wp-block-file\"><a id=\"wp-block-file--media-cd752f68-e205-432c-8a54-0628750",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Prince Rupert Port Authority",
    "task_id": "CL-SN-02585"
   },
   {
    "email": "info@rupertport.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rupertport.com/infosource/",
    "quote": "ce Rupert Port Authority. All rights reserved. Address Prince Rupert Port Authority 200 - 215 Cow Bay Rd. Prince Rupert, BC +1 250 627-8899 info@rupertport.com Contact Follow Us Documents Port Information Guide Public Documents Transparency Info Source Corporate Privacy Statement Accessibi",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Prince Rupert Port Authority",
    "task_id": "CL-WS-00466"
   },
   {
    "email": "info@rupertport.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rupertport.com/wp-content/uploads/2020/04/20200128_669159_RPT_RIELP_ProjectDescription_Final.pdf",
    "quote": "ailing Address 200 – 215 Cow Bay Rd. Prince Rupert, BC V8J 1A2 Jack Smith Principal Contact Director, Environmental Planning and Compliance info@rupertport.com Contact Information 1 250 627-8899 (office) 1 250 627 5621 (community comment line) 1.3 Purpose and Need for the Project The Proje",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Prince Rupert Port Authority",
    "task_id": "CL-WS-00415"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site:rupertport.com \"accounts payable\" invoice finance vendor Prince Rupert Port Authority | site:rupertport.com \"finance@rupertport.com\" | site:rupertport.com \"procurement@\" OR \"purchasing@\" OR \"accountspayable@\" Prince Rupert Port Authority invoice",
  "site crawl of rupertport.com (57 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 5)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-03629:ba609e34-b53a-4832-9469-d5f988be8fae | Rural Municipalities of Alberta (RMA) | Rural Municipalities of Alberta (RMA) - Request for Proposal - Notice of Request for Proposals for Federal Advocacy Services | 396000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03629 |
| ca_alberta_apc:AB-2025-05490:057f93a7-8137-4b51-9e9f-1107c44ec43e | Rocky View County | Rocky View County - Request for Proposal - RFP-25-014 Prairie Gateway Advocacy Support Final | 400475.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05490 |
| ca_bidsandtenders:db39e740-c644-4f15-82af-be05630ee65a:1 | Canoe Procurement Group of Canada | Federal Advocacy Services |  |  |  | https://canoe.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/db39e740-c644-4f15-82af-be05630ee65a |
| ca_merx:3958773725:1 | La Cité Collégiale | Services de relations gouvernementales et d’appui stratégique |  |  |  | https://www.merx.com/lacitecollegiale/solicitations/Services-de-relations-gouvernementales-et-d-appui-strat-gique/0000321958?origin=0 |
| ca_merx:2276649010:5 | Toronto Transit Commission - PCM Operating | REQUEST FOR SUPPLIER QUALIFICATION - COMMUNITY RELATIONS COMMUNICATIONS SERVICES | 1.0 |  |  | https://www.merx.com/ttc/ttcpurchasingandsales/solicitations/REQUEST-FOR-SUPPLIER-QUALIFICATION-COMMUNITY-RELATIONS-COMMUNICATIONS-SERVICES/0000230709?origin=0 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

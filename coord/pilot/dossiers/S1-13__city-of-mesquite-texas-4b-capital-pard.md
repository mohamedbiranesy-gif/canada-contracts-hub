# S1-13 — City of Mesquite, Texas — 4B Capital PARD ⇄ WHITEWATER WEST INDUSTRIES LTD.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Mesquite (stated on https://cityofmesquite.com/privacy) — 757 N. Galloway Ave., Mesquite, TX 75149
SUBMIT TO: accounting@cityofmesquite.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: Reference City PO)
FROM / REMIT TO: WHITEWATER WEST INDUSTRIES LTD. — 6700 MCMILLAN WAY, RICHMOND, BC, V6W1J7 | GST/HST 105673271RT0001 (account derived from the BN9)
TAX: Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/ | CURRENCY: USD | TERMS: Payment Terms: The City of Mesquite pays in
DESCRIPTION: Contractual Services | AMOUNT: 11,496.56 USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 11
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Mesquite, Texas — 4B Capital PARD (US city / county / local government, US) — public contract / purchase award in the last 12 months (dated record): WHITEWATER WEST INDUSTRIES LTD. | subject: Contractual Services | instrument: vendor payments (no contract published) | all identifiers: {"payment_ids": ["623036"], "inv_numbers": ["SOINV-006347"]} | value: 11496.56 USD | awarded 2026-06-10, start 2026-06-10 | published by: City of Mesquite Open Checkbook — Check Register + Vendor | record: https://opendata.cityofmesquite.com/d/6tva-azs5 | vendor in Canada because: Vendor dataset (qnqi-i9bs) state = 'BC' (Canadian province code), zip 'V6W1J7' (Canadian FSA), city 'RICHMOND' | status rule: likely active (awarded in the last 12 months, no end date published) | this buyer has 6 records with Canada-located vendors (6 distinct vendors; 2 in the last 12 months; latest 2026-06-10)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:0bb6d702e9094e1a|b:498e44cebc67835c|b:822e63bed3f870e1|b:e7d8c24499363999|b:e93f58290d4afcb8|b:f134445cfdce0f99
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: City of Mesquite, Texas — 4B Capital PARD
- **buyer_website**: https://www.cityofmesquite.com
- **buyer_address**: 757 N. Galloway Ave., Mesquite, TX 75149
- **buyer_phone**: 972-288-7711
- **buyer_contact_evidence_url**: https://cityofmesquite.com/m/directory
- **buyer_legal_name_as_published**: City of Mesquite (stated on https://cityofmesquite.com/privacy)
- **buyer_logo_url**: https://cityofmesquite.com/ImageRepository/Document?documentID=22148
- **buyer_website_status**: site answers
- **buyer_supplier_portals_linked**: BidNet Direct (e-tendering): https://www.bidnetdirect.com/texas/cityofmesquite
- **buyer_type**: US city / county / local government
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://cityofmesquite.com/m/directory (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide); invoicing requirements: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide); payment terms: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide); PO requirement: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide)
- **buyer_tax_exempt_status**: Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 6

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@cityofmesquite.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide
- **email_evidence_quote**: ons regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com. Payment Terms: The City of Mesquite pays in
- **email_evidence_context**: ing department upon shipment. The mailing location is printed at the heading of the purchase order under BILL TO. Questions regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com. Payment Terms: The City of Mesquite pays in compliance with the Texas Prompt Payment Act. The City of Mesquite pays vendors twice a week. Checks are mailed on Tuesdays and Thursdays of each week. Direct Deposit: The City of Mesquite has chosen the (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounting@cityofmesquite.com (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29 | page: https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide | quote: "ons regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01048
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; aspf=r; adkim=r;
- **dmarc_record_domain**: cityofmesquite.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx ip4:207.64.149.0/24 ip4:207.126.144.0/20 ip4:207.7.154.9/24 ip4:209.237.241.0/24 ip4:192.189.81.0/24 ip4:23.98.132.80/32 ip4:192.189.81.18/32 include:spf.protection.outlook.com include:spf.emailsignatures365.com include:_spf.saffire.com include:mail.cityofmesquite.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 972.216.6205
- **invoicing_requirements**: Reference City PO number and PO prices; invoice forwarded to ordering department upon shipment, using BILL TO location printed on PO. StandardTerms: payment by 30th calendar day after latest of goods receipt, service completion or invoice receipt, in accordance with stated TexasPromptPaymentAct refe
- **payment_terms_as_published**: Payment Terms: The City of Mesquite pays in
- **po_required_as_published**: yes (as published: Reference City PO)
- **ap_system_hint**: linked from the buyer's site: BidNet Direct (e-tendering)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "Payment Terms: The City of Mesquite pays in", "po_required": "yes (as published: Reference City PO)", "ap_phone": "972.216.6205", "requirements_text": "Reference City PO number and PO prices; invoice forwarded to ordering department upon shipment, using BILL TO location printed on PO. StandardTerms: payment by 30th calendar day after latest of goods receipt, service completion or invoice receipt, in accordance with stated TexasPromptPaymentAct refe"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Mesquite (stated on https://cityofmesquite.com/privacy) — 757 N. Galloway Ave., Mesquite, TX 75149 ⏎ SUBMIT TO: accounting@cityofmesquite.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Reference City PO) ⏎ FROM / REMIT TO: WHITEWATER WEST INDUSTRIES LTD. — 6700 MCMILLAN WAY, RICHMOND, BC, V6W1J7 | GST/HST 105673271RT0001 (account derived from the BN9) ⏎ TAX: Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/ | CURRENCY: USD | TERMS: Payment Terms: The City of Mesquite pays in ⏎ DESCRIPTION: Contractual Services | AMOUNT: 11,496.56 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Mesquite (stated on https://cityofmesquite.com/privacy)", "legal_name_is_published": true, "address": "757 N. Galloway Ave., Mesquite, TX 75149", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@cityofmesquite.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "linked from the buyer's site: BidNet Direct (e-tendering)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Reference City PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Reference City PO))"}, "terms": {"payment_terms": "Payment Terms: The City of Mesquite pays in", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide, re-read 2026-11-08)", "buyer_tax_status_is_published": true, "indicative_rate": "", "currency": "USD", "currency_is_published": true, "vendor_gst_hst": "105673271RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "WHITEWATE
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Reference City PO))

## Vendor
- **vendor**: WHITEWATER WEST INDUSTRIES LTD.
- **vendor_legal_name**: WHITEWATER WEST INDUSTRIES LTD.
- **vendor_registry_id**: BC OrgBook (BC registration): BC1238701
- **vendor_registry_url**: https://orgbook.gov.bc.ca/entity/BC1238701
- **vendor_legal_form**: BC company (home jurisdiction BC)
- **vendor_address**: 6700 MCMILLAN WAY, RICHMOND, BC, V6W1J7
- **vendor_country_basis**: Vendor dataset (qnqi-i9bs) state = 'BC' (Canadian province code), zip 'V6W1J7' (Canadian FSA), city 'RICHMOND'
- **vendor_bn9**: 105673271
- **vendor_gst_hst_derived**: 105673271RT0001
- **vendor_website**: https://www.whitewaterwest.com/
- **vendor_contact_evidence_url**: https://www.whitewaterwest.com/contact/
- **vendor_logo_url**: https://www.whitewaterwest.com/wp-content/uploads/2025/10/logo-1.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.whitewaterwest.com/ (Water Park Manufacturer and Designer - WhiteWater Skip to content this.handleScroll()); }, handleScroll() { const currentScroll = window.pageYOffset; // Don't h)
- **vendor_facts_provenance**: name and address: the record's vendor block (City of Mesquite Open Checkbook — Check Register + Vendor); registry identity: BC OrgBook (BC registration): BC1238701 status BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; strong); BN9: bc_orgbook BC1238701 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2020-02-01; phone / role e-mails / logo: the vendor's own site, https://www.whitewaterwest.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.whitewaterwest.com/
- **vendor_concentration_top_share**: TUMBLEWEED PRESS INC: 16% of 6 records
- **vendor_registry_status**: BC OrgBook (BC registration): Active
- **vendor_registry_match_level**: strong
- **vendor_incorporation_date**: 2020-02-01
- **vendor_years_in_business**: 6.8 (since 2020-02-01, registry date)
- **vendor_bn_source**: bc_orgbook BC1238701 (strong match)

## Contract
- **po_required_as_published**: yes (as published: Reference City PO)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"payment_ids": ["623036"], "inv_numbers": ["SOINV-006347"]}
- **contract_title**: Contractual Services
- **contract_description**: Contractual Services
- **contract_value**: 11496.56
- **currency**: USD
- **award_date**: 2026-06-10
- **start_date**: 2026-06-10
- **contract_link**: https://opendata.cityofmesquite.com/d/6tva-azs5
- **source**: City of Mesquite Open Checkbook — Check Register + Vendor
- **contracts_with_canadian_suppliers**: 6
- **records_last_12_months**: 2
- **record_sources**: City of Mesquite Open Checkbook — Check Register + Vendor (6)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 6 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 105673271RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Mesquite (stated on https://cityofmesquite.com/privacy) — 757 N. Galloway Ave., Mesquite, TX 75149 ⏎ SUBMIT TO: accounting@cityofmesquite.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Reference City PO) ⏎ FROM / REMIT TO: WHITEWATER WEST INDUSTRIES LTD. — 6700 MCMILLAN WAY, RICHMOND, BC, V6W1J7 | GST/HST 105673271RT0001 (account derived from the BN9) ⏎ TAX: Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/ | CURRENCY: USD | TERMS: Payment Terms: The City of Mesquite pays in ⏎ DESCRIPTION: Contractual Services | AMOUNT: 11,496.56 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Mesquite (stated on https://cityofmesquite.com/privacy)", "legal_name_is_published": true, "address": "757 N. Galloway Ave., Mesquite, TX 75149", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@cityofmesquite.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "linked from the buyer's site: BidNet Direct (e-tendering)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Reference City PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Reference City PO))"}, "terms": {"payment_terms": "Payment Terms: The City of Mesquite pays in", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "Tax exemption certificates will be provided by the Purchasing office, upon request by the supplier (as printed on https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide, re-read 2026-11-08)", "buyer_tax_status_is_published": true, "indicative_rate": "", "currency": "USD", "currency_is_published": true, "vendor_gst_hst": "105673271RT0001", "vendor_qst": ""}, "vendor_identity": {"legal_name": "WHITEWATE
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["accounting@cityofmesquite.com (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29", "page: https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide", "quote: \"ons regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01048"], "buyer_facts": ["address and phone: the buyer's own site, https://cityofmesquite.com/m/directory (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide)", "invoicing requirements: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide)", "payment terms: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide)", "PO requirement: the lane's AP page (https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide)"], "vendor_facts":

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide | 2026-11-08 | ok |  | purchase-order terms published (as published: must be externally identified with a packing list indicating contents and referencing the City purchase order number) |  | 972.216.6205 |  |  |  |  | will be provided by the Purchasing office, upon request by the supplier. All shipments must be externally identified with a packing list indicating contents and referencing the City purchase order number and department n |

## Buyer site facts (org_extras, cityofmesquite.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://cityofmesquite.com/ImageRepository/Document?documentID=22148
- **logo_basis**: logo image on the site
- **domain**: cityofmesquite.com
- **key**: b:0bb6d702e9094e1a
- **name**: City of Mesquite, Texas — 4B Capital PARD
- **website**: https://cityofmesquite.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: City of Mesquite
- **legal_name_stated_url**: https://cityofmesquite.com/privacy
- **legal_name_stated_quote**: s Events & Culture How Do I... Search Home Government Legal Privacy Statement Privacy Statement The City of Mesquite and its subsidiaries are committed to respecting and protecting your privacy. The Web site is struc
- **portals**: [{'name': 'BidNet Direct', 'kind': 'e-tendering', 'url': 'https://www.bidnetdirect.com/texas/cityofmesquite', 'on_page': 'https://cityofmesquite.com/accessibility'}]
- **mentions**: {'payment_method': {'text': 'Interactive Maps Online Project Tracking Other Development Resources Building Inspectio', 'url': 'https://cityofmesquite.com/accessibility', 'quote': 'Plans Codes & Ordinances Commercial Solid Waste Demographics Historic Preservation Division Online Interactive Maps Online Project Tracking Other Development Resources Building Inspection Engineering Planning & Zoning Permits & Fees Sale of City Owned Propert'}}
- **tel_links**: 972-288-7711; 972-216-6424; 972-216-6206; 972-216-6759; 972-216-4130,; 972-216-6272,; 972-216-6404,; 972-329-8388,; 972-

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "757 N. Galloway Ave., Mesquite, TX 75149", "address_country": "US", "address_url": "https://cityofmesquite.com/m/directory", "address_method": "pattern", "address_quote": "1515 N. Galloway Ave. Mesquite, TX 75149 Phone: 972-288-7711 Mesquite City Hall 757 N. Galloway Ave. Mesquite, TX 75149 Phone: 972-288-7711 Community Services 1616 N. Galloway Ave.", "phone": "972-288-7711", "phone_url": "https://cityofmesquite.com/m/directory", "emails": "communications@cityofmesquite.com", "emails_url": "https://cityofmesquite.com/m/directory", "domain": "cityofmesquite.com", "key": "b:0bb6d702e9094e1a", "name": "City of Mesquite, Texas — 4B Capital PARD", "website": "https://cityofmesquite.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, whitewaterwest.com)
- **status**: ok
- **pages**: 6
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Whitewater
- **jsonld_logo**: https://www.whitewaterwest.com/wp-content/uploads/2019/11/whitewater-logo-colour.png
- **jsonld_url**: https://www.whitewaterwest.com/
- **jsonld_same_as**: https://www.facebook.com/WhiteWaterWest; https://x.com/WhiteWaterWest; https://www.instagram.com/whitewaterwest/; https://ca.linkedin.com/company/whitewaterwest; https://www.youtube.com/user/WhiteWaterWest; https://en.wikipedia.org/wiki/WhiteWater_West
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.whitewaterwest.com\/","url":"https:\/\/www.whitewaterwest.com\/","name":"Water Park Manufacturer and Designer - WhiteWater","isPartOf":{"@id":"https:\/\/www.whitewaterwest.com\/#website"},"about":{"@id":"https:\/\/w
- **jsonld_page**: https://www.whitewaterwest.com/
- **linkedin_url**: https://ca.linkedin.com/company/whitewaterwest
- **language**: en
- **logo_url**: https://www.whitewaterwest.com/wp-content/uploads/2025/10/logo-1.png
- **logo_basis**: logo image in the site header
- **domain**: whitewaterwest.com
- **key**: vendor:WHITEWATER WEST INDUSTRIES LTD.
- **name**: WHITEWATER WEST INDUSTRIES LTD.
- **website**: https://whitewaterwest.com/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "3655 Pacific Highway, #A, San Diego, CA 92101", "address_country": "US", "address_url": "https://www.whitewaterwest.com/contact/", "address_method": "pattern", "address_quote": "ai United Arab Emirates +971 (0) 4 422 9318 Get directions USA FlowRider Office 3655 Pacific Highway, #A San Diego, CA 92101 USA +1 604 273 1068 Get directions China Unit 1608, Shu", "domain": "whitewaterwest.com", "key": "vendor:WHITEWATER WEST INDUSTRIES LTD.", "name": "WHITEWATER WEST INDUSTRIES LTD.", "website": "https://whitewaterwest.com/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | City of Mesquite, Texas — 4B Capital PARD |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:0bb6d702e9094e1a",
 "ap_contact_team": {
  "emails": [
   "accounting@cityofmesquite.com",
   "purchasing@cityofmesquite.com"
  ],
  "invoice_portal": null,
  "phone": "972.216.6205",
  "mailing_address": null,
  "invoicing_requirements": "Reference City PO number and PO prices; invoice forwarded to ordering department upon shipment, using BILL TO location printed on PO. StandardTerms: payment by 30th calendar day after latest of goods receipt, service completion or invoice receipt, in accordance with stated TexasPromptPaymentAct reference. No fixed all-City invoice postal/portal established.",
  "evidence": [
   {
    "email": "accounting@cityofmesquite.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": "972.216.6205",
    "mailing_address": null,
    "requirements": "Reference City PO number and PO prices; invoice forwarded to ordering department upon shipment, using BILL TO location printed on PO. StandardTerms: payment by 30th calendar day after latest of goods receipt, service completion or invoice receipt, in accordance with stated TexasPromptPaymentAct reference. No fixed all-City invoice postal/portal established.",
    "applies_to": "parent_central_ap",
    "page_url": "https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide",
    "quote": "ons regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com. Payment Terms: The City of Mesquite pays in",
    "retrieved_date": "2026-10-29",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch11.csv",
    "org": "City of Mesquite, Texas — 4B Capital PARD",
    "task_id": "CH-AP-01048"
   },
   {
    "email": "accounting@cityofmesquite.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide",
    "quote": "TO. Questions regarding billing or payments and changes to the “Remit To” address should be directed to Accounts Payable at 972.216.6205 or accounting@cityofmesquite.com. Payment Terms: The City of Mesquite pays in compliance with the Texas Prompt Payment Act. The City of Mesquite pays ven",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Mesquite, Texas — 4B Capital PARD",
    "task_id": "CH-AP-01048"
   },
   {
    "email": "purchasing@cityofmesquite.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cityofmesquite.com/DocumentCenter/View/29149/Vendor-Guide",
    "quote": "City of Mesquite Municipal Complex 757 N. Galloway Avenue City Hall, 2nd floor Mesquite, Texas 75149 Procurement, Room 3037 972.216.6201 purchasing@cityofmesquite.com Page | 1 This guide is intended to give a brief insight into the City’s procurement process. While this guide does not enc",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Mesquite, Texas — 4B Capital PARD",
    "task_id": "CH-AP-01048"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site:cityofmesquite.com accounts payable invoices supplierpayment; opened VendorGuide, Accounting, ContractsAndProcurement, DirectDeposit and StandardTerms; sixCityunit/ledgerlabels researchedtogether",
  "site crawl of www.cityofmesquite.com (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.cityofmesquite.com (25 pages, robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| us_city_mesquite_tx:6969-2107060 | us_city_mesquite_tx | end_date_unknown | Contractual Services | 11496.56 | USD |  |  | {"payment_ids": ["623036"], "inv_numbers": ["SOINV-006347"]} | https://opendata.cityofmesquite.com/d/6tva-azs5 |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

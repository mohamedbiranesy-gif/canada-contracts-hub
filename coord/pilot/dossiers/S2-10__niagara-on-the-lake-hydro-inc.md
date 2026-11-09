# S2-10 — Niagara-on-the-Lake Hydro Inc ⇄ Niagara-on-the-Lake

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Niagara-on-the-Lake Hydro Inc — PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0 — buyer tax no. 863605929 (Canada's Business Registries, ON 1424833, 2026-11-08)
SUBMIT TO: invoice@notlhydro.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility) — PO Box 100, Virgil, ON L0S 1T0 | GST/HST 106979487 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2020-06-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake
```

## Relationship
- **rank_group**: E4
- **data_quality_score**: 66
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Niagara-on-the-Lake Hydro Inc (utility / public corporation, jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Niagara-on-the-Lake | subject: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake | published by: the Canada-located vendor's own website | record: https://www.notl.com/recreation-community/community-news/town-niagara-lake-launches-queen-street-secondary-plan-project | vendor in Canada because: vendor located in Canada (wd)=notl.com | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:6439a0ef2bff29da
- **tier**: E
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Niagara-on-the-Lake Hydro Inc
- **buyer_website**: https://notlhydro.com/
- **buyer_address**: PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0
- **buyer_contact_evidence_url**: https://www.notlhydro.com/contact-us/
- **buyer_legal_name_as_published**: Niagara-on-the-Lake Hydro Inc
- **buyer_bn_as_published**: 863605929 (Canada's Business Registries, ON 1424833, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 863605929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.notlhydro.com/wp-content/uploads/2025/10/cropped-favicon-32x32-1-180x180.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/niagara-on-the-lake-hydro
- **buyer_registry_id**: 1424833 (ON; https://ised-isde.canada.ca/cbr-rec/en/search?q=Niagara-on-the-Lake%20Hydro%20Inc)
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1424833, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.notlhydro.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoice@notlhydro.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.notlhydro.com/wp-content/uploads/2024/09/New-Vendor-Form-2024-0905-Fillable.pdf
- **email_evidence_quote**: / and agree to the Vendor Acknowledgement terms listed. Y es No N/A VENDOR INFORMATION SHEET Ensure this form is completed and submitted to invoice@notlhydro.com if you are a new vendor or if your information changes. If information is missing or incomplete, your supplier registration will
- **email_evidence_context**: VENDOR INFORMATION SHEET Ensure this form is completed and submitted to invoice@notlhydro.com if you are a new vendor or if your information changes. If information is missing or incomplete, your supplier registration will be delayed. TYPE OF REQUEST SUPPLIER TYPE* New Vendor Setup Business (corporation / partnership / sole-proprietorship) U (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoice@notlhydro.com (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.notlhydro.com/wp-content/uploads/2024/09/New-Vendor-Form-2024-0905-Fillable.pdf | quote: "/ and agree to the Vendor Acknowledgement terms listed. Y es No N/A VENDOR INFORMATION SHEET Ensure this form is completed and submitted to invoice@notlhydro.co" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-11561
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine; rua=mailto:dmarc-collector@skycomp.ca; ruf=mailto:dmarc-collector@skycomp.ca; pct=100; fo=1
- **dmarc_record_domain**: notlhydro.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:66.209.48.90/30 ip4:66.209.54.161/28 ip4:209.167.31.0/24 ip4:209.167.35.130/26 ip4:72.142.12.198/28 ip4:216.234.63.42 ip4:216.234.32.64/28 ip4:63.104.149.38 ip4:199.168.249.18 include:spf.skycomp.ca include:spf.protection.outlook.com include:relay.mailchannels.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Niagara-on-the-Lake Hydro Inc — PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0 — buyer tax no. 863605929 (Canada's Business Registries, ON 1424833, 2026-11-08) ⏎ SUBMIT TO: invoice@notlhydro.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility) — PO Box 100, Virgil, ON L0S 1T0 | GST/HST 106979487 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2020-06-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake
- **invoice_card_json**: {"bill_to": {"legal_name": "Niagara-on-the-Lake Hydro Inc", "legal_name_is_published": true, "address": "PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0", "address_is_the_invoice_address": false, "tax_number": "863605929 (Canada's Business Registries, ON 1424833, 2026-11-08)", "language": "en"}, "submit_to": {"email": "invoice@notlhydro.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "106979487RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility)", "bn9": "106979487 (recipient_business_number in the feder
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Niagara-on-the-Lake
- **vendor_legal_name**: Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility)
- **vendor_trading_name**: Niagara-on-the-Lake
- **vendor_address**: PO Box 100, Virgil, ON L0S 1T0
- **vendor_country_basis**: vendor located in Canada (wd)=notl.com
- **vendor_bn9**: 106979487 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2020-06-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 106979487RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://notl.com
- **vendor_emails**: info@notl.com
- **vendor_phone**: 905-468-3266
- **vendor_contact_evidence_url**: https://www.notl.com/contact-us
- **vendor_logo_url**: https://www.notl.com/sites/default/files/notl-logo.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/town-of-niagara-on-the-lake/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.notl.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://notl.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake
- **contract_description**: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake (the record's title; the source publishes no separate description)
- **contract_link**: https://www.notl.com/recreation-community/community-news/town-niagara-lake-launches-queen-street-secondary-plan-project
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 863605929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 106979487RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Niagara-on-the-Lake Hydro Inc — PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0 — buyer tax no. 863605929 (Canada's Business Registries, ON 1424833, 2026-11-08) ⏎ SUBMIT TO: invoice@notlhydro.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility) — PO Box 100, Virgil, ON L0S 1T0 | GST/HST 106979487 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2020-06-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Town of Niagara-on-the-Lake Launches Queen Street Secondary Plan Project | Town of Niagara-on-the-Lake
- **invoice_card_json**: {"bill_to": {"legal_name": "Niagara-on-the-Lake Hydro Inc", "legal_name_is_published": true, "address": "PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0", "address_is_the_invoice_address": false, "tax_number": "863605929 (Canada's Business Registries, ON 1424833, 2026-11-08)", "language": "en"}, "submit_to": {"email": "invoice@notlhydro.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "106979487RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Town of Niagara-on-the-Lake (stated on the vendor's legal page: https://www.notl.com/accessibility)", "bn9": "106979487 (recipient_business_number in the feder
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["invoice@notlhydro.com (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.notlhydro.com/wp-content/uploads/2024/09/New-Vendor-Form-2024-0905-Fillable.pdf", "quote: \"/ and agree to the Vendor Acknowledgement terms listed. Y es No N/A VENDOR INFORMATION SHEET Ensure this form is completed and submitted to invoice@notlhydro.co\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-11561"], "buyer_facts": ["address and phone: the buyer's own site, https://www.notlhydro.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "BN9: federal grants & contributions disclosure (recipient_business_number)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / rol

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.notlhydro.com/wp-content/uploads/2024/09/New-Vendor-Form-2024-0905-Fillable.pdf | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, notlhydro.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.notlhydro.com/wp-content/uploads/2025/10/cropped-favicon-32x32-1-180x180.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: notlhydro.com
- **key**: lead:6439a0ef2bff29da
- **name**: notlhydro.com
- **website**: https://notlhydro.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Electric Vehicle Charging
- **legal_name_stated_url**: https://www.notlhydro.com/accessibility-feedback-form/
- **legal_name_stated_quote**: Programs Outage Notifications Search for: Customer Service Rates Residential Rates Commercial Rates Electric Vehicle Charging (EVC) Rate Price Plans Explained Water Rates Retailer Awareness Returning to Regulated Price Plan B
- **mentions**: {'payment_method': {'text': 'interactions through challenges', 'url': 'https://www.notlhydro.com/', 'quote': 'e Recaptcha Recaptcha Google reCAPTCHA helps protect websites from spam and abuse by verifying user interactions through challenges. Name Description Duration _GRECAPTCHA Google reCAPTCHA sets a necessary cookie (_GRECAPTCHA) when'}}
- **linkedin_url**: https://www.linkedin.com/company/niagara-on-the-lake-hydro
- **legal_name**: Niagara-on-the-Lake Hydro Inc
- **legal_name_url**: https://www.notlhydro.com/
- **legal_name_quote**: Home - Niagara-on-the-Lake Hydro Inc. Skip to content Niagara-on-the-Lake Hydro Inc. NOTLs Community-Owned Electric Utility Menu Home Re

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "PO Box 460, 8 HENEGAN ROAD, Virgil, ON L0S 1T0", "address_country": "CA", "address_url": "https://www.notlhydro.com/contact-us/", "address_method": "pattern", "address_quote": "t Programs Outage Notifications NOTL HYDRO PO Box 460 8 HENEGAN ROAD Virgil, ON L0S 1T0 905-468-4235 Copyright 2017, Niagara-on-the-Lake Hydro Inc. X Facebook Linkedin", "domain": "notlhydro.com", "key": "lead:6439a0ef2bff29da", "name": "notlhydro.com", "website": "https://notlhydro.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, notl.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.notl.com/sites/default/files/notl-logo.png
- **logo_basis**: logo image in the site header
- **domain**: notl.com
- **key**: b:d883ea3defb97f08
- **name**: Town of Niagara-on-the-Lake
- **website**: https://notl.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Town of Niagara-on-the-Lake
- **legal_name_stated_url**: https://www.notl.com/accessibility
- **legal_name_stated_quote**: Accessibility & Inclusion | Town of Niagara-on-the-Lake Skip to main content Skip to main menu Skip to footer Alert How Do I . . . Header menu Search the W
- **linkedin_url**: https://www.linkedin.com/company/town-of-niagara-on-the-lake/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "PO Box 100, Virgil, ON L0S 1T0", "address_country": "CA", "address_url": "https://www.notl.com/contact-us", "address_method": "pattern", "address_quote": "nistration Building (Town Hall) 1593 Four Mile Creek Road PO Box 100 Virgil, ON L0S 1T0 Main Phone: 905-468-3266 After Hours Phone: 905-468-3278 Office Hours: Monday t", "phone": "905-468-3266", "phone_url": "https://www.notl.com/contact-us", "emails": "info@notl.com", "emails_url": "https://www.notl.com/contact-us", "domain": "notl.com", "key": "vd:notl.com", "name": "Niagara-on-the-Lake", "website": "https://notl.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Niagara-on-the-Lake Hydro Inc | found | NIAGARA-ON-THE-LAKE HYDRO INC. | 863605929 | 1424833 | ON | ONTARIO BUSINESS CORP. | Active | 2000-07-01 | VIRGIL | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Niagara-on-the-Lake%20Hydro%20Inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Town of Niagara-on-the-Lake |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:6439a0ef2bff29da",
 "ap_contact_team": {
  "emails": [
   "invoice@notlhydro.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoice@notlhydro.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.notlhydro.com/wp-content/uploads/2024/09/New-Vendor-Form-2024-0905-Fillable.pdf",
    "quote": "/ and agree to the Vendor Acknowledgement terms listed. Y es No N/A VENDOR INFORMATION SHEET Ensure this form is completed and submitted to invoice@notlhydro.com if you are a new vendor or if your information changes. If information is missing or incomplete, your supplier registration will",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "notlhydro.com",
    "task_id": "CL-LD-11561"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of notlhydro.com (12 pages, robots.txt respected), no AI, no search engine"
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

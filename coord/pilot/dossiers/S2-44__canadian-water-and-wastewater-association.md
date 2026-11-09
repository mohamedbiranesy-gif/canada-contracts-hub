# S2-44 — Canadian Water and Wastewater Association ⇄ inferred: Canada Post Corporation

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08) — 1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)
SUBMIT TO: accounts@cwwa.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Canadian Water and Wastewater Association (utility / public corporation, CA) — inferred: no record; the organisation's type and province mak
```

## Relationship
- **rank_group**: I4
- **data_quality_score**: 58
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: Canadian Water and Wastewater Association (utility / public corporation, CA) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada; generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Cana
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: wd:Q30295045
- **tier**: I
- **grade**: 4

## Buyer
- **buyer**: Canadian Water and Wastewater Association
- **buyer_website**: https://cwwa.ca
- **buyer_address**: 11, 1010 Polytek Street, Ottawa, ON K1J 9H9
- **buyer_contact_evidence_url**: https://cwwa.ca/contact-us/
- **buyer_legal_name_as_published**: CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08)
- **buyer_logo_url**: https://cwwa.ca/wp-content/uploads/2019/04/CWWA_Leaf_vector_final_wht.png
- **buyer_website_status**: site answers
- **buyer_registry_id**: corporation number 2310627 (Corporations Canada (open data); https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2310627)
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q30295045; organization
- **buyer_founded**: 1986-01-01 (Wikidata Q30295045, official website on the organisation's domain (http://www.cwwa.ca/home_e.asp) + name; 2026-11-08)
- **buyer_legal_form**: Canada Not-for-profit Corporations Act (Corporations Canada (open data), corporation number 2310627, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://cwwa.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts@cwwa.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://cwwa.ca/contact-us/
- **email_evidence_quote**: Isabel Fowles Accounts Payable Accounts@cwwa.ca Kara Parisien Communication Manager Kparisien@cwwa.ca Adrian Toth Director of Government Relations atoth@cwwa.ca Louisa Spina Account
- **email_evidence_context**: Email admin@cwwa.ca Phone This field is for validation purposes and should be left unchanged. Name First Last Phone Email Tell Us A Little About Your Request CWWA Staff Robert Haller Executive Director rhaller@cwwa.ca Isabel Fowles Accounts Payable Accounts@cwwa.ca Kara Parisien Communication Manager Kparisien@cwwa.ca Adrian Toth Director of Government Relations atoth@cwwa.ca Louisa Spina Accounts & Membership Coordinator lspina@cwwa.ca CWWA is a non-profit national body representing the common interests of Ca (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts@cwwa.ca (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://cwwa.ca/contact-us/ | quote: "Isabel Fowles Accounts Payable Accounts@cwwa.ca Kara Parisien Communication Manager Kparisien@cwwa.ca Adrian Toth Director of Government Relations atoth@cwwa.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-015053
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: cwwa.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 a include:spf.protection.outlook.com include:_spf.membeemail.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "mailing_address": "1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08) — 1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08) ⏎ SUBMIT TO: accounts@cwwa.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Canadian Water and Wastewater Association (utility / public corporation, CA) — inferred: no record; the organisation's type and province mak
- **invoice_card_json**: {"bill_to": {"legal_name": "CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08)", "legal_name_is_published": true, "address": "1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts@cwwa.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vend
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: Canada Post Corporation
- **vendor_address**: 2701 Riverside Drive, Ottawa ON K1A 0B1
- **vendor_country_basis**: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2701 Riverside Drive, N1160 Ottawa ON K1A 0B1'
- **vendor_bn9**: 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)
- **vendor_website**: https://www.canadapost-postescanada.ca
- **vendor_phone**: 1-800-267-7651 (Credit Management Group (invoices and billing); https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to)
- **vendor_contact_evidence_url**: https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to
- **vendor_logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to (tools/org_contacts.py, org_extras.py); website: https://www.canadapost-postescanada.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)

## Contract
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada; generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08) — 1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08) ⏎ SUBMIT TO: accounts@cwwa.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Canadian Water and Wastewater Association (utility / public corporation, CA) — inferred: no record; the organisation's type and province mak
- **invoice_card_json**: {"bill_to": {"legal_name": "CANADIAN WATER AND WASTEWATER ASSOCIATION (as registered: Corporations Canada (open data), corporation number 2310627, 2026-11-08)", "legal_name_is_published": true, "address": "1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts@cwwa.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1010 Polytek Street, Ottawa, ON K1J 9H9 (as printed on https://cwwa.ca/contact-us/, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vend
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 71
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounts@cwwa.ca (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://cwwa.ca/contact-us/", "quote: \"Isabel Fowles Accounts Payable Accounts@cwwa.ca Kara Parisien Communication Manager Kparisien@cwwa.ca Adrian Toth Director of Government Relations atoth@cwwa.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-015053"], "buyer_facts": ["address and phone: the buyer's own site, https://cwwa.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 +

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://cwwa.ca/contact-us/ | 2026-11-08 | ok |  |  |  |  | 1010 Polytek Street, Ottawa, ON K1J 9H9 |  |  |  |  |

## Buyer site facts (org_extras, cwwa.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://cwwa.ca/wp-content/uploads/2019/04/CWWA_Leaf_vector_final_wht.png
- **logo_basis**: logo image on the site
- **domain**: cwwa.ca
- **key**: wd:Q30295045
- **name**: Canadian Water and Wastewater Association
- **website**: https://cwwa.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Canadian Water & Wastewater Association
- **jsonld_logo**: https://cwwa.ca/wp-content/uploads/2019/12/cwwa_logo_footer.jpg
- **jsonld_url**: https://cwwa.ca/
- **jsonld_same_as**: https://www.facebook.com/CanadianWaterAndWastewaterAssociation/; https://x.com/CWWACEPU
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://cwwa.ca/","url":"https://cwwa.ca/","name":"Home - Canadian Water and Wastewater Association","isPartOf":{"@id":"https://cwwa.ca/#website"},"about":{"@id":"https://cwwa.ca/#organization"},"datePublished":"2019-04-03T05:48:38
- **jsonld_page**: https://cwwa.ca/
- **legal_name_stated**: About Us The Canadian Water and Wastewater Association
- **legal_name_stated_url**: https://cwwa.ca/about-us/
- **legal_name_stated_quote**: American Water Works Association, the Water Environment Federation, and their Canadian affiliates. About Us The Canadian Water and Wastewater Association (CWWA) was established in 1986 to represent the common interest of Canada’s municipal water and was

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "11, 1010 Polytek Street, Ottawa, ON K1J 9H9", "address_country": "CA", "address_url": "https://cwwa.ca/contact-us/", "address_method": "pattern", "address_quote": "am and 5:00 pm Address Address: CWWA, Unit 11, 1010 Polytek Street, Ottawa, ON K1J 9H9 Canada Phone Office phone: (613) 747-0524 Ofifice fax: (613) 747-0523 General E", "emails": "accounts@cwwa.ca; admin@cwwa.ca", "emails_url": "https://cwwa.ca/contact-us/", "domain": "cwwa.ca", "key": "wd:Q30295045", "name": "Canadian Water and Wastewater Association", "website": "https://cwwa.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, canadapost-postescanada.ca)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **logo_basis**: logo image on the site
- **domain**: canadapost-postescanada.ca
- **key**: b:2aa5e3d1f7b796f4
- **name**: Canada Post
- **website**: https://canadapost-postescanada.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Canadian Water and Wastewater Association | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Canadian%20Water%20and%20Wastewater%20Association | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Canadian Water and Wastewater Association | found | CANADIAN WATER AND WASTEWATER ASSOCIATION |  | corporation number 2310627 | Corporations Canada (open data) | Canada Not-for-profit Corporations Act | Active | 2014-09-29 | OTTAWA | ON | 1010 POLYTEK STREET, UNIT 11, OTTAWA, ON, K1J 9H9 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | Canadian Water and Wastewater Association | Q30295045 | official website on the organisation's domain (http://www.cwwa.ca/home_e.asp) + name |  | Canadian Water and Wastewater Association | Association Nationale qui Représente les Intérêts Communs des Services Publics | organization |  | Canada | 1986-01-01 |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "wd:Q30295045",
 "ap_contact_team": {
  "emails": [
   "accounts@cwwa.ca",
   "admin@cwwa.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounts@cwwa.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cwwa.ca/contact-us/",
    "quote": "Isabel Fowles Accounts Payable Accounts@cwwa.ca Kara Parisien Communication Manager Kparisien@cwwa.ca Adrian Toth Director of Government Relations atoth@cwwa.ca Louisa Spina Account",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Canadian Water and Wastewater Association",
    "task_id": "CL-WD-015053"
   },
   {
    "email": "admin@cwwa.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cwwa.ca/",
    "quote": "ners. Follow Follow Follow View our privacy policy Head Office CWWA, Unit 11, 1010 Polytek Street, Ottawa, ON K1J 9H9 Canada (613) 747-0524 admin@cwwa.ca Facebook X Instagram RSS Copyright CWWA 2019",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Canadian Water and Wastewater Association",
    "task_id": "CL-WD-015053"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.cwwa.ca (3 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.cwwa.ca (3 pages, robots.txt respected), no AI, no search engine"
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

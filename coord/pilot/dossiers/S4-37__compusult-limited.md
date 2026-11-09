# S4-37 — Compusult Limited ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Compusult Limited — 40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA — buyer tax no. 101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: info@compusult.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Compusult Limited (organisation (type not stated in the record), NL) — inferred: no record; the organisation's type and province make a Cana
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: Compusult Limited (organisation (type not stated in the record), NL) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from its address in the vendor table of the release); generic: Canada Post holds the
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: v:a274fd243da9c3ca
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Compusult Limited
- **buyer_website**: https://www.compusult.com/
- **buyer_address**: 40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA
- **buyer_phone**: //709-745-7914
- **buyer_contact_evidence_url**: https://www.compusult.com/contact-us
- **buyer_legal_name_as_published**: Compusult Limited
- **buyer_bn_as_published**: 101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 101080836RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.compusult.com/image/layout_set_logo?img_id=32256&t=1789482390708
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/compusult-limited
- **buyer_registry_id**: 1759915 (ON; https://ised-isde.canada.ca/cbr-rec/en/search?q=Compusult%20Limited)
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_legal_form**: EP FOREIGN WITH SHARE (Canada's Business Registries, ON 1759915, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.compusult.com/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@compusult.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.compusult.com/contact-us
- **email_evidence_quote**: (UGV) Solutions Careers Feedback Contact Us Contact Us How can we assist you? Go Somewhere --> Contact Information Compusult Limited Email: info@compusult.com Toll Free: +1 888 745 7914 Head Office Mount Pearl, Newfoundland and Labrador Compusult Limited Street Delivery Address: 40 Bannist
- **email_evidence_context**: rvices Solutions Geospatial Solutions Assistive Technology Solutions Asset & Item Tracking Solutions Robotics (UGV) Solutions Careers Feedback Contact Us Contact Us How can we assist you? Go Somewhere --> Contact Information Compusult Limited Email: info@compusult.com Toll Free: +1 888 745 7914 Head Office Mount Pearl, Newfoundland and Labrador Compusult Limited Street Delivery Address: 40 Bannister Street Mount Pearl, NL Canada A1N 1W1 Mailing Address: P.O.Box 1000 Mount Pearl, NL Canada A1N 3C9 Tel: +1 709 745 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@compusult.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.compusult.com/contact-us | quote: "(UGV) Solutions Careers Feedback Contact Us Contact Us How can we assist you? Go Somewhere --> Contact Information Compusult Limited Email: info@compusult.com T" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (pmg1.compusult.com) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-000764
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (pmg1.compusult.com)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=50; rua=mailto:dmarc@compusult.com
- **dmarc_record_domain**: compusult.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:24.137.216.0/24 ip4:24.137.213.0/24 ip4:209.128.38.161 ip4:3.98.170.125 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Compusult Limited — 40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA — buyer tax no. 101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@compusult.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Compusult Limited (organisation (type not stated in the record), NL) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Compusult Limited", "legal_name_is_published": true, "address": "40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA", "address_is_the_invoice_address": false, "tax_number": "101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@compusult.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Newfoundland and Labrador) (province from its address in the vendor table of the release); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 101080836RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **invoice_currency_derived**: EUR (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Compusult Limited — 40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA — buyer tax no. 101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@compusult.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: DERIVED: EUR (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Compusult Limited (organisation (type not stated in the record), NL) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Compusult Limited", "legal_name_is_published": true, "address": "40 Bannister St, Mount Pearl, Newfoundland and Labrador, A1N 1W1, CA", "address_is_the_invoice_address": false, "tax_number": "101080836 (recipient_business_number in the federal grants & contributions disclosure, 14 agreement(s), last 2026-05-04; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@compusult.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "DERIVED: EUR (derived from the buyer's country; C", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@compusult.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.compusult.com/contact-us", "quote: \"(UGV) Solutions Careers Feedback Contact Us Contact Us How can we assist you? Go Somewhere --> Contact Information Compusult Limited Email: info@compusult.com T\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (pmg1.compusult.com)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-000764"], "buyer_facts": ["address and phone: the buyer's own site, https://www.compusult.com/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.compusult.com/contact-us | 2026-11-08 | ok |  |  |  | +1 888 745 7914 |  |  |  |  |  |

## Buyer site facts (org_extras, compusult.com)
- **status**: ok
- **pages**: 3
- **language**: en
- **legal_name**: Compusult Limited
- **legal_name_url**: https://www.compusult.com/
- **legal_name_quote**: gramming and integration services to government, business, technical and scientific sectors. © 2026 Compusult Limited. All Rights Reserved. Home About Web Enterprise Suite Other Products Solutions Careers Feedback Con
- **logo_url**: https://www.compusult.com/image/layout_set_logo?img_id=32256&t=1789482390708
- **logo_basis**: logo image in the site header
- **domain**: compusult.com
- **key**: vendor:Compusult Limited
- **name**: Compusult Limited
- **website**: https://compusult.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Compusult Systems Incorporated
- **legal_name_stated_url**: https://www.compusult.com/about
- **legal_name_stated_quote**: Europe B.V., is located in The Hague, The Netherlands . Compusult also operates a U.S. subsidiary, Compusult Systems Incorporated (CSI) located in Chantilly, Virginia . CSI provides systems integration, installation and training
- **linkedin_url**: https://www.linkedin.com/company/compusult-limited
- **tel_links**: //709-745-7914; //902-406-3088; //+31-687-604-502; //703-464-5649

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "40 Bannister Street, Mount Pearl, NL, Canada, A1N 1W1", "address_country": "CA", "address_url": "https://www.compusult.com/contact-us", "address_method": "pattern", "address_quote": "ult Limited Street Delivery Address: 40 Bannister Street Mount Pearl, NL Canada A1N 1W1 Mailing Address: P.O.Box 1000 Mount Pearl, NL Canada A1N 3C9 Tel: +1 709 745 79", "phone": "//709-745-7914", "phone_url": "https://www.compusult.com/contact-us", "emails": "info@compusult.com", "emails_url": "https://www.compusult.com/contact-us", "domain": "compusult.com", "key": "vd:compusult.com", "name": "Compusult Limited", "website": "https://compusult.com/", "kind": "vendor", "date": "2026-11-03"}

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
| buyer | Compusult Limited | found | COMPUSULT LIMITED |  | 1759915 | ON | EP FOREIGN WITH SHARE | Active | 1985-02-01 | MOUNT PEARL | NewfoundlandandLabrador |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Compusult%20Limited | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | Compusult Limited |  |  |  |  |  |  |  |  |  |  |
| v | Compusult Limited |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "v:a274fd243da9c3ca",
 "ap_contact_team": {
  "emails": [
   "info@compusult.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@compusult.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.compusult.com/contact-us",
    "quote": "(UGV) Solutions Careers Feedback Contact Us Contact Us How can we assist you? Go Somewhere --> Contact Information Compusult Limited Email: info@compusult.com Toll Free: +1 888 745 7914 Head Office Mount Pearl, Newfoundland and Labrador Compusult Limited Street Delivery Address: 40 Bannist",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Compusult Limited",
    "task_id": "CL-VD-000764"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.compusult.com (3 pages, robots.txt respected), no AI, no search engine"
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

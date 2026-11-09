# S4-28 — Heart Lake First Nation ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08) — PO Box 447 Lac La Biche, AB T0A 2C0 — buyer tax no. 140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: info@heartlakefirstnation.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purcha | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Heart Lake First Nation (First Nation / Indigenous government, AB) — inferred: no record; the organisation's type and province make a Canadi
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: Heart Lake First Nation (First Nation / Indigenous government, AB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): medium confidence; the buyer is an institution (school, college, university, health or government body) located in Canada (Alberta) (province from the postal code on its own page (T0A 2
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: wd:Q24054847
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Heart Lake First Nation
- **buyer_website**: https://heartlakefirstnation.com
- **buyer_address**: PO Box 447 Lac La Biche, AB T0A 2C0
- **buyer_phone**: 780-623-2130
- **buyer_contact_evidence_url**: https://heartlakefirstnation.com/contact-us/
- **buyer_legal_name_as_published**: Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08)
- **buyer_bn_as_published**: 140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 140102708RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://heartlakefirstnation.com/wp-content/uploads/2021/07/HLFN_stacked_RGB_REV.png
- **buyer_website_status**: site answers
- **buyer_type**: First Nation / Indigenous government
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q24054847; First Nation band
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://heartlakefirstnation.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@heartlakefirstnation.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://heartlakefirstnation.com/contact-us/
- **email_evidence_quote**: oint Venture Partnerships Industry Relationships Events Contact Us Home » Contact Us Contact Us Call: 780-623-2130 Fax: 780-623-3505 Email: info@heartlakefirstnation.com Address: PO Box 447 Lac La Biche, AB T0A 2C0 CONTACT US PO Box 2228 Lac La Biche, AB T0A 2C0 Phone: 780-623-2935 Fax: 78
- **email_evidence_context**: s Latest News and Updates Newsletter Photo Gallery Economic Development Heart Lake First Nation Construction Joint Venture Partnerships Industry Relationships Events Contact Us Home » Contact Us Contact Us Call: 780-623-2130 Fax: 780-623-3505 Email: info@heartlakefirstnation.com Address: PO Box 447 Lac La Biche, AB T0A 2C0 CONTACT US PO Box 2228 Lac La Biche, AB T0A 2C0 Phone: 780-623-2935 Fax: 780-623-4093 Design by Liquid Trends Media | Admin CONTACT US PO Box 2228 Lac La Biche, AB T0A 2C0 Phone: 780-623-2935 Fax: 780-623 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@heartlakefirstnation.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://heartlakefirstnation.com/contact-us/ | quote: "oint Venture Partnerships Industry Relationships Events Contact Us Home » Contact Us Contact Us Call: 780-623-2130 Fax: 780-623-3505 Email: info@heartlakefirstn" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Namecheap | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-014501
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Namecheap
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.heartlakefirstnation.com; confirmed by 8.8.8.8
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.efwd.registrar-servers.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08) — PO Box 447 Lac La Biche, AB T0A 2C0 — buyer tax no. 140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@heartlakefirstnation.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purcha | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Heart Lake First Nation (First Nation / Indigenous government, AB) — inferred: no record; the organisation's type and province make a Canadi
- **invoice_card_json**: {"bill_to": {"legal_name": "Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "PO Box 447 Lac La Biche, AB T0A 2C0", "address_is_the_invoice_address": false, "tax_number": "140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@heartlakefirstnation.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask ", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "v
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
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
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an institution (school, college, university, health or government body) located in Canada (Alberta) (province from the postal code on its own page (T0A 2C0)); Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); such institutions mail letters and notices
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 140102708RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08) — PO Box 447 Lac La Biche, AB T0A 2C0 — buyer tax no. 140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@heartlakefirstnation.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purcha | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Heart Lake First Nation (First Nation / Indigenous government, AB) — inferred: no record; the organisation's type and province make a Canadi
- **invoice_card_json**: {"bill_to": {"legal_name": "Heart Lake First Nation (label per Wikidata Q24054847, official website on the organisation's domain (https://heartlakefirstnation.com/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "PO Box 447 Lac La Biche, AB T0A 2C0", "address_is_the_invoice_address": false, "tax_number": "140102708 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-11-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "info@heartlakefirstnation.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: provincial government entity in Alberta: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask ", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "v
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@heartlakefirstnation.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://heartlakefirstnation.com/contact-us/", "quote: \"oint Venture Partnerships Industry Relationships Events Contact Us Home » Contact Us Contact Us Call: 780-623-2130 Fax: 780-623-3505 Email: info@heartlakefirstn\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Namecheap", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-014501"], "buyer_facts": ["address and phone: the buyer's own site, https://heartlakefirstnation.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://heartlakefirstnation.com/contact-us/ | 2026-11-08 | ok |  |  |  | 780-623-2130 | PO Box 447 Lac La Biche, AB T0A 2C0 |  |  |  |  |

## Buyer site facts (org_extras, heartlakefirstnation.com)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://heartlakefirstnation.com/wp-content/uploads/2021/07/HLFN_stacked_RGB_REV.png
- **logo_basis**: logo image in the site header
- **domain**: heartlakefirstnation.com
- **key**: wd:Q24054847
- **name**: Heart Lake First Nation
- **website**: https://heartlakefirstnation.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Heart Lake First Nation
- **jsonld_logo**: https://heartlakefirstnation.com/wp-content/uploads/2021/07/HLFN_stacked_RGB_REV.png
- **jsonld_url**: https://heartlakefirstnation.com/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://heartlakefirstnation.com/","url":"https://heartlakefirstnation.com/","name":"Home - Heart Lake First Nation","isPartOf":{"@id":"https://heartlakefirstnation.com/#website"},"about":{"@id":"https://heartlakefirstnation.com/#o
- **jsonld_page**: https://heartlakefirstnation.com/
- **legal_name_stated**: Town of Lac
- **legal_name_stated_url**: https://heartlakefirstnation.com/
- **legal_name_stated_quote**: etter Tomorrow Heart Lake First Nation #469 is located approximately 70 kilometers northeast of the Town of Lac La Biche, Alberta, 220 kilometers northeast of Edmonton, Alberta. READ OUR STORY TAWOW • WELCOME ou

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "PO Box 447 Lac La Biche, AB T0A 2C0", "address_country": "CA", "address_url": "https://heartlakefirstnation.com/contact-us/", "address_method": "pattern", "address_quote": "3505 Email: info@heartlakefirstnation.com Address: PO Box 447 Lac La Biche, AB T0A 2C0 CONTACT US PO Box 2228 Lac La Biche, AB T0A 2C0 Phone: 780-623-2935 Fax: 780-62", "phone": "780-623-2130", "phone_url": "https://heartlakefirstnation.com/contact-us/", "emails": "info@heartlakefirstnation.com", "emails_url": "https://heartlakefirstnation.com/contact-us/", "domain": "heartlakefirstnation.com", "key": "wd:Q24054847", "name": "Heart Lake First Nation", "website": "https://heartlakefirstnation.com/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | Heart Lake First Nation | Q24054847 | official website on the organisation's domain (https://heartlakefirstnation.com/) + name |  | Heart Lake First Nation | Heart Lake | First Nation band |  | Canada |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "wd:Q24054847",
 "ap_contact_team": {
  "emails": [
   "info@heartlakefirstnation.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@heartlakefirstnation.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://heartlakefirstnation.com/contact-us/",
    "quote": "oint Venture Partnerships Industry Relationships Events Contact Us Home » Contact Us Contact Us Call: 780-623-2130 Fax: 780-623-3505 Email: info@heartlakefirstnation.com Address: PO Box 447 Lac La Biche, AB T0A 2C0 CONTACT US PO Box 2228 Lac La Biche, AB T0A 2C0 Phone: 780-623-2935 Fax: 78",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Heart Lake First Nation",
    "task_id": "CL-WD-014501"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of heartlakefirstnation.com (2 pages, robots.txt respected), no AI, no search engine"
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

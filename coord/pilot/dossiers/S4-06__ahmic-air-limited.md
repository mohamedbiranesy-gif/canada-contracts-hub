# S4-06 — AHMIC AIR LIMITED ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08) — 3502 Wiley Road 
Wiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA — buyer tax no. 860481449 (Canada's Business Registries, CC 6023606, 2026-11-08)
SUBMIT TO: info@ahmicair.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: AHMIC AIR LIMITED (organisation (type not stated in the record), NT) — inferred: no record; the organisation's type and province make a Cana
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: AHMIC AIR LIMITED (organisation (type not stated in the record), NT) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Northwest Territories) (province from its address in the vendor table of the release); generic: Canada Post holds the exc
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: v:17186fb77d2b82d7
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: AHMIC AIR LIMITED
- **buyer_website**: https://www.ahmicair.com/
- **buyer_address**: 3502 Wiley Road  ⏎ Wiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA
- **buyer_phone**: 867-920-4400
- **buyer_contact_evidence_url**: https://ahmicair.com/
- **buyer_legal_name_as_published**: Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08)
- **buyer_bn_as_published**: 860481449 (Canada's Business Registries, CC 6023606, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 860481449RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://ahmicair.com/images/logo.png
- **buyer_website_status**: site answers
- **buyer_registry_id**: 6023606 (CC; https://ised-isde.canada.ca/cbr-rec/en/search?q=AHMIC%20AIR%20LIMITED)
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_legal_form**: Business Corporation (Canada's Business Registries, CC 6023606, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://ahmicair.com/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@ahmicair.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.ahmicair.com/
- **email_evidence_quote**: reasing oil & fuel prices. Book a Flight Tour Gift Certificates EXPLORE AhMIC AIR Come Fly With AHMIC AIR Flight Reservations: 867-920-4400 info@ahmicair.com Book Flight Tours Now We are pleased to offer charter services with our float & ski equipped aircraft from Yellowknife, NT Canada. W
- **email_evidence_context**: ght Support Services Floating Docks Shop Merchandise Gift Certificates Tariff Expediting Yellowknife Canoe Co. Coast Dog Aviation Treat Yourself To An Adventure of a Lifetime EXPLORE AhMIC AIR Come Fly With AHMIC AIR Flight Reservations 867-920-4400 info@ahmicair.com Book a Flight Tour We are pleased to offer charter services with our float & ski equipped aircraft from Yellowknife, NT Canada. We strongly believe that your flights with Ahmic Air should be enjoyable and a distinct part of your northern vacation. W (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@ahmicair.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.ahmicair.com/ | quote: "reasing oil & fuel prices. Book a Flight Tour Gift Certificates EXPLORE AhMIC AIR Come Fly With AHMIC AIR Flight Reservations: 867-920-4400 info@ahmicair.com Bo" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (ahmicair.com) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-002893
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (ahmicair.com)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: ahmicair.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:66.102.137.52 a mx include:relay.mailchannels.net include:spf.hostpapa.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08) — 3502 Wiley Road  ⏎ Wiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA — buyer tax no. 860481449 (Canada's Business Registries, CC 6023606, 2026-11-08) ⏎ SUBMIT TO: info@ahmicair.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: AHMIC AIR LIMITED (organisation (type not stated in the record), NT) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08)", "legal_name_is_published": true, "address": "3502 Wiley Road \nWiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA", "address_is_the_invoice_address": false, "tax_number": "860481449 (Canada's Business Registries, CC 6023606, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@ahmicair.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (NT)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST regis
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (Northwest Territories) (province from its address in the vendor table of the release); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 860481449RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (NT) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08) — 3502 Wiley Road  ⏎ Wiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA — buyer tax no. 860481449 (Canada's Business Registries, CC 6023606, 2026-11-08) ⏎ SUBMIT TO: info@ahmicair.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: AHMIC AIR LIMITED (organisation (type not stated in the record), NT) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Ahmic Air Ltd. (as registered: Canada's Business Registries, CC 6023606, 2026-11-08)", "legal_name_is_published": true, "address": "3502 Wiley Road \nWiley's Wharf, Yellowknife, Northwest Territories, X1A 2L6, CA", "address_is_the_invoice_address": false, "tax_number": "860481449 (Canada's Business Registries, CC 6023606, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@ahmicair.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NT on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (NT)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST regis
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@ahmicair.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.ahmicair.com/", "quote: \"reasing oil & fuel prices. Book a Flight Tour Gift Certificates EXPLORE AhMIC AIR Come Fly With AHMIC AIR Flight Reservations: 867-920-4400 info@ahmicair.com Bo\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (ahmicair.com)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-002893"], "buyer_facts": ["address and phone: the buyer's own site, https://ahmicair.com/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST der

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.ahmicair.com/ | 2026-11-08 | ok |  |  |  | 867-920-4400 |  |  |  |  |  |

## Buyer site facts (org_extras, ahmicair.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://ahmicair.com/images/logo.png
- **logo_basis**: logo image in the site header
- **domain**: ahmicair.com
- **key**: vendor:AHMIC AIR LIMITED
- **name**: AHMIC AIR LIMITED
- **website**: https://ahmicair.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'interactive watershed map Close to Yellowknife Campsites & short river trips Tell Us Yo', 'url': 'https://ahmicair.com/', 'quote': 'nformation. Yes, we fly canoes and kayaks! Plan your paddling trip Paddling Adventures 13 regions · interactive watershed map Close to Yellowknife Campsites & short river trips Tell Us Your Route Anywhere we can fly a canoe Lock in 2026 rates for your 2027 adv'}}
- **tel_links**: 8679204400

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "Yellowknife (CEN9) Operations & Admin: , 3502 Wiley Road, Back Bay, Old Town Yellowknife, NT X1A-2L6, 867-920-4400", "address_country": "", "address_url": "https://ahmicair.com/", "address_method": "address-tag", "address_quote": "prices and charter rates by booking this summer's trips now. Contact AHMIC AIR Yellowknife (CEN9) Operations & Admin: 3502 Wiley Road, Back Bay Old Town Yellowknife, NT X1A-2L6 867-920-4400 info@ahm", "phone": "867-920-4400", "phone_url": "https://ahmicair.com/", "emails": "info@ahmicair.com", "emails_url": "https://ahmicair.com/", "domain": "ahmicair.com", "key": "vd:ahmicair.com", "name": "AHMIC AIR LIMITED", "website": "https://ahmicair.com/", "kind": "vendor", "date": "2026-11-03"}

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
| buyer | AHMIC AIR LIMITED | found | Ahmic Air Ltd. | 860481449 | 6023606 | CC | Business Corporation | Active | 2002-09-27 | Yellowknife | Northwest Territories |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=AHMIC%20AIR%20LIMITED | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | AHMIC AIR LIMITED | found | Ahmic Air Ltd. | 860481449 | corporation number 6023606 | Corporations Canada (open data) | Canada Business Corporations Act | Active | 2002-09-27 | Yellowknife | NT | 3502 Wiley Road, Building #2, Yellowknife, NT, X1A 2L6 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | AHMIC AIR LIMITED |  |  |  |  |  |  |  |  |  |  |
| v | Ahmic Air Ltd. |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "v:17186fb77d2b82d7",
 "ap_contact_team": {
  "emails": [
   "info@ahmicair.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@ahmicair.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ahmicair.com/",
    "quote": "reasing oil & fuel prices. Book a Flight Tour Gift Certificates EXPLORE AhMIC AIR Come Fly With AHMIC AIR Flight Reservations: 867-920-4400 info@ahmicair.com Book Flight Tours Now We are pleased to offer charter services with our float & ski equipped aircraft from Yellowknife, NT Canada. W",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "AHMIC AIR LIMITED",
    "task_id": "CL-VD-002893"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.ahmicair.com (2 pages, robots.txt respected), no AI, no search engine"
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

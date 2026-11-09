# S4-23 — Leon's Furniture Saint John ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/) — 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/)
SUBMIT TO: contact@leonssaintjohn.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Leon's Furniture Saint John (organisation (type not stated in the record), NB) — inferred: no record; the organisation's type and province m
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: Leon's Furniture Saint John (organisation (type not stated in the record), NB) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (New Brunswick) (province from the postal code on its own page (E2J2C4)); generic: Canada Post holds the exclusive privile
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: crux:leonssaintjohn.ca
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Leon's Furniture Saint John
- **buyer_website**: https://leonssaintjohn.ca
- **buyer_address**: 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/)
- **buyer_phone**: (506) 634-1966
- **buyer_contact_evidence_url**: https://www.leonssaintjohn.ca/contact
- **buyer_legal_name_as_published**: Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/)
- **buyer_logo_url**: https://images.squarespace-cdn.com/content/v1/5e9901ef8a3476717a295443/1587086075484-6040XGCSYPG6PH3WXY41/Leon_s_Logo_ellipse.png?format=1500w
- **buyer_website_status**: site answers
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.leonssaintjohn.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: contact@leonssaintjohn.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.leonssaintjohn.ca/
- **email_evidence_quote**: to get special offers and be the first to know about sales! Email Address Sign Up Thank you! Contact 428 Rothesay Ave Saint John, NB E2J2C4 contact@leonssaintjohn.ca (506) 634-1966
- **email_evidence_context**: the block and enter a storage location via the Storage tab. Stay in the loop Sign up with your email address to get special offers and be the first to know about sales! Email Address Sign Up Thank you! Contact 428 Rothesay Ave Saint John, NB E2J2C4 contact@leonssaintjohn.ca (506) 634-1966 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: contact@leonssaintjohn.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://www.leonssaintjohn.ca/ | quote: "to get special offers and be the first to know about sales! Email Address Sign Up Thank you! Contact 428 Rothesay Ave Saint John, NB E2J2C4 contact@leonssaintjo" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Zoho | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-041664
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Zoho
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none
- **dmarc_record_domain**: leonssaintjohn.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:squarespace-mail.com include:zoho.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/) — 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/) ⏎ SUBMIT TO: contact@leonssaintjohn.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Leon's Furniture Saint John (organisation (type not stated in the record), NB) — inferred: no record; the organisation's type and province m
- **invoice_card_json**: {"bill_to": {"legal_name": "Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/)", "legal_name_is_published": true, "address": "428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "contact@leonssaintjohn.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_ide
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)

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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (New Brunswick) (province from the postal code on its own page (E2J2C4)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (New Brunswick) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/) — 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/) ⏎ SUBMIT TO: contact@leonssaintjohn.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Leon's Furniture Saint John (organisation (type not stated in the record), NB) — inferred: no record; the organisation's type and province m
- **invoice_card_json**: {"bill_to": {"legal_name": "Leon's Furniture Saint John (schema.org JSON-LD legalName on https://www.leonssaintjohn.ca/)", "legal_name_is_published": true, "address": "428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada (schema.org JSON-LD PostalAddress on https://www.leonssaintjohn.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "contact@leonssaintjohn.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (New Brunswick)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_ide
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["contact@leonssaintjohn.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://www.leonssaintjohn.ca/", "quote: \"to get special offers and be the first to know about sales! Email Address Sign Up Thank you! Contact 428 Rothesay Ave Saint John, NB E2J2C4 contact@leonssaintjo\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Zoho", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-041664"], "buyer_facts": ["address and phone: the buyer's own site, https://www.leonssaintjohn.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, htt

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.leonssaintjohn.ca/ | 2026-11-08 | ok |  |  |  | (506) 634-1966 | 428 Rothesay Ave Saint John, NB E2J2C4 |  |  |  |  |

## Buyer site facts (org_extras, leonssaintjohn.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://images.squarespace-cdn.com/content/v1/5e9901ef8a3476717a295443/1587086075484-6040XGCSYPG6PH3WXY41/Leon_s_Logo_ellipse.png?format=1500w
- **logo_basis**: logo image on the site
- **domain**: leonssaintjohn.ca
- **key**: crux:leonssaintjohn.ca
- **name**: leonssaintjohn.ca
- **website**: https://leonssaintjohn.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: Leon's Furniture Saint John
- **jsonld_address**: 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada
- **jsonld_phone**: (506) 634-1966
- **jsonld_email**: contact@leonssaintjohn.ca
- **jsonld_same_as**: https://www.instagram.com/leonssaintjohn; https://www.facebook.com/LeonsFurnitureSaintJohn; https://www.tiktok.com/@leons.saint.john?lang=en
- **jsonld_quote**: {"address":"428 Rothesay Avenue\nSaint John, NB, E2J 2B3\nCanada","image":"https://static1.squarespace.com/static/5e9901ef8a3476717a295443/t/5e9902fbdafb0b5647fcea94/1793709472832/","name":"Leon's Furniture Saint John","openingHours":"Mo 09:30-19:00, Tu 09:30-19:00, We 09:30-19:00, Th 09:30-19:00, F
- **jsonld_page**: https://www.leonssaintjohn.ca/
- **tel_links**: +15066341966

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada", "address_country": "CA", "address_url": "https://www.leonssaintjohn.ca/contact", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: 428 Rothesay Avenue Saint John, NB, E2J 2B3 Canada", "phone": "(506) 634-1966", "phone_url": "https://www.leonssaintjohn.ca/contact", "emails": "contact@leonssaintjohn.ca", "emails_url": "https://www.leonssaintjohn.ca/contact", "domain": "leonssaintjohn.ca", "key": "crux:leonssaintjohn.ca", "name": "leonssaintjohn.ca", "website": "https://leonssaintjohn.ca/", "kind": "buyer", "date": "2026-11-06"}

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
| buyer | leonssaintjohn.ca | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=leonssaintjohn.ca | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "crux:leonssaintjohn.ca",
 "ap_contact_team": {
  "emails": [
   "contact@leonssaintjohn.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "contact@leonssaintjohn.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.leonssaintjohn.ca/",
    "quote": "to get special offers and be the first to know about sales! Email Address Sign Up Thank you! Contact 428 Rothesay Ave Saint John, NB E2J2C4 contact@leonssaintjohn.ca (506) 634-1966",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "leonssaintjohn.ca",
    "task_id": "CL-CRUX-041664"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.leonssaintjohn.ca (8 pages, robots.txt respected), no AI, no search engine"
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

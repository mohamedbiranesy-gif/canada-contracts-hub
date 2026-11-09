# S2-05 — Dafco Filtration Group ⇄ inferred: SaskPower

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade B · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Filtration Group- IAQ — Regina, SK — buyer tax no. 830340949 (Canada's Business Registries, CC 6427618, 2026-11-08)
SUBMIT TO: ap-hvac@filtrationgroup.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactu
DESCRIPTION: Dafco Filtration Group (company (private sector), SK) — inferred: no record; the organisation's type and province make a Canadian supplier r
```

## Relationship
- **rank_group**: I4
- **data_quality_score**: 58
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: Dafco Filtration Group (company (private sector), SK) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: SaskPower | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://saskpower.com/contact: 'Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Saskatchewan (province from its address in the vendor table of the release); SaskPower holds the electricity franchise in Saskatchewan
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: v:f986fb94dc3b00b8
- **tier**: I
- **grade**: 4

## Buyer
- **buyer**: Dafco Filtration Group
- **buyer_website**: https://www.filtrationgroupiaq.com/
- **buyer_address**: Regina, SK
- **buyer_legal_name_as_published**: Filtration Group- IAQ
- **buyer_bn_as_published**: 830340949 (Canada's Business Registries, CC 6427618, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 830340949RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.filtrationgroupiaq.com/wp-content/uploads/2020/07/cropped-FG_IndoorAirQuality_Short.png
- **buyer_registry_id**: 6427618 (CC; https://ised-isde.canada.ca/cbr-rec/en/search?q=Dafco%20Filtration%20Group)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: Business Corporation (Canada's Business Registries, CC 6427618, 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap-hvac@filtrationgroup.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/
- **email_evidence_quote**: For any inquiries about funds owed by FG IAQ, please fill out the contact form. Alternatively, you can also contact us at (815) 774-1227 or AP-HVAC@FiltrationGroup.com" /> <meta property="og:url" content="https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/" /> <meta property="
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap-hvac@filtrationgroup.com (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/ | quote: "For any inquiries about funds owed by FG IAQ, please fill out the contact form. Alternatively, you can also contact us at (815) 774-1227 or AP-HVAC@FiltrationGr" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; DNS lookup failed; mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-000884
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; DNS lookup failed; mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com;
- **dmarc_record_domain**: filtrationgroup.com
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactus/terms/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactus/terms/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Filtration Group- IAQ — Regina, SK — buyer tax no. 830340949 (Canada's Business Registries, CC 6427618, 2026-11-08) ⏎ SUBMIT TO: ap-hvac@filtrationgroup.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactu ⏎ DESCRIPTION: Dafco Filtration Group (company (private sector), SK) — inferred: no record; the organisation's type and province make a Canadian supplier r
- **invoice_card_json**: {"bill_to": {"legal_name": "Filtration Group- IAQ", "legal_name_is_published": true, "address": "Regina, SK", "address_is_the_invoice_address": false, "tax_number": "830340949 (Canada's Business Registries, CC 6427618, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ap-hvac@filtrationgroup.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactus/terms/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: SaskPower", "bn9": "119429678 (GST/HST registrati
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: SaskPower
- **vendor_address**: 2025 Victoria Avenue, Regina, SK S4P 0S1
- **vendor_country_basis**: the vendor's own site, https://saskpower.com/contact: 'Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1'
- **vendor_bn9**: 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)
- **vendor_gst_hst_derived**: 119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))
- **vendor_website**: https://www.saskpower.com
- **vendor_phone**: 310-2220
- **vendor_contact_evidence_url**: https://saskpower.com/contact-us
- **vendor_logo_url**: https://saskpower.com/-/media/saskpower/logo.png?la=en&h=92&w=344&hash=2F4CBFD7B403E69A4530EB778FAD7A1E
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://saskpower.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://www.saskpower.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business)

## Contract
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Saskatchewan (province from its address in the vendor table of the release); SaskPower holds the electricity franchise in Saskatchewan outside the Saskatoon and Swift Current municipal utilities (The Power Corporation Act); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 830340949RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Filtration Group- IAQ — Regina, SK — buyer tax no. 830340949 (Canada's Business Registries, CC 6427618, 2026-11-08) ⏎ SUBMIT TO: ap-hvac@filtrationgroup.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactu ⏎ DESCRIPTION: Dafco Filtration Group (company (private sector), SK) — inferred: no record; the organisation's type and province make a Canadian supplier r
- **invoice_card_json**: {"bill_to": {"legal_name": "Filtration Group- IAQ", "legal_name_is_published": true, "address": "Regina, SK", "address_is_the_invoice_address": false, "tax_number": "830340949 (Canada's Business Registries, CC 6427618, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ap-hvac@filtrationgroup.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "payment shall be due within 30 days (as printed on https://www.filtrationgroupiaq.com/en-ca/contactus/terms/, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: SaskPower", "bn9": "119429678 (GST/HST registrati
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["ap-hvac@filtrationgroup.com (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/", "quote: \"For any inquiries about funds owed by FG IAQ, please fill out the contact form. Alternatively, you can also contact us at (815) 774-1227 or AP-HVAC@FiltrationGr\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; DNS lookup failed; mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-000884"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business)", "GST/HST derived BN9

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, filtrationgroupiaq.com)
- **status**: ok
- **pages**: 5
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Filtration Group
- **jsonld_logo**: https://www.filtrationgroupiaq.com/wp-content/uploads/2019/06/FGC-logo-1.png
- **jsonld_url**: https://www.filtrationgroupiaq.com/
- **jsonld_same_as**: https://www.linkedin.com/company/11857850/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.filtrationgroupiaq.com\/","url":"https:\/\/www.filtrationgroupiaq.com\/","name":"home - Filtration Group- IAQ","isPartOf":{"@id":"https:\/\/www.filtrationgroupiaq.com\/#website"},"about":{"@id":"https:\/\/www.filtra
- **jsonld_page**: https://www.filtrationgroupiaq.com/
- **language**: en
- **legal_name**: Filtration Group- IAQ
- **legal_name_url**: https://www.filtrationgroupiaq.com/
- **legal_name_quote**: home - Filtration Group- IAQ Parker Hannifin has completed its acquisition of Filtration Group Corporation, creating a powerful
- **logo_url**: https://www.filtrationgroupiaq.com/wp-content/uploads/2020/07/cropped-FG_IndoorAirQuality_Short.png
- **logo_basis**: logo image in the site header
- **domain**: filtrationgroupiaq.com
- **key**: v:f986fb94dc3b00b8
- **name**: Dafco Filtration Group
- **website**: https://filtrationgroupiaq.com/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, saskpower.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://saskpower.com/-/media/saskpower/logo.png?la=en&h=92&w=344&hash=2F4CBFD7B403E69A4530EB778FAD7A1E
- **logo_basis**: logo image in the site header
- **domain**: saskpower.com
- **key**: b:7c6184faae853053
- **name**: SaskPower
- **website**: https://saskpower.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Open Access Transmission Tariff
- **legal_name_stated_url**: https://saskpower.com/accounts/mysaskpower/your-account/terms-and-conditions
- **legal_name_stated_quote**: rical Services and other SaskPower Services with the exception of matters dealt with in SaskPower’s Open Access Transmission Tariff (OATT). SaskPower's Terms and Conditions of Service Cookies Our website uses cookies to personalize
- **mentions**: {'payment_method': {'text': 'Credit Card Payments Equalized Payment Plan Equalized Payment Plan Payment Arrangements Power Rates', 'url': 'https://saskpower.com/home', 'quote': 'Your Bill Pre-authorized Payments Payment History Trouble Paying Your Bill? Pre-authorized Payments Credit Card Payments Equalized Payment Plan Equalized Payment Plan Payment Arrangements Power Rates ← Power Rates Power Supply Rates 2026 and 2027 Rate Increase'}}
- **linkedin_url**: http://www.linkedin.com/company/saskpower
- **tel_links**: 1-888-355-5589; 18887576937; 18883555589; 3065362886

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "10,000 , PO Box 6300, STN Main, Regina, SK S4P 4J5", "address_country": "CA", "address_url": "https://saskpower.com/contact-us", "address_method": "pattern", "address_quote": "ail Us Send payments to: Cheques under $10,000 PO Box 6300, STN Main Regina, SK S4P 4J5 Cheques $10,000+ SaskPower Payment Support 10NE – 2025 Victoria Avenue Regina", "phone": "310-2220", "phone_url": "https://saskpower.com/contact-us", "domain": "saskpower.com", "key": "b:7c6184faae853053", "name": "SaskPower", "website": "https://saskpower.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Dafco Filtration Group | found | Dafco Filtration Group Corporation | 830340949 | 6427618 | CC | Business Corporation | Active | 2005-08-04 | MISSISSAUGA | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Dafco%20Filtration%20Group | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Dafco Filtration Group | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | SaskPower | Q2225615 | official website on the organisation's domain (https://www.saskpower.com/) + name | Saskatchewan Power Corporation [en] | SaskPower | SaskPower | electricity supply company | state-owned enterprise | Canada | 1929-01-01 | Regina; SaskPower Building |
| b | Dafco Filtration Group |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "v:f986fb94dc3b00b8",
 "ap_contact_team": {
  "emails": [
   "ap-hvac@filtrationgroup.com",
   "ap-dafco@filtrationgroup.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "ap-hvac@filtrationgroup.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/",
    "quote": "For any inquiries about funds owed by FG IAQ, please fill out the contact form. Alternatively, you can also contact us at (815) 774-1227 or AP-HVAC@FiltrationGroup.com\" /> <meta property=\"og:url\" content=\"https://www.filtrationgroupiaq.com/accounting-inquiry/suppliers/\" /> <meta property=\"",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Dafco Filtration Group",
    "task_id": "CL-VD-000884"
   },
   {
    "email": "ap-dafco@filtrationgroup.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.filtrationgroupiaq.com/en-ca/accounting-inquiry/suppliers/",
    "quote": "For any inquiries about funds owed by FG IAQ, please fill out the contact form. Alternatively, you can also contact us at 1-888-788-9234 or AP-DAFCO@FiltrationGroup.com\" /> <meta property=\"og:url\" content=\"https://www.filtrationgroupiaq.com/en-ca/accounting-inquiry/suppliers/\" /> <meta pro",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Dafco Filtration Group",
    "task_id": "CL-VD-000884"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.filtrationgroupiaq.com (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.filtrationgroupiaq.com (25 pages, robots.txt respected), no AI, no search engine"
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

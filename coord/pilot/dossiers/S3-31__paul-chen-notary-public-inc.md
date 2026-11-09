# S3-31 — Paul Chen Notary Public Inc ⇄ Maida & Chen Notaries Public

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Paul Chen Notary Public Inc — 02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8 — buyer tax no. 703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08)
SUBMIT TO: info@luxenotary.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Maida & Chen Notaries Public — 740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8 | GST/HST 703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Luxe Notaries Public | Richmond, BC
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 41
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Paul Chen Notary Public Inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Maida & Chen Notaries Public | subject: Luxe Notaries Public | Richmond, BC | published by: the Canada-located vendor's own website | record: https://www.maidachen.com/case-studies | vendor in Canada because: vendor located in Canada (osm)=maidachen.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:f1c3fa3d822f87f6
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Paul Chen Notary Public Inc
- **buyer_website**: https://luxenotary.ca/
- **buyer_address**: 02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8
- **buyer_phone**: 604-270-8644
- **buyer_contact_evidence_url**: https://www.luxenotary.ca/contact-us/
- **buyer_legal_name_as_published**: Paul Chen Notary Public Inc
- **buyer_bn_as_published**: 703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.luxenotary.ca/wp-content/uploads/2026/07/luxe-logo-horizontal-transparent.png
- **buyer_website_status**: site answers
- **buyer_registry_id**: BC1126758 (BC; https://ised-isde.canada.ca/cbr-rec/en/search?q=Paul%20Chen%20Notary%20Public%20Inc)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: BC Company (Canada's Business Registries, BC BC1126758, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.luxenotary.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@luxenotary.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.luxenotary.ca/
- **email_evidence_quote**: stalCode":"V6X 0X8","addressCountry":"CA"},"telephone":["604-273-9688","604-270-8644"],"faxNumber":["604-270-8133","604-273-9680"],"email":"info@luxenotary.ca","url":"https://www.luxenotary.ca","knowsLanguage":["en","zh-Hans","zh-Hant"],"award":["Richmond News Readers’ Choice, notary categ
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@luxenotary.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.luxenotary.ca/ | quote: "stalCode":"V6X 0X8","addressCountry":"CA"},"telephone":["604-273-9688","604-270-8644"],"faxNumber":["604-270-8133","604-273-9680"],"email":"info@luxenotary.ca"," | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (luxenotary.ca) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08594
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (luxenotary.ca)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: luxenotary.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:148.113.170.104 include:spf.web-dns1.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Paul Chen Notary Public Inc — 02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8 — buyer tax no. 703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08) ⏎ SUBMIT TO: info@luxenotary.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Maida & Chen Notaries Public — 740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8 | GST/HST 703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Luxe Notaries Public | Richmond, BC
- **invoice_card_json**: {"bill_to": {"legal_name": "Paul Chen Notary Public Inc", "legal_name_is_published": true, "address": "02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8", "address_is_the_invoice_address": false, "tax_number": "703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@luxenotary.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Maida & Chen Notaries Public", "bn9": "703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18
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
- **vendor**: Maida & Chen Notaries Public
- **vendor_address**: 740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8
- **vendor_country_basis**: vendor located in Canada (osm)=maidachen.com
- **vendor_bn9**: 703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://maidachen.com
- **vendor_phone**: 604-270-8644
- **vendor_contact_evidence_url**: https://maidachen.com/
- **vendor_logo_url**: https://maidachen.com/Luxe-Logo_Horizontal_transparent.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://maidachen.com/ (tools/org_contacts.py, org_extras.py); website: https://maidachen.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Luxe Notaries Public | Richmond, BC
- **contract_description**: Luxe Notaries Public | Richmond, BC (the record's title; the source publishes no separate description)
- **contract_link**: https://www.maidachen.com/case-studies
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Paul Chen Notary Public Inc — 02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8 — buyer tax no. 703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08) ⏎ SUBMIT TO: info@luxenotary.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Maida & Chen Notaries Public — 740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8 | GST/HST 703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Luxe Notaries Public | Richmond, BC
- **invoice_card_json**: {"bill_to": {"legal_name": "Paul Chen Notary Public Inc", "legal_name_is_published": true, "address": "02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8", "address_is_the_invoice_address": false, "tax_number": "703829929 (Canada's Business Registries, BC BC1126758, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@luxenotary.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "703829929RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Maida & Chen Notaries Public", "bn9": "703829929 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-07-18
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@luxenotary.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.luxenotary.ca/", "quote: \"stalCode\":\"V6X 0X8\",\"addressCountry\":\"CA\"},\"telephone\":[\"604-273-9688\",\"604-270-8644\"],\"faxNumber\":[\"604-270-8133\",\"604-273-9680\"],\"email\":\"info@luxenotary.ca\",\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (luxenotary.ca)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08594"], "buyer_facts": ["address and phone: the buyer's own site, https://www.luxenotary.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "BN9: federal grants & contributions disclosure (recipient_business_number)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not autom

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.luxenotary.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, luxenotary.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Paul Chen Notary Public Inc
- **legal_name_url**: https://www.luxenotary.ca/
- **legal_name_quote**: N 中文 Questions? Call 604-270-8644 or Get in Touch © 2026 Luxe Notaries Public. All rights reserved. Paul Chen Notary Public Inc., operating as a Notary Corporation. Terms of Service Privacy Policy imunify-bot-check
- **logo_url**: https://www.luxenotary.ca/wp-content/uploads/2026/07/luxe-logo-horizontal-transparent.png
- **logo_basis**: logo image in the site header
- **domain**: luxenotary.ca
- **key**: lead:f1c3fa3d822f87f6
- **name**: Paul Chen Notary Public Inc
- **website**: https://luxenotary.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Personal Information Protection Act
- **legal_name_stated_url**: https://www.luxenotary.ca/privacy-policy/
- **legal_name_stated_quote**: he “Notaries”) — formerly Maida & Chen Notaries Public and Ng & Schick-Skinner Notaries Public. The Personal Information Protection Act (“PIPA”) regulates the way organizations in British Columbia use, keep, secure, disclose and collec
- **tel_links**: 6042708644; 6042739688; 2503875629

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "02 / VISIT US, Getting Here, 740 - 5599 No.3 Rd, Richmond BC V6X 0X8", "address_country": "CA", "address_url": "https://www.luxenotary.ca/contact-us/", "address_method": "pattern", "address_quote": "mmodated by request. 02 / VISIT US Getting Here 740 - 5599 No.3 Rd, Richmond BC V6X 0X8 We are conveniently located in central Richmond, directly across from Lansdowne", "phone": "604-270-8644", "phone_url": "https://www.luxenotary.ca/contact-us/", "emails": "info@luxenotary.ca", "emails_url": "https://www.luxenotary.ca/contact-us/", "domain": "luxenotary.ca", "key": "lead:f1c3fa3d822f87f6", "name": "luxenotary.ca", "website": "https://luxenotary.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, maidachen.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://maidachen.com/Luxe-Logo_Horizontal_transparent.png
- **logo_basis**: logo image in the site header
- **domain**: maidachen.com
- **key**: vendor:Maida & Chen Notaries Public
- **name**: Maida & Chen Notaries Public
- **website**: https://maidachen.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **tel_links**: 6042708644; 6042739688

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8", "address_country": "CA", "address_url": "https://maidachen.com/", "address_method": "pattern", "address_quote": "982年服務至今，如今合而為一。您慣用的電話號碼維持不變。 Visit Us At 地址 #740 – 5599 No. 3 Rd, Richmond, BC V6X 0X8 Real Estate 房地產 604-270-8644 realestate@luxenotary.ca Wills & Personal Planning", "phone": "604-270-8644", "phone_url": "https://maidachen.com/", "domain": "maidachen.com", "key": "vd:maidachen.com", "name": "Maida & Chen Notaries Public", "website": "https://maidachen.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Paul Chen Notary Public Inc | found | PAUL CHEN NOTARY PUBLIC INC. | 703829929 | BC1126758 | BC | BC Company | Active | 2017-07-14 | RICHMOND | BC |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Paul%20Chen%20Notary%20Public%20Inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Paul Chen Notary Public Inc |  |  |  |  |  |  |  |  |  |  |
| v | Maida & Chen Notaries Public |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:f1c3fa3d822f87f6",
 "ap_contact_team": {
  "emails": [
   "info@luxenotary.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@luxenotary.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.luxenotary.ca/",
    "quote": "stalCode\":\"V6X 0X8\",\"addressCountry\":\"CA\"},\"telephone\":[\"604-273-9688\",\"604-270-8644\"],\"faxNumber\":[\"604-270-8133\",\"604-273-9680\"],\"email\":\"info@luxenotary.ca\",\"url\":\"https://www.luxenotary.ca\",\"knowsLanguage\":[\"en\",\"zh-Hans\",\"zh-Hant\"],\"award\":[\"Richmond News Readers’ Choice, notary categ",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "luxenotary.ca",
    "task_id": "CL-LD-08594"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of luxenotary.ca (9 pages, robots.txt respected), no AI, no search engine"
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

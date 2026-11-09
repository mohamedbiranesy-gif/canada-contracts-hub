# S5-06 — CORNERSTONE CHRISTIAN SCHOOL INC. ⇄ CoreFour Inc. (Edsby)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name) — 43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9 — buyer tax no. 893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)
SUBMIT TO: payables@ccsmj.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: CoreFour Inc. (Edsby) — One Apple Park Way, Cupertino, CA 95014 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: CORNERSTONE CHRISTIAN SCHOOL INC. (company (private sector), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on th
```

## Relationship
- **rank_group**: GOLD-T
- **data_quality_score**: 80
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: CORNERSTONE CHRISTIAN SCHOOL INC. (company (private sector), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: CoreFour Inc. (Edsby) | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.ccsmj.ca/Overview | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=questions, concerns or grievances you may have related to your Personal Information. We may also be reached as follows: 68B Leek Crescent, Suite 200 Richm | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor CoreFour Inc. (Edsby)
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:783a1f02630c0f63
- **tier**: T
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: CORNERSTONE CHRISTIAN SCHOOL INC.
- **buyer_website**: https://ccsmj.ca/
- **buyer_address**: 43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9
- **buyer_phone**: 306 693 2937
- **buyer_contact_evidence_url**: https://www.ccsmj.ca/contact
- **buyer_legal_name_as_published**: CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)
- **buyer_bn_as_published**: 893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 893970970RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.ccsmj.ca/graphics/sb_ccsmj/apple-touch-icon.png?v=20261015
- **buyer_website_status**: site answers
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.ccsmj.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: payables@ccsmj.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.ccsmj.ca/Accounts
- **email_evidence_quote**: ounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. For information on your student account or to make a payment over the phone, please contact Mrs. Barb Slessor at the CCS Office at
- **email_evidence_context**: Canteen Account Info Facility Rental Shop Facebook Twitter Search Website Contact Us The Office The Office Accounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. For information on your student account or to make a payment over the phone, please contact Mrs. Barb Slessor at the CCS Office at 306-693-2937 ext. 232 The Office Report Student Absence The Office How Can We Help You Today? Office Hours Accounts & (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: payables@ccsmj.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.ccsmj.ca/Accounts | quote: "ounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. F" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00038
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; rua=mailto:smith.terry@ccsmj.ca; ruf=mailto:smith.terry@ccsmj.ca
- **dmarc_record_domain**: ccsmj.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 306-693-2937 ext. 232 (as printed on https://www.ccsmj.ca/Accounts, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "306-693-2937 ext. 232 (as printed on https://www.ccsmj.ca/Accounts, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name) — 43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9 — buyer tax no. 893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name) ⏎ SUBMIT TO: payables@ccsmj.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CoreFour Inc. (Edsby) — One Apple Park Way, Cupertino, CA 95014 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CORNERSTONE CHRISTIAN SCHOOL INC. (company (private sector), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on th
- **invoice_card_json**: {"bill_to": {"legal_name": "CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)", "legal_name_is_published": true, "address": "43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9", "address_is_the_invoice_address": false, "tax_number": "893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)", "language": "en"}, "submit_to": {"email": "payables@ccsmj.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: CoreFour Inc. (Edsby)
- **vendor_address**: One Apple Park Way, Cupertino, CA 95014
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=questions, concerns or grievances you may have related to your Personal Information. We may also be reached as follows: 68B Leek Crescent, Suite 200 Richmond Hill, Ontario L4B 1H1 Canada +1 (877) 337-0070 17.0 California
- **vendor_website**: https://apps.apple.com/
- **vendor_contact_evidence_url**: https://www.apple.com/contact/
- **vendor_logo_url**: https://apps.apple.com/assets/favicon/favicon-180.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://apps.apple.com/ca/app/edsby/id548642814 (on Watch TV Edsby Empowering K-12 Free Share 558 Ratings 1.8 Age Rating 4+ In-App Controls Chart #84 Education Developer CoreFour Inc. Language EN English Size )
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); phone / role e-mails / logo: the vendor's own site, https://www.apple.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://apps.apple.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor CoreFour Inc. (Edsby)
- **award_date**: 2026-11-03
- **contract_link**: https://www.ccsmj.ca/Overview
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 893970970RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name) — 43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9 — buyer tax no. 893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name) ⏎ SUBMIT TO: payables@ccsmj.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CoreFour Inc. (Edsby) — One Apple Park Way, Cupertino, CA 95014 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CORNERSTONE CHRISTIAN SCHOOL INC. (company (private sector), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on th
- **invoice_card_json**: {"bill_to": {"legal_name": "CORNERSTONE CHRISTIAN SCHOOL INC. (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)", "legal_name_is_published": true, "address": "43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9", "address_is_the_invoice_address": false, "tax_number": "893970970RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ccsmj.ca) + name)", "language": "en"}, "submit_to": {"email": "payables@ccsmj.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["payables@ccsmj.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.ccsmj.ca/Accounts", "quote: \"ounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. F\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00038"], "buyer_facts": ["address and phone: the buyer's own site, https://www.ccsmj.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "phone / role e-mails / logo: the vendor's own site, https://www.apple.com/contact/ (tools/org_contacts.py, org_extras.

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.ccsmj.ca/Accounts | 2026-11-08 | ok |  |  |  | 306-693-2937 ext. 232 |  |  |  |  |  |

## Buyer site facts (org_extras, ccsmj.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **domain**: ccsmj.ca
- **key**: lead:783a1f02630c0f63
- **name**: CORNERSTONE CHRISTIAN SCHOOL INC.
- **website**: https://ccsmj.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **logo_url**: https://www.ccsmj.ca/graphics/sb_ccsmj/apple-touch-icon.png?v=20261015
- **logo_basis**: site icon (apple-touch-icon)

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "43 Iroquois Street East, Moose Jaw, Saskatchewan, Canada, S6H 4S9", "address_country": "CA", "address_url": "https://www.ccsmj.ca/contact", "address_method": "pattern", "address_quote": "Christian School Address: 43 Iroquois Street East Moose Jaw Saskatchewan Canada S6H 4S9 Email: ccsoffice@ccsmj.ca Phone: 306 693 2937 Fax: 306 694 1880 Contact Us Cont", "phone": "306 693 2937", "phone_url": "https://www.ccsmj.ca/contact", "domain": "ccsmj.ca", "key": "lead:783a1f02630c0f63", "name": "CORNERSTONE CHRISTIAN SCHOOL INC.", "website": "https://ccsmj.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | CORNERSTONE CHRISTIAN SCHOOL INC. | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=CORNERSTONE%20CHRISTIAN%20SCHOOL%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | CORNERSTONE CHRISTIAN SCHOOL INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:783a1f02630c0f63",
 "ap_contact_team": {
  "emails": [
   "payables@ccsmj.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "payables@ccsmj.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ccsmj.ca/Accounts",
    "quote": "ounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. For information on your student account or to make a payment over the phone, please contact Mrs. Barb Slessor at the CCS Office at",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "CORNERSTONE CHRISTIAN SCHOOL INC.",
    "task_id": "CL-LD-17481"
   },
   {
    "email": "payables@ccsmj.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ccsmj.ca/Accounts",
    "quote": "ounts & Payment Any account payments can be made either in person at the CCS Office by cash, cheque, or E-transfers which can be emailed to payables@ccsmj.ca. For information on your student account or to make a payment over the phone, please contact Mrs. Barb Slessor at the CCS Office at",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "CORNERSTONE CHRISTIAN SCHOOL INC.",
    "task_id": "CL-WS-00038"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of ccsmj.ca (11 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

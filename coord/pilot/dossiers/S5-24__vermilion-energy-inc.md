# S5-24 — VERMILION ENERGY INC ⇄ Petrel Robertson Consulting (Canada)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: VERMILION ENERGY INC — 3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3
SUBMIT TO: ap_invoices@vermilionenergy.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.openinvoice.com — OpenInvoice / Enverus | format: invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Petrel Robertson Consulting (Canada) — Calgary (headquarters per Wikidata Q30295388; not the registered address) | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Clients - Petrel Robertson Consulting Ltd.
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 68
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: VERMILION ENERGY INC (utility / public corporation, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Petrel Robertson Consulting (Canada) | subject: Clients - Petrel Robertson Consulting Ltd. | published by: the Canada-located vendor's own website | record: https://www.petrelrob.com/clients | vendor in Canada because: vendor located in Canada (wd)=petrelrob.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:cea2f9c345b3e741
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: VERMILION ENERGY INC
- **buyer_website**: https://vermilionenergy.com/
- **buyer_address**: 3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3
- **buyer_phone**: 1-403-269-4884
- **buyer_contact_evidence_url**: https://www.vermilionenergy.com/contact-us/
- **buyer_legal_name_as_published**: VERMILION ENERGY INC
- **buyer_logo_url**: https://www.vermilionenergy.com/wp-content/uploads/2022/08/head-logo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/65851/
- **buyer_registry_id**: 2015489657 (AB; https://ised-isde.canada.ca/cbr-rec/en/search?q=VERMILION%20ENERGY%20INC)
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 2015489657, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.vermilionenergy.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: EFT as the preferred (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap_invoices@vermilionenergy.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf
- **email_evidence_quote**: ds. • Can I send multiple invoices in one email? o No, please send one email per invoice with the Excel template. 2 o The email you send to AP_invoices@vermilionenergy.com should contain one Excel template and a PDF of your invoice (including any associated backup). o If you have more Exce
- **email_evidence_context**: s laid out by the template) you can insert a lump sum amount and not use the quantity and unit of measure fields. • Can I send multiple invoices in one email? o No, please send one email per invoice with the Excel template. 2 o The email you send to AP_invoices@vermilionenergy.com should contain one Excel template and a PDF of your invoice (including any associated backup). o If you have more Excel files or other document types to send as backup for your invoice, please email those documents to accountspayable@vermilionenergy (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap_invoices@vermilionenergy.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf | quote: "ds. • Can I send multiple invoices in one email? o No, please send one email per invoice with the Excel template. 2 o The email you send to AP_invoices@vermilio" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_deep01.csv task CL-DA-00986
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc@vermilionenergy.com; ruf=mailto:dmarc@vermilionenergy.com; sp=reject; fo=1;
- **dmarc_record_domain**: vermilionenergy.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:74.200.30.37 ip4:64.141.40.239 ip4:207.236.101.74 ip4:40.78.111.145 ip4:61.95.108.160/28 a:smtp.concurcompleat.com mx:taleo.net include:spf.protection.outlook.com include:spf.afas.online include:proxy.afas.online include:lms.plusport.com include:_spf.psm.knowbe4.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://www.openinvoice.com — OpenInvoice / Enverus
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: OpenInvoice / Enverus (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "https://www.openinvoice.com — OpenInvoice / Enverus", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)", "requirements_text": "invoice format as published: invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: VERMILION ENERGY INC — 3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3 ⏎ SUBMIT TO: ap_invoices@vermilionenergy.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.openinvoice.com — OpenInvoice / Enverus | format: invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Petrel Robertson Consulting (Canada) — Calgary (headquarters per Wikidata Q30295388; not the registered address) | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Clients - Petrel Robertson Consulting Ltd.
- **invoice_card_json**: {"bill_to": {"legal_name": "VERMILION ENERGY INC", "legal_name_is_published": true, "address": "3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "ap_invoices@vermilionenergy.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.openinvoice.com — OpenInvoice / Enverus", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)", "system": "named on the buyer's page: OpenInvoice / Enverus (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "EFT as the preferred (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 76
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; PO rule published; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Petrel Robertson Consulting (Canada)
- **vendor_address**: Calgary (headquarters per Wikidata Q30295388; not the registered address)
- **vendor_country_basis**: vendor located in Canada (wd)=petrelrob.com
- **vendor_website**: https://petrelrob.com
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); website: https://petrelrob.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q30295388; business
- **vendor_founded**: 1972-01-01 (Wikidata Q30295388, official website on the organisation's domain (http://www.petrelrob.com/) + name; 2026-11-08)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Clients - Petrel Robertson Consulting Ltd.
- **contract_description**: Clients - Petrel Robertson Consulting Ltd. (the record's title; the source publishes no separate description)
- **contract_link**: https://www.petrelrob.com/clients
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: VERMILION ENERGY INC — 3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3 ⏎ SUBMIT TO: ap_invoices@vermilionenergy.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://www.openinvoice.com — OpenInvoice / Enverus | format: invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Petrel Robertson Consulting (Canada) — Calgary (headquarters per Wikidata Q30295388; not the registered address) | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Clients - Petrel Robertson Consulting Ltd.
- **invoice_card_json**: {"bill_to": {"legal_name": "VERMILION ENERGY INC", "legal_name_is_published": true, "address": "3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "ap_invoices@vermilionenergy.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.openinvoice.com — OpenInvoice / Enverus", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "invoices changing? in PDF (as printed on https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf, re-read 2026-11-08)", "system": "named on the buyer's page: OpenInvoice / Enverus (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "EFT as the preferred (as printed on https://www.vermilionenergy.com/our-operations/vendors/, re-read 2026-11-08)", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 76
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; PO rule published; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["ap_invoices@vermilionenergy.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf", "quote: \"ds. • Can I send multiple invoices in one email? o No, please send one email per invoice with the Excel template. 2 o The email you send to AP_invoices@vermilio\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_deep01.csv task CL-DA-00986"], "buyer_facts": ["address and phone: the buyer's own site, https://www.vermilionenergy.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "website: https://petrelrob.com"], "relat

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, vermilionenergy.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: VERMILION ENERGY INC
- **legal_name_url**: https://www.vermilionenergy.com/
- **legal_name_quote**: alia: +61 8 9215 0300 About Us Invest With Us Our Operations Our Responsibility Careers News © 2026 VERMILION ENERGY INC. LEGAL / PRIVACY / ABBREVIATIONS / CONTACT
- **logo_url**: https://www.vermilionenergy.com/wp-content/uploads/2022/08/head-logo.png
- **logo_basis**: logo image in the site header
- **domain**: vermilionenergy.com
- **key**: lead:cea2f9c345b3e741
- **name**: VERMILION ENERGY INC
- **website**: https://vermilionenergy.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Vermilion Energy
- **jsonld_logo**: https://www.vermilionenergy.com/wp-content/uploads/2022/07/Vermilion_Energy-logo.svg
- **jsonld_url**: https://www.vermilionenergy.com/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://www.vermilionenergy.com/","url":"https://www.vermilionenergy.com/","name":"Home - Vermilion Energy","isPartOf":{"@id":"https://www.vermilionenergy.com/#website"},"about":{"@id":"https://www.vermilionenergy.com/#organization
- **jsonld_page**: https://www.vermilionenergy.com/
- **legal_name_stated**: Central & Eastern Europe
- **legal_name_stated_url**: https://www.vermilionenergy.com/about-us/
- **legal_name_stated_quote**: out Our Operations Our Operations Canadian Vendors Canada Europe France Netherlands Germany Ireland Central & Eastern Europe (CEE) Australia Wandoo Consultation Activities View our Sustainability > Sustainability Our Respons
- **linkedin_url**: https://www.linkedin.com/company/65851/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "3500, 520 3rd Avenue SW, Calgary, Alberta T2P 0R3", "address_country": "CA", "address_url": "https://www.vermilionenergy.com/contact-us/", "address_method": "pattern", "address_quote": "lion Head Office Vermilion Energy Inc. 3500, 520 3rd Avenue SW Calgary, Alberta T2P 0R3 Phone 1-403-269-4884 Fax 1-403-476-8100 Investor Relations 1-866-895-8101 Email", "phone": "1-403-269-4884", "phone_url": "https://www.vermilionenergy.com/contact-us/", "domain": "vermilionenergy.com", "key": "lead:cea2f9c345b3e741", "name": "vermilionenergy.com", "website": "https://vermilionenergy.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | VERMILION ENERGY INC | found | VERMILION ENERGY INC. |  | 2015489657 | AB | Alberta Business Corporation | Inactive | 2010-07-21 | CALGARY | ALBERTA |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=VERMILION%20ENERGY%20INC | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | VERMILION ENERGY INC |  |  |  |  |  |  |  |  |  |  |
| b | Petrel Robertson Consulting (Canada) | Q30295388 | official website on the organisation's domain (http://www.petrelrob.com/) + name |  | Petrel Robertson Consulting (Canada) |  | business |  | Canada | 1972-01-01 | Calgary |
| v | Petrel Robertson Consulting (Canada) | Q30295388 | official website on the organisation's domain (http://www.petrelrob.com/) + name |  | Petrel Robertson Consulting (Canada) |  | business |  | Canada | 1972-01-01 | Calgary |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:cea2f9c345b3e741",
 "ap_contact_team": {
  "emails": [
   "ap_invoices@vermilionenergy.com",
   "accountspayable@vermilionenergy.com",
   "payables@tmaxenergy.ca",
   "ap@alliedenergy2.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "ap_invoices@vermilionenergy.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf",
    "quote": "ds. • Can I send multiple invoices in one email? o No, please send one email per invoice with the Excel template. 2 o The email you send to AP_invoices@vermilionenergy.com should contain one Excel template and a PDF of your invoice (including any associated backup). o If you have more Exce",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "Vermilion Energy Inc. (France)",
    "task_id": "CL-DA-00986"
   },
   {
    "email": "accountspayable@vermilionenergy.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf",
    "quote": "mer department Accounts Payable – Canada. • If your company does not currently use OpenInvoice, please email your invoices in PDF format to accountspayable@vermilionenergy.com • Please do not combine invoices at this time. You will receive notification when invoices can be combined for sub",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "vermilionenergy.com",
    "task_id": "CL-LD-07416"
   },
   {
    "email": "payables@tmaxenergy.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.vermilionenergy.com/wp-content/uploads/2025/02/VET-Westbrick-Vendor-Notice.pdf",
    "quote": "nt to Vermilion will be rejected. The invoicing details for TMax Energy are as follows: TMax Energy P.O.Box 7832 Drayton Valley, AB T7A 1S9 payables@tmaxenergy.ca Asset Type From To Asset Type From To Pipeline 11-22-049-12W5 16-35-048-12W5 Pipeline 05-21-049-11W5 08-24-049-12W5 Pipeline 16",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "vermilionenergy.com",
    "task_id": "CL-LD-07416"
   },
   {
    "email": "ap@alliedenergy2.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.vermilionenergy.com/wp-content/uploads/2025/07/SK-and-MB-Vendor-Letter.pdf",
    "quote": ". contact information is as follows: Allied Energy II Corp. Suite 500 400 5th Avenue SW Calgary Alberta T2P 0L6 Phone (587) 392-9201 Email: ap@alliedenergy2.ca If you have any questions or concerns regarding this notice, please e-mail Vermilion at",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "vermilionenergy.com",
    "task_id": "CL-LD-07416"
   },
   {
    "email": "accountspayable@vermilionenergy.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.vermilionenergy.com/wp-content/uploads/2023/05/Vermilion-Invoice-Coding-Template-Guide.pdf",
    "quote": "r Number Enter your Vermilion vendor code. Note: Vendor numbers have been updated - to find out your new vendor number, please reach out to accountspayable@vermilionenergy.com. Company Code Defaulted to 1020 – please do not change this unless you have been notified by our AP team. Invoice",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "Vermilion Energy Inc. (France)",
    "task_id": "CL-DA-00986"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of vermilionenergy.com (13 pages, robots.txt respected), no AI, no search engine",
  "site crawl of vermilionenergy.com (13 pages, robots.txt respected), no AI, no search engine",
  "site crawl of vermilionenergy.com (13 pages, robots.txt respected), no AI, no search engine",
  "Wayback Machine URL index of vermilionenergy.com (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine",
  "Wayback Machine URL index of vermilionenergy.com (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine"
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

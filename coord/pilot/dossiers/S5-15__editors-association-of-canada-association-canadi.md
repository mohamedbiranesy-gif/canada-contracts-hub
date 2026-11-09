# S5-15 — Editors' Association of Canada / Association canadienne des réviseurs ⇄ Young Associates

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Editors' Association of Canada / Association canadienne des réviseurs — PO Box 45655, Surrey, BC V4A 9N3
SUBMIT TO: treasurer@editors.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Young Associates — 2550 Victoria Park Avenue Suite 501, Toronto, Ontario, M2J 5A9 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-0
DESCRIPTION: Reference Links - Young Associates
```

## Relationship
- **rank_group**: E3
- **data_quality_score**: 55
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Editors' Association of Canada / Association canadienne des réviseurs (non-profit / association / cultural body, jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Young Associates | subject: Reference Links - Young Associates | published by: the Canada-located vendor's own website | record: https://youngassociates.ca/links/ | vendor in Canada because: vendor located in Canada (wd)=youngassociates.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:12722405f412879c
- **tier**: E
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Editors' Association of Canada / Association canadienne des réviseurs
- **buyer_website**: https://editors.ca/
- **buyer_address**: PO Box 45655, Surrey, BC V4A 9N3
- **buyer_contact_evidence_url**: https://editors.ca/about/contact-us/
- **buyer_legal_name_as_published**: Editors' Association of Canada / Association canadienne des réviseurs
- **buyer_logo_url**: https://editors.ca/wp-content/themes/Editors-Canada-child-main-English/img/logo/logo-sm-light.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/editors-association-of-canada-association-canadienne-des-reviseurs/
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://editors.ca/about/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: treasurer@editors.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://editors.ca/about/governance/national-executive-council/
- **email_evidence_quote**: "https://blog.editors.ca/the-nec-in-detail-vice-president-and-treasurer/">Learn more</a>.)</p> <h4 class="wp-block-heading"><a href="mailto:treasurer@editors.ca">Błażej Szpakowicz</a></h4> <p class="wp-block-paragraph">Editors British Columbia</p> <p class="wp-block-paragraph">A former aca
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: treasurer@editors.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://editors.ca/about/governance/national-executive-council/ | quote: ""https://blog.editors.ca/the-nec-in-detail-vice-president-and-treasurer/">Learn more</a>.)</p> <h4 class="wp-block-heading"><a href="mailto:treasurer@editors.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-28281
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:heartfelt@editors.ca; pct=10; adkim=r; aspf=r
- **dmarc_record_domain**: editors.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:198.27.74.64 +ip4:70.32.100.63 +ip4:173.255.152.101 +ip4:162.212.202.67 +ip4:173.240.3.29 +ip4:198.2.129.12 +ip4:159.203.6.15 +include:servers.mcsv.net +mx:webhost2.editors.ca +mx:editors.ca +include:_spf.google.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: 30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-06-07-1.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-06-07-1.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Editors' Association of Canada / Association canadienne des réviseurs — PO Box 45655, Surrey, BC V4A 9N3 ⏎ SUBMIT TO: treasurer@editors.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Young Associates — 2550 Victoria Park Avenue Suite 501, Toronto, Ontario, M2J 5A9 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-0 ⏎ DESCRIPTION: Reference Links - Young Associates
- **invoice_card_json**: {"bill_to": {"legal_name": "Editors' Association of Canada / Association canadienne des réviseurs", "legal_name_is_published": true, "address": "PO Box 45655, Surrey, BC V4A 9N3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@editors.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-06-07-1.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Young Associates", "bn9": "", "neq": "", "remit_address": "2550 Victoria Park Avenue Suite 501, Toronto, Ontar
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Young Associates
- **vendor_address**: 2550 Victoria Park Avenue Suite 501, Toronto, Ontario, M2J 5A9
- **vendor_country_basis**: vendor located in Canada (wd)=youngassociates.ca
- **vendor_website**: https://youngassociates.ca
- **vendor_emails**: info@youngassociates.ca
- **vendor_phone**: 416.923.8557
- **vendor_contact_evidence_url**: https://youngassociates.ca/contact/
- **vendor_logo_url**: https://youngassociates.ca/wp-content/uploads/2026/05/YoungAssociates-Logo-transparent.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://youngassociates.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://youngassociates.ca (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Reference Links - Young Associates
- **contract_description**: Reference Links - Young Associates (the record's title; the source publishes no separate description)
- **contract_link**: https://youngassociates.ca/links/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Editors' Association of Canada / Association canadienne des réviseurs — PO Box 45655, Surrey, BC V4A 9N3 ⏎ SUBMIT TO: treasurer@editors.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Young Associates — 2550 Victoria Park Avenue Suite 501, Toronto, Ontario, M2J 5A9 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-0 ⏎ DESCRIPTION: Reference Links - Young Associates
- **invoice_card_json**: {"bill_to": {"legal_name": "Editors' Association of Canada / Association canadienne des réviseurs", "legal_name_is_published": true, "address": "PO Box 45655, Surrey, BC V4A 9N3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@editors.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "30 days from the receipt (as printed on https://editors.ca/wp-content/uploads/2023/08/Bylaw_1-2014-06-07-1.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Young Associates", "bn9": "", "neq": "", "remit_address": "2550 Victoria Park Avenue Suite 501, Toronto, Ontar
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["treasurer@editors.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://editors.ca/about/governance/national-executive-council/", "quote: \"\"https://blog.editors.ca/the-nec-in-detail-vice-president-and-treasurer/\">Learn more</a>.)</p> <h4 class=\"wp-block-heading\"><a href=\"mailto:treasurer@editors.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-28281"], "buyer_facts": ["address and phone: the buyer's own site, https://editors.ca/about/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://youngassociates.ca/contact/ (tools/org_contacts.py, org_extras.py)", "website: https://youngassociates.ca (s

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://editors.ca/about/governance/national-executive-council/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, editors.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Editors' Association of Canada / Association canadienne des réviseurs
- **legal_name_url**: https://editors.ca/
- **legal_name_quote**: orrespondence only): 2967 Dundas Street West, #1449 Toronto, Ontario M6P 1Z2 info@editors.ca © 2026 Editors' Association of Canada / Association canadienne des réviseurs Designed & Developed by: Mango Innovation Copyright Notice Privacy Policy To top
- **logo_url**: https://editors.ca/wp-content/themes/Editors-Canada-child-main-English/img/logo/logo-sm-light.svg
- **logo_basis**: logo image in the site header
- **domain**: editors.ca
- **key**: lead:12722405f412879c
- **name**: Editors' Association of Canada / Association canadienne des réviseurs
- **website**: https://editors.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Editors Canada
- **jsonld_logo**: https://editors.ca/wp-content/uploads/2024/01/Editors_canada_EN_rgb.png
- **jsonld_url**: https://editors.ca/
- **jsonld_same_as**: https://www.facebook.com/pages/Editors-Association-of-Canada-Association-canadienne-des-rviseurs/271502192279; https://x.com/editorscanada; https://www.linkedin.com/company/editors-association-of-canada-association-canadienne-des-reviseurs/; http://instagram.com/editorscanada
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/editors.ca\/","url":"https:\/\/editors.ca\/","name":"Editors Canada","isPartOf":{"@id":"https:\/\/editors.ca\/#website"},"about":{"@id":"https:\/\/editors.ca\/#organization"},"datePublished":"2023-05-04T23:35:47+00:00",
- **jsonld_page**: https://editors.ca/
- **legal_name_stated**: Indigenous Editors Association
- **legal_name_stated_url**: https://editors.ca/about/
- **legal_name_stated_quote**: ning Chartered Institute of Editing and Proofreading (CIEP) Editorial Freelancers Association (EFA) Indigenous Editors Association (IEA) Institute of Professional Editors (IPEd) JSTOR Literary Review of Canada Northwest Editors Gu
- **mentions**: {'payment_method': {'text': 'Interactive Voice to give all members a chance to voice their concerns or perspectives', 'url': 'https://editors.ca/about/governance/structure/', 'quote': 'the focus of the 2010 national conference. In the months following the AGM, a thread was started on Interactive Voice to give all members a chance to voice their concerns or perspectives regarding the NEC’s plans. A new version of our discussion paper, called'}}
- **linkedin_url**: https://www.linkedin.com/company/editors-association-of-canada-association-canadienne-des-reviseurs/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "PO Box 45655, Surrey, BC V4A 9N3", "address_country": "CA", "address_url": "https://editors.ca/about/contact-us/", "address_method": "pattern", "address_quote": "site Email: calgary@editors.ca Editors British Columbia PO Box 45655 Surrey, BC V4A 9N3 Website Email: bc@editors.ca Editors Edmonton Website Email: edmonton@editors.c", "emails": "info@editors.ca", "emails_url": "https://editors.ca/about/contact-us/", "domain": "editors.ca", "key": "vd:editors.ca", "name": "Association canadienne des réviseurs", "website": "https://editors.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, youngassociates.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://youngassociates.ca/wp-content/uploads/2026/05/YoungAssociates-Logo-transparent.png
- **logo_basis**: logo image in the site header
- **domain**: youngassociates.ca
- **key**: vendor:Young Associates
- **name**: Young Associates
- **website**: https://youngassociates.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Payroll Compliance Professional
- **legal_name_stated_url**: https://youngassociates.ca/about-us/
- **legal_name_stated_quote**: P, Payroll Manager Read Bio Candi (she/her) joined Young Associates in July 2020 and is a certified Payroll Compliance Professional (PCP) through the National Payroll Institute. With more than a decade of experience in finance admi
- **mentions**: {'tax_exempt': {'text': 'HST rebates, managing complex grant reconciliation reports and preparing accurate CRA fili', 'url': 'https://youngassociates.ca/', 'quote': 'rities and non-profit organizations face increasingly technical compliance requirements. Navigating HST rebates, managing complex grant reconciliation reports and preparing accurate CRA filings such as the T3010 charity return can be daunting without the right'}, 'payment_method': {'text': 'interact with according the privacy standards of PIPEDA and CASL', 'url': 'https://youngassociates.ca/privacy-policy/', 'quote': 'requirements
- **tel_links**: 416-923-8557

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2550 Victoria Park Avenue Suite 501, Toronto, Ontario, M2J 5A9", "address_country": "CA", "address_url": "https://youngassociates.ca/contact/", "address_method": "pattern", "address_quote": "@youngassociates.ca Office 2550 Victoria Park Avenue Suite 501 Toronto, Ontario M2J 5A9 Let’s Connect Tell us a bit about your organization and what you’re looking for", "phone": "416.923.8557", "phone_url": "https://youngassociates.ca/contact/", "emails": "info@youngassociates.ca", "emails_url": "https://youngassociates.ca/contact/", "domain": "youngassociates.ca", "key": "vd:youngassociates.ca", "name": "Young Associates", "website": "https://youngassociates.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Editors' Association of Canada / Association canadienne des réviseurs | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Editors%27%20Association%20of%20Canada%20%2F%20Association%20canadienne%20des%20r%C3%A9viseurs | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Editors' Association of Canada / Association canadienne des réviseurs |  |  |  |  |  |  |  |  |  |  |
| b | Young Associates |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:12722405f412879c",
 "ap_contact_team": {
  "emails": [
   "info@editors.ca",
   "treasurer@editors.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@editors.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://editors.ca/",
    "quote": "ekly Member portal Editors Canada Virtual office address (for correspondence only): 2967 Dundas Street West, #1449 Toronto, Ontario M6P 1Z2 info@editors.ca © 2026 Editors' Association of Canada / Association canadienne des réviseurs Designed & Developed by: Mango Innovation Copyright Notic",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "editors.ca",
    "task_id": "CL-LD-15067"
   },
   {
    "email": "treasurer@editors.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://editors.ca/about/governance/national-executive-council/",
    "quote": "\"https://blog.editors.ca/the-nec-in-detail-vice-president-and-treasurer/\">Learn more</a>.)</p> <h4 class=\"wp-block-heading\"><a href=\"mailto:treasurer@editors.ca\">Błażej Szpakowicz</a></h4> <p class=\"wp-block-paragraph\">Editors British Columbia</p> <p class=\"wp-block-paragraph\">A former aca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "editors.ca",
    "task_id": "CL-LD-28281"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of editors.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of editors.ca (49 pages, robots.txt respected), no AI, no search engine"
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

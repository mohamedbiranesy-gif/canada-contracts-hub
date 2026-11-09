# S3-01 — Sault Ste. Marie Public Library ⇄ BiblioCommons Corp.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/) — 50 East St., Sault Ste. Marie, ON P6A 3C3 — buyer tax no. 119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name)
SUBMIT TO: admin.child.lib@cityssm.on.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Sault Ste. Marie Public Library | BiblioCommons
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 52
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Sault Ste. Marie Public Library (non-profit / association / cultural body, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: BiblioCommons Corp. | subject: Sault Ste. Marie Public Library | BiblioCommons | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://ssmpl.bibliocommons.com/v2/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5 | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:0b658f993c09d9d5
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Sault Ste. Marie Public Library
- **buyer_website**: https://ssmpl.ca/
- **buyer_address**: 50 East St., Sault Ste. Marie, ON P6A 3C3
- **buyer_contact_evidence_url**: https://ssmpl.ca/about-us/hours-locations/
- **buyer_legal_name_as_published**: ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/)
- **buyer_bn_as_published**: 119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 119141828RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://ssmpl.ca/images/HeaderGraphics/ssmpl_logo.png
- **buyer_website_status**: site answers
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name)
- **buyer_charity_designation**: C; 0200
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q53678144; library network; public library; charitable organization
- **buyer_budget_or_revenue**: revenue 2568569 Q1104069; 2675927 Q1104069; 3249086 Q1104069; 2862419 Q1104069; 3090897 Q1104069; 3217497 Q1104069; 3145084 Q110 (Wikidata Q53678144, official website on the organisation's domain (http://www.ssmpl.ca) + name; 2026-11-08)
- **buyer_employees**: 62; 66; 64; 60; 65; 72; 73; 78; 80; 58; 67; 59; 44; 51 (Wikidata Q53678144, official website on the organisation's domain (http://www.ssmpl.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://ssmpl.ca/about-us/hours-locations/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: admin.child.lib@cityssm.on.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://ssmpl.ca/about-us/contact/
- **email_evidence_quote**: r /> Fax: 705-759-8752</span></td> <td><span style="font-size:14px;">Children's Services<br /> Phone: 705-759-5241<br /> <u><a href="mailto:admin.child.lib@cityssm.on.ca">
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: admin.child.lib@cityssm.on.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04 | page: https://ssmpl.ca/about-us/contact/ | quote: "r /> Fax: 705-759-8752</span></td> <td><span style="font-size:14px;">Children's Services<br /> Phone: 705-759-5241<br /> <u><a href="mailto:admin.child.lib@city" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00029
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.cityssm.on.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx ip4:209.105.201.123 include:spf.protection.outlook.com include:sparkpostmail.com include:relay01.evenue.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/) — 50 East St., Sault Ste. Marie, ON P6A 3C3 — buyer tax no. 119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name) ⏎ SUBMIT TO: admin.child.lib@cityssm.on.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Sault Ste. Marie Public Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/)", "legal_name_is_published": true, "address": "50 East St., Sault Ste. Marie, ON P6A 3C3", "address_is_the_invoice_address": false, "tax_number": "119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name)", "language": "en"}, "submit_to": {"email": "admin.child.lib@cityssm.on.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "ven
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: BiblioCommons Corp.
- **vendor_legal_name**: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_registry_id**: 2733173 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=BiblioCommons%20Corp.
- **vendor_registered_address**: Mississauga, Ontario (registered office city / province; Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_address**: 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5
- **vendor_bn9**: 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2733173, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2019-12-19
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_incorporation_date**: 2019-12-19
- **vendor_years_in_business**: 6.9 (since 2019-12-19, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2733173, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **contract_title**: Sault Ste. Marie Public Library | BiblioCommons
- **contract_description**: Sault Ste. Marie Public Library | BiblioCommons (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://ssmpl.bibliocommons.com/v2/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 119141828RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/) — 50 East St., Sault Ste. Marie, ON P6A 3C3 — buyer tax no. 119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name) ⏎ SUBMIT TO: admin.child.lib@cityssm.on.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Sault Ste. Marie Public Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "ABOUT US Hours & Locations Contact Our Library Board (stated on https://ssmpl.ca/about-us/)", "legal_name_is_published": true, "address": "50 East St., Sault Ste. Marie, ON P6A 3C3", "address_is_the_invoice_address": false, "tax_number": "119141828RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (ssmpl.ca) + name)", "language": "en"}, "submit_to": {"email": "admin.child.lib@cityssm.on.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "ven
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["admin.child.lib@cityssm.on.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04", "page: https://ssmpl.ca/about-us/contact/", "quote: \"r /> Fax: 705-759-8752</span></td> <td><span style=\"font-size:14px;\">Children's Services<br /> Phone: 705-759-5241<br /> <u><a href=\"mailto:admin.child.lib@city\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00029"], "buyer_facts": ["address and phone: the buyer's own site, https://ssmpl.ca/about-us/hours-locations/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data"

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://ssmpl.ca/about-us/contact/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, ssmpl.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://ssmpl.ca/images/HeaderGraphics/ssmpl_logo.png
- **logo_basis**: logo image in the site header
- **domain**: ssmpl.ca
- **key**: lead:0b658f993c09d9d5
- **name**: Sault Ste. Marie Public Library
- **website**: https://ssmpl.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: ABOUT US Hours & Locations Contact Our Library Board
- **legal_name_stated_url**: https://ssmpl.ca/about-us/
- **legal_name_stated_quote**: S SEARCH CATALOGUE Website Catalogue Sault Ste. Marie Public Library HOME > ABOUT US Text Size: A A ABOUT US Hours & Locations Contact Our Library Board Strategic Plan Policies Employment Volunteer Support Your Library Friends of the Library Home · Usi

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "50 East St., Sault Ste. Marie, ON P6A 3C3", "address_country": "CA", "address_url": "https://ssmpl.ca/about-us/hours-locations/", "address_method": "pattern", "address_quote": "ck HERE ) James L. McIntyre Centennial Library 50 East St. Sault Ste. Marie, ON P6A 3C3 705-759-5230 Monday - Thursday 9:00am - 9:00pm Friday 9:00am - 6:00pm Saturday", "domain": "ssmpl.ca", "key": "lead:0b658f993c09d9d5", "name": "Sault Ste. Marie Public Library", "website": "https://ssmpl.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Sault Ste. Marie Public Library | Q53678144 | official website on the organisation's domain (http://www.ssmpl.ca) + name |  | Sault Ste. Marie Public Library |  | library network; public library; charitable organization |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:0b658f993c09d9d5",
 "ap_contact_team": {
  "emails": [
   "admin.library@cityssm.on.ca",
   "admin.child.lib@cityssm.on.ca",
   "admin.lib.circ4@cityssm.on.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "admin.library@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "Text Size: A A Contact To submit an online question or comment please use the Ask a Question form Administration Office Phone: 705-759-5242 admin.library@cityssm.on.ca Fax: 705-759-8752 Children's Services Phone: 705-759-5241",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-LD-42169"
   },
   {
    "email": "admin.child.lib@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "r /> Fax: 705-759-8752</span></td> <td><span style=\"font-size:14px;\">Children's Services<br /> Phone: 705-759-5241<br /> <u><a href=\"mailto:admin.child.lib@cityssm.on.ca\">",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-LD-42169"
   },
   {
    "email": "admin.lib.circ4@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "a</a></u></span></td> <td><span style=\"font-size:14px;\">Account and Circulation Services<br /> Phone: 705-759-5231<br /> <u><a href=\"mailto:admin.lib.circ4@cityssm.on.ca\">",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-LD-42169"
   },
   {
    "email": "admin.child.lib@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "r /> Fax: 705-759-8752</span></td> <td><span style=\"font-size:14px;\">Children's Services<br /> Phone: 705-759-5241<br /> <u><a href=\"mailto:admin.child.lib@cityssm.on.ca\">",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-WS-00029"
   },
   {
    "email": "admin.library@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "Text Size: A A Contact To submit an online question or comment please use the Ask a Question form Administration Office Phone: 705-759-5242 admin.library@cityssm.on.ca Fax: 705-759-8752 Children's Services Phone: 705-759-5241",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-WS-00029"
   },
   {
    "email": "admin.lib.circ4@cityssm.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ssmpl.ca/about-us/contact/",
    "quote": "a</a></u></span></td> <td><span style=\"font-size:14px;\">Account and Circulation Services<br /> Phone: 705-759-5231<br /> <u><a href=\"mailto:admin.lib.circ4@cityssm.on.ca\">",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Sault Ste. Marie Public Library",
    "task_id": "CL-WS-00029"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of ssmpl.ca (15 pages, robots.txt respected), no AI, no search engine",
  "site crawl of ssmpl.ca (15 pages, robots.txt respected), no AI, no search engine",
  "site crawl of ssmpl.ca (15 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

## The vendor's other buyers in the dataset (first 60 of 6)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:32761475-333e-41ac-b891-ffddc5f83ade:1 | City of Mississauga | Library Online Resource Discovery & Mobile App |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/32761475-333e-41ac-b891-ffddc5f83ade |
| us_county_fulton_ga:81357d5a48e75900-650 | Fulton County, Georgia — Library | Books-Library | 1042856.5700000001 |  |  | https://data.fultoncountyga.gov/d/mxhc-krcg |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~75a33202896d | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~1e00a517d323 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~c355691972d8 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~f8057c8ad9ef | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

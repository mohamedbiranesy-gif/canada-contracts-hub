# S4-14 — BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 ⇄ inferred: SaskPower

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Prince Albert Catholic School Division — 118 11TH STREET EAST, Prince Albert, SK, S6V1A1 — buyer tax no. 107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name)
SUBMIT TO: info@pacsd.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 (school board / school district, SK) — inferred: no re
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: HIGH (statutory or sole-provider relationship for this type of organisation)
- **relationship_detail**: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 (school board / school district, SK) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: SaskPower | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://saskpower.com/contact: 'Send us a letter: SaskPower Corporate Relations and Communications 9th Floor, 2025 Victoria Ave Regina, SK S4P 0S1' | status rule: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Saskatchewan (province from its registered address in the CRA List of charities 
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:107858359
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6
- **buyer_website**: https://pacsd.ca
- **buyer_address**: 118 11TH STREET EAST, Prince Albert, SK, S6V1A1
- **buyer_phone**: 306-953-7500
- **buyer_contact_evidence_url**: https://pacsd.ca/about-us/contact-us/
- **buyer_legal_name_as_published**: Prince Albert Catholic School Division
- **buyer_bn_as_published**: 107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 107858359RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://pacsd.ca/wp-content/uploads/PACSD-Logo.png
- **buyer_website_status**: site answers
- **buyer_supplier_portals_linked**: DocuSign (e-signature): https://ca.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=9355cdea-7c23-45ae-87a2-7ac541c627b5&env=ca&acct=1e725ad5-17b7-46b6-b919-160eff8dc255&v=2
- **buyer_type**: school board / school district
- **buyer_sector**: education: K-12
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://pacsd.ca/about-us/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@pacsd.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://pacsd.ca/
- **email_evidence_quote**: mation Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: Catholic Education Centre 118 – 11th St. East Prince Albert, Saskatchewan, Canada S6V 1A1 Copyright ©2021-2025 Prince Albert Catho
- **email_evidence_context**: Staff Email Employee Self Service Tech Help Desk School Messenger for Staff Teacher Portal T4 Reference Information Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: Catholic Education Centre 118 – 11th St. East Prince Albert, Saskatchewan, Canada S6V 1A1 Copyright ©2021-2025 Prince Albert Catholic School Division. All Rights Reserved. Instagram Page load link Go to Top (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@pacsd.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://pacsd.ca/ | quote: "mation Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-00627
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.pacsd.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:64.46.59.64/27 include:atrieveerp.com include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_system_hint**: linked from the buyer's site: DocuSign (e-signature)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prince Albert Catholic School Division — 118 11TH STREET EAST, Prince Albert, SK, S6V1A1 — buyer tax no. 107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name) ⏎ SUBMIT TO: info@pacsd.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 (school board / school district, SK) — inferred: no re
- **invoice_card_json**: {"bill_to": {"legal_name": "Prince Albert Catholic School Division", "legal_name_is_published": true, "address": "118 11TH STREET EAST, Prince Albert, SK, S6V1A1", "address_is_the_invoice_address": false, "tax_number": "107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name)", "language": "en"}, "submit_to": {"email": "info@pacsd.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "linked from the buyer's site: DocuSign (e-signature)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "11
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
- **contract_status**: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Saskatchewan (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); SaskPower holds the electricity franchise in Saskatchewan outside the Saskatoon and Swift Current municipal utilities (The Power Corporation Act); it pays electricity for the buildings it operates
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 107858359RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119429678RT0001 (R119429678 (printed in the older 'R' format on the sample business bill))

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prince Albert Catholic School Division — 118 11TH STREET EAST, Prince Albert, SK, S6V1A1 — buyer tax no. 107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name) ⏎ SUBMIT TO: info@pacsd.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SaskPower — 2025 Victoria Avenue, Regina, SK S4P 0S1 | GST/HST 119429678 (GST/HST registration number printed by the organisation itself: https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 (school board / school district, SK) — inferred: no re
- **invoice_card_json**: {"bill_to": {"legal_name": "Prince Albert Catholic School Division", "legal_name_is_published": true, "address": "118 11TH STREET EAST, Prince Albert, SK, S6V1A1", "address_is_the_invoice_address": false, "tax_number": "107858359RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (pacsd.ca) + name)", "language": "en"}, "submit_to": {"email": "info@pacsd.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "linked from the buyer's site: DocuSign (e-signature)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (SK)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "11
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@pacsd.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://pacsd.ca/", "quote: \"mation Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-00627"], "buyer_facts": ["address and phone: the buyer's own site, https://pacsd.ca/about-us/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.saskpower.com/accounts/billing/your-power-bill/how-to-read-your-bill/business)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protec

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://pacsd.ca/ | 2026-11-08 | ok |  |  |  | 306-953-7500 |  |  |  |  |  |

## Buyer site facts (org_extras, pacsd.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://pacsd.ca/wp-content/uploads/PACSD-Logo.png
- **logo_basis**: logo image on the site
- **legal_name**: Prince Albert Catholic School Division
- **legal_name_url**: https://pacsd.ca/about-us/
- **legal_name_quote**: for Staff Teacher Portal T4 Reference Information Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: Catholic Education Centre 118 – 11
- **domain**: pacsd.ca
- **key**: cra:107858359
- **name**: BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6
- **website**: https://pacsd.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Prince Albert Catholic School Divison
- **jsonld_logo**: https://pacsd.ca/wp-content/uploads/logo-job-postings-3.png
- **jsonld_url**: https://pacsd.ca/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/pacsd.ca\/","url":"https:\/\/pacsd.ca\/","name":"Home - Prince Albert Catholic School Divison","isPartOf":{"@id":"https:\/\/pacsd.ca\/#website"},"about":{"@id":"https:\/\/pacsd.ca\/#organization"},"primaryImageOfPage":{
- **jsonld_page**: https://pacsd.ca/
- **legal_name_stated**: 2021-2025 Prince Albert Catholic School Division
- **legal_name_stated_url**: https://pacsd.ca/about-us/
- **legal_name_stated_quote**: atholic Education Centre 118 – 11th St. East Prince Albert, Saskatchewan, Canada S6V 1A1 Copyright ©2021-2025 Prince Albert Catholic School Division. All Rights Reserved. Instagram Page load link /* <![CDATA[ */ /*! This file is auto-generated */ v
- **portals**: [{'name': 'DocuSign', 'kind': 'e-signature', 'url': 'https://ca.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=9355cdea-7c23-45ae-87a2-7ac541c627b5&env=ca&acct=1e725ad5-17b7-46b6-b919-160eff8dc255&v=2', 'on_page': 'https://pacsd.ca/about-us/employment-opportunities/'}]

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "118 – 11th Street East, Prince Albert, Saskatchewan, S6V 1A1", "address_country": "CA", "address_url": "https://pacsd.ca/about-us/contact-us/", "address_method": "pattern", "address_quote": "Us Catholic Education Centre 118 – 11th Street East Prince Albert Saskatchewan S6V 1A1 Canada Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca For privacy r", "phone": "306-953-7500", "phone_url": "https://pacsd.ca/about-us/contact-us/", "emails": "info@pacsd.ca", "emails_url": "https://pacsd.ca/about-us/contact-us/", "domain": "pacsd.ca", "key": "cra:107858359", "name": "BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6", "website": "https://pacsd.ca/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | SaskPower | Q2225615 | official website on the organisation's domain (https://www.saskpower.com/) + name | Saskatchewan Power Corporation [en] | SaskPower | SaskPower | electricity supply company | state-owned enterprise | Canada | 1929-01-01 | Regina; SaskPower Building |
| b | BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6 |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:107858359",
 "ap_contact_team": {
  "emails": [
   "info@pacsd.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@pacsd.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://pacsd.ca/",
    "quote": "mation Catholic Family Services Information Get Updates Prince Albert Catholic School Division Phone: 306-953-7500 Fax: 306-763-1723 Email: info@pacsd.ca Mail: Catholic Education Centre 118 – 11th St. East Prince Albert, Saskatchewan, Canada S6V 1A1 Copyright ©2021-2025 Prince Albert Catho",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "BOARD OF EDUCATION OF THE PRINCE ALBERT ROMAN CATHOLIC SEPARATE SCHOOL DIVISION NO. 6",
    "task_id": "CL-CRA-00627"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.pacsd.ca (13 pages, robots.txt respected), no AI, no search engine"
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

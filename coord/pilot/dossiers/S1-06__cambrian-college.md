# S1-06 — Cambrian College ⇄ KPMG LLP

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Cambrian College Faculty and staff — 1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/) — buyer tax no. 106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name)
SUBMIT TO: POINVOICE@cambriancollege.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: Include PO)
FROM / REMIT TO: KPMG INC. — 333 Bay Street, Suite 4600, Toronto, ON, M5H2S5, Canada | GST/HST 882544158RT0001 (account derived from the BN9) | NEQ 1141883729
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Cambrian College (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): KP
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 89
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Cambrian College (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): KPMG LLP | awarded 2026-06-03 | published by: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C | record: https://media.cambriancollege.ca/uploads/2026/08/26101520/AnnualReport_2025-FINAL-AUG26.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Sudbury, Canada)=private English company limited by guarantee. KPMG Canada provides services to KPMG LLP. | ... countants Sudbury, Canada Ju | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:849a24941f3d3f79
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C; 0 in the contract dataset)

## Buyer
- **buyer**: Cambrian College
- **buyer_website**: https://cambriancollege.ca/
- **buyer_address**: 1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/)
- **buyer_phone**: +1-705-566-8101
- **buyer_contact_evidence_url**: https://cambriancollege.ca/contact-us
- **buyer_legal_name_as_published**: Cambrian College Faculty and staff
- **buyer_bn_as_published**: 106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 106833874RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://cambriancollege.ca/logo-watermark.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/school/cambrian-college
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q5025284; college; public educational institution; charitable organization
- **buyer_founded**: 1967-00-00 (Wikidata Q5025284, official website on the organisation's domain (http://www.cambriancollege.ca) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 83091683 Q1104069; 89975017 Q1104069; 101855621 Q1104069; 104532865 Q1104069; 97725331 Q1104069; 134126673 Q1104069; 191 (Wikidata Q5025284, official website on the organisation's domain (http://www.cambriancollege.ca) + name; 2026-11-08)
- **buyer_employees**: 1005; 1085; 1120; 1264; 931; 1025; 1152; 1247; 1336 (Wikidata Q5025284, official website on the organisation's domain (http://www.cambriancollege.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://cambriancollege.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the lane's AP page (https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf); PO requirement: the lane's AP page (https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: POINVOICE@cambriancollege.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf
- **email_evidence_quote**: Invoices should be emailed to POINVOICE@cambriancollege.ca only.
- **mailbox_provenance**: poinvoice@cambriancollege.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08 | page: https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf | quote: "Invoices should be emailed to POINVOICE@cambriancollege.ca only." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50097
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:628d3a4ae5897@ag.dmarcly.com; ruf=mailto:628d3a4ae5897@fo.dmarcly.com; sp=quarantine;
- **dmarc_record_domain**: cambriancollege.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:_u.cambriancollege.ca._spf.dmarclc.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:628d3a4ae5897@tls.dmarcly.com)
- **bimi**: no BIMI record
- **invoicing_requirements**: After delivery or service completion, email AP. Include PO number, quantities, description, price and invoice number. Units and price should match PO.
- **po_required_as_published**: yes (as published: Include PO)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "yes (as published: Include PO)", "requirements_text": "After delivery or service completion, email AP. Include PO number, quantities, description, price and invoice number. Units and price should match PO."}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Cambrian College Faculty and staff — 1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/) — buyer tax no. 106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name) ⏎ SUBMIT TO: POINVOICE@cambriancollege.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Include PO) ⏎ FROM / REMIT TO: KPMG INC. — 333 Bay Street, Suite 4600, Toronto, ON, M5H2S5, Canada | GST/HST 882544158RT0001 (account derived from the BN9) | NEQ 1141883729 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Cambrian College (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): KP
- **invoice_card_json**: {"bill_to": {"legal_name": "Cambrian College Faculty and staff", "legal_name_is_published": true, "address": "1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/)", "address_is_the_invoice_address": false, "tax_number": "106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name)", "language": "en"}, "submit_to": {"email": "POINVOICE@cambriancollege.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Include PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Include PO))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their"
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Include PO))

## Vendor
- **vendor**: KPMG LLP
- **vendor_legal_name**: KPMG INC.
- **vendor_trading_name**: KPMG LLP
- **vendor_registry_id**: Corporations Canada (corporation number): 2531828
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2531828
- **vendor_registered_address**: 333 Bay Street, Suite 4600, Bay Adelaide Centre, TORONTO, ON, M5H 2S5, CA
- **vendor_neq**: 1141883729 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 7799 — AUTRES SERVICES AUX ENTREPRISES
- **vendor_employees_quebec**: Aucun
- **vendor_establishments_quebec**: KPMG INC.: BUREAU 1500, 600, BOULEVARD DE MAISONNEUVE OUEST, MONTRÉAL (QUÉBEC), H3A0A3
- **vendor_directors_range**: 1 to 25 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 1989-10-24
- **vendor_address**: 333 Bay Street, Suite 4600, Toronto, ON, M5H2S5, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Sudbury, Canada)=private English company limited by guarantee. KPMG Canada provides services to KPMG LLP. | ... countants Sudbury, Canada June 3, 2026
- **vendor_bn9**: 882544158
- **vendor_gst_hst_derived**: 882544158RT0001
- **vendor_website**: https://kpmg.com/
- **vendor_logo_url**: https://kpmg.com/content/experience-fragments/kpmgpublic/xx/en/site/header/master/_jcr_content/root/header_v2/logo.coreimg.svg/1787056531657/logo.svg
- **vendor_linkedin_url**: https://www.linkedin.com/company/kpmg
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Sudbury, C); registry identity: Corporations Canada (corporation number): 2531828 status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-10) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1989-10-24; website: https://kpmg.com/; NEQ: 1141883729 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-01-10)
- **vendor_incorporation_date**: 1989-10-24
- **vendor_years_in_business**: 37.0 (since 1989-10-24, registry date)

## Contract
- **po_required_as_published**: yes (as published: Include PO)
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C)
- **award_date**: 2026-06-03
- **contract_link**: https://media.cambriancollege.ca/uploads/2026/08/26101520/AnnualReport_2025-FINAL-AUG26.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Sudbury, C; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 106833874RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 882544158RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Cambrian College Faculty and staff — 1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/) — buyer tax no. 106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name) ⏎ SUBMIT TO: POINVOICE@cambriancollege.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Include PO) ⏎ FROM / REMIT TO: KPMG INC. — 333 Bay Street, Suite 4600, Toronto, ON, M5H2S5, Canada | GST/HST 882544158RT0001 (account derived from the BN9) | NEQ 1141883729 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Cambrian College (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): KP
- **invoice_card_json**: {"bill_to": {"legal_name": "Cambrian College Faculty and staff", "legal_name_is_published": true, "address": "1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA (schema.org JSON-LD PostalAddress on https://cambriancollege.ca/)", "address_is_the_invoice_address": false, "tax_number": "106833874RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (cambriancollege.ca) + name)", "language": "en"}, "submit_to": {"email": "POINVOICE@cambriancollege.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Include PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Include PO))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their"
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["poinvoice@cambriancollege.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08", "page: https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf", "quote: \"Invoices should be emailed to POINVOICE@cambriancollege.ca only.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50097"], "buyer_facts": ["address and phone: the buyer's own site, https://cambriancollege.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the lane's AP page (https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf)", "PO requirement: the lane's AP page (https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Sudbury, C)", "registry identity: Co

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://cambriancollege.ca/supports-services/procurement-services | 2026-11-08 | ok |  |  |  | 705-524-7315 |  |  |  |  |  |

## Buyer site facts (org_extras, cambriancollege.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Cambrian College Faculty and staff
- **legal_name_url**: https://cambriancollege.ca/
- **legal_name_quote**: also recognize the contributions of Wahnapitae First Nation and the Metis Nation of Ontario. © 2026 Cambrian College Faculty and staff
- **logo_url**: https://cambriancollege.ca/logo-watermark.svg
- **logo_basis**: logo image on the site
- **domain**: cambriancollege.ca
- **key**: lead:849a24941f3d3f79
- **name**: Cambrian College
- **website**: https://cambriancollege.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization/LocalBusiness/CollegeOrUniversity
- **jsonld_name**: Cambrian College of Applied Arts and Technology
- **jsonld_legal_name**: Cambrian College of Applied Arts and Technology
- **jsonld_alternate_name**: Cambrian College
- **jsonld_address**: 1400 Barry Downe Road, Sudbury, ON, P3A 3V8, CA
- **jsonld_phone**: +1-705-566-8101
- **jsonld_email**: info@cambriancollege.ca
- **jsonld_logo**: https://media.cambriancollege.ca/uploads/2026/02/23152959/cambrian-college-vertical.png
- **jsonld_url**: https://cambriancollege.ca/
- **jsonld_founding_date**: 1967
- **jsonld_same_as**: https://www.facebook.com/cambriancollege; https://x.com/cambriancollege; https://www.instagram.com/cambriancollege; https://ca.linkedin.com/school/cambrian-college; https://www.tiktok.com/@cambriancollege; https://www.youtube.com/channel/UCOFOh-0gUaorfMs-1AcSS-Q
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://cambriancollege.ca/","url":"https://cambriancollege.ca/","name":"Cambrian College | College of Applied Arts and Technology","isPartOf":{"@id":"https://cambriancollege.ca/#website"},"datePublished":"2023-10-18T15:29:19+00:00
- **jsonld_page**: https://cambriancollege.ca/
- **legal_name_stated**: Cambrian College
- **legal_name_stated_url**: https://cambriancollege.ca/about-cambrian
- **legal_name_stated_quote**: About Cambrian | Cambrian College Skip to main content Apply now Search Saved Programs Open Menu About Cambrian Welcome to Cambrian C
- **mentions**: {'payment_method': {'text': 'interactive map Social media Facebook X Instagram LinkedIn TikTok YouTube Get ready to', 'url': 'https://cambriancollege.ca/contact-us', 'quote': 'ns Barry Downe campus maps Campus map Floor 1 Floor 2 Floor 3 Floor 4 Find your way around campus - interactive map Social media Facebook X Instagram LinkedIn TikTok YouTube Get ready to take on the world. Apply today Cambrian College 1400 Barry Downe Rd. Sudb'}}
- **linkedin_url**: https://ca.linkedin.com/school/cambrian-college
- **tel_links**: 1-705-566-8101; 1-800-461-7145; 705-566-8101; 7055668101; +18004617145

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1400 Barry Downe Road, Sudbury, ON, P3A 3V8", "address_country": "CA", "address_url": "https://cambriancollege.ca/contact-us", "address_method": "json-ld", "address_quote": "ake on the world. Apply today Cambrian College 1400 Barry Downe Rd. Sudbury, ON P3A 3V8 Send email Copy email 1-705-566-8101 TF 1-800-461-7145 Programs Admissions Supp", "phone": "+1-705-566-8101", "phone_url": "https://cambriancollege.ca/contact-us", "emails": "info@cambriancollege.ca; international@cambriancollege.ca", "emails_url": "https://cambriancollege.ca/contact-us", "domain": "cambriancollege.ca", "key": "lead:849a24941f3d3f79", "name": "Cambrian College", "website": "https://cambriancollege.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, kpmg.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Releases Company Careers About Us Company Careers About Us
- **legal_name_url**: https://kpmg.com/xx/en.html
- **legal_name_quote**: tact Us Submit RFP Contact Contact Us Submit RFP Media Newsroom Press Releases Media Newsroom Press Releases Company Careers About Us Company Careers About Us Legal Privacy Accessibility Help © 2026 Copyright owned by one or more of the KPMG International en
- **logo_url**: https://kpmg.com/content/experience-fragments/kpmgpublic/xx/en/site/header/master/_jcr_content/root/header_v2/logo.coreimg.svg/1787056531657/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: kpmg.com
- **key**: vendor:KPMG LLP
- **name**: KPMG LLP
- **website**: https://kpmg.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Corporation
- **jsonld_name**: KPMG International | Home
- **jsonld_logo**: https://assets.kpmg.com/is/image/kpmg/kpmg-logo-1
- **jsonld_url**: https://kpmg.com/xx/en#home
- **jsonld_quote**: { "@context" : "https://schema.org", "@type" : "SiteNavigationElement", "name" : "KPMG", "url" : "https://kpmg.com/xx/en#home", "mainEntity" : { "@type" : "ItemList", "itemListElement" : [ { "@type" : "ListItem", "name" : "AI and Technology", "url" : "https://kpmg.com/xx/en/our-insights/ai-and-techn
- **jsonld_page**: https://kpmg.com/xx/en.html
- **legal_name_stated**: KPMG International Limited
- **legal_name_stated_url**: https://kpmg.com/xx/en/misc/legal.html
- **legal_name_stated_quote**: terms close Cancel Legal KPMG is a global organization of independent member firms affiliated with KPMG International Limited, a private English company limited by guarantee. KPMG International Limited and its related entitie
- **mentions**: {'payment_method': {'text': 'interaction is displayed on our web pages (e', 'url': 'https://kpmg.com/xx/en/misc/privacy.html', 'quote': 'dgets or buttons may place a cookie on your device to make their service easier to use, ensure your interaction is displayed on our web pages (e.g. the social share count cache is updated) and log information about your activities across the In'}}
- **linkedin_url**: https://www.linkedin.com/company/kpmg

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Cambrian College | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Cambrian%20College | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Cambrian College | Q5025284 | official website on the organisation's domain (http://www.cambriancollege.ca) + name |  | Cambrian College | Collège Cambrian | college; public educational institution; charitable organization |  | Canada | 1967-00-00 |  |
| v | KPMG INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:849a24941f3d3f79",
 "ap_contact_team": {
  "emails": [
   "POINVOICE@cambriancollege.ca",
   "poinvoice@cambriancollege.ca",
   "purchasing@cambriancollege.ca",
   "u003epurchasing@cambriancollege.ca",
   "purchasing@archive.cambriancollege.ca",
   "info@cambriancollege.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "After delivery or service completion, email AP. Include PO number, quantities, description, price and invoice number. Units and price should match PO.",
  "evidence": [
   {
    "email": "POINVOICE@cambriancollege.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "After delivery or service completion, email AP. Include PO number, quantities, description, price and invoice number. Units and price should match PO.",
    "applies_to": "whole_organisation",
    "page_url": "https://media.cambriancollege.ca/uploads/2024/10/03125001/Vendors-Guide.pdf",
    "quote": "Invoices should be emailed to POINVOICE@cambriancollege.ca only.",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "Cambrian College",
    "task_id": "CH-AP-50097"
   },
   {
    "email": "poinvoice@cambriancollege.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/policies/travel-meal-and-hospitality-expenses-procedure",
    "quote": "hospitality expenditures for the fiscal year (April 1 to March 31). Obtain the appropriate approvals. Submit the approved form via email to poinvoice@cambriancollege.ca and the accounting office will retain it for compliance purposes. Incur the expense noting on the Statement of Travelling",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Cambrian College",
    "task_id": "CL-WS-00131"
   },
   {
    "email": "purchasing@cambriancollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/supports-services/procurement-services",
    "quote": "ils Location Floor 4, room 4020 Cost Free Hours of Operation Monday to Friday, 8:30 a.m. to 4:30 p.m. General Contacts Procurement Services purchasing@cambriancollege.ca Send email Copy email 705-524-7315 Overview Procurement Services is the central purchasing and contract management depar",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Cambrian College",
    "task_id": "CL-LD-32985"
   },
   {
    "email": "u003epurchasing@cambriancollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/supports-services/procurement-services",
    "quote": "\\\\\\\"\\u003epurchasing@cambriancollege.ca\\u003c/a\\u003e. As indicated above, Vendors are encouraged to register for an account with Bonfire.\\u003c/p\\u003e\\\\n",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Cambrian College",
    "task_id": "CL-LD-32985"
   },
   {
    "email": "purchasing@archive.cambriancollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/supports-services/procurement-services",
    "quote": "receiving opportunities to provide quotes on individual procurements are encouraged to submit their company information to <a href=\"mailto:purchasing@archive.cambriancollege.ca\">",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Cambrian College",
    "task_id": "CL-LD-32985"
   },
   {
    "email": "purchasing@archive.cambriancollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/supports-services/procurement-services",
    "quote": "receiving opportunities to provide quotes on individual procurements are encouraged to submit their company information to <a href=\"mailto:purchasing@archive.cambriancollege.ca\">",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Cambrian College",
    "task_id": "CL-WS-00131"
   },
   {
    "email": "purchasing@cambriancollege.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cambriancollege.ca/supports-services/procurement-services",
    "quote": "ils Location Floor 4, room 4020 Cost Free Hours of Operation Monday to Friday, 8:30 a.m. to 4:30 p.m. General Contacts Procurement Services purchasing@cambriancollege.ca Send email Copy email 705-524-7315 Overview Procurement Services is the central purchasing and contract management depar",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Cambrian College",
    "task_id
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-04081:2b7edb70-a946-4b41-bf24-41c213e35355 | Municipal District of Taber | Municipal District of Taber - Request for Proposal - Professional Auditing Services - Professional Auditing Services | 265200.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-04081 |
| ca_alberta_apc:AB-2024-07264:c16842d6-fbfa-4aa5-a680-aca81f25b061 | Lethbridge County | Lethbridge County - Request for Proposal - Professional Auditing Services | 394800.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07264 |
| ca_alberta_apc:AB-2024-07530:07426c5e-9d92-4fc6-9903-30978acd7664 | MacEwan University | MacEwan University - Request for Proposal - RFP 24-25-1404 Indirect Tax Advisory Services | 300000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-07530 |
| ca_alberta_apc:AB-2024-08528:ef5ddb92-4211-4bf3-ac80-4902195643f1 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Request for Quotes - Supplier Qualification for Roster for Consultant Services (without Pricing) |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-08528 |
| ca_alberta_apc:AB-2024-09365:9b6bd9d7-08f9-4dd9-be99-607cc0c1c56f | Northern Alberta Institute of Technology (NAIT) | Northern Alberta Institute of Technology (NAIT) - Request for Proposal - Indirect Tax Advisory Services | 65000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-09365 |
| ca_alberta_apc:AB-2024-09660:6db5b57a-1040-4c0a-86ca-0e226de21d42 | Alberta Energy Regulator | Alberta Energy Regulator - Request for Proposal - Audit of the Senior Employees Pension Plan Fund | 260000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-09660 |
| ca_alberta_apc:AB-2025-01856:2e033cb1-9c11-4645-84f9-314843385722 | Bow Valley College | Bow Valley College - Request for Proposal - MARKETING PROJECT MANAGEMENT TOOL | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01856 |
| ca_alberta_apc:AB-2025-01856:a136742f-a79d-4d6e-9245-fcdb6c8453c1 | Bow Valley College | Bow Valley College - Request for Proposal - MARKETING PROJECT MANAGEMENT TOOL |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-01856 |
| ca_alberta_apc:AB-2025-03696:ad042266-e40e-4b02-93ab-4f9a68821724 | Calgary Housing Company | Calgary Housing Company - Negotiated Request for Proposal - Board of Directors (Board) and Executive Leadership Team (ELT) Facilitation |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-03696 |
| ca_alberta_apc:AB-2025-05462:27f0e9cf-ad6e-45d7-9907-19de155122bd | Auditor General | Auditor General - Request for Proposal - Financial Statements Audits of the Health System Entities | 10095500.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05462 |
| ca_alberta_apc:AB-2025-06457:65dec299-3421-4ebd-9296-ecbe0a547264 | Strathcona County | Strathcona County - Request for Proposal - RFP #25.0097 Consulting Services - Internal Controls Program | 386000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06457 |
| ca_alberta_apc:AB-2025-07354:6db9daec-3ba6-4552-a04f-18c5c56d0621 | Alberta Municipalities | Alberta Municipalities - Request for Proposal - Alberta Asset Management Handbook Update |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-07354 |
| ca_alberta_apc:AB-2025-07555:f6c74ca2-cbca-4e06-b526-6d2b651ce4b2 | University of Calgary | University of Calgary - Request for Proposal - Tax Advisory Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-07555 |
| ca_alberta_apc:AB-2026-00049:a646a350-ee10-4f43-99b6-fcd10b566c5f | Alberta Investment Management Corporation | Alberta Investment Management Corporation - Negotiated Request for Proposal - IA Co-Sourcing Support Services   |  |  |  | https://purchasing.alberta.ca/posting/AB-2026-00049 |
| ca_alberta_apc:AB-2026-01669:eba8bf13-e0f2-4773-9fa3-d4d567cb86e3 | City of Red Deer | City of Red Deer - Negotiated Request for Proposal - Emergency Services Operational Review | 114997.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01669 |
| ca_alberta_apc:AB-2026-02982:d43f03e3-906c-44ca-8d39-7c68427d59e6 | City of Calgary | City of Calgary - Request for Proposal - RFP 26-1566-B Treasury Financial Advisory Services (Stage B) | 1812693.75 |  |  | https://purchasing.alberta.ca/posting/AB-2026-02982 |
| ca_alberta_apc:AB-2026-03553:f6a24348-be9e-4e90-93ae-685ea08b9508 | University of Calgary | University of Calgary - Request for Proposal - Consulting Services - Supply Chain Management Process Analysis | 280000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03553 |
| ca_alberta_apc:AB-2026-03908:83c7aab2-df71-441b-bf3a-06a726e22dd5 | City of St. Albert | City of St. Albert - Negotiated Request for Proposal - Financial Audit Services | 586798.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03908 |
| ca_alberta_apc:AB-2026-04180:0dfe6b77-66ac-45b3-b7e8-fbe6caed6708 | City of Lethbridge | City of Lethbridge - Request for Proposal - Business Advisory and Forensic Accounting Consulting Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2026-04180 |
| ca_alberta_apc:AB-2026-04963:628b2921-44c7-4011-87b4-166071e0f3bf | Northern Alberta Institute of Technology (NAIT) | Northern Alberta Institute of Technology (NAIT) - Request for Proposal - Workday Professional Services | 100000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04963 |
| ca_alberta_apc:AB-2026-05293:1ffcf911-eb22-41eb-95cc-2a79c9d183f9 | Infrastructure | Infrastructure - Request for Proposal - RFP for CONSULTANT SERVICES for STRATEGIC REVIEW OF ASSET MANAGEMENT PLAN | 158808.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05293 |
| ca_alberta_apc:AB-2026-05891:4ddcce16-099f-45c7-8417-1751452da492 | City of Lethbridge | City of Lethbridge - Request for Proposal - Consulting Services for the Review and Modelling of Integrated Coordinated Access (ICA) – Lethbridge’s Coordinated A | 163125.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05891 |
| ca_bc_ministry_awards:fe87faecd70ec37b | Ministry of Environment | Performance Review of B.C.’s Carbon Neutral Government Program A | 37500.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:7ceade4f79cc2f80 | Ministry of Agriculture | Audit Work | 106150.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:3bd78b6058e331a5 | Ministry of Transportation and Infrastructure | Capital Project Advisor Services RFP |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:ecab57ecd2451bb2 | Ministry of Environment and Climate Change Strategy | Third-party Assurance w.r.t. a Proposed Green Bond Program | 15000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:e1ced15835b3a423 | Ministry of Forests, Lands, Natural Resource Operations and R.D. | IS18NRTS0005SRFP KNOWLEDGE AND RECORDS MANAGEMENT SERVICES | 98000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:34edc3bca86e6b96 | Ministry of Finance | FICOM Expenditure Costing Model Review | 60000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:a716f9c5e00ce793 | BC Timber Sales - Contracts | Certification Registrar Services | 772700.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b113f1d3-3a78-4e10-a978-9a73a8c44be1/download/ministry-contract-awards-apr-jun-2022.csv |
| ca_bc_ministry_awards:7184fb225e5da8f7 | Ministry of Jobs and Economic Growth | RFP26JEG87 - Venture Capital Tax Credit Program Registrant Audit | 102000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/6b1db703-3de8-4f34-bd94-aa25a1e27ad1/download/ministry-contract-awards-apr-to-jun-2026.csv |
| ca_bc_ministry_awards:78fbdb30dd9e815d | Procurement Services Branch | MCFD Professional and Consulting Services RSA | 1.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/fbeba6e0-4d60-4cf1-a62f-c4849f617194/download/ministry-contract-awards-jan-mar-2025.xlsx |
| ca_bc_ministry_awards:5c60457c45d216da | Ministry of Health | Provincial Food Security Framework | 75000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/0aaa523e-12d2-4c71-867d-156bcb8fb59f/download/ministry-contract-awards-jan-to-mar-2022.csv |
| ca_bc_ministry_awards:e5a69bae48d0c0de | Ministry of Citizens' Services | Cellular In-Building Enhancement Strategy | 99000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/0aaa523e-12d2-4c71-867d-156bcb8fb59f/download/ministry-contract-awards-jan-to-mar-2022.csv |
| ca_bc_ministry_awards:4b22c25f98eb9c05 | Ministry of Environment and Climate Change Strategy | Industrial Project Risk Rating Model | 99900.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:a3ffda86c6e4e3f5 | Ministry of Environment and Climate Change Strategy | Market Readiness of Emissions Reduction Technologies | 145000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/5a23f279-099c-4060-b7ce-207826ccc7ca/download/ministry-contract-awards-jul-sep-2022.csv |
| ca_bc_ministry_awards:60e9fb3ac02c6a93 | Procurement Services Branch | Community Recovery Manager Services |  |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/56029c39-3065-4f60-bfcd-28119a725068/download/ministry-contract-awards-jul-sep-2023.csv |
| ca_bc_ministry_awards:014be2dc94975e4e | Office of the Chief Forester | CLIMATE ADAPTATION POLICY FRAMEWORK ENGAGEMENT AND DEVELOPMENT | 290000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/56029c39-3065-4f60-bfcd-28119a725068/download/ministry-contract-awards-jul-sep-2023.csv |
| ca_bc_ministry_awards:cab57ee25b09201d | Rehabilitation and Maintenance | HIGHWAY MAINTENANCE CONTRACT RENEWAL SUPPORT | 750000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/4f421446-8e0d-4581-bb1d-58e085861855/download/ministry-contract-awards-jul-to-sep-2025.csv |
| ca_bc_ministry_awards:7bda370a35690a1a | Ministry of Citizens' Services | OCIO Service Automation: My Service Centre | 15000000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/4f421446-8e0d-4581-bb1d-58e085861855/download/ministry-contract-awards-jul-to-sep-2025.csv |
| ca_bc_ministry_awards:8524d175108e377a | Ministry of Children and Family Development | Evaluation and Assessment of Trauma Informed Practices | 174825.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/d8dd9bc0-fd7a-434c-b6ae-fd87700dbb05/download/ministry-contract-awards-oct-dec-2024.xlsx |
| ca_bc_ministry_awards:fc58c2466c51eda4 | Liquor Distribution Branch | RFP2024-08-30 Audit Services | 1037016.98 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/d8dd9bc0-fd7a-434c-b6ae-fd87700dbb05/download/ministry-contract-awards-oct-dec-2024.xlsx |
| ca_biddingo:39680528:41129975 | City of Cambridge | Audit Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003134/39680528 |
| ca_biddingo:38665628:41145962 | Workplace Safety and Insurance Board (WSIB) | ServiceNow Software Licenses Subscription, Maintenance and Support |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003099/38665628 |
| ca_biddingo:35847128:41145962 | Town of Collingwood | Collingwood Grain Terminals: Revitalization, Infrastructure Development and Alternative Financing Advisor |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003111/35847128 |
| ca_biddingo:34948528:41145962 | Children's Hospital of Eastern Ontario (CHEO) | Audit Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003840/34948528 |
| ca_biddingo:33617828:41145962 | Workplace Safety and Insurance Board (WSIB) | ServiceNow License Purchase |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003099/33617828 |
| ca_biddingo:32265528:41145962 | City of Waterloo | Financial Audit Services 2019‐2021 |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003305/32265528 |
| ca_biddingo:32185428:41145962 | Town of Lincoln | Annual Audit Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/41064533/32185428 |
| ca_biddingo:32153628:41145962 | Liquor Control Board of Ontario (LCBO) | Information and Security Management processes and controls review | 136000.0 |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/41033725/32153628 |
| ca_biddingo:32126628:41145962 | City of Cambridge | External Audit Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003134/32126628 |
| ca_biddingo:31528428:41145962 | Workplace Safety and Insurance Board (WSIB) | Business Transformation Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003099/31528428 |
| ca_bidsandtenders:3fc5a327-519e-4702-861b-24f5262355e6:1 | United Counties of Leeds and Grenville | External Audit Services |  |  |  | https://leedsgrenville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3fc5a327-519e-4702-861b-24f5262355e6 |
| ca_bidsandtenders:872b729b-a2d7-4f20-8197-2d036ae80d77:1 | City of Lethbridge | Consulting Services for the Review and Modelling of Integrated Coordinated Access (ICA) – Lethbridge’s Coordinated Access System | 163125.0 |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/872b729b-a2d7-4f20-8197-2d036ae80d77 |
| ca_bidsandtenders:ae5a2de9-fe39-491e-bd95-0247a747afe0:1 | Town of Saugeen Shores | Bruce C Prime Consultant |  |  |  | https://saugeenshores.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ae5a2de9-fe39-491e-bd95-0247a747afe0 |
| ca_bidsandtenders:7be19a9d-8ec5-4e8a-b243-c93b8c5ec025:1 | City of Burnaby | External Municipal Operation Review |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7be19a9d-8ec5-4e8a-b243-c93b8c5ec025 |
| ca_bidsandtenders:2b684c5a-9c8c-4ae5-a3f3-10e02bc5d003:1 | Thunder Bay Port Authority | Strategic Development Opportunities Analysis |  |  |  | https://portthunderbay.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2b684c5a-9c8c-4ae5-a3f3-10e02bc5d003 |
| ca_bidsandtenders:0f29d2d5-38b1-4523-bc96-5f451f8501e4:1 | City of Lethbridge | Business Advisory and Forensic Accounting Consulting Services |  |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0f29d2d5-38b1-4523-bc96-5f451f8501e4 |
| ca_bidsandtenders:80d234c8-9808-4c43-aa6b-9449aa2faeec:1 | City of St. Albert | Financial Audit Services |  |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/80d234c8-9808-4c43-aa6b-9449aa2faeec |
| ca_bidsandtenders:6e81741b-a6ee-4aa7-bf6d-33804714cb44:1 | City of Brampton | Develop A Funding Opportunities Assessment For Climate Change Adaptation Plan | 96447.0 |  |  | https://brampton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6e81741b-a6ee-4aa7-bf6d-33804714cb44 |
| ca_bidsandtenders:246bfafb-5f9f-4595-a098-b54b31069da8:1 | City of Burlington | Cyber Security Maturity Assessment | 68020.35 |  |  | https://burlington.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/246bfafb-5f9f-4595-a098-b54b31069da8 |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

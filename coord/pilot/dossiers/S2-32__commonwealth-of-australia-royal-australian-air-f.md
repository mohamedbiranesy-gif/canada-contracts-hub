# S2-32 — Commonwealth of Australia (Royal Australian Air Force) ⇄ CAE Inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08) — CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)
SUBMIT TO: peppol.einvoices@defence.gov.au (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): https://www.ato.gov.au
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: CAE INC. — Montreal (Saint-Laurent), QC | GST/HST 100717065RT0001 (account derived from the BN9) | NEQ 1144199529
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: CAE awarded contract to deliver Australia's Future Air Mission Training System | AMOUNT: 270,000,000.00 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Commonwealth of Australia (Royal Australian Air Force) (government ministry / agency, AU) — public contract / purchase award in the last 12 months (dated record): CAE Inc. | subject: CAE awarded contract to deliver Australia's Future Air Mission Training System | instrument: contract (training system and services) | all identifiers: {"program": "Project AIR5428 Phase 3 / F-AMTS"} | value: 270000000 CAD | awarded 2025-12-11 | published by: Cision newswire.ca (CNW Group) press releases | record: https://www.newswire.ca/news-releases/cae-awarded-contract-to-deliver-australia-s-future-air-mission-training-system-871925883.html | vendor in Canada because: CAE Inc. headquartered in Saint-Laurent (Montreal), QC; release datelined Sydney | status rule: likely active (source marks it as continuing; awarded in the last 3 years, no end date published) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 1 in the last 12 months; latest 2025-12-11)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:b7add5e9f23e7893
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Commonwealth of Australia (Royal Australian Air Force)
- **buyer_website**: https://www.defence.gov.au
- **buyer_address**: CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)
- **buyer_legal_name_as_published**: Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); invoicing requirements: the lane's AP page (https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers); invoice portal: the lane's AP page (https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australian GST is accounted for by the buyer where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: peppol.einvoices@defence.gov.au
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers
- **email_evidence_quote**: 68 706 814 312 DEPARTMENT OF DEFENCE peppol.einvoices@defence.gov.au
- **mailbox_provenance**: peppol.einvoices@defence.gov.au (invoicing/AP) | researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-11-01 | page: https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers | quote: "68 706 814 312 DEPARTMENT OF DEFENCE peppol.einvoices@defence.gov.au" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (actmail.defence.gov.au) | lane file: gemini/gemini_buyer_ap_results_batch28.csv task GE-AP-28079
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (actmail.defence.gov.au)
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc.failures@defence.gov.au; ruf=mailto:dmarc.failures@defence.gov.au
- **dmarc_record_domain**: defence.gov.au
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:203.6.68.1 ip4:203.6.69.66 ip4:203.6.76.1 ip4:203.6.77.66 a:actmail.defence.gov.au a:nactmail.defence.gov.au include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: e-invoices accepted on the Peppol network (participant 0151:68706814312)
- **invoice_portal_url**: https://www.ato.gov.au
- **invoice_portal_kind**: other page named by the buyer (check before use)
- **invoice_portal_note**: (additional channel published by the buyer; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "https://www.ato.gov.au", "portal_kind": "other page named by the buyer (check before use)", "requirements_text": "e-invoices accepted on the Peppol network (participant 0151:68706814312)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08) — CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08) ⏎ SUBMIT TO: peppol.einvoices@defence.gov.au (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): https://www.ato.gov.au ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CAE INC. — Montreal (Saint-Laurent), QC | GST/HST 100717065RT0001 (account derived from the BN9) | NEQ 1144199529 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CAE awarded contract to deliver Australia's Future Air Mission Training System | AMOUNT: 270,000,000.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)", "legal_name_is_published": true, "address": "CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "peppol.einvoices@defence.gov.au", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.ato.gov.au", "portal_kind": "other page named by the buyer (check before use)", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 74
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published | missing: finance mailbox; PO rule published; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: only system ids published (see all_identifiers)

## Vendor
- **vendor**: CAE Inc.
- **vendor_legal_name**: CAE INC.
- **vendor_trading_name**: CAE; CAE ELECTRONICS; CAE ELECTRONICS LTD.; CAE Formation pour l’aviation militaire; CAE Montréal; CAE Numérique; CAE SCREENPLATES INC.; CAE ÉLECTRONIQUE LTÉE; CANADIAN AVIATION ELECTRONICS INTERNATIONAL LTD.; LA SOCIÉTÉ INTERNATIONALE D'ÉLECTRONIQUE AÉRONAUTIQUE CANADIENNE; Presagis Canada; Système (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1144199529
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 8585 COTE DE LIESSE, SAINT-LAURENT, QC, H4T 1G6, CA
- **vendor_neq**: 1144199529 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 3359 — FABRICATION DES PRODUITS DE SIMULATION DE VOL | secondary: CENTRE DE FORMATION AERONAUTIQUE
- **vendor_employees_quebec**: De 2500 à 4999
- **vendor_establishments_quebec**: CAE INC.: 8585 ch. de la Côte-de-Liesse, Montréal (Québec), H4T1G6
- **vendor_directors_range**: 3 to 21 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2014-04-01
- **vendor_address**: Montreal (Saint-Laurent), QC
- **vendor_country_basis**: CAE Inc. headquartered in Saint-Laurent (Montreal), QC; release datelined Sydney
- **vendor_bn9**: 100717065
- **vendor_gst_hst_derived**: 100717065RT0001
- **vendor_website**: https://www.cae.com
- **vendor_phone**: +1-514-341-6780
- **vendor_contact_evidence_url**: https://www.cae.com/contact-us
- **vendor_logo_url**: https://www.cae.com/assets/img/cae-logo-popup-burger.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/cae/
- **vendor_contacts_found_by**:  lane, referee-verified on 
- **vendor_facts_provenance**: name and address: the record's vendor block (Cision newswire.ca (CNW Group) press releases); registry identity: Québec REQ (NEQ): 1144199529 status Québec REQ (NEQ): Immatriculée (1995-03-27); Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 8739056 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1947-03-17; phone / role e-mails / logo: the vendor's own site, https://www.cae.com/contact-us (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the  lane, referee-verified on ; website: https://www.cae.com (site answers); NEQ: 1144199529 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: CAE Inc.: 100% of 1 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (1995-03-27); Corporations Canada (corporation number): Active
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1947-03-17
- **vendor_years_in_business**: 79.6 (since 1947-03-17, registry date)
- **vendor_bn_source**: corporations_canada 8739056 (strong match)

## Contract
- **contract_status**: likely active (source marks it as continuing; awarded in the last 3 years, no end date published)
- **contract_reference**: {"program": "Project AIR5428 Phase 3 / F-AMTS"}
- **contract_title**: CAE awarded contract to deliver Australia's Future Air Mission Training System
- **contract_description**: Future Air Mission Training System (F-AMTS) under Project AIR5428 Phase 3: integrated training system (learning environment, courseware, synthetic ground and airborne training) at RAAF Base East Sale
- **contract_value**: 270000000
- **currency**: CAD
- **award_date**: 2025-12-11
- **contract_link**: https://www.newswire.ca/news-releases/cae-awarded-contract-to-deliver-australia-s-future-air-mission-training-system-871925883.html
- **source**: Cision newswire.ca (CNW Group) press releases
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: Cision newswire.ca (CNW Group) press releases (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australian GST is accounted for by the buyer where applicable
- **vendor_gst_hst_derived**: 100717065RT0001

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08) — CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08) ⏎ SUBMIT TO: peppol.einvoices@defence.gov.au (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): https://www.ato.gov.au ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CAE INC. — Montreal (Saint-Laurent), QC | GST/HST 100717065RT0001 (account derived from the BN9) | NEQ 1144199529 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: CAE awarded contract to deliver Australia's Future Air Mission Training System | AMOUNT: 270,000,000.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Royal Australian Navy Relief Trust Fund (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)", "legal_name_is_published": true, "address": "CP3-1-130 (provincial municipal directory: https://data.gov.au/data/dataset/c77cface-69aa-4dd0-b99f-b065dc33c8e6/resource/6d58f54c-8f24-4b2c-a819-c22f71c39ca1/download/agor-2026-09-30.csv, 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "peppol.einvoices@defence.gov.au", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.ato.gov.au", "portal_kind": "other page named by the buyer (check before use)", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 74
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published | missing: finance mailbox; PO rule published; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["peppol.einvoices@defence.gov.au (invoicing/AP)", "researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-11-01", "page: https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers", "quote: \"68 706 814 312 DEPARTMENT OF DEFENCE peppol.einvoices@defence.gov.au\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (actmail.defence.gov.au)", "lane file: gemini/gemini_buyer_ap_results_batch28.csv task GE-AP-28079"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "invoicing requirements: the lane's AP page (https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers)", "invoice portal: the lane's AP page (https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers)"], "vendor_facts": ["name and address: the record's vendor block (Cision newswire.ca (CNW Group) press releases)", "registry identity: Québec REQ (NEQ): 1144199529 status Québec REQ (NEQ): Immatriculée (1995-03-27)", "Corporations Canada (corporation number)

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://directory.peppol.eu/search/1.0/json?participant=iso6523-actorid-upis%3A%3A0151%3A68706814312 | 2026-11-08 | robots |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, cae.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: CAE Inc
- **legal_name_url**: https://www.cae.com/
- **legal_name_quote**: CAE Social media presence Corporate CAE Inc. Civil Aviation CAE Pilot CAE Aviation Jobs Defense & Security Defence & Security Civil Aviation CA
- **logo_url**: https://www.cae.com/assets/img/cae-logo-popup-burger.png
- **logo_basis**: logo image on the site
- **domain**: cae.com
- **key**: lead:0ec7ae2193b0b12d
- **name**: CAE Lucina Trains Nurse Examiners in Wisconsin
- **website**: https://cae.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Royal Canadian Air Force
- **legal_name_stated_url**: https://www.cae.com/about-cae/history
- **legal_name_stated_quote**: 1947, CAE, then known as Canadian Aviation Electronics Ltd., was founded by Mr. Ken Patrick, an ex-Royal Canadian Air Force (RCAF) officer. His goal was to "...create something Canadian and take advantage of a war-trained t
- **linkedin_url**: https://www.linkedin.com/company/cae/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "8585 Cote-de-Liesse, Saint-Laurent, Québec, H4T 1G6", "address_country": "CA", "address_url": "https://www.cae.com/contact-us", "address_method": "pattern", "address_quote": "e Contacts CAE Corporate Headquarters 8585 Cote-de-Liesse Saint-Laurent, Québec H4T 1G6 Canada Telephone: +1-514-341-6780 Investor Relations For more information as a", "phone": "+1-514-341-6780", "phone_url": "https://www.cae.com/contact-us", "domain": "cae.com", "key": "vd:cae.com", "name": "CAE Inc.", "website": "https://cae.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Department of Defence |  |  |  |  |  |  |  |  |  |  |
| b | CAE Lucina Trains Nurse Examiners in Wisconsin |  |  |  |  |  |  |  |  |  |  |
| v | CAE INC. | Q180922 | official website on the organisation's domain (http://www.cae.com) + name |  | CAE Inc. | CAE | business; public company | Quebec business corporation | Canada | 1947-01-01 | Montreal |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:b7add5e9f23e7893",
 "ap_contact_team": {
  "emails": [
   "invoices@defence.gov.au",
   "peppol.einvoices@defence.gov.au",
   "procurement.asdefcon@defence.gov.au"
  ],
  "invoice_portal": "https://www.ato.gov.au",
  "phone": null,
  "mailing_address": "Defence Accounts Payable, PO Box 800, Salisbury South SA 5106",
  "invoicing_requirements": "Pay within30days after later goods/services receipt or correctly rendered invoice. Invoice must include Defence PO number, relevant DefenceContactOfficer name/full telephone/email, date received/stamped, invoice number, goods/services description and value.",
  "evidence": [
   {
    "email": "invoices@defence.gov.au",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": "Defence Accounts Payable, PO Box 800, Salisbury South SA 5106",
    "requirements": "Pay within30days after later goods/services receipt or correctly rendered invoice. Invoice must include Defence PO number, relevant DefenceContactOfficer name/full telephone/email, date received/stamped, invoice number, goods/services description and value.",
    "applies_to": "parent_central_ap",
    "page_url": "https://www.defence.gov.au/about/governance/accounts-payable",
    "quote": "invoices@defence.gov.au",
    "retrieved_date": "2026-11-09",
    "found_by": "codex",
    "verification": "verified",
    "source_file": "codex_buyer_ap_results_batch04.csv",
    "org": "Department of Defence, Commonwealth of Australia",
    "task_id": "CO-AP-00323",
    "verified_via": "https://web.archive.org/web/20260713154610/https://www.defence.gov.au/about/governance/accounts-payable"
   },
   {
    "email": "peppol.einvoices@defence.gov.au",
    "type": "invoice_submission",
    "invoice_portal": "https://www.ato.gov.au",
    "phone": null,
    "mailing_address": null,
    "requirements": "Australian Department of Defence / Royal Australian Air Force receives eInvoices via Peppol framework (ABN: 68 706 814 312). Supplier eInvoicing contact: peppol.einvoices@defence.gov.au.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers",
    "quote": "68 706 814 312 DEPARTMENT OF DEFENCE peppol.einvoices@defence.gov.au",
    "retrieved_date": "2026-11-01",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch28.csv",
    "org": "Commonwealth of Australia (Royal Australian Air Force)",
    "task_id": "GE-AP-28079",
    "verified_via": "https://web.archive.org/web/20260613021239/https://www.ato.gov.au/businesses-and-organisations/einvoicing/einvoicing-for-government/einvoicing-enabled-government-entities-and-suppliers"
   },
   {
    "email": "procurement.asdefcon@defence.gov.au",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://web.archive.org/web/20251217131737/http://www.defence.gov.au/business-industry/procurement/contracting-templates/asdefcon-suite/shortform-goods",
    "quote": ":\"\\u003Ch2\\u003EContacts\\u003C\\/h2\\u003E\\n\\u003Ch3\\u003EContracting and initiatives\\u003C\\/h3\\u003E\\n\\u003Cp\\u003E\\u003Ca href=\\u0022mailto:procurement.asdefcon@defence.gov.au\\u0022\\u003Eprocurement.asdefcon@\\u200bdefence.gov.au\\u003C\\/a\\u003E\\u003C\\/p\\u003E\\n\\u003Ch3\\u003EStatement of wor",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Commonwealth of Australia (Royal Australian Air Force)",
    "task_id": "CL-WS-00002"
   },
   {
    "email": "procurement.asdefcon@defence.gov.au",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://web.archive.org/web/20251213091940/http://www.defence.gov.au/sites/default/files/2024-04/Complex-services_Part-2_Conditions-of-Contract.pdf",
    "quote": "et/casg/commercial/CommercialPolicyFramework/Pages/ASDEFCON- Templates.aspx If you have any questions relating to the clauses please email: procurement.asdefcon@defence.gov.au For information in relation to CCSF and policy related questions please email:",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Commonwealth of Australia (Royal Australian Air Force)",
    "task_id": "CL-WS-00171"
   },
   {
    "email": "procurement.policy@defence.gov.au",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://web.archive.org/web/20251213091940/http://www.defence.gov.au/sites/default/files/2024-04/Complex-services_Part-2_Conditions-of-Contract.pdf",
    "quote": "For information in relation to CCSF and policy related questions please email: procurement.policy@defence.gov.au For further assistance and guidance in relation to the application of the CCSF please refer to the Child Safety Fram",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Commonwealth of Australia (Royal Australian Air Force)",
    "task_id": "CL-WS-00171"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); t
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| private_press:390d6de918de77ca63a25a3a2975e375650fa4a9 | private_press | ongoing_inferred | CAE awarded contract to deliver Australia's Future Air Mission Training System | 270000000 | CAD |  |  | {"program": "Project AIR5428 Phase 3 / F-AMTS"} | https://www.newswire.ca/news-releases/cae-awarded-contract-to-deliver-australia-s-future-air-mission-training-system-871925883.html |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 43)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| austender:CN4237507 | Department of Defence | Software Licence | 10269.37 |  |  | https://www.tenders.gov.au/Cn/Show/f38b553a-893b-40a1-abd7-8c30e736fae6 |
| canada_federal:dfo-mpo:F7013-120014/003/CAG(4500007128) | Fisheries and Oceans Canada | Aircraft | 29298209.31 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2024-2025-Q2-01965 |
| canada_federal:dnd-mdn:W8475-08SA99/001/NT | National Defence | Weapons (including parts) | 714647908.85 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-02446 |
| canada_federal:dnd-mdn:W8475-235496/001/RWS | National Defence | Aircraft | 79674690.88 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2024-2025-Q3-00032 |
| canada_federal:dnd-mdn:W8485-20MF01 | National Defence | Other equipment | 156312900.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-08437 |
| canada_federal:dnd-mdn:WS4308482870 | National Defence | Teachers and instructors on contract | 10248040.01 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q1-00028 |
| canada_federal:dnd-mdn:CW2369723 | National Defence | Teachers and instructors on contract | 5705718.89 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q1-00055 |
| canada_federal:tc:T8080-210322 | Transport Canada | AIRCRAFT PARTS | 69319.97 |  |  | https://search.open.canada.ca/contracts/record/tc,TC-2023-2024-Q3-00036 |
| canada_federal:tc:T8493-24-0059 | Transport Canada | AIRCRAFT | 39727.72 |  |  | https://search.open.canada.ca/contracts/record/tc,TC-2024-2025-Q4-00338 |
| canada_federal:tc:T8493-25-0070 | Transport Canada | AIRCRAFT | 158910.88 |  |  | https://search.open.canada.ca/contracts/record/tc,TC-2025-2026-Q4-00400 |
| canada_federal:cb:CW2375355 | Department of Public Works and Government Services (PSPC) | TSPS SA (Task Based) - CAE Inc. |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2375355 |
| canada_federal:cb:CW2379544 | Department of National Defence (DND) | Multi-Fleet Training Devices (MFTD) | 156312900.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2379544 |
| canada_federal:cb:CW2388748 | Department of National Defence (DND) | W0125-24WR03 - Learning Services | 10248040.51 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2388748 |
| canada_federal:cb:CW2464888 | Department of National Defence (DND) | W8703-270055 Defence Drone Initiative (DDI) Marketplace SA 019 | 1.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2464888 |
| canada_federal:cb:EN537-05IT01/090/EI | Department of Public Works and Government Services (PSPC) | SBIPS SA - CAE Inc. |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| canada_federal:cb:PW-21-00962347-1029248 | Department of National Defence | One (1) Senior and Eight (8) Intermediate Instructors for Pilots and Flight Engineers | 2908692.32 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-21-00962347-1029248 |
| canada_federal:cb:W8485-22MT01:001:BQ | Department of National Defence | Operation Training Devices - Repair | 19550000.0 |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| private_press:4bf4a54ecb04d154f24d218f763b65d18753b366 | Saab AB | CAE signs agreement with Saab for GlobalEye training platforms |  |  |  | https://www.newswire.ca/news-releases/cae-signs-agreement-with-saab-for-globaleye-training-platforms-807677250.html |
| seao_quebec:1119200:cae | CIUSSS du Centre-ouest-de-l'Île-de-Montréal | Acquisition du système de simulation CAE Vimedix | 176749.14 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=06111e38-b3f0-4f88-874b-c5086e7f8deb |
| seao_quebec:1214048:cae | École de technologie supérieure | Licence CAE | 186480.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ac2626f4-e02b-423d-89a1-719819ea2e22 |
| seao_quebec:1223091:cae | Centre intégré universitaire de santé et de services sociaux de l’Est-de-l’Île-de-Montréal (CIUSSS) | Acquisition d'un simulateur échocardiaque avec contrat de service | 66753.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3a3f1789-4c7e-46b3-92ee-68ea5183ce3a |
| seao_quebec:20065425:cae-inc | Ministère des Transports et de la Mobilité durable (Direction générale de la gestion contractuelle) | 9001-24-PVC1 - Réparation du dispositif d'entretien de vol (DEV)  pour avions-citernes de type CL-415 du Service aérien gouvernemental | 20857.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=de888f89-aa0b-4a9a-8287-2ff6b4e74c98 |
| seao_quebec:20088635:cae-inc | Ministère des Transports et de la Mobilité durable (Direction générale de la gestion contractuelle) | 9001-24-ZZ15 - Service de formation sur simulateur pour avions Challenger CL-650 du Service aérien gouvernemental | 4977218.22 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5f05bc6c-e37d-41dc-8706-1790838c982e |
| seao_quebec:20104517:cae-inc | Ministère des Transports et de la Mobilité durable (Direction générale de la gestion contractuelle) | 9001-25-PV91 - Réparation du dispositif d'entraînement de vol CL-415 du Service aérien gouvernemental | 106730.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=87bbb73e-d3a5-4f19-b882-5a620bd0e91b |
| seao_quebec:20151854:cae-inc | Ministère des Transports et de la Mobilité durable (Direction générale de la gestion contractuelle) | 9001-25-ZZ23 - Formation pour la maintenance des Challenger de la Direction générale du service aérien gouvernemental | 872648.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=224007fa-e4d1-46da-9681-266f002d790f |
| seao_quebec:313767:cae | École de technologie supérieure | Cessna | 377792.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=18fa1f51-2383-4525-9f84-9562456d47fe |
| ted_eu:165727-2020:award1 | Ministry of Defence, C&C, C&C | Provision of Magnetic Anomaly Detection-XR Sensors | 935000.0 |  |  | https://ted.europa.eu/en/notice/-/detail/165727-2020 |
| ted_eu:693978-2026:TEN-0001 | Ministerie van Defensie | Haalbaarheidsonderzoek vluchtsimulator Midlife Update | -1.0 |  |  | https://ted.europa.eu/en/notice/-/detail/693978-2026 |
| ted_eu:703667-2026:TEN-0001 | Ministerie van Defensie | Haalbaarheidsonderzoek vluchtsimulator Midlife Update | 1.0 |  |  | https://ted.europa.eu/en/notice/-/detail/703667-2026 |
| usaspending:CONT_IDV_6973GH23D00009_6920 | Department of Transportation | BOEING B-737 MAX8 AIRCRAFT SYSTEMS FAMILIARIZATION TRAINING MULTIPLE YEAR CONTRACT | 46415.0 |  |  | https://www.usaspending.gov/award/CONT_IDV_6973GH23D00009_6920/ |
| usaspending:sub:CONT_AWD_FA868926CB006_9700_-NONE-_-NONE-:4300109786:LVSPFPM1RXH9 | GENERAL ATOMICS AERONAUTICAL SYSTEMS, INC. | 1.000	TAIWAN CLS SUPPORT - ACTIVATION PERIOD | 493266.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_FA868926CB006_9700_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:W8475-235496/001/RWS | Department of National Defence | CAE INC (W8475-235496/001/RWS~001) | 79674691.0 |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:EN537-05IT01/090/EI | Department of Public Works and Government Services (PSPC) | SBIPS SA - CAE Inc. |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:EN578-170432/060/EI | Public Works and Government Services Canada | CAE INC (EN578-170432/060/EI~002) |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:W7701-176500/006/MTB | Defence Research and Development Canada (DRDC) | Amend 000 - Supply Arrangement C4ISR - CAE Inc. |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:E60ZT-180027/173/ZT | Department of Public Works and Government Services (PSPC) | Proservices SA - CAE Inc. |  |  |  | https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 |
| ca_canadabuys_contract_history:an:E60ZN-13TSPS:155:ZN | Public Works and Government Services Canada | TSPS 2013 Renewal |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| ca_canadabuys_contract_history:an:PW-16-00758006-762330 | Department of National Defence | W8482-168241 SBIPS Options Analysis Report for the Royal Canadian Navy | 83536.38 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00758006-762330 |
| ca_canadabuys_contract_history:an:E60ZH-1700LS:027:ZH | Public Works and Government Services Canada | End-to-End Learning Services (Excludes COTS Training) |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| ca_canadabuys_contract_history:an:E60ZH-2000LS:087:ZH | Public Works and Government Services Canada | End-to-End Learning Services (Excludes COTS Training) |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| ca_canadabuys_contract_history:an:PW-22-00983408 | Public Works and Government Services Canada | Product/Material - Design, Development, Formulation, Modification: Science and Technology Related (R&D) (CW2229968)(W7714-228156 ) | 1121026.9 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-22-00983408 |
| canada_sosa:CW2251302 | Defence R&D Canada - Ottawa | Amend 003 - Supply Arrangement C4ISR - CAE Inc. |  |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2251302 |
| canada_sosa:CW2464888 | Department of National Defence | Contract Workspace W8703-270055 Defence Drone Initiative (DDI) Marketplace | 1.0 |  |  | https://buyandsell.gc.ca/procurement-data/standing-offers-and-supply-arrangements/CW2464888 |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

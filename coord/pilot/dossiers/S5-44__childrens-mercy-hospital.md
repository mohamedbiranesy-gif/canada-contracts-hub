# S5-44 — Childrens Mercy Hospital ⇄ THE RESEARCH INSTITUTE OF THE MCGILL UNIVERSITY HEALTH CENTRE

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Childrens Mercy Hospital — 2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)
SUBMIT TO: invoices@cmh.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PO number of the Buyer in the customer reference)
FROM / REMIT TO: L'INSTITUT DE RECHERCHE DU CENTRE UNIVERSITAIRE DE SANTÉ MCGILL — 2155 RUE GUY BUREAU 500, MONTREAL, QC, H3H 2R9, CAN | GST/HST number not public | NEQ 1142146688
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD (derived from the source's government) | TERMS: 45 days following receipt (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 
DESCRIPTION: Childrens Mercy Hospital (hospital / health authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 107722.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 93
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Childrens Mercy Hospital (hospital / health authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): THE RESEARCH INSTITUTE OF THE MCGILL UNIVERSITY HEALTH CENTRE | all identifiers: {"internal_id": "42370229", "prime_award_internal_id": "270219240", "Sub-Award ID": "42370229", "Prime Award ID": "R01HD111570", "prime_award_generated_internal_id": "ASST_NON_R01HD111570_075"} | value: 107722.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2025-12-22 | published by: subawardee country | record: https://www.usaspending.gov/award/R01HD111570 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:0b69204881b3e4c6
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: Childrens Mercy Hospital
- **buyer_website**: https://cmh.edu
- **buyer_address**: 2401 Gillham Road, Kansas City, MO 64108
- **buyer_phone**: (816) 234-3000
- **buyer_contact_evidence_url**: https://www.cmh.edu/contact
- **buyer_logo_url**: https://www.cmh.edu/siteassets/media-icons-social-media/threads-icon.png
- **buyer_type**: hospital / health authority
- **buyer_sector**: healthcare
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.cmh.edu/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); logo: og:image / logo image of the buyer's site; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Required checks (as printed on https://www.cmh.edu/siteassets/media-documents-for-depts-section/documents-for-about-us/supplier-management/health-screen-and-background-check-requirements.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoices@cmh.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/
- **email_evidence_quote**: 34-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We prefer all invoices be sent electronically to invoices@cmh.edu in PDF format, one PDF file/invoice per email message. Our preferre
- **email_evidence_context**: Application Information Ship To: The Children’s Mercy Hospital 2401 Gillham Road Kansas City, MO 64108 (816) 234-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We prefer all invoices be sent electronically to invoices@cmh.edu in PDF format, one PDF file/invoice per email message. Our preferred method of payment is via credit card through Commerce Bank. Download and fill out our Vendor Enrollment Form . The (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoices@cmh.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/ | quote: "34-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00069
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc_agg@vali.email,mailto:dmarc_agg@dmarc.everest.email;
- **dmarc_record_domain**: cmh.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:52.249.60.155 ip4:199.242.168.195 ip4:148.59.100.16/28 ip4:67.231.153.25 ip4:67.231.145.37 ip4:192.254.115.42 include:spf.protection.outlook.com include:_spf.salesforce.com a:c.spf.service-now.com include:_spf.psm.knowbe4.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: yes (v=BIMI1; l=https://www.childrensmercy.org/siteassets/media/icons/tiny-ps-logo.sv)
- **ap_phone**: (816) 234-3616 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)
- **invoice_mailing_address**: 2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)
- **invoicing_requirements**: invoice format as published: PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)
- **payment_terms_as_published**: 45 days following receipt (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: PO number of the Buyer in the customer reference) (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "45 days following receipt (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: PO number of the Buyer in the customer reference) (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "ap_phone": "(816) 234-3616 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "mailing_address": "2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "requirements_text": "invoice format as published: PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Childrens Mercy Hospital — 2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08) ⏎ SUBMIT TO: invoices@cmh.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PO number of the Buyer in the customer reference) ⏎ FROM / REMIT TO: L'INSTITUT DE RECHERCHE DU CENTRE UNIVERSITAIRE DE SANTÉ MCGILL — 2155 RUE GUY BUREAU 500, MONTREAL, QC, H3H 2R9, CAN | GST/HST number not public | NEQ 1142146688 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD (derived from the source's government) | TERMS: 45 days following receipt (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read  ⏎ DESCRIPTION: Childrens Mercy Hospital (hospital / health authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 107722.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Childrens Mercy Hospital", "legal_name_is_published": false, "address": "2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@cmh.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "format": "PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: PO number of the Buyer in the customer reference) (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 42370229 (internal_id) — source usaspending"}, "terms": {"payment_terms": "45 days following receipt (as print
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: award or notice id: 42370229 (internal_id) — source usaspending

## Vendor
- **vendor**: THE RESEARCH INSTITUTE OF THE MCGILL UNIVERSITY HEALTH CENTRE
- **vendor_legal_name**: L'INSTITUT DE RECHERCHE DU CENTRE UNIVERSITAIRE DE SANTÉ MCGILL
- **vendor_trading_name**: THE RESEARCH INSTITUTE OF THE MCGILL UNIVERSITY HEALTH CENTRE
- **vendor_registry_id**: Québec REQ (NEQ): 1142146688; NEQ 1142146688 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 500-2155 rue Guy, Montréal (Québec), H3H2R9
- **vendor_neq**: 1142146688 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Personne morale sans but lucratif — QUÉBEC : Loi sur les compagnies, Partie 3 (RLRQ, C. C-38)
- **vendor_activity_code**: CAE 8686 — AUTRES LABORATOIRES DU DOMAINE DE LA SANTÉ
- **vendor_employees_quebec**: De 1000 à 2499
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 2155 RUE GUY BUREAU 500, MONTREAL, QC, H3H 2R9, CAN
- **vendor_country_basis**: subawardee country=CAN
- **vendor_website**: https://mcgill.ca/
- **vendor_phone**: 514-398-3000
- **vendor_contact_evidence_url**: https://www.mcgill.ca/newsroom/contacts
- **vendor_logo_url**: https://www.mcgill.ca/about/themes/custom/miles/assets/svgs/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.mcgill.ca/about/ (udents from more than 150 countries make up nearly 30% of McGill's student body ‒ the highest proportion of any Canadian research university. History McGill is )
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); registry identity: Québec REQ (NEQ): 1142146688; NEQ 1142146688 (Registraire des entreprises du Québec (open data)) status Québec REQ (NEQ): Immatriculée (1995-01-26) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 1973-03-13; phone / role e-mails / logo: the vendor's own site, https://www.mcgill.ca/newsroom/contacts (tools/org_contacts.py, org_extras.py); website: https://mcgill.ca/; NEQ: 1142146688 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (1995-01-26)
- **vendor_incorporation_date**: 1973-03-13
- **vendor_years_in_business**: 53.7 (since 1973-03-13, registry date)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: PO number of the Buyer in the customer reference) (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "42370229", "prime_award_internal_id": "270219240", "Sub-Award ID": "42370229", "Prime Award ID": "R01HD111570", "prime_award_generated_internal_id": "ASST_NON_R01HD111570_075"}
- **award_or_notice_id**: 42370229 (internal_id); 42370229 (Sub-Award ID); R01HD111570 (Prime Award ID); 270219240 (prime_award_internal_id); ASST_NON_R01HD111570_075 (prime_award_generated_internal_id)
- **contract_value**: 107722.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2025-12-22
- **contract_link**: https://www.usaspending.gov/award/R01HD111570
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Childrens Mercy Hospital — 2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08) ⏎ SUBMIT TO: invoices@cmh.edu (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal | format: PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: PO number of the Buyer in the customer reference) ⏎ FROM / REMIT TO: L'INSTITUT DE RECHERCHE DU CENTRE UNIVERSITAIRE DE SANTÉ MCGILL — 2155 RUE GUY BUREAU 500, MONTREAL, QC, H3H 2R9, CAN | GST/HST number not public | NEQ 1142146688 ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD (derived from the source's government) | TERMS: 45 days following receipt (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read  ⏎ DESCRIPTION: Childrens Mercy Hospital (hospital / health authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 107722.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Childrens Mercy Hospital", "legal_name_is_published": false, "address": "2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoices@cmh.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "2401 Gillham Road Kansas City, MO 64108 (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "format": "PDF format (as printed on https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: PO number of the Buyer in the customer reference) (as printed on https://www.cmh.edu/about-us/supplier-management/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 42370229 (internal_id) — source usaspending"}, "terms": {"payment_terms": "45 days following receipt (as print
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **facts_provenance_json**: {"mailbox": ["invoices@cmh.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/", "quote: \"34-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00069"], "buyer_facts": ["address and phone: the buyer's own site, https://www.cmh.edu/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "logo: og:image / logo image of the buyer's site", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page r

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/ | 2026-11-08 | ok |  |  | supplier / vendor portal | (816) 234-3616 | 2401 Gillham Road Kansas City, MO 64108 | PDF format |  |  |  |

## Buyer site facts (org_extras, cmh.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: The Children's Mercy Hospital
- **legal_name_url**: https://www.cmh.edu/
- **legal_name_quote**: Newsroom For Suppliers 2401 Gillham Road, Kansas City, MO 64108 View all locations © Copyright 2026 The Children's Mercy Hospital Terms of Use Privacy Policy HIPAA Notice of Privacy Practices No Surprises Act Price Transparency L
- **logo_url**: https://www.cmh.edu/siteassets/media-icons-social-media/threads-icon.png
- **logo_basis**: logo image on the site
- **domain**: cmh.edu
- **key**: lead:0b69204881b3e4c6
- **name**: Childrens Mercy Hospital
- **website**: https://cmh.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Copyright 2026 The Children's Mercy Hospital
- **legal_name_stated_url**: https://www.cmh.edu/about-us/
- **legal_name_stated_quote**: mployees Legal Newsroom For Suppliers 2401 Gillham Road, Kansas City, MO 64108 View all locations © Copyright 2026 The Children's Mercy Hospital Terms of Use Privacy Policy HIPAA Notice of Privacy Practices No Surprises Act Price Transparency L
- **mentions**: {'payment_method': {'text': 'electronic funds transfer', 'url': 'https://www.cmh.edu/about-us/supplier-management/', 'quote': 'nvoice. Vendor will accept payment in the following forms: ePayables, cash, check, credit card, and electronic funds transfer. Buyer is exempt from most sales and use taxes and will not be responsible for the payment of any s'}}
- **linkedin_url**: https://www.linkedin.com/company/childrensmercy/
- **tel_links**: 8162343000; 8665122168; 8004663729; 8167015100; 8162343757; 8162343900; 8163021650; 8162343567; 8167014524; 8167015200; 

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "2401 Gillham Road, Kansas City, MO 64108", "address_country": "US", "address_url": "https://www.cmh.edu/contact", "address_method": "pattern", "address_quote": "ate now About Us Blog Careers Contact Us Employees Legal Newsroom For Suppliers 2401 Gillham Road, Kansas City, MO 64108 View all locations © Copyright 2026 The Children's Mercy", "phone": "(816) 234-3000", "phone_url": "https://www.cmh.edu/contact", "domain": "cmh.edu", "key": "lead:0b69204881b3e4c6", "name": "Childrens Mercy Hospital", "website": "https://cmh.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, mcgill.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: McGill University
- **legal_name_url**: https://www.mcgill.ca/about/
- **legal_name_quote**: About McGill - McGill University Skip to main content Offline Error loading page resources Please try to reload the page to display
- **logo_url**: https://www.mcgill.ca/about/themes/custom/miles/assets/svgs/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: mcgill.ca
- **key**: b:bb129f3294827f21
- **name**: McGill University
- **website**: https://mcgill.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: CollegeOrUniversity
- **jsonld_name**: McGill University
- **jsonld_url**: https://www.mcgill.ca
- **jsonld_same_as**: http://www.facebook.com/McGillUniversity; http://www.linkedin.com/edu/mcgill-university-10890; http://twitter.com/mcgillu; http://www.instagram.com/mcgillu/; http://www.youtube.com/mcgilluniversity
- **jsonld_quote**: {"@context":"http:\/\/schema.org","@type":"WebSite","url":"https:\/\/www.mcgill.ca","potentialAction":{"@type":"SearchAction","target":"https:\/\/www.mcgill.ca\/search\/?query={search_term_string}","query-input":"required name=search_term_string"}}
- **jsonld_page**: https://www.mcgill.ca/
- **legal_name_stated**: McGill University
- **legal_name_stated_url**: https://www.mcgill.ca/about/
- **legal_name_stated_quote**: About McGill - McGill University Skip to main content Offline Error loading page resources Please try to reload the page to display
- **mentions**: {'payment_method': {'text': 'interaction should be indifferent to the direction of time', 'url': 'https://www.mcgill.ca/about/alumni', 'quote': "1980 Nobel Prize in Physics for a 1964 experiment that disproved the long-held theory that particle interaction should be indifferent to the direction of time. David Hubel , BSc'47, MDCM'51, was co-recipient of the 1981 Nobel Prize in Medicine for his ground"}}
- **linkedin_url**: https://www.linkedin.com/school/mcgill-university/
- **tel_links**: 514-398-3000; 514-398-7777; 514-398-4556; 514-398-7770; 514-398-7878; 514-398-6200; 514-398-3970; 514-398-7000; 514-398-

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "514-398-3000", "phone_url": "https://www.mcgill.ca/contact-us/", "address": "845 Sherbrooke Street West, Montréal, Québec H3A 0G4", "address_country": "CA", "address_url": "https://www.mcgill.ca/newsroom/contacts", "address_method": "pattern", "address_quote": "tions James Administration Building 845 Sherbrooke Street West Montréal, Québec H3A 0G4 514-398-6693 Contact info Column 1 McGill news McGill Reporter News releases Of", "domain": "mcgill.ca", "key": "b:bb129f3294827f21", "name": "McGill University", "website": "https://mcgill.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Childrens Mercy Hospital | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Childrens%20Mercy%20Hospital | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | McGill University | Q201492 | official website on the organisation's domain (https://www.mcgill.ca/) + name |  | McGill University | Université McGill | public research university; open-access publisher; university in Quebec |  | Canada | 1821-00-00 | Montreal |
| b | Childrens Mercy Hospital |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:0b69204881b3e4c6",
 "ap_contact_team": {
  "emails": [
   "invoices@cmh.edu",
   "accountspayable@cmh.edu",
   "vendormanagement@cmh.edu",
   "supplierengagement@cmh.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoices@cmh.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/",
    "quote": "34-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We prefer all invoices be sent electronically to invoices@cmh.edu in PDF format, one PDF file/invoice per email message. Our preferre",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Childrens Mercy Hospital",
    "task_id": "CL-DT-00005"
   },
   {
    "email": "invoices@cmh.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.childrensmercy.org/about-us/supplier-management/credit-application-information/",
    "quote": "34-3616 Fax: (816) 855-1791 Bill To: Children’s Mercy Hospitals PO Box 804938 Kansas City, MO 64180-4938 (816) 234-3616 Fax: (816) 855-1791 invoices@cmh.edu We prefer all invoices be sent electronically to invoices@cmh.edu in PDF format, one PDF file/invoice per email message. Our preferre",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Childrens Mercy Hospital",
    "task_id": "CL-WS-00069"
   },
   {
    "email": "accountspayable@cmh.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.childrensmercy.org/siteassets/media-documents-for-depts-section/documents-for-about-us/supplier-management/vendor-enrollment-form.pdf",
    "quote": "For questions contact accountspayable@cmh.edu updated 11/19/2021",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Childrens Mercy Hospital",
    "task_id": "CL-DT-00005"
   },
   {
    "email": "vendormanagement@cmh.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.childrensmercy.org/about-us/supplier-management/",
    "quote": "escribed in our affirmative action plan for protected veterans and individuals with a disability. If you have any questions, please contact vendormanagement@cmh.edu . Supplier Company Registration Credit Application Information Purchase order standard terms and conditions Last updated 08/1",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Childrens Mercy Hospital",
    "task_id": "CL-DT-00005"
   },
   {
    "email": "supplierengagement@cmh.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cmh.edu/about-us/supplier-management/small-local-business-supplier-program/",
    "quote": "origin, or the presence of any sensory, mental, or physical disability in consideration for a contract award. For more information, contact SupplierEngagement@cmh.edu . Supplier Management Menu Supplier Management Supplier Portal Credit Application Information Small Local Business Supplier",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Childrens Mercy Hospital",
    "task_id": "CL-WS-00068"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of childrensmercy.org (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of childrensmercy.org (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of childrensmercy.org (60 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| usaspending:CONT_AWD_75D30121C10167_7523_-NONE-_-NONE- | Department of Health and Human Services | TUBERCULOSIS TRIALS CONSORTIUM SERVICES | 7795637.03 |  |  | https://www.usaspending.gov/award/CONT_AWD_75D30121C10167_7523_-NONE-_-NONE-/ |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

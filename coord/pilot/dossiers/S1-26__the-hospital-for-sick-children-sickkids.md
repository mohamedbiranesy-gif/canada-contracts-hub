# S1-26 — The Hospital for Sick Children (SickKids) ⇄ Ernst & Young LLP

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: The Hospital for Sick Children (SickKids) — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 — buyer tax no. 107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: ap.inquiries@sickkids.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order, all prices specified herein shall)
FROM / REMIT TO: ERNST & YOUNG S.R.L. / S.E.N.C.R.L. — 100 Adelaide St W, Toronto, ON, M5H 1S3, Canada | GST/HST 123425522RT0001 (account derived from the BN9) | NEQ 3342276048
TAX: tax exemptions, employee benefit information, bank account number, name of group life and pension beneficiary Use (as printed on https://www.sickkids.ca/en/abou | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable by Purchaser within 45 days (as printed on https://www.sickkids.ca/en/about/accountability/p
DESCRIPTION: CPN Funded Research Projects - Chronic Pain Network
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: The Hospital for Sick Children (SickKids) (hospital / health authority, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Ernst & Young LLP | subject: CPN Funded Research Projects - Chronic Pain Network | awarded 2026-06-01 | published by: auditor of record (own audited financial statements, auditor's report signed in Toronto, C | record: https://www.sickkids.ca/siteassets/about/about-sickkids/the-hospital-for-sick-children---audited-financials---2025-2026.pdf | vendor in Canada because: auditor of record (own audited financial statements, auditor's report signed in Toronto, Canada)=oving the financial statements. | The financial statements have been audited by Ernst & Young LLP, the external auditor, in | status rule: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Toronto, C)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:1fc1730fcac57997
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Toronto, C; 0 in the contract dataset)

## Buyer
- **buyer**: The Hospital for Sick Children (SickKids)
- **buyer_website**: https://sickkids.ca/
- **buyer_address**: 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8
- **buyer_phone**: 416-813-1500
- **buyer_contact_evidence_url**: https://www.sickkids.ca/en/about/contact
- **buyer_legal_name_as_published**: The Hospital for Sick Children (SickKids)
- **buyer_bn_as_published**: 107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 107492928RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.sickkids.ca/contentassets/232e33f4208c495eb192e035ee7ba6e5/sickkids-logo-header.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: http://www.linkedin.com/company/the-hospital-for-sick-children
- **buyer_type**: hospital / health authority
- **buyer_sector**: healthcare
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.sickkids.ca/en/about/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: tax exemptions, employee benefit information, bank account number, name of group life and pension beneficiary Use (as printed on https://www.sickkids.ca/en/about/freedom-of-information/personal-information-banks/, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap.inquiries@sickkids.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.sickkids.ca/en/about/contact/
- **email_evidence_quote**: ode=min&metadata=false&dt=637399260410000000" width="400" alt="" > </div> <div class="card-body"> <p class="card-title h6"> <a href="mailto:ap.inquiries@sickkids.ca" class="external-link" target="" title="Email Accounts Payable" > Accounts Payable </a> </p> <p class="card-subtitle">Vendor
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap.inquiries@sickkids.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.sickkids.ca/en/about/contact/ | quote: "ode=min&metadata=false&dt=637399260410000000" width="400" alt="" > </div> <div class="card-body"> <p class="card-title h6"> <a href="mailto:ap.inquiries@sickkid" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00378
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:31f64b7a@mxtoolbox.dmarc-report.com; ruf=mailto:31f64b7a@forensics.dmarc-report.com; fo=1; pct=100
- **dmarc_record_domain**: sickkids.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com ip4:142.20.16.4 ip4:20.104.87.214 ip4:192.75.158.250 ip4:192.75.158.251 ip4:192.75.158.252 ip4:20.151.66.242 ip4:20.151.64.254 -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: payable by Purchaser within 45 days (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payable by Purchaser within 45 days (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Hospital for Sick Children (SickKids) — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 — buyer tax no. 107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: ap.inquiries@sickkids.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order, all prices specified herein shall) ⏎ FROM / REMIT TO: ERNST & YOUNG S.R.L. / S.E.N.C.R.L. — 100 Adelaide St W, Toronto, ON, M5H 1S3, Canada | GST/HST 123425522RT0001 (account derived from the BN9) | NEQ 3342276048 ⏎ TAX: tax exemptions, employee benefit information, bank account number, name of group life and pension beneficiary Use (as printed on https://www.sickkids.ca/en/abou | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable by Purchaser within 45 days (as printed on https://www.sickkids.ca/en/about/accountability/p ⏎ DESCRIPTION: CPN Funded Research Projects - Chronic Pain Network
- **invoice_card_json**: {"bill_to": {"legal_name": "The Hospital for Sick Children (SickKids)", "legal_name_is_published": true, "address": "555 University Avenue, Toronto, Ontario, Canada, M5G 1X8", "address_is_the_invoice_address": false, "tax_number": "107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "ap.inquiries@sickkids.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-co)"}, "terms": {
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-co)

## Vendor
- **vendor**: Ernst & Young LLP
- **vendor_legal_name**: ERNST & YOUNG S.R.L. / S.E.N.C.R.L.
- **vendor_trading_name**: Ernst & Young LLP
- **vendor_registry_id**: Québec REQ (NEQ): 3342276048
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 100 Adelaide Street West, Suite 3900, TORONTO, ON, M5H 0B3, CA
- **vendor_neq**: 3342276048 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 7731 — EXPERTS-COMPTABLES | secondary: SERVICES FISCAUX
- **vendor_employees_quebec**: De 750 à 999
- **vendor_establishments_quebec**: ERNST & YOUNG S.R.L. / S.E.N.C.R.L.: 2300-900 boul. De Maisonneuve O., Montréal (Québec), H3A0A8; ERNST & YOUNG S.R.L. / S.E.N.C.R.L.: 410-2875 BOUL. Laurier, Delta III, Québec (Québec), G1C0C7
- **vendor_directors_range**: 3 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 1999-03-01
- **vendor_address**: 100 Adelaide St W, Toronto, ON, M5H 1S3, Canada
- **vendor_country_basis**: auditor of record (own audited financial statements, auditor's report signed in Toronto, Canada)=oving the financial statements. | The financial statements have been audited by Ernst & Young LLP, the external auditor, in accordance wi ... udit. | Toronto, Canada June 1, 2026 | The Hospital for
- **vendor_bn9**: 123425522
- **vendor_gst_hst_derived**: 123425522RT0001
- **vendor_website**: https://www.ey.com/en_ca
- **vendor_emails**: contact@ey.com
- **vendor_contact_evidence_url**: https://www.ey.com/en_ca
- **vendor_logo_url**: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/ai/images/ey-ai-the-reimagination-engine-logo-yellow-3840x2560px-v1.jpg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.ey.com/en_ca (s Open LinkedIn profile Open Youtube profile EY refers to the global organization, and may refer to one or more, of the member firms of Ernst &amp; Young Global)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (own audited financial statements, auditor's report signed in Toronto, C); registry identity: Québec REQ (NEQ): 3342276048 status Québec REQ (NEQ): Immatriculée (2000-01-11); Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1991-11-01; phone / role e-mails / logo: the vendor's own site, https://www.ey.com/en_ca (tools/org_contacts.py, org_extras.py); website: https://www.ey.com/en_ca; NEQ: 3342276048 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2000-01-11); Corporations Canada (corporation number): Active
- **vendor_incorporation_date**: 1991-11-01
- **vendor_years_in_business**: 35.0 (since 1991-11-01, registry date)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (own audited financial statements, auditor's report signed in Toronto, C)
- **contract_title**: CPN Funded Research Projects - Chronic Pain Network
- **contract_description**: CPN Funded Research Projects - Chronic Pain Network (the record's title; the source publishes no separate description)
- **award_date**: 2026-06-01
- **contract_link**: https://www.sickkids.ca/siteassets/about/about-sickkids/the-hospital-for-sick-children---audited-financials---2025-2026.pdf
- **source**: auditor of record (own audited financial statements, auditor's report signed in Toronto, C
- **contracts_with_canadian_suppliers**: 6
- **records_with_this_vendor**: 1 (relationship record: auditor of record (own audited financial statements, auditor's report signed in Toronto, C; 0 in the contract dataset)
- **records_in_contract_dataset**: 6 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 107492928RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 123425522RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: The Hospital for Sick Children (SickKids) — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 — buyer tax no. 107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: ap.inquiries@sickkids.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order, all prices specified herein shall) ⏎ FROM / REMIT TO: ERNST & YOUNG S.R.L. / S.E.N.C.R.L. — 100 Adelaide St W, Toronto, ON, M5H 1S3, Canada | GST/HST 123425522RT0001 (account derived from the BN9) | NEQ 3342276048 ⏎ TAX: tax exemptions, employee benefit information, bank account number, name of group life and pension beneficiary Use (as printed on https://www.sickkids.ca/en/abou | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payable by Purchaser within 45 days (as printed on https://www.sickkids.ca/en/about/accountability/p ⏎ DESCRIPTION: CPN Funded Research Projects - Chronic Pain Network
- **invoice_card_json**: {"bill_to": {"legal_name": "The Hospital for Sick Children (SickKids)", "legal_name_is_published": true, "address": "555 University Avenue, Toronto, Ontario, Canada, M5G 1X8", "address_is_the_invoice_address": false, "tax_number": "107492928 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-04-01; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "ap.inquiries@sickkids.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-conditions/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order, all prices specified herein shall) (as printed on https://www.sickkids.ca/en/about/accountability/purchase-orders/purchase-orders-terms-co)"}, "terms": {
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["ap.inquiries@sickkids.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.sickkids.ca/en/about/contact/", "quote: \"ode=min&metadata=false&dt=637399260410000000\" width=\"400\" alt=\"\" > </div> <div class=\"card-body\"> <p class=\"card-title h6\"> <a href=\"mailto:ap.inquiries@sickkid\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00378"], "buyer_facts": ["address and phone: the buyer's own site, https://www.sickkids.ca/en/about/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (own 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.sickkids.ca/en/about/contact/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, sickkids.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: The Hospital for Sick Children (SickKids)
- **legal_name_url**: https://www.sickkids.ca/
- **legal_name_quote**: dat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River. Copyright © 2026 The Hospital for Sick Children (SickKids). All rights reserved. Accessibility | Privacy | Terms of Use Back to Top
- **logo_url**: https://www.sickkids.ca/contentassets/232e33f4208c495eb192e035ee7ba6e5/sickkids-logo-header.png
- **logo_basis**: logo image in the site header
- **domain**: sickkids.ca
- **key**: lead:1fc1730fcac57997
- **name**: The Hospital for Sick Children (SickKids)
- **website**: https://sickkids.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: 2026 The Hospital
- **legal_name_stated_url**: https://www.sickkids.ca/en/patients-visitors/privacy/
- **legal_name_stated_quote**: n-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River. Copyright © 2026 The Hospital for Sick Children (SickKids). All rights reserved. Accessibility | Privacy | Terms of Use Back to T
- **mentions**: {'payment_method': {'text': 'interactive science experiences and programs', 'url': 'https://www.sickkids.ca/', 'quote': 'aregivers preparing to go home. Kids Science This outreach program educates and inspires youth with interactive science experiences and programs. School at SickKids Board-certified teachers provide one-on-one teaching at the patient’s bedside.'}}
- **linkedin_url**: http://www.linkedin.com/company/the-hospital-for-sick-children
- **tel_links**: 416-813-7474; 416-326-3333; 1-800-387-0073

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "555 University Avenue, Toronto, Ontario, Canada, M5G 1X8", "address_country": "CA", "address_url": "https://www.sickkids.ca/en/about/contact", "address_method": "pattern", "address_quote": "ss The Hospital for Sick Children 555 University Avenue Toronto, Ontario Canada M5G 1X8 Main entrance and Emergency 170 Elizabeth Street Learn more about Coming to the", "phone": "416-813-1500", "phone_url": "https://www.sickkids.ca/en/about/contact", "emails": "ap.inquiries@sickkids.ca", "emails_url": "https://www.sickkids.ca/en/about/contact", "domain": "sickkids.ca", "key": "lead:1fc1730fcac57997", "name": "sickkids.ca", "website": "https://sickkids.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, ey.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/ai/images/ey-ai-the-reimagination-engine-logo-yellow-3840x2560px-v1.jpg
- **logo_basis**: logo image on the site
- **domain**: ey.com
- **key**: lead:4530a6b7123c6b6b
- **name**: ey.com
- **website**: https://ey.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Global Executive
- **legal_name_stated_url**: https://www.ey.com/en_ca/about-us
- **legal_name_stated_quote**: successful CFE writers Committed to diversity and inclusiveness To demonstrate our commitment, the Global Executive (GE) has signed a statement, which you can read below. Read the statement Our human rights commitme
- **mentions**: {'payment_method': {'text': 'interacted with AI in customer experiences, including chatbots, recommendations and per', 'url': 'https://www.ey.com/en_ca/newsroom/2026/05/canadians-say-they-are-cautious-about-ai-but-many-are-already-letting-it-decide', 'quote': 's route optimization, travel planning or managing home energy consumption. Sixty‑seven percent have interacted with AI in customer experiences, including chatbots, recommendations and personalized offers.</p>\\r\\n<p>Technology and entertainment is another major'}}
- **linkedin_url**: https://www.linkedin.com/company/1073

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "emails": "contact@ey.com", "emails_url": "https://www.ey.com/en_ca", "domain": "ey.com", "key": "lead:4530a6b7123c6b6b", "name": "ey.com", "website": "https://ey.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | The Hospital for Sick Children (SickKids) | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=The%20Hospital%20for%20Sick%20Children%20%28SickKids%29 | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | The Hospital for Sick Children (SickKids) |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:1fc1730fcac57997",
 "ap_contact_team": {
  "emails": [
   "ap.inquiries@sickkids.ca",
   "research.payments@sickkids.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "ap.inquiries@sickkids.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.sickkids.ca/en/about/contact/",
    "quote": "ode=min&metadata=false&dt=637399260410000000\" width=\"400\" alt=\"\" > </div> <div class=\"card-body\"> <p class=\"card-title h6\"> <a href=\"mailto:ap.inquiries@sickkids.ca\" class=\"external-link\" target=\"\" title=\"Email Accounts Payable\" > Accounts Payable </a> </p> <p class=\"card-subtitle\">Vendor",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "sickkids.ca",
    "task_id": "CL-LD-03725"
   },
   {
    "email": "ap.inquiries@sickkids.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.sickkids.ca/en/about/contact/",
    "quote": "ode=min&metadata=false&dt=637399260410000000\" width=\"400\" alt=\"\" > </div> <div class=\"card-body\"> <p class=\"card-title h6\"> <a href=\"mailto:ap.inquiries@sickkids.ca\" class=\"external-link\" target=\"\" title=\"Email Accounts Payable\" > Accounts Payable </a> </p> <p class=\"card-subtitle\">Vendor",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "The Hospital for Sick Children (SickKids)",
    "task_id": "CL-WS-00378"
   },
   {
    "email": "research.payments@sickkids.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://payments.research.sickkids.ca/",
    "quote": "wed and agreed to the Privacy Policy/Terms & Conditions. Proceed to payment Contact Us Questions? We are here to help! Please contact us at research.payments@sickkids.ca This web application was created and is maintained and hosted by Research IT at the SickKids Research Institute.",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "The Hospital for Sick Children (SickKids)",
    "task_id": "CL-WS-00378"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of sickkids.ca (25 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 183)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2020-06238:40f63d35-de53-e35f-0a5c-39c2ed480000 | Service Alberta and Red Tape Reduction | Service Alberta and Red Tape Reduction - Negotiated Request for Proposal - Robotic Process Automation (RPA) Strategy Development and Pilot Projects | 3278750.0 |  |  | https://purchasing.alberta.ca/posting/AB-2020-06238 |
| ca_alberta_apc:AB-2023-05989:b2af6688-b26b-4514-82ee-0e26e4320282 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Negotiated Request for Proposal - Master Data Management (MDM) Platform | 4933600.0 |  |  | https://purchasing.alberta.ca/posting/AB-2023-05989 |
| ca_alberta_apc:AB-2024-03047:224f638a-14c0-497b-9bdb-b05d8298a7e3 | Service Alberta and Red Tape Reduction | Service Alberta and Red Tape Reduction - Request for Proposal - Organizational Change Management and Project Management Services | 6400000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03047 |
| ca_alberta_apc:AB-2024-03047:e21c998d-94f8-44f3-be2d-662e2d6e010b | Service Alberta and Red Tape Reduction | Service Alberta and Red Tape Reduction - Request for Proposal - Organizational Change Management and Project Management Services | 20300000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03047 |
| ca_alberta_apc:AB-2024-03216:0dfddf1e-27d1-4b72-a6c9-7d9a7e2ba6b7 | Strathcona County | Strathcona County - Negotiated Request for Proposal - RFP#24.0017 - External Audit Services | 1009734.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03216 |
| ca_alberta_apc:AB-2024-03802:f1dc8d1c-2fb9-4cb4-979a-52cd20144618 | Auditor General | Auditor General - Request for Proposal - Norquest College FS Audit RFP | 573300.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03802 |
| ca_alberta_apc:AB-2024-08067:6a58e1e2-cb32-42ce-a867-88904ae1c386 | Northern Alberta Institute of Technology (NAIT) | Northern Alberta Institute of Technology (NAIT) - Request for Proposal - REQUEST FOR PROPOSAL  Advanced Skills Centre  Advisory Services | 1044272.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-08067 |
| ca_alberta_apc:AB-2024-10023:df8d4ced-ca33-4f8d-9c8b-37aa9508dfb9 | Alberta Energy Regulator | Alberta Energy Regulator - Request for Proposal - Cloud Service Providers |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-10023 |
| ca_alberta_apc:AB-2025-01647:083997ed-dc21-41f6-8a97-2869a1e3c760 | City of Lethbridge | City of Lethbridge - Request for Quotes - Economic and Market Studies Consultant Roster |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-01647 |
| ca_alberta_apc:AB-2025-03477:b8a0dbe6-44c5-47b9-9a52-8acc3f2e78a5 | City of Calgary | City of Calgary - Request for Proposal - RFP 25-1557 Supply, Configuration, Implementation, Maintenance and Support of a Human Resource Service Delivery Softwar | 2927538.89 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03477 |
| ca_alberta_apc:AB-2025-03500:8b2cbc74-e198-4d9a-94cc-a7a9770b82f4 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Request for Proposal - Automation Agency of Record |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-03500 |
| ca_alberta_apc:AB-2025-03560:c9ddda59-0d2f-4034-9307-940af05a7e51 | Treasury Board and Finance | Treasury Board and Finance - Request for Proposal - Implementation of Care-First Auto Insurance Program | 5755000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03560 |
| ca_alberta_apc:AB-2025-06970:364d8cf5-5b17-4a5a-9670-5168f02f7d73 | Primary and Preventative Health Services | Primary and Preventative Health Services - Request for Proposal - Health System Category Resourcing |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-06970 |
| ca_alberta_apc:AB-2025-07707:7ea33684-9b56-4121-9c81-bd9e090efe4b | Alberta Electric System Operator | Alberta Electric System Operator - Request for Proposal - External Audit Services | 520000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-07707 |
| ca_alberta_apc:AB-2026-00631:936a7007-28b4-4899-a45b-05b2ef1966ec | City of Calgary | City of Calgary - Request for Proposal - 26-2001 Financial Consulting and Advisory Services | 500000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00631 |
| ca_alberta_apc:AB-2026-03850:7e509d36-67f9-4326-bf41-b7fd0a50928c | City of Calgary | City of Calgary - Request for Proposal - RFP 26-1556 Major Sports and Event Facilities Feasibility and Strategic Advisory Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2026-03850 |
| ca_alberta_apc:AB-2026-05703:bc2dc8d4-4697-49c4-83f9-2cc32d8adfe5 | Affordability and Utilities | Affordability and Utilities - Request for Proposal - Ministry of Affordability and Utilities - RFP - Nuclear Energy Strategy Consulting Services | 250000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-05703 |
| ca_alberta_sole_source:528d2596ce9ac049 | Treasury Board and Finance | Care First Automobile Insurance Reform Categories 2 & 3 | 8200000.0 |  |  | https://www.alberta.ca/sole-source-contracts-disclosure-table |
| ca_bc_ministry_awards:3cd1dcf7c049fd05 | Ministry of Environment and Climate Change Strategy | Aluminum Sector Benchmark study | 98500.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:78ca358ac6c540b3 | Ministry of Energy, Mines, and Low Carbon Innovation | LNG Financial Modelling | 200000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b84ec72e-30ad-4f85-be66-a26dac65a137/download/ministry-contract-awards-jan-to-mar-2021.csv |
| ca_bc_ministry_awards:50c96cc15d4f98d2 | Ministry of Health | Statistical Sampling | 450000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b84ec72e-30ad-4f85-be66-a26dac65a137/download/ministry-contract-awards-jan-to-mar-2021.csv |
| ca_biddingo:41124428:41032943 | Atlantic Lottery Corporation | AML Program Assessment Services / |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003564/41124428 |
| ca_biddingo:40384828:41167458 | Liquor Control Board of Ontario (LCBO) | Consulting Services for the Evaluation of Proposals for LCBO’s  Ocean Services for Freight Transport and Consolidation |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/41033725/40384828 |
| ca_biddingo:38820028:41032943 | St. Joseph's Healthcare Hamilton | Provision of Clinical and Financial Benchmarking Services |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003972/38820028 |
| ca_biddingo:38701228:41032943 | Ontario Tech University | Transaction Advisor for Purpose-Built Student Housing |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/41101702/38701228 |
| ca_biddingo:38579628:41032943 | Atlantic Lottery Corporation | ESG Consulting Services / Services de conseil ESG | 240000.0 |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003564/38579628 |
| ca_bidsandtenders:cf9f6c5e-71ab-4d51-9a12-0cfa7347bb6b:1 | City of Guelph | RFP Evaluating Our Role in Building Affordable Housing |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cf9f6c5e-71ab-4d51-9a12-0cfa7347bb6b |
| ca_bidsandtenders:0e01725c-a52b-4a61-82ef-16a4791dfa9c:35 | Halifax Regional Municipality | Prequalified Consulting & Professional Services Supplier List |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0e01725c-a52b-4a61-82ef-16a4791dfa9c |
| ca_bidsandtenders:6ec5cb08-6045-49f2-93db-4de7b92a8926:1 | Halifax Regional Municipality | Municipal Service Review |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6ec5cb08-6045-49f2-93db-4de7b92a8926 |
| ca_bidsandtenders:a2355324-7705-46ff-94d6-5585b9860081:1 | City Of Peterborough | Consulting Services Effectiveness & Efficiency Review |  |  |  | https://cityofpeterborough.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a2355324-7705-46ff-94d6-5585b9860081 |
| ca_bidsandtenders:8c1035c1-e414-4bb9-80cc-c2c3541e76aa:1 | City of Hamilton | Professional Services Required to Complete Implementation of UKG Pro Workforce Management (Formerly Kronos Workforce Central) |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8c1035c1-e414-4bb9-80cc-c2c3541e76aa |
| ca_bidsandtenders:e1996fea-8a58-4c41-9d83-8d691badd710:1 | City of St. Catharines | RFP - Supply and Implementation of a Human Capital Management System |  |  |  | https://stcatharines.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e1996fea-8a58-4c41-9d83-8d691badd710 |
| ca_bidsandtenders:92021c6f-1686-4918-b0e4-264db8de6858:3 | Halifax Regional Municipality | RFSQ Information Technology Consultants |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/92021c6f-1686-4918-b0e4-264db8de6858 |
| ca_bidsandtenders:72bd06cd-9f4a-4cac-9362-ba7e5a2bf579:2 | City of Hamilton | Professional Services Required to Complete Implementation of UKG Pro Workforce Management (Formerly Kronos Workforce Central) |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/72bd06cd-9f4a-4cac-9362-ba7e5a2bf579 |
| ca_bidsandtenders:bc74edf4-4e7b-4fbd-9f61-aeb5616727f8:2 | City of Burnaby | Pre-Qualification for IT Consulting Services for ServiceNow & Microsoft 365 |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bc74edf4-4e7b-4fbd-9f61-aeb5616727f8 |
| ca_bidsandtenders:1fbc8f68-d712-439e-9716-186cbd17acf5:2 | City of Lethbridge | Economic and Market Studies Consultant Roster |  |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1fbc8f68-d712-439e-9716-186cbd17acf5 |
| ca_bidsandtenders:ee0dcc97-c418-4c73-97f4-4520aeac758e:1 | City of Hamilton | Proposal for Consulting Services for CityHousing Hamilton Budget Modernization | 350000.0 |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ee0dcc97-c418-4c73-97f4-4520aeac758e |
| ca_bidsandtenders:4593711b-a81b-4b9d-81f0-4f646590e40c:1 | Metro Vancouver | District Energy Business Case |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4593711b-a81b-4b9d-81f0-4f646590e40c |
| ca_bidsandtenders:a463ccf3-13ca-47c4-ab64-23e30d4e1873:1 | County of Simcoe | Simcoe County Hospital Alliance (SCHA) Long-Term Capital Planning Review |  |  |  | https://simcoecounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a463ccf3-13ca-47c4-ab64-23e30d4e1873 |
| ca_bidsandtenders:1fee2c61-513a-411c-83ee-f0eb0d5d88c7:1 | Waterloo Regional Police Service | HXM Application Management Services (AMS) |  |  |  | https://wrps.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1fee2c61-513a-411c-83ee-f0eb0d5d88c7 |
| ca_bidsandtenders:0325ba25-ebf7-4d2d-a493-6181ca97a90b:3 | Municipal Property Assessment Corporation | Artificial Intelligence (AI) Training & Services |  |  |  | https://mpac.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0325ba25-ebf7-4d2d-a493-6181ca97a90b |
| ca_bidsandtenders:6a3b39ec-cbcd-4d8b-85af-157a709b91e7:4 | City of Brampton | Prequalification for IT Resources to Support Microsoft Dynamics 365 And Mobile App for a five (5) Year Period |  |  |  | https://brampton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6a3b39ec-cbcd-4d8b-85af-157a709b91e7 |
| ca_bidsandtenders:c3006080-e948-48f7-a633-0b49974d1a39:1 | City of Vaughan | Vendor of Record for Citizen Relationship Management Consulting Services |  |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c3006080-e948-48f7-a633-0b49974d1a39 |
| ca_bidsandtenders:d355f1ad-eda9-40a6-9dfb-7851f44370f2:17 | Metro Vancouver | Infrastructure Project Advisory Consulting Services |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d355f1ad-eda9-40a6-9dfb-7851f44370f2 |
| ca_bidsandtenders:64346d1f-705c-4fdc-b02a-be51ff538832:5 | City of Hamilton | Proposal for Develop, Integrate and Support Microsoft Power Platform Applications Services for Microsoft Power Platform |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/64346d1f-705c-4fdc-b02a-be51ff538832 |
| ca_bidsandtenders:935dc30c-3e4a-468e-98eb-68ed92cc0685:3 | Region of Durham | Prequalification for consulting services - resources, organizational structure, and culture projects in the Region of Durham |  |  |  | https://durham.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/935dc30c-3e4a-468e-98eb-68ed92cc0685 |
| ca_bidsandtenders:6324db8d-fe47-4274-b594-43e22acdffe9:1 | Region of Halton | Consulting Services for Organizational Review for Water & Wastewater System Services Linear and Stations Operations | 350000.0 |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6324db8d-fe47-4274-b594-43e22acdffe9 |
| ca_bidsandtenders:dea1a9ea-ae9b-4ed0-aec0-4c2d58e24432:4 | Newfoundland Labrador Hydro | Master Standing Offer - Regulatory, Accounting, and Treasury Support Services |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dea1a9ea-ae9b-4ed0-aec0-4c2d58e24432 |
| ca_bidsandtenders:45bdbb17-7f21-40a2-8fe2-8c23084bce4c:1 | Region of Halton | Consulting Services to Review/Assess the Region’s Segregation of Duties in the Finance Department |  |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/45bdbb17-7f21-40a2-8fe2-8c23084bce4c |
| ca_bidsandtenders:9fabcfb3-6206-43d7-a755-73f9323651ab:14 | Government of Yukon | Identity Management Solutions and Partners |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9fabcfb3-6206-43d7-a755-73f9323651ab |
| ca_bidsandtenders:de30cabb-ed7c-4ad0-a45b-630992ef2cb6:12 | City of Burnaby | Pre-qualification of IT Consulting Services |  |  |  | https://burnaby.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/de30cabb-ed7c-4ad0-a45b-630992ef2cb6 |
| ca_bidsandtenders:858b2088-328c-468e-b089-f77b97a66645:1 | City of Hamilton | Proposal for Professional services to complete Phase I (Scoping, Design & Business Process Analysis) for the implementation of a corporate-wide Kronos time and  | 291180.0 |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/858b2088-328c-468e-b089-f77b97a66645 |
| ca_bidsandtenders:b0687d48-f37c-4bec-983b-f7de81cba082:1 | Region of Peel | Water & Wastewater Strategic Utility Resource Assessment |  |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b0687d48-f37c-4bec-983b-f7de81cba082 |
| ca_bidsandtenders:3c8177bc-ef78-4ad8-a219-8897a9814972:1 | Metro Vancouver | Iona Island Wastewater Treatment Plant Projects Financial Advisory Services |  |  |  | https://metrovancouver.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3c8177bc-ef78-4ad8-a219-8897a9814972 |
| ca_bidsandtenders:7326ffe2-a551-409a-9922-155a616113ee:1 | Region of Peel | CONSULTING SERVICES FOR WATER BILLING RESIDENT PORTAL INTEGRATION |  |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7326ffe2-a551-409a-9922-155a616113ee |
| ca_bidsandtenders:b200b74e-ca77-49a8-8396-3f263baabc9c:1 | Region of Halton | ERP Consulting Services to Review the Region's SAP Environment and Set a Future Roadmap and Strategy |  |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b200b74e-ca77-49a8-8396-3f263baabc9c |
| ca_bidsandtenders:fcc5134a-5642-4215-8a31-1c815b6a90f9:1 | Region of Peel | CONSULTING SERVICES FOR REVIEW OF TRANSFORMATION OF FINANCIAL SERVICE DELIVERY | 249035.0 |  |  | https://peelregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fcc5134a-5642-4215-8a31-1c815b6a90f9 |
| ca_bidsandtenders:326d21f7-4629-4ad5-8fa0-2caa734a0e5e:1 | Region of Halton | CONSULTING SERVICES FOR THE STUDY OF FINANCIAL RISKS FOR THE REGIONAL MUNICIPALITY OF HALTON RELATED TO CHANGES IN ECONOMIC AND EMPLOYMENT GROWTH | 175850.0 |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/326d21f7-4629-4ad5-8fa0-2caa734a0e5e |
| ca_bidsandtenders:18816cd6-43cf-40d7-aa8f-ffc44eb6da4e:2 | London Hydro | IT Advisor Services for SAP Customer Information System Refresh |  |  |  | https://londonhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/18816cd6-43cf-40d7-aa8f-ffc44eb6da4e |
| ca_bidsandtenders:b46fb2aa-550c-4f87-beda-4f045e824570:1 | Region of Halton | Consulting Services for Feasibility Study and Public Benefit Review for a Vacant Home Tax in Halton Region |  |  |  | https://haltonregion.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b46fb2aa-550c-4f87-beda-4f045e824570 |
| … 123 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**Legal name and the relationship in the buyer's own statements.** "The Hospital for Sick Children", financial statements "the year ended March 31,
2026", auditor "Ernst & Young LLP", "Toronto, Canada", report dated "June 1, 2026" —
https://www.sickkids.ca/siteassets/about/about-sickkids/the-hospital-for-sick-children---audited-financials---2025-2026.pdf; "Accounts payable mature within
six months." → BILL TO "The Hospital for Sick Children" (not "SickKids"); the hospital is an Ontario public hospital (HST 13 % charged, hospital claims its
PSB rebate). BPSAA attestation (June 2026) at https://www.sickkids.ca/siteassets/about/accountability/bpsaa-attestation-form/broader-public-sector-accountabiliy-act-attestation-form-june2026.pdf
confirms it follows the Broader Public Sector procurement directive (competitive procurement, PO practice).

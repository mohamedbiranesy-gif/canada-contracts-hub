# S5-47 — City of Mesa ⇄ Brookfield Renewable Trading and Marketing LP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: City of Mesa — P.O. Box 1466, Mesa, AZ 85211
SUBMIT TO: accountspayable@mesaaz.gov (invoicing/AP mailbox, confirmed by the referee) | format: PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: yes (as published: purchase order, delivery order, requis)
FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC
DESCRIPTION: C1945
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: City of Mesa (municipality / local government, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Brookfield Renewable Trading and Marketing LP | subject: C1945 | all identifiers: {"ferc_tariff_reference": "MBR Tariff, FERC Electric Tariff, Volume No. 1, 4.0.0"} | awarded 2026-06-30 | published by: contact_address/contact_country_name (FERC EQR seller identity, 2026q2) | record: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet | vendor in Canada because: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=41 Victoria Street, Gatineau, QC J8X2A1, CA | status rule: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:c30b82a435db668f
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)

## Buyer
- **buyer**: City of Mesa
- **buyer_website**: https://mesaaz.gov/
- **buyer_address**: 1 N Macdonald, Suite 209, Mesa, AZ, 85021
- **buyer_phone**: 480-827-4700
- **buyer_contact_evidence_url**: https://www.visitmesa.com/
- **buyer_legal_name_as_published**: City of Mesa
- **buyer_logo_url**: https://www.mesaaz.gov/files/assets/public/v/1/stock-images/all-america-logo-white.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/22048/
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.visitmesa.com/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the lane's AP page (https://www.mesaaz.gov/Government/Finance/Accounting); invoice mailing address: the lane's AP page (https://www.mesaaz.gov/Government/Finance/Accounting); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required, check (as printed on https://www.mesaaz.gov/files/assets/public/v/2/business-development/engineering/facilities-management-prcf-construction-and-maintenance-standards-2025.pdf, re-read 2026-11-08)
- **buyer_ap_cycle_published**: monthly payment cycle (as printed on https://www.mesaaz.gov/files/assets/public/v/2/business-development/engineering/facilities-management-prcf-construction-and-maintenance-standards-2025.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: DocuSign Envelope ID: A12D188C-3BFB-41B4-88CC-36DA0CF546E3 end of the month basis, for t (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC-45A2-498F-95A6-C7F025187EA8%7D_0.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@mesaaz.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.mesaaz.gov/Government/Finance/Accounting
- **email_evidence_quote**: ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesaaz.gov Payroll 480-644-1122 (option 2)
- **email_evidence_context**: 4-2999 Location 20 E. Main St., Suite 350 85201 View Map Hours Monday - Thursday 7:00 am to 6:00 pm Service Contacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesaaz.gov Payroll 480-644-1122 (option 2) payroll@mesaaz.gov Time & Labor 480-644-1122 (option 1) time@mesaaz.gov Share Facebook X Email Print LinkedIn Back to top Site Footer Footer Contact Mesa City Hall 20 E. Main Street Mesa, AZ 85201 Mailing Address: P.O (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@mesaaz.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04 | page: https://www.mesaaz.gov/Government/Finance/Accounting | quote: "ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesa" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00001
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com
- **dmarc_record_domain**: mesaaz.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:%{ir}.%{v}.%{d}.spf.has.pphosted.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 480-644-2355
- **invoice_mailing_address**: P.O. Box 1466, Mesa, AZ 85211
- **invoicing_requirements**: City AP advises contacting the department that ordered the product/service for quickest service. Current May15,2025 standard terms: final payment upon termination within30calendar days after City appraisal and receipt of properly prepared final invoice; this is a termination provision, not a univers | invoice format as published: PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08)
- **payment_terms_as_published**: 10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC-45A2-498F-95A6-C7F025187EA8%7D_0.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC-45A2-498F-95A6-C7F025187EA8%7D_0.pdf, re-read 2026-11-08)", "po_required": "yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08)", "invoice_format": "PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08)", "ap_phone": "480-644-2355", "mailing_address": "P.O. Box 1466, Mesa, AZ 85211", "requirements_text": "City AP advises contacting the department that ordered the product/service for quickest service. Current May15,2025 standard terms: final payment upon termination within30calendar days after City appraisal and receipt of properly prepared final invoice; this is a termination provision, not a univers"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Mesa — P.O. Box 1466, Mesa, AZ 85211 ⏎ SUBMIT TO: accountspayable@mesaaz.gov (invoicing/AP mailbox, confirmed by the referee) | format: PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order, delivery order, requis) ⏎ FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC ⏎ DESCRIPTION: C1945
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Mesa", "legal_name_is_published": true, "address": "P.O. Box 1466, Mesa, AZ 85211", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@mesaaz.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "P.O. Box 1466, Mesa, AZ 85211", "format": "PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC-45A2-498F-95A6-C7F025187EA8%7D_0.pdf, re-read 2026-11-08)", "payment_method": "required, check (as printed on https://www.mesaaz.gov/files/assets/public/v/2/business-development/enginee
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08))

## Vendor
- **vendor**: Brookfield Renewable Trading and Marketing LP
- **vendor_legal_name**: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_registry_id**: 281056739 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Brookfield%20Renewable%20Trading%20and%20Marketing%20LP
- **vendor_registered_address**: TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_legal_form**: LIMITED PARTNERSHIP ON (Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_country_basis**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)=41 Victoria Street, Gatineau, QC J8X2A1, CA
- **vendor_facts_provenance**: name and address: the record's vendor block (contact_address/contact_country_name (FERC EQR seller identity, 2026q2)); registry identity: 281056739 (ON) status Active (Canada's Business Registries, ON 281056739, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2018-10-05
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, ON 281056739, 2026-11-08)
- **vendor_incorporation_date**: 2018-10-05
- **vendor_years_in_business**: 8.1 (since 2018-10-05, registry date)

## Contract
- **po_required_as_published**: yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: contact_address/contact_country_name (FERC EQR seller identity, 2026q2))
- **contract_reference**: {"ferc_tariff_reference": "MBR Tariff, FERC Electric Tariff, Volume No. 1, 4.0.0"}
- **contract_title**: C1945
- **contract_description**: C1945 (the record's title; the source publishes no separate description)
- **award_date**: 2026-06-30
- **contract_link**: https://s3.us-west-2.amazonaws.com/pudl.catalyst.coop/ferceqr/core_ferceqr__contracts/2026q2.parquet
- **source**: contact_address/contact_country_name (FERC EQR seller identity, 2026q2)
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: contact_address/contact_country_name (FERC EQR seller identity, 2026q2); 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: City of Mesa — P.O. Box 1466, Mesa, AZ 85211 ⏎ SUBMIT TO: accountspayable@mesaaz.gov (invoicing/AP mailbox, confirmed by the referee) | format: PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: purchase order, delivery order, requis) ⏎ FROM / REMIT TO: BROOKFIELD RENEWABLE TRADING AND MARKETING LP (as registered: Canada's Business Registries, ON 281056739, 2026-11-08) — TORONTO, Ontario (registered office city / province; Canada's Business Registries, ON 281056739, 2026-11-08) | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: 10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC ⏎ DESCRIPTION: C1945
- **invoice_card_json**: {"bill_to": {"legal_name": "City of Mesa", "legal_name_is_published": true, "address": "P.O. Box 1466, Mesa, AZ 85211", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@mesaaz.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "P.O. Box 1466, Mesa, AZ 85211", "format": "PDF format (as printed on https://apps.mesaaz.gov/purchasingcontracts/Search, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: purchase order, delivery order, requis) (as printed on https://apps.mesaaz.gov/jobdescriptions/documents/jobdescriptions/cs3415.pdf, re-read 2026-11-08))"}, "terms": {"payment_terms": "10 days of approval (as printed on https://apps.mesaaz.gov/purchasingcontracts/Documents/%7B9A3FE6EC-45A2-498F-95A6-C7F025187EA8%7D_0.pdf, re-read 2026-11-08)", "payment_method": "required, check (as printed on https://www.mesaaz.gov/files/assets/public/v/2/business-development/enginee
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: A
- **ap_score**: 90
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["accountspayable@mesaaz.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-04", "page: https://www.mesaaz.gov/Government/Finance/Accounting", "quote: \"ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesa\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Proofpoint", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00001"], "buyer_facts": ["address and phone: the buyer's own site, https://www.visitmesa.com/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the lane's AP page (https://www.mesaaz.gov/Government/Finance/Accounting)", "invoice mailing address: the lane's AP page (https://www.mesaaz.gov/Government/Finance/Accounting)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's ev

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.mesaaz.gov/Government/Finance/Accounting | 2026-11-08 | ok |  |  |  | 480-644-2355 | 20 E. Main Street Mesa, AZ 85201 |  |  |  |  |
| https://www.mesaaz.gov/Business-Development/Procurement-Services/How-to-Do-Business-with-Mesa | 2026-11-08 | ok |  |  |  | 480-644-2301 | 20 E. Main Street Mesa, AZ 85201 |  |  |  |  |

## Buyer site facts (org_extras, mesaaz.gov)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: City of Mesa
- **legal_name_url**: https://www.mesaaz.gov/Home
- **legal_name_quote**: Home - City of Mesa --> Skip to main content opens in new tab or window Unofficial General Election Results View Electi
- **logo_url**: https://www.mesaaz.gov/files/assets/public/v/1/stock-images/all-america-logo-white.png
- **logo_basis**: logo image on the site
- **domain**: mesaaz.gov
- **key**: lead:c30b82a435db668f
- **name**: City of Mesa
- **website**: https://mesaaz.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: East Mesa Interconnect Pipe
- **legal_name_stated_url**: https://www.mesaaz.gov/Government/About-Mesa
- **legal_name_stated_quote**: ates Woodglen Park Playground Project - CP1175WOOD Meadowgreen Park Playground Project - CP1175MEGR East Mesa Interconnect Pipe (EMIP) CP1050EM01 Eastmark Aquatic Complex - CP0756SEAQ Innovation & Efficiency Together Mesa Acces
- **mentions**: {'payment_method': {'text': 'interactive map', 'url': 'https://www.mesaaz.gov/Home', 'quote': 'fic Restrictions See current road restrictions and closures, related projects and timelines on this interactive map. Vendor Bid Opportunities Register as a vendor and receive current bid opportunity soliciations. St'}}
- **linkedin_url**: https://www.linkedin.com/company/22048/
- **tel_links**: 4806442211; 4806442221; 4806442262; 4806444277

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1 N Macdonald, Suite 209, Mesa, AZ, 85021", "address_country": "US", "address_url": "https://www.visitmesa.com/", "address_method": "json-ld", "address_quote": "e Request Relocation About Us Visitors Mean Business Blog Media Public Meetings 1 N Macdonald Suite 209 Mesa, Arizona 85201 480-827-4700 © 2026 Visit Mesa Privacy Policy Rec", "phone": "480-827-4700", "phone_url": "https://www.visitmesa.com/", "domain": "mesaaz.gov", "key": "lead:c30b82a435db668f", "name": "City of Mesa", "website": "https://mesaaz.gov/", "kind": "buyer", "date": "2026-11-03"}

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
| b | City of Mesa |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:c30b82a435db668f",
 "ap_contact_team": {
  "emails": [
   "accountspayable@mesaaz.gov",
   "purchasingadmin@mesaaz.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@mesaaz.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.mesaaz.gov/Government/Finance/Accounting",
    "quote": "ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesaaz.gov Payroll 480-644-1122 (option 2)",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Mesa",
    "task_id": "CL-SN-00936",
    "verified_via": "referee saw it on this page on 2026-11-08; the page could not be read today (unverified_page_unavailable)"
   },
   {
    "email": "accountspayable@mesaaz.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.mesaaz.gov/Government/Finance/Accounting",
    "quote": "ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesaaz.gov Payroll 480-644-1122 (option 2)",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Mesa",
    "task_id": "CL-WS-00001",
    "verified_via": "referee saw it on this page on 2026-11-08; the page could not be read today (unverified_page_unavailable)"
   },
   {
    "email": "accountspayable@mesaaz.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.mesaaz.gov/Government/Finance/Accounting",
    "quote": "ntacts Accounts Payable For quickest service, please contact the department that ordered service or product from your company. 480-644-2355 accountspayable@mesaaz.gov Payroll 480-644-1122 (option 2)",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "City of Mesa",
    "task_id": "CL-WS-00061",
    "verified_via": "referee saw it on this page on 2026-11-08; the page could not be read today (unverified_page_unavailable)"
   },
   {
    "email": "purchasingadmin@mesaaz.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.mesaaz.gov/Business-Development/Procurement-Services/How-to-Do-Business-with-Mesa",
    "quote": "e applicable laws, regulations, or procedures, those laws, regulations, and procedures take precedence. Contact Us Phone 480-644-2301 Email purchasingadmin@mesaaz.gov Hours Monday - Thursday 7:00 am to 6:00 pm Share Facebook X Email Print LinkedIn Back to top Site Footer Footer Contact Mes",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Mesa",
    "task_id": "CL-SN-00936",
    "verified_via": "https://web.archive.org/web/20261010224013/https://www.mesaaz.gov/Business-Development/Procurement-Services/How-to-Do-Business-with-Mesa"
   },
   {
    "email": "purchasingsupport@mesaaz.gov",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.mesaaz.gov/Business-Development/Procurement-Services",
    "quote": "Vendor Registration Questions Phone 480-644-6464 Email purchasingsupport@mesaaz.gov Staff Contacts Staff by Area of Responsibility Purchasing Liaisons by Department Cooperative Partners Axia Cooperative Om",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "City of Mesa",
    "task_id": "CL-SN-00936"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of mesaaz.gov (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of mesaaz.gov (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of mesaaz.gov (60 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

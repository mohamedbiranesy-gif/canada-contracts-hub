# S1-22 — Manitoba Housing ⇄ Mac-Tower Inc

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html) — 352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)
SUBMIT TO: housingaccountspayable@gov.mb.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): http://www.merx.com — MERX
REFERENCE: contract 2026-008-T-2011008 (contract_number); tender 2026-008-P-2011008 (solicitation_number) | PO rule: purchase-order terms published (as published: P.O. NUMBER REQUIS)
FROM / REMIT TO: MAC-TOWER INC. (as registered: Canada's Business Registries, MB 6724346, 2026-11-08) — Unit 15-1201 Grassmere Road, West St Paul, MB, R4A 1C4 | GST/HST 804954840 (Canada's Business Registries, MB 6724346, 2026-11-08)RT0001 (account derived from the BN9)
TAX: GST exempt (as printed on https://www.gov.mb.ca/central/psc/pubs/buysell/2.%20purchasing_card_guidelines_december_2001.pdf, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment application within 10 days (as printed on https://web2.gov.mb.ca/bills/41-3/b218e.php, re-re
DESCRIPTION: C2 Geothermal Heat Pump Replacement, Gimli | AMOUNT: 326,368.60 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 13
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Manitoba Housing (organisation (type not stated in the record), CA) — public contract / purchase award with a published end date (dated record): Mac-Tower Inc | subject: C2 Geothermal Heat Pump Replacement, Gimli | instrument: contract | contract number: 2026-008-T-2011008 (contract_number); 0000322703 (merx_reference_number) | solicitation: 2026-008-P-2011008 (solicitation_number) | all identifiers: {"merx_id": "3969394580", "merx_reference_number": "0000322703", "contract_number": "2026-008-T-2011008", "awardee_index": 1, "solicitation_number": "2026-008-P-2011008", "source_id": "PP.CO.MB.667179.C97273"} | value: 326368.6 CAD | awarded 2026-10-01, start 2026-10-01, end 2027-01-12 | published by: MERX public Awarded Solicitations (award notices) | record: https://www.merx.com/mbgov/manitobahousing/solicitations/C2-Geothermal-Heat-Pump-Replacement-Gimli/0000322703?origin=0 | vendor in Canada because: MERX award notice 'Address' block, last line = 'Canada' (with city/province/postal code lines as published) | status rule: active (published end date today or later) | this buyer has 57 records with Canada-located vendors (37 distinct vendors; 9 in the last 12 months; latest 2026-10-01)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:3064b26722a9d5fc
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 2

## Buyer
- **buyer**: Manitoba Housing
- **buyer_website**: https://www.gov.mb.ca/housing
- **buyer_phone**: 204-945-3744
- **buyer_contact_evidence_url**: https://www.gov.mb.ca/contact/
- **buyer_legal_name_as_published**: Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html)
- **buyer_logo_url**: https://gov.mb.ca/templates/en/common/images/mb-logo.png
- **buyer_website_status**: site answers
- **buyer_type**: government ministry / agency (from the organisation's name / web domain)
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoicing requirements: the lane's AP page (https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required, set out the details in Schedule 2 and check (as printed on https://web2.gov.mb.ca/laws/regs/current/forms/084_2021/sched_b1e.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: GST exempt (as printed on https://www.gov.mb.ca/central/psc/pubs/buysell/2.%20purchasing_card_guidelines_december_2001.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: housingaccountspayable@gov.mb.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf
- **email_evidence_quote**: HousingAccountsPayable@gov.mb.ca
- **email_evidence_context**: sistent, with this Agreement. Further I am responsible and shall indemnify Manitoba Housing for any liability or damages however caused that relate directly or indirectly to this service. I can obtain more information by emailing Manitoba Housing at HousingAccountsPayable@gov.mb.ca Authorized Name Title / Position Signature Date THIS AGREEMENT CAN BE MAILED, OR FAXED TO: Vendor Number Mail: Manitoba Housing Accounts Payable 700 - 352 Donald St. Winnipeg, MB, R3B 2H8 Fax: 204-945-4710 v 2015.3 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: housingaccountspayable@gov.mb.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27 | page: https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf | quote: "HousingAccountsPayable@gov.mb.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: chatgpt/chatgpt_buyer_ap_results_batch05.csv task CH-AP-00484
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1;p=reject;fo=1;rua=mailto:dmarc_rua@emaildefense.proofpoint.com;ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com;
- **dmarc_record_domain**: gov.mb.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf-0.gov.mb.ca include:spf-1.gov.mb.ca include:_spf-can.echoworx.com include:spf-004a1001.pphosted.com include:spf.protection.outlook.com include:spf.successbyemail.com include:_spf-dc17.sapsf.com include:spf.serverdata.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)
- **invoicing_requirements**: Current supplierresources link2015FOR25POterms: paymentwithin30days of submitted/approvedinvoice after satisfactorygoods/services,unlessagreedotherwise. Supplier EFT/PDS enrollment role separately published; bankchanges/cancellation at least15businessdaysbefore nextdeposit, with voidcheque or bank-c
- **payment_terms_as_published**: payment application within 10 days (as printed on https://web2.gov.mb.ca/bills/41-3/b218e.php, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: P.O. NUMBER REQUIS) (as printed on https://www.gov.mb.ca/agriculture/food-and-ag-processing/starting-a-food-business/pubs/sales-invoice-template.pdf, re-read 2026-11-08)
- **invoice_portal_url**: http://www.merx.com — MERX
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: MERX (as printed on https://www.gov.mb.ca/tenders/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment application within 10 days (as printed on https://web2.gov.mb.ca/bills/41-3/b218e.php, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: P.O. NUMBER REQUIS) (as printed on https://www.gov.mb.ca/agriculture/food-and-ag-processing/starting-a-food-business/pubs/sales-invoice-template.pdf, re-read 2026-11-08)", "portal_url": "http://www.merx.com — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)", "requirements_text": "Current supplierresources link2015FOR25POterms: paymentwithin30days of submitted/approvedinvoice after satisfactorygoods/services,unlessagreedotherwise. Supplier EFT/PDS enrollment role separately published; bankchanges/cancellation at least15businessdaysbefore nextdeposit, with voidcheque or bank-c"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html) — 352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08) ⏎ SUBMIT TO: housingaccountspayable@gov.mb.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): http://www.merx.com — MERX ⏎ REFERENCE: contract 2026-008-T-2011008 (contract_number); tender 2026-008-P-2011008 (solicitation_number) | PO rule: purchase-order terms published (as published: P.O. NUMBER REQUIS) ⏎ FROM / REMIT TO: MAC-TOWER INC. (as registered: Canada's Business Registries, MB 6724346, 2026-11-08) — Unit 15-1201 Grassmere Road, West St Paul, MB, R4A 1C4 | GST/HST 804954840 (Canada's Business Registries, MB 6724346, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: GST exempt (as printed on https://www.gov.mb.ca/central/psc/pubs/buysell/2.%20purchasing_card_guidelines_december_2001.pdf, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment application within 10 days (as printed on https://web2.gov.mb.ca/bills/41-3/b218e.php, re-re ⏎ DESCRIPTION: C2 Geothermal Heat Pump Replacement, Gimli | AMOUNT: 326,368.60 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html)", "legal_name_is_published": true, "address": "352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "housingaccountspayable@gov.mb.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "http://www.merx.com — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: MERX (as printed on https://www.gov.mb.ca/tenders/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: P.O. NUMBER REQUIS) (as printed on https://www.gov.mb.ca/agriculture/food-and-ag-processing/starting-a-food-business/pubs/sales-invoice-template.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "2026-008-T-2011008 (contract_number); 0000322703 (merx_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 2
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: 2026-008-T-2011008 (contract_number) — source ca_merx

## Vendor
- **vendor**: Mac-Tower Inc
- **vendor_legal_name**: MAC-TOWER INC. (as registered: Canada's Business Registries, MB 6724346, 2026-11-08)
- **vendor_registry_id**: 6724346 (MB)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Mac-Tower%20Inc
- **vendor_registered_address**: WINNIPEG, MB (registered office city / province; Canada's Business Registries, MB 6724346, 2026-11-08)
- **vendor_legal_form**: MB SHARE CORPORATION (Canada's Business Registries, MB 6724346, 2026-11-08)
- **vendor_address**: Unit 15-1201 Grassmere Road, West St Paul, MB, R4A 1C4
- **vendor_country_basis**: MERX award notice 'Address' block, last line = 'Canada' (with city/province/postal code lines as published)
- **vendor_bn9**: 804954840 (Canada's Business Registries, MB 6724346, 2026-11-08)
- **vendor_gst_hst_derived**: 804954840RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.mac-tower.com/
- **vendor_emails**: service@mac-tower.com
- **vendor_phone**: 204-667-7471
- **vendor_contact_evidence_url**: https://www.mac-tower.com/contact/
- **vendor_logo_url**: https://www.mac-tower.com/wp-content/uploads/2023/07/logo.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (MERX public Awarded Solicitations (award notices)); registry identity: 6724346 (MB) status Active (Canada's Business Registries, MB 6724346, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; no_match); BN9: registry: Canada's Business Registries, MB 6724346, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2013-06-07; phone / role e-mails / logo: the vendor's own site, https://www.mac-tower.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.mac-tower.com/ (site answers)
- **vendor_concentration_top_share**: Legacy Mechanical Services Inc: 5% of 57 records
- **vendor_registry_status**: Active (Canada's Business Registries, MB 6724346, 2026-11-08)
- **vendor_registry_match_level**: no_match
- **vendor_incorporation_date**: 2013-06-07
- **vendor_years_in_business**: 13.4 (since 2013-06-07, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, MB 6724346, 2026-11-08

## Contract
- **po_required_as_published**: purchase-order terms published (as published: P.O. NUMBER REQUIS) (as printed on https://www.gov.mb.ca/agriculture/food-and-ag-processing/starting-a-food-business/pubs/sales-invoice-template.pdf, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"merx_id": "3969394580", "merx_reference_number": "0000322703", "contract_number": "2026-008-T-2011008", "awardee_index": 1, "solicitation_number": "2026-008-P-2011008", "source_id": "PP.CO.MB.667179.C97273"}
- **contract_title**: C2 Geothermal Heat Pump Replacement, Gimli
- **contract_description**: Awarded
- **contract_or_agreement_number**: 2026-008-T-2011008 (contract_number); 0000322703 (merx_reference_number)
- **solicitation_or_tender_number**: 2026-008-P-2011008 (solicitation_number)
- **award_or_notice_id**: 3969394580 (merx_id); PP.CO.MB.667179.C97273 (source_id); 1 (awardee_index)
- **contract_value**: 326368.6
- **currency**: CAD
- **award_date**: 2026-10-01
- **start_date**: 2026-10-01
- **end_date**: 2027-01-12
- **contract_link**: https://www.merx.com/mbgov/manitobahousing/solicitations/C2-Geothermal-Heat-Pump-Replacement-Gimli/0000322703?origin=0
- **source**: MERX public Awarded Solicitations (award notices)
- **contracts_with_canadian_suppliers**: 57
- **records_last_12_months**: 9
- **record_sources**: MERX public Awarded Solicitations (award notices) (57)
- **records_with_this_vendor**: 2
- **records_in_contract_dataset**: 57 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 804954840RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html) — 352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08) ⏎ SUBMIT TO: housingaccountspayable@gov.mb.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): http://www.merx.com — MERX ⏎ REFERENCE: contract 2026-008-T-2011008 (contract_number); tender 2026-008-P-2011008 (solicitation_number) | PO rule: purchase-order terms published (as published: P.O. NUMBER REQUIS) ⏎ FROM / REMIT TO: MAC-TOWER INC. (as registered: Canada's Business Registries, MB 6724346, 2026-11-08) — Unit 15-1201 Grassmere Road, West St Paul, MB, R4A 1C4 | GST/HST 804954840 (Canada's Business Registries, MB 6724346, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: GST exempt (as printed on https://www.gov.mb.ca/central/psc/pubs/buysell/2.%20purchasing_card_guidelines_december_2001.pdf, re-read 2026-11-08) | CURRENCY: CAD | TERMS: payment application within 10 days (as printed on https://web2.gov.mb.ca/bills/41-3/b218e.php, re-re ⏎ DESCRIPTION: C2 Geothermal Heat Pump Replacement, Gimli | AMOUNT: 326,368.60 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Manitoba Government (stated on https://gov.mb.ca/accessibility/index.html)", "legal_name_is_published": true, "address": "352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "housingaccountspayable@gov.mb.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "http://www.merx.com — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "352 Donald St. Winnipeg, MB, R3B 2H8 (as printed on https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: MERX (as printed on https://www.gov.mb.ca/tenders/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: P.O. NUMBER REQUIS) (as printed on https://www.gov.mb.ca/agriculture/food-and-ag-processing/starting-a-food-business/pubs/sales-invoice-template.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "2026-008-T-2011008 (contract_number); 0000322703 (merx_reference_number)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 2
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["housingaccountspayable@gov.mb.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-27", "page: https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf", "quote: \"HousingAccountsPayable@gov.mb.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: chatgpt/chatgpt_buyer_ap_results_batch05.csv task CH-AP-00484"], "buyer_facts": ["legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoicing requirements: the lane's AP page (https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (MERX public Awarded Solicitations (aw

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf | 2026-11-08 | ok |  |  |  |  | 352 Donald St. Winnipeg, MB, R3B 2H8 |  |  |  |  |
| https://www.gov.mb.ca/mr/mwsb/ | 2026-11-08 | ok |  |  |  | (204) 726-6076 | 2010 Currie Boulevard Brandon, Manitoba, R7B 4E7 |  |  |  |  |

## Buyer site facts (org_extras, gov.mb.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://gov.mb.ca/templates/en/common/images/mb-logo.png
- **logo_basis**: logo image in the site header
- **domain**: gov.mb.ca
- **key**: b:3064b26722a9d5fc
- **name**: Manitoba Housing
- **website**: https://gov.mb.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Manitoba Government Accessibility Plan
- **legal_name_stated_url**: https://gov.mb.ca/accessibility/index.html
- **legal_name_stated_quote**: trol over the information; the information relates to product labels or other product information.” Manitoba Government Accessibility Plan and Policies Learn more about The Accessibility for Manitobans Act , and find additional informatio

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "phone": "204-945-3744", "phone_url": "https://www.gov.mb.ca/contact/", "domain": "gov.mb.ca", "key": "b:34d574ac09615e62", "name": "Manitoba Water Services Board", "website": "https://gov.mb.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, mac-tower.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://www.mac-tower.com/wp-content/uploads/2023/07/logo.png
- **logo_basis**: logo image on the site
- **domain**: mac-tower.com
- **key**: vendor:Mac-Tower Inc
- **name**: Mac-Tower Inc
- **website**: https://mac-tower.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Dry Bulb Temperature
- **legal_name_stated_url**: https://www.mac-tower.com/cooling-tower-fluid-cooler-terms/
- **legal_name_stated_quote**: inator, while allowing the passage of exhausted air through the eliminator and into the atmosphere. Dry Bulb Temperature (DBT) – The temperature of the air entering the cooling tower, measured in degrees Fahrenheit. Entr
- **tel_links**: 204-667-7471; 1-866-415-2595

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1201 Grassmere Rd., West St. Paul, Manitoba, R4A 1C4", "address_country": "CA", "address_url": "https://www.mac-tower.com/contact/", "address_method": "pattern", "address_quote": ". Cooling Tower Specialists Unit 15- 1201 Grassmere Rd. West St. Paul, Manitoba R4A 1C4 Phone: 204-667-7471 Toll Free: 1-866-415-2595 Fax: 204-336-0203 service@mac-tow", "phone": "204-667-7471", "phone_url": "https://www.mac-tower.com/contact/", "emails": "service@mac-tower.com", "emails_url": "https://www.mac-tower.com/contact/", "domain": "mac-tower.com", "key": "vd:mac-tower.com", "name": "Mac-Tower Inc", "website": "https://mac-tower.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Manitoba Housing | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Manitoba%20Housing | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Manitoba Housing |  |  |  |  |  |  |  |  |  |  |
| b | Manitoba Water Services Board |  |  |  |  |  |  |  |  |  |  |
| b | Manitoba Environment and Climate Change |  |  |  |  |  |  |  |  |  |  |
| b | Manitoba Public Service Delivery |  |  |  |  |  |  |  |  |  |  |
| b | Manitoba Transportation and Infrastructure - Tendering and Contracts |  |  |  |  |  |  |  |  |  |  |
| v | Mac-Tower Inc |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:3064b26722a9d5fc",
 "ap_contact_team": {
  "emails": [
   "mhrcagencyservices@gov.mb.ca",
   "HousingAccountsPayable@gov.mb.ca",
   "mhprocurement@gov.mb.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": "Agency Services, Manitoba Housing Renewal Corporation, 6th Floor-352 Donald Street, Winnipeg MB R3B 2H8 (2018/19 short-term shelter schedule only)",
  "invoicing_requirements": "Historical 2018/19 short-term shelter agreement: monthly invoice states number of asylum seekers receiving room/board; payment within30days of receipt. Invoice to AgencyServices by statedmail/fax2049438898/email. No evidence this temporary program route remains current.",
  "evidence": [
   {
    "email": "mhrcagencyservices@gov.mb.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": "Agency Services, Manitoba Housing Renewal Corporation, 6th Floor-352 Donald Street, Winnipeg MB R3B 2H8 (2018/19 short-term shelter schedule only)",
    "requirements": "Historical 2018/19 short-term shelter agreement: monthly invoice states number of asylum seekers receiving room/board; payment within30days of receipt. Invoice to AgencyServices by statedmail/fax2049438898/email. No evidence this temporary program route remains current.",
    "applies_to": "this_unit_only",
    "page_url": "https://www.gov.mb.ca/housing/rtr/portfolio-management/agency-services/spa-and-schedules/2018-19-asylum-seekers-schedule.pdf",
    "quote": "Email: mhrcagencyservices@gov.mb.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch05.csv",
    "org": "Manitoba Housing Renewal Corporation",
    "task_id": "CH-AP-00484"
   },
   {
    "email": "HousingAccountsPayable@gov.mb.ca",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "Current supplierresources link2015FOR25POterms: paymentwithin30days of submitted/approvedinvoice after satisfactorygoods/services,unlessagreedotherwise. Supplier EFT/PDS enrollment role separately published; bankchanges/cancellation at least15businessdaysbefore nextdeposit, with voidcheque or bank-completed bankingdetails.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.gov.mb.ca/housing/pubs/procurement/mh-pds_agreement_form_v2015.3.pdf",
    "quote": "HousingAccountsPayable@gov.mb.ca",
    "retrieved_date": "2026-10-27",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch05.csv",
    "org": "Manitoba Housing / Manitoba Housing and Renewal Corporation",
    "task_id": "CH-AP-00484"
   },
   {
    "email": "mhprocurement@gov.mb.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.gov.mb.ca/housing/business/procurement.html",
    "quote": "open a new page) Contact Procurement Manitoba Housing Procurement 500 - 352 Donald St. Winnipeg MB R3B 2H8 Fax: (204) 948-1407 --> E-mail: MHProcurement@gov.mb.ca Manitoba Housing Home | Our Programs | Find Housing | Tenant Resources | Our Communities | News | About Us | Working with Mani",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Manitoba Housing Renewal Corporation",
    "task_id": "CH-AP-00484"
   }
  ]
 },
 "research_status": {
  "found": 2,
  "unclear": 1
 },
 "queries_tried": [
  "site:gov.mb.ca/housing invoices accounts payable; site:gov.mb.ca/housing \"HousingAccountsPayable\"; opened officialhousinghome,currentProcurement/SupplierResourcesandlinkedPDS/formandPOterms;incorrect/procurement/indexroutewasdiscarded",
  "site:gov.mb.ca/housing \"invoices\" \"email\"; opened official2018-19ShortTermShelterForAsylumSeekersschedule",
  "site crawl of www.gov.mb.ca (25 pages, robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_merx:3969394580:1 | ca_merx | ongoing | C2 Geothermal Heat Pump Replacement, Gimli | 326368.6 | CAD |  |  | {"merx_id": "3969394580", "merx_reference_number": "0000322703", "contract_number": "2026-008-T-2011008", "awardee_index": 1, "solicitation_number": "2026-008-P-2011008", "source_id": "PP.CO.MB.667179 | https://www.merx.com/mbgov/manitobahousing/solicitations/C2-Geothermal-Heat-Pump-Replacement-Gimli/0000322703?origin=0 |
| ca_merx:3475123917:1 | ca_merx | ongoing | Wood Stove Preventative Maintenance - Brochet, MB |  |  |  |  | {"merx_id": "3475123917", "merx_reference_number": "0000295456", "contract_number": null, "awardee_index": 1} | https://www.merx.com/mbgov/manitobahousing/solicitations/Wood-Stove-Preventative-Maintenance-Brochet-MB/0000295456?origin=0 |

## The buyer's other Canadian-vendor records (first 60 of 55)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_merx:3953329960:1 | Dufresne Furniture | New Appliance - Brandon Area 1 - 7 | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/New-Appliance-Brandon-Area-1-7/0000321506?origin=0 |
| ca_merx:3857967366:1 | Global Mechanical Ltd. | Residential Furnace & HRV New and Replace - North Eastman Area 1 & 2 | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Furnace-HRV-New-and-Replace-North-Eastman-Area-1-2/0000315540?origin=0 |
| ca_merx:3596354972:1 | Cobbe's Plumbing & Heating Ltd. | Furnace, Dryer Vents & AC Preventative Maintenance -Portage & Central Manitoba | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-Portage-Central-Manitoba/0000302645?origin=0 |
| ca_merx:3596354972:2 | Wahoski Mechanical Ltd. | Furnace, Dryer Vents & AC Preventative Maintenance -Portage & Central Manitoba | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-Portage-Central-Manitoba/0000302645?origin=0 |
| ca_merx:3593946520:1 | Global Mechanical Ltd. | Furnace, Dryer Vents & AC Preventative Maintenance -Selkirk, MB | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-Selkirk-MB/0000302456?origin=0 |
| ca_merx:3601367519:1 | AOK Furnace and Duct Cleaning | Furnace, Dryer Vents & AC Preventative Maintenance -DPR & Swan River, MB | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-DPR-Swan-River-MB/0000302966?origin=0 |
| ca_merx:3601367519:2 | Super Plumbing & Heating | Furnace, Dryer Vents & AC Preventative Maintenance -DPR & Swan River, MB | 1.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-DPR-Swan-River-MB/0000302966?origin=0 |
| ca_merx:3606730698:1 | Wheat City Electric | Furnace, Dryer Vents & AC Preventative Maintenance -Brandon Areas 1 - 7 |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Furnace-Dryer-Vents-AC-Preventative-Maintenance-Brandon-Areas-1-7/0000303398?origin=0 |
| ca_merx:3546322724:1 | JRoss Construction & Landscaping Ltd | Drainage Remediation - Bridgwater Lakes and Trails | 656000.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Drainage-Remediation-Bridgwater-Lakes-and-Trails/0000299500?origin=0 |
| ca_merx:3442047765:1 | Legacy Mechanical Services Inc | Residential Heat Recovery Ventilators (HRV) Inspection and Service-Portage& Cent |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Portage-Cent/0000293459?origin=0 |
| ca_merx:3434421014:1 | G.Chura Enterprises | Residential Heat Recovery Ventilators (HRV) Inspection and Service -DPR, MB |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-DPR-MB/0000292958?origin=0 |
| ca_merx:3438691322:1 | Denko Mechanical Ltd | Residential Heat Recovery Ventilators (HRV) Inspection and Service -Selkirk, MB |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Selkirk-MB/0000293291?origin=0 |
| ca_merx:3411781973:1 | Legacy Mechanical Services Inc | Residential Heat Recovery Ventilators (HRV) Inspection and Service -Brandon 1- 7 |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Brandon-1-7/0000291551?origin=0 |
| ca_merx:3411781973:2 | Wheat City Electric | Residential Heat Recovery Ventilators (HRV) Inspection and Service -Brandon 1- 7 |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Brandon-1-7/0000291551?origin=0 |
| ca_merx:3211162266:1 | Veseris | Pesticide & Pest Monitoring Supplies - Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Pesticide-Pest-Monitoring-Supplies-Winnipeg/0000281654?origin=0 |
| ca_merx:3317580762:1 | Denko Mechanical Ltd | Residential Heat Recovery Ventilators (HRV) Inspection and Service - Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Winnipeg/0000286491?origin=0 |
| ca_merx:3317580762:2 | Legacy Mechanical Services Inc | Residential Heat Recovery Ventilators (HRV) Inspection and Service - Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Residential-Heat-Recovery-Ventilators-HRV-Inspection-and-Service-Winnipeg/0000286491?origin=0 |
| ca_merx:2811381668:1 | Bosch Building Technologies Inc. \| Paladin Technologies Inc. | Security Upgrade Project - 248 - 8th Street, Brandon - Princess Towers |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Security-Upgrade-Project-248-8th-Street-Brandon-Princess-Towers/0000264968?origin=0 |
| ca_merx:2842921765:1 | The Urban Garden | Replacement of Carpet - 555 Ellice Ave., Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Replacement-of-Carpet-555-Ellice-Ave-Winnipeg/0000266670?origin=0 |
| ca_merx:2782496312:1 | Bosch Building Technologies Inc. \| Paladin Technologies Inc. | Security Upgrade Project - 777 Sargent Ave, Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Security-Upgrade-Project-777-Sargent-Ave-Winnipeg/0000263479?origin=0 |
| ca_merx:2730826011:1 | Creel Painting And Wallpapering | Contract Caretaker Services - Portage La Prairie |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Contract-Caretaker-Services-Portage-La-Prairie/0000261297?origin=0 |
| ca_merx:2567584563:1 | The Secure Construction Group | Remove, supply and install fire rated doors and hardware - 101 Marion Street |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Remove-supply-and-install-fire-rated-doors-and-hardware-101-Marion-Street/0000253259?origin=0 |
| ca_merx:2690406169:1 | Coinamatic Canada Inc. | Washer and Dryer Rentals - MB Wide |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Washer-and-Dryer-Rentals-MB-Wide/0000259835?origin=0 |
| ca_merx:2668863726:1 | Frontier Power Products | Emergency Generator Preventative Maintenance - MB Wide |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Emergency-Generator-Preventative-Maintenance-MB-Wide/0000258942?origin=0 |
| ca_merx:2577479828:1 | EyeQ Security Services | Security Guard Services - The Pas |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Security-Guard-Services-The-Pas/0000253998?origin=0 |
| ca_merx:2547834116:1 | Merv's Excavating Ltd. | Supply and Install New Water Lines and Sewer Lines - Churchill |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Supply-and-Install-New-Water-Lines-and-Sewer-Lines-Churchill/0000251846?origin=0 |
| ca_merx:2555027777:1 | Priority Restoration | Insurance Rebuild - 7-265 Gordon Ave., Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Insurance-Rebuild-7-265-Gordon-Ave-Winnipeg/0000252361?origin=0 |
| ca_merx:2555027775:1 | Priority Restoration | Insurance Rebuild - 21-265 Gordon Ave., Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Insurance-Rebuild-21-265-Gordon-Ave-Winnipeg/0000252356?origin=0 |
| ca_merx:2462582961:1 | WESTERN CONSTRUCTION SERVICES INC. | Rose Lake Green Fountain Pump House and Plaza Repairs - 96 Rose Lake Court, Wpg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Rose-Lake-Green-Fountain-Pump-House-and-Plaza-Repairs-96-Rose-Lake-Court-Wpg/0000244897?origin=0 |
| ca_merx:2449678909:1 | Green Drop Tree Care | Tree Planting - Bridgwater Lakes, Centre and Trails (Phase 1 & 2) - Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Tree-Planting-Bridgwater-Lakes-Centre-and-Trails-Phase-1-2-Winnipeg/0000243810?origin=0 |
| ca_merx:2414097618:1 | WESTERN CONSTRUCTION SERVICES INC. | Parkade Ceiling Upgrade - 641 Spence Street, Winnipeg, MB |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Parkade-Ceiling-Upgrade-641-Spence-Street-Winnipeg-MB/0000241145?origin=0 |
| ca_merx:2183425847:1 | Dufresne Operations INC | New Appliances - Portage & Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/New-Appliances-Portage-Central-Manitoba/0000222560?origin=0 |
| ca_merx:2183425846:1 | Dufresne Operations INC | New Appliances - Selkirk and Surrounding Areas |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/New-Appliances-Selkirk-and-Surrounding-Areas/0000222555?origin=0 |
| ca_merx:2164976522:1 | Otis Canada Inc | Elevator Preventive Maintenance - Winnipeg |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Elevator-Preventive-Maintenance-Winnipeg/0000221089?origin=0 |
| ca_merx:2162626903:1 | BHP Mechanical Service Group Ltd. | In Unit Plumbing - Dauphin, Roblin, and Parklands |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Dauphin-Roblin-and-Parklands/0000220893?origin=0 |
| ca_merx:2162626903:2 | G.Chura Enterprises | In Unit Plumbing - Dauphin, Roblin, and Parklands |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Dauphin-Roblin-and-Parklands/0000220893?origin=0 |
| ca_merx:2156268403:1 | Claude's Water Treatment | In Unit Plumbing - IL 1&2, NE 1&2, SE 1&2 and Berens River |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-IL-1-2-NE-1-2-SE-1-2-and-Berens-River/0000220393?origin=0 |
| ca_merx:2156268403:2 | Gulay Supply Ltd | In Unit Plumbing - IL 1&2, NE 1&2, SE 1&2 and Berens River |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-IL-1-2-NE-1-2-SE-1-2-and-Berens-River/0000220393?origin=0 |
| ca_merx:2152556936:1 | Bergmann Plumbing & Heating Ltd. | In Unit Plumbing - Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Central-Manitoba/0000220222?origin=0 |
| ca_merx:2152556936:2 | Claude's Water Treatment | In Unit Plumbing - Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Central-Manitoba/0000220222?origin=0 |
| ca_merx:2152556936:3 | Cobbe's Plumbing & Heating Ltd. | In Unit Plumbing - Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Central-Manitoba/0000220222?origin=0 |
| ca_merx:2152556936:4 | Gulay Supply Ltd | In Unit Plumbing - Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Central-Manitoba/0000220222?origin=0 |
| ca_merx:2152556936:5 | Wahoski Mechanical Ltd. | In Unit Plumbing - Central Manitoba |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/In-Unit-Plumbing-Central-Manitoba/0000220222?origin=0 |
| ca_merx:2004135604:1 | Kontzamanis Graumann Smith Macmillan Inc. (o/a KGS GROUP) | Prime Consultant Services for Exterior Refresh, Mechanical Upgrades & Site Work | 1241361.65 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Prime-Consultant-Services-for-Exterior-Refresh-Mechanical-Upgrades-Site-Work/0000211068?origin=0 |
| ca_merx:2002630369:1 | Kontzamanis Graumann Smith Macmillan Inc. (o/a KGS GROUP) | Prime Consultant Services for Exterior Retrofit and Site Work | 192496.64 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Prime-Consultant-Services-for-Exterior-Retrofit-and-Site-Work/0000211009?origin=0 |
| ca_merx:1945987106:1 | f-BLOK architecture inc | Consultant, Exterior Retrofit, Mechanical Upgrades and Site Works | 244192.66 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Consultant-Exterior-Retrofit-Mechanical-Upgrades-and-Site-Works/0000208027?origin=0 |
| ca_merx:2009365954:1 | Kontzamanis Graumann Smith Macmillan Inc. (o/a KGS GROUP) | Prime Consultant Services, Replacement & Relocation of Make-Up Air Unit | 31285.36 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Prime-Consultant-Services-Replacement-Relocation-of-Make-Up-Air-Unit/0000211409?origin=0 |
| ca_merx:1946004538:1 | Eagle Valley Acres O/A The Brick | New Appliances - Thompson & Churchill |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/New-Appliances-Thompson-Churchill/0000208096?origin=0 |
| ca_merx:1944009976:1 | Paul's Plumbing & Heating Ltd. | Oil Fired Furnace Annual Preventative Maintenance - Brochet, MB |  |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Oil-Fired-Furnace-Annual-Preventative-Maintenance-Brochet-MB/0000207909?origin=0 |
| ca_merx:1882569861:1 | MCW Consultants Ltd. | Consultant, Fire Detection and Emergency Lighting System | 117322.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Consultant-Fire-Detection-and-Emergency-Lighting-System/0000204769?origin=0 |
| ca_merx:1712633453:1 | Central Elevator Ltd. | Elevator Modernization | 344221.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Elevator-Modernization/0000192283?origin=0 |
| ca_merx:1709303024:1 | Central Elevator Ltd. | Elevator Modernization | 157221.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Elevator-Modernization/0000192033?origin=0 |
| ca_merx:1692885255:1 | Central Elevator Ltd. | Elevator Modernization | 147221.0 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Elevator-Modernization/0000190937?origin=0 |
| ca_merx:1813247769:1 | f-BLOK architecture inc | Consultant, Exterior Retrofit, Mechanical, Electrical & Site Works | 171590.28 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Consultant-Exterior-Retrofit-Mechanical-Electrical-Site-Works/0000200001?origin=0 |
| ca_merx:1813247758:1 | Bouwen Architecture Ltd. | Consultant, Exterior Retrofit and Site Work | 151609.01 |  |  | https://www.merx.com/mbgov/manitobahousing/solicitations/Consultant-Exterior-Retrofit-and-Site-Work/0000199971?origin=0 |

## The vendor's other buyers in the dataset (first 60 of 4)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:b3e4b5aa-0441-4ed1-b85a-09818cfcf65b:1 | Manitoba Water Services Board | Asessippi Provincial Park Water Treatment Plant Upgrade |  |  |  | https://mwsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b3e4b5aa-0441-4ed1-b85a-09818cfcf65b |
| ca_merx:3602586212:8 | The City of Winnipeg | Provision of Minor Electrical Systems Maintenance and Modifications |  |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Provision-of-Minor-Electrical-Systems-Maintenance-and-Modifications/0000303065?origin=0 |
| ca_merx:3538123527:5 | The City of Winnipeg | Provision of Plumbing Services |  |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Provision-of-Plumbing-Services/0000298854?origin=0 |
| ca_merx:3538123532:5 | The City of Winnipeg | Inspection and Repair of HVAC Services |  |  |  | https://www.merx.com/mbgov/cityofwinnipeg/solicitations/Inspection-and-Repair-of-HVAC-Services/0000298863?origin=0 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

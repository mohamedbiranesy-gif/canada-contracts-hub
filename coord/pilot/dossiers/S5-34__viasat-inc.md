# S5-34 — VIASAT INC ⇄ AWC MANUFACTURING LP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Viasat, Inc — 6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA — buyer tax no. 859098378 (Canada's Business Registries, MB 6814191, 2026-11-08)
SUBMIT TO: ViasatAP@viasat.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: SAP Ariba
REFERENCE: none in the record | PO rule: yes (as published: reference PO)
FROM / REMIT TO: AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08) — 95 LYON AVE N, TILBURY, ON, N0P 2L0 | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: net60
DESCRIPTION: METAL FAB (first sentence of the record's description; the source publishes no separate title) | AMOUNT: 137,760.00 USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 11
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: VIASAT INC (company (private sector), US) — public contract / purchase award in the last 12 months (dated record): AWC MANUFACTURING LP | subject: METAL FAB (first sentence of the record's description; the source publishes no separate title) | instrument: subcontract | all identifiers: {"subaward_number": "4318939", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sam_report_ids": ["F1E6E527-93D5-4C63-8147-5F9B430DA647"], "subaward_sam_report_periods": ["2026-9"]} | value: 137760.0 USD | awarded 2026-08-17, start 2026-08-17 (contract signature date as published) | published by: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports) | record: https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/ | vendor in Canada because: subawardee_country_code == 'CAN' (SAM.gov/FSRS SubAwardeeLegalEntityCountryCode; bulk download filtered on recipient_locations country=CAN, applied to sub_recipient_location_country_code for subawards) | status rule: likely active (source marks it as continuing; awarded in the last 3 years, no end date published) | this buyer has 4 records with Canada-located vendors (1 distinct vendors; 4 in the last 12 months; latest 2026-08-17)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:0bd395a97cc23d6e
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 4

## Buyer
- **buyer**: VIASAT INC
- **buyer_website**: https://www.viasat.com
- **buyer_address**: 6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA
- **buyer_contact_evidence_url**: https://www.viasat.com/contact/
- **buyer_legal_name_as_published**: Viasat, Inc
- **buyer_bn_as_published**: 859098378 (Canada's Business Registries, MB 6814191, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 859098378RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.viasat.com/etc.clientlibs/viasat-base/clientlibs/clientlib-resources/resources/social/ogImage.jpg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/viasat/
- **buyer_registry_id**: 6814191 (MB; https://ised-isde.canada.ca/cbr-rec/en/search?q=VIASAT%20INC)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7924358; business; telecommunications company; public company
- **buyer_founded**: 1986-00-00 (Wikidata Q7924358, official website on the organisation's domain (http://viasat.com) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 860000000 Q4917 (Wikidata Q7924358, official website on the organisation's domain (http://viasat.com) + name; 2026-11-08)
- **buyer_legal_form**: Delaware corporation (Wikidata Q7924358, official website on the organisation's domain (http://viasat.com) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.viasat.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoicing requirements: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf); payment terms: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf); PO requirement: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ViasatAP@viasat.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf
- **email_evidence_quote**: cable goods or services. Unless instructed otherwise by Viasat in writing, invoices shall be sent to Viasat via email at ViasatAP@viasat.com. d. Excluding any Seller that is a certified small business p
- **mailbox_provenance**: viasatap@viasat.com (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29 | page: https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf | quote: "cable goods or services. Unless instructed otherwise by Viasat in writing, invoices shall be sent to Viasat via email at ViasatAP@viasat.com. d. Excluding any S" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint | lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01070
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; fo=1; rua=mailto:dmarc_rua@emaildefense.proofpoint.com; ruf=mailto:dmarc_ruf@emaildefense.proofpoint.com
- **dmarc_record_domain**: viasat.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf-0085b301.gpphosted.com include:spf-0085b303.pphosted.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: ViasatIncPR001076Rev050: invoice after goods delivery/service performance and reference PO. Unless PO says otherwise, net60 after later receipt of correct invoice or acceptance. Email AP unless written direction differs. Use designated supplier systems as Viasat directs.
- **payment_terms_as_published**: net60
- **po_required_as_published**: yes (as published: reference PO)
- **invoice_portal_url**: SAP Ariba
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SAP Ariba
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "net60", "po_required": "yes (as published: reference PO)", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "requirements_text": "ViasatIncPR001076Rev050: invoice after goods delivery/service performance and reference PO. Unless PO says otherwise, net60 after later receipt of correct invoice or acceptance. Email AP unless written direction differs. Use designated supplier systems as Viasat directs."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Viasat, Inc — 6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA — buyer tax no. 859098378 (Canada's Business Registries, MB 6814191, 2026-11-08) ⏎ SUBMIT TO: ViasatAP@viasat.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: SAP Ariba ⏎ REFERENCE: none in the record | PO rule: yes (as published: reference PO) ⏎ FROM / REMIT TO: AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08) — 95 LYON AVE N, TILBURY, ON, N0P 2L0 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: net60 ⏎ DESCRIPTION: METAL FAB (first sentence of the record's description; the source publishes no separate title) | AMOUNT: 137,760.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Viasat, Inc", "legal_name_is_published": true, "address": "6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA", "address_is_the_invoice_address": false, "tax_number": "859098378 (Canada's Business Registries, MB 6814191, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ViasatAP@viasat.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: reference PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 4318939 (subaward_number) — source usaspending"}, "terms": {"payment_terms": "net60", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "USD", "currency_is_published": true, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08)",
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: award or notice id: 4318939 (subaward_number) — source usaspending

## Vendor
- **vendor**: AWC MANUFACTURING LP
- **vendor_legal_name**: AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08)
- **vendor_registry_id**: 241207406 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=AWC%20MANUFACTURING%20LP
- **vendor_registered_address**: WINDSOR, Ontario (registered office city / province; Canada's Business Registries, ON 241207406, 2026-11-08)
- **vendor_legal_form**: LIMITED PARTNERSHIP ON (Canada's Business Registries, ON 241207406, 2026-11-08)
- **vendor_address**: 95 LYON AVE N, TILBURY, ON, N0P 2L0
- **vendor_country_basis**: subawardee_country_code == 'CAN' (SAM.gov/FSRS SubAwardeeLegalEntityCountryCode; bulk download filtered on recipient_locations country=CAN, applied to sub_recipient_location_country_code for subawards)
- **vendor_website**: https://awcmanufacturing.com/
- **vendor_emails**: info@awcmanufacturing.com
- **vendor_phone**: 5198220577 (tel: link on https://awcmanufacturing.com/)
- **vendor_contact_evidence_url**: https://awcmanufacturing.com/contact-us
- **vendor_logo_url**: https://awcmanufacturing.com/images/header-logo.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/awcmanufacturing
- **vendor_facts_provenance**: name and address: the record's vendor block (USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports)); registry identity: 241207406 (ON) status Active — registered (Canada's Business Registries, ON 241207406, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; no_match); incorporated / registered: 2014-12-22; phone / role e-mails / logo: the vendor's own site, https://awcmanufacturing.com/contact-us (tools/org_contacts.py, org_extras.py); website: https://awcmanufacturing.com/ (site answers)
- **vendor_concentration_top_share**: AWC MANUFACTURING LP: 100% of 4 records
- **vendor_registry_status**: Active — registered (Canada's Business Registries, ON 241207406, 2026-11-08)
- **vendor_registry_match_level**: no_match
- **vendor_incorporation_date**: 2014-12-22
- **vendor_years_in_business**: 11.9 (since 2014-12-22, registry date)

## Contract
- **po_required_as_published**: yes (as published: reference PO)
- **contract_status**: likely active (source marks it as continuing; awarded in the last 3 years, no end date published)
- **contract_reference**: {"subaward_number": "4318939", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sam_report_ids": ["F1E6E527-93D5-4C63-8147-5F9B430DA647"], "subaward_sam_report_periods": ["2026-9"]}
- **contract_title**: METAL FAB (first sentence of the record's description; the source publishes no separate title)
- **contract_description**: METAL FAB
- **award_or_notice_id**: 4318939 (subaward_number); 47QFLA25F0054 (prime_award_piid); 47QFLA25D0001 (prime_award_parent_piid); 2026-9 (subaward_sam_report_periods); CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732 (prime_award_unique_key); F1E6E527-93D5-4C63-8147-5F9B430DA647 (subaward_sam_report_ids)
- **commodity_codes**: NAICS 334290 (OTHER COMMUNICATIONS EQUIPMENT MANUFACTURING)
- **contract_value**: 137760.0
- **currency**: USD
- **award_date**: 2026-08-17
- **start_date**: 2026-08-17 (contract signature date as published)
- **contract_link**: https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/
- **source**: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports)
- **contracts_with_canadian_suppliers**: 4
- **records_last_12_months**: 4
- **record_sources**: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports) (4)
- **records_with_this_vendor**: 4
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 859098378RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Viasat, Inc — 6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA — buyer tax no. 859098378 (Canada's Business Registries, MB 6814191, 2026-11-08) ⏎ SUBMIT TO: ViasatAP@viasat.com (invoicing/AP mailbox, confirmed by the referee) | invoice portal: SAP Ariba ⏎ REFERENCE: none in the record | PO rule: yes (as published: reference PO) ⏎ FROM / REMIT TO: AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08) — 95 LYON AVE N, TILBURY, ON, N0P 2L0 | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state  | CURRENCY: USD | TERMS: net60 ⏎ DESCRIPTION: METAL FAB (first sentence of the record's description; the source publishes no separate title) | AMOUNT: 137,760.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Viasat, Inc", "legal_name_is_published": true, "address": "6155, EL CAMINO REAL, CARLSBAD, CA, 920091602, USA", "address_is_the_invoice_address": false, "tax_number": "859098378 (Canada's Business Registries, MB 6814191, 2026-11-08)", "language": "en"}, "submit_to": {"email": "ViasatAP@viasat.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: reference PO)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 4318939 (subaward_number) — source usaspending"}, "terms": {"payment_terms": "net60", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state ", "buyer_tax_status_is_published": false, "indicative_rate": "", "currency": "USD", "currency_is_published": true, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "AWC MANUFACTURING LP (as registered: Canada's Business Registries, ON 241207406, 2026-11-08)",
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["viasatap@viasat.com (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-29", "page: https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf", "quote: \"cable goods or services. Unless instructed otherwise by Viasat in writing, invoices shall be sent to Viasat via email at ViasatAP@viasat.com. d. Excluding any S\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Proofpoint", "lane file: chatgpt/chatgpt_buyer_ap_results_batch11.csv task CH-AP-01070"], "buyer_facts": ["address and phone: the buyer's own site, https://www.viasat.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoicing requirements: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf)", "payment terms: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf)", "PO requirement: the lane's AP page (https://www.viasat.com/content/dam/us-site/supplier/

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf | 2026-11-08 | http_404 |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, viasat.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Viasat, Inc
- **legal_name_url**: https://www.viasat.com/
- **legal_name_quote**: vice is not available in all areas. Offer may be changed or withdrawn at any time. Copyright © 2026 Viasat, Inc. All rights reserved. Viasat, the Viasat logo and the Viasat signal are registered trademarks of Vi
- **logo_url**: https://www.viasat.com/etc.clientlibs/viasat-base/clientlibs/clientlib-resources/resources/social/ogImage.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: viasat.com
- **key**: b:0bd395a97cc23d6e
- **name**: VIASAT INC
- **website**: https://viasat.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: American Institute
- **legal_name_stated_url**: https://www.viasat.com/about/company/viasat-history/
- **legal_name_stated_quote**: Viasat named a Washington Technology Top 100 Government Contractor 2008 Mark Dankberg received the American Institute of Aeronautics and Astronautics (AIAA) 2008 Aerospace International Communications Award Viasat nam
- **linkedin_url**: https://www.linkedin.com/company/viasat/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "6155 El Camino Real, Carlsbad, CA 92009", "address_country": "US", "address_url": "https://www.viasat.com/contact/", "address_method": "pattern", "address_quote": "ntact us Contact Viasat Viasat headquarters – Carlsbad, California Viasat, Inc. 6155 El Camino Real Carlsbad, CA 92009 USA Phone: (760) 476-2200 Fax: (760) 929-3941 See all of our", "domain": "viasat.com", "key": "b:0bd395a97cc23d6e", "name": "VIASAT INC", "website": "https://viasat.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, awcmanufacturing.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://awcmanufacturing.com/images/header-logo.png
- **logo_basis**: logo image in the site header
- **domain**: awcmanufacturing.com
- **key**: vendor:AWC MANUFACTURING LP
- **name**: AWC MANUFACTURING LP
- **website**: https://awcmanufacturing.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: AWC Manufacturing LP
- **jsonld_email**: info@awcmanufacturing.com
- **jsonld_url**: https://awcmanufacturing.com
- **jsonld_same_as**: https://ca.linkedin.com/company/awcmanufacturing
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "Organization", "name": "AWC Manufacturing LP", "url": "https://awcmanufacturing.com", "email": "info@awcmanufacturing.com", "sameAs": "https://ca.linkedin.com/company/awcmanufacturing", "department": { "@type": "LocalBusiness", "name": "AWC Manufacturing
- **jsonld_page**: https://awcmanufacturing.com/
- **linkedin_url**: https://ca.linkedin.com/company/awcmanufacturing
- **tel_links**: 5198220577; (519) 822-0577; (519) 272-0110; (519) 682-0470; (519) 805-2520

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "163 Curtis Drive, Guelph, ON, N1K1S9", "address_country": "CA", "address_url": "https://awcmanufacturing.com/contact-us", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: 163 Curtis Drive, Guelph, ON, N1K1S9", "phone": "+15198220577", "phone_url": "https://awcmanufacturing.com/contact-us", "emails": "info@awcmanufacturing.com", "emails_url": "https://awcmanufacturing.com/contact-us", "domain": "awcmanufacturing.com", "key": "vd:awcmanufacturing.com", "name": "AWC MANUFACTURING LP", "website": "https://awcmanufacturing.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | VIASAT INC | found | VIASAT, INC. | 859098378 | 6814191 | MB | EXTRA-PROVINCIAL - SHARE CORPORATION | Active | 2013-10-02 | CARISBAD | CA |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=VIASAT%20INC | 2026-11-08 |
| buyer | AWC MANUFACTURING LP | found | AWC MANUFACTURING LP |  | 241207406 | ON | LIMITED PARTNERSHIP ON | Active | 2014-12-22 | WINDSOR | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=AWC%20MANUFACTURING%20LP | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | VIASAT INC | Q7924358 | official website on the organisation's domain (http://viasat.com) + name |  | Viasat | ViaSat | business; telecommunications company; public company | Delaware corporation | United States | 1986-00-00 | Carlsbad |
| b | AWC MANUFACTURING LP |  |  |  |  |  |  |  |  |  |  |
| v | AWC MANUFACTURING LP |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:0bd395a97cc23d6e",
 "ap_contact_team": {
  "emails": [
   "ViasatAP@viasat.com",
   "ap@viasat.com",
   "supplierenablement@viasat.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "ViasatIncPR001076Rev050: invoice after goods delivery/service performance and reference PO. Unless PO says otherwise, net60 after later receipt of correct invoice or acceptance. Email AP unless written direction differs. Use designated supplier systems as Viasat directs.",
  "evidence": [
   {
    "email": "ViasatAP@viasat.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "ViasatIncPR001076Rev050: invoice after goods delivery/service performance and reference PO. Unless PO says otherwise, net60 after later receipt of correct invoice or acceptance. Email AP unless written direction differs. Use designated supplier systems as Viasat directs.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.viasat.com/content/dam/us-site/supplier/documents/PR001076_Rev050.pdf",
    "quote": "cable goods or services. Unless instructed otherwise by Viasat in writing, invoices shall be sent to Viasat via email at ViasatAP@viasat.com. d. Excluding any Seller that is a certified small business p",
    "retrieved_date": "2026-10-29",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch11.csv",
    "org": "VIASAT INC",
    "task_id": "CH-AP-01070",
    "verified_via": "referee saw it on this page on 2026-11-07; the page could not be read today (unverified_page_unavailable)"
   },
   {
    "email": "ap@viasat.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.viasat.com/content/dam/us-site/supplier/documents/ACH-Bank-Transfer-payment-methods-vs-%20ePayables-Credit-Card.pdf",
    "quote": "Enhanced reporting. Suppliers will receive enhanced remittance information for more efficient back-end reconciliation. Questions?  Contact ap@viasat.com for any questions.",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "VIASAT INC",
    "task_id": "CH-AP-01070"
   },
   {
    "email": "supplierenablement@viasat.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.viasat.com/content/dam/us-site/supplier/documents/Ariba_SLP_Supplier_FAQs.pdf",
    "quote": "ion, US Gov Reps & Certs, or Supplier Quality Survey, but it should be directed to a different point of contact. What do I do? Please email supplierenablement@viasat.com with the details on what form you are needing sent to a different contact, and the first name, last name, and email addr",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "VIASAT INC",
    "task_id": "CH-AP-01070"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site:viasat.com suppliers invoice accounts payable; opened current SupplierInformation/ToolsResources/TermsConditions, currentlinkedPR001076Rev050 and SupplierPacketAugust2023; indexedCoupaGuidev2returned404",
  "site crawl of www.viasat.com (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.viasat.com (25 pages, robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| usaspending:sub:CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732:4313484:D3KWRS9KT7U7 | usaspending | ongoing_inferred | FABRICATED METAL 332999 | 220800.0 | USD |  |  | {"subaward_number": "4313484", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sa | https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/ |
| usaspending:sub:CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732:4316727:D3KWRS9KT7U7 | usaspending | ongoing_inferred | HOUSING | 101124.0 | USD |  |  | {"subaward_number": "4316727", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sa | https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/ |
| usaspending:sub:CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732:4316728:D3KWRS9KT7U7 | usaspending | ongoing_inferred | LOAD FRAME | 30800.0 | USD |  |  | {"subaward_number": "4316728", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sa | https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/ |
| usaspending:sub:CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732:4318939:D3KWRS9KT7U7 | usaspending | ongoing_inferred | METAL FAB | 137760.0 | USD |  |  | {"subaward_number": "4318939", "prime_award_unique_key": "CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732", "prime_award_piid": "47QFLA25F0054", "prime_award_parent_piid": "47QFLA25D0001", "subaward_sa | https://www.usaspending.gov/award/CONT_AWD_47QFLA25F0054_4732_47QFLA25D0001_4732/ |

## The buyer's other Canadian-vendor records (first 60 of 1)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| private_press:db743f3c3a583d9f1a6fdcd6004f4c6b3dbdb41a | Telesat Corporation | Telesat secures substantial multi-year contract with Viasat for Telesat Lightspeed services |  |  |  | https://www.globenewswire.com/news-release/2025/04/07/3056644/0/en/telesat-secures-substantial-multi-year-contract-with-viasat-for-telesat-lightspeed-services.html |

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

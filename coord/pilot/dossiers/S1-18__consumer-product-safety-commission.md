# S1-18 — Consumer Product Safety Commission ⇄ PAGEFREEZER SOFTWARE INC

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC) — 441 G Street NW, Washington, DC 20548
SUBMIT TO: 9-amc-amz-cpsc-accounts-payable@faa.gov (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: PO 61320626F0050 (piid); contract 47QTCA18D00DD (parent_award_id_piid) | PO rule: purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE)
FROM / REMIT TO: PAGEFREEZER SOFTWARE INC. — 311 WATER ST SUITE 500, VANCOUVER, BC, V6B1B8 | GST/HST 839583267RT0001 (account derived from the BN9)
TAX: Tax Exemption (as printed on https://www.cpsc.gov/s3fs-public/pdfs/purchasecard2012.pdf, re-read 2026-11-08) | CURRENCY: USD | TERMS: Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)
DESCRIPTION: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. (first sentence of the record's description; t | AMOUNT: 28,875.00 USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Consumer Product Safety Commission (US government body (federal, state or local), US) — public contract / purchase award with a published end date (dated record): PAGEFREEZER SOFTWARE INC | subject: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. (first sentence of the record's description; the source publishes no separate title) | instrument: delivery order | PO / procurement number: 61320626F0050 (piid) | contract number: 47QTCA18D00DD (parent_award_id_piid); CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732 (contract_award_unique_key); 6100_4732_61320626F0050_0_47QTCA18D00DD_0 (lat | all identifiers: {"contract_award_unique_key": "CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732", "piid": "61320626F0050", "awarding_agency_code": "061", "awarding_sub_agency_code": "6100", "parent_award_id_piid": "47QTCA18D00DD", "parent_award_agency_id": "4732", "solicitation_identifier": null, "latest_contract_tra | value: 28875.0 USD | awarded 2026-08-12, start 2026-08-12, end 2027-09-14 | published by: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports) | record: https://www.usaspending.gov/award/CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732/ | vendor in Canada because: recipient_country_code == 'CAN' (FPDS LegalEntityCountryCode of the latest transaction; bulk download filtered on recipient_locations country=CAN) | status rule: active (published end date today or later) | this buyer has 1
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:c9ff0459dd27d806
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Consumer Product Safety Commission
- **buyer_website**: https://www.cpsc.gov
- **buyer_address**: 441 G Street NW, Washington, DC 20548
- **buyer_contact_evidence_url**: https://www.cpsc.gov/About-CPSC/Contact-Information
- **buyer_legal_name_as_published**: U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC)
- **buyer_logo_url**: https://www.cpsc.gov/sites/default/themes/cpsc/assets/images/freedom-250-logo-rgb-full-color.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/u.s.-consumer-product-safety-commission/
- **buyer_type**: US government body (federal, state or local)
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2995379; independent agency of the United States government
- **buyer_founded**: 1972-00-00 (Wikidata Q2995379, official website on the organisation's domain (http://www.cpsc.gov/) + name; 2026-11-08)
- **buyer_employees**: 500 (Wikidata Q2995379, official website on the organisation's domain (http://www.cpsc.gov/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.cpsc.gov/About-CPSC/Contact-Information (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: EFT banking information on the invoice only if required (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: Tax Exemption (as printed on https://www.cpsc.gov/s3fs-public/pdfs/purchasecard2012.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_org_codes**: 061 (awarding_agency_code); 4732 (parent_award_agency_id); 6100 (awarding_sub_agency_code)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: 9-amc-amz-cpsc-accounts-payable@faa.gov
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf
- **email_evidence_quote**: 25710 Oklahoma City, Ok. 73125 5 FEDEX CPSC Accounts Payable Branch, AMZ-160 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 OR Via email to: 9-AMC-AMZ-CPSC-Accounts-Payable@faa.gov Invoices not submitted in accordance with the above stated minimum requirements will not be processed for paym
- **email_evidence_context**: voice. ORIGll-.JAL VOUCHERS/INVOICES SHALL BE SENT TO: U.S. Mail CPSC Accounts Payable Branch, AMZ-160 PO Box 25710 Oklahoma City, Ok. 73125 5 FEDEX CPSC Accounts Payable Branch, AMZ-160 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 OR Via email to: 9-AMC-AMZ-CPSC-Accounts-Payable@faa.gov Invoices not submitted in accordance with the above stated minimum requirements will not be processed for payment. Deficient invoices will be returned to the vendor within seven days or sooner. Standard forms 1034 and 1035 will be furnished by CPSC (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: 9-amc-amz-cpsc-accounts-payable@faa.gov (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf | quote: "25710 Oklahoma City, Ok. 73125 5 FEDEX CPSC Accounts Payable Branch, AMZ-160 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 OR Via email to: 9-AMC-AMZ-CPSC-Accou" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (amcrelay1.faa.gov) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00111
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (amcrelay1.faa.gov)
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc_agg@valigov.email,mailto:9-AIF-340-DMARC-REPORTS@faa.gov,mailto:reports@dmarc.cyber.dhs.gov; ruf=mailto:9-AIF-340-DMARC-REPORTS@faa.gov
- **dmarc_record_domain**: faa.gov
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:faa.gov._nspf.valigov.email include:%{i}._ip.%{h}._ehlo.%{d}._spf.valigov.email ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC) — 441 G Street NW, Washington, DC 20548 ⏎ SUBMIT TO: 9-amc-amz-cpsc-accounts-payable@faa.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: PO 61320626F0050 (piid); contract 47QTCA18D00DD (parent_award_id_piid) | PO rule: purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) ⏎ FROM / REMIT TO: PAGEFREEZER SOFTWARE INC. — 311 WATER ST SUITE 500, VANCOUVER, BC, V6B1B8 | GST/HST 839583267RT0001 (account derived from the BN9) ⏎ TAX: Tax Exemption (as printed on https://www.cpsc.gov/s3fs-public/pdfs/purchasecard2012.pdf, re-read 2026-11-08) | CURRENCY: USD | TERMS: Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08) ⏎ DESCRIPTION: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. (first sentence of the record's description; t | AMOUNT: 28,875.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC)", "legal_name_is_published": true, "address": "441 G Street NW, Washington, DC 20548", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "9-amc-amz-cpsc-accounts-payable@faa.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "po_number": "61320626F0050 (piid)", "contract_or_agreement_number": "47QTCA18D00DD (parent_award_id_piid); CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732 (contract_award_unique_key); 6100_4732_61320626F0050_0_47QTCA18D00DD_0 (latest_contract_transaction_unique_key)", "vendor_id_with_buyer": "", "reference_hint": "purchase order / procurement number: 61320626F0050 (piid) — source usaspending"}, "terms": {"payment_terms": "Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "payment_method": "EFT banking information on the invoice only if required (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "payment_
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **po_number_as_published**: 61320626F0050 (piid)
- **invoice_reference_hint**: purchase order / procurement number: 61320626F0050 (piid) — source usaspending

## Vendor
- **vendor**: PAGEFREEZER SOFTWARE INC
- **vendor_legal_name**: PAGEFREEZER SOFTWARE INC.
- **vendor_registry_id**: BC OrgBook (BC registration): BC0865911
- **vendor_registry_url**: https://orgbook.gov.bc.ca/entity/BC0865911
- **vendor_legal_form**: BC company (home jurisdiction BC)
- **vendor_address**: 311 WATER ST SUITE 500, VANCOUVER, BC, V6B1B8
- **vendor_country_basis**: recipient_country_code == 'CAN' (FPDS LegalEntityCountryCode of the latest transaction; bulk download filtered on recipient_locations country=CAN)
- **vendor_bn9**: 839583267
- **vendor_gst_hst_derived**: 839583267RT0001
- **vendor_website**: https://www.pagefreezer.com/
- **vendor_emails**: info@pagefreezer.com; sales@pagefreezer.com; support@pagefreezer.com
- **vendor_phone**: +1-888-916-3999
- **vendor_contact_evidence_url**: https://www.pagefreezer.com/contact-us/
- **vendor_logo_url**: https://www.pagefreezer.com/wp-content/uploads/Pagefreezer-Logo-WEB.webp
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.pagefreezer.com/ (Pagefreezer Digital Archiving Software Solutions Compliance Government FOIA & Open Records Financial Services eDiscovery eDiscovery & Litigation Legal Hold & Re)
- **vendor_facts_provenance**: name and address: the record's vendor block (USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports)); registry identity: BC OrgBook (BC registration): BC0865911 status BC OrgBook (BC registration): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; strong); BN9: bc_orgbook BC0865911 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2009-11-10; phone / role e-mails / logo: the vendor's own site, https://www.pagefreezer.com/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.pagefreezer.com/
- **vendor_concentration_top_share**: PAGEFREEZER SOFTWARE INC: 100% of 1 records
- **vendor_registry_status**: BC OrgBook (BC registration): Active
- **vendor_registry_match_level**: strong
- **vendor_incorporation_date**: 2009-11-10
- **vendor_years_in_business**: 17.0 (since 2009-11-10, registry date)
- **vendor_bn_source**: bc_orgbook BC0865911 (strong match)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"contract_award_unique_key": "CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732", "piid": "61320626F0050", "awarding_agency_code": "061", "awarding_sub_agency_code": "6100", "parent_award_id_piid": "47QTCA18D00DD", "parent_award_agency_id": "4732", "solicitation_identifier": null, "latest_contract_transaction_unique_key": "6100_4732_61320626F0050_0_47QTCA18D00DD_0", "latest_modification_number": "0", "transaction_unique_keys": ["6100_4732_61320626F0050_0_47QTCA18D00DD_0"], "modification_numbers": ["0"]}
- **contract_title**: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. (first sentence of the record's description; the source publishes no separate title)
- **contract_description**: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS.
- **po_number_as_published**: 61320626F0050 (piid)
- **contract_or_agreement_number**: 47QTCA18D00DD (parent_award_id_piid); CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732 (contract_award_unique_key); 6100_4732_61320626F0050_0_47QTCA18D00DD_0 (latest_contract_transaction_unique_key)
- **commodity_codes**: NAICS 511210 (SOFTWARE PUBLISHERS); PSC 7A21 (IT AND TELECOM - BUSINESS APPLICATION SOFTWARE (PERPETUAL LICENSE SOFTWARE))
- **contract_value**: 28875.0
- **currency**: USD
- **award_date**: 2026-08-12
- **start_date**: 2026-08-12
- **end_date**: 2027-09-14
- **contract_link**: https://www.usaspending.gov/award/CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732/
- **source**: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports)
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS subaward reports) (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 839583267RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC) — 441 G Street NW, Washington, DC 20548 ⏎ SUBMIT TO: 9-amc-amz-cpsc-accounts-payable@faa.gov (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: PO 61320626F0050 (piid); contract 47QTCA18D00DD (parent_award_id_piid) | PO rule: purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) ⏎ FROM / REMIT TO: PAGEFREEZER SOFTWARE INC. — 311 WATER ST SUITE 500, VANCOUVER, BC, V6B1B8 | GST/HST 839583267RT0001 (account derived from the BN9) ⏎ TAX: Tax Exemption (as printed on https://www.cpsc.gov/s3fs-public/pdfs/purchasecard2012.pdf, re-read 2026-11-08) | CURRENCY: USD | TERMS: Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08) ⏎ DESCRIPTION: RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. (first sentence of the record's description; t | AMOUNT: 28,875.00 USD
- **invoice_card_json**: {"bill_to": {"legal_name": "U.S. Consumer Product Safety Commission (stated on https://www.cpsc.gov/About-CPSC)", "legal_name_is_published": true, "address": "441 G Street NW, Washington, DC 20548", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "9-amc-amz-cpsc-accounts-payable@faa.gov", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "po_number": "61320626F0050 (piid)", "contract_or_agreement_number": "47QTCA18D00DD (parent_award_id_piid); CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732 (contract_award_unique_key); 6100_4732_61320626F0050_0_47QTCA18D00DD_0 (latest_contract_transaction_unique_key)", "vendor_id_with_buyer": "", "reference_hint": "purchase order / procurement number: 61320626F0050 (piid) — source usaspending"}, "terms": {"payment_terms": "Net 30 (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "payment_method": "EFT banking information on the invoice only if required (as printed on https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf, re-read 2026-11-08)", "payment_
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; payment cycle or method published (plausibility) | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["9-amc-amz-cpsc-accounts-payable@faa.gov (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf", "quote: \"25710 Oklahoma City, Ok. 73125 5 FEDEX CPSC Accounts Payable Branch, AMZ-160 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 OR Via email to: 9-AMC-AMZ-CPSC-Accou\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by self-hosted or other (amcrelay1.faa.gov)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00111"], "buyer_facts": ["address and phone: the buyer's own site, https://www.cpsc.gov/About-CPSC/Contact-Information (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (USAspending.gov Custom Award Data Download (FPDS prime contract transactions + SAM.gov/FSRS su

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf | 2026-11-08 | ok | Net 30 | purchase-order terms published (as published: PURCHASE ORDER INCORPORATES BY REFERENCE) |  |  |  |  |  | STANDMD BETHESDA MD 20814 SMALl8U$INESS 1! DeUV[!RY FOR Foa CEsnNA~ 12, DISCOUNT TERMS T!ON UNLESS aLOCK is [ ] 130. THIS CONTRACT IS A MARKED Net 30 RATED ORDER UNDER 14. METhOD OF SOuClTAr;ON o SEE SCHEDULE DPAS {1S(;F | BY Kt:..t"",NCE FAR 52.212-1,52212-4. FAR 52212-3 AND 52 212-5 ARE ATTACHED ADDENDA CJ ARE C ARE NOT ATTACHED. 'J 27b. CONTRACTIPURCHASE ORDER INCORPORATES BY REFERENCE FAR 52.212-4, FAR 52.212-5 IS ATTACHED. ADDENDA n A |

## Buyer site facts (org_extras, cpsc.gov)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.cpsc.gov/sites/default/themes/cpsc/assets/images/freedom-250-logo-rgb-full-color.png
- **logo_basis**: logo image in the site header
- **domain**: cpsc.gov
- **key**: b:c9ff0459dd27d806
- **name**: Consumer Product Safety Commission
- **website**: https://cpsc.gov/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: U.S. Consumer Product Safety Commission
- **legal_name_stated_url**: https://www.cpsc.gov/About-CPSC
- **legal_name_stated_quote**: pment of safe products. Acting Chairman Peter A. Feldman Peter A. Feldman is Acting Chairman of the U.S. Consumer Product Safety Commission (CPSC). Learn More CPSC Commissioners Biographies and contact information for CPSC’s Commissioners.
- **linkedin_url**: https://www.linkedin.com/company/u.s.-consumer-product-safety-commission/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "441 G Street NW, Washington, DC 20548", "address_country": "US", "address_url": "https://www.cpsc.gov/About-CPSC/Contact-Information", "address_method": "pattern", "address_quote": "nization Chart Locations Washington, DC U.S. Consumer Product Safety Commission 441 G Street NW Washington, DC 20548 Rockville National Product Testing and Evaluation Center 5", "domain": "cpsc.gov", "key": "b:c9ff0459dd27d806", "name": "Consumer Product Safety Commission", "website": "https://cpsc.gov/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, pagefreezer.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Pagefreezer Software Inc
- **legal_name_url**: https://www.pagefreezer.com/
- **legal_name_quote**: t targeted Industry news, great tips and valuable insights Follow Follow Follow Follow Follow ©2026 Pagefreezer Software Inc. All Rights Reserved. Privacy Policy and Acceptable Use Policy . Commercial use and distribution of
- **logo_url**: https://www.pagefreezer.com/wp-content/uploads/Pagefreezer-Logo-WEB.webp
- **logo_basis**: logo image in the site header
- **domain**: pagefreezer.com
- **key**: wd:Q20712307
- **name**: PageFreezer
- **website**: https://pagefreezer.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Pagefreezer
- **jsonld_logo**: https://www.pagefreezer.com/wp-content/uploads/Pagefreezer-Logo-black.png
- **jsonld_url**: https://www.pagefreezer.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.pagefreezer.com\/","url":"https:\/\/www.pagefreezer.com\/","name":"Pagefreezer Digital Archiving Software","isPartOf":{"@id":"https:\/\/www.pagefreezer.com\/#website"},"about":{"@id":"https:\/\/www.pagefreezer.com\/
- **jsonld_page**: https://www.pagefreezer.com/
- **legal_name_stated**: Sprott Shaw College
- **legal_name_stated_url**: https://www.pagefreezer.com/ediscovery-litigation-readiness/
- **legal_name_stated_quote**: us with protection from litigation that involves online content. ” – Scott Elliot, Web Strategist, Sprott Shaw College Real-Time Collection and Preservation Collect and preserve websites, social media, mobile text mess
- **mentions**: {'esignature': {'text': 'digital signatures and metadata ensuring authenticity and complete records', 'url': 'https://www.pagefreezer.com/', 'quote': 'terprise solutions capture internal chat records and complex websites. All content is captured with digital signatures and metadata ensuring authenticity and complete records. How does Pagefreezer help organizations maintain evidence? Pagefreezer’s WebPreserve'}}
- **linkedin_url**: https://www.linkedin.com/company/pagefreezer-software-inc-
- **tel_links**: 1-888-916-3999

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "408-55 Water Street – Unit 8327, Vancouver, BC V6B1A1", "address_country": "CA", "address_url": "https://www.pagefreezer.com/contact-us/", "address_method": "pattern", "address_quote": "t@pagefreezer.com Mailing Address 408-55 Water Street – Unit 8327 Vancouver, BC V6B1A1 Canada Europe Office: Van Leeuwenhoekpark 1 – Office 5 2611 DW, Delft Netherlan", "phone": "+1-888-916-3999", "phone_url": "https://www.pagefreezer.com/contact-us/", "emails": "info@pagefreezer.com; sales@pagefreezer.com; support@pagefreezer.com", "emails_url": "https://www.pagefreezer.com/contact-us/", "domain": "pagefreezer.com", "key": "wd:Q20712307", "name": "PageFreezer", "website": "https://pagefreezer.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Consumer Product Safety Commission | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Consumer%20Product%20Safety%20Commission | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Consumer Product Safety Commission | Q2995379 | official website on the organisation's domain (http://www.cpsc.gov/) + name |  | United States Consumer Product Safety Commission | La commission de la sécurité des produits des consommateurs des États-Unis | independent agency of the United States government |  | United States | 1972-00-00 | Bethesda |
| b | PageFreezer | Q20712307 | official website on the organisation's domain (http://www.pagefreezer.com) + name |  | PageFreezer |  | website; business |  | Canada | 2009-11-09 | Vancouver |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:c9ff0459dd27d806",
 "ap_contact_team": {
  "emails": [
   "9-amc-amz-cpsc-accounts-payable@faa.gov",
   "9-amc-amz-cpsc-accounts-payable@fas.gov"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "9-amc-amz-cpsc-accounts-payable@faa.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-12-0059.pdf",
    "quote": "25710 Oklahoma City, Ok. 73125 5 FEDEX CPSC Accounts Payable Branch, AMZ-160 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 OR Via email to: 9-AMC-AMZ-CPSC-Accounts-Payable@faa.gov Invoices not submitted in accordance with the above stated minimum requirements will not be processed for paym",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Consumer Product Safety Commission",
    "task_id": "CL-WS-00111"
   },
   {
    "email": "9-amc-amz-cpsc-accounts-payable@fas.gov",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cpsc.gov/s3fs-public/pdfs/CPSC-S-11-0053.pdf",
    "quote": "5710 Oklahoma City, Ok. 73125 FEDEX CPSC Accounts Payable Branch, AMZ-I60 6500 MacArthur Blvd. Oklahoma City, Ok. 73169 11 OR Via email to: 9-AMC-AMZ-CPSC-Accounts-Payable@fas.gov Invoices not submitted in accordance with the above stated minimum requirements will not be processed for paym",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Consumer Product Safety Commission",
    "task_id": "CL-WS-00111"
   }
  ]
 },
 "research_status": {
  "found": 2,
  "not_published": 1
 },
 "queries_tried": [
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "site:cpsc.gov \"invoices\" OR \"accounts payable\" email OR IPP; browsed official contact forms"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| usaspending:CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732 | usaspending | ongoing | RENEW WEBPRESERVER ONLINE EVIDENCE CAPTURE PLATFORM WITH UNLIMITED DEVICES AND PRESERVATIONS. | 28875.0 | USD |  |  | {"contract_award_unique_key": "CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732", "piid": "61320626F0050", "awarding_agency_code": "061", "awarding_sub_agency_code": "6100", "parent_award_id_piid": "47Q | https://www.usaspending.gov/award/CONT_AWD_61320626F0050_6100_47QTCA18D00DD_4732/ |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 10)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:jus:4500157732 | Department of Justice Canada | LICENSE/MAINTENANCE FEES FOR CLIENT SOFTWARE | 24781.61 |  |  | https://search.open.canada.ca/contracts/record/jus,C-2025-2026-Q4-00140 |
| us_state_ny_abo:d84c-dk28:bd20dc7c58aadb8a | New York City Economic Development Corporation | Repairs & Maintenance - Computer |  |  |  | https://data.ny.gov/d/d84c-dk28 |
| usaspending:CONT_AWD_2032H826P00007_2050_-NONE-_-NONE- | Department of the Treasury | THIS CONTRACT IS TO PROVIDE SOCIAL MEDIA ARCHIVING SERVICES IN THE FORM OF A SOFTWARE AS A SERVICE. THIS CONTRACT IS FOR A ONE-YEAR BASE PERIOD AND FOUR ONE-YEA | 4513.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_2032H826P00007_2050_-NONE-_-NONE-/ |
| usaspending:CONT_AWD_29FTC126P0006_2900_-NONE-_-NONE- | Federal Trade Commission | WEBPRESERVER TEAM EDITION - ONLINE EVIDENCE CAPTURE PLATFORM | 18375.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_29FTC126P0006_2900_-NONE-_-NONE-/ |
| usaspending:CONT_AWD_50310223F0147_5000_47QTCA18D00DD_4732 | Securities and Exchange Commission | WEBPRESERVER PROFESSIONAL EDITION - EVIDENCE CAPTURE PLATFORM ANNUAL SUBSCRIPTION | 59996.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_50310223F0147_5000_47QTCA18D00DD_4732/ |
| usaspending:CONT_AWD_7571TE26F80071_7571_47QTCA18D00DD_4732 | Department of Health and Human Services | WEB AND SOCIAL MEDIA ARCHIVING SUPPORT SERVICES | 552713.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_7571TE26F80071_7571_47QTCA18D00DD_4732/ |
| usaspending:CONT_AWD_91990024F0074_9100_47QTCA18D00DD_4732 | Department of Education | WEB ARCHIVE TOOL | 459000.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_91990024F0074_9100_47QTCA18D00DD_4732/ |
| usaspending:CONT_IDV_47QTCA18D00DD_4732 | General Services Administration | FEDERAL SUPPLY SCHEDULE CONTRACT | 600000.0 |  |  | https://www.usaspending.gov/award/CONT_IDV_47QTCA18D00DD_4732/ |
| ny_procurement_d84c-dk28:_new_york_city_economic_development_corporation_pagefreezer_software,_inc._21 | New York City Economic Development Corporation | Repairs & Maintenance - Computer |  |  |  | https://data.ny.gov/dataset/d84c-dk28 |
| us_ny_state_authorities_procurement:68bae641ee107b95 | New York City Economic Development Corporation | Repairs & Maintenance - Computer |  |  |  | https://data.ny.gov/dataset/Procurement-Report-for-Local-Development-Corporations/d84c-dk28 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S1-09 — Wright State University ⇄ QUEENS UNIVERSITY AT KINGSTON

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Pioneer Path University (stated on https://www.wright.edu/about) — Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435
SUBMIT TO: accounts_payable@wright.edu (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the univer
FROM / REMIT TO: QUEENS UNIVERSITY AT KINGSTON — 99 UNVERSITY AVENUE, KINGSTON, ON, K7L 3N6, CAN | GST/HST 107868705 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-11-07; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: tax exemption (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: Net 30
DESCRIPTION: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY. | AMOUNT: 48556.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 93
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Wright State University (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): QUEENS UNIVERSITY AT KINGSTON | subject: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY. | all identifiers: {"internal_id": "671904-1", "prime_award_internal_id": "270319955", "Sub-Award ID": "671904-1", "Prime Award ID": "R21HD112763", "prime_award_generated_internal_id": "ASST_NON_R21HD112763_075"} | value: 48556.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2025-11-18 | published by: subawardee country | record: https://www.usaspending.gov/award/R21HD112763 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:bf038e2257ebb4d0
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: Wright State University
- **buyer_website**: http://www.wright.edu
- **buyer_address**: 3640 Colonel Glenn Hwy., Dayton, OH 45435
- **buyer_phone**: 937-775-1000
- **buyer_contact_evidence_url**: https://www.wright.edu/about
- **buyer_legal_name_as_published**: Pioneer Path University (stated on https://www.wright.edu/about)
- **buyer_logo_url**: https://www.wright.edu/themes/custom/wsu_base/dist/components/03-features/brand/logos/biplane_white.png
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2002085; public research university; public educational institution of the United States
- **buyer_founded**: 1964-00-00 (Wikidata Q2002085, official website on the organisation's domain (http://www.wright.edu) + name; 2026-11-08)
- **buyer_employees**: 1945 (Wikidata Q2002085, official website on the organisation's domain (http://www.wright.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.wright.edu/about (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf); invoicing requirements: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf); payment terms: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Form (PDF) Employee Direct Deposit Form (PDF) (campus username and password required) IRS Mile (as printed on https://www.wright.edu/financial-operations/controller/accounts-payable, re-read 2026-11-08)
- **buyer_tax_exempt_status**: tax exemption (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts_payable@wright.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf
- **email_evidence_quote**: line along with Seller’s name and invoice number, to: accounts_payable@wright.edu.
- **mailbox_provenance**: accounts_payable@wright.edu (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08 | page: https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf | quote: "line along with Seller’s name and invoice number, to: accounts_payable@wright.edu." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch51.csv task CH-AP-51009
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;sp=none;aspf=r;adkim=r;rua=mailto:dmarc_agg@vali.email;
- **dmarc_record_domain**: wright.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:130.108.66.0/24 ip4:130.108.128.0/24 ip4:216.68.250.2 ip4:75.101.161.27 ip4:54.166.123.167 ip4:34.236.72.193 ip4:44.194.182.36 include:secure.giftlegacy.com  include:_tuf-spf.touchnet.com include:_spf.qualtrics.com include:a._spf.brightspace.com include:spf.protection.outlook.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435
- **invoicing_requirements**: Email invoices with PO number, seller name and invoice number in the subject. Match the PO line by line. Paper invoices go to Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435. Net 30 from the latest of receipt/completion, invoice receipt, o
- **payment_terms_as_published**: Net 30
- **po_required_as_published**: purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the university shall) (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "Net 30", "po_required": "purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the university shall) (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)", "mailing_address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435", "requirements_text": "Email invoices with PO number, seller name and invoice number in the subject. Match the PO line by line. Paper invoices go to Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435. Net 30 from the latest of receipt/completion, invoice receipt, o"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pioneer Path University (stated on https://www.wright.edu/about) — Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435 ⏎ SUBMIT TO: accounts_payable@wright.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the univer ⏎ FROM / REMIT TO: QUEENS UNIVERSITY AT KINGSTON — 99 UNVERSITY AVENUE, KINGSTON, ON, K7L 3N6, CAN | GST/HST 107868705 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-11-07; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: tax exemption (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: Net 30 ⏎ DESCRIPTION: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY. | AMOUNT: 48556.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Pioneer Path University (stated on https://www.wright.edu/about)", "legal_name_is_published": true, "address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts_payable@wright.edu", "email_type": "invoicing/AP", "supplier_setup_url": "https://www.wright.edu/user/login?destination=system/files/uploads/2023/02/page_restricted/direct-deposit-authorization.pdf", "portal_url": "", "portal_kind": "", "mailing_address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the university shall) (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 671904-1 (internal_id) — source usaspending"}, "terms": {"payment_terms": "Net 30", "payment_method": "Form (PDF) Employee Direct Deposit Form (PDF) (campus username and password required) IRS Mile (as printed on https://www.wright.edu/financial-operations/control
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor legal name
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **supplier_setup_url**: https://www.wright.edu/user/login?destination=system/files/uploads/2023/02/page_restricted/direct-deposit-authorization.pdf (linked as "Employee Direct Deposit Form (PDF)" (as printed on https://www.wright.edu/financial-operations/controller/accounts-payable, re-read 2026-11-08))
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: award or notice id: 671904-1 (internal_id) — source usaspending

## Vendor
- **vendor**: QUEENS UNIVERSITY AT KINGSTON
- **vendor_address**: 99 UNVERSITY AVENUE, KINGSTON, ON, K7L 3N6, CAN
- **vendor_country_basis**: subawardee country=CAN
- **vendor_bn9**: 107868705 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-11-07; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 107868705RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.queensu.ca/
- **vendor_contact_evidence_url**: https://ctg.queensu.ca/public/contact-us
- **vendor_logo_url**: https://www.queensu.ca/resources/assets/logos/Queens-logo-reversed.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.queensu.ca/ (Queen’s University Canada Skip to main content Skip to navigation Skip to footer Frequently Searched Undergraduate Admission Human Resources Library Student Aff)
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://ctg.queensu.ca/public/contact-us (tools/org_contacts.py, org_extras.py); website: https://www.queensu.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the university shall) (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "671904-1", "prime_award_internal_id": "270319955", "Sub-Award ID": "671904-1", "Prime Award ID": "R21HD112763", "prime_award_generated_internal_id": "ASST_NON_R21HD112763_075"}
- **contract_title**: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY.
- **contract_description**: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY. (the record's title; the source publishes no separate description)
- **award_or_notice_id**: 671904-1 (internal_id); 671904-1 (Sub-Award ID); R21HD112763 (Prime Award ID); 270319955 (prime_award_internal_id); ASST_NON_R21HD112763_075 (prime_award_generated_internal_id)
- **contract_value**: 48556.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2025-11-18
- **contract_link**: https://www.usaspending.gov/award/R21HD112763
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **vendor_gst_hst_derived**: 107868705RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Pioneer Path University (stated on https://www.wright.edu/about) — Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435 ⏎ SUBMIT TO: accounts_payable@wright.edu (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the univer ⏎ FROM / REMIT TO: QUEENS UNIVERSITY AT KINGSTON — 99 UNVERSITY AVENUE, KINGSTON, ON, K7L 3N6, CAN | GST/HST 107868705 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-11-07; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: tax exemption (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: Net 30 ⏎ DESCRIPTION: OVERSEE THE ASSESSMENT AND EVALUATION OF MOUSE PLACENTAL HISTOLOGY RESULTING FROM EXPERIMENTS CONDUCTED AT WRIGHT STATE UNIVERSITY. | AMOUNT: 48556.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Pioneer Path University (stated on https://www.wright.edu/about)", "legal_name_is_published": true, "address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts_payable@wright.edu", "email_type": "invoicing/AP", "supplier_setup_url": "https://www.wright.edu/user/login?destination=system/files/uploads/2023/02/page_restricted/direct-deposit-authorization.pdf", "portal_url": "", "portal_kind": "", "mailing_address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase orders for their departments with vendors on behalf of the university shall) (as printed on https://policy.wright.edu/policy/9320-purchasing-external-vendors, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "award or notice id: 671904-1 (internal_id) — source usaspending"}, "terms": {"payment_terms": "Net 30", "payment_method": "Form (PDF) Employee Direct Deposit Form (PDF) (campus username and password required) IRS Mile (as printed on https://www.wright.edu/financial-operations/control
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor legal name
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accounts_payable@wright.edu (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08", "page: https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf", "quote: \"line along with Seller’s name and invoice number, to: accounts_payable@wright.edu.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch51.csv task CH-AP-51009"], "buyer_facts": ["address and phone: the buyer's own site, https://www.wright.edu/about (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf)", "invoicing requirements: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf)", "payment terms: the lane's AP page (https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf)", "PO requirement: t

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.wright.edu/financial-operations/procurement-and-contract-services/wrightbuy | 2026-11-08 | ok |  | purchase-order terms published (as published: needed to an existing purchase order) |  |  |  |  |  |  | require several payments over a period of time. Change Order Request Form: Use this form when a change (increase or decrease) is needed to an existing purchase order. eDPO Form: Use this form for revenue and general ledg |
| https://www.wright.edu/financial-operations/procurement-and-contract-services/bid-notices | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, wright.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.wright.edu/themes/custom/wsu_base/dist/components/03-features/brand/logos/biplane_white.png
- **logo_basis**: logo image on the site
- **domain**: wright.edu
- **key**: lead:bf038e2257ebb4d0
- **name**: Wright State University
- **website**: https://wright.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Pioneer Path University
- **legal_name_stated_url**: https://www.wright.edu/about
- **legal_name_stated_quote**: list. More Rankings Admissions Employment Alumni Who we are Right Here. Right Now. Wright State. - Pioneer Path University Mega Footer First Column Colleges & Schools Business, Raj Soin College of Engineering and Computer
- **tel_links**: +19377751000

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "3640 Colonel Glenn Hwy., Dayton, OH 45435", "address_country": "US", "address_url": "https://www.wright.edu/about", "address_method": "pattern", "address_quote": "r A-Z Index Apply Employment Make a Gift Wright State Cares Contact Information 3640 Colonel Glenn Hwy. Dayton, OH 45435 USA 937-775-1000 Facebook Instagram LinkedIn TikTok YouTube Co", "phone": "937-775-1000", "phone_url": "https://www.wright.edu/about", "domain": "wright.edu", "key": "lead:bf038e2257ebb4d0", "name": "Wright State University", "website": "https://wright.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, queensu.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Queen’s University
- **legal_name_url**: https://sdm.queensu.ca/
- **legal_name_quote**: tact Forms Room Booking Footer Menu 2 Queen's Library The Isabel The Tett Centre Donate Web Privacy Queen’s University is situated on the territory of the Haudenosaunee and Anishinaabek . © 2026 Queen’s University
- **logo_url**: https://www.queensu.ca/resources/assets/logos/Queens-logo-reversed.svg
- **logo_basis**: logo image on the site
- **domain**: queensu.ca
- **key**: lead:85dbcd43724ef16d
- **name**: DAN School of Drama and Music
- **website**: https://sdm.queensu.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Accessible & Inclusive Music Theatre
- **legal_name_stated_url**: https://sdm.queensu.ca/about/facilities
- **legal_name_stated_quote**: on Window Displays Research Faculty Research Centre for Spectatorship and Audience Research RENOMAD Accessible & Inclusive Music Theatre (AIMT) Student Research FOLDA Pandemic Preparedness Secondary School Arts Enrolment Report Performa
- **mentions**: {'payment_method': {'text': 'interactions, and liberal arts and a practical education', 'url': 'https://sdm.queensu.ca/', 'quote': 'p skills. We aim to balance structure and flexibility, disciplinary knowledge and interdisciplinary interactions, and liberal arts and a practical education. Students can specialize in a range of areas and engage in a variety of hands-on and practical lear'}}
- **linkedin_url**: https://www.linkedin.com/company/dan-school-of-drama-and-music/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "10 Stuart Street, Kingston, Ontario, K7L 3N6", "address_country": "CA", "address_url": "https://ctg.queensu.ca/public/contact-us", "address_method": "pattern", "address_quote": "an Cancer Trials Group Queen's University, 10 Stuart Street, Kingston, Ontario, K7L 3N6 (613) 533-6430 (613) 533-2941 (613) 533-2411 CCTG Contact List ( requires passw", "domain": "queensu.ca", "key": "vd:queensu.ca", "name": "National Cancer Institute of Canada Clinical Trials Group", "website": "https://ctg.queensu.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Wright State University | Q2002085 | official website on the organisation's domain (http://www.wright.edu) + name |  | Wright State University | Université d'État Wright | public research university; public educational institution of the United States |  | United States | 1964-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:bf038e2257ebb4d0",
 "ap_contact_team": {
  "emails": [
   "accounts_payable@wright.edu",
   "purchasing@wright.edu",
   "coi-procurement@wright.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435",
  "invoicing_requirements": "Email invoices with PO number, seller name and invoice number in the subject. Match the PO line by line. Paper invoices go to Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435. Net 30 from the latest of receipt/completion, invoice receipt, or installation/acceptance. Payment can be by card, ACH or check. The AP page also links an invoice submission form.",
  "evidence": [
   {
    "email": "accounts_payable@wright.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": "Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435",
    "requirements": "Email invoices with PO number, seller name and invoice number in the subject. Match the PO line by line. Paper invoices go to Wright State University, c/o Accounts Payable, 3640 Colonel Glenn Hwy, 300 University Hall, Dayton, OH 45435. Net 30 from the latest of receipt/completion, invoice receipt, or installation/acceptance. Payment can be by card, ACH or check. The AP page also links an invoice submission form.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf",
    "quote": "line along with Seller’s name and invoice number, to: accounts_payable@wright.edu.",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch51.csv",
    "org": "Wright State University",
    "task_id": "CH-AP-51009"
   },
   {
    "email": "accounts_payable@wright.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf",
    "quote": "ces may also be sent electronically, referencing its purchase order number in subject line along with Seller’s name and invoice number, to: accounts_payable@wright.edu. 1.7 Payment. Purchaser payment terms are NET30 days, to be calculated from: (1) the date the goods are received or the se",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Wright State University",
    "task_id": "CL-WS-00146"
   },
   {
    "email": "purchasing@wright.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/financial-operations/procurement-and-contract-services/wrightbuy",
    "quote": "can access the requisition, update it, and resubmit. Order Status and Order Cancellation How do I cancel a purchase order? Send an email to purchasing@wright.edu explaining the reason for canceling the purchase order. Purchasing will cancel the order in WrightBuy and in Banner. Purchasing",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Wright State University",
    "task_id": "CL-SQ-01025"
   },
   {
    "email": "purchasing@wright.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/financial-operations/procurement-and-contract-services/wrightbuy",
    "quote": "can access the requisition, update it, and resubmit. Order Status and Order Cancellation How do I cancel a purchase order? Send an email to purchasing@wright.edu explaining the reason for canceling the purchase order. Purchasing will cancel the order in WrightBuy and in Banner. Purchasing",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Wright State University",
    "task_id": "CL-WS-00014"
   },
   {
    "email": "coi-procurement@wright.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf",
    "quote": "to be sent to the Purchaser’s Procurement and Contract Services office at 3640 Colonel Glenn Hwy, 300 University Hall Dayton, Ohio 45435 or coi-procurement@wright.edu. Each certificate required by this contract must be in effect at or prior to commencement of work under this contract and r",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Wright State University",
    "task_id": "CL-WS-00146"
   },
   {
    "email": "purchasing@wright.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wright.edu/sites/www.wright.edu/files/page/attachments/procurement-terms-and-conditions.pdf",
    "quote": "reasonably amend its notice address(es) upon written notice to the other party. All such notices shall also be sent via electronic mail to purchasing@wright.edu. 5.4 Assignments; Subcontract
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 2)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| usaspending:CONT_AWD_W912HQ26CA021_9700_-NONE-_-NONE- | Department of Defense | SERDP PROJECT FOR RESEARCH AND DEVELOPMENT | 1431968.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_W912HQ26CA021_9700_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:an:PW-21-00980105 | Public Works and Government Services Canada | Product/Material - Design, Development, Formulation, Modification: Science and Technology Related (R&D) (CW2229078)(W7714-228155) | 1148855.28 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-21-00980105 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

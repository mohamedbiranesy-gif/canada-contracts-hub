# S5-25 — Carcross/ Tagish First Nation ⇄ Acera Insurance Services

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Carcross/ Tagish First Nation — 130 Carcross, YT Y0B 1B0
SUBMIT TO: accountspayable@ctfn.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://ctfn.bidsandtenders.ca/ — bids&tenders
REFERENCE: contract RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFP2026006FIN (bid_number) | PO rule: yes (as published: purchase orders or cheque requis)
FROM / REMIT TO: Acera Insurance Services — 201-9016 Quartz Road, Whitehorse, YT, Y1A 2Z5 | GST/HST number not public
TAX: status Indians, non-status Indians or native people, as the case may be (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagi | CURRENCY: CAD | TERMS: 90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcro
DESCRIPTION: Insurance Brokerage Services
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 2
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Carcross/ Tagish First Nation (First Nation / Indigenous government, CA) — public contract / purchase award in the last 12 months (dated record): Acera Insurance Services | subject: Insurance Brokerage Services | instrument: contract | contract number: RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract referenc | solicitation: RFP2026006FIN (bid_number) | all identifiers: {"bid_number": "RFP2026006FIN", "bidsandtenders_tender_id": "346f9af9-eacf-4957-a362-516f84dc58ec", "portal": "ctfn.bidsandtenders.ca", "submission_name": "Submission 1"} | awarded 2025-11-20 | published by: bids&tenders (eSolutions) public procurement portals - awarded bids | record: https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/346f9af9-eacf-4957-a362-516f84dc58ec | vendor in Canada because: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published) | status rule: likely active (awarded in the last 12 months, no end date published) | this buyer has 4 records with Canada-located vendors (4 distinct vendors; 2 in the last 12 months; latest 2025-11-20)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:528c64842afa4e7b
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Carcross/ Tagish First Nation
- **buyer_website**: https://ctfn.ca
- **buyer_address**: 130 Carcross, YT Y0B 1B0
- **buyer_phone**: 867-821-4251
- **buyer_contact_evidence_url**: https://www.ctfn.ca/contact-us
- **buyer_logo_url**: https://www.ctfn.ca/assets/layout/logo-ctfn.png
- **buyer_type**: First Nation / Indigenous government
- **buyer_sector**: government: provincial / federal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.ctfn.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); logo: og:image / logo image of the buyer's site; AP phone: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf); invoicing requirements: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: required before the next cheque run and not processing the cheque (as printed on https://www.ctfn.ca/media/documents/Financial_Policy_Feb_7th__2021.pdf, re-read 2026-11-08)
- **buyer_tax_exempt_status**: status Indians, non-status Indians or native people, as the case may be (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagish-Final_Agreement.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: provincial government entity in Yukon: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@ctfn.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf
- **email_evidence_quote**: Accounts Payable 8245 accountspayable@ctfn.ca
- **email_evidence_context**: Officer (CFO) 8209 1-867-332-5547 kristine.hildebrand@ctfn.ca Andy Tran Accounts Payable Supervisor 8205 andy.tran@ctfn.ca Jat Petal Finance Administrator 8028 Jay.petal@ctfn.ca Tinashe Chisandure Finance Clerk 8214 Karen Hall Accounts Payable 8245 accountspayable@ctfn.ca Matthias Liniger Senior Finance Manager 8218 1-867-332-3824 matthias.liniger@ctfn.ca Mike Baerg Senior Financial Analyst 8247 mike.baerg@ctfn.ca Kiryl Vrubleuski I.T. Manager 8001 1-867-334-3927 helpdesk@ctfn.ca Allen Mendez I.T. Technician helpdesk (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@ctfn.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-07 | page: https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf | quote: "Accounts Payable 8245 accountspayable@ctfn.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Titan / Hostinger | lane file: chatgpt/chatgpt_buyer_ap_results_batch12.csv task CH-AP-01159
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Titan / Hostinger
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none
- **dmarc_record_domain**: ctfn.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 mx a:mail.ctfn.ca include:mailgun.org ip4:199.85.226.10 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Mike Baerg Senior (Senior Finance Manager) (as printed by the organisation on its own accounts-payable page (as printed on https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf, re-read 2026-11-08))
- **ap_phone**: 867-821-4251 ext. 8245
- **invoicing_requirements**: Published financial policy: AP matches invoices/receipts with authorized purchase orders or cheque requisitions; discrepancies return for correction/authorization. Finance seeks original invoice when a photocopy/fax was paid. Cheques released on 15th and 30th. No universal submission route stated.
- **payment_terms_as_published**: 90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagish-FinalAgreementImplementationPlan.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: purchase orders or cheque requis)
- **invoice_portal_url**: https://ctfn.bidsandtenders.ca/ — bids&tenders
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: bids&tenders (as printed on https://www.ctfn.ca/departments/finance-and-human-resources/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagish-FinalAgreementImplementationPlan.pdf, re-read 2026-11-08)", "po_required": "yes (as published: purchase orders or cheque requis)", "portal_url": "https://ctfn.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "867-821-4251 ext. 8245", "requirements_text": "Published financial policy: AP matches invoices/receipts with authorized purchase orders or cheque requisitions; discrepancies return for correction/authorization. Finance seeks original invoice when a photocopy/fax was paid. Cheques released on 15th and 30th. No universal submission route stated."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Carcross/ Tagish First Nation — 130 Carcross, YT Y0B 1B0 ⏎ SUBMIT TO: accountspayable@ctfn.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://ctfn.bidsandtenders.ca/ — bids&tenders ⏎ REFERENCE: contract RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFP2026006FIN (bid_number) | PO rule: yes (as published: purchase orders or cheque requis) ⏎ FROM / REMIT TO: Acera Insurance Services — 201-9016 Quartz Road, Whitehorse, YT, Y1A 2Z5 | GST/HST number not public ⏎ TAX: status Indians, non-status Indians or native people, as the case may be (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagi | CURRENCY: CAD | TERMS: 90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcro ⏎ DESCRIPTION: Insurance Brokerage Services
- **invoice_card_json**: {"bill_to": {"legal_name": "Carcross/ Tagish First Nation", "legal_name_is_published": false, "address": "130 Carcross, YT Y0B 1B0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@ctfn.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://ctfn.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.ctfn.ca/departments/finance-and-human-resources/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: purchase orders or cheque requis)", "po_number": "", "contract_or_agreement_number": "RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bidsandtenders"}, "terms": {"payment_terms": "90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagish-FinalAgreementImpleme
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bidsandtenders

## Vendor
- **vendor**: Acera Insurance Services
- **vendor_address**: 201-9016 Quartz Road, Whitehorse, YT, Y1A 2Z5
- **vendor_country_basis**: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published)
- **vendor_website**: https://acera.ca/
- **vendor_phone**: 1.800.670.1877
- **vendor_contact_evidence_url**: https://acera.ca/contact/
- **vendor_logo_url**: https://acera.ca/wp-content/uploads/2023/12/acera-logo.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://acera.ca/ (Acera Insurance | Personal Insurance for Canadians Skip to content Effective November 1, 2026, Acera will now be doing business as Navacord. Service, policies a)
- **vendor_facts_provenance**: name and address: the record's vendor block (bids&tenders (eSolutions) public procurement portals - awarded bids); phone / role e-mails / logo: the vendor's own site, https://acera.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://acera.ca/
- **vendor_concentration_top_share**: Acera Insurance Services: 25% of 4 records
- **vendor_registry_match_level**: weak_candidates_only

## Contract
- **po_required_as_published**: yes (as published: purchase orders or cheque requis)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"bid_number": "RFP2026006FIN", "bidsandtenders_tender_id": "346f9af9-eacf-4957-a362-516f84dc58ec", "portal": "ctfn.bidsandtenders.ca", "submission_name": "Submission 1"}
- **contract_title**: Insurance Brokerage Services
- **contract_description**: C/TFN is seeking a qualified Insurance Broker to provide risk management and advisory services and represent C/TFN to the commercial insurance market to obtain insurance coverage that best covers C/TFN’s risks at the most competitive rate.
- **number_of_bids**: 2
- **contract_or_agreement_number**: RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: RFP2026006FIN (bid_number)
- **award_or_notice_id**: 346f9af9-eacf-4957-a362-516f84dc58ec (bidsandtenders_tender_id) — notice id; the award is published within this notice, the source assigns no separate award id
- **currency**: CAD
- **award_date**: 2025-11-20
- **contract_link**: https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/346f9af9-eacf-4957-a362-516f84dc58ec
- **source**: bids&tenders (eSolutions) public procurement portals - awarded bids
- **contracts_with_canadian_suppliers**: 4
- **records_last_12_months**: 2
- **record_sources**: bids&tenders (eSolutions) public procurement portals - awarded bids (4)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 4 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: provincial government entity in Yukon: a LISTED entity does not pay GST/HST at the point of purchase when an authorized official certifies the purchase — ask for the exemption certificate or certification clause before invoicing without tax — GST/HST Memorandum 18-2 para. 24 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Listed entities in Manitoba, Saskatchewan, Alberta, the Northwest Territories and Yukon do not pay the GST/HST on purchases of taxable property and services, provided that an authorized official of the listed entity provides sufficient evidence"); derived from buyer type and province, not published by the buyer; whether this body is a listed entity is not verified
- **tax_rate_indicative_derived**: GST 5% (YT) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Carcross/ Tagish First Nation — 130 Carcross, YT Y0B 1B0 ⏎ SUBMIT TO: accountspayable@ctfn.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://ctfn.bidsandtenders.ca/ — bids&tenders ⏎ REFERENCE: contract RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender RFP2026006FIN (bid_number) | PO rule: yes (as published: purchase orders or cheque requis) ⏎ FROM / REMIT TO: Acera Insurance Services — 201-9016 Quartz Road, Whitehorse, YT, Y1A 2Z5 | GST/HST number not public ⏎ TAX: status Indians, non-status Indians or native people, as the case may be (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagi | CURRENCY: CAD | TERMS: 90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcro ⏎ DESCRIPTION: Insurance Brokerage Services
- **invoice_card_json**: {"bill_to": {"legal_name": "Carcross/ Tagish First Nation", "legal_name_is_published": false, "address": "130 Carcross, YT Y0B 1B0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@ctfn.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://ctfn.bidsandtenders.ca/ — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: bids&tenders (as printed on https://www.ctfn.ca/departments/finance-and-human-resources/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: purchase orders or cheque requis)", "po_number": "", "contract_or_agreement_number": "RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: RFP2026006FIN (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bidsandtenders"}, "terms": {"payment_terms": "90 days of receipt (as printed on https://www.ctfn.ca/media/documents/Publications/Agreements/carcross-tagish-FinalAgreementImpleme
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: bill-to legal name (published); vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | missing: finance mailbox; bill-to legal name published | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published bill-to legal name
- **ap_payability**: not yet payable — missing: bill-to legal name and address
- **facts_provenance_json**: {"mailbox": ["accountspayable@ctfn.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-07", "page: https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf", "quote: \"Accounts Payable 8245 accountspayable@ctfn.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Titan / Hostinger", "lane file: chatgpt/chatgpt_buyer_ap_results_batch12.csv task CH-AP-01159"], "buyer_facts": ["address and phone: the buyer's own site, https://www.ctfn.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "logo: og:image / logo image of the buyer's site", "AP phone: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf)", "invoicing requirements: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the lane's AP page (https://www.ctfn.ca/media/documents/Departments/Finance_Human_Res

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf | 2026-11-08 | ok |  |  |  | 1-867-332-5547 |  |  |  |  |  |

## Buyer site facts (org_extras, ctfn.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.ctfn.ca/assets/layout/logo-ctfn.png
- **logo_basis**: logo image in the site header
- **domain**: ctfn.ca
- **key**: b:528c64842afa4e7b
- **name**: Carcross/ Tagish First Nation
- **website**: https://ctfn.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Canada's Anti-Spam Legislation
- **legal_name_stated_url**: https://www.ctfn.ca/privacy-policy/
- **legal_name_stated_quote**: maintain personal information for market research or marketing purposes. This is in accordance with Canada's Anti-Spam Legislation (CASL). Privacy Policy Quick Access Working Together Facebook Twitter Instagram Services Links Gall
- **portals**: [{'name': 'bids&tenders', 'kind': 'e-tendering', 'url': 'https://ctfn.bidsandtenders.ca/', 'on_page': 'https://www.ctfn.ca/'}]

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "130 Carcross, YT Y0B 1B0", "address_country": "CA", "address_url": "https://www.ctfn.ca/contact-us", "address_method": "pattern", "address_quote": "us We want to hear from you! Carcross/Tagish First Nation Box 130 Carcross, YT Y0B 1B0 P: (867) 821-4251 F: (867) 821-4802 Toll Free: (855) 686-4251 Download our phon", "phone": "867-821-4251", "phone_url": "https://www.ctfn.ca/haa-shagoon-hidi/contact", "domain": "ctfn.ca", "key": "b:528c64842afa4e7b", "name": "Carcross/ Tagish First Nation", "website": "https://ctfn.ca/", "kind": "buyer", "date": "2026-11-08"}

## Vendor site facts (org_extras, acera.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Acera Insurance Services Ltd
- **legal_name_url**: https://acera.ca/
- **legal_name_quote**: erage Quick Links Strata Certificate Request Follow Us Facebook LinkedIn Instagram Copyright © 2026 Acera Insurance Services Ltd. , All Rights Reserved. Developed by Twirling Umbrellas Terms of Use Cookie Policy Privacy Policy S
- **logo_url**: https://acera.ca/wp-content/uploads/2023/12/acera-logo.png
- **logo_basis**: logo image on the site
- **domain**: acera.ca
- **key**: vendor:Acera Insurance Services
- **name**: Acera Insurance Services
- **website**: https://acera.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Acera Insurance Services Ltd
- **legal_name_stated_url**: https://acera.ca/terms/
- **legal_name_stated_quote**: n which it is accessed, including (without limitation), Canada. General This website is provided by Acera Insurance Services Ltd. Some of the information available on this website has been provided by other companies. Separate t
- **linkedin_url**: https://www.linkedin.com/company/acera-insurance/
- **tel_links**: 1-8006701877; 18006701877; 18885955212; 18005658132; 3062704432; 18774325118; 9023341320; 18884132149
- **tel_links_url**: https://acera.ca/terms/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "phone": "1.800.670.1877", "phone_url": "https://acera.ca/contact/", "domain": "acera.ca", "key": "lead:83de4db02793deb8", "name": "acera.ca", "website": "https://acera.ca/", "kind": "buyer", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Carcross/ Tagish First Nation |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:528c64842afa4e7b",
 "ap_contact_team": {
  "emails": [
   "accountspayable@ctfn.ca",
   "reception@ctfn.ca"
  ],
  "invoice_portal": null,
  "phone": "867-821-4251 ext. 8245",
  "mailing_address": null,
  "invoicing_requirements": "Published financial policy: AP matches invoices/receipts with authorized purchase orders or cheque requisitions; discrepancies return for correction/authorization. Finance seeks original invoice when a photocopy/fax was paid. Cheques released on 15th and 30th. No universal submission route stated.",
  "evidence": [
   {
    "email": "accountspayable@ctfn.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": "867-821-4251 ext. 8245",
    "mailing_address": null,
    "requirements": "Published financial policy: AP matches invoices/receipts with authorized purchase orders or cheque requisitions; discrepancies return for correction/authorization. Finance seeks original invoice when a photocopy/fax was paid. Cheques released on 15th and 30th. No universal submission route stated.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.ctfn.ca/media/documents/Departments/Finance_Human_Resources/CA_-_DOC-0038_-_01.00_-_Staff_Directory_-_2026-03-27_-_M.pdf",
    "quote": "Accounts Payable 8245 accountspayable@ctfn.ca",
    "retrieved_date": "2026-11-07",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch12.csv",
    "org": "Carcross/ Tagish First Nation",
    "task_id": "CH-AP-01159"
   },
   {
    "email": "accountspayable@ctfn.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ctfn.ca/media/documents/2026_August_Updated_Staff_Directory.pdf",
    "quote": "Karen Hall Accounts Payable 8245 accountspayable@ctfn.ca Shelley Whelan Accounts Receivable 8244",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Carcross/ Tagish First Nation",
    "task_id": "CL-WS-00082"
   },
   {
    "email": "reception@ctfn.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.ctfn.ca/media/documents/2026_August_Updated_Staff_Directory.pdf",
    "quote": "Mierl Richard Reception 8241 1-867-335-2136 reception@ctfn.ca Adri Lera Councils Clerk 8224",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Carcross/ Tagish First Nation",
    "task_id": "CL-WS-00082"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "Carcross Tagish First Nation finance accounts payable invoices email",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_bidsandtenders:346f9af9-eacf-4957-a362-516f84dc58ec:1 | ca_bidsandtenders | end_date_unknown | Insurance Brokerage Services |  | CAD |  |  | {"bid_number": "RFP2026006FIN", "bidsandtenders_tender_id": "346f9af9-eacf-4957-a362-516f84dc58ec", "portal": "ctfn.bidsandtenders.ca", "submission_name": "Submission 1"} | https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/346f9af9-eacf-4957-a362-516f84dc58ec |

## The buyer's other Canadian-vendor records (first 60 of 3)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:71fe1239-3434-40e3-a5ff-6499b4621c9f:1 | Blastek Engineering Group | Safety Management Plan |  |  |  | https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/71fe1239-3434-40e3-a5ff-6499b4621c9f |
| ca_bidsandtenders:d70657e2-efeb-4302-8e99-34b099950829:1 | BLDG Sci Advisory Inc. | Asset Condition Inspections | 88478.0 |  |  | https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d70657e2-efeb-4302-8e99-34b099950829 |
| ca_bidsandtenders:e127ee75-6b90-49e0-a8f2-8c8ea17fa6e3:1 | Stratford Managers | Job Classification Services | 34000.0 |  |  | https://ctfn.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e127ee75-6b90-49e0-a8f2-8c8ea17fa6e3 |

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

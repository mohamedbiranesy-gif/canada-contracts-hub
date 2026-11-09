# S1-11 — Toronto District School Board ⇄ Softchoice Canada Corp

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Toronto District School Board — Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8 — buyer tax no. 895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name)
SUBMIT TO: apinvoices@tdsb.on.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders | format: Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)
REFERENCE: contract BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender BM26-278P (bid_number) | PO rule: yes (as published: Purchase Order Number clearly indicated on the invoice or must)
FROM / REMIT TO: SOFTCHOICE LP — 116 Albert St Suite 201, Ottawa, ON, K1P 5G3 | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461
TAX: DERIVED: taxable purchaser presumed (no exe
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 14
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Toronto District School Board (school board / school district, CA) — public contract / purchase award in the last 12 months (dated record): Softchoice Canada Corp | subject: Cisco Email Security Service | instrument: contract | contract number: BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference | solicitation: BM26-278P (bid_number) | all identifiers: {"bid_number": "BM26-278P", "bidsandtenders_tender_id": "505f529e-b841-4e0f-b17d-d365c0b0f2d6", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"} | value: 250000.00 (as printed in the buyer's own council / committee report or minutes: https://www.tdsb.on.ca/Leadership/Boardroom/Agenda-Minutes/Type/A?Folder=Agenda%2F20200122&Filename=5.2.pdf, read 2026-11-08: "service to schools and centres. Agenda Page 38 APPENDIX C Contracts Requiring Board Approval (contracts over $250,000 and Consulting Services over $50,000) Projected Low Bid/ # of Estimated User/Budge") CAD | awarded 2026-06-01 | published by: bids&tenders (eSolutions) public procurement portals - awarded bids | record: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/505f529e-b841-4e0f-b17d-d365c0b0f2d6 | vendor in Canada because: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published) | status rule: likely active (awarded in the last 12 months, no end date published) | this bu
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:fda131e15c76fe84
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 4

## Buyer
- **buyer**: Toronto District School Board
- **buyer_website**: http://www.tdsb.on.ca
- **buyer_address**: 5050 Yonge St, Toronto, ON, M2N5N8, CA
- **buyer_phone**: 1-866-921-6714
- **buyer_contact_evidence_url**: https://www.tdsb.on.ca/About-Us/Accessibility/Contact
- **buyer_legal_name_as_published**: Toronto District School Board
- **buyer_bn_as_published**: 895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 895788222RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.tdsb.on.ca/images/TDSB/TDSB_Print_Logo.gif
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/toronto-district-school-board
- **buyer_supplier_portals_linked**: bids&tenders (e-tendering): https://tdsb.bidsandtenders.ca/Module/Tenders/en
- **buyer_type**: school board / school district
- **buyer_sector**: education: K-12
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1189302; academic institution; school district of Canada; charitable organization
- **buyer_budget_or_revenue**: revenue 2197243247 Q1104069; 2220616669 Q1104069; 2433387769 Q1104069; 2480371147 Q1104069; 2465815193 Q1104069; 2536448694 Q110 (Wikidata Q1189302, official website on the organisation's domain (http://www.tdsb.on.ca/) + name; 2026-11-08)
- **buyer_employees**: 37800; 35650; 35657; 36689; 36235; 36850; 5292; 53416; 46066; 45725; 42500; 40172; 42556; 40530; 38647; 36602; 37239; 36 (Wikidata Q1189302, official website on the organisation's domain (http://www.tdsb.on.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.tdsb.on.ca/About-Us/Accessibility/Contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the lane's AP page (https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the lane's AP page (https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: direct deposit system (electronic funds transfer) as the only (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: apinvoices@tdsb.on.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d
- **email_evidence_quote**: nt defects. Billing Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Number clearly indicated on the invoice or must be submitted in writing directly to: Accounts Payable, 5050 Yonge S
- **email_evidence_context**: nce of any Goods/Services delivered or performed hereunder. Acceptance shall not relieve the successful Bidder of its warranty obligations or liability for latent defects. Billing Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Number clearly indicated on the invoice or must be submitted in writing directly to: Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON, M2N 5N8. Hand written invoices will not be accepted and will (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: apinvoices@tdsb.on.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-26 | page: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d | quote: "nt defects. Billing Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Numbe" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF without an all mechanism; mail handled by Cisco | lane file: chatgpt/chatgpt_buyer_ap_results_batch01.csv task CH-AP-00011
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF without an all mechanism; mail handled by Cisco
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:17feab9856ab644@rep.ca.mimecastdmarcanalyzer.com
- **dmarc_record_domain**: tdsb.on.ca
- **spf_policy**: SPF without an all mechanism
- **spf_record**: v=spf1 redirect=8wui6wtr._spf._d.mim.ec
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8
- **invoicing_requirements**: Individual PDF invoices; clearly state PO number; no handwritten invoices; taxes shown separately. | invoice format as published: Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)
- **payment_terms_as_published**: 90 days after receipt (as printed on https://www.tdsb.on.ca/Portals/0/AboutUs/Business%20Services/Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: Purchase Order Number clearly indicated on the invoice or must)
- **invoice_portal_url**: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: bids&tenders (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08); linked from the buyer's site: bids&tenders (e-tendering)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "90 days after receipt (as printed on https://www.tdsb.on.ca/Portals/0/AboutUs/Business%20Services/Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)", "po_required": "yes (as published: Purchase Order Number clearly indicated on the invoice or must)", "portal_url": "https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)", "mailing_address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8", "requirements_text": "Individual PDF invoices; clearly state PO number; no handwritten invoices; taxes shown separately. | invoice format as published: Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Toronto District School Board — Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8 — buyer tax no. 895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name) ⏎ SUBMIT TO: apinvoices@tdsb.on.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders | format: Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08) ⏎ REFERENCE: contract BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender BM26-278P (bid_number) | PO rule: yes (as published: Purchase Order Number clearly indicated on the invoice or must) ⏎ FROM / REMIT TO: SOFTCHOICE LP — 116 Albert St Suite 201, Ottawa, ON, K1P 5G3 | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461 ⏎ TAX: DERIVED: taxable purchaser presum
- **invoice_card_json**: {"bill_to": {"legal_name": "Toronto District School Board", "legal_name_is_published": true, "address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8", "address_is_the_invoice_address": true, "tax_number": "895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name)", "language": "en"}, "submit_to": {"email": "apinvoices@tdsb.on.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8", "format": "Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)", "system": "named on the buyer's page: bids&tenders (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08); linked from the buyer's site: bids&tenders (e-tendering)", "e_invoicing_peppol": "", "portal_is_invoice_channel":
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference — source ca_bidsandtenders

## Vendor
- **vendor**: Softchoice Canada Corp
- **vendor_legal_name**: SOFTCHOICE LP
- **vendor_trading_name**: Softchoice Canada Corp
- **vendor_registry_id**: Québec REQ (NEQ): 3369689461; corporation number 11065742 (Corporations Canada (open data))
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 173 Dufferin Street, Suite 200, Toronto, ON, M6K 3H7, CA
- **vendor_neq**: 3369689461 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société non constituée au Québec
- **vendor_activity_code**: CAE 5999 — Service d'informatique / solution technologique et fournisseur de services
- **vendor_employees_quebec**: De 50 à 99
- **vendor_establishments_quebec**: SOFTCHOICE (TMA394232): 3201-1751 rue Richardson, Montréal (Québec), H3K1G6; SOFTCHOICE (TMA394232): 380-1751 rue du Marais, Québec (Québec), G1M0A2
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2019-12-31
- **vendor_address**: 116 Albert St Suite 201, Ottawa, ON, K1P 5G3
- **vendor_country_basis**: bids&tenders 'Awarded' vendor table field 'Country' = 'Canada' (with ProvinceState/City/PostalCode as published)
- **vendor_bn9**: 124209297
- **vendor_gst_hst_derived**: 124209297RT0001
- **vendor_website**: https://www.softchoice.com
- **vendor_logo_url**: https://www.softchoice.com/assets/img/logos/softchoice-logo-new.svg
- **vendor_contacts_found_by**:  lane, referee-verified on 
- **vendor_facts_provenance**: name and address: the record's vendor block (bids&tenders (eSolutions) public procurement portals - awarded bids); registry identity: Québec REQ (NEQ): 3369689461; corporation number 11065742 (Corporations Canada (open data)) status Québec REQ (NEQ): Immatriculée (2013-12-13); Corporations Canada (corporation number): Inactive (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 11816110 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2013-11-21; role / billing mailboxes researched by the  lane, referee-verified on ; website: https://www.softchoice.com; NEQ: 3369689461 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: The BearStar Group Inc.: 2% of 2014 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2013-12-13); Corporations Canada (corporation number): Inactive
- **vendor_registry_note**: another registry lists a lapsed registration (Corporations Canada (corporation number): Inactive); the primary record is alive
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2013-11-21
- **vendor_years_in_business**: 13.0 (since 2013-11-21, registry date)
- **vendor_bn_source**: corporations_canada 11816110 (strong match)

## Contract
- **po_required_as_published**: yes (as published: Purchase Order Number clearly indicated on the invoice or must)
- **contract_status**: likely active (awarded in the last 12 months, no end date published)
- **contract_reference**: {"bid_number": "BM26-278P", "bidsandtenders_tender_id": "505f529e-b841-4e0f-b17d-d365c0b0f2d6", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"}
- **contract_title**: Cisco Email Security Service
- **contract_description**: The Toronto District School Board (TDSB) is requesting pricing for one and three-year subscription terms from Canadian based Cisco reseller partners for the products and quantities outlined herein.
- **number_of_bids**: 7 (as printed in the buyer's own council / committee report or minutes: https://www.tdsb.on.ca/Leadership/Boardroom/Agenda-Minutes/Type/A?Folder=Agenda%2F20200122&Filename=5.2.pdf, read 2026-11-08: "ety of enterprise software products, in addition to providing related acquisition and administrative support. Seven proposals were received. Softchoice Canada Inc. scored the highest and was the prefe")
- **contract_or_agreement_number**: BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: BM26-278P (bid_number)
- **award_or_notice_id**: 505f529e-b841-4e0f-b17d-d365c0b0f2d6 (bidsandtenders_tender_id) — notice id; the award is published within this notice, the source assigns no separate award id
- **contract_value**: 250000.00 (as printed in the buyer's own council / committee report or minutes: https://www.tdsb.on.ca/Leadership/Boardroom/Agenda-Minutes/Type/A?Folder=Agenda%2F20200122&Filename=5.2.pdf, read 2026-11-08: "service to schools and centres. Agenda Page 38 APPENDIX C Contracts Requiring Board Approval (contracts over $250,000 and Consulting Services over $50,000) Projected Low Bid/ # of Estimated User/Budge")
- **currency**: CAD
- **award_date**: 2026-06-01
- **contract_link**: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/505f529e-b841-4e0f-b17d-d365c0b0f2d6
- **source**: bids&tenders (eSolutions) public procurement portals - awarded bids
- **contracts_with_canadian_suppliers**: 2014
- **records_last_12_months**: 316
- **record_sources**: bids&tenders (eSolutions) public procurement portals - awarded bids (2014)
- **records_with_this_vendor**: 4
- **records_in_contract_dataset**: 2014 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 895788222RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 124209297RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Toronto District School Board — Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8 — buyer tax no. 895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name) ⏎ SUBMIT TO: apinvoices@tdsb.on.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders | format: Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08) ⏎ REFERENCE: contract BM26-278P (bid_number) — the source publishes the award under this tender / notice number and no separate contract number; tender BM26-278P (bid_number) | PO rule: yes (as published: Purchase Order Number clearly indicated on the invoice or must) ⏎ FROM / REMIT TO: SOFTCHOICE LP — 116 Albert St Suite 201, Ottawa, ON, K1P 5G3 | GST/HST 124209297RT0001 (account derived from the BN9) | NEQ 3369689461 ⏎ TAX: DERIVED: taxable purchaser presum
- **invoice_card_json**: {"bill_to": {"legal_name": "Toronto District School Board", "legal_name_is_published": true, "address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8", "address_is_the_invoice_address": true, "tax_number": "895788222RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (tdsb.on.ca) + name)", "language": "en"}, "submit_to": {"email": "apinvoices@tdsb.on.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d — bids&tenders", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8", "format": "Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08)", "system": "named on the buyer's page: bids&tenders (as printed on https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d, re-read 2026-11-08); linked from the buyer's site: bids&tenders (e-tendering)", "e_invoicing_peppol": "", "portal_is_invoice_channel":
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 88
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; AP phone or AP contact
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["apinvoices@tdsb.on.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-26", "page: https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d", "quote: \"nt defects. Billing Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Numbe\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF without an all mechanism; mail handled by Cisco", "lane file: chatgpt/chatgpt_buyer_ap_results_batch01.csv task CH-AP-00011"], "buyer_facts": ["address and phone: the buyer's own site, https://www.tdsb.on.ca/About-Us/Accessibility/Contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the lane's AP page (https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: th

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d | 2026-11-08 | ok |  | yes (as published: Purchase Order Number clearly indicated on the invoice or must) | bids&tenders |  |  | Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb |  |  | must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Number clearly indicated on the invoice or must be submitted in writing directly to: Accounts  |

## Buyer site facts (org_extras, tdsb.on.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Toronto District School Board
- **legal_name_url**: https://www.tdsb.on.ca/
- **legal_name_quote**: Toronto District School Board --> Skip to main content Go to... New to Canada | Policies About Us | Staff | Careers Translate Go
- **logo_url**: https://www.tdsb.on.ca/images/TDSB/TDSB_Print_Logo.gif
- **logo_basis**: logo image in the site header
- **domain**: tdsb.on.ca
- **key**: b:fda131e15c76fe84
- **name**: Toronto District School Board
- **website**: https://tdsb.on.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: About Us Our Students The Toronto District School Board
- **legal_name_stated_url**: https://www.tdsb.on.ca/About-Us
- **legal_name_stated_quote**: g Respect at the TDSB PowerSchool Cyber Incident Reporting of Suspected Wrongdoing (Whistleblowing) About Us Our Students The Toronto District School Board (TDSB) is the largest and one of the most diverse school boards in Canada. We serve approximately 2
- **portals**: [{'name': 'bids&tenders', 'kind': 'e-tendering', 'url': 'https://tdsb.bidsandtenders.ca/Module/Tenders/en', 'on_page': 'https://www.tdsb.on.ca/About-Us'}]
- **mentions**: {'payment_method': {'text': 'Interacting with a Person with a Service Animal Interacting with a Person who has a Sup', 'url': 'https://www.tdsb.on.ca/About-Us', 'quote': 'ies Intellectual or Developmental Disabilities Learning Disabilities Speech or Language Impairments Interacting with a Person with a Service Animal Interacting with a Person who has a Support Person Information and Communications Service Disruptions Assistive'}}
- **linkedin_url**: https://www.linkedin.com/company/toronto-district-school-board

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "5050 Yonge Street - 5th Floor, Toronto, ON M2N 5N8", "address_country": "CA", "address_url": "https://www.tdsb.on.ca/About-Us/Accessibility/Contact", "address_method": "pattern", "address_quote": "Address Toronto District School Board 5050 Yonge Street - 5th Floor Toronto, ON M2N 5N8 Telephone: (416) 397-2401 Barrier Identification at TDSB Please fill out the Ba", "phone": "1-866-921-6714", "phone_url": "https://www.tdsb.on.ca/Contact-Us/Reporting-of-Suspected-Wrongdoing", "domain": "tdsb.on.ca", "key": "b:fda131e15c76fe84", "name": "Toronto District School Board", "website": "https://tdsb.on.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, softchoice.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.softchoice.com/assets/img/logos/softchoice-logo-new.svg
- **logo_basis**: logo image in the site header
- **domain**: softchoice.com
- **key**: vendor:Softchoice Canada Corp
- **name**: Softchoice Canada Corp
- **website**: https://softchoice.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Toronto District School Board | Q1189302 | official website on the organisation's domain (http://www.tdsb.on.ca/) + name |  | Toronto District School Board | Conseil scolaire du district de Toronto | academic institution; school district of Canada; charitable organization |  | Canada |  | Toronto |
| v | SOFTCHOICE LP |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:fda131e15c76fe84",
 "ap_contact_team": {
  "emails": [
   "apinvoices@tdsb.on.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8",
  "invoicing_requirements": "Individual PDF invoices; clearly state PO number; no handwritten invoices; taxes shown separately.",
  "evidence": [
   {
    "email": "apinvoices@tdsb.on.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": "Accounts Payable, 5050 Yonge Street, 3rd Floor, Toronto, ON M2N 5N8",
    "requirements": "Individual PDF invoices; clearly state PO number; no handwritten invoices; taxes shown separately.",
    "applies_to": "whole_organisation",
    "page_url": "https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95cbbc0f-3515-4d0f-9eef-710ae6047d2d",
    "quote": "nt defects. Billing Invoices must be e-mailed in PDF format individually to this address: apinvoices@tdsb.on.ca (preferred method) with the Purchase Order Number clearly indicated on the invoice or must be submitted in writing directly to: Accounts Payable, 5050 Yonge S",
    "retrieved_date": "2026-10-26",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch01.csv",
    "org": "Toronto District School Board",
    "task_id": "CH-AP-00011"
   },
   {
    "email": "apinvoices@tdsb.on.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.tdsb.on.ca/Portals/0/docs/Fundraising-Vendors-Directory.pdf",
    "quote": ". After services are rendered, the school will release the purchase on SAP. 5. Vendor will submit a detailed invoice to Accounts Payable at apinvoices@tdsb.on.ca including the PO#. If the vendor sets up an E-funds Transfer, payment will be deposited directly into the vendor's bank account.",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Toronto District School Board",
    "task_id": "CL-WS-00267"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "\"Toronto District School Board\" \"invoice\" \"accounts payable\"",
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
| ca_bidsandtenders:505f529e-b841-4e0f-b17d-d365c0b0f2d6:1 | ca_bidsandtenders | end_date_unknown | Cisco Email Security Service |  | CAD |  |  | {"bid_number": "BM26-278P", "bidsandtenders_tender_id": "505f529e-b841-4e0f-b17d-d365c0b0f2d6", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"} | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/505f529e-b841-4e0f-b17d-d365c0b0f2d6 |
| ca_bidsandtenders:3a2adc39-922c-43eb-be47-7354a3de0f35:1 | ca_bidsandtenders | end_date_unknown | GoAnywhere Licensing |  | CAD |  |  | {"bid_number": "AS23-696P", "bidsandtenders_tender_id": "3a2adc39-922c-43eb-be47-7354a3de0f35", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"} | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3a2adc39-922c-43eb-be47-7354a3de0f35 |
| ca_bidsandtenders:c023a4bc-4c24-481b-942f-af2b13ec61cc:2 | ca_bidsandtenders | end_date_unknown | ServiceNow Governance Risk & Compliance |  | CAD |  |  | {"bid_number": "AS21-546P", "bidsandtenders_tender_id": "c023a4bc-4c24-481b-942f-af2b13ec61cc", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"} | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c023a4bc-4c24-481b-942f-af2b13ec61cc |
| ca_bidsandtenders:56ecd9ed-fe43-4702-9eaf-47254020afdf:1 | ca_bidsandtenders | end_date_unknown | Splunk |  | CAD |  |  | {"bid_number": "AS21-123P", "bidsandtenders_tender_id": "56ecd9ed-fe43-4702-9eaf-47254020afdf", "portal": "tdsb.bidsandtenders.ca", "submission_name": "Submission 1"} | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/56ecd9ed-fe43-4702-9eaf-47254020afdf |

## The buyer's other Canadian-vendor records (first 60 of 300)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:c1747345-f2ef-48ce-b7b4-c04468caef7a:1 | F. Greco & Sons Ltd | Phase 2 - Heydon Park Relocation to VRA at Vaughan Road Academy / Heydon Park Secondary School |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c1747345-f2ef-48ce-b7b4-c04468caef7a |
| ca_bidsandtenders:d406998a-f9e7-47d2-85d4-87b67cc7ab86:1 | Zencorp Mechanical Inc. | Heating Plant Replacement at Humberside CI TR-25-0391 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d406998a-f9e7-47d2-85d4-87b67cc7ab86 |
| ca_bidsandtenders:295fa6ef-d82e-44b2-9962-ad1b9d54b171:1 | Cordeiro Roofing Ltd. | Roof replacement (areas A, A2, D6, E6, G) at Vaughan Road Academy - TR-26-0176 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/295fa6ef-d82e-44b2-9962-ad1b9d54b171 |
| ca_bidsandtenders:9854b9ca-5e3a-40df-bfbf-f8d9af547078:1 | RCN Electric | B/F Lift Replacement at Heydon Park S.S. TR-26-0325 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9854b9ca-5e3a-40df-bfbf-f8d9af547078 |
| ca_bidsandtenders:cb6ca6f1-c181-445d-8f6d-4c4a8ce16041:1 | Etude Architects Inc. | Professional Services, Orde Childcare Centre Accommodation at Contact Alternative School - TR-26-0600 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cb6ca6f1-c181-445d-8f6d-4c4a8ce16041 |
| ca_bidsandtenders:66d44f32-2c57-4652-890e-0dbe7df6faa0:1 | Glen Chemicals Limited | Supply and Delivery of Pool Chemicals for Toronto District School Board (TDSB) and Toronto Catholic District School Board (TCDSB) |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/66d44f32-2c57-4652-890e-0dbe7df6faa0 |
| ca_bidsandtenders:66d44f32-2c57-4652-890e-0dbe7df6faa0:2 | Superior Pool Spa & Leisure Ltd. | Supply and Delivery of Pool Chemicals for Toronto District School Board (TDSB) and Toronto Catholic District School Board (TCDSB) |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/66d44f32-2c57-4652-890e-0dbe7df6faa0 |
| ca_bidsandtenders:66d44f32-2c57-4652-890e-0dbe7df6faa0:3 | 2261990 Ontario Inc | Supply and Delivery of Pool Chemicals for Toronto District School Board (TDSB) and Toronto Catholic District School Board (TCDSB) |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/66d44f32-2c57-4652-890e-0dbe7df6faa0 |
| ca_bidsandtenders:d086e49d-cd43-4d63-931b-77a979f5f6df:1 | Buxton & Dawe Limited | Elevator Modernization and Cylinder Replacement at William J. McCordic S. |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d086e49d-cd43-4d63-931b-77a979f5f6df |
| ca_bidsandtenders:16809485-32ce-4194-81e8-db6563633367:1 | Gym-Con Ltd. | Gym Floor Replacement at Maryvale PS TR-26-0354 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/16809485-32ce-4194-81e8-db6563633367 |
| ca_bidsandtenders:65c19a0d-0f39-4599-b74e-0466a92174c8:1 | Kudlak-Baird (1982) Limited | Barrier Free Lift Replacement at Northlea EMS TR-25-0992 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/65c19a0d-0f39-4599-b74e-0466a92174c8 |
| ca_bidsandtenders:a3dc48bb-2113-4fd7-af46-3587df16c08a:1 | Kertech Electric Inc. | Chair Lift Replacement at Humbercrest PS TR-26-0074 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a3dc48bb-2113-4fd7-af46-3587df16c08a |
| ca_bidsandtenders:1dcd3ed1-9888-4153-90b3-c6325f8cafa0:1 | Liftsafe Engineering and Service Group Inc. | Inspections of Lifting Devices and Repairs in Auto Shops at TDSB |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1dcd3ed1-9888-4153-90b3-c6325f8cafa0 |
| ca_bidsandtenders:47e0b848-b004-4196-8ea5-d8e879c25124:1 | DOLE Contracting Inc | Pape Avenue JPS - Building Envelope, Mechanical, and Electrical Systems Replacement - TR-25-0039 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/47e0b848-b004-4196-8ea5-d8e879c25124 |
| ca_bidsandtenders:95928518-d8e1-4ec7-ac82-de8c74f21c1f:1 | LAKESIDE CONTRACTING COMPANY LIMITED | Kindergarten Play Area Upgrades at Timberbank JPS - TR-24-0740 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95928518-d8e1-4ec7-ac82-de8c74f21c1f |
| ca_bidsandtenders:7f343f0e-5f55-4bdf-b5e2-df41b9f72968:1 | Bortolotto Design Architect | Professional Services, Interior Renovations at Heydon Park (70 D'Arcy Street) TR-26-0561 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7f343f0e-5f55-4bdf-b5e2-df41b9f72968 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:1 | Trinity Construction Management Limited | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:2 | Icon Builders Inc | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:3 | Harbridge & Cross Limited | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:4 | Corebuild Construction Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:5 | Torcom Construction Inc | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:6 | Van Horne Construction Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:7 | Area Construction Inc | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:8 | Aquicon Construction Co. Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:9 | GARRITANO BROS LTD | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:10 | Quad Pro Construction Inc. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:11 | REMO GENERAL CONTRACTING LTD. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:12 | Percon Construction Inc | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:13 | Everstrong Construction Ltd | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:14 | JR Certus Construction Co. Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:15 | Rutherford Contracting Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:16 | Tambro Construction Ltd. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:17 | PRE-ENG CONTRACTING LTD. | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:18 | M.J. Dixon Construction Limited | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:29dcdffe-2a50-40e8-87fd-e2f64037ca94:19 | Norlon Builders | Prequalification of General Contractors for TDSB Capital Projects |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/29dcdffe-2a50-40e8-87fd-e2f64037ca94 |
| ca_bidsandtenders:1e5fcb3b-81c5-49e2-ac32-d3dd19360740:1 | unit a architecture inc. | Professional Services, Washrooms Revitalization at Ionview PS TR-26-0172 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1e5fcb3b-81c5-49e2-ac32-d3dd19360740 |
| ca_bidsandtenders:5bb5f181-b041-4132-a8ea-bf7d64799d15:1 | Onsite Contracting Inc | Replace Play Area at Lillian PS |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5bb5f181-b041-4132-a8ea-bf7d64799d15 |
| ca_bidsandtenders:bf1dcae6-2111-42bc-9fd3-4ac3341556b0:1 | Hart-Well Electrical Company Ltd. | Emergency Lighting System Replacement at Mason Road JPS TR-23-1094 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bf1dcae6-2111-42bc-9fd3-4ac3341556b0 |
| ca_bidsandtenders:fc2bd206-1938-4e0c-ab6e-d25c808e17a9:1 | Kertech Electric Inc. | B/F Lift Modernization and Chair Lift Replacement at Vaughan Road Academy TR-21-1682 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fc2bd206-1938-4e0c-ab6e-d25c808e17a9 |
| ca_bidsandtenders:d969acd0-fd76-4675-b205-2751536c73df:1 | DURON ONTARIO LTD | Accessibility Improvements at Hollycrest MS TR-25-0946, North Albion CI TR-25-0947 and Silverthorn CI TR-25-0948 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d969acd0-fd76-4675-b205-2751536c73df |
| ca_bidsandtenders:05ef1a15-35d2-4881-a059-dfe99922b3b8:1 | Active Mechanical o/b 1246175 Ontario Limited | Multizone Units Replacement at Withrow Ave JPS TR-23-0420 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/05ef1a15-35d2-4881-a059-dfe99922b3b8 |
| ca_bidsandtenders:0eb676dc-5105-409c-9dce-401f3f077de8:1 | ALLTECH ELECTRICAL SYSTEMS INC. | Integrated P. A./In-house Phone System Replacement at John English JMS TR-24-0386 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0eb676dc-5105-409c-9dce-401f3f077de8 |
| ca_bidsandtenders:e5d570b1-a2c7-4288-949f-f55370171962:1 | DURON ONTARIO LTD | Accessibility Improvements at Humber Valley Village JMS - TR-25-0954, Lakeshore CI - TR-25-0955 Richview CI - TR-25-0956 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e5d570b1-a2c7-4288-949f-f55370171962 |
| ca_bidsandtenders:d45cd2c7-56ae-4c78-8abf-0210ecb11b92:1 | Building Arts Architects Inc | Professional Services, Interior Retrofit at Faywood Art Based Curriculum School TR-26-0537 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d45cd2c7-56ae-4c78-8abf-0210ecb11b92 |
| ca_bidsandtenders:a4ba37cd-7321-4f6e-a14a-504b48ff5f16:1 | LAKESIDE CONTRACTING COMPANY LIMITED | Upgrade Kindergarten Play Area at Dallington PS TR-24-0773 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a4ba37cd-7321-4f6e-a14a-504b48ff5f16 |
| ca_bidsandtenders:c82f634e-c75e-4b01-8b87-9ce2e8eb4d68:1 | Inter-All Ltd | Room Use Change - Room 25 to Classroom, Phase 2 at Humberside CI TR-26-0464 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c82f634e-c75e-4b01-8b87-9ce2e8eb4d68 |
| ca_bidsandtenders:fcf4fd14-66fa-4d29-9492-be640abf91f5:1 | Hart-Well Electrical Company Ltd. | Elevator Modernization at Dr Rita Cox-Kina Minagok PS |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fcf4fd14-66fa-4d29-9492-be640abf91f5 |
| ca_bidsandtenders:f5b98324-fb96-4da1-9fdb-94b076593618:1 | Baycrest Project & Construction Management | Accessibility Improvements at Bowmore Road JSPS TR-25-0969 and Crestview PS TR-25-0971 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f5b98324-fb96-4da1-9fdb-94b076593618 |
| ca_bidsandtenders:a8ac1626-6fa7-4a50-a2d0-3fe78d6a10b4:1 | LAKESIDE CONTRACTING COMPANY LIMITED | Replace Asphalt and Play Equipment at Indian Road Crescent JPS TR-25-0447 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a8ac1626-6fa7-4a50-a2d0-3fe78d6a10b4 |
| ca_bidsandtenders:0f9238a9-7969-4078-97bd-f1e75173b3d0:1 | Envirosafe Inc | Hazardous Materials Abatement - Network Security Camera System Replacement at RH King Academy TR-25-0738 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0f9238a9-7969-4078-97bd-f1e75173b3d0 |
| ca_bidsandtenders:d93188c7-1b99-4e71-b563-d346b133412c:1 | The BearStar Group Inc. | Hazardous Materials Abatement - Network Security Camera System Replacement at York Memorial CI TR-25-0734 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d93188c7-1b99-4e71-b563-d346b133412c |
| ca_bidsandtenders:b42e4dfe-2183-4ac0-b381-649c3891ec00:1 | DURON ONTARIO LTD | Gymnasiums Renovations at Malvern CI TR-25-0036 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b42e4dfe-2183-4ac0-b381-649c3891ec00 |
| ca_bidsandtenders:e0dab9e3-fad0-4efa-86c2-ac7b6032f7e6:1 | Inter-All Ltd | Replace Seating and Interior Finishes in Auditorium at East York CI TR-23-1131 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e0dab9e3-fad0-4efa-86c2-ac7b6032f7e6 |
| ca_bidsandtenders:2f3bbe96-312a-4ca8-8412-95f416e715a5:1 | Gym-Con Ltd. | Gym Floors Refinishing and Interior Finishes Replacement: Phase 1 at Rolph Rd ES |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2f3bbe96-312a-4ca8-8412-95f416e715a5 |
| ca_bidsandtenders:a39da6ea-a338-45ea-b7c5-9810aefa7318:1 | LAKESIDE CONTRACTING COMPANY LIMITED | New Junior Play Equipment at Donwood Park PS TR-25-0636 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a39da6ea-a338-45ea-b7c5-9810aefa7318 |
| ca_bidsandtenders:ec45df57-5c2a-48b3-bcb2-b69761be592f:1 | WINDSPEC INC. | Supply of Thermally Broken Curtain Wall and Entrance Door Systems for Brian PS TR-26-0302 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ec45df57-5c2a-48b3-bcb2-b69761be592f |
| ca_bidsandtenders:ae90101a-70a8-40a8-b973-94f0f8bf8c30:1 | 1172270 ONTARIO INC O/A BARWOOD FLOORING | Refinish Gym Floor at Summit Heights PS TR-23-1158 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ae90101a-70a8-40a8-b973-94f0f8bf8c30 |
| ca_bidsandtenders:9e82d357-fb33-4a7a-b4ee-b20f301cf24b:1 | Lisgar Construction Company a Divison of United Shelters Limited | Emergency Drain Pipe Installation at Oriole Park JPS TR-26-0339 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9e82d357-fb33-4a7a-b4ee-b20f301cf24b |
| ca_bidsandtenders:91cf64b4-38ea-4db8-9746-b9f6393f777e:1 | Kertech Electric Inc. | Fire Alarm System Replacement at J. B. Tyrrell SPS |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/91cf64b4-38ea-4db8-9746-b9f6393f777e |
| ca_bidsandtenders:6f735efa-b97c-4083-bf1c-1f7922845153:1 | Ashland Paving Ltd | Replace Deteriorated Paving and Play Features at Owen PS TR-25-0673 |  |  |  | https://tdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6f735efa-b97c-4083-bf1c-1f7922845153 |
| … 240 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-00890:663d1c0f-9142-46b4-b05b-23f899d45db0 | Alberta Electric System Operator | Alberta Electric System Operator - Request for Proposal - Penetration Testing Services | 40000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00890 |
| ca_alberta_apc:AB-2025-04899:19184072-d010-4641-b548-d37e8cbbf49d | Technology and Innovation | Technology and Innovation - Request for Quotes - Adobe Experience Manager Forms Maintenance and Support Renewal | 80376.4 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04899 |
| ca_alberta_apc:AB-2025-06674:17423463-d4d9-46f6-95f6-70813d00a7e6 | University of Alberta | University of Alberta - Request for Proposal - Solarwinds Observability Advanced for Enterprise AE2000 Software Subscription | 444391.01 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06674 |
| ca_alberta_apc:AB-2026-00821:06cf7018-8237-4dc0-b4c3-7c0efd2691dd | Technology and Innovation | Technology and Innovation - Request for Quotes - SOLARWINDS SELF-HOSTED ADVANCED A250 Subscription Licence | 74571.39 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00821 |
| ca_alberta_apc:AB-2026-01700:4c95ce4d-61eb-46a5-ba54-0ccf96ac9d27 | Technology and Innovation | Technology and Innovation - Request for Quotes - VMware SaaS Purchase 2026-2027 | 357067.1 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01700 |
| ca_alberta_apc:AB-2026-01798:81c4d078-e871-4b40-8900-8c1feb63ed35 | University of Calgary | University of Calgary - Request for Quotes - Veeam License Renewal | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01798 |
| ca_alberta_apc:AB-2026-01814:35f7c74d-e76e-4954-8c1a-45e99993ea81 | The Good Samaritan Society (A Lutheran Social Service Organization) | The Good Samaritan Society (A Lutheran Social Service Organization) - Request for Proposal - Microsoft License | 732996.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01814 |
| ca_alberta_apc:AB-2026-03029:7cd74eba-6ba6-4651-9f9c-620104022512 | Town of Okotoks | Town of Okotoks - Request for Quotes - Supply of Microsoft Software Licenses | 84386.4 |  |  | https://purchasing.alberta.ca/posting/AB-2026-03029 |
| ca_bc_ministry_awards:1eea79ae91f1303b | Ministry of Finance | IBM Content Manager Software Subscription & Support Renewal | 87695.8 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:167446e43a315706 | Ministry of Technology, Innovation and Citizens' Services | IBM Annual SW Subscription Renewal (Victoria) | 30891.09 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:26af234827ef750c | Ministry of Technology, Innovation and Citizens' Services | TOAD for Oracle (Victoria) | 7502.66 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:8a8989d609d0e3c1 | Ministry of Technology, Innovation and Citizens' Services | Annual Adobe Livecycle/Reader renwals (Victoria, BC) | 53129.52 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c0c860279f64bb3a | Ministry of Technology, Innovation and Citizens' Services | Attachmate Licenses & Support (Victoria) | 22461.05 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:5cc06791be6cda95 | Ministry of Technology, Innovation and Citizens' Services | ieSpell Corporate License (Victoria) | 8923.07 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c19db4b271c2d009 | Ministry of Technology, Innovation and Citizens' Services | SSO Plugin Standard License (Victoria, BC) | 13273.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:9e6510e1a6d49db4 | Ministry of Technology, Innovation and Citizens' Services | SDSI IBM DB2 Connect Support Renewal (Victoria, BC) | 20083.44 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:a5adf8e43f53db25 | Ministry of Technology, Innovation and Citizens' Services | Attachmate Licenses (Victoria) | 92799.9 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:eb42539b68e24c3b | Ministry of Technology, Innovation and Citizens' Services | IBM Cognos BI Analytics User Licenses and Support (Victoria, BC) | 118489.73 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:fb24218434cdf46d | Ministry of Technology, Innovation and Citizens' Services | Opentext SecureShell and Exceed Maintenance | 13976.93 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:5bf576ca45010761 | Ministry of Technology, Innovation and Citizens' Services | IPSwitch March 31, 2015- March 30, 2016 support renewal | 5648.13 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:867b259729dab772 | Ministry of Technology, Innovation and Citizens' Services | i-640571 MoH Splunk Enterprise License and Support | 64716.98 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:66d2c066c1105156 | Ministry of Technology, Innovation and Citizens' Services | Ipswitch Licenses (Victoria) | 6970.86 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:9fb61882d03e8df7 | Ministry of Technology, Innovation and Citizens' Services | Exceed Maintenance (Victoria, BC) | 17733.86 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:d087b323539d9034 | Ministry of Technology, Innovation and Citizens' Services | Allround Automations PL/SQL Developer (Victoria, BC) | 11013.01 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:d65d4e090f225b22 | Ministry of Technology, Innovation and Citizens' Services | ableau Software Desktop - Professional User (Victoria, BC) | 12004.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:3ecd8600f4cef245 | Ministry of Technology, Innovation and Citizens' Services | Nuance DNS support renewal (Victoria) | 15959.45 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c71cb1fdf4297c16 | Ministry of Technology, Innovation and Citizens' Services | SmartTerm Office User Site Licences (Victoria, BC) | 129819.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:41b14adb5749b227 | Ministry of Technology, Innovation and Citizens' Services | Tableau Desktop Professional (Victoria, BC) | 19682.55 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:7117c2f994f9aa3e | Ministry of Technology, Innovation and Citizens' Services | Techsmith true up (Victoria, BC) | 8561.28 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:61150e3b76010049 | Ministry of Citizens' Services | Splunk Enterprise Support Renewal (Victoria) | 12327.54 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:3bbe27f345029f79 | Ministry of Citizens' Services | Nuance DNS Support Renewal (Victoria) | 15351.64 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:975d74244b99493a | Ministry of Citizens' Services | Content Matrix - SharePoint Managed Capacity - Perpetual License | 122101.63 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:c79bfc9d4d0d91e0 | Ministry of Citizens' Services | Content Matrix - SharePoint Managed Capacity - Perpetual License | 122101.63 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:e59d3c4ff1b9c7c9 | Ministry of Citizens' Services | Lansweeper Ultimate Edition (Victoria) | 8174.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:f130d481e9dabf8d | Ministry of Citizens' Services | REQUOTE-ERWin Data Modeler Workgroup & 1 year Enterprise Maint. | 15290.44 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:deb5a114b25f1870 | Ministry of Citizens' Services | Splunk Enterprise Software Support Renewal (Victoria, BC) | 11188.89 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:239341e273fe2374 | Ministry of Citizens' Services | Lansweeper Ultimate Edition (Victoria, BC) | 7697.24 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:b9cfe6d886ee38de | Ministry of Citizens' Services | Attachmate Reflections Desktop Licenses & Maintenance (Vic, BC) | 6955.76 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:154aab4003f11b4f | Ministry of Citizens' Services | Reflection Desktop for Unix & OpenVMS (Victoria) | 11624.93 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:cf266230f2bae27a | Ministry of Citizens' Services | Reflection Desktop for Unix & OpnenVMS Licences (Victoria) | 24156.73 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:965a3339d15b2a19 | Ministry of Citizens' Services | Tidal Software Support and Maintenance (Victoria) | 12649.85 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:4b51f495f7c9f7ad | Ministry of Citizens' Services | Shareplex Standard Edition Maintenance Renewal (Victoria) | 21262.5 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/aee0fed5-e1f5-4e32-b17c-c98eafdd0d36/download/ministry-contract-awards-2012-dec-31-2018.csv |
| ca_bc_ministry_awards:438b1ed3613f7fc2 | Ministry of Citizens' Services | MySQL Enterprise Edition Subscription License | 15855.84 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:fc8699737b4bfa7a | Ministry of Citizens' Services | JIRA Software Licenses (Victoria) | 25263.39 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:af7d039553cd53d9 | Ministry of Citizens' Services | Oracle Xpert Edition W/Quest DBA Admin Module License | 14773.92 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:9fa7f6580879131c | Ministry of Citizens' Services | Quest Maintenance Renewals – Various Titles (Victoria) | 205704.71 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:c39ccea37402a60a | Ministry of Citizens' Services | Splunk Enterprise Support Renewal (Victoria) | 13753.6 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:ae81e88864348c79 | Ministry of Citizens' Services | SAP Crystal Server2016 License & Support (Victoria) | 5669.53 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/3ebd6010-3c30-4fa8-b95d-ed2362ce863f/download/ministry-contract-awards-2019.csv |
| ca_bc_ministry_awards:c4a3e071097eb61d | Ministry of Citizens' Services | RStudio Connect Standard Named User  (Victoria) | 42322.56 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b113f1d3-3a78-4e10-a978-9a73a8c44be1/download/ministry-contract-awards-apr-jun-2022.csv |
| ca_bc_ministry_awards:97443a3d6c408d05 | Liquor Distribution Branch | ITQ2023-05-08 InformaCast Advanced Notification Subscription Endpoint | 3647.5 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/e948421d-a061-4aeb-be00-46f84bec8b32/download/ministry-contract-awards-apr-jun-2023.csv |
| ca_bc_ministry_awards:d14ff0c8c7bacf9b | Liquor Distribution Branch | ITQ2023-05-23 Purchase and Renewal of Camtasia Licenses | 6100.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/e948421d-a061-4aeb-be00-46f84bec8b32/download/ministry-contract-awards-apr-jun-2023.csv |
| ca_bc_ministry_awards:9dab6626a7fd10d2 | Ministry of Citizens' Services | Quest Annual Support Renewal | 272170.97 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:3bac3c0953691764 | Ministry of Citizens' Services | Cisco Adapters & Modules (Victoria) | 9008.22 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:81a7f73f825a9e5e | Ministry of Citizens' Services | MySQL Enterprise Edition Renewal | 14746.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:dbf79efeb21de4fa | Ministry of Citizens' Services | Red Hat JBoss EAP Renewal Subscription | 43445.53 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/ee6045f4-dcaf-4a2b-80ef-8eeb876c64a1/download/ministry-contract-awards-apr-to-jun-2020.csv |
| ca_bc_ministry_awards:a03d37b079105ea4 | Ministry of Citizens' Services | Quest Support Renewal for the period 01-Apr-21 to 31-May-22 | 125837.72 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/500eda3c-e5a9-405d-a7c2-7443ce237387/download/ministry-contract-awards-apr-to-june-2021.csv |
| ca_bc_ministry_awards:9694ae1c0256ae42 | Ministry of Citizens' Services | IBM InfoSphere Master Data Management (MDM) (Victoria BC) | 275755.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/500eda3c-e5a9-405d-a7c2-7443ce237387/download/ministry-contract-awards-apr-to-june-2021.csv |
| ca_bc_ministry_awards:b9b88db2c121d312 | Ministry of Health | Jira Software Upgrade 100 Users (from 25 users) | 6143.2 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:58c6a40d6d342b0d | Ministry of Citizens' Services | IBM WebSphere Support Renewal | 85977.45 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/2ff7c805-5187-4ab4-a8ec-c0f85dca97fb/download/ministry-contract-awards-jan-to-apr-2020.csv |
| ca_bc_ministry_awards:0eab596ee23cf369 | Ministry of Citizens' Services | True-up of COTS TechSmith Camtasia and TechSmith Snag | 49415.66 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/b84ec72e-30ad-4f85-be66-a26dac65a137/download/ministry-contract-awards-jan-to-mar-2021.csv |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S1-20 — Aquatera Utilities Inc. ⇄ Stantec

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08) — 11101-104 Ave, Grande Prairie, T8V 8H6, CA — buyer tax no. 897610002 (Canada's Business Registries, AB 209590090, 2026-11-08)
SUBMIT TO: accountspayable@aquatera.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: contract AB-2025-06265 (apc_reference_number); tender EC-03-025-02 (solicitation_number) | PO rule: yes (as published: must include PO)
FROM / REMIT TO: Stantec Inc. — 200-325 25 Street SE, Calgary, AB, T2A 7H8 | GST/HST 130521958RT0001 (account derived from the BN9) | NEQ 1170241336
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work
DESCRIPTION: Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering | AMOUNT: 579,251.00 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 93
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Aquatera Utilities Inc. (company (private sector), AB) — public contract / purchase award with a published end date (dated record): Stantec | subject: Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering | instrument: contract award (OPEN-COMPETITIVE) | contract number: AB-2025-06265 (apc_reference_number) | solicitation: EC-03-025-02 (solicitation_number); d02a80e1-75d8-4f86-a5b8-942394ef4431 (opportunity_id) | all identifiers: {"apc_reference_number": "AB-2025-06265", "opportunity_id": "d02a80e1-75d8-4f86-a5b8-942394ef4431", "solicitation_number": "EC-03-025-02", "award_id": "6b9be44e-d253-4a59-abc4-b4dd192af3ab", "supplier_id": "b61bbb81-4111-42a0-b8a4-417a0b31cc16", "parent_id": null} | value: 579251.0 CAD | awarded 2025-12-23, start 2025-11-03, end 2026-12-28 | published by: Alberta Purchasing Connection (APC) - awarded opportunities | record: https://purchasing.alberta.ca/posting/AB-2025-06265 | vendor in Canada because: awards[].address.country == 'CA' (stateProvince 'CA-AB') | status rule: active (published end date today or later) | this buyer has 11 records with Canada-located vendors (9 distinct vendors; 8 in the last 12 months; latest 2026-06-04)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:eaf16832447fca28
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Aquatera Utilities Inc.
- **buyer_website**: https://www.aquatera.ca
- **buyer_address**: 11101-104 Ave, Grande Prairie, T8V 8H6, CA
- **buyer_legal_name_as_published**: AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08)
- **buyer_bn_as_published**: 897610002 (Canada's Business Registries, AB 209590090, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 897610002RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_registry_id**: 209590090 (AB; https://ised-isde.canada.ca/cbr-rec/en/search?q=Aquatera%20Utilities%20Inc.)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 209590090, 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; invoicing requirements: the lane's AP page (https://www.aquatera.ca/public/download/files/327360); PO requirement: the lane's AP page (https://www.aquatera.ca/public/download/files/327360)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_vendor_id**: b61bbb81-4111-42a0-b8a4-417a0b31cc16 (supplier_id)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@aquatera.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.aquatera.ca/public/download/files/327360
- **email_evidence_quote**: Seller will submit invoices with reference to the Purchase Order to: accountspayable@aquatera.ca 16. Seller agrees not to invoice at price higher than those formally agreed to by this order or subsequent amendment. 17
- **mailbox_provenance**: accountspayable@aquatera.ca (invoicing/AP) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-28 | page: https://www.aquatera.ca/public/download/files/327360 | quote: "Seller will submit invoices with reference to the Purchase Order to: accountspayable@aquatera.ca 16. Seller agrees not to invoice at price higher than those for" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch09.csv task CH-AP-00842
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; rua=mailto:05b0c3a4107c457b96b0ab36c0b3d14d@dmarc-reports.cloudflare.net;
- **dmarc_record_domain**: aquatera.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:70.32.90.40 ip4:206.172.31.0/28 ip4:207.229.45.32/28 ip4:207.229.45.34 ip4:104.219.130.131 ip4:173.252.27.180 include:spf.protection.outlook.com include:sendgrid.net -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: PO terms updated2026-10-26: submit invoices referencing PO to accountspayable@aquatera.ca; prices must not exceed order or amendment. All contract correspondence must include PO number. Unless stated otherwise, payable in Canadian dollars; materials/service payment may be subject to construction lie
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4, s. 32.2(1) (current to 2025-04-01) (https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf, read 2026-11-08: "an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice"); s. 1.1(1.1): does not apply to Crown public works; applies only if this contract is an improvement under the Act
- **po_required_as_published**: yes (as published: must include PO)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "yes (as published: must include PO)", "requirements_text": "PO terms updated2026-10-26: submit invoices referencing PO to accountspayable@aquatera.ca; prices must not exceed order or amendment. All contract correspondence must include PO number. Unless stated otherwise, payable in Canadian dollars; materials/service payment may be subject to construction lie"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08) — 11101-104 Ave, Grande Prairie, T8V 8H6, CA — buyer tax no. 897610002 (Canada's Business Registries, AB 209590090, 2026-11-08) ⏎ SUBMIT TO: accountspayable@aquatera.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract AB-2025-06265 (apc_reference_number); tender EC-03-025-02 (solicitation_number) | PO rule: yes (as published: must include PO) ⏎ FROM / REMIT TO: Stantec Inc. — 200-325 25 Street SE, Calgary, AB, T2A 7H8 | GST/HST 130521958RT0001 (account derived from the BN9) | NEQ 1170241336 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering | AMOUNT: 579,251.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08)", "legal_name_is_published": true, "address": "11101-104 Ave, Grande Prairie, T8V 8H6, CA", "address_is_the_invoice_address": false, "tax_number": "897610002 (Canada's Business Registries, AB 209590090, 2026-11-08)", "language": "en"}, "submit_to": {"email": "accountspayable@aquatera.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: must include PO)", "po_number": "", "contract_or_agreement_number": "AB-2025-06265 (apc_reference_number)", "vendor_id_with_buyer": "b61bbb81-4111-42a0-b8a4-417a0b31cc16 (supplier_id)", "reference_hint": "contract or agreement number: AB-2025-06265 (apc_reference_number) — source ca_alberta_apc"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4, s. 32.2(1) (current to 2025-04-01) (https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf, read 2026-11-08: \"an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: AB-2025-06265 (apc_reference_number) — source ca_alberta_apc

## Vendor
- **vendor**: Stantec
- **vendor_legal_name**: Stantec Inc.
- **vendor_trading_name**: Stantec
- **vendor_registry_id**: Corporations Canada (corporation number): 3018784; corporation number 3018784 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=3018784
- **vendor_registered_address**: Suite 300, 10220 103 Avenue Northwest, Edmonton, AB, T5J 0K4, CA
- **vendor_neq**: 1170241336 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 7799 — Engineering and environmental consulting
- **vendor_employees_quebec**: De 1000 à 2499
- **vendor_establishments_quebec**: STANTEC EXPERTS-CONSEILS LTÉE: 101-4 rue Principale N, Amos (Québec), J9T2K6; STANTEC EXPERTS-CONSEILS LTÉE: 300-1200 boul. Saint-Martin O, Laval (Québec), H7S2E4; STANTEC EXPERTS-CONSEILS LTÉE: 400-375 boul. Roland-Therrien, Longueuil (Québec), J4H4A6
- **vendor_directors_range**: 3 to 20 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2025; Corporations Canada anniversary 1994-03-30
- **vendor_address**: 200-325 25 Street SE, Calgary, AB, T2A 7H8
- **vendor_country_basis**: awards[].address.country == 'CA' (stateProvince 'CA-AB')
- **vendor_bn9**: 130521958
- **vendor_gst_hst_derived**: 130521958RT0001
- **vendor_website**: https://www.stantec.com/
- **vendor_emails**: media@stantec.com
- **vendor_logo_url**: https://www.stantec.com/static/img/favicon/apple-touch-icon.png
- **vendor_facts_provenance**: name and address: the record's vendor block (Alberta Purchasing Connection (APC) - awarded opportunities); registry identity: Corporations Canada (corporation number): 3018784; corporation number 3018784 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (2014-07-28) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 3018784 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-01-01; website: https://www.stantec.com/; NEQ: 1170241336 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: N.P.A., a Division of Colas Western Canada Inc.: 27% of 11 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (2014-07-28)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2014-01-01
- **vendor_years_in_business**: 12.9 (since 2014-01-01, registry date)
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q2331913; business; public company
- **vendor_founded**: 1954-01-01 (Wikidata Q2331913, official website on the organisation's domain (https://www.stantec.com/) + name; 2026-11-08)
- **vendor_employees**: 22000 (Wikidata Q2331913, official website on the organisation's domain (https://www.stantec.com/) + name; 2026-11-08)
- **vendor_bn_source**: corporations_canada 3018784 (exact match)

## Contract
- **po_required_as_published**: yes (as published: must include PO)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"apc_reference_number": "AB-2025-06265", "opportunity_id": "d02a80e1-75d8-4f86-a5b8-942394ef4431", "solicitation_number": "EC-03-025-02", "award_id": "6b9be44e-d253-4a59-abc4-b4dd192af3ab", "supplier_id": "b61bbb81-4111-42a0-b8a4-417a0b31cc16", "parent_id": null}
- **contract_title**: Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering
- **commodity**: 81000000, 81000000, 81000000 Engineering and Research and Technology Based Services > Professional engineering services; Engineering and Research and Technology
- **contract_description**: The Owner is developing the WASTEWATER UV DISINFECTION project, to meet current Alberta Environment regulations for treated wastewater. The Wastewater UV system will disinfect wastewater prior to being returned to the Wapiti River.
- **contract_or_agreement_number**: AB-2025-06265 (apc_reference_number)
- **solicitation_or_tender_number**: EC-03-025-02 (solicitation_number); d02a80e1-75d8-4f86-a5b8-942394ef4431 (opportunity_id)
- **award_or_notice_id**: 6b9be44e-d253-4a59-abc4-b4dd192af3ab (award_id)
- **commodity_codes**: UNSPSC 81000000 (Engineering and Research and Technology Based Services > Professional engineerin); GSIN C219
- **contract_value**: 579251.0
- **currency**: CAD
- **award_date**: 2025-12-23
- **start_date**: 2025-11-03
- **end_date**: 2026-12-28
- **contract_link**: https://purchasing.alberta.ca/posting/AB-2025-06265
- **source**: Alberta Purchasing Connection (APC) - awarded opportunities
- **contracts_with_canadian_suppliers**: 11
- **records_last_12_months**: 8
- **record_sources**: Alberta Purchasing Connection (APC) - awarded opportunities (11)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 11 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Engineering and Research and Technology Based Services > Pro (3); Building and Facility Construction and Maintenance Services  (3); Financial and Insurance Services > Accounting and bookkeepin (1)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 897610002RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4, s. 32.2(1) (current to 2025-04-01) (https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf, read 2026-11-08: "an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice"); s. 1.1(1.1): does not apply to Crown public works; applies only if this contract is an improvement under the Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 130521958RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08) — 11101-104 Ave, Grande Prairie, T8V 8H6, CA — buyer tax no. 897610002 (Canada's Business Registries, AB 209590090, 2026-11-08) ⏎ SUBMIT TO: accountspayable@aquatera.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: contract AB-2025-06265 (apc_reference_number); tender EC-03-025-02 (solicitation_number) | PO rule: yes (as published: must include PO) ⏎ FROM / REMIT TO: Stantec Inc. — 200-325 25 Street SE, Calgary, AB, T2A 7H8 | GST/HST 130521958RT0001 (account derived from the BN9) | NEQ 1170241336 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering | AMOUNT: 579,251.00 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "AQUATERA UTILITIES INC. (as registered: Canada's Business Registries, AB 209590090, 2026-11-08)", "legal_name_is_published": true, "address": "11101-104 Ave, Grande Prairie, T8V 8H6, CA", "address_is_the_invoice_address": false, "tax_number": "897610002 (Canada's Business Registries, AB 209590090, 2026-11-08)", "language": "en"}, "submit_to": {"email": "accountspayable@aquatera.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: must include PO)", "po_number": "", "contract_or_agreement_number": "AB-2025-06265 (apc_reference_number)", "vendor_id_with_buyer": "b61bbb81-4111-42a0-b8a4-417a0b31cc16 (supplier_id)", "reference_hint": "contract or agreement number: AB-2025-06265 (apc_reference_number) — source ca_alberta_apc"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Prompt Payment and Construction Lien Act, R.S.A. 2000, c. P-26.4, s. 32.2(1) (current to 2025-04-01) (https://kings-printer.alberta.ca/documents/Acts/P26P4.pdf, read 2026-11-08: \"an owner who owes money under a proper invoice must pay the amount payable under a proper invoice no later than 28 days after receiving the proper
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 80
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published | missing: finance mailbox; payment terms published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["accountspayable@aquatera.ca (invoicing/AP)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-10-28", "page: https://www.aquatera.ca/public/download/files/327360", "quote: \"Seller will submit invoices with reference to the Purchase Order to: accountspayable@aquatera.ca 16. Seller agrees not to invoice at price higher than those for\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch09.csv task CH-AP-00842"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "invoicing requirements: the lane's AP page (https://www.aquatera.ca/public/download/files/327360)", "PO requirement: the lane's AP page (https://www.aquatera.ca/public/download/files/327360)"], "vendor_facts": ["name and address: the record's vendor block (Alberta Purchasing Connection (APC) - awarded opportunities)", "registry identity: Corporations Canada (corporation number): 3018784", "corporation number 3018784 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active", "Québ

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.aquatera.ca/public/download/files/327360 | 2026-11-08 | blocked |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, stantec.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.stantec.com/static/img/favicon/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: stantec.com
- **key**: vendor:Stantec
- **name**: Stantec
- **website**: https://stantec.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Stantec
- **jsonld_url**: https://www.stantec.com/.html
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "WebPage", "name": "", "url": "/content/stantec/en.html" }
- **jsonld_page**: https://www.stantec.com/en
- **legal_name_stated**: Developing Professionals Group
- **legal_name_stated_url**: https://www.stantec.com/en
- **legal_name_stated_quote**: duates", "link": "\/en\/careers\/students\u002Dgraduates.html", "subMenuLevel2": [ ] }, { "label": "Developing Professionals Group (DPG)", "link": "\/en\/careers\/developing\u002Dprofessionals\u002Dgroup.html", "subMenuLevel2": [

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Aquatera Utilities Inc. | found | AQUATERA UTILITIES INC. | 897610002 | 209590090 | AB | Alberta Business Corporation | Active | 2001-11-02 | GRANDE PRAIRIE | AB |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Aquatera%20Utilities%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Stantec | Q2331913 | official website on the organisation's domain (https://www.stantec.com/) + name |  | Stantec | Stantec | business; public company | business corporation | Canada | 1954-01-01 | Edmonton |
| b | Aquatera Utilities Inc. |  |  |  |  |  |  |  |  |  |  |
| b | Stantec Inc. | Q2331913 | official website on the organisation's domain (https://www.stantec.com/) + name |  | Stantec | Stantec | business; public company | business corporation | Canada | 1954-01-01 | Edmonton |
| v | Stantec Inc. | Q2331913 | official website on the organisation's domain (https://www.stantec.com/) + name |  | Stantec | Stantec | business; public company | business corporation | Canada | 1954-01-01 | Edmonton |
| v | STANTEC ARCHITECTURE LTD. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:eaf16832447fca28",
 "ap_contact_team": {
  "emails": [
   "accountspayable@aquatera.ca",
   "utilitybills@hinton.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": "PO terms updated2026-10-26: submit invoices referencing PO to accountspayable@aquatera.ca; prices must not exceed order or amendment. All contract correspondence must include PO number. Unless stated otherwise, payable in Canadian dollars; materials/service payment may be subject to construction lien holdback.",
  "evidence": [
   {
    "email": "accountspayable@aquatera.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": "PO terms updated2026-10-26: submit invoices referencing PO to accountspayable@aquatera.ca; prices must not exceed order or amendment. All contract correspondence must include PO number. Unless stated otherwise, payable in Canadian dollars; materials/service payment may be subject to construction lien holdback.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.aquatera.ca/public/download/files/327360",
    "quote": "Seller will submit invoices with reference to the Purchase Order to: accountspayable@aquatera.ca 16. Seller agrees not to invoice at price higher than those formally agreed to by this order or subsequent amendment. 17",
    "retrieved_date": "2026-10-28",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch09.csv",
    "org": "Aquatera Utilities Inc.",
    "task_id": "CH-AP-00842",
    "verified_via": "referee saw it on this page on 2026-11-07; the page could not be read today (unverified_page_unavailable)"
   },
   {
    "email": "utilitybills@hinton.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.aquatera.ca/contact",
    "quote": "<strong>Phone:</strong> <a class=\"phone\" href=\"tel:780.865.6014\">780.865.6014</a></p> <p><strong>Email:</strong> <a class=\"email\" href=\"tel:utilitybills@hinton.ca\"><span class=\"__cf_email__\" data-cfemail=\"106564797c79646972797c7c635078797e647f7e3e7371\">[email protected]</span></a></p> </di",
    "retrieved_date": "2026-10-26",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Aquatera Utilities Inc.",
    "task_id": "CH-AP-00842",
    "verified_via": "referee saw it on this page on 2026-11-07; the page could not be read today (unverified_page_unavailable)"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site:aquatera.ca invoice accounts payable suppliers; site:aquatera.ca purchasing; opened Contact, Resources and current-linked PO Terms and Purchasing Policy; old PurchasingPolicy download404",
  "site crawl of www.aquatera.ca (25 pages, robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2025-06265:6b9be44e-d253-4a59-abc4-b4dd192af3ab | ca_alberta_apc | ongoing | Aquatera Utilities Inc. - Request for Proposal - Wasterwater UV Disinfection - Engineering | 579251.0 | CAD |  |  | {"apc_reference_number": "AB-2025-06265", "opportunity_id": "d02a80e1-75d8-4f86-a5b8-942394ef4431", "solicitation_number": "EC-03-025-02", "award_id": "6b9be44e-d253-4a59-abc4-b4dd192af3ab", "supplier | https://purchasing.alberta.ca/posting/AB-2025-06265 |

## The buyer's other Canadian-vendor records (first 60 of 10)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-08143:48ce7f5a-f1cd-40f4-af55-2561fddc675e | Tetra Tech Canada Inc. | Aquatera Utilities Inc. - Request for Proposal - Landfill Expansion and Closure Planning - Engineering Services | 315442.04 |  |  | https://purchasing.alberta.ca/posting/AB-2024-08143 |
| ca_alberta_apc:AB-2025-02474:37967ca9-5d12-4fb6-b5a6-d47b3f473b5b | Fletcher Mudryk LLP | Aquatera Utilities Inc. - Negotiated Request for Proposal - EXTERNAL AUDIT SERVICES | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-02474 |
| ca_alberta_apc:AB-2025-03021:3cc324ff-e396-42fc-be68-07ee59bbe651 | N.P.A., a Division of Colas Western Canada Inc. | Aquatera Utilities Inc. - Request for Proposal - CONCRETE PAVEMENT & SERVICES  | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03021 |
| ca_alberta_apc:AB-2025-05450:b6c4ede8-136c-49c4-8338-36f2618233f0 | Sustainable Developments Commercial Services Inc. | Aquatera Utilities Inc. - Negotiated Request for Proposal - RFP for CRLS DIRECT TO GP | 706961.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05450 |
| ca_alberta_apc:AB-2025-06216:64200466-d470-4551-bbbc-dae9c91e48ef | Insituform Technologies Limited | Aquatera Utilities Inc. - Request for Proposal - 2026 Sanitary Lining Program | 879482.9 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06216 |
| ca_alberta_apc:AB-2025-06436:8a1525ff-ffd5-4573-bcac-025eae504201 | Hatfield Consultants | Aquatera Utilities Inc. - Request for Proposal - Wapiti River Long Term Monitoring Program | 189936.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-06436 |
| ca_alberta_apc:AB-2026-00749:72d901f7-66fd-4fbd-bb6f-2e54359ac24b | N.P.A., a Division of Colas Western Canada Inc. | Aquatera Utilities Inc. - Request for Proposal - 2026 Water Valve Replacement Program-49071 | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00749 |
| ca_alberta_apc:AB-2026-00788:8072f366-1991-47f1-a517-43189c435492 | N.P.A., a Division of Colas Western Canada Inc. | Aquatera Utilities Inc. - Request for Proposal - RFP for 97B Street Utilities Upgrade and Road Rebuild - 49068 | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00788 |
| ca_alberta_apc:AB-2026-00808:b004bfb7-001c-47b9-83d6-f7d1aaf885bc | Norwest Construction and Management Ltd. | Aquatera Utilities Inc. - Request for Proposal - RFP for WTP Reservoir #2 Mechanical and Electrical Installation | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00808 |
| ca_alberta_apc:AB-2026-00869:56ca1db5-8a05-406f-b949-66ec4753a9e7 | Associated Engineering Alberta Ltd. | Aquatera Utilities Inc. - Request for Proposal - RFP FOR VERTICAL ASSET DESIGN AND CONSTRUCTION STANDARDS | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00869 |

## The vendor's other buyers in the dataset (first 60 of 200)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2020-03027:54a7ca5e-9d01-eb61-1a2c-39c2ed490000 | Christ the Redeemer Catholic Separate School Division | Christ the Redeemer Catholic Separate School Division - Invitation to Bid - OKOTOKS-ECOLE GOOD SHEPHERD SCHOOL PERMANENT 800-CAPACITY GYMNASIUM | 238100.0 |  |  | https://purchasing.alberta.ca/posting/AB-2020-03027 |
| ca_alberta_apc:AB-2022-03632:12f9c15e-328a-2063-17f4-39c2ed480000 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Negotiated Request for Proposal - Electrical Distribution System Upgrade | 170000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2022-03632 |
| ca_alberta_apc:AB-2023-05732:f8cf354c-73ad-a665-1ec8-39c2ed480000 | Alberta Gaming, Liquor and Cannabis Commission | Alberta Gaming, Liquor and Cannabis Commission - Negotiated Request for Proposal - Consulting Services for Office Tower Retrofit Project | 998392.15 |  |  | https://purchasing.alberta.ca/posting/AB-2023-05732 |
| ca_alberta_apc:AB-2023-07045:c7ff46e2-756f-4695-8342-3ff1807cd1b3 | City of Calgary | City of Calgary - Request for Proposal - Green Stormwater Infrastructure Triple Bottom Line Tool | 314840.0 |  |  | https://purchasing.alberta.ca/posting/AB-2023-07045 |
| ca_alberta_apc:AB-2024-02816:fc1682e1-754e-426c-b5c4-9b339e0f02d7 | City of St. Albert | City of St. Albert - Request for Proposal - Annual Groundwater Sampling Program | 57732.87 |  |  | https://purchasing.alberta.ca/posting/AB-2024-02816 |
| ca_alberta_apc:AB-2024-08411:44744dbf-5e4c-4a6f-b30c-a2ab3d764300 | City of Calgary | City of Calgary - Request for Proposal - 24-1677 Thornhill Aquatic and Recreation Centre – Service Cycle Upgrades | 2102997.88 |  |  | https://purchasing.alberta.ca/posting/AB-2024-08411 |
| ca_alberta_apc:AB-2024-09315:2f3255bb-8042-402a-83fe-b09b0b3c1de4 | Epcor | Epcor - Request for Proposal - Environmental, Health and Safety (EH&S), and  Operation and Maintenance (O&M) Audit  Services |  |  |  | https://purchasing.alberta.ca/posting/AB-2024-09315 |
| ca_alberta_apc:AB-2024-09917:4cddb584-0c3c-44b0-aa2c-2f3e7d1af179 | Environment and Protected Areas | Environment and Protected Areas - Request for Proposal - Thorsby Flood Study | 199888.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-09917 |
| ca_alberta_apc:AB-2025-01047:b56dc33d-4b34-47c7-82a8-3e38e1ce7a4f | Rocky View School Division | Rocky View School Division - Request for Proposal - Architectural Prime Consultants | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-01047 |
| ca_alberta_apc:AB-2025-03446:97423ce2-4f62-42fc-87a4-a679c3ca0fae | City of St. Albert | City of St. Albert - Negotiated Request for Proposal - SWMF Condition Assessment and Bathymetric Survey | 211023.2 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03446 |
| ca_alberta_apc:AB-2025-03619:52e720f0-2db9-4d86-8abb-946cd6fe3e78 | City of Camrose | City of Camrose - Heritage Survey and Inventory | 29999.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-03619 |
| ca_alberta_apc:AB-2025-04617:f78da450-5359-44ef-828e-712da9eb6c2b | City of St. Albert | City of St. Albert - Negotiated Request for Proposal - Engineering Services for 2025 Utility Master Plan | 798406.35 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04617 |
| ca_alberta_apc:AB-2025-04995:538e49f5-3fce-4798-8ab3-5d206268bff9 | MacEwan University | MacEwan University - Request for Proposal - Architect Prime Consultant for Faculty of Science Labs - RFP (Consecutive Negotiations) | 107000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-04995 |
| ca_alberta_apc:AB-2025-05628:e0484781-cdcc-4ad9-bb22-d97fa27e146f | City of Calgary | City of Calgary - Invitation to Bid - RFSO 25-2020 For Design and Construction Contract Administration of Pressurized Sewer Collection System Facilities |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-05628 |
| ca_alberta_apc:AB-2025-05628:4a37e433-03e8-40c5-91c4-4ee1a49ee538 | City of Calgary | City of Calgary - Invitation to Bid - RFSO 25-2020 For Design and Construction Contract Administration of Pressurized Sewer Collection System Facilities |  |  |  | https://purchasing.alberta.ca/posting/AB-2025-05628 |
| ca_alberta_apc:AB-2025-05935:3d2f10bb-6f8b-4375-9d8b-632183cb5d6c | City of St. Albert | City of St. Albert - Request for Proposal - Carrot Creek Erosion and Sediment Control (Multiple Locations) | 529709.55 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05935 |
| ca_alberta_apc:AB-2026-00358:158b8b34-3a8c-4763-8991-2a0dcb377b86 | University of Lethbridge | University of Lethbridge - Request for Proposal - Sports Dome - Provision of Consulting and Design Services | 1.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00358 |
| ca_alberta_apc:AB-2026-00435:20d812dc-84a8-429f-8467-bf4d92a75ede | The Good Samaritan Society (A Lutheran Social Service Organization) | The Good Samaritan Society (A Lutheran Social Service Organization) - Request for Quotes - Commissioning Services | 86975.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-00435 |
| ca_alberta_apc:AB-2026-01650:d3582333-a440-4d67-ab43-1a1cea860050 | Infrastructure | Infrastructure - Request for Proposal - RFP FOR CONSULTANT SERVICES FOR EDMONTON – JOHN E BROWNLEE BUILDING – ASSESSMENT AND FEASIBILITY STUDY | 408358.86 |  |  | https://purchasing.alberta.ca/posting/AB-2026-01650 |
| ca_bc_ministry_awards:a37d15c781ff9e6b | Ministry of Transportation and Infrastructure | As and When Expert Earthquake Engineering Consulting Services | 50000.0 |  |  | https://catalogue.data.gov.bc.ca/dataset/9bff5da9-fced-4671-8ff3-f6117e5c8266/resource/576417ba-791e-4727-8f74-f7f6955a5190/download/ministry-contract-awards-oct-to-dec-2020.csv |
| ca_bidsandtenders:75c6ce1c-6cf3-4d3a-b358-a28294d55404:1 | Regional Municipality of Wood Buffalo | Flood Mitigation - Hangingstone Expansion Area - Pre-Design |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/75c6ce1c-6cf3-4d3a-b358-a28294d55404 |
| ca_bidsandtenders:951d03d1-fc0c-40d9-a7ec-4033e34c9978:1 | City of Lethbridge | 2026 Parks Drainage Repairs - Consulting Services | 46899.0 |  |  | https://lethbridge.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/951d03d1-fc0c-40d9-a7ec-4033e34c9978 |
| ca_bidsandtenders:3d4db0b7-9bdb-49d4-941b-9558423d220a:1 | Regional Municipality of Wood Buffalo | Fort McKay Raw Water Supply Infrastructure – Design and Construction Administration Services |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3d4db0b7-9bdb-49d4-941b-9558423d220a |
| ca_bidsandtenders:898a9191-de71-4f76-8890-b41b1e905b90:1 | EPCOR Canada | EPCOR Harmony 2027 Cost of Service Design Study for Water and Wastewater |  |  |  | https://epcor.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/898a9191-de71-4f76-8890-b41b1e905b90 |
| ca_bidsandtenders:87eb5b68-0df9-424a-8d7d-38efa756e764:1 | City of Saskatoon | Consultant Services for Make-Up Air System Upgrade and Structural Design | 55270.0 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/87eb5b68-0df9-424a-8d7d-38efa756e764 |
| ca_bidsandtenders:3bc00a75-a7be-4d00-ab11-72a47bd5326e:1 | City of Yellowknife | 2026 Water and Sewer Upgrade Program Engineering Services | 655649.6 |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3bc00a75-a7be-4d00-ab11-72a47bd5326e |
| ca_bidsandtenders:a861085f-57f0-4454-8122-23e8868c187b:1 | City of Yellowknife | Niven Lake Ravine Consultation, Design and Construction Management Services |  |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a861085f-57f0-4454-8122-23e8868c187b |
| ca_bidsandtenders:0a6cfcbb-923a-47c7-9f9e-d8ebd9596dee:1 | City of Medicine Hat | Consultant Engineering Services - Wastewater Treatment Plant 2026 Shoreline Protection | 344240.06 |  |  | https://medicinehat.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0a6cfcbb-923a-47c7-9f9e-d8ebd9596dee |
| ca_bidsandtenders:944e5fe0-7762-4f88-8a79-5fced776e77b:1 | City of Camrose | 2026 Sidewalk and Paved Trail Condition Assessments | 67945.0 |  |  | https://camrose.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/944e5fe0-7762-4f88-8a79-5fced776e77b |
| ca_bidsandtenders:4abb60c7-e9da-4bf1-8919-963384d46e8d:1 | Regional Municipality of Wood Buffalo | Saline Creek Borrow Pit Management and Reclamation |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4abb60c7-e9da-4bf1-8919-963384d46e8d |
| ca_bidsandtenders:300393d7-5465-47af-88c5-20a797098a88:1 | City of Yellowknife | Facility Use Study |  |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/300393d7-5465-47af-88c5-20a797098a88 |
| ca_bidsandtenders:a21ca9c2-e033-42d6-a37e-8622706aab28:1 | Regional Municipality of Wood Buffalo | Fort Chipewyan Mackenzie Avenue Sidewalk Feasibility Study |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a21ca9c2-e033-42d6-a37e-8622706aab28 |
| ca_bidsandtenders:3fe9b1df-42e0-4a17-b29d-f5f902dffabc:1 | Regional Municipality of Wood Buffalo | Conklin Northland Drive Walking Trail Rehabilitation and Addition |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3fe9b1df-42e0-4a17-b29d-f5f902dffabc |
| ca_bidsandtenders:5c21e721-7c02-4af5-8351-413fdd8c38c0:6 | Government of Yukon | Aviation Technical Advisory and Engineering Services |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5c21e721-7c02-4af5-8351-413fdd8c38c0 |
| ca_bidsandtenders:364a2324-6d71-47e4-a44e-0d85249ce70c:1 | City of St. Albert | Carrot Creek Erosion and Sediment Control (Multiple Locations) |  |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/364a2324-6d71-47e4-a44e-0d85249ce70c |
| ca_bidsandtenders:22a8f944-2d8d-415a-b400-3ac7befee459:1 | City of Saskatoon | North Siphon Chambers Inspection and Condition Assessment | 90000.0 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/22a8f944-2d8d-415a-b400-3ac7befee459 |
| ca_bidsandtenders:350c562a-339e-4cd5-a991-9b0252f8cffd:1 | City of St. Albert | Badger Lands Environmental Study | 59942.0 |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/350c562a-339e-4cd5-a991-9b0252f8cffd |
| ca_bidsandtenders:0f654215-9b9c-4196-a52a-6f94f5b6bbc3:1 | City of St. Albert | Engineering Services for 2025 Utility Master Plan | 798406.35 |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0f654215-9b9c-4196-a52a-6f94f5b6bbc3 |
| ca_bidsandtenders:6efdac82-cb48-42fc-9c58-f3b869e9a21c:1 | City of Camrose | Heritage Survey and Inventory | 29999.0 |  |  | https://camrose.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6efdac82-cb48-42fc-9c58-f3b869e9a21c |
| ca_bidsandtenders:0a576d69-8b93-4afb-a84a-720c9b87cd8d:1 | City of Saskatoon | Consulting Services - Digester Tank B Refurbishment | 481969.77 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0a576d69-8b93-4afb-a84a-720c9b87cd8d |
| ca_bidsandtenders:cd4ac7a7-b117-4072-bbaa-e3b485877d25:1 | EPCOR Canada | RFP - EWSI - 9K - AB - ED - HZ - 2028 PBR Cost of Service Study and Rate Design Scope |  |  |  | https://epcor.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cd4ac7a7-b117-4072-bbaa-e3b485877d25 |
| ca_bidsandtenders:ddea780b-8101-459c-999c-65bce8a9feb0:1 | City of St. Albert | SWMF Condition Assessment and Bathymetric Survey |  |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ddea780b-8101-459c-999c-65bce8a9feb0 |
| ca_bidsandtenders:ec3d87df-af16-46dc-9c11-1d286814af37:1 | City of Yellowknife | Landfill Gas Assessment 2025 |  |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ec3d87df-af16-46dc-9c11-1d286814af37 |
| ca_bidsandtenders:b5a5ac2c-0add-4b6e-8a0f-1828f6fd508e:2 | Government of Yukon | Heritage Assessment SOA |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b5a5ac2c-0add-4b6e-8a0f-1828f6fd508e |
| ca_bidsandtenders:ff2751a7-f130-49f3-be60-c782a86a9da4:1 | City of Saskatoon | Dry Pond Landscape Architectural Design and Construction Management Services | 88546.58 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ff2751a7-f130-49f3-be60-c782a86a9da4 |
| ca_bidsandtenders:6a1c436a-d8af-40fd-9e95-3a83fd9b1ea2:1 | City of Red Deer | Waste Management Facility Cell Redevelopment |  |  |  | https://reddeer.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6a1c436a-d8af-40fd-9e95-3a83fd9b1ea2 |
| ca_bidsandtenders:83a01581-f93e-4dc5-b868-80f89293e919:2 | Government of Yukon | Professional Planning Services, 2025-2028 | 3440.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/83a01581-f93e-4dc5-b868-80f89293e919 |
| ca_bidsandtenders:851c3ef8-74ea-4a45-9c19-cf8f4ac1befb:1 | City of Grande Prairie | Road Condition Assessment & Pavement Management System Update 2025-2027 | 251448.16 |  |  | https://cityofGP.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/851c3ef8-74ea-4a45-9c19-cf8f4ac1befb |
| ca_bidsandtenders:5b81b5ef-801d-4692-93b6-266e7915d4eb:2 | EPCOR Canada | Environmental, Health and Safety (EH&S), and Operation and Maintenance (O&M) Audit Services |  |  |  | https://epcor.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5b81b5ef-801d-4692-93b6-266e7915d4eb |
| ca_bidsandtenders:627623ce-69d3-4d4b-b1cf-2ef7e424fb69:1 | Regional Municipality of Wood Buffalo | Flood Mitigation Reach 1, 2 and 9 Design and Construction Engineering Services |  |  |  | https://rmwb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/627623ce-69d3-4d4b-b1cf-2ef7e424fb69 |
| ca_bidsandtenders:983fcaf3-5ecd-4e02-b0cc-11afc6da6ba8:1 | Government of Yukon | Geoexchange Exploration Program – Design & Technical Administration | 248322.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/983fcaf3-5ecd-4e02-b0cc-11afc6da6ba8 |
| ca_bidsandtenders:8e876747-51aa-44be-9a11-4c6015a0a994:9 | Government of Yukon | Consultant Services for Green Energy Projects |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8e876747-51aa-44be-9a11-4c6015a0a994 |
| ca_bidsandtenders:16d4116e-6228-4306-bbd2-92a108236720:1 | City of Yellowknife | Climate Action Plan 2026-2036 | 75.34 |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/16d4116e-6228-4306-bbd2-92a108236720 |
| ca_bidsandtenders:2d48d8f3-265c-4c3d-a4cd-734143578191:1 | City of Yellowknife | Engineering Services - 2025 & 2026 Paving Program | 748908.51 |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2d48d8f3-265c-4c3d-a4cd-734143578191 |
| ca_bidsandtenders:25645490-1e28-48a6-ac5d-ebe1ce735e45:1 | City of Yellowknife | Engineering Services – Fiddler’s Lagoon Sludge Removal Options | 74982.36 |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/25645490-1e28-48a6-ac5d-ebe1ce735e45 |
| ca_bidsandtenders:9d1d6795-de4f-4d11-a128-46f277f1c8e6:1 | City of St. Albert | Annual Groundwater Sampling Program |  |  |  | https://stalbert.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9d1d6795-de4f-4d11-a128-46f277f1c8e6 |
| ca_bidsandtenders:c9f41343-18ff-46d3-8685-ccafe61f1e79:12 | Government of Yukon | Building Engineering and Design Services |  |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c9f41343-18ff-46d3-8685-ccafe61f1e79 |
| ca_bidsandtenders:00bd0cf8-a634-4b00-8454-875187302143:6 | Government of Yukon | Survey Services 2024-2027 | 19670.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/00bd0cf8-a634-4b00-8454-875187302143 |
| ca_bidsandtenders:c7d90529-2940-40cf-9116-ab2d8cf3570b:1 | City of Yellowknife | Engineering Services - 2025 Water & Sewer Upgrade Program | 524867.9 |  |  | https://yellowknife.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c7d90529-2940-40cf-9116-ab2d8cf3570b |
| ca_bidsandtenders:91cbafed-a58c-47bd-a7d5-48280289b383:10 | Government of Yukon | Environmental Services and Regulatory Submissions Support 2024-2027 | 23575.0 |  |  | https://yukon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/91cbafed-a58c-47bd-a7d5-48280289b383 |
| … 140 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane). Budget rule (PLAN §4d): layer 1 already carries this buyer's confirmed channel, PO rule and terms with quotes; the notes below add only what changes how the invoice is built.

**Row is complete as published** (Aquatera's PO terms updated 2026-10-26: "must include" the PO number; submission instruction in `invoicing_requirements`;
confirmed AP mailbox). Aquatera Utilities Inc. is a municipally controlled corporation (Grande Prairie, AB) — a taxable purchaser: GST 5 % (Alberta,
no PST). Stantec bills from Stantec Consulting Ltd. (Canadian entity) — the registry name in the row; project / PO number on every progress invoice.

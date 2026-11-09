# S5-36 — University of Prince Edward Island ⇄ Acme United Limited (DBA First Aid Central)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: University of Prince Edward Island — 550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3 — buyer tax no. 108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
SUBMIT TO: financialservices@upei.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Acme United Limited — 2139 Dagenais W Blvd, Laval, QC, H7L 5W9, CA | GST/HST number not public | NEQ 1175126672
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Eastern Canada Westcott Retailers School Tools
```

## Relationship
- **rank_group**: E3
- **data_quality_score**: 55
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University of Prince Edward Island (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Acme United Limited (DBA First Aid Central) | subject: Eastern Canada Westcott Retailers School Tools | published by: the Canada-located vendor's own website | record: https://www.acmeunited.ca/BacktoSchool/Regional-Retailers-Eastern-Canada.php | vendor in Canada because: vendor located in Canada (v)=acmeunited.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:202af86fb66c7727
- **tier**: E
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: University of Prince Edward Island
- **buyer_website**: https://bookstore.upei.ca/
- **buyer_address**: 550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3
- **buyer_contact_evidence_url**: https://www.upei.ca/contact
- **buyer_legal_name_as_published**: University of Prince Edward Island
- **buyer_bn_as_published**: 108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 108162108RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://bookstore.upei.ca/theme/images/logo-upei-new.png
- **buyer_website_status**: site answers
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1030305; public university; open-access publisher; public research university; charitable organization
- **buyer_founded**: 1969-00-00 (Wikidata Q1030305, official website on the organisation's domain (http://upei.ca/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 73467388 Q1104069; 83786809 Q1104069; 86072514 Q1104069; 89867565 Q1104069; 99507947 Q1104069; 104494405 Q1104069; 11514 (Wikidata Q1030305, official website on the organisation's domain (http://upei.ca/) + name; 2026-11-08)
- **buyer_employees**: 795; 840; 896; 937; 943; 1400; 950; 1062; 919; 770; 755; 696; 877; 912; 971; 929; 1116; 1274; 1350; 1250 (Wikidata Q1030305, official website on the organisation's domain (http://upei.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.upei.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: financialservices@upei.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.upei.ca/financial-services
- **email_evidence_quote**: ble, Research Accounting, and Data Control and Banking. The Financial Services Office reports directly to the Comptroller. General contact: financialservices@upei.ca 902-566-6000 Financial Services Full Site Accounts Payable Petty Cash Procedures Professional Development Travel Reimburseme
- **email_evidence_context**: unit is comprised of five separate sections which include Student Accounts, Accounts Receivable, Accounts Payable, Research Accounting, and Data Control and Banking. The Financial Services Office reports directly to the Comptroller. General contact: financialservices@upei.ca 902-566-6000 Financial Services Full Site Accounts Payable Petty Cash Procedures Professional Development Travel Reimbursement (PDTR) Purchases Requisitions Suppliers T4As Accounts Receivable Manual Invoicing Wire Transfers Data Control and Banking (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: financialservices@upei.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.upei.ca/financial-services | quote: "ble, Research Accounting, and Data Control and Banking. The Financial Services Office reports directly to the Comptroller. General contact: financialservices@up" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF without an all mechanism; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-001266
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF without an all mechanism; mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; sp=none; rua=mailto:dmarcreports@upei.ca,mailto:dmarc_agg@vali.email; ruf=mailto:dmarcreports@upei.ca; fo=1; 
- **dmarc_record_domain**: upei.ca
- **spf_policy**: SPF without an all mechanism
- **spf_record**: v=spf1 include:spf.protection.outlook.com redirect=upei.ca.on.autospf.email
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 902-566-6000 (as printed on https://www.upei.ca/financial-services, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "902-566-6000 (as printed on https://www.upei.ca/financial-services, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of Prince Edward Island — 550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3 — buyer tax no. 108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: financialservices@upei.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Acme United Limited — 2139 Dagenais W Blvd, Laval, QC, H7L 5W9, CA | GST/HST number not public | NEQ 1175126672 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Eastern Canada Westcott Retailers School Tools
- **invoice_card_json**: {"bill_to": {"legal_name": "University of Prince Edward Island", "legal_name_is_published": true, "address": "550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3", "address_is_the_invoice_address": false, "tax_number": "108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "financialservices@upei.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Prince Edward Island)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Acme United Limited (DBA First Aid Central)
- **vendor_legal_name**: Acme United Limited
- **vendor_trading_name**: Acme United Limited (DBA First Aid Central)
- **vendor_registry_id**: Québec REQ (NEQ): 1175126672
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 183 ST Durham W, Mount Forest (ON), N0G2L1
- **vendor_neq**: 1175126672 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Vente d'outils, de fournitures de bureau et de sécurité
- **vendor_employees_quebec**: De 26 à 49
- **vendor_establishments_quebec**: Premiers Soins Plus: 2139 BOUL. Dagenais O, Laval (Québec), H7L5W9
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 2139 Dagenais W Blvd, Laval, QC, H7L 5W9, CA
- **vendor_country_basis**: vendor located in Canada (v)=acmeunited.ca
- **vendor_website**: https://www.acmeunited.ca/
- **vendor_phone**: 1-800-265-2310
- **vendor_contact_evidence_url**: https://acmeunited.ca/AcmeContact.php
- **vendor_logo_url**: https://acmeunited.ca/images/logo.gif
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Québec REQ (NEQ): 1175126672 status Québec REQ (NEQ): Immatriculée (2020-01-07) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 1980-07-17; phone / role e-mails / logo: the vendor's own site, https://acmeunited.ca/AcmeContact.php (tools/org_contacts.py, org_extras.py); website: https://www.acmeunited.ca/ (site answers); NEQ: 1175126672 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2020-01-07)
- **vendor_incorporation_date**: 1980-07-17
- **vendor_years_in_business**: 46.3 (since 1980-07-17, registry date)

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Eastern Canada Westcott Retailers School Tools
- **contract_description**: Eastern Canada Westcott Retailers School Tools (the record's title; the source publishes no separate description)
- **contract_link**: https://www.acmeunited.ca/BacktoSchool/Regional-Retailers-Eastern-Canada.php
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 108162108RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (Prince Edward Island) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: University of Prince Edward Island — 550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3 — buyer tax no. 108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: financialservices@upei.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Acme United Limited — 2139 Dagenais W Blvd, Laval, QC, H7L 5W9, CA | GST/HST number not public | NEQ 1175126672 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Eastern Canada Westcott Retailers School Tools
- **invoice_card_json**: {"bill_to": {"legal_name": "University of Prince Edward Island", "legal_name_is_published": true, "address": "550 University Ave, Charlottetown, Prince Edward Island, Canada C1A 4P3", "address_is_the_invoice_address": false, "tax_number": "108162108RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "financialservices@upei.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of PE on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Prince Edward Island)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["financialservices@upei.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.upei.ca/financial-services", "quote: \"ble, Research Accounting, and Data Control and Banking. The Financial Services Office reports directly to the Comptroller. General contact: financialservices@up\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF without an all mechanism; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-001266"], "buyer_facts": ["address and phone: the buyer's own site, https://www.upei.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Québec

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.upei.ca/financial-services | 2026-11-08 | ok |  |  |  | 902-566-6000 |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, acmeunited.ca)
- **status**: ok
- **pages**: 2
- **language**: en
- **logo_url**: https://acmeunited.ca/images/logo.gif
- **logo_basis**: logo image on the site
- **domain**: acmeunited.ca
- **key**: vendor:Acme United Limited (DBA First Aid Central)
- **name**: Acme United Limited (DBA First Aid Central)
- **website**: https://acmeunited.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: First Aid Central
- **legal_name_stated_url**: https://acmeunited.ca/
- **legal_name_stated_quote**: of professionals since 1877 and are engineered for the demands of continuous daily use. What's New… First Aid Central Acme United Canada Ltd is thrilled to announce that today we have acquired the assets of First Aid

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "210 Broadway Avenue, Suite 204, Orangeville, Ontario, Canada, L9W 5G4", "address_country": "CA", "address_url": "https://acmeunited.ca/AcmeContact.php", "address_method": "pattern", "address_quote": "e United Canada Ltd. 210 Broadway Avenue, Suite 204 Orangeville, Ontario Canada L9W 5G4 Phone: 1-800-265-2310 Fax: 1-800-668-2263 Email: [email protected] What's New…", "phone": "1-800-265-2310", "phone_url": "https://acmeunited.ca/AcmeContact.php", "domain": "acmeunited.ca", "key": "vd:acmeunited.ca", "name": "Acme United Limited (DBA First Aid Central)", "website": "https://acmeunited.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | University of Prince Edward Island | Q1030305 | official website on the organisation's domain (http://upei.ca/) + name |  | University of Prince Edward Island | Université de l'Île-du-Prince-Édouard | public university; open-access publisher; public research university; charitable organization |  | Canada | 1969-00-00 | Charlottetown |

## Lanes' verified findings for this buyer (team_buyers)
```
none
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
| ca_alberta_apc:AB-2024-08227:e18a588f-2d43-45c7-9e80-e43a1d8fdd2a | Service Alberta and Red Tape Reduction | Service Alberta and Red Tape Reduction - Request for Quotes - Defibrillators and First Aid Kits  | 2000000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-08227 |
| ca_alberta_apc:AB-2025-00257:6dcd1213-adcd-4791-9908-c86be98d350d | Calgary Roman Catholic Separate School Division | Calgary Roman Catholic Separate School Division - Negotiated Request for Proposal - Request for Proposals For Safety & First Aid Supplies #2025-021 | 100000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00257 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

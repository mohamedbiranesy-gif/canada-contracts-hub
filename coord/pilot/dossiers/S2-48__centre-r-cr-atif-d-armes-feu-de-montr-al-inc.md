# S2-48 — CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. ⇄ Shopify Inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08) — 2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3 — buyer tax no. 834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: info@crafm.com (general mailbox, confirmed by the referee) | invoice portal: https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 54
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (non-profit / association / cultural body, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: Shopify Inc. | subject: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://crafm.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:81c799137de0f730
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.
- **buyer_website**: https://crafm.com/
- **buyer_address**: 2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3
- **buyer_phone**: (514) 635-4867
- **buyer_contact_evidence_url**: https://crafm.com/pages/contact
- **buyer_legal_name_as_published**: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08)
- **buyer_bn_as_published**: 834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 834516544RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://crafm.com/cdn/shop/files/logo_fqtir_white_c2ea5548-2209-4fd7-86e6-49eea73045c7.webp?v=1715626111&width=220
- **buyer_website_status**: site answers
- **buyer_registry_id**: 1163036917 (QC; https://ised-isde.canada.ca/cbr-rec/en/search?q=CENTRE%20R%C3%89CR%C3%89ATIF%20D%27ARMES%20%C3%80%20FEU%20DE%20MONTR%C3%89AL%20INC.); NEQ 1163036917 (Registraire des entreprises du Québec (open data))
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_legal_form**: Société par actions ou compagnie (Canada's Business Registries, QC 1163036917, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://crafm.com/pages/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@crafm.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://crafm.com/policies/refund-policy
- **email_evidence_quote**: <script id="shopify-chat-page-data" type="application/json">{"greetingMessage":"Welcome to CRAFM. How can I help?","customerServiceEmail":"info@crafm.com","onlineStorePasswordProtected":false,"exportCommand":false,"shopName":"CRAFM","translations":[{"key":"agent_chat.panel.open_chat","val
- **mailbox_provenance**: info@crafm.com (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://crafm.com/policies/refund-policy | quote: "<script id="shopify-chat-page-data" type="application/json">{"greetingMessage":"Welcome to CRAFM. How can I help?","customerServiceEmail":"info@crafm.com","onli" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00456
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; fo=0; adkim=r; aspf=r; sp=none; rf=afrf; pct=100; ri=86400
- **dmarc_record_domain**: crafm.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 +a +mx include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Kofax, Tungsten, tungsten
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08) — 2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3 — buyer tax no. 834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@crafm.com (general mailbox, confirmed by the referee) | invoice portal: https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08)", "legal_name_is_published": true, "address": "2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3", "address_is_the_invoice_address": false, "tax_number": "834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@crafm.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Kofax, Tungsten, tungsten", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: Shopify Inc.
- **vendor_legal_name**: Shopify Inc.
- **vendor_trading_name**: Shopify TM (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1169259380; 4261607 (CC)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 151 O'Connor St., Ground Floor, Ottawa (Ontario), K2P2L8
- **vendor_neq**: 1169259380 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Fournisseur des services de logiciel pour commerce.
- **vendor_employees_quebec**: De 50 à 99
- **vendor_establishments_quebec**: Shopify TM: 490 rue De La Gauchetière O, Montréal (Québec), H2Z0B3
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada
- **vendor_bn9**: 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://finance.yahoo.com/
- **vendor_logo_url**: https://s.yimg.com/cv/apiv2/default/finance/favicon-180x180.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://finance.yahoo.com/quote/SHOP/profile/ (Shopify Inc. (SHOP) Company Profile & Facts - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column Home News Fi)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: Québec REQ (NEQ): 1169259380; 4261607 (CC) status Québec REQ (NEQ): Immatriculée (2013-06-21) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 4261607, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2004-09-28; website: https://finance.yahoo.com/; NEQ: 1169259380 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2013-06-21)
- **vendor_incorporation_date**: 2004-09-28
- **vendor_years_in_business**: 22.1 (since 2004-09-28, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, CC 4261607, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **contract_title**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **contract_description**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://crafm.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 834516544RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08) — 2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3 — buyer tax no. 834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: info@crafm.com (general mailbox, confirmed by the referee) | invoice portal: https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. (as registered: Canada's Business Registries, QC 1163036917, 2026-11-08)", "legal_name_is_published": true, "address": "2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3", "address_is_the_invoice_address": false, "tax_number": "834516544 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2023-09-27; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@crafm.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://crafm.com/products/boss-components-cz-shadow-2-tungsten-guide-rod — Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Kofax, Tungsten, tungsten", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@crafm.com (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://crafm.com/policies/refund-policy", "quote: \"<script id=\"shopify-chat-page-data\" type=\"application/json\">{\"greetingMessage\":\"Welcome to CRAFM. How can I help?\",\"customerServiceEmail\":\"info@crafm.com\",\"onli\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00456"], "buyer_facts": ["address and phone: the buyer's own site, https://crafm.com/pages/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: Québec REQ (NEQ): 116925938

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://crafm.com/products/standard-manufacturing-dp-12-dual-tone-black-gold-12ga-18-5-bbl | 2026-11-06 | blocked |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, crafm.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://crafm.com/cdn/shop/files/logo_fqtir_white_c2ea5548-2209-4fd7-86e6-49eea73045c7.webp?v=1715626111&width=220
- **logo_basis**: logo image on the site
- **domain**: crafm.com
- **key**: lead:81c799137de0f730
- **name**: CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.
- **website**: https://crafm.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: CRAFM
- **jsonld_logo**: https://crafm.com/cdn/shop/files/CRAM.png?v=1773172271&width=900
- **jsonld_url**: https://crafm.com
- **jsonld_same_as**: https://www.facebook.com/crafm; https://www.youtube.com/@crafm; https://www.instagram.com/crafm.outlet/; https://twitter.com/CRAFMontreal
- **jsonld_quote**: { "@context": "http://schema.org", "@type": "WebSite", "name": "CRAFM", "url": "https:\/\/crafm.com", "potentialAction": { "@type": "SearchAction", "target": "https:\/\/crafm.com\/search?q={search_term_string}", "query-input": "required name=search_term_string" } }
- **jsonld_page**: https://crafm.com/
- **legal_name_stated**: Club de Tir de Montréal
- **legal_name_stated_url**: https://crafm.com/pages/about-us
- **legal_name_stated_quote**: al Shooting Club (CTM) and the CRAFM Outlet... Come to visit us ! Nous vous présentons le CRAFM, le Club de Tir de Montréal (CTM) et le CRAFM Outlet... Venez nous voir ! Video Histoire de Succès - TVA Pillars of Integrity U
- **mentions**: {'payment_method': {'text': 'interaction and decision within our establishment', 'url': 'https://crafm.com/pages/about-us', 'quote': 'at CRAFM. From our qualified staff to our valued clients and friends, these principles guide every interaction and decision within our establishment. We take pride in fostering a culture of mutual respect and shared enthusiasm for the shooting spor'}}
- **tel_links**: 1-877-635-4867; 1.877.635.4867; 5146354867; +18776354867; (450)455-0033

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2206, 52ieme Avenue, Lachine, Québec, Canada H8T 2Y3", "address_country": "CA", "address_url": "https://crafm.com/pages/contact", "address_method": "pattern", "address_quote": "ore CRAFM & Club de tir de Montréal 2206, 52ieme Avenue, Lachine Québec, Canada H8T 2Y3 Phone: (514) 635-4867 Toll Free: 1-877-635-4867 Fax: (514) 635-4868 Email: info", "phone": "(514) 635-4867", "phone_url": "https://crafm.com/pages/contact", "emails": "info@crafm.com", "emails_url": "https://crafm.com/pages/contact", "domain": "crafm.com", "key": "lead:81c799137de0f730", "name": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.", "website": "https://crafm.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. | found | CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. |  | 1163036917 | QC | Société par actions ou compagnie | Active | 2005-06-07 | Montréal | Québec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=CENTRE%20R%C3%89CR%C3%89ATIF%20D%27ARMES%20%C3%80%20FEU%20DE%20MONTR%C3%89AL%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. | found | CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. |  | NEQ 1163036917 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 2005-06-07 | Montréal | QC | 2206 52e Avenue, Montréal (Québec), H8T2Y3 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:81c799137de0f730",
 "ap_contact_team": {
  "emails": [
   "info@crafm.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@crafm.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://crafm.com/products/standard-manufacturing-dp-12-dual-tone-black-gold-12ga-18-5-bbl",
    "quote": "<script id=\"shopify-chat-page-data\" type=\"application/json\">{\"greetingMessage\":\"Welcome to CRAFM. How can I help?\",\"customerServiceEmail\":\"info@crafm.com\",\"onlineStorePasswordProtected\":false,\"continueAsChip\":true,\"exportCommand\":false,\"shopName\":\"CRAFM\",\"translations\":[{\"key\":\"agent_chat",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.",
    "task_id": "CL-LD-35569"
   },
   {
    "email": "info@crafm.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://crafm.com/",
    "quote": "<script id=\"shopify-chat-page-data\" type=\"application/json\">{\"greetingMessage\":\"Welcome to CRAFM. How can I help?\",\"customerServiceEmail\":\"info@crafm.com\",\"onlineStorePasswordProtected\":false,\"continueAsChip\":true,\"exportCommand\":false,\"shopName\":\"CRAFM\",\"translations\":[{\"key\":\"agent_chat",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.",
    "task_id": "CL-LD-35569"
   },
   {
    "email": "info@crafm.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://crafm.com/policies/refund-policy",
    "quote": "<script id=\"shopify-chat-page-data\" type=\"application/json\">{\"greetingMessage\":\"Welcome to CRAFM. How can I help?\",\"customerServiceEmail\":\"info@crafm.com\",\"onlineStorePasswordProtected\":false,\"exportCommand\":false,\"shopName\":\"CRAFM\",\"translations\":[{\"key\":\"agent_chat.panel.open_chat\",\"val",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "CENTRE RÉCRÉATIF D'ARMES À FEU DE MONTRÉAL INC.",
    "task_id": "CL-WS-00456"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of crafm.com (12 pages, robots.txt respected), no AI, no search engine",
  "site crawl of crafm.com (25 pages, robots.txt respected), no AI, no search engine",
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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

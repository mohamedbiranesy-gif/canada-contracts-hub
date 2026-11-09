# S5-39 — Lyft Canada Inc. ⇄ Crestview Strategy

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08) — 1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08) — buyer tax no. 819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08)
SUBMIT TO: accounting@lyft.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal
REFERENCE: none in the record | PO rule: yes (as published: bon de commande par Lyft? Quelles sont les exig)
FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: null
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 89
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Lyft Canada Inc. (company (private sector), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Crestview Strategy | subject: null | awarded 2026-10-16, start 2026-10-16 | published by: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv) | record: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6563&regId=56585128 | vendor in Canada because: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=222 Queen Suite 1100, Ottawa, ON, K1P 5V9, CAN | status rule: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:63b49abd5529556b
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)

## Buyer
- **buyer**: Lyft Canada Inc.
- **buyer_website**: https://lyft.com
- **buyer_address**: 1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08)
- **buyer_legal_name_as_published**: LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08)
- **buyer_bn_as_published**: 819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 819000126RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://images.ctfassets.net/q8mvene1wzq4/1CReHhI5S5XXFcCwsfNQVF/5b15440986a3dd896a652a06bdb29f6e/Driver_App_Icon_DT.png?w=1500&q=60&fm=
- **buyer_registry_id**: corporation number 9336842 (Corporations Canada (open data); https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=9336842)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: Canada Business Corporations Act (Corporations Canada (open data), corporation number 9336842, 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@lyft.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.lyft.com/suppliers
- **email_evidence_quote**: e facture à partir du portail des fournisseurs ».\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com. "}]}]},"query":{},"pathname":"/suppliers","defaultData":{"componentType":"Page","id":"64RWaRNWRnzltRmKuS0LSn","displayName":"defa
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounting@lyft.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02 | page: https://www.lyft.com/suppliers | quote: "e facture à partir du portail des fournisseurs ».\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00024
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Google Workspace
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:6ig9o43x@ag.dmarcian.com; ruf=mailto:6ig9o43x@fr.dmarcian.com;
- **dmarc_record_domain**: lyft.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:qemailserver.com include:docebosaas.com include:_spf.google.com include:mailgun.org include:amazonses.com include:mail.zendesk.com include:spf_c.oraclecloud.com include:usermail.zohocreator.com include:_spf.salesforce.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **po_required_as_published**: yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08)
- **invoice_portal_url**: supplier / vendor portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08)", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08) — 1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08) — buyer tax no. 819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08) ⏎ SUBMIT TO: accounting@lyft.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: yes (as published: bon de commande par Lyft? Quelles sont les exig) ⏎ FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "legal_name_is_published": true, "address": "1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "language": "fr (invoicing page in French)"}, "submit_to": {"email": "accounting@lyft.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature"
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: fr
- **template_language**: fr (invoicing page in French)
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08))

## Vendor
- **vendor**: Crestview Strategy
- **vendor_legal_name**: Crestview Strategy Inc.
- **vendor_trading_name**: Crestview Strategy
- **vendor_registry_id**: Québec REQ (NEQ): 1181904914
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 330 Bay Street, Unit 10, Toronto (Ontario), M5H2S8
- **vendor_neq**: 1181904914 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Agence internationale d'affaires publiques
- **vendor_employees_quebec**: De 1 à 5
- **vendor_establishments_quebec**: Agence Stratégie Crestview: 2200-1250 boul. René-Lévesque O, Montréal (Québec), H3B4W8
- **vendor_address**: 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA
- **vendor_country_basis**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=222 Queen Suite 1100, Ottawa, ON, K1P 5V9, CAN
- **vendor_website**: https://www.crestviewstrategy.com/
- **vendor_emails**: contactus@crestviewstrategy.com
- **vendor_phone**: +1 416.645.2912
- **vendor_contact_evidence_url**: https://www.crestviewstrategy.com/contact/
- **vendor_logo_url**: https://www.crestviewstrategy.com/wp-content/uploads/2025/02/logo.svg
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)); registry identity: Québec REQ (NEQ): 1181904914 status Québec REQ (NEQ): Immatriculée (2026-03-12) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2025-12-09; phone / role e-mails / logo: the vendor's own site, https://www.crestviewstrategy.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.crestviewstrategy.com/ (site answers); NEQ: 1181904914 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2026-03-12)
- **vendor_incorporation_date**: 2025-12-09
- **vendor_years_in_business**: 0.9 (since 2025-12-09, registry date)

## Contract
- **po_required_as_published**: yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **contract_title**: null
- **contract_description**: null (the record's title; the source publishes no separate description)
- **award_date**: 2026-10-16
- **start_date**: 2026-10-16
- **contract_link**: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=6563&regId=56585128
- **source**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 819000126RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08) — 1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08) — buyer tax no. 819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08) ⏎ SUBMIT TO: accounting@lyft.com (invoicing/AP mailbox, confirmed by the referee) | portal (not confirmed as an invoice channel): supplier / vendor portal ⏎ REFERENCE: none in the record | PO rule: yes (as published: bon de commande par Lyft? Quelles sont les exig) ⏎ FROM / REMIT TO: Crestview Strategy Inc. — 335 - 8th Avenue SW Bankers Hall, Suite 1840, Calgary, AB, T2P 1C9, CA | GST/HST number not public | NEQ 1181904914 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "LYFT CANADA INC. (as registered: Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "legal_name_is_published": true, "address": "1812 Serenity Place, Victoria, BC, V8N 6K2 (registered address; Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "address_is_the_invoice_address": false, "tax_number": "819000126 (Corporations Canada (open data), corporation number 9336842, 2026-11-08)", "language": "fr (invoicing page in French)"}, "submit_to": {"email": "accounting@lyft.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "supplier / vendor portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "portal (not confirmed as an invoice channel)"}, "references_required": {"po_required": "yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: bon de commande par Lyft? Quelles sont les exig) (as printed on https://www.lyft.com/suppliers, re-read 2026-11-08))"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature"
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["accounting@lyft.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02", "page: https://www.lyft.com/suppliers", "quote: \"e facture à partir du portail des fournisseurs ».\\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00024"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))", "registry identity: Québec REQ (NEQ): 1181904914 status Québec REQ (NEQ): Immat

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.lyft.com/suppliers | 2026-11-08 | ok |  | yes (as published: bon de commande par Lyft? Quelles sont les exig) | supplier / vendor portal |  |  |  |  |  | class="sc-7f17c9bc-0 btEOCF"> FAQ – Facturation Quelles sont les étapes suivantes pour un fournisseur après l'émission d'un bon de commande par Lyft? Quelles sont les exigences de Lyft en matière de facturation? Comment  |

## Buyer site facts (org_extras, lyft.com)
- **status**: ok
- **pages**: 6
- **language**: fr
- **legal_name**: Lyft, Inc
- **legal_name_url**: https://www.lyft.com/
- **legal_name_quote**: FR Conditions Confidentialité Déclaration d'accessibilité Vos choix en matière de confidentialité © Lyft, Inc., 2026. CPUC ID No. TCP0032513-P
- **logo_url**: https://images.ctfassets.net/q8mvene1wzq4/1CReHhI5S5XXFcCwsfNQVF/5b15440986a3dd896a652a06bdb29f6e/Driver_App_Icon_DT.png?w=1500&q=60&fm=
- **logo_basis**: logo image on the site
- **domain**: lyft.com
- **key**: lead:63b49abd5529556b
- **name**: Lyft Canada Inc.
- **website**: https://lyft.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Lyft
- **jsonld_logo**: https://cdn.lyft.com/static/lyftcomfe/lyft-logo.svg
- **jsonld_quote**: {"@context":"https://schema.org","@type":"Organization","@id":"https://www.lyft.com/#organization","name":"Lyft","logo":"https://cdn.lyft.com/static/lyftcomfe/lyft-logo.svg"}
- **jsonld_page**: https://www.lyft.com/
- **legal_name_stated**: Federal Arbitration Act
- **legal_name_stated_url**: https://www.lyft.com/terms
- **legal_name_stated_quote**: ATION, as set forth below. This agreement to arbitrate ("Arbitration Agreement") is governed by the Federal Arbitration Act ("FAA"), 9 U.S.C. §§ 1-16, including both the FAA's procedural and substantive provisions. If the F
- **mentions**: {'payment_method': {'text': 'interactions with other members of the public, and we act only as a passive conduit for', 'url': 'https://www.lyft.com/terms', 'quote': "is as provided in Lyft's Privacy Policy . You are solely responsible for your Information and your interactions with other members of the public, and we act only as a passive conduit for your online posting of your Information. You agree to provide and mainta"}}

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, crestviewstrategy.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.crestviewstrategy.com/wp-content/uploads/2025/02/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: crestviewstrategy.com
- **key**: vendor:Crestview Strategy
- **name**: Crestview Strategy
- **website**: https://crestviewstrategy.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Crestview Strategy
- **jsonld_logo**: https://www.crestviewstrategy.com/wp-content/uploads/2025/03/Favicon.svg
- **jsonld_url**: https://www.crestviewstrategy.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.crestviewstrategy.com\/","url":"https:\/\/www.crestviewstrategy.com\/","name":"Top Public Affairs Agency | Crestview Strategy","isPartOf":{"@id":"https:\/\/www.crestviewstrategy.com\/#website"},"about":{"@id":"https
- **jsonld_page**: https://www.crestviewstrategy.com/
- **legal_name_stated**: Crestview Strategy and are
- **legal_name_stated_url**: https://www.crestviewstrategy.com/terms-and-conditions/
- **legal_name_stated_quote**: of Service. Intellectual Property The Site and all of its original content are the sole property of Crestview Strategy and are, as such, fully protected by the appropriate international copyright and other intellectual propert
- **mentions**: {'payment_method': {'text': 'interaction information (such as scrolling, clicks, and mouse-overs), and methods used', 'url': 'https://www.crestviewstrategy.com/privacy-policy/', 'quote': 'clicked), page response times, download errors, length of visits to certain pages on the Site, page interaction information (such as scrolling, clicks, and mouse-overs), and methods used to browse away from the Site) We do not collect any Special Categories of'}}
- **tel_links**: 14166452912; +61.2.8580.5467; 971585868730; 16132323192; 61.2.8580.5467; 416-645-2912 x1

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "330 Bay St, Suite 1000, Toronto ON, Canada , M5H 2S8", "address_country": "CA", "address_url": "https://www.crestviewstrategy.com/contact/", "address_method": "pattern", "address_quote": ".2.8580.5467 Location Details Toronto 330 Bay St, Suite 1000 Toronto ON, Canada M5H 2S8 Email +1 416.645.2912 Location Details Vancouver 555 Burrard Street, Floor 17", "phone": "+1 416.645.2912", "phone_url": "https://www.crestviewstrategy.com/contact/", "emails": "contactus@crestviewstrategy.com", "emails_url": "https://www.crestviewstrategy.com/contact/", "domain": "crestviewstrategy.com", "key": "vd:crestviewstrategy.com", "name": "Crestview Strategy", "website": "https://crestviewstrategy.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Lyft Canada Inc. | ambiguous |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Lyft%20Canada%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Lyft Canada Inc. | found | LYFT CANADA INC. | 819000126 | corporation number 9336842 | Corporations Canada (open data) | Canada Business Corporations Act | Active | 2015-06-16 | Victoria | BC | 1812 Serenity Place, Victoria, BC, V8N 6K2 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |
| buyer | Crestview Strategy | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Lyft Canada Inc. |  |  |  |  |  |  |  |  |  |  |
| b | Crestview Strategy |  |  |  |  |  |  |  |  |  |  |
| v | Crestview Strategy Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:63b49abd5529556b",
 "ap_contact_team": {
  "emails": [
   "accounting@lyft.com",
   "supplierhelp@lyft.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounting@lyft.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "e facture à partir du portail des fournisseurs ».\\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com. \"}]}]},\"query\":{},\"pathname\":\"/suppliers\",\"defaultData\":{\"componentType\":\"Page\",\"id\":\"64RWaRNWRnzltRmKuS0LSn\",\"displayName\":\"defa",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-DT03-00011"
   },
   {
    "email": "accounting@lyft.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "e facture à partir du portail des fournisseurs ».\\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com. \"}]}]},\"query\":{},\"pathname\":\"/suppliers\",\"defaultData\":{\"componentType\":\"Page\",\"id\":\"64RWaRNWRnzltRmKuS0LSn\",\"displayName\":\"defa",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-WS-00024"
   },
   {
    "email": "accounting@lyft.com",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "e facture à partir du portail des fournisseurs ».\\n- Pour toute question supplémentaire concernant les factures ou les paiements, contactez accounting@lyft.com. \"}]}]},\"query\":{},\"pathname\":\"/suppliers\",\"defaultData\":{\"componentType\":\"Page\",\"id\":\"64RWaRNWRnzltRmKuS0LSn\",\"displayName\":\"defa",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-WS-00054"
   },
   {
    "email": "supplierhelp@lyft.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "ures sur des ordres d’achat ouverts, pour mettre à jour votre profil de fournisseur et vérifier les détails de paiement, veuillez contacter supplierhelp@lyft.com.\\n- Si des problèmes techniques vous empêchent d'accéder au portail de soumission de factures, veuillez communiquer avec supplie",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-DT03-00011"
   },
   {
    "email": "supplierhelp@lyft.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "ures sur des ordres d’achat ouverts, pour mettre à jour votre profil de fournisseur et vérifier les détails de paiement, veuillez contacter supplierhelp@lyft.com.\\n- Si des problèmes techniques vous empêchent d'accéder au portail de soumission de factures, veuillez communiquer avec supplie",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-WS-00024"
   },
   {
    "email": "supplierhelp@lyft.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.lyft.com/suppliers",
    "quote": "ures sur des ordres d’achat ouverts, pour mettre à jour votre profil de fournisseur et vérifier les détails de paiement, veuillez contacter supplierhelp@lyft.com.\\n- Si des problèmes techniques vous empêchent d'accéder au portail de soumission de factures, veuillez communiquer avec supplie",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Lyft Canada Inc.",
    "task_id": "CL-WS-00054"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of www.lyft.com (8 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.lyft.com (8 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

## The vendor's other buyers in the dataset (first 60 of 5)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-03629:ba609e34-b53a-4832-9469-d5f988be8fae | Rural Municipalities of Alberta (RMA) | Rural Municipalities of Alberta (RMA) - Request for Proposal - Notice of Request for Proposals for Federal Advocacy Services | 396000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03629 |
| ca_alberta_apc:AB-2025-05490:057f93a7-8137-4b51-9e9f-1107c44ec43e | Rocky View County | Rocky View County - Request for Proposal - RFP-25-014 Prairie Gateway Advocacy Support Final | 400475.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-05490 |
| ca_bidsandtenders:db39e740-c644-4f15-82af-be05630ee65a:1 | Canoe Procurement Group of Canada | Federal Advocacy Services |  |  |  | https://canoe.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/db39e740-c644-4f15-82af-be05630ee65a |
| ca_merx:3958773725:1 | La Cité Collégiale | Services de relations gouvernementales et d’appui stratégique |  |  |  | https://www.merx.com/lacitecollegiale/solicitations/Services-de-relations-gouvernementales-et-d-appui-strat-gique/0000321958?origin=0 |
| ca_merx:2276649010:5 | Toronto Transit Commission - PCM Operating | REQUEST FOR SUPPLIER QUALIFICATION - COMMUNITY RELATIONS COMMUNICATIONS SERVICES | 1.0 |  |  | https://www.merx.com/ttc/ttcpurchasingandsales/solicitations/REQUEST-FOR-SUPPLIER-QUALIFICATION-COMMUNITY-RELATIONS-COMMUNICATIONS-SERVICES/0000230709?origin=0 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

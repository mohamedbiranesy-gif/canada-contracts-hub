# S5-32 — Metrolinx ⇄ Alstom Canada (Alstom Transport Canada Inc.)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08) — 97 Front Street West, Toronto, Ontario M5J 1E6
SUBMIT TO: it.invoices@metrolinx.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX | format: facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: yes (as published: bon de commande? J’ai reçu une notification indiqu)
FROM / REMIT TO: ALSTOM Transport Canada Inc. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08) — Saint-Bruno-de-Montarville, QC | GST/HST number not public | NEQ 1178311404
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express fleets in Toront
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 90
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Metrolinx (organisation (type not stated in the record), CA) — public contract / purchase award with a published end date (dated record): Alstom Canada (Alstom Transport Canada Inc.) | subject: Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express fleets in Toronto, Canada | instrument: O&M contract extension | all identifiers: {"record_id": "private_press:59631005c4ecbedcca53d92630615ceae3b96ac6"} | value: 1300000000 CAD | awarded 2026-03-20, start 2026-03-20, end 2031-12-31 | published by: Cision newswire.ca (CNW Group) press releases | record: https://www.newswire.ca/news-releases/alstom-signs-a-5-year-contract-extension-to-operate-and-maintain-the-go-transit-and-up-express-fleets-in-toronto-canada-895448544.html | vendor in Canada because: Alstom Canada (Canadian subsidiary) performs with ~1,300 staff in GTHA; parent HQ France - flag | status rule: active (published end date today or later) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 1 in the last 12 months; latest 2026-03-20)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:5bb1f5ce64f64535
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Metrolinx
- **buyer_website**: https://metrolinx.com
- **buyer_address**: 97 Front Street West, Toronto, Ontario M5J 1E6
- **buyer_phone**: 416-869-3600
- **buyer_contact_evidence_url**: https://www.metrolinx.com/en/contact-us
- **buyer_legal_name_as_published**: Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08)
- **buyer_logo_url**: https://assets.metrolinx.com/image/upload/v1649772475/Images/Metrolinx/Img-2-Bitmap_vll3cm.png
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q3307451; Crown agency
- **buyer_founded**: 2006-00-00 (Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08)
- **buyer_legal_form**: Crown agency (Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.metrolinx.com/en/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: Electronic Funds Transfer, and shall, if requested by Metrolinx, provide the account information required (as printed on https://assets.metrolinx.com/image/upload/v1663240007/Documents/Metrolinx/IT-2018-NETI-292.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: it.invoices@metrolinx.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract
- **email_evidence_quote**: s Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices
- **email_evidence_context**: erations Invoicing.Stations@metrolinx.com GO Expansion RERInvoices@metrolinx.com Rapid Transit RTI.Invoices@metrolinx.com Subways SubwayInvoices@metrolinx.com Presto PRESTO_AP@metrolinx.com Realty RealtyUtilityBills@metrolinx.com Business Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices directly to Metrolinx Accounts Payable, please send your invoices via email to: payablesrequest@metrolinx.com All payments from Metrolinx to its vendors will be made by Electronic Funds Transfer (EFT). (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: it.invoices@metrolinx.com (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract | quote: "s Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00014
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; pct=100; rua=mailto:dmarc.qua@metrolinx.com
- **dmarc_record_domain**: metrolinx.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:158.106.77.208 ip4:216.71.116.208 ip4:52.254.6.249 ip4:192.29.15.141 include:spf.protection.outlook.com include:service-now.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: invoice format as published: facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/faq, re-read 2026-11-08)
- **invoice_portal_url**: https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: MERX (as printed on https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/faq, re-read 2026-11-08)", "portal_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08)", "requirements_text": "invoice format as published: facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08) — 97 Front Street West, Toronto, Ontario M5J 1E6 ⏎ SUBMIT TO: it.invoices@metrolinx.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX | format: facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: bon de commande? J’ai reçu une notification indiqu) ⏎ FROM / REMIT TO: ALSTOM Transport Canada Inc. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08) — Saint-Bruno-de-Montarville, QC | GST/HST number not public | NEQ 1178311404 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express flee
- **invoice_card_json**: {"bill_to": {"legal_name": "Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08)", "legal_name_is_published": true, "address": "97 Front Street West, Toronto, Ontario M5J 1E6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "it.invoices@metrolinx.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08)", "system": "named on the buyer's page: MERX (as printed on https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/faq, re-read 2026-11-08)", "po_number": "", "contract_or_agreeme
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/fa)

## Vendor
- **vendor**: Alstom Canada (Alstom Transport Canada Inc.)
- **vendor_legal_name**: ALSTOM Transport Canada Inc. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_trading_name**: Alstom Canada (Alstom Transport Canada Inc.)
- **vendor_registry_id**: NEQ 1178311404 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx
- **vendor_registered_address**: 1101 rue Parent, Saint-Bruno-de-Montarville (Québec), J3V6E6 (registered address; Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_neq**: 1178311404 (Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_legal_form**: CIE (société par actions (compagnie)) (Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_address**: Saint-Bruno-de-Montarville, QC
- **vendor_country_basis**: Alstom Canada (Canadian subsidiary) performs with ~1,300 staff in GTHA; parent HQ France - flag
- **vendor_website**: https://www.alstom.com/alstom-canada
- **vendor_logo_url**: https://www.alstom.com/sites/alstom.com/files/2026/02/12/Braunschweig%20Wayside%20site_employee_office_2024_2.jpg
- **vendor_linkedin_url**: https://www.linkedin.com/company/alstom
- **vendor_contacts_found_by**:  lane, referee-verified on 
- **vendor_facts_provenance**: name and address: the record's vendor block (Cision newswire.ca (CNW Group) press releases); registry identity: NEQ 1178311404 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; weak_candidates_only); incorporated / registered: 2023-01-06; role / billing mailboxes researched by the  lane, referee-verified on ; website: https://www.alstom.com/alstom-canada; NEQ: 1178311404 (Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_concentration_top_share**: Alstom Canada (Alstom Transport Canada Inc.): 100% of 1 records
- **vendor_registry_status**: immatriculée (Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08)
- **vendor_registry_match_level**: weak_candidates_only
- **vendor_incorporation_date**: 2023-01-06
- **vendor_years_in_business**: 3.8 (since 2023-01-06, registry date)

## Contract
- **po_required_as_published**: yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/faq, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"record_id": "private_press:59631005c4ecbedcca53d92630615ceae3b96ac6"}
- **contract_title**: Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express fleets in Toronto, Canada
- **contract_description**: Five-year renewal of operations and maintenance services for GO Transit rail operations and UP Express
- **contract_value**: 1300000000
- **currency**: CAD
- **award_date**: 2026-03-20
- **start_date**: 2026-03-20
- **end_date**: 2031-12-31
- **contract_link**: https://www.newswire.ca/news-releases/alstom-signs-a-5-year-contract-extension-to-operate-and-maintain-the-go-transit-and-up-express-fleets-in-toronto-canada-895448544.html
- **source**: Cision newswire.ca (CNW Group) press releases
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: Cision newswire.ca (CNW Group) press releases (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08) — 97 Front Street West, Toronto, Ontario M5J 1E6 ⏎ SUBMIT TO: it.invoices@metrolinx.com (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX | format: facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: yes (as published: bon de commande? J’ai reçu une notification indiqu) ⏎ FROM / REMIT TO: ALSTOM Transport Canada Inc. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178311404, 2026-11-08) — Saint-Bruno-de-Montarville, QC | GST/HST number not public | NEQ 1178311404 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express flee
- **invoice_card_json**: {"bill_to": {"legal_name": "Metrolinx (label per Wikidata Q3307451, official website on the organisation's domain (http://www.metrolinx.com) + name; 2026-11-08)", "legal_name_is_published": true, "address": "97 Front Street West, Toronto, Ontario M5J 1E6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "it.invoices@metrolinx.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract — MERX", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "facture établie avec un bon de commande ( vidéo ) ( pdf ) Voir les détails du bon de commande ( vidéo ) ( pdf ) Vie (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/ressources, re-read 2026-11-08)", "system": "named on the buyer's page: MERX (as printed on https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: bon de commande? J’ai reçu une notification indiqu) (as printed on https://www.metrolinx.com/fr/a-propos-de-nous/faire-des-affaires-avec-metrolinx/ressources-du-portail-isupplier/faq, re-read 2026-11-08)", "po_number": "", "contract_or_agreeme
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["it.invoices@metrolinx.com (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract", "quote: \"s Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00014"], "buyer_facts": ["address and phone: the buyer's own site, https://www.metrolinx.com/en/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (Cision newswire.ca (CNW Group) press releases)", "registry identity: NEQ 1178311404 (Registraire d

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract | 2026-11-08 | ok |  |  | MERX |  |  |  |  |  |  |

## Buyer site facts (org_extras, metrolinx.com)
- **status**: ok
- **pages**: 6
- **v**: 2
- **legal_name_stated**: Union Station Rail Corridor
- **legal_name_stated_url**: https://www.metrolinx.com/en/about-us/annual-reports
- **legal_name_stated_quote**: KB Safety Reports File Type Document Title Date Size PDF Executive Summary – GO 3009 Derailment at Union Station Rail Corridor (USRC), Mile 0.30 2026 327 KB PDF GO 3009 Derailment at Union Station Rail Corridor (USRC), Mile 0.
- **portals**: [{'name': 'Oracle Fusion Cloud (supplier portal)', 'kind': 'e-procurement', 'url': 'https://ehtc.fa.ca2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1', 'on_page': 'https://www.metrolinx.com/en'}]
- **linkedin_url**: https://www.linkedin.com/company/metrolinx/
- **language**: en
- **logo_url**: https://assets.metrolinx.com/image/upload/v1649772475/Images/Metrolinx/Img-2-Bitmap_vll3cm.png
- **logo_basis**: og:image of the home page
- **domain**: metrolinx.com
- **key**: b:5bb1f5ce64f64535
- **name**: Metrolinx
- **website**: https://metrolinx.com/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "97 Front Street West, Toronto, Ontario M5J 1E6", "address_country": "CA", "address_url": "https://www.metrolinx.com/en/contact-us", "address_method": "pattern", "address_quote": "m . Metrolinx Contact Information Office 97 Front Street West, Toronto, Ontario M5J 1E6 Phone : 416-869-3600 See Directions Directions Walking Directions : From Union", "phone": "416-869-3600", "phone_url": "https://www.metrolinx.com/en/contact-us", "domain": "metrolinx.com", "key": "b:5bb1f5ce64f64535", "name": "Metrolinx", "website": "https://metrolinx.com/", "kind": "buyer", "date": "2026-11-08"}

## Vendor site facts (org_extras, alstom.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: ALSTOM SA
- **legal_name_url**: https://www.alstom.com/
- **legal_name_quote**: new tab) English Français Accessibility: partially compliant Site map Cookie Policy Legal Notice © ALSTOM SA 2026
- **logo_url**: https://www.alstom.com/sites/alstom.com/files/2026/02/12/Braunschweig%20Wayside%20site_employee_office_2024_2.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: alstom.com
- **key**: vendor:Alstom Canada (Alstom Transport Canada Inc.)
- **name**: Alstom Canada (Alstom Transport Canada Inc.)
- **website**: https://alstom.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: ALSTOM Holdings
- **legal_name_stated_url**: https://www.alstom.com/legal-notice
- **legal_name_stated_quote**: accepts the terms and conditions contained in this notice. This portal is the exclusive property of ALSTOM Holdings, a public limited company with a capital of 5,720,097,597.30 euros created and governed by French l
- **linkedin_url**: https://www.linkedin.com/company/alstom

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Metrolinx | Q3307451 | official website on the organisation's domain (http://www.metrolinx.com) + name |  | Metrolinx | Metrolinx | Crown agency | Crown agency | Canada | 2006-00-00 | Union Station |
| b | ALSTOM RENEWABLE US LLC |  |  |  |  |  |  |  |  |  |  |
| v | ALSTOM SA |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:5bb1f5ce64f64535",
 "ap_contact_team": {
  "emails": [
   "it.invoices@metrolinx.com",
   "rerinvoices@metrolinx.com",
   "rti.invoices@metrolinx.com"
  ],
  "invoice_portal": null,
  "phone": "416-869-3200",
  "mailing_address": "97 Front Street West, Toronto, ON M5J 1E6, Canada",
  "invoicing_requirements": "Regional transit agency for Greater Toronto and Hamilton Area; vendor invoices submitted via Oracle iSupplier Portal or emailed with supporting documents to iSupplierSupport@metrolinx.com.",
  "evidence": [
   {
    "email": "it.invoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract",
    "quote": "s Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00014"
   },
   {
    "email": "rerinvoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract",
    "quote": "GO Expansion RERInvoices@metrolinx.com Rapid Transit RTI.Invoices@metrolinx.com Subways SubwayInvoices@metrolinx.com Presto PRESTO_AP@metrolinx.com Realty RealtyUt",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00014"
   },
   {
    "email": "rti.invoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.metrolinx.merx.com/public/solicitations/1271823555/abstract",
    "quote": "GO Expansion RERInvoices@metrolinx.com Rapid Transit RTI.Invoices@metrolinx.com Subways SubwayInvoi",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00014"
   },
   {
    "email": "rerinvoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://assets.metrolinx.com/image/upload/v1663236726/Documents/Metrolinx/Important-Message-to-Vendors-Submitting-Invoices-by-Mail.pdf",
    "quote": "GO Expansion RERInvoices@metrolinx.com Rapid Transit",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00062"
   },
   {
    "email": "rti.invoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://assets.metrolinx.com/image/upload/v1663236726/Documents/Metrolinx/Important-Message-to-Vendors-Submitting-Invoices-by-Mail.pdf",
    "quote": "Rapid Transit RTI.Invoices@metrolinx.com Subways",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00062"
   },
   {
    "email": "it.invoices@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://assets.metrolinx.com/image/upload/v1663236726/Documents/Metrolinx/Important-Message-to-Vendors-Submitting-Invoices-by-Mail.pdf",
    "quote": "Business Technology IT.Invoices@metrolinx.com If you are currently sending hard-copy invoices directly to Metrolinx Accounts Payable, please send your invoices via email",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Metrolinx",
    "task_id": "CL-WS-00062"
   },
   {
    "email": "iSupplierSupport@metrolinx.com",
    "type": "invoice_submission",
    "invoice_portal": "https://www.metrolinx.com/en/about-us/doing-business-with-metrolinx/isupplier-resources",
    "phone": "416-869-3200",
    "mailing_address": "97 Front Street West, Toronto, ON M5J 1E6, Canada",
    "requirements": "Regional transit agency for Greater Toronto and Hamilton Area; vendor invoices submitted via Oracle iSupplier Portal or emailed with supporting documents to iSupplierSupport@metrolinx.com.",
    "applies_to": "whole_organisation",
    "page_url": "https://assets.metrolinx.com/image/upload/v1733259290/Documents/Metrolinx/Submit_a_PO-Based_Invoice_User_Guide_v2.0.pdf",
    "quote": "Should this situation arise, please email your invoice along with any necessary supporting documents to iSupplierSupport@metrolinx.com and copy your Metrolinx Business Contact.",
    "retrieved_date": "2026-11-02",
    "found_by": "gemini",
    "verification": "unverified_page_unavailable",
    "source_file": "gemini_buyer_ap_results_batch35.csv",
    "org": "Metrolinx",
    "task_id": "CH-AP-01580"
   }
  ]
 },
 "research_status": {
  "found": 7
 },
 "queries_tried": [
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoic
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| private_press:59631005c4ecbedcca53d92630615ceae3b96ac6 | private_press | ongoing | Alstom signs a 5-year contract extension to operate and maintain the GO Transit and UP express fleets in Toronto, Canada | 1300000000 | CAD |  |  | {} | https://www.newswire.ca/news-releases/alstom-signs-a-5-year-contract-extension-to-operate-and-maintain-the-go-transit-and-up-express-fleets-in-toronto-canada-895448544.html |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| private_press:f22a92366b6c4ea378eec8dd43619c116f205fdc | VIA Rail Canada Inc. | Alstom wins landmark contract to renew VIA Rail Canada's long-distance fleet | 4700000000 |  |  | https://www.newswire.ca/news-releases/alstom-wins-landmark-contract-to-renew-via-rail-canada-s-long-distance-fleet-812452972.html |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

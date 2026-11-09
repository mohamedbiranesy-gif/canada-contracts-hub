# S1-17 — Société de transport de Montréal ⇄ DECASULT INC.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08) — 1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA
SUBMIT TO: facture.comptesapayer@stm.info (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO
REFERENCE: contract 20168351|20168352 (ocds_contract_ids); tender 6000041033 (numero) | PO rule: purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la T
FROM / REMIT TO: DECASULT INC. — 600 de Maisonneuve Ouest ,Suite 3200, Montréal, QC, H3A3J2 | GST/HST 101313286RT0001 (account derived from the BN9) | NEQ 1142909408
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)
DESCRIPTION: S115 - Services d'experts indépendants en vérification de coûts | AMOUNT: 416,594.66 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Société de transport de Montréal (transport / transit authority, QC) — public contract / purchase award with a published end date (dated record): DECASULT INC. | subject: S115 - Services d'experts indépendants en vérification de coûts | instrument: contract | contract number: 20168351|20168352 (ocds_contract_ids); 6000041033 (numero) — the source publishes the award under this tender / notice number and no separate contract number; q | solicitation: 6000041033 (numero) | all identifiers: {"numeroseao": "20156032", "numero": "6000041033", "ocid": "ocds-ec9k95-20156032", "ocds_contract_ids": ["20168351", "20168352"], "ocds_award_ids": ["20168351", "20168352"], "seao_item_id": "69a2966a-0bd5-4bf3-800e-4a9c212c10fc"} | value: 416594.66000000003 CAD | awarded 2026-09-29, start 2026-09-29, end 2030-09-29 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=69a2966a-0bd5-4bf3-800e-4a9c212c10fc | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 2442 records with Canada-located vendors (1431 distinct vendors; 479 in the last 12 months; latest 2026-10-16)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:20ce5c29bd01bb97|b:a8e54c2a44c63bfd
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 2

## Buyer
- **buyer**: Société de transport de Montréal
- **buyer_website**: https://www.stm.info
- **buyer_address**: 1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA
- **buyer_legal_name_as_published**: Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08)
- **buyer_registry_id**: NEQ 8831854607 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: transport / transit authority
- **buyer_sector**: transport / transit
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1817151; transit district
- **buyer_founded**: 2002-00-00; 1861-00-00 (Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08)
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8831854607, 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 2

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: facture.comptesapayer@stm.info
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.stm.info/espace-affaires/fournisseur
- **email_evidence_quote**: el à l’adresse courriel qui vous a été fournie par le demandeur. Si votre facture concerne des biens , envoyez votre facture par courriel à facture.comptesapayer@stm.info Respectez les instructions indiquées sur la confirmation de commande. L’envoi des factures doit respecter les condition
- **email_evidence_context**: our accélérer leur traitement. Si votre facture concerne des services rendus, envoyez votre facture par courriel à l’adresse courriel qui vous a été fournie par le demandeur. Si votre facture concerne des biens , envoyez votre facture par courriel à facture.comptesapayer@stm.info Respectez les instructions indiquées sur la confirmation de commande. L’envoi des factures doit respecter les conditions suivantes : La facture doit être en pièce jointe. L’adresse de comptes à payer est réservée à l’envoi de factures et d’états de (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: facture.comptesapayer@stm.info (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.stm.info/espace-affaires/fournisseur | quote: "el à l’adresse courriel qui vous a été fournie par le demandeur. Si votre facture concerne des biens , envoyez votre facture par courriel à facture.comptesapaye" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task GE-AP-00029
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; ruf=mailto:securiteconformite@stm.info; rua=mailto:securiteconformite@stm.info
- **dmarc_record_domain**: stm.info
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)
- **invoice_portal_url**: SEAO
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SEAO (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08) — 1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA ⏎ SUBMIT TO: facture.comptesapayer@stm.info (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO ⏎ REFERENCE: contract 20168351|20168352 (ocds_contract_ids); tender 6000041033 (numero) | PO rule: purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la T ⏎ FROM / REMIT TO: DECASULT INC. — 600 de Maisonneuve Ouest ,Suite 3200, Montréal, QC, H3A3J2 | GST/HST 101313286RT0001 (account derived from the BN9) | NEQ 1142909408 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08) ⏎ DESCRIPTION: S115 - Services d'experts indépendants en vérification de coûts | AMOUNT: 416,594.66 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08)", "legal_name_is_published": true, "address": "1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "facture.comptesapayer@stm.info", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "20168351|20168352 (ocds_contract_ids); 6000041033 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20168351|201
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20168351|20168352 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: DECASULT INC.
- **vendor_legal_name**: DECASULT INC.
- **vendor_trading_name**: DECAREL CONSULTANTS INC.; DECASULT (other names in the registry)
- **vendor_registry_id**: Corporations Canada (corporation number): 2205301; NEQ 1142909408 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=2205301
- **vendor_registered_address**: 3200-600 Boulevard de Maisonneuve Ouest, Montréal, QC, H3A 3J2, CA
- **vendor_neq**: 1142909408 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 4411 — GESTION DE PROJET DE CONSTRUCTION
- **vendor_employees_quebec**: De 50 à 99
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 1987-06-16
- **vendor_address**: 600 de Maisonneuve Ouest ,Suite 3200, Montréal, QC, H3A3J2
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_bn9**: 101313286
- **vendor_gst_hst_derived**: 101313286RT0001
- **vendor_website**: https://www.decasult.com/
- **vendor_emails**: info@decasult.com
- **vendor_phone**: 514 849-7697
- **vendor_contact_evidence_url**: https://www.decasult.com/contact-decasult/
- **vendor_logo_url**: https://www.decasult.com/wp-content/uploads/2025/06/Logo-blanc.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/decasult/
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Corporations Canada (corporation number): 2205301; NEQ 1142909408 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-02-23) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 2205301 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1987-06-16; phone / role e-mails / logo: the vendor's own site, https://www.decasult.com/contact-decasult/ (tools/org_contacts.py, org_extras.py); website: https://www.decasult.com/ (site answers); NEQ: 1142909408 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Prevost, une division du Groupe Volvo Canada Inc.: 1% of 2442 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-02-23)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1987-06-16
- **vendor_years_in_business**: 39.4 (since 1987-06-16, registry date)
- **vendor_bn_source**: corporations_canada 2205301 (exact match)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20156032", "numero": "6000041033", "ocid": "ocds-ec9k95-20156032", "ocds_contract_ids": ["20168351", "20168352"], "ocds_award_ids": ["20168351", "20168352"], "seao_item_id": "69a2966a-0bd5-4bf3-800e-4a9c212c10fc"}
- **contract_title**: S115 - Services d'experts indépendants en vérification de coûts
- **commodity**: 93151607 Services de vérification publique
- **contract_description**: services; Services professionnels
- **contract_or_agreement_number**: 20168351|20168352 (ocds_contract_ids); 6000041033 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: 6000041033 (numero)
- **award_or_notice_id**: 20156032 (numeroseao); 20168351|20168352 (ocds_award_ids); ocds-ec9k95-20156032 (ocid); 69a2966a-0bd5-4bf3-800e-4a9c212c10fc (seao_item_id)
- **commodity_codes**: UNSPSC 93151607 (Services de vérification publique)
- **contract_value**: 416594.66000000003
- **currency**: CAD
- **award_date**: 2026-09-29
- **start_date**: 2026-09-29
- **end_date**: 2030-09-29
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=69a2966a-0bd5-4bf3-800e-4a9c212c10fc
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 2442
- **records_last_12_months**: 479
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (2441); Cision newswire.ca (CNW Group) press releases (1)
- **records_with_this_vendor**: 2
- **records_in_contract_dataset**: 2442 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Véhicules, composantes et accessoires (45); Produits et matériel pour véhicules de transport (42); Gestion, ressources humaines et administration (41)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 101313286RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08) — 1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA ⏎ SUBMIT TO: facture.comptesapayer@stm.info (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO ⏎ REFERENCE: contract 20168351|20168352 (ocds_contract_ids); tender 6000041033 (numero) | PO rule: purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la T ⏎ FROM / REMIT TO: DECASULT INC. — 600 de Maisonneuve Ouest ,Suite 3200, Montréal, QC, H3A3J2 | GST/HST 101313286RT0001 (account derived from the BN9) | NEQ 1142909408 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: net 30 jours (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08) ⏎ DESCRIPTION: S115 - Services d'experts indépendants en vérification de coûts | AMOUNT: 416,594.66 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Société de transport de Montréal (label per Wikidata Q1817151, official website on the organisation's domain (https://www.stm.info) + name; 2026-11-08)", "legal_name_is_published": true, "address": "1170-800 RUE de La Gauchetière O, Montréal, QC, H5A1J6, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "facture.comptesapayer@stm.info", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) (as printed on https://www.stm.info/espace-affaires/fournisseur, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "20168351|20168352 (ocds_contract_ids); 6000041033 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20168351|201
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: AP phone or contact for follow-up
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["facture.comptesapayer@stm.info (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.stm.info/espace-affaires/fournisseur", "quote: \"el à l’adresse courriel qui vous a été fournie par le demandeur. Si votre facture concerne des biens , envoyez votre facture par courriel à facture.comptesapaye\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task GE-AP-00029"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes)", "registry identity: Corporations Canada (corporation number): 2205301", "NEQ 1142909408 (Registraire des entreprises d

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.stm.info/espace-affaires/fournisseur | 2026-11-08 | ok | net 30 jours | purchase-order terms published (as published: indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande) | SEAO |  |  |  |  | et le plus fiable pour les deux parties. Si le fournisseur n’accorde pas d’escompte de paiement, le terme de paiement standard appliqué est de net 30 jours. Le fournisseur n'a droit à aucun paiement pour un bien ou servi | des taxes applicables Taxe de vente du Québec (TVQ) et taxe sur les produits et services (TPS) indiqués séparément Les numéros d'identification relatifs à la TVQ et la TPS Le numéro de commande De 7 chiffres débutant par |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, decasult.com)
- **status**: ok
- **pages**: 4
- **language**: fr
- **logo_url**: https://www.decasult.com/wp-content/uploads/2025/06/Logo-blanc.svg
- **logo_basis**: logo image on the site
- **domain**: decasult.com
- **key**: vendor:DECASULT INC.
- **name**: DECASULT INC.
- **website**: https://decasult.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Project Management Institute
- **legal_name_stated_url**: https://www.decasult.com/a-propos-decasult/
- **legal_name_stated_quote**: construction, durant lesquels il a déjà occupé le poste de président de la section montréalaise du Project Management Institute (PMI). Au cours de sa carrière, il s’est illustré à la direction de quelques-uns des plus prestigie
- **linkedin_url**: https://www.linkedin.com/company/decasult/
- **tel_links**: -15148497697; 15148497697

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "514 849-7697 , Adresse, 600 boul. de Maisonneuve Ouest, 32e étage, Montréal (QC) H3A 3J2", "address_country": "CA", "address_url": "https://www.decasult.com/contact-decasult/", "address_method": "pattern", "address_quote": "m 514 849-7697 Adresse 600 boul. de Maisonneuve Ouest, 32e étage, Montréal (QC) H3A 3J2 Heures d’affaires 7h30 à 15h30 Réseaux sociaux Suivez-nous sur LinkedIn Contact", "phone": "514 849-7697", "phone_url": "https://www.decasult.com/contact-decasult/", "emails": "info@decasult.com", "emails_url": "https://www.decasult.com/contact-decasult/", "domain": "decasult.com", "key": "vd:decasult.com", "name": "DECASULT INC.", "website": "https://decasult.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Société de transport de Montréal | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Soci%C3%A9t%C3%A9%20de%20transport%20de%20Montr%C3%A9al | 2026-11-08 |
| buyer | DECASULT INC. | found | DECASULT INC. | 101313286 | 2205301 | CC | Business Corporation | Active | 1987-06-16 | Montréal | Quebec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=DECASULT%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Société de transport de Montréal | found | SOCIÉTÉ DE TRANSPORT DE MONTRÉAL |  | NEQ 8831854607 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 2001-12-10 | Montréal | QC | 1170-800 RUE de La Gauchetière O, Montréal (Québec), H5A1J6 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |
| buyer | DECASULT INC. | found | DECASULT INC. |  | NEQ 1142909408 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 1995-02-23 | Montréal | QC | 3200-600 boul. De Maisonneuve O, Montréal (Québec), H3A3J2 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Société de transport de Montréal | Q1817151 | official website on the organisation's domain (https://www.stm.info) + name |  | Société de transport de Montréal | Société de transport de Montréal | transit district |  | Canada | 2002-00-00; 1861-00-00 | Place Bonaventure; Montreal |
| b | DECASULT INC. |  |  |  |  |  |  |  |  |  |  |
| v | DECASULT INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:20ce5c29bd01bb97",
 "ap_contact_team": {
  "emails": [
   "facture.comptesapayer@stm.info",
   "compte.apayer@stm.info",
   "fournisseur@stm.info",
   "cger@transports.gouv.qc.ca"
  ],
  "invoice_portal": null,
  "phone": "418 643-5430",
  "mailing_address": "1170, boulevard Lebourgneuf, bureau 110, Québec (Québec) G2K 2E3",
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "facture.comptesapayer@stm.info",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.stm.info/espace-affaires/fournisseur",
    "quote": "el à l’adresse courriel qui vous a été fournie par le demandeur. Si votre facture concerne des biens , envoyez votre facture par courriel à facture.comptesapayer@stm.info Respectez les instructions indiquées sur la confirmation de commande. L’envoi des factures doit respecter les condition",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Société de transport de Montréal (STM) as agent for Association du transport urbain du Québec (ATUQ) - nine transit authorities and exo",
    "task_id": "GE-AP-00029"
   },
   {
    "email": "compte.apayer@stm.info",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.stm.info/espace-affaires/fournisseur",
    "quote": "ul ce format est accepté. Ne retournez pas des factures déjà envoyées, si requis nous vous contacterons afin d’obtenir une copie. Contact : compte.apayer@stm.info Aucun courriel de confirmation ou de non-conformité Vous ne recevrez aucune confirmation par courriel de la réception de votre",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Société de transport de Montréal (STM) as agent for Association du transport urbain du Québec (ATUQ) - nine transit authorities and exo",
    "task_id": "GE-AP-00029"
   },
   {
    "email": "fournisseur@stm.info",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.stm.info/espace-affaires/fournisseur",
    "quote": "de publication: 19 octobre 2026 Devenir fournisseur Remplissez le formulaire d’enregistrement au répertoire des fournisseurs. Envoyez-le à Fournisseur@stm.info . Nous analysons chaque demande et vous contactons si un besoin se précise. Inscrire mon entreprise (XLSX - 148.35 Ko) Interdicti",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Société de transport de Montréal (STM) as agent for Association du transport urbain du Québec (ATUQ) - nine transit authorities and exo",
    "task_id": "GE-AP-00029"
   },
   {
    "email": "cger@transports.gouv.qc.ca",
    "type": "general_info",
    "invoice_portal": null,
    "phone": "418 643-5430",
    "mailing_address": "1170, boulevard Lebourgneuf, bureau 110, Québec (Québec) G2K 2E3",
    "requirements": null,
    "applies_to": "parent_entity",
    "page_url": "https://www.quebec.ca/gouvernement/ministeres-organismes/transports/coordonnees-structure/supplementaires",
    "quote": "Centre de gestion de l'équipement roulant ... Centre administratif 1170, boulevard Lebourgneuf, bureau 110 Québec (Québec) G2K 2E3 Téléphone : 418 643-5430 Télécopieur : 418 528-5582 Ligne sans frais : 1 866 275-0241 Courriel : cger@transports.gouv.qc.ca",
    "retrieved_date": "2026-04-20",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch01.csv",
    "org": "Ministère des Transports et de la Mobilité durable - CGER (STM as agent for Association du transport urbain du Québec (ATUQ))",
    "task_id": "GE-AP-00029"
   },
   {
    "email": "medias@transports.gouv.qc.ca",
    "type": "general_info",
    "invoice_portal": "https://www.stm.info/fr/a-propos/informations-entreprise-et-financieres/fournisseurs",
    "phone": "514 873-5600",
    "mailing_address": "800, rue De La Gauchetière Ouest, Montréal (Québec) H5A 1J6",
    "requirements": null,
    "applies_to": "parent_entity",
    "page_url": "https://www.quebec.ca/nouvelles/responsables-medias",
    "quote": "Ministère des Transports et de la Mobilité durable Porte-parole auprès des médias Québec : 418 644-4444 Montréal : 514 873-5600 Sans frais : 1 866 341-5724 medias@transports.gouv.qc.ca",
    "retrieved_date": "2026-04-20",
    "found_by": "gemini",
    "verification": "not_found_on_page",
    "source_file": "gemini_buyer_ap_results_batch01.csv",
    "org": "Ministère des Transports et de la Mobilité durable (STM as agent for Association du transport urbain du Québec - ATUQ)",
    "task_id": "GE-AP-00029"
   }
  ]
 },
 "research_status": {
  "found": 5,
  "not_published": 1
 },
 "queries_tried": [
  "site crawl of www.stm.info (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.stm.info (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.stm.info (25 pages, robots.txt respected), no AI, no search engine",
  "\"Société de transport de Montréal\" \"ATUQ\" facturation OR \"comptes à payer\"; site:stm.info facturation OR \"comptes à payer\" OR fournisseurs courriel",
  "STM ATUQ fournisseurs MTMD quebec.ca"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 1)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| private_press:cd57e0d7af45e1c71242ecb64effea716ccfc6da | Nova Bus Inc. (Volvo Group) | Nova Bus makes history by winning a bid for an order of up to 1,229 long-range battery electric buses in Quebec | 583000000 |  |  | https://www.newswire.ca/news-releases/nova-bus-makes-history-by-winning-a-bid-for-an-order-of-up-to-1-229-long-range-battery-electric-buses-in-quebec-858566699.html |

## The vendor's other buyers in the dataset (first 60 of 27)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:pwgsc-tpsgc:700858620 | Public Services and Procurement Canada | Engineering services not elsewhere specified | 17229.0 |  |  | https://search.open.canada.ca/contracts/record/pwgsc-tpsgc,C-2026-2027-Q1-00485 |
| canada_federal:cb:CW2331718 | Department of Public Works and Government Services (PSPC) | TSPS SA (Task Based) - Decasult Inc. |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2331718 |
| canada_federal:cb:CW2432546 | Department of Public Works and Government Services (PSPC) | ProServices SA – Decasult Inc. |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2432546 |
| seao_quebec:1107860:decasult-inc | Université McGill | P0639589 | 30522.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ba1a0520-20b3-4438-ae1b-c165348444ce |
| seao_quebec:1117230:decasult-inc | Université de Montréal - Direction des immeubles | 78000_RÉAFFECTATION DES ESPACES LIBÉRÉS - SITE DE LA MONTAGNE | 4607119.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ef5c1a52-61bd-4fba-8342-fc96950176f0 |
| seao_quebec:1677242:decasult-inc | Parc olympique | Services professionnels d'accompagnement en gestion de projet | 90000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8a309333-5be6-47f9-9a19-4bae619baa80 |
| seao_quebec:1687805:decasult-inc | Université de Montréal - DPMI | 70100_MIL_Expert-conseil_Gestion projet | 6282000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9617551c-29a7-49e8-bae4-f33958ea7e23 |
| seao_quebec:1757661:decasult-inc | Université McGill | 22-001 – Services professionnels de gestion de projet – École de Technologie Supérieurs (ÉTS), HPC Centre-Phase II | 484225.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=476e46ea-c7e3-43df-b8f7-22f893093b62 |
| seao_quebec:1828280:decasult-inc | Université McGill | 22-021 PROJECT MANAGEMENT NO MMP/SEAO | 116531.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f5675685-b646-4d44-843b-69aba031ca72 |
| seao_quebec:20046613:decasult-inc | Ville de Châteauguay. | Analyse économique de son portefeuille de biens immobiliers et l'évaluation sommaire d'un projet de pôle municipal | 129695.41 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c6100cdb-38b3-4913-a791-6a6fc694b9b8 |
| seao_quebec:20113286:decasult-inc | Centre de services scolaire de Laval. |  Services de support en gestion de projet | 98100.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8b81b9b6-3d70-4969-9d3c-8ce65f8be76f |
| seao_quebec:20143177:decasult-inc | Société de transport de Montréal | Services professionnels en estimation | 1246329.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=80144133-7835-475a-9147-e888585b4d60 |
| seao_quebec:20143600:decasult-inc | Ville de Montréal - Service de la Gestion et de la Planification des Immeubles |   Services professionnels pour l'élaboration d'une aide-mémoire pour les paramètres d'estimation des projets. SGPI | 27023.78 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7706d0f5-9f61-4384-9265-289ae81971eb |
| seao_quebec:20156032:decasult-inc | Société de transport de Montréal | S115 - Services d'experts indépendants en vérification de coûts | 416594.66000000003 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=69a2966a-0bd5-4bf3-800e-4a9c212c10fc |
| seao_quebec:20162899:decasult-inc | Société du Palais des Congrès de Montréal | Dossier d’opportunité concernant la modernisation du Palais des congrès de Montréal  | 49000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e689d370-e697-4389-9d11-e4b4b2237776 |
| seao_quebec:20168576:decasult-inc | Parc olympique | Préparation du devis - Opération du nouveau funiculaire de la Tour du stade olympique de Montréal | 48000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c8c3d110-3dba-4fb5-9d8b-2f4a09b1c3a4 |
| seao_quebec:20175206:decasult-inc | Ville de Longueuil | Analyse de risques dans le cadre du projet de rénovation majeur du centre sportif Rosanne-Laflamme | 78183.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ac8f66da-a047-48d5-91bb-bedb794cdbe3 |
| seao_quebec:317985:decasult-inc | Université McGill | Services de gestion de projet pour la rénovation de trois immeubles | 1348997.34 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5aae4b73-cc50-4934-83b2-eb08fb542991 |
| seao_quebec:569196:decasult-inc | Université McGill | P0300668 | 92000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=83f13e62-5091-4073-bd7d-7ac8d412cd2a |
| seao_quebec:574220:decasult-inc | Université de Montréal - Direction des immeubles | 70000 - Équipe maître gestion projets - Const Pav Sciences-Pav Ens+Bib | 10599419.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9fe176a7-c21b-42f2-a343-156976d90366 |
| seao_quebec:581147:decasult-inc | Secrétariat du Conseil du trésor-Service des contrats | Agir à titre de président du comité de revue diligente. | 29000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=017c5487-65e2-4cb7-950e-d3cfd64b10c4 |
| seao_quebec:625321:decasult-inc | Université de Montréal - Direction des immeubles | Université Montréal_ Appel offres Gestion projets, services adm., estimation et approvisionnement  Lot no. 5 | 985469.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=95560ed2-c0ca-4c09-bccb-efffbbc8f85c |
| seao_quebec:636925:decasult-inc | Université McGill | P0370311 | 60000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=11274770-7424-4f37-952b-842c3bf2ca16 |
| seao_quebec:695665:decasult-inc | Université McGill | P0268379 | 63600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c89c6280-fd6c-4726-8b6a-eeeffea3e0eb |
| seao_quebec:695673:decasult-inc | Université McGill | P0270252 | 60900.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=37ed662e-7496-432c-ab56-c1564c1c41b2 |
| ca_montreal_contrats:fonctionnaires-146587-1768326 | Ville de Montréal | SGPI - 2 soumissions - Services professionnels pour l'élaboration d'une aide-mémoire pour les paramètres d'estimation des projets. | 27023.78 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_quebec_city_laval_gatineau_longueuil:laval:13110 | Ville de Laval | Services professionnels - Analyse de réclamation | 36750.0 |  |  | https://www.donneesquebec.ca/recherche/dataset/6acde2c0-6f08-407a-86e2-db49dd0bbb49 |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

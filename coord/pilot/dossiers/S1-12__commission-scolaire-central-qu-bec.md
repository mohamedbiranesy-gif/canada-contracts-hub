# S1-12 — Commission scolaire Central Québec ⇄ Englobe Corp.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: à la Commission scolaire Central Québec — 2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA
SUBMIT TO: payables@cqsb.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO
REFERENCE: contract 20128057 (ocds_contract_ids); tender JSMS10M-Laboratoire (numero) | PO rule: yes (as published: must be confirmed by signing a contract or by issuing a purchase order)
FROM / REMIT TO: Englobe Corp. — 1200, boul. Saint-Martin Ouest, bureau 400,, Laval, QC, H7S2E4 | GST/HST 100524297RT0001 (account derived from the BN9) | NEQ 1167280206
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Mandat - Laboratoire de contrôle - Surveillance | AMOUNT: 73,999.86 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 95
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Commission scolaire Central Québec (school board / school district, QC) — public contract / purchase award with a published end date (dated record): Englobe Corp. | subject: Mandat - Laboratoire de contrôle - Surveillance | instrument: contract | contract number: 20128057 (ocds_contract_ids); JSMS10M-Laboratoire (numero) — the source publishes the award under this tender / notice number and no separate contract number; q | solicitation: JSMS10M-Laboratoire (numero) | all identifiers: {"numeroseao": "20125710", "numero": "JSMS10M-Laboratoire", "ocid": "ocds-ec9k95-20125710", "ocds_contract_ids": ["20128057"], "ocds_award_ids": ["20128057"], "seao_item_id": "895fe4c3-6168-461f-ae38-4a59cef37980"} | value: 73999.86 CAD | awarded 2026-03-19, start 2026-03-19, end 2026-11-18 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=895fe4c3-6168-461f-ae38-4a59cef37980 | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 112 records with Canada-located vendors (89 distinct vendors; 2 in the last 12 months; latest 2026-03-19)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:0738579c7d4219de
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Commission scolaire Central Québec
- **buyer_website**: https://www.cqsb.qc.ca
- **buyer_address**: 2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA
- **buyer_phone**: 418-688-8730
- **buyer_contact_evidence_url**: https://www.cqsb.qc.ca/fr/web/cscq/nous-joindre
- **buyer_legal_name_as_published**: à la Commission scolaire Central Québec
- **buyer_logo_url**: https://www.cqsb.qc.ca/image/layout_set_logo?img_id=438040&t=1793389464879
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/central-quebec-school-board
- **buyer_registry_id**: NEQ 8831849649 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: school board / school district
- **buyer_sector**: education: K-12
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2986738; school board of Quebec; chapel
- **buyer_founded**: 1864-00-00 (Wikidata Q2986738, official website on the organisation's domain (https://www.cqsb.qc.ca/en) + name; 2026-11-08)
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8831849649, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.cqsb.qc.ca/fr/web/cscq/nous-joindre (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: payables@cqsb.qc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.cqsb.qc.ca/en/financial-services/contact-us
- **email_evidence_quote**: payables@cqsb.qc.ca receivables@cqsb.qc.ca Telephone: 418-688-8730 ext. 3000 Fax: 418-688-8281 Quick Links Quick Links Establishment Closures New High
- **email_evidence_context**: nal Payments Contact Us - CQSB Administration - bannière Administration Navigation Menu Mandate Contact Us Policies Forms Financial Services - Contact Us Financial Services - Contact Us To reach a member of the Financial Services: finance@cqsb.qc.ca payables@cqsb.qc.ca receivables@cqsb.qc.ca Telephone: 418-688-8730 ext. 3000 Fax: 418-688-8281 Quick Links Quick Links Establishment Closures New High School COMMITMENT-TO-SUCCESS PLAN Careers Find Your School Parent information Registration Eligibility Summer School C (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: payables@cqsb.qc.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://www.cqsb.qc.ca/en/financial-services/contact-us | quote: "payables@cqsb.qc.ca receivables@cqsb.qc.ca Telephone: 418-688-8730 ext. 3000 Fax: 418-688-8281 Quick Links Quick Links Establishment Closures New High" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00026
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject;rua=mailto:dmarc@cqsb.qc.ca
- **dmarc_record_domain**: cqsb.qc.ca
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 418-688-8730 ext. 3000 (as printed on https://www.cqsb.qc.ca/en/financial-services/contact-us, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: must be confirmed by signing a contract or by issuing a purchase order) (as printed on https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550, re-read 2026-11-08)
- **invoice_portal_url**: SEAO
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SEAO (as printed on https://www.cqsb.qc.ca/documents/37503/90000/2019-12-11_CofC_FR.pdf.pdf/f53df5d6-6389-059e-c766-508622a89c3e?t=1629941312123, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "yes (as published: must be confirmed by signing a contract or by issuing a purchase order) (as printed on https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550, re-read 2026-11-08)", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "418-688-8730 ext. 3000 (as printed on https://www.cqsb.qc.ca/en/financial-services/contact-us, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: à la Commission scolaire Central Québec — 2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA ⏎ SUBMIT TO: payables@cqsb.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO ⏎ REFERENCE: contract 20128057 (ocds_contract_ids); tender JSMS10M-Laboratoire (numero) | PO rule: yes (as published: must be confirmed by signing a contract or by issuing a purchase order) ⏎ FROM / REMIT TO: Englobe Corp. — 1200, boul. Saint-Martin Ouest, bureau 400,, Laval, QC, H7S2E4 | GST/HST 100524297RT0001 (account derived from the BN9) | NEQ 1167280206 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Mandat - Laboratoire de contrôle - Surveillance | AMOUNT: 73,999.86 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "à la Commission scolaire Central Québec", "legal_name_is_published": true, "address": "2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "payables@cqsb.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.cqsb.qc.ca/documents/37503/90000/2019-12-11_CofC_FR.pdf.pdf/f53df5d6-6389-059e-c766-508622a89c3e?t=1629941312123, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: must be confirmed by signing a contract or by issuing a purchase order) (as printed on https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "20128057 (ocds_contract_ids); JSMS10M-Laboratoire (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20128057 (ocds_cont
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: payment terms
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; AP phone or AP contact | missing: finance mailbox; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: fr/en
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20128057 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: Englobe Corp.
- **vendor_legal_name**: Englobe Corp.
- **vendor_trading_name**: Arrow, une division d'Englobe Corp.; BIOGÉNIE S.R.D.C.; BIOGÉNIE, DIVISION CARACTÉRISATION ET RÉHABILITATION DE SITES; BIOGÉNIE, DIVISION CRS; BIOGÉNIE, DIVISION GESTION DE MATIÈRES RÉSIDUELLES; BIOGÉNIE, DIVISION GMR; BIOGÉNIE, DIVISION VALORISATION AGRICOLE; BIOGÉNIE, GMRO; Biogénie; Biogénie, une (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1167280206; NEQ 1167280206 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 1200 Saint-Martin West Blvd., Suite 400, Laval, QC, H7S 2E4, CA
- **vendor_neq**: 1167280206 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 4039 — Services spécialisés en génie des sols, des matériaux et de l'environnement
- **vendor_employees_quebec**: De 1000 à 2499
- **vendor_establishments_quebec**: EnGlobe: 363 rue Joseph-Gagné S, Saguenay (Québec), G7B3P6; EnGlobe: 4222 boul. Bourque, Sherbrooke (Québec), J1L1W6; EnGlobe: 1309 boul. Saint-Paul, Saguenay (Québec), G7J3Y2
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2026-02-01
- **vendor_address**: 1200, boul. Saint-Martin Ouest, bureau 400,, Laval, QC, H7S2E4
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_bn9**: 100524297
- **vendor_gst_hst_derived**: 100524297RT0001
- **vendor_website**: https://www.englobecorp.com
- **vendor_phone**: 705 719-0700
- **vendor_contact_evidence_url**: https://www.englobecorp.com/en-ca/contact-us/
- **vendor_logo_url**: https://www.englobecorp.com/apple-touch-icon.png
- **vendor_website_status**: site answers
- **vendor_contacts_found_by**:  lane, referee-verified on 
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Québec REQ (NEQ): 1167280206; NEQ 1167280206 (Registraire des entreprises du Québec (open data)) status Québec REQ (NEQ): Immatriculée (2011-04-07); Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 17652941 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2011-01-13; phone / role e-mails / logo: the vendor's own site, https://www.englobecorp.com/en-ca/contact-us/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the  lane, referee-verified on ; website: https://www.englobecorp.com (site answers); NEQ: 1167280206 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Les Entreprises Québechab Ltée: 3% of 112 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2011-04-07); Corporations Canada (corporation number): Active
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2011-01-13
- **vendor_years_in_business**: 15.8 (since 2011-01-13, registry date)
- **vendor_bn_source**: corporations_canada 17652941 (strong match)

## Contract
- **po_required_as_published**: yes (as published: must be confirmed by signing a contract or by issuing a purchase order) (as printed on https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550, re-read 2026-11-08)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20125710", "numero": "JSMS10M-Laboratoire", "ocid": "ocds-ec9k95-20125710", "ocds_contract_ids": ["20128057"], "ocds_award_ids": ["20128057"], "seao_item_id": "895fe4c3-6168-461f-ae38-4a59cef37980"}
- **contract_title**: Mandat - Laboratoire de contrôle - Surveillance
- **commodity**: 81141500 Contrôle de la qualité
- **contract_description**: services; Services professionnels
- **contract_or_agreement_number**: 20128057 (ocds_contract_ids); JSMS10M-Laboratoire (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: JSMS10M-Laboratoire (numero)
- **award_or_notice_id**: 20125710 (numeroseao); 20128057 (ocds_award_ids); ocds-ec9k95-20125710 (ocid); 895fe4c3-6168-461f-ae38-4a59cef37980 (seao_item_id)
- **commodity_codes**: UNSPSC 81141500 (Contrôle de la qualité)
- **contract_value**: 73999.86
- **currency**: CAD
- **award_date**: 2026-03-19
- **start_date**: 2026-03-19
- **end_date**: 2026-11-18
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=895fe4c3-6168-461f-ae38-4a59cef37980
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 112
- **records_last_12_months**: 2
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (112)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 112 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Nettoyage et entretien de bureaux et de bâtiments divers (3); Construction et maintenance de systèmes de chauffage, de ven (3); Services d'architectes (2)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 100524297RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: à la Commission scolaire Central Québec — 2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA ⏎ SUBMIT TO: payables@cqsb.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): SEAO ⏎ REFERENCE: contract 20128057 (ocds_contract_ids); tender JSMS10M-Laboratoire (numero) | PO rule: yes (as published: must be confirmed by signing a contract or by issuing a purchase order) ⏎ FROM / REMIT TO: Englobe Corp. — 1200, boul. Saint-Martin Ouest, bureau 400,, Laval, QC, H7S2E4 | GST/HST 100524297RT0001 (account derived from the BN9) | NEQ 1167280206 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Mandat - Laboratoire de contrôle - Surveillance | AMOUNT: 73,999.86 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "à la Commission scolaire Central Québec", "legal_name_is_published": true, "address": "2046 ch. Saint-Louis, Québec, QC, G1T1P4, CA", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "payables@cqsb.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.cqsb.qc.ca/documents/37503/90000/2019-12-11_CofC_FR.pdf.pdf/f53df5d6-6389-059e-c766-508622a89c3e?t=1629941312123, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "yes (as published: must be confirmed by signing a contract or by issuing a purchase order) (as printed on https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "20128057 (ocds_contract_ids); JSMS10M-Laboratoire (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20128057 (ocds_cont
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: payment terms
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; AP phone or AP contact | missing: finance mailbox; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["payables@cqsb.qc.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://www.cqsb.qc.ca/en/financial-services/contact-us", "quote: \"payables@cqsb.qc.ca receivables@cqsb.qc.ca Telephone: 418-688-8730 ext. 3000 Fax: 418-688-8281 Quick Links Quick Links Establishment Closures New High\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00026"], "buyer_facts": ["address and phone: the buyer's own site, https://www.cqsb.qc.ca/fr/web/cscq/nous-joindre (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (Système électronique d'appel d'offres du Qué

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.cqsb.qc.ca/en/financial-services/contact-us | 2026-11-08 | ok |  |  |  | 418-688-8730 ext. 3000 |  |  |  |  |  |

## Buyer site facts (org_extras, cqsb.qc.ca)
- **status**: ok
- **pages**: 6
- **language**: fr
- **legal_name**: Tous droits réservés à la Commission scolaire Central Québec
- **legal_name_url**: https://www.cqsb.qc.ca/fr/
- **legal_name_quote**: que masculin est utilisé sans aucune discrimination et uniquement dans le but d'alléger le texte. © Tous droits réservés à la Commission scolaire Central Québec 2021
- **logo_url**: https://www.cqsb.qc.ca/image/layout_set_logo?img_id=438040&t=1793389464879
- **logo_basis**: logo image in the site header
- **domain**: cqsb.qc.ca
- **key**: b:0738579c7d4219de
- **name**: Commission scolaire Central Québec
- **website**: https://cqsb.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/central-quebec-school-board
- **tel_links**: 4186888730; 18002495573

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "418-688-8730", "phone_url": "https://www.cqsb.qc.ca/fr/nous-joindre-nl", "address": "2046, ch. Saint-Louis, Québec, Québec, G1T 1P4", "address_country": "CA", "address_url": "https://www.cqsb.qc.ca/fr/web/cscq/nous-joindre", "address_method": "pattern", "address_quote": "indre - CSCQ - Nous joindre Nous joindre 2046, ch. Saint-Louis, Québec, Québec, G1T 1P4 Téléphone : 418.688.8730 Télécopieur : 418.682.5891 Sans frais : 1-800-249-5573", "domain": "cqsb.qc.ca", "key": "b:0738579c7d4219de", "name": "Commission scolaire Central Québec", "website": "https://cqsb.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, englobecorp.com)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://www.englobecorp.com/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: englobecorp.com
- **key**: vendor:Englobe Corp.
- **name**: Englobe Corp.
- **website**: https://englobecorp.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: National Association
- **legal_name_stated_url**: https://www.englobecorp.com/en-ca/about-us/
- **legal_name_stated_quote**: (CWB) – CSA W178.1 Certified welding inspection organization (Brampton, Laval, Quebec and Saguenay) National Association of Corrosion Engineers (NACE) – Certified engineers and inspectors for corrosion and paint Quebec M
- **tel_links**: +705 719-0700; +905 681-5542; +506 384-5555; +506 384-8899; +905 643-7560; +306 668-1966; +306 382-6000; +1 306 382-6999

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "Barrie (Cambium), 10, Checkley Street, L4N 1W1, Barrie CA, Tel:, 705 719-0700", "address_country": "", "address_url": "https://www.englobecorp.com/en-ca/contact-us/", "address_method": "address-tag", "address_quote": "y . Submit Our Locations Business Offices Barrie (Cambium) 10, Checkley Street, L4N 1W1, Barrie CA Tel: 705 719-0700 Burlington (Tanknology) 1800, Appleby Line, Unit 4", "phone": "705 719-0700", "phone_url": "https://www.englobecorp.com/en-ca/contact-us/", "domain": "englobecorp.com", "key": "vd:englobecorp.com", "name": "Englobe Corp.", "website": "https://englobecorp.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Commission scolaire Central Québec | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Commission%20scolaire%20Central%20Qu%C3%A9bec | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Commission scolaire Central Québec | found | COMMISSION SCOLAIRE CENTRAL QUÉBEC |  | NEQ 8831849649 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 1998-07-22 | Québec | QC | 2046 ch. Saint-Louis, Québec (Québec), G1T1P4 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Commission scolaire Central Québec | Q2986738 | official website on the organisation's domain (https://www.cqsb.qc.ca/en) + name |  | Central Quebec School Board | commission scolaire Central Québec | school board of Quebec; chapel |  | Canada | 1864-00-00 |  |
| v | Englobe Corp. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:0738579c7d4219de",
 "ap_contact_team": {
  "emails": [
   "finance@cqsb.qc.ca",
   "payables@cqsb.qc.ca",
   "achat@cqsb.qc.ca"
  ],
  "invoice_portal": null,
  "phone": "418-688-8730",
  "mailing_address": null,
  "invoicing_requirements": "General school board contact email is cqsb@cqsb.qc.ca (418-688-8730); no separate accounts payable mailbox is published.",
  "evidence": [
   {
    "email": "finance@cqsb.qc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cqsb.qc.ca/fr/service-des-ressources-financieres/nous-joindre",
    "quote": "financières - Nous joindre Service des ressources financières - Nous joindre Pour joindre un membre du Service des ressources financières: finance@cqsb.qc.ca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Commission  scolaire Central Québec",
    "task_id": "GE-AP-00526"
   },
   {
    "email": "payables@cqsb.qc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cqsb.qc.ca/fr/service-des-ressources-financieres/nous-joindre",
    "quote": "payables@cqsb.qc.ca receivables@cqsb.qc.ca Téléphone: 418-688-8730 poste 3000 Télécopieur: 418-688-8281 Liens rapides Liens rapides Fermeture d'établi",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Commission  scolaire Central Québec",
    "task_id": "GE-AP-00526"
   },
   {
    "email": "payables@cqsb.qc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cqsb.qc.ca/en/financial-services/contact-us",
    "quote": "payables@cqsb.qc.ca receivables@cqsb.qc.ca Telephone: 418-688-8730 ext. 3000 Fax: 418-688-8281 Quick Links Quick Links Establishment Closures New High",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Commission scolaire Central Québec",
    "task_id": "CL-WS-00026"
   },
   {
    "email": "finance@cqsb.qc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cqsb.qc.ca/en/financial-services/contact-us",
    "quote": "date Contact Us Policies Forms Financial Services - Contact Us Financial Services - Contact Us To reach a member of the Financial Services: finance@cqsb.qc.ca",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Commission scolaire Central Québec",
    "task_id": "CL-WS-00026"
   },
   {
    "email": "achat@cqsb.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cqsb.qc.ca/fr/service-d-approvisionnement/nous-joindre",
    "quote": "itiques Service de l'approvisionnement - Nous joindre Service de l'approvisionnement - Nous joindre Pour joindre un membre de notre équipe: achat@cqsb.qc.ca Téléphone: 418-688-8730, poste 3051 Télécopieur: 418-688-8281 Liens rapides Liens rapides Fermeture d'établissements Nouvelle école s",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Commission  scolaire Central Québec",
    "task_id": "GE-AP-00526"
   },
   {
    "email": "cqsb@cqsb.qc.ca",
    "type": "general_info",
    "invoice_portal": null,
    "phone": "418-688-8730",
    "mailing_address": null,
    "requirements": "General school board contact email is cqsb@cqsb.qc.ca (418-688-8730); no separate accounts payable mailbox is published.",
    "applies_to": "all_suppliers",
    "page_url": "https://www.cqsb.qc.ca/",
    "quote": "Au besoin, vous pouvez nous contacter par courriel à l'adresse cqsb@cqsb.qc.ca ou par téléphone au 418-688-8730.",
    "retrieved_date": "2026-04-20",
    "found_by": "gemini",
    "verification": "not_found_on_page",
    "source_file": "gemini_buyer_ap_results_batch06.csv",
    "org": "Commission scolaire Central Québec (Central Québec School Board)",
    "task_id": "GE-AP-00526"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of www.cqsb.qc.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.cqsb.qc.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.cqsb.qc.ca (25 pages, robots.txt respected), no AI, no search engine",
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
| seao_quebec:20125710:englobe-corp | seao_quebec | ongoing | Mandat - Laboratoire de contrôle - Surveillance | 73999.86 | CAD |  |  | {"numeroseao": "20125710", "numero": "JSMS10M-Laboratoire", "ocid": "ocds-ec9k95-20125710", "ocds_contract_ids": ["20128057"], "ocds_award_ids": ["20128057"], "seao_item_id": "895fe4c3-6168-461f-ae38- | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=895fe4c3-6168-461f-ae38-4a59cef37980 |
| seao_quebec:865556:englobe | seao_quebec | ongoing_inferred | Création d’un registre électronique des matériaux susceptibles de contenir de l’amiante. | 49307.22 | CAD |  |  | {"numeroseao": "865556", "numero": "CQSB85", "seao_item_id": "dc32c91f-c057-41bb-afe3-4399fb046f22"} | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dc32c91f-c057-41bb-afe3-4399fb046f22 |

## The buyer's other Canadian-vendor records (first 60 of 109)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1025113:informatique-procontact-inc | Informatique ProContact inc. | 2016-04-IT Pare-feu Fortigate | 58346.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=39b0f64d-26ef-4f39-af23-701404f77a8e |
| seao_quebec:1031466:telus-communications-inc | TELUS Communications inc. | 2016-05-IT Système Téléphonique | 52574.27 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a4c19ba7-8f1f-4e5d-9769-eea224e53170 |
| seao_quebec:1060863:construction-a-carrier-inc | Construction A.Carrier Inc. | Réfection de la maçonnerie - École St-Patrick | 548888.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=213478d7-2c3f-4940-8dc6-ea5db425adfe |
| seao_quebec:1070022:les-constructions-beland-lapointe-inc | Les constructions BÉLAND & Lapointe Inc.. | Réfection Blocs sanitaires - fenêtres et finis - École Primaire Holland | 752300.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=03613c93-1b11-4c09-8e21-3588fd36fbd2 |
| seao_quebec:1070522:construction-marc-bolduc-inc | Construction Marc Bolduc Inc. | Réfection toiture et blocs sanitaires - Bishop Mountain | 252000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7e64227d-3635-42db-82bb-5460db7d9b9e |
| seao_quebec:1074194:les-entreprises-quebechab-ltee | Les Entreprises Québechab Ltée | Réfection blocs sanitaires et laboratoire pharmacie | 308400.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a90f23c6-53d3-4961-ab3b-0a3ee27c6c1e |
| seao_quebec:1076017:larouche-construction | Larouche construction | Réfection blocs sanitaires - École MacLean Chibougamau | 140000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=72e57154-2870-43ec-b133-7624bd4db55c |
| seao_quebec:1135548:tessier-recreo-parc-inc | Tessier Récréo-Parc Inc | Fourniture et aménagement d'une aire de jeux 5-12 ans | 61261.33 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0858a0f3-d2bb-42a7-b76b-639de3c79315 |
| seao_quebec:1161417:claveau-fils-inc | Claveau & Fils Inc | Tunnel école Riverside - Imperméabilisation | 61831.55 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=23d3c24a-a922-48d5-8c07-338a23479b06 |
| seao_quebec:1162268:construction-marc-bolduc-inc | Construction Marc Bolduc Inc. | Travaux divers de réfection d'enveloppe et conformité | 112700.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=aed4a383-5e98-467b-9a6e-b9eb74009c72 |
| seao_quebec:1164841:a-plus-construction | A Plus Construction | Réfection des entrées et balcon | 103806.05 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d97d27e7-c7fb-4f48-989c-32bf8597978b |
| seao_quebec:1169986:construction-sipro-inc | Construction Sipro inc. | Rénovation des planchers et vestiaires - Shawinigan High School | 308971.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6a7c292a-1fe7-4a2d-8da5-d6a64ccd20b7 |
| seao_quebec:1170198:av-tech-inc | Av-Tech INC.. | Programme d’entretien préventif Région de Québec et Thetford Mines | 14046.53 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1ffc114b-5cfa-49da-8dc6-80ea44a5ec87 |
| seao_quebec:1170215:multi-energie-best-inc | Multi-Énergie Best Inc | Programme d’entretien préventif Région de la Mauricie | 7469.56 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=292c864f-a067-4d3a-9dad-f1954d54eba1 |
| seao_quebec:1170223:procombustion-inc | Procombustion inc. | Programme d’entretien préventif Région du Saguenay | 2324.97 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6a764d43-47c5-4bc9-874b-8f06840734be |
| seao_quebec:1170230:honeywell-ltee | Honeywell Ltée | Programme d’entretien préventif Région de Chibougamau | 3490.45 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=15f9d870-676a-43ec-9ce2-acf940fd3e3e |
| seao_quebec:1170232:honeywell-ltee | Honeywell Ltée | Programme d’entretien préventif Région de Shefferville | 12794.18 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d2929fc8-d2ae-43b6-b1b1-6021fdff17d9 |
| seao_quebec:1170433:construction-a-ouellet-9016-8436-quebec-inc | Construction A. Ouellet  / (9016-8436 Québec Inc) | Réfection des finis intérieurs | 124000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d8d897bb-eaf7-4839-9d77-7e3714569418 |
| seao_quebec:1172446:novipro | Novipro | Stockage | 32056.68 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f393ec38-9264-4e4f-9452-c50803da137f |
| seao_quebec:1181237:unisource-canada-inc-succursale-de-montreal | Unisource Canada Inc. (Succursale de Montréal) | Papier et carton | 36432.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bab45290-d4f4-4ccd-883e-d1da36a7de4d |
| seao_quebec:1199972:levesque-et-associees-construction-inc | Lévesque et Associées Construction Inc. | Réfection du mur "EST" | 127000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f7bb0748-3abf-4d15-9ee9-0fba3a79f20f |
| seao_quebec:1220112:it-2-go | IT-2-go | 2018-12-IT Serveurs | 24318.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2458d46d-40b9-44dd-a282-9b72a4a27288 |
| seao_quebec:1228155:fdf-construction | FDF Construction. | Travaux divers de réfection - Salles de toilettes/Éclairage/Contrôles et ventilation | 2986817.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=aadad524-e35e-48ac-aba7-7d67872baa08 |
| seao_quebec:1340809:autobus-girardin-inc | Autobus Girardin Inc. | ACHAT D'AUTOBUS SCOLAIRE | 350138.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=691fcc05-37dd-4d82-bf2c-e9767c1556e7 |
| seao_quebec:1479429:bgla-inc | BGLA INC. | Services professionnels - Agrandissement de l'école Riverside Regional Elementary School | 207203.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=87f03f2d-e2c7-4ab3-a87d-54f8901821af |
| seao_quebec:1479429:les-services-exp-inc | LES SERVICES EXP INC. | Services professionnels - Agrandissement de l'école Riverside Regional Elementary School | 461339.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=87f03f2d-e2c7-4ab3-a87d-54f8901821af |
| seao_quebec:1501642:alithya-canada-inc | Alithya Canada inc. | Mise a jour site web et correction failles de sécurité | 35062.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5c346498-a8d5-4000-b775-4a8d33ec8283 |
| seao_quebec:1505950:raymond-chabot-grant-thornton-s-e-n-c-r-l | Raymond Chabot Grant Thornton S.E.N.C.R.L. | Sélection des vérificateurs externes | 109500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ad19c08b-c836-49c1-b8bb-d172aa9b0abf |
| seao_quebec:1836288:mallette-s-e-n-c-r-l | MALLETTE S.E.N.C.R.L. | Services professionnels pour l'audit des états financiers | 270375.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=db899041-6f37-45ec-8042-7629f50ecab8 |
| seao_quebec:20070127:derko-ltee | DERKO LTÉE | APPEL D'OFFRES DE SERVICES SPÉCIALISÉS POUR TRAVAUX D’HYGIÈNE ET SALUBRITÉ | 2647802.27 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7428b0e8-a5d4-4d50-94e8-94d8019c6a3d |
| seao_quebec:20070134:maintenance-eureka-ltee | MAINTENANCE EURÉKA LTÉE | APPEL D'OFFRES DE SERVICES SPÉCIALISÉS POUR TRAVAUX D’HYGIÈNE ET SALUBRITÉ | 490998.93 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=23cc3c4e-4878-44f9-b95d-63a2fd8cb3b3 |
| seao_quebec:20070145:maintenance-eureka-ltee | MAINTENANCE EURÉKA LTÉE | APPEL D'OFFRES DE SERVICES SPÉCIALISÉS POUR TRAVAUX D’HYGIÈNE ET SALUBRITÉ | 638774.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d437595b-0e0e-4b38-9b1d-e874e1371f56 |
| seao_quebec:20070154:maintenance-eureka-ltee | MAINTENANCE EURÉKA LTÉE | APPEL D'OFFRES DE SERVICES SPÉCIALISÉS POUR TRAVAUX D’HYGIÈNE ET SALUBRITÉ | 516841.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a8274660-a0f0-464a-988d-54289b9d7699 |
| seao_quebec:20084405:pro-combustion-inc | PRO COMBUSTION INC. | Programme d'entretien préventif pour les écoles de la Ville de Chibougamau et Ville Saguenay | 26731.68 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b1dc0123-cfaf-4040-a57a-f9cb941f7699 |
| seao_quebec:20084907:multi-energie-best-inc | MULTI-ENERGIE BEST INC. | Programme d’entretien préventif Région de la Mauricie | 36220.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b354a3b2-162c-471e-9535-1b923f325fc1 |
| seao_quebec:20084919:av-tech-inc | av-tech inc. | Programme d’entretien préventif Région de Québec et Thetford Mines | 90856.79 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cf35d238-7006-4da3-818e-dab641df5250 |
| seao_quebec:20084930:av-tech-inc | av-tech inc. | Programme d’entretien préventif Région de Schefferville | 83868.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bef676f5-490c-4332-8d56-c8479e6ddccf |
| seao_quebec:20098464:9210-3837-quebec-inc | 9210-3837 QUÉBEC INC. | Construction de résidences pour le corps professoral | 14757210.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7d98abd0-211f-4aa4-be54-387eb4063a31 |
| seao_quebec:266458:qualite-construction-cdn-ltee | QUALITÉ CONSTRUCTION (CDN) LTÉE. | Agrandissement école primaire de Portneuf | 525524.7 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1ec1faa9-3336-4f76-ae87-515718f682cd |
| seao_quebec:335034:laplante-construction-2006-inc | Laplante Construction (2006) Inc. | Revêtement extérieur - École primaire Holland | 27875.97 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=54905eb9-d835-475f-ba05-5b3f87088923 |
| seao_quebec:335087:les-entreprises-real-berube-inc | Les Entreprises Réal Bérubé inc. | Remplacement Réservoir d'huile - École primaire Valcartier | 14686.4 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=444bea14-b28e-4794-905e-77ae6d6611b4 |
| seao_quebec:335336:carmichael-ltee | Carmichael Ltée.. | Travaux de Ventilation - École St. Vincent | 16722.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=849d459f-effc-4f5d-a102-0f6995730873 |
| seao_quebec:335428:les-constructions-olisa-inc | Les Constructions Olisa inc. | Travaux d'accessibilté universelle - École A.S. Johnson | 64023.62 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b1070384-f9c1-4e00-af89-eba970a2f824 |
| seao_quebec:335440:index-construction | Index Construction | Remplacement de portes - École St. Patrick Secondaire | 83691.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7a00b1df-e67d-46a3-9c38-6911efc52f4f |
| seao_quebec:335481:construction-signature-plus-inc | Construction Signature Plus Inc. | Réamenagement classe menuisier - École St. Patrick Secondaire | 26921.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=03f75161-7cd5-42b7-9b82-45c0bb14b683 |
| seao_quebec:335498:construction-signature-plus-inc | Construction Signature Plus Inc. | Rémenagement classe menuisier - École Quebec High School | 32481.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a68d7fb5-3267-4a58-b0e5-cb23b82f382f |
| seao_quebec:335511:constructions-christian-duchesne | Constructions Christian Duchesne | Réamenagement classe menuisier - École Rverside High | 33720.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=31aa9577-993a-47d6-8184-789943f42bd3 |
| seao_quebec:366914:vitrerie-a-e-fortin-inc | Vitrerie A. & E. fortin inc. | Remplacement des fenêtres et portes École Riverside High | 569900.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=91d8501d-c2cf-4565-bbe2-ae30f46d7f1a |
| seao_quebec:367770:toitures-jules-chabot-inc | Toitures Jules Chabot Inc. | Réfection partielle de la toiture - École Everest | 161000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=29b3a21c-2130-427d-a90f-441d231fc70c |
| seao_quebec:373585:telus | TELUS | Achat et installation d'un système de téléphone IP | 239372.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0dc437a4-6f90-4fbd-a715-04cdbca2bc67 |
| seao_quebec:379356:shalwin-inc | Shalwin Inc. | Remplacement des fenêtres et portes École St. Vincent | 240689.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1be4c25c-c843-48f8-a475-df22885cae57 |
| seao_quebec:384051:construction-mmg-inc | Construction MMG Inc. | Remplacement des fenêtres et portes École A.S. Johnson | 204302.32 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0d6ae49e-d596-4fc3-8640-d3ad9b06a896 |
| seao_quebec:391401:multi-energie-best-inc | Multi-Énergie Best Inc | Réfection Partielle du Réseau d'eau, Shawinigan High School | 113800.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c0a31e01-1c00-4ccf-9965-56d8cddd90e0 |
| seao_quebec:391952:construction-berthin-cloutier-2005-inc | Construction Berthin Cloutier 2005 Inc. | Réfection de la Salle de Toilettes des Filles - La Tuque High School | 93749.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1bb4adc9-2f6f-484e-9bc4-1017996c5ac3 |
| seao_quebec:392941:derko-ltee | Derko Ltée. | Travaux d'Hygiène et Salubrité - St. Patrick's High School | 134971.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9237d00c-3b26-4184-8340-2c3d2cb1c4f1 |
| seao_quebec:406389:toitures-jules-chabot-inc | Toitures Jules Chabot Inc. | Réfection partielle de la toîture - Ste-Foy Elementary School | 120000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e5b54399-5022-44aa-8daa-965236df82a1 |
| seao_quebec:412610:les-constructions-beland-lapointe-inc | Les constructions BÉLAND & Lapointe Inc.. | Agrandissement de l'École Jimmy Sandy Memorial | 2087250.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4a527427-cd2f-4e93-a62b-73cdad1d8b8e |
| seao_quebec:477719:toitures-qualitoit-inc | Toitures Qualitoit Inc | Travaux de tôlerie et de membrane - St. Patrick's School | 22730.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9fe7e7e6-8754-410e-ad5f-8796f591fa85 |
| seao_quebec:477913:simon-robert-inc | Simon Robert Inc. | Réfection et réparations de murs de briques, St. Patrick's School | 57075.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a01a36c8-da69-4314-be1a-0c26495fdc7d |
| seao_quebec:477938:les-entreprises-j-chabot-inc | Les Entreprises J. Chabot Inc | Réfection de la toiture -École primaire Holland | 86500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=11c1c53b-5439-4c54-a75e-f9a1b91d1d69 |
| … 49 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 300)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_alberta_apc:AB-2024-03793:938eb76d-ec0c-4742-a155-fc20df925a17 | Infrastructure | Infrastructure - Request for Proposal - REQUEST FOR PROPOSAL (RFP) for SITE INVESTIGATION CONSULTANT SERVICES for NEW 7-12 GYM FOR THE CALGARY SCHOOL CHARTER HU | 125177.0 |  |  | https://purchasing.alberta.ca/posting/AB-2024-03793 |
| ca_alberta_apc:AB-2025-00169:ed059eba-ae60-4208-b0fe-ff90f74cad54 | Infrastructure | Infrastructure - Request for Proposal - REQUEST FOR PROPOSAL (RFP) for ENGINEERING CONSULTANT SERVICES for Portfolio 1: NORTH AND Portfolio 2: SOUTH Multi-Disci | 2200000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2025-00169 |
| ca_alberta_apc:AB-2026-04568:fdb213d6-3836-42db-a049-3a1628438603 | Transportation and Economic Corridors | Transportation and Economic Corridors - Request for Proposal - CON0025473 - Reach 12 - Check Drop 4 Structure Replacement Waterton St. Mary Headworks System Car | 627225.37 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04568 |
| ca_alberta_apc:AB-2026-04716:52082652-47ee-409a-a61f-41c10057c83a | Rocky View County | Rocky View County - Request for Proposal - RFP 26-012 Graham Creek Reservoir Detailed Engineering Final | 1890000.0 |  |  | https://purchasing.alberta.ca/posting/AB-2026-04716 |
| ca_bidsandtenders:40132e63-dd67-4b65-bdac-e6d5b7324cfd:1 | City of Cornwall | Engineering Design and Construction Administration for Thermal Plant Conversion to Natural Gas Condensing Boilers at the Civic Complex & Aquatic Centre | 86320.0 |  |  | https://cornwall.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/40132e63-dd67-4b65-bdac-e6d5b7324cfd |
| ca_bidsandtenders:f5080894-2521-4d86-9496-edc83ec8e669:1 | Town of Orangeville | Professional Services for SCADA System Replacement and Upgrade |  |  |  | https://orangeville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f5080894-2521-4d86-9496-edc83ec8e669 |
| ca_bidsandtenders:a3a7b49c-0f29-47cf-8eb5-e033a555c160:1 | Newfoundland Labrador Hydro | LIL Access Bridge Upgrade Project – Consultant Support | 616180.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a3a7b49c-0f29-47cf-8eb5-e033a555c160 |
| ca_bidsandtenders:ad924fcd-adc5-461e-8263-082c85bc2424:1 | Newfoundland Labrador Hydro | RFP - Intake Structure Public Safety around Dams - Options Review & Design | 99100.0 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/ad924fcd-adc5-461e-8263-082c85bc2424 |
| ca_bidsandtenders:89b84b98-cebb-4249-9ee1-8f2c53d5dae6:1 | City of Greater Sudbury | Request for Proposal (RFP) for Data Collection Services for Pavement Management System | 144130.8 |  |  | https://greatersudbury.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/89b84b98-cebb-4249-9ee1-8f2c53d5dae6 |
| ca_bidsandtenders:01810e69-3f5a-43d7-b3ee-5e228d1b31b9:1 | Town of Aurora | PARKING LOT CONDITION ASSESSMENT |  |  |  | https://aurora.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/01810e69-3f5a-43d7-b3ee-5e228d1b31b9 |
| ca_bidsandtenders:95ecb000-4fc8-4c03-aad1-d52a928828fe:1 | Halifax Regional Municipality | Eastern Shore Active Transportation Connection Functional Plan |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/95ecb000-4fc8-4c03-aad1-d52a928828fe |
| ca_bidsandtenders:f3003e2f-7257-4c93-b948-35c05723ea19:2 | City of Mount Pearl | Traffic Engineering Services, 2026-2027 |  |  |  | https://mountpearl.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f3003e2f-7257-4c93-b948-35c05723ea19 |
| ca_bidsandtenders:de18bdcc-2672-4bd8-a864-33a46f5d4aff:1 | City of Medicine Hat | WWTP - Solids Equipment Repairs/Replacement Study | 72000.0 |  |  | https://medicinehat.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/de18bdcc-2672-4bd8-a864-33a46f5d4aff |
| ca_bidsandtenders:e56f15a3-c883-46e8-a441-883a19955012:1 | Kneehill County | Village of Carbon-Infrastructure Audit |  |  |  | https://kneehillcounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/e56f15a3-c883-46e8-a441-883a19955012 |
| ca_bidsandtenders:bf3f3efa-fd11-4125-8cc3-607541c24965:1 | York Region | Designated Substances And Hazardous Material Surveys Of Various York Region Water And Wastewater Facilities | 54549.5 |  |  | https://york.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bf3f3efa-fd11-4125-8cc3-607541c24965 |
| ca_bidsandtenders:bd6c6ff4-2b1e-4fcc-8eba-8ec8ebd27d4b:1 | City of Saskatoon | Preston Crossing - CPKC Trenchless Rail Crossing: Geotechnical Design and Support Services | 123583.0 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bd6c6ff4-2b1e-4fcc-8eba-8ec8ebd27d4b |
| ca_bidsandtenders:d72699a1-dcb6-4a99-8dad-fd3070fa7b5e:7 | Town of Aurora | GEOTECHNICAL ENGINEERING SERVICES FOR SOIL AND MATERIAL TESTING |  |  |  | https://aurora.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d72699a1-dcb6-4a99-8dad-fd3070fa7b5e |
| ca_bidsandtenders:0e01725c-a52b-4a61-82ef-16a4791dfa9c:50 | Halifax Regional Municipality | Prequalified Consulting & Professional Services Supplier List |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0e01725c-a52b-4a61-82ef-16a4791dfa9c |
| ca_bidsandtenders:f4284afd-e68f-413e-9e88-c842279c2d4f:73 | Halton District School Board | Consulting Services - Various Categories |  |  |  | https://hdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f4284afd-e68f-413e-9e88-c842279c2d4f |
| ca_bidsandtenders:de301b1f-2c97-42f2-a413-0a8d386fd21e:1 | City of Vaughan | Geotechnical Investigation and Material Testing Services | 1198330.0 |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/de301b1f-2c97-42f2-a413-0a8d386fd21e |
| ca_bidsandtenders:fb01283d-dfdc-49d9-902a-ad26634012b1:1 | City of Mount Pearl | Geotechnical Assessment of City Streets | 114890.75 |  |  | https://mountpearl.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fb01283d-dfdc-49d9-902a-ad26634012b1 |
| ca_bidsandtenders:9e01dc28-2182-4257-9d6f-d18ea497c648:1 | Town of Tillsonburg | Consulting Services for Pavement Condition Assessments |  |  |  | https://tillsonburg.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9e01dc28-2182-4257-9d6f-d18ea497c648 |
| ca_bidsandtenders:98114792-1408-4360-a1b9-09c30f6f4136:1 | United Counties of Leeds and Grenville | Public Works Professional Services Roster |  |  |  | https://leedsgrenville.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/98114792-1408-4360-a1b9-09c30f6f4136 |
| ca_bidsandtenders:5f79d0ae-3c97-4aa9-a82c-c2aef44c0898:7 | City of Barrie | Geotechnical and Environmental Engineering Roster Services |  |  |  | https://barrie.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5f79d0ae-3c97-4aa9-a82c-c2aef44c0898 |
| ca_bidsandtenders:5901af0b-7467-49b7-9edf-0211bce83b24:1 | City of Vaughan | BUILDING CONDITION ASSESSMENT | 65995.0 |  |  | https://vaughan.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5901af0b-7467-49b7-9edf-0211bce83b24 |
| ca_bidsandtenders:d219d836-1320-49d1-98b8-a53f1e9d60f6:1 | City of Red Deer | WTP Vestibule Renovations - Consulting Services | 183279.6 |  |  | https://reddeer.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d219d836-1320-49d1-98b8-a53f1e9d60f6 |
| ca_bidsandtenders:f8db6fb3-43fc-44b6-956c-bccbd548369b:1 | City of Moncton / Ville de Moncton | Feasibility Study - Downtown Moncton Flood Mitigation | 97387.75 |  |  | https://moncton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f8db6fb3-43fc-44b6-956c-bccbd548369b |
| ca_bidsandtenders:8f42ad3e-e047-4cee-a005-c4c08f183342:14 | York Region District School Board | Request for Prequalification for Consultants for Building Envelope |  |  |  | https://yrdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8f42ad3e-e047-4cee-a005-c4c08f183342 |
| ca_bidsandtenders:cdf0f91a-ed0e-48ff-af96-027da4842adf:1 | Newfoundland Labrador Hydro | BDE Bridge Assessment | 80720.36 |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/cdf0f91a-ed0e-48ff-af96-027da4842adf |
| ca_bidsandtenders:d25ed5a4-a883-46ed-9187-9b5248a336f6:1 | Newfoundland Labrador Hydro | RFP - Salmon River Dam Riprap Sizing & Constructability Study |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/d25ed5a4-a883-46ed-9187-9b5248a336f6 |
| ca_bidsandtenders:34a421bb-8175-4dda-8480-ab4f165638d5:1 | Region of Waterloo | Waterloo Regional Housing Unit Inspections and Asbestos Reassessments (Under PQ2025-01) |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/34a421bb-8175-4dda-8480-ab4f165638d5 |
| ca_bidsandtenders:f0324802-a8c6-4325-afc5-fa63d4cf4b2c:1 | City of Mississauga | Sidewalks, Trails, and Engineered Walkway Condition Assessment |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f0324802-a8c6-4325-afc5-fa63d4cf4b2c |
| ca_bidsandtenders:945de047-6392-436b-96f1-d61c17c15ba8:1 | Loyalist Township | Amherstview WPCP Geotechnical Investigation | 21790.0 |  |  | https://loyalist.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/945de047-6392-436b-96f1-d61c17c15ba8 |
| ca_bidsandtenders:108959ec-93b1-4732-94bd-427f457123eb:1 | City of Saskatoon | 2025/2026 Materials Testing | 429325.0 |  |  | https://saskatoon.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/108959ec-93b1-4732-94bd-427f457123eb |
| ca_bidsandtenders:de79a6a4-35f0-4337-8f5a-ff4398b0c0f5:12 | Toronto Catholic District School Board | REQUEST FOR SUPPLIER QUALIFICATIONS for Consultant – Electrical Engineering Services |  |  |  | https://tcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/de79a6a4-35f0-4337-8f5a-ff4398b0c0f5 |
| ca_bidsandtenders:f3eeaf58-5dca-4194-b007-89c522403097:3 | Toronto Catholic District School Board | REQUEST FOR SUPPLIER QUALIFICATIONS for Consultant – Structural Engineering Services |  |  |  | https://tcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f3eeaf58-5dca-4194-b007-89c522403097 |
| ca_bidsandtenders:55e0cdcd-26b9-4408-bad1-cf1eb2302f4d:2 | Toronto Catholic District School Board | REQUEST FOR SUPPLIER QUALIFICATIONS for Consultant – Building Envelope and Foundation Engineering Services |  |  |  | https://tcdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/55e0cdcd-26b9-4408-bad1-cf1eb2302f4d |
| ca_bidsandtenders:15dce555-12ec-4436-a98c-96e656dcbb98:5 | City of Guelph | Environmental Engineering, Hydrogeological, and Geotechnical (EHG) Reporting Services |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/15dce555-12ec-4436-a98c-96e656dcbb98 |
| ca_bidsandtenders:303c04bc-c46c-4671-9843-c87c82b92b50:11 | City of Hamilton | Category 12 - Geotechnical Investigation and Inspection Services |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/303c04bc-c46c-4671-9843-c87c82b92b50 |
| ca_bidsandtenders:fc8992b4-36d3-45e1-8c37-216730e4caaf:2 | City of Hamilton | Category 17 Environmental Assessment |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fc8992b4-36d3-45e1-8c37-216730e4caaf |
| ca_bidsandtenders:40ce4e13-28c7-4f23-8f1a-ce45d751e88b:1 | City of Hamilton | Category 20 - Legislative Compliance |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/40ce4e13-28c7-4f23-8f1a-ce45d751e88b |
| ca_bidsandtenders:3eb3a183-e9d7-4679-b29e-37f4f1b683bd:3 | City of Hamilton | Category 24 - Building Envelope and Roof Consulting |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/3eb3a183-e9d7-4679-b29e-37f4f1b683bd |
| ca_bidsandtenders:f497d5f8-d405-434a-877a-8e839650cd67:2 | City of Hamilton | Category 30A - Structural - Facilities |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f497d5f8-d405-434a-877a-8e839650cd67 |
| ca_bidsandtenders:6526e72a-7763-4579-b0ab-6a291ef743a0:1 | City of Thunder Bay | Engineering Consultant for Pavement Condition Analysis |  |  |  | https://thunderbay.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6526e72a-7763-4579-b0ab-6a291ef743a0 |
| ca_bidsandtenders:b1a31375-60c1-4241-aafa-f5f550c4ddc9:1 | Halifax Regional Municipality | Halifax Urban Greenway Connection to SMU |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/b1a31375-60c1-4241-aafa-f5f550c4ddc9 |
| ca_bidsandtenders:0bb5718b-18b2-4fba-8125-1aa810880e2e:1 | Halifax Regional Municipality | Mumford Terminal Interim Upgrades - Design |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/0bb5718b-18b2-4fba-8125-1aa810880e2e |
| ca_bidsandtenders:88cf669a-c5dc-4435-a8cb-0091416041aa:1 | Halifax Regional Municipality | Materials Testing and Inspection - Standing Offer |  |  |  | https://halifax.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/88cf669a-c5dc-4435-a8cb-0091416041aa |
| ca_bidsandtenders:f7ba34a5-27e3-46c5-b252-a42c4f889b45:4 | Oxford County | Request for Letters of Interest - Building Condition Assessments |  |  |  | https://oxfordcounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f7ba34a5-27e3-46c5-b252-a42c4f889b45 |
| ca_bidsandtenders:56ce7280-5e91-4589-b0a1-e0fdc3602d64:8 | Region of Waterloo | Prequalification of Consultants for Asbestos & Designated Substance Surveys |  |  |  | https://regionofwaterloo.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/56ce7280-5e91-4589-b0a1-e0fdc3602d64 |
| ca_bidsandtenders:5e4c1542-b71b-4eae-a11d-11e7a6fd99ad:1 | City of Guelph | Precondition Survey Services for the Downtown Infrastructure Renewal Program Phase 1 |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5e4c1542-b71b-4eae-a11d-11e7a6fd99ad |
| ca_bidsandtenders:dad81b36-32f4-4156-a570-75b41957914b:1 | City of Moncton / Ville de Moncton | Sewer System Review and Master Plan - Phase 10 |  |  |  | https://moncton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dad81b36-32f4-4156-a570-75b41957914b |
| ca_bidsandtenders:5926f7d7-0fb2-4390-9c8a-b4fbf1948c31:1 | City of Guelph | Consulting Services for Roof Replacement Works | 121036.11 |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5926f7d7-0fb2-4390-9c8a-b4fbf1948c31 |
| ca_bidsandtenders:1a15a430-2546-410c-a527-fe5efbeeb872:1 | Town of Ingersoll | Geotechnical Enviro Services |  |  |  | https://ingersoll.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1a15a430-2546-410c-a527-fe5efbeeb872 |
| ca_bidsandtenders:8789ca59-6d8c-4091-a3bd-67467d7faac0:2 | Town of Newmarket | Geotechnical & Material Testing Services Roster |  |  |  | https://newmarket.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8789ca59-6d8c-4091-a3bd-67467d7faac0 |
| ca_bidsandtenders:dd923dcc-d624-4d73-a800-489597142bba:1 | Municipality of the County of Kings | Environmental Monitoring Program for Meadowview Landfill | 59850.0 |  |  | https://countyofkings.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/dd923dcc-d624-4d73-a800-489597142bba |
| ca_bidsandtenders:7217432f-2ca7-4d18-90e8-2f000c5d0047:1 | City of Guelph | Environmental Services from the Pre-Qualified for Wyndham Street North |  |  |  | https://guelph.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7217432f-2ca7-4d18-90e8-2f000c5d0047 |
| ca_bidsandtenders:65f756ef-d299-41ba-953b-09aa63373a21:3 | City of Mount Pearl | RFQs - Traffic Engineering Services |  |  |  | https://mountpearl.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/65f756ef-d299-41ba-953b-09aa63373a21 |
| ca_bidsandtenders:8138e721-2ec4-4821-b1da-5238f4e34e2f:1 | City of Kitchener | Professional Services – Gas Main Replacement on Duke at Metrolinx Railway Corridor – Geotechnical Investigation |  |  |  | https://kitchener.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8138e721-2ec4-4821-b1da-5238f4e34e2f |
| ca_bidsandtenders:6cea34d1-2a26-4cd3-95e6-8c83ceca38d5:1 | Town of Paradise | Consulting Services: Water and Sewer Installations Drovers Road | 145986.75 |  |  | https://paradise.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/6cea34d1-2a26-4cd3-95e6-8c83ceca38d5 |
| ca_bidsandtenders:fc4b3382-cd8e-4a9b-9163-b0dea521ce28:1 | Township of Leeds and Thousand Islands | Facility Structural Review |  |  |  | https://leeds1000islands.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/fc4b3382-cd8e-4a9b-9163-b0dea521ce28 |
| … 240 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**Buyer's contract policy (the PO rule the row already quotes, in full).** "POLICY ON SUPPLY, SERVICE AND CONSTRUCTION CONTRACTS", adopted May 10, 2013,
revised Oct 18, 2013 and March 25, 2015 (s. 18.1), https://www.cqsb.qc.ca/documents/37503/40386/Policy+on+Supply%2C+Services+and+Construction+Contracts.pdf/4c5e6650-08b8-1bba-301a-4e0e33c2dc9d?t=1623708185550
(linked from https://www.cqsb.qc.ca/en/purchasing-department/policies, the only purchasing policy listed): s. 16.2 commitments "must be confirmed by signing a
contract or by issuing a purchase order."; s. 16.3 "All contracts and purchase orders must be signed by a person authorized by the School Board."; s. 16.4
"Invoices are paid by Financial Services or the schools and Centre."; thresholds: public tender "equal to or more than $100,000" (10.1.1 / 11.1.1 / 12.1.1),
invitation $10,000–$99,999 (goods/services), direct quotes $2,500–$9,999. No payment-terms or invoice-address clause (absent). The Englobe mandate
("Mandat - Laboratoire de contrôle - Surveillance", $73,999.86, SEAO contract 20128057 / tender JSMS10M-Laboratoire) sits in the invitation band → a signed
contract or PO exists; quote the SEAO contract number and the PO; invoices go to Financial Services (the row's confirmed mailbox).
**Purchasing service page** https://www.cqsb.qc.ca/en/service-d-approvisionnement/mandat: mandate "purchase goods and services at the best possible cost";
no PO / invoice / payment text; contact page https://www.cqsb.qc.ca/en/purchasing-department/contact-us (not read). Note: the board has been a Centre de
services scolaire since 2020 for French boards, but English boards kept the "Commission scolaire / School Board" name — bill to "Central Québec School
Board / Commission scolaire Central Québec" (row's registry name), never "à la …".

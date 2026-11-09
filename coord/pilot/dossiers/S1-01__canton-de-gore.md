# S1-01 — Canton de Gore ⇄ Services Ricova Inc.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08) — 9, chemin Cambria, Gore, QC, J0V1K0, CA — buyer tax no. 130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: facturation@cantondegore.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://seao.gouv.qc.ca/contrats-par-organisation — SEAO
REFERENCE: contract 20029145 (ocds_contract_ids); tender ARG-2024-GMR (numero) | PO rule: not published
FROM / REMIT TO: Ricova Services Inc. — 3400 rue de l’Éclipse,suite 540, Brossard, QC, J4Z0P3 | GST/HST 825350028RT0001 (account derived from the BN9) | NEQ 1165661415
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD | TERMS: payment, payable within 31 days (as printed on https://www.cantondegore.qc.ca/en/municipal-services/
DESCRIPTION: COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POU | AMOUNT: 183,055.68 CAD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 96
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Canton de Gore (municipality / local government, QC) — public contract / purchase award with a published end date (dated record): Services Ricova Inc. | subject: COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POUR DEUX (2) PÉRIODES SUBSÉQUENTES D’UNE ANNÉE | instrument: contract | contract number: 20029145 (ocds_contract_ids); ARG-2024-GMR (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it | solicitation: ARG-2024-GMR (numero) | all identifiers: {"numeroseao": "20030622", "numero": "ARG-2024-GMR", "ocid": "ocds-ec9k95-20030622", "ocds_contract_ids": ["20029145"], "ocds_award_ids": ["20029145"], "seao_item_id": "0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9"} | value: 183055.68 CAD | awarded 2024-10-07, start 2024-10-07, end 2029-10-07 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9 | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 46 records with Canada-located vendors (39 distinct vendors; 6 in the last 12 months; latest 2026-0
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:61573b39d41eb0a4
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Canton de Gore
- **buyer_website**: https://www.cantondegore.qc.ca
- **buyer_address**: 9, chemin Cambria, Gore, QC, J0V1K0, CA
- **buyer_phone**: 4505622025 (provincial municipal directory: https://donneesouvertes.affmunqc.net/repertoire/MUN.csv, 2026-11-08)
- **buyer_contact_evidence_url**: https://cantondegore.qc.ca/fr/contact
- **buyer_legal_name_as_published**: CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08)
- **buyer_bn_as_published**: 130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 130588890RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://cantondegore.qc.ca/themes/cdg/assets/images/icones/logo.svg
- **buyer_website_status**: site answers
- **buyer_registry_id**: NEQ 8813435334 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_municipal_tier**: local municipality of MRC MRC Argenteuil (760) (MAMH répertoire) (provincial municipal directory: https://donneesouvertes.affmunqc.net/repertoire/MUN.csv, 2026-11-08)
- **buyer_population**: 2765 (provincial municipal directory: https://donneesouvertes.affmunqc.net/repertoire/MUN.csv, 2026-11-08)
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://cantondegore.qc.ca/fr/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: facturation@cantondegore.qc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.cantondegore.qc.ca/fr/contact
- **email_evidence_quote**: Mélissa Ouellette Coordonnatrice à la comptabilité 450 562-2025 poste 3524 facturation@cantondegore.qc.ca
- **email_evidence_context**: 3525 schannell@cantondegore.qc.ca Diane Chales Dir. Adjointe aux finances/Ass. greffière-trésorière/Adj. Service Incendies 450 562-2025 poste 3523 dchales@cantondegore.qc.ca Mélissa Ouellette Coordonnatrice à la comptabilité 450 562-2025 poste 3524 facturation@cantondegore.qc.ca Alain Giroux Maire maire@cantondegore.qc.ca Cristian Frincu Directeur des finances 4505622025 poste 3527 cfrincu@cantondegore.qc.ca Service municipaux Tammy Hall Coordonnatrice du service d'inspection 450-562-2025 poste 3542 thall@cantondegore.qc.ca (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: facturation@cantondegore.qc.ca (invoicing/AP) | mailbox from the dataset build, re-submitted so the referee re-fetched the page on 2026-11-04 | page: https://www.cantondegore.qc.ca/fr/contact | quote: "Mélissa Ouellette Coordonnatrice à la comptabilité 450 562-2025 poste 3524 facturation@cantondegore.qc.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_dsenrich01.csv task CL-DS-00025
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:dmarc@cantondegore.qc.ca; ruf=mailto:dmarc@cantondegore.qc.ca;
- **dmarc_record_domain**: cantondegore.qc.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:170.39.23.101 +include:servers.mcsv.net +include:spf.protection.outlook.com +include:spfsmtp2go.idside.com  ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Diane Chales Dir (Adjointe aux finances) (as printed by the organisation on its own accounts-payable page (as printed on https://www.cantondegore.qc.ca/fr/contact, re-read 2026-11-08))
- **ap_phone**: 450 562-2025 poste 3523 (as printed on https://www.cantondegore.qc.ca/fr/contact, re-read 2026-11-08)
- **payment_terms_as_published**: payment, payable within 31 days (as printed on https://www.cantondegore.qc.ca/en/municipal-services/municipal-taxes, re-read 2026-11-08)
- **invoice_portal_url**: https://seao.gouv.qc.ca/contrats-par-organisation — SEAO
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SEAO (as printed on https://www.cantondegore.qc.ca/en/publications/contract-management, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment, payable within 31 days (as printed on https://www.cantondegore.qc.ca/en/municipal-services/municipal-taxes, re-read 2026-11-08)", "portal_url": "https://seao.gouv.qc.ca/contrats-par-organisation — SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "450 562-2025 poste 3523 (as printed on https://www.cantondegore.qc.ca/fr/contact, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08) — 9, chemin Cambria, Gore, QC, J0V1K0, CA — buyer tax no. 130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: facturation@cantondegore.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://seao.gouv.qc.ca/contrats-par-organisation — SEAO ⏎ REFERENCE: contract 20029145 (ocds_contract_ids); tender ARG-2024-GMR (numero) | PO rule: not published ⏎ FROM / REMIT TO: Ricova Services Inc. — 3400 rue de l’Éclipse,suite 540, Brossard, QC, J4Z0P3 | GST/HST 825350028RT0001 (account derived from the BN9) | NEQ 1165661415 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD | TERMS: payment, payable within 31 days (as printed on https://www.cantondegore.qc.ca/en/municipal-services/ ⏎ DESCRIPTION: COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POU | AMOUNT: 183
- **invoice_card_json**: {"bill_to": {"legal_name": "CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08)", "legal_name_is_published": true, "address": "9, chemin Cambria, Gore, QC, J0V1K0, CA", "address_is_the_invoice_address": false, "tax_number": "130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "facturation@cantondegore.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://seao.gouv.qc.ca/contrats-par-organisation — SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.cantondegore.qc.ca/en/publications/contract-management, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20029145 (ocds_contract_ids); ARG-2024-GMR (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contr
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: PO rule
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20029145 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: Services Ricova Inc.
- **vendor_legal_name**: Ricova Services Inc.
- **vendor_trading_name**: Services Ricova Inc.
- **vendor_registry_id**: Corporations Canada (corporation number): 7103867; NEQ 1165661415 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=7103867
- **vendor_registered_address**: 3400 RUE DE L'ÉCLIPSE, SUITE 540, BROSSARD, QC, J4Z 0P3, CA
- **vendor_neq**: 1165661415 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Domaine du recyclage | secondary: collecte et enlèvement de matières résiduelles
- **vendor_employees_quebec**: De 26 à 49
- **vendor_establishments_quebec**: Services Ricova Inc.: 12000 BOUL. Henri-Bourassa Est, Montréal (Québec), H1C1S9
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2026; Corporations Canada anniversary 2009-01-07
- **vendor_address**: 3400 rue de l’Éclipse,suite 540, Brossard, QC, J4Z0P3
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_bn9**: 825350028
- **vendor_gst_hst_derived**: 825350028RT0001
- **vendor_website**: https://ricova.com/
- **vendor_emails**: info@ricova.com
- **vendor_phone**: 450-466-6688
- **vendor_contact_evidence_url**: https://ricova.com/contact/
- **vendor_logo_url**: https://ricova.com/wp-content/uploads/2024/11/logo.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/ricova-services-inc/
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://ricova.com/en/contact/; https://ricova.com/en/contact/
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Corporations Canada (corporation number): 7103867; NEQ 1165661415 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (2009-02-02) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 7103867 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2009-01-07; phone / role e-mails / logo: the vendor's own site, https://ricova.com/contact/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://ricova.com/en/contact/; https://ricova.com/en/contact/; website: https://ricova.com/ (site answers); NEQ: 1165661415 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Calclo Inc.: 6% of 46 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (2009-02-02)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2009-01-07
- **vendor_years_in_business**: 17.8 (since 2009-01-07, registry date)
- **vendor_bn_source**: corporations_canada 7103867 (exact match)

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20030622", "numero": "ARG-2024-GMR", "ocid": "ocds-ec9k95-20030622", "ocds_contract_ids": ["20029145"], "ocds_award_ids": ["20029145"], "seao_item_id": "0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9"}
- **contract_title**: COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POUR DEUX (2) PÉRIODES SUBSÉQUENTES D’UNE ANNÉE
- **commodity**: 76121501 Collecte, traitement ou élimination des ordures ménagères
- **contract_description**: services; Services de nature technique
- **contract_or_agreement_number**: 20029145 (ocds_contract_ids); ARG-2024-GMR (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: ARG-2024-GMR (numero)
- **award_or_notice_id**: 20030622 (numeroseao); 20029145 (ocds_award_ids); ocds-ec9k95-20030622 (ocid); 0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9 (seao_item_id)
- **commodity_codes**: UNSPSC 76121501 (Collecte, traitement ou élimination des ordures ménagères)
- **contract_value**: 183055.68
- **currency**: CAD
- **award_date**: 2024-10-07
- **start_date**: 2024-10-07
- **end_date**: 2029-10-07
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 46
- **records_last_12_months**: 6
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (46)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 46 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Génie des barrages (2); Pare-poussière (1); Services de déneigement (1)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 130588890RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 825350028RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08) — 9, chemin Cambria, Gore, QC, J0V1K0, CA — buyer tax no. 130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: facturation@cantondegore.qc.ca (invoicing/AP mailbox, confirmed by the referee) | tender portal (not an invoice channel): https://seao.gouv.qc.ca/contrats-par-organisation — SEAO ⏎ REFERENCE: contract 20029145 (ocds_contract_ids); tender ARG-2024-GMR (numero) | PO rule: not published ⏎ FROM / REMIT TO: Ricova Services Inc. — 3400 rue de l’Éclipse,suite 540, Brossard, QC, J4Z0P3 | GST/HST 825350028RT0001 (account derived from the BN9) | NEQ 1165661415 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: CAD | TERMS: payment, payable within 31 days (as printed on https://www.cantondegore.qc.ca/en/municipal-services/ ⏎ DESCRIPTION: COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POU | AMOUNT: 183
- **invoice_card_json**: {"bill_to": {"legal_name": "CANTON DE GORE (as registered: Registraire des entreprises du Québec (open data), NEQ 8813435334, 2026-11-08)", "legal_name_is_published": true, "address": "9, chemin Cambria, Gore, QC, J0V1K0, CA", "address_is_the_invoice_address": false, "tax_number": "130588890RP0003 (recipient_business_number in the federal grants & contributions disclosure, 1 agreement(s), last 2019-05-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "facturation@cantondegore.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://seao.gouv.qc.ca/contrats-par-organisation — SEAO", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SEAO (as printed on https://www.cantondegore.qc.ca/en/publications/contract-management, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": "tender portal (not an invoice channel)"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20029145 (ocds_contract_ids); ARG-2024-GMR (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contr
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: PO rule
- **ap_grade**: B
- **ap_score**: 79
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["facturation@cantondegore.qc.ca (invoicing/AP)", "mailbox from the dataset build, re-submitted so the referee re-fetched the page on 2026-11-04", "page: https://www.cantondegore.qc.ca/fr/contact", "quote: \"Mélissa Ouellette Coordonnatrice à la comptabilité 450 562-2025 poste 3524 facturation@cantondegore.qc.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_dsenrich01.csv task CL-DS-00025"], "buyer_facts": ["address and phone: the buyer's own site, https://cantondegore.qc.ca/fr/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP cont

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.cantondegore.qc.ca/fr/contact | 2026-11-08 | ok |  |  |  | 450 562-2025 poste 3523 |  |  |  |  |  |

## Buyer site facts (org_extras, cantondegore.qc.ca)
- **status**: ok
- **pages**: 4
- **language**: fr
- **logo_url**: https://cantondegore.qc.ca/themes/cdg/assets/images/icones/logo.svg
- **logo_basis**: logo image on the site
- **domain**: cantondegore.qc.ca
- **key**: b:61573b39d41eb0a4
- **name**: Canton de Gore
- **website**: https://cantondegore.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Canton de Gore
- **legal_name_stated_url**: https://cantondegore.qc.ca/fr/publications/avis-et-communiques
- **legal_name_stated_quote**: min Cambria Gore (Québec) J0V 1K0 Nous joindre 450 562-2025 9, chemin Cambria Gore (Québec) J0V 1K0 Canton de Gore © 2019 Tous droits réservés #Blankonumerique

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "9, chemin Cambria , Gore (Québec) J0V 1K0", "address_country": "CA", "address_url": "https://cantondegore.qc.ca/fr/contact", "address_method": "pattern", "address_quote": "nel EN Nous joindre Nous joindre Hôtel de ville 9, chemin Cambria Gore (Québec) J0V 1K0 450 562-2025 info@cantondegore.qc.ca Heures de bureau: Lundi au jeudi de 9 h à", "emails": "facturation@cantondegore.qc.ca; info@cantondegore.qc.ca", "emails_url": "https://cantondegore.qc.ca/fr/contact", "domain": "cantondegore.qc.ca", "key": "b:61573b39d41eb0a4", "name": "Canton de Gore", "website": "https://cantondegore.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, ricova.com)
- **status**: ok
- **pages**: 4
- **language**: fr
- **logo_url**: https://ricova.com/wp-content/uploads/2024/11/logo.png
- **logo_basis**: logo image on the site
- **domain**: ricova.com
- **key**: vendor:Services Ricova Inc.
- **name**: Services Ricova Inc.
- **website**: https://ricova.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'interactions avec vous et vous fournir les services et les informations que vous demand', 'url': 'https://ricova.com/politique-de-confidentialite/', 'quote': 'et fournisseurs de services, en tenant compte des intérêts légitimes de Ricova, comme améliorer les interactions avec vous et vous fournir les services et les informations que vous demandez, conformément à ce qui est permis par la loi applicable. Sauf si inter'}}
- **linkedin_url**: https://www.linkedin.com/company/ricova-services-inc/
- **tel_links**: +14504666688

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "3400, rue de l’Éclipse, bureau 540 Brossard, QC J4Z 0P3", "address_country": "CA", "address_url": "https://ricova.com/contact/", "address_method": "pattern", "address_quote": "otre bureau principal Adresse : 3400, rue de l’Éclipse, bureau 540 Brossard, QC J4Z 0P3 Courriel : info@ricova.com Téléphone : 450-466-6688 Adresse : 3400, rue de l’Éc", "phone": "450-466-6688", "phone_url": "https://ricova.com/contact/", "emails": "info@ricova.com", "emails_url": "https://ricova.com/contact/", "domain": "ricova.com", "key": "vd:ricova.com", "name": "Services Ricova Inc.", "website": "https://ricova.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Services Ricova Inc. | found | Services Ricova Inc. |  | 1165661415 | QC | Société par actions ou compagnie | Active | 2009-01-07 | Brossard | Québec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Services%20Ricova%20Inc. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Canton de Gore | found | CANTON DE GORE |  | NEQ 8813435334 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 1855-07-01 | Gore | QC | 9 ch. Cambria, Gore (Québec), J0V1K0 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |
| buyer | Services Ricova Inc. | found | Services Ricova Inc. |  | NEQ 1165661415 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 2009-02-02 | Brossard | QC | 540-3400 RUE de l'Éclipse, Brossard (Québec), J4Z0P3 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canton de Gore |  |  |  |  |  |  |  |  |  |  |
| b | Services Ricova Inc. |  |  |  |  |  |  |  |  |  |  |
| v | Ricova Services Inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:61573b39d41eb0a4",
 "ap_contact_team": {
  "emails": [
   "info@cantondegore.qc.ca",
   "facturation@cantondegore.qc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@cantondegore.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cantondegore.qc.ca/fr/services-municipaux/taxes-municipales",
    "quote": "d'adresse doivent être envoyés par la poste au 9, chemin Cambria, Gore (Québec) J0V 1K0, par télécopieur au 450 562-5424 ou par courriel à info@cantondegore.qc.ca . Veuillez nous aviser si le changement d'adresse s'applique à plus d'un dossier. Liens rapides Avis et communiqués Permis et",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Canton de Gore",
    "task_id": "CL-WS-00092"
   },
   {
    "email": "facturation@cantondegore.qc.ca",
    "type": "invoicing",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.cantondegore.qc.ca/fr/contact",
    "quote": "Mélissa Ouellette Coordonnatrice à la comptabilité 450 562-2025 poste 3524 facturation@cantondegore.qc.ca",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_dsenrich01.csv",
    "org": "Canton de Gore",
    "task_id": "CL-DS-00025"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "dataset enrichment (ap_crawler / targeted search) re-submitted for referee verification",
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
| seao_quebec:20030622:services-ricova-inc | seao_quebec | ongoing | COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POUR DEUX (2) PÉRIODES  | 183055.68 | CAD |  |  | {"numeroseao": "20030622", "numero": "ARG-2024-GMR", "ocid": "ocds-ec9k95-20030622", "ocds_contract_ids": ["20029145"], "ocds_award_ids": ["20029145"], "seao_item_id": "0ff0f1fb-fa52-48ce-a1c6-ea10d06 | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0ff0f1fb-fa52-48ce-a1c6-ea10d06ee3b9 |

## The buyer's other Canadian-vendor records (first 60 of 45)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1239769:entreprises-claude-rodrigue-inc | ENTREPRISES CLAUDE RODRIGUE INC. | Travaux de réfection de la rue Williams | 849080.03 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cd8bf177-6965-4f1e-906a-f6b008355274 |
| seao_quebec:1324277:centre-de-tri-d-argenteuil-inc | Centre de tri d'Argenteuil inc. | Collecte et gestion des résidus de construction, de rénovation et de démolition récupérés à l’écocentre municipal | 457426.74 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2b234fc4-d1bc-4869-96fd-5f3d64f23b4e |
| seao_quebec:1473504:innovative-surface-solutions-canada | Innovative Surface Solutions Canada | Fourniture, livraison, épandage de divers produits utilisés comme abat-poussière pour l'année 2021 | 53553.38 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7b111ed4-5f88-4579-aa78-8c442b8f5e16 |
| seao_quebec:1478489:9129-6558-quebec-inc | 9129-6558 QUÉBEC INC. | APPEL D'OFFRES POUR L’ENLÈVEMENT DE LA NEIGE,  LA FOURNITURE ET L’ÉPANDAGE D’UN MÉLANGE DE SEL ET DE SABLE CONTRAT DE 3 SAISONS AVEC OPTION DE RENOUVELLEMENT AN | 3764338.98 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9d71b19b-923f-453d-ba3c-430b0ebd484b |
| seao_quebec:1581253:mazout-g-belanger-inc | MAZOUT G. BELANGER INC. | Fourniture et livraison de carburants en vrac dans diverses municipalités | 58399.94 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fa218bfd-c123-44e9-b0bf-1ebf39c3f730 |
| seao_quebec:1586854:multi-routes-inc | MULTI ROUTES INC. | Fourniture, livraison, épandage de divers produits utilisés comme abat-poussière pour l'année 2022 | 64031.22 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=38950182-7150-44d0-a57f-a39980851e7b |
| seao_quebec:1716903:9129-6558-quebec-inc | 9129-6558 QUÉBEC INC. | Nivelage des chemins municipaux pour l'année 2023 avec option de renouvellement pour 2024 et 2025 | 95572.96 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b20ea51d-28ef-4141-a0af-8b13f11ff388 |
| seao_quebec:1716936:equipe-laurence-inc | ÉQUIPE LAURENCE INC. | CONCEPTION DES PLANS ET DEVIS RELATIVEMENT AUX TRAVAUX DE RÉFECTION PRÉVUS EN 2024 SUR LE CHEMIN CAMBRIA | 83701.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f91fc888-2ba3-42d7-bcd7-4ef5b8110ed7 |
| seao_quebec:1796429:4520556-canada-inc | 4520556 CANADA INC. | 2023-11-357 Contrat de trois (3) ans pour l'entretien menagère des bâtiments municipaux (2024, 2025 et 2026) | 108376.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b353c732-ea72-47b6-b2ea-6b582d7ddab6 |
| seao_quebec:1809317:9254-8783-quebec-inc | 9254-8783 QUÉBEC INC. | TRAVAUX DE MARQUAGE DE LA CHAUSSÉE DES CHEMINS MUNICIPAUX POUR LES ANNÉES 2024 ET 2025 AVEC OPTION DE RENOUVELLEMENT POUR 2026 ET 2027 | 42995.19 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2d1cbb18-4370-47d2-86b1-d8e0e11ca681 |
| seao_quebec:1809429:equipe-laurence-inc | ÉQUIPE LAURENCE INC. | MANDAT POUR LA SURVEILLANCE DES TRAVAUX DE RÉFECTION DU CHEMIN CAMBRIA | 123023.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3739d1ea-09fe-43fb-b6c9-2d6a5bde8169 |
| seao_quebec:1827153:multi-routes-inc | MULTI ROUTES INC. | Fourniture, livraison, épandage de divers produits utilisés comme abat-poussière pour l'année 2024 avec options de reconduction pour 2025 et 2026 | 215930.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=502b0f78-2c9c-4185-bc4f-c82afef67866 |
| seao_quebec:20030685:puits-christian-monette-inc | PUITS CHRISTIAN MONETTE INC. | CONTRAT POUR LE CREUSAGE DE PUITS AU PARC DU LAC BEATTIE | 26656.95 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b517d999-8048-429c-b6be-60b7c938c810 |
| seao_quebec:20042097:services-conseils-aqua-ingenium-s-e-n-c | Services-conseils Aqua Ingenium S.E.N.C. | ÉVALUATION DE  L’APPAREIL D’ÉVACUATION ET LA CONCEPTION DES PLANS ET DEVIS POUR LA RÉPARATION DU BARRAGE DU LAC DAWSON (X0004841) | 34929.41 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=44c4bef2-3bf6-4afd-a66d-2a2a40b65bbc |
| seao_quebec:20042104:david-riddell-excavation-transport | DAVID RIDDELL EXCAVATION/TRANSPORT | ACHAT TRACTEUR NEW HOLLAND | 51738.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=74efb4b9-1ef2-4d64-bdee-413b81dc65f7 |
| seao_quebec:20056323:l-atelier-urbain-inc | L'ATELIER URBAIN INC. | LA REFONTE DES RÈGLEMENTS D’URBANISME | 117634.26 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0e270171-5be4-4bc3-bd7b-d09da95e0835 |
| seao_quebec:20069897:services-conseils-aqua-ingenium-inc | SERVICES-CONSEILS AQUA INGENIUM INC. | PLANS ET DEVIS CONCERNANT LE RENFORCEMENT DU BARRAGE SOLAR | 95480.99 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b7a8767f-c25e-4974-9889-f5aed686c0cc |
| seao_quebec:20106106:6005438-canada-inc | 6005438 CANADA INC. | PRÉPARATION DES PLANS ET DEVIS DU PROJET DE CONSTRUCTION D’UNE PASSERELLE ET D’UN BELVÉDÈRE D’OBSERVATION AU PARC DU LAC BEATTIE | 66823.47 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=44c7704d-a366-439f-a98e-eb6491617aba |
| seao_quebec:20117370:13553752-canada-inc | 13553752 Canada Inc. | CHALET 20’X16’ – MODÈLE MOUNTAIN DE RUSTICATE | 83494.85 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d103ba1b-56e5-4ca9-a28e-1f3ea1bd6879 |
| seao_quebec:20117408:david-riddell-excavation-transport | DAVID RIDDELL EXCAVATION/TRANSPORT | NIVELAGE DES CHEMINS MUNICIPAUX POUR L’ANNÉE 2026 AVEC OPTION DE RENOUVELLEMENT POUR 2027 ET 2028 | 101683.89 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8742a96b-cc07-4df2-af7f-9b9ec755faf5 |
| seao_quebec:20121242:9161-4396-quebec-inc | 9161-4396 Quebec Inc | DÉNEIGEMENT DES CHEMINS MUNICIPAUX INCLUANT LA FOURNITURE ET L’ÉPANDAGE D’UN MÉLANGE DE SEL ET DE SABLE ABRASIF- CONTRAT DE 3 SAISONS AVEC OPTION DE RENOUVELLEM | 3090528.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f3e8a6e0-acc2-4bd6-8293-9b5fb433370c |
| seao_quebec:20142427:pg-solutions-inc | PG SOLUTIONS INC. | Service PG 2026 | 91538.6 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3a6bfb21-71ee-481a-9cb3-9cb51ef1e954 |
| seao_quebec:20158695:hb-construction | HB Construction | TRAVAUX DE RÉNOVATION DE LA CUISINE ET L’AMÉNAGEMENT D’UNE SALLE DE LAVAGE AU CENTRE COMMUNAUTAIRE | 65575.99 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8385145d-321d-4c09-9ba5-2c43b37ea4a4 |
| seao_quebec:20158717:cummins-canada-ulc | Cummins Canada ULC | RÉPARATION — CAMION 344 DU SERVICE DE SÉCURITÉ INCENDIE | 57413.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bc05f6cc-23d2-4d24-b48e-0c70027ba5b3 |
| seao_quebec:516318:les-entreprises-forestieres-t-w-seale-inc | Les Entreprises Forestieres T & W Seale inc | Enlèvement de la neige ainsi que la fourniture et l'épandage d'un mélange de sel et de sable- contrat de 3 ans ou 5 ans | 1772683.53 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e6c4b05e-09a5-468d-a6ef-3afe91cb4d67 |
| seao_quebec:520429:r-c-i-environnement-une-division-de-wm-quebec | R.C.I. Environnement une division de WM Québec | Pour l'enlèvement des ordures, des objets lourds, des matériaux de construction et des matières recyclables | 876994.65 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8673a296-430a-457a-a94a-6ecfa09498d2 |
| seao_quebec:536436:auto-desrosiers-ford-inc | Auto Desrosiers Ford Inc | Achat d'un camion de type (chassis-cabine) | 44368.09 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=40d83e03-566a-4522-b553-83cbcc042306 |
| seao_quebec:536472:les-machineries-saint-jovite-inc | Les Machineries Saint-Jovite Inc. | Achat d'une benne basculante pour camion de 1.5 tonne avec côtés ouvrants | 14283.71 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9661f08a-81cb-4e8a-b7a3-027380844024 |
| seao_quebec:536929:calclo-inc | Calclo Inc. | Fourniture et épandage d'abat-poussières liquide pour 2011 | 37404.19 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=037a1097-b20f-42a1-9cf9-869f7ae7466f |
| seao_quebec:551210:camions-helie-2003-inc | Camions Hélie (2003) Inc. | ACHAT D'UN (1) CAMION UNITÉ D'URGENCE DE L'ANNÉE 2012 | 136624.79 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3968080c-9b61-49a7-aeef-ad96464c70c6 |
| seao_quebec:555400:bock-inc | Bock inc. | ACHAT D'UNE (1) CHARGEUSE/RÉTROCAVEUSE NEUVE 2012 | 96004.13 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=aa63c021-a96f-4c03-b19e-25ec2ffb7bdf |
| seao_quebec:567895:asphalte-beton-carrieres-rive-nord-inc | Asphalte, Béton, Carrières Rive-Nord inc. | Rechargement granulaire et recouvrement en enrobé bitumineux sur le chemin Cambria | 514063.34 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=51601ac6-8a7a-437c-b2e8-52954fab6b4a |
| seao_quebec:568865:les-entreprises-forestieres-t-w-seale | Les Entreprises Forestières T. & W. Seale | Aménagement du terrain de l'écocentre du Canton de Gore | 63523.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6dbd81f7-bedd-43e4-ac5d-4c22650b5dac |
| seao_quebec:652824:uniroc-construction-inc | Uniroc Construction inc | Réfection de chaussée et pose d'enrobé bitumineux pour les chemins Cascade et Tamarac | 455500.01 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6bd54f1d-b1c8-4735-858c-a1318e91ad6a |
| seao_quebec:744417:les-entreprises-forestieres-t-w-seale-inc | Les Entreprises Forestieres T & W Seale inc | Aménagement du terrain de l'écocentre | 63523.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bf1c7748-192a-4b6d-88a9-add27d4712bd |
| seao_quebec:744451:laurentides-experts-conseils | Laurentides Experts Conseils | Réalisation d'une étude de faisablilité d'un programme ÉcoPrêt pour le remplacement des systèmes de traitement des eaux usées des résidences isolées | 44840.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4a22fb19-4549-418f-8de2-acdb54cb8487 |
| seao_quebec:744850:cbf-telecom-ltee | CBF Telecom Ltee | Construction d'un réseau de fibre optique | 34144.42 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d5ac4df2-f46d-4909-afb8-592b13e38da7 |
| seao_quebec:744859:arbrexpert-enr | Arbrexpert Enr | Service d'élagage | 47691.63 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=942e1c7f-ad9a-4672-bd24-93eb0031bb5d |
| seao_quebec:744867:les-industries-permo | Les industries Permo | Achat d'un (1) bâtiment d'entreposage de type dôme | 51623.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=495f97ab-fa9a-473e-b622-20acac10e2e6 |
| seao_quebec:744881:calclo-inc | Calclo Inc. | Fourniture et épandage d'abat poussière liquide pour 2013 | 26516.84 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=59bcfaeb-58f6-4a75-8e45-fd0e2df41136 |
| seao_quebec:744893:service-de-recyclage-sterling | Service de recyclage Sterling | Gestion des résidus de construction, de rénovation et de démolition récupérés à l'écocentre municipal | 24186.14 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0693ee58-4db0-429e-a445-5719872d7d29 |
| seao_quebec:753655:j-rene-lafond-inc | J.-René Lafond inc. | Achat d'une débroussailleuse de marque ORSI avec outils interchangeables pour installations sur un tracteur Case 80 MXC | 43460.55 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b382cd07-6d2d-4311-84eb-9a3f4a389d27 |
| seao_quebec:753676:cmp-mayer | CMP Mayer | Achat d'habit de combat pour pompier | 19266.36 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0e04d708-5f80-4a47-a93c-d023518794ba |
| seao_quebec:785048:calclo-inc | Calclo Inc. | Fourniture et épandage d'abat-poussière liquide pour 2014 | 36591.07 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d95100a7-a662-4399-8ae3-680263a94fed |
| seao_quebec:808670:transport-rls | Transport RLS | Collecte et transport des matières résiduelles et des résidus encombrants | 639960.05 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2bd0a3cd-55e6-42a2-8464-73f0e2da1728 |

## The vendor's other buyers in the dataset (first 60 of 141)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1086999:services-ricova-inc | Municipalité de la Paroisse Très-Saint-Sacrement | collecte et transport des matières résiduelles domestiques | 54739.59 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d19098e9-849c-4e8f-bec3-3566974cd10c |
| seao_quebec:1088352:services-ricova-inc | Ville de Chambly. | Collecte et transport des matières organiques | 297858.72 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2636b0de-0bb4-4a36-8989-b1d98b53a8d1 |
| seao_quebec:1160824:services-ricova-inc | Commission scolaire des Grandes Seigneuries | Services de collecte et de disposition des matières résiduelles et location de compacteurs/conteneurs | 87561.49 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=18ed877e-a464-4565-9165-842f9b3bab28 |
| seao_quebec:1190024:services-ricova-inc | Ville de Chambly. | Collecte, transport et traitement des matières recyclables | 607416.37 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8d59f09b-294e-49b9-b834-5e39148f8643 |
| seao_quebec:1202404:services-ricova-inc | MRC des Jardins-de-Napierville . | Enlèvement, transport et traitement des matières recyclables - 2e appel d'offres | 488527.28 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0ef38b83-0855-40ae-aa13-12bbfcc991c3 |
| seao_quebec:1205816:services-ricova-inc | Municipalité Saint-Ignace-de-Stanbridge | Collectes des matières destinées à l'enfouissement , au recyclage et au compostage | 69835.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=27e4da0e-04f0-462e-94fe-1a2985c7d0a7 |
| seao_quebec:1206753:services-ricova-inc | Municipalité de Saint-André-d'Argenteuil | Fournitures de services concernant la collecte et le transport matières résiduelles, recyclables et compostables | 117018.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cba26e45-7e3b-47bc-87bd-b173cd74a00a |
| seao_quebec:1211162:services-ricova-inc | Municipalité  Sainte-Sabine. | Collecte et transport des matières résiduelles destinées à l'enfouissement, au recyclage et au compostage | 384583.43 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=96e828cb-e488-416b-9d2e-b453ac048d35 |
| seao_quebec:1214385:services-ricova-inc | Ville de Westmount | La collecte et le transport des matières recyclables du 1er avril 2019 au 31 mars 2022 avec (2) options de renouvellement pour la ville de Westmount | 335224.51 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=309b66c3-0ad2-4534-961f-1f2e11f09fd7 |
| seao_quebec:1389231:services-ricova-inc | Ville de Brossard | Service de collecte de résidus alimentaires | 6373853.21 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=08e515fc-7131-470d-99ee-7f0726026033 |
| seao_quebec:1395245:services-ricova-inc | Ville de Beaconsfield | Collecte et transport des déchets, matières organiques, et déchets volumineux pour les années 2021, 2022 et 2023 avec deux (2) options de renouvellement | 3204821.31 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c7b2e2e4-b88a-4c98-ae5e-d274b940c20f |
| seao_quebec:1409688:services-ricova-inc | Municipalité de la Paroisse Très-Saint-Sacrement | collecte, transport, traitement et mise en marché des matières recyclables | 99.82 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=465580e0-3842-4d7e-85fe-e8abc0ce7f3e |
| seao_quebec:1411115:services-ricova-inc | Ville de Baie D'Urfé | Collecte et transport des matières recyclables 2021-2022, avec une année d'option supplémentaire | 177911.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=be9313a9-daf6-4de9-b448-b39ad721bf24 |
| seao_quebec:1411173:services-ricova-inc | Ville de Baie D'Urfé | Collecte et transport des ordures ménagères 2021-2022, avec une (1) année d’option supplémentaire pour la Ville de Baie-D’Urfé | 249900.69 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9b5a865b-3bab-48f2-ad2e-81ccdb1a7251 |
| seao_quebec:1413762:services-ricova-inc | Ville de Boucherville | COLLECTE ET TRANSPORT DES MATIÈRES ORGANIQUES | 1006514.15 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1a349b10-ed6d-473e-837c-1f992d3eb55a |
| seao_quebec:1417121:services-ricova-inc | Ville de Saint-Constant. | Services de location de conteneurs pour la disposition de diverses matières pour les édifices municipaux | 256686.29 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=40e22683-e7ad-4f0e-8bae-b0d913443166 |
| seao_quebec:1495204:services-ricova-inc | Ville de Chambly. | Collecte transport et traitement des matières recyclables | 1675006.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cbf521c6-12df-430b-88d6-f0969e10bda8 |
| seao_quebec:1503824:services-ricova-inc | Ville de Sainte-Anne-de-Bellevue | Fourniture de services pour la collecte et le transport des matières résiduelles (du 1er février 2022 au 31 janvier 2025 inclusivement avec deux années suppléme | 35872.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=26bbb454-7619-41ca-956c-1ad912d79215 |
| seao_quebec:1532990:services-ricova-inc | Municipalité régionale de comté de Marguerite-D'Youville | Gestion des matières recyclables | 5193394.48 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cf0fc6dd-69c3-4099-bc32-12ca8885db6b |
| seao_quebec:1537177:services-ricova-inc | Ville de Saint-Jean-sur-Richelieu. | Transport et valorisation des biosolides incluant la disposition des déchets de la station d’épuration (2022-2027) | 4246587.31 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c017cc7f-8142-4625-8f20-8dce05510675 |
| seao_quebec:1541683:services-ricova-inc | Municipalité des Cèdres | COLLECTE, TRANSPORT ET DISPOSITION DES MATIÈRES ORGANIQUES - ANNÉE 2022 AVEC 3 ANNÉES OPTIONNELLES (2023, 2024 ET 2025) | 595887.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ba5d940f-92a1-487a-85c5-a57063b6abd8 |
| seao_quebec:1562376:services-ricova-inc | Ville de Longueuil . | COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES DES CONTENEURS SEMI-ENFOUIS À CHARGEMENT PAR GRUE DE LONGUEUIL | 361741.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=92b56fb5-ccec-4d48-8d9c-c93e1b051633 |
| seao_quebec:1563705:services-ricova-inc | Ville de Hampstead | Contrats pour la collecte et le transport des matières récupérables | 504124.44 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=42a6dc30-3370-405e-aa86-04ae07b39f00 |
| seao_quebec:1590160:services-ricova-inc | Ministère des Transports (Direction de l'administration des appels d'offres publics) | 2904-21-SC01 - Contrat à exécution sur demande pour fourniture des contenants, transport et disposition des déchets provenant des autoroutes situées sur le terr | 20125.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4bd7b303-02b3-42e0-84cd-3a53b10e3559 |
| seao_quebec:1620577:services-ricova-inc | Commission scolaire New Frontiers. | Services de recyclage | 27000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6fe5b9c8-1af1-4d3d-8499-104369857e73 |
| seao_quebec:1632042:services-ricova-inc | Ville de Notre-Dame-de-l'Île-Perrot | GT2022-21 – Services de collecte et transport des résidus organiques et services complémentaires pour les municipalités de l'île Perrot | 1163011.36 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dd3af42f-b0c6-4113-a176-d6b4bc61f6d2 |
| seao_quebec:1641472:services-ricova-inc | Municipalité de Mille-Isles | COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS 2023-2024 | 339972.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6998a53d-648f-40a3-a2d8-75270e3396f5 |
| seao_quebec:1642904:services-ricova-inc | Ville de Kirkland. | COLLECTE ET TRANSPORT DES RÉSIDUS ENCOMBRANTS À VOLET RECYCLABLE AVEC QUATRE (4) OPTIONS DE RENOUVELLEMENT | 51071.9 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6fbaa95f-4b5a-4ad9-aa51-2833761cde15 |
| seao_quebec:1643468:services-ricova-inc | MRC de Beauharnois-Salaberry | Collecte et transport des déchets domestiques | 516613.26 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bbfc56c4-8525-40eb-b743-693d6d54cbde |
| seao_quebec:1649701:services-ricova-inc | Ville de Vaudreuil-Dorion. | Collecte et transport de déchets et de résidus organiques - Conteneurs semi-enfouis à sac | 281708.05 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=36f87bc6-2347-4124-8336-65ad6117d4b0 |
| seao_quebec:1685493:services-ricova-inc | MRC des Pays-d'en-Haut | Collecte de bacs roulants et transport des matières résiduelles | 2118426.95 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=98f4f76b-0406-4d5a-aa78-88ea08240e3a |
| seao_quebec:1719162:services-ricova-inc | Corporation de gestion des matières résiduelles de La Haute-Yamaska. | Mise en valeur de matières résiduelles | 33276.66 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7de6d0ce-25c5-4596-a4a7-b627c247c8a2 |
| seao_quebec:1721291:services-ricova-inc | MRC de Beauharnois-Salaberry | Collecte, transport et traitement des matières organiques | 1986200.02 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a22e65da-457d-4536-a6e0-5b3bf3b48922 |
| seao_quebec:1734916:services-ricova-inc | Commission scolaire New Frontiers. | Services de recyclage | 34700.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=113589b1-e01d-43cd-9dbc-41952612a110 |
| seao_quebec:1737634:services-ricova-inc | Ville de Vaudreuil-Dorion. | Collecte et transport des matières résiduelles - Déchets et matières organiques | 22594723.56 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7e10982d-3cd7-4dcb-a076-20270b41fa3e |
| seao_quebec:1746365:services-ricova-inc | Ville de Boucherville | Collecte des déchets et des encombrants, des matières recyclables, des résidus verts et des sapins | 2647597.94 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6a330ae7-08da-464c-ba29-6dbc1fb1c9ed |
| seao_quebec:1764006:services-ricova-inc | Ville de Mascouche. | Collecte et transport d’encombrants sur l’avenue de la Gare pour les années 2024 à 2026 | 31282.97 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=96349ed8-0e30-4683-8f1a-b5965d110a0a |
| seao_quebec:1770681:services-ricova-inc | Municipalité de la Paroisse Très-Saint-Sacrement | collecte, transport, traitement et mise en marché des matières recyclables | 89101.72 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2ac3cad9-fec4-4028-9bf2-2a7a9d79ff89 |
| seao_quebec:1774866:services-ricova-inc | Ville de L'Île-Perrot | Services de collecte et transport des résidus organiques et services complémentaires pour les Villes de L'Île Perrot, Pincourt et Notre-Dame-de-l'Île-Perrot pou | 813016.97 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c3e02851-e5d8-4a49-8ddf-fd8a731eb643 |
| seao_quebec:1775324:services-ricova-inc | Ville de Pincourt. | Services de collecte et transport des résidus organiques et services complémentaires pour les Villes de L'Île Perrot, Pincourt et Notre-Dame-de-l'Île-Perrot pou | 919638.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=97c7f34d-cf16-4c3e-a885-fe26fe74a231 |
| seao_quebec:1775534:services-ricova-inc | Ville de Pointe-Claire. | Fournir les services de collecte des matelas et sommiers pour les années 2024, 2025 et 2026 avec deux (2) options de renouvellement | 235463.16 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a4545e1f-c1a8-41f0-b311-0b1dc71a8f28 |
| seao_quebec:1777297:services-ricova-inc | Ville de Boucherville | Chargement et transport des matières résiduelles avec fourniture de conteneur | 50961.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3edde712-bd00-4011-bae0-95406d789a01 |
| seao_quebec:1782715:services-ricova-inc | Ville de Saint-Constant. | Services de location de conteneurs et de collecte pour la disposition des matières résiduelles sur divers sites (bâtiments municipaux) | 295531.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=55438081-ad3b-438b-ba94-906e0dc60b59 |
| seao_quebec:1806705:services-ricova-inc | MRC des Pays-d'en-Haut | Collecte des bacs roulants et transport des matières résiduelles (déchets, matières organiques et encombrants) | 24602849.53 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8b942777-3b84-4c98-a179-5e645f7cdce7 |
| seao_quebec:1807753:services-ricova-inc | Ville de Laval | Service de collecte et de transport des matières résiduelles en conteneurs semi-enfouis à chargement par grue | 792292.73 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a52efc68-263c-469a-a898-cd72a982e6b6 |
| seao_quebec:1810970:services-ricova-inc | Ville de Kirkland. | COLLECTE ET TRANSPORT DES ORDURES MÉNAGÈRES  ET MATIÈRES ORGANIQUES AVEC DEUX (2) OPTIONS DE RENOUVELLEMENT | 947494.21 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7c159969-beb5-47a2-b957-a25c35eec05c |
| seao_quebec:1813038:services-ricova-inc | Ville de Dollard-des-Ormeaux | Collecte des déchets et des matières organiques du 1er juin 2024 au 31 mai 2027, avec 2 options de renouvellement | 2243958.86 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d02ce53b-2f59-4e30-9363-3c1a70cff43a |
| seao_quebec:1819044:services-ricova-inc | Régie Intermunicipale du Comté de Beauce-sud | Collecte et transport de matières recyclables | 9364659.11 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a8ade066-4cfc-47f0-bca5-a210643c7bd7 |
| seao_quebec:1823746:services-ricova-inc | Ville de Montréal - Service de l'environnement | Service de collecte et transport de matières résiduelles de conteneurs à chargement avant et semi-enfouis, incluant la location de conteneurs à chargement avant | 1745047.6 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3a71e53a-bff2-4bc4-b1eb-3685e32abf9d |
| seao_quebec:1826599:services-ricova-inc | Ville de L'Île-Perrot | GT2022-21 – Services de collecte et transport des résidus organiques et services complémentaires pour les municipalités de l'île Perrot | 352145.71 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9b367f90-7b0c-4510-a316-fcb937a7485b |
| seao_quebec:1826891:services-ricova-inc | Ville de Montréal - Service de l'environnement | Collecte et transport des matières résiduelles pour les arrondissements de l'Ile-Bizard-Sainte-Genevièveet Pierrefonds-Roxboro-60 mois + une option de prolongat | 23246993.939999998 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ba9b59fd-2e3a-4038-bb62-e750f79712fb |
| seao_quebec:1828501:services-ricova-inc | Ville de Saint-Lambert | Collecte et transport des déchets, de matières organiques et d'encombrant sur le territoire de la ville de Saint-Lambert | 1264623.33 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fc6d1af8-e055-4f6f-aeb4-ff314006f535 |
| seao_quebec:1845152:services-ricova-inc | Centre de services scolaire des Patriotes | Enlèvement des rebuts pour certaines unités administratives du centre de services scolaire des patriotes | 5153.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=77e9ba4c-31db-4924-b122-17a829defd13 |
| seao_quebec:20005896:services-ricova-inc | MRC de Montmagny | Collecte et transport des matières recyclables dans la MRC de Montmagny 2025-2029 | 2642036.89 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0cb12a76-0353-466b-849c-9e98b87cad7f |
| seao_quebec:20006655:services-ricova-inc | MRC d'Argenteuil | COLLECTE ET TRANSPORT DES MATIÈRES RÉSIDUELLES ET RÉSIDUS ENCOMBRANTS POUR LES ANNÉES 2025 À 2029 AVEC UNE POSSIBILITÉ DE RENOUVELLEMENT POUR DEUX (2) PÉRIODES  | 362659.46 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1421d3c4-c5e7-411d-b2d2-bed707b0236c |
| seao_quebec:20011641:services-ricova-inc | Ville de Chambly | Collecte, transport et traitement ou élimination des matières recyclables, organiques, ordures, encombrants, résidus verts et matières recyclables | 10369944.49 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=38537dad-9b10-4d28-aa28-b590e25a0b82 |
| seao_quebec:20011827:services-ricova-inc | MRC de Matawinie | Services de collecte et transport des matières recyclables de cinq municipalités de la MRC de Matawinie (axe 125) | 1207613.34 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=24bda949-5ad6-49f7-8346-9767c7491836 |
| seao_quebec:20022194:services-ricova-inc | Ville de Deux-Montagnes. | Collecte et transport des déchets et des matières organiques - Années 2025-2028 | 826210.1 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=213af427-8e57-4510-b0b1-28114790b8ae |
| seao_quebec:20022760:services-ricova-inc | MRC de Rivière-du-Loup | Collecte et transport des matières résiduelles | 1449125.86 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=818b46e0-0942-4a39-b743-d0ffa2b786ee |
| seao_quebec:20027889:services-ricova-inc | Ville de Dollard-des-Ormeaux | Poursuite et fin des opérations de nettoyage de la Ville suite aux pluies diluviennes du 9 août 2024 | 46726.32 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3c691d80-e89b-4044-ba27-ebc7d20927c4 |
| … 81 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

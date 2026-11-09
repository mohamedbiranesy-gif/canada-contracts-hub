# S1-05 — Hydro-Québec ⇄ G.L.R. INC.

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08) — 75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA — buyer tax no. 119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: "car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605")
SUBMIT TO: comptes.fournisseurs@hydro.qc.ca (invoicing/AP mailbox, confirmed by the referee) | format: facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)
REFERENCE: contract 20169105 (ocds_contract_ids); tender AM010743 (numero) | PO rule: yes (as published: PO/Reference)
FROM / REMIT TO: G.L.R. INC. — 1150 rue Valets,, L'Ancienne-Lorette, QC, G2E5Y9 | GST/HST 102123858RT0001 (account derived from the BN9) | NEQ 1143021146
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: pai
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 97
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Hydro-Québec (utility / public corporation, QC) — public contract / purchase award with a published end date (dated record): G.L.R. INC. | subject: Provincial / Contrat-cadre multi projets - lignes aériennes de transport | instrument: contract | contract number: 20169105 (ocds_contract_ids); AM010743 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as  | solicitation: AM010743 (numero) | all identifiers: {"numeroseao": "20127043", "numero": "AM010743", "ocid": "ocds-ec9k95-20127043", "ocds_contract_ids": ["20169105"], "ocds_award_ids": ["20169105"], "seao_item_id": "dd3a427f-7e84-417a-bc85-f357d282fb9a"} | value: 103320625.0 CAD | awarded 2026-07-23, start 2026-07-23, end 2029-01-22 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dd3a427f-7e84-417a-bc85-f357d282fb9a | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 1593 records with Canada-located vendors (1081 distinct vendors; 579 in the last 12 months; latest 2026-12-01)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:43240b176b1f24b7
- **tier**: A
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Hydro-Québec
- **buyer_website**: https://www.hydroquebec.com
- **buyer_address**: 75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA
- **buyer_phone**: +1-888-858-7927
- **buyer_contact_evidence_url**: https://www.hydroquebec.com/nous-joindre/
- **buyer_legal_name_as_published**: Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)
- **buyer_bn_as_published**: 119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: "car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605")
- **buyer_bn_program**: RT (GST/HST program account)
- **buyer_gst_hst_derived**: 119449775RT0001 (printed by the buyer itself; not derived)
- **buyer_website_status**: site answers
- **buyer_registry_id**: NEQ 8811141181 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: utility / public corporation
- **buyer_sector**: utility
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q167840; Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity
- **buyer_founded**: 1944-04-14 (Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 13638000000 Q1104069; 12881000000 Q1104069; 12228000000 Q1104069 (Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)
- **buyer_employees**: 23616 (Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)
- **buyer_legal_form**: Crown corporation (Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.hydroquebec.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; website: site answers; invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the lane's AP page (https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptes.fournisseurs@hydro.qc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html
- **email_evidence_quote**: Transmettez votre facture à Hydro-Québec ou à la Société d'énergie de la Baie James (SEBJ) par courriel à l'adresse suivante : comptes.fournisseurs@hydro.qc.ca.
- **email_evidence_context**: serez pour envoyer votre facture sera celle que nous utiliserons pour vous informer des rejets (ou refus) de factures. Faites parvenir votre facture à Hydro-Québec ou à la Société d’énergie de la Baie James (SEBJ) par courriel à l’adresse suivante : comptes.fournisseurs@hydro.qc.ca Cette adresse courriel est utilisée uniquement pour la réception de factures ou de crédits. Tous les autres documents reçus à cette adresse courriel (états de compte ou autre) seront détruits. La facture, qui doit être ajoutée en pièce jointe au cou (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptes.fournisseurs@hydro.qc.ca (invoicing/AP) | researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-11-01 | page: https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html | quote: "Transmettez votre facture à Hydro-Québec ou à la Société d'énergie de la Baie James (SEBJ) par courriel à l'adresse suivante : comptes.fournisseurs@hydro.qc.ca." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: gemini/gemini_buyer_ap_results_batch22.csv task GE-AP-P0027
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=reject; fo=1; rua=mailto:dmarc@hydro.qc.ca;ruf=mailto:dmarc@hydro.qc.ca
- **dmarc_record_domain**: hydro.qc.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:199.22.56.220 ip4:199.22.60.220 a:mailer.visard.ca include:spf.hornetsecurity.com a:smtp-50.lnk01.com a:smtp-out.ivalua.ca ip4:172.16.40.64 ip4:216.191.121.194 include:spf.protection.outlook.com include:sendgrid.net ip4:74.213.188.78 ip4:24.137.204.14 ip4:24.137.204.2 ip4:69.77.177.51 inc
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements**: Bill-to: Hydro-Québec ou la Société d'énergie de la Baie James (SEBJ); PO/Reference required: Numéro de commande (10 chiffres débutant par 45, ou 7 chiffres 9XXXXXX / 8 chiffres 19XXXXXX ou 7XXXXXXX) ou CII (2 lettres + 4 chiffres); Format: pièce jointe PDF (texte de préférence), TIFF (min 400 ppp), | invoice format as published: facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)
- **payment_terms_as_published**: paiement se fait habituellement dans les 30 jours (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: PO/Reference)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "paiement se fait habituellement dans les 30 jours (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)", "po_required": "yes (as published: PO/Reference)", "invoice_format": "facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)", "requirements_text": "Bill-to: Hydro-Québec ou la Société d'énergie de la Baie James (SEBJ); PO/Reference required: Numéro de commande (10 chiffres débutant par 45, ou 7 chiffres 9XXXXXX / 8 chiffres 19XXXXXX ou 7XXXXXXX) ou CII (2 lettres + 4 chiffres); Format: pièce jointe PDF (texte de préférence), TIFF (min 400 ppp),"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08) — 75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA — buyer tax no. 119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: "car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605") ⏎ SUBMIT TO: comptes.fournisseurs@hydro.qc.ca (invoicing/AP mailbox, confirmed by the referee) | format: facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08) ⏎ REFERENCE: contract 20169105 (ocds_contract_ids); tender AM010743 (numero) | PO rule: yes (as published: PO/Reference) ⏎ FROM / REMIT TO: G.L.R. INC. — 1150 rue Valets,, L'Ancienne-Lorette, QC, G2E5Y9 | GST/HST 102123858RT0001 (account derived from the BN9) | NEQ 1143021146 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | 
- **invoice_card_json**: {"bill_to": {"legal_name": "Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA", "address_is_the_invoice_address": false, "tax_number": "119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: \"car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605\")", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptes.fournisseurs@hydro.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: PO/Reference)", "po_number": "", "contract_or_agreement_number": "20169105 (ocds_contract_ids); AM010743 (numero) — the source publishes the award under this tender / notice number and no sepa
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20169105 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: G.L.R. INC.
- **vendor_legal_name**: G.L.R. INC.
- **vendor_trading_name**: GLR (other names in the registry)
- **vendor_registry_id**: Corporations Canada (corporation number): 1770527; NEQ 1143021146 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=1770527
- **vendor_registered_address**: 1150 Rue Valets, L'Ancienne-Lorette, QC, G2E 5Y9, CA
- **vendor_neq**: 1143021146 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 4037 — ENTREPR. GÉNÉRAL CONST. LIGNES DE TRANSPORT D'ÉNERGIE ET TOURS MICRO-ONDES
- **vendor_employees_quebec**: De 100 à 249
- **vendor_directors_range**: 1 to 9 directors (Corporations Canada)
- **vendor_last_annual_filing**: REQ annual declaration 2025; Corporations Canada anniversary 1984-09-19
- **vendor_address**: 1150 rue Valets,, L'Ancienne-Lorette, QC, G2E5Y9
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_bn9**: 102123858
- **vendor_gst_hst_derived**: 102123858RT0001
- **vendor_website**: https://glrinc.ca/contact/
- **vendor_emails**: glr@glrinc.ca; payables@glrinc.ca
- **vendor_phone**: (418) 872-7420
- **vendor_contact_evidence_url**: https://glrinc.ca/contact/
- **vendor_logo_url**: https://glrinc.ca/wp-content/uploads/2025/01/Logo-RougeBlanc-Side-1.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/glrqc
- **vendor_billing_ar_email**: payables@glrinc.ca
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://glrinc.ca/contact/; https://glrinc.ca/contact/
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Corporations Canada (corporation number): 1770527; NEQ 1143021146 (Registraire des entreprises du Québec (open data)) status Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-02-27) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); BN9: corporations_canada 1770527 (exact match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1984-09-19; phone / role e-mails / logo: the vendor's own site, https://glrinc.ca/contact/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://glrinc.ca/contact/; https://glrinc.ca/contact/; website: https://glrinc.ca/contact/ (site answers); NEQ: 1143021146 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: SERVICES MENAGERS TRIFLUVIENS INC: 1% of 1593 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active; Québec REQ (NEQ): Immatriculée (1995-02-27)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1984-09-19
- **vendor_years_in_business**: 42.1 (since 1984-09-19, registry date)
- **vendor_bn_source**: corporations_canada 1770527 (exact match)

## Contract
- **po_required_as_published**: yes (as published: PO/Reference)
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20127043", "numero": "AM010743", "ocid": "ocds-ec9k95-20127043", "ocds_contract_ids": ["20169105"], "ocds_award_ids": ["20169105"], "seao_item_id": "dd3a427f-7e84-417a-bc85-f357d282fb9a"}
- **contract_title**: Provincial / Contrat-cadre multi projets - lignes aériennes de transport
- **commodity**: 72141122 Construction de lignes électriques
- **contract_description**: works; Travaux de construction
- **contract_or_agreement_number**: 20169105 (ocds_contract_ids); AM010743 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: AM010743 (numero)
- **award_or_notice_id**: 20127043 (numeroseao); 20169105 (ocds_award_ids); ocds-ec9k95-20127043 (ocid); dd3a427f-7e84-417a-bc85-f357d282fb9a (seao_item_id)
- **commodity_codes**: UNSPSC 72141122 (Construction de lignes électriques)
- **contract_value**: 103320625.0
- **currency**: CAD
- **award_date**: 2026-07-23
- **start_date**: 2026-07-23
- **end_date**: 2029-01-22
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dd3a427f-7e84-417a-bc85-f357d282fb9a
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 1593
- **records_last_12_months**: 579
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (1500); Hydro-Québec contracts awarded (93)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1593 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Entretien et réparation d’installations extérieures (238); Services de transport des marchandises (57); Services de déneigement (49)

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 119449775RT0001 (printed by the buyer itself; not derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **vendor_gst_hst_derived**: 102123858RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08) — 75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA — buyer tax no. 119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: "car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605") ⏎ SUBMIT TO: comptes.fournisseurs@hydro.qc.ca (invoicing/AP mailbox, confirmed by the referee) | format: facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08) ⏎ REFERENCE: contract 20169105 (ocds_contract_ids); tender AM010743 (numero) | PO rule: yes (as published: PO/Reference) ⏎ FROM / REMIT TO: G.L.R. INC. — 1150 rue Valets,, L'Ancienne-Lorette, QC, G2E5Y9 | GST/HST 102123858RT0001 (account derived from the BN9) | NEQ 1143021146 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | 
- **invoice_card_json**: {"bill_to": {"legal_name": "Hydro-Quebec (label per Wikidata Q167840, official website on the organisation's domain (http://www.hydroquebec.com/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "75 BOUL. René-Lévesque O, Montréal, QC, H2Z1A4, CA", "address_is_the_invoice_address": false, "tax_number": "119449775RT0001 (GST/HST number as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html: \"car nous sommes inscrits aux taxes dans le cadre du régime régulier. Voici les numéros de TPS et de TVQ d’Hydro‑Québec : TPS : 119449775 RT0001 TVQ : 1000042605\")", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptes.fournisseurs@hydro.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi (as printed on https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: PO/Reference)", "po_number": "", "contract_or_agreement_number": "20169105 (ocds_contract_ids); AM010743 (numero) — the source publishes the award under this tender / notice number and no sepa
- **invoice_readiness**: 11/11 invoice elements present
- **ap_grade**: A
- **ap_score**: 86
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; invoice format / requirements published | missing: finance mailbox; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["comptes.fournisseurs@hydro.qc.ca (invoicing/AP)", "researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-11-01", "page: https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html", "quote: \"Transmettez votre facture à Hydro-Québec ou à la Société d'énergie de la Baie James (SEBJ) par courriel à l'adresse suivante : comptes.fournisseurs@hydro.qc.ca.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: gemini/gemini_buyer_ap_results_batch22.csv task GE-AP-P0027"], "buyer_facts": ["address and phone: the buyer's own site, https://www.hydroquebec.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "website: site answers", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the lane's AP page (https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html | 2026-11-08 | ok | paiement se fait habituellement dans les 30 jours | yes (as published: référence Indiquez obligatoirement sur votre facture l’une des références suivantes : Numéro de commande) |  |  |  | facture, qui doit être ajoutée en pièce jointe au courriel, peut être un fichier PDF (en format texte, de préférence, ou en format image), un fi |  | le paiement. Traitement de la facture et paiement : La facture est traitée et payée selon les modalités prévues. Le paiement se fait habituellement dans les 30 jours suivant la date de réception d’une facture valide ou d | James (SEBJ), selon le cas. Tout autre libellé entraînera un rejet de la facture. Un numéro de référence Indiquez obligatoirement sur votre facture l’une des références suivantes : Numéro de commande : série de dix chiff |

## Buyer site facts (org_extras, hydroquebec.com)
- **status**: ok
- **pages**: 1
- **language**: fr
- **domain**: hydroquebec.com
- **key**: b:43240b176b1f24b7
- **name**: Hydro-Québec
- **website**: https://hydroquebec.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "75, boulevard René-Lévesque Ouest, Montréal, QC, H2Z 1A4", "address_country": "CA", "address_url": "https://www.hydroquebec.com/nous-joindre/", "address_method": "json-ld", "address_quote": "social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4 Fermé pour rénovation jusqu'en 2029 En savoir plus Sujets connexes Commentaire", "phone": "+1-888-858-7927", "phone_url": "https://www.hydroquebec.com/nous-joindre/", "domain": "hydroquebec.com", "key": "vd:hydroquebec.com", "name": "Hydro-Québec.", "website": "https://hydroquebec.com/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, glrinc.ca)
- **status**: ok
- **pages**: 2
- **language**: fr
- **logo_url**: https://glrinc.ca/wp-content/uploads/2025/01/Logo-RougeBlanc-Side-1.png
- **logo_basis**: logo image in the site header
- **domain**: glrinc.ca
- **key**: vendor:G.L.R. INC.
- **name**: G.L.R. INC.
- **website**: https://glrinc.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: GLR
- **jsonld_logo**: https://glrinc.ca/wp-content/uploads/2024/12/Logo-GLR-BlancRouge-Tagline-FR-1.png
- **jsonld_url**: https://glrinc.ca/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/glrinc.ca\/","url":"https:\/\/glrinc.ca\/","name":"Accueil - GLR","isPartOf":{"@id":"https:\/\/glrinc.ca\/#website"},"about":{"@id":"https:\/\/glrinc.ca\/#organization"},"primaryImageOfPage":{"@id":"https:\/\/glrinc.ca\
- **jsonld_page**: https://glrinc.ca/
- **linkedin_url**: https://www.linkedin.com/company/glrqc
- **tel_links**: 4188727420; 418 872-7420; 418 872-2001; (418)271-3972; (418)930-0087; (418)520-4846; (418)951-3043; (418)849-0769

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "1150, rue Valets, L'Ancienne-Lorette (Québec), Canada G2E 5Y9", "address_country": "CA", "address_url": "https://glrinc.ca/contact/", "address_method": "pattern", "address_quote": "18) 872-2001 Siège social 1150, rue Valets, L'Ancienne-Lorette (Québec), Canada G2E 5Y9 Vous avez des questions ? Données de facturation Voici les informations à inscr", "phone": "(418) 872-7420", "phone_url": "https://glrinc.ca/contact/", "domain": "glrinc.ca", "key": "vd:glrinc.ca", "name": "G.L.R. INC.", "website": "https://glrinc.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Hydro-Québec | found | HYDRO-QUÉBEC |  | NEQ 8811141181 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | non immatriculée | 1944-04-14 | Montréal | QC | 75 BOUL. René-Lévesque O, Montréal (Québec), H2Z1A4 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Hydro-Québec | Q167840 | official website on the organisation's domain (http://www.hydroquebec.com/) + name |  | Hydro-Quebec | Hydro-Québec | Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity | Crown corporation | Canada | 1944-04-14 | Hydro-Québec Building |
| v | G.L.R. INC. |  |  |  |  |  |  |  |  |  |  |
| v | Hydro-Québec Développement énergétique inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:43240b176b1f24b7",
 "ap_contact_team": {
  "emails": [
   "comptes.fournisseurs@hydro.qc.ca",
   "infoacquisition@hydro.qc.ca",
   "dpas_achats_responsables@hydroquebec.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "comptes.fournisseurs@hydro.qc.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html",
    "quote": "Transmettez votre facture à Hydro-Québec ou à la Société d'énergie de la Baie James (SEBJ) par courriel à l'adresse suivante : comptes.fournisseurs@hydro.qc.ca.",
    "retrieved_date": "2026-11-01",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch22.csv",
    "org": "Hydro-Québec",
    "task_id": "GE-AP-P0027"
   },
   {
    "email": "infoacquisition@hydro.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html",
    "quote": "the same as the one on the purchase order. If a third party delivered the goods or rendered the service, please contact the <a href=\"mailto:infoacquisition@hydro.qc.ca\">Info‑Acquisition Line</a> to let us know.</p> </li> <li><strong>Invoice date</strong></li> <li> <strong>Invoice number</s",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Hydro-Québec",
    "task_id": "GE-AP-P0027"
   },
   {
    "email": "comptes.fournisseurs@hydro.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html",
    "quote": "used to inform you if an invoice is rejected. Send your invoice to Hydro-Québec or Société d’énergie de la Baie James (SEBJ) by e-mail to: comptes.fournisseurs@hydro.qc.ca This email address is used exclusively to receive invoices and credit notes. Any other documents received using this",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Hydro-Québec",
    "task_id": "GE-AP-P0027"
   },
   {
    "email": "dpas_achats_responsables@hydroquebec.com",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/suppliers/contact-us/",
    "quote": ". If you have questions about the procedure, please send an email to DPAS_achats_responsables@hydroquebec.com after consulting the document Other information and most frequently asked questions [PDF 146 kB ] . During th",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Hydro-Québec",
    "task_id": "GE-AP-P0027"
   },
   {
    "email": "comptes.fournisseurs@hydro.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html",
    "quote": "actures. Faites parvenir votre facture à Hydro-Québec ou à la Société d’énergie de la Baie James (SEBJ) par courriel à l’adresse suivante : comptes.fournisseurs@hydro.qc.ca Cette adresse courriel est utilisée uniquement pour la réception de factures ou de crédits. Tous les autres documents",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "Hydro-Québec",
    "task_id": "CL-DP-00872"
   },
   {
    "email": "infoacquisition@hydro.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.hydroquebec.com/fournisseurs/facturation-et-paiement/preparer-transmettre-facture.html",
    "quote": "est le même que celui sur le bon de commande. Si une tierce partie a livré le bien ou rendu le service, communiquez avec la <a href=\"mailto:infoacquisition@hydro.qc.ca\">Ligne Info‑Acquisition</a> pour nous en aviser.</p> </li> <li><strong>La date de la facture</strong></li> <li> <strong>Le",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "Hydro-Québec",
    "task_id": "CL-DP-00872"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of www.hydroquebec.com (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.hydroquebec.com (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.hydroquebec.com (60 pages, robots.txt respected), no AI, no search engine",
  "Wayback Machine URL index of www.hydroquebec.com (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine",
  "Wayback Machine URL index of www.hydroquebec.com (addresses about invoices / suppliers / finance), then 15 live pages read (robots.txt respected), no AI, no search engine"
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| seao_quebec:20127043:g-l-r-inc | seao_quebec | ongoing | Provincial / Contrat-cadre multi projets - lignes aériennes de transport | 103320625.0 | CAD |  |  | {"numeroseao": "20127043", "numero": "AM010743", "ocid": "ocds-ec9k95-20127043", "ocds_contract_ids": ["20169105"], "ocds_award_ids": ["20169105"], "seao_item_id": "dd3a427f-7e84-417a-bc85-f357d282fb9 | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dd3a427f-7e84-417a-bc85-f357d282fb9a |

## The buyer's other Canadian-vendor records (first 60 of 300)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1236355:total-canada-inc | TOTAL CANADA INC. | Nord-du-Québec - Régional - Fourniture et livraison d'huiles lubrifiantes neuves, de solvant, d'antigel pur et de dégraisseur aux centrales du Nunavik (14 villa | 1690000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0d3d141c-1c54-4f3b-9cea-e577c1582626 |
| seao_quebec:1247645:la-compagnie-de-construction-et-de-developpement-crie-ltee | LA COMPAGNIE DE CONSTRUCTION ET DE DÉVELOPPEMENT CRIE LTÉE | Nord-du-Québec / Résidences Sakami (LG-3) - Remplacement des systèmes d'eau potable et de protection-incendie  | 15577777.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=47561bb7-70b8-4dbe-994b-bfb7a6529699 |
| seao_quebec:1329242:produits-industriels-kara | PRODUITS INDUSTRIELS KARA | Montérégie / Beauharnois et Varenne - Nord-du-Québec / Chibougamau - Fourniture de gel silice et d'hydroxytoluène butylé en sac   | 758069.42 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a7768be8-458b-4e48-98c8-eace6306c2ff |
| seao_quebec:1398499:coentreprise-ata-bersimis | Coentreprise ATA Bersimis  | Côte-Nord / Centrale Bersimis-2 - Travaux préparatoires associés au remplacement des robinets de garde et remplacement des systèmes auxiliaires et de la command | 45533526.37 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d4c9f066-48f2-46fe-8090-48d3c2087b6a |
| seao_quebec:1494593:abb-e-mobilite-inc | ABB E-MOBILITÉ INC. | Fourniture de bornes de recharges rapide à 50 kW pour V.E. |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=31882d80-50b3-4eb3-aa6b-a8e7330925fa |
| seao_quebec:1494593:addenergie-technologies-inc | ADDÉNERGIE TECHNOLOGIES INC. | Fourniture de bornes de recharges rapide à 50 kW pour V.E. |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=31882d80-50b3-4eb3-aa6b-a8e7330925fa |
| seao_quebec:1531678:services-menagers-trifluviens-inc | SERVICES MENAGERS TRIFLUVIENS INC. | Nord-du-Québec - Service d'entretien ménager dans diverses installations d'Hydro-Québec | 1929550.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=536e1011-0787-4484-8bb1-c001bed615df |
| seao_quebec:1544362:aramark-quebec-inc | ARAMARK QUÉBEC INC. | Côte-Nord / Manic-5 et Hart Jaune / Conciergerie, alimentation et hébergement   | 11800439.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f7b3843e-863d-489d-a0ec-a329819a0384 |
| seao_quebec:1564449:hayes-communications-inc | HAYES COMMUNICATIONS INC. | Plusieurs régions / Signalisation routière de courte durée sur demande  | 2739637.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bfd7dc76-c072-49b5-9e68-cfee5e3872fc |
| seao_quebec:1564449:signalisation-des-cantons-inc | Signalisation des Cantons inc. | Plusieurs régions / Signalisation routière de courte durée sur demande  | 469102.15 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bfd7dc76-c072-49b5-9e68-cfee5e3872fc |
| seao_quebec:1564449:signalisation-gardaworld-s-e-n-c | Signalisation GardaWorld S.E.N.C. | Plusieurs régions / Signalisation routière de courte durée sur demande  | 2136455.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bfd7dc76-c072-49b5-9e68-cfee5e3872fc |
| seao_quebec:1565283:signalisation-stp | SIGNALISATION STP | Laval / Montréal / Montérégie / Capitale-Nationale - Signalisation routière de courte durée du réseau de transport sur demande | 696457.4 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=27dd2e84-1e01-4096-bc36-90a3d509e54e |
| seao_quebec:1565283:signalisation-gardaworld-s-e-n-c | Signalisation GardaWorld S.E.N.C. | Laval / Montréal / Montérégie / Capitale-Nationale - Signalisation routière de courte durée du réseau de transport sur demande | 116789.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=27dd2e84-1e01-4096-bc36-90a3d509e54e |
| seao_quebec:1566155:aeronav-inc | AÉRONAV INC. | Montreal - Acquisition de systèmes automatisés d'observations météorologiques aux aérodromes Hydro-Québec | 507236.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f64d82af-941c-4e8e-bdb5-089cf7b1b383 |
| seao_quebec:1568575:talvi-inc | TALVI INC. | Laval / Poste Duvernay lot 2B et connexes - Travaux de pérennité 315-120 kV  | 6274844.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b8cca1ee-ded2-4b9b-be96-e5218ba7752a |
| seao_quebec:1571250:somavrac-c-c-inc | SOMAVRAC (C.C.) INC. | Mauricie / La Tuque - Travaux d’application d’abat poussières Route 25 et RDC/CA | 2810000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f7ab4509-d6b7-488e-9f03-adf6571bb58b |
| seao_quebec:1571776:electro-saguenay-ltee | ELECTRO SAGUENAY LTÉE | Laval - Fourniture d'abris météo avec revêtement métallique | 703412.79 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=40a14c06-14a6-4d90-b2af-6355bb312859 |
| seao_quebec:1573612:transelec-common-inc | TRANSELEC/COMMON INC. | Montréal / Beaumont_Fleury_Canalisation souterraine et forage_120kV | 13657844.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b8caecfc-5898-43c1-99d2-2e7edbee1736 |
| seao_quebec:1576246:egl-construction-inc | EGL CONSTRUCTION INC. | Saguenay-Lac-St-Jean / Poste Chamouchouane - Lot 2- Agrandissement du poste, ajout d’une section 735 kV et remplacement de disjoncteurs et transformateurs de co | 27672220.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3e85097f-467b-476f-b860-04dfdfba4e2c |
| seao_quebec:1576805:prevention-incendie-safety-first-inc | PRÉVENTION-INCENDIE SAFETY FIRST INC. | Provincial - Entretien des extincteurs | 996030.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d6fa9b0b-451a-44b6-a565-3e3f8dcc2628 |
| seao_quebec:1576805:protection-incendie-piq-inc | Protection Incendie PIQ inc. | Provincial - Entretien des extincteurs | 952997.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d6fa9b0b-451a-44b6-a565-3e3f8dcc2628 |
| seao_quebec:1577350:groupe-pro-b-inc | GROUPE PRO-B INC. | Mauricie / Centrale La Trenche - Ajout d'un séparateur eau/huile de type gravitaire | 995102.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=93684e44-cc0d-41da-9121-395a3ccbe2e6 |
| seao_quebec:1577356:transelec-common-inc | TRANSELEC/COMMON INC. | Montréal / Poste Saraguay - Chomedey  | 12120444.86 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d5ed5a43-6975-4de0-996d-e8ee34448b0b |
| seao_quebec:1577363:echafaudage-falardeau-inc | ÉCHAFAUDAGE FALARDEAU INC. | Provincial - Fourniture d'échafaudages sur demande | 1824984.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=464220ef-a44f-46fb-8ecf-e1b0419a9de9 |
| seao_quebec:1577363:echafaudage-industriel-inc | ÉCHAFAUDAGE INDUSTRIEL INC. | Provincial - Fourniture d'échafaudages sur demande | 3437707.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=464220ef-a44f-46fb-8ecf-e1b0419a9de9 |
| seao_quebec:1577371:deshaies-raymond-inc | DESHAIES & RAYMOND INC. | Montérégie - Construction du Centre de Services de St Bruno Atelier TransÉnergie | 12982324.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a7ce28d4-f04b-4632-913b-7b0e49fd6077 |
| seao_quebec:1578989:g-tek | G-TEK | Capitale-Nationale / Montmorency - Construction, entretien et modification sur demande de réseaux souterrains de distribution | 3694612.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9769877e-3504-4a9c-89ad-d767a6b148fa |
| seao_quebec:1579454:kepasc | KEPASC | PROVINCIAL - Service sur demande de déboisement | 466724.65 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dccd0175-7b8e-4e87-b4e4-2c659fe3a5d5 |
| seao_quebec:1579454:9192-8994-quebec-inc | 9192-8994 QUÉBEC INC. | PROVINCIAL - Service sur demande de déboisement | 632734.51 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dccd0175-7b8e-4e87-b4e4-2c659fe3a5d5 |
| seao_quebec:1579454:deboisement-raymond-ste-marie-inc | DÉBOISEMENT RAYMOND STE-MARIE INC. | PROVINCIAL - Service sur demande de déboisement | 1731173.58 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dccd0175-7b8e-4e87-b4e4-2c659fe3a5d5 |
| seao_quebec:1581024:construction-meskano-inc | CONSTRUCTION MESKANO INC. | Mauricie / La Tuque / Centrale Rapide-Blanc - Service de signaleurs | 601530.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ebed1070-e7b0-4507-ab6a-784ad7159bf5 |
| seao_quebec:1582166:couverture-montreal-nord-ltee | COUVERTURE MONTRÉAL-NORD LTÉE | Plusieurs régions - Réfection de toitures | 10155151.34 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3134c943-5432-47de-8810-ba2ff4deaf30 |
| seao_quebec:1584944:fcnq-construction-inc | FCNQ CONSTRUCTION INC. | Nord-du-Québec - Puvirnituq - Nouvelle centrale diesel lot #1 | 10083919.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ceb18358-2adc-4cf2-ac9c-f34296e915ec |
| seao_quebec:1587743:mcinnis-fils-inc | MCINNIS & FILS INC. | Plusieurs régions - Maîtrise de la végétation - Entretien mécanique | 487035.6 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c7a4032a-7525-4943-b667-c4839b1499c0 |
| seao_quebec:1588189:construction-valard-quebec-inc | CONSTRUCTION VALARD (QUÉBEC) INC. | Mauricie / Montérégie - Plantage de poteaux | 17120785.28 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2605bbf6-7254-4ee7-9863-72a81edc963f |
| seao_quebec:1588189:les-entreprises-electriques-angers-inc | LES ENTREPRISES ÉLECTRIQUES ANGERS INC. | Mauricie / Montérégie - Plantage de poteaux | 15102139.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2605bbf6-7254-4ee7-9863-72a81edc963f |
| seao_quebec:1591643:les-chariots-kirmar-inc | LES CHARIOTS KIRMAR INC. | Montérégie / Outaouais – Transport de véhicules et d’équipements | 166359.93 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=50b4fe25-feaa-455b-9804-a89f20f47f72 |
| seao_quebec:1592852:transelec-common-inc | TRANSELEC/COMMON INC. | Nord-du-Qc / Poste Chibougamau - Travaux de remplacement du T2, d'agrandissement du poste et de déplacement des chemins existants. | 4191209.36 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b4eb7c45-5be8-4756-a188-a56dd6ef4ee7 |
| seao_quebec:1593768:9150-2344-quebec-inc | 9150-2344 QUÉBEC INC. | Île-de-la-Madeleine / Plusieurs  adresses - Entretien ménager | 1330175.39 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fd871056-d19a-42be-87f5-869bb58087bd |
| seao_quebec:1594385:transport-r-lamarre-et-fils | Transport R. Lamarre et Fils | Côte-Nord / Micoua - Route accès et Campement Uaueiashtan - Service de déneigement | 482106.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7e4be88d-dc7f-49c0-86fb-cf1294731b0e |
| seao_quebec:1595661:moteurs-electriques-laval-ltee | MOTEURS ÉLECTRIQUES LAVAL LTÉE | Complexe Robert-Bourassa - Fourniture de réfection des moteurs de pompes | 485000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=442b152f-4864-468b-8912-718dd88808a3 |
| seao_quebec:1596245:centrap-inc | CENTRAP INC. | Entretien Ménager - Plusieurs adresses | 1067115.13 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:maintenance-trans-quebec-inc | MAINTENANCE TRANS-QUÉBEC INC. | Entretien Ménager - Plusieurs adresses | 832764.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:services-menagers-trifluviens-inc | SERVICES MENAGERS TRIFLUVIENS INC. | Entretien Ménager - Plusieurs adresses | 651860.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:nettoyage-g-s-b | NETTOYAGE G.S.B. | Entretien Ménager - Plusieurs adresses | 272913.28 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:nasco-entretien-menager-d-immeubles-inc | NASCO ENTRETIEN MÉNAGER D'IMMEUBLES INC. | Entretien Ménager - Plusieurs adresses | 1131740.96 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:solutions-thermaclean-inc | Solutions Thermaclean inc. | Entretien Ménager - Plusieurs adresses | 178199.84 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1596245:qualipro | QUALIPRO | Entretien Ménager - Plusieurs adresses | 532123.68 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=561702fb-8327-49d1-a171-bd530004d846 |
| seao_quebec:1607149:gfl-environmental-inc | GFL ENVIRONMENTAL INC. | Plusieurs régions / Gestion des matières résiduelles | 620318.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ca6243c2-4a52-4001-8a77-c9ab4cb742a9 |
| seao_quebec:1607658:toromont-cat-quebec | TOROMONT CAT (Québec) | Groupes Électrogènes - Contrat-Cadre fourniture pièces de rechange et services - Réseaux Autonomes et CSP | 50700000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a2f44c28-c750-4687-9066-8553280b0921 |
| seao_quebec:1611005:remorquage-mbb | REMORQUAGE MBB | Outaouais – Transport de véhicules et d’équipements | 935275.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ed815d39-8a87-4d21-99bf-8b4c7d6842d4 |
| seao_quebec:1620818:irving-oil-limited | IRVING OIL LIMITED | Îles-de-la-Madeleine - Fourniture de Carburants et Huile lubrifiante | 8671696.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=392f357d-cd9e-4ca6-83b8-d986e706b8f5 |
| seao_quebec:1620818:kildair-service-ulc | KILDAIR SERVICE ULC | Îles-de-la-Madeleine - Fourniture de Carburants et Huile lubrifiante | 111578104.14 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=392f357d-cd9e-4ca6-83b8-d986e706b8f5 |
| seao_quebec:1640390:atelier-de-debosselage-baie-comeau-inc | ATELIER DE DÉBOSSELAGE BAIE-COMEAU INC. | Provincial - Services de réparation de carrosserie de véhicules légers | 122278.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d6e6acce-41fe-4d67-885a-b97ec9efa926 |
| seao_quebec:1640390:2853-5185-quebec-inc | 2853-5185 QUÉBEC INC. | Provincial - Services de réparation de carrosserie de véhicules légers | 69484.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d6e6acce-41fe-4d67-885a-b97ec9efa926 |
| seao_quebec:1643608:transport-guilbault-inc | TRANSPORT GUILBAULT INC. | Provincial - Service sur demande, de transport de marchandises en expédition de détail  (LTL) | 11315000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bad7025c-468b-4c82-b5da-24f3cbbcbeee |
| seao_quebec:1646615:lanauco | Lanauco | Provincial - Construction, entretien et modification de réseaux de distribution aériens | 23298434.4 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=56bedc12-c68b-4cbc-a9e7-1a5ef898cbd4 |
| seao_quebec:1646615:laurin-laurin-1991-inc | LAURIN, LAURIN (1991) INC. | Provincial - Construction, entretien et modification de réseaux de distribution aériens | 21502050.1 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=56bedc12-c68b-4cbc-a9e7-1a5ef898cbd4 |
| seao_quebec:1646615:construction-valard-quebec-inc | CONSTRUCTION VALARD (QUÉBEC) INC. | Provincial - Construction, entretien et modification de réseaux de distribution aériens | 47509106.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=56bedc12-c68b-4cbc-a9e7-1a5ef898cbd4 |
| seao_quebec:1646615:electro-saguenay-ltee | ELECTRO SAGUENAY LTÉE | Provincial - Construction, entretien et modification de réseaux de distribution aériens | 7597348.33 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=56bedc12-c68b-4cbc-a9e7-1a5ef898cbd4 |
| … 240 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

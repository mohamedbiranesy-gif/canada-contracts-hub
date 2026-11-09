# S5-07 — Cégep Garneau ⇄ LES ARTISANS DU PAYSAGE DU QUÉBEC INC.

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08) — 1660, boulevard de L'Entente, Québec (Québec) G1S 4S3
SUBMIT TO: finances@cegepgarneau.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: contract 20171734 (ocds_contract_ids); tender 2627-11-AOP (numero) | PO rule: not published
FROM / REMIT TO: LES ARTISANS DU PAYSAGE DU QUÉBEC INC. — 7668 Boul. Wilfrid-Hamel,, Québec, QC, G2G1C1 | GST/HST number not public | NEQ 1177062164
TAX: montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-etudiants-internat | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Déneigement | AMOUNT: 491,269.42 CAD
```

## Relationship
- **rank_group**: A3
- **data_quality_score**: 85
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 203
- **reverify_due**: yes (mailbox evidence older than 60 days)
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Cégep Garneau (university / college, QC) — public contract / purchase award with a published end date (dated record): LES ARTISANS DU PAYSAGE DU QUÉBEC INC. | subject: Déneigement | instrument: contract | contract number: 20171734 (ocds_contract_ids); 2627-11-AOP (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it  | solicitation: 2627-11-AOP (numero) | all identifiers: {"numeroseao": "20164859", "numero": "2627-11-AOP", "ocid": "ocds-ec9k95-20164859", "ocds_contract_ids": ["20171734"], "ocds_award_ids": ["20171734"], "seao_item_id": "0fe1dce2-6900-43f1-98ed-b05dc64750f5"} | value: 491269.42 CAD | awarded 2026-10-16, start 2026-10-16, end 2029-10-16 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0fe1dce2-6900-43f1-98ed-b05dc64750f5 | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 167 records with Canada-located vendors (134 distinct vendors; 19 in the last 12 months; latest 2026-10-16)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:d34268a4888e9125
- **tier**: A
- **grade**: 3
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Cégep Garneau
- **buyer_website**: https://espace-etudiant.cegepgarneau.ca
- **buyer_address**: 1660 boul. de l'Entente, Québec, QC, G1S4S3, CA
- **buyer_contact_evidence_url**: https://espace-etudiant.cegepgarneau.ca/nous-joindre/
- **buyer_legal_name_as_published**: Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08)
- **buyer_logo_url**: https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/03/Icone_G_blanc.svg
- **buyer_registry_id**: NEQ 8814178875 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_municipal_tier**: local municipality (MAMH répertoire) (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08)
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q3009985; CEGEP; charitable organization
- **buyer_founded**: 1969-08-00 (Wikidata Q3009985, official website on the organisation's domain (http://cegepgarneau.ca) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 47199592 Q1104069; 46982830 Q1104069; 47265436 Q1104069; 47334498 Q1104069; 50712729 Q1104069; 52242306 Q1104069; 560503 (Wikidata Q3009985, official website on the organisation's domain (http://cegepgarneau.ca) + name; 2026-11-08)
- **buyer_employees**: 956; 944; 928; 753; 930; 965; 816; 805; 794; 829; 1181; 1283; 1245; 1159; 1847; 1804; 1923; 1823; 1865; 2233; 2253; 2303 (Wikidata Q3009985, official website on the organisation's domain (http://cegepgarneau.ca) + name; 2026-11-08)
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8814178875, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://espace-etudiant.cegepgarneau.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; AP phone: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/); invoice mailing address: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/); invoicing requirements: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/)
- **buyer_tax_exempt_status**: montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-etudiants-internationaux-A2026.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finances@cegepgarneau.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/
- **email_evidence_quote**: Par la suite, tu dois ajouter le destinataire Cégep Garneau et l'adresse courriel finances@cegepgarneau.ca. ... 418 688-8310 communications@cegepgarneau.ca.
- **email_evidence_context**: , comme les épiceries, les dépanneurs, etc. 2. VIREMENT INTERAC Tout d’abord, tu dois te rendre sur le site de ton institution bancaire et choisir le virement Interac. Par la suite, tu dois ajouter le destinataire Cégep Garneau et l’adresse courriel finances@cegepgarneau.ca . Ensuite, tu dois inscrire une question de sécurité. Elle n’aura aucun impact pour nous puisque nous sommes inscrits au dépôt automatique, mais tu devras tout de même en créer une. Pour ce faire, nous te suggérons d’inscrire la question Quel est mo (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finances@cegepgarneau.ca (finance/accounting dept or supplier-payment office) | researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-04-20 | page: https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/ | quote: "Par la suite, tu dois ajouter le destinataire Cégep Garneau et l'adresse courriel finances@cegepgarneau.ca. ... 418 688-8310 communications@cegepgarneau.ca." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: gemini/gemini_buyer_ap_results_batch05.csv task GE-AP-00406
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:admin@cegepgarneau.ca; sp=none; adkim=r; aspf=r; ruf=mailto:admin@cegepgarneau.ca; fo=1
- **dmarc_record_domain**: cegepgarneau.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:206.167.102.0/23 ip4:206.167.100.0/23 ip4:206.167.109.246 ip4:167.114.208.11 ip4:199.202.73.3 ip4:206.167.139.18 ip4:206.167.139.17 ip4:199.202.87.56 ip4:198.50.195.209  ip4:173.46.148.17 ip4:174.142.128.36 ip4:192.77.70.7 ip4:67.215.2.146 ip4:72.0.195.148/30 ip4:54.232.96.81 ip4:54.232.9
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 418 688-8310, poste 2461
- **invoice_mailing_address**: 1660, boulevard de L'Entente, Québec (Québec) G1S 4S3
- **invoicing_requirements**: Finance department email finances@cegepgarneau.ca; Direction des finances phone 418 688-8310 poste 2461; general email communications@cegepgarneau.ca.
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "418 688-8310, poste 2461", "mailing_address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3", "requirements_text": "Finance department email finances@cegepgarneau.ca; Direction des finances phone 418 688-8310 poste 2461; general email communications@cegepgarneau.ca."}
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08) — 1660, boulevard de L'Entente, Québec (Québec) G1S 4S3 ⏎ SUBMIT TO: finances@cegepgarneau.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract 20171734 (ocds_contract_ids); tender 2627-11-AOP (numero) | PO rule: not published ⏎ FROM / REMIT TO: LES ARTISANS DU PAYSAGE DU QUÉBEC INC. — 7668 Boul. Wilfrid-Hamel,, Québec, QC, G2G1C1 | GST/HST number not public | NEQ 1177062164 ⏎ TAX: montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-etudiants-internat | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Déneigement | AMOUNT: 491,269.42 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08)", "legal_name_is_published": true, "address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "finances@cegepgarneau.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20171734 (ocds_contract_ids); 2627-11-AOP (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20171734 (ocds_contract_ids) — source seao_quebec"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-et
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 66
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20171734 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: LES ARTISANS DU PAYSAGE DU QUÉBEC INC.
- **vendor_legal_name**: LES ARTISANS DU PAYSAGE DU QUÉBEC INC.
- **vendor_trading_name**: Aménagement artizen; Aménagement artizens; Artizen; Artizen du paysage; LES ARTISANS DU PAYSAGE; Les Aménagements Paysart; Les Terres en Vrac du Québec; MPCH Neige et Excavation; Mon pays c'est l'hiver!; Mon pays c'est l'hiver! Déneigement Professionnel; Multivrac RG; Paysagiste Artizen; Paysagiste  (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1177062164; NEQ 1177062164 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 7668 BOUL. Wilfrid-Hamel, Québec (Québec), G2G1C1
- **vendor_neq**: 1177062164 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — QUÉBEC : Loi sur les sociétés par actions (RLRQ, C. S-31.1)
- **vendor_activity_code**: CAE 4219 — Réalisation de plans d'aménagement paysager, entretien d'espaces verts, déneigement, création et installation de décorations festives, conception de plans d'aménagement paysager
- **vendor_employees_quebec**: De 50 à 99
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 7668 Boul. Wilfrid-Hamel,, Québec, QC, G2G1C1
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_website**: https://permacon.ca/en/installer/les-artisans-du-paysage-du-quebec-inc/
- **vendor_emails**: artisans@artisansdupaysage.com
- **vendor_phone**: 1 888 737-6226
- **vendor_contact_evidence_url**: https://permacon.ca/fr/contact/
- **vendor_logo_url**: https://permacon.ca/wp-content/themes/permacon/dist/images/logo_6681b97e61e522d5629c.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://ca.linkedin.com/company/permaconapg
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://veq.ca/directory/les-artisans-du-paysage-du-quebec-inc/
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Québec REQ (NEQ): 1177062164; NEQ 1177062164 (Registraire des entreprises du Québec (open data)) status Québec REQ (NEQ): Immatriculée (2021-11-02) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); incorporated / registered: 2021-11-01; phone / role e-mails / logo: the vendor's own site, https://permacon.ca/fr/contact/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://veq.ca/directory/les-artisans-du-paysage-du-quebec-inc/; website: https://permacon.ca/en/installer/les-artisans-du-paysage-du-quebec-inc/ (site answers); NEQ: 1177062164 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Les Constructions Jean Méthot Ltée.: 4% of 167 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2021-11-02)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 2021-11-01
- **vendor_years_in_business**: 5.0 (since 2021-11-01, registry date)

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20164859", "numero": "2627-11-AOP", "ocid": "ocds-ec9k95-20164859", "ocds_contract_ids": ["20171734"], "ocds_award_ids": ["20171734"], "seao_item_id": "0fe1dce2-6900-43f1-98ed-b05dc64750f5"}
- **contract_title**: Déneigement
- **commodity**: 72102903 Déneigement des toitures, entrées et stationnements
- **contract_description**: services; Services de nature technique
- **contract_or_agreement_number**: 20171734 (ocds_contract_ids); 2627-11-AOP (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: 2627-11-AOP (numero)
- **award_or_notice_id**: 20164859 (numeroseao); 20171734 (ocds_award_ids); ocds-ec9k95-20164859 (ocid); 0fe1dce2-6900-43f1-98ed-b05dc64750f5 (seao_item_id)
- **commodity_codes**: UNSPSC 72102903 (Déneigement des toitures, entrées et stationnements)
- **contract_value**: 491269.42
- **currency**: CAD
- **award_date**: 2026-10-16
- **start_date**: 2026-10-16
- **end_date**: 2029-10-16
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0fe1dce2-6900-43f1-98ed-b05dc64750f5
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 167
- **records_last_12_months**: 19
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (167)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 167 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Technologies de l'information, radiodiffusion et télécommuni (4); Services informatiques (3); Services d’ingénierie (3)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08) — 1660, boulevard de L'Entente, Québec (Québec) G1S 4S3 ⏎ SUBMIT TO: finances@cegepgarneau.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract 20171734 (ocds_contract_ids); tender 2627-11-AOP (numero) | PO rule: not published ⏎ FROM / REMIT TO: LES ARTISANS DU PAYSAGE DU QUÉBEC INC. — 7668 Boul. Wilfrid-Hamel,, Québec, QC, G2G1C1 | GST/HST number not public | NEQ 1177062164 ⏎ TAX: montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-etudiants-internat | CURRENCY: CAD | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Déneigement | AMOUNT: 491,269.42 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "Cégep Garneau (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08)", "legal_name_is_published": true, "address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "finances@cegepgarneau.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20171734 (ocds_contract_ids); 2627-11-AOP (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20171734 (ocds_contract_ids) — source seao_quebec"}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "montant total de la facture (avant les taxes) (as printed on https://espace-etudiant.cegepgarneau.ca/wp-content/uploads/sites/3/2026/06/Guide-et
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 66
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["finances@cegepgarneau.ca (finance/accounting dept or supplier-payment office)", "researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-04-20", "page: https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/", "quote: \"Par la suite, tu dois ajouter le destinataire Cégep Garneau et l'adresse courriel finances@cegepgarneau.ca. ... 418 688-8310 communications@cegepgarneau.ca.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: gemini/gemini_buyer_ap_results_batch05.csv task GE-AP-00406"], "buyer_facts": ["address and phone: the buyer's own site, https://espace-etudiant.cegepgarneau.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "AP phone: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/)", "invoice mailing address: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/)", "invoicing requirements: the lane's AP page (https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/)"], "vendor_facts": ["name and address: the re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, domain unknown)
_not read_

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, permacon.ca)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://permacon.ca/wp-content/themes/permacon/dist/images/logo_6681b97e61e522d5629c.svg
- **logo_basis**: logo image in the site header
- **domain**: permacon.ca
- **key**: vendor:LES ARTISANS DU PAYSAGE DU QUÉBEC INC.
- **name**: LES ARTISANS DU PAYSAGE DU QUÉBEC INC.
- **website**: https://permacon.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://ca.linkedin.com/company/permaconapg
- **tel_links**: +18887376226

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "8145, rue Bombardier, Anjou, (Québec), H1J 1A5", "address_country": "CA", "address_url": "https://permacon.ca/fr/contact/", "address_method": "pattern", "address_quote": "e) CAPTCHA Nos coordonnées Siège social : 8145, rue Bombardier, Anjou (Québec), H1J 1A5. 1 888 737-6226 Garantie Catalogues 2026 Consultez les catalogues en ligne Séle", "phone": "1 888 737-6226", "phone_url": "https://permacon.ca/fr/contact/", "domain": "permacon.ca", "key": "vd:permacon.ca", "name": "LES ARTISANS DU PAYSAGE DU QUÉBEC INC.", "website": "https://permacon.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Cégep Garneau | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=C%C3%A9gep%20Garneau | 2026-11-08 |
| buyer | LES ARTISANS DU PAYSAGE DU QUÉBEC INC. | ambiguous |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=LES%20ARTISANS%20DU%20PAYSAGE%20DU%20QU%C3%89BEC%20INC. | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Cégep Garneau | found | COLLÈGE D'ENSEIGNEMENT GÉNÉRAL ET PROFESSIONNEL FRANÇOIS-XAVIER GARNEAU |  | NEQ 8814178875 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 1969-08-07 | Québec | QC | 1660 boul. de l'Entente, Québec (Québec), G1S4S3 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |
| buyer | LES ARTISANS DU PAYSAGE DU QUÉBEC INC. | found | LES ARTISANS DU PAYSAGE DU QUÉBEC INC. |  | NEQ 1177062164 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 2021-11-02 | Québec | QC | 7668 BOUL. Wilfrid-Hamel, Québec (Québec), G2G1C1 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Cégep Garneau | Q3009985 | official website on the organisation's domain (http://cegepgarneau.ca) + name | Collège d’enseignement général et professionnel François-Xavier Garneau [fr-ca] | Cégep Garneau | Cégep Garneau | CEGEP; charitable organization |  | Canada | 1969-08-00 |  |
| b | LES ARTISANS DU PAYSAGE DU QUÉBEC INC. |  |  |  |  |  |  |  |  |  |  |
| v | LES ARTISANS DU PAYSAGE DU QUÉBEC INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:d34268a4888e9125",
 "ap_contact_team": {
  "emails": [
   "finances@cegepgarneau.ca",
   "communications@cegepgarneau.ca"
  ],
  "invoice_portal": null,
  "phone": "418 688-8310",
  "mailing_address": "Service des finances, 1580, boulevard de l'Entente, Local K-2915, Québec (Québec) G1S 4S3",
  "invoicing_requirements": "Finance department email finances@cegepgarneau.ca; Direction des finances phone 418 688-8310 poste 2461; general email communications@cegepgarneau.ca.",
  "evidence": [
   {
    "email": "finances@cegepgarneau.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/",
    "quote": "ton institution bancaire et choisir le virement Interac. Par la suite, tu dois ajouter le destinataire Cégep Garneau et l’adresse courriel finances@cegepgarneau.ca . Ensuite, tu dois inscrire une question de sécurité. Elle n’aura aucun impact pour nous puisque nous sommes inscrits au dépô",
    "retrieved_date": "2026-11-06",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Cégep Garneau",
    "task_id": "GE-AP-44042"
   },
   {
    "email": "communications@cegepgarneau.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": "418 688-8310",
    "mailing_address": "Service des finances, 1580, boulevard de l'Entente, Local K-2915, Québec (Québec) G1S 4S3",
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://cegepgarneau.ca/nous-joindre/",
    "quote": "Cégep Garneau 1660, boulevard de L'Entente Québec (Québec) G1S 4S3 418 688-8310 communications@cegepgarneau.ca",
    "retrieved_date": "2026-11-08",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch44.csv",
    "org": "Cégep Garneau",
    "task_id": "GE-AP-44042"
   },
   {
    "email": "finances@cegepgarneau.ca",
    "type": "finance",
    "invoice_portal": null,
    "phone": "418 688-8310, poste 2461",
    "mailing_address": "1660, boulevard de L'Entente, Québec (Québec) G1S 4S3",
    "requirements": "Finance department email finances@cegepgarneau.ca; Direction des finances phone 418 688-8310 poste 2461; general email communications@cegepgarneau.ca.",
    "applies_to": "all",
    "page_url": "https://espace-etudiant.cegepgarneau.ca/nouveaux-admis/paiement-des-frais-de-session/",
    "quote": "Par la suite, tu dois ajouter le destinataire Cégep Garneau et l'adresse courriel finances@cegepgarneau.ca. ... 418 688-8310 communications@cegepgarneau.ca.",
    "retrieved_date": "2026-04-20",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch05.csv",
    "org": "Cégep Garneau",
    "task_id": "GE-AP-00406"
   }
  ]
 },
 "research_status": {
  "found": 3,
  "not_published": 2
 },
 "queries_tried": [
  "site crawl of espace-etudiant.cegepgarneau.ca (54 pages, robots.txt respected), no AI, no search engine",
  "\"cegepgarneau.ca/nous-joindre\" OR \"cegepgarneau.ca\" \"comptes payables\" OR \"finances\" OR \"688-8310\" \"@\"",
  "browsed https://cegepgarneau.ca/nous-joindre/; site:cegepgarneau.ca \"comptabilite@\" OR \"finances@\"",
  "Claude grounded web search (claude-haiku-5-5); 5 source pages checked",
  "site:cegepgarneau.ca \"finances@cegepgarneau.ca\" OR \"comptes payables\" OR \"comptes à payer\" OR \"fournisseurs\""
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| seao_quebec:20164859:les-artisans-du-paysage-du-quebec-inc | seao_quebec | ongoing | Déneigement | 491269.42 | CAD |  |  | {"numeroseao": "20164859", "numero": "2627-11-AOP", "ocid": "ocds-ec9k95-20164859", "ocds_contract_ids": ["20171734"], "ocds_award_ids": ["20171734"], "seao_item_id": "0fe1dce2-6900-43f1-98ed-b05dc647 | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0fe1dce2-6900-43f1-98ed-b05dc64750f5 |

## The buyer's other Canadian-vendor records (first 60 of 164)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1105081:maintenance-eureka-ltee | Maintenance Euréka Ltée | Services d'entretien ménager pour les pavillons du Cégep Garneau | 2365585.65 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=018862eb-f693-4404-b1af-de75e5ccf0ff |
| seao_quebec:1243502:groupe-de-securite-garda-senc | Groupe de sécurité Garda SENC | Services de sécurité et de gardiennage pour le Cégep Garneau | 1414572.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1f450356-0cbd-462f-a86e-dc6127591d14 |
| seao_quebec:1376597:banque-royale-du-canada | Banque Royale du Canada | Services bancaires | 60000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4d78fc02-a62d-4f82-b766-8af845506fe5 |
| seao_quebec:1428008:brainbox-architecture | BRAINBOX ARCHITECTURE | Services professionnels en architecture - Projet d'agrandissement et de réaménagement du CPE La Frimousse | 31222.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3399a676-f317-463d-bcce-773069584456 |
| seao_quebec:1430250:cima-quebec-s-e-n-c | CIMA Québec s.e.n.c. | Services professionnels en structure et civil - CPE La Frimousse | 37360.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c7a9edf2-b2f5-4f3f-a21d-f91f717f1dd2 |
| seao_quebec:1430258:lgt | LGT | Services professionnels en mécanique et électricité - CPE La Frimousse | 28600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dd9d0991-b7aa-4715-ba4c-23f10743f960 |
| seao_quebec:1496109:abcp-architecture-et-urbanisme-ltee | ABCP ARCHITECTURE ET URBANISME LTÉE | Services professionnels en architecture pour la réfection de la clinique d'hygiène dentaire du Cégep Garneau | 322308.62 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=400ea99b-236d-4ac9-96d2-8edceb6142bf |
| seao_quebec:1496145:pageau-morel-et-associes-inc | PAGEAU MOREL ET ASSOCIÉS INC. | Services professionnels en ingénierie pour la réfection de la clinique d'hygiène dentaire du Cégep Garneau | 247493.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=98f2c7bd-d4ff-476c-95ef-c07192e3a728 |
| seao_quebec:1501946:micro-logic | Micro Logic | Service de support Aruba | 49894.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=22a75758-318e-4b32-9d75-80feae4295cb |
| seao_quebec:1603891:ogilvy-montreal-inc | Ogilvy Montréal Inc. | Image de marque | 92000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8e8ef4d1-6edd-4660-81b3-c4d30e9d04f2 |
| seao_quebec:1604683:iti-inc | ITI INC. | Projet FluidApp au Cégep Garneau | 50470.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6931d221-4f4a-4d5c-a9e3-af4e83e3a861 |
| seao_quebec:1604704:iti-inc | ITI INC. | Licences CITRIX / FluidApp | 35631.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b3111a4f-29da-4f7f-a547-3f2eea9e5511 |
| seao_quebec:1604929:terranova-worldwide-corporation | TERRANOVA WORLDWIDE CORPORATION | Sensibilisation à la sécurité informatique | 26392.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7ac76bf3-e71d-4ae7-9d76-4d1bece2a984 |
| seao_quebec:1651534:agence-creative-les-pretentieux-inc | Agence créative Les Prétentieux inc. | Campagne de marketing numérique de la DFCSAE | 34315.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0fcac7b2-f24a-4126-802e-00f66af9851e |
| seao_quebec:1653576:leclerc-communication-inc | Leclerc communication inc. | Publicité radio | 25000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=76b91a32-c1cc-4983-95a1-f2ba1f87cd89 |
| seao_quebec:1653612:cote-fleury-inc | CÔTÉ FLEURY INC. | Services de serrurerie pour le Cégep Garneau | 80000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d7ee768f-1716-4b43-b30b-75d68e8091b9 |
| seao_quebec:1653617:druide-informatique-inc | DRUIDE INFORMATIQUE INC. | Abonnement à Antidote Web Françcais | 50200.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=09994c62-a7b3-4b05-9120-6763af3d48f1 |
| seao_quebec:1659362:cima-s-e-n-c | CIMA+ S.E.N.C. | Services professionnels en électromécanique | 26550.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=48862026-7efc-48a2-b53a-99892a08ee7f |
| seao_quebec:1660641:abp-location-inc | ABP LOCATION INC. | Location de structures pour les portes ouvertes du Cégep Garneau | 52002.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d60c8d6c-8189-4148-a91c-4669799c47bb |
| seao_quebec:1662588:kone-inc | KONE INC. | Remplacement du contrôleur de l'ascenseur no 1 | 43986.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3d7dddd9-0180-4310-b40f-c205a4236555 |
| seao_quebec:1728297:medical-minogue-inc | MÉDICAL MINOGUE INC. | Acquisition d'un mannequin  aux fins de simulation | 76590.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cf9ebf5b-9e65-485a-bf7a-e32fdfee20b6 |
| seao_quebec:1728318:ptp-peintre-inc | PTP PEINTRE INC. | Travaux de peinture au Cégep Garneau - été 2023 | 39570.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0c578e9f-4413-435d-b144-44f56101e4ee |
| seao_quebec:1728355:le-groupe-gesfor-poirier-pinchin-inc | LE GROUPE GESFOR, POIRIER, PINCHIN INC. | Mise à jour du registre d'amiante | 28000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=76b162c3-06fd-4105-94aa-2e2b5ccff3fb |
| seao_quebec:1728854:panavideo-inc | PANAVIDÉO INC. | Acquisition de caméras | 42904.3 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=432364f8-6322-495a-a181-2356161b3956 |
| seao_quebec:1730817:9265-3427-quebec-inc | 9265-3427 Québec inc. | Cours de conduite préventive et de précision - Printemps 2023 | 68060.82 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9dcf37fb-ced2-4ee4-908e-f1fc5727d2c7 |
| seao_quebec:1822769:solutions-it2go-inc | SOLUTIONS IT2GO INC. | Contrat Ruckus Watchdog - Support commutateurs d'acces Ruckus | 35526.24 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=05e852a5-7c43-4061-a4fc-e9ebdd0b0b8c |
| seao_quebec:1824670:equipements-physika | ÉQUIPEMENTS PHYSIKA | Équipement salles de sport | 100261.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=662a118d-c61f-465d-91ef-bba9a32d4bc1 |
| seao_quebec:1831703:groupe-de-securite-garda-senc | GROUPE DE SÉCURITÉ GARDA SENC | Services de sécurité et de gardiennage au Cégep Garneau | 607867.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=84843bcc-ad48-432a-af5a-21b2ee6820fc |
| seao_quebec:1836374:ptp-peintre-inc | PTP PEINTRE INC. | Contrat de peinture | 45185.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c16e88d3-581a-432f-8ec8-47f6c9559a49 |
| seao_quebec:1836405:c-p-u-design-inc | C.P.U. DESIGN INC. | Logiciel Aruba 3 ans | 27159.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a3ed74f2-a799-4abf-a41e-fcb6e65453cb |
| seao_quebec:1837097:autobus-transco-1988-inc | AUTOBUS TRANSCO (1988) INC. | TRANSPORT NOLISÉ DE PERSONNES | 60375.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b3ff9cfb-d9f7-48d3-b228-c7961c28fdc1 |
| seao_quebec:1837097:autobus-la-quebecoise-inc | AUTOBUS LA QUEBECOISE INC. | TRANSPORT NOLISÉ DE PERSONNES | 9955.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b3ff9cfb-d9f7-48d3-b228-c7961c28fdc1 |
| seao_quebec:1837705:av-tech-inc | AV-TECH INC. | ENTRETIEN DES GÉNÉRATRICES AU CÉGEP GARNEAU | 24195.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6a3325b6-44bc-42bb-83a4-8542fe5e6344 |
| seao_quebec:1839409:solutions-informatiques-inso-inc | SOLUTIONS INFORMATIQUES INSO INC. | Remplacement d'équipe informatique Eaton UPS | 51767.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1a5c1dc3-c5ee-4636-9ff3-ab0d9efe79ea |
| seao_quebec:1839416:louis-fecteau-inc | LOUIS FECTEAU INC. | Travaux de réfection de toiture et autres éléments | 26049.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fb50fd7a-4dec-4c04-871d-43e38431882a |
| seao_quebec:1846246:9111-0767-quebec-inc | 9111-0767 QUÉBEC INC. | Conversion contrôle brûleur Fireye chaudière | 68350.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=87209920-cb58-45b7-955f-0516f6666ee8 |
| seao_quebec:1847163:collecto-services-regroupes-en-education | Collecto Services Regroupés en Éducation | Collecto - Expert Cybersécurité | 74000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6abe433a-feb1-497e-99f8-2ed98ed10e32 |
| seao_quebec:1850813:thermo-energie | Thermo-Énergie | ACHAT CHAUFFE-EAU | 58600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a6bc0b24-d92e-4228-8ebe-5644ab2ff144 |
| seao_quebec:1851129:presence-informatique-inc | PRÉSENCE INFORMATIQUE INC. | Aménagement multimédia de la salle du conseil | 40575.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=22bce06b-285a-4c9c-97c0-2cb1a5ae070f |
| seao_quebec:20000114:pavage-carmichael-inc | Pavage Carmichael inc. | Pavage et Asphaltage | 47144.3 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=31c6d096-fb70-4859-ab63-2236d30380b0 |
| seao_quebec:20022144:la-boite-beet-inc | La Boîte Beet inc. | Refonte et entretien du site Web et du site satellite de la Direction de la formation continue et des services aux entreprises du Cégep Garneau | 95500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=12bd61ba-123d-403a-a0e6-634bf68f681e |
| seao_quebec:20103606:9213-0137-quebec-inc-amiral-agence-web | 9213-0137 Québec inc. (Amiral Agence Web) | Services informatiques | 74360.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=101bf36a-7030-4fa8-8348-c9f5e5fc242d |
| seao_quebec:20106980:cima-s-e-n-c | CIMA+ S.E.N.C. |  Ingénierie (phase 1 aménagement des espaces  extérieurs) | 122800.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1472eba8-36b8-4b85-a47f-b06372cd46fc |
| seao_quebec:20108220:relevance-studio | Relevance Studio | Système de gestion des candidatures (ATS) | 84000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9412ae77-3ffd-4fe5-812d-cc306fd72b5b |
| seao_quebec:20108540:cima-s-e-n-c | Cima + s.e.n.c. | Réaménagement du chauffage à l'eau chaude | 79208.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9afa9e8b-6c26-48ad-9acc-7dd5f7732957 |
| seao_quebec:20108574:bc2-groupe-conseil-inc | BC2 GROUPE CONSEIL INC. | Aménagement des espaces extérieurs | 107950.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=69df0489-812c-4be6-85a0-a3e5614c0b67 |
| seao_quebec:20111520:la-boite-beet-inc | La Boîte Beet inc. | Hébergement et maintenance de systèmes | 29780.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c7ba63ed-fd6a-4c7c-838a-3da70ba3f0ef |
| seao_quebec:20112700:mallette-s-e-n-c-r-l | MALLETTE S.E.N.C.R.L. | Audit externe | 147500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a1d6e9e3-e01c-4705-8483-dc637bb95304 |
| seao_quebec:20115334:laplante-construction-2006-inc | LAPLANTE CONSTRUCTION (2006) INC. | Réfections aux pavillons A, F et G du Cégep Garneau | 2133761.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b0b1a70d-12ca-4570-a1f7-3d49d473f845 |
| seao_quebec:20122330:brigad-architecture-et-design-inc | BRIGAD ARCHITECTURE ET DESIGN INC. | Architecture-réaménagement des espaces extérieurs | 38550.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=44a767ee-94f6-4738-8272-9f6c80c2a533 |
| seao_quebec:20135305:solotech-inc | SOLOTECH INC. | Remplacement d'équipements audiovisuels. | 57616.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4d0318b7-f4a9-427c-a20f-e5de2296176b |
| seao_quebec:20145738:risq | RISQ | Déplacement fibre optique  | 27105.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2e037af9-aa01-4260-ada5-2cb5feb0f532 |
| seao_quebec:20152833:druide-informatique-inc | DRUIDE INFORMATIQUE INC. | Renouvellement licence de site Antidote Pro  | 39096.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f177104a-332e-4f5e-be4e-144671c95922 |
| seao_quebec:20154895:les-services-exp-inc | LES SERVICES EXP INC. | Contrat de services professionnels en ingénierie mécanique et électrique  | 28230.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=62100593-c627-4c46-9278-b273fa653b8e |
| seao_quebec:20156808:cobalt-intelligence-inc | COBALT INTELLIGENCE INC. | Renouvellement plateforme logicielle Cobalt  | 76133.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b38cdeb3-fdf8-4980-bd1c-87fec4849235 |
| seao_quebec:20157347:banque-royale-du-canada | BANQUE ROYALE DU CANADA | Services bancaires | 45000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e4760505-c1ae-4dda-9ad1-f6a80d5d8e52 |
| seao_quebec:20158573:skytech-communications-inc | Skytech communications inc. | Progiciel de gestion intégré | 1693000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a4e0e994-7fe5-47d7-8cf5-d90b4282fa9c |
| seao_quebec:20158742:marie-chantal-dumas | Marie-Chantal Dumas | Accompagnement pour les travaux de planification stratégique | 90000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d98b619b-7fc6-4cc6-9579-f6ffca376c28 |
| seao_quebec:20172422:pluritec-ltee | PLURITEC LTÉE | Services professionnels en ingénierie - remplacement de la surface synthétique et éclairage  | 67495.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=218535b2-61d7-4244-8d30-6a0b24bc7513 |
| seao_quebec:20172931:it2go-solutions-inc | IT2GO Solutions Inc.  | Renouvellement de support Ruckus | 52522.26 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=febb2db5-4c1f-4438-9f78-0b3a2d9d43e7 |
| … 104 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 14)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1108856:les-artisans-du-paysage-du-quebec-inc | Commission scolaire des Découvreurs. | Déneigement Projet Secteur St-Augustin (village) | 26585.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ca38328d-4bcc-4dc6-af89-e091f1ba1f2b |
| seao_quebec:1195893:les-artisans-du-paysage-du-quebec-inc | Directeur Général des Élections du Québec | Services techniques de déneigement au sol | 93816.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f69b9f26-63bf-48c6-a627-eadbf7dc8bd0 |
| seao_quebec:1475535:les-artisans-du-paysage-du-quebec-inc | Institut universitaire de cardiologie et de pneumologie de Québec-Université Laval | Entretien d'amenagement paysager | 165600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=91e70ad1-aa79-4dac-a294-a0a12c6a15b2 |
| seao_quebec:1484678:les-artisans-du-paysage-du-quebec-inc | Réseau de transport de la Capitale. | Entretien paysager de divers Terminus, Parc-O-Bus et installations du RTC | 74452.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e7da742b-c949-48a3-87b7-829cf1bb2459 |
| seao_quebec:1556510:les-artisans-du-paysage-du-quebec-inc | Directeur général des élections du Québec | Services de déneigement au sol | 28282.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0a37750f-208b-40ea-9906-1c55a34aa040 |
| seao_quebec:1579022:les-artisans-du-paysage-du-quebec-inc | Réseau de transport de la Capitale. | Entretien paysager du Centre Lebourgneuf, du Centre Métrobus et de divers Terminus | 263215.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=17a97f2d-5123-4bba-9932-c5b4dd959264 |
| seao_quebec:1776013:les-artisans-du-paysage-du-quebec-inc | SQI-Direction immobilière Sud de Québec | Entretien paysager | 36973.52 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fa4ae5e8-08ba-492a-90b9-a3e2538a754c |
| seao_quebec:20015166:les-artisans-du-paysage-du-quebec-inc | SQI-Direction immobilière Sud de Québec | Déneigement au 700, 7e rue de l’Aéroport, Québec (QC) G2G 2S8 | 206856.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5f7ef5dd-c2bf-48b1-b1ae-4aeec7a28879 |
| seao_quebec:20098629:les-artisans-du-paysage-du-quebec-inc | CEGEP de Ste-Foy |  Entretien des plates-bandes | 97614.33 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fde6d506-8240-49e9-9f12-663ad1de297f |
| seao_quebec:20141940:les-artisans-du-paysage-du-quebec-inc | SQI-Direction immobilière Nord de Québec | Entretien paysager au PJQ | 68289.31 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9a2a540a-17c4-4277-b3da-e720ffdbde49 |
| seao_quebec:20144365:les-artisans-du-paysage-du-quebec-inc | Commission de la construction du Québec.- CCQ | SERVICES D'ENTRETIEN DES ESPACES EXTÉRIEURS | 13384.91 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=73289815-1364-472a-96ba-2212a6542288 |
| seao_quebec:591120:les-artisans-du-paysage-du-quebec-inc | SQI-DI Ouest de Québec et Les-deux-rives | Entretien paysager | 8400.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fb5569f5-f838-4341-b503-b071e974d535 |
| seao_quebec:596587:les-artisans-du-paysage-du-quebec-inc | Directeur Général des Élections du Québec | Déneigement |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=26692076-195b-4416-b617-5c1baf309a47 |
| seao_quebec:902131:les-artisans-du-paysage-du-quebec-inc | Directeur Général des Élections du Québec | Services de déneigement au sol | 77700.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b85575e2-a05f-423a-9ff2-c806f18b632d |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S5-16 — Société de Transport de Trois-Rivières. ⇄ PAGUI INC.

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08) — 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3
SUBMIT TO: info@sttr.qc.ca (general mailbox, confirmed by the referee) | invoice portal: Coupa
REFERENCE: contract 20149684 (ocds_contract_ids); tender 26-03 (numero) | PO rule: not published
FROM / REMIT TO: PAGUI INC. — 15971, boul de la Colline,Québec, Québec, QC, G3G3A7 | GST/HST number not public | NEQ 1141727561
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initi
DESCRIPTION: Installation et mise en service infrastructures de recharge | AMOUNT: 355,703.91 CAD
```

## Relationship
- **rank_group**: A1
- **data_quality_score**: 69
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 203
- **reverify_due**: yes (mailbox evidence older than 60 days)
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Société de Transport de Trois-Rivières. (transport / transit authority, QC) — public contract / purchase award with a published end date (dated record): PAGUI INC. | subject: Installation et mise en service infrastructures de recharge | instrument: contract | contract number: 20149684 (ocds_contract_ids); 26-03 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the | solicitation: 26-03 (numero) | all identifiers: {"numeroseao": "20143713", "numero": "26-03", "ocid": "ocds-ec9k95-20143713", "ocds_contract_ids": ["20149684"], "ocds_award_ids": ["20149684"], "seao_item_id": "e8c59f1f-b37e-4c49-9969-d29877d49d3a"} | value: 355703.91 CAD | awarded 2026-06-18, start 2026-06-18, end 2027-06-18 | published by: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes | record: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e8c59f1f-b37e-4c49-9969-d29877d49d3a | vendor in Canada because: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code) | status rule: active (published end date today or later) | this buyer has 146 records with Canada-located vendors (110 distinct vendors; 3 in the last 12 months; latest 2026-06-18)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:07d464f173baf8ce
- **tier**: A
- **grade**: 1
- **records_with_this_vendor**: 2

## Buyer
- **buyer**: Société de Transport de Trois-Rivières.
- **buyer_website**: https://sttr.qc.ca
- **buyer_address**: 2000 rue Bellefeuille, Trois-Rivières, QC, G9A3Y2, CA
- **buyer_phone**: 819 373-4533
- **buyer_contact_evidence_url**: https://sttr.qc.ca/nous-joindre/
- **buyer_legal_name_as_published**: SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08)
- **buyer_logo_url**: https://sttr.qc.ca/app/themes/Stereo/assets/img/favicon/apple-touch-icon.png
- **buyer_registry_id**: NEQ 8831854664 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: transport / transit authority
- **buyer_sector**: transport / transit
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://sttr.qc.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; AP phone: the lane's AP page (https://sttr.qc.ca/nous-joindre/); invoice mailing address: the lane's AP page (https://sttr.qc.ca/nous-joindre/); invoicing requirements: the lane's AP page (https://sttr.qc.ca/nous-joindre/); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@sttr.qc.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://sttr.qc.ca/nous-joindre/
- **email_evidence_quote**: Siège social ... 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 ... Téléphone : 819 373-4533 ... Courriel : info@sttr.qc.ca
- **email_evidence_context**: rnis demeureront confidentiels. Pour obtenir de l’information concernant les parcours et les horaires, veuillez communiquer avec le service à la clientèle 819 373-4533 . Téléphone : 819 373-4533 Téléphone : 819 373-1778 (Transport adapté) Courriel : info@sttr.qc.ca Choisissez le formulaire qui correspond à vos besoins à l’aide des options suivantes : Adhésion au programme avantages Demande de renseignements Enregistrement de votre carte Cité Félicitations Objet perdu Plainte Rechargement en ligne de la carte C (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@sttr.qc.ca (general) | researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-04-20 | page: https://sttr.qc.ca/nous-joindre/ | quote: "Siège social ... 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 ... Téléphone : 819 373-4533 ... Courriel : info@sttr.qc.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Trend Micro | lane file: gemini/gemini_buyer_ap_results_batch05.csv task GE-AP-00445
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Trend Micro
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; sp=none; adkim=r; aspf=r
- **dmarc_record_domain**: sttr.qc.ca
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 819 373-4533
- **invoice_mailing_address**: 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3
- **invoicing_requirements**: General contact email info@sttr.qc.ca, tel. 819 373-4533; head office at 2000 rue Bellefeuille, C.P. 696, Trois-Rivières, Québec G9A 5J3.
- **payment_terms_as_published**: 45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initiation-vf.pdf, re-read 2026-11-08)
- **invoice_portal_url**: Coupa
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Coupa
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initiation-vf.pdf, re-read 2026-11-08)", "portal_url": "Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "ap_phone": "819 373-4533", "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3", "requirements_text": "General contact email info@sttr.qc.ca, tel. 819 373-4533; head office at 2000 rue Bellefeuille, C.P. 696, Trois-Rivières, Québec G9A 5J3."}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08) — 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3 ⏎ SUBMIT TO: info@sttr.qc.ca (general mailbox, confirmed by the referee) | invoice portal: Coupa ⏎ REFERENCE: contract 20149684 (ocds_contract_ids); tender 26-03 (numero) | PO rule: not published ⏎ FROM / REMIT TO: PAGUI INC. — 15971, boul de la Colline,Québec, Québec, QC, G3G3A7 | GST/HST number not public | NEQ 1141727561 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initi ⏎ DESCRIPTION: Installation et mise en service infrastructures de recharge | AMOUNT: 355,703.91 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08)", "legal_name_is_published": true, "address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@sttr.qc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20149684 (ocds_contract_ids); 26-03 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20149684 (ocds_contract_ids) — source seao_quebec"}, "terms": {"payment_terms": "45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initiation-vf.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVE
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 62
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)
- **invoice_reference_hint**: contract or agreement number: 20149684 (ocds_contract_ids) — source seao_quebec

## Vendor
- **vendor**: PAGUI INC.
- **vendor_legal_name**: PAGUI INC.
- **vendor_registry_id**: Québec REQ (NEQ): 1141727561; 1141727561 (QC)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 15971 boul. de la Colline, Québec (Québec), G3G3A7
- **vendor_neq**: 1141727561 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — QUÉBEC : Loi sur les sociétés par actions (RLRQ, C. S-31.1)
- **vendor_activity_code**: CAE 4261 — ÉLECTRICITÉ | secondary: VENTILATION
- **vendor_employees_quebec**: De 50 à 99
- **vendor_last_annual_filing**: REQ annual declaration 2026
- **vendor_address**: 15971, boul de la Colline,Québec, Québec, QC, G3G3A7
- **vendor_country_basis**: OCDS parties[role=supplier].address.countryName: supplier country field = "CAN" (CAN = Canada per SEAO Annexe A; "CA" accepted as Canada: all such rows carry a Canadian province code and/or postal code)
- **vendor_website**: https://pagui.groupesmtardif.com/
- **vendor_emails**: info@pagui.com; payable@sm-inc.com
- **vendor_phone**: 418 849-1832
- **vendor_contact_evidence_url**: https://pagui.groupesmtardif.com/nous-joindre/
- **vendor_logo_url**: https://pagui.groupesmtardif.com/wp-content/uploads/sites/3/2023/05/pagui-couleurs-rvb.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/sm-construction/
- **vendor_billing_ar_email**: payable@sm-inc.com
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://pagui.groupesmtardif.com/en/contact-us/; https://pagui.groupesmtardif.com/en/contact-us/
- **vendor_facts_provenance**: name and address: the record's vendor block (Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes); registry identity: Québec REQ (NEQ): 1141727561; 1141727561 (QC) status Québec REQ (NEQ): Immatriculée (1994-12-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); incorporated / registered: 1991-01-25; phone / role e-mails / logo: the vendor's own site, https://pagui.groupesmtardif.com/nous-joindre/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://pagui.groupesmtardif.com/en/contact-us/; https://pagui.groupesmtardif.com/en/contact-us/; website: https://pagui.groupesmtardif.com/ (site answers); NEQ: 1141727561 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: Roi Mauricien des Habits: 4% of 146 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (1994-12-08)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1991-01-25
- **vendor_years_in_business**: 35.8 (since 1991-01-25, registry date)

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"numeroseao": "20143713", "numero": "26-03", "ocid": "ocds-ec9k95-20143713", "ocds_contract_ids": ["20149684"], "ocds_award_ids": ["20149684"], "seao_item_id": "e8c59f1f-b37e-4c49-9969-d29877d49d3a"}
- **contract_title**: Installation et mise en service infrastructures de recharge
- **commodity**: 39121700 Matériel électrique et fournitures
- **contract_description**: goods; Approvisionnement (biens)
- **contract_or_agreement_number**: 20149684 (ocds_contract_ids); 26-03 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference
- **solicitation_or_tender_number**: 26-03 (numero)
- **award_or_notice_id**: 20143713 (numeroseao); 20149684 (ocds_award_ids); ocds-ec9k95-20143713 (ocid); e8c59f1f-b37e-4c49-9969-d29877d49d3a (seao_item_id)
- **commodity_codes**: UNSPSC 39121700 (Matériel électrique et fournitures)
- **contract_value**: 355703.91
- **currency**: CAD
- **award_date**: 2026-06-18
- **start_date**: 2026-06-18
- **end_date**: 2027-06-18
- **contract_link**: https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e8c59f1f-b37e-4c49-9969-d29877d49d3a
- **source**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes
- **contracts_with_canadian_suppliers**: 146
- **records_last_12_months**: 3
- **record_sources**: Système électronique d'appel d'offres du Québec (SEAO) - données ouvertes (146)
- **records_with_this_vendor**: 2
- **records_in_contract_dataset**: 146 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Technologies de l'information, radiodiffusion et télécommuni (5); Finances et assurances (5); Services financiers et d'assurance (3)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08) — 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3 ⏎ SUBMIT TO: info@sttr.qc.ca (general mailbox, confirmed by the referee) | invoice portal: Coupa ⏎ REFERENCE: contract 20149684 (ocds_contract_ids); tender 26-03 (numero) | PO rule: not published ⏎ FROM / REMIT TO: PAGUI INC. — 15971, boul de la Colline,Québec, Québec, QC, G3G3A7 | GST/HST number not public | NEQ 1141727561 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: 45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initi ⏎ DESCRIPTION: Installation et mise en service infrastructures de recharge | AMOUNT: 355,703.91 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES (as registered: Registraire des entreprises du Québec (open data), NEQ 8831854664, 2026-11-08)", "legal_name_is_published": true, "address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@sttr.qc.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20149684 (ocds_contract_ids); 26-03 (numero) — the source publishes the award under this tender / notice number and no separate contract number; quote it as the contract reference", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20149684 (ocds_contract_ids) — source seao_quebec"}, "terms": {"payment_terms": "45 jours suivant la réception (as printed on https://sttr.qc.ca/app/uploads/2021/08/sttr-guide-initiation-vf.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVE
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 62
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; invoice format / requirements published; AP phone or AP contact | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **facts_provenance_json**: {"mailbox": ["info@sttr.qc.ca (general)", "researched by the Gemini agent (lane gemini) (page opened and quoted) on 2026-04-20", "page: https://sttr.qc.ca/nous-joindre/", "quote: \"Siège social ... 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 ... Téléphone : 819 373-4533 ... Courriel : info@sttr.qc.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Trend Micro", "lane file: gemini/gemini_buyer_ap_results_batch05.csv task GE-AP-00445"], "buyer_facts": ["address and phone: the buyer's own site, https://sttr.qc.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "AP phone: the lane's AP page (https://sttr.qc.ca/nous-joindre/)", "invoice mailing address: the lane's AP page (https://sttr.qc.ca/nous-joindre/)", "invoicing requirements: the lane's AP page (https://sttr.qc.ca/nous-joindre/)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://sttr.qc.ca/nous-joindre/ | 2026-11-08 | ok |  |  |  | 819 373-4533 |  |  |  |  |  |

## Buyer site facts (org_extras, sttr.qc.ca)
- **status**: ok
- **pages**: 6
- **language**: fr
- **logo_url**: https://sttr.qc.ca/app/themes/Stereo/assets/img/favicon/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: sttr.qc.ca
- **key**: b:07d464f173baf8ce
- **name**: Société de Transport de Trois-Rivières.
- **website**: https://sttr.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Société de transport de Trois-Rivières
- **legal_name_stated_url**: https://sttr.qc.ca/
- **legal_name_stated_quote**: ffrira le transport gratuit le jour du vote, le 5 octobre Trois-Rivières, le 29 septembre 2026 – La Société de transport de Trois-Rivières (STTR) offrira gratuitement ses services de transport urbain et de transport adapté le lundi 5 octo
- **mentions**: {'payment_method': {'text': 'virement Interac * Courriel pour virement Interac * Commentaires additionnels Envoyer Pr', 'url': 'https://sttr.qc.ca/nous-joindre/', 'quote': 'ier choisi Mode de remboursement * Chèque Paiement direct Paiement direct --> Téléphone mobile pour virement Interac * Courriel pour virement Interac * Commentaires additionnels Envoyer Prévoyez un délai de 60 jours minimum pour l’analyse de votre demande. Si'}}
- **linkedin_url**: https://ca.linkedin.com/company/soci%C3%A9t%C3%A9-de-transport-de-trois-rivi%C3%A8res
- **tel_links**: 8193734533; 819-373-4533; 819-373-1778

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec, G9A 5J3", "address_country": "CA", "address_url": "https://sttr.qc.ca/nous-joindre/", "address_method": "pattern", "address_quote": "et de 13h à 16h 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 Demandes médiatiques Les demandes médiatiques sont traitées par la firme Beaudo", "phone": "819 373-4533", "phone_url": "https://sttr.qc.ca/nous-joindre/", "emails": "info@sttr.qc.ca", "emails_url": "https://sttr.qc.ca/nous-joindre/", "domain": "sttr.qc.ca", "key": "b:07d464f173baf8ce", "name": "Société de Transport de Trois-Rivières.", "website": "https://sttr.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Société de Transport de Trois-Rivières. | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Soci%C3%A9t%C3%A9%20de%20Transport%20de%20Trois-Rivi%C3%A8res. | 2026-11-08 |
| buyer | Pagui inc | found | PAGUI INC. |  | 1141727561 | QC | Société par actions ou compagnie | Active | 1991-01-25 | Québec | Québec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Pagui%20inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Société de Transport de Trois-Rivières. | found | SOCIÉTÉ DE TRANSPORT DE TROIS-RIVIÈRES |  | NEQ 8831854664 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 2001-12-11 | Trois-Rivières | QC | 2000 rue Bellefeuille, Trois-Rivières (Québec), G9A3Y2 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |
| buyer | Pagui inc | found | PAGUI INC. |  | NEQ 1141727561 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 1994-12-08 | Québec | QC | 15971 boul. de la Colline, Québec (Québec), G3G3A7 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Société de Transport de Trois-Rivières. |  |  |  |  |  |  |  |  |  |  |
| b | Pagui inc |  |  |  |  |  |  |  |  |  |  |
| v | PAGUI INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:07d464f173baf8ce",
 "ap_contact_team": {
  "emails": [
   "info@sttr.qc.ca"
  ],
  "invoice_portal": null,
  "phone": "819 373-4533",
  "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3",
  "invoicing_requirements": "Bill-to legal name: Société de Transport de Trois-Rivières (STTR). Head office mailing address: 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3. Official general contact mailbox: info@sttr.qc.ca; head office phone: 819 373-4533. Service à la clientèle is located at 246 rue Saint-Roch, Trois-Rivières, Québec G9A 0H4.",
  "evidence": [
   {
    "email": "info@sttr.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://sttr.qc.ca/nous-joindre/",
    "quote": "z communiquer avec le service à la clientèle 819 373-4533 . Téléphone : 819 373-4533 Téléphone : 819 373-1778 (Transport adapté) Courriel : info@sttr.qc.ca Choisissez le formulaire qui correspond à vos besoins à l’aide des options suivantes : Adhésion au programme avantages Demande de rens",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Société de Transport de Trois-Rivières.",
    "task_id": "CL-SQ-00070"
   },
   {
    "email": "info@sttr.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://sttr.qc.ca/nous-joindre/",
    "quote": "z communiquer avec le service à la clientèle 819 373-4533 . Téléphone : 819 373-4533 Téléphone : 819 373-1778 (Transport adapté) Courriel : info@sttr.qc.ca Choisissez le formulaire qui correspond à vos besoins à l’aide des options suivantes : Adhésion au programme avantages Demande de rens",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Société de Transport de Trois-Rivières.",
    "task_id": "CL-WS-00061"
   },
   {
    "email": "info@sttr.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://sttr.qc.ca/app/uploads/2025/04/sttr-guide-transport-adapte-2025-1.pdf",
    "quote": "ue Saint-Roch Trois-Rivières (Québec) G9A 0H4 Téléphone : 819 373-4533 Téléphone transport adapté : 819 373-1778 Télécopieur : 819 373-6158 info@sttr.qc.ca",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Société de Transport de Trois-Rivières.",
    "task_id": "CL-WS-00393"
   },
   {
    "email": "info@sttr.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": "819 373-4533",
    "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3",
    "requirements": "Bill-to legal name: Société de Transport de Trois-Rivières (STTR). Head office mailing address: 2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3. Official general contact mailbox: info@sttr.qc.ca; head office phone: 819 373-4533. Service à la clientèle is located at 246 rue Saint-Roch, Trois-Rivières, Québec G9A 0H4.",
    "applies_to": "all",
    "page_url": "https://sttr.qc.ca/nous-joindre/",
    "quote": "Siège social ... 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 ... Téléphone : 819 373-4533 ... Courriel : info@sttr.qc.ca",
    "retrieved_date": "2026-11-08",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch47.csv",
    "org": "Société de Transport de Trois-Rivières (STTR)",
    "task_id": "GE-AP-47001"
   },
   {
    "email": "info@sttr.qc.ca",
    "type": "general_info",
    "invoice_portal": null,
    "phone": "819 373-4533",
    "mailing_address": "2000 rue Bellefeuille, case postale 696, Trois-Rivières, Québec G9A 5J3",
    "requirements": "General contact email info@sttr.qc.ca, tel. 819 373-4533; head office at 2000 rue Bellefeuille, C.P. 696, Trois-Rivières, Québec G9A 5J3.",
    "applies_to": "all",
    "page_url": "https://sttr.qc.ca/nous-joindre/",
    "quote": "Siège social ... 2000 rue Bellefeuille, case postale 696 Trois-Rivières, Québec G9A 5J3 ... Téléphone : 819 373-4533 ... Courriel : info@sttr.qc.ca",
    "retrieved_date": "2026-04-20",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch05.csv",
    "org": "Société de Transport de Trois-Rivières (STTR)",
    "task_id": "GE-AP-00445"
   }
  ]
 },
 "research_status": {
  "found": 5
 },
 "queries_tried": [
  "site crawl of sttr.qc.ca (35 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "\"sttr.qc.ca\" \"comptes payables\" OR \"facturation\" OR \"finances\" OR \"info@sttr.qc.ca\" OR \"nous joindre\"",
  "\"sttr.qc.ca\" facturation OR comptes payables; \"info@sttr.qc.ca\" OR \"comptabilite@sttr.qc.ca\""
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| seao_quebec:20143713:pagui-inc | seao_quebec | ongoing | Installation et mise en service infrastructures de recharge | 355703.91 | CAD |  |  | {"numeroseao": "20143713", "numero": "26-03", "ocid": "ocds-ec9k95-20143713", "ocds_contract_ids": ["20149684"], "ocds_award_ids": ["20149684"], "seao_item_id": "e8c59f1f-b37e-4c49-9969-d29877d49d3a"} | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e8c59f1f-b37e-4c49-9969-d29877d49d3a |
| seao_quebec:20174716:pagui-inc | seao_quebec | ongoing_inferred | Achat d'un coffret de distribution | 71628.53 | CAD |  |  | {"numeroseao": "20174716", "numero": "202525", "ocid": "ocds-ec9k95-20174716", "ocds_contract_ids": ["20169440"], "ocds_award_ids": ["20169440"], "seao_item_id": "ab70e772-6902-4cf5-ae38-ce5ab7feac0a" | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ab70e772-6902-4cf5-ae38-ce5ab7feac0a |

## The buyer's other Canadian-vendor records (first 60 of 144)
| record_id | vendor | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1016471:lavery-de-billy-sencrl | Lavery de Billy, sencrl | Services professionnels d'un avocat spécialisé dans le domaine des relations de travail | 67978.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=40344492-0957-4601-91b0-21520f90f617 |
| seao_quebec:1040892:roi-mauricien-des-habits | Roi Mauricien des Habits | Uniformes chauffeurs | 86017.4 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=711c697e-4f0a-4a88-88c8-3f37e239c87f |
| seao_quebec:1046714:gnr-corbus-inc | GNR Corbus inc | Remplacement des unités de ventilation, climatisation, chauffage du centre de service de la STTR | 917290.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=595e6d12-991a-4f79-9b4c-26d54ac6af0d |
| seao_quebec:1075535:services-menagers-trifluviens-inc | Services Menagers Trifluviens inc. | Entretien ménager du centre de service de la STTR | 53862.22 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=89ccc0cb-c59f-4f1e-8b45-bdfa5383b5ca |
| seao_quebec:1076890:manufacturier-sheltec-inc | Manufacturier Sheltec Inc | Acquisition et installation d'abribus | 109050.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0ba41827-7ed0-4622-a9ed-01a9efb6f9dc |
| seao_quebec:1134387:groupe-pro-b-inc | Groupe Pro-b inc | Remplacement du lave-autobus du centre de service de la STTR | 588128.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d1401dcd-c4bd-42f3-83ef-f32681281205 |
| seao_quebec:1185899:stereo | Stéréo | création du portail de la Société de Transport de Trois-Rivières | 37720.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e60db74a-db78-4d0a-ad71-34f3dacd207b |
| seao_quebec:1186769:equipements-martel-inc | Équipements Martel inc. | Phase 1 d'implantation d'un terminus sur les terrains de l'UQTR | 121088.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=50f4c96c-85b4-41d6-b4d1-90aa46a8679a |
| seao_quebec:1187046:acolyte-communication-inc | Acolyte communication Inc. | Refonte du site web de la STTR | 28513.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4f214a98-de5c-448f-b662-edf2d47053b0 |
| seao_quebec:1187176:pluritec-ltee | Pluritec Ltée | remplacement lave-autobus services professionnels | 25501.46 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d0d2d229-4573-4625-b46e-72a3e38c1d44 |
| seao_quebec:1187208:manutention-toromont | Manutention Toromont | Remplacement du chariot élévateur | 30670.73 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=180352a9-e9ee-4198-a43a-a2e7d6c025f6 |
| seao_quebec:1187212:auger-automobile | Auger automobile | Acquisition d'un véhicule électrique : Chevrolet volt | 37981.27 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6c5d5e20-4806-4edb-8ee2-38c8255267d2 |
| seao_quebec:1187448:infodev | Infodev | remplacement de compteurs passagers | 80935.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bd21ca17-eb6c-4593-bede-b03e940441c9 |
| seao_quebec:1187457:tennant-sales-and-service-canada | Tennant sales and service Canada | achat d'une balayeuse récureuse autoportée industrielle | 97727.6 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=acea503b-0c99-424b-a8fe-bd811b3f85c4 |
| seao_quebec:1187490:les-enseignes-professionnelles | Les Enseignes professionnelles | Pavillon sanitaire pour terminus des Galeries du Cap | 74129.84 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ae065dac-aeec-48a7-a3a6-ddb696ce60c0 |
| seao_quebec:1187662:les-constructions-jp-dufresne-et-fils | Les constructions JP Dufresne et fils | Mise aux normes de la salle de bain des mécaniciens | 37481.85 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7481101d-22ed-43d5-b419-af619d9c4127 |
| seao_quebec:1187663:coencorp | Coencorp | Acquisition d'un système automatisé de gestion des fluides | 43454.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=36eebffc-b5dc-4247-acb0-2d806e30aa30 |
| seao_quebec:1189091:trois-rivieres-ford-lincoln | Trois-Rivières Ford Lincoln | Acquisition d'un véhicule d'entretien pour le réseau | 72212.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f6173774-ee20-411e-a636-117abd76fa02 |
| seao_quebec:1193446:option-neon | Option néon | achat d'arrêts d'autobus pour le réseau | 83101.1 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e2245d6b-3b74-4c81-b0f9-58ee4d5eaf99 |
| seao_quebec:1193455:exp | EXP | Services professionnels pour réalisation du terminus UQTR phase 1 | 17890.11 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3b198efe-f803-4233-93f0-0e141b16296f |
| seao_quebec:1193481:groupe-desroches | Groupe Desroches | achat d'huiles | 36277.83 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f0da1dd9-b465-41c7-af98-bd9df5613de4 |
| seao_quebec:1193485:nicolet-chrysler-fiat-le-prix-du-gros | Nicolet Chrysler Fiat (le prix du gros) | Achat d'un Chrysler Pacifica hybrid | 53625.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2b9b930a-4b58-48d2-a3b7-faa8806a6d70 |
| seao_quebec:1193506:prevost-une-division-du-groupe-volvo-inc | Prevost une division du groupe Volvo Inc. | achat de supports à vélos | 48588.21 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4ffe9335-cebc-435b-8a53-e5b70e6768f6 |
| seao_quebec:1213175:pluritec | Pluritec | Services professionnels pour terminus UQTR phase 2 | 67202.89 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=34670c72-2b93-4074-acc7-cd157f0ee7b5 |
| seao_quebec:1225544:roi-mauricien-des-habits | Roi Mauricien des Habits | achat d'uniformes pour les chauffeurs (es) | 49282.88 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5d791d36-ae80-42ad-a38e-904e1006ccec |
| seao_quebec:1270781:toitures-des-2-rives | Toitures Des 2 Rives | Réfection de la toiture au 2000, rue Bellefeuille | 935752.78 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=18d74d20-ccb6-4248-8b56-6d1ae3e3bbc0 |
| seao_quebec:1309817:recochem-inc | Recochem inc | Fourniture de Fluide d’Échappement Diesel DEF-URÉE  (Achat regroupé) |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=81c9d779-f65e-420d-a96f-c6f055394333 |
| seao_quebec:1323316:solotech-inc | Solotech Inc. | achat d'afficheurs numériques dynamiques | 402297.53 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=268ba86f-d6c9-4b74-99ec-81a40988490f |
| seao_quebec:1324403:manufacturier-sheltec-inc | Manufacturier Sheltec Inc | Achat d'abribus | 128657.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4baa88e3-4abc-4e69-bfe7-effb58e9c0cd |
| seao_quebec:1354497:interconnexions-ld | Interconnexions LD | Mise à jour du système téléphonique | 22925.39 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=03af7601-955e-4d13-9150-ea9ba84359dc |
| seao_quebec:1354505:auger-automobiles | Auger automobiles | achat de deux Bolt 2019 | 89156.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=055310e1-d819-46c5-9351-265c3f5220d7 |
| seao_quebec:1354512:les-industries-harnois | les industries Harnois | achat d'un dôme | 58510.78 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d723cefc-bdcb-4dd9-97a8-c758ee29db43 |
| seao_quebec:1378415:roi-mauricien-des-habits | Roi Mauricien des Habits | Achat de manteaux d'hiver pour les chauffeurs | 37711.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=efd6191f-4264-49a9-9949-1f7da5e2d350 |
| seao_quebec:1378424:roi-mauricien-des-habits | Roi Mauricien des Habits | Achat de vêtements pour chauffeurs | 52060.68 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5d5fe05e-186f-451d-a9f6-a7e35183947e |
| seao_quebec:1378429:androide | Androïde | Achat de matériels pour serveur | 36145.67 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=789c5258-8d92-402e-a5c0-9a9f24f34778 |
| seao_quebec:1378438:groupe-clr | Groupe CLR | Achat de radios pour autobus | 66792.43 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=186f2ff7-db52-49c9-be8b-b370cba8258a |
| seao_quebec:1379060:les-huiles-desroches-inc | Les huiles Desroches Inc. | Achat d'huiles | 27197.34 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=de94457f-000e-48d1-8a89-cf3e1c6a5e10 |
| seao_quebec:1415335:alarme-alliance | Alarme Alliance | Gestion des accès du bâtiment et gestion de caméras | 55773.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a46d690f-32ce-48b3-83c2-b25319b02a9e |
| seao_quebec:1415435:lessard-buick-chevrolet | Lessard Buick Chevrolet | Achat de deux Bolt 2020 | 78029.56 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c3492e03-e830-4f5a-8cc9-cc6fa4ebcd6c |
| seao_quebec:1425132:new-flyer-industries-canada | New Flyer Industries Canada | Achat regroupé pour l'acquisition de pièces de transmissions et différentiels pour autobus urbains | 190912.23 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c085ca8f-c343-48c2-bdb1-9ca0488fc5df |
| seao_quebec:1425132:solutions-serafin-inc | SOLUTIONS SERAFIN INC | Achat regroupé pour l'acquisition de pièces de transmissions et différentiels pour autobus urbains | 2600841.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c085ca8f-c343-48c2-bdb1-9ca0488fc5df |
| seao_quebec:1425132:cbm-n-a | CBM N.A. | Achat regroupé pour l'acquisition de pièces de transmissions et différentiels pour autobus urbains | 3216040.63 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c085ca8f-c343-48c2-bdb1-9ca0488fc5df |
| seao_quebec:1425132:prevost-une-division-du-groupe-volvo-canada-inc | Prévost, une division du Groupe Volvo Canada Inc. | Achat regroupé pour l'acquisition de pièces de transmissions et différentiels pour autobus urbains | 990192.51 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c085ca8f-c343-48c2-bdb1-9ca0488fc5df |
| seao_quebec:1428989:norda-stelo-inc-siege-social | Norda Stelo Inc. (siège social) | Mise à jour du logiciel et maintenance | 44882.79 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ec6fa210-0823-4d3d-8483-a0acdaf62981 |
| seao_quebec:1482098:lemieux-ryan-et-associes | Lemieux, Ryan et associés | Portefeuille d'assurances dommage 2017-2018 | 140732.58 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=78600ad6-6ffe-4cd4-bfea-b427ae4c479b |
| seao_quebec:1482123:isr-transit | ISR transit | entretien logiciel annuel et entretien équipement SIV annuel | 29530.46 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=02b3999f-a5ad-43c8-bea9-47808a7d722c |
| seao_quebec:1482137:roi-mauricien-des-habits | Roi Mauricien des Habits | Achat de vêtements pour chauffeurs | 70438.86 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1480b77a-a0c0-4764-919b-3502e9c5d013 |
| seao_quebec:1515634:reynolds-communications-inc | REYNOLDS COMMUNICATIONS INC. | Acquisition d’appareils cellulaires et de forfaits cellulaires corporatifs | 39436.93 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=156e0292-7e48-4b05-a735-8c1f9d92c881 |
| seao_quebec:1589904:9066-9060-quebec-inc | 9066-9060 QUÉBEC INC. | Pavillon sanitaire pour terminus du Carrefour Trois-Rivières-Ouest | 119854.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f3f68989-4a32-4a35-9796-7dc1f69041c3 |
| seao_quebec:1608926:stereo-station-design-web-inc | STÉRÉO STATION DESIGN & WEB INC. | refonte de l'intranet |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3d29d05b-3066-47b4-bc8c-360771f9ffec |
| seao_quebec:1608931:9200-7210-quebec-inc | 9200-7210 QUÉBEC INC. | Remplacement d'aérothermes | 41120.21 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=05847654-ce5e-4056-9e3c-14d4ada4fc4c |
| seao_quebec:1625585:martel-yan | MARTEL, YAN | Entretien ménager de divers bâtiments | 265900.15 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5e9a65ca-6dbd-49c2-b3ad-073a0b0c026f |
| seao_quebec:1642258:giro-inc-le-groupe-en-informatique-et-recherche-operationnel | GIRO INC./LE GROUPE EN INFORMATIQUE ET RECHERCHE OPERATIONNELLE | Acquisition de modules d'un outil d'aide à la planification du réseau | 1297115.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=80f61714-500c-4b45-9e41-dc601232991c |
| seao_quebec:1716992:a-girardin-inc | A. GIRARDIN INC. | Acquisition de Minibus pour le transport adapté et le transport urbain pour diverses sociétés de transport du Québec | 900000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b25cbe05-c29e-446c-b552-a5c2896616ea |
| seao_quebec:1717752:city-view-bus-truck-repair-sales-ltd | CITY VIEW BUS & TRUCK REPAIR & SALES LTD. | Achat regroupé pour l'acquisition de batteries Lithium-Ion haute tension pour autobus urbains (ATUQ) | 345955.66 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7b1537de-13a2-426a-9f26-efc61c3ed9da |
| seao_quebec:1725254:aon-canada-inc | AON CANADA INC. | portefeuille d'assurances de dommages | 236079.37 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0d5dd807-2791-427b-946b-3ee8c3ccc2fa |
| seao_quebec:1725341:association-du-transport-urbain-du-quebec | Association du transport urbain du Québec | Cotisation annuelle ATUQ | 77145.04 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=357bffa8-7261-4a96-b79f-b4f00cae90ad |
| seao_quebec:1727920:societe-immobiliere-g3r-inc | SOCIÉTÉ IMMOBILIÈRE G3R INC. | Bail commercial | 539225.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ca0653c2-d3ad-4ae9-b6a2-3730ea23a5d0 |
| seao_quebec:1727947:taxis-coop-de-la-mauricie-1992 | TAXIS COOP DE LA MAURICIE 1992 | service de taxi collectif "taxibus" | 89427.67 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=20f3c9f7-50dc-4491-8209-6d5dad59cabb |
| seao_quebec:1728021:raymond-chabot-grant-thornton-cie-s-e-n-c-r-l | Raymond Chabot Grant Thornton & Cie S.E.N.C.R.L. | Accompagnement pour appel d'offres d'assurances de dommages | 28240.81 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=530e404a-4d5c-4e0c-b971-4fbfa83604f2 |
| … 84 more rows in the .json | ||||||

## The vendor's other buyers in the dataset (first 60 of 71)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| canada_federal:pwgsc-tpsgc:EF99450122 | Public Services and Procurement Canada | Other engineering works | 1696327.14 |  |  | https://search.open.canada.ca/contracts/record/pwgsc-tpsgc,C-2025-2026-Q4-02070 |
| canada_federal:pwgsc-tpsgc:CW2452687 | Public Services and Procurement Canada | Other engineering works | 544481.36 |  |  | https://search.open.canada.ca/contracts/record/pwgsc-tpsgc,C-2026-2027-Q1-02304 |
| canada_federal:cb:CW2452686 | Department of Public Works and Government Services (PSPC) | Installation of a second high-temperature recovery heat pump  at Laurentian Forestry Centre (LFC) in Québec | 544481.36 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2452686 |
| seao_quebec:1038593:pagui-inc | Ville de Québec | Acquisition de commutateur industriel | 539559.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b526bf92-f7c6-4ef5-8a81-51fa565d9e59 |
| seao_quebec:1066004:pagui-inc | Ville de Québec | Contrat de service - Pièces et main-d'oeuvre pour les systèmes d'alimentation sans coupure | 53700.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c052d942-18c0-4b0c-82c6-dea062746f8c |
| seao_quebec:1079259:pagui-inc | Commission scolaire des Navigateurs | Services d'entrepreneurs en électricité | 947184.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a4bb6f54-2123-456f-8fc8-672884c03f78 |
| seao_quebec:1092003:pagui-inc | Commission scolaire des Découvreurs. | Travaux de plomberie école Fernand-Séguin | 31000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f7ed8899-4507-4d0e-909c-da3cadd71162 |
| seao_quebec:1105732:pagui-inc | Service de l'amélioration des infrastructures | Fourniture et installation de câblage structuré - Centre des visiteurs | 371575.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9a5543d9-4ece-49e8-b473-9d5aea774a2d |
| seao_quebec:1256343:pagui-inc | Ville de Baie-Saint-Paul. | AMÉNAGEMENT DE L’INTERSECTION DES RUES FORGET ET RENÉ-RICHARD (FEUX DE CIRCULATION ET TROTTOIRS) | 129893.01 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2eb6c5db-f70f-4a10-9a05-5cf8262dbda8 |
| seao_quebec:1399440:pagui-inc | Commission scolaire des Découvreurs. | Remplacement d'un serpentin à l'eau chaude - Piscine Sylvie-Bernier. | 46850.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1dab295b-c508-4a66-b5ea-eb72020e5e64 |
| seao_quebec:1405409:pagui-inc | Commission scolaire des Découvreurs. | Travaux de plomberie à l'entrée d'eau principale de la Polyvalente de L'Ancienne-Lorette | 27600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e37f810d-d2d2-44da-9600-3a7c0dbc4492 |
| seao_quebec:1626136:pagui-inc | Société de Transport de l'Outaouais. | FOURNITURE ET INSTALLATION D'ÉQUIPEMENT DE RECHARGE POUR TROIS (3) AUTOBUS ÉLECTRIQUES (CAAG) | 365554.64 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4f95e1eb-abfc-4669-9dc4-5b5190998325 |
| seao_quebec:1644082:pagui-inc | Assemblée nationale-Direction des ressources financières, de l'approvisionnement et de la vérification | Remplacement du réservoir de diesel de l'édifice Jean-Antoine Panet | 92660.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4f8aae01-fbfb-4838-bad8-fe84d7853ea0 |
| seao_quebec:1766868:pagui-inc | Ville de Québec | Contrat de service pièces et main-d'¿uvre - Systèmes d'alimentation sans coupure | 97558.07 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8b392877-5439-4532-a89b-52b5cc469484 |
| seao_quebec:1781686:pagui-inc | Institut de technologie agroalimentaire du Québec | Travaux de câblage et fibres optiques | 63950.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=477489a7-1539-49df-a030-90aecc9b1635 |
| seao_quebec:20024194:pagui-inc | Ville de Québec | Infrastructure de câblage à l’intérieur des bâtiments | 1502281.17 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=638d9cc5-60e9-45c8-b611-330b93ac6cee |
| seao_quebec:20086595:pagui-inc | Réseau de transport de la Capitale. | Éclairage remises Lebourgneuf | 24200.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e072f114-2e55-4eee-9ba9-83e4928ce555 |
| seao_quebec:20095014:pagui-inc | Société de transport de Lévis | Travaux d'électrification d'un abribus - Taniata | 31215.71 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f5c2b0ef-ceb4-4ad5-bae7-fd03d6fa8955 |
| seao_quebec:20122916:pagui-inc | Centre de services scolaire des Premières Seigneuries | Remplacement de l'entrée électrique / École du Boisé 2 | 173995.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e5d667b8-d8e9-4eae-9192-e5dc1e76b69a |
| seao_quebec:20124253:pagui-inc | Université Laval | CHM-30140 - Remplacement du transformateur 25 kV | 1062455.14 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ef3df894-2ce5-4c35-ab54-fb19eb1012a5 |
| seao_quebec:20133005:pagui-inc | Centre de services scolaire des Premières Seigneuries | Refaire l'entrée électrique / École de la Place-de-l'Éveil | 329494.57 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1b279b53-c856-4f89-9d69-c52e83fb02e7 |
| seao_quebec:20140308:pagui-inc | Ville de Québec | Câblage extérieur interbâtiments | 3814135.81 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9c76ee8a-5314-4f5f-833c-57dcd6839ac9 |
| seao_quebec:20150372:pagui-inc | Santé Québec Capitale-Nationale – Universitaire | Remplacement des disjoncteurs génératrices hôpital BSP | 277775.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5d91ddf1-5c99-443a-8ee7-7e137fabe59b |
| seao_quebec:20150465:pagui-inc | Université Laval | Remplacement de conduite d’eau  | 38486.12 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e03451f7-357f-40ba-a144-38a87c2af4fe |
| seao_quebec:20152304:pagui-inc | Université Laval | Contrat à exécution sur demande visant l’entretien, la réparation et l’exécution de certains travaux en électricité | 1605002.07 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d768c2a4-feaf-4fc5-af6f-a3436bca42e6 |
| seao_quebec:20174443:pagui-inc | Université Laval | Changement de soupapes dans les salles mécaniques  | 97682.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3d7786d8-2cf1-4f2e-9531-bffe125484ac |
| seao_quebec:271119:pagui-inc | CIUSSS de la Capitale-Nationale-IRDPQ | Installation d'un nouveau refroidisseur | 205523.81 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cf669252-0a26-4ff2-907b-fa96fc7456f5 |
| seao_quebec:271878:pagui-inc | Université Laval | Climatisation de 12 bureaux(1740 à 1762) Pavillon Afdrien-Pouliot | 58471.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1a483b63-2900-46ab-acee-e556ad0bf8ad |
| seao_quebec:273430:pagui-inc | Cégep Limoilou | Refroidissement salle des serveurs local 3427 | 73798.45 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5b70e123-cd27-4d44-b579-2575173d6355 |
| seao_quebec:282563:pagui-inc | CIUSSS de la Capitale-Nationale. | Câblage réseau intégré CLSC de-la-Jacques-Cartier | 44500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=dff63cdd-99d9-4501-a5e6-e970760ee3fb |
| seao_quebec:300027:pagui-inc | Commission Scolaire des Premières Seigneuries | Efficacité énergétique au Centre de formation en transport de Charlesbourg (chauffage) | 227700.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=00f85fb4-c6a4-467e-915b-c4ca58a2fc1f |
| seao_quebec:305473:pagui-inc | Commission scolaire de la Capitale. | Modernisation du chauffage, des chauffe-eau et contrôle centralisé - école primaire Anne-Hébert | 552400.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=47337454-01ae-4d50-a243-0e940d96dc6b |
| seao_quebec:306329:pagui-inc | SQI-Direction immobilière Sud de Québec | Remplacement des panneaux électriques | 29300.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=77ab9f26-3ce2-4f99-9d74-8cff7125edbe |
| seao_quebec:348573:pagui-inc | Commission Scolaire des Premières Seigneuries | Installer un humidificateur - systèmes 1-AR et 44-AR | 82000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fd3b34ca-9410-42b5-9643-9c9bf8e40a0b |
| seao_quebec:353444:pagui-inc | Université Laval | CERSO - Remplacement de compresseurs d'air et ajout de refroidisseur écoénergétique | 2639099.83 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=718e3931-2f38-448b-9742-333ab7429225 |
| seao_quebec:382991:pagui-inc | Centre de services partagés du Québec- Direction générale des acquisitions (DGACQ) | Services de câblage informatique de catégories 5, 5e, 6, 6a, 7 et fibre optique de réseaux locaux et de téléphonie. |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cd90bba7-64f3-4750-8579-8e5d7f44caf0 |
| seao_quebec:389647:pagui-inc | SQI-Direction immobilière Sud de Québec | Mise aux normes de la ventilation | 63850.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=cd35d7c3-e2c8-4409-a55b-327985647e0e |
| seao_quebec:423704:pagui-inc | Université Laval | Université Laval - Stade de Soccer - Alimentation de vapeur | 140750.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5c7dfec3-389b-4fb2-8692-9402ccc8ed5f |
| seao_quebec:451850:pagui-inc | Commission scolaire de la Capitale. | Divers travaux d'électricité (phase 2) - EMOICQ (pavillon des Tanneurs) | 71900.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=61f0d2c4-d2e3-4f7b-959c-12f8f754a148 |
| seao_quebec:453984:pagui-inc | Commission scolaire de la Capitale. | Divers travaux d'électricité (phase 1) - EMOICQ (pavillon des Tanneurs) | 73219.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=39ed7f2e-f5d9-4fae-b551-f395e0459f20 |
| seao_quebec:475076:pagui-inc | Université Laval | Université Laval - Forêt Montmorency - Remplacement des chauffe-eau des résidences | 49349.28 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2c2556f2-cd0d-4b57-a3d3-b45bf62cdf21 |
| seao_quebec:493398:pagui-inc | Université Laval | Fourniture et installation de cabinets et de barres d’alimentation | 177202.22 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=17ca6bdb-14cd-4e28-a0a8-58158d0ca9fd |
| seao_quebec:497978:pagui-inc | Commission scolaire de la Capitale. | Ajout d'un accumulateur thermique et optimisation des contrôles - école De Château-d'Eau | 214000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d3b63674-ab46-4db6-a1ad-6d6b6c649565 |
| seao_quebec:499807:pagui-inc | Commission Scolaire des Premières Seigneuries | Mise à jour des systèmes CVCA - école de l'Île d'Orléans (St-Pierre) | 91100.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9f400953-cf86-4943-8c88-bfc94701a315 |
| seao_quebec:499820:pagui-inc | Commission Scolaire des Premières Seigneuries | Mise à jour des systèmes CVCA - école du Parc-Orléans | 162000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c96a3f74-44d4-4aee-90a0-6c0e2bc86ead |
| seao_quebec:505366:pagui-inc | SQI-Direction des contrats | Lot 352.3 - Plomberie, phases 4 à 13 - Travaux de rénov., d'agrandissement et d'aménagement - Atrium - 5700, 4e Avenue Ouest, Québec | 795860.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=96d6d4d3-38d8-4099-b531-4e90b6d7a86d |
| seao_quebec:512628:pagui-inc | Société de l'assurance automobile du Québec . | Réception et installation d’un refroidisseur centrifuge de 400 tonnes au siège social de la SAAQ | 129735.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5b18dd71-b66b-4741-861e-591748cd480e |
| seao_quebec:520997:pagui-inc | Musée de la civilisation | Réfection d'entrée d'eau et d'égout combiné au MAF | 69750.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c3f00d51-cc9e-429b-84c1-9a66acd12b72 |
| seao_quebec:525789:pagui-inc | Ville de Québec | Services techniques - Câblage extérieur interbâtiment - Réseaux informatiques et téléphoniques | 581701.05 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=11380e7f-261e-45b8-9b11-1073e388c295 |
| seao_quebec:529686:pagui-inc | CEGEP de Ste-Foy | Remplacement d’une unité de ventilation de toit | 93000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=434c196a-0d7a-4eb5-90e5-aece2139f0d1 |
| seao_quebec:537467:pagui-inc | Université Laval | Université Laval - pavillon Adrien-Pouliot - Aménagement d'une salle à température et humidité contrôlées - local 0950C | 34000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=83ce77fd-f3d9-4c07-b848-90815d1b82be |
| seao_quebec:542757:pagui-inc | SQI-Direction des contrats | Remplacement du drainage - lot 352.5 - Travaux de rénovation, d'agrandissement et d'aménagement - 5700 - 4e Avenue Ouest, Québec | 187650.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9fd7bd9e-4c44-4afc-9181-2cbef46942e6 |
| seao_quebec:548176:pagui-inc | Commission Scolaire des Premières Seigneuries | Remise à niveau des systèmes CVCA - école Chabot | 215800.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d0607868-535e-4fda-8b39-846e5fd385e4 |
| seao_quebec:550472:pagui-inc | Université Laval | Université Laval - Tunnel de services - Réfection des supports et de la tuyauterie d'eau refroidie | 64510.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b907895f-8d42-4011-a6f2-9f57f77431e3 |
| seao_quebec:552567:pagui-inc | SQI-Direction des contrats | Ajout d'un refroidisseur de récupération - 300, boul. Jean-Lesage, Québec | 489720.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b29e364a-1a5b-4649-8cb1-e0568be210cb |
| seao_quebec:558332:pagui-inc | Commission Scolaire des Premières Seigneuries | Raccord de la climatisation sur la géothermie - école Le Sommet | 29875.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e33e7103-1c39-495f-a55a-37b9e1ec635f |
| seao_quebec:560308:pagui-inc | SQI-Direction immobilière Nord de Québec | Travaux réparation - système géothermique | 43510.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e70a6dd4-1770-44db-a87e-77fc5c9e2b7c |
| seao_quebec:566726:pagui-inc | Assemblée nationale-Direction des ressources financières, de l'approvisionnement et de la vérification | Pose de câblage intégré | 36750.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1e2ee5d0-e016-45b8-a1b3-ec811cee66c8 |
| seao_quebec:567518:pagui-inc | CEGEP de Ste-Foy | Ventilation - Remplacement des unités de toit | 313499.99 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4c723040-96c7-4c2c-9322-a3e84838ba4b |
| seao_quebec:569598:pagui-inc | Ville de Québec | Projet de câblage général 2012-2014 - Travaux de câblage d'infrastructures réseaux dans divers bâtiments pour la Ville de Québec | 410117.32 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c6744738-78a7-4064-95ac-6773321d91e8 |
| … 11 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

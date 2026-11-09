# S2-50 — Collège Stanislas ⇄ Solutions inLibro inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Collège Stanislas — 780 Dollard Outremont, Québec, H2V 3G5
SUBMIT TO: comptes.clients@stanislas.qc.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: SOLUTIONS INLIBRO INC. — 305-7236 rue Waverly,, Montréal, QC, H2R0C2, CAN | GST/HST 854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1163682637
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Collège Stanislas (university / college, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer s
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 70
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Collège Stanislas (university / college, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Solutions inLibro inc. | published by: the Canada-located vendor's own website | record: https://inlibro.com/en/our-clients/ | vendor in Canada because: vendor located in Canada (osm)=inlibro.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:7b2bb9599ef487dc
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Collège Stanislas
- **buyer_website**: http://www.stanislas.qc.ca
- **buyer_address**: 780 Dollard Outremont, Québec, H2V 3G5
- **buyer_phone**: 514 273-9521 (tel: link on https://stanislas.qc.ca/)
- **buyer_contact_evidence_url**: https://stanislas.qc.ca/nous-joindre-2/
- **buyer_legal_name_as_published**: Collège Stanislas
- **buyer_logo_url**: https://stanislas.qc.ca/wp-content/uploads/2021/07/logo_2025.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/college-stanislas/
- **buyer_registry_id**: NEQ 1142238600 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_municipal_tier**: local municipality (MAMH répertoire) (provincial municipal directory: https://www.donneesquebec.ca/recherche/dataset/2d3b5cf8-b347-49c7-ad3b-bd6a9c15e443/resource/13aa95e2-22a3-4f20-878a-47dbf3480338/download/es_collegial.csv, 2026-11-08)
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2983700; secondary school; collège; primary school; private school
- **buyer_founded**: 1938-01-01 (Wikidata Q2983700, official website on the organisation's domain (http://www.stanislas.qc.ca) + name; 2026-11-08)
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 1142238600, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://stanislas.qc.ca/nous-joindre-2/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptes.clients@stanislas.qc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://stanislas.qc.ca/nous-joindre-2/
- **email_evidence_quote**: slas.qc.ca 418 527-9998 poste 3223 Services financiers Frais de scolarité et facturation Facturation et recouvrement des frais de scolarité comptes.clients@stanislas.qc.ca Contact des fournisseurs
- **email_evidence_context**: poste 2361 Infirmerie – Campus de Québec Anthony Murphy, Responsable du SVE et infirmerie anthony.murphy@stanislas.qc.ca 418 527-9998 poste 3223 Services financiers Frais de scolarité et facturation Facturation et recouvrement des frais de scolarité comptes.clients@stanislas.qc.ca Contact des fournisseurs comptes.fournisseurs@stanislas.qc.ca Vie étudiante Service de vie étudiante – Campus de Montréal Véronique Bougeard, Adjointe administrative du service à la vie étudiante veronique.bougeard@stanislas.qc.ca 514 273-9521 poste (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptes.clients@stanislas.qc.ca (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://stanislas.qc.ca/nous-joindre-2/ | quote: "slas.qc.ca 418 527-9998 poste 3223 Services financiers Frais de scolarité et facturation Facturation et recouvrement des frais de scolarité comptes.clients@stan" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23134
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:ee6c428b50b54ab8b8604eb0915dd4ab@dmarc-reports.cloudflare.net;
- **dmarc_record_domain**: stanislas.qc.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:64.187.185.214 ip4:184.94.119.12 include:spf.protection.outlook.com include:amazonses.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 418 527-9998 poste 3223 (as printed on https://stanislas.qc.ca/nous-joindre-2/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "418 527-9998 poste 3223 (as printed on https://stanislas.qc.ca/nous-joindre-2/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Collège Stanislas — 780 Dollard Outremont, Québec, H2V 3G5 ⏎ SUBMIT TO: comptes.clients@stanislas.qc.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SOLUTIONS INLIBRO INC. — 305-7236 rue Waverly,, Montréal, QC, H2R0C2, CAN | GST/HST 854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1163682637 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Collège Stanislas (university / college, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer s
- **invoice_card_json**: {"bill_to": {"legal_name": "Collège Stanislas", "legal_name_is_published": true, "address": "780 Dollard Outremont, Québec, H2V 3G5", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptes.clients@stanislas.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "854084761RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "SOLUTIONS INLIBRO INC.", "bn9": "854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-759
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)

## Vendor
- **vendor**: Solutions inLibro inc.
- **vendor_legal_name**: SOLUTIONS INLIBRO INC.
- **vendor_registry_id**: Québec REQ (NEQ): 1163682637; 1163682637 (QC)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 305-7236 RUE Waverly, Montréal (Québec), H2R0C2
- **vendor_neq**: 1163682637 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — QUÉBEC : Loi sur les sociétés par actions (RLRQ, C. S-31.1)
- **vendor_activity_code**: CAE 7721 — Consultation et développement informatique pour les technologies documentaires (bibliothèques, GED) et pour la gestion d'infrastructure informatique | secondary: -
- **vendor_employees_quebec**: De 6 à 10
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 305-7236 rue Waverly,, Montréal, QC, H2R0C2, CAN
- **vendor_country_basis**: vendor located in Canada (osm)=inlibro.com
- **vendor_bn9**: 854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 854084761RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://inlibro.com
- **vendor_phone**: 888-604-2627
- **vendor_contact_evidence_url**: https://inlibro.com/
- **vendor_logo_url**: https://inlibro.com/wp-content/uploads/2017/09/inLibro.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Québec REQ (NEQ): 1163682637; 1163682637 (QC) status Québec REQ (NEQ): Immatriculée (2006-04-27) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2006-04-13; phone / role e-mails / logo: the vendor's own site, https://inlibro.com/ (tools/org_contacts.py, org_extras.py); website: https://inlibro.com (site answers); NEQ: 1163682637 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2006-04-27)
- **vendor_incorporation_date**: 2006-04-13
- **vendor_years_in_business**: 20.6 (since 2006-04-13, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://inlibro.com/en/our-clients/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 854084761RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Collège Stanislas — 780 Dollard Outremont, Québec, H2V 3G5 ⏎ SUBMIT TO: comptes.clients@stanislas.qc.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: SOLUTIONS INLIBRO INC. — 305-7236 rue Waverly,, Montréal, QC, H2R0C2, CAN | GST/HST 854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1163682637 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Collège Stanislas (university / college, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer s
- **invoice_card_json**: {"bill_to": {"legal_name": "Collège Stanislas", "legal_name_is_published": true, "address": "780 Dollard Outremont, Québec, H2V 3G5", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptes.clients@stanislas.qc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "854084761RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "SOLUTIONS INLIBRO INC.", "bn9": "854084761 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-11-06; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-759
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["comptes.clients@stanislas.qc.ca (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://stanislas.qc.ca/nous-joindre-2/", "quote: \"slas.qc.ca 418 527-9998 poste 3223 Services financiers Frais de scolarité et facturation Facturation et recouvrement des frais de scolarité comptes.clients@stan\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23134"], "buyer_facts": ["address and phone: the buyer's own site, https://stanislas.qc.ca/nous-joindre-2/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Québec REQ (NEQ): 1163682637", "1163682637 (QC) status Québec REQ (NEQ): Immatriculée (2006-04-27) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & cont

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://stanislas.qc.ca/nous-joindre-2/ | 2026-11-08 | ok |  |  |  | 418 527-9998 poste 3223 |  |  |  |  |  |

## Buyer site facts (org_extras, stanislas.qc.ca)
- **status**: ok
- **pages**: 4
- **language**: fr
- **legal_name**: Collège Stanislas
- **legal_name_url**: https://stanislas.qc.ca/
- **legal_name_quote**: École privée à Montréal et Québec - Collège Stanislas Actualités Événements Carrières à Stan Recrutement AEFE TCF, centre d’examen agréé Nous joindre Fon
- **logo_url**: https://stanislas.qc.ca/wp-content/uploads/2021/07/logo_2025.png
- **logo_basis**: logo image in the site header
- **domain**: stanislas.qc.ca
- **key**: lead:7b2bb9599ef487dc
- **name**: Collège Stanislas
- **website**: https://stanislas.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Test de Connaissance du Français
- **legal_name_stated_url**: https://stanislas.qc.ca/nous-joindre-2/
- **legal_name_stated_quote**: bec Anthony Murphy, Service de vie étudiante anthony.murphy@stanislas.qc.ca 418-527-9998 poste 3223 Test de Connaissance du Français (TCF) Campus Québec tcfquebec@stanislas.qc.ca 418-527-9998 poste 3239 Campus Montréal tcfmontreal@s
- **linkedin_url**: https://www.linkedin.com/school/college-stanislas/
- **tel_links**: 514 273-9521; 418 527-9998

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "780 Dollard Outremont, Québec, H2V 3G5", "address_country": "CA", "address_url": "https://stanislas.qc.ca/nous-joindre-2/", "address_method": "pattern", "address_quote": "us Montréal tcfmontreal@stanislas.qc.ca Montréal 780 Dollard Outremont, Québec, H2V 3G5 514 273-9521 Québec 1605 Chemin Ste Foy Québec, Québec G1S 2P1 418 527-9998 © C", "emails": "communications@stanislas.qc.ca; direction@stanislas.qc.ca; support-tic@stanislas.qc.ca", "emails_url": "https://stanislas.qc.ca/nous-joindre-2/", "domain": "stanislas.qc.ca", "key": "lead:7b2bb9599ef487dc", "name": "stanislas.qc.ca", "website": "https://stanislas.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, inlibro.com)
- **status**: ok
- **pages**: 2
- **language**: fr
- **logo_url**: https://inlibro.com/wp-content/uploads/2017/09/inLibro.png
- **logo_basis**: logo image in the site header
- **domain**: inlibro.com
- **key**: vendor:Solutions inLibro inc.
- **name**: Solutions inLibro inc.
- **website**: https://inlibro.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Solutions inLibro inc.
- **jsonld_url**: https://inlibro.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https:\/\/inlibro.com\/#breadcrumblist","itemListElement":[{"@type":"ListItem","@id":"https:\/\/inlibro.com#listItem","position":1,"name":"Home"}]},{"@type":"Organization","@id":"https:\/\/inlibro.com\/#organization","name
- **jsonld_page**: https://inlibro.com/
- **mentions**: {'payment_method': {'text': 'interactions clients et les ventes Gérer les comptes et la facturation Vous informer su', 'url': 'https://inlibro.com/politique_confidentialite_renseignements_personnels/', 'quote': 'incluent : Répondre aux demandes de contact Analyser le trafic et améliorer nos services Gérer les interactions clients et les ventes Gérer les comptes et la facturation Vous informer sur les mises à jour, les nouvelles fonctionnalités et les offres spéciales'}}

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "7236, rue Waverly, bureau 303, Montréal (Québec) H2R 2Y8", "address_country": "CA", "address_url": "https://inlibro.com/", "address_method": "pattern", "address_quote": "n des renseignements personnels 7236, rue Waverly, bureau 303 Montréal (Québec) H2R 2Y8", "phone": "888-604-2627", "phone_url": "https://inlibro.com/", "domain": "inlibro.com", "key": "vd:inlibro.com", "name": "Solutions inLibro inc.", "website": "https://inlibro.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Collège Stanislas | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Coll%C3%A8ge%20Stanislas | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Collège Stanislas | found | COLLÈGE STANISLAS INCORPORÉ |  | NEQ 1142238600 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | immatriculée | 1995-02-01 | Montréal | QC | 780 boul. Dollard, Montréal (Québec), H2V3G5 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Collège Stanislas | Q2983700 | official website on the organisation's domain (http://www.stanislas.qc.ca) + name |  | Collège Stanislas | Collège Stanislas | secondary school; collège; primary school; private school |  | Canada | 1938-01-01 |  |
| v | SOLUTIONS INLIBRO INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:7b2bb9599ef487dc",
 "ap_contact_team": {
  "emails": [
   "comptes.clients@stanislas.qc.ca",
   "comptes.fournisseurs@stanislas.qc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "comptes.clients@stanislas.qc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://stanislas.qc.ca/nous-joindre-2/",
    "quote": "slas.qc.ca 418 527-9998 poste 3223 Services financiers Frais de scolarité et facturation Facturation et recouvrement des frais de scolarité comptes.clients@stanislas.qc.ca Contact des fournisseurs",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "stanislas.qc.ca",
    "task_id": "CL-LD-23134"
   },
   {
    "email": "comptes.fournisseurs@stanislas.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://stanislas.qc.ca/nous-joindre-2/",
    "quote": "Contact des fournisseurs comptes.fournisseurs@stanislas.qc.ca Vie étudiante Service de vie étudiante – Campus de Montréal Véronique Bougeard, Adjointe administrative du servic",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "stanislas.qc.ca",
    "task_id": "CL-LD-23134"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of www.stanislas.qc.ca (8 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.stanislas.qc.ca (8 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 14)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1054198:solutions-inlibro-inc | Bibliothèque et Archives nationales du Québec | Contrat de services pour le transfert de connaissances, le support et la maintenance du catalogue du service québécois de traitement documentaire (SQTD) | 100910.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5d6ca4d1-fb70-48b1-b58a-aacd5543e276 |
| seao_quebec:1061635:solutions-inlibro-inc | CÉGEP André Laurendeau | Développement et déploiement de l’archive ouverte EDUQ | 25000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5bb5c8b9-fb2a-4d52-bf23-108001d26344 |
| seao_quebec:1324023:solutions-inlibro-inc | Ville de Deux-Montagnes. | Services professionnels - Implantation et support d'un système intégré de gestion de bibliothèque | 63236.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=daed1af1-4f3c-4e63-9579-e8ad56bcd3a8 |
| seao_quebec:1525814:solutions-inlibro-inc | Institut national de santé publique du Québec. | Hébergement du logiciel Koha, soutien technique, mise à jour annuelle | 20820.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d475a861-fa9f-49a8-b3e4-79b2133bbefa |
| seao_quebec:1625284:solutions-inlibro-inc | Heritage College | Renouvelllement et Services de soutien et d'hébergement pour logiciel Koha | 26481.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8d8001f1-d412-4899-a3ae-908225aee2ba |
| seao_quebec:1744413:solutions-inlibro-inc | Collecto Services regroupés en éducation | Services de migrations et de services informatiques de programmation  et en bibliothéconomie.  « Koha » | 358281.21 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d62d5cc6-f753-44ab-8952-5268587a31b6 |
| seao_quebec:20048305:solutions-inlibro-inc | Ville de Sorel-Tracy (approvisionnement) | Renouvellement des licences Koha et SécurAccès pour 1 an | 25734.62 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c201efac-b055-471d-87c1-2d15f6226bc0 |
| seao_quebec:20054048:solutions-inlibro-inc | Collège de Maisonneuve | Analyse de l'infrastructure et soutien mensuel pour dépannage | 52400.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=e8a8ea82-c8bd-4a5f-b03c-52fb663e73f3 |
| seao_quebec:20100808:solutions-inlibro-inc | Ville de Saguenay | SOLUTION DE GESTION D'IMPRESSION, DE COPIE ET DE NUMÉRISATION LIBRE-SERVICE DANS LES BIBLIOTHÈQUES PUBLIQUES DE SAGUENAY | 74791.62 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=00fa5e20-1182-4117-bb4a-ba1e45e32542 |
| seao_quebec:20120359:solutions-inlibro-inc | Ville de Rimouski. | Nouveau portail bibliothèque - Totem | 25869.38 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=089136d0-4a53-412e-a1fa-b05aafded555 |
| seao_quebec:20122375:solutions-inlibro-inc | Ville  de Sainte-Catherine | Système intégré de gestion de bibliothèque (SIGB) pour la bibliothèque Jocelyne-Larrivée-Bates | 69715.19 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=daad9cba-5a0b-47f2-bbd0-f0ab2fd10610 |
| seao_quebec:20159691:solutions-inlibro-inc | Municipalité  Saint-Thomas | Logiciel de gestion bibliothèque | 26124.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ff78adf7-a9fa-4431-8f6a-fd888442514b |
| seao_quebec:479487:solutions-inlibro-inc | Bibliothèque et Archives nationales du Québec | MODULE DE CATALOGAGE DANS LE CADRE DE LA MISE EN PLACE DU SERVICE QUÉBÉCOIS DE TRAITEMENT DOCUMENTAIRE | 300000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=68669d42-72ab-4619-a1e5-663c73e4aeb1 |
| seao_quebec:923191:solutions-inlibro-inc | Bibliothèque et Archives nationales du Québec | Contrat de développement par la firme lnLibro pour l'ajout de nouvelles fonctionnalités  au catalogue SQTD | 85910.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=63c144e2-7ba3-4e13-8361-0a70c2f15a27 |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

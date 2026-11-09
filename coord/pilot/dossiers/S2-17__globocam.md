# S2-17 — Globocam ⇄ Pedlex Ltée

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Globocam Montréal Inc — 11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3
SUBMIT TO: finance.cornwall@globocam.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE — 10000 boul du Golf, Montréal, QC, H1J 2Y7, CAN | GST/HST 103280152 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-02-09; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1142907162
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Étude de cas Pedlex aménage le département de service pour Globocam
```

## Relationship
- **rank_group**: L3
- **data_quality_score**: 66
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Globocam (organisation (type not stated in the record), jurisdiction not stated) — dated deal or payment 12 to 36 months ago: Pedlex Ltée | subject: Étude de cas Pedlex aménage le département de service pour Globocam | awarded 2025-08-07 | published by: customer story published by the vendor (dated) | record: https://www.pedlex.com/case-study/globocam/ | vendor in Canada because: customer story published by the vendor (dated)=que AGV – Rangerman Contactez-nous 10 000 boul. du Golf Montréal (Anjou) Québec H1J 2Y7 514 324-5310 514 32 | status rule: likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)
- **how_relationship_was_found**: a dated public record (payment register, subaward, vendor news release or EDC transaction) 12 to 36 months old, harvested by the lead scanners
- **keys**: lead:207e3f3e5358f023
- **tier**: L
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: customer story published by the vendor (dated); 0 in the contract dataset)

## Buyer
- **buyer**: Globocam
- **buyer_website**: https://globocam.ca/
- **buyer_address**: 11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3
- **buyer_phone**: 1 844 920-2276
- **buyer_contact_evidence_url**: https://globocam.ca/fr/nous-joindre/
- **buyer_legal_name_as_published**: Globocam Montréal Inc
- **buyer_logo_url**: https://globocam.ca/wp-content/uploads/2020/11/globocam-logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/globocam-lecamioncestnous
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://globocam.ca/fr/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance.cornwall@globocam.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://globocam.ca/fr/nous-joindre/?val=Financement/
- **email_evidence_quote**: __cf_email__" data-cfemail="55263027233c36307b363a273b223439391532393a373a3634387b3634">[email protected]</template></option><option value="finance.cornwall@globocam.ca"><template class="__cf_email__" data-cfemail="f4929d9a959a9791da979b869a83959898b493989b969b979599da9795">[email protecte
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance.cornwall@globocam.ca (finance/accounting dept or supplier-payment office) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02 | page: https://globocam.ca/fr/nous-joindre/?val=Financement/ | quote: "__cf_email__" data-cfemail="55263027233c36307b363a273b223439391532393a373a3634387b3634">[email protected]</template></option><option value="finance.cornwall@glo" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_deep01.csv task CL-DA-03001
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject;ruf=mailto:globocam@ca.cp-dmarc.com; rua=mailto:globocam@ca.cp-dmarc.com;
- **dmarc_record_domain**: globocam.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spfa.cpmails.com include:spf.protection.outlook.com ip4:170.2.198.64/32 ip4:170.2.52.28/32 ip4:207.253.3.126/28 ip4:108.163.138.126/27 ip4:74.91.80.0/20 exists:%{i}._spf.mta.salesforce.com include:u5965629.wl130.sendgrid.net include:servers.mcsv.net include:_spf.smtp.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Globocam Montréal Inc — 11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3 ⏎ SUBMIT TO: finance.cornwall@globocam.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE — 10000 boul du Golf, Montréal, QC, H1J 2Y7, CAN | GST/HST 103280152 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-02-09; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1142907162 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Étude de cas Pedlex aménage le département de service pour Globocam
- **invoice_card_json**: {"bill_to": {"legal_name": "Globocam Montréal Inc", "legal_name_is_published": true, "address": "11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "finance.cornwall@globocam.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "103280152RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE", "bn9": "103280152 (recipient_business_number in the fed
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: Pedlex Ltée
- **vendor_legal_name**: LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE
- **vendor_trading_name**: Pedlex Ltée
- **vendor_registry_id**: Québec REQ (NEQ): 1142907162
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 10 000, BOULEVARD DU GOLF, MONTRÉAL (QUÉBEC), H1J2Y7
- **vendor_neq**: 1142907162 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 5619 — COMM. GROS CONBIN. MÉTAUX ET PRODUITS EN MÉTAL
- **vendor_employees_quebec**: De 26 à 49
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 10000 boul du Golf, Montréal, QC, H1J 2Y7, CAN
- **vendor_country_basis**: customer story published by the vendor (dated)=que AGV – Rangerman Contactez-nous 10 000 boul. du Golf Montréal (Anjou) Québec H1J 2Y7 514 324-5310 514 32
- **vendor_bn9**: 103280152 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-02-09; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 103280152RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.pedlex.com/
- **vendor_phone**: (514) 324-5310 poste : 247
- **vendor_contact_evidence_url**: https://www.pedlex.com/contact/
- **vendor_logo_url**: https://www.pedlex.com/wp-content/uploads/2025/07/logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/pedlex/
- **vendor_facts_provenance**: name and address: the record's vendor block (customer story published by the vendor (dated)); registry identity: Québec REQ (NEQ): 1142907162 status Québec REQ (NEQ): Immatriculée (1995-02-23) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 1976-09-27; phone / role e-mails / logo: the vendor's own site, https://www.pedlex.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.pedlex.com/ (site answers); NEQ: 1142907162 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (1995-02-23)
- **vendor_incorporation_date**: 1976-09-27
- **vendor_years_in_business**: 50.1 (since 1976-09-27, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: likely active (awarded 12-36 months ago; deal announced by the Canada-based vendor: press release / EDC transaction)
- **contract_title**: Étude de cas Pedlex aménage le département de service pour Globocam
- **contract_description**: Étude de cas Pedlex aménage le département de service pour Globocam (the record's title; the source publishes no separate description)
- **award_date**: 2025-08-07
- **contract_link**: https://www.pedlex.com/case-study/globocam/
- **source**: customer story published by the vendor (dated)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: customer story published by the vendor (dated); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 103280152RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Globocam Montréal Inc — 11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3 ⏎ SUBMIT TO: finance.cornwall@globocam.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE — 10000 boul du Golf, Montréal, QC, H1J 2Y7, CAN | GST/HST 103280152 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2023-02-09; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1142907162 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Étude de cas Pedlex aménage le département de service pour Globocam
- **invoice_card_json**: {"bill_to": {"legal_name": "Globocam Montréal Inc", "legal_name_is_published": true, "address": "11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "finance.cornwall@globocam.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "103280152RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE", "bn9": "103280152 (recipient_business_number in the fed
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance.cornwall@globocam.ca (finance/accounting dept or supplier-payment office)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02", "page: https://globocam.ca/fr/nous-joindre/?val=Financement/", "quote: \"__cf_email__\" data-cfemail=\"55263027233c36307b363a273b223439391532393a373a3634387b3634\">[email protected]</template></option><option value=\"finance.cornwall@glo\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_deep01.csv task CL-DA-03001"], "buyer_facts": ["address and phone: the buyer's own site, https://globocam.ca/fr/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (customer story published by the vendor (dated))", "registry identity: Québec REQ (NEQ): 1142907162 status Québec REQ (NEQ): Immatriculée (1995-02-23) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & contributions disclosure (recipient_business_number)", "GST/HST derived BN9 + RT0001 (CRA re

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://globocam.ca/fr/nous-joindre/?val=Financement/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, globocam.ca)
- **status**: ok
- **pages**: 2
- **language**: fr
- **legal_name**: Globocam Montréal Inc
- **legal_name_url**: https://globocam.ca/
- **legal_name_quote**: c’est nous. Plus de 30 ans d’expérience à votre service Recevoir l'infolettre Nous joindre © 2026 Globocam Montréal Inc. Tous droits réservés. Politique de vie privée © 2026 Globocam Montréal Inc. Tous droits réservés.
- **logo_url**: https://globocam.ca/wp-content/uploads/2020/11/globocam-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: globocam.ca
- **key**: vendor:GLOBOCAM (MONTRÉAL) INC.
- **name**: GLOBOCAM (MONTRÉAL) INC.
- **website**: https://globocam.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/globocam-lecamioncestnous
- **tel_links**: 18449202276; 5143444000; 18442385558; 5143534000; 18442626944; 4506414008; 18004635603; 4186572425; 18006063661; 4188373

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "11 275, boul. Métropolitain Est, Montréal-Est QC H1B 1A3", "address_country": "CA", "address_url": "https://globocam.ca/fr/nous-joindre/", "address_method": "pattern", "address_quote": "6 [email protected] Coordonnées 11 275, boul. Métropolitain Est Montréal-Est QC H1B 1A3 Heures d’ouverture Ventes Lun - Ven 8h à 17h Pièces et service Lun - Ven 7h à m", "phone": "1 844 920-2276", "phone_url": "https://globocam.ca/fr/nous-joindre/", "emails": "info@globocam.ca; sales.cornwall@globocam.ca; service.cornwall@globocam.ca; ventes@globocam.ca", "emails_url": "https://globocam.ca/fr/nous-joindre/", "domain": "globocam.ca", "key": "vd:globocam.ca", "name": "GLOBOCAM (MONTRÉAL) INC.", "website": "https://globocam.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, pedlex.com)
- **status**: ok
- **pages**: 5
- **language**: fr
- **logo_url**: https://www.pedlex.com/wp-content/uploads/2025/07/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: pedlex.com
- **key**: vendor:Pedlex Ltée
- **name**: Pedlex Ltée
- **website**: https://pedlex.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Pedlex
- **jsonld_logo**: https://www.pedlex.com/wp-content/uploads/2025/07/logo.svg
- **jsonld_url**: https://www.pedlex.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.pedlex.com\/a-propos\/","url":"https:\/\/www.pedlex.com\/a-propos\/","name":"À propos de Pedlex | Experts en solutions d’entreposage et manutention","isPartOf":{"@id":"https:\/\/www.pedlex.com\/#website"},"datePubli
- **jsonld_page**: https://www.pedlex.com/a-propos/
- **mentions**: {'payment_method': {'text': 'interactivité Vos renseignements personnels sont collectés par le biais des formulaires', 'url': 'https://www.pedlex.com/privacy-policy/', 'quote': 'ivante, des fichiers témoins (cookies) pour réunir des informations vous concernant. Formulaires et interactivité Vos renseignements personnels sont collectés par le biais des formulaires, à savoir : Formulaire de contact pour demander une soumission sur notre'}}
- **linkedin_url**: https://www.linkedin.com/company/pedlex/
- **tel_links**: 18887335399; 514 324-5310; 1-888-733-5399; 5143245310; +15143245310,247; (514) 324-5310

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "10,000 Boul. du Golf Montréal (Anjou), Québec H1J 2Y7", "address_country": "CA", "address_url": "https://www.pedlex.com/contact/", "address_method": "pattern", "address_quote": "Au plaisir de vous servir! Pedlex 10,000 Boul. du Golf Montréal (Anjou), Québec H1J 2Y7 514 324-5310 514 324-1849 1-888-733-5399 [email protected] Contact Page Form «", "phone": "(514) 324-5310 poste : 247", "phone_url": "https://www.pedlex.com/contact/", "domain": "pedlex.com", "key": "vd:pedlex.com", "name": "Pedlex Ltée", "website": "https://pedlex.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Globocam | not_found |  |  |  | Corporations Canada (open data) |  |  |  |  |  |  | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Globocam |  |  |  |  |  |  |  |  |  |  |
| v | CAMIONS GLOBOCAM ESTRIE INC. |  |  |  |  |  |  |  |  |  |  |
| v | CAMIONS GLOBOCAM QUÉBEC ET LÉVIS INC. |  |  |  |  |  |  |  |  |  |  |
| v | GLOBOCAM INC. |  |  |  |  |  |  |  |  |  |  |
| v | LES PRODUITS D'ENTREPOSAGE PEDLEX LTÉE |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:207e3f3e5358f023",
 "ap_contact_team": {
  "emails": [
   "finance.cornwall@globocam.ca",
   "info@globocam.ca",
   "administration.cornwall@globocam.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance.cornwall@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "__cf_email__\" data-cfemail=\"cdbea8bfbba4aea8e3aea2bfa3baaca1a18daaa1a2afa2aeaca0e3aeac\">[email protected]</template></option><option value=\"finance.cornwall@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"5b3d32353a35383e75383429352c3a37371b3c37343934383a3675383a\">[email protecte",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "info@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "ct wpcf7-validates-as-required dynamic-email-address\" aria-required=\"true\" aria-invalid=\"false\" name=\"dynamic-email-address\"><option value=\"info@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"01686f676e41666d6e636e62606c2f6260\">[email protected]</template></option><option value=",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "administration.cornwall@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "ct wpcf7-validates-as-required dynamic-email-address\" aria-required=\"true\" aria-invalid=\"false\" name=\"dynamic-email-address\"><option value=\"administration.cornwall@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"a9c8cdc4c0c7c0dadddbc8ddc0c6c787cac6dbc7dec8c5c5e9cec5c6cbc6cac8c487",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "finance.cornwall@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "__cf_email__\" data-cfemail=\"582b3d2a2e313b3d763b372a362f393434183f34373a373b3935763b39\">[email protected]</template></option><option value=\"finance.cornwall@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"92f4fbfcf3fcf1f7bcf1fde0fce5f3fefed2f5fefdf0fdf1f3ffbcf1f3\">[email protecte",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "info@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "ct wpcf7-validates-as-required dynamic-email-address\" aria-required=\"true\" aria-invalid=\"false\" name=\"dynamic-email-address\"><option value=\"info@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"fe97909891be9992919c919d9f93d09d9f\">[email protected]</template></option><option value=",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "administration.cornwall@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/",
    "quote": "ct wpcf7-validates-as-required dynamic-email-address\" aria-required=\"true\" aria-invalid=\"false\" name=\"dynamic-email-address\"><option value=\"administration.cornwall@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"650401080c0b0c16111704110c0a0b4b060a170b120409092502090a070a0604084b",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Globocam",
    "task_id": "CL-LD-31816"
   },
   {
    "email": "finance.cornwall@globocam.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://globocam.ca/fr/nous-joindre/?val=Financement/",
    "quote": "__cf_email__\" data-cfemail=\"55263027233c36307b363a273b223439391532393a373a3634387b3634\">[email protected]</template></option><option value=\"finance.cornwall@globocam.ca\"><template class=\"__cf_email__\" data-cfemail=\"f4929d9a959a9791da979b869a83959898b493989b969b979599da9795\">[email protecte",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_deep01.csv",
    "org": "Globocam",
    "task_id": "CL-DA-03001"
   }
  ]
 },
 "research_status": {
  "found": 7
 },
 "queries_tried": [
  "site crawl of globocam.ca (13 p
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 13)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1100786:pedlex-ltee | Commission Scolaire de la Pointe de L'Île | ACHAT ET INSTALLATION D'UN SYSTÈME D'ENTREPOSAGE | 26262.17 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f8f9e9d6-5572-4a98-a444-fe173643be30 |
| seao_quebec:1153304:pedlex-ltee | Commission scolaire de Laval. | Acquisition et installation de rangement pour le Centre de formation Le Chantier | 44709.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0b947750-b603-40bc-8a94-47ebbb875999 |
| seao_quebec:1326189:pedlex-ltee | Centre intégré de santé et de services sociaux de la Montérégie-Est | Acquisition d'établis de travail, cabinets et d'armoires de rangement pour pièces électroniques | 90491.95 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=97a94886-07c9-46c0-ba6f-0b23c0b787fc |
| seao_quebec:1337571:pedlex-ltee | Héma-Québec | MOBILIER MÉTALLIQUE | 281716.92 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=7c32fade-0fcf-41ac-98c9-27bac4cdac58 |
| seao_quebec:281695:pedlex-ltee | École Polytechnique | Mobilier de laboratoire | 27966.88 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=4660d3b9-2be5-4981-af80-2767ae78c770 |
| seao_quebec:323357:pedlex-ltee | Ministère de la Justice | Réaménagement des salles d'archives du Palais de justice de Baie-Comeau | 36988.58 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=27645b61-ec7e-43af-b5e2-3363b7d6a0b1 |
| seao_quebec:443054:pedlex-ltee | Centre de services partagés du Québec- Direction générale des acquisitions (DGACQ) | Tabourets robustes à deux marches | 24070.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b7fbdd3c-e7a1-470b-8de6-65a55d897339 |
| seao_quebec:451980:pedlex | Centre intégré de santé et de services sociaux (CISSS) des Laurentides | Cabinets et étagères de rangement | 74683.93 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5fb6f342-573d-4257-88a0-f03952198e44 |
| seao_quebec:563378:pedlex-ltee | Centre de services partagés du Québec- Direction générale des acquisitions (DGACQ) | Étagères pour un centre de préarchivage | 57596.16 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9da75c10-84c0-4207-913a-5812eab8746d |
| seao_quebec:586952:pedlex-ltee | Centre de services partagés du Québec- Direction générale des acquisitions (DGACQ) | Potence et palan | 20631.06 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c657d30a-4784-4b91-8a3a-2d1be8534e32 |
| seao_quebec:600449:pedlex-ltee | Cégep de l'Outaouais... | mezzanine | 26233.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fa83c6b6-91e0-48e4-b424-d3e2cbe9dab5 |
| seao_quebec:608428:pedlex-ltee | Commission Scolaire de la Pointe de L'Île | Fabrication de système de rangement modulaire | 32982.54 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=fde9986a-def6-4f34-ba9a-bcbaf21c3621 |
| seao_quebec:929582:pedlex-ltee | Commission des services électriques de Montréal | Système de palettiers, mezzanine, garde-fou et porte à faux. | 45845.07 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b82106ae-4f20-4fb5-ae25-a18b4e97ad81 |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S1-27 — Université Paris-Saclay ⇄ DNA Genotek Inc

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade B · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08) — Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay
SUBMIT TO: service.facturier@universite-paris-saclay.fr (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)
REFERENCE: contract CON-0001 (contract_id); tender TEN-0001 (tender_id) | PO rule: yes (as published: mentioning the purchase order number)
FROM / REMIT TO: DNA Genotek Inc. — 3000-500 Palladium Drive, Ottawa, On K2v 1c2 | GST/HST 872965843RT0001 (account derived from the BN9)
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: EUR | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay | AMOUNT: 1,300,000.00 EUR
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 93
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Université Paris-Saclay (organisation (type not stated in the record), EU) — public contract / purchase award in the last 12 months (dated record): DNA Genotek Inc | subject: Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay | instrument: framework agreement | contract number: CON-0001 (contract_id); 2026-017 (contract_reference); 2026-017 (buyer_contract_reference_api) | solicitation: TEN-0001 (tender_id); TEN-0001 (tender_reference); baae747a-99ea-4ef8-b742-fc51613cf426 (notice_id_uuid) | all identifiers: {"publication_number": "202074-2026", "ojs_issue": "58/2026", "notice_id_uuid": "baae747a-99ea-4ef8-b742-fc51613cf426", "procedure_id": "4ec561b3-0013-44ad-aa6c-1cad85320ee1", "procedure_internal_id": "2025-A007", "lot_id": "LOT-0000", "lot_internal_id": "F-PF-1797276", "lot_result_id": "RES-0001",  | value: 1300000.0 EUR | awarded 2026-03-13, start 2026-03-13 | published by: TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU) | record: https://ted.europa.eu/en/notice/-/detail/202074-2026 | vendor in Canada because: eForms XML efac:Organizations/efac:Organization/efac:Company/cac:PostalAddress/cac:Country/cbc:IdentificationCode = CAN for the tenderer organization referenced by the winning tender (BT-514-Organization-Company); API fi | status rule: likely active (source marks it as continuing; awarded in the last 3 years, no end date published) | this buyer has 1 records with Canada-located
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: b:ce936a703160422e
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Université Paris-Saclay
- **buyer_website**: https://www.universite-paris-saclay.fr
- **buyer_address**: Gif Sur Yvette, 91190, FRA
- **buyer_legal_name_as_published**: Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08)
- **buyer_logo_url**: https://www.universite-paris-saclay.fr/sites/default/files/media/2019-12/logo-ups.svg
- **buyer_linkedin_url**: https://www.linkedin.com/company/universit%C3%A9-paris-saclay
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q109409389; university in France; public university
- **buyer_founded**: 2019-11-05 (Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08)
- **buyer_legal_form**: public scientific, cultural or professional establishment (Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08)
- **buyer_facts_provenance**: address: the buyer's record / buyer table; legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; invoice mailing address: the lane's AP page (https://www.universite-paris-saclay.fr/faq-fournisseurs); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_payment_method_preference**: encourage you to look for journals that do not charge APCs: Check (as printed on https://www.universite-paris-saclay.fr/en/recherche/science-ouverte/publication-fees-apc, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: service.facturier@universite-paris-saclay.fr
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.universite-paris-saclay.fr/faq-fournisseurs
- **email_evidence_quote**: ompte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@universite-paris-saclay.fr . 2 - Chorus Portail Pro (CPP) Pour déposer votre/vos facture(s), vous avez uniquement besoin du numéro d
- **email_evidence_context**: ay. Votre/Vos facture(s) doit/doivent normalement être déposées sur Chorus Portail Pro . Vous devez créer un compte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@universite-paris-saclay.fr . 2 - Chorus Portail Pro (CPP) Pour déposer votre/vos facture(s), vous avez uniquement besoin du numéro de SIRET de l’Université Paris Saclay (13002602400054) et du numéro d’engagement juridique (4500xxxxxx). Aucun code service n’est nécessaire au d (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: service.facturier@universite-paris-saclay.fr (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.universite-paris-saclay.fr/faq-fournisseurs | quote: "ompte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@un" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mx1.u-psud.fr) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00020
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mx1.u-psud.fr)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:dmarc-report@universite-paris-saclay.fr; ruf=mailto:dmarc-report@universite-paris-saclay.fr; fo=1; adkim=r; aspf=r
- **dmarc_record_domain**: universite-paris-saclay.fr
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 mx ip4:129.175.213.0/25 ip4:129.175.213.128/32 ip4:129.175.212.64/29 include:spf.protection.outlook.com include:spf.jobaffinity.fr include:spf.saclay.cblue.be include:spfa.alinto.net include:sendgrid.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: yes (v=BIMI1; l=https://www.universite-paris-saclay.fr/UPS_BIMI.svg;)
- **invoice_mailing_address**: Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay
- **invoicing_requirements**: Normally submit through ChorusPortailPro; published temporary email option while creating freeportalaccount. Same mailbox handles status/reminders. Invoice routing SIRET13002602400054 and engagementjuridique/PO4500xxxxxx, no servicecode required. Incorrect/missingengagement rejected byportal or emai | invoice format as published: pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: mentioning the purchase order number) (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "yes (as published: mentioning the purchase order number) (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "invoice_format": "pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "mailing_address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay", "requirements_text": "Normally submit through ChorusPortailPro; published temporary email option while creating freeportalaccount. Same mailbox handles status/reminders. Invoice routing SIRET13002602400054 and engagementjuridique/PO4500xxxxxx, no servicecode required. Incorrect/missingengagement rejected byportal or emai"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08) — Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay ⏎ SUBMIT TO: service.facturier@universite-paris-saclay.fr (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08) ⏎ REFERENCE: contract CON-0001 (contract_id); tender TEN-0001 (tender_id) | PO rule: yes (as published: mentioning the purchase order number) ⏎ FROM / REMIT TO: DNA Genotek Inc. — 3000-500 Palladium Drive, Ottawa, On K2v 1c2 | GST/HST 872965843RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: EUR | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay | AMOUNT: 1,300,000.00 EUR
- **invoice_card_json**: {"bill_to": {"legal_name": "Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (invoicing page in French)"}, "submit_to": {"email": "service.facturier@universite-paris-saclay.fr", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay", "format": "pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: mentioning the purchase order number) (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "CON-0001 (contract_id); 2026-017 (contract_reference); 2026-017 (buyer_contract_reference_api)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CON-0001 (contract_id) — source ted_eu"}, "terms": {"pay
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: payment terms; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: fr
- **template_language**: fr (invoicing page in French)
- **invoice_reference_hint**: contract or agreement number: CON-0001 (contract_id) — source ted_eu

## Vendor
- **vendor**: DNA Genotek Inc
- **vendor_legal_name**: DNA Genotek Inc.
- **vendor_registry_id**: Corporations Canada (corporation number): 7935226; corporation number 7935226 (Corporations Canada (open data))
- **vendor_registry_url**: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=7935226
- **vendor_registered_address**: 500 PALLADIUM DRIVE, SUITE 3000, KANATA, ON, K2V 1C2, CA
- **vendor_legal_form**: Canada Business Corporations Act (Canada (federal))
- **vendor_directors_range**: 1 to 10 directors (Corporations Canada)
- **vendor_last_annual_filing**: ; Corporations Canada anniversary 2011-08-17
- **vendor_address**: 3000-500 Palladium Drive, Ottawa, On K2v 1c2
- **vendor_country_basis**: eForms XML efac:Organizations/efac:Organization/efac:Company/cac:PostalAddress/cac:Country/cbc:IdentificationCode = CAN for the tenderer organization referenced by the winning tender (BT-514-Organization-Company); API field winner-country / organisation-country-tenderer
- **vendor_bn9**: 872965843
- **vendor_gst_hst_derived**: 872965843RT0001
- **vendor_website**: https://dnagenotek.com/
- **vendor_logo_url**: https://dnagenotek.com/images/dna-genotek-logo-index.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://dnagenotek.com/ (DNA Genotek Inc. Welcome to DNA Genotek Inc., a leading provider of products for biological sample collection, stabilization and preparation. To ensure you see )
- **vendor_peppol_id**: iso6523-actorid-upis 0060:872965843 (Peppol Directory, registered 2026-06-26; https://directory.peppol.eu/public/locale-en_US/menuitem-search?q=0060%3A872965843)
- **vendor_facts_provenance**: name and address: the record's vendor block (TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU)); registry identity: Corporations Canada (corporation number): 7935226; corporation number 7935226 (Corporations Canada (open data)) status Corporations Canada (corporation number): Active (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; strong); BN9: corporations_canada 7935226 (strong match); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2011-08-17; website: https://dnagenotek.com/
- **vendor_concentration_top_share**: DNA Genotek Inc: 100% of 1 records
- **vendor_registry_status**: Corporations Canada (corporation number): Active
- **vendor_registry_match_level**: strong
- **vendor_incorporation_date**: 2011-08-17
- **vendor_years_in_business**: 15.2 (since 2011-08-17, registry date)
- **vendor_bn_source**: corporations_canada 7935226 (strong match)

## Contract
- **po_required_as_published**: yes (as published: mentioning the purchase order number) (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)
- **contract_status**: likely active (source marks it as continuing; awarded in the last 3 years, no end date published)
- **contract_reference**: {"publication_number": "202074-2026", "ojs_issue": "58/2026", "notice_id_uuid": "baae747a-99ea-4ef8-b742-fc51613cf426", "procedure_id": "4ec561b3-0013-44ad-aa6c-1cad85320ee1", "procedure_internal_id": "2025-A007", "lot_id": "LOT-0000", "lot_internal_id": "F-PF-1797276", "lot_result_id": "RES-0001", "tender_id": "TEN-0001", "tender_reference": "TEN-0001", "contract_id": "CON-0001", "contract_reference": ["2026-017"], "previous_notice_ids": [], "buyer_contract_reference_api": ["2026-017"]}
- **contract_title**: Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay
- **contract_description**: Projet BioCF France 2030 - Achat de kits salivaires pour les cohortes E3N-Générations et Constances UPSaclay Le présent accord-cadre a pour objet la fourniture et la livraison d'une quantité prévisionnelle de 80 000 kits d'auto-prélèvements salivaires sur stabilisateur pour extraction d'ADN pour …
- **contract_or_agreement_number**: CON-0001 (contract_id); 2026-017 (contract_reference); 2026-017 (buyer_contract_reference_api)
- **solicitation_or_tender_number**: TEN-0001 (tender_id); TEN-0001 (tender_reference); baae747a-99ea-4ef8-b742-fc51613cf426 (notice_id_uuid)
- **award_or_notice_id**: LOT-0000 (lot_id); RES-0001 (lot_result_id); F-PF-1797276 (lot_internal_id); 2025-A007 (procedure_internal_id); 4ec561b3-0013-44ad-aa6c-1cad85320ee1 (procedure_id)
- **commodity_codes**: CPV 33954000
- **contract_value**: 1300000.0
- **currency**: EUR
- **award_date**: 2026-03-13
- **start_date**: 2026-03-13
- **contract_link**: https://ted.europa.eu/en/notice/-/detail/202074-2026
- **source**: TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU)
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 1
- **record_sources**: TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU) (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is accounted for by the buyer under the reverse charge where applicable
- **vendor_gst_hst_derived**: 872965843RT0001

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08) — Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay ⏎ SUBMIT TO: service.facturier@universite-paris-saclay.fr (invoicing/AP mailbox, confirmed by the referee) | format: pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08) ⏎ REFERENCE: contract CON-0001 (contract_id); tender TEN-0001 (tender_id) | PO rule: yes (as published: mentioning the purchase order number) ⏎ FROM / REMIT TO: DNA Genotek Inc. — 3000-500 Palladium Drive, Ottawa, On K2v 1c2 | GST/HST 872965843RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); EU VAT is | CURRENCY: EUR | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay | AMOUNT: 1,300,000.00 EUR
- **invoice_card_json**: {"bill_to": {"legal_name": "Université Paris-Saclay (official name per Wikidata Q109409389, official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name; 2026-11-08)", "legal_name_is_published": true, "address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay", "address_is_the_invoice_address": true, "tax_number": "", "language": "fr (invoicing page in French)"}, "submit_to": {"email": "service.facturier@universite-paris-saclay.fr", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay", "format": "pdf format (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: mentioning the purchase order number) (as printed on https://www.universite-paris-saclay.fr/en/doctoral-schools/mechanical-energy-and-materials-engineering-smemag, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "CON-0001 (contract_id); 2026-017 (contract_reference); 2026-017 (buyer_contract_reference_api)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: CON-0001 (contract_id) — source ted_eu"}, "terms": {"pay
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: payment terms; AP phone or contact for follow-up
- **ap_grade**: B
- **ap_score**: 82
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known; invoice format / requirements published; payment cycle or method published (plausibility) | missing: finance mailbox; payment terms published; AP phone or AP contact
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["service.facturier@universite-paris-saclay.fr (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.universite-paris-saclay.fr/faq-fournisseurs", "quote: \"ompte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@un\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mx1.u-psud.fr)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00020"], "buyer_facts": ["address: the buyer's record / buyer table", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "invoice mailing address: the lane's AP page (https://www.universite-paris-saclay.fr/faq-fournisseurs)", "invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (TED - Tenders Electronic Daily (Supplement to the Official Journal of the EU))", "registry identity: Corporat

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.universite-paris-saclay.fr/faq-fournisseurs | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, universite-paris-saclay.fr)
- **status**: ok
- **pages**: 6
- **language**: fr
- **legal_name**: Université Paris
- **legal_name_url**: https://www.universite-paris-saclay.fr/
- **legal_name_quote**: Université Paris-Saclay Aller au contenu principal Les autres sites de l'université Faculté de Droit Economie Manage
- **logo_url**: https://www.universite-paris-saclay.fr/sites/default/files/media/2019-12/logo-ups.svg
- **logo_basis**: logo image in the site header
- **domain**: universite-paris-saclay.fr
- **key**: b:ce936a703160422e
- **name**: Université Paris-Saclay
- **website**: https://universite-paris-saclay.fr/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Centre for Research
- **legal_name_stated_url**: https://www.universite-paris-saclay.fr/en/about/universite-paris-saclay-scientific-framework
- **legal_name_stated_quote**: ue Public health OVERVIEW The Graduate School for Public Health, built on research conducted by the Centre for Research in Epidemiology and Population Health (CESP) and its affiliated units, focuses on significant healt
- **mentions**: {'payment_method': {'text': 'Interactive, 4 rue de la République, 69001 Lyon, www', 'url': 'https://www.universite-paris-saclay.fr/mentions-legales', 'quote': 'ion graphique / développement / maintenance Le site a été créé et développé par la société Intuitiv Interactive, 4 rue de la République, 69001 Lyon, www.intuitiv-interactive.com . Le site est maintenu par la société Axess, 8 avenue de la gare, 26958 Va'}}
- **linkedin_url**: https://www.linkedin.com/company/universit%C3%A9-paris-saclay

## Buyer role mailboxes found on its site (org_contacts)
_not read_

## Vendor site facts (org_extras, dnagenotek.com)
- **status**: ok
- **pages**: 1
- **v**: 2
- **language**: en
- **logo_url**: https://dnagenotek.com/images/dna-genotek-logo-index.png
- **logo_basis**: logo image in the site header
- **domain**: dnagenotek.com
- **key**: vendor:DNA Genotek Inc
- **name**: DNA Genotek Inc
- **website**: https://dnagenotek.com/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Université Paris-Saclay | Q109409389 | official website on the organisation's domain (https://www.universite-paris-saclay.fr) + name | Université Paris-Saclay [fr] | Paris-Saclay University | université Paris-Saclay | university in France; public university | public scientific, cultural or professional establishment | France | 2019-11-05 | Gif-sur-Yvette |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:ce936a703160422e",
 "ap_contact_team": {
  "emails": [
   "service.facturier@universite-paris-saclay.fr",
   "contact@agorae-paris-saclay.fr",
   "contact@tremplin-handicap.fr",
   "info@mjctati.fr"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay",
  "invoicing_requirements": "Normally submit through ChorusPortailPro; published temporary email option while creating freeportalaccount. Same mailbox handles status/reminders. Invoice routing SIRET13002602400054 and engagementjuridique/PO4500xxxxxx, no servicecode required. Incorrect/missingengagement rejected byportal or email. Orderingservice suppliesPO; invoiceoffice cannot. Market/agreementnumber alone insufficient. Singleinvoiceaddress Servicefacturier,rueDoyenGeorgesPoitou,91400Orsay. No fixedpaymentperiod/format onFAQ.",
  "evidence": [
   {
    "email": "service.facturier@universite-paris-saclay.fr",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.universite-paris-saclay.fr/faq-fournisseurs",
    "quote": "ompte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@universite-paris-saclay.fr . 2 - Chorus Portail Pro (CPP) Pour déposer votre/vos facture(s), vous avez uniquement besoin du numéro d",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Université Paris-Saclay",
    "task_id": "CO-AP-00373"
   },
   {
    "email": "service.facturier@universite-paris-saclay.fr",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.universite-paris-saclay.fr/faq-fournisseurs",
    "quote": "ompte, c’est gratuit. En attendant la création de votre compte sur le portail Chorus Pro, vous pouvez nous la/les faire parvenir par mail à service.facturier@universite-paris-saclay.fr . 2 - Chorus Portail Pro (CPP) Pour déposer votre/vos facture(s), vous avez uniquement besoin du numéro d",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Université Paris-Saclay",
    "task_id": "CL-WS-00020"
   },
   {
    "email": "service.facturier@universite-paris-saclay.fr",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": "Université Paris-Saclay, Service facturier, rue du doyen Georges Poitou, 91400 Orsay",
    "requirements": "Normally submit through ChorusPortailPro; published temporary email option while creating freeportalaccount. Same mailbox handles status/reminders. Invoice routing SIRET13002602400054 and engagementjuridique/PO4500xxxxxx, no servicecode required. Incorrect/missingengagement rejected byportal or email. Orderingservice suppliesPO; invoiceoffice cannot. Market/agreementnumber alone insufficient. Singleinvoiceaddress Servicefacturier,rueDoyenGeorgesPoitou,91400Orsay. No fixedpaymentperiod/format onFAQ.",
    "applies_to": "whole_organisation",
    "page_url": "https://www.universite-paris-saclay.fr/faq-fournisseurs",
    "quote": "service.facturier@universite-paris-saclay.fr . 2 - Chorus Portail Pro (CPP) Pour déposer votre/vos facture(s), vous avez uniquement besoin du numéro de SIRET de l’Université Paris Saclay (13002602400054) et du numéro d’engagement juridique (4500xxxxxx). Aucun",
    "retrieved_date": "2026-11-09",
    "found_by": "codex",
    "verification": "verified",
    "source_file": "codex_buyer_ap_results_batch04.csv",
    "org": "Université Paris-Saclay",
    "task_id": "CO-AP-00373"
   },
   {
    "email": "contact@agorae-paris-saclay.fr",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.universite-paris-saclay.fr/admission/bourses-et-aides-financieres/la-cooperative-solidaire",
    "quote": "diants d’acheter des produits 90 % moins cher qu’en supermarché et propose des ateliers et événements gratuits ou à prix réduits. Contact : contact@agorae-paris-saclay.fr Plus d'informations pratiques à retrouver sur la page des Aides alimentaires . Devenir bénéficiaire de l’épicerie solid",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Université Paris-Saclay",
    "task_id": "CO-AP-00373"
   },
   {
    "email": "contact@tremplin-handicap.fr",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.universite-paris-saclay.fr/admission/bourses-et-aides-financieres/la-cooperative-solidaire",
    "quote": "accompagne l’étudiante et l’étudiant dans son projet académique et professionnel en réalisant notamment des ateliers collectifs. Contact : contact@tremplin-handicap.fr Plus d'informations : N’hésitez pas à vous rendre sur le site internet de l’association http://www.tremplin-handicap.fr/",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Université Paris-Saclay",
    "task_id": "CO-AP-00373"
   },
   {
    "email": "info@mjctati.fr",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.univers
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| ted_eu:202074-2026:TEN-0001 | ted_eu | ongoing_inferred | Projet Biocf France 2030 - Achat de kits salivaires pour les cohortes E3n-Générations et Constances Upsaclay | 1300000.0 | EUR |  |  | {"publication_number": "202074-2026", "ojs_issue": "58/2026", "notice_id_uuid": "baae747a-99ea-4ef8-b742-fc51613cf426", "procedure_id": "4ec561b3-0013-44ad-aa6c-1cad85320ee1", "procedure_internal_id": | https://ted.europa.eu/en/notice/-/detail/202074-2026 |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 6)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1622182:dna-genotek-inc | Institut de Cardiologie de Montréal. | ACQUISITION DE MATÉRIEL DE COLLECTE DE SALIVE POUR ÉTUDE COLCOT | 118000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c188fc8d-9c03-436d-9816-19b487287650 |
| us_state_virginia:2026:A236_P0310321: | Virginia Commonwealth University | OGR600Saliva SelfCollection Kit | 3250.0 |  |  | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| us_state_virginia:2026:A236_P0340796: | Virginia Commonwealth University | OGR600Saliva SelfCollection Kit | 875.0 |  |  | https://data.virginia.gov/dataset/eva-procurement-data-2026-virginia |
| who:201334348 | World Health Organization - Headquarters | Diagnostics and Research Biologicals | 577053.0 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2015-goods-awarded-contracts.pdf?sfvrsn=c4b96b6f_3&ua=1 |
| worldbank:DS00005:1630461:516306 | Georgia (borrower; implementing agency not published) | Procurement of the Saliva collection kits | 363000.0 |  |  | https://projects.worldbank.org/en/projects-operations/project-detail/P173911 |
| us_ny_state_authorities_procurement:0bfd677c17a3f76b | New York City Health and Hospitals Corporation | OTHER |  |  |  | https://data.ny.gov/dataset/Procurement-Report-for-Local-Authorities/8w5p-k45m |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

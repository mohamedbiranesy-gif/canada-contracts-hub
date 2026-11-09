# S2-38 — Regroupement québécois de la danse ⇄ maison pour la danse de Québec

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08) — 3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/)
SUBMIT TO: info@quebecdanse.org (general mailbox, confirmed by the referee) | invoice portal: https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Ville de Québec (stated on the vendor's legal page: https://www.maisonpourladanse.ca/a-propos/partenaires/) — 336, rue du Roi, Québec (Québec), G1K 2W5 | GST/HST 119012946 (as printed on the vendor's site: https://www.maisonpourladanse.ca/a-propos/faire-une-difference/)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 38
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Regroupement québécois de la danse (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): maison pour la danse de Québec | subject: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse | published by: the Canada-located vendor's own website | record: https://www.maisonpourladanse.ca/appel-a-projets/appel-a-participation-le-bloc-danse/ | vendor in Canada because: vendor located in Canada (wd)=maisonpourladanse.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:9834ceed0e69997d
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Regroupement québécois de la danse
- **buyer_website**: https://quebecdanse.org/
- **buyer_address**: 3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/)
- **buyer_phone**: (514) 849-4003
- **buyer_contact_evidence_url**: https://www.quebecdanse.org/a-propos/contact/
- **buyer_legal_name_as_published**: REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08)
- **buyer_logo_url**: https://www.quebecdanse.org/
- **buyer_website_status**: site answers
- **buyer_registry_id**: NEQ 1140380222 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.quebecdanse.org/a-propos/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@quebecdanse.org
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.quebecdanse.org/
- **email_evidence_quote**: membre Réseaux sociaux Coordonnées 1450,rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Voir la carte Téléphone: (514) 849-4003 info@quebecdanse.org Langue English Français Le RQD reconnaît que nous sommes situés en territoire non-cédé de la nation Kanien'kehá:ka, gardienne des
- **email_evidence_context**: RQD Adhérer au RQD Ressources Navigation Agenda de la danse Actualités de la danse Babillard Répertoire Espace membre Réseaux sociaux Coordonnées 1450,rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Voir la carte Téléphone: (514) 849-4003 info@quebecdanse.org Langue English Français Le RQD reconnaît que nous sommes situés en territoire non-cédé de la nation Kanien'kehá:ka, gardienne des terres et des eaux. C’est dans le respect des liens avec le passé, le présent et l'avenir que nous reconnaissons les re (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@quebecdanse.org (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.quebecdanse.org/ | quote: "membre Réseaux sociaux Coordonnées 1450,rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Voir la carte Téléphone: (514) 849-4003 info@quebecdanse.org " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23332
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100; rua=mailto:re+dsbbads3ka8@dmarc.postmarkapp.com; sp=none; aspf=r;
- **dmarc_record_domain**: quebecdanse.org
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 mx a ip4:149.56.126.210 ip4:67.43.226.2 ip4:67.43.224.103 ip4:68.168.119.163 ip4:149.56.38.221  include:_spf.google.com include:servers.mcsv.net a:mail.quebecdanse.org ip4:72.10.170.194 include:spf.web-dns1.com include:_spf.layer7.hosting ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Coupa
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08) — 3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/) ⏎ SUBMIT TO: info@quebecdanse.org (general mailbox, confirmed by the referee) | invoice portal: https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Ville de Québec (stated on the vendor's legal page: https://www.maisonpourladanse.ca/a-propos/partenaires/) — 336, rue du Roi, Québec (Québec), G1K 2W5 | GST/HST 119012946 (as printed on the vendor's site: https://www.maisonpourladanse.ca/a-propos/faire-une-difference/)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse
- **invoice_card_json**: {"bill_to": {"legal_name": "REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08)", "legal_name_is_published": true, "address": "3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@quebecdanse.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": fal
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)

## Vendor
- **vendor**: maison pour la danse de Québec
- **vendor_legal_name**: Ville de Québec (stated on the vendor's legal page: https://www.maisonpourladanse.ca/a-propos/partenaires/)
- **vendor_trading_name**: maison pour la danse de Québec
- **vendor_address**: 336, rue du Roi, Québec (Québec), G1K 2W5
- **vendor_country_basis**: vendor located in Canada (wd)=maisonpourladanse.ca
- **vendor_bn9**: 119012946 (as printed on the vendor's site: https://www.maisonpourladanse.ca/a-propos/faire-une-difference/)
- **vendor_gst_hst_derived**: 119012946RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://maisonpourladanse.ca
- **vendor_emails**: info@maisonpourladanse.ca
- **vendor_contact_evidence_url**: https://www.maisonpourladanse.ca/nous-joindre/
- **vendor_logo_url**: https://www.maisonpourladanse.ca/wp-content/themes/maisonpourladanse/assets/images/logo-maisonpourladanse--white@2x.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/10990746/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); BN9: registry match; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.maisonpourladanse.ca/nous-joindre/ (tools/org_contacts.py, org_extras.py); website: https://maisonpourladanse.ca (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse
- **contract_description**: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse (the record's title; the source publishes no separate description)
- **contract_link**: https://www.maisonpourladanse.ca/appel-a-projets/appel-a-participation-le-bloc-danse/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119012946RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08) — 3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/) ⏎ SUBMIT TO: info@quebecdanse.org (general mailbox, confirmed by the referee) | invoice portal: https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Ville de Québec (stated on the vendor's legal page: https://www.maisonpourladanse.ca/a-propos/partenaires/) — 336, rue du Roi, Québec (Québec), G1K 2W5 | GST/HST 119012946 (as printed on the vendor's site: https://www.maisonpourladanse.ca/a-propos/faire-une-difference/)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Appel à participation - Le Bloc.Danse - Maison pour la danse : Maison pour la danse
- **invoice_card_json**: {"bill_to": {"legal_name": "REGROUPEMENT QUÉBÉCOIS DE LA DANSE (as registered: Registraire des entreprises du Québec (open data), NEQ 1140380222, 2026-11-08)", "legal_name_is_published": true, "address": "3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5 (schema.org JSON-LD PostalAddress on https://www.quebecdanse.org/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@quebecdanse.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://www.quebecdanse.org/agenda/leo-hit-coupal-hanna-sybille-muller/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": fal
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@quebecdanse.org (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.quebecdanse.org/", "quote: \"membre Réseaux sociaux Coordonnées 1450,rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Voir la carte Téléphone: (514) 849-4003 info@quebecdanse.org \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23332"], "buyer_facts": ["address and phone: the buyer's own site, https://www.quebecdanse.org/a-propos/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "BN9: registry match", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, https://www.maisonpourladanse.ca/n

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.quebecdanse.org/ | 2026-11-08 | ok |  |  | Coupa | (514) 849-4003 |  |  |  |  |  |

## Buyer site facts (org_extras, quebecdanse.org)
- **status**: ok
- **pages**: 6
- **language**: fr
- **legal_name**: emeurant à l'écoute et en apprentissage continue des réalités des membres de sa communauté
- **legal_name_url**: https://www.quebecdanse.org/
- **legal_name_quote**: onnaît également ses biais discriminatoires passés et travaille continuellement à les éliminer, en demeurant à l'écoute et en apprentissage continue des réalités des membres de sa communauté. © 2026 Regroupement québécois de la danse. Politique de confidentialité — Conditions d'utilisation
- **logo_url**: https://www.quebecdanse.org/
- **logo_basis**: logo image in the site header
- **domain**: quebecdanse.org
- **key**: lead:9834ceed0e69997d
- **name**: quebecdanse.org
- **website**: https://quebecdanse.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: Regroupement québécois de la danse
- **jsonld_alternate_name**: RQD
- **jsonld_address**: 3680, rue Jeanne-Mance, bureau 440, Montreal, QC, H2X 2K5
- **jsonld_phone**: (514) 849-4003
- **jsonld_url**: https://quebecdanse.org/
- **jsonld_founding_date**: 1984-10-04
- **jsonld_same_as**: https://twitter.com/quebecdanse; https://www.facebook.com/quebecdanse/; https://www.instagram.com/quebecdanse/; https://vimeo.com/user62366480
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"Organization","@id":"https:\/\/www.quebecdanse.org\/#schema-publishing-organization","url":"https:\/\/www.quebecdanse.org","name":"Regroupement qu\u00e9b\u00e9cois de la danse","description":"Le portail des professionnels et des passionn\u00e9s 
- **jsonld_page**: https://www.quebecdanse.org/
- **legal_name_stated**: Prix de la danse de Montréal
- **legal_name_stated_url**: https://www.quebecdanse.org/a-propos/prix-interprete/
- **legal_name_stated_quote**: gélique Willkie © Kevin Calixte À PROPOS Créé en 2014 à l’occasion du 30 e anniversaire du RQD, le Prix de la danse de Montréal – Catégorie INTERPRÈTE présenté par le Regroupement québécois de la danse et la Caisse Desjardins d
- **mentions**: {'payment_method': {'text': 'interactives et à l’intelligence artificielle', 'url': 'https://www.quebecdanse.org/a-propos/presentation/journee-internationale-de-la-danse/', 'quote': 'dans une vidéo où son image s’hybride avec une diversité de corps grâce aux technologies numériques interactives et à l’intelligence artificielle. Un hommage brut à l’art de la danse et à son caractère universel, réalisé en collaboration avec l’'}}
- **tel_links**: 5148494003

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "1450 rue City Councillors, bureau 500, Montréal (Québec) H3A 2E6", "address_country": "CA", "address_url": "https://www.quebecdanse.org/a-propos/contact/", "address_method": "pattern", "address_quote": "t québécois de la danse 1450 rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Téléphone : (514) 849-4003 Télécopieur : (514) 849-3288 Courriel : info@quebecd", "phone": "(514) 849-4003", "phone_url": "https://www.quebecdanse.org/a-propos/contact/", "emails": "administration@quebecdanse.org; communication@quebecdanse.org; info@quebecdanse.org", "emails_url": "https://www.quebecdanse.org/a-propos/contact/", "domain": "quebecdanse.org", "key": "lead:9834ceed0e69997d", "name": "quebecdanse.org", "website": "https://quebecdanse.org/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, maisonpourladanse.ca)
- **status**: ok
- **pages**: 6
- **language**: fr
- **logo_url**: https://www.maisonpourladanse.ca/wp-content/themes/maisonpourladanse/assets/images/logo-maisonpourladanse--white@2x.png
- **logo_basis**: logo image in the site header
- **bn**: 119012946
- **bn_program**: RR0001
- **bn_label**: numéro d’organisme de bienfaisance 11901
- **bn_url**: https://www.maisonpourladanse.ca/a-propos/faire-une-difference/
- **bn_quote**: nt émis pour les dons de 25 $ et plus par le Groupe Danse Partout , OBNL gestionnaire de la Maison (numéro d’organisme de bienfaisance 119012946RR0001). Saviez-vous qu’en tant que particulier, un premier don de 5 000 $ en soutien à la culture vous do
- **domain**: maisonpourladanse.ca
- **key**: vendor:maison pour la danse de Québec
- **name**: maison pour la danse de Québec
- **website**: https://maisonpourladanse.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Maison pour la danse
- **jsonld_logo**: https://www.maisonpourladanse.ca/wp-content/uploads/2017/11/MPD_LOGO-RGB.png
- **jsonld_url**: https://www.maisonpourladanse.ca/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.maisonpourladanse.ca\/","url":"https:\/\/www.maisonpourladanse.ca\/","name":"Maison pour la danse - Énergie collective. Synergie créative.","isPartOf":{"@id":"https:\/\/www.maisonpourladanse.ca\/#website"},"about":{
- **jsonld_page**: https://www.maisonpourladanse.ca/
- **legal_name_stated**: Ville de Québec
- **legal_name_stated_url**: https://www.maisonpourladanse.ca/a-propos/partenaires/
- **legal_name_stated_quote**: nse (5,4 M$). Ministère de la Culture et des Communications (2,5 M $) Patrimoine canadien (1,5 M $) Ville de Québec (750 000 $) Groupe Danse Partout (500 000 $) et d’autres sources de financement. Si vous souhaitez
- **linkedin_url**: https://www.linkedin.com/company/10990746/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "336, rue du Roi, Québec (Québec), G1K 2W5", "address_country": "CA", "address_url": "https://www.maisonpourladanse.ca/nous-joindre/", "address_method": "pattern", "address_quote": "les locations Coordonnées Maison pour la danse 336, rue du Roi Québec (Québec) G1K 2W5 418 476-5013 Pour les demandes d’informations et de tarifs en lien avec les cou", "emails": "info@maisonpourladanse.ca", "emails_url": "https://www.maisonpourladanse.ca/nous-joindre/", "domain": "maisonpourladanse.ca", "key": "vd:maisonpourladanse.ca", "name": "maison pour la danse de Québec", "website": "https://maisonpourladanse.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Regroupement québécois de la danse | found | REGROUPEMENT QUÉBÉCOIS DE LA DANSE |  | NEQ 1140380222 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | immatriculée | 1994-05-09 | Montréal | QC | 500-1450 rue City Councillors, Montréal (Québec), H3A2E6 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
_none_

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:9834ceed0e69997d",
 "ap_contact_team": {
  "emails": [
   "info@quebecdanse.org",
   "administration@quebecdanse.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@quebecdanse.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.quebecdanse.org/",
    "quote": "membre Réseaux sociaux Coordonnées 1450,rue City Councillors, bureau 500 Montréal (Québec) H3A 2E6 Voir la carte Téléphone: (514) 849-4003 info@quebecdanse.org Langue English Français Le RQD reconnaît que nous sommes situés en territoire non-cédé de la nation Kanien'kehá:ka, gardienne des",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "quebecdanse.org",
    "task_id": "CL-LD-23332"
   },
   {
    "email": "administration@quebecdanse.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.quebecdanse.org/a-propos/contact/",
    "quote": "lass=\"desc\">Contact pour membres corporatifs et individuels - Poste 223</div> </a> <a class=\"m-card-vertical is-membre-comite\" href=\"mailto:administration@quebecdanse.org\"> <div> <div class=\"image lazyload\" style=\"background-image:inherit;\" data-bg-image=\"url(https://www.quebecdanse.org/wp",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "quebecdanse.org",
    "task_id": "CL-LD-23332"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of quebecdanse.org (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of quebecdanse.org (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

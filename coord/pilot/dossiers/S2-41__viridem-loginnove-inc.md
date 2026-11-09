# S2-41 — Viridem · Loginnove inc ⇄ Loginnove

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Viridem · Loginnove inc — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1
SUBMIT TO: info@viridem.ca (general mailbox, confirmed by the referee) | invoice portal: https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: LOGINNOVE INC. (as registered: Canada's Business Registries, QC 1169574309, 2026-11-08) — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 | GST/HST 837621176 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-04-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1169574309
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-gu
DESCRIPTION: Viridem · Loginnove inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / 
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 44
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Viridem · Loginnove inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Loginnove | published by: the Canada-located vendor's own website | record: https://www.loginnove.ca | vendor in Canada because: vendor located in Canada (wall)=loginnove.ca | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:db972b0591b68ca3
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Viridem · Loginnove inc
- **buyer_website**: https://viridem.ca/
- **buyer_address**: 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1
- **buyer_phone**: 8196046886 (tel: link on https://viridem.ca/)
- **buyer_contact_evidence_url**: https://viridem.ca/fr/contactez-nous
- **buyer_legal_name_as_published**: Viridem · Loginnove inc
- **buyer_logo_url**: https://viridem.ca/images/viridem-logo-full.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://linkedin.com/showcase/viridem/
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://viridem.ca/fr/contactez-nous (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_ap_cycle_published**: cycle de paiement est chroniquement en retard (mentioned on https://viridem.ca/fr)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_esignature_preference**: Signature électronique multi-niveaux, conforme et tracée (as printed on https://viridem.ca/fr, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@viridem.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://viridem.ca/fr
- **email_evidence_quote**: CA" }, "contactPoint": { "@type": "ContactPoint", "contactType": "customer service", "availableLanguage": ["French", "English"] , "email": "info@viridem.ca", "telephone": "819 604-6886" }, "sameAs": [ "https://linkedin.com/showcase/viridem/","https://facebook.com/viridem.solution", "https:
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@viridem.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://viridem.ca/fr | quote: "CA" }, "contactPoint": { "@type": "ContactPoint", "contactType": "customer service", "availableLanguage": ["French", "English"] , "email": "info@viridem.ca", "t" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-14631
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; sp=none; pct=100; ri=86400; rua=mailto:dmarc@viridem.ca
- **dmarc_record_domain**: viridem.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf.clients.secure-exchanges.com  -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-guide, re-read 2026-11-08)
- **invoice_portal_url**: https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Yooz (as printed on https://viridem.ca/fr, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-guide, re-read 2026-11-08)", "portal_url": "https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Viridem · Loginnove inc — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 ⏎ SUBMIT TO: info@viridem.ca (general mailbox, confirmed by the referee) | invoice portal: https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LOGINNOVE INC. (as registered: Canada's Business Registries, QC 1169574309, 2026-11-08) — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 | GST/HST 837621176 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-04-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1169574309 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-gu ⏎ DESCRIPTION: Viridem · Loginnove inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / 
- **invoice_card_json**: {"bill_to": {"legal_name": "Viridem · Loginnove inc", "legal_name_is_published": true, "address": "560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@viridem.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Yooz (as printed on https://viridem.ca/fr, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-guide, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "cycle de paiement est chroniquement en retard (mentioned on https://viridem.ca/fr)", "e_signature": "Signature électronique multi-niveaux, conforme et tracée (as printed on https://viridem.ca/fr, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); ch
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 59
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; payment cycle or method published (plausibility) | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: Loginnove
- **vendor_legal_name**: LOGINNOVE INC. (as registered: Canada's Business Registries, QC 1169574309, 2026-11-08)
- **vendor_trading_name**: Loginnove
- **vendor_registry_id**: 1169574309 (QC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Loginnove
- **vendor_registered_address**: Victoriaville, Québec (registered office city / province; Canada's Business Registries, QC 1169574309, 2026-11-08)
- **vendor_neq**: 1169574309 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_legal_form**: Société par actions ou compagnie (Canada's Business Registries, QC 1169574309, 2026-11-08)
- **vendor_address**: 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1
- **vendor_country_basis**: vendor located in Canada (wall)=loginnove.ca
- **vendor_bn9**: 837621176 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-04-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 837621176RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://loginnove.ca
- **vendor_emails**: info@viridem.ca
- **vendor_phone**: 8196046886 (tel: link on https://loginnove.ca/)
- **vendor_contact_evidence_url**: https://www.viridem.ca/fr/contactez-nous
- **vendor_logo_url**: https://www.viridem.ca/images/viridem-logo-full.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://linkedin.com/showcase/viridem/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 1169574309 (QC) status Active (Canada's Business Registries, QC 1169574309, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2013-10-28; phone / role e-mails / logo: the vendor's own site, https://www.viridem.ca/fr/contactez-nous (tools/org_contacts.py, org_extras.py); website: https://loginnove.ca (site answers); NEQ: 1169574309 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, QC 1169574309, 2026-11-08)
- **vendor_incorporation_date**: 2013-10-28
- **vendor_years_in_business**: 13.0 (since 2013-10-28, registry date)
- **vendor_founded**: 2013 (schema.org JSON-LD foundingDate on https://www.viridem.ca/fr/historique)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.loginnove.ca
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 837621176RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Viridem · Loginnove inc — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 ⏎ SUBMIT TO: info@viridem.ca (general mailbox, confirmed by the referee) | invoice portal: https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: LOGINNOVE INC. (as registered: Canada's Business Registries, QC 1169574309, 2026-11-08) — 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 | GST/HST 837621176 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-04-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1169574309 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-gu ⏎ DESCRIPTION: Viridem · Loginnove inc (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / 
- **invoice_card_json**: {"bill_to": {"legal_name": "Viridem · Loginnove inc", "legal_name_is_published": true, "address": "560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@viridem.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "https://viridem.ca/en/blog-yooz-alternative-canada-honest-ap-automation-comparison — Yooz", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Yooz (as printed on https://viridem.ca/fr, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "net 30 (as printed on https://viridem.ca/en/blog-accounts-payable-automation-canada-complete-2026-guide, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "cycle de paiement est chroniquement en retard (mentioned on https://viridem.ca/fr)", "e_signature": "Signature électronique multi-niveaux, conforme et tracée (as printed on https://viridem.ca/fr, re-read 2026-11-08)"}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); ch
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 59
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known; payment cycle or method published (plausibility) | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@viridem.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://viridem.ca/fr", "quote: \"CA\" }, \"contactPoint\": { \"@type\": \"ContactPoint\", \"contactType\": \"customer service\", \"availableLanguage\": [\"French\", \"English\"] , \"email\": \"info@viridem.ca\", \"t\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-14631"], "buyer_facts": ["address and phone: the buyer's own site, https://viridem.ca/fr/contactez-nous (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 1169574309 (QC) status Active (Canada's Business Registries, QC 1169574309, 2026-11-08) (scripts/enrichment_*

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://viridem.ca/fr | 2026-11-08 | ok |  |  | Yooz |  |  |  | SAP, Acomba, Microsoft Dynamics |  |  |

## Buyer site facts (org_extras, viridem.ca)
- **status**: ok
- **pages**: 5
- **language**: fr
- **legal_name**: Viridem · Loginnove inc
- **legal_name_url**: https://viridem.ca/fr
- **legal_name_quote**: ville (Québec) G6P 1T1 Nous contacter → Légal Confidentialité Témoins Paramètres des témoins © 2025 Viridem · Loginnove inc. · 560, rue Notre-Dame Ouest, Victoriaville (QC) G6P 1T1 Nous respectons votre vie privée Ce site u
- **logo_url**: https://viridem.ca/images/viridem-logo-full.png
- **logo_basis**: logo image on the site
- **domain**: viridem.ca
- **key**: lead:db972b0591b68ca3
- **name**: Viridem · Loginnove inc
- **website**: https://viridem.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Viridem
- **jsonld_legal_name**: Loginnove inc.
- **jsonld_alternate_name**: Viridem inc.; Viridem Solutions
- **jsonld_logo**: https://viridem.ca/images/viridem-logo-full.png
- **jsonld_url**: https://viridem.ca
- **jsonld_founding_date**: 2013
- **jsonld_same_as**: https://linkedin.com/showcase/viridem/; https://facebook.com/viridem.solution; https://jebatimatech.com/solutions/viridem/; https://www.acomba.com/solutions/chercher-un-logiciel-compatible/logiciel/viridem
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [ { "@type": "Question", "name": "Qu'est-ce que Viridem ?", "acceptedAnswer": { "@type": "Answer", "text": "Viridem est un logiciel québécois propriétaire d'automatisation des comptes payables et des tâches administratives, dévelo
- **jsonld_page**: https://viridem.ca/fr
- **legal_name_stated**: Viridem sont régis par le droit de la Province de Québec
- **legal_name_stated_url**: https://viridem.ca/fr/conditions-utilisation
- **legal_name_stated_quote**: s et litiges Les présentes modalités et conditions et tout litige qui pourrait naître entre vous et Viridem sont régis par le droit de la Province de Québec, sans égard à ses règles de conflit de lois, et par les lois du Canada qui s'y appliquent et tout l
- **mentions**: {'payment_method': {'text': 'dépôt direct', 'url': 'https://viridem.ca/fr', 'quote': "nne Le parcours d'un document chez Viridem 01 Réception Capture multicanal, courriel, numérisation, dépôt direct. 02 Capture Lecture intelligente OCR + IA, extraction des données clés. 03 Flux de travail Routage"}, 'esignature': {'text': 'Signature électronique multi-niveaux, conforme et tracée', 'url': 'https://viridem.ca/fr', 'quote': "éception). 05 Validation Revue des exceptions par votre équipe, décision en un clic. 06 Approbation Signature électronique multi-niveaux, conforme et tracée. 07 Archivage Écr
- **linkedin_url**: https://linkedin.com/showcase/viridem/
- **tel_links**: 8196046886

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1", "address_country": "CA", "address_url": "https://viridem.ca/fr/contactez-nous", "address_method": "pattern", "address_quote": "enaires ERP Loginnove Contact 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 Nous contacter → Légal Confidentialité Témoins Paramètres des témoins © 2025 Vi", "emails": "info@viridem.ca", "emails_url": "https://viridem.ca/fr/contactez-nous", "domain": "viridem.ca", "key": "lead:db972b0591b68ca3", "name": "viridem.ca", "website": "https://viridem.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, loginnove.ca)
- **status**: ok
- **pages**: 5
- **language**: fr
- **legal_name**: Viridem · Loginnove inc
- **legal_name_url**: https://www.viridem.ca/fr/historique
- **legal_name_quote**: ville (Québec) G6P 1T1 Nous contacter → Légal Confidentialité Témoins Paramètres des témoins © 2025 Viridem · Loginnove inc. · 560, rue Notre-Dame Ouest, Victoriaville (QC) G6P 1T1 Nous respectons votre vie privée Ce site u
- **logo_url**: https://www.viridem.ca/images/viridem-logo-full.png
- **logo_basis**: logo image on the site
- **domain**: loginnove.ca
- **key**: vendor:Loginnove
- **name**: Loginnove
- **website**: https://loginnove.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Viridem
- **jsonld_legal_name**: Loginnove inc.
- **jsonld_alternate_name**: Viridem inc.; Viridem Solutions
- **jsonld_logo**: https://viridem.ca/images/viridem-logo-full.png
- **jsonld_url**: https://viridem.ca
- **jsonld_founding_date**: 2013
- **jsonld_same_as**: https://linkedin.com/showcase/viridem/; https://facebook.com/viridem.solution; https://jebatimatech.com/solutions/viridem/; https://www.acomba.com/solutions/chercher-un-logiciel-compatible/logiciel/viridem
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "AboutPage", "@id": "http://www.viridem.ca/fr/historique#about", "name": "Historique", "url": "http://www.viridem.ca/fr/historique", "publisher": { "@id": "https://viridem.ca/#organization" }, "mainEntity": { "@id": "https://viridem.ca/#organization" } }
- **jsonld_page**: https://www.viridem.ca/fr/historique
- **legal_name_stated**: Viridem sont régis par le droit de la Province de Québec
- **legal_name_stated_url**: https://www.viridem.ca/fr/conditions-utilisation
- **legal_name_stated_quote**: s et litiges Les présentes modalités et conditions et tout litige qui pourrait naître entre vous et Viridem sont régis par le droit de la Province de Québec, sans égard à ses règles de conflit de lois, et par les lois du Canada qui s'y appliquent et tout l
- **mentions**: {'payment_method': {'text': 'interactions aux fins de consultation et, dans certains cas, de mise à jour', 'url': 'https://www.viridem.ca/fr/privacy', 'quote': 'puis-je consulter ? Viridem donne accès à de nombreux renseignements concernant votre compte et vos interactions aux fins de consultation et, dans certains cas, de mise à jour. Cette liste évoluera au fur et à mesure que Viridem évolue. L’accès aux documents d'}}
- **linkedin_url**: https://linkedin.com/showcase/viridem/
- **tel_links**: 8196046886

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1", "address_country": "CA", "address_url": "https://www.viridem.ca/fr/contactez-nous", "address_method": "pattern", "address_quote": "enaires ERP Loginnove Contact 560, rue Notre-Dame Ouest, Victoriaville (Québec) G6P 1T1 Nous contacter → Légal Confidentialité Témoins Paramètres des témoins © 2025 Vi", "emails": "info@viridem.ca", "emails_url": "https://www.viridem.ca/fr/contactez-nous", "domain": "loginnove.ca", "key": "vd:loginnove.ca", "name": "Loginnove", "website": "https://loginnove.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Viridem · Loginnove inc | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Viridem%20%C2%B7%20Loginnove%20inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Viridem · Loginnove inc |  |  |  |  |  |  |  |  |  |  |
| v | Viridem · Loginnove inc |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:db972b0591b68ca3",
 "ap_contact_team": {
  "emails": [
   "info@viridem.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@viridem.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://viridem.ca/fr",
    "quote": "CA\" }, \"contactPoint\": { \"@type\": \"ContactPoint\", \"contactType\": \"customer service\", \"availableLanguage\": [\"French\", \"English\"] , \"email\": \"info@viridem.ca\", \"telephone\": \"819 604-6886\" }, \"sameAs\": [ \"https://linkedin.com/showcase/viridem/\",\"https://facebook.com/viridem.solution\", \"https:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "viridem.ca",
    "task_id": "CL-LD-14631"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of viridem.ca (40 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:20169963:loginnove-inc | Ville de Saint-Lambert | Fourniture d'une solution de paiement de factures automatisée | 98839.58 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d67554ac-0c53-4f3a-89ed-d38b03588f7f |

## Open questions for hand research (layer 2)

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

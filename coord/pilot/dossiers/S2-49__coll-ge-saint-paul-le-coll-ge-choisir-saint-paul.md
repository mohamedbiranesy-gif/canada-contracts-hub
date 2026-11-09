# S2-49 — Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi ⇄ inferred: Hydro-Québec

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi — 235, rue Sainte-Anne, Varennes (Québec) J3X 1P9
SUBMIT TO: finance@college-st-paul.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi (university / college, QC) — inferred: no record; the organisation's
```

## Relationship
- **rank_group**: I3
- **data_quality_score**: 48
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: HIGH (statutory or sole-provider relationship for this type of organisation)
- **relationship_detail**: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi (university / college, QC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Hydro-Québec | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4' | status rule: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Québec (province from its domain college-st-paul.qc.ca); Hydro-Québec holds the 
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: crux:college-st-paul.qc.ca
- **tier**: I
- **grade**: 3

## Buyer
- **buyer**: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi
- **buyer_website**: https://college-st-paul.qc.ca
- **buyer_address**: 235, rue Sainte-Anne, Varennes (Québec) J3X 1P9
- **buyer_phone**: 450 652-2941
- **buyer_contact_evidence_url**: https://college-st-paul.qc.ca/nous-joindre/
- **buyer_legal_name_as_published**: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi
- **buyer_logo_url**: https://college-st-paul.qc.ca/wp-content/uploads/2023/08/CollegeSaintPaul_logo_mini-e1744385633540.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/college-saint-paul/
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://college-st-paul.qc.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@college-st-paul.qc.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://college-st-paul.qc.ca/bottin-du-personnel/
- **email_evidence_quote**: Poste: 2135 Rivera Gonzalez, Scarlett Technicienne à la comptabilité finance@college-st-paul.qc.ca Poste: 2133 Rochefort, Valérie Agente de bureau, RH vrochefort@college-st-paul.qc.ca Royer, Marie-Claude Technicienne en
- **email_evidence_context**: a Piché, Nancy Technicienne en éducation spécialisée npiche@college-st-paul.qc.ca Poste: 2128 Provost, Jennifer Technicienne en éducation spécialisée jprovost@college-st-paul.qc.ca Poste: 2135 Rivera Gonzalez, Scarlett Technicienne à la comptabilité finance@college-st-paul.qc.ca Poste: 2133 Rochefort, Valérie Agente de bureau, RH vrochefort@college-st-paul.qc.ca Royer, Marie-Claude Technicienne en organisation scolaire mcroyer@college-st-paul.qc.ca Poste: 2107 Savaria, Marielle Surveillante d’élèves msavaria@college-st-paul (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@college-st-paul.qc.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://college-st-paul.qc.ca/bottin-du-personnel/ | quote: "Poste: 2135 Rivera Gonzalez, Scarlett Technicienne à la comptabilité finance@college-st-paul.qc.ca Poste: 2133 Rochefort, Valérie Agente de bureau, RH vrochefor" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-006297
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine;
- **dmarc_record_domain**: college-st-paul.qc.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:md02.com ip4:206.41.88.170 ip4:206.41.88.171 ip4:173.46.148.17 ip4:64.187.185.214 include:spf.protection.outlook.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Valérie Agente (Technicienne à la comptabilité) (as printed by the organisation on its own accounts-payable page (as printed on https://college-st-paul.qc.ca/bottin-du-personnel/, re-read 2026-11-08))
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi — 235, rue Sainte-Anne, Varennes (Québec) J3X 1P9 ⏎ SUBMIT TO: finance@college-st-paul.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi (university / college, QC) — inferred: no record; the organisation's
- **invoice_card_json**: {"bill_to": {"legal_name": "Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi", "legal_name_is_published": true, "address": "235, rue Sainte-Anne, Varennes (Québec) J3X 1P9", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "finance@college-st-paul.qc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Hydro-Québec", "bn9": "119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroqueb
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: fr/en
- **template_language**: fr (Québec buyer; French first)

## Vendor
- **vendor**: inferred: Hydro-Québec
- **vendor_address**: 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4
- **vendor_country_basis**: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4'
- **vendor_bn9**: 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)
- **vendor_website**: https://www.hydroquebec.com
- **vendor_phone**: +1-888-858-7927
- **vendor_contact_evidence_url**: https://www.hydroquebec.com/nous-joindre/
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.hydroquebec.com/nous-joindre/ (tools/org_contacts.py, org_extras.py); website: https://www.hydroquebec.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html)

## Contract
- **contract_status**: inferred relationship (no record): high confidence; the buyer is an institution (school, college, university, health or government body) in Québec (province from its domain college-st-paul.qc.ca); Hydro-Québec holds the exclusive right to distribute electricity in Québec outside the 9 municipal networks (Alma, Amos, Baie-Comeau, Coaticook, Joliette, Magog, Saguenay-Jonquière, Sherbrooke, Westmount) and the Saint-Jean-Baptiste-de-Rouville co-op (Act respecting the Régie de l'énergie); it pays electricity for the buildings it operates
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi — 235, rue Sainte-Anne, Varennes (Québec) J3X 1P9 ⏎ SUBMIT TO: finance@college-st-paul.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi (university / college, QC) — inferred: no record; the organisation's
- **invoice_card_json**: {"bill_to": {"legal_name": "Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi", "legal_name_is_published": true, "address": "235, rue Sainte-Anne, Varennes (Québec) J3X 1P9", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "finance@college-st-paul.qc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Hydro-Québec", "bn9": "119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroqueb
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@college-st-paul.qc.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://college-st-paul.qc.ca/bottin-du-personnel/", "quote: \"Poste: 2135 Rivera Gonzalez, Scarlett Technicienne à la comptabilité finance@college-st-paul.qc.ca Poste: 2133 Rochefort, Valérie Agente de bureau, RH vrochefor\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-006297"], "buyer_facts": ["address and phone: the buyer's own site, https://college-st-paul.qc.ca/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://college-st-paul.qc.ca/bottin-du-personnel/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, college-st-paul.qc.ca)
- **status**: ok
- **pages**: 5
- **language**: fr
- **legal_name**: Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Vi
- **legal_name_url**: https://college-st-paul.qc.ca/
- **legal_name_quote**: es secondaires (DES). Politique de confidentialité Nétiquette Protecteur national de l'élève © 2026 Collège Saint-Paul Le Collège Choisir Saint-Paul À propos Historique Visite virtuelle Administration Équipe de direction Emplois Conseil d’administration En savoir plus Co
- **logo_url**: https://college-st-paul.qc.ca/wp-content/uploads/2023/08/CollegeSaintPaul_logo_mini-e1744385633540.png
- **logo_basis**: logo image in the site header
- **domain**: college-st-paul.qc.ca
- **key**: crux:college-st-paul.qc.ca
- **name**: college-st-paul.qc.ca
- **website**: https://college-st-paul.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Collège Saint-Paul
- **jsonld_logo**: https://college-st-paul.qc.ca/wp-content/uploads/2023/08/CollegeSaintPaul_logo_mini.png
- **jsonld_url**: https://college-st-paul.qc.ca/
- **jsonld_same_as**: https://www.facebook.com/college.stpaul; https://www.instagram.com/collegesaintpaul/; https://www.linkedin.com/school/college-saint-paul/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/college-st-paul.qc.ca\/","url":"https:\/\/college-st-paul.qc.ca\/","name":"Collège Saint-Paul","isPartOf":{"@id":"https:\/\/college-st-paul.qc.ca\/#website"},"about":{"@id":"https:\/\/college-st-paul.qc.ca\/#organizatio
- **jsonld_page**: https://college-st-paul.qc.ca/
- **mentions**: {'payment_method': {'text': 'interactions positives', 'url': 'https://college-st-paul.qc.ca/a-propos/', 'quote': 'lèves de se réaliser et de contribuer à la société. Encourager des comportements respectueux et des interactions positives. Favoriser une utilisation responsable des outils technologiques et des médias sociaux. Nos valeurs'}}
- **linkedin_url**: https://www.linkedin.com/school/college-saint-paul/
- **tel_links**: 4506522941

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "235, rue Sainte-Anne, Varennes (Québec) J3X 1P9", "address_country": "CA", "address_url": "https://college-st-paul.qc.ca/nous-joindre/", "address_method": "pattern", "address_quote": "ées. 450 652-2941 info@college-st-paul.qc.ca 235, rue Sainte-Anne Varennes, Qc, J3X 1P9 Heures d’ouverture Lundi au vendredi, 8 h 30 à 16 h 30 Fermé lors des jours fér", "phone": "450 652-2941", "phone_url": "https://college-st-paul.qc.ca/nous-joindre/", "emails": "info@college-st-paul.qc.ca; secretariat@college-st-paul.qc.ca", "emails_url": "https://college-st-paul.qc.ca/nous-joindre/", "domain": "college-st-paul.qc.ca", "key": "crux:college-st-paul.qc.ca", "name": "college-st-paul.qc.ca", "website": "https://college-st-paul.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, hydroquebec.com)
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

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "75, boulevard René-Lévesque Ouest, Montréal, QC, H2Z 1A4", "address_country": "CA", "address_url": "https://www.hydroquebec.com/nous-joindre/", "address_method": "json-ld", "address_quote": "social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4 Fermé pour rénovation jusqu'en 2029 En savoir plus Sujets connexes Commentaire", "phone": "+1-888-858-7927", "phone_url": "https://www.hydroquebec.com/nous-joindre/", "domain": "hydroquebec.com", "key": "vd:hydroquebec.com", "name": "Hydro-Québec.", "website": "https://hydroquebec.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | college-st-paul.qc.ca | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=college-st-paul.qc.ca | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Hydro-Québec | Q167840 | official website on the organisation's domain (http://www.hydroquebec.com/) + name |  | Hydro-Quebec | Hydro-Québec | Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity | Crown corporation | Canada | 1944-04-14 | Hydro-Québec Building |
| v | Hydro-Québec Développement énergétique inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "crux:college-st-paul.qc.ca",
 "ap_contact_team": {
  "emails": [
   "finance@college-st-paul.qc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@college-st-paul.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://college-st-paul.qc.ca/bottin-du-personnel/",
    "quote": "Poste: 2135 Rivera Gonzalez, Scarlett Technicienne à la comptabilité finance@college-st-paul.qc.ca Poste: 2133 Rochefort, Valérie Agente de bureau, RH vrochefort@college-st-paul.qc.ca Royer, Marie-Claude Technicienne en",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "college-st-paul.qc.ca",
    "task_id": "CL-CRUX-006297"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of college-st-paul.qc.ca (9 pages, robots.txt respected), no AI, no search engine"
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

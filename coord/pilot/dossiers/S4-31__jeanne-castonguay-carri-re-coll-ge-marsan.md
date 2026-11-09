# S4-31 — Jeanne Castonguay-Carrière Collège MARSAN ⇄ inferred: Hydro-Québec

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Jeanne Castonguay-Carrière Collège MARSAN — 3536 Boul St-Laurent, Montréal, QC H2X 2V1
SUBMIT TO: info@collegemarsan.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Jeanne Castonguay-Carrière Collège MARSAN (university / college, QC) — inferred: no record; the organisation's type and province make a Cana
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 29
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: Jeanne Castonguay-Carrière Collège MARSAN (university / college, QC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Hydro-Québec | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from its domain collegemarsan.qc.ca); Hydro-Québec holds the exclusive right to distribute electricity in Québec outs
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: crux:collegemarsan.qc.ca
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Jeanne Castonguay-Carrière Collège MARSAN
- **buyer_website**: https://collegemarsan.com
- **buyer_address**: 3536 Boul St-Laurent, Montréal, QC H2X 2V1
- **buyer_contact_evidence_url**: https://collegemarsan.qc.ca/fr/contact/
- **buyer_legal_name_as_published**: Jeanne Castonguay-Carrière Collège MARSAN
- **buyer_logo_url**: https://collegemarsan.qc.ca/wp-content/plugins/ecoles-creatives-banner-0.0.2/public/images/ecoles-creatives-logo-dark.png
- **buyer_website_status**: site answers
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://collegemarsan.qc.ca/fr/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@collegemarsan.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://collegemarsan.qc.ca/fr/contact/
- **email_evidence_quote**: -call-url="" data-rtid="i5bPHTFlwzgA" data-ved="2ahUKEwjJ9_33k6_iAhVqU98KHUvlBPkQkAgoADAXegQIFxAD">(514) 525-3030</a><br /> <a href="mailto:info@collegemarsan.com">
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@collegemarsan.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03 | page: https://collegemarsan.qc.ca/fr/contact/ | quote: "-call-url="" data-rtid="i5bPHTFlwzgA" data-ved="2ahUKEwjJ9_33k6_iAhVqU98KHUvlBPkQkAgoADAXegQIFxAD">(514) 525-3030</a><br /> <a href="mailto:info@collegemarsan.c" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by self-hosted or other (collegemarsan.com) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-023592
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by self-hosted or other (collegemarsan.com)
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.collegemarsan.com; confirmed by 8.8.8.8
- **spf_policy**: no SPF record
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Jeanne Castonguay-Carrière Collège MARSAN — 3536 Boul St-Laurent, Montréal, QC H2X 2V1 ⏎ SUBMIT TO: info@collegemarsan.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Jeanne Castonguay-Carrière Collège MARSAN (university / college, QC) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Jeanne Castonguay-Carrière Collège MARSAN", "legal_name_is_published": true, "address": "3536 Boul St-Laurent, Montréal, QC H2X 2V1", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@collegemarsan.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Hydro-Québec", "bn9": "119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)", "
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: fr
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
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from its domain collegemarsan.qc.ca); Hydro-Québec holds the exclusive right to distribute electricity in Québec outside the 9 municipal networks (Alma, Amos, Baie-Comeau, Coaticook, Joliette, Magog, Saguenay-Jonquière, Sherbrooke, Westmount) and the Saint-Jean-Baptiste-de-Rouville co-op (Act respecting the Régie de l'énergie); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
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
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Jeanne Castonguay-Carrière Collège MARSAN — 3536 Boul St-Laurent, Montréal, QC H2X 2V1 ⏎ SUBMIT TO: info@collegemarsan.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Jeanne Castonguay-Carrière Collège MARSAN (university / college, QC) — inferred: no record; the organisation's type and province make a Cana
- **invoice_card_json**: {"bill_to": {"legal_name": "Jeanne Castonguay-Carrière Collège MARSAN", "legal_name_is_published": true, "address": "3536 Boul St-Laurent, Montréal, QC H2X 2V1", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@collegemarsan.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Hydro-Québec", "bn9": "119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)", "
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@collegemarsan.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-03", "page: https://collegemarsan.qc.ca/fr/contact/", "quote: \"-call-url=\"\" data-rtid=\"i5bPHTFlwzgA\" data-ved=\"2ahUKEwjJ9_33k6_iAhVqU98KHUvlBPkQkAgoADAXegQIFxAD\">(514) 525-3030</a><br /> <a href=\"mailto:info@collegemarsan.c\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by self-hosted or other (collegemarsan.com)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRUX-023592"], "buyer_facts": ["address and phone: the buyer's own site, https://collegemarsan.qc.ca/fr/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://collegemarsan.qc.ca/fr/contact/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, collegemarsan.com)
- **status**: ok
- **pages**: 3
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Collège Marsan
- **jsonld_alternate_name**: Collège Marsan
- **jsonld_logo**: https://collegemarsan.qc.ca/wp-content/uploads/2020/02/Nature-Morte-2-2.jpg
- **jsonld_url**: https://collegemarsan.qc.ca/fr
- **jsonld_same_as**: https://www.facebook.com/CollegeMarsan/; https://www.instagram.com/collegemarsan/
- **jsonld_quote**: {"@context":"https://schema.org","@type":"LocalBusiness","image":"https://collegemarsan.qc.ca/wp-content/uploads/2020/02/Nature-Morte-2-2.jpg","@id":"https://collegemarsan.qc.ca/fr/#organization","name":"Collège Marsan","telephone":"(514) 525-3030","priceRange":"c.dumont","address":{"@type":"PostalA
- **jsonld_page**: https://collegemarsan.qc.ca/fr/
- **language**: fr
- **logo_url**: https://collegemarsan.qc.ca/wp-content/plugins/ecoles-creatives-banner-0.0.2/public/images/ecoles-creatives-logo-dark.png
- **logo_basis**: logo image in the site header
- **legal_name**: Jeanne Castonguay-Carrière Collège MARSAN
- **legal_name_url**: https://collegemarsan.qc.ca/fr/a-propos/
- **legal_name_quote**: tivités, tout en respectant à la fois leurs identités artistiques et les impératifs de production. ©Jeanne Castonguay-Carrière Collège MARSAN – Montréal MARSAN ne compte que des professionnels parmi ses enseignants. Ces praticiens de la créa
- **domain**: collegemarsan.com
- **key**: crux:collegemarsan.qc.ca
- **name**: collegemarsan.qc.ca
- **website**: https://collegemarsan.com/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "3536 Boul St-Laurent, Montréal, QC H2X 2V1", "address_country": "CA", "address_url": "https://collegemarsan.qc.ca/fr/contact/", "address_method": "pattern", "address_quote": "lus brefs délais. Coordonnées Collège Marsan 3536 Boul St-Laurent, Montréal, QC H2X 2V1 ➝ Ouvrir dans Google Maps Tél. (514) 525-3030 info@collegemarsan.qc.ca Formulai", "emails": "info@collegemarsan.com; info@collegemarsan.qc.ca", "emails_url": "https://collegemarsan.qc.ca/fr/contact/", "domain": "collegemarsan.com", "key": "crux:collegemarsan.qc.ca", "name": "collegemarsan.qc.ca", "website": "https://collegemarsan.com/", "kind": "buyer", "date": "2026-11-04"}

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
| buyer | Jeanne Castonguay-Carrière Collège MARSAN | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Jeanne%20Castonguay-Carri%C3%A8re%20Coll%C3%A8ge%20MARSAN | 2026-11-08 |

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
 "buyer_key": "crux:collegemarsan.qc.ca",
 "ap_contact_team": {
  "emails": [
   "info@collegemarsan.com",
   "info@collegemarsan.qc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@collegemarsan.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://collegemarsan.qc.ca/fr/contact/",
    "quote": "-call-url=\"\" data-rtid=\"i5bPHTFlwzgA\" data-ved=\"2ahUKEwjJ9_33k6_iAhVqU98KHUvlBPkQkAgoADAXegQIFxAD\">(514) 525-3030</a><br /> <a href=\"mailto:info@collegemarsan.com\">",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "collegemarsan.qc.ca",
    "task_id": "CL-CRUX-023592"
   },
   {
    "email": "info@collegemarsan.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://collegemarsan.qc.ca/fr/contact/",
    "quote": "les plus brefs délais. Coordonnées Collège Marsan 3536 Boul St-Laurent, Montréal, QC H2X 2V1 ➝ Ouvrir dans Google Maps Tél. (514) 525-3030 info@collegemarsan.qc.ca Formulaire de contact Nom * Prénom * E-mail * Téléphone Message * Envoyer Réalisez rapidement votre rêve. Débutez vos études",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "collegemarsan.qc.ca",
    "task_id": "CL-CRUX-023592"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of collegemarsan.qc.ca (12 pages, robots.txt respected), no AI, no search engine",
  "site crawl of collegemarsan.qc.ca (12 pages, robots.txt respected), no AI, no search engine"
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

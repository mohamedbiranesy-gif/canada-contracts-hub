# S4-44 — Factero Advisory Services ⇄ inferred: Hydro-Québec

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite) — 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr)
SUBMIT TO: info@factero.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Factero Advisory Services (government ministry / agency, QC) — inferred: no record; the organisation's type and province make a Canadian sup
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: Factero Advisory Services (government ministry / agency, QC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Hydro-Québec | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from the postal code on its own page (J2W 1C9)); Hydro-Québec holds the exclusive right to distribute electricity in 
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: wd:Q141376718
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: Factero Advisory Services
- **buyer_website**: https://factero.ca
- **buyer_address**: 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr)
- **buyer_phone**: +15145567795 (schema.org JSON-LD telephone on https://factero.ca/fr)
- **buyer_contact_evidence_url**: https://factero.ca/fr/contactus
- **buyer_legal_name_as_published**: Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite)
- **buyer_logo_url**: https://factero.ca/public/images/factero_logo_dark_small.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/factero/
- **buyer_type**: government ministry / agency
- **buyer_sector**: government: provincial / federal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q141376718; business; consulting company
- **buyer_founded**: 2022-05-25 (Wikidata Q141376718, official website on the organisation's domain (https://factero.ca) + name; 2026-11-08)
- **buyer_employees**: 10 (Wikidata Q141376718, official website on the organisation's domain (https://factero.ca) + name; 2026-11-08)
- **buyer_legal_form**: Quebec business corporation (Wikidata Q141376718, official website on the organisation's domain (https://factero.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://factero.ca/fr/contactus (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@factero.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://factero.ca/fr
- **email_evidence_quote**: te d'indépendance Trust Center Notre équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) 2022-2026 Factero, Tous droits réservés. Site web par Factero: contact . Design par Marie Longpré: contact . -->
- **email_evidence_context**: uriser votre avenir numérique. Réserver un appel Contact Prendre rendez-vous Politique de confidentialité Charte d'indépendance Trust Center Notre équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) 2022-2026 Factero, Tous droits réservés. Site web par Factero: contact . Design par Marie Longpré: contact . --> (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@factero.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://factero.ca/fr | quote: "te d'indépendance Trust Center Notre équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (factero-ca.r-v1.mx.microsoft) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-026080
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (factero-ca.r-v1.mx.microsoft)
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; adkim=s; aspf=s; rua=mailto:0bb3829c5bba4f6981a3c2fe82d6a2d2@dmarc-reports.cloudflare.net,mailto:postmaster@factero.ca; ruf=mailto:postmaster@factero.ca; fo=1
- **dmarc_record_domain**: factero.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com -all
- **mta_sts**: yes (v=STSv1; id=20260805T232123Z)
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:tlsrpt@factero.ca)
- **bimi**: yes (v=BIMI1; l=https://factero.ca/public/images/bimi_logo.svg; a=;)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite) — 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr) ⏎ SUBMIT TO: info@factero.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Factero Advisory Services (government ministry / agency, QC) — inferred: no record; the organisation's type and province make a Canadian sup
- **invoice_card_json**: {"bill_to": {"legal_name": "Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite)", "legal_name_is_published": true, "address": "900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@factero.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": 
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

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
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from the postal code on its own page (J2W 1C9)); Hydro-Québec holds the exclusive right to distribute electricity in Québec outside the 9 municipal networks (Alma, Amos, Baie-Comeau, Coaticook, Joliette, Magog, Saguenay-Jonquière, Sherbrooke, Westmount) and the Saint-Jean-Baptiste-de-Rouville co-op (Act respecting the Régie de l'énergie); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The governments of all the participating provinces, as well as Quebec, British Columbia and Nunavut, have agreed to use the pay and rebate model. Therefore, their government departments and all of their Crown agents will pay the GST/HST on their purchases"); derived from buyer type and province, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite) — 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr) ⏎ SUBMIT TO: info@factero.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-ag | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Factero Advisory Services (government ministry / agency, QC) — inferred: no record; the organisation's type and province make a Canadian sup
- **invoice_card_json**: {"bill_to": {"legal_name": "Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (stated on https://factero.ca/fr/confidentialite)", "legal_name_is_published": true, "address": "900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA (schema.org JSON-LD PostalAddress on https://factero.ca/fr)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@factero.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: pays GST/HST on purchases (pay-and-rebate model): charge GST/HST on the invoice — GST/HST Memorandum 18-2 para. 23 (https://www.canada.ca/en/revenue-agency/serv", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)", "vendor_qst": ""}, "vendor_identity": 
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@factero.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://factero.ca/fr", "quote: \"te d'indépendance Trust Center Notre équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by self-hosted or other (factero-ca.r-v1.mx.microsoft)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-026080"], "buyer_facts": ["address and phone: the buyer's own site, https://factero.ca/fr/contactus (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "phone / role e-mails / logo: the vendor's own site, https://www.hydroquebec.com/nous-

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://factero.ca/fr | 2026-11-08 | ok |  |  |  | +1 (514) 556-7795 |  |  |  |  |  |

## Buyer site facts (org_extras, factero.ca)
- **status**: ok
- **pages**: 4
- **language**: fr
- **logo_url**: https://factero.ca/public/images/factero_logo_dark_small.svg
- **logo_basis**: logo image in the site header
- **domain**: factero.ca
- **key**: wd:Q141376718
- **name**: Factero Advisory Services
- **website**: https://factero.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Factero
- **jsonld_legal_name**: 9467-8711 Quebec inc.
- **jsonld_alternate_name**: Factero
- **jsonld_address**: 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9, CA
- **jsonld_phone**: +15145567795
- **jsonld_email**: info@factero.ca
- **jsonld_logo**: https://factero.ca/public/images/logo_seo.png://
- **jsonld_url**: https://factero.ca://
- **jsonld_naics**: 541512
- **jsonld_same_as**: https://www.linkedin.com/company/factero/; https://www.facebook.com/profile.php?id=61586515747682; https://share.google/MgSjrRgtfhAVovCGg
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://factero.ca/#organization://", "name": "Factero", "description": "Cabinet de conseil indépendant en gouvernance TI et cybersécurité desservant les municipalités et PME du Québec, de l'Ontario et du Nouveau-Brun
- **jsonld_page**: https://factero.ca/fr
- **legal_name_stated**: Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero
- **legal_name_stated_url**: https://factero.ca/fr/confidentialite
- **legal_name_stated_quote**: applicable: Province de Québec Langue English | Français --> Afficher la table des matières --> 1. Qui sommes-nous 9467-8711 Québec inc., exploitant l'entreprise sous le nom Factero (ci-après « nous », « notre » ou « nos »), offre des services exclusivement B2B, incluant le consei
- **mentions**: {'payment_method': {'text': 'interaction avec nous, nous pouvons recueillir les catégories suivantes de renseignemen', 'url': 'https://factero.ca/fr/confidentialite', 'quote': "Québec, tel qu'exigé par la Loi. 4. Renseignements que nous recueillons Selon le contexte de votre interaction avec nous, nous pouvons recueillir les catégories suivantes de renseignements personnels : Coordonnées professionnelles Nom, organisation, titre ou"}}
- **linkedin_url**: https://www.linkedin.com/company/factero/
- **tel_links**: +15145567795

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu, QC, J2W 1C9", "address_country": "CA", "address_url": "https://factero.ca/fr/contactus", "address_method": "json-ld", "address_quote": "re équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) 2022-2026 Factero, Tous droits réservés.", "phone": "+15145567795", "phone_url": "https://factero.ca/fr/contactus", "emails": "info@factero.ca", "emails_url": "https://factero.ca/fr/contactus", "domain": "factero.ca", "key": "wd:Q141376718", "name": "Factero Advisory Services", "website": "https://factero.ca/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Hydro-Québec | Q167840 | official website on the organisation's domain (http://www.hydroquebec.com/) + name |  | Hydro-Quebec | Hydro-Québec | Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity | Crown corporation | Canada | 1944-04-14 | Hydro-Québec Building |
| b | Factero Advisory Services | Q141376718 | official website on the organisation's domain (https://factero.ca) + name |  | Factero Advisory Services | Services Conseils Factero | business; consulting company | Quebec business corporation | Canada | 2022-05-25 | Saint-Jean-sur-Richelieu |
| v | Hydro-Québec Développement énergétique inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "wd:Q141376718",
 "ap_contact_team": {
  "emails": [
   "info@factero.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@factero.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://factero.ca/fr",
    "quote": "te d'indépendance Trust Center Notre équipe À propos 900 du séminaire N, bur. 320, Saint-Jean-sur-Richelieu (QC), J2W 1C9 +1 (514) 556-7795 info@factero.ca (c) 2022-2026 Factero, Tous droits réservés. Site web par Factero: contact . Design par Marie Longpré: contact . -->",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Factero Advisory Services",
    "task_id": "CL-WD-026080"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of factero.ca (25 pages, robots.txt respected), no AI, no search engine"
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

# S3-14 — MRC de Coaticook ⇄ Collège Rivier

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/) — 102, rue Child, Coaticook, QC J1A 2B3
SUBMIT TO: info@cjecoaticook.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Réalisations - Collège Rivier
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 44
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: MRC de Coaticook (municipality / local government, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Collège Rivier | subject: Réalisations - Collège Rivier | published by: the Canada-located vendor's own website | record: https://collegerivier.com/fondation/realisations/ | vendor in Canada because: vendor located in Canada (wd)=collegerivier.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:dc0c22aa91c863ca
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: MRC de Coaticook
- **buyer_website**: https://cjecoaticook.com/
- **buyer_address**: 102, rue Child, Coaticook, QC J1A 2B3
- **buyer_phone**: 819 849-0440
- **buyer_contact_evidence_url**: https://cjecoaticook.com/nous-joindre/
- **buyer_legal_name_as_published**: MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/)
- **buyer_logo_url**: https://cjecoaticook.com/wp-content/uploads/2024/02/logo_CJECoaticook-cadre.svg
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://cjecoaticook.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@cjecoaticook.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://divanorangecoaticook.ca/
- **email_evidence_quote**: RC de Coaticook avec le fonds Vitalité. Gratitude infinie! Divan Orange, espace collaboratif 102, rue Child, Coaticook J1A 2B3 819 849-0440 info@cjecoaticook.com Facebook Instagram S'abonner Abonné Divan Orange, espace collaboratif M’inscrire Vous avez un compte WordPress.com ? Connectez-v
- **email_evidence_context**: it pu être possible sans la précieuse collaboration de la SADC de la région de Coaticook et du soutien de la MRC de Coaticook avec le fonds Vitalité. Gratitude infinie! Divan Orange, espace collaboratif 102, rue Child, Coaticook J1A 2B3 819 849-0440 info@cjecoaticook.com Facebook Instagram S'abonner Abonné Divan Orange, espace collaboratif M’inscrire Vous avez un compte WordPress.com ? Connectez-vous maintenant. Divan Orange, espace collaboratif Copier lien court Voir la publication dans le Lecteur Gérer les abonnem (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@cjecoaticook.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://divanorangecoaticook.ca/ | quote: "RC de Coaticook avec le fonds Vitalité. Gratitude infinie! Divan Orange, espace collaboratif 102, rue Child, Coaticook J1A 2B3 819 849-0440 info@cjecoaticook.co" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-OS904-002316
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.cjecoaticook.com; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 +include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/) — 102, rue Child, Coaticook, QC J1A 2B3 ⏎ SUBMIT TO: info@cjecoaticook.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Réalisations - Collège Rivier
- **invoice_card_json**: {"bill_to": {"legal_name": "MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/)", "legal_name_is_published": true, "address": "102, rue Child, Coaticook, QC J1A 2B3", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@cjecoaticook.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)", "bn9": "107621443 (recipient_business_number in the federal grants &
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
- **vendor**: Collège Rivier
- **vendor_legal_name**: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_registry_id**: NEQ 1170189659 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx
- **vendor_registered_address**: 343 rue Saint-Jacques N, Coaticook (Québec), J1A2R2 (registered address; Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_neq**: 1170189659 (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_address**: 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2
- **vendor_country_basis**: vendor located in Canada (wd)=collegerivier.com
- **vendor_bn9**: 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://collegerivier.com
- **vendor_emails**: information@collegerivier.com
- **vendor_phone**: 819 849-4833
- **vendor_contact_evidence_url**: https://collegerivier.com/nous-joindre/
- **vendor_logo_url**: https://collegerivier.com/wp-content/uploads/2017/01/logo-CollegeRivier-1.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: NEQ 1170189659 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2014-07-03; phone / role e-mails / logo: the vendor's own site, https://collegerivier.com/nous-joindre/ (tools/org_contacts.py, org_extras.py); website: https://collegerivier.com (site answers); NEQ: 1170189659 (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: immatriculée (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)
- **vendor_incorporation_date**: 2014-07-03
- **vendor_years_in_business**: 12.4 (since 2014-07-03, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Réalisations - Collège Rivier
- **contract_description**: Réalisations - Collège Rivier (the record's title; the source publishes no separate description)
- **contract_link**: https://collegerivier.com/fondation/realisations/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/) — 102, rue Child, Coaticook, QC J1A 2B3 ⏎ SUBMIT TO: info@cjecoaticook.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659 ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Réalisations - Collège Rivier
- **invoice_card_json**: {"bill_to": {"legal_name": "MRC de Coaticook (stated on https://cjecoaticook.com/a-propos/)", "legal_name_is_published": true, "address": "102, rue Child, Coaticook, QC J1A 2B3", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "info@cjecoaticook.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08)", "bn9": "107621443 (recipient_business_number in the federal grants &
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@cjecoaticook.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://divanorangecoaticook.ca/", "quote: \"RC de Coaticook avec le fonds Vitalité. Gratitude infinie! Divan Orange, espace collaboratif 102, rue Child, Coaticook J1A 2B3 819 849-0440 info@cjecoaticook.co\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-OS904-002316"], "buyer_facts": ["address and phone: the buyer's own site, https://cjecoaticook.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: NEQ 1170189659 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & contributions disclosure (recipient_business_number)",

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://divanorangecoaticook.ca/ | 2026-11-08 | ok |  |  |  | 819 849-0440 |  |  |  |  |  |

## Buyer site facts (org_extras, cjecoaticook.com)
- **status**: ok
- **pages**: 4
- **language**: fr
- **logo_url**: https://cjecoaticook.com/wp-content/uploads/2024/02/logo_CJECoaticook-cadre.svg
- **logo_basis**: logo image in the site header
- **domain**: cjecoaticook.com
- **key**: lead:dc0c22aa91c863ca
- **name**: cjecoaticook.com
- **website**: https://cjecoaticook.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Carrefour jeunesse-emploi MRC de Coaticook
- **jsonld_logo**: http://cjecoaticook.com/wp-content/uploads/2016/09/CJE_logo.jpg
- **jsonld_url**: https://cjecoaticook.com/
- **jsonld_same_as**: https://www.facebook.com/cjemrccoaticook
- **jsonld_quote**: {"@context":"http:\/\/schema.org","@type":"Organization","url":"https:\/\/cjecoaticook.com\/","sameAs":["https:\/\/www.facebook.com\/cjemrccoaticook"],"@id":"#organization","name":"Carrefour jeunesse-emploi MRC de Coaticook","logo":"http:\/\/cjecoaticook.com\/wp-content\/uploads\/2016\/09\/CJE_logo.
- **jsonld_page**: https://cjecoaticook.com/
- **legal_name_stated**: MRC de Coaticook
- **legal_name_stated_url**: https://cjecoaticook.com/a-propos/
- **legal_name_stated_quote**: À propos • Carrefour jeunesse-emploi de la MRC de Coaticook 819 849-0440 search En Prendre rendez-vous Je suis… Individu Un emploi Faire mon CV Faire une lettr
- **tel_links**: 8198490440

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "102, rue Child, Coaticook, QC J1A 2B3", "address_country": "CA", "address_url": "https://cjecoaticook.com/nous-joindre/", "address_method": "pattern", "address_quote": "ex Media 2024-12-06T11:34:33+00:00 Nos coordonnées 102, rue Child Coaticook, QC J1A 2B3 Tél. : 819 849-0440 [email protected] Heures d’ouverture Du lundi au jeudi : 8", "phone": "819 849-0440", "phone_url": "https://cjecoaticook.com/nous-joindre/", "domain": "cjecoaticook.com", "key": "vd:cjecoaticook.com", "name": "Carrefour jeunesse-emploi MRC de Coaticook", "website": "https://cjecoaticook.com/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, collegerivier.com)
- **status**: ok
- **pages**: 5
- **language**: fr
- **logo_url**: https://collegerivier.com/wp-content/uploads/2017/01/logo-CollegeRivier-1.png
- **logo_basis**: logo image in the site header
- **domain**: collegerivier.com
- **key**: vendor:Collège Rivier
- **name**: Collège Rivier
- **website**: https://collegerivier.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'Interaction avec le Collège Rivier dans les réseaux sociaux Le Collège Rivier peut vous', 'url': 'https://collegerivier.com/politique-de-confidentialite/', 'quote': 'eurs ne peuvent pas garantir la livraison des notifications, que ce soit par texto ou par courriel. Interaction avec le Collège Rivier dans les réseaux sociaux Le Collège Rivier peut vous offrir la possibilité d’interagir avec son contenu sur des applications'}}

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "343, rue St-Jacques Nord, Coaticook, QC J1A 2R2", "address_country": "CA", "address_url": "https://collegerivier.com/nous-joindre/", "address_method": "pattern", "address_quote": "Nous joindre Notre adresse Collège Rivier 343, rue St-Jacques Nord Coaticook QC J1A 2R2 Tél. : 819 849-4833 Cellulaire (après 16h): 819 238-4833 admission@collegerivie", "phone": "819 849-4833", "phone_url": "https://collegerivier.com/nous-joindre/", "emails": "information@collegerivier.com", "emails_url": "https://collegerivier.com/nous-joindre/", "domain": "collegerivier.com", "key": "vd:collegerivier.com", "name": "Collège Rivier", "website": "https://collegerivier.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | Collège Rivier |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
none
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

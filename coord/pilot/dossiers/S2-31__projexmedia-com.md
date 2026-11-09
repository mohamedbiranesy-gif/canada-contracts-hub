# S2-31 — projexmedia.com ⇄ Collège Rivier

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: 9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08) — 686, rue Sherbrooke, Magog, QC J1X 2S6
SUBMIT TO: comptabilite@projexmedia.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Réalisations - Collège Rivier
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 63
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: projexmedia.com (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Collège Rivier | subject: Réalisations - Collège Rivier | published by: the Canada-located vendor's own website | record: https://collegerivier.com/fondation/realisations/ | vendor in Canada because: vendor located in Canada (wd)=collegerivier.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:699b0f5d5928abdc
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: projexmedia.com
- **buyer_website**: https://projexmedia.com/
- **buyer_address**: 686, rue Sherbrooke, Magog, QC J1X 2S6
- **buyer_phone**: 819 933-7765
- **buyer_contact_evidence_url**: https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/
- **buyer_legal_name_as_published**: 9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08)
- **buyer_logo_url**: https://projexmedia.com/web/wp-content/uploads/2020/12/logo-ProjexMedia-white.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/projexmedia/
- **buyer_registry_id**: NEQ 1163106900 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_legal_form**: CIE (société par actions (compagnie)) (Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptabilite@projexmedia.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/
- **email_evidence_quote**: Comptabilité comptabilite@projexmedia.com Soutien technique Pour toutes demandes de soutien technique, veuillez ouvrir un ticket via notre plateforme en ligne . No
- **email_evidence_context**: 024-11-05T15:44:43-05:00 Nos experts s’occupent de votre projet Bureau Chef – Magog 686, rue Sherbrooke, Magog, QC J1X 2S6 819 933-7765 Nos départements Ventes, soumissions et comptabilité Dominic Morin 819 933-7765 info@projexmedia.com Comptabilité comptabilite@projexmedia.com Soutien technique Pour toutes demandes de soutien technique, veuillez ouvrir un ticket via notre plateforme en ligne . Notre équipe d’experts Pour commencer Et si on travaillait ensemble? Venez jaser de votre projet avec nous autour d’un bon café. N (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptabilite@projexmedia.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/ | quote: "Comptabilité comptabilite@projexmedia.com Soutien technique Pour toutes demandes de soutien technique, veuillez ouvrir un ticket via notre plateforme en ligne ." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Amazon / transactional | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-00412
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Amazon / transactional
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;pct=100;fo=1
- **dmarc_record_domain**: projexmedia.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.projexmail.com include:zcsend.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 819 933-7765 (as printed on https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "819 933-7765 (as printed on https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08) — 686, rue Sherbrooke, Magog, QC J1X 2S6 ⏎ SUBMIT TO: comptabilite@projexmedia.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Réalisations - Collège Rivier
- **invoice_card_json**: {"bill_to": {"legal_name": "9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08)", "legal_name_is_published": true, "address": "686, rue Sherbrooke, Magog, QC J1X 2S6", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@projexmedia.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open d
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
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
- **contracts_with_canadian_suppliers**: 9
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 9 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08) — 686, rue Sherbrooke, Magog, QC J1X 2S6 ⏎ SUBMIT TO: comptabilite@projexmedia.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open data), NEQ 1170189659, 2026-11-08) — 343, rue St-Jacques Nord, Coaticook, QC J1A 2R2 | GST/HST 107621443 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-06-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170189659 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Réalisations - Collège Rivier
- **invoice_card_json**: {"bill_to": {"legal_name": "9158-2361 QUÉBEC INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1163106900, 2026-11-08)", "legal_name_is_published": true, "address": "686, rue Sherbrooke, Magog, QC J1X 2S6", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@projexmedia.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "107621443RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COLLÈGE RIVIER (as registered: Registraire des entreprises du Québec (open d
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["comptabilite@projexmedia.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/", "quote: \"Comptabilité comptabilite@projexmedia.com Soutien technique Pour toutes demandes de soutien technique, veuillez ouvrir un ticket via notre plateforme en ligne .\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Amazon / transactional", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-00412"], "buyer_facts": ["address and phone: the buyer's own site, https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: NEQ 1170189659 (Registraire des entreprises du Québec (open data)) status immatriculée (Regist

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/ | 2026-11-08 | ok |  |  |  | 819 933-7765 |  |  |  |  |  |

## Buyer site facts (org_extras, projexmedia.com)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://projexmedia.com/web/wp-content/uploads/2020/12/logo-ProjexMedia-white.svg
- **logo_basis**: logo image on the site
- **domain**: projexmedia.com
- **key**: lead:699b0f5d5928abdc
- **name**: projexmedia.com
- **website**: https://projexmedia.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Projex Media
- **jsonld_logo**: https://projexmedia.com/web/wp-content/uploads/2020/12/Projex.png
- **jsonld_url**: https://projexmedia.com/web/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://projexmedia.com/web/","url":"https://projexmedia.com/web/","name":"ProjexMedia - Conception Sites Web Sherbrooke - Magog - Estrie","isPartOf":{"@id":"https://projexmedia.com/web/#website"},"about":{"@id":"https://projexmedi
- **jsonld_page**: https://projexmedia.com/web/
- **legal_name_stated**: MRC du Haut-Saint-François
- **legal_name_stated_url**: https://projexmedia.com/web/
- **legal_name_stated_quote**: Centre pour femmes immigrantes de Sherbrooke Fête du Lac des Nations Pomtech Énergie Foresta Lumina MRC du Haut-Saint-François Laser Plus Sentiers frontaliers Groupe Mégarbane Équipements Marquis CIGN FM96.7 – Radio de Coatico
- **linkedin_url**: https://www.linkedin.com/company/projexmedia/
- **tel_links**: 8199337765; 8195787654

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "686, rue Sherbrooke, Magog, QC J1X 2S6", "address_country": "CA", "address_url": "https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/", "address_method": "pattern", "address_quote": "s s’occupent de votre projet Bureau Chef – Magog 686, rue Sherbrooke, Magog, QC J1X 2S6 819 933-7765 Nos départements Ventes, soumissions et comptabilité Dominic Morin", "phone": "819 933-7765", "phone_url": "https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/", "domain": "projexmedia.com", "key": "lead:699b0f5d5928abdc", "name": "projexmedia.com", "website": "https://projexmedia.com/", "kind": "buyer", "date": "2026-11-03"}

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
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | projexmedia.com | found | 9158-2361 QUÉBEC INC. |  | NEQ 1163106900 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 2005-07-13 | Magog | QC | 686 rue Sherbrooke, Magog (Québec), J1X2S6 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | Collège Rivier |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:699b0f5d5928abdc",
 "ap_contact_team": {
  "emails": [
   "info@projexmedia.com",
   "comptabilite@projexmedia.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@projexmedia.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/",
    "quote": "– Magog 686, rue Sherbrooke, Magog, QC J1X 2S6 819 933-7765 Nos départements Ventes, soumissions et comptabilité Dominic Morin 819 933-7765 info@projexmedia.com Comptabilité",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "projexmedia.com",
    "task_id": "CL-LD-00412"
   },
   {
    "email": "comptabilite@projexmedia.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://projexmedia.com/web/contactez-nous-pour-la-conception-de-sites-web/",
    "quote": "Comptabilité comptabilite@projexmedia.com Soutien technique Pour toutes demandes de soutien technique, veuillez ouvrir un ticket via notre plateforme en ligne . No",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "projexmedia.com",
    "task_id": "CL-LD-00412"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of projexmedia.com (12 pages, robots.txt respected), no AI, no search engine",
  "site crawl of projexmedia.com (12 pages, robots.txt respected), no AI, no search engine"
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

# S3-37 — EMBLM sont régis par le droit de la Province de Québec ⇄ St-Joseph Design d'espaces

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/) — 2121, rue Berlier, Laval (QC) H7L 3M9
SUBMIT TO: info@emblm.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 1170852033, 2026-11-08) — 5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4 | GST/HST 821750569 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-09-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170852033
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Sinergix | St-Joseph Design d'Espaces
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 40
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: EMBLM sont régis par le droit de la Province de Québec (organisation (type not stated in the record), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): St-Joseph Design d'espaces | subject: Sinergix | St-Joseph Design d'Espaces | published by: the Canada-located vendor's own website | record: https://www.st-joseph.co/projet/sinergix | vendor in Canada because: vendor located in Canada (osm)=st-joseph.co | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:580e9acf560ee128
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: EMBLM sont régis par le droit de la Province de Québec
- **buyer_website**: https://emblm.com/
- **buyer_address**: 2121, rue Berlier, Laval (QC) H7L 3M9
- **buyer_phone**: 1 855 463-6256
- **buyer_contact_evidence_url**: https://emblm.com/nous-joindre/
- **buyer_legal_name_as_published**: EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/)
- **buyer_logo_url**: https://emblm.com/wp-content/uploads/2022/08/cropped-EMBLM_logo_degrade_vert_cmyk.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: http://linkedin.com/company/emblmcanada
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://emblm.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@emblm.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://emblm.com/
- **email_evidence_quote**: mblmcanada","https:\/\/www.linkedin.com\/company\/emblmcanada"],"contactPoint":[{"@type":"ContactPoint","telephone":"+18554636256","email":"info@emblm.com","contactType":"customer support"}]}</script> <link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@emblm.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://emblm.com/ | quote: "mblmcanada","https:\/\/www.linkedin.com\/company\/emblmcanada"],"contactPoint":[{"@type":"ContactPoint","telephone":"+18554636256","email":"info@emblm.com","con" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08378
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: emblm.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:dc-8e814c8572._spfm.emblm.com include:centrixmail.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/) — 2121, rue Berlier, Laval (QC) H7L 3M9 ⏎ SUBMIT TO: info@emblm.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 1170852033, 2026-11-08) — 5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4 | GST/HST 821750569 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-09-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170852033 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Sinergix | St-Joseph Design d'Espaces
- **invoice_card_json**: {"bill_to": {"legal_name": "EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/)", "legal_name_is_published": true, "address": "2121, rue Berlier, Laval (QC) H7L 3M9", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@emblm.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "821750569RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 117085
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: St-Joseph Design d'espaces
- **vendor_legal_name**: ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 1170852033, 2026-11-08)
- **vendor_registry_id**: 1170852033 (QC)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=St-Joseph%20Design%20d%27espaces
- **vendor_registered_address**: Lévis, Québec (registered office city / province; Canada's Business Registries, QC 1170852033, 2026-11-08)
- **vendor_neq**: 1170852033 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_legal_form**: Société par actions ou compagnie (Canada's Business Registries, QC 1170852033, 2026-11-08)
- **vendor_address**: 5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4
- **vendor_country_basis**: vendor located in Canada (osm)=st-joseph.co
- **vendor_bn9**: 821750569 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-09-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 821750569RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://st-joseph.co
- **vendor_emails**: info@st-joseph.co
- **vendor_phone**: 418-929-5388
- **vendor_contact_evidence_url**: https://www.st-joseph.co/a-propos
- **vendor_logo_url**: https://cdn.prod.website-files.com/645176d18b99f5d3f70427ce/645178271a94545420c10a7e_STJOSEPH-LOGO-01.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/st-joseph-design-d-espaces
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 1170852033 (QC) status Active (Canada's Business Registries, QC 1170852033, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2015-04-04; phone / role e-mails / logo: the vendor's own site, https://www.st-joseph.co/a-propos (tools/org_contacts.py, org_extras.py); website: https://st-joseph.co (site answers); NEQ: 1170852033 (Registraire des entreprises du Québec (open data), 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, QC 1170852033, 2026-11-08)
- **vendor_incorporation_date**: 2015-04-04
- **vendor_years_in_business**: 11.6 (since 2015-04-04, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Sinergix | St-Joseph Design d'Espaces
- **contract_description**: Sinergix | St-Joseph Design d'Espaces (the record's title; the source publishes no separate description)
- **contract_link**: https://www.st-joseph.co/projet/sinergix
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 821750569RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/) — 2121, rue Berlier, Laval (QC) H7L 3M9 ⏎ SUBMIT TO: info@emblm.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 1170852033, 2026-11-08) — 5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4 | GST/HST 821750569 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2024-09-26; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1170852033 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Sinergix | St-Joseph Design d'Espaces
- **invoice_card_json**: {"bill_to": {"legal_name": "EMBLM sont régis par le droit de la Province de Québec (stated on https://emblm.com/termes-et-conditions/)", "legal_name_is_published": true, "address": "2121, rue Berlier, Laval (QC) H7L 3M9", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "info@emblm.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "821750569RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ST-JOSEPH DESIGN D'ESPACES INC. (as registered: Canada's Business Registries, QC 117085
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@emblm.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://emblm.com/", "quote: \"mblmcanada\",\"https:\\/\\/www.linkedin.com\\/company\\/emblmcanada\"],\"contactPoint\":[{\"@type\":\"ContactPoint\",\"telephone\":\"+18554636256\",\"email\":\"info@emblm.com\",\"con\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-08378"], "buyer_facts": ["address and phone: the buyer's own site, https://emblm.com/nous-joindre/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 1170852033 (QC) status Active (Canada's Business Registries, QC 1170852033, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & contributions disclosure (recipient_business_number)", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-p

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://emblm.com/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, emblm.com)
- **status**: ok
- **pages**: 5
- **language**: fr
- **legal_name**: Liens utiles Carrières Blogue Équipe Gouvernement EN
- **legal_name_url**: https://emblm.com/
- **legal_name_quote**: litiques de confidentialité et de gestion de données personnelles © EMBLM 2026 Tous droits réservés Liens utiles Carrières Blogue Équipe Gouvernement EN Contact 1 855 463-6256 (sans frais) [email protected]
- **logo_url**: https://emblm.com/wp-content/uploads/2022/08/cropped-EMBLM_logo_degrade_vert_cmyk.png
- **logo_basis**: logo image in the site header
- **domain**: emblm.com
- **key**: vendor:SOLUTIONS ZOOM INC.
- **name**: SOLUTIONS ZOOM INC.
- **website**: https://emblm.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: EMBLM
- **jsonld_alternate_name**: EMBLM
- **jsonld_logo**: https://emblm.com/wp-content/uploads/2024/03/cropped-EMBLM_logo_degrade_vert_cmyk-e1711207229895.png
- **jsonld_url**: https://emblm.com
- **jsonld_same_as**: https://www.facebook.com/emblm.canada; https://www.instagram.com/emblm.canada; https://www.youtube.com/@emblmcanada; https://www.linkedin.com/company/emblmcanada
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@type":"Organization","name":"EMBLM","url":"https:\/\/emblm.com","alternateName":"EMBLM","description":"EMBLM","logo":"https:\/\/emblm.com\/wp-content\/uploads\/2024\/03\/cropped-EMBLM_logo_degrade_vert_cmyk-e1711207229895.png","sameAs":["https:\/\/www.facebook.co
- **jsonld_page**: https://emblm.com/
- **legal_name_stated**: EMBLM sont régis par le droit de la Province de Québec
- **legal_name_stated_url**: https://emblm.com/termes-et-conditions/
- **legal_name_stated_quote**: du Québec : les présentes modalités et conditions et tout litige qui pourrait naître entre vous et EMBLM sont régis par le droit de la Province de Québec, sans égard à ses règles de conflit de lois, et par les lois du Canada qui s’y appliquent et tout l
- **linkedin_url**: http://linkedin.com/company/emblmcanada
- **tel_links**: 18554636256; 1 855 463-6256; 8198644281; 4182285745; 8193784841

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "2121, rue Berlier, Laval (QC) H7L 3M9", "address_country": "CA", "address_url": "https://emblm.com/nous-joindre/", "address_method": "pattern", "address_quote": "6h30, lundi au vendredi EMBLM | Montréal Rive-Nord 2121, rue Berlier Laval (QC) H7L 3M9 450 973-9666 1 855 463-6256 (sans frais) [email protected] Salle de montre : 8h", "phone": "1 855 463-6256", "phone_url": "https://emblm.com/nous-joindre/", "emails": "info@emblm.com", "emails_url": "https://emblm.com/", "domain": "emblm.com", "key": "vd:emblm.com", "name": "SOLUTIONS ZOOM INC.", "website": "https://emblm.com/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, st-joseph.co)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://cdn.prod.website-files.com/645176d18b99f5d3f70427ce/645178271a94545420c10a7e_STJOSEPH-LOGO-01.svg
- **logo_basis**: logo image on the site
- **domain**: st-joseph.co
- **key**: vendor:St-Joseph Design d'espaces
- **name**: St-Joseph Design d'espaces
- **website**: https://st-joseph.co/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/st-joseph-design-d-espaces
- **tel_links**: 4189295388

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4", "address_country": "CA", "address_url": "https://www.st-joseph.co/a-propos", "address_method": "pattern", "address_quote": "@st-joseph.co Téléphone 418-929-5388 Bureaux 5986 Rue Saint-Laurent, Lévis, QC, G6V 3P4 Inscrivez-vous à notre infolettre! Vous êtes maintenant inscrit! Oops! Une erre", "phone": "418-929-5388", "phone_url": "https://www.st-joseph.co/a-propos", "emails": "info@st-joseph.co", "emails_url": "https://www.st-joseph.co/a-propos", "domain": "st-joseph.co", "key": "vd:st-joseph.co", "name": "St-Joseph Design d'espaces", "website": "https://st-joseph.co/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | St-Joseph Design d'espaces |  |  |  |  |  |  |  |  |  |  |
| v | SOLUTIONS ZOOM INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:580e9acf560ee128",
 "ap_contact_team": {
  "emails": [
   "info@emblm.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@emblm.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://emblm.com/",
    "quote": "mblmcanada\",\"https:\\/\\/www.linkedin.com\\/company\\/emblmcanada\"],\"contactPoint\":[{\"@type\":\"ContactPoint\",\"telephone\":\"+18554636256\",\"email\":\"info@emblm.com\",\"contactType\":\"customer support\"}]}</script> <link rel=\"alternate\" title=\"oEmbed (JSON)\" type=\"application/json+oembed\" href=\"https://",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "emblm.com",
    "task_id": "CL-LD-08378"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of emblm.com (9 pages, robots.txt respected), no AI, no search engine"
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
| seao_quebec:1641267:st-joseph-design-d-espaces-inc | La Financière agricole du Québec | Technologue en architecture | 110000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=43594ff9-6138-44f9-922a-95e9516af4db |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

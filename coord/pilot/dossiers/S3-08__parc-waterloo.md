# S3-08 — Parc Waterloo ⇄ Soucy Aquatik inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Designed by Crystal Fountains Inc — 60 Snow Blvd., Toronto, ON, Canada, L4K 4B3
SUBMIT TO: info@crystalfountains.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Soucy Aquatik inc. — 3605 boul Wilfrid-Hamel, Québec, QC, G1P 2J4, CAN | GST/HST 134804640 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2021-10-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1178204187
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work
DESCRIPTION: Parc Waterloo – Construction de Fontaine - Soucy Aquatik
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 42
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Parc Waterloo (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Soucy Aquatik inc. | subject: Parc Waterloo – Construction de Fontaine - Soucy Aquatik | published by: the Canada-located vendor's own website | record: https://soucyaquatik.com/fr/etudes-de-cas/parc-waterloo-fontaine/ | vendor in Canada because: vendor located in Canada (stories; contract data vendor country)=soucyaquatik.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:a378feaa9e2fd613
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Parc Waterloo
- **buyer_website**: https://crystalfountains.com/
- **buyer_address**: 60 Snow Blvd., Toronto, ON, Canada, L4K 4B3
- **buyer_phone**: +1-905-660-6674
- **buyer_contact_evidence_url**: https://crystalfountains.com/contact-us/
- **buyer_legal_name_as_published**: Designed by Crystal Fountains Inc
- **buyer_logo_url**: https://crystalfountains.com/
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/crystal-fountains
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://crystalfountains.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@crystalfountains.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://crystalfountains.com/
- **email_evidence_quote**: ality": "Vaughan", "addressRegion": "Ontario", "postalCode": "L4K 4B3", "addressCountry": "CA" }, "telephone": "+1-905-660-6674", "email": "info@crystalfountains.com", "sameAs": [ "https://twitter.com/Crystal_Ftns", "https://www.linkedin.com/company/crystal-fountains", "https://www.youtube
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@crystalfountains.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://crystalfountains.com/ | quote: "ality": "Vaughan", "addressRegion": "Ontario", "postalCode": "L4K 4B3", "addressCountry": "CA" }, "telephone": "+1-905-660-6674", "email": "info@crystalfountain" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-21558
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;sp=none;pct=100;ruf=mailto:admin@crystalfountains.com;rua=mailto:admin@crystalfountains.com;ri=86400;aspf=r;adkim=r;fo=1
- **dmarc_record_domain**: crystalfountains.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:38.69.140.131  include:spf.protection.outlook.com include:relay.kinstamailservice.com include:spf.mandrillapp.com include:aspmx.pardot.com include:_spf.salesforce.com include:_spf.psm.knowbe4.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Designed by Crystal Fountains Inc — 60 Snow Blvd., Toronto, ON, Canada, L4K 4B3 ⏎ SUBMIT TO: info@crystalfountains.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Soucy Aquatik inc. — 3605 boul Wilfrid-Hamel, Québec, QC, G1P 2J4, CAN | GST/HST 134804640 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2021-10-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1178204187 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Parc Waterloo – Construction de Fontaine - Soucy Aquatik
- **invoice_card_json**: {"bill_to": {"legal_name": "Designed by Crystal Fountains Inc", "legal_name_is_published": true, "address": "60 Snow Blvd., Toronto, ON, Canada, L4K 4B3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@crystalfountains.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: \"an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor\"); applies only if this contract is an improvement under the Act", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "i
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Soucy Aquatik inc.
- **vendor_legal_name**: Soucy Aquatik inc.
- **vendor_trading_name**: Soucy Aquatik (schema.org alternateName on the vendor's site: https://soucyaquatik.com/)
- **vendor_registry_id**: Québec REQ (NEQ): 1178204187; NEQ 1178204187 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 3605 boul. Wilfrid-Hamel, Québec (Québec), G1P2J4
- **vendor_neq**: 1178204187 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — QUÉBEC : Loi sur les sociétés par actions (RLRQ, C. S-31.1)
- **vendor_activity_code**: CAE 4259 — Construction de piscines institutionnelles, jeux d'eau, fontaines et parc aquatiques. | secondary: Vente d'accessoires de piscines et spas.
- **vendor_employees_quebec**: De 50 à 99
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 3605 boul Wilfrid-Hamel, Québec, QC, G1P 2J4, CAN
- **vendor_country_basis**: vendor located in Canada (stories; contract data vendor country)=soucyaquatik.com
- **vendor_bn9**: 134804640 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2021-10-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 134804640RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://soucyaquatik.com/
- **vendor_phone**: +1-418-781-0620
- **vendor_contact_evidence_url**: https://soucyaquatik.com/contact-us/
- **vendor_logo_url**: https://soucyaquatik.com/wp-content/uploads/2022/12/OG-global-img.jpg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/soucyaquatik/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: Québec REQ (NEQ): 1178204187; NEQ 1178204187 (Registraire des entreprises du Québec (open data)) status Québec REQ (NEQ): Immatriculée (2022-11-24) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2022-11-01; phone / role e-mails / logo: the vendor's own site, https://soucyaquatik.com/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://soucyaquatik.com/ (site answers); NEQ: 1178204187 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2022-11-24)
- **vendor_incorporation_date**: 2022-11-01
- **vendor_years_in_business**: 4.0 (since 2022-11-01, registry date)
- **vendor_founded**: 1964 (schema.org JSON-LD foundingDate on https://soucyaquatik.com/)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Parc Waterloo – Construction de Fontaine - Soucy Aquatik
- **contract_description**: Parc Waterloo – Construction de Fontaine - Soucy Aquatik (the record's title; the source publishes no separate description)
- **contract_link**: https://soucyaquatik.com/fr/etudes-de-cas/parc-waterloo-fontaine/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 134804640RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Designed by Crystal Fountains Inc — 60 Snow Blvd., Toronto, ON, Canada, L4K 4B3 ⏎ SUBMIT TO: info@crystalfountains.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Soucy Aquatik inc. — 3605 boul Wilfrid-Hamel, Québec, QC, G1P 2J4, CAN | GST/HST 134804640 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2021-10-19; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1178204187 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Parc Waterloo – Construction de Fontaine - Soucy Aquatik
- **invoice_card_json**: {"bill_to": {"legal_name": "Designed by Crystal Fountains Inc", "legal_name_is_published": true, "address": "60 Snow Blvd., Toronto, ON, Canada, L4K 4B3", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@crystalfountains.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: \"an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor\"); applies only if this contract is an improvement under the Act", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "i
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@crystalfountains.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://crystalfountains.com/", "quote: \"ality\": \"Vaughan\", \"addressRegion\": \"Ontario\", \"postalCode\": \"L4K 4B3\", \"addressCountry\": \"CA\" }, \"telephone\": \"+1-905-660-6674\", \"email\": \"info@crystalfountain\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-21558"], "buyer_facts": ["address and phone: the buyer's own site, https://crystalfountains.com/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: Québec REQ (NEQ): 1178204187", "NEQ 1178204187 (Registraire des entreprises du Québec (open data)) status Québec REQ (NEQ): Immatriculée (2022-11-24) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & contributions disc

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://crystalfountains.com/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, crystalfountains.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Designed by Crystal Fountains Inc
- **legal_name_url**: https://crystalfountains.com/
- **legal_name_quote**: nterested in working at Crystal? FIND OUT MORE Youtube Twitter Facebook-f Linkedin Instagram © 2026 Designed by Crystal Fountains Inc. ","library":"fa-solid"}}" data-widget_type="nav-menu.default"> Accessibility Policy Privacy Policy
- **logo_url**: https://crystalfountains.com/
- **logo_basis**: logo image on the site
- **bn**: 516147308
- **bn_label**: tps://www.facebook.com/help/516147308
- **bn_url**: https://crystalfountains.com/privacy-policy/
- **bn_quote**: ook Inc. You can learn more about interest-based advertising from Facebook by visiting this page: https://www.facebook.com/help/516147308587266 To opt-out from Facebook’s interest-based ads, follow these instructions from Facebook: https
- **domain**: crystalfountains.com
- **key**: lead:a378feaa9e2fd613
- **name**: Parc Waterloo
- **website**: https://crystalfountains.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Crystal Fountains Inc.
- **jsonld_legal_name**: Crystal Fountains
- **jsonld_alternate_name**: Crystal Fountains
- **jsonld_phone**: (905) 660-6674
- **jsonld_email**: marketing@crystalfountains.com
- **jsonld_logo**: https://crystalfountains.com/wp-content/uploads/2021/09/Crystal-Fountans-logo.png
- **jsonld_url**: https://crystalfountains.com/
- **jsonld_same_as**: https://www.facebook.com/CrystalFountains; https://x.com/Crystal_Ftns; https://www.linkedin.com/company/crystal-fountains; https://www.pinterest.co.uk/crystalftns/; https://www.youtube.com/user/crystalfountainsinc
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Crystal Fountains", "url": "https://crystalfountains.com/", "description": "Crystal Fountains is a globally recognized professional service specializing in design, manufacturing, and installation of commercial and interacti
- **jsonld_page**: https://crystalfountains.com/
- **legal_name_stated**: Twitter Inc
- **legal_name_stated_url**: https://crystalfountains.com/privacy-policy/
- **legal_name_stated_quote**: ms web page: https://policies.google.com/privacy Twitter Twitter remarketing service is provided by Twitter Inc. You can opt-out from Twitter’s interest-based ads by following their instructions: https://support
- **mentions**: {'payment_method': {'text': 'interactive play decks, Crystal’s sequencing nozzles are manufactured for captivation', 'url': 'https://crystalfountains.com/', 'quote': 'fficient, and sustainable. Sequencing Nozzles Used for both traditional entertainment fountains and interactive play decks, Crystal’s sequencing nozzles are manufactured for captivation, longevity, and public safety. Available with or without built-in LED ligh'}}
- **linkedin_url**: https://www.linkedin.com/company/crystal-fountains
- **tel_links**: +1-905-660-6674; 1-800-539-8858; 905-660-6674; +971-4512-4010; +49 2571 8063 977; +65 6485 8748; +1 847 275 5688; +1-800

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "60 Snow Blvd., Toronto, ON, Canada, L4K 4B3", "address_country": "CA", "address_url": "https://crystalfountains.com/contact-us/", "address_method": "pattern", "address_quote": "our order form: DOWNLOAD PDF Addresses CANADA 60 Snow Blvd. Toronto, ON, Canada L4K 4B3 UAE myOffice Business Center, Suite 2902 Marina Plaza, Dubai Marina P.O.Box 500", "phone": "+1-905-660-6674", "phone_url": "https://crystalfountains.com/contact-us/", "emails": "info@crystalfountains.com; sales_amc@crystalfountains.com", "emails_url": "https://crystalfountains.com/", "domain": "crystalfountains.com", "key": "vd:crystalfountains.com", "name": "Crystal Fountains", "website": "https://crystalfountains.com/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, soucyaquatik.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://soucyaquatik.com/wp-content/uploads/2022/12/OG-global-img.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: soucyaquatik.com
- **key**: vendor:Soucy Aquatik inc.
- **name**: Soucy Aquatik inc.
- **website**: https://soucyaquatik.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization/GeneralContractor
- **jsonld_name**: Soucy Aquatik
- **jsonld_alternate_name**: Soucy Aquatik
- **jsonld_address**: 3605 Wilfrid-Hamel Blvd, Québec, QC, G1P 2J4, CA
- **jsonld_phone**: +1-418-781-0620
- **jsonld_logo**: https://soucyaquatik.com/wp-content/uploads/2022/12/soucy_logo-svg.png
- **jsonld_url**: https://soucyaquatik.com/
- **jsonld_founding_date**: 1964
- **jsonld_same_as**: https://www.facebook.com/soucyaquatik/; https://www.linkedin.com/company/soucyaquatik/; https://www.pinterest.ca/SoucyAquatik/; https://www.youtube.com/@soucyaquatik9404
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://soucyaquatik.com/","url":"https://soucyaquatik.com/","name":"Commercial & Rooftop Pool Design-Build | Soucy Aquatik","isPartOf":{"@id":"https://soucyaquatik.com/#website"},"about":{"@id":"https://soucyaquatik.com/#organizat
- **jsonld_page**: https://soucyaquatik.com/
- **legal_name_stated**: Laval University
- **legal_name_stated_url**: https://soucyaquatik.com/about-us/our-team/
- **legal_name_stated_quote**: e in delivering quality projects. Jonathan holds a Bachelor’s degree in Mechanical Engineering from Laval University and has been a member of the Ordre des ingénieurs du Québec since 2012, as well as the Association
- **mentions**: {'payment_method': {'text': 'interactivity to any environment', 'url': 'https://soucyaquatik.com/', 'quote': 'asis of freshness. By diffusing a light, refreshing fog, this FOGPAVER™ brings a touch of magic and interactivity to any environment. Whether it’s a park, public square or urban space, imagine offering your visitors a unique sensory'}}
- **linkedin_url**: https://www.linkedin.com/company/soucyaquatik/
- **tel_links**: 4187810620; +14187810620; +1587-635-1135; +17783734856

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "3605 Wilfrid-Hamel Blvd, Québec, QC, G1P 2J4", "address_country": "CA", "address_url": "https://soucyaquatik.com/contact-us/", "address_method": "json-ld", "address_quote": "e will get back to you soon! Québec 3605 Wilfrid-Hamel Blvd Québec City, Quebec G1P 2J4 Canada (418) 781-0620 Edmonton 10050 112 St NW Suite 904 Edmonton, AB T5K 2J1 C", "phone": "+1-418-781-0620", "phone_url": "https://soucyaquatik.com/contact-us/", "domain": "soucyaquatik.com", "key": "vd:soucyaquatik.com", "name": "Soucy Aquatik inc.", "website": "https://soucyaquatik.com/", "kind": "vendor", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Parc Waterloo |  |  |  |  |  |  |  |  |  |  |
| v | Soucy Aquatik inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:a378feaa9e2fd613",
 "ap_contact_team": {
  "emails": [
   "info@crystalfountains.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@crystalfountains.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://crystalfountains.com/",
    "quote": "ality\": \"Vaughan\", \"addressRegion\": \"Ontario\", \"postalCode\": \"L4K 4B3\", \"addressCountry\": \"CA\" }, \"telephone\": \"+1-905-660-6674\", \"email\": \"info@crystalfountains.com\", \"sameAs\": [ \"https://twitter.com/Crystal_Ftns\", \"https://www.linkedin.com/company/crystal-fountains\", \"https://www.youtube",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Parc Waterloo",
    "task_id": "CL-LD-21558"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of crystalfountains.com (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 54)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:1005525:soucy-aquatik-inc | Ville de Saint-Hyacinthe . | Construction d'un SkatePlaza | 481745.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=89c70a4c-85c3-4fed-aa29-1b3df3ac857c |
| seao_quebec:1060580:soucy-aquatik-inc | Ville de Saguenay | ENTRETIEN DES SYSTÈMES DE BRUMISATION ET DE JETS D'EAU - PLACE DU CITOYEN / Arrondissement de Chicoutimi | 112029.92 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3d7e2ec6-3c52-4c95-b35e-2f9b888b4f1c |
| seao_quebec:1096024:soucy-aquatik-inc | Municipalité de Notre-Dame-du-Portage | Réfection des bassins et équipements piscine | 133658.44 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=1f561018-e1e6-419d-8c43-7efe191780b4 |
| seao_quebec:1102866:soucy-aquatik-inc | Ville de Saint-Hyacinthe . | Fourniture et installaton des équipements de filtration des jeux d'eau et des avancées de béton pour la piscine Laurier | 730317.25 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=f1125a19-770a-4c52-826c-4e5d125647ed |
| seao_quebec:1182629:soucy-aquatik-inc | Ville de Pincourt. | TRAVAUX DE RÉFECTION DU BASSIN DE LA PISCINE MUNICIPALE | 878983.88 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=214c7815-b678-4c01-9d2c-7de2725aa812 |
| seao_quebec:1221084:soucy-aquatik-inc | Ville de Drummondville. | Piscine Woodyatt - Réfection | 2515767.98 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=119e04ef-1c31-412c-8682-653fe2f3ddc7 |
| seao_quebec:1340658:soucy-aquatik-inc | Ville de Saguenay | ENTRETIEN DES SYSTÈMES DE BRUMISATION ET DE JETS D'EAU - PLACE DU CITOYEN | 176246.61 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=114d298f-ad1d-4979-9703-7b708ae4aa8e |
| seao_quebec:1542704:soucy-aquatik-inc | Ville de Saint-Hyacinthe . | Travaux de réfection de la tuyauterie périmétrale et remise à neuf du bassin de la piscine Assomption | 263292.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b7468ff0-06e3-4647-a183-8f86615027c7 |
| seao_quebec:1647358:soucy-aquatik-inc | Municipalité de McMasterville. | Réfection et mise aux normes de la salle de filtration pour la piscine et la pataugeoire | 81574.76 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c624a70c-3edd-4404-ba2c-2277bf82bc6e |
| seao_quebec:1682931:soucy-aquatik-inc | Ville de L'Île-Perrot | Équipements pour le nouveau complexe aquatique | 97728.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5234066e-2e23-4e1e-91f2-0c37a492248c |
| seao_quebec:1686966:soucy-aquatik-inc | Ville de Montmagny | Rénovation de la piscine Guylaine-Cloutier | 657657.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=eea270d7-808e-4435-bdec-235c7e205935 |
| seao_quebec:1705875:soucy-aquatik-inc | Ville de Candiac. | Remplacement du système de chauffe-eau à la piscine municipale |  |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0c34e15e-99dc-4c12-b1b9-da037523e4c3 |
| seao_quebec:20040304:soucy-aquatik-inc | Ville de Saguenay | MISE EN MARCHE, HIVERNATION ET ENTRETIEN DU SYSTÈME DE JETS D'EAU ET DE BRUMISATION - PLACE DU CITOYEN / Arrondissement de Chicoutimi | 81981.77 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b510941c-d911-4bae-b5a6-e7f284cb6e65 |
| seao_quebec:20044530:soucy-aquatik-inc | Ville de Montréal - Service de la Gestion et de la Planification des Immeubles | Travaux pour remplacer les 3 drains de fond de la partie profonde de la piscine du parc Confédération. SGPI | 65000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=6910b0d2-4f1e-48c9-893f-584b8a1d8240 |
| seao_quebec:20050779:soucy-aquatik-inc | Ville de Lévis. | Opération, programmation et entretien des systèmes de jets d'eau du quai Paquet à Lévis | 862105.55 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=a5cfba40-262c-4031-ac50-f01885054218 |
| seao_quebec:20051547:soucy-aquatik-inc | Ville de Drummondville. | Remplacement des médias filtrant de l'Aquacomplexe | 30698.33 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=81c71f40-c7d5-42a2-8255-380929e78b80 |
| seao_quebec:20053499:soucy-aquatik-inc | Ville de Drummondville. |  Fourniture et installation d'une glissade pour la piscine du Centre | 97728.75 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9b446c85-fe29-455d-a4bb-656c7f5e4cb5 |
| seao_quebec:20100349:soucy-aquatik-inc | Ville de Malartic. | Réfection des installations aquatiques du camping régional de Malartic | 2308698.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=496758e7-8824-4bbc-b2d0-9bee697fbdd3 |
| seao_quebec:20110312:soucy-aquatik-inc | Ville de Montréal - Arrondissement de Ville-Marie | Remplacement d'équipements du système de contrôle fontainier au pavillon du square Viger | 130957.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=03ed8228-c5c4-46dc-aae6-59e1e30b2819 |
| seao_quebec:20129931:soucy-aquatik-inc | Commission de la capitale nationale du Québec . | Remplacement d'imperméabilisation du bassin de fontaine et construction d'une fosse mécanique au parc du Bois-de-Coulonge | 148100.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=49825cac-b39b-4d27-bdb3-b314094b8760 |
| seao_quebec:20145757:soucy-aquatik-inc | Ville de Montréal - Arrondissement CDN-NDG - SDF590204 | Ajout d’une rampe d’accès universelle à la piscine du parc Martin-Luther-King | 562860.11 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=df160191-d20a-4390-b314-6e898fefc7ce |
| seao_quebec:20148238:soucy-aquatik-inc | Ville de Saguenay | ENTRETIEN DU SYSTÈME DE JETS D'EAU ET DE BRUMISATION - PLACE DU CITOYEN / Arrondissement de Chicoutimi | 82757.86 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=5c1e6ab5-19d3-45d7-a810-265db417b50d |
| seao_quebec:20159180:soucy-aquatik-inc | Ville de Lachute | Réfection de la surface en béton de la piscine extérieure | 137970.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9395aeba-38bd-4859-8c44-0b8abe89d9f1 |
| seao_quebec:20166484:soucy-aquatik-inc | Ville de Montréal - Arrondissement Montreal-Nord. | Remplacement média filtrants pour les piscines extérieures dans plusieurs parcs | 90087.8 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=c169a68f-9ca6-4dd7-9cf2-0b730a45c96a |
| seao_quebec:20175448:soucy-aquatik-inc | Santé Québec Outaouais | REMPLACEMENT COMPLET DU SYSTEME DE TRAITEMENT D'EAU ET DES COMPOSANTES MECANIQUE DE LA PISCINE | 110600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=51da6de0-a820-4ccc-bd7f-7b3a2076a61e |
| seao_quebec:492586:soucy-aquatik-inc | Commission scolaire de la Beauce-Etchemin. | REMPLACEMENT DES POMPES ET DIVERS TRAVAUX DE MÉCANIQUE DE LA PISCINE | 129000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=0db44364-a654-4614-a9ac-b88fed265c73 |
| seao_quebec:507129:soucy-aquatik-inc | Commission scolaire des Hautes Rivières | RÉFECTION DU BASSIN DE LA PISCINE INTÉRIEURE (069) | 36500.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ea2eecf5-4707-421d-84fa-e1d432e8bcd9 |
| seao_quebec:509160:soucy-aquatik-inc | Ville de Dollard-des-Ormeaux | Contrat pour la fourniture et l'installation d'équipements de filtration pour la piscine #1 du Centre civique de la Ville de Dollard-des-Ormeaux | 370077.2 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=305a4932-c715-4501-a76e-9cb992fa94a8 |
| seao_quebec:510980:soucy-aquatik-inc | Université Laval | Université Laval - PEPS volet A - agrandissement du PEPS - Plancher à hauteur variable pour bassin de natation | 865830.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=21f9128c-40d0-4357-abde-b5903e245f89 |
| seao_quebec:550787:soucy-aquatik-inc | Ville de Richmond . | Reconstruction d'une piscine | 298245.15 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=bf0b8bf2-7aad-4a47-a822-ffb07967bcae |
| seao_quebec:577629:soucy-aquatik-inc | Ville de Beaconsfield | Réhabilitation de la piscine municipale | 53877.29 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d8af9020-04f9-4f8c-b2cf-cd5995bf76dc |
| seao_quebec:617088:soucy-aquatik-inc | Municipalité de Verchères | Réfection de la piscine et pataugeoire de la rue Dalpé | 224976.18 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=841f7aea-8675-40b5-b645-0d86923c965c |
| seao_quebec:619972:soucy-aquatik-inc | Ville de Neuville | FOURNITURE ET INSTALLATION D'UN SYSTÈME COMPLET POUR JEUX D'EAU | 155662.35 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=78bb292a-ea3c-4e91-9356-355c994afa59 |
| seao_quebec:620542:soucy-aquatik-inc | Commission scolaire de la Capitale. | RÉFECTION DES GOULOTTES, DES BLOCS DE DÉPART ET MISE AUX NORMES DES TREMPLINS | 280600.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=d1718450-4c27-4c91-b9a4-e73ad249ff41 |
| seao_quebec:621613:soucy-aquatik-inc | Commission scolaire des Hautes Rivières | École Mgr Euclide TYhéberge (069) Remplacement du système de filtration de la piscine | 131180.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=b106f514-acac-4ac1-8cd6-2621927a2827 |
| seao_quebec:622409:soucy-aquatik-inc | Ville de Fermont.. | Réfection de la piscine municipale de Fermont | 1765689.47 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=44a08910-70ee-4e9b-a2c6-d5738ecef290 |
| seao_quebec:667668:soucy-aquatik-inc | Saint-Placide | Aménagement de jeux d'eau au Parc Cyrille-Lalande | 258607.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=92af4d80-fe72-46c2-bdb8-321c6ea37c4a |
| seao_quebec:738497:soucy-aquatik-inc | Cégep de l'Outaouais... | Réfection du bassin de la piscine et travaux connexes | 165888.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=82eedfa4-f4a2-4b53-9953-44b00188d53a |
| seao_quebec:787371:soucy-aquatik-inc | Ville de Drummondville. | Travaux de réfection de la piscine Ste-Thérèse | 600169.5 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=9c479db8-0062-43f0-bbf5-130c397e3443 |
| seao_quebec:826748:soucy-aquatik-inc | Ville de Montréal - Arrondissement d'Ahuntsic-Cartierville | Amélioration du système de filtration de la pataugeoire au chalet du parc De Mésy | 187343.72 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=ef1b9337-7f10-4755-b6e3-1eeec91a5bff |
| ca_montreal_contrats:fonctionnaires-12946-1544729 | Ville de Montréal | BEAULIEU - REMPLACER LES REMPLISSEURS DE CHLORE POUR BAT: 9999 | 7043.54 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-49865-1572858 | Ville de Montréal | BEAULIEU - Remplacer les réservoirs de remplisseur de chlore par des 600L POUR BAT:9999 | 7839.44 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-97339-1688655 | Ville de Montréal | SGPI - Remplacement du filtre aquatique à cartouche TC500 - Jardin Botanique | 2926.0 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-111029-1270259 | Ville de Montréal | 2187513001-Contrat de services prof afin dassister le Service DSS dans lévaluation des coûts de construction du projet de rénovation des installations aquatiq | 4779.03 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-113807-1707696 | Ville de Montréal | SGPI - Travaux pour remplacer les 3 drains de fond de la partie profonde de la piscine du parc Confédération | 68241.87 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-116133-765946 | Ville de Montréal | L'euvre Mastodo de Charles Daudelin, actuellement au Square Viger, sera relocalisée aux bassins du Nouveau-Havre. Comme il s'agit d'une euvre-fontaine, les test | 12592.14 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-152228-1517690 | Ville de Montréal | Bordage - Formation du contrôleur Becys5 avec ses sonde | 5249.37 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-176889-1584352 | Ville de Montréal | Filtration UV - SGPI Insectarium - JF | 4410.62 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-181011-1576854 | Ville de Montréal | SGPI Jardin Botanique - JF  Fourniture de lumieres - | 13119.98 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-186394-1045717 | Ville de Montréal | Étude technique - Évaluation de l'uvre sculpture fontaine MASTODO | 21006.95 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_montreal_contrats:fonctionnaires-193350-1574984 | Ville de Montréal | SGPI Insectarium - JF Lampes UV | 2083.67 |  |  | https://donnees.montreal.ca/dataset/0b7955a7-8523-4254-8f95-81a59684866d/resource/e4b758ab-3edb-4b6a-8764-2a443b6b9404/download/contratsfonctionnaires.csv |
| ca_quebec_city_laval_gatineau_longueuil:longueuil:22213196 | Ville de Longueuil | REMPLACEMENT DE LA TOILE DE LA PISCINE RENE-VEILLET ET REPARATIONS MINEURES | 463430.0 |  |  | https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6 |
| ca_quebec_city_laval_gatineau_longueuil:longueuil:20209374 | Ville de Longueuil | SD-2020-1869 / GG-20-029 / MOBILIER URBAIN - ZONE FRAICHEUR | 37209.5 |  |  | https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6 |
| ca_quebec_city_laval_gatineau_longueuil:longueuil:16212121 | Ville de Longueuil | CE-160628-1.8 / APP-16-154 / CONTRAT 2 / FOURNITURE DE PULSAR PLUS HYPOCHLORITE DE CALCIUM EN BRIQUETTES POUR LES PISCINES | 36212.0 |  |  | https://www.donneesquebec.ca/recherche/dataset/96c41f45-6f76-4cc2-a6a8-98299fe26cd6 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

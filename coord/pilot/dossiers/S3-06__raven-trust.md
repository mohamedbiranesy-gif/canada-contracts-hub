# S3-06 — RAVEN Trust ⇄ Projet 10

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/) — 509 – 620 View Street, Victoria, BC, Canada, V8W 1J6
SUBMIT TO: info@raventrust.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08) — 10138 Rue Lajeunesse, Suite #301 , Montréal, QC H3L 2E2 | GST/HST 861819316 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-05-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1149123755
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Reconnaissance du Territoire | Get Involved Today — Project 10
```

## Relationship
- **rank_group**: E1
- **data_quality_score**: 37
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: RAVEN Trust (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Projet 10 | subject: Reconnaissance du Territoire | Get Involved Today — Project 10 | published by: the Canada-located vendor's own website | record: https://www.p10.qc.ca/reconnaissance-du-territoire | vendor in Canada because: vendor located in Canada (wd)=p10.qc.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:303fa656cb547682
- **tier**: E
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: RAVEN Trust
- **buyer_website**: https://raventrust.com/
- **buyer_address**: 509 – 620 View Street, Victoria, BC, Canada, V8W 1J6
- **buyer_phone**: (250) 383-2331 (printed next to the organisation's mailbox (as printed on https://raventrust.com/, re-read 2026-11-08))
- **buyer_contact_evidence_url**: https://raventrust.com/about-us/
- **buyer_legal_name_as_published**: RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/)
- **buyer_logo_url**: https://raventrust.com/wp-content/uploads/2024/11/Raven-logo-black-horizontal.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/raven-respecting-aboriginal-values-
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://raventrust.com/about-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@raventrust.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://raventrust.com/
- **email_evidence_quote**: e Organize Involve Your Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com For Media Inquiries:
- **email_evidence_context**: is day. ABOUT RAVEN About Us How We Work People RAVEN Champions Annual Reports GET INVOLVED Volunteer Fundraise Organize Involve Your Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com For Media Inquiries: media@raventrust.com Join the Ecosystem of Giving Become a Monthly Donor © Copyright RAVEN – Canadian Charitable Tax # 85484 0147 RR0001 – U.S. 501(c)(3) EIN 98-0628334 Site designed & built by Julia Hoang . Management by WPAssi (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@raventrust.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://raventrust.com/ | quote: "e Organize Involve Your Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-10744
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;sp=none;adkim=r;aspf=r;pct=100;fo=0;rf=afrf;ri=86400
- **dmarc_record_domain**: raventrust.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:209.54.116.231 +ip4:209.54.112.204 +include:_spf.createsend.com +include:_spf.google.com +include:mailgun.org ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/) — 509 – 620 View Street, Victoria, BC, Canada, V8W 1J6 ⏎ SUBMIT TO: info@raventrust.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08) — 10138 Rue Lajeunesse, Suite #301 , Montréal, QC H3L 2E2 | GST/HST 861819316 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-05-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1149123755 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Reconnaissance du Territoire | Get Involved Today — Project 10
- **invoice_card_json**: {"bill_to": {"legal_name": "RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/)", "legal_name_is_published": true, "address": "509 – 620 View Street, Victoria, BC, Canada, V8W 1J6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@raventrust.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "861819316RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)", "bn9": "861819316 (recipient_business_number in the federal grants & contri
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Projet 10
- **vendor_legal_name**: PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_registry_id**: NEQ 1149123755 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx
- **vendor_registered_address**: 10138 rue Lajeunesse, Montréal (Québec), H3L2E2 (registered address; Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_neq**: 1149123755 (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_address**: 10138 Rue Lajeunesse, Suite #301 , Montréal, QC H3L 2E2
- **vendor_country_basis**: vendor located in Canada (wd)=p10.qc.ca
- **vendor_bn9**: 861819316 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-05-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 861819316RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://p10.qc.ca
- **vendor_contact_evidence_url**: https://www.p10.qc.ca/
- **vendor_logo_url**: https://images.squarespace-cdn.com/content/v1/6759cfbaac998c304b38a103/71b471a3-cc97-4f7e-91a2-f1444ea46665/35logo.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: NEQ 1149123755 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2000-02-15; phone / role e-mails / logo: the vendor's own site, https://www.p10.qc.ca/ (tools/org_contacts.py, org_extras.py); website: https://p10.qc.ca (site answers); NEQ: 1149123755 (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: immatriculée (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)
- **vendor_incorporation_date**: 2000-02-15
- **vendor_years_in_business**: 26.7 (since 2000-02-15, registry date)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Reconnaissance du Territoire | Get Involved Today — Project 10
- **contract_description**: Reconnaissance du Territoire | Get Involved Today — Project 10 (the record's title; the source publishes no separate description)
- **contract_link**: https://www.p10.qc.ca/reconnaissance-du-territoire
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 861819316RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/) — 509 – 620 View Street, Victoria, BC, Canada, V8W 1J6 ⏎ SUBMIT TO: info@raventrust.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08) — 10138 Rue Lajeunesse, Suite #301 , Montréal, QC H3L 2E2 | GST/HST 861819316 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2019-05-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) | NEQ 1149123755 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Reconnaissance du Territoire | Get Involved Today — Project 10
- **invoice_card_json**: {"bill_to": {"legal_name": "RAVEN Trust (schema.org JSON-LD Organization name on https://raventrust.com/)", "legal_name_is_published": true, "address": "509 – 620 View Street, Victoria, BC, Canada, V8W 1J6", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@raventrust.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "861819316RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "PROJET 10 (as registered: Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08)", "bn9": "861819316 (recipient_business_number in the federal grants & contri
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@raventrust.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://raventrust.com/", "quote: \"e Organize Involve Your Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-10744"], "buyer_facts": ["address and phone: the buyer's own site, https://raventrust.com/about-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: NEQ 1149123755 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1149123755, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: federal grants & contributions disclosure (recipient_busi

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://raventrust.com/ | 2026-11-08 | ok |  |  |  | (250) 383-2331 |  |  |  |  |  |

## Buyer site facts (org_extras, raventrust.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://raventrust.com/wp-content/uploads/2024/11/Raven-logo-black-horizontal.png
- **logo_basis**: logo image on the site
- **domain**: raventrust.com
- **key**: lead:303fa656cb547682
- **name**: raventrust.com
- **website**: https://raventrust.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: RAVEN Trust
- **jsonld_logo**: https://raventrust.com/wp-content/uploads/2020/09/RAVENLogopng.png
- **jsonld_url**: https://raventrust.com/
- **jsonld_same_as**: https://www.facebook.com/pages/RAVEN-Respecting-Aboriginal-Values-Environmental-Needs/121099651233937; https://x.com/raventrust; https://www.instagram.com/raven_trust
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/raventrust.com\/","url":"https:\/\/raventrust.com\/","name":"Home - Raven Trust","isPartOf":{"@id":"https:\/\/raventrust.com\/#website"},"about":{"@id":"https:\/\/raventrust.com\/#organization"},"primaryImageOfPage":{"@
- **jsonld_page**: https://raventrust.com/
- **legal_name_stated**: McGill University
- **legal_name_stated_url**: https://raventrust.com/about-us/people/
- **legal_name_stated_quote**: ge. Joshua Ben David Nichols Joshua Ben David Nichols is Associate Professor at the Faculty of Law, McGill University. He works on the philosophy of law, the history of legal and political thought, constitutionalism
- **linkedin_url**: https://www.linkedin.com/company/raven-respecting-aboriginal-values-

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "509 – 620 View Street, Victoria, BC, Canada, V8W 1J6", "address_country": "CA", "address_url": "https://raventrust.com/about-us/", "address_method": "pattern", "address_quote": "Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com For Media Inquiries: media@rav", "emails": "info@raventrust.com", "emails_url": "https://raventrust.com/about-us/", "domain": "raventrust.com", "key": "lead:303fa656cb547682", "name": "raventrust.com", "website": "https://raventrust.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, p10.qc.ca)
- **status**: ok
- **pages**: 1
- **language**: fr-en
- **logo_url**: https://images.squarespace-cdn.com/content/v1/6759cfbaac998c304b38a103/71b471a3-cc97-4f7e-91a2-f1444ea46665/35logo.png
- **logo_basis**: logo image on the site
- **domain**: p10.qc.ca
- **key**: vendor:Projet 10
- **name**: Projet 10
- **website**: https://p10.qc.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "10138 Rue Lajeunesse, Suite #301 , Montréal, QC H3L 2E2", "address_country": "CA", "address_url": "https://www.p10.qc.ca/", "address_method": "pattern", "address_quote": "roject 10 — 1991 English Français 10138 Rue Lajeunesse, Suite #301 Montréal, QC H3L 2E2 (514) 989-0001 questions@p10.qc.ca Project 10 is located on Tio’tia:ke (Montrea", "domain": "p10.qc.ca", "key": "vd:p10.qc.ca", "name": "Projet 10", "website": "https://p10.qc.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Project 10 |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:303fa656cb547682",
 "ap_contact_team": {
  "emails": [
   "info@raventrust.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@raventrust.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://raventrust.com/",
    "quote": "e Organize Involve Your Business Get RAVEN News CONTACT US 509 – 620 View Street, Victoria, BC, Canada V8W 1J6 Phone: (250) 383-2331 Email: info@raventrust.com For Media Inquiries:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "raventrust.com",
    "task_id": "CL-LD-10744"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of raventrust.com (7 pages, robots.txt respected), no AI, no search engine"
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

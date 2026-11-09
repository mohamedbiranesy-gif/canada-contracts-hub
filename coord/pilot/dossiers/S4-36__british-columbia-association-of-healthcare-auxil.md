# S4-36 — BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES ⇄ inferred: Canada Post Corporation

Stratum: **S4_routed_company_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: BC Association of Healthcare Auxiliaries / — 682 MONTCALM RD, Trail, BC, V1R2J8 — buyer tax no. 870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/)
SUBMIT TO: info@bchealthcareaux.org (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES (hospital / health authority, BC) — inferred: no record; the organisation's type and 
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 30
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES (hospital / health authority, BC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Canada Post Corporation | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2 | status rule: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (British Columbia) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Can
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:132023128
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES
- **buyer_website**: https://bchealthcareaux.org
- **buyer_address**: 682 MONTCALM RD, Trail, BC, V1R2J8
- **buyer_phone**: 250-368-1657
- **buyer_contact_evidence_url**: https://bchealthcareaux.org/contact/
- **buyer_legal_name_as_published**: BC Association of Healthcare Auxiliaries /
- **buyer_bn_as_published**: 870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/)
- **buyer_bn_program**: RR (registered charity program account)
- **buyer_gst_hst_derived**: 870704442RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://bchealthcareaux.org/wp-content/uploads/2021/06/cropped-BCA-icon-180x180.jpg
- **buyer_website_status**: site answers
- **buyer_type**: hospital / health authority
- **buyer_sector**: healthcare
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (bchealthcareaux.org) + name)
- **buyer_charity_designation**: C; 0110
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://bchealthcareaux.org/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@bchealthcareaux.org
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://bchealthcareaux.org/
- **email_evidence_quote**: _1_tb_footer et_pb_text_align_right et_pb_text_align_center-tablet et_pb_bg_layout_light"> <div class="et_pb_text_inner"><p><a href="mailto:info@bchealthcareaux.org"><span class="__eae_cssd">gro.xuaerachtlaehcb@ofni</span></a><br />250-368-1657<br />Charity # 870704442 RR0001</p></div> </d
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@bchealthcareaux.org (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://bchealthcareaux.org/ | quote: "_1_tb_footer et_pb_text_align_right et_pb_text_align_center-tablet et_pb_bg_layout_light"> <div class="et_pb_text_inner"><p><a href="mailto:info@bchealthcareaux" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (bchealthcareaux.org) | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-06664
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (bchealthcareaux.org)
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none;sp=none;adkim=r;aspf=r;pct=100;fo=1;rf=afrf;ri=86400;rua=mailto:re+awxfxwjn2vk@dmarc.postmarkapp.com
- **dmarc_record_domain**: bchealthcareaux.org
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +a +mx +ip4:107.161.38.121 include:servers.mcsv.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BC Association of Healthcare Auxiliaries / — 682 MONTCALM RD, Trail, BC, V1R2J8 — buyer tax no. 870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/) ⏎ SUBMIT TO: info@bchealthcareaux.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES (hospital / health authority, BC) — inferred: no record; the organisation's type and 
- **invoice_card_json**: {"bill_to": {"legal_name": "BC Association of Healthcare Auxiliaries /", "legal_name_is_published": true, "address": "682 MONTCALM RD, Trail, BC, V1R2J8", "address_is_the_invoice_address": false, "tax_number": "870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/)", "language": "en"}, "submit_to": {"email": "info@bchealthcareaux.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number printed by the organisation itself: https:/
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: Canada Post Corporation
- **vendor_address**: 2701 Riverside Drive, Ottawa ON K1A 0B1
- **vendor_country_basis**: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/our-company/transparency-and-trust/privacy-centre/info-source/additional-information.page: 'Access to Information and Privacy Canada Post Corporation 2701 Riverside Drive, N1160 Ottawa ON K1A 0B1'
- **vendor_bn9**: 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)
- **vendor_website**: https://www.canadapost-postescanada.ca
- **vendor_phone**: 1-800-267-7651 (Credit Management Group (invoices and billing); https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to)
- **vendor_contact_evidence_url**: https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to
- **vendor_logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.canadapost-postescanada.ca/cpc/en/support/kb/billing/payments/what-address-should-i-send-payment-to (tools/org_contacts.py, org_extras.py); website: https://www.canadapost-postescanada.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf)

## Contract
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation located in Canada (British Columbia) (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); generic: Canada Post holds the exclusive privilege of collecting, transmitting and delivering letters within Canada (Canada Post Corporation Act, s. 14); most organisations mail some letters, but not every one does
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 870704442RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BC Association of Healthcare Auxiliaries / — 682 MONTCALM RD, Trail, BC, V1R2J8 — buyer tax no. 870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/) ⏎ SUBMIT TO: info@bchealthcareaux.org (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Canada Post Corporation — 2701 Riverside Drive, Ottawa ON K1A 0B1 | GST/HST 119321495 (GST/HST registration number printed by the organisation itself: https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sample-pdf-invoice.pdf, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES (hospital / health authority, BC) — inferred: no record; the organisation's type and 
- **invoice_card_json**: {"bill_to": {"legal_name": "BC Association of Healthcare Auxiliaries /", "legal_name_is_published": true, "address": "682 MONTCALM RD, Trail, BC, V1R2J8", "address_is_the_invoice_address": false, "tax_number": "870704442 RR0001 (as printed: Charity # 870704442 RR0001; https://bchealthcareaux.org/)", "language": "en"}, "submit_to": {"email": "info@bchealthcareaux.org", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "119321495RT0001 (GST/HST 119321495 (RT program; account suffix not printed); QST 1006393299)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "inferred: Canada Post Corporation", "bn9": "119321495 (GST/HST registration number printed by the organisation itself: https:/
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@bchealthcareaux.org (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://bchealthcareaux.org/", "quote: \"_1_tb_footer et_pb_text_align_right et_pb_text_align_center-tablet et_pb_bg_layout_light\"> <div class=\"et_pb_text_inner\"><p><a href=\"mailto:info@bchealthcareaux\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by self-hosted or other (bchealthcareaux.org)", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-06664"], "buyer_facts": ["address and phone: the buyer's own site, https://bchealthcareaux.org/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.canadapost-postescanada.ca/cpc/doc/en/postal-services/sa

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://bchealthcareaux.org/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, bchealthcareaux.org)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: BC Association of Healthcare Auxiliaries /
- **legal_name_url**: https://bchealthcareaux.org/
- **legal_name_quote**: s News Donate gro.xuaerachtlaehcb@ofni 250-368-1657 Charity # 870704442 RR0001 Follow Follow © 2021 BC Association of Healthcare Auxiliaries / Website by Spryberry.co
- **bn**: 870704442
- **bn_program**: RR0001
- **bn_label**: Charity # 870704442 RR0001
- **bn_url**: https://bchealthcareaux.org/
- **bn_quote**: About Leadership Volunteering Member Auxiliaries News Donate gro.xuaerachtlaehcb@ofni 250-368-1657 Charity # 870704442 RR0001 Follow Follow © 2021 BC Association of Healthcare Auxiliaries / Website by Spryberry.co
- **logo_url**: https://bchealthcareaux.org/wp-content/uploads/2021/06/cropped-BCA-icon-180x180.jpg
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: bchealthcareaux.org
- **key**: cra:132023128
- **name**: BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES
- **website**: https://bchealthcareaux.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: BC. The BC Association
- **legal_name_stated_url**: https://bchealthcareaux.org/
- **legal_name_stated_quote**: lthcare centres and health services, thereby promoting the health and welfare of communities within BC. The BC Association of Healthcare Auxiliaries (BCAHA) was established in 1945 to promote education, leadership, effecti
- **mentions**: {'payment_method': {'text': 'interaction at the local and provincial levels, including annual provincial and regiona', 'url': 'https://bchealthcareaux.org/', 'quote': 'timely information and resource material through our website, a regular newsletter and face-to-face interaction at the local and provincial levels, including annual provincial and regional annual general meetings and conferences. Learn More About BCAHA BCAHA T'}}

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "682 Montcalm Rd, Trail B.C., V1R 2J8", "address_country": "CA", "address_url": "https://bchealthcareaux.org/contact/", "address_method": "pattern", "address_quote": "CAHA  By email: gro.xuaerachtlaehcb@ofni  address: 682 Montcalm Rd Trail B.C. V1R 2J8  by phone: 250-368-1657 t ask the president: gro.xuaerachtlaehcb@tnediserp Or", "phone": "250-368-1657", "phone_url": "https://bchealthcareaux.org/contact/", "emails": "info@bchealthcareaux.org", "emails_url": "https://bchealthcareaux.org/contact/", "domain": "bchealthcareaux.org", "key": "cra:132023128", "name": "BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES", "website": "https://bchealthcareaux.org/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, canadapost-postescanada.ca)
- **status**: ok
- **pages**: 1
- **language**: en
- **logo_url**: https://www.canadapost-postescanada.ca/cpc/assets/cpc/uploads/banners/personal/ccmopc-36907-secondary-hero-large.svg
- **logo_basis**: logo image on the site
- **domain**: canadapost-postescanada.ca
- **key**: b:2aa5e3d1f7b796f4
- **name**: Canada Post
- **website**: https://canadapost-postescanada.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=BRITISH%20COLUMBIA%20ASSOCIATION%20OF%20HEALTHCARE%20AUXILIARIES | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canada Post | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |
| b | BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES |  |  |  |  |  |  |  |  |  |  |
| v | SOCIÉTÉ CANADIENNE DES POSTES | Q1032001 | official website on the organisation's domain (https://www.canadapost-postescanada.ca/) + name |  | Canada Post | Postes Canada | business; state-owned enterprise | business corporation | Canada | 1867-07-01 | Ottawa |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:132023128",
 "ap_contact_team": {
  "emails": [
   "info@bchealthcareaux.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@bchealthcareaux.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://bchealthcareaux.org/",
    "quote": "_1_tb_footer et_pb_text_align_right et_pb_text_align_center-tablet et_pb_bg_layout_light\"> <div class=\"et_pb_text_inner\"><p><a href=\"mailto:info@bchealthcareaux.org\"><span class=\"__eae_cssd\">gro.xuaerachtlaehcb@ofni</span></a><br />250-368-1657<br />Charity # 870704442 RR0001</p></div> </d",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "BRITISH COLUMBIA ASSOCIATION OF HEALTHCARE AUXILIARIES",
    "task_id": "CL-CRA-06664"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.bchealthcareaux.org (11 pages, robots.txt respected), no AI, no search engine"
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

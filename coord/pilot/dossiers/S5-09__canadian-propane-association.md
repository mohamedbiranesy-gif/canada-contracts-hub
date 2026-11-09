# S5-09 — Canadian Propane Association ⇄ Enterprise Canada

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Canadian Propane Association English Français ( French ) — 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 — buyer tax no. 848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08)
SUBMIT TO: info@propane.ca (general mailbox, confirmed by the referee) | invoice portal: Tungsten / Kofax
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ENTERPRISE CANADA INC. (as registered: Canada's Business Registries, AB 2122081132, 2026-11-08) — FIRM_ADDRESS: 595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN; vendor_address_missing: False | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: null
```

## Relationship
- **rank_group**: B1
- **data_quality_score**: 60
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Canadian Propane Association (non-profit / association / cultural body, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Enterprise Canada | subject: null | awarded 2026-06-30, start 2026-05-15, end 2026-06-30 | published by: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv) | record: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=5878&regId=56583361 | vendor in Canada because: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN | status rule: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:3f7b4c6d48ed1498
- **tier**: B
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)

## Buyer
- **buyer**: Canadian Propane Association
- **buyer_website**: https://propane.ca/
- **buyer_address**: 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7
- **buyer_phone**: 613.683.2270
- **buyer_contact_evidence_url**: https://propane.ca/contact/
- **buyer_legal_name_as_published**: Canadian Propane Association English Français ( French )
- **buyer_bn_as_published**: 848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 848552717RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://propane.ca/wp-content/uploads/2022/04/logo-header.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/canadian-propane-association
- **buyer_registry_id**: corporation number 7633939 (Corporations Canada (open data); https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=7633939)
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_legal_form**: Canada Not-for-profit Corporations Act (Corporations Canada (open data), corporation number 7633939, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://propane.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@propane.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://propane.ca/where-to-buy/
- **email_evidence_quote**: unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Media Inquiries:
- **email_evidence_context**: Sign up to receive our monthly newsletter X/Twitter This field is for validation purposes and should be left unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Media Inquiries: media@propane.ca Calgary Office Propane Training Institute 715-5th Avenue S.W, Suite 2700 Calgary, Alberta T2P 2X6 Tel: (403) 543.6518 Toll-Free: (877) 784.4636 Fax: (403) 543.6508 Email: training@propane.ca Emergency Response Assis (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@propane.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://propane.ca/where-to-buy/ | quote: "unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Medi" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00210
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100
- **dmarc_record_domain**: propane.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:64.141.31.66 ip4:158.85.75.244 include:spf.protection.outlook.com include:saas3.mpower.ca ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: Tungsten / Kofax
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Kofax, Tungsten
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Canadian Propane Association English Français ( French ) — 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 — buyer tax no. 848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08) ⏎ SUBMIT TO: info@propane.ca (general mailbox, confirmed by the referee) | invoice portal: Tungsten / Kofax ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ENTERPRISE CANADA INC. (as registered: Canada's Business Registries, AB 2122081132, 2026-11-08) — FIRM_ADDRESS: 595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN; vendor_address_missing: False | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Canadian Propane Association English Français ( French )", "legal_name_is_published": true, "address": "406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7", "address_is_the_invoice_address": false, "tax_number": "848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@propane.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Kofax, Tungsten", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ENTERPRISE CANADA INC. (as registered: Canada's Business Registrie
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Enterprise Canada
- **vendor_legal_name**: ENTERPRISE CANADA INC. (as registered: Canada's Business Registries, AB 2122081132, 2026-11-08)
- **vendor_registry_id**: 2122081132 (AB)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Enterprise%20Canada
- **vendor_legal_form**: Alberta Business Corporation (Canada's Business Registries, AB 2122081132, 2026-11-08)
- **vendor_address**: FIRM_ADDRESS: 595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN; vendor_address_missing: False
- **vendor_country_basis**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)=595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN
- **vendor_website**: https://leadiq.com/
- **vendor_emails**: sales@leadiq.com; support@leadiq.com
- **vendor_phone**: 1-888-653-2347
- **vendor_contact_evidence_url**: https://leadiq.com/
- **vendor_logo_url**: https://cdn.prod.website-files.com/60819f9be381394642b5659e/6081a538174f4d6bc01bdd27_leadiq-logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://leadiq.com/ (cy Center Support Partner Program Request Demo Discover how our customers use our data to unlock sales success. Pricing Enterprise Login Start free Contact us D)
- **vendor_facts_provenance**: name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)); registry identity: 2122081132 (AB) status Active (Canada's Business Registries, AB 2122081132, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2019-07-29; phone / role e-mails / logo: the vendor's own site, https://leadiq.com/ (tools/org_contacts.py, org_extras.py); website: https://leadiq.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active (Canada's Business Registries, AB 2122081132, 2026-11-08)
- **vendor_incorporation_date**: 2019-07-29
- **vendor_years_in_business**: 7.3 (since 2019-07-29, registry date)

## Contract
- **contract_status**: likely active (record dated in the last 12 months: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))
- **contract_title**: null
- **contract_description**: null (the record's title; the source publishes no separate description)
- **award_date**: 2026-06-30
- **start_date**: 2026-05-15
- **end_date**: 2026-06-30
- **contract_link**: https://www.lobbyistsregistrar.bc.ca/app/secure/orl/lrs/do/vwRg?cno=5878&regId=56583361
- **source**: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 848552717RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Canadian Propane Association English Français ( French ) — 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 — buyer tax no. 848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08) ⏎ SUBMIT TO: info@propane.ca (general mailbox, confirmed by the referee) | invoice portal: Tungsten / Kofax ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ENTERPRISE CANADA INC. (as registered: Canada's Business Registries, AB 2122081132, 2026-11-08) — FIRM_ADDRESS: 595 Bay Street, Suite 1202, Toronto, ON, M5G 2C2, CAN; vendor_address_missing: False | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: null
- **invoice_card_json**: {"bill_to": {"legal_name": "Canadian Propane Association English Français ( French )", "legal_name_is_published": true, "address": "406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7", "address_is_the_invoice_address": false, "tax_number": "848552717 (Corporations Canada (open data), corporation number 7633939, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@propane.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "Tungsten / Kofax", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Kofax, Tungsten", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "ENTERPRISE CANADA INC. (as registered: Canada's Business Registrie
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@propane.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://propane.ca/where-to-buy/", "quote: \"unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Medi\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00210"], "buyer_facts": ["address and phone: the buyer's own site, https://propane.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (FIRM_ADDRESS (BC Registrar of Lobbyists open data, Registration_Primary_Export.csv))", "registry identity: 2122081132 (AB) status Active 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://propane.ca/ | 2026-11-08 | ok |  |  |  | (613) 683.2270 | 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 |  |  |  |  |

## Buyer site facts (org_extras, propane.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Canadian Propane Association English Français ( French )
- **legal_name_url**: https://propane.ca/
- **legal_name_quote**: berta T2P 2X6 Tel: (587) 349.5880 Fax: (403) 543.6099 Email: info@erac.org Website: erac.org © 2026 Canadian Propane Association English Français ( French )
- **logo_url**: https://propane.ca/wp-content/uploads/2022/04/logo-header.png
- **logo_basis**: logo image in the site header
- **domain**: propane.ca
- **key**: lead:3f7b4c6d48ed1498
- **name**: Canadian Propane Association
- **website**: https://propane.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: 2026 Canadian Propane Association
- **legal_name_stated_url**: https://propane.ca/about-cpa/
- **legal_name_stated_quote**: y, Alberta T2P 2X6 Tel: (587) 349.5880 Fax: (403) 543.6099 Email: info@erac.org Website: erac.org © 2026 Canadian Propane Association English Français ( French )
- **linkedin_url**: https://ca.linkedin.com/company/canadian-propane-association
- **tel_links**: (613) 683.2270; (403) 543.6518; (877) 784.4636; (403) 543.6508; (587) 349.5880; (403) 543.6099; 613.683.2270; 403.543.65

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7", "address_country": "CA", "address_url": "https://propane.ca/contact/", "address_method": "pattern", "address_quote": "u as soon as possible National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: 613.683.2270 Email: info@propane.ca Calgary Office Propane Training Instit", "phone": "613.683.2270", "phone_url": "https://propane.ca/contact/", "emails": "info@propane.ca", "emails_url": "https://propane.ca/contact/", "domain": "propane.ca", "key": "lead:3f7b4c6d48ed1498", "name": "Canadian Propane Association", "website": "https://propane.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, leadiq.com)
- **status**: ok
- **pages**: 6
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: LeadIQ
- **jsonld_address**: 548 Market Street PMB, San Francisco, CA, 94104, US
- **jsonld_phone**: +18886532347
- **jsonld_logo**: https://cdn.prod.website-files.com/60819f9be381394642b5659e/6081a538174f4d6bc01bdd27_leadiq-logo.svg
- **jsonld_url**: https://leadiq.com
- **jsonld_founding_date**: 2015
- **jsonld_same_as**: https://www.facebook.com/leadiq; https://twitter.com/leadiq; https://www.linkedin.com/company/leadiq-inc/; https://www.youtube.com/channel/UCNb5aT5w8EIMX4QKFuFL_Yg
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://leadiq.com/#organization", "name": "LeadIQ", "url": "https://leadiq.com", "logo": { "@type": "ImageObject", "url": "https://cdn.prod.website-files.com/60819f9be381394642b5659e/6081a538174f4d6bc01bdd27_leadiq-l
- **jsonld_page**: https://leadiq.com/
- **linkedin_url**: https://www.linkedin.com/company/leadiq-inc/
- **tel_links**: 18886532347
- **tel_links_url**: https://leadiq.com/
- **language**: en
- **legal_name**: LeadIQ, Inc
- **legal_name_url**: https://leadiq.com/
- **legal_name_quote**: eadIQ vs. Usergems LeadIQ vs. Champify Contact 1-888-653-2347 support@leadiq.com sales@leadiq.com © LeadIQ, Inc. All rights reserved.
- **logo_url**: https://cdn.prod.website-files.com/60819f9be381394642b5659e/6081a538174f4d6bc01bdd27_leadiq-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: leadiq.com
- **key**: vendor:Corporate Mirror INC
- **name**: Corporate Mirror INC
- **website**: https://leadiq.com/
- **kind**: vendor
- **date**: 2026-11-08

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "phone": "1-888-653-2347", "phone_url": "https://leadiq.com/book-a-demo", "emails": "sales@leadiq.com; support@leadiq.com", "emails_url": "https://leadiq.com/book-a-demo", "address": "548 Market Street PMB, San Francisco, CA, 94104", "address_country": "US", "address_url": "https://leadiq.com/", "address_method": "json-ld", "address_quote": "JSON-LD PostalAddress on the page: 548 Market Street PMB, San Francisco, CA, 94104", "domain": "leadiq.com", "key": "vendor:Corporate Mirror INC", "name": "Corporate Mirror INC", "website": "https://leadiq.com/", "kind": "vendor", "date": "2026-11-08"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Canadian Propane Association | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Canadian%20Propane%20Association | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Canadian Propane Association | found | CANADIAN PROPANE ASSOCIATION | 848552717 | corporation number 7633939 | Corporations Canada (open data) | Canada Not-for-profit Corporations Act | Active | 2014-09-18 | Ottawa | ON | 410 Laurier Avenue West, Suite 406, Ottawa, ON, K1R 1B7 | https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2 | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Canadian Propane Association |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:3f7b4c6d48ed1498",
 "ap_contact_team": {
  "emails": [
   "info@propane.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@propane.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://propane.ca/",
    "quote": "unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Media Inquiries:",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Canadian Propane Association",
    "task_id": "CL-SN-02426"
   },
   {
    "email": "info@propane.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://propane.ca/where-to-buy/",
    "quote": "unchanged. Your Email (Required) Subscribe --> National Office 406-410 Laurier Ave. West Ottawa, Ontario K1R 1B7 Tel: (613) 683.2270 Email: info@propane.ca Media Inquiries:",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Canadian Propane Association",
    "task_id": "CL-WS-00210"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of propane.ca (8 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI"
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

## The vendor's other buyers in the dataset (first 60 of 78)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:7cc7d711-9b90-42a7-b11f-8a80a9d7ffcc:13 | Comox Valley Regional District | RFQ - Communications Preferred Vendor List (PVL) |  |  |  | https://comoxvalleyrd.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7cc7d711-9b90-42a7-b11f-8a80a9d7ffcc |
| ca_bidsandtenders:1e363b36-b3bb-4304-bf07-7eab1956e6fc:4 | City of Leduc | Request for Pre-Qualification for Public Relations / Communications Services |  |  |  | https://leduc.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1e363b36-b3bb-4304-bf07-7eab1956e6fc |
| ca_bidsandtenders:73ba26d2-c41c-455c-8880-d621b90af710:1 | City of St. John's | Rental of Light Duty Vehicles - Standing Offer Agreement |  |  |  | https://stjohns.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/73ba26d2-c41c-455c-8880-d621b90af710 |
| ca_bidsandtenders:35f17b47-83c4-4533-a499-0411fa8345e5:1 | City of Grande Prairie | Vehicle Rentals |  |  |  | https://cityofGP.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/35f17b47-83c4-4533-a499-0411fa8345e5 |
| ca_bidsandtenders:8723ca14-e515-4a39-a0bb-af915b1b257f:2 | City of Hamilton | Roster for Intergovernmental Relations Consultants for the City of Hamilton |  |  |  | https://hamilton.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8723ca14-e515-4a39-a0bb-af915b1b257f |
| ca_merx:1756295719:1 | ONTARIO PENSION BOARD | Media Monitoring and Crisis Communication Services |  |  |  | https://www.merx.com/ontariopensionboard/solicitations/Media-Monitoring-and-Crisis-Communication-Services/0000195679?origin=0 |
| ca_merx:1796534703:1 | Waypoint Centre for Mental Health Care | Strategic Plan Development : Pine River Institute |  |  |  | https://www.merx.com/waypointcentreformentalhealthcare/solicitations/Strategic-Plan-Development-Pine-River-Institute/0000198617?origin=0 |
| ca_newfoundland:7aec3c993b97cd7c | Executive Council | Professional Services Contract - Communications Comprehensive Review | 125000.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-July-1-15-Contract-Awards-Report.pdf |
| ca_newfoundland:c9b4b37c1fd7b99f | Cabinet Secretariat | Professional Service Contract | 65000.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-June-16-30-Contract-Awards-Report.REVISED.pdf |
| ca_newfoundland:d45c4e322277ac88 | Cabinet Secretariat | Professional Service Contract | 65000.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-June-16-30-Contract-Awards-Report.pdf |
| ca_newfoundland:0e5480b233309b44 | Executive Council | Communications Strategic Support - Budget | 54000.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-May-16-31-Contract-Awards-Report.pdf |
| ca_saskatchewan:a4cf0859-a60a-47f5-91fd-5bc8dbbae6c3:0 | University of Saskatchewan | Vehicle Rental Services | 2250000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=a4cf0859-a60a-47f5-91fd-5bc8dbbae6c3 |
| ca_saskatchewan:bee7686f-b2fc-4268-93b0-5ea3965d5363:0 | SaskBuilds and Procurement | Daily Vehicle Rental Services | 9000000.0 |  |  | https://www.sasktenders.ca/Competitions/Print?id=bee7686f-b2fc-4268-93b0-5ea3965d5363 |
| canada_federal:dnd-mdn:4502776510 | National Defence | Rental of motor and other vehicles | 77666.4 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2024-2025-Q2-00744 |
| canada_federal:dnd-mdn:4503046786 | National Defence | Rental of motor and other vehicles | 26338.97 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03622 |
| canada_federal:dnd-mdn:4503046789 | National Defence | Rental of motor and other vehicles | 26338.97 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03623 |
| canada_federal:dnd-mdn:4503046790 | National Defence | Rental of motor and other vehicles | 26338.97 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03624 |
| canada_federal:dnd-mdn:4503046832 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03625 |
| canada_federal:dnd-mdn:4503046834 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03626 |
| canada_federal:dnd-mdn:4503046841 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03627 |
| canada_federal:dnd-mdn:4503046931 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03628 |
| canada_federal:dnd-mdn:4503046936 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03629 |
| canada_federal:dnd-mdn:4503046938 | National Defence | Rental of motor and other vehicles | 21813.93 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03630 |
| canada_federal:dnd-mdn:4503047158 | National Defence | Rental of motor and other vehicles | 20768.24 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03632 |
| canada_federal:dnd-mdn:4503047164 | National Defence | Rental of motor and other vehicles | 20768.24 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03633 |
| canada_federal:dnd-mdn:4503048795 | National Defence | Rental of motor and other vehicles | 25168.42 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03647 |
| canada_federal:dnd-mdn:4503048801 | National Defence | Rental of motor and other vehicles | 25168.42 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03648 |
| canada_federal:dnd-mdn:4503048808 | National Defence | Rental of motor and other vehicles | 25168.42 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03649 |
| canada_federal:dnd-mdn:4503048818 | National Defence | Rental of motor and other vehicles | 25168.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03650 |
| canada_federal:dnd-mdn:4503048825 | National Defence | Rental of motor and other vehicles | 25168.75 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03651 |
| canada_federal:dnd-mdn:4503048833 | National Defence | Rental of motor and other vehicles | 22606.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03652 |
| canada_federal:dnd-mdn:4503048841 | National Defence | Rental of motor and other vehicles | 22606.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03653 |
| canada_federal:dnd-mdn:4503048853 | National Defence | Rental of motor and other vehicles | 22606.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03654 |
| canada_federal:dnd-mdn:4503048857 | National Defence | Rental of motor and other vehicles | 22606.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03655 |
| canada_federal:dnd-mdn:4503048858 | National Defence | Rental of motor and other vehicles | 22606.25 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03656 |
| canada_federal:dnd-mdn:4503048870 | National Defence | Rental of motor and other vehicles | 20543.75 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03657 |
| canada_federal:dnd-mdn:4503048877 | National Defence | Rental of motor and other vehicles | 20543.75 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03658 |
| canada_federal:dnd-mdn:4503048881 | National Defence | Rental of motor and other vehicles | 20543.75 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03659 |
| canada_federal:dnd-mdn:4503048910 | National Defence | Rental of motor and other vehicles | 25168.42 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03666 |
| canada_federal:dnd-mdn:4503053959 | National Defence | Rental of motor and other vehicles | 37000.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03673 |
| canada_federal:dnd-mdn:4503054938 | National Defence | Rental of motor and other vehicles | 14500.73 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03678 |
| canada_federal:dnd-mdn:4503056104 | National Defence | Rental of motor and other vehicles | 144718.35 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2025-2026-Q4-03686 |
| canada_federal:dnd-mdn:260064 | National Defence | Rental of motor and other vehicles | 11838.64 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00343 |
| canada_federal:dnd-mdn:260071 | National Defence | Rental of motor and other vehicles | 15566.76 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00345 |
| canada_federal:dnd-mdn:260072 | National Defence | Rental of motor and other vehicles | 15566.76 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00346 |
| canada_federal:dnd-mdn:260073 | National Defence | Rental of motor and other vehicles | 15566.76 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00347 |
| canada_federal:dnd-mdn:260075 | National Defence | Rental of motor and other vehicles | 15566.76 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00348 |
| canada_federal:dnd-mdn:260076 | National Defence | Rental of motor and other vehicles | 14975.54 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00349 |
| canada_federal:dnd-mdn:260116A | National Defence | Rental of motor and other vehicles | 17484.63 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-00359 |
| canada_federal:dnd-mdn:4503066355 | National Defence | Rental of motor and other vehicles | 33000.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-02682 |
| canada_federal:dnd-mdn:4503066742 | National Defence | Rental of motor and other vehicles | 22745.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-02702 |
| canada_federal:dnd-mdn:4503076019 | National Defence | Rental of motor and other vehicles | 35000.0 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-02991 |
| canada_federal:dnd-mdn:4503079998 | National Defence | Rental of motor and other vehicles | 25233.65 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03092 |
| canada_federal:dnd-mdn:4503080048 | National Defence | Rental of motor and other vehicles | 25233.65 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03093 |
| canada_federal:dnd-mdn:4503083933 | National Defence | Rental of motor and other vehicles | 68389.96 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03222 |
| canada_federal:dnd-mdn:4503083964 | National Defence | Rental of motor and other vehicles | 46996.39 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03223 |
| canada_federal:dnd-mdn:4503085360 | National Defence | Rental of motor and other vehicles | 42623.42 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03268 |
| canada_federal:dnd-mdn:4503085411 | National Defence | Rental of motor and other vehicles | 21311.71 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03270 |
| canada_federal:dnd-mdn:4503085450 | National Defence | Rental of motor and other vehicles | 21311.71 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03271 |
| canada_federal:dnd-mdn:4503085600 | National Defence | Rental of motor and other vehicles | 399114.02 |  |  | https://search.open.canada.ca/contracts/record/dnd-mdn,C-2026-2027-Q1-03273 |
| … 18 more rows in the .json | ||||||

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

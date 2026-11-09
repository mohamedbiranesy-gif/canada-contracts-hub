# S3-30 — Annapolis Valley Regional Library ⇄ BiblioCommons Corp.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Annapolis Valley Regional Library — 236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0 — buyer tax no. 106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name)
SUBMIT TO: administration@valleylibrary.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Recent Activity | Annapolis Valley Regional Library | BiblioCommons
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 53
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Annapolis Valley Regional Library (non-profit / association / cultural body, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: BiblioCommons Corp. | subject: Recent Activity | Annapolis Valley Regional Library | BiblioCommons | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://valleylibrary.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5 | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:6dcc262f6223797b
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Annapolis Valley Regional Library
- **buyer_website**: https://valleylibrary.ca/
- **buyer_address**: 236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0
- **buyer_phone**: 1-866-922-0229
- **buyer_contact_evidence_url**: https://valleylibrary.ca/
- **buyer_legal_name_as_published**: Annapolis Valley Regional Library
- **buyer_bn_as_published**: 106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 106714819RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://valleylibrary.ca/wp-content/uploads/2022/11/logo-avrl.svg
- **buyer_website_status**: site answers
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name)
- **buyer_charity_designation**: C; 0200
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q20311253; library network; public library; charitable organization
- **buyer_founded**: 1949-00-00 (Wikidata Q20311253, official website on the organisation's domain (http://www.valleylibrary.ca) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 1919349 Q1104069; 1971432 Q1104069; 2229178 Q1104069; 2123058 Q1104069; 2226145 Q1104069; 2191916 Q1104069; 2182253 Q110 (Wikidata Q20311253, official website on the organisation's domain (http://www.valleylibrary.ca) + name; 2026-11-08)
- **buyer_employees**: 64; 54; 52; 57; 65; 66; 76; 75; 69; 72; 68; 67; 73; 80 (Wikidata Q20311253, official website on the organisation's domain (http://www.valleylibrary.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://valleylibrary.ca/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: administration@valleylibrary.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://valleylibrary.ca/branches/middleton-rosa-m-harvey-middleton-area-library/
- **email_evidence_quote**: riend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valleylibrary.ca Toll Free: 1-866-922-0229 Local: 1-902-538-BOOK (902-538-2665) Find Your Branch Annapolis Royal Library Berwick and Di
- **email_evidence_context**: lection, so we have created a variety of ways for you to get involved and show your support. Donate Become a Friend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valleylibrary.ca Toll Free: 1-866-922-0229 Local: 1-902-538-BOOK (902-538-2665) Find Your Branch Annapolis Royal Library Berwick and District Library Bridgetown & Area Library Hantsport - Isabel & Roy Jodrey Memorial Library Kentville Library Kingston Library Middle (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: administration@valleylibrary.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://valleylibrary.ca/branches/middleton-rosa-m-harvey-middleton-area-library/ | quote: "riend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valle" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00408
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.valleylibrary.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.mlsend.com mx ip4:142.227.59.14 ip4:142.227.59.6 ip4:142.227.59.51 ?ip4:142.227.0.0/16 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Annapolis Valley Regional Library — 236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0 — buyer tax no. 106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name) ⏎ SUBMIT TO: administration@valleylibrary.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Recent Activity | Annapolis Valley Regional Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "Annapolis Valley Regional Library", "legal_name_is_published": true, "address": "236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0", "address_is_the_invoice_address": false, "tax_number": "106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name)", "language": "en"}, "submit_to": {"email": "administration@valleylibrary.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Nova Scotia)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "755272
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
- **vendor**: BiblioCommons Corp.
- **vendor_legal_name**: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_registry_id**: 2733173 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=BiblioCommons%20Corp.
- **vendor_registered_address**: Mississauga, Ontario (registered office city / province; Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_address**: 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=BiblioCommons Corp. 5060 Spectrum Way, Suite 100 Mississauga, ON L4W 5N5
- **vendor_bn9**: 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2733173, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2019-12-19
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08)
- **vendor_incorporation_date**: 2019-12-19
- **vendor_years_in_business**: 6.9 (since 2019-12-19, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2733173, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor BiblioCommons Corp.
- **contract_title**: Recent Activity | Annapolis Valley Regional Library | BiblioCommons
- **contract_description**: Recent Activity | Annapolis Valley Regional Library | BiblioCommons (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://valleylibrary.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 3
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 106714819RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (Nova Scotia) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 755272937RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Annapolis Valley Regional Library — 236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0 — buyer tax no. 106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name) ⏎ SUBMIT TO: administration@valleylibrary.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BIBLIOCOMMONS CORP. (as registered: Canada's Business Registries, ON 2733173, 2026-11-08) — 119 Spadina Avenue , Toronto , ON, M5V 2L1, Canada | GST/HST 755272937 (Canada's Business Registries, ON 2733173, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Recent Activity | Annapolis Valley Regional Library | BiblioCommons
- **invoice_card_json**: {"bill_to": {"legal_name": "Annapolis Valley Regional Library", "legal_name_is_published": true, "address": "236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0", "address_is_the_invoice_address": false, "tax_number": "106714819RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (valleylibrary.ca) + name)", "language": "en"}, "submit_to": {"email": "administration@valleylibrary.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NS on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Nova Scotia)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "755272
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["administration@valleylibrary.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://valleylibrary.ca/branches/middleton-rosa-m-harvey-middleton-area-library/", "quote: \"riend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valle\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00408"], "buyer_facts": ["address and phone: the buyer's own site, https://valleylibrary.ca/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: 2733173 (ON) status Active — incorporated (Canada's Business Registries, ON 2733173, 2026-11-08) (scripts/enrichment_*: Corporations Cana

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://valleylibrary.ca/ | 2026-11-08 | ok |  |  |  | 1-866-922-0229 | 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 |  |  |  |  |

## Buyer site facts (org_extras, valleylibrary.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Annapolis Valley Regional Library
- **legal_name_url**: https://valleylibrary.ca/
- **legal_name_quote**: Annapolis Valley Regional Library Skip to content Read the 2026 Library Service Changes Announcement Click here to find closure infor
- **logo_url**: https://valleylibrary.ca/wp-content/uploads/2022/11/logo-avrl.svg
- **logo_basis**: logo image on the site
- **domain**: valleylibrary.ca
- **key**: lead:6dcc262f6223797b
- **name**: Annapolis Valley Regional Library
- **website**: https://valleylibrary.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: LibrarySystem/Organization
- **jsonld_name**: Annapolis Valley Regional Library
- **jsonld_logo**: https://valleylibrary.ca/wp-content/uploads/2022/11/logo-avrl.png
- **jsonld_url**: https://valleylibrary.ca
- **jsonld_same_as**: https://www.facebook.com/AVRLibrary; https://twitter.com/valleylibs; https://instagram.com/avrlibrary/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":["LibrarySystem","Organization"],"@id":"https://valleylibrary.ca/#organization","name":"Annapolis Valley Regional Library","url":"https://valleylibrary.ca","sameAs":["https://www.facebook.com/AVRLibrary","https://twitter.com/valleylibs","https://in
- **jsonld_page**: https://valleylibrary.ca/
- **legal_name_stated**: Annapolis Valley Regional Library
- **legal_name_stated_url**: https://valleylibrary.ca/about-the-library/
- **legal_name_stated_quote**: About the Library - Annapolis Valley Regional Library Skip to content Click here to find closure information for one or more of our branches Browse Catal
- **tel_links**: 18669220229; 19025382665

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "236 Commercial Street, PO Box 510, Berwick, Nova Scotia, B0P 1E0", "address_country": "CA", "address_url": "https://valleylibrary.ca/", "address_method": "pattern", "address_quote": "ard Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valleylibrary.ca Toll Free: 1-866-922-0229 Local: 1-902-538-BOOK", "phone": "1-866-922-0229", "phone_url": "https://valleylibrary.ca/", "emails": "administration@valleylibrary.ca", "emails_url": "https://valleylibrary.ca/", "domain": "valleylibrary.ca", "key": "lead:6dcc262f6223797b", "name": "Annapolis Valley Regional Library", "website": "https://valleylibrary.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Annapolis Valley Regional Library | Q20311253 | official website on the organisation's domain (http://www.valleylibrary.ca) + name |  | Annapolis Valley Regional Library |  | library network; public library; charitable organization |  | Canada | 1949-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:6dcc262f6223797b",
 "ap_contact_team": {
  "emails": [
   "administration@valleylibrary.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "administration@valleylibrary.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://valleylibrary.ca/",
    "quote": "riend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valleylibrary.ca Toll Free: 1-866-922-0229 Local: 1-902-538-BOOK (902-538-2665) Find Your Branch Annapolis Royal Library Berwick and Di",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Annapolis Valley Regional Library",
    "task_id": "CL-LD-08428"
   },
   {
    "email": "administration@valleylibrary.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://valleylibrary.ca/branches/middleton-rosa-m-harvey-middleton-area-library/",
    "quote": "riend of the Library Attend an Event Get a Library Card Administration Office 236 Commercial Street PO Box 510 Berwick, Nova Scotia B0P 1E0 administration@valleylibrary.ca Toll Free: 1-866-922-0229 Local: 1-902-538-BOOK (902-538-2665) Find Your Branch Annapolis Royal Library Berwick and Di",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Annapolis Valley Regional Library",
    "task_id": "CL-WS-00408"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of valleylibrary.ca (21 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 6)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:32761475-333e-41ac-b891-ffddc5f83ade:1 | City of Mississauga | Library Online Resource Discovery & Mobile App |  |  |  | https://mississauga.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/32761475-333e-41ac-b891-ffddc5f83ade |
| us_county_fulton_ga:81357d5a48e75900-650 | Fulton County, Georgia — Library | Books-Library | 1042856.5700000001 |  |  | https://data.fultoncountyga.gov/d/mxhc-krcg |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~75a33202896d | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_81357d5a48e75900_vendor_name_:_Bi~1e00a517d323 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~c355691972d8 | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |
| us_socrata_sweep_continue:data.fultoncountyga.gov:2jx8-2ffx:_vendor_id_:_ccc6a7f05b8387ab_vendor_name_:_Bi~f8057c8ad9ef | Fulton County Government (GA) |  |  |  |  | https://data.fultoncountyga.gov/d/2jx8-2ffx |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

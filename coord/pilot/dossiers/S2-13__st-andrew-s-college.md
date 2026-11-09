# S2-13 — St. Andrew's College ⇄ CoreFour Inc.

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 1 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: St. Andrew's College — 15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08) — buyer tax no. 108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name)
SUBMIT TO: ap@sac.on.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: St. Andrew's College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own sit
```

## Relationship
- **rank_group**: GOLD-T
- **data_quality_score**: 84
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: St. Andrew's College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: CoreFour Inc. | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.sac.on.ca/community/parents | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor CoreFour Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:79b978669223e9c8
- **tier**: T
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: St. Andrew's College
- **buyer_website**: https://www.sac.on.ca/
- **buyer_address**: 15800 Yonge Street, Aurora, ON L4G 3H7
- **buyer_phone**: 905-727-3178
- **buyer_contact_evidence_url**: https://www.sac.on.ca/contact-us
- **buyer_legal_name_as_published**: St. Andrew's College
- **buyer_bn_as_published**: 108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 108004144RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://bbk12e1-cdn.myschoolcdn.com/ftpimages/842/logo/SAC-Logo.png
- **buyer_website_status**: site answers
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7586852; boys' high school; boarding school
- **buyer_founded**: 1899-00-00 (Wikidata Q7586852, official website on the organisation's domain (https://www.sac.on.ca) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 16089064 Q1104069; 18461394 Q1104069; 19491988 Q1104069; 20497042 Q1104069; 22132174 Q1104069; 23178241 Q1104069; 246900 (Wikidata Q7586852, official website on the organisation's domain (https://www.sac.on.ca) + name; 2026-11-08)
- **buyer_employees**: 180; 175; 181; 184; 198; 168; 254; 257; 262; 290; 287; 284; 340; 361; 329; 351; 279; 398; 424; 478 (Wikidata Q7586852, official website on the organisation's domain (https://www.sac.on.ca) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.sac.on.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: ap@sac.on.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.sac.on.ca/contact-us
- **email_evidence_quote**: Phone: (905) 727-3178 Business Office Email: ap@sac.on.ca Phone: (905) 727-3178 Fax: (905) 727-9289 Campus Shop Email: campus.shop@sac.on.ca Phone: (905) 727-3178 x279 Health Centre Email: health
- **email_evidence_context**: s Monday - Friday: 8 a.m. - 4 p.m. Departments Admission Email: admission@sac.on.ca Toll Free: 1 (877) 378-1899 Phone: (905) 727-3178 x303 Fax: (905) 727-9032 Alumni & Advancement Email: oldboys@sac.on.ca Phone: (905) 727-3178 Business Office Email: ap@sac.on.ca Phone: (905) 727-3178 Fax: (905) 727-9289 Campus Shop Email: campus.shop@sac.on.ca Phone: (905) 727-3178 x279 Health Centre Email: health.centre@sac.on.ca Phone: (905) 727-3178 x276 Direct Line: (905) 727-9843 Fax: (905) 727-7305 Human Resources Ema (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: ap@sac.on.ca (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.sac.on.ca/contact-us | quote: "Phone: (905) 727-3178 Business Office Email: ap@sac.on.ca Phone: (905) 727-3178 Fax: (905) 727-9289 Campus Shop Email: campus.shop@sac.on.ca Phone: (905) 727-31" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Barracuda | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011670
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Barracuda
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; pct=100; rua=mailto:80058e2e0eaa4855b5468a27f05a3e90@dmarc-reports.cloudflare.net,mailto:dmarc@sac.on.ca; fo=1
- **dmarc_record_domain**: sac.on.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:24.114.250.23 ip4:205.139.105.140 ip4:208.91.113.0/24 ip4:208.91.114.0/25 ip4:208.91.114.128/28 ip4:208.91.114.144/30 ip4:208.91.114.148/31 ip4:208.91.114.150 ip4:208.91.114.152/29 ip4:208.91.114.160/27 ip4:208.91.114.192/26 ip4:96.45.36.0/24 ip4:54.219.139.180/32 ip4:54.219.139.149/32 ip
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 1 (877) 378-1899 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)
- **invoice_mailing_address**: 15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "1 (877) 378-1899 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)", "mailing_address": "15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: St. Andrew's College — 15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08) — buyer tax no. 108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name) ⏎ SUBMIT TO: ap@sac.on.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: St. Andrew's College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own sit
- **invoice_card_json**: {"bill_to": {"legal_name": "St. Andrew's College", "legal_name_is_published": true, "address": "15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name)", "language": "en"}, "submit_to": {"email": "ap@sac.on.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: CoreFour Inc.
- **vendor_legal_name**: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_registry_id**: 2247351 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=CoreFour%20Inc.
- **vendor_registered_address**: Richmond Hill, Ontario (registered office city / province; Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_address**: 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada
- **vendor_bn9**: 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_gst_hst_derived**: 806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://corefour.com/
- **vendor_contact_evidence_url**: https://corefour.com/
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://corefour.com/ (CoreFour Skip to the content CoreFour Menu Home Close Menu Home CoreFour Inc. Developers of the Edsby learning platform for K‑12, and the Unison education data )
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: 2247351 (ON) status Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2247351, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2010-06-15; phone / role e-mails / logo: the vendor's own site, https://corefour.com/ (tools/org_contacts.py, org_extras.py); website: https://corefour.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_incorporation_date**: 2010-06-15
- **vendor_years_in_business**: 16.4 (since 2010-06-15, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2247351, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor CoreFour Inc.
- **award_date**: 2026-11-02
- **contract_link**: https://www.sac.on.ca/community/parents
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 108004144RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: St. Andrew's College — 15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08) — buyer tax no. 108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name) ⏎ SUBMIT TO: ap@sac.on.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: St. Andrew's College (university / college, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own sit
- **invoice_card_json**: {"bill_to": {"legal_name": "St. Andrew's College", "legal_name_is_published": true, "address": "15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "108004144RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (sac.on.ca) + name)", "language": "en"}, "submit_to": {"email": "ap@sac.on.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "15800 Yonge Street Aurora, ON L4G 3H7 (as printed on https://www.sac.on.ca/contact-us, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["ap@sac.on.ca (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.sac.on.ca/contact-us", "quote: \"Phone: (905) 727-3178 Business Office Email: ap@sac.on.ca Phone: (905) 727-3178 Fax: (905) 727-9289 Campus Shop Email: campus.shop@sac.on.ca Phone: (905) 727-31\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Barracuda", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011670"], "buyer_facts": ["address and phone: the buyer's own site, https://www.sac.on.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.sac.on.ca/contact-us | 2026-11-08 | ok |  |  |  | 1 (877) 378-1899 | 15800 Yonge Street Aurora, ON L4G 3H7 |  |  |  |  |

## Buyer site facts (org_extras, sac.on.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: St. Andrew's College
- **legal_name_url**: https://www.sac.on.ca/
- **legal_name_quote**: Home : St. Andrew's College Search Careers Parents SAS Support SAC Admission Academics Arts Athletics Boarding Community Cinema
- **logo_url**: https://bbk12e1-cdn.myschoolcdn.com/ftpimages/842/logo/SAC-Logo.png
- **logo_basis**: logo image in the site header
- **domain**: sac.on.ca
- **key**: lead:79b978669223e9c8
- **name**: St. Andrew's College
- **website**: https://sac.on.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: St. Andrew's College
- **legal_name_stated_url**: https://www.sac.on.ca/privacy
- **legal_name_stated_quote**: Privacy : St. Andrew's College Search Careers Parents SAS Support SAC Admission Academics Arts Athletics Boarding Community Privac
- **mentions**: {'payment_method': {'text': 'Interacts with the website From public sources How We Use Your Information: We will use', 'url': 'https://www.sac.on.ca/privacy', 'quote': 'lowing manner: When a user fills up the registration form or otherwise submits personal information Interacts with the website From public sources How We Use Your Information: We will use the information that we collect about you for the following purposes: Cr'}}

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "15800 Yonge Street, Aurora, ON L4G 3H7", "address_country": "CA", "address_url": "https://www.sac.on.ca/contact-us", "address_method": "pattern", "address_quote": "Community Contact Us Address St. Andrew's College 15800 Yonge Street Aurora, ON L4G 3H7 Canada Tel: 905-727-3178 Email: info@sac.on.ca View Larger Map Click on the ima", "phone": "905-727-3178", "phone_url": "https://www.sac.on.ca/contact-us", "emails": "ap@sac.on.ca; info@sac.on.ca", "emails_url": "https://www.sac.on.ca/contact-us", "domain": "sac.on.ca", "key": "lead:79b978669223e9c8", "name": "St. Andrew's College", "website": "https://sac.on.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, corefour.com)
- **status**: ok
- **pages**: 1
- **v**: 2
- **language**: en
- **domain**: corefour.com
- **key**: vendor:CoreFour Inc.
- **name**: CoreFour Inc.
- **website**: https://corefour.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1", "address_country": "CA", "address_url": "https://corefour.com/", "address_method": "pattern", "address_quote": "United States 01810 68B Leek Crescent, Suite 200 Richmond Hill, Ontario Canada L4B 1H1 28 Devon Street Aro Valley Wellington New Zealand 6021 © 2026 CoreFour Powered", "domain": "corefour.com", "key": "vendor:CoreFour Inc.", "name": "CoreFour Inc.", "website": "https://corefour.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | St. Andrew's College | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=St.%20Andrew%27s%20College | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | St. Andrew's College | Q7586852 | official website on the organisation's domain (https://www.sac.on.ca) + name |  | St. Andrew's College |  | boys' high school; boarding school |  | Canada | 1899-00-00 |  |

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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

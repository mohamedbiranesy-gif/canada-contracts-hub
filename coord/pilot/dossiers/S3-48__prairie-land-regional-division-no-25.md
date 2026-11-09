# S3-48 — Prairie Land Regional Division No. 25 ⇄ CoreFour Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Prairie Land School Division — 670, 101 Palliser Trail, Hanna, AB T0J 1P0 — buyer tax no. 140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
SUBMIT TO: hello@plrd.ab.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Prairie Land Regional Division No. 25 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Can
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 53
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 7
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Prairie Land Regional Division No. 25 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: CoreFour Inc. | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://plrd.ab.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor CoreFour Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:46f528cc608e03d7
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Prairie Land Regional Division No. 25
- **buyer_website**: https://plrd.ab.ca/
- **buyer_address**: 670, 101 Palliser Trail, Hanna, AB T0J 1P0
- **buyer_phone**: 18006013898
- **buyer_contact_evidence_url**: https://plrd.ab.ca/contact-us/
- **buyer_legal_name_as_published**: Prairie Land School Division
- **buyer_bn_as_published**: 140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 140709882RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://plrd.ab.ca/wp-content/uploads/2023/09/PL-Logo-Vector.png
- **buyer_website_status**: site answers
- **buyer_type**: school board / school district (from the organisation's name / web domain)
- **buyer_sector**: education: K-12
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_charity_designation**: C; 0010
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q17514750
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://plrd.ab.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: hello@plrd.ab.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://plrd.ab.ca/about-us/division-contacts/
- **email_evidence_quote**: ivision Contacts Central Services Directory School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax: 403-854-2803 Toll Free: 1-800-601-3898 Administrators Cam McKeage - Superintendent Katherine Mann - Deputy Superintendent Syed R
- **email_evidence_context**: tes, Minutes & Motions Board Highlights Public Disclosure of Expenses Work With Us Contact Division Contacts Division Contacts Central Services Directory School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax: 403-854-2803 Toll Free: 1-800-601-3898 Administrators Cam McKeage - Superintendent Katherine Mann - Deputy Superintendent Syed Raza - Associate Superintendent Mark Nikota - Secretary-Treasurer Administrative Assistant Jennifer Cooper - Administ (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: hello@plrd.ab.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02 | page: https://plrd.ab.ca/about-us/division-contacts/ | quote: "ivision Contacts Central Services Directory School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00087
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:plrdtech@plrd.ab.ca
- **dmarc_record_domain**: plrd.ab.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.google.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prairie Land School Division — 670, 101 Palliser Trail, Hanna, AB T0J 1P0 — buyer tax no. 140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: hello@plrd.ab.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Prairie Land Regional Division No. 25 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Can
- **invoice_card_json**: {"bill_to": {"legal_name": "Prairie Land School Division", "legal_name_is_published": true, "address": "670, 101 Palliser Trail, Hanna, AB T0J 1P0", "address_is_the_invoice_address": false, "tax_number": "140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "hello@plrd.ab.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qs
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
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
- **contract_link**: https://plrd.ab.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 140709882RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (AB) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Prairie Land School Division — 670, 101 Palliser Trail, Hanna, AB T0J 1P0 — buyer tax no. 140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: hello@plrd.ab.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Prairie Land Regional Division No. 25 (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Can
- **invoice_card_json**: {"bill_to": {"legal_name": "Prairie Land School Division", "legal_name_is_published": true, "address": "670, 101 Palliser Trail, Hanna, AB T0J 1P0", "address_is_the_invoice_address": false, "tax_number": "140709882RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "hello@plrd.ab.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of AB on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (AB)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qs
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["hello@plrd.ab.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-02", "page: https://plrd.ab.ca/about-us/division-contacts/", "quote: \"ivision Contacts Central Services Directory School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00087"], "buyer_facts": ["address and phone: the buyer's own site, https://plrd.ab.ca/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: 2247351 (ON) status Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://plrd.ab.ca/about-us/division-contacts/ | 2026-11-08 | ok |  |  |  | 403-854-4481 | 101 Palliser Trail Hanna, AB T0J 1P0 |  |  |  |  |

## Buyer site facts (org_extras, plrd.ab.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Prairie Land School Division Home
- **legal_name_url**: https://plrd.ab.ca/
- **legal_name_quote**: eaching & Learning Culture & Wellness Innovation & Opportunity Engagement & Community Search © 2026 Prairie Land School Division Home 2024/2025 School Calendar Who We Are News & Highlights Teaching and Learning Culture and Wellness I
- **logo_url**: https://plrd.ab.ca/wp-content/uploads/2023/09/PL-Logo-Vector.png
- **logo_basis**: logo image in the site header
- **domain**: plrd.ab.ca
- **key**: lead:46f528cc608e03d7
- **name**: Prairie Land Regional Division No. 25
- **website**: https://plrd.ab.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: EducationalOrganization/Organization
- **jsonld_name**: Violet DEV Testing
- **jsonld_logo**: http://plrd.ab.ca/wp-content/uploads/2023/09/PL-Logo-Vector.png
- **jsonld_url**: https://plrd.ab.ca
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":["EducationalOrganization","Organization"],"@id":"https://plrd.ab.ca/#organization","name":"Violet DEV Testing","url":"https://plrd.ab.ca","logo":{"@type":"ImageObject","@id":"https://plrd.ab.ca/#logo","url":"http://plrd.ab.ca/wp-content/uploads/20
- **jsonld_page**: https://plrd.ab.ca/
- **legal_name_stated**: Prairie Land School Division
- **legal_name_stated_url**: https://plrd.ab.ca/about-us/
- **legal_name_stated_quote**: About Us - Prairie Land School Division Skip to content Next Board Meeting: October 27, 2026 STAFF HUB SHOP Menu Menu Home About Who We Are
- **tel_links**: 18006013898; 403-854-4481; 1-800-601-3898

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "670, 101 Palliser Trail, Hanna, AB T0J 1P0", "address_country": "CA", "address_url": "https://plrd.ab.ca/contact-us/", "address_method": "pattern", "address_quote": "ic School Division School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax: 403-854-2803 Toll Free: 1-800", "phone": "18006013898", "phone_url": "https://plrd.ab.ca/contact-us/", "emails": "hello@plrd.ab.ca", "emails_url": "https://plrd.ab.ca/contact-us/", "domain": "plrd.ab.ca", "key": "lead:46f528cc608e03d7", "name": "Prairie Land Regional Division No. 25", "website": "https://plrd.ab.ca/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Prairie Land Regional Division No. 25 | Q17514750 | official website on the organisation's domain (http://www.plrd.ab.ca) + name |  | Prairie Land Regional Division No. 25 |  |  |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:46f528cc608e03d7",
 "ap_contact_team": {
  "emails": [
   "hello@plrd.ab.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "hello@plrd.ab.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://plrd.ab.ca/",
    "quote": "de to those whose territory we reside on or are visiting. 101 Palliser Trail PO Box 670, Hanna, Alberta T0J 1P0 403-854-4481 1-800-601-3898 hello@plrd.ab.ca Home About Schools Students & Parents Board of Trustees Contact Atrieve Portal Teaching & Learning Culture & Wellness Innovation & Op",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Prairie Land Regional Division No. 25",
    "task_id": "CL-LD-36032"
   },
   {
    "email": "hello@plrd.ab.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://plrd.ab.ca/about-us/division-contacts/",
    "quote": "ivision Contacts Central Services Directory School District Office Box 670, 101 Palliser Trail Hanna, AB T0J 1P0 Phone: 403-854-4481 Email: hello@plrd.ab.ca Fax: 403-854-2803 Toll Free: 1-800-601-3898 Administrators Cam McKeage - Superintendent Katherine Mann - Deputy Superintendent Syed R",
    "retrieved_date": "2026-11-02",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Prairie Land Regional Division No. 25",
    "task_id": "CL-WS-00087"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of plrd.ab.ca (8 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

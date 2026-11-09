# S3-07 — Suspension Bridge ⇄ Shopify Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08) — 260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2
SUBMIT TO: info@sceniccaves.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 53
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Suspension Bridge (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: Shopify Inc. | subject: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://sceniccaves.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:7e5232032d118bc7
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Suspension Bridge
- **buyer_website**: https://sceniccaves.com/
- **buyer_address**: 260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2
- **buyer_contact_evidence_url**: https://sceniccaves.com/pages/contact-us
- **buyer_legal_name_as_published**: Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08)
- **buyer_logo_url**: https://sceniccaves.com/cdn/shop/files/SCNA19_logo-BridgeBL-01_240x.png?v=1613745409
- **buyer_website_status**: site answers
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q114664216; suspension bridge
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://sceniccaves.com/pages/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@sceniccaves.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://sceniccaves.com/pages/contact-us
- **email_evidence_quote**: 2026-2027 WINTER SEASON PASSES ON SALE UNTIL NOVEMBER 30 - CLICK TO PURCHASE OR VIEW MORE DETAILS>>>>> Contact Us General Inquiries Email: info@sceniccaves.com Note: emails are answered during office hours Monday - Friday between 9am - 5pm. If you require immediate attention, please call
- **mailbox_provenance**: info@sceniccaves.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://sceniccaves.com/pages/contact-us | quote: "2026-2027 WINTER SEASON PASSES ON SALE UNTIL NOVEMBER 30 - CLICK TO PURCHASE OR VIEW MORE DETAILS>>>>> Contact Us General Inquiries Email: info@sceniccaves.com " | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-020958
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;rua=mailto:dmarc@sceniccaves.com
- **dmarc_record_domain**: sceniccaves.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:shops.shopify.com include:spf.constantcontact.com include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08) — 260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2 ⏎ SUBMIT TO: info@sceniccaves.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08)", "legal_name_is_published": true, "address": "260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@sceniccaves.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Shopify Inc.", "bn9": "847871746 (Canada's Business Registries, CC 4261607, 2026-11
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Shopify Inc.
- **vendor_legal_name**: Shopify Inc.
- **vendor_trading_name**: Shopify TM (other names in the registry)
- **vendor_registry_id**: Québec REQ (NEQ): 1169259380; 4261607 (CC)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 151 O'Connor St., Ground Floor, Ottawa (Ontario), K2P2L8
- **vendor_neq**: 1169259380 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — CANADA: Loi canadienne sur les sociétés par actions, L.R.C. (1985), c. C-44
- **vendor_activity_code**: CAE 9999 — Fournisseur des services de logiciel pour commerce.
- **vendor_employees_quebec**: De 50 à 99
- **vendor_establishments_quebec**: Shopify TM: 490 rue De La Gauchetière O, Montréal (Québec), H2Z0B3
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada
- **vendor_bn9**: 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://finance.yahoo.com/
- **vendor_logo_url**: https://s.yimg.com/cv/apiv2/default/finance/favicon-180x180.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://finance.yahoo.com/quote/SHOP/profile/ (Shopify Inc. (SHOP) Company Profile & Facts - Yahoo Finance Oops, something went wrong Skip to navigation Skip to main content Skip to right column Home News Fi)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: Québec REQ (NEQ): 1169259380; 4261607 (CC) status Québec REQ (NEQ): Immatriculée (2013-06-21) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, CC 4261607, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2004-09-28; website: https://finance.yahoo.com/; NEQ: 1169259380 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (2013-06-21)
- **vendor_incorporation_date**: 2004-09-28
- **vendor_years_in_business**: 22.1 (since 2004-09-28, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, CC 4261607, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **contract_title**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **contract_description**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://sceniccaves.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08) — 260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2 ⏎ SUBMIT TO: info@sceniccaves.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "Suspension Bridge (label per Wikidata Q114664216, official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name; 2026-11-08)", "legal_name_is_published": true, "address": "260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "info@sceniccaves.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Shopify Inc.", "bn9": "847871746 (Canada's Business Registries, CC 4261607, 2026-11
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@sceniccaves.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://sceniccaves.com/pages/contact-us", "quote: \"2026-2027 WINTER SEASON PASSES ON SALE UNTIL NOVEMBER 30 - CLICK TO PURCHASE OR VIEW MORE DETAILS>>>>> Contact Us General Inquiries Email: info@sceniccaves.com \"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-020958"], "buyer_facts": ["address and phone: the buyer's own site, https://sceniccaves.com/pages/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: Québec REQ (NEQ): 1169259380", "4261607 (CC) status Québec REQ (NEQ): Immatriculée (2013-06-21) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, CC 4261607, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protecte

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://sceniccaves.com/pages/contact-us | 2026-11-06 | blocked |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, sceniccaves.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://sceniccaves.com/cdn/shop/files/SCNA19_logo-BridgeBL-01_240x.png?v=1613745409
- **logo_basis**: logo image in the site header
- **domain**: sceniccaves.com
- **key**: lead:7e5232032d118bc7
- **name**: Suspension Bridge
- **website**: https://sceniccaves.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'interaction on our site', 'url': 'https://sceniccaves.com/pages/privacy-policy', 'quote': 'then enables us to present you with retargeting advertising on other sites based on your previous interaction on our site. The techniques our partners employ do not collect personal information such as your name, email ad'}}

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "260 Scenic Caves Rd, Blue Mountains, Ontario, L9Y 0P2", "address_country": "CA", "address_url": "https://sceniccaves.com/pages/contact-us", "address_method": "pattern", "address_quote": "446-0256 ext. 223 Street Address: 260 Scenic Caves Rd Blue Mountains, Ontario, L9Y 0P2 Canada GPS: 44°29'14.6\"N 80°18'59.7\"W Postal Address: Scenic Caves Nature Adven", "emails": "info@sceniccaves.com", "emails_url": "https://sceniccaves.com/pages/contact-us", "domain": "sceniccaves.com", "key": "lead:7e5232032d118bc7", "name": "Suspension Bridge", "website": "https://sceniccaves.com/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Suspension Bridge | Q114664216 | official website on the organisation's domain (https://sceniccaves.com/products/suspension-bridge) + name |  | Suspension Bridge |  | suspension bridge |  | Canada |  |  |

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

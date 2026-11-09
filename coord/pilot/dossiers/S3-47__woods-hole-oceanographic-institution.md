# S3-47 — Woods Hole Oceanographic Institution ⇄ Shopify Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08) — 266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050 — buyer tax no. 1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: procurement@whoi.edu (purchasing mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order must)
FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380
TAX: tax-exempt organization under Section 501(c)(3) of the Internal Revenue Code as it is organized and operated f (as printed on https://www.whoi.edu/wp-content/up | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
```

## Relationship
- **rank_group**: T2
- **data_quality_score**: 65
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Woods Hole Oceanographic Institution (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: Shopify Inc. | subject: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://shop.whoi.edu/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:9dc5ad4b3713afbb
- **tier**: T
- **grade**: 2
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Woods Hole Oceanographic Institution
- **buyer_website**: https://www.whoi.edu/
- **buyer_address**: 266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050
- **buyer_phone**: (508) 289-4895
- **buyer_contact_evidence_url**: https://www.whoi.edu/giving/contact/
- **buyer_legal_name_as_published**: Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)
- **buyer_bn_as_published**: 1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 100007751RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.whoi.edu/wp-content/uploads/2022/01/WHOI_PrimaryWhiteType®.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/woods-hole-oceanographic-institution/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1404053; research institute; educational institution; nonprofit organization
- **buyer_founded**: 1930-00-00 (Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 215727317 Q4917; 261786466 Q4917; 203711976 Q4917; 204987861 Q4917; 353851530 Q4917; 294655196 Q4917; 345864759 Q4917; 2 (Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)
- **buyer_legal_form**: 501(c)(3) organization (Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.whoi.edu/giving/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: tax-exempt organization under Section 501(c)(3) of the Internal Revenue Code as it is organized and operated f (as printed on https://www.whoi.edu/wp-content/uploads/2023/08/2022-Audited-Financial-Statement.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: procurement@whoi.edu
- **email_type**: purchasing
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); purchasing mailbox
- **email_evidence_url**: https://www.whoi.edu/who-we-are/work-with-whoi/vendors-contractors/
- **email_evidence_quote**: artment for assistance. WHOI Procurement Department 266 Woods Hole Road MS #1 Woods Hole, MA tel: (508) 289-2371 fax: (508) 457-2192 email: procurement@whoi.edu website: https://www.whoi.edu/procurement (Photo by Jayne Doucette, Woods Hole Oceanographic Institution) 266 Woods Hole Road, Wo
- **email_evidence_context**: g with WHOI or you have an existing relationship with the Institution, please contact our WHOI Procurement department for assistance. WHOI Procurement Department 266 Woods Hole Road MS #1 Woods Hole, MA tel: (508) 289-2371 fax: (508) 457-2192 email: procurement@whoi.edu website: https://www.whoi.edu/procurement (Photo by Jayne Doucette, Woods Hole Oceanographic Institution) 266 Woods Hole Road, Woods Hole, MA 02543-1050 Woods Hole Oceanographic Institution is a 501 (c)(3) organization. We are proud to be recognized (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: procurement@whoi.edu (purchasing) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.whoi.edu/who-we-are/work-with-whoi/vendors-contractors/ | quote: "artment for assistance. WHOI Procurement Department 266 Woods Hole Road MS #1 Woods Hole, MA tel: (508) 289-2371 fax: (508) 457-2192 email: procurement@whoi.edu" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-01092
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; np=none; sp=none; rua=mailto:82a5c8216791.a@dmarcinput.com; ruf=mailto:82a5c8216791.f@dmarcinput.com; fo=1; psd=u; t=n
- **dmarc_record_domain**: whoi.edu
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:_s00819647.autospf.email -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **po_required_as_published**: purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-services/shared-equipment/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-services/shared-equipment/, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08) — 266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050 — buyer tax no. 1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: procurement@whoi.edu (purchasing mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order must) ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: tax-exempt organization under Section 501(c)(3) of the Internal Revenue Code as it is organized and operated f (as printed on https://www.whoi.edu/wp-content/up | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050", "address_is_the_invoice_address": false, "tax_number": "1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "procurement@whoi.edu", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-services/shared-equipment/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order must) (as printed on https://www.wh
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-servic)

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
- **po_required_as_published**: purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-services/shared-equipment/, re-read 2026-11-08)
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **contract_title**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **contract_description**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://shop.whoi.edu/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 100007751RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08) — 266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050 — buyer tax no. 1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: procurement@whoi.edu (purchasing mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order must) ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: tax-exempt organization under Section 501(c)(3) of the Internal Revenue Code as it is organized and operated f (as printed on https://www.whoi.edu/wp-content/up | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "Woods Hole Oceanographic Institution (label per Wikidata Q1404053, official website on the organisation's domain (https://www.whoi.edu/) + name; 2026-11-08)", "legal_name_is_published": true, "address": "266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050", "address_is_the_invoice_address": false, "tax_number": "1000077511 (recipient_business_number in the federal grants & contributions disclosure, 2 agreement(s), last 2020-09-08; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "procurement@whoi.edu", "email_type": "purchasing", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order must) (as printed on https://www.whoi.edu/what-we-do/explore/ships/marine-facilities-operations/marine-facilities-operations-support-services/shared-equipment/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order must) (as printed on https://www.wh
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **facts_provenance_json**: {"mailbox": ["procurement@whoi.edu (purchasing)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.whoi.edu/who-we-are/work-with-whoi/vendors-contractors/", "quote: \"artment for assistance. WHOI Procurement Department 266 Woods Hole Road MS #1 Woods Hole, MA tel: (508) 289-2371 fax: (508) 457-2192 email: procurement@whoi.edu\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-01092"], "buyer_facts": ["address and phone: the buyer's own site, https://www.whoi.edu/giving/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry ide

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.whoi.edu/who-we-are/work-with-whoi/vendors-contractors/ | 2026-11-08 | ok |  |  |  | (508) 289-2371 | 266 Woods Hole Road, Woods Hole, MA 02543-1050 |  |  |  |  |

## Buyer site facts (org_extras, whoi.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.whoi.edu/wp-content/uploads/2022/01/WHOI_PrimaryWhiteType®.png
- **logo_basis**: logo image in the site header
- **domain**: whoi.edu
- **key**: lead:9dc5ad4b3713afbb
- **name**: Woods Hole Oceanographic Institution
- **website**: https://whoi.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Woods Hole Oceanographic Institution
- **jsonld_logo**: https://www.whoi.edu/wp-content/uploads/2022/05/whoi-square-logo.png
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "WebSite", "url" : "https:\/\/www.whoi.edu", "potentialAction": { "@type": "SearchAction", "target": "https:\/\/www.whoi.edu\/?s={search_term_string}", "query-input": "required name=search_term_string" } }
- **jsonld_page**: https://www.whoi.edu/
- **legal_name_stated**: National Science Foundation
- **legal_name_stated_url**: https://www.whoi.edu/who-we-are/about-us/history-legacy/
- **legal_name_stated_quote**: making observations on trade wind physics and dynamics. In 1950, the U.S. Congress established the National Science Foundation (NSF) to promote national efforts in science and engineering. WHOI’s first support from NSF came in
- **mentions**: {'payment_method': {'text': 'Interactive Science Maps READ ABOUT OUR LATEST RESEARCH News Give Now GIVE NOW Ways to', 'url': 'https://www.whoi.edu/', 'quote': 'cean blue? What causes ocean waves? How is beach sand created? Multimedia Images Video Illustration Interactive Science Maps READ ABOUT OUR LATEST RESEARCH News Give Now GIVE NOW Ways to give Learn More --> Leadership & Giving Circles 1930 Society Ocean Partne'}}
- **linkedin_url**: https://www.linkedin.com/school/woods-hole-oceanographic-institution/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "266 Woods Hole Road, MS #40, Woods Hole, MA 02543-1050", "address_country": "US", "address_url": "https://www.whoi.edu/giving/contact/", "address_method": "pattern", "address_quote": "of U.S. charities. WHOI Development Office Woods Hole Oceanographic Institution 266 Woods Hole Road, MS #40 Woods Hole, MA 02543-1050 Phone: (508) 289-4895 Fax: 508-457-2167 Email", "phone": "(508) 289-4895", "phone_url": "https://www.whoi.edu/giving/contact/", "emails": "information@whoi.edu; procurement@whoi.edu", "emails_url": "https://www.whoi.edu/who-we-are/contact-us/", "domain": "whoi.edu", "key": "lead:9dc5ad4b3713afbb", "name": "Woods Hole Oceanographic Institution", "website": "https://whoi.edu/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Woods Hole Oceanographic Institution | Q1404053 | official website on the organisation's domain (https://www.whoi.edu/) + name |  | Woods Hole Oceanographic Institution | Institut océanographique de Woods Hole | research institute; educational institution; nonprofit organization | 501(c)(3) organization | United States | 1930-00-00 | Woods Hole |

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
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

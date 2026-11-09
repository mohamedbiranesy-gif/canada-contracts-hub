# S3-42 — Frosteam ⇄ Shopify Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: 9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08) — 202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/)
SUBMIT TO: hello@thefrosteam.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-r
DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 56
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Frosteam (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: Shopify Inc. | subject: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://thefrosteam.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:597846ec1b551888
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Frosteam
- **buyer_website**: https://thefrosteam.com/
- **buyer_address**: 202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/)
- **buyer_phone**: +18077703165 (tel: link on https://thefrosteam.com/)
- **buyer_contact_evidence_url**: https://thefrosteam.com/pages/contact
- **buyer_legal_name_as_published**: 9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08)
- **buyer_logo_url**: https://thefrosteam.com/cdn/shop/files/F_Logo_Horizontal_Noir.png?v=1773271287&width=4432
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/the-frosteam/
- **buyer_type**: company (private sector) (from the organisation's name / web domain)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q141818757; business
- **buyer_founded**: 2024-10-22 (Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08)
- **buyer_legal_form**: Quebec business corporation (Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://thefrosteam.com/pages/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: hello@thefrosteam.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://thefrosteam.com/pages/policies
- **email_evidence_quote**: erated by 9527-3165 Québec Inc., a Canadian company headquartered at 17390 rue Victor, Suite 202, Mirabel, Québec J7J 1A7, Canada. Support: hello@thefrosteam.com · +1 (807) 770-3165 · Monday to Friday, 9:00 a.m. – 5:00 p.m. Eastern. Questions about a policy If anything on these pages is un
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: hello@thefrosteam.com (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://thefrosteam.com/pages/policies | quote: "erated by 9527-3165 Québec Inc., a Canadian company headquartered at 17390 rue Victor, Suite 202, Mirabel, Québec J7J 1A7, Canada. Support: hello@thefrosteam.co" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00220
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; sp=quarantine; pct=100; adkim=r; aspf=r; rua=mailto:aa9b9b155c554d5db585add5e377c6c4@dmarc-reports.cloudflare.net,mailto:586d22e616@rua.easydmarc.us,mailto:dmarc_aggregate_analyser+d2fa3c24ee283b7c8e4c79d1743d0b5d@zerobounce.net
- **dmarc_record_domain**: thefrosteam.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.google.com ~all
- **mta_sts**: yes (v=STSv1; id=2026091201)
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:tlsrpt-tkn_a582df2918e2150212dfd4d7367ce4e3@mailsrv1.capt)
- **bimi**: yes (v=BIMI1; l=https://bimi.thefrosteam.com/9527-3165_quebec_inc_1551866320.svg; a=h)
- **payment_terms_as_published**: 14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08) — 202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/) ⏎ SUBMIT TO: hello@thefrosteam.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-r ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08)", "legal_name_is_published": true, "address": "202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "hello@thefrosteam.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": fals
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

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
- **contract_link**: https://thefrosteam.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08) — 202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/) ⏎ SUBMIT TO: hello@thefrosteam.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-r ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "9527-3165 Québec inc. (official name per Wikidata Q141818757, official website on the organisation's domain (https://thefrosteam.com) + name; 2026-11-08)", "legal_name_is_published": true, "address": "202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA (schema.org JSON-LD PostalAddress on https://thefrosteam.com/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "hello@thefrosteam.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "14 jours suivant la réception (as printed on https://thefrosteam.com/fr/policies/refund-policy, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": fals
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["hello@thefrosteam.com (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://thefrosteam.com/pages/policies", "quote: \"erated by 9527-3165 Québec Inc., a Canadian company headquartered at 17390 rue Victor, Suite 202, Mirabel, Québec J7J 1A7, Canada. Support: hello@thefrosteam.co\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00220"], "buyer_facts": ["address and phone: the buyer's own site, https://thefrosteam.com/pages/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: Québec REQ (NEQ): 1169259380", "4261607 (CC) status Québec REQ (NEQ): Immatriculée (2013-06-21) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada'

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://thefrosteam.com | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, thefrosteam.com)
- **status**: ok
- **pages**: 5
- **language**: en
- **logo_url**: https://thefrosteam.com/cdn/shop/files/F_Logo_Horizontal_Noir.png?v=1773271287&width=4432
- **logo_basis**: logo image in the site header
- **domain**: thefrosteam.com
- **key**: lead:597846ec1b551888
- **name**: Frosteam
- **website**: https://thefrosteam.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: OnlineStore
- **jsonld_name**: Frosteam
- **jsonld_legal_name**: 9527-3165 Québec inc.
- **jsonld_alternate_name**: The Frosteam
- **jsonld_address**: 202-17390 rue Victor, Mirabel, QC, J7J 1A7, CA
- **jsonld_logo**: https://thefrosteam.com/cdn/shop/files/bimi-svg-tiny-12-ps_2_Logo.svg?v=1782996548&width=512&format=png
- **jsonld_url**: https://thefrosteam.com/
- **jsonld_founding_date**: 2024-10-22
- **jsonld_duns**: 243336875
- **jsonld_lei**: 9845004OA55C12E3D598
- **jsonld_same_as**: https://www.linkedin.com/company/the-frosteam/; https://www.instagram.com/the.frosteam/; https://www.facebook.com/the.frosteam/; https://www.youtube.com/@TheFrosteam; https://www.tiktok.com/@the.frosteam; https://x.com/Thefrosteam; https://www.threads.com/@the.frosteam; https://www.pinterest.com/The_Frosteam/; https://www.snapchat.com/@the_frosteam; https://www.crunchbase.com/organization/the-fros
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "OnlineStore", "@id": "https://thefrosteam.com/#organization","hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "@id": "https://thefrosteam.com/#return-policy", "applicableCountry": ["CA","US","MX"], "returnPolicyCategory": "https://schema.org
- **jsonld_page**: https://thefrosteam.com/
- **mentions**: {'payment_method': {'text': 'interact with the Services, where you live, and as permitted or required by applicable', 'url': 'https://thefrosteam.com/policies/privacy-policy', 'quote': 'rsonal information, including inferences drawn from this personal information, depending on how you interact with the Services, where you live, and as permitted or required by applicable law: Contact details including your name, address, billing address, shipp'}}
- **linkedin_url**: https://www.linkedin.com/company/the-frosteam/
- **tel_links**: +18077703165

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "202-17390 rue Victor, Mirabel, QC, J7J 1A7", "address_country": "CA", "address_url": "https://thefrosteam.com/pages/contact", "address_method": "json-ld", "address_quote": "770-3165 Business Address Frosteam™ 17390 Rue Victor, Suite 202 Mirabel, Quebec J7J 1A7 Canada 📍 Get Directions on Google Maps 📧 Email Us 📞 Call Us Business Hours Mond", "phone": "+18077703165", "phone_url": "https://thefrosteam.com/pages/contact", "emails": "hello@thefrosteam.com; sales@thefrosteam.com", "emails_url": "https://thefrosteam.com/pages/contact", "domain": "thefrosteam.com", "key": "lead:597846ec1b551888", "name": "Frosteam", "website": "https://thefrosteam.com/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Frosteam | Q141818757 | official website on the organisation's domain (https://thefrosteam.com) + name | 9527-3165 Québec inc. [fr] | Frosteam | Frosteam | business | Quebec business corporation | Canada | 2024-10-22 | Mirabel |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:597846ec1b551888",
 "ap_contact_team": {
  "emails": [
   "hello@thefrosteam.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "hello@thefrosteam.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://thefrosteam.com/pages/policies",
    "quote": "erated by 9527-3165 Québec Inc., a Canadian company headquartered at 17390 rue Victor, Suite 202, Mirabel, Québec J7J 1A7, Canada. Support: hello@thefrosteam.com · +1 (807) 770-3165 · Monday to Friday, 9:00 a.m. – 5:00 p.m. Eastern. Questions about a policy If anything on these pages is un",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Frosteam",
    "task_id": "CL-WS-00220"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
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

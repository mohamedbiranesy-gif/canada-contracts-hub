# S3-25 — Wedance ⇄ Shopify Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: International Dance Shoes (stated on https://wedance.ca/fr) — 122 Castlegreen Private, Ottawa, ON K1T 3N2 — buyer tax no. 763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service)
SUBMIT TO: contact@wedance.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: indiquant votre numéro de commande)
FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-1
DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 58
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Wedance (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: Shopify Inc. | subject: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://wedance.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=United States or Canada Shopify Inc., a Canadian corporation 151 O'Connor Street, Ground floor, Ottawa, Ontario, K2P 2L8, Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:a836fdb0c373b6d0
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Wedance
- **buyer_website**: https://wedance.ca/
- **buyer_address**: 122 Castlegreen Private, Ottawa, ON K1T 3N2
- **buyer_phone**: (343) 988-5981
- **buyer_contact_evidence_url**: https://wedance.ca/fr/policies/contact-information
- **buyer_legal_name_as_published**: International Dance Shoes (stated on https://wedance.ca/fr)
- **buyer_bn_as_published**: 763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 763871829RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://wedance.ca/cdn/shop/files/Wedance_Rectangular_Logo_Gold_6kb.webp?v=1749688731&width=600
- **buyer_website_status**: site answers
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://wedance.ca/fr/policies/contact-information (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: contact@wedance.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://wedance.ca/fr
- **email_evidence_quote**: de danse Soirées de danse Guides Programme partenaire À propos À propos Nous visiter Remboursement Conditions Confidentialité Coordonnées : contact@wedance.ca Ottawa (343) 988-5981 Showroom: 122 Castlegreen Private Hours: Mon–Fri & Sun 7:30 AM–9 PM Sat 4–9 PM · earlier by appointment Book
- **email_evidence_context**: e Guide des tailles FAQ Récompenses Livraison et retours Nous joindre Ressources Écoles de danse Compétitions de danse Soirées de danse Guides Programme partenaire À propos À propos Nous visiter Remboursement Conditions Confidentialité Coordonnées : contact@wedance.ca Ottawa (343) 988-5981 Showroom: 122 Castlegreen Private Hours: Mon–Fri & Sun 7:30 AM–9 PM Sat 4–9 PM · earlier by appointment Book your appointment Montréal (514) 638-1221 Showroom: 4420 Chemin de la Côte-de-Liesse, #204 Hours: Mon, Wed & Thu 5:45–7 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: contact@wedance.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://wedance.ca/fr | quote: "de danse Soirées de danse Guides Programme partenaire À propos À propos Nous visiter Remboursement Conditions Confidentialité Coordonnées : contact@wedance.ca O" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Zoho | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-OS906-004669
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Zoho
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:ba1a2df86229445d80e881e9082d1044@dmarc-reports.cloudflare.net;
- **dmarc_record_domain**: wedance.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:zcsend.ca include:zohocloud.ca ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: 65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: International Dance Shoes (stated on https://wedance.ca/fr) — 122 Castlegreen Private, Ottawa, ON K1T 3N2 — buyer tax no. 763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service) ⏎ SUBMIT TO: contact@wedance.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: indiquant votre numéro de commande) ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-1 ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "International Dance Shoes (stated on https://wedance.ca/fr)", "legal_name_is_published": true, "address": "122 Castlegreen Private, Ottawa, ON K1T 3N2", "address_is_the_invoice_address": false, "tax_number": "763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service)", "language": "en"}, "submit_to": {"email": "contact@wedance.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08))"}, "terms": {"payment_terms": "65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08))

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
- **po_required_as_published**: purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08)
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor Shopify Inc.
- **contract_title**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **contract_description**: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada (the record's title; the source publishes no separate description)
- **award_date**: 2026-11-02
- **contract_link**: https://wedance.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 763871829RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 847871746RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: International Dance Shoes (stated on https://wedance.ca/fr) — 122 Castlegreen Private, Ottawa, ON K1T 3N2 — buyer tax no. 763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service) ⏎ SUBMIT TO: contact@wedance.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: indiquant votre numéro de commande) ⏎ FROM / REMIT TO: Shopify Inc. — 490 rue De La Gauchetière Ouest, Montréal, QC, H2Z1E3, CAN | GST/HST 847871746 (Canada's Business Registries, CC 4261607, 2026-11-08)RT0001 (account derived from the BN9) | NEQ 1169259380 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: 65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-1 ⏎ DESCRIPTION: Shopify Inc. contracts only with merchants whose billing address is in the United States or Canada
- **invoice_card_json**: {"bill_to": {"legal_name": "International Dance Shoes (stated on https://wedance.ca/fr)", "legal_name_is_published": true, "address": "122 Castlegreen Private, Ottawa, ON K1T 3N2", "address_is_the_invoice_address": false, "tax_number": "763871829  (as printed: Numéro d’entreprise : 763871829; https://wedance.ca/fr/policies/terms-of-service)", "language": "en"}, "submit_to": {"email": "contact@wedance.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: indiquant votre numéro de commande) (as printed on https://wedance.ca/fr/policies/shipping-policy, re-read 2026-11-08))"}, "terms": {"payment_terms": "65 jours après réception (as printed on https://wedance.ca/fr/policies/refund-policy, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: invoicing / AP mailbox; finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general)
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **facts_provenance_json**: {"mailbox": ["contact@wedance.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://wedance.ca/fr", "quote: \"de danse Soirées de danse Guides Programme partenaire À propos À propos Nous visiter Remboursement Conditions Confidentialité Coordonnées : contact@wedance.ca O\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Zoho", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-OS906-004669"], "buyer_facts": ["address and phone: the buyer's own site, https://wedance.ca/fr/policies/contact-information (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ v

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://wedance.ca/fr | 2026-11-08 | ok |  |  |  | (343) 988-5981 |  |  |  |  |  |

## Buyer site facts (org_extras, wedance.ca)
- **status**: ok
- **pages**: 6
- **language**: fr
- **logo_url**: https://wedance.ca/cdn/shop/files/Wedance_Rectangular_Logo_Gold_6kb.webp?v=1749688731&width=600
- **logo_basis**: logo image on the site
- **domain**: wedance.ca
- **key**: lead:a836fdb0c373b6d0
- **name**: Wedance
- **website**: https://wedance.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Wedance
- **jsonld_logo**: https://wedance.ca/cdn/shop/files/Wedance_Rectangular_Logo_Gold_6kb.webp?v=1749688731&width=600
- **jsonld_url**: https://wedance.ca
- **jsonld_same_as**: https://www.facebook.com/wedance.ca; https://www.instagram.com/wedance.ca
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "Organization", "@id": "https://wedance.ca/#organization", "name": "Wedance", "url": "https://wedance.ca","logo": "https://wedance.ca/cdn/shop/files/Wedance_Rectangular_Logo_Gold_6kb.webp?v=1749688731&width=600" ,"image": "https://wedance.ca
- **jsonld_page**: https://wedance.ca/fr
- **legal_name_stated**: International Dance Shoes
- **legal_name_stated_url**: https://wedance.ca/fr
- **legal_name_stated_quote**: ants, et des chaussures de pratique confortables. Nous offrons des marques de confiance, dont AIDA, International Dance Shoes, Freed of London, BD Dance, Candy, Rosso Latino, Zym, Primabella, Primavera, Aery Jo, Starbody et b
- **mentions**: {'payment_method': {'text': 'interactive Magasiner Nouveautés Prêt à expédier Solde Chaussures de danse à pied large', 'url': 'https://wedance.ca/fr', 'quote': '00 CAD Prix unitaire / par Trouvez nos boutiques — Ottawa et Montréal Cliquez pour charger la carte interactive Magasiner Nouveautés Prêt à expédier Solde Chaussures de danse à pied large Cartes-cadeaux Aide Guide des tailles FAQ Récompenses Livraison et retou'}}
- **tel_links**: +13439885981; +15146381221
- **bn**: 763871829
- **bn_label**: Numéro d’entreprise : 763871829
- **bn_url**: https://wedance.ca/fr/policies/terms-of-service
- **bn_quote**: ivate, Ottawa, ON K1T 3N2, Canada. Numéro de téléphone : +13439885981 Courriel : contact@wedance.ca Numéro d’entreprise : 763871829 Trouvez nos boutiques — Ottawa et Montréal Cliquez pour charger la carte interactive Magasiner Nouve

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "(343) 988-5981", "phone_url": "https://wedance.ca/fr/pages/contact", "emails": "contact@wedance.ca", "emails_url": "https://wedance.ca/fr/pages/contact", "address": "122 Castlegreen Private, Ottawa, ON K1T 3N2", "address_country": "CA", "address_url": "https://wedance.ca/fr/policies/contact-information", "address_method": "pattern", "address_quote": "iel : contact@wedance.ca Adresse physique : 122 Castlegreen Private, Ottawa, ON K1T 3N2, Canada Trouvez nos boutiques — Ottawa et Montréal Cliquez pour charger la cart", "domain": "wedance.ca", "key": "lead:a836fdb0c373b6d0", "name": "Wedance", "website": "https://wedance.ca/", "kind": "buyer", "date": "2026-11-03"}

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
| b | Wedance |  |  |  |  |  |  |  |  |  |  |

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

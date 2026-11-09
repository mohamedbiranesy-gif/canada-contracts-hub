# S5-31 — Telefilm Canada ⇄ P & R Desjardins Construction Inc

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08) — 700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada
SUBMIT TO: payment.paiement@telefilm.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: contract 20250214 (an_contract_number); tender 20250214 (an_solicitation_number) | PO rule: not published
FROM / REMIT TO: P. & R. DESJARDINS CONSTRUCTION INC. — 1777 Begin, Saint-Laurent, Quebec, H4R 2B5 | GST/HST number not public | NEQ 1143656032
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work
DESCRIPTION: Request for proposal Construction Manager | AMOUNT: 4,129,184.72 CAD
```

## Relationship
- **rank_group**: A3
- **data_quality_score**: 82
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 5
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Telefilm Canada (organisation (type not stated in the record), FED) — public contract / purchase award with a published end date (dated record): P & R Desjardins Construction Inc | subject: Request for proposal Construction Manager | contract number: 20250214 (an_contract_number); cb-665-17873129 (tn_reference_number); cb-431-1808606 (an_reference_numbers); cb-431-1808606 (an_reference_number_latest) | solicitation: 20250214 (an_solicitation_number); 20250214 (tn_solicitation_number) | all identifiers: {"an_reference_number_latest": "cb-431-1808606", "an_reference_numbers": ["cb-431-1808606"], "an_contract_number": "20250214", "an_solicitation_number": "20250214", "tn_reference_number": "cb-665-17873129", "tn_solicitation_number": "20250214"} | value: 4129184.72 CAD | awarded 2025-05-15, start 2025-05-15, end 2026-11-17 | published by: CanadaBuys award notices (+ CanadaBuys tender notice) | record: https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-431-1808606 | vendor in Canada because: supplierAddressCountry-fournisseurAdressePays-eng = 'Canada' | status rule: active (published end date today or later) | this buyer has 1 records with Canada-located vendors (1 distinct vendors; 0 in the last 12 months; latest 2025-05-15)
- **how_relationship_was_found**: the award record was harvested from the public procurement source named in `source` (scripts/<source> pipeline), matched to the buyer by its canonical name/key, and the vendor's Canada location read from the source's own vendor address/country field (`vendor_country_basis`)
- **keys**: b:1382482eb35e183b
- **tier**: A
- **grade**: 3
- **records_with_this_vendor**: 1

## Buyer
- **buyer**: Telefilm Canada
- **buyer_website**: https://telefilm.ca/en/?q=en
- **buyer_address**: 700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada
- **buyer_phone**: 1 800-567-0890
- **buyer_contact_evidence_url**: https://telefilm.ca/en/who-we-are/contact-us
- **buyer_legal_name_as_published**: TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08)
- **buyer_logo_url**: https://telefilm.ca/wp-content/themes/tel11799-2026-telefilm.ca/assets_dist/images/brand_logo-telefilm-canada_neg.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://ca.linkedin.com/company/telefilm-canada
- **buyer_registry_id**: NEQ 8813532965 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://telefilm.ca/en/who-we-are/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_esignature_preference**: electronic signature option will be implemented gradually (as printed on https://telefilm.ca/wp-content/uploads/guide-how-to-navigate-dialogue.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: payment.paiement@telefilm.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html
- **email_evidence_quote**: payment.paiement@telefilm.ca
- **email_evidence_context**: ail: fe-cdfs-supplierid@statcan.gc.ca Superintendent of Financial Institutions (Office of the) Email: finance@osfi-bsif.gc.ca Supreme Court of Canada Accounting Telephone: 613-996-7663 Email: accounting.comptabilite@scc-csc.ca Telefilm Canada Email: payment.paiement@telefilm.ca Transport Canada Telephone: 1-888-639-2199 , option #2 Email: tc.apsvendors-uccfournisseurs.tc@tc.gc.ca Transportation Safety Board of Canada Financial Services Telephone: 819‑953‑1645 Email: finance@tsb-bst.gc.ca Treasury Board of Canada Secretaria (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: payment.paiement@telefilm.ca (finance/accounting dept or supplier-payment office) | mailbox from the dataset build, re-submitted so the referee re-fetched the page on 2026-11-04 | page: https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html | quote: "payment.paiement@telefilm.ca" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_dsenrich01.csv task CL-DS-00050
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; adkim=s; aspf=s; fo=1:d:s; pct=100; ri=1200; rua=mailto:dmarc@telefilm.ca; ruf=mailto:dmarc@telefilm.ca;
- **dmarc_record_domain**: telefilm.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 mx a ip4:72.0.195.150 ip4:198.103.159.6 ip4:52.60.72.30 ip4:40.86.245.224 ip4:52.60.97.65 ip4:52.235.40.191 ip4:99.79.102.254 ip4:205.193.149.116 ip4:184.72.123.171 ip4:108.163.168.146 ip4:52.237.19.125 ip4:52.235.42.137 ip4:198.103.155.75 ip4:3.98.218.104 ip4:35.183.211.105 ip4:3.99.96.22 ip
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 613-996-7663 (as printed on https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html, re-read 2026-11-08)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the Crown must pay a proper invoice no later than the 28th day after receiving it — Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387, s. 9(2), in force 2023-12-09 (https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html, read 2026-11-08: "no later than the 28th day after the day on which the proper invoice is received"); applies only to construction work for a federal project under that Act
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "613-996-7663 (as printed on https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html, re-read 2026-11-08)"}
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08) — 700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada ⏎ SUBMIT TO: payment.paiement@telefilm.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract 20250214 (an_contract_number); tender 20250214 (an_solicitation_number) | PO rule: not published ⏎ FROM / REMIT TO: P. & R. DESJARDINS CONSTRUCTION INC. — 1777 Begin, Saint-Laurent, Quebec, H4R 2B5 | GST/HST number not public | NEQ 1143656032 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Request for proposal Construction Manager | AMOUNT: 4,129,184.72 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08)", "legal_name_is_published": true, "address": "700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada", "address_is_the_invoice_address": false, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "payment.paiement@telefilm.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20250214 (an_contract_number); cb-665-17873129 (tn_reference_number); cb-431-1808606 (an_reference_numbers); cb-431-1808606 (an_reference_number_latest)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20250214 (an_contract_number) — source canada_federal"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the Crown must pay a proper invoice no later than the 28th day after receiving it — Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387, s. 9(2), in force 2023-12-09 (https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html, read 2026-11-08: \"no late
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)
- **invoice_reference_hint**: contract or agreement number: 20250214 (an_contract_number) — source canada_federal

## Vendor
- **vendor**: P & R Desjardins Construction Inc
- **vendor_legal_name**: P. & R. DESJARDINS CONSTRUCTION INC.
- **vendor_registry_id**: Québec REQ (NEQ): 1143656032; 1143656032 (QC)
- **vendor_registry_url**: https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises
- **vendor_registered_address**: 1777 rue Bégin, Montréal (Québec), H4R2B5
- **vendor_neq**: 1143656032 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_legal_form**: Société par actions ou compagnie — QUÉBEC : Loi sur les sociétés par actions (RLRQ, C. S-31.1)
- **vendor_activity_code**: CAE 4011 — ENTREPRENEUR GÉNÉRAL EN CONSTRUCTION
- **vendor_employees_quebec**: De 26 à 49
- **vendor_last_annual_filing**: REQ annual declaration 2025
- **vendor_address**: 1777 Begin, Saint-Laurent, Quebec, H4R 2B5
- **vendor_country_basis**: supplierAddressCountry-fournisseurAdressePays-eng = 'Canada'
- **vendor_website**: https://prdesjardins.com/
- **vendor_emails**: info@prdesjardins.com
- **vendor_contact_evidence_url**: https://prdesjardins.com/fr/contact/
- **vendor_logo_url**: https://prdesjardins.com/content/themes/prd/public/images/logo.svg
- **vendor_website_status**: site answers
- **vendor_contacts_found_by**: gemini lane, referee-verified on https://prdesjardins.com/fr/contact/
- **vendor_facts_provenance**: name and address: the record's vendor block (CanadaBuys award notices (+ CanadaBuys tender notice)); registry identity: Québec REQ (NEQ): 1143656032; 1143656032 (QC) status Québec REQ (NEQ): Immatriculée (1995-03-15) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; exact); incorporated / registered: 1960-09-23; phone / role e-mails / logo: the vendor's own site, https://prdesjardins.com/fr/contact/ (tools/org_contacts.py, org_extras.py); role / billing mailboxes researched by the gemini lane, referee-verified on https://prdesjardins.com/fr/contact/; website: https://prdesjardins.com/ (site answers); NEQ: 1143656032 (Registraire des entreprises du Québec, bulk register https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises; retrieved 2026-10-25)
- **vendor_concentration_top_share**: P & R Desjardins Construction Inc: 100% of 1 records
- **vendor_registry_status**: Québec REQ (NEQ): Immatriculée (1995-03-15)
- **vendor_registry_match_level**: exact
- **vendor_incorporation_date**: 1960-09-23
- **vendor_years_in_business**: 66.1 (since 1960-09-23, registry date)

## Contract
- **contract_status**: active (published end date today or later)
- **contract_reference**: {"an_reference_number_latest": "cb-431-1808606", "an_reference_numbers": ["cb-431-1808606"], "an_contract_number": "20250214", "an_solicitation_number": "20250214", "tn_reference_number": "cb-665-17873129", "tn_solicitation_number": "20250214"}
- **contract_title**: Request for proposal Construction Manager
- **commodity**: 72100000 | 72120000 | 72130000 Building and facility maintenance and repair services | Nonresidential building construction services | General building construc
- **contract_description**: Following the pre-qualification call for tenders, Telefilm Canada is currently seeking to select its construction manager who will carry out the construction and fit-up of its future offices through this competitive process. …
- **contract_or_agreement_number**: 20250214 (an_contract_number); cb-665-17873129 (tn_reference_number); cb-431-1808606 (an_reference_numbers); cb-431-1808606 (an_reference_number_latest)
- **solicitation_or_tender_number**: 20250214 (an_solicitation_number); 20250214 (tn_solicitation_number)
- **commodity_codes**: UNSPSC 72100000, 72120000, 72130000 (Building and facility maintenance and repair services | Nonresidential building )
- **contract_value**: 4129184.72
- **currency**: CAD
- **award_date**: 2025-05-15
- **start_date**: 2025-05-15
- **end_date**: 2026-11-17
- **contract_link**: https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-431-1808606
- **source**: CanadaBuys award notices (+ CanadaBuys tender notice)
- **contracts_with_canadian_suppliers**: 1
- **records_last_12_months**: 0
- **record_sources**: CanadaBuys award notices (+ CanadaBuys tender notice) (1)
- **records_with_this_vendor**: 1
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: Building and facility maintenance and repair services | Nonr (1)

## Tax / currency / terms (derived)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the Crown must pay a proper invoice no later than the 28th day after receiving it — Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387, s. 9(2), in force 2023-12-09 (https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html, read 2026-11-08: "no later than the 28th day after the day on which the proper invoice is received"); applies only to construction work for a federal project under that Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08) — 700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada ⏎ SUBMIT TO: payment.paiement@telefilm.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: contract 20250214 (an_contract_number); tender 20250214 (an_solicitation_number) | PO rule: not published ⏎ FROM / REMIT TO: P. & R. DESJARDINS CONSTRUCTION INC. — 1777 Begin, Saint-Laurent, Quebec, H4R 2B5 | GST/HST number not public | NEQ 1143656032 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: CAD | TERMS: statutory default for construction work ⏎ DESCRIPTION: Request for proposal Construction Manager | AMOUNT: 4,129,184.72 CAD
- **invoice_card_json**: {"bill_to": {"legal_name": "TÉLÉFILM CANADA (as registered: Registraire des entreprises du Québec (open data), NEQ 8813532965, 2026-11-08)", "legal_name_is_published": true, "address": "700 boulevard René Lévesque Ouest, Montreal, Quebec, H3B 1X8, Canada", "address_is_the_invoice_address": false, "tax_number": "", "language": "en-fr (bilingual body: federal / New Brunswick; use the language of its invoicing page: en)"}, "submit_to": {"email": "payment.paiement@telefilm.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "20250214 (an_contract_number); cb-665-17873129 (tn_reference_number); cb-431-1808606 (an_reference_numbers); cb-431-1808606 (an_reference_number_latest)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: 20250214 (an_contract_number) — source canada_federal"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the Crown must pay a proper invoice no later than the 28th day after receiving it — Federal Prompt Payment for Construction Work Act, S.C. 2019, c. 29, s. 387, s. 9(2), in force 2023-12-09 (https://laws-lois.justice.gc.ca/eng/acts/F-7.7/FullText.html, read 2026-11-08: \"no late
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: PO rule; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["payment.paiement@telefilm.ca (finance/accounting dept or supplier-payment office)", "mailbox from the dataset build, re-submitted so the referee re-fetched the page on 2026-11-04", "page: https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html", "quote: \"payment.paiement@telefilm.ca\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_dsenrich01.csv task CL-DS-00050"], "buyer_facts": ["address and phone: the buyer's own site, https://telefilm.ca/en/who-we-are/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (CanadaBuys award notices (+ CanadaBuys tender notice))", "registry identity: Québec REQ (NEQ): 1143656032", "1143656032 (QC) status Québec REQ (NEQ): Immatriculée (1995-03-15) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "exact)", "incorporated / registered: 1960-09-23", "ph

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html | 2026-11-08 | ok |  |  |  | 613-996-7663 |  |  |  |  |  |

## Buyer site facts (org_extras, telefilm.ca)
- **status**: ok
- **pages**: 6
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Telefilm Canada
- **jsonld_logo**: https://telefilm.ca/wp-content/uploads/2026/05/cropped-tfc_favicon_512.png
- **jsonld_url**: https://telefilm.ca/en/
- **jsonld_same_as**: https://www.facebook.com/TelefilmCanada/; https://x.com/Telefilm_Canada; https://www.instagram.com/telefilm_canada/; https://www.linkedin.com/company/telefilm-canada/; https://www.youtube.com/user/telefilmcanada
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/telefilm.ca\/en","url":"https:\/\/telefilm.ca\/en","name":"Telefilm Canada | Partner of Choice","isPartOf":{"@id":"https:\/\/telefilm.ca\/en\/#website"},"about":{"@id":"https:\/\/telefilm.ca\/en\/#organization"},"datePu
- **jsonld_page**: https://telefilm.ca/en
- **legal_name_stated**: Ottawa Hospital
- **legal_name_stated_url**: https://telefilm.ca/en/who-we-are/about-us/board-of-directors
- **legal_name_stated_quote**: d Finance Committee of the National Judicial Institute. He served as a governor on the board of The Ottawa Hospital (TOH) from June 2016 to 2025, and from June 2022 to June 2025, was Chair of the Board at TOH, as we
- **linkedin_url**: https://ca.linkedin.com/company/telefilm-canada
- **language**: en
- **logo_url**: https://telefilm.ca/wp-content/themes/tel11799-2026-telefilm.ca/assets_dist/images/brand_logo-telefilm-canada_neg.svg
- **logo_basis**: logo image in the site header
- **domain**: telefilm.ca
- **key**: b:1382482eb35e183b
- **name**: Telefilm Canada
- **website**: https://telefilm.ca/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "700 René-Lévesque Blvd. West, suite 1000, Montreal, Quebec, H3B 1X8", "address_country": "CA", "address_url": "https://telefilm.ca/en/who-we-are/contact-us", "address_method": "pattern", "address_quote": "Quebec – Head Office 700 René-Lévesque Blvd. West, suite 1000 Montreal, Quebec, H3B 1X8 Toll-free number : 1 800 567-0890 info@telefilm.ca Ontario and Nunavut 474, rue", "phone": "1 800-567-0890", "phone_url": "https://telefilm.ca/en/who-we-are/contact-us", "emails": "info@telefilm.ca", "emails_url": "https://telefilm.ca/en/who-we-are/contact-us", "domain": "telefilm.ca", "key": "b:1382482eb35e183b", "name": "Telefilm Canada", "website": "https://telefilm.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, prdesjardins.com)
- **status**: ok
- **pages**: 6
- **language**: fr
- **logo_url**: https://prdesjardins.com/content/themes/prd/public/images/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: prdesjardins.com
- **key**: vendor:P & R Desjardins Construction Inc
- **name**: P & R Desjardins Construction Inc
- **website**: https://prdesjardins.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Québec. Commission
- **legal_name_stated_url**: https://prdesjardins.com/fr/about/sustainability/
- **legal_name_stated_quote**: du Québec (RBQ), l’organisme responsable de la qualification et de l’intégrité des entrepreneurs au Québec. Commission de la construction du Québec (CCQ) Inscrits auprès de la CCQ, nous nous conformons aux règlements d

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1777 Bégin, St-Laurent, QC H4R 2B5", "address_country": "CA", "address_url": "https://prdesjardins.com/fr/contact/", "address_method": "address-tag", "address_quote": "ients et proches de leurs projets. Demandes générales 1777 Bégin St-Laurent, QC H4R 2B5 T. 514 748 1234 F. 514 748 1110 info@prdesjardins.com 1777 Bégin St-Laurent, QC", "emails": "info@prdesjardins.com", "emails_url": "https://prdesjardins.com/fr/contact/", "domain": "prdesjardins.com", "key": "vd:prdesjardins.com", "name": "P & R Desjardins Construction Inc", "website": "https://prdesjardins.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | P & R Desjardins Construction Inc | found | P. & R. DESJARDINS CONSTRUCTION INC. |  | 1143656032 | QC | Société par actions ou compagnie | Active | 1960-09-23 | Montréal | Québec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=P%20%26%20R%20Desjardins%20Construction%20Inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Telefilm Canada | found | TÉLÉFILM CANADA |  | NEQ 8813532965 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | non immatriculée | 1967-03-03 | Montréal | QC | 1000-700 boul. René-Lévesque O, Montréal (Québec), H3B1X8 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |
| buyer | P & R Desjardins Construction Inc | found | P. & R. DESJARDINS CONSTRUCTION INC. |  | NEQ 1143656032 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 1995-03-15 | Montréal | QC | 1777 rue Bégin, Montréal (Québec), H4R2B5 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Telefilm Canada |  |  |  |  |  |  |  |  |  |  |
| b | P & R Desjardins Construction Inc |  |  |  |  |  |  |  |  |  |  |
| v | P. & R. DESJARDINS CONSTRUCTION INC. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "b:1382482eb35e183b",
 "ap_contact_team": {
  "emails": [
   "info@telefilm.ca",
   "payment.paiement@telefilm.ca"
  ],
  "invoice_portal": null,
  "phone": "1 800-567-0890",
  "mailing_address": "700 René-Lévesque Blvd. West, suite 1000, Montreal, Quebec, H3B 1X8",
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@telefilm.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://telefilm.ca/en/who-we-are/contact-us",
    "quote": "leases Industry advisories Logos and brand guidelines Contact Home / Who we are Contact Toll-free number 1 800-567-0890 Contact us by email info@telefilm.ca Our offices Call to action Quebec – Head Office 700 René-Lévesque Blvd. West, suite 1000 Montreal, Quebec, H3B 1X8 Toll-free number :",
    "retrieved_date": "2026-11-06",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Telefilm Canada",
    "task_id": "GE-AP-44001"
   },
   {
    "email": "info@telefilm.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": "1 800-567-0890",
    "mailing_address": "700 René-Lévesque Blvd. West, suite 1000, Montreal, Quebec, H3B 1X8",
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://telefilm.ca/en/who-we-are/contact-us",
    "quote": "Quebec – Head Office 700 René-Lévesque Blvd. West, suite 1000 Montreal, Quebec, H3B 1X8 Toll-free number : 1 800 567-0890 info@telefilm.ca",
    "retrieved_date": "2026-11-08",
    "found_by": "gemini",
    "verification": "verified",
    "source_file": "gemini_buyer_ap_results_batch44.csv",
    "org": "Telefilm Canada",
    "task_id": "GE-AP-44001"
   },
   {
    "email": "payment.paiement@telefilm.ca",
    "type": "invoicing",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html",
    "quote": "payment.paiement@telefilm.ca",
    "retrieved_date": "2026-11-04",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_dsenrich01.csv",
    "org": "Telefilm Canada",
    "task_id": "CL-DS-00050",
    "verified_via": "https://web.archive.org/web/20260710105949/https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit/businesses/suppliers.html"
   }
  ]
 },
 "research_status": {
  "found": 3,
  "not_published": 1
 },
 "queries_tried": [
  "site crawl of telefilm.ca (40 pages, robots.txt respected), no AI, no search engine",
  "dataset enrichment (ap_crawler / targeted search) re-submitted for referee verification",
  "Claude grounded web search (claude-haiku-5-5); 5 source pages checked",
  "\"Telefilm Canada\" \"payment.paiement@telefilm.ca\" OR \"invoices\" OR \"accounts payable\"; site:telefilm.ca \"facturation\" OR \"invoicing\""
 ],
 "ingested_at": "2026-11-09T16:04:50Z"
}
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
| record_id | source | status | title | value | currency | start | end | identifiers | link |
|---|---|---|---|---|---|---|---|---|---|
| canada_federal:cb:cb-431-1808606 | canada_federal | ongoing | Request for proposal Construction Manager | 4129184.72 | CAD |  |  | {"an_reference_number_latest": "cb-431-1808606", "an_reference_numbers": ["cb-431-1808606"], "an_contract_number": "20250214", "an_solicitation_number": "20250214", "tn_reference_number": "cb-665-1787 | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-431-1808606 |

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 2)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:302182:p-r-desjardins-construction-inc | Université McGill | Modifications | 47725.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=8f3f7e77-b36a-4a90-a71d-5fd17ee9ba71 |
| seao_quebec:323678:p-r-desjardins-construction-inc | Centre intégré universitaire de l'Est-de-l'île-de-montréal | Réfection laverie CH Saint-Michel | 274560.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=3b5bfa64-994b-4710-b04b-df5ed5e90fa6 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S5-11 — Science Based Targets initiative ⇄ AkzoNobel (Canada)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us) — 66 Lincoln's Inn Fields, London, England, WC2A 3LH
SUBMIT TO: financialinstitutions@sciencebasedtargets.org (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08) — 8600 av. de l'épée, Montréal, QC, H3N 2G6, CAN | GST/HST number not public | NEQ 1178483823
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Paints and coatings add more than color to green buildings | AkzoNobel
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 56
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Science Based Targets initiative (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: AkzoNobel (Canada) | subject: Paints and coatings add more than color to green buildings | AkzoNobel | published by: the Canada-located vendor's own website | record: https://www.akzonobel.com/en/about-us/stories/paints-and-coatings-add-more-than-color-to-green-buildings | vendor in Canada because: vendor located in Canada (stories; Wikidata country + address on its site)=akzonobel.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:3a4fded43be8d971
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Science Based Targets initiative
- **buyer_website**: https://sciencebasedtargets.org/
- **buyer_address**: 66 Lincoln's Inn Fields, London, England, WC2A 3LH
- **buyer_contact_evidence_url**: https://sciencebasedtargets.org/contact
- **buyer_legal_name_as_published**: Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us)
- **buyer_logo_url**: https://media.sciencebasedtargets.org/production/media/home20241219.jpg?w=1200&h=630&auto=compress%2Cformat&fit=crop&dm=1734627337&s=13d7af83373c1ad444dfede96f2dad2c
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/science-based-targets
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://sciencebasedtargets.org/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: financialinstitutions@sciencebasedtargets.org
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://sciencebasedtargets.org/financial-institutions
- **email_evidence_quote**: of the review process. See this blog for more information . Contact For queries related to our financial institutions work, please contact financialinstitutions@sciencebasedtargets.org . Stay up to date with the latest developments in science-based targets for financial institutions by si
- **email_evidence_context**: needed. Companies whose targets continue to meet the applicable Criteria will not have to update them as part of the review process. See this blog for more information . Contact For queries related to our financial institutions work, please contact financialinstitutions@sciencebasedtargets.org . Stay up to date with the latest developments in science-based targets for financial institutions by signing up to our finance newsletter . Case Studies View All Case Studies Supplier Engagement Case Study - H&M Group H&M Group is a global fashion (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: financialinstitutions@sciencebasedtargets.org (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://sciencebasedtargets.org/financial-institutions | quote: "of the review process. See this blog for more information . Contact For queries related to our financial institutions work, please contact financialinstitutions" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-27624
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1;p=none; rua=mailto:dmarc_agg@vali.email;
- **dmarc_record_domain**: sciencebasedtargets.org
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:dc-aa8e722993._spfm.sciencebasedtargets.org ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Howard Shih (Financial Standards Lead) (as printed by the organisation on its own accounts-payable page (as printed on https://sciencebasedtargets.org/financial-institutions, re-read 2026-11-08))
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us) — 66 Lincoln's Inn Fields, London, England, WC2A 3LH ⏎ SUBMIT TO: financialinstitutions@sciencebasedtargets.org (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08) — 8600 av. de l'épée, Montréal, QC, H3N 2G6, CAN | GST/HST number not public | NEQ 1178483823 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Paints and coatings add more than color to green buildings | AkzoNobel
- **invoice_card_json**: {"bill_to": {"legal_name": "Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us)", "legal_name_is_published": true, "address": "66 Lincoln's Inn Fields, London, England, WC2A 3LH", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financialinstitutions@sciencebasedtargets.org", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)", "bn9": "", "neq": "1178483823 (Registraire des entreprises du Québe
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: AkzoNobel (Canada)
- **vendor_legal_name**: CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_registry_id**: NEQ 1178483823 (Registraire des entreprises du Québec (open data))
- **vendor_registry_url**: https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx
- **vendor_registered_address**: 3100 boul. de la Concorde E, Laval (Québec), H7E2B8 (registered address; Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_neq**: 1178483823 (Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_legal_form**: CIE (société par actions (compagnie)) (Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_address**: 8600 av. de l'épée, Montréal, QC, H3N 2G6, CAN
- **vendor_country_basis**: vendor located in Canada (stories; Wikidata country + address on its site)=akzonobel.com
- **vendor_website**: https://akzonobel.com
- **vendor_logo_url**: https://images.akzonobel.com/akzonobel-corporate/global/en/admin/logo-akzonobel.png?impolicy=.auto
- **vendor_linkedin_url**: http://www.linkedin.com/company/akzonobel
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: NEQ 1178483823 (Registraire des entreprises du Québec (open data)) status immatriculée (Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); incorporated / registered: 2023-03-01; website: https://akzonobel.com; NEQ: 1178483823 (Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: immatriculée (Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)
- **vendor_incorporation_date**: 2023-03-01
- **vendor_years_in_business**: 3.7 (since 2023-03-01, registry date)
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q30338834; business

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Paints and coatings add more than color to green buildings | AkzoNobel
- **contract_description**: Paints and coatings add more than color to green buildings | AkzoNobel (the record's title; the source publishes no separate description)
- **contract_link**: https://www.akzonobel.com/en/about-us/stories/paints-and-coatings-add-more-than-color-to-green-buildings
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us) — 66 Lincoln's Inn Fields, London, England, WC2A 3LH ⏎ SUBMIT TO: financialinstitutions@sciencebasedtargets.org (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08) — 8600 av. de l'épée, Montréal, QC, H3N 2G6, CAN | GST/HST number not public | NEQ 1178483823 ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Paints and coatings add more than color to green buildings | AkzoNobel
- **invoice_card_json**: {"bill_to": {"legal_name": "Science Based Targets initiative (stated on https://sciencebasedtargets.org/about-us)", "legal_name_is_published": true, "address": "66 Lincoln's Inn Fields, London, England, WC2A 3LH", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "financialinstitutions@sciencebasedtargets.org", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "CANADA INC. (as registered: Registraire des entreprises du Québec (open data), NEQ 1178483823, 2026-11-08)", "bn9": "", "neq": "1178483823 (Registraire des entreprises du Québe
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["financialinstitutions@sciencebasedtargets.org (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://sciencebasedtargets.org/financial-institutions", "quote: \"of the review process. See this blog for more information . Contact For queries related to our financial institutions work, please contact financialinstitutions\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-27624"], "buyer_facts": ["address and phone: the buyer's own site, https://sciencebasedtargets.org/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP contact name: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: NEQ 1178483823 (Registraire des entreprises du Québec (open data)) status immatriculée

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://sciencebasedtargets.org/financial-institutions | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, sciencebasedtargets.org)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://media.sciencebasedtargets.org/production/media/home20241219.jpg?w=1200&h=630&auto=compress%2Cformat&fit=crop&dm=1734627337&s=13d7af83373c1ad444dfede96f2dad2c
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: sciencebasedtargets.org
- **key**: lead:3a4fded43be8d971
- **name**: sciencebasedtargets.org
- **website**: https://sciencebasedtargets.org/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Science Based Targets initiative
- **legal_name_stated_url**: https://sciencebasedtargets.org/about-us
- **legal_name_stated_quote**: and impact SBTi Services Join Our Team News & Events Contact FAQs Set a Target search About us The Science Based Targets initiative (SBTi) is a corporate climate action organization that enables companies and financial institutions
- **linkedin_url**: https://www.linkedin.com/company/science-based-targets

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "66 Lincoln's Inn Fields, London, England, WC2A 3LH", "address_country": "GB", "address_url": "https://sciencebasedtargets.org/contact", "address_method": "pattern", "address_quote": "a charity (1205768) and a limited company (14960097), with registered address: 66 Lincoln's Inn Fields, London, England, WC2A 3LH. SBTI Services Limited is a limited company register", "emails": "info@sciencebasedtargets.org", "emails_url": "https://sciencebasedtargets.org/contact", "domain": "sciencebasedtargets.org", "key": "lead:3a4fded43be8d971", "name": "sciencebasedtargets.org", "website": "https://sciencebasedtargets.org/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, akzonobel.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://images.akzonobel.com/akzonobel-corporate/global/en/admin/logo-akzonobel.png?impolicy=.auto
- **logo_basis**: logo image in the site header
- **domain**: akzonobel.com
- **key**: vendor:AkzoNobel (Canada)
- **name**: AkzoNobel (Canada)
- **website**: https://akzonobel.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Alternative Performance Measure
- **legal_name_stated_url**: https://www.akzonobel.com/en/about-us/annual-report
- **legal_name_stated_quote**: enda and translating those actions into tangible and structural improvements in our performance.” * Alternative Performance Measure (APM). AkzoNobel uses APM adjustments to the IFRS measures to provide supplementary information on
- **mentions**: {'payment_method': {'text': 'Interactive PDF ESEF PACKAGE Annual report archive If you want to read more of our annu', 'url': 'https://www.akzonobel.com/en/about-us/annual-report', 'quote': 'case of discrepancies between the PDF version and the ESEF reporting package, the latter prevails. Interactive PDF ESEF PACKAGE Annual report archive If you want to read more of our annual reports, you can visit the online archive. It contains every AkzoNobel'}}
- **linkedin_url**: http://www.linkedin.com/company/akzonobel

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | AkzoNobel | Q50912 | official website on the organisation's domain (https://www.akzonobel.com/) + name |  | AkzoNobel | AkzoNobel | business; enterprise; public company | naamloze vennootschap | Netherlands | 1994-01-01 | Amsterdam; Wuppertal |
| v | AkzoNobel (Canada) | Q30338834 | official website on the organisation's domain (https://www.akzonobel.com/eka/) + name |  | AkzoNobel (Canada) |  | business |  | Canada |  | Salaberry-de-Valleyfield |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:3a4fded43be8d971",
 "ap_contact_team": {
  "emails": [
   "financialinstitutions@sciencebasedtargets.org",
   "info@sciencebasedtargets.org"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "financialinstitutions@sciencebasedtargets.org",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://sciencebasedtargets.org/financial-institutions",
    "quote": "of the review process. See this blog for more information . Contact For queries related to our financial institutions work, please contact financialinstitutions@sciencebasedtargets.org . Stay up to date with the latest developments in science-based targets for financial institutions by si",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "sciencebasedtargets.org",
    "task_id": "CL-LD-27624"
   },
   {
    "email": "info@sciencebasedtargets.org",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://sciencebasedtargets.org/",
    "quote": "<svg> <use xlink:href=\"#linkedin\"></use> </svg> </i> </a> </li> <li class=\"flex items-center pt-px uppercase border-white\"> <a href=\"mailto:info@sciencebasedtargets.org\" target=\"_blank\" title=\"Email\" class=\"inline-block p-2.5 transition-opacity hover:opacity-50\"> <i class=\"icon icon--envel",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "sciencebasedtargets.org",
    "task_id": "CL-LD-27624"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of sciencebasedtargets.org (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of sciencebasedtargets.org (25 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| seao_quebec:397909:akzonobel | Commission Scolaire de la Pointe de L'Île | Fourniture sur demande de produits de peinture et accessoires | 34851.93 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=2b6bb28d-477c-4143-a9aa-558c10278066 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

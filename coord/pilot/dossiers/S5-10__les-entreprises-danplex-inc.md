# S5-10 — Les Entreprises Danplex Inc ⇄ EVduty

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Les Entreprises Danplex Inc — 120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/)
SUBMIT TO: comptabilite@danplex.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: EVduty — 1141, 2e Avenue , Shawinigan (Québec) , Canada G9T 2X9 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Représentants & installateurs – Boutique EVduty
```

## Relationship
- **rank_group**: E3
- **data_quality_score**: 55
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Les Entreprises Danplex Inc (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): EVduty | subject: Représentants & installateurs – Boutique EVduty | published by: the Canada-located vendor's own website | record: https://evduty.elmec.ca/pages/representants-et-installateurs | vendor in Canada because: vendor located in Canada (wd)=evduty.elmec.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:a72868c6cb7922cd
- **tier**: E
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Les Entreprises Danplex Inc
- **buyer_website**: https://danplex.qc.ca/
- **buyer_address**: 120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/)
- **buyer_phone**: 418-484-3080
- **buyer_contact_evidence_url**: https://www.danplex.qc.ca/contact
- **buyer_legal_name_as_published**: Les Entreprises Danplex Inc
- **buyer_logo_url**: https://images.squarespace-cdn.com/content/v1/607dd158032f3e73b4bf37c7/1618859337472-LMQTN5ZQUP0N14MVPMZG/LOGO+%28La+Boite%29+BON.png?format=1500w
- **buyer_website_status**: site answers
- **buyer_registry_id**: 1144261667 (QC; https://ised-isde.canada.ca/cbr-rec/en/search?q=Les%20Entreprises%20Danplex%20Inc); NEQ 1144261667 (Registraire des entreprises du Québec (open data))
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: Société par actions ou compagnie (Canada's Business Registries, QC 1144261667, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.danplex.qc.ca/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptabilite@danplex.qc.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.danplex.qc.ca/
- **email_evidence_quote**: ">{"legalName":"Les Entreprises Danplex Inc. ","address":"120 Boulevard Bernard\nSaint-\u00C9phrem-de-Beauce, QC, G0M 1R0\nCanada","email":"comptabilite@danplex.qc.ca","telephone":"418-484-3080","sameAs":["https://www.facebook.com/LesEntreprisesDanplex"],"@context":"http://schema.org","@ty
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptabilite@danplex.qc.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.danplex.qc.ca/ | quote: "">{"legalName":"Les Entreprises Danplex Inc. ","address":"120 Boulevard Bernard\nSaint-\u00C9phrem-de-Beauce, QC, G0M 1R0\nCanada","email":"comptabilite@danplex" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23909
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.danplex.qc.ca; confirmed by 8.8.8.8
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 a mx include:spf.protection.outlook.com ip4:64.21.16.24 ip4:199.167.160.137 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Les Entreprises Danplex Inc — 120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/) ⏎ SUBMIT TO: comptabilite@danplex.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: EVduty — 1141, 2e Avenue , Shawinigan (Québec) , Canada G9T 2X9 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Représentants & installateurs – Boutique EVduty
- **invoice_card_json**: {"bill_to": {"legal_name": "Les Entreprises Danplex Inc", "legal_name_is_published": true, "address": "120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "comptabilite@danplex.qc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "EVduty", "bn9": "", "neq": "", "remit_address": "1141, 2e Avenue , Shawinigan (Québec) , Canad
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: fr (Québec buyer; French first; its invoicing page is in English, English also accepted)

## Vendor
- **vendor**: EVduty
- **vendor_address**: 1141, 2e Avenue , Shawinigan (Québec) , Canada G9T 2X9
- **vendor_country_basis**: vendor located in Canada (wd)=evduty.elmec.ca
- **vendor_website**: https://evduty.elmec.ca
- **vendor_emails**: services@elmec.ca
- **vendor_phone**: 819 533-3888
- **vendor_contact_evidence_url**: https://evduty.elmec.ca/pages/nous-joindre
- **vendor_logo_url**: https://evduty.elmec.ca/cdn/shop/files/logo_evduty_110x.png?v=1613793555
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/evduty-elmec/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://evduty.elmec.ca/pages/nous-joindre (tools/org_contacts.py, org_extras.py); website: https://evduty.elmec.ca (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Représentants & installateurs – Boutique EVduty
- **contract_description**: Représentants & installateurs – Boutique EVduty (the record's title; the source publishes no separate description)
- **contract_link**: https://evduty.elmec.ca/pages/representants-et-installateurs
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Les Entreprises Danplex Inc — 120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/) ⏎ SUBMIT TO: comptabilite@danplex.qc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: EVduty — 1141, 2e Avenue , Shawinigan (Québec) , Canada G9T 2X9 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Représentants & installateurs – Boutique EVduty
- **invoice_card_json**: {"bill_to": {"legal_name": "Les Entreprises Danplex Inc", "legal_name_is_published": true, "address": "120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada (schema.org JSON-LD PostalAddress on https://www.danplex.qc.ca/)", "address_is_the_invoice_address": false, "tax_number": "", "language": "fr (Québec buyer; French first; its invoicing page is in English, English also accepted)"}, "submit_to": {"email": "comptabilite@danplex.qc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (QC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "EVduty", "bn9": "", "neq": "", "remit_address": "1141, 2e Avenue , Shawinigan (Québec) , Canad
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["comptabilite@danplex.qc.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.danplex.qc.ca/", "quote: \"\">{\"legalName\":\"Les Entreprises Danplex Inc. \",\"address\":\"120 Boulevard Bernard\\nSaint-\\u00C9phrem-de-Beauce, QC, G0M 1R0\\nCanada\",\"email\":\"comptabilite@danplex\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-23909"], "buyer_facts": ["address and phone: the buyer's own site, https://www.danplex.qc.ca/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://evduty.elmec.ca/pages/nous-joindre (tools/org_contacts.py, org_extras.py)", "website: https://evduty.elmec.ca (site answers)"], "relationship": "tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site o

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.danplex.qc.ca/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, danplex.qc.ca)
- **status**: ok
- **pages**: 4
- **language**: fr
- **legal_name**: Les Entreprises Danplex Inc
- **legal_name_url**: https://www.danplex.qc.ca/
- **legal_name_quote**: rojet 120, boul. Bernard, St-Éphrem, QC, G0M 1R0 | (418) 484-3080 | reception@danplex.qc.ca © 2021, Les Entreprises Danplex Inc., Tous droits réservés.
- **logo_url**: https://images.squarespace-cdn.com/content/v1/607dd158032f3e73b4bf37c7/1618859337472-LMQTN5ZQUP0N14MVPMZG/LOGO+%28La+Boite%29+BON.png?format=1500w
- **logo_basis**: logo image in the site header
- **domain**: danplex.qc.ca
- **key**: lead:a72868c6cb7922cd
- **name**: Les Entreprises Danplex Inc
- **website**: https://danplex.qc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_legal_name**: Les Entreprises Danplex Inc.
- **jsonld_address**: 120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada
- **jsonld_phone**: 418-484-3080
- **jsonld_email**: comptabilite@danplex.qc.ca
- **jsonld_same_as**: https://www.facebook.com/LesEntreprisesDanplex
- **jsonld_quote**: {"address":"120 Boulevard Bernard\nSaint-\u00C9phrem-de-Beauce, QC, G0M 1R0\nCanada","image":"https://static1.squarespace.com/static/607dd158032f3e73b4bf37c7/t/607dd54974d8b36fbdcd2ba3/1790105439758/","name":"Les Entreprises Danplex Inc. ","@context":"http://schema.org","@type":"LocalBusiness"}
- **jsonld_page**: https://www.danplex.qc.ca/
- **tel_links**: +14184843080

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "120 Boulevard Bernard Saint-Éphrem-de-Beauce, QC, G0M 1R0 Canada", "address_country": "CA", "address_url": "https://www.danplex.qc.ca/contact", "address_method": "json-ld", "address_quote": "ous Appelez-nous ou rendez-nous visite. 120 boulevard Bernard Saint-Éphrem, QC, G0M 1R0 (418) 484-3080 Sébastien Routhier, Président & Chargé de projets achats@danplex", "phone": "418-484-3080", "phone_url": "https://www.danplex.qc.ca/contact", "emails": "achats@danplex.qc.ca; comptabilite@danplex.qc.ca; reception@danplex.qc.ca", "emails_url": "https://www.danplex.qc.ca/contact", "domain": "danplex.qc.ca", "key": "lead:a72868c6cb7922cd", "name": "danplex.qc.ca", "website": "https://danplex.qc.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Les Entreprises Danplex Inc | found | LES ENTREPRISES DANPLEX INC. |  | 1144261667 | QC | Société par actions ou compagnie | Active | 1991-10-28 | Saint-Éphrem-de-Beauce | Québec |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Les%20Entreprises%20Danplex%20Inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Les Entreprises Danplex Inc | found | LES ENTREPRISES DANPLEX INC. |  | NEQ 1144261667 | Registraire des entreprises du Québec (open data) | CIE (société par actions (compagnie)) | immatriculée | 1995-03-28 | Saint-Éphrem-de-Beauce | QC | 120 boul. Bernard, Saint-Éphrem-de-Beauce (Québec), G0M1R0 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Les Entreprises Danplex Inc |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:a72868c6cb7922cd",
 "ap_contact_team": {
  "emails": [
   "achats@danplex.qc.ca",
   "comptabilite@danplex.qc.ca",
   "reception@danplex.qc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "achats@danplex.qc.ca",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.danplex.qc.ca/contact",
    "quote": "ous ou rendez-nous visite. 120 boulevard Bernard Saint-Éphrem, QC, G0M 1R0 (418) 484-3080 Sébastien Routhier, Président & Chargé de projets achats@danplex.qc.ca Marie-Noël Routhier, Vice-présidente et Gestion administrative Responsable de la protection des renseignements personnels comptab",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "danplex.qc.ca",
    "task_id": "CL-LD-23909"
   },
   {
    "email": "comptabilite@danplex.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.danplex.qc.ca/",
    "quote": "\">{\"legalName\":\"Les Entreprises Danplex Inc. \",\"address\":\"120 Boulevard Bernard\\nSaint-\\u00C9phrem-de-Beauce, QC, G0M 1R0\\nCanada\",\"email\":\"comptabilite@danplex.qc.ca\",\"telephone\":\"418-484-3080\",\"sameAs\":[\"https://www.facebook.com/LesEntreprisesDanplex\"],\"@context\":\"http://schema.org\",\"@ty",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "danplex.qc.ca",
    "task_id": "CL-LD-23909"
   },
   {
    "email": "reception@danplex.qc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.danplex.qc.ca/",
    "quote": "cité. RÉSIDENTIEL - COMMERCIAL - INDUSTRIEL - AGRICOLE Soumettre votre projet 120, boul. Bernard, St-Éphrem, QC, G0M 1R0 | (418) 484-3080 | reception@danplex.qc.ca © 2021, Les Entreprises Danplex Inc., Tous droits réservés.",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "danplex.qc.ca",
    "task_id": "CL-LD-23909"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of danplex.qc.ca (8 pages, robots.txt respected), no AI, no search engine",
  "site crawl of danplex.qc.ca (8 pages, robots.txt respected), no AI, no search engine",
  "site crawl of danplex.qc.ca (8 pages, robots.txt respected), no AI, no search engine"
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

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

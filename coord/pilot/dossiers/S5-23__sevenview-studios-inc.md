# S5-23 — Sevenview Studios Inc ⇄ Meridian Engineering Inc.

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Sevenview Studios Inc — P.O. Box 8431, St. John’s, NL, A1B 3N9
SUBMIT TO: accounting@sevenview.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Meridian Engineering Inc. — 10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Projects - Meridian Engineering
```

## Relationship
- **rank_group**: E3
- **data_quality_score**: 55
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Sevenview Studios Inc (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Meridian Engineering Inc. | subject: Projects - Meridian Engineering | published by: the Canada-located vendor's own website | record: https://www.meridianengineering.ca/projects/ | vendor in Canada because: vendor located in Canada (v)=meridianengineering.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:355d27494e45dc1c
- **tier**: E
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Sevenview Studios Inc
- **buyer_website**: https://sevenview.ca/
- **buyer_address**: P.O. Box 8431, St. John’s, NL, A1B 3N9
- **buyer_phone**: (888) 488-0819
- **buyer_contact_evidence_url**: https://www.sevenview.ca/contact/
- **buyer_legal_name_as_published**: Sevenview Studios Inc
- **buyer_logo_url**: https://www.sevenview.ca/wp-content/uploads/2023/12/svs-logo-white.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/sevenview-studios
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.sevenview.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@sevenview.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.sevenview.ca/contact/
- **email_evidence_quote**: Sales: sales@sevenview.ca Accounting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s,
- **email_evidence_context**: is here to assist you. Feel free to reach out to us through the following channels:  Call Us Toll Free: (888) 488-0819 Telephone: (709) 700-0031 Fax: (709) 700-0312  Email General Inquiries: info@sevenview.ca Sales: sales@sevenview.ca Accounting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s, NL A1B 3N9 Take The Next Step Your digital transformation starts here Name * Company Email Address * Phone Number * Message * 0 / 180 Send Message This site is protected by reCAPTCHA and the Google Priv (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounting@sevenview.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.sevenview.ca/contact/ | quote: "Sales: sales@sevenview.ca Accounting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s," | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-13982
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:steve@sevenview.ca
- **dmarc_record_domain**: sevenview.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 +mx +a +ip4:147.182.150.165 +include:_spf.google.com +include:_spf.freeagent.com +include:sendgrid.net ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: (888) 488-0819 (as printed on https://www.sevenview.ca/contact/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "(888) 488-0819 (as printed on https://www.sevenview.ca/contact/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Sevenview Studios Inc — P.O. Box 8431, St. John’s, NL, A1B 3N9 ⏎ SUBMIT TO: accounting@sevenview.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Meridian Engineering Inc. — 10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Projects - Meridian Engineering
- **invoice_card_json**: {"bill_to": {"legal_name": "Sevenview Studios Inc", "legal_name_is_published": true, "address": "P.O. Box 8431, St. John’s, NL, A1B 3N9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@sevenview.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Newfoundland and Labrador)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Meridian Engineering Inc.", "bn9": "", "neq": "", "remit_address": "10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada"}, "follow_up": {"ap_phone": "(888) 488-0819 (as printed on https://www.sevenview.ca/contact/, re-read 2026-11-08)", "ap_contact": "", 
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Meridian Engineering Inc.
- **vendor_address**: 10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada
- **vendor_country_basis**: vendor located in Canada (v)=meridianengineering.ca
- **vendor_website**: https://www.meridianengineering.ca/
- **vendor_phone**: 709 466 2700
- **vendor_contact_evidence_url**: https://www.meridianengineering.ca/contact/
- **vendor_logo_url**: https://www.meridianengineering.ca/wp-content/uploads/2018/04/logo-2.png
- **vendor_website_status**: site answers
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://www.meridianengineering.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.meridianengineering.ca/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: Projects - Meridian Engineering
- **contract_description**: Projects - Meridian Engineering (the record's title; the source publishes no separate description)
- **contract_link**: https://www.meridianengineering.ca/projects/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 15% (Newfoundland and Labrador) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Sevenview Studios Inc — P.O. Box 8431, St. John’s, NL, A1B 3N9 ⏎ SUBMIT TO: accounting@sevenview.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Meridian Engineering Inc. — 10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Projects - Meridian Engineering
- **invoice_card_json**: {"bill_to": {"legal_name": "Sevenview Studios Inc", "legal_name_is_published": true, "address": "P.O. Box 8431, St. John’s, NL, A1B 3N9", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@sevenview.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of NL on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 15% (Newfoundland and Labrador)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "Meridian Engineering Inc.", "bn9": "", "neq": "", "remit_address": "10 Thompson Street, Clarenville, NL, A5A 1Y9, Canada"}, "follow_up": {"ap_phone": "(888) 488-0819 (as printed on https://www.sevenview.ca/contact/, re-read 2026-11-08)", "ap_contact": "", 
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounting@sevenview.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.sevenview.ca/contact/", "quote: \"Sales: sales@sevenview.ca Accounting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s,\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-13982"], "buyer_facts": ["address and phone: the buyer's own site, https://www.sevenview.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://www.meridianengineering.ca/contact/ (tools/org_contacts.py, org_extras.py)", "website: https://www.meridianengineering.ca/ (site answers)"], "relationshi

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.sevenview.ca/contact/ | 2026-11-08 | ok |  |  |  | (888) 488-0819 |  |  |  |  |  |

## Buyer site facts (org_extras, sevenview.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Sevenview Studios Inc
- **legal_name_url**: https://www.sevenview.ca/
- **legal_name_quote**:  info@sevenview.ca  1-888-488-0819  Mon-Fri 9am - 5pm NST Location St. John’s, NL Canada © 2026 Sevenview Studios Inc.
- **logo_url**: https://www.sevenview.ca/wp-content/uploads/2023/12/svs-logo-white.png
- **logo_basis**: logo image in the site header
- **domain**: sevenview.ca
- **key**: lead:355d27494e45dc1c
- **name**: Sevenview Studios Inc
- **website**: https://sevenview.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Sevenview Studios
- **jsonld_logo**: https://www.sevenview.ca/wp-content/uploads/2024/08/Sevenview-Studios-Logo.png
- **jsonld_url**: https://sv.sevenview.dev/
- **jsonld_same_as**: https://www.facebook.com/SevenviewStudios; https://x.com/sevenviewstudio; https://www.instagram.com/sevenview_studios; https://www.linkedin.com/company/sevenview-studios
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.sevenview.ca\/","url":"https:\/\/www.sevenview.ca\/","name":"Home - Sevenview Studios","isPartOf":{"@id":"https:\/\/sv.sevenview.dev\/#website"},"about":{"@id":"https:\/\/sv.sevenview.dev\/#organization"},"datePubli
- **jsonld_page**: https://www.sevenview.ca/
- **linkedin_url**: https://www.linkedin.com/company/sevenview-studios
- **tel_links**: +18884880819; +17097000031

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "P.O. Box 8431, St. John’s, NL, A1B 3N9", "address_country": "CA", "address_url": "https://www.sevenview.ca/contact/", "address_method": "pattern", "address_quote": "ting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s, NL A1B 3N9 Take The Next Step Your digital transformation starts here Name * Company Email", "phone": "(888) 488-0819", "phone_url": "https://www.sevenview.ca/contact/", "emails": "accounting@sevenview.ca; info@sevenview.ca; sales@sevenview.ca", "emails_url": "https://www.sevenview.ca/contact/", "domain": "sevenview.ca", "key": "lead:355d27494e45dc1c", "name": "sevenview.ca", "website": "https://sevenview.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, meridianengineering.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://www.meridianengineering.ca/wp-content/uploads/2018/04/logo-2.png
- **logo_basis**: logo image on the site
- **domain**: meridianengineering.ca
- **key**: vendor:Meridian Engineering Inc.
- **name**: Meridian Engineering Inc.
- **website**: https://meridianengineering.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Meridian Engineering
- **jsonld_logo**: https://www.meridianengineering.ca/wp-content/uploads/2018/04/logo-200.jpg
- **jsonld_url**: https://www.meridianengineering.ca/
- **jsonld_same_as**: https://www.facebook.com/Meridian-Engineering-220617955184214/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.meridianengineering.ca\/","url":"https:\/\/www.meridianengineering.ca\/","name":"Home - Meridian Engineering","isPartOf":{"@id":"https:\/\/www.meridianengineering.ca\/#website"},"about":{"@id":"https:\/\/www.meridia
- **jsonld_page**: https://www.meridianengineering.ca/
- **tel_links**: +17094662700

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "10 Thompson Street, Clarenville, NL A5A 1Y9", "address_country": "CA", "address_url": "https://www.meridianengineering.ca/contact/", "address_method": "pattern", "address_quote": "eam of experienced professionals.  Find Us 10 Thompson Street, Clarenville, NL A5A 1Y9  Phone 709 466 2700  Email solutions@meridianengineering.ca Get In Touch We a", "phone": "709 466 2700", "phone_url": "https://www.meridianengineering.ca/contact/", "domain": "meridianengineering.ca", "key": "vd:meridianengineering.ca", "name": "Meridian Engineering Inc.", "website": "https://meridianengineering.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Sevenview Studios Inc | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Sevenview%20Studios%20Inc | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Sevenview Studios Inc |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:355d27494e45dc1c",
 "ap_contact_team": {
  "emails": [
   "accounting@sevenview.ca",
   "info@sevenview.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounting@sevenview.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.sevenview.ca/contact/",
    "quote": "Sales: sales@sevenview.ca Accounting: accounting@sevenview.ca  Address Accounting P.O. Box 8431 St. John’s,",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "sevenview.ca",
    "task_id": "CL-LD-13982"
   },
   {
    "email": "info@sevenview.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.sevenview.ca/",
    "quote": "pply. We provide full-service digital marketing solutions. Follow Follow Follow Follow Menu Home About Services Portfolio Contact Contact  info@sevenview.ca  1-888-488-0819  Mon-Fri 9am - 5pm NST Location St. John’s, NL Canada © 2026 Sevenview Studios Inc.",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "sevenview.ca",
    "task_id": "CL-LD-13982"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of sevenview.ca (8 pages, robots.txt respected), no AI, no search engine",
  "site crawl of sevenview.ca (8 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 15)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:de1df23a-a68d-463e-b9e2-b0b74335034c:1 | Town of Paradise | Consulting Services - Water and Sewer Installations Bayview Heights | 88077.28 |  |  | https://paradise.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/de1df23a-a68d-463e-b9e2-b0b74335034c |
| ca_bidsandtenders:7394eb25-6a4d-4ac0-956f-fecf9e4ba9fb:1 | Newfoundland Labrador Hydro | Request for Proposals - Professional Services for Churchill Falls Airport Apron & Taxiway Rehabilitation |  |  |  | https://nlhydro.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/7394eb25-6a4d-4ac0-956f-fecf9e4ba9fb |
| ca_merx:3864415352:1 | Government of Newfoundland and Labrador (GNL) - Municipal Infrastructure (TI) | Consult Serv - Watermain & Sanitary Sewer Upgr - Norris Point - 17-CHIF-26-00013 | 190618.34 |  |  | https://www.merx.com/govnl/municipalinfrastructureti/solicitations/Consult-Serv-Watermain-Sanitary-Sewer-Upgr-Norris-Point-17-CHIF-26-00013/0000315986?origin=0 |
| ca_merx:3445008817:1 | Government of Newfoundland and Labrador (GNL) - Municipal Infrastructure (TI) | Consultant Services - Private and Municipal Sewer Reconstruction - Fiona-SW-01 | 283474.13 |  |  | https://www.merx.com/govnl/municipalinfrastructureti/solicitations/Consultant-Services-Private-and-Municipal-Sewer-Reconstruction-Fiona-SW-01/0000293727?origin=0 |
| ca_merx:3390838602:1 | Government of Newfoundland and Labrador (GNL) - Municipal Infrastructure (TI) | Deer Lake - Consultant Services - Infrastructure Upgrade Ph. 2 - 17-MCW-25-00021 | 117859.21 |  |  | https://www.merx.com/govnl/municipalinfrastructureti/solicitations/Deer-Lake-Consultant-Services-Infrastructure-Upgrade-Ph-2-17-MCW-25-00021/0000290221?origin=0 |
| ca_merx:3382791695:1 | Government of Newfoundland and Labrador (GNL) - Municipal Infrastructure (TI) | Town of Deer Lake - Consultant Services - Lift Station Upgrade - 17-MCW-25-00023 | 87870.89 |  |  | https://www.merx.com/govnl/municipalinfrastructureti/solicitations/Town-of-Deer-Lake-Consultant-Services-Lift-Station-Upgrade-17-MCW-25-00023/0000289787?origin=0 |
| ca_merx:3374213582:1 | Town of Carbonear | Parking Lot Treatment for Recreation Facility | 5750.0 |  |  | https://www.merx.com/govnl/townofcarbonear/solicitations/Parking-Lot-Treatment-for-Recreation-Facility/0000289236?origin=0 |
| canada_federal:dfo-mpo:4600000497 | Fisheries and Oceans Canada | # |  |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2023-2024-Q3-00036 |
| canada_federal:dfo-mpo:4600000503 | Fisheries and Oceans Canada | # |  |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2023-2024-Q3-00042 |
| canada_federal:dfo-mpo:4600000520 | Fisheries and Oceans Canada | # |  |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2023-2024-Q3-00059 |
| canada_federal:dfo-mpo:4500109258 | Fisheries and Oceans Canada | Repair and maintenance - Marine installations | 26691.5 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2026-2027-Q1-00141 |
| canada_federal:dfo-mpo:4500109260 | Fisheries and Oceans Canada | Repair and maintenance - Marine installations | 23908.5 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2026-2027-Q1-00142 |
| canada_federal:dfo-mpo:4500109798 | Fisheries and Oceans Canada | Repair and maintenance - Marine installations | 66498.75 |  |  | https://search.open.canada.ca/contracts/record/dfo-mpo,C-2026-2027-Q1-00158 |
| canada_federal:pwgsc-tpsgc:EA00312409 | Public Services and Procurement Canada | Engineering consultants - Construction | 1105995.31 |  |  | https://search.open.canada.ca/contracts/record/pwgsc-tpsgc,C-2025-2026-Q4-01906 |
| canada_federal:cb:EA011-230625:001:HAL | Public Works and Government Services Canada | Indian River Fishway Replacement | 125000.0 |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

# S5-26 — Tulane Alumni University ⇄ BioRender (Science Suit Inc.)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade B · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Tulane Alumni University (stated on https://tulane.edu/about) — 6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)
SUBMIT TO: accountspayable@tulane.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Jaggaer
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required • Release requisition and purchase order)
FROM / REMIT TO: BioRender (Science Suit Inc.) — 49 Spadina Avenue, Suite 200, Toronto, CA, M5V 2J1, Canada | GST/HST number not public
TAX: Tax-Exempt status – Sales tax exemptions Office of General Counse l (504) 865-5783 https://counsel (as printed on https://policy.tulane.edu/policy/purchasing-po | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Tulane Alumni University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located v
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 70
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Tulane Alumni University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: BioRender (Science Suit Inc.) | published by: the Canada-located vendor's own website | record: https://www.biorender.com/ | vendor in Canada because: vendor located in Canada (wall)=biorender.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:27a2f6036745d6eb
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Tulane Alumni University
- **buyer_website**: https://tulane.edu
- **buyer_address**: 6823 St. Charles Ave., New Orleans, LA, 70118, US (schema.org JSON-LD PostalAddress on https://tulane.edu/)
- **buyer_phone**: 504-865-5000
- **buyer_contact_evidence_url**: https://tulane.edu/contact-us
- **buyer_legal_name_as_published**: Tulane Alumni University (stated on https://tulane.edu/about)
- **buyer_logo_url**: https://tulane.edu/themes/custom/tulane_tailwindcss/logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/tulane-university/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://tulane.edu/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax-Exempt status – Sales tax exemptions Office of General Counse l (504) 865-5783 https://counsel (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@tulane.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://procure.tulane.edu/content/information-vendors
- **email_evidence_quote**: ase order. In most cases those terms are net thirty days. For invoice questions, issues, or reconciliation please email Accounts Payable at AccountsPayable@tulane.edu . You can also email an invoice directly to them. __________________________________________________________ Tulane Procure
- **email_evidence_context**: asing, and moving services. Suppliers are paid according to the terms and conditions of their individual purchase order. In most cases those terms are net thirty days. For invoice questions, issues, or reconciliation please email Accounts Payable at AccountsPayable@tulane.edu . You can also email an invoice directly to them. __________________________________________________________ Tulane Procurement Services 1555 Poydras St, 7th floor, New Orleans, La. 70112 procurementservices@tulane.edu • (504) 865-5211 Primary Navig (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@tulane.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://procure.tulane.edu/content/information-vendors | quote: "ase order. In most cases those terms are net thirty days. For invoice questions, issues, or reconciliation please email Accounts Payable at AccountsPayable@tula" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00063
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; pct=100; rua=mailto:67408bb2a8d02@ag.dmarcly.com; ruf=mailto:67408bb2a8d02@fo.dmarcly.com; sp=none; aspf=r;
- **dmarc_record_domain**: tulane.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:mail.zendesk.com include:_u.tulane.edu._spf.dmarcli.com ~all
- **mta_sts**: yes (v=STSv1; id=1735937044770)
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:67408bb2a8d02@tls.dmarcly.com)
- **bimi**: no BIMI record
- **invoice_mailing_address**: 6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)
- **invoice_portal_url**: Jaggaer
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Jaggaer
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "po_required": "purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)", "portal_url": "Jaggaer", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)"}
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Tulane Alumni University (stated on https://tulane.edu/about) — 6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@tulane.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Jaggaer ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required • Release requisition and purchase order) ⏎ FROM / REMIT TO: BioRender (Science Suit Inc.) — 49 Spadina Avenue, Suite 200, Toronto, CA, M5V 2J1, Canada | GST/HST number not public ⏎ TAX: Tax-Exempt status – Sales tax exemptions Office of General Counse l (504) 865-5783 https://counsel (as printed on https://policy.tulane.edu/policy/purchasing-po | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Tulane Alumni University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located v
- **invoice_card_json**: {"bill_to": {"legal_name": "Tulane Alumni University (stated on https://tulane.edu/about)", "legal_name_is_published": true, "address": "6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@tulane.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Jaggaer", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: Jaggaer", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purc
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-1)

## Vendor
- **vendor**: BioRender (Science Suit Inc.)
- **vendor_address**: 49 Spadina Avenue, Suite 200, Toronto, CA, M5V 2J1, Canada
- **vendor_country_basis**: vendor located in Canada (wall)=biorender.com
- **vendor_website**: https://www.biorender.com/
- **vendor_emails**: support@biorender.com
- **vendor_contact_evidence_url**: https://www.biorender.com/contact-sales
- **vendor_logo_url**: https://cdn.prod.website-files.com/621e95f9ac30687a56e4297e/69af053328eb062ecd36906c_AbbVie%20Logo.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/biorender
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://www.biorender.com/contact-sales (tools/org_contacts.py, org_extras.py); website: https://www.biorender.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.biorender.com/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **invoice_currency_derived**: USD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Tulane Alumni University (stated on https://tulane.edu/about) — 6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@tulane.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Jaggaer ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: required • Release requisition and purchase order) ⏎ FROM / REMIT TO: BioRender (Science Suit Inc.) — 49 Spadina Avenue, Suite 200, Toronto, CA, M5V 2J1, Canada | GST/HST number not public ⏎ TAX: Tax-Exempt status – Sales tax exemptions Office of General Counse l (504) 865-5783 https://counsel (as printed on https://policy.tulane.edu/policy/purchasing-po | CURRENCY: DERIVED: USD (derived from the buyer's country; C | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Tulane Alumni University (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located v
- **invoice_card_json**: {"bill_to": {"legal_name": "Tulane Alumni University (stated on https://tulane.edu/about)", "legal_name_is_published": true, "address": "6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@tulane.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Jaggaer", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "6823 St. Charles Avenue New Orleans, LA 70118 (as printed on https://procure.tulane.edu/content/information-vendors, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: Jaggaer", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purchasing-policy-and-procedures-manual, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: required • Release requisition and purchase order) (as printed on https://policy.tulane.edu/policy/purc
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 77
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published payment terms
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms not published (buyer's default applies)
- **facts_provenance_json**: {"mailbox": ["accountspayable@tulane.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://procure.tulane.edu/content/information-vendors", "quote: \"ase order. In most cases those terms are net thirty days. For invoice questions, issues, or reconciliation please email Accounts Payable at AccountsPayable@tula\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00063"], "buyer_facts": ["address and phone: the buyer's own site, https://tulane.edu/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://procure.tulane.edu/content/information-vendors | 2026-11-08 | ok |  |  |  |  | 6823 St. Charles Avenue New Orleans, LA 70118 |  |  |  |  |

## Buyer site facts (org_extras, tulane.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://tulane.edu/themes/custom/tulane_tailwindcss/logo.svg
- **logo_basis**: logo image in the site header
- **domain**: tulane.edu
- **key**: lead:27a2f6036745d6eb
- **name**: tulane.edu
- **website**: https://tulane.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: EducationalOrganization
- **jsonld_name**: Tulane University
- **jsonld_address**: 6823 St. Charles Ave., New Orleans, LA, 70118, US
- **jsonld_phone**: 504-865-5000
- **jsonld_logo**: https://tulane.edu/themes/custom/tulane_tailwindcss/logo.svg
- **jsonld_url**: https://tulane.edu
- **jsonld_same_as**: https://www.linkedin.com/school/tulane-university/
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "EducationalOrganization", "additionalType": "CollegeOrUniversity", "@id": "https://tulane.edu", "name": "Tulane University", "description": "Tulane University is a comprehensive research university in New Orleans, Louisiana. Tulanians see c
- **jsonld_page**: https://tulane.edu/
- **legal_name_stated**: Tulane Alumni University
- **legal_name_stated_url**: https://tulane.edu/about
- **legal_name_stated_quote**: nts Faculty & Staff Parents & Families Visitors Alumni and Friends Request Info Visit Apply Give to Tulane Alumni University Info Primary Navigation this.$refs.button.focus()) }, close(focusAfter) { if (!this.open) return th
- **linkedin_url**: https://www.linkedin.com/school/tulane-university/
- **tel_links**: 5048655000

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "6823 St. Charles Avenue, New Orleans, LA 70118", "address_country": "US", "address_url": "https://tulane.edu/contact-us", "address_method": "pattern", "address_quote": "ogin Email Gibson Online Contact Us Tulane University Address Tulane University 6823 St. Charles Avenue New Orleans, LA 70118 Tulane University Phone Number University Operator: 504-8", "phone": "504-865-5000", "phone_url": "https://tulane.edu/contact-us", "emails": "help@tulane.edu", "emails_url": "https://tulane.edu/contact-us", "domain": "tulane.edu", "key": "lead:27a2f6036745d6eb", "name": "tulane.edu", "website": "https://tulane.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, biorender.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: g Case Studies Company About us Careers
- **legal_name_url**: https://www.biorender.com/
- **legal_name_quote**: s Brainstorming Learn Webinars Guides & Tutorials Help Center Free Tools Engage In-Person Events Blog Case Studies Company About us Careers Contact Support Trust Center Newsroom System status © 2026 BioRender Privacy Terms BioRender uses c
- **logo_url**: https://cdn.prod.website-files.com/621e95f9ac30687a56e4297e/69af053328eb062ecd36906c_AbbVie%20Logo.svg
- **logo_basis**: logo image in the site header
- **domain**: biorender.com
- **key**: vendor:BioRender (Science Suit Inc.)
- **name**: BioRender (Science Suit Inc.)
- **website**: https://biorender.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: BioRender
- **jsonld_logo**: https://cdn.prod.website-files.com/621e6f1effebfe03881da9bd/69ab7753f02b2fc630059def_biorender-logo-upd.svg
- **jsonld_quote**: { "@context": "https://schema.org", "@type": ["SoftwareApplication", "WebApplication"], "name": "BioRender", "description": "Create publication-ready scientific figures in minutes. Build professional science figures, graphs, and slides — all in one place. No design skills needed.", "url": "https://w
- **jsonld_page**: https://www.biorender.com/
- **legal_name_stated**: My College
- **legal_name_stated_url**: https://www.biorender.com/contact-sales
- **legal_name_stated_quote**: elect an option Myself My Team (2-5 researchers) My Lab, Department or Institute (6-50 researchers) My College, School, or University (50+ researchers) Select an option RECOMMENDED FOR YOU For a single license
- **mentions**: {'payment_method': {'text': 'interact with the Services, we receive the following information about your visit, use', 'url': 'https://www.biorender.com/privacy', 'quote': 'ur identity or age. Personal Data We Receive from Your Use of the Services: When you visit, use, or interact with the Services, we receive the following information about your visit, use, or interactions (" Technical Information "): Log Data : We collect infor'}}
- **linkedin_url**: https://www.linkedin.com/company/biorender

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "emails": "support@biorender.com", "emails_url": "https://www.biorender.com/contact-sales", "domain": "biorender.com", "key": "vd:biorender.com", "name": "BioRender (Science Suit Inc.)", "website": "https://biorender.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v | BioRender | Q137394547 | official website on the organisation's domain (https://www.biorender.com/) + name |  | BioRender.com |  | website; enterprise |  | Canada |  | Toronto |
| v | BioRender (Science Suit Inc.) |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:27a2f6036745d6eb",
 "ap_contact_team": {
  "emails": [
   "accountspayable@tulane.edu",
   "stoppayment@tulane.edu",
   "procurementservices@tulane.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@tulane.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://procure.tulane.edu/content/information-vendors",
    "quote": "ase order. In most cases those terms are net thirty days. For invoice questions, issues, or reconciliation please email Accounts Payable at AccountsPayable@tulane.edu . You can also email an invoice directly to them. __________________________________________________________ Tulane Procure",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Tulane University",
    "task_id": "CL-WS-00063"
   },
   {
    "email": "stoppayment@tulane.edu",
    "type": "supplier_payment",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://tams.tulane.edu/sites/default/files/TULANE_ACCOUNTS_PAYABLE_CONTACT_LIST.pdf",
    "quote": "S PAYABLE CONTACT LIST All forms for Concur are on the Concur Resources website AP LIST OF CONTACTS Stop Payment Questions and Submissions: stoppayment@tulane.edu Purchase Order Invoice Processing:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Tulane University",
    "task_id": "CL-WS-00063"
   },
   {
    "email": "procurementservices@tulane.edu",
    "type": "procurement",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://procure.tulane.edu/content/information-vendors",
    "quote": ". __________________________________________________________ Tulane Procurement Services 1555 Poydras St, 7th floor, New Orleans, La. 70112 procurementservices@tulane.edu • (504) 865-5211 Primary Navigation Purchase Order Standard Terms and Conditions University Holidays ---> 6823 St. Char",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Tulane University",
    "task_id": "CL-WS-00063"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
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

## The vendor's other buyers in the dataset (first 60 of 1)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| uk_find_a_tender:ocds-h6vhtk-05e8fb:1 | Secretary of State for Health and Social Care acting as part of the Crown through UK Health Security Agency | BioRender licences 25/26 | 10115.4 |  |  | https://www.find-tender.service.gov.uk/Notice/077158-2025 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

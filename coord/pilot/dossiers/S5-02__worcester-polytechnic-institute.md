# S5-02 — Worcester Polytechnic Institute ⇄ HOSPITAL FOR SICK CHILDREN, THE

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/) — 100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)
SUBMIT TO: accountspayable@wpi.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Workday supplier portal
REFERENCE: contract {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" (reference) | PO rule: yes (as published: purchase orders must)
FROM / REMIT TO: HOSPITAL FOR SICK CHILDREN, THE — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 | GST/HST number not public
TAX: Tax Exemption WPI is a 501(C) (3) Tax Exempt organization exempting the university from sales tax in states where (as printed on https://www.wpi.edu/offices/pro | CURRENCY: USD (derived from the source's government) | TERMS: Payment is due within 30 days (as printed on https://www.wpi.edu/offices/bursar/payment, re-read 202
DESCRIPTION: Worcester Polytechnic Institute (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 61916.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Worcester Polytechnic Institute (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): HOSPITAL FOR SICK CHILDREN, THE | contract number: {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_ | all identifiers: {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" | value: 61916.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2026-02-18 | published by: subawardee country | record: https://www.usaspending.gov/award/R21EB034833 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:17de3a7d174c113a
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: Worcester Polytechnic Institute
- **buyer_website**: http://www.wpi.edu
- **buyer_address**: 100 Institute Road, Worcester, MA, 01609, USA (schema.org JSON-LD PostalAddress on https://www.wpi.edu/)
- **buyer_phone**: 508-831-5000
- **buyer_contact_evidence_url**: https://www.wpi.edu/contact
- **buyer_legal_name_as_published**: Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/)
- **buyer_logo_url**: https://www.wpi.edu/sites/default/files/inline-image/Offices/Marketing-Communications/WPI_Inst_Prim_FulClr.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/worcester-polytechnic-institute/
- **buyer_type**: university / college
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q195046; university; private not-for-profit educational institution
- **buyer_founded**: 1865-00-00 (Wikidata Q195046, official website on the organisation's domain (http://www.wpi.edu) + name; 2026-11-08)
- **buyer_employees**: 1283 (Wikidata Q195046, official website on the organisation's domain (http://www.wpi.edu) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.wpi.edu/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the lane's AP page (https://www.wpi.edu/offices/procurement/procedures); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: Tax Exemption WPI is a 501(C) (3) Tax Exempt organization exempting the university from sales tax in states where (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_esignature_preference**: DocuSign for an electronic signature, and then forwarded to the finance office (as printed on https://www.wpi.edu/sites/default/files/PurchasingPolicy_FINAL_10.14.2020withlinks.pdf, re-read 2026-11-08)
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@wpi.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.wpi.edu/offices/procurement/procedures
- **email_evidence_quote**: o maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.edu . For Invoices received without a related purchase order you must "Create a supplier invoice request" in Workday. Invoice addr
- **email_evidence_context**: is the foremost consideration. A specific good or service is required and sanctioned in a grant or contract to maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.edu . For Invoices received without a related purchase order you must "Create a supplier invoice request" in Workday. Invoice address Supplier invoices should be sent to: Worcester Polytechnic Institute Accounts Payable 100 Institute Road Worcester, MA (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@wpi.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.wpi.edu/offices/procurement/procedures | quote: "o maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi." | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00049
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; fo=1; ri=3600; rua=mailto:dmarc_agg@vali.email; 
- **dmarc_record_domain**: wpi.edu
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com  include:aspmx.pardot.com include:servers.mcsv.net include:spf1.service.formassembly.com include:_spf.qemailserver.com include:wpi.campusgroups.com ip4:130.215.33.240 ip4:66.151.109.16 ip4:139.146.146.128/25 ip4:139.146.160.0/25 ip4:74.122.104.0/22 ip4:149.7
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_mailing_address**: 100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)
- **payment_terms_as_published**: Payment is due within 30 days (as printed on https://www.wpi.edu/offices/bursar/payment, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: purchase orders must)
- **invoice_portal_url**: Workday supplier portal
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Workday
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "Payment is due within 30 days (as printed on https://www.wpi.edu/offices/bursar/payment, re-read 2026-11-08)", "po_required": "yes (as published: purchase orders must)", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/) — 100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@wpi.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Workday supplier portal ⏎ REFERENCE: contract {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" (reference) | PO rule: yes (as published: purchase orders must) ⏎ FROM / REMIT TO: HOSPITAL FOR SICK CHILDREN, THE — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 | GST/HST number not public ⏎ TAX: Tax Exemption WPI is a 501(C) (3) Tax Exempt organization exempting the university from sales tax in states where (as printed on https://www.wpi.edu/offices/pro | CURRENCY: USD (derived from the source's government) | TERMS: Payment is due within 30 days (as printed on https://www.wpi.edu/offices/bursar/payment, re-read 202 ⏎ DESCRIPTION: Worcester Polytechnic Institute (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 61916.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/)", "legal_name_is_published": true, "address": "100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@wpi.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: purchase orders must)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"25089-SUB-01\", \"prime_award_internal_id\": \"270314935\", \"Sub-Award ID\": \"25089-SUB-01\", \"Prime Award ID\": \"R21EB034833\", \"prime_award_generated_internal_id\": \"ASST_NON_R21EB034833_075\" (reference)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: {\"internal_id\": \"25089-SUB-01\", \"prime_award_internal_id\": \"270314935\", \"Sub-Award ID\": \"25089-SUB-01\", \"Prime Award ID\": \"R21EB0348
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" (reference) — source usaspending

## Vendor
- **vendor**: HOSPITAL FOR SICK CHILDREN, THE
- **vendor_address**: 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8
- **vendor_country_basis**: subawardee country=CAN
- **vendor_website**: https://www.sickkids.ca/
- **vendor_emails**: ap.inquiries@sickkids.ca
- **vendor_phone**: 416-813-1500
- **vendor_contact_evidence_url**: https://www.sickkids.ca/en/about/contact
- **vendor_logo_url**: https://www.sickkids.ca/contentassets/232e33f4208c495eb192e035ee7ba6e5/sickkids-logo-header.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.sickkids.ca/ (SickKids | The Hospital for Sick Children Skip to Main Content Construction on University Avenue Watermain and road restoration work may affect travel to SickKi)
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); phone / role e-mails / logo: the vendor's own site, https://www.sickkids.ca/en/about/contact (tools/org_contacts.py, org_extras.py); website: https://www.sickkids.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: purchase orders must)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075"
- **contract_or_agreement_number**: {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" (reference)
- **contract_value**: 61916.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2026-02-18
- **contract_link**: https://www.usaspending.gov/award/R21EB034833
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 5
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 5 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/) — 100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08) ⏎ SUBMIT TO: accountspayable@wpi.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Workday supplier portal ⏎ REFERENCE: contract {"internal_id": "25089-SUB-01", "prime_award_internal_id": "270314935", "Sub-Award ID": "25089-SUB-01", "Prime Award ID": "R21EB034833", "prime_award_generated_internal_id": "ASST_NON_R21EB034833_075" (reference) | PO rule: yes (as published: purchase orders must) ⏎ FROM / REMIT TO: HOSPITAL FOR SICK CHILDREN, THE — 555 University Avenue, Toronto, Ontario, Canada, M5G 1X8 | GST/HST number not public ⏎ TAX: Tax Exemption WPI is a 501(C) (3) Tax Exempt organization exempting the university from sales tax in states where (as printed on https://www.wpi.edu/offices/pro | CURRENCY: USD (derived from the source's government) | TERMS: Payment is due within 30 days (as printed on https://www.wpi.edu/offices/bursar/payment, re-read 202 ⏎ DESCRIPTION: Worcester Polytechnic Institute (university / college, jurisdiction not stated) — public contract / purchase award in the last 12 months (da | AMOUNT: 61916.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "Worcester Polytechnic Institute (schema.org JSON-LD legalName on https://www.wpi.edu/)", "legal_name_is_published": true, "address": "100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@wpi.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Workday supplier portal", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "100 Institute Road Worcester, MA 01609-2280 (as printed on https://www.wpi.edu/offices/procurement/procedures, re-read 2026-11-08)", "format": "", "system": "named on the buyer's page: Workday", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "yes (as published: purchase orders must)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"25089-SUB-01\", \"prime_award_internal_id\": \"270314935\", \"Sub-Award ID\": \"25089-SUB-01\", \"Prime Award ID\": \"R21EB034833\", \"prime_award_generated_internal_id\": \"ASST_NON_R21EB034833_075\" (reference)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: {\"internal_id\": \"25089-SUB-01\", \"prime_award_internal_id\": \"270314935\", \"Sub-Award ID\": \"25089-SUB-01\", \"Prime Award ID\": \"R21EB0348
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accountspayable@wpi.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.wpi.edu/offices/procurement/procedures", "quote: \"o maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00049"], "buyer_facts": ["address and phone: the buyer's own site, https://www.wpi.edu/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the lane's AP page (https://www.wpi.edu/offices/procurement/procedures)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendo

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.wpi.edu/offices/procurement/procedures | 2026-11-08 | ok |  | yes (as published: purchase orders must) | Workday supplier portal |  | 100 Institute Road Worcester, MA 01609-2280 |  |  |  | in a grant or contract to maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.edu . For Invoices received without  |

## Buyer site facts (org_extras, wpi.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **domain**: wpi.edu
- **key**: lead:17de3a7d174c113a
- **name**: Worcester Polytechnic Institute
- **website**: https://wpi.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: CollegeOrUniversity
- **jsonld_name**: Worcester Polytechnic Institute
- **jsonld_legal_name**: Worcester Polytechnic Institute
- **jsonld_alternate_name**: WPI
- **jsonld_address**: 100 Institute Road, Worcester, MA, 01609, USA
- **jsonld_phone**: +1-508-831-5000
- **jsonld_logo**: https://www.wpi.edu/sites/default/files/inline-image/Offices/Marketing-Communications/WPI_Inst_Prim_FulClr.png
- **jsonld_url**: https://www.wpi.edu
- **jsonld_founding_date**: 1865
- **jsonld_naics**: 611310
- **jsonld_same_as**: https://twitter.com/WPI; https://www.instagram.com/wpi/; https://www.facebook.com/wpi.edu; https://www.youtube.com/user/WPI; https://www.linkedin.com/school/worcester-polytechnic-institute/; https://en.wikipedia.org/wiki/Worcester_Polytechnic_Institute; https://www.wikidata.org/wiki/Q195046; https://dbpedia.org/resource/Worcester_Polytechnic_Institute; https://ror.org/05ejpqr48; https://openalex.o
- **jsonld_quote**: { "@context": "https://schema.org", "@graph": [ { "@type": "CollegeOrUniversity", "@id": "https://www.wpi.edu/#organization", "description": "Worcester Polytechnic Institute (WPI) is a private research university founded in 1865 in Worcester, Massachusetts. Enrollment: ~7,000 students. Student-to-fa
- **jsonld_page**: https://www.wpi.edu/
- **legal_name_stated**: STEM Education and Research Worcester Polytechnic Institute
- **legal_name_stated_url**: https://www.wpi.edu/about
- **legal_name_stated_quote**: waiver? Who qualifies and how to ask Breadcrumb Home About WPI About WPI A Distinctive Approach to STEM Education and Research Worcester Polytechnic Institute (WPI), a global leader in project-based learning, is a distinctive, top-tier technological universi
- **linkedin_url**: https://www.linkedin.com/school/worcester-polytechnic-institute/
- **tel_links**: 508-831-5000; 508 831 6272
- **logo_url**: https://www.wpi.edu/sites/default/files/inline-image/Offices/Marketing-Communications/WPI_Inst_Prim_FulClr.png
- **logo_basis**: schema.org JSON-LD logo

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "100 Institute Road, Worcester, MA 01609-2280", "address_country": "US", "address_url": "https://www.wpi.edu/contact", "address_method": "microdata", "address_quote": "rary Offices Topics Student Resources & Support WORCESTER POLYTECHNIC INSTITUTE 100 Institute Road Worcester , MA | 01609-2280 Ph: 508-831-5000 Contact Us | Visit WPI | Accessibi", "phone": "508-831-5000", "phone_url": "https://www.wpi.edu/contact", "domain": "wpi.edu", "key": "lead:17de3a7d174c113a", "name": "Worcester Polytechnic Institute", "website": "https://wpi.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, sickkids.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: The Hospital for Sick Children (SickKids)
- **legal_name_url**: https://www.sickkids.ca/
- **legal_name_quote**: dat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River. Copyright © 2026 The Hospital for Sick Children (SickKids). All rights reserved. Accessibility | Privacy | Terms of Use Back to Top
- **logo_url**: https://www.sickkids.ca/contentassets/232e33f4208c495eb192e035ee7ba6e5/sickkids-logo-header.png
- **logo_basis**: logo image in the site header
- **domain**: sickkids.ca
- **key**: lead:1fc1730fcac57997
- **name**: The Hospital for Sick Children (SickKids)
- **website**: https://sickkids.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: 2026 The Hospital
- **legal_name_stated_url**: https://www.sickkids.ca/en/patients-visitors/privacy/
- **legal_name_stated_quote**: n-Wendat and Petun First Nations, the Seneca, and the Mississaugas of the Credit River. Copyright © 2026 The Hospital for Sick Children (SickKids). All rights reserved. Accessibility | Privacy | Terms of Use Back to T
- **mentions**: {'payment_method': {'text': 'interactive science experiences and programs', 'url': 'https://www.sickkids.ca/', 'quote': 'aregivers preparing to go home. Kids Science This outreach program educates and inspires youth with interactive science experiences and programs. School at SickKids Board-certified teachers provide one-on-one teaching at the patient’s bedside.'}}
- **linkedin_url**: http://www.linkedin.com/company/the-hospital-for-sick-children
- **tel_links**: 416-813-7474; 416-326-3333; 1-800-387-0073

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "555 University Avenue, Toronto, Ontario, Canada, M5G 1X8", "address_country": "CA", "address_url": "https://www.sickkids.ca/en/about/contact", "address_method": "pattern", "address_quote": "ss The Hospital for Sick Children 555 University Avenue Toronto, Ontario Canada M5G 1X8 Main entrance and Emergency 170 Elizabeth Street Learn more about Coming to the", "phone": "416-813-1500", "phone_url": "https://www.sickkids.ca/en/about/contact", "emails": "ap.inquiries@sickkids.ca", "emails_url": "https://www.sickkids.ca/en/about/contact", "domain": "sickkids.ca", "key": "lead:1fc1730fcac57997", "name": "sickkids.ca", "website": "https://sickkids.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Worcester Polytechnic Institute | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Worcester%20Polytechnic%20Institute | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Worcester Polytechnic Institute | Q195046 | official website on the organisation's domain (http://www.wpi.edu) + name |  | Worcester Polytechnic Institute | Institut polytechnique de Worcester | university; private not-for-profit educational institution |  | United States | 1865-00-00 |  |
| b | The Hospital for Sick Children (SickKids) |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:17de3a7d174c113a",
 "ap_contact_team": {
  "emails": [
   "accountspayable@wpi.edu",
   "financeoperations@wpi.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@wpi.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wpi.edu/offices/procurement/procedures",
    "quote": "o maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.edu . For Invoices received without a related purchase order you must \"Create a supplier invoice request\" in Workday. Invoice addr",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-SQ-00815"
   },
   {
    "email": "accountspayable@wpi.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wpi.edu/offices/procurement/procedures",
    "quote": "o maintain the integrity of the project. Invoices / Payment / Prepayments Invoices received with related purchase orders must be emailed to AccountsPayable@wpi.edu . For Invoices received without a related purchase order you must \"Create a supplier invoice request\" in Workday. Invoice addr",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-WS-00049"
   },
   {
    "email": "accountspayable@wpi.edu",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wpi.edu/sites/default/files/2024-07/Business_Expense_Policy.pdf",
    "quote": "n expenditure, please submit an appeal form using the link here. VII. Questions If you have any questions about this policy, please contact accountspayable@wpi.edu. * * * Policy Sponsor: Chief Financial Officer Responsible Department: Office of Finance and Operations Effective Date (i.e.,",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-WS-00372"
   },
   {
    "email": "financeoperations@wpi.edu",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wpi.edu/offices/procurement/procedures",
    "quote": "tems for use in Massachusetts. Every state has specific requirements regarding tax exempt status. Please contact the </span><a href=\"mailto:financeoperations@wpi.edu\" target=\"_blank\">Controller’s office</a><span> to obtain proper documentation.</span></p> </div> </div> </details> <details",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-SQ-00815"
   },
   {
    "email": "financeoperations@wpi.edu",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.wpi.edu/offices/procurement/procedures",
    "quote": "tems for use in Massachusetts. Every state has specific requirements regarding tax exempt status. Please contact the </span><a href=\"mailto:financeoperations@wpi.edu\" target=\"_blank\">Controller’s office</a><span> to obtain proper documentation.</span></p> </div> </div> </details> <details",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-WS-00049"
   },
   {
    "email": "stars-invoice@wpi.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://web.wpi.edu/Images/CMS/Finops/STARS_instructions(1).pdf",
    "quote": "Update the order. Close the order (blanket orders should remain open until final invoice is received). Vendor invoice should be emailed to STARS-INVOICE@WPI.EDU for processing. Banner encumbrance will be relieved upon invoice payment. No check request is required. 8/31/15 Appendix: Progra",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "unverified_page_unavailable",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Worcester Polytechnic Institute",
    "task_id": "CL-WS-00049"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of www.wpi.edu (60 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.wpi.edu (60 pages, robots.txt respected), no AI, no search engine",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page then read by tools/deep_pages.py with the crawler's rules, no AI",
  "web search for the buyer's invoicing / accounts payable page (the search only gave the address); the page the
```

## PO-level open data naming this buyer
_none_

## Contract records between the pair (dataset)
_none_

## The buyer's other Canadian-vendor records (first 60 of 0)
_none_

## The vendor's other buyers in the dataset (first 60 of 11)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_newfoundland:8d09d200a47caa27 | Department of Education and Early Childhood Development | Training Base Package Developmental Screening & Supportive Plan | 56392.0 |  |  | https://www.gov.nl.ca/ppa/files/2026-Mar-16-31-Contract-Awards-Report.pdf |
| canada_federal:nrc-cnrc:1043329 | National Research Council Canada | Scientific services | 70100.0 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2026-2027-Q1-00467 |
| canada_federal:nrc-cnrc:1043662 | National Research Council Canada | Scientific services | 25614.75 |  |  | https://search.open.canada.ca/contracts/record/nrc-cnrc,C-2026-2027-Q1-00524 |
| canada_federal:phac-aspc:6D0378131N | Public Health Agency of Canada | Other business services not elsewhere specified | 29822.87 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2026-2027-Q1-00377 |
| canada_federal:phac-aspc:6D0235370K | Public Health Agency of Canada | Data and Database Access Services | 99999.96 |  |  | https://search.open.canada.ca/contracts/record/phac-aspc,C-2026-2027-Q1-00355 |
| canada_federal:cb:CW2417339 | Department of Health (HC) | Ontario Poison Centre support to Canadian Surveillance System for Poison Information | 338627.1 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2417339 |
| canada_federal:cb:CW2441566 | Public Health Agency of Canada (PHAC) | 6D037-248131-014-SL - CANADIAN NOSOCOMIAL INFECTION SURVEILLANCE PROGRAM (CNISP) | 29822.87 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2441566 |
| canada_federal:cb:CW2442524 | Public Health Agency of Canada (PHAC) | CHIRPP Contract 015 - The Hospital for Sick Children | 99999.96 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2442524 |
| seao_quebec:433893:hospital-for-sick-children | Université McGill | Fluoresence In Situ Hybridization (FISH) eperiments | 40000.0 |  |  | https://seao.gouv.qc.ca/avis-resultat-recherche/consulter?ItemId=136956d2-9961-4a53-9f2a-e6dc2801bb12 |
| who:202549340 | World Health Organization - Headquarters | Research & Normative work | 50000.0 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2021_contract_awards_services.pdf?sfvrsn=79df0a71_5 |
| who:202576711 | World Health Organization - Headquarters | Research & Normative work | 48159.0 |  |  | https://cdn.who.int/media/docs/default-source/procurement/2021_contract_awards_services.pdf?sfvrsn=79df0a71_5 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

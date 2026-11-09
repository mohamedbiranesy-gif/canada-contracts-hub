# S5-18 — Beach Enerrgy ⇄ Okta - Toronto

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Beach Energy Limited — 8, 80 Flinders Street, Adelaide SA 5000
SUBMIT TO: accounts@beachenergy.com.au (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Good
FROM / REMIT TO: Okta, Inc (schema.org JSON-LD legalName: https://www.okta.com/) — 100 First Street, San Francisco, CA, 94105, US (schema.org JSON-LD PostalAddress on https://www.okta.com/) | GST/HST number not public
TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: DERIVED: AUD (derived from the buyer's country; C | TERMS: payable by it within 14 days (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Ener
DESCRIPTION: Beach Enerrgy | Okta
```

## Relationship
- **rank_group**: D4
- **data_quality_score**: 74
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Beach Enerrgy (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Okta - Toronto | subject: Beach Enerrgy | Okta | published by: the Canada-located vendor's own website | record: https://www.okta.com/en-ca/customers/beach-energy/ | vendor in Canada because: vendor located in Canada (stories; OpenStreetMap + address on its site)=okta.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:1fb425dd2c1645cf
- **tier**: D
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Beach Enerrgy
- **buyer_website**: https://beachenergy.com.au/
- **buyer_address**: 8, 80 Flinders Street, Adelaide SA 5000
- **buyer_phone**: (08) 8338 2833
- **buyer_contact_evidence_url**: https://beachenergy.com.au/contact-us/
- **buyer_legal_name_as_published**: Beach Energy Limited
- **buyer_logo_url**: https://beachenergy.com.au/wp-content/themes/beachenergy/dist/images/Beach-Logo-RGB_4f24ada8.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/beach-energy-ltd/
- **buyer_type**: utility / public corporation (from the organisation's name / web domain)
- **buyer_sector**: utility
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://beachenergy.com.au/contact-us/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australian GST is accounted for by the buyer where applicable
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounts@beachenergy.com.au
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf
- **email_evidence_quote**: riate supporting documentation for any other fees, charges or expenses. 8.2. Except as otherwise agreed, all invoices must be forwarded to: accounts@beachenergy.com.au. 8.3. Subject to clause 6 and the remaining provisions of this clause the Company shall pay the amount properly invoiced b
- **email_evidence_context**: ds 8.2. Except as otherwise agreed, all invoices must be 2.1. When the Company requires the supply of Goods and/or Services and/or Rental Items from and/or Rental Items delivered. Any monies paid by the Company to the Supplier prior to forwarded to: accounts@beachenergy.com.au. the Supplier, the Company will issue a Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall be deemed to have been paid conditional 8.3. Subject to clause 6 and the remaining provisions of this claus (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accounts@beachenergy.com.au (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf | quote: "riate supporting documentation for any other fees, charges or expenses. 8.2. Except as otherwise agreed, all invoices must be forwarded to: accounts@beachenergy" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-29774
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1; p=reject; rua=mailto:dmarc_agg@vali.email;
- **dmarc_record_domain**: beachenergy.com.au
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf.exclaimer.net include:servers.mcsv.net ip4:202.136.99.196 ip4:20.5.80.155 ip4:20.5.82.25 include:coupahost.com include:spf.boreal-is.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: payable by it within 14 days (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)
- **po_required_as_published**: purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Coupa, coupa
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payable by it within 14 days (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)", "po_required": "purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)", "portal_url": "https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: AUD (derived from the buyer's country; CAD if the parties agreed so)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Beach Energy Limited — 8, 80 Flinders Street, Adelaide SA 5000 ⏎ SUBMIT TO: accounts@beachenergy.com.au (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Good ⏎ FROM / REMIT TO: Okta, Inc (schema.org JSON-LD legalName: https://www.okta.com/) — 100 First Street, San Francisco, CA, 94105, US (schema.org JSON-LD PostalAddress on https://www.okta.com/) | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: DERIVED: AUD (derived from the buyer's country; C | TERMS: payable by it within 14 days (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Ener ⏎ DESCRIPTION: Beach Enerrgy | Okta
- **invoice_card_json**: {"bill_to": {"legal_name": "Beach Energy Limited", "legal_name_is_published": true, "address": "8, 80 Flinders Street, Adelaide SA 5000", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts@beachenergy.com.au", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa, coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-conten)"}, "terms": {"payment_terms": "payable by it within 14 days (as printed on htt
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-conten)

## Vendor
- **vendor**: Okta - Toronto
- **vendor_legal_name**: Okta, Inc (schema.org JSON-LD legalName: https://www.okta.com/)
- **vendor_trading_name**: Okta - Toronto
- **vendor_address**: 100 First Street, San Francisco, CA, 94105, US (schema.org JSON-LD PostalAddress on https://www.okta.com/)
- **vendor_country_basis**: vendor located in Canada (stories; OpenStreetMap + address on its site)=okta.com
- **vendor_website**: https://okta.com
- **vendor_emails**: info@okta.com
- **vendor_phone**: 1-800-588-1656
- **vendor_contact_evidence_url**: https://www.okta.com/contact/
- **vendor_logo_url**: https://www.okta.com/content/dam/okta---digital/en_us/images/header/logos/okta.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/okta-inc-
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://www.okta.com/contact/ (tools/org_contacts.py, org_extras.py); website: https://okta.com (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_founded**: 2009-01-01 (schema.org JSON-LD foundingDate on https://www.okta.com/)

## Contract
- **po_required_as_published**: purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Beach Enerrgy | Okta
- **contract_description**: Beach Enerrgy | Okta (the record's title; the source publishes no separate description)
- **contract_link**: https://www.okta.com/en-ca/customers/beach-energy/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australian GST is accounted for by the buyer where applicable
- **invoice_currency_derived**: AUD (derived from the buyer's country; CAD if the parties agreed so)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Beach Energy Limited — 8, 80 Flinders Street, Adelaide SA 5000 ⏎ SUBMIT TO: accounts@beachenergy.com.au (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Good ⏎ FROM / REMIT TO: Okta, Inc (schema.org JSON-LD legalName: https://www.okta.com/) — 100 First Street, San Francisco, CA, 94105, US (schema.org JSON-LD PostalAddress on https://www.okta.com/) | GST/HST number not public ⏎ TAX: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); Australia | CURRENCY: DERIVED: AUD (derived from the buyer's country; C | TERMS: payable by it within 14 days (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Ener ⏎ DESCRIPTION: Beach Enerrgy | Okta
- **invoice_card_json**: {"bill_to": {"legal_name": "Beach Energy Limited", "legal_name_is_published": true, "address": "8, 80 Flinders Street, Adelaide SA 5000", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounts@beachenergy.com.au", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://beachenergy.com.au/coupa-supplier-portal-tips/ — Coupa", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: Coupa, coupa", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) (as printed on https://beachenergy.com.au/wp-conten)"}, "terms": {"payment_terms": "payable by it within 14 days (as printed on htt
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["accounts@beachenergy.com.au (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf", "quote: \"riate supporting documentation for any other fees, charges or expenses. 8.2. Except as otherwise agreed, all invoices must be forwarded to: accounts@beachenergy\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-29774"], "buyer_facts": ["address and phone: the buyer's own site, https://beachenergy.com.au/contact-us/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: th

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf | 2026-11-08 | ok | payable by it within 14 days | purchase-order terms published (as published: Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall) |  |  |  |  |  | Company will pay the amount (if any) determined to be personally and as trustee of any trusts for which it is trustee. Company may: payable by it within 14 days of resolution of the dispute. 2.3. The Supplier agrees to s | prior to forwarded to: accounts@beachenergy.com.au. the Supplier, the Company will issue a Purchase Order for the Goods and/or Services and/or inspection of the Goods and/or Rental Items shall be deemed to have been paid |

## Buyer site facts (org_extras, beachenergy.com.au)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Beach Energy Limited
- **legal_name_url**: https://beachenergy.com.au/
- **legal_name_quote**: d. Contact Us Privacy Policy Disclaimer Sign up for ASX updates Sign up for ASX updates subscribe © Beach Energy Limited 2026 Site by atomix
- **logo_url**: https://beachenergy.com.au/wp-content/themes/beachenergy/dist/images/Beach-Logo-RGB_4f24ada8.png
- **logo_basis**: logo image in the site header
- **domain**: beachenergy.com.au
- **key**: lead:1fb425dd2c1645cf
- **name**: Beach Enerrgy
- **website**: https://beachenergy.com.au/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Beach Energy
- **jsonld_url**: https://beachenergy.com.au/
- **jsonld_same_as**: https://twitter.com/beachenergyltd; https://www.linkedin.com/company/beach-energy-ltd/
- **jsonld_quote**: {"@context":"https://schema.org","@type":"Organization","url":"https://beachenergy.com.au/","name":"Beach Energy","sameAs":["https://twitter.com/beachenergyltd","https://www.linkedin.com/company/beach-energy-ltd/"]}
- **jsonld_page**: https://beachenergy.com.au/
- **legal_name_stated**: Centre Investor
- **legal_name_stated_url**: https://beachenergy.com.au/disclaimer/
- **legal_name_stated_quote**: ria Enterprise Project Bass Basin Western Australia Perth Basin New Zealand Taranaki Basin Investor Centre Investor Overview Annual General Meeting (AGM) ASX Announcements Company Reporting & Calendar Dividend Histo
- **mentions**: {'payment_method': {'text': 'interacts with Beach in person or electronically, for example when an individual access', 'url': 'https://beachenergy.com.au/privacy-policy/', 'quote': 'collect personal information about an individual in a variety of ways, including when an individual interacts with Beach in person or electronically, for example when an individual accesses Beach’s website. Beach will only collect personal information about an'}}
- **linkedin_url**: https://www.linkedin.com/company/beach-energy-ltd/
- **tel_links**: (08) 8338 2833; +64 6 769 9800; 1300737760; +61 2 9290 9600

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "8, 80 Flinders Street, Adelaide SA 5000", "address_country": "AU", "address_url": "https://beachenergy.com.au/contact-us/", "address_method": "pattern", "address_quote": "ct our head office or speak to our team, fill in the form below or call us on (08) 8338 2833 Name * First Last Phone * Email * Your message: * Submit Beach Energ", "phone": "(08) 8338 2833", "phone_url": "https://beachenergy.com.au/contact-us/", "emails": "corporate@beachenergy.com.au; info@beachenergy.com.au", "emails_url": "https://beachenergy.com.au/contact-us/", "domain": "beachenergy.com.au", "key": "lead:1fb425dd2c1645cf", "name": "Beach Enerrgy", "website": "https://beachenergy.com.au/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, okta.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.okta.com/content/dam/okta---digital/en_us/images/header/logos/okta.svg
- **logo_basis**: logo image on the site
- **domain**: okta.com
- **key**: vendor:Okta - Toronto
- **name**: Okta - Toronto
- **website**: https://okta.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Okta
- **jsonld_legal_name**: Okta, Inc.
- **jsonld_address**: 100 First Street, San Francisco, CA, 94105, US
- **jsonld_phone**: +1-800-588-1656
- **jsonld_email**: info@okta.com
- **jsonld_logo**: https://s7d9.scene7.com/is/image/okta/logo-okta?$Transparent$
- **jsonld_url**: https://www.okta.com/
- **jsonld_founding_date**: 2009-01-01
- **jsonld_same_as**: https://www.facebook.com/Okta/; https://www.linkedin.com/company/okta-inc; https://en.wikipedia.org/wiki/Okta,_Inc.
- **jsonld_quote**: { "@context": "https://schema.org", "@type": "Organization", "name": "Okta", "legalName": "Okta, Inc.", "url": "https://www.okta.com/", "logo": "https://s7d9.scene7.com/is/image/okta/logo-okta?$Transparent$", "description": "The Okta and Auth0 Platforms enable secure access, authentication, and auto
- **jsonld_page**: https://www.okta.com/
- **legal_name_stated**: Developers Company
- **legal_name_stated_url**: https://www.okta.com/accessibility/
- **legal_name_stated_quote**: exico Netherlands Singapore Spain Sweden United Kingdom Login Products Solutions Learning & Support Developers Company Free trial Contact us Products Our platforms secure all types of identity from AI agents to your cu
- **linkedin_url**: https://www.linkedin.com/company/okta-inc-
- **tel_links**: +1 (800) 588-1656; +18004251267; +1-800-425-1267; 1-800-425-1267; +18005881656; +61272088383; +16476994538; +1 (800) 425

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "100 First Street, San Francisco, CA, 94105", "address_country": "US", "address_url": "https://www.okta.com/contact/", "address_method": "json-ld", "address_quote": "8 80 Support: +33 800 914 949 Email: [email protected] San Francisco (HQ North) 100 First Street, 6th Floor San Francisco, CA 94105, USA Sales: 1-800-588-1656 Support: 1-800-21", "phone": "1-800-588-1656", "phone_url": "https://www.okta.com/contact/", "emails": "info@okta.com", "emails_url": "https://www.okta.com/", "domain": "okta.com", "key": "lead:b4dafbebc07e29de", "name": "Okta for Good", "website": "https://okta.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Beach Enerrgy |  |  |  |  |  |  |  |  |  |  |
| b | Okta |  |  |  |  |  |  |  |  |  |  |
| v | Okta - Toronto |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:1fb425dd2c1645cf",
 "ap_contact_team": {
  "emails": [
   "accounts@beachenergy.com.au",
   "info@beachenergy.com.au"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounts@beachenergy.com.au",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://beachenergy.com.au/wp-content/uploads/Beach-Energy-NZ-Purchase-Order-Terms-and-Conditions.pdf",
    "quote": "riate supporting documentation for any other fees, charges or expenses. 8.2. Except as otherwise agreed, all invoices must be forwarded to: accounts@beachenergy.com.au. 8.3. Subject to clause 6 and the remaining provisions of this clause the Company shall pay the amount properly invoiced b",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Beach Enerrgy",
    "task_id": "CL-LD-29774"
   },
   {
    "email": "info@beachenergy.com.au",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://beachenergy.com.au/for-suppliers/",
    "quote": "ithdraw your consent to the use of your personal information and to complain about a breach of your privacy. Email our Company Secretary at info@beachenergy.com.au if you have further questions about how we process your personal information. Beach Supplier Portal Beach Energy uses the Beac",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Beach Enerrgy",
    "task_id": "CL-LD-29774"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of beachenergy.com.au (15 pages, robots.txt respected), no AI, no search engine",
  "site crawl of beachenergy.com.au (15 pages, robots.txt respected), no AI, no search engine"
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
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

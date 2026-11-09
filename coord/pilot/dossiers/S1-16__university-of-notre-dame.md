# S1-16 — University of Notre Dame ⇄ YORK UNIVERSITY

Stratum: **S1_gold_complete_published_PO_rule** · pay on sight: yes · channel tier 1 · AP grade A · missing: —

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: 2026 University (stated on https://www.nd.edu/about/) — 100, Notre Dame, IN 46556
SUBMIT TO: invoice@nd.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks
REFERENCE: contract {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO (reference) | PO rule: purchase-order terms published (as published: purchase order include)
FROM / REMIT TO: YORK UNIVERSITY — 4700 Keele St, Toronto, Ontario, M3J 1P3, CA | GST/HST 119306736 (as printed on the vendor's site: https://www.yorku.ca/alumniandfriends/give/)RT0001 (account derived from the BN9)
TAX: TAX EXEMPTION (as printed on https://controller.nd.edu/assets/93354/procard_policy.pdf, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: payment terms during registration and ongoing negotia
DESCRIPTION: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS | AMOUNT: 50600.0 (source field: Sub-Award Amount) USD
```

## Relationship
- **rank_group**: GOLD
- **data_quality_score**: 92
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: University of Notre Dame (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): YORK UNIVERSITY | subject: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS | contract number: {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_intern | all identifiers: {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO | value: 50600.0 (source field: Sub-Award Amount) USD (derived from the source's government) | awarded 2026-05-04 | published by: subawardee country | record: https://www.usaspending.gov/award/W912HQ24C0063 | vendor in Canada because: subawardee country=CAN | status rule: likely active (record dated in the last 12 months: subawardee country)
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:abc7538deb739227|lead:e2813b3d82ff31af
- **tier**: B
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)

## Buyer
- **buyer**: University of Notre Dame
- **buyer_website**: https://nd.edu/
- **buyer_address**: 100, Notre Dame, IN 46556
- **buyer_phone**: (574) 631-5000
- **buyer_contact_evidence_url**: https://www.nd.edu:443/about/visit/
- **buyer_legal_name_as_published**: 2026 University (stated on https://www.nd.edu/about/)
- **buyer_logo_url**: https://static.nd.edu/images/webclips/default/webclip-180.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/school/university-of-notre-dame/
- **buyer_type**: university / college (from the organisation's name / web domain)
- **buyer_sector**: education: post-secondary
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q178848; private university; private not-for-profit educational institution; Catholic university; academic publisher; open-access publisher
- **buyer_founded**: 1842-11-26 (Wikidata Q178848, official website on the organisation's domain (https://www.nd.edu/) + name; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 1396955832 Q4917; 1434633185 Q4917; 1584150976 Q4917; 1974296447 Q4917; 2184292145 Q4917; 1939878857 Q4917; 2076264785 Q (Wikidata Q178848, official website on the organisation's domain (https://www.nd.edu/) + name; 2026-11-08)
- **buyer_employees**: 1396; 6226 (Wikidata Q178848, official website on the organisation's domain (https://www.nd.edu/) + name; 2026-11-08)
- **buyer_legal_form**: Q130264562 (Wikidata Q178848, official website on the organisation's domain (https://www.nd.edu/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.nd.edu:443/about/visit/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the lane's AP page (https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_exempt_status**: TAX EXEMPTION (as printed on https://controller.nd.edu/assets/93354/procard_policy.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer
- **buyer_keys**: 2

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: invoice@nd.edu
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf
- **email_evidence_quote**: to agreed upon payment terms during registration and ongoing negotiations. Suppliers are directed to submit all purchase order invoices to invoice@nd.edu or via mail to 725 Grace Hall to Accounts Payable for processing. Accounts Payable is responsible for processing invoices and issuing p
- **email_evidence_context**: of purchase order invoices is a priority for the University and payment of supplier invoices are set according to agreed upon payment terms during registration and ongoing negotiations. Suppliers are directed to submit all purchase order invoices to invoice@nd.edu or via mail to 725 Grace Hall to Accounts Payable for processing. Accounts Payable is responsible for processing invoices and issuing payments for companies. Accounts Payables verifies that the quantities and prices on the invoice match the related (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: invoice@nd.edu (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf | quote: "to agreed upon payment terms during registration and ongoing negotiations. Suppliers are directed to submit all purchase order invoices to invoice@nd.edu or via" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00494
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: p=reject
- **dmarc_record**: v=DMARC1;p=reject;sp=quarantine;pct=100;fo=1;ri=3600;rua=mailto:8e60b3db@inbox.ondmarc.com,mailto:dmarc-list@nd.edu;ruf=mailto:8e60b3db@inbox.ondmarc.com,mailto:dmarc-list@nd.edu;
- **dmarc_record_domain**: nd.edu
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_u.nd.edu._spf.smart.ondmarc.com ~all
- **mta_sts**: yes (v=STSv1; id=1665778474075)
- **tls_rpt**: yes (v=TLSRPTv1; rua=mailto:8e60b3db@inbox.ondmarc.com;)
- **bimi**: yes (v=BIMI1;l=https://vmc.digicert.com/9c5adaa3-c900-493d-8bf8-2a24a8ae1164.svg;a=ht)
- **payment_terms_as_published**: payment terms during registration and ongoing negotia
- **po_required_as_published**: purchase-order terms published (as published: purchase order include) (as printed on https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf, re-read 2026-11-08)
- **invoice_portal_url**: https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: PaymentWorks (as printed on https://controller.nd.edu/our-services/accounts-payable/payments-to-businesses/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "payment_terms": "payment terms during registration and ongoing negotia", "po_required": "purchase-order terms published (as published: purchase order include) (as printed on https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf, re-read 2026-11-08)", "portal_url": "https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 2026 University (stated on https://www.nd.edu/about/) — 100, Notre Dame, IN 46556 ⏎ SUBMIT TO: invoice@nd.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks ⏎ REFERENCE: contract {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO (reference) | PO rule: purchase-order terms published (as published: purchase order include) ⏎ FROM / REMIT TO: YORK UNIVERSITY — 4700 Keele St, Toronto, Ontario, M3J 1P3, CA | GST/HST 119306736 (as printed on the vendor's site: https://www.yorku.ca/alumniandfriends/give/)RT0001 (account derived from the BN9) ⏎ TAX: TAX EXEMPTION (as printed on https://controller.nd.edu/assets/93354/procard_policy.pdf, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: payment terms during registration and ongoing negotia ⏎ DESCRIPTION: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS | AMOUNT: 50600.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "2026 University (stated on https://www.nd.edu/about/)", "legal_name_is_published": true, "address": "100, Notre Dame, IN 46556", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoice@nd.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: PaymentWorks (as printed on https://controller.nd.edu/our-services/accounts-payable/payments-to-businesses/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order include) (as printed on https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"208317YU\", \"prime_award_internal_id\": \"349903865\", \"Sub-Award ID\": \"208317YU\", \"Prime Award ID\": \"W912HQ24C0063\", \"prime_award_generated_internal_id\": \"CONT_AWD_W912HQ24C0063_9700_-NO (reference)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: {\"internal_id\": \"208317YU\", \"prime_award_internal_id\": \"349903865\", \"Sub-Award ID\": \"2083
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: contract or agreement number: {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO (reference) — source usaspending

## Vendor
- **vendor**: YORK UNIVERSITY
- **vendor_address**: 4700 Keele St, Toronto, Ontario, M3J 1P3, CA
- **vendor_country_basis**: subawardee country=CAN
- **vendor_bn9**: 119306736 (as printed on the vendor's site: https://www.yorku.ca/alumniandfriends/give/)
- **vendor_website**: https://www.yorku.ca/
- **vendor_phone**: (416) 736-2100
- **vendor_contact_evidence_url**: https://schulich.yorku.ca/
- **vendor_logo_url**: https://www.yorku.ca/
- **vendor_facts_provenance**: name and address: the record's vendor block (subawardee country); BN9: see the same vendor's other rows — carried from this vendor's row with Holland Bloorview Kids Rehabilitation Hospital; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://schulich.yorku.ca/ (tools/org_contacts.py, org_extras.py); website: https://www.yorku.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q849751; public research university; charitable organization; university in Ontario
- **vendor_founded**: 1959-00-00 (Wikidata Q849751, exact name match + country + organisation claims; 2026-11-08)
- **vendor_employees**: 7000; 5454; 7592; 6799; 7219; 8541; 8719; 9233; 9750; 9572; 9651; 9415; 9869; 9604; 9005; 8929; 9558; 9719; 10105; 10572 (Wikidata Q849751, exact name match + country + organisation claims; 2026-11-08)
- **vendor_bn_source**: see the same vendor's other rows — carried from this vendor's row with Holland Bloorview Kids Rehabilitation Hospital

## Contract
- **po_required_as_published**: purchase-order terms published (as published: purchase order include) (as printed on https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf, re-read 2026-11-08)
- **contract_status**: likely active (record dated in the last 12 months: subawardee country)
- **contract_reference**: {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO
- **contract_title**: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS
- **contract_description**: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS (the record's title; the source publishes no separate description)
- **contract_or_agreement_number**: {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO (reference)
- **contract_value**: 50600.0 (source field: Sub-Award Amount)
- **currency**: USD (derived from the source's government)
- **award_date**: 2026-05-04
- **contract_link**: https://www.usaspending.gov/award/W912HQ24C0063
- **source**: subawardee country
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: subawardee country; 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: buyer outside Canada — services and goods exported to a non-resident are generally zero-rated for GST/HST (ETA Schedule VI, Parts V and VII); US state sales / use tax is self-assessed by the buyer

## Pay on sight / grades
- **pay_on_sight**: yes
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: 2026 University (stated on https://www.nd.edu/about/) — 100, Notre Dame, IN 46556 ⏎ SUBMIT TO: invoice@nd.edu (invoicing/AP mailbox, confirmed by the referee) | invoice portal: https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks ⏎ REFERENCE: contract {"internal_id": "208317YU", "prime_award_internal_id": "349903865", "Sub-Award ID": "208317YU", "Prime Award ID": "W912HQ24C0063", "prime_award_generated_internal_id": "CONT_AWD_W912HQ24C0063_9700_-NO (reference) | PO rule: purchase-order terms published (as published: purchase order include) ⏎ FROM / REMIT TO: YORK UNIVERSITY — 4700 Keele St, Toronto, Ontario, M3J 1P3, CA | GST/HST 119306736 (as printed on the vendor's site: https://www.yorku.ca/alumniandfriends/give/)RT0001 (account derived from the BN9) ⏎ TAX: TAX EXEMPTION (as printed on https://controller.nd.edu/assets/93354/procard_policy.pdf, re-read 2026-11-08) | CURRENCY: USD (derived from the source's government) | TERMS: payment terms during registration and ongoing negotia ⏎ DESCRIPTION: REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS | AMOUNT: 50600.0 (source field: Sub-Award Amount) USD
- **invoice_card_json**: {"bill_to": {"legal_name": "2026 University (stated on https://www.nd.edu/about/)", "legal_name_is_published": true, "address": "100, Notre Dame, IN 46556", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "invoice@nd.edu", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "https://controller.nd.edu/our-services/accounts-payable/paymentworks/ — PaymentWorks", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: PaymentWorks (as printed on https://controller.nd.edu/our-services/accounts-payable/payments-to-businesses/, re-read 2026-11-08)", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order include) (as printed on https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "{\"internal_id\": \"208317YU\", \"prime_award_internal_id\": \"349903865\", \"Sub-Award ID\": \"208317YU\", \"Prime Award ID\": \"W912HQ24C0063\", \"prime_award_generated_internal_id\": \"CONT_AWD_W912HQ24C0063_9700_-NO (reference)", "vendor_id_with_buyer": "", "reference_hint": "contract or agreement number: {\"internal_id\": \"208317YU\", \"prime_award_internal_id\": \"349903865\", \"Sub-Award ID\": \"2083
- **invoice_readiness**: 9/11 invoice elements present
- **invoice_missing**: vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 83
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known | missing: finance mailbox; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup known; terms published
- **facts_provenance_json**: {"mailbox": ["invoice@nd.edu (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf", "quote: \"to agreed upon payment terms during registration and ongoing negotiations. Suppliers are directed to submit all purchase order invoices to invoice@nd.edu or via\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=reject; SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00494"], "buyer_facts": ["address and phone: the buyer's own site, https://www.nd.edu:443/about/visit/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the lane's AP page (https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (subawardee country)", 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://procurement.nd.edu/assets/648791/procurement_policy_manual_21326.pdf | 2026-11-08 | ok | 15 days of receipt | purchase-order terms published (as published: purchase order include) |  |  |  |  |  | and, if possible, photograph the damaged shipment. Initiating a Claim The shipper's main office should be notified in writing within 15 days of receipt of the damaged merchandise. The formal claim letter should: • descri | doing business with the University must disclose any perceived or known conflict of interest to University for review. Each contract and purchase order includes the right for the University to unilaterally terminate any  |

## Buyer site facts (org_extras, nd.edu)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://static.nd.edu/images/webclips/default/webclip-180.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: nd.edu
- **key**: lead:abc7538deb739227
- **name**: University of Notre Dame
- **website**: https://nd.edu/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: 2026 University
- **legal_name_stated_url**: https://www.nd.edu/about/
- **legal_name_stated_quote**: r InsideND Directory Canvas Hesburgh Library Campus Dining RecSports Basilica Schedule Light/Dark © 2026 University of Notre Dame Policies & Resources Accessibility Emergency Closed Captioning Notice of Non-Discrimi
- **mentions**: {'payment_method': {'text': 'Interactive Campus Map : A campus map with overlays for accessible building entrances a', 'url': 'https://www.nd.edu/about/accessibility/', 'quote': 'ccessibility initiative website . Additional Accessibility Services and Resources Navigating Campus Interactive Campus Map : A campus map with overlays for accessible building entrances and accessible parking. Interactive Campus Closure Map : A campus map with'}}
- **linkedin_url**: https://www.linkedin.com/school/university-of-notre-dame/
- **tel_links**: 5746315000

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "(574) 631-5000", "phone_url": "https://www.nd.edu:443/about/contact/", "address": "100, Notre Dame, IN 46556", "address_country": "US", "address_url": "https://www.nd.edu:443/about/visit/", "address_method": "pattern", "address_quote": "resources, and regularly scheduled campus tours. Address: Eck Visitors Center, 100, Notre Dame, IN 46556 Hours: Monday - Friday, 8 AM - 5PM Phone: (574) 631 - 572", "domain": "nd.edu", "key": "lead:faef3a5d0b99e793", "name": "nd.edu", "website": "https://nd.edu/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, yorku.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Schulich School of Business, York University
- **legal_name_url**: https://schulich.yorku.ca/
- **legal_name_quote**: culty & Staff Media Schulich Info About Faculty Directory Student Services Site Map Careers Contact Schulich School of Business, York University 4700 Keele Street, Toronto, ON M3J 1P3, Canada Connect with Schulich Instagram Facebook TikTok Link
- **logo_url**: https://www.yorku.ca/
- **logo_basis**: logo image in the site header
- **domain**: yorku.ca
- **key**: b:ef2b82a9f7fbb866
- **name**: York University
- **website**: https://yorku.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: York University
- **jsonld_logo**: https://www.yorku.ca/wp-content/uploads/2025/08/YorkULogo_DIGITAL_Hor_RGB.png
- **jsonld_url**: https://www.yorku.ca/?lang=en/
- **jsonld_same_as**: https://www.facebook.com/yorkuniversity/; https://x.com/YorkUniversity; https://www.youtube.com/@YorkUniversityOfficial; https://www.linkedin.com/school/167012/
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://www.yorku.ca/","url":"https://www.yorku.ca/","name":"York University | Toronto, Canada","isPartOf":{"@id":"https://www.yorku.ca/?lang=en/#website"},"about":{"@id":"https://www.yorku.ca/?lang=en/#organization"},"primaryImage
- **jsonld_page**: https://www.yorku.ca/
- **legal_name_stated**: York University
- **legal_name_stated_url**: https://www.yorku.ca/about/
- **legal_name_stated_quote**: About | York University × Global Search search box search button Popular Links Programs of Study eClass Email Faculty & Sta
- **mentions**: {'payment_method': {'text': 'EFT and Wire Transfers If you would like to make a gift by electronic fund transfer', 'url': 'https://www.yorku.ca/alumniandfriends/give/', 'quote': 'ifts of stocks or securities overview Step by step instructions Transfer form to complete your gift EFT and Wire Transfers If you would like to make a gift by electronic fund transfer or wire transfer, please contact us at give@yorku.ca and we will provide you'}}
- **linkedin_url**: https://www.linkedin.com/school/167012/
- **tel_links**: 4167362100
- **bn**: 119306736
- **bn_program**: RR0001
- **bn_label**: Registration Number : 11930 6736 RR0001
- **bn_url**: https://www.yorku.ca/alumniandfriends/give/
- **bn_quote**: Division of Advancement Tel: (416) 650-8221 barlas@yorku.ca Legal Name : York University Charitable Registration Number : 11930 6736 RR0001 This information is general in nature, does not constitute legal or financial advice, and should no

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "phone": "(416) 736-2100", "phone_url": "https://schulich.yorku.ca/about/contact-directory/", "address": "4700 Keele Street, Toronto, ON M3J 1P3", "address_country": "CA", "address_url": "https://schulich.yorku.ca/", "address_method": "pattern", "address_quote": "act Schulich School of Business, York University 4700 Keele Street, Toronto, ON M3J 1P3, Canada Connect with Schulich Instagram Facebook TikTok LinkedIn X YouTube Copy", "domain": "yorku.ca", "key": "vd:yorku.ca", "name": "schulich.yorku.ca", "website": "https://schulich.yorku.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | York University | Q849751 | official website on the organisation's domain (https://www.yorku.ca/) + name |  | York University | Université York | public research university; charitable organization; university in Ontario |  | Canada | 1959-00-00 | Toronto |
| b | University of Notre Dame | Q178848 | official website on the organisation's domain (https://www.nd.edu/) + name | University of Notre Dame du Lac [en] \| L’Université de Notre Dame du Lac [fr] | University of Notre Dame | Université de Notre-Dame-du-Lac | private university; private not-for-profit educational institution; Catholic university; academic publisher; open-access publisher | Q130264562 | United States | 1842-11-26 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:abc7538deb739227",
 "ap_contact_team": {
  "emails": [
   "invoice@nd.edu"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "invoice@nd.edu",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://procurement.nd.edu/assets/577460/procurement_policy_manual_10224.pdf",
    "quote": "to agreed upon payment terms during registration and ongoing negotiations. Suppliers are directed to submit all purchase order invoices to invoice@nd.edu or via mail to 725 Grace Hall to Accounts Payable for processing. Accounts Payable is responsible for processing invoices and issuing p",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "University of Notre Dame",
    "task_id": "CL-WS-00494"
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

## The vendor's other buyers in the dataset (first 60 of 10)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_newfoundland:e8af23db73e7d7a0 | Digital Government & Service NL | Training For Residential Tenancies | 10785.0 |  |  | https://www.gov.nl.ca/ppa/files/Contract-Award-Report-2024-04-01-To-2024-04-15-KD-Edits.pdf |
| canada_federal:csa-asc:9F52160316 | Canadian Space Agency | Scientific consultants | 3766576.32 |  |  | https://search.open.canada.ca/contracts/record/csa-asc,C-2022-2023-Q4-00151 |
| canada_federal:dfatd-maecd:7475979 | Global Affairs Canada | Teachers and instructors on contract | 85983.71 |  |  | https://search.open.canada.ca/contracts/record/dfatd-maecd,C-2026-2027-Q1-00479 |
| canada_federal:cb:CW2342755 | Department of Public Works and Government Services (PSPC) | ProServices SA – York University, Schulich Executive Education Centre (SEEC), Schulich School of Business |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2342755 |
| canada_federal:cb:CW2343613 | Department of Public Works and Government Services (PSPC) | TSPS SA (Task Based) - York University |  |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2343613 |
| usaspending:sub:CONT_AWD_W912HQ24C0063_9700_-NONE-_-NONE-:208317YU:HT23J5SXQ1J4 | UNIVERSITY OF NOTRE DAME DU LAC | REAL-TIME ANALYSIS OF GAS-PHASE PRODUCTS OF INCOMPLETE DESTRUCTION DURING THE THERMAL TREATMENT OF PFAS | 50600.0 |  |  | https://www.usaspending.gov/award/CONT_AWD_W912HQ24C0063_9700_-NONE-_-NONE-/ |
| ca_canadabuys_contract_history:an:PW-14-00629631-642414 | Canadian Space Agency | 2014 CSA Exploration Core Science Definition Studies for Space Exploration | 149818.85 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-14-00629631-642414 |
| ca_canadabuys_contract_history:an:PW-15-00710951 | Canadian Space Agency | SPACE EXPLORATION TOPICAL TEAMS | 15000.0 |  |  | https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-15-00710951 |
| ca_canadabuys_contract_history:an:E60ZH-2000LS:160:ZH | Public Works and Government Services Canada | Learning Services SA |  |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |
| ca_canadabuys_contract_history:an:H4033-030001:002:SS | Health Canada | Medical (R&D) | 298000.0 |  |  | https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb |

## Open questions for hand research (layer 2)

- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

Read 2026-11-09 (Claude, integrator lane).

**This is a research SUBAWARD, not a purchase — the channel is the prime's sponsored-programs financial contact, not its AP mailbox.** US universities
issue subawards on the Federal Demonstration Partnership template (FDP Cost Reimbursement Research Subaward, "FDP Sept 2017" footer; copy read at
https://www.tntech.edu/research/pdf/ada-compliantpdf/Sub_Cost_Reimburse_RE.pdf): invoices "not more often than monthly and not less frequently than
quarterly"; "shall be directed to the party's Contact, shown in Attachment 3A." (Attachment 3A: "Email invoices? Yes", "Invoice email (if different)");
each invoice "shall include current and cumulative costs (including cost sharing), Subaward number, and certification"; payment "in accordance with this
Subaward and 2 CFR 200.305"; final invoice "not later than 60 days after the" end of the period. → York University invoices Notre Dame's post-award office at the e-mail named
in Attachment 3A of the executed subaward, quoting the subaward number (the subaward number on the executed agreement), cumulative costs and the certification; the university AP mailbox in the row
is the fallback contact, and the PO terms in the row apply only if the prime issued a PO for the subaward. No Canadian GST (export of research services);
invoice in USD unless the subaward says CAD. Notre Dame's controller portal (row) is for vendor invoices; subaward invoices follow Attachment 3A.

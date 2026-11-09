# S5-43 — Kindersley ⇄ ICEsoft Technologies Canada Corp. (Voyent Alert!)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade A · missing: the vendor's GST/HST number (BN9)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Town of Kindersley — 106 5th Avenue East, Kindersley, SK S0L 1S0
SUBMIT TO: accountspayable@kindersley.ca (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: yes (as published: Purchase Order at the time of purchase, then the invoice shall)
FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public
TAX: First Nations are exempt from this requirement and need only meet the criteria outlined above:  In the case of a local gove (as printed on https://www.kindersl | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.c
DESCRIPTION: Kindersley (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the b
```

## Relationship
- **rank_group**: GOLD-T
- **data_quality_score**: 84
- **ship_ready**: yes
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Kindersley (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: ICEsoft Technologies Canada Corp. (Voyent Alert!) | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.kindersley.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary,  | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:a2073a8a30d121c7
- **tier**: T
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Kindersley
- **buyer_website**: https://kindersley.ca/
- **buyer_address**: 106 5th Avenue East, Kindersley, SK S0L 1S0
- **buyer_phone**: 1.306.463.2675 Mon-Fri: 8.30am-4.30pm
- **buyer_contact_evidence_url**: https://www.kindersley.ca/contact/
- **buyer_legal_name_as_published**: Town of Kindersley
- **buyer_logo_url**: https://www.kindersley.ca/wp-content/uploads/2019/02/Town_of_Kindersley_logo_small.png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government (from the organisation's name / web domain)
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q1914835; town
- **buyer_founded**: 1910-00-00 (Wikidata Q1914835, official website on the organisation's domain (http://www.kindersley.ca/) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.kindersley.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); AP contact name: the lane's AP page (https://www.kindersley.ca/contact/staff-directory/)
- **buyer_tax_exempt_status**: First Nations are exempt from this requirement and need only meet the criteria outlined above:  In the case of a local gove (as printed on https://www.kindersley.ca/getFileByName/2018%20PDAP%20Guidelines.pdf, re-read 2026-11-08)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accountspayable@kindersley.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.kindersley.ca/contact/staff-directory/
- **email_evidence_quote**: Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception –
- **email_evidence_context**: to Learn More Administration Jenna Lavoie, Corporate Services Manager/Deputy Administrator – jenna.l@kindersley.ca Jennifer Taylor, Utilities & Accounts Receivable Clerk – utilityclerk@kindersley.ca Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception – reception1@kindersley.ca Communications & Tourism Anna Polsfut, Communications Coordinator – communications@kindersley.ca Seasonal Tourism Information Centre – tourismkindersley@kindersley.ca Depar (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: accountspayable@kindersley.ca (invoicing/AP) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08 | page: https://www.kindersley.ca/contact/staff-directory/ | quote: "Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception –" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00053
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine;
- **dmarc_record_domain**: kindersley.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:173.46.152.128/25 ip4:199.244.76.0/24 a:dispatch-us.ppe-hosted.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_contact_name_as_published**: Emma Dies (as printed by the organisation next to its invoicing mailbox)
- **payment_terms_as_published**: payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.ca/wp-content/uploads/2022/11/WCEC_RENTAL_AGREEMENT_FINAL.pdf, re-read 2026-11-08)
- **po_required_as_published**: yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINAL.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.ca/wp-content/uploads/2022/11/WCEC_RENTAL_AGREEMENT_FINAL.pdf, re-read 2026-11-08)", "po_required": "yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINAL.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Kindersley — 106 5th Avenue East, Kindersley, SK S0L 1S0 ⏎ SUBMIT TO: accountspayable@kindersley.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Purchase Order at the time of purchase, then the invoice shall) ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: First Nations are exempt from this requirement and need only meet the criteria outlined above:  In the case of a local gove (as printed on https://www.kindersl | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.c ⏎ DESCRIPTION: Kindersley (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the b
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Kindersley", "legal_name_is_published": true, "address": "106 5th Avenue East, Kindersley, SK S0L 1S0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@kindersley.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINAL.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINA)"}, "terms": {"payment_terms": "payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.ca/wp-content/uploads/2022/11/WCEC_RENTAL_AGREEMENT_FINAL.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "First Nations are exempt fro
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINA)

## Vendor
- **vendor**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **vendor_address**: 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary, AB, T3G 0B4 1-877-263-3822 product.sales@icesoft.com Social Co
- **vendor_website**: https://thecse.com/
- **vendor_emails**: info@thecse.com
- **vendor_contact_evidence_url**: https://thecse.com/fr/contact-us/
- **vendor_logo_url**: https://thecse.com/apple-touch-icon.png
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://thecse.com/listings/icesoft-technologies-canada-corp/ (ICEsoft Technologies Canada Corp. | The Canadian Securities Exchange (CSE) Search Symbol, Name or Keyword en en Quote About Disclosure ISFT 0.00% ISFT 0.00% ICE)
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); phone / role e-mails / logo: the vendor's own site, https://thecse.com/fr/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://thecse.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **po_required_as_published**: yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINAL.pdf, re-read 2026-11-08)
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **award_date**: 2026-11-03
- **contract_link**: https://www.kindersley.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Town of Kindersley — 106 5th Avenue East, Kindersley, SK S0L 1S0 ⏎ SUBMIT TO: accountspayable@kindersley.ca (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: yes (as published: Purchase Order at the time of purchase, then the invoice shall) ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: First Nations are exempt from this requirement and need only meet the criteria outlined above:  In the case of a local gove (as printed on https://www.kindersl | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.c ⏎ DESCRIPTION: Kindersley (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the b
- **invoice_card_json**: {"bill_to": {"legal_name": "Town of Kindersley", "legal_name_is_published": true, "address": "106 5th Avenue East, Kindersley, SK S0L 1S0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accountspayable@kindersley.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINAL.pdf, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes that invoices must quote a PO number (yes (as published: Purchase Order at the time of purchase, then the invoice shall) (as printed on https://www.kindersley.ca/wp-content/uploads/2024/04/2018.05.09_Procurement-and-Purchasing-Policy-FINA)"}, "terms": {"payment_terms": "payment to the Town of Kindersley as invoiced within 30 days (as printed on https://www.kindersley.ca/wp-content/uploads/2022/11/WCEC_RENTAL_AGREEMENT_FINAL.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "First Nations are exempt fro
- **invoice_readiness**: 8/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: A
- **ap_score**: 85
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; payment terms published; currency known; AP phone or AP contact | missing: finance mailbox; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: none
- **ap_payability**: payable today: channel + bill-to + reference rule + tax treatment; supplier setup form not found (first payment may need it); terms published
- **facts_provenance_json**: {"mailbox": ["accountspayable@kindersley.ca (invoicing/AP)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-08", "page: https://www.kindersley.ca/contact/staff-directory/", "quote: \"Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception –\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by self-hosted or other (mx1-us1.ppe-hosted.com)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00053"], "buyer_facts": ["address and phone: the buyer's own site, https://www.kindersley.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "AP contact name: the lane's AP page (https://www.kindersley.ca/contact/staff-directory/)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.kindersley.ca/contact/staff-directory/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, kindersley.ca)
- **status**: ok
- **pages**: 5
- **language**: en
- **legal_name**: Town of Kindersley
- **legal_name_url**: https://www.kindersley.ca/
- **legal_name_quote**: Home - Town of Kindersley Skip to content 1.306.463.2675 Mon-Fri: 8.30am-4.30pm Contact Us Report a Concern Search for: COMMU
- **logo_url**: https://www.kindersley.ca/wp-content/uploads/2019/02/Town_of_Kindersley_logo_small.png
- **logo_basis**: logo image in the site header
- **domain**: kindersley.ca
- **key**: lead:a2073a8a30d121c7
- **name**: Kindersley
- **website**: https://kindersley.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Town of Kindersley
- **legal_name_stated_url**: https://www.kindersley.ca/
- **legal_name_stated_quote**: Home - Town of Kindersley Skip to content 1.306.463.2675 Mon-Fri: 8.30am-4.30pm Contact Us Report a Concern Search for: COMMU
- **tel_links**: +13064632675; 3064632675; 3064634577

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "106 5th Avenue East, Kindersley, SK S0L 1S0", "address_country": "CA", "address_url": "https://www.kindersley.ca/contact/", "address_method": "pattern", "address_quote": "Monday – Friday 8:30am – 4:30pm P.O Box 1269 106 5th Avenue East Kindersley, SK S0L 1S0 Get Directions Facebook Twitter Careers Meet the Mayor Report a Concern Staff D", "phone": "1.306.463.2675 Mon-Fri: 8.30am-4.30pm", "phone_url": "https://www.kindersley.ca/contact/", "emails": "office@kindersley.ca", "emails_url": "https://www.kindersley.ca/contact/", "domain": "kindersley.ca", "key": "vd:kindersley.ca", "name": "Kindersley", "website": "https://kindersley.ca/", "kind": "vendor", "date": "2026-11-03"}

## Vendor site facts (org_extras, thecse.com)
- **status**: ok
- **pages**: 4
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/canadian-securities-exchange
- **language**: fr
- **legal_name**: CNSX Markets Inc
- **legal_name_url**: https://thecse.com/fr/
- **legal_name_quote**: Pender Street, Suite 305 Vancouver, (Colombie-Britannique), V6E 2M6 Communiquer avec nous fr © 2026 CNSX Markets Inc. Tous droits réservés. Modalités du site Énoncé sur la protection des renseignements personnels Acc
- **logo_url**: https://thecse.com/apple-touch-icon.png
- **logo_basis**: site icon (apple-touch-icon)
- **domain**: thecse.com
- **key**: vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **name**: ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **website**: https://thecse.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1", "address_country": "CA", "address_url": "https://thecse.com/fr/contact-us/", "address_method": "address-tag", "address_quote": "416-572-4160 (télécopieur) 100 King Street West, Suite 7210 Toronto, (Ontario), M5X 1E1 Bureau de Vancouver 604-331-1213 604-687-1188 (télécopieur) 1095 West Pender St", "emails": "info@thecse.com", "emails_url": "https://thecse.com/fr/contact-us/", "domain": "thecse.com", "key": "vendor:ICEsoft Technologies Canada Corp. (Voyent Alert!)", "name": "ICEsoft Technologies Canada Corp. (Voyent Alert!)", "website": "https://thecse.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Kindersley | Q1914835 | official website on the organisation's domain (http://www.kindersley.ca/) + name |  | Kindersley | Kindersley | town |  | Canada | 1910-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:a2073a8a30d121c7",
 "ap_contact_team": {
  "emails": [
   "accountspayable@kindersley.ca",
   "office@kindersley.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accountspayable@kindersley.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kindersley.ca/contact/staff-directory/",
    "quote": "Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception – reception1@kindersley.ca Communications & Tourism Anna Polsfut, Comm",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Kindersley",
    "task_id": "CL-LD-17511"
   },
   {
    "email": "accountspayable@kindersley.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kindersley.ca/contact/staff-directory/",
    "quote": "Hilda Wessels, Accounts Payable Clerk/Reception – accountspayable@kindersley.ca Emma Dies, Corporate Services Assistant/Reception –",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Kindersley",
    "task_id": "CL-WS-00053"
   },
   {
    "email": "office@kindersley.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kindersley.ca/contact/report-a-concern/",
    "quote": "ress, location on street, nearby landmarks, description of pothole, etc. Submit Get in Touch Phone: (306) 4632675 Fax: (306) 4634577 Email: office@kindersley.ca Hours: Monday – Friday 8:30am – 4:30pm P.O Box 1269 106 5th Avenue East Kindersley, SK S0L 1S0 Get Directions Careers Departments",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Kindersley",
    "task_id": "CL-LD-17511"
   },
   {
    "email": "office@kindersley.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.kindersley.ca/contact/staff-directory/",
    "quote": "ne: (304) 463-2675 Fax: (306) 463-4577 Hours Monday – Friday 8:30 am – 4:30 pm Town Office Phone: (306) 463-2675 Fax: (306) 463-4577 Email: office@kindersley.ca Hours: Monday – Friday 8:30am – 4:30pm P.O Box 1269 106 5th Avenue East Kindersley, SK S0L 1S0 Get Directions Facebook Twitter Ca",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Kindersley",
    "task_id": "CL-WS-00053"
   }
  ]
 },
 "research_status": {
  "found": 4
 },
 "queries_tried": [
  "site crawl of kindersley.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of kindersley.ca (25 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 0)
_none_

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

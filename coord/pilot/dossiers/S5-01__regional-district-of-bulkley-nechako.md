# S5-01 — Regional District of Bulkley-Nechako ⇄ ICEsoft Technologies Canada Corp. (Voyent Alert!)

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Regional District of Bulkley-Nechako — 37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0 — buyer tax no. 121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
SUBMIT TO: finance@rdbn.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Regional District of Bulkley-Nechako (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ vendor 
```

## Relationship
- **rank_group**: T3
- **data_quality_score**: 71
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 6
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Regional District of Bulkley-Nechako (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: ICEsoft Technologies Canada Corp. (Voyent Alert!) | awarded 2026-11-03 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://www.rdbn.bc.ca/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=ources Admin Support About Voyent Alert! Product Features Resources Admin Support About Voyent Alert! Contact Suite 340 600 Crowfoot Crescent NW Calgary,  | status rule: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:57d27233c4bccab6
- **tier**: T
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Regional District of Bulkley-Nechako
- **buyer_website**: https://rdbn.bc.ca/
- **buyer_address**: 37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0
- **buyer_phone**: 250-692-3195
- **buyer_contact_evidence_url**: https://www.rdbn.bc.ca/contacts
- **buyer_legal_name_as_published**: Regional District of Bulkley-Nechako
- **buyer_bn_as_published**: 121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 121430631RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://www.rdbn.bc.ca/application/files/thumbnails/small/1816/4866/5339/RDBN_Colour_Logo.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/rdbn/
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q2095384; regional district in British Columbia
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.rdbn.bc.ca/contacts (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@rdbn.bc.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://www.rdbn.bc.ca/departments/finance/contacts
- **email_evidence_quote**: Finance Contacts Contact the RDBN Finance Department Phone: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 General Finance inquiries: finance@rdbn.bc.ca Accounts Payable:
- **email_evidence_context**: es Recycling, Garbage, and Utilities Finance Planning Agriculture Hospital Districts Home Departments Finance Finance Contacts Contact the RDBN Finance Department Phone: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 General Finance inquiries: finance@rdbn.bc.ca Accounts Payable: ap@rdbn.bc.ca Accounts Receivable: ar@rdbn.bc.ca Online Payments Reports Annual Budgets Your Property Assessment Change and your Property Taxes Paying Your Property Taxes Long-term Financing Rural Property Tax Estimator BC Assessme (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@rdbn.bc.ca (finance/accounting dept or supplier-payment office) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03 | page: https://www.rdbn.bc.ca/departments/finance/contacts | quote: "Finance Contacts Contact the RDBN Finance Department Phone: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 General Finance inquiries: finance@rdbn.bc.ca A" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00046
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:itservices@rdffg.bc.ca,mailto:dmarc_agg@vali.email; ruf=mailto:itservices@rdffg.bc.ca; fo=1;
- **dmarc_record_domain**: rdbn.bc.ca
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: (250) 692-3195 (as printed on https://www.rdbn.bc.ca/departments/finance/contacts, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "(250) 692-3195 (as printed on https://www.rdbn.bc.ca/departments/finance/contacts, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Regional District of Bulkley-Nechako — 37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0 — buyer tax no. 121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: finance@rdbn.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Regional District of Bulkley-Nechako (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ vendor 
- **invoice_card_json**: {"bill_to": {"legal_name": "Regional District of Bulkley-Nechako", "legal_name_is_published": true, "address": "37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0", "address_is_the_invoice_address": false, "tax_number": "121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "finance@rdbn.bc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identit
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
- **contract_status**: active service seen on the buyer's own site (2026-11-03): Canada-HQ vendor ICEsoft Technologies Canada Corp. (Voyent Alert!)
- **award_date**: 2026-11-03
- **contract_link**: https://www.rdbn.bc.ca/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 121430631RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Regional District of Bulkley-Nechako — 37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0 — buyer tax no. 121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv) ⏎ SUBMIT TO: finance@rdbn.bc.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: ICEsoft Technologies Canada Corp. (Voyent Alert!) — 100 King Street West, Suite 7210, Toronto, (Ontario), M5X 1E1 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Regional District of Bulkley-Nechako (municipality / local government, jurisdiction not stated) — active paid service of a Canada-HQ vendor 
- **invoice_card_json**: {"bill_to": {"legal_name": "Regional District of Bulkley-Nechako", "legal_name_is_published": true, "address": "37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0", "address_is_the_invoice_address": false, "tax_number": "121430631RP0001 (recipient_business_number in the federal grants & contributions disclosure, 5 agreement(s), last 2022-04-25; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)", "language": "en"}, "submit_to": {"email": "finance@rdbn.bc.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identit
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@rdbn.bc.ca (finance/accounting dept or supplier-payment office)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-03", "page: https://www.rdbn.bc.ca/departments/finance/contacts", "quote: \"Finance Contacts Contact the RDBN Finance Department Phone: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 General Finance inquiries: finance@rdbn.bc.ca A\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00046"], "buyer_facts": ["address and phone: the buyer's own site, https://www.rdbn.bc.ca/contacts (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "phone / ro

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.rdbn.bc.ca/departments/finance/contacts | 2026-11-08 | ok |  |  |  | (250) 692-3195 |  |  |  |  |  |

## Buyer site facts (org_extras, rdbn.bc.ca)
- **status**: ok
- **pages**: 2
- **language**: en
- **legal_name**: Regional District of Bulkley-Nechako
- **legal_name_url**: https://www.rdbn.bc.ca/
- **legal_name_quote**: nities Current Bid Opportunities Media Board Highlights - July/August 2026 Saik’uz First Nation and Regional District of Bulkley-Nechako Sign Protocol Agreement Water Station now open in Fort St. James Statement on Tumbler Ridge Shootin
- **logo_url**: https://www.rdbn.bc.ca/application/files/thumbnails/small/1816/4866/5339/RDBN_Colour_Logo.png
- **logo_basis**: logo image in the site header
- **domain**: rdbn.bc.ca
- **key**: lead:57d27233c4bccab6
- **name**: Regional District of Bulkley-Nechako
- **website**: https://rdbn.bc.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Regional District of Bulkley-Nechako
- **legal_name_stated_url**: https://www.rdbn.bc.ca/
- **legal_name_stated_quote**: nities Current Bid Opportunities Media Board Highlights - July/August 2026 Saik’uz First Nation and Regional District of Bulkley-Nechako Sign Protocol Agreement Water Station now open in Fort St. James Statement on Tumbler Ridge Shootin
- **mentions**: {'payment_method': {'text': 'credit card payments', 'url': 'https://www.rdbn.bc.ca/', 'quote': 'hwest British Columbia Resource Benefits Alliance. The Regional District of Bulkley-Nechako accepts credit card payments. Home Departments Media & Status Updates Gallery Contacts Events & Programs Masterplan Copyright ©'}}
- **linkedin_url**: https://www.linkedin.com/company/rdbn/

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "37 3rd Avenue, PO Box 820, Burns Lake, British Columbia V0J 1E0", "address_country": "CA", "address_url": "https://www.rdbn.bc.ca/contacts", "address_method": "pattern", "address_quote": "ct Information Location: 37 3rd Avenue, PO Box 820 Burns Lake, British Columbia V0J 1E0 Email: info@rdbn.bc.ca Phone: 250-692-3195 / 1-800-320-3339 Fax: 250-692-3305 O", "phone": "250-692-3195", "phone_url": "https://www.rdbn.bc.ca/contacts", "emails": "admin@rdbn.bc.ca; info@rdbn.bc.ca", "emails_url": "https://www.rdbn.bc.ca/contacts", "domain": "rdbn.bc.ca", "key": "vd:rdbn.bc.ca", "name": "Regional District of Bulkley-Nechako", "website": "https://rdbn.bc.ca/", "kind": "vendor", "date": "2026-11-03"}

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
| b | Regional District of Bulkley-Nechako | Q2095384 | official website on the organisation's domain (https://www.rdbn.bc.ca/) + name |  | Regional District of Bulkley-Nechako | district régional de Bulkley-Nechako | regional district in British Columbia |  | Canada |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:57d27233c4bccab6",
 "ap_contact_team": {
  "emails": [
   "finance@rdbn.bc.ca",
   "ap@rdbn.bc.ca",
   "info@rdbn.bc.ca",
   "admin@rdbn.bc.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@rdbn.bc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/departments/finance/budgets",
    "quote": "ance Annual Budgets For further information about the Budget details or process, please contact us by phone at 250 692 3195, or by email at finance@rdbn.bc.ca. 2026 Budget 2025 Budget 2024 Budget 2023 Budget 2022 Budget 2021 Budget 2020 Budget 2019 Budget 2018 Budget 2017 Budget 2016 Budge",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-LD-17486"
   },
   {
    "email": "ap@rdbn.bc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/departments/finance/contacts",
    "quote": "Accounts Payable: ap@rdbn.bc.ca Accounts Receivable: ar@rdbn.bc.ca Online Payments Reports Annual Budgets Your Property Assessment Change and your Property Taxes Paying",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-LD-17486"
   },
   {
    "email": "finance@rdbn.bc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/departments/finance/contacts",
    "quote": "Finance Contacts Contact the RDBN Finance Department Phone: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 General Finance inquiries: finance@rdbn.bc.ca Accounts Payable:",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-WS-00046"
   },
   {
    "email": "ap@rdbn.bc.ca",
    "type": "accounts_payable",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/departments/finance/contacts",
    "quote": "Accounts Payable: ap@rdbn.bc.ca Accounts Receivable:",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-WS-00046"
   },
   {
    "email": "info@rdbn.bc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/departments/hospital-districts/hospital-district-contacts",
    "quote": "urns Lake, B.C. V0J 1E0 Office Location: 37 - 3rd Avenue, Burns Lake, B.C. Tel: (250) 692-3195 or 1-800-320-3339 Fax: (250) 692-3305 Email: info@rdbn.bc.ca Northwest Regional Hospital District Suite 300-4545 Lazelle Avenue Terrace, BC V8G 4E1 Tel: 250-615-6100 Fax: 250-635-9222 Toll Free:",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-LD-17486"
   },
   {
    "email": "admin@rdbn.bc.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.rdbn.bc.ca/contacts",
    "quote": "ces, Human Resources Advisor​​​​​​, Administration Clerk, and First Nations Liaison. To contact the Administration Department, please email admin@rdbn.bc.ca . Finance Department: The Finance Department includes the Chief Financial Officer​​​​​​ and Payroll, Accounts Receivable, and Account",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Regional District of Bulkley-Nechako",
    "task_id": "CL-WS-00046"
   }
  ]
 },
 "research_status": {
  "found": 6
 },
 "queries_tried": [
  "site crawl of rdbn.bc.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of rdbn.bc.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of rdbn.bc.ca (25 pages, robots.txt respected), no AI, no search engine",
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
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

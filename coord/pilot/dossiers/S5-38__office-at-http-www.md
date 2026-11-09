# S5-38 — Office at: http://www ⇄ 598424 Ontario Ltd. o/a R. Russell Construction

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Office at: http://www — 331 Aberdeen Drive, London, ON N5V 4S4
SUBMIT TO: accounting@ldca.on.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: 598424 Ontario Ltd. o/a R. Russell Construction — P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Office at: http://www (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vend
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 56
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Office at: http://www (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: 598424 Ontario Ltd. o/a R. Russell Construction | published by: the Canada-located vendor's own website | record: https://www.rrussellconstruction.ca/ | vendor in Canada because: vendor located in Canada (wall)=rrussellconstruction.ca | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:0d9efd93c5fc7fa5
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Office at: http://www
- **buyer_website**: https://ldca.on.ca/
- **buyer_address**: 331 Aberdeen Drive, London, ON N5V 4S4
- **buyer_phone**: 519 453 5322
- **buyer_contact_evidence_url**: https://ldca.on.ca/page/ContactUs
- **buyer_legal_name_as_published**: Office at: http://www
- **buyer_logo_url**: https://cdn.ymaws.com/ldca.site-ym.com/graphics/logo2024.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/79964333
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://ldca.on.ca/page/ContactUs (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: accounting@ldca.on.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://ldca.on.ca/page/ContactUs
- **email_evidence_quote**: ?subject=Message%20from%20LDCA%20Website">Kerry Rajotte</a></td> </tr> <tr> <td>Accounting</td> <td><a href="mailto:Accounting@ldca.on.ca?subject=Message%20from%20LDCA%20Website">Raven MacKinnon</a></td> </tr> <tr> <td>Member Services</td> <td><a href="mailto:member
- **mailbox_provenance**: accounting@ldca.on.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://ldca.on.ca/page/ContactUs | quote: "?subject=Message%20from%20LDCA%20Website">Kerry Rajotte</a></td> </tr> <tr> <td>Accounting</td> <td><a href="mailto:Accounting@ldca.on.ca?subject=Message%20from" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06206
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none;
- **dmarc_record_domain**: ldca.on.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:64.187.178.10 include:spf.protection.outlook.com include:amazonses.com include:spfa.cpmails.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Office at: http://www — 331 Aberdeen Drive, London, ON N5V 4S4 ⏎ SUBMIT TO: accounting@ldca.on.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: 598424 Ontario Ltd. o/a R. Russell Construction — P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Office at: http://www (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vend
- **invoice_card_json**: {"bill_to": {"legal_name": "Office at: http://www", "legal_name_is_published": true, "address": "331 Aberdeen Drive, London, ON N5V 4S4", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@ldca.on.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "598424 Ontario Ltd. o/a R. Russell Construction", "bn9": "", "neq": "", "remit_address": "P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada"}, "follow_up": {"ap_phone": "519 453 5322", "ap_contact": "", "requirements_text": ""}}
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: 598424 Ontario Ltd. o/a R. Russell Construction
- **vendor_address**: P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada
- **vendor_country_basis**: vendor located in Canada (wall)=rrussellconstruction.ca
- **vendor_website**: https://www.rrussellconstruction.ca/
- **vendor_emails**: office@rrussellconstruction.ca
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); website: https://www.rrussellconstruction.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_link**: https://www.rrussellconstruction.ca/
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
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Office at: http://www — 331 Aberdeen Drive, London, ON N5V 4S4 ⏎ SUBMIT TO: accounting@ldca.on.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: 598424 Ontario Ltd. o/a R. Russell Construction — P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Office at: http://www (organisation (type not stated in the record), jurisdiction not stated) — named as a client by the Canada-located vend
- **invoice_card_json**: {"bill_to": {"legal_name": "Office at: http://www", "legal_name_is_published": true, "address": "331 Aberdeen Drive, London, ON N5V 4S4", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "accounting@ldca.on.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "598424 Ontario Ltd. o/a R. Russell Construction", "bn9": "", "neq": "", "remit_address": "P.O. Box 111 Lambeth Stn, London, ON, N6P 1P9, Canada"}, "follow_up": {"ap_phone": "519 453 5322", "ap_contact": "", "requirements_text": ""}}
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["accounting@ldca.on.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://ldca.on.ca/page/ContactUs", "quote: \"?subject=Message%20from%20LDCA%20Website\">Kerry Rajotte</a></td> </tr> <tr> <td>Accounting</td> <td><a href=\"mailto:Accounting@ldca.on.ca?subject=Message%20from\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-06206"], "buyer_facts": ["address and phone: the buyer's own site, https://ldca.on.ca/page/ContactUs (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "website: https://www.rrussellconstruction.ca/"], "relationship": "tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer"}

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://ldca.on.ca/page/ContactUs | 2026-11-08 | http_500 |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, ldca.on.ca)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://cdn.ymaws.com/ldca.site-ym.com/graphics/logo2024.png
- **logo_basis**: logo image in the site header
- **legal_name**: Office at: http://www
- **legal_name_url**: https://ldca.on.ca/ams/legal-privacy.htm
- **legal_name_quote**: otification. For further information about the DMCA, please visit the Website of the U.S. Copyright Office at: http://www.copyright.gov/onlinesp . YourMembership.com Privacy Policy For information regarding YourMembership
- **domain**: ldca.on.ca
- **key**: lead:0d9efd93c5fc7fa5
- **name**: Office at: http://www
- **website**: https://ldca.on.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'esignature': {'text': 'electronic signature; Identification of the material that has been removed or to which access has be', 'url': 'https://ldca.on.ca/ams/legal-privacy.htm', 'quote': 'ter notification is a written communication that incorporates the following elements: A physical or electronic signature; Identification of the material that has been removed or to which access has been disabled and the location at which the material appeared'}}
- **linkedin_url**: https://www.linkedin.com/company/79964333

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "331 Aberdeen Drive, London, ON N5V 4S4", "address_country": "CA", "address_url": "https://ldca.on.ca/page/ContactUs", "address_method": "pattern", "address_quote": "Phone 519 453 5322 Email info@ldca.on.ca Address 331 Aberdeen Drive London, ON N5V 4S4 Get directions → Office Hours Monday – Friday, 8:00 am – 4:00 pm For after-hour", "phone": "519 453 5322", "phone_url": "https://ldca.on.ca/page/ContactUs", "emails": "accounting@ldca.on.ca; info@ldca.on.ca", "emails_url": "https://ldca.on.ca/page/ContactUs", "domain": "ldca.on.ca", "key": "lead:0d9efd93c5fc7fa5", "name": "ldca.on.ca", "website": "https://ldca.on.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, domain unknown)
_not read_

## Vendor role mailboxes found on its site (org_contacts)
_not read_

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | 598424 Ontario Ltd. o/a R. Russell Construction | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=598424%20Ontario%20Ltd.%20o%2Fa%20R.%20Russell%20Construction | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Office at: http://www |  |  |  |  |  |  |  |  |  |  |
| b | 598424 Ontario Ltd. o/a R. Russell Construction |  |  |  |  |  |  |  |  |  |  |
| v | 598424 Ontario Ltd. o/a R. Russell Construction |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:0d9efd93c5fc7fa5",
 "ap_contact_team": {
  "emails": [
   "accounting@ldca.on.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "accounting@ldca.on.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://ldca.on.ca/page/ContactUs",
    "quote": "?subject=Message%20from%20LDCA%20Website\">Kerry Rajotte</a></td> </tr> <tr> <td>Accounting</td> <td><a href=\"mailto:Accounting@ldca.on.ca?subject=Message%20from%20LDCA%20Website\">Raven MacKinnon</a></td> </tr> <tr> <td>Member Services</td> <td><a href=\"mailto:member",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "ldca.on.ca",
    "task_id": "CL-LD-06206"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of ldca.on.ca (28 pages, robots.txt respected), no AI, no search engine"
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

## The vendor's other buyers in the dataset (first 60 of 13)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_bidsandtenders:f601f77a-b5ab-4695-9fe2-5541ad4d5396:8 | London District Catholic School Board | Prequalification for Paving and Concrete Contractors |  |  |  | https://ldcsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/f601f77a-b5ab-4695-9fe2-5541ad4d5396 |
| ca_bidsandtenders:37b8a246-1449-4049-9fb7-c90a0a069e51:1 | City of St. Thomas | St. George and Pearl St. Reconstruction (under RFPQ2026-010) | 1478890.65 |  |  | https://stthomas.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/37b8a246-1449-4049-9fb7-c90a0a069e51 |
| ca_bidsandtenders:4837c8bd-ed03-408e-8a6c-b53995389dea:1 | Municipality of South Huron | Exeter WWTP Sand Filter Media Replacement - Phase 2 | 1036167.4 |  |  | https://southhuron.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/4837c8bd-ed03-408e-8a6c-b53995389dea |
| ca_bidsandtenders:5e1634df-a4d4-4929-95df-fef5ac4dcadf:2 | City of St. Thomas | Prequalification - St. George and Pearl St. Construction |  |  |  | https://stthomas.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/5e1634df-a4d4-4929-95df-fef5ac4dcadf |
| ca_bidsandtenders:2efea1f3-e320-468f-a8d0-5e047bb83bce:1 | Municipality of West Perth | Wellington Street Reconstruction and Frank Street Watermain |  |  |  | https://westperth.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/2efea1f3-e320-468f-a8d0-5e047bb83bce |
| ca_bidsandtenders:c6edc0d7-1a0c-40ad-b26d-4680c1cadef2:14 | Lambton Kent District School Board | Contractor Qualification |  |  |  | https://lkdsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c6edc0d7-1a0c-40ad-b26d-4680c1cadef2 |
| ca_bidsandtenders:01461d70-50db-4893-8003-6d488a32f4ca:1 | Town of Ingersoll | Raglan Street Reconstruction | 1126731.5 |  |  | https://ingersoll.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/01461d70-50db-4893-8003-6d488a32f4ca |
| ca_bidsandtenders:703723b1-38a6-4b08-8f15-398c8d2a6379:1 | Town of Tillsonburg | Townline Road Storm Sewers |  |  |  | https://tillsonburg.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/703723b1-38a6-4b08-8f15-398c8d2a6379 |
| ca_bidsandtenders:a8305530-5cd1-4241-9b94-993725e61cd1:1 | Oxford County | Bobolink Drive Watermain Upgrades |  |  |  | https://oxfordcounty.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/a8305530-5cd1-4241-9b94-993725e61cd1 |
| ca_bidsandtenders:bdce4b72-fe4e-48fd-b4e5-20ad31680cc0:8 | London District Catholic School Board | Prequalification for Subtrades |  |  |  | https://ldcsb.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/bdce4b72-fe4e-48fd-b4e5-20ad31680cc0 |
| ca_bidsandtenders:1da387ae-2b8f-4429-931e-ce9e02dd656e:1 | City of London | 2022 Infrastructure Renewal Program Northcrest Drive | 992370.0 |  |  | https://london.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/1da387ae-2b8f-4429-931e-ce9e02dd656e |
| ca_bidsandtenders:472ddaaf-b424-4670-abcc-e873d60a2fde:1 | City of St. Thomas | William St and St Annes Place Construction |  |  |  | https://stthomas.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/472ddaaf-b424-4670-abcc-e873d60a2fde |
| ca_bidsandtenders:79eddc0d-1a87-4d00-9f2d-91a8f7c28913:1 | City of St. Thomas | Apron Expansion - St. Thomas Municipal Airport |  |  |  | https://stthomas.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/79eddc0d-1a87-4d00-9f2d-91a8f7c28913 |

## Open questions for hand research (layer 2)

- the vendor's GST/HST number (BN9)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

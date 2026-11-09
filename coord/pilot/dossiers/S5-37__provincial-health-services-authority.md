# S5-37 — Provincial Health Services Authority ⇄ inferred: BC Hydro

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about) — PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only) — buyer tax no. 863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)
SUBMIT TO: phsainventory_apinvoices@hssbc.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware | format: Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Provinc
```

## Relationship
- **rank_group**: I4
- **data_quality_score**: 61
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: Provincial Health Services Authority (hospital / health authority, BC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: BC Hydro | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.bchydro.com/contact.html: 'Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3' | status rule: inferred relationship (no record): medium confidence; the buyer is an institution (school, college, university, health or government body) in British Columbia (province from the postal code on its own page (V3A 8H3)); BC
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: wd:Q7252644
- **tier**: I
- **grade**: 4

## Buyer
- **buyer**: Provincial Health Services Authority
- **buyer_website**: https://hssbc.ca
- **buyer_address**: 200 - 1333 BROADWAY W, VANCOUVER, BC, V6H4C1 (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)
- **buyer_phone**: 604-675-7400
- **buyer_contact_evidence_url**: https://www.phsa.ca/contact-us
- **buyer_legal_name_as_published**: BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about)
- **buyer_bn_as_published**: 863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 863530135RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://www.phsa.ca/SiteAssets/phsa-logo.png
- **buyer_website_status**: site answers
- **buyer_type**: hospital / health authority
- **buyer_sector**: healthcare
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)
- **buyer_charity_designation**: C; 0110
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7252644; nonprofit organization
- **buyer_founded**: 2001-00-00 (Wikidata Q7252644, exact name match + country + organisation claims; 2026-11-08)
- **buyer_budget_or_revenue**: revenue 2511478460 Q1104069; 2314971656 Q1104069; 2553308536 Q1104069; 2749476871 Q1104069; 3801511829 Q1104069; 4536546593 Q110 (Wikidata Q7252644, exact name match + country + organisation claims; 2026-11-08)
- **buyer_employees**: 5842; 4278; 4703; 14932; 15163; 16094; 17326; 18585; 20245; 3847; 3672; 5435; 5535; 5720 (Wikidata Q7252644, exact name match + country + organisation claims; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.phsa.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the lane's AP page (https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf); invoice mailing address: the lane's AP page (https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf); invoicing requirements: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: phsainventory_apinvoices@hssbc.ca
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf
- **email_evidence_quote**: PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 PHSAInventory_APInvoices@hssbc.ca Fraser Health (FHA) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 FHA_APInvoices@hssbc.ca Interior Health (IHA
- **email_evidence_context**: Willingdon Avenue, PHSA_APinvoices@phsa.ca Burnaby, BC V5C 6E3 Provincial Health Services Authority (PHSA) 1795 Willingdon Avenue, PHSA_Invoices@pdf.basware.com Burnaby, BC V5C 6E3 PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, PHSAInventory_APInvoices@hssbc.ca Langley, BC V3A 8H3 Fraser Health (FHA) PO Box 4001 Station Location 1, FHA_APInvoices@hssbc.ca Langley, BC V3A 8H3 Interior Health (IHA) #101 – 2355 Ackland Rd AP_VEN_INVOICES@interiorhealth.ca Kelowna, BC V1X 7X9 Northern Health (NHA) 300 299 Vict (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: phsainventory_apinvoices@hssbc.ca (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf | quote: "PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 PHSAInventory_APInvoices@hssbc.ca Fraser Health (FHA) PO Box 4001 Stati" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ?all (neutral); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011052
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ?all (neutral); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:dmarc@phsa.ca
- **dmarc_record_domain**: hssbc.ca
- **spf_policy**: SPF ?all (neutral)
- **spf_record**: v=spf1 include:spf365.phsa.ca ?all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 604-455-1304 ext.741487
- **invoice_mailing_address**: PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)
- **invoicing_requirements**: Jan2026: submitphysicalinvoiceorPDFemailattachmenttobuyer-specificroute;statementsmonthlytoseparatestatementmailbox. PO#wheneverpossible;negotiatedaccuratepricesonly;latechargesonlyifcontractuallydefined. May2026inquiries:current0–30daysnoresponse,31–60daysinquiry,61–120manager,120+director,150+seni | invoice format as published: Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08)
- **invoice_portal_url**: Basware
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: Basware
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer", "invoice_format": "Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08)", "ap_phone": "604-455-1304 ext.741487", "mailing_address": "PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)", "requirements_text": "Jan2026: submitphysicalinvoiceorPDFemailattachmenttobuyer-specificroute;statementsmonthlytoseparatestatementmailbox. PO#wheneverpossible;negotiatedaccuratepricesonly;latechargesonlyifcontractuallydefined. May2026inquiries:current0–30daysnoresponse,31–60daysinquiry,61–120manager,120+director,150+seni"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about) — PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only) — buyer tax no. 863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province) ⏎ SUBMIT TO: phsainventory_apinvoices@hssbc.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware | format: Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPT
- **invoice_card_json**: {"bill_to": {"legal_name": "BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about)", "legal_name_is_published": true, "address": "PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)", "address_is_the_invoice_address": true, "tax_number": "863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)", "language": "en"}, "submit_to": {"email": "phsainventory_apinvoices@hssbc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)", "format": "Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08)", "system": "named on the buyer's page: Basware", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_num
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 76
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: inferred: BC Hydro
- **vendor_address**: 333 Dunsmuir St., Vancouver, B.C. V6B 5R3
- **vendor_country_basis**: the vendor's own site, https://www.bchydro.com/contact.html: 'Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3'
- **vendor_website**: https://www.bchydro.com
- **vendor_phone**: 1 800 224 9376
- **vendor_contact_evidence_url**: https://www.bchydro.com/toolbar/contact.html
- **vendor_logo_url**: https://www.bchydro.com/content/experience-fragments/bchydro-web/header/master/_jcr_content/root/container/container/image.coreimg.svg/1723787760686/logo-bchydro.svg
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); phone / role e-mails / logo: the vendor's own site, https://www.bchydro.com/toolbar/contact.html (tools/org_contacts.py, org_extras.py); website: https://www.bchydro.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an institution (school, college, university, health or government body) in British Columbia (province from the postal code on its own page (V3A 8H3)); BC Hydro is the electricity utility for most of British Columbia (FortisBC and a few municipal utilities serve parts of the Okanagan and Kootenays); it pays electricity for the buildings it operates
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 863530135RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about) — PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only) — buyer tax no. 863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province) ⏎ SUBMIT TO: phsainventory_apinvoices@hssbc.ca (invoicing/AP mailbox, confirmed by the referee) | invoice portal: Basware | format: Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of BC on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPT
- **invoice_card_json**: {"bill_to": {"legal_name": "BC Early Hearing Program BC Emergency Health Services (stated on https://www.phsa.ca/about)", "legal_name_is_published": true, "address": "PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)", "address_is_the_invoice_address": true, "tax_number": "863530135RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name + province)", "language": "en"}, "submit_to": {"email": "phsainventory_apinvoices@hssbc.ca", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "Basware", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "PO Box 4001 Station Location 1, Langley, BC V3A 8H3 (PHSA Langley Fulfillment Centre inventory only)", "format": "Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed (as printed on https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf, re-read 2026-11-08)", "system": "named on the buyer's page: Basware", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_num
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 76
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; invoice format / requirements published; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["phsainventory_apinvoices@hssbc.ca (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf", "quote: \"PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 PHSAInventory_APInvoices@hssbc.ca Fraser Health (FHA) PO Box 4001 Stati\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ?all (neutral); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-WD-011052"], "buyer_facts": ["address and phone: the buyer's own site, https://www.phsa.ca/contact-us (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the lane's AP page (https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf)", "invoice mailing address: the lane's AP page (https://www.phsa.ca/our-services-

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf | 2026-11-08 | ok |  |  | Basware |  | 2355 Ackland Rd AP_VEN_INVOICES@interiorhealth.ca Kelowna, BC V1X 7X9 | Invoice Submissions Invoices must be submitted physically or digitally in PDF format as attachments to the email address listed |  |  |  |

## Buyer site facts (org_extras, hssbc.ca)
- **status**: ok
- **pages**: 6
- **v**: 2
- **legal_name_stated**: BC Early Hearing Program BC Emergency Health Services
- **legal_name_stated_url**: https://www.phsa.ca/about
- **legal_name_stated_quote**: ervices BC Cancer BC Centre for Disease Control BC Children's Hospital and Sunny Hill Health Centre BC Early Hearing Program BC Emergency Health Services BC Mental Health & Substance Use Services BC Renal BC Surgical Patient Registry BC Transplant BC Wo
- **language**: en
- **logo_url**: https://www.phsa.ca/SiteAssets/phsa-logo.png
- **logo_basis**: logo image in the site header
- **domain**: hssbc.ca
- **key**: wd:Q7252644
- **name**: Provincial Health Services Authority
- **website**: https://hssbc.ca/
- **kind**: buyer
- **date**: 2026-11-08

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "phone": "604-675-7400", "phone_url": "https://www.phsa.ca/contact-us", "domain": "hssbc.ca", "key": "wd:Q7252644", "name": "Provincial Health Services Authority", "website": "https://hssbc.ca/", "kind": "buyer", "date": "2026-11-08"}

## Vendor site facts (org_extras, bchydro.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.bchydro.com/content/experience-fragments/bchydro-web/header/master/_jcr_content/root/container/container/image.coreimg.svg/1723787760686/logo-bchydro.svg
- **logo_basis**: logo image in the site header
- **domain**: bchydro.com
- **key**: lead:91f9dd8f8d8b6802
- **name**: BC Hydro and Power Authority
- **website**: https://bchydro.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: B.C. Utilities Commission
- **legal_name_stated_url**: https://www.bchydro.com/toolbar/about.html
- **legal_name_stated_quote**: cture, conserve, supply, acquire, and dispose of power and related products Regulatory power to the B.C. Utilities Commission (BCUC), to ensure our customers receive safe, reliable and non-discriminatory energy services at fa
- **linkedin_url**: https://ca.linkedin.com/company/bchydro
- **tel_links**: 18002249376; 1 800 224 9376

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "P.O. Box 8910, Vancouver, B.C., V6B 4X3", "address_country": "CA", "address_url": "https://www.bchydro.com/toolbar/contact.html", "address_method": "pattern", "address_quote": "even to eight business days. Mail Mailing address P.O. Box 8910 Vancouver, B.C. V6B 4X3 Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3 Corporate inform", "phone": "1 800 224 9376", "phone_url": "https://www.bchydro.com/toolbar/contact.html", "domain": "bchydro.com", "key": "lead:304f77e20b959d3b", "name": "bchydro.com", "website": "https://bchydro.com/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Provincial Health Services Authority | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Provincial%20Health%20Services%20Authority | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | BC Hydro and Power Authority | Q795720 | official website on the organisation's domain (https://www.bchydro.com/) + name |  | B.C. Hydro | BC Hydro | state-owned enterprise | Crown corporation | Canada | 1961-01-01 | Vancouver |
| b | Provincial Health Services Authority | Q7252644 | exact name match + country + organisation claims |  | Provincial Health Services Authority | Provincial Health Services Authority | nonprofit organization |  | Canada | 2001-00-00 |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "wd:Q7252644",
 "ap_contact_team": {
  "emails": [
   "phsainventory_apinvoices@hssbc.ca",
   "phsa_apinvoices@phsa.ca",
   "phsa_invoices@pdf.basware.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "phsainventory_apinvoices@hssbc.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf",
    "quote": "PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 PHSAInventory_APInvoices@hssbc.ca Fraser Health (FHA) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 FHA_APInvoices@hssbc.ca Interior Health (IHA",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Provincial Health Services Authority",
    "task_id": "CL-WD-011052"
   },
   {
    "email": "phsa_apinvoices@phsa.ca",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf",
    "quote": "he email address listed. Entity Address Invoice Submission Email Vancouver Coastal Health (VCH) 1795 Willingdon Avenue, Burnaby, BC V5C 6E3 PHSA_APinvoices@phsa.ca Providence Health (PHC) 1795 Willingdon Avenue, Burnaby, BC V5C 6E3 PHSA_APinvoices@phsa.ca Provincial Health Services Authori",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Provincial Health Services Authority",
    "task_id": "CL-WD-011052"
   },
   {
    "email": "phsa_invoices@pdf.basware.com",
    "type": "invoice_submission",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.phsa.ca/our-services-site/Documents/AP%20Invoice%20and%20Statement%20Submissions_30JAN26.pdf",
    "quote": "Provincial Health Services Authority (PHSA) 1795 Willingdon Avenue, Burnaby, BC V5C 6E3 PHSA_Invoices@pdf.basware.com PHSA Langley Fulﬁllment Centre (LFC) PO Box 4001 Station Location 1, Langley, BC V3A 8H3 PHSAInventory_APInvoices@hssbc.",
    "retrieved_date": "2026-10-28",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Provincial Health Services Authority",
    "task_id": "CL-WD-011052"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site crawl of www.phsa.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.phsa.ca (25 pages, robots.txt respected), no AI, no search engine",
  "site crawl of www.phsa.ca (25 pages, robots.txt respected), no AI, no search engine"
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

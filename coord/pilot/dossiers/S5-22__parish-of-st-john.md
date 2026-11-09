# S5-22 — PARISH OF ST JOHN ⇄ inferred: BC Hydro

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: St. John the Divine Anglican Church — PO BOX 236, Garibaldi Highlands, BC, V0N1T0 — buyer tax no. 893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name)
SUBMIT TO: info@squamishanglicanchurch.ca (general mailbox, confirmed by the referee) | invoice portal: SAP Ariba
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: PARISH OF ST JOHN (municipality / local government, BC) — inferred: no record; the organisation's type and province make a Canadian supplier
```

## Relationship
- **rank_group**: I1
- **data_quality_score**: 29
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: LOW (plausible supplier only)
- **relationship_detail**: PARISH OF ST JOHN (municipality / local government, BC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: BC Hydro | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.bchydro.com/contact.html: 'Corporate head office 333 Dunsmuir St. Vancouver, B.C. V6B 5R3' | status rule: inferred relationship (no record): low confidence; the buyer is an organisation in British Columbia (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); BC Hydro is the electricity u
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:893030643
- **tier**: I
- **grade**: 1

## Buyer
- **buyer**: PARISH OF ST JOHN
- **buyer_website**: https://squamishanglicanchurch.ca
- **buyer_address**: PO BOX 236, Garibaldi Highlands, BC, V0N1T0
- **buyer_phone**: 604-898-5100
- **buyer_contact_evidence_url**: https://www.squamishanglicanchurch.ca:443/contact
- **buyer_legal_name_as_published**: St. John the Divine Anglican Church
- **buyer_bn_as_published**: 893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 893030643RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://dq5pwpg1q8ru0.cloudfront.net/2021/11/10/12/39/22/6a9dd36a-a0a9-4ead-8899-1f6fdb7f8d74/St%20John%20the%20Divine%20Squamish%20(1).png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name)
- **buyer_charity_designation**: C; 0030
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.squamishanglicanchurch.ca:443/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@squamishanglicanchurch.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://www.squamishanglicanchurch.ca/
- **email_evidence_quote**: Location 1930 Diamond Road Squamish, BC View on Google Maps P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Contact Phone: 604-898-5100 Email : info@squamishanglicanchurch.ca Office Hours Wednesdays and Thursdays 9:00AM - 12:00PM Menu Home Rentals About Give Rector's Reflection Calendar Events
- **email_evidence_context**: ign up for our Newsletter Subscribe to receive email updates with the latest news. Enter Your Email Subscribe Location 1930 Diamond Road Squamish, BC View on Google Maps P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Contact Phone: 604-898-5100 Email : info@squamishanglicanchurch.ca Office Hours Wednesdays and Thursdays 9:00AM - 12:00PM Menu Home Rentals About Give Rector's Reflection Calendar Events About About Us Our Staff I'm New Our History Labyrinth Quilts Donate to St John the Divine Squamish ACKNOWLEDGEMENT St. John the (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@squamishanglicanchurch.ca (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://www.squamishanglicanchurch.ca/ | quote: "Location 1930 Diamond Road Squamish, BC View on Google Maps P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Contact Phone: 604-898-5100 Email : info@squamishanglica" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-09139
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.squamishanglicanchurch.ca; confirmed by 8.8.8.8
- **spf_policy**: no SPF record
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoice_portal_url**: SAP Ariba
- **invoice_portal_kind**: actionable supplier / invoice portal named by the buyer
- **invoice_portal_note**: (additional channel named on the buyer's page; the e-mail is the contact)
- **ap_system_hint**: named on the buyer's page: SAP Ariba
- **invoicing_requirements_structured**: {"submission_channel": "e-mail + portal", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: St. John the Divine Anglican Church — PO BOX 236, Garibaldi Highlands, BC, V0N1T0 — buyer tax no. 893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name) ⏎ SUBMIT TO: info@squamishanglicanchurch.ca (general mailbox, confirmed by the referee) | invoice portal: SAP Ariba ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: PARISH OF ST JOHN (municipality / local government, BC) — inferred: no record; the organisation's type and province make a Canadian supplier
- **invoice_card_json**: {"bill_to": {"legal_name": "St. John the Divine Anglican Church", "legal_name_is_published": true, "address": "PO BOX 236, Garibaldi Highlands, BC, V0N1T0", "address_is_the_invoice_address": false, "tax_number": "893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name)", "language": "en"}, "submit_to": {"email": "info@squamishanglicanchurch.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD 
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
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
- **contract_status**: inferred relationship (no record): low confidence; the buyer is an organisation in British Columbia (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); BC Hydro is the electricity utility for most of British Columbia (FortisBC and a few municipal utilities serve parts of the Okanagan and Kootenays); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 893030643RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (BC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: St. John the Divine Anglican Church — PO BOX 236, Garibaldi Highlands, BC, V0N1T0 — buyer tax no. 893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name) ⏎ SUBMIT TO: info@squamishanglicanchurch.ca (general mailbox, confirmed by the referee) | invoice portal: SAP Ariba ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: BC Hydro — 333 Dunsmuir St., Vancouver, B.C. V6B 5R3 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: PARISH OF ST JOHN (municipality / local government, BC) — inferred: no record; the organisation's type and province make a Canadian supplier
- **invoice_card_json**: {"bill_to": {"legal_name": "St. John the Divine Anglican Church", "legal_name_is_published": true, "address": "PO BOX 236, Garibaldi Highlands, BC, V0N1T0", "address_is_the_invoice_address": false, "tax_number": "893030643RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (squamishanglicanchurch.ca) + name)", "language": "en"}, "submit_to": {"email": "info@squamishanglicanchurch.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "SAP Ariba", "portal_kind": "actionable supplier / invoice portal named by the buyer", "mailing_address": "", "format": "", "system": "named on the buyer's page: SAP Ariba", "e_invoicing_peppol": "", "portal_is_invoice_channel": true, "portal_class": "e-invoicing portal"}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "GST 5% (BC)", "currency": "DERIVED: CAD 
- **invoice_readiness**: 6/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number; vendor legal name
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["info@squamishanglicanchurch.ca (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://www.squamishanglicanchurch.ca/", "quote: \"Location 1930 Diamond Road Squamish, BC View on Google Maps P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Contact Phone: 604-898-5100 Email : info@squamishanglica\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; no SPF record; mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-09139"], "buyer_facts": ["address and phone: the buyer's own site, https://www.squamishanglicanchurch.ca:443/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "invoice portal: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "phone / role e-mails / logo: the 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.squamishanglicanchurch.ca/ | 2026-11-08 | ok |  |  | SAP Ariba | 604-898-5100 | P.O. Box 236 Garibaldi Highlands, BC V0N1T0 |  |  |  |  |

## Buyer site facts (org_extras, squamishanglicanchurch.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: St. John the Divine Anglican Church
- **legal_name_url**: https://www.squamishanglicanchurch.ca:443/
- **legal_name_quote**: St. John the Divine Anglican Church | Anglican Church in Squamish, BC "> Search Donate Contact Toggle navigation Menu Home Rentals Abou
- **logo_url**: https://dq5pwpg1q8ru0.cloudfront.net/2021/11/10/12/39/22/6a9dd36a-a0a9-4ead-8899-1f6fdb7f8d74/St%20John%20the%20Divine%20Squamish%20(1).png
- **logo_basis**: logo image in the site header
- **domain**: squamishanglicanchurch.ca
- **key**: cra:893030643
- **name**: PARISH OF ST JOHN
- **website**: https://squamishanglicanchurch.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'e-transfers', 'url': 'https://www.squamishanglicanchurch.ca/pages/donate-to-st-john-the-divine-squamish', 'quote': 'urs, or mailed to PO Box 236, Garibaldi Highlands, BC, V0N 1T0. 3. St. John the Divine also accepts e-transfers. An INTERAC e-transfer allows you to send your contribution securely, without sharing any personal'}}
- **tel_links**: 1-604-898-5100

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "1930 Diamond Road , Squamish, BC , Canada", "address_country": "", "address_url": "https://www.squamishanglicanchurch.ca:443/contact", "address_method": "address-tag", "address_quote": "glicanchurch.ca Office Hours Wednesdays and Thursdays 9:00AM - 12:00PM Location 1930 Diamond Road Squamish, BC Canada P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Canada Sign up f", "phone": "604-898-5100", "phone_url": "https://www.squamishanglicanchurch.ca:443/contact", "emails": "info@squamishanglicanchurch.ca", "emails_url": "https://www.squamishanglicanchurch.ca:443/contact", "domain": "squamishanglicanchurch.ca", "key": "cra:893030643", "name": "PARISH OF ST JOHN", "website": "https://squamishanglicanchurch.ca/", "kind": "buyer", "date": "2026-11-03"}

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
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | PARISH OF ST JOHN |  |  |  |  |  |  |  |  |  |  |
| b | BC Hydro and Power Authority | Q795720 | official website on the organisation's domain (https://www.bchydro.com/) + name |  | B.C. Hydro | BC Hydro | state-owned enterprise | Crown corporation | Canada | 1961-01-01 | Vancouver |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:893030643",
 "ap_contact_team": {
  "emails": [
   "info@squamishanglicanchurch.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@squamishanglicanchurch.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://www.squamishanglicanchurch.ca/",
    "quote": "Location 1930 Diamond Road Squamish, BC View on Google Maps P.O. Box 236 Garibaldi Highlands, BC V0N1T0 Contact Phone: 604-898-5100 Email : info@squamishanglicanchurch.ca Office Hours Wednesdays and Thursdays 9:00AM - 12:00PM Menu Home Rentals About Give Rector's Reflection Calendar Events",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "PARISH OF ST JOHN",
    "task_id": "CL-CRA-09139"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.squamishanglicanchurch.ca (7 pages, robots.txt respected), no AI, no search engine"
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

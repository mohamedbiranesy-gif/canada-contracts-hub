# S5-35 — Municipality of Magnetawan ⇄ Baker Tilly SNT LLP

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 2 · AP grade B · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08) — 4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0
SUBMIT TO: treasurer@magnetawan.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Baker Tilly SNT LLP — 130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4 | GST/HST number not public
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/202
DESCRIPTION: Municipality of Magnetawan (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the
```

## Relationship
- **rank_group**: B3
- **data_quality_score**: 76
- **ship_ready**: yes (finance mailbox, not AP)
- **sensitivity_flag**: no
- **evidence_age_days**: 1
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Municipality of Magnetawan (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the last 12 months (dated record): Baker Tilly SNT LLP | awarded 2026-10-06 | published by: auditor of record (Ontario FIR 2025 Schedule 02) | record: https://efis.fma.csc.gov.on.ca/fir/wp-content/uploads/fir-files/reports-and-dashboards/by-year-and-municipality/2025//FI254944%20Magnetawan%20M.zip | vendor in Canada because: auditor of record (Ontario FIR 2025 Schedule 02)=Baker Tilly SNT LLP Unit A, 1850 Bond Street North Bay, ON P1B 4V6 | status rule: likely active (record dated in the last 12 months: auditor of record (Ontario FIR 2025 Schedule 02))
- **how_relationship_was_found**: same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own field
- **keys**: lead:03fbb65abd6dcab2
- **tier**: B
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: auditor of record (Ontario FIR 2025 Schedule 02); 0 in the contract dataset)

## Buyer
- **buyer**: Municipality of Magnetawan
- **buyer_website**: https://magnetawan.com/
- **buyer_address**: 4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0
- **buyer_phone**: 705-387-3947
- **buyer_contact_evidence_url**: https://magnetawan.com/government/staff-members
- **buyer_legal_name_as_published**: Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)
- **buyer_logo_url**: https://magnetawan.com/styles/default/images/logo.png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government (from the organisation's name / web domain)
- **buyer_sector**: government: municipal
- **buyer_municipal_tier**: Single Tier (Ontario MMAH list) (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://magnetawan.com/government/staff-members (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: treasurer@magnetawan.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://magnetawan.com/government/staff-members
- **email_evidence_quote**: Email Stephanie (treasurer@magnetawan.com)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: treasurer@magnetawan.com (finance/accounting dept or supplier-payment office) | researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08 | page: https://magnetawan.com/government/staff-members | quote: "Email Stephanie (treasurer@magnetawan.com)" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50024
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: no DMARC record
- **dmarc_record**: no DMARC record at _dmarc.magnetawan.com; confirmed by 8.8.8.8
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 ip4:209.91.139.195 include:spf.protection.outlook.com -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_as_published**: terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/2022-tenders-and-proposals/rfp-project-no.-2022-02-replacement-of-boat-ramp-town-of-magneta.pdf, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "payment_terms": "terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/2022-tenders-and-proposals/rfp-project-no.-2022-02-replacement-of-boat-ramp-town-of-magneta.pdf, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08) — 4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0 ⏎ SUBMIT TO: treasurer@magnetawan.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Baker Tilly SNT LLP — 130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/202 ⏎ DESCRIPTION: Municipality of Magnetawan (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the
- **invoice_card_json**: {"bill_to": {"legal_name": "Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)", "legal_name_is_published": true, "address": "4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@magnetawan.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/2022-tenders-and-proposals/rfp-project-no.-2022-02-replacement-of-boat-ramp-town-of-magneta.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)"
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Baker Tilly SNT LLP
- **vendor_address**: 130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4
- **vendor_country_basis**: auditor of record (Ontario FIR 2025 Schedule 02)=Baker Tilly SNT LLP Unit A, 1850 Bond Street North Bay, ON P1B 4V6
- **vendor_website**: https://www.bakertilly.ca/
- **vendor_emails**: info@bakertilly.ca
- **vendor_phone**: (902) 404-4000
- **vendor_contact_evidence_url**: https://www.bakertilly.ca/locations
- **vendor_logo_url**: https://www.bakertilly.ca/assets/images/logo.svg
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://www.bakertilly.ca/ (Baker Tilly Canada | Canadian audit, tax, and advisory solutions. Skip to main content this.$refs.searchInput.focus()) }, closeSearch() { this.searchVisible = f)
- **vendor_facts_provenance**: name and address: the record's vendor block (auditor of record (Ontario FIR 2025 Schedule 02)); phone / role e-mails / logo: the vendor's own site, https://www.bakertilly.ca/locations (tools/org_contacts.py, org_extras.py); website: https://www.bakertilly.ca/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: likely active (record dated in the last 12 months: auditor of record (Ontario FIR 2025 Schedule 02))
- **award_date**: 2026-10-06
- **contract_link**: https://efis.fma.csc.gov.on.ca/fir/wp-content/uploads/fir-files/reports-and-dashboards/by-year-and-municipality/2025//FI254944%20Magnetawan%20M.zip
- **source**: auditor of record (Ontario FIR 2025 Schedule 02)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: auditor of record (Ontario FIR 2025 Schedule 02); 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08) — 4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0 ⏎ SUBMIT TO: treasurer@magnetawan.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Baker Tilly SNT LLP — 130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4 | GST/HST number not public ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/202 ⏎ DESCRIPTION: Municipality of Magnetawan (organisation (type not stated in the record), jurisdiction not stated) — public contract / purchase award in the
- **invoice_card_json**: {"bill_to": {"legal_name": "Municipality of Magnetawan (provincial municipal directory: https://data.ontario.ca/dataset/62e83cbc-0731-4d66-abdc-2f2b31bcd76c/resource/6783a586-6b05-4a73-9663-e60a6963c91e/download/municipalities_-_en_2026-0526.csv, 2026-11-08)", "legal_name_is_published": true, "address": "4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "treasurer@magnetawan.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "terms of payment are net 30 (as printed on https://magnetawan.com/content/government/rfp-tenders/2022-tenders-and-proposals/rfp-project-no.-2022-02-replacement-of-boat-ramp-town-of-magneta.pdf, re-read 2026-11-08)", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.can", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)"
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); vendor GST/HST number; vendor legal name
- **ap_grade**: B
- **ap_score**: 67
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; payment terms published; currency known | missing: invoicing / AP mailbox; PO rule published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["treasurer@magnetawan.com (finance/accounting dept or supplier-payment office)", "researched by the ChatGPT/Codex agent (lane chatgpt) (page opened and quoted) on 2026-11-08", "page: https://magnetawan.com/government/staff-members", "quote: \"Email Stephanie (treasurer@magnetawan.com)\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: no DMARC record; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: chatgpt/chatgpt_buyer_ap_results_batch50.csv task CH-AP-50024"], "buyer_facts": ["address and phone: the buyer's own site, https://magnetawan.com/government/staff-members (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "payment terms: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (auditor of record (Ontario FIR 2025 Schedule 02))", "phone / role e-mails / logo: the vendor's own site, https://www.bakertilly.ca/locations (tools/org_contacts.py, org_extras.py)", "website: https://www.bakertilly.ca/"], "relationship": "same as above: a dated award record from the public source in `source`, vendor located in Canada per the source's own 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://magnetawan.com/government/staff-members | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, magnetawan.com)
- **status**: ok
- **pages**: 4
- **language**: en
- **logo_url**: https://magnetawan.com/styles/default/images/logo.png
- **logo_basis**: logo image in the site header
- **domain**: magnetawan.com
- **key**: lead:03fbb65abd6dcab2
- **name**: Municipality of Magnetawan
- **website**: https://magnetawan.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Certified Building Code Official
- **legal_name_stated_url**: https://magnetawan.com/government/staff-members
- **legal_name_stated_quote**: 3034 Email Scott Stephanie Lewin Treasurer/Tax Collector Extension 1003 Email Stephanie Tyler Irwin Certified Building Code Official (CBCO) Phone (705) 387-4029 Email Tyler --> Back to Top --> About Magnetawan The Municipality of Ma
- **mentions**: {'payment_method': {'text': 'Interactive Mapping Links Fire Rating Landfill and Recycling Looking for a safe, licens', 'url': 'https://magnetawan.com/', 'quote': 'tact --> Back to Top --> 2026 ANNUAL CHRISTMAS TREE LIGHTING Events Calendar Landfills Contact News Interactive Mapping Links Fire Rating Landfill and Recycling Looking for a safe, licensed STA? Latest News 2026 ANNUAL CHRISTMAS TREE LIGHTING View REMEMBRANCE'}}
- **tel_links**: 7053873947

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "4304 Hwy #520, P.O. Box 70 Magnetawan, Ontario , Canada, P0A 1P0", "address_country": "CA", "address_url": "https://magnetawan.com/government/staff-members", "address_method": "address-tag", "address_quote": "all! Contact Information 4304 Hwy #520, P.O. Box 70 Magnetawan Ontario , Canada P0A 1P0 info@magnetawan.com 705-387-3947 Quick Links Explore Government Residents Join", "phone": "705-387-3947", "phone_url": "https://magnetawan.com/government/staff-members", "emails": "info@magnetawan.com", "emails_url": "https://magnetawan.com/government/staff-members", "domain": "magnetawan.com", "key": "lead:03fbb65abd6dcab2", "name": "Municipality of Magnetawan", "website": "https://magnetawan.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, bakertilly.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.bakertilly.ca/assets/images/logo.svg
- **logo_basis**: logo image on the site
- **domain**: bakertilly.ca
- **key**: lead:7bc22d4cc3b6b17d
- **name**: Unlocking the highest value
- **website**: https://bakertilly.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: LocalBusiness
- **jsonld_name**: Baker Tilly Canada
- **jsonld_alternate_name**: BTI
- **jsonld_logo**: https://bti-global.transforms.svdcdn.com/production/network/canada/images/logos/Growth-symbol_Charcoal-RGB.jpg?w=600&h=600&q=82&fm=png&fit=max&dm=1727186527&s=a1012d09fd6f6cf603b582d82e80867b
- **jsonld_url**: https://www.bakertilly.ca
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebSite","author":{"@id":"https://www.bakertilly.ca#identity"},"copyrightHolder":{"@id":"https://www.bakertilly.ca#identity"},"copyrightYear":"2025","creator":{"@id":"#creator"},"dateCreated":"2025-01-30T08:26:44-05:00","dateModified":"2026-11-06T
- **jsonld_page**: https://www.bakertilly.ca/
- **mentions**: {'payment_method': {'text': 'interactions or transactions with Baker Tilly or otherwise receive the full benefit of', 'url': 'https://www.bakertilly.ca/privacy-policy', 'quote': 'and on reasonable notice to Baker Tilly, but you then may not be able to proceed with your intended interactions or transactions with Baker Tilly or otherwise receive the full benefit of Baker Tilly’s products and services. Please refer to section 7 of this Pr'}}
- **linkedin_url**: https://www.linkedin.com/company/baker-tilly-canada/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "130 Eileen Stubbs Ave, Suite 201, Dartmouth, NS, B3B 2C4", "address_country": "CA", "address_url": "https://www.bakertilly.ca/locations", "address_method": "pattern", "address_quote": "chewan Nationwide National office 130 Eileen Stubbs Ave Suite 201 Dartmouth, NS B3B 2C4 (902) 404-4000 info@bakertilly.ca Baker Tilly Canada Capital Corporation 900-40", "phone": "(902) 404-4000", "phone_url": "https://www.bakertilly.ca/locations", "emails": "info@bakertilly.ca", "emails_url": "https://www.bakertilly.ca/locations", "domain": "bakertilly.ca", "key": "lead:7bc22d4cc3b6b17d", "name": "Unlocking the highest value", "website": "https://bakertilly.ca/", "kind": "buyer", "date": "2026-11-04"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Municipality of Magnetawan |  |  |  |  |  |  |  |  |  |  |
| b | Unlocking the highest value |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:03fbb65abd6dcab2",
 "ap_contact_team": {
  "emails": [
   "treasurer@magnetawan.com",
   "info@magnetawan.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "treasurer@magnetawan.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://magnetawan.com/government/staff-members",
    "quote": "Email Stephanie (treasurer@magnetawan.com)",
    "retrieved_date": "2026-11-08",
    "found_by": "chatgpt",
    "verification": "verified",
    "source_file": "chatgpt_buyer_ap_results_batch50.csv",
    "org": "Municipality of Magnetawan",
    "task_id": "CH-AP-50024"
   },
   {
    "email": "treasurer@magnetawan.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://magnetawan.com/government/staff-members",
    "quote": "ie Lewin</h1> <div class=\"item t-html\"> <div class=\"data wysiwyg\"> <h4>Treasurer/Tax Collector </h4><p>Extension 1003</p><p><a href=\"mailto:treasurer@magnetawan.com\">Email Stephanie</a></p></div> </div> </article> <article class=\"t-html ext-html odd\" data-id=\"603\" data-category_id=\"41\"> <h",
    "retrieved_date": "2026-11-03",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Municipality of Magnetawan",
    "task_id": "CL-SM-00005"
   },
   {
    "email": "info@magnetawan.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://magnetawan.com/government/rfp-tenders",
    "quote": "mer, Spring and Fall and look forward to seeing you all! Contact Information 4304 Hwy #520, P.O. Box 70 Magnetawan Ontario , Canada P0A 1P0 info@magnetawan.com 705-387-3947 Quick Links Explore Government Residents Join Our Mailing List Privacy Policy",
    "retrieved_date": "2026-11-08",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Municipality of Magnetawan",
    "task_id": "CL-WS-00373"
   }
  ]
 },
 "research_status": {
  "found": 3
 },
 "queries_tried": [
  "site:magnetawan.com \"accounts payable\" invoice treasurer Magnetawan | site:magnetawan.com \"invoice\" \"payment\" purchase order by-law supplier Magnetawan",
  "site crawl of magnetawan.com (60 pages, robots.txt respected), no AI, no search engine",
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

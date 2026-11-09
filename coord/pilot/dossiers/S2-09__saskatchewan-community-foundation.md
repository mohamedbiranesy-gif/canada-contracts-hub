# S2-09 — Saskatchewan Community Foundation ⇄ Special Olympics Canada

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Saskatchewan Community Foundation — 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08) — buyer tax no. 890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
SUBMIT TO: finance@saskfoundation.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Special Olympics Canada — 21 St. Clair Avenue East, Suite 600, Toronto, ON M4T 1L9 | GST/HST 118836337 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2026-04-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: A force on the fie
```

## Relationship
- **rank_group**: D3
- **data_quality_score**: 63
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Saskatchewan Community Foundation (non-profit / association / cultural body, jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Special Olympics Canada | subject: A force on the field. A champion for inclusion. George Reed’s legacy lives on. | published by: the Canada-located vendor's own website | record: https://www.specialolympics.ca/saskatchewan/what-we-do/stories/george-reed-s-legacy-lives-on/ | vendor in Canada because: vendor located in Canada (stories; Wikidata country + address on its site)=21 St Clair Avenue East Toronto, ON M4T 1L9 | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:b22b496ad08ed7a9
- **tier**: D
- **grade**: 3
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Saskatchewan Community Foundation
- **buyer_website**: https://saskfoundation.ca/
- **buyer_address**: 1911 Broad St. (Path Cowork – Basecamp) , Regina, SK, S4P 1Y1
- **buyer_phone**: +1 (306) 751-4756
- **buyer_contact_evidence_url**: https://saskfoundation.ca/contact/
- **buyer_legal_name_as_published**: Saskatchewan Community Foundation
- **buyer_bn_as_published**: 890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 890271448RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://saskfoundation.ca/wp-content/uploads/2024/09/Header-White-Horizontal-Logos-Saskatchewan-Community-Foundation-1.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/saskatchewan-community-foundation
- **buyer_type**: non-profit / association / cultural body
- **buyer_sector**: non-profit
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)
- **buyer_charity_designation**: A; 0210
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://saskfoundation.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell); invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: finance@saskfoundation.ca
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://saskfoundation.ca/contact/
- **email_evidence_quote**: kfoundation.ca Finance Inquiries: finance@saskfoundation.ca Donor Portal Support: techsupport@sa
- **email_evidence_context**: k – Basecamp) Regina, SK, S4P 1Y1 Call Us or Email Us General Inquiries: info@saskfoundation.ca Donors and Funds: legacy@saskfoundation.ca Professional Advisors: advisors@saskfoundation.ca Grant Inquiries: grants@saskfoundation.ca Finance Inquiries: finance@saskfoundation.ca Donor Portal Support: techsupport@saskfoundation.ca Job Opportunities and Applications: careers@saskfoundation.ca Phone: +1 (306) 751-4756 Toll Free: +1 (877) 751-4756 The information on this page was last updated: February 20, 2026 Facebook-f Insta (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: finance@saskfoundation.ca (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://saskfoundation.ca/contact/ | quote: "kfoundation.ca Finance Inquiries: finance@saskfoundation.ca Donor Portal Support: techsupport@sa" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-26930
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;sp=none;pct=100;rua=mailto:6651c62aaa@rua.ca.easydmarc.com;ruf=mailto:6651c62aaa@ruf.ca.easydmarc.com;ri=86400;fo=1;
- **dmarc_record_domain**: saskfoundation.ca
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 include:_spf.saskfoundation_ca._d.easydmarc.pro -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: +1 (306) 751-4756 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)
- **invoice_mailing_address**: 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "+1 (306) 751-4756 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)", "mailing_address": "1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Saskatchewan Community Foundation — 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08) — buyer tax no. 890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: finance@saskfoundation.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Special Olympics Canada — 21 St. Clair Avenue East, Suite 600, Toronto, ON M4T 1L9 | GST/HST 118836337 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2026-04-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: A forc
- **invoice_card_json**: {"bill_to": {"legal_name": "Saskatchewan Community Foundation", "legal_name_is_published": true, "address": "1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "finance@saskfoundation.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buy
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Special Olympics Canada
- **vendor_address**: 21 St. Clair Avenue East, Suite 600, Toronto, ON M4T 1L9
- **vendor_country_basis**: vendor located in Canada (stories; Wikidata country + address on its site)=21 St Clair Avenue East Toronto, ON M4T 1L9
- **vendor_bn9**: 118836337 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2026-04-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)
- **vendor_gst_hst_derived**: 118836337RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.specialolympics.ca
- **vendor_emails**: communications@specialolympics.ca; info@specialolympics.ca
- **vendor_phone**: 416.927.9050
- **vendor_contact_evidence_url**: https://www.specialolympics.ca/contact-us/
- **vendor_logo_url**: https://www.specialolympics.ca/media/dd0ddxu0/logo.svg?width=100&height=20&v=1db4b6de8ee9570
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); BN9: federal grants & contributions disclosure (recipient_business_number); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.specialolympics.ca/contact-us/ (tools/org_contacts.py, org_extras.py); website: https://www.specialolympics.ca
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_wikidata**: https://www.wikidata.org/wiki/Q7574635; nonprofit organization
- **vendor_employees**: 14; 17; 13; 11; 10; 12; 18; 19; 21; 22; 20; 24; 29; 28; 30; 37; 36 (Wikidata Q7574635, exact name match + country + organisation claims; 2026-11-08)
- **vendor_bn_source**: federal grants & contributions disclosure (recipient_business_number)

## Contract
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: A force on the field. A champion for inclusion. George Reed’s legacy lives on.
- **contract_description**: A force on the field. A champion for inclusion. George Reed’s legacy lives on. (the record's title; the source publishes no separate description)
- **contract_link**: https://www.specialolympics.ca/saskatchewan/what-we-do/stories/george-reed-s-legacy-lives-on/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 1 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 890271448RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (SK) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 118836337RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Saskatchewan Community Foundation — 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08) — buyer tax no. 890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name) ⏎ SUBMIT TO: finance@saskfoundation.ca (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Special Olympics Canada — 21 St. Clair Avenue East, Suite 600, Toronto, ON M4T 1L9 | GST/HST 118836337 (recipient_business_number in the federal grants & contributions disclosure, last agreement 2026-04-20; https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: A forc
- **invoice_card_json**: {"bill_to": {"legal_name": "Saskatchewan Community Foundation", "legal_name_is_published": true, "address": "1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)", "address_is_the_invoice_address": true, "tax_number": "890271448RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by exact name)", "language": "en"}, "submit_to": {"email": "finance@saskfoundation.ca", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 (as printed on https://saskfoundation.ca/contact/, re-read 2026-11-08)", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of SK on the invoice; public service bodies claim their", "buy
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["finance@saskfoundation.ca (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://saskfoundation.ca/contact/", "quote: \"kfoundation.ca Finance Inquiries: finance@saskfoundation.ca Donor Portal Support: techsupport@sa\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-26930"], "buyer_facts": ["address and phone: the buyer's own site, https://saskfoundation.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)", "invoice mailing address: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "BN9: federal 

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://saskfoundation.ca/contact/ | 2026-11-08 | ok |  |  |  | +1 (306) 751-4756 | 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 |  |  |  |  |

## Buyer site facts (org_extras, saskfoundation.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: Saskatchewan Community Foundation
- **legal_name_url**: https://saskfoundation.ca/
- **legal_name_quote**: Saskatchewan Community Foundation – Your legacy, forever. Skip to content Our website will be undergoing planned maintenance on Frida
- **logo_url**: https://saskfoundation.ca/wp-content/uploads/2024/09/Header-White-Horizontal-Logos-Saskatchewan-Community-Foundation-1.svg
- **logo_basis**: logo image on the site
- **domain**: saskfoundation.ca
- **key**: lead:b22b496ad08ed7a9
- **name**: Saskatchewan Community Foundation
- **website**: https://saskfoundation.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Vital Signs Community Network
- **legal_name_stated_url**: https://saskfoundation.ca/
- **legal_name_stated_quote**: anned Giving Donor Portal Login Professional Advisors For Charities & Grantees Grants Create a Fund Vital Signs Community Network Recognition Logos Charity Resource Hub Charity Portal Login Community Impact & News Impact Stories
- **mentions**: {'payment_method': {'text': 'e-transfer, or even credit card', 'url': 'https://saskfoundation.ca/donors/ways-to-give/', 'quote': 'odities and personal belongings, including: Monetary Donations We accept donations by cash, cheque, e-transfer, or even credit card. While these options are convenient, typically these gifts are the least tax efficient way of donat'}}
- **linkedin_url**: https://www.linkedin.com/company/saskatchewan-community-foundation
- **tel_links**: +1 306-751-4756; +1 (306) 751-4756; +1-877-751-4756

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "1911 Broad St. (Path Cowork – Basecamp) , Regina, SK, S4P 1Y1", "address_country": "CA", "address_url": "https://saskfoundation.ca/contact/", "address_method": "pattern", "address_quote": "chewan Community Foundation 1911 Broad St. (Path Cowork – Basecamp) Regina, SK, S4P 1Y1 Call Us or Email Us General Inquiries: info@saskfoundation.ca Donors and Funds:", "phone": "+1 (306) 751-4756", "phone_url": "https://saskfoundation.ca/contact/", "emails": "info@saskfoundation.ca", "emails_url": "https://saskfoundation.ca/contact/", "domain": "saskfoundation.ca", "key": "lead:b22b496ad08ed7a9", "name": "saskfoundation.ca", "website": "https://saskfoundation.ca/", "kind": "buyer", "date": "2026-11-04"}

## Vendor site facts (org_extras, specialolympics.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **logo_url**: https://www.specialolympics.ca/media/dd0ddxu0/logo.svg?width=100&height=20&v=1db4b6de8ee9570
- **logo_basis**: logo image in the site header
- **domain**: specialolympics.ca
- **key**: lead:09e34047afe5edd3
- **name**: specialolympics.ca
- **website**: https://specialolympics.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **linkedin_url**: https://www.linkedin.com/company/specialolcanada/

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "21 St. Clair Avenue East, Suite 600, Toronto, ON M4T 1L9", "address_country": "CA", "address_url": "https://www.specialolympics.ca/contact-us/", "address_method": "pattern", "address_quote": "ograms. Special Olympics Canada 21 St. Clair Avenue East, Suite 600 Toronto, ON M4T 1L9 Phone: 416.927.9050 Toll free: 1.888.888.0608 General Requests : info@specialol", "phone": "416.927.9050", "phone_url": "https://www.specialolympics.ca/contact-us/", "emails": "communications@specialolympics.ca; info@specialolympics.ca", "emails_url": "https://www.specialolympics.ca/contact-us/", "domain": "specialolympics.ca", "key": "lead:09e34047afe5edd3", "name": "specialolympics.ca", "website": "https://specialolympics.ca/", "kind": "buyer", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Saskatchewan Community Foundation | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Saskatchewan%20Community%20Foundation | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Saskatchewan Community Foundation |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:b22b496ad08ed7a9",
 "ap_contact_team": {
  "emails": [
   "finance@saskfoundation.ca",
   "info@saskfoundation.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "finance@saskfoundation.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://saskfoundation.ca/contact/",
    "quote": "kfoundation.ca Finance Inquiries: finance@saskfoundation.ca Donor Portal Support: techsupport@sa",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "saskfoundation.ca",
    "task_id": "CL-LD-26930"
   },
   {
    "email": "info@saskfoundation.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://saskfoundation.ca/",
    "quote": "for our Newsletter Facebook-f Instagram Linkedin Youtube Spotify 1911 Broad St. (PATH Cowork — Basecamp) Regina, SK, S4P1Y1 (306) 751-4756 info@saskfoundation.ca Saskatchewan Community Foundation acknowledges our presence on lands covered by Treaty 2, 4, 5, 6, 8 and 10 territories: the tr",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "saskfoundation.ca",
    "task_id": "CL-LD-26930"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of saskfoundation.ca (10 pages, robots.txt respected), no AI, no search engine",
  "site crawl of saskfoundation.ca (10 pages, robots.txt respected), no AI, no search engine"
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

- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

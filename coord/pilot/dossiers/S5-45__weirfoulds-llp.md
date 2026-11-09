# S5-45 — WeirFoulds LLP ⇄ Association of Registered Graphic Designers of Ontario

Stratum: **S5_vendor_supplies_own_GST** · pay on sight: no · channel tier 1 · AP grade C · missing: the vendor's GST/HST number (BN9); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: WeirFoulds LLP — 4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7
SUBMIT TO: payments@weirfoulds.com (invoicing/AP mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: About the Association (stated on the vendor's legal page: https://rgd.ca/about) — PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7 | GST/HST number not public
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: RGD | RGD Project-Based Mentorship open for applications for Fall 2026
```

## Relationship
- **rank_group**: E4
- **data_quality_score**: 66
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 12
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: WeirFoulds LLP (company (private sector), jurisdiction not stated) — linked from the Canada-located vendor's site (weakest listed relationship): Association of Registered Graphic Designers of Ontario | subject: RGD | RGD Project-Based Mentorship open for applications for Fall 2026 | published by: the Canada-located vendor's own website | record: https://rgd.ca/articles/the-rgd-project-based-mentorship-program-is-open-for-applications-2026-2027 | vendor in Canada because: vendor located in Canada (wd)=rgd.ca | status rule: linked from a page of the Canada-located vendor's site (not a client page)
- **how_relationship_was_found**: tools/provider_mentions.py / news_match.py found the buyer linked from the vendor's own site or release
- **keys**: lead:66cbecd144e26c2b
- **tier**: E
- **grade**: 4
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: WeirFoulds LLP
- **buyer_website**: https://weirfoulds.com/
- **buyer_address**: 4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7
- **buyer_phone**: 416-365-1110
- **buyer_contact_evidence_url**: https://www.weirfoulds.com/contact
- **buyer_legal_name_as_published**: WeirFoulds LLP
- **buyer_logo_url**: https://www.weirfoulds.com/assets/uploads/weirfoulds-llp-logo.svg
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/weirfoulds-llp
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_wikidata**: https://www.wikidata.org/wiki/Q7980284; law firm
- **buyer_founded**: 1860-00-00 (Wikidata Q7980284, official website on the organisation's domain (http://www.weirfoulds.com) + name; 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://www.weirfoulds.com/contact (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: payments@weirfoulds.com
- **email_type**: invoicing/AP
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); invoicing / AP mailbox
- **email_evidence_url**: https://www.weirfoulds.com/pay
- **email_evidence_quote**: and will be credited to your WeirFoulds LLP account once received. For any inquiries about your invoice, please contact WeirFoulds LLP at: payments@weirfoulds.com . Stripe does not have information regarding the details of your invoice. Thank you. Continue Toronto Office 4100 – 66 Welling
- **email_evidence_context**: and other payment details as prompted in the portal. Payments are normally processed within two business days and will be credited to your WeirFoulds LLP account once received. For any inquiries about your invoice, please contact WeirFoulds LLP at: payments@weirfoulds.com . Stripe does not have information regarding the details of your invoice. Thank you. Continue Toronto Office 4100 – 66 Wellington St. W. PO Box 35, TD Bank Tower Toronto, ON Canada M5K 1B7 TEL: 416-365-1110 FAX: 416-365-1876 Oakville Office 1320 Cor (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: payments@weirfoulds.com (invoicing/AP) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28 | page: https://www.weirfoulds.com/pay | quote: "and will be credited to your WeirFoulds LLP account once received. For any inquiries about your invoice, please contact WeirFoulds LLP at: payments@weirfoulds.c" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-002412
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; fo=1; pct=100; rua=mailto:dmarc@weirfoulds.com,mailto:dmarc_agg@vali.email; ruf=mailto:dmarc@weirfoulds.com,mailto:dmarc_agg@vali.email; sp=quarantine;
- **dmarc_record_domain**: weirfoulds.com
- **spf_policy**: DNS lookup failed
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 416-365-1110 (as printed on https://www.weirfoulds.com/pay, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "416-365-1110 (as printed on https://www.weirfoulds.com/pay, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 1
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: WeirFoulds LLP — 4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7 ⏎ SUBMIT TO: payments@weirfoulds.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: About the Association (stated on the vendor's legal page: https://rgd.ca/about) — PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: RGD | RGD Project-Based Mentorship open for applications for Fall 2026
- **invoice_card_json**: {"bill_to": {"legal_name": "WeirFoulds LLP", "legal_name_is_published": true, "address": "4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "payments@weirfoulds.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "About the Association (stated on the vendor's legal page: https://rgd.ca/about)", "bn9": "", "neq": "", "remit_address": "PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7"}, "follow_up": {"ap_phone": "416-365-1110 (as printed on https://www.weirfoulds.com/pay, re-read
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: Association of Registered Graphic Designers of Ontario
- **vendor_legal_name**: About the Association (stated on the vendor's legal page: https://rgd.ca/about)
- **vendor_trading_name**: Association of Registered Graphic Designers of Ontario
- **vendor_address**: PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7
- **vendor_country_basis**: vendor located in Canada (wd)=rgd.ca
- **vendor_website**: https://rgd.ca
- **vendor_emails**: info@rgd.ca
- **vendor_contact_evidence_url**: https://rgd.ca/about/contact-us
- **vendor_logo_url**: https://rgd.ca/assets/images/utility/rgd-logo-red.svg
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/rgdcanada
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); phone / role e-mails / logo: the vendor's own site, https://rgd.ca/about/contact-us (tools/org_contacts.py, org_extras.py); website: https://rgd.ca (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer

## Contract
- **contract_status**: linked from a page of the Canada-located vendor's site (not a client page)
- **contract_title**: RGD | RGD Project-Based Mentorship open for applications for Fall 2026
- **contract_description**: RGD | RGD Project-Based Mentorship open for applications for Fall 2026 (the record's title; the source publishes no separate description)
- **contract_link**: https://rgd.ca/articles/the-rgd-project-based-mentorship-program-is-open-for-applications-2026-2027
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)

## Pay on sight / grades
- **pay_on_sight**: no
- **pay_on_sight_missing**: the vendor's GST/HST number (BN9); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: WeirFoulds LLP — 4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7 ⏎ SUBMIT TO: payments@weirfoulds.com (invoicing/AP mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: About the Association (stated on the vendor's legal page: https://rgd.ca/about) — PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7 | GST/HST number not public ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: RGD | RGD Project-Based Mentorship open for applications for Fall 2026
- **invoice_card_json**: {"bill_to": {"legal_name": "WeirFoulds LLP", "legal_name_is_published": true, "address": "4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "payments@weirfoulds.com", "email_type": "invoicing/AP", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "", "vendor_qst": ""}, "vendor_identity": {"legal_name": "About the Association (stated on the vendor's legal page: https://rgd.ca/about)", "bn9": "", "neq": "", "remit_address": "PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7"}, "follow_up": {"ap_phone": "416-365-1110 (as printed on https://www.weirfoulds.com/pay, re-read
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor GST/HST number
- **ap_grade**: C
- **ap_score**: 73
- **ap_grade_basis**: met: invoicing / AP mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: finance mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility)
- **ap_gap_to_A**: published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["payments@weirfoulds.com (invoicing/AP)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-10-28", "page: https://www.weirfoulds.com/pay", "quote: \"and will be credited to your WeirFoulds LLP account once received. For any inquiries about your invoice, please contact WeirFoulds LLP at: payments@weirfoulds.c\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; DNS lookup failed; mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-VD-002412"], "buyer_facts": ["address and phone: the buyer's own site, https://www.weirfoulds.com/contact (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "phone / role e-mails / logo: the vendor's own site, https://rgd.ca/about/contact-us (tools/org_contacts.py, org_extras.py)", "website: https://rgd.ca (site answers)"], "relationship": "tools/provider_mentions.py / news_match.py found the buyer linked fr

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.weirfoulds.com/pay | 2026-11-08 | ok |  |  |  | 416-365-1110 |  |  |  |  |  |

## Buyer site facts (org_extras, weirfoulds.com)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: WeirFoulds LLP
- **legal_name_url**: https://www.weirfoulds.com/
- **legal_name_quote**: WeirFoulds LLP - WeirFoulds LLP Skip to content People Search Search by Name Practice Area Practice Area All Pract
- **logo_url**: https://www.weirfoulds.com/assets/uploads/weirfoulds-llp-logo.svg
- **logo_basis**: logo image in the site header
- **domain**: weirfoulds.com
- **key**: lead:66cbecd144e26c2b
- **name**: WeirFoulds LLP
- **website**: https://weirfoulds.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: WeirFoulds LLP
- **jsonld_legal_name**: WeirFoulds LLP
- **jsonld_phone**: 416-365-1110
- **jsonld_logo**: https://www.weirfoulds.com/assets/uploads/wf-favicon.webp
- **jsonld_url**: https://www.weirfoulds.com/
- **jsonld_founding_date**: 1860-01-01
- **jsonld_same_as**: https://www.linkedin.com/company/weirfoulds-llp
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/www.weirfoulds.com\/","url":"https:\/\/www.weirfoulds.com\/","name":"WeirFoulds LLP - WeirFoulds LLP","isPartOf":{"@id":"https:\/\/www.weirfoulds.com\/#website"},"about":{"@id":"https:\/\/www.weirfoulds.com\/#organizati
- **jsonld_page**: https://www.weirfoulds.com/
- **legal_name_stated**: American Institute
- **legal_name_stated_url**: https://www.weirfoulds.com/about-us
- **legal_name_stated_quote**: e firm achieving the Trust Services Criteria in security and data confidentiality. Developed by the American Institute of CPAs (AICPA), SOC 2 is recognized as the highest possible data security compliance standard for
- **linkedin_url**: https://www.linkedin.com/company/weirfoulds-llp
- **tel_links**: 4163651110; 4163651876; 9058292035; +14169475043; +14169475066; +14169475049; +14169475027; +14169475007; +14169475041; 

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "4100 – 66 Wellington Street West, PO Box 35, TD Bank Tower, Toronto, Ontario M5K 1B7", "address_country": "CA", "address_url": "https://www.weirfoulds.com/contact", "address_method": "pattern", "address_quote": "fice 4100 – 66 Wellington Street West PO Box 35, TD Bank Tower Toronto, Ontario M5K 1B7 Canada VIEW MAP Tel: 416.365.1110 Fax: 416.365.1876 Oakville Office 1320 Cornwa", "phone": "416-365-1110", "phone_url": "https://www.weirfoulds.com/contact", "domain": "weirfoulds.com", "key": "lead:66cbecd144e26c2b", "name": "weirfoulds.com", "website": "https://weirfoulds.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, rgd.ca)
- **status**: ok
- **pages**: 6
- **language**: en
- **legal_name**: the Association of Registered Graphic
- **legal_name_url**: https://rgd.ca/
- **legal_name_quote**: ngram Context Creative is proud to be a design sponsor and collaborator for the RGD website. © 2026 the Association of Registered Graphic Designers.
- **logo_url**: https://rgd.ca/assets/images/utility/rgd-logo-red.svg
- **logo_basis**: logo image in the site header
- **domain**: rgd.ca
- **key**: vendor:Association of Registered Graphic Designers of Ontario
- **name**: Association of Registered Graphic Designers of Ontario
- **website**: https://rgd.ca/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Association of Registered Graphic Designers
- **jsonld_alternate_name**: RGD
- **jsonld_logo**: https://rgd.ca/assets/images/users/_600x60_fit_center-center_82_none/110766/rgd-logo-red.jpg?mtime=1706710682
- **jsonld_quote**: {"@context":"https://schema.org","@graph":[{"@type":"WebPage","author":{"@id":"#identity"},"copyrightHolder":{"@id":"#identity"},"copyrightYear":"2023","creator":{"@id":"#creator"},"dateCreated":"2023-01-19T16:45:53-05:00","dateModified":"2026-11-03T16:07:00-05:00","datePublished":"2023-01-19T16:46:
- **jsonld_page**: https://rgd.ca/
- **legal_name_stated**: About the Association
- **legal_name_stated_url**: https://rgd.ca/about
- **legal_name_stated_quote**: RGD | About the Association of Registered Graphic Designers (RGD) About the Association of Registered Graphic Designers (RGD) S
- **linkedin_url**: https://www.linkedin.com/company/rgdcanada

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "PO Box 70604, Junction Gardens PO, Toronto ON M6P 4E7", "address_country": "CA", "address_url": "https://rgd.ca/about/contact-us", "address_method": "pattern", "address_quote": "on of Registered Graphic Designers PO Box 70604, Junction Gardens PO Toronto ON M6P 4E7 Sponsored Sponsor Just released: Slanted Magazine #48—Seoul Sponsor WeirFoulds", "emails": "info@rgd.ca", "emails_url": "https://rgd.ca/about/contact-us", "domain": "rgd.ca", "key": "vd:rgd.ca", "name": "Association of Registered Graphic Designers of Ontario", "website": "https://rgd.ca/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | WeirFoulds LLP | Q7980284 | official website on the organisation's domain (http://www.weirfoulds.com) + name |  | WeirFoulds LLP | WeirFoulds LLP | law firm |  | Canada | 1860-00-00 | Toronto |
| b | Association of Registered Graphic Designers of Ontario | Q7714734 | official website on the organisation's domain (https://rgd.ca/) + name |  | Association of Registered Graphic Designers of Ontario | Association agrée des graphistes de l'Ontario | organization |  | Canada | 1996-00-00 | Toronto |

## Lanes' verified findings for this buyer (team_buyers)
```
none
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

# S3-18 — Abcott Construction Ltd ⇄ Abcott Construction Ltd.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Abcott Construction Ltd — 124 Garden Avenue, Brantford, ON N3S 7W4 — buyer tax no. 100010883 (Canada's Business Registries, ON 287520, 2026-11-08)
SUBMIT TO: info@abcott.ca (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall)
FROM / REMIT TO: ABCOTT CONSTRUCTION LTD. (as registered: Canada's Business Registries, ON 1872487, 2026-11-08) — 124 Garden Avenue, Brantford, ON, N3S 7W4, Canada | GST/HST 100010883 (Canada's Business Registries, ON 1872487, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work
DESCRIPTION: Our Projects | Abcott Construction
```

## Relationship
- **rank_group**: D1
- **data_quality_score**: 46
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Abcott Construction Ltd (company (private sector), jurisdiction not stated) — named as a client by the Canada-located vendor (client list / customer story), dated: Abcott Construction Ltd. | subject: Our Projects | Abcott Construction | published by: the Canada-located vendor's own website | record: https://www.abcottconstruction.com/ | vendor in Canada because: vendor located in Canada (wall)=abcottconstruction.com | status rule: client listing on the vendor's own site (undated)
- **how_relationship_was_found**: tools/client_lists.py / dated_stories.py read the vendor's dated customer story / case study naming the buyer
- **keys**: lead:84dcd1f61af2051e
- **tier**: D
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)

## Buyer
- **buyer**: Abcott Construction Ltd
- **buyer_website**: https://abcott.ca/
- **buyer_address**: 124 Garden Avenue, Brantford, ON N3S 7W4
- **buyer_phone**: Call: 519-756-4350
- **buyer_contact_evidence_url**: https://abcott.ca/contact/
- **buyer_legal_name_as_published**: Abcott Construction Ltd
- **buyer_bn_as_published**: 100010883 (Canada's Business Registries, ON 287520, 2026-11-08)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 100010883RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **buyer_logo_url**: https://abcott.ca/img/Home/Logos/Abcott_LogoFinal.png
- **buyer_website_status**: site answers
- **buyer_linkedin_url**: https://www.linkedin.com/company/abcott-construction-ltd/
- **buyer_registry_id**: 287520 (ON; https://ised-isde.canada.ca/cbr-rec/en/search?q=Abcott%20Construction%20Ltd)
- **buyer_type**: company (private sector)
- **buyer_sector**: private sector
- **buyer_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 287520, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://abcott.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: info@abcott.ca
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://abcott.ca/terms-and-conditions/
- **email_evidence_quote**: y other rights Abcott may have under contract or otherwise at law. Updated: January 2021 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE QUOTE REQU
- **email_evidence_context**: esponsible for all penalties, costs, damages or losses suffered or incurred by Abcott, without prejudice to any other rights Abcott may have under contract or otherwise at law. Updated: January 2021 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE QUOTE REQUEST × I am a(n) * Customer Existing Customer New Customer Company Name Phone Email Budget I am interested in: * In (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: info@abcott.ca (general) | page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01 | page: https://abcott.ca/terms-and-conditions/ | quote: "y other rights Abcott may have under contract or otherwise at law. Updated: January 2021 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abco" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mail.abcott.ca) | lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00098
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mail.abcott.ca)
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1;p=quarantine;sp=quarantine;adkim=r;aspf=r;pct=100;fo=1;rf=afrf;ri=3600;rua=mailto:abcottca@rua.agari.com,mailto:donna@abcott.ca;ruf=mailto:abcottca@ruf.agari.com,mailto:donna@abcott.ca
- **dmarc_record_domain**: abcott.ca
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 ip4:51.79.18.35 +mx +a +ip4:68.71.44.194 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **po_required_as_published**: purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "po_required": "purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Abcott Construction Ltd — 124 Garden Avenue, Brantford, ON N3S 7W4 — buyer tax no. 100010883 (Canada's Business Registries, ON 287520, 2026-11-08) ⏎ SUBMIT TO: info@abcott.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) ⏎ FROM / REMIT TO: ABCOTT CONSTRUCTION LTD. (as registered: Canada's Business Registries, ON 1872487, 2026-11-08) — 124 Garden Avenue, Brantford, ON, N3S 7W4, Canada | GST/HST 100010883 (Canada's Business Registries, ON 1872487, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Our Projects | Abcott Construction
- **invoice_card_json**: {"bill_to": {"legal_name": "Abcott Construction Ltd", "legal_name_is_published": true, "address": "124 Garden Avenue, Brantford, ON N3S 7W4", "address_is_the_invoice_address": false, "tax_number": "100010883 (Canada's Business Registries, ON 287520, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@abcott.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08))"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **language_hint**: en
- **template_language**: en
- **invoice_reference_hint**: the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08))

## Vendor
- **vendor**: Abcott Construction Ltd.
- **vendor_legal_name**: ABCOTT CONSTRUCTION LTD. (as registered: Canada's Business Registries, ON 1872487, 2026-11-08)
- **vendor_registry_id**: 1872487 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=Abcott%20Construction%20Ltd.
- **vendor_registered_address**: BRANTFORD, Ontario (registered office city / province; Canada's Business Registries, ON 1872487, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 1872487, 2026-11-08)
- **vendor_address**: 124 Garden Avenue, Brantford, ON, N3S 7W4, Canada
- **vendor_country_basis**: vendor located in Canada (wall)=abcottconstruction.com
- **vendor_bn9**: 100010883 (Canada's Business Registries, ON 1872487, 2026-11-08)
- **vendor_gst_hst_derived**: 100010883RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://www.abcottconstruction.com/
- **vendor_emails**: info@abcott.ca
- **vendor_phone**: Call: 519-756-4350
- **vendor_contact_evidence_url**: https://abcott.ca/contact/
- **vendor_logo_url**: https://abcott.ca/img/Home/Logos/Abcott_LogoFinal.png
- **vendor_website_status**: site answers
- **vendor_linkedin_url**: https://www.linkedin.com/company/abcott-construction-ltd/
- **vendor_facts_provenance**: name and address: the record's vendor block (the Canada-located vendor's own website); registry identity: 1872487 (ON) status Active — incorporated (Canada's Business Registries, ON 1872487, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 1872487, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2012-05-01; phone / role e-mails / logo: the vendor's own site, https://abcott.ca/contact/ (tools/org_contacts.py, org_extras.py); website: https://www.abcottconstruction.com/ (site answers)
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 1872487, 2026-11-08)
- **vendor_incorporation_date**: 2012-05-01
- **vendor_years_in_business**: 14.5 (since 2012-05-01, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 1872487, 2026-11-08

## Contract
- **po_required_as_published**: purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08)
- **contract_status**: client listing on the vendor's own site (undated)
- **contract_title**: Our Projects | Abcott Construction
- **contract_description**: Our Projects | Abcott Construction (the record's title; the source publishes no separate description)
- **contract_link**: https://www.abcottconstruction.com/
- **source**: the Canada-located vendor's own website
- **contracts_with_canadian_suppliers**: 2
- **records_with_this_vendor**: 1 (relationship record: the Canada-located vendor's own website; 0 in the contract dataset)
- **records_in_contract_dataset**: 2 records with Canada-located vendors (this row's organisation)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 100010883RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **payment_terms_default_policy**: statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c30, read 2026-11-08: "an owner shall pay the amount payable under a proper invoice no later than 28 days after receiving the proper invoice from the contractor"); applies only if this contract is an improvement under the Act
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 100010883RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Abcott Construction Ltd — 124 Garden Avenue, Brantford, ON N3S 7W4 — buyer tax no. 100010883 (Canada's Business Registries, ON 287520, 2026-11-08) ⏎ SUBMIT TO: info@abcott.ca (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) ⏎ FROM / REMIT TO: ABCOTT CONSTRUCTION LTD. (as registered: Canada's Business Registries, ON 1872487, 2026-11-08) — 124 Garden Avenue, Brantford, ON, N3S 7W4, Canada | GST/HST 100010883 (Canada's Business Registries, ON 1872487, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: statutory default for construction work ⏎ DESCRIPTION: Our Projects | Abcott Construction
- **invoice_card_json**: {"bill_to": {"legal_name": "Abcott Construction Ltd", "legal_name_is_published": true, "address": "124 Garden Avenue, Brantford, ON N3S 7W4", "address_is_the_invoice_address": false, "tax_number": "100010883 (Canada's Business Registries, ON 287520, 2026-11-08)", "language": "en"}, "submit_to": {"email": "info@abcott.ca", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08)", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": "the buyer's purchase-order number: the buyer publishes purchase-order terms, so the PO number is the reference to quote (purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) (as printed on https://abcott.ca/terms-and-conditions/, re-read 2026-11-08))"}, "terms": {"payment_terms": "statutory default for construction work (buyer published no terms): the owner must pay a proper invoice no later than 28 days after receiving it — Construction Act, R.S.O. 1990, c. C.30, s. 6.4(1), in force 2019-10-01; s. 3(1) binds the Crown (https://www.ontario.ca/laws/statute/90c
- **invoice_readiness**: 10/11 invoice elements present
- **invoice_missing**: reference to quote (PO / contract / vendor id)
- **ap_grade**: C
- **ap_score**: 57
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; PO rule published; currency known | missing: invoicing / AP mailbox; finance mailbox; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel
- **facts_provenance_json**: {"mailbox": ["info@abcott.ca (general)", "page located by a web search (AI agent located the URL only), then read by tools/deep_pages.py without AI on 2026-11-01", "page: https://abcott.ca/terms-and-conditions/", "quote: \"y other rights Abcott may have under contract or otherwise at law. Updated: January 2021 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abco\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by self-hosted or other (mail.abcott.ca)", "lane file: claude/claude_buyer_ap_results_search01.csv task CL-WS-00098"], "buyer_facts": ["address and phone: the buyer's own site, https://abcott.ca/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "PO requirement: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (the Canada-located vendor's own website)", "registry identity: 1872487 (ON) status Active — incorporated (Canada's Business Registries, ON 1872487, 2026-11

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://abcott.ca/terms-and-conditions/ | 2026-11-08 | ok |  | purchase-order terms published (as published: purchase order issued by Abcott and accepted by the Vendor shall) |  | 1 519-756-4350 | 124 Garden Ave. Brantford, ON N3S 7W4 |  |  |  | at Abcott’s office, and all as per governing jurisdictional authorities’ permit requirements and codes. Any purchase order issued by Abcott and accepted by the Vendor shall constitute, together with these Terms and Condi |

## Buyer site facts (org_extras, abcott.ca)
- **status**: ok
- **pages**: 4
- **language**: en
- **legal_name**: Abcott Construction Ltd
- **legal_name_url**: https://abcott.ca/
- **legal_name_quote**: ngineered systems. FIND OUT MORE 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE
- **logo_url**: https://abcott.ca/img/Home/Logos/Abcott_LogoFinal.png
- **logo_basis**: logo image on the site
- **domain**: abcott.ca
- **key**: lead:84dcd1f61af2051e
- **name**: Abcott Construction Ltd
- **website**: https://abcott.ca/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Township of North
- **legal_name_stated_url**: https://abcott.ca/
- **legal_name_stated_quote**: ices expert. Select a project below to learn more about our process. VIEW ALL PROJECTS VIEW PROJECT Township of North Dumfries Administration Office Design-build of a 3,283 sq. ft. administration building for the Town
- **linkedin_url**: https://www.linkedin.com/company/abcott-construction-ltd/
- **tel_links**: 5197564350; 519-756-4350

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "124 Garden Avenue, Brantford, ON N3S 7W4", "address_country": "CA", "address_url": "https://abcott.ca/contact/", "address_method": "pattern", "address_quote": "OUCH Phone: 519-756-4350 Email: info@abcott.ca 124 Garden Avenue, Brantford, ON N3S 7W4 LET’S WORK TOGETHER Get started on your next project with Abcott Construction.", "phone": "Call: 519-756-4350", "phone_url": "https://abcott.ca/contact/", "emails": "info@abcott.ca", "emails_url": "https://abcott.ca/contact/", "domain": "abcott.ca", "key": "lead:84dcd1f61af2051e", "name": "abcott.ca", "website": "https://abcott.ca/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, abcottconstruction.com)
- **status**: ok
- **pages**: 1
- **language**: en
- **legal_name**: Abcott Construction Ltd
- **legal_name_url**: https://abcottconstruction.com/
- **legal_name_quote**: ngineered systems. FIND OUT MORE 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE
- **logo_url**: https://abcott.ca/img/Home/Logos/Abcott_LogoFinal.png
- **logo_basis**: logo image on the site
- **domain**: abcottconstruction.com
- **key**: vendor:Abcott Construction Ltd.
- **name**: Abcott Construction Ltd.
- **website**: https://abcottconstruction.com/
- **kind**: vendor
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: Township of North
- **legal_name_stated_url**: https://abcottconstruction.com/
- **legal_name_stated_quote**: ices expert. Select a project below to learn more about our process. VIEW ALL PROJECTS VIEW PROJECT Township of North Dumfries Administration Office Design-build of a 3,283 sq. ft. administration building for the Town
- **linkedin_url**: https://www.linkedin.com/company/abcott-construction-ltd/
- **tel_links**: 5197564350; 519-756-4350

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 3, "address": "124 Garden Avenue, Brantford, ON N3S 7W4", "address_country": "CA", "address_url": "https://abcott.ca/contact/", "address_method": "pattern", "address_quote": "OUCH Phone: 519-756-4350 Email: info@abcott.ca 124 Garden Avenue, Brantford, ON N3S 7W4 LET’S WORK TOGETHER Get started on your next project with Abcott Construction.", "phone": "Call: 519-756-4350", "phone_url": "https://abcott.ca/contact/", "emails": "info@abcott.ca", "emails_url": "https://abcott.ca/contact/", "domain": "abcottconstruction.com", "key": "vd:abcottconstruction.com", "name": "Abcott Construction Ltd.", "website": "https://abcottconstruction.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | Abcott Construction Ltd | found | ABCOTT CONSTRUCTION LTD. | 100010883 | 287520 | ON | ONTARIO BUSINESS CORP. | Inactive | 1974-06-20 | BRANTFORD | Ontario |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=Abcott%20Construction%20Ltd | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Abcott Construction Ltd |  |  |  |  |  |  |  |  |  |  |
| v | Abcott Construction Ltd |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:84dcd1f61af2051e",
 "ap_contact_team": {
  "emails": [
   "info@abcott.ca"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "info@abcott.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://abcott.ca/",
    "quote": "ir building projects with a full range of Butler ® pre-engineered systems. FIND OUT MORE 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE QUOTE REQU",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "abcott.ca",
    "task_id": "CL-LD-06806"
   },
   {
    "email": "info@abcott.ca",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://abcott.ca/terms-and-conditions/",
    "quote": "y other rights Abcott may have under contract or otherwise at law. Updated: January 2021 519-756-4350 124 Garden Ave. Brantford, ON N3S 7W4 info@abcott.ca ©Abcott Construction Ltd. 2026. All rights reserved. Plans Room Terms and Conditions Sitemap REQUEST A QUOTE REQUEST A QUOTE QUOTE REQU",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_search01.csv",
    "org": "Butler Building Systems",
    "task_id": "CL-WS-00098"
   }
  ]
 },
 "research_status": {
  "found": 2
 },
 "queries_tried": [
  "site crawl of abcott.ca (16 pages, robots.txt respected), no AI, no search engine",
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

## The vendor's other buyers in the dataset (first 60 of 7)
| record_id | buyer | title | value | start | end | link |
|---|---|---|---|---|---|---|
| ca_biddingo:39648628:41080062 | Grand Erie District School Board | Culinary Renovations at North Park Collegiate and Vocational School |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003331/39648628 |
| ca_biddingo:39322228:41080062 | Grand Erie District School Board | Temporary Child Care Centre for Banbury Heights School - Grand Erie DSB |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003331/39322228 |
| ca_biddingo:38227428:41080062 | Grand Erie District School Board | Brier Park Public School - Interior Renovations  |  |  |  | https://api.biddingo.com/restapi/bidding/noauthorize/1/11003331/38227428 |
| ca_bidsandtenders:c0aa5f89-97fc-47ee-a84c-e9fbaf9a3411:1 | City of Brantford | Construction of Walter Gretzky Golf Course Maintenance Building | 1686016.72 |  |  | https://brantford.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c0aa5f89-97fc-47ee-a84c-e9fbaf9a3411 |
| ca_bidsandtenders:9afed4da-c1f1-4c7f-99b1-5c9a2b31c224:1 | City of Woodstock | Southside Park Works Building Renovations |  |  |  | https://cityofwoodstock.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/9afed4da-c1f1-4c7f-99b1-5c9a2b31c224 |
| ca_bidsandtenders:8cf0c014-872f-42fe-9ae2-de9dc5f20bfa:1 | County of Brant | Burford Fire Station Bunker Gear Relocation | 192033.0 |  |  | https://brant.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/8cf0c014-872f-42fe-9ae2-de9dc5f20bfa |
| ca_bidsandtenders:c963bc96-9e9b-4b35-825b-d5eae2e58ae9:1 | North Dumfries | Design Build Public Works Administration Building |  |  |  | https://northdumfries.bidsandtenders.ca/Module/Tenders/en/Tender/Detail/c963bc96-9e9b-4b35-825b-d5eae2e58ae9 |

## Open questions for hand research (layer 2)

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

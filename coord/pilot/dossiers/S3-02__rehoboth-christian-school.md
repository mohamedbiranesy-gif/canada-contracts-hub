# S3-02 — Rehoboth Christian School ⇄ CoreFour Inc.

Stratum: **S3_routed_public_body_general_inbox** · pay on sight: routed — complete invoice, but only a purchasing / general inbox is confirmed · channel tier 3 · AP grade C · missing: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/) — 43 Main St E, Norwich, ON N0J 1P0
SUBMIT TO: office@rcsnorwich.com (general mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none)
DESCRIPTION: Rehoboth Christian School (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendo
```

## Relationship
- **rank_group**: T1
- **data_quality_score**: 52
- **ship_ready**: no (mailbox below finance grade)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: n/a (the relationship is a record, not an inference)
- **relationship_detail**: Rehoboth Christian School (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendor seen on the buyer's own site: CoreFour Inc. | awarded 2026-11-02 | published by: the buyer's own website (service of a Canada-HQ vendor in use) | record: https://rcsnorwich.com/ | vendor in Canada because: service of a Canada-HQ vendor seen on the buyer's own site (tech)=Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada | status rule: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor CoreFour Inc.
- **how_relationship_was_found**: tools/tech_portals2.py / tech_relationships.py found the buyer's own web property running the Canada-HQ vendor's paid platform (portal host or embedded service), dated by the page read
- **keys**: lead:690ec2dacb42bd0f
- **tier**: T
- **grade**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)

## Buyer
- **buyer**: Rehoboth Christian School
- **buyer_website**: https://rcsnorwich.com/
- **buyer_address**: 43 Main St E, Norwich, ON N0J 1P0
- **buyer_contact_evidence_url**: https://rcsnorwich.com/contact/
- **buyer_legal_name_as_published**: Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/)
- **buyer_logo_url**: https://rcsnorwich.com/wp-content/uploads/2020/04/RCS-Norwich-logo.jpg
- **buyer_website_status**: site answers
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://rcsnorwich.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: office@rcsnorwich.com
- **email_type**: general
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); general role mailbox
- **email_evidence_url**: https://rcsnorwich.com/contact/
- **email_evidence_quote**: ffice@rcsnorwich.com">office@rcsnorwich.com</a></p></div></div></div><div class="et_pb_column et_pb_column_1_2 et_pb_column_1 et_pb_css_mix_blend_mod
- **mailbox_recheck_note**: mailbox not seen in the page text when re-read 2026-11-08 (dynamic page, PDF or removed — the referee's own re-fetch decides; check before use)
- **mailbox_provenance**: office@rcsnorwich.com (general) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://rcsnorwich.com/contact/ | quote: "ffice@rcsnorwich.com">office@rcsnorwich.com</a></p></div></div></div><div class="et_pb_column et_pb_column_1_2 et_pb_column_1 et_pb_css_mix_blend_mod" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-36064
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365
- **dmarc_policy**: p=quarantine
- **dmarc_record**: v=DMARC1; p=quarantine; rua=mailto:omln0v4r@ag.dmarcian.com; pct=1;
- **dmarc_record_domain**: rcsnorwich.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:spf.protection.outlook.com include:spf1.secureserver.net include:spf.mailjet.com ip4:64.39.162.26 ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 3
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/) — 43 Main St E, Norwich, ON N0J 1P0 ⏎ SUBMIT TO: office@rcsnorwich.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Rehoboth Christian School (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendo
- **invoice_card_json**: {"bill_to": {"legal_name": "Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/)", "legal_name_is_published": true, "address": "43 Main St E, Norwich, ON N0J 1P0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "office@rcsnorwich.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08)", "bn9": "806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)", "neq": ""
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **language_hint**: en
- **template_language**: en

## Vendor
- **vendor**: CoreFour Inc.
- **vendor_legal_name**: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_registry_id**: 2247351 (ON)
- **vendor_registry_url**: https://ised-isde.canada.ca/cbr-rec/en/search?q=CoreFour%20Inc.
- **vendor_registered_address**: Richmond Hill, Ontario (registered office city / province; Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_legal_form**: ONTARIO BUSINESS CORP. (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_address**: 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1
- **vendor_country_basis**: service of a Canada-HQ vendor seen on the buyer's own site (tech)=Richmond Hill 68B Leek Crescent Suite 200 Richmond Hill, Ontario L4B 1H1 Canada
- **vendor_bn9**: 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_gst_hst_derived**: 806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)
- **vendor_website**: https://corefour.com/
- **vendor_contact_evidence_url**: https://corefour.com/
- **vendor_website_basis**: found by a web search, confirmed by reading the site on 2026-11-08: https://corefour.com/ (CoreFour Skip to the content CoreFour Menu Home Close Menu Home CoreFour Inc. Developers of the Edsby learning platform for K‑12, and the Unison education data )
- **vendor_facts_provenance**: name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use)); registry identity: 2247351 (ON) status Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data; match); BN9: registry: Canada's Business Registries, ON 2247351, 2026-11-08; GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); incorporated / registered: 2010-06-15; phone / role e-mails / logo: the vendor's own site, https://corefour.com/ (tools/org_contacts.py, org_extras.py); website: https://corefour.com/
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_registry_status**: Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08)
- **vendor_incorporation_date**: 2010-06-15
- **vendor_years_in_business**: 16.4 (since 2010-06-15, registry date)
- **vendor_bn_source**: registry: Canada's Business Registries, ON 2247351, 2026-11-08

## Contract
- **contract_status**: active service seen on the buyer's own site (2026-11-02): Canada-HQ vendor CoreFour Inc.
- **award_date**: 2026-11-02
- **contract_link**: https://rcsnorwich.com/
- **source**: the buyer's own website (service of a Canada-HQ vendor in use)
- **contracts_with_canadian_suppliers**: 1
- **records_with_this_vendor**: 1 (relationship record: the buyer's own website (service of a Canada-HQ vendor in use); 0 in the contract dataset)
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: HST 13% (Ontario) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)

## Pay on sight / grades
- **pay_on_sight**: routed — complete invoice, but only a purchasing / general inbox is confirmed
- **pay_on_sight_missing**: an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed); (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/) — 43 Main St E, Norwich, ON N0J 1P0 ⏎ SUBMIT TO: office@rcsnorwich.com (general mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08) — 68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1 | GST/HST 806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their | CURRENCY: DERIVED: CAD (derived: the buyer is in Canada and | TERMS: vendor's standard terms (buyer publishes none) ⏎ DESCRIPTION: Rehoboth Christian School (organisation (type not stated in the record), jurisdiction not stated) — active paid service of a Canada-HQ vendo
- **invoice_card_json**: {"bill_to": {"legal_name": "Rehoboth Christian School, Norwich (schema.org JSON-LD Organization name on https://rcsnorwich.com/)", "legal_name_is_published": true, "address": "43 Main St E, Norwich, ON N0J 1P0", "address_is_the_invoice_address": false, "tax_number": "", "language": "en"}, "submit_to": {"email": "office@rcsnorwich.com", "email_type": "general", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of ON on the invoice; public service bodies claim their", "buyer_tax_status_is_published": false, "indicative_rate": "HST 13% (Ontario)", "currency": "DERIVED: CAD (derived: the buyer is in Canada and", "currency_is_published": false, "vendor_gst_hst": "806996658RT0001 (derived: BN9 + RT0001; GST/HST registration not confirmed)", "vendor_qst": ""}, "vendor_identity": {"legal_name": "COREFOUR INC. (as registered: Canada's Business Registries, ON 2247351, 2026-11-08)", "bn9": "806996658 (Canada's Business Registries, ON 2247351, 2026-11-08)", "neq": ""
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; AP phone or contact for follow-up
- **ap_grade**: C
- **ap_score**: 51
- **ap_grade_basis**: met: referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; finance mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: a confirmed invoicing / AP or finance channel; the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["office@rcsnorwich.com (general)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://rcsnorwich.com/contact/", "quote: \"ffice@rcsnorwich.com\">office@rcsnorwich.com</a></p></div></div></div><div class=\"et_pb_column et_pb_column_1_2 et_pb_column_1 et_pb_css_mix_blend_mod\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "DMARC enforced: p=quarantine; SPF ~all (soft fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-LD-36064"], "buyer_facts": ["address and phone: the buyer's own site, https://rcsnorwich.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (the buyer's own website (service of a Canada-HQ vendor in use))", "registry identity: 2247351 (ON) status Active — incorporated (Canada's Business Registries, ON 2247351, 2026-11-08) (scripts/enrichment_*: Corporations Canada / REQ / BC OrgBook bulk data", "match)", "BN9: registry: Canada's Business Registries, ON 2247351, 2026-11-08", "GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected", "not automated)", "inc

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://rcsnorwich.com/contact/ | 2026-11-08 | ok |  |  |  |  | 43 Main St E Norwich, ON N0J 1P0 |  |  |  |  |

## Buyer site facts (org_extras, rcsnorwich.com)
- **status**: ok
- **pages**: 3
- **language**: en
- **logo_url**: https://rcsnorwich.com/wp-content/uploads/2020/04/RCS-Norwich-logo.jpg
- **logo_basis**: logo image in the site header
- **domain**: rcsnorwich.com
- **key**: lead:690ec2dacb42bd0f
- **name**: Rehoboth Christian School
- **website**: https://rcsnorwich.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **jsonld_type**: Organization
- **jsonld_name**: Rehoboth Christian School, Norwich
- **jsonld_logo**: https://rcsnorwich.com/wp-content/uploads/2020/03/logo.png
- **jsonld_url**: https://rcsnorwich.com/
- **jsonld_quote**: {"@context":"https:\/\/schema.org","@graph":[{"@type":"WebPage","@id":"https:\/\/rcsnorwich.com\/","url":"https:\/\/rcsnorwich.com\/","name":"RCS Norwich | Rehoboth Christian School","isPartOf":{"@id":"https:\/\/rcsnorwich.com\/#website"},"about":{"@id":"https:\/\/rcsnorwich.com\/#organization"},"pr
- **jsonld_page**: https://rcsnorwich.com/
- **mentions**: {'payment_method': {'text': 'interact and communicate with people with various types of disabilities', 'url': 'https://rcsnorwich.com/accessibility/', 'quote': 'of the Accessibility Standards for Customer Service , Ontario O. Reg 191/11 Instructions on how to interact and communicate with people with various types of disabilities. Instructions on how to interact with people with disabilities who: Use assistive device'}}

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "address": "43 Main St E, Norwich, ON N0J 1P0", "address_country": "CA", "address_url": "https://rcsnorwich.com/contact/", "address_method": "pattern", "address_quote": "eporting Select Page Contact Rehoboth Christian School 43 Main St E Norwich, ON N0J 1P0 Phone: (519) 863-2403 Elementary Principal: Andrew Korevaar Email: elementarypr", "emails": "office@rcsnorwich.com", "emails_url": "https://rcsnorwich.com/contact/", "domain": "rcsnorwich.com", "key": "lead:690ec2dacb42bd0f", "name": "Rehoboth Christian School", "website": "https://rcsnorwich.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, corefour.com)
- **status**: ok
- **pages**: 1
- **v**: 2
- **language**: en
- **domain**: corefour.com
- **key**: vendor:CoreFour Inc.
- **name**: CoreFour Inc.
- **website**: https://corefour.com/
- **kind**: vendor
- **date**: 2026-11-09

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "68B Leek Crescent, Suite 200, Richmond Hill, Ontario, Canada L4B 1H1", "address_country": "CA", "address_url": "https://corefour.com/", "address_method": "pattern", "address_quote": "United States 01810 68B Leek Crescent, Suite 200 Richmond Hill, Ontario Canada L4B 1H1 28 Devon Street Aro Valley Wellington New Zealand 6021 © 2026 CoreFour Powered", "domain": "corefour.com", "key": "vendor:CoreFour Inc.", "name": "CoreFour Inc.", "website": "https://corefour.com/", "kind": "vendor", "date": "2026-11-09"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Rehoboth Christian School |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "lead:690ec2dacb42bd0f",
 "ap_contact_team": {
  "emails": [
   "office@rcsnorwich.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "office@rcsnorwich.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://rcsnorwich.com/contact/",
    "quote": "ffice@rcsnorwich.com\">office@rcsnorwich.com</a></p></div></div></div><div class=\"et_pb_column et_pb_column_1_2 et_pb_column_1 et_pb_css_mix_blend_mod",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "Rehoboth Christian School",
    "task_id": "CL-LD-36064"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of rcsnorwich.com (7 pages, robots.txt respected), no AI, no search engine"
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

- an invoicing / AP or finance mailbox (only a purchasing / general inbox is confirmed: the invoice is routed, not addressed)
- (reference rule not published)
- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)
- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship

## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)

_pending_

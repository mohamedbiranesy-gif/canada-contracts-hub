# S2-34 — ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION ⇄ inferred: Hydro-Québec

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name) — 12025 RUE DEPATIE, Montreal, QC, H4J1W8 — buyer tax no. 732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)
SUBMIT TO: comptabilite@jaimemaville.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVED: CAD (de
```

## Relationship
- **rank_group**: I3
- **data_quality_score**: 48
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION (municipality / local government, QC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Hydro-Québec | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); Hydro-Québec holds the exclusive rig
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:732604335
- **tier**: I
- **grade**: 3

## Buyer
- **buyer**: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION
- **buyer_website**: https://jaimemaville.com
- **buyer_address**: 12025 RUE DEPATIE, Montreal, QC, H4J1W8
- **buyer_phone**: 514 532-1105
- **buyer_contact_evidence_url**: https://jaimemaville.com/
- **buyer_legal_name_as_published**: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)
- **buyer_bn_as_published**: 732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 732604335RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://jaimemaville.com/wp-content/themes/jaimemaville-wp-theme/images/logoPin.png
- **buyer_website_status**: site answers
- **buyer_type**: municipality / local government
- **buyer_sector**: government: municipal
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)
- **buyer_charity_designation**: C; 0160
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://jaimemaville.com/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptabilite@jaimemaville.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://jaimemaville.com/
- **email_evidence_quote**: n-form/fdc3299f-c4bc-4fef-8a9b-a940ba9d9506?modal=true" class="btn__dons btn__nonBlurable"> Faire un don en ligne </a> <!-- <a href="mailto:comptabilite@jaimemaville.com?subject=Faire un don à JMV&body=Bonjour, j'aimerais faire un don à J'aime ma ville par Virement Interac ou par chèque. P
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptabilite@jaimemaville.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://jaimemaville.com/ | quote: "n-form/fdc3299f-c4bc-4fef-8a9b-a940ba9d9506?modal=true" class="btn__dons btn__nonBlurable"> Faire un don en ligne </a> <!-- <a href="mailto:comptabilite@jaimema" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04303
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none; rua=mailto:1d6398bb6a7a4fb2a021800f5ac48cda@dmarc-reports.cloudflare.net;
- **dmarc_record_domain**: jaimemaville.com
- **spf_policy**: SPF ~all (soft fail)
- **spf_record**: v=spf1 include:_spf.google.com include:spf.turbo-smtp.com ~all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **invoicing_requirements_structured**: {"submission_channel": "e-mail"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name) — 12025 RUE DEPATIE, Montreal, QC, H4J1W8 — buyer tax no. 732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name) ⏎ SUBMIT TO: comptabilite@jaimemaville.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVE
- **invoice_card_json**: {"bill_to": {"legal_name": "ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)", "legal_name_is_published": true, "address": "12025 RUE DEPATIE, Montreal, QC, H4J1W8", "address_is_the_invoice_address": false, "tax_number": "732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@jaimemaville.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipalit
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **language_hint**: fr
- **template_language**: fr (Québec buyer; French first)

## Vendor
- **vendor**: inferred: Hydro-Québec
- **vendor_address**: 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4
- **vendor_country_basis**: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4'
- **vendor_bn9**: 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)
- **vendor_website**: https://www.hydroquebec.com
- **vendor_phone**: +1-888-858-7927
- **vendor_contact_evidence_url**: https://www.hydroquebec.com/nous-joindre/
- **vendor_facts_provenance**: name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record)); BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html); GST/HST derived BN9 + RT0001 (CRA registry is CAPTCHA-protected; not automated); phone / role e-mails / logo: the vendor's own site, https://www.hydroquebec.com/nous-joindre/ (tools/org_contacts.py, org_extras.py); website: https://www.hydroquebec.com
- **vendor_concentration_top_share**: no dataset record for this pair / buyer
- **vendor_bn_source**: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html)

## Contract
- **contract_status**: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); Hydro-Québec holds the exclusive right to distribute electricity in Québec outside the 9 municipal networks (Alma, Amos, Baie-Comeau, Coaticook, Joliette, Magog, Saguenay-Jonquière, Sherbrooke, Westmount) and the Saint-Jean-Baptiste-de-Rouville co-op (Act respecting the Régie de l'énergie); an organisation with premises there buys its electricity from it, unless its landlord pays it through the lease
- **source**: inference from the buyer's type and province (no contract, payment or listing record)
- **contracts_with_canadian_suppliers**: 0
- **records_in_contract_dataset**: none found for this organisation (matched by website domain and exact name)
- **commodity_distribution_top3**: no dataset record for this pair / buyer

## Tax / currency / terms (derived)
- **buyer_gst_hst_derived**: 732604335RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "Note: A municipality is not a government for purposes of the GST/HST"); charge GST/HST; derived from buyer type, not published by the buyer
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name) — 12025 RUE DEPATIE, Montreal, QC, H4J1W8 — buyer tax no. 732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name) ⏎ SUBMIT TO: comptabilite@jaimemaville.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: municipality: GST/HST applies to supplies to it — a municipality is not a government for GST/HST purposes (GST/HST Memorandum 18-2 para. 2 note, https: | CURRENCY: DERIVE
- **invoice_card_json**: {"bill_to": {"legal_name": "ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)", "legal_name_is_published": true, "address": "12025 RUE DEPATIE, Montreal, QC, H4J1W8", "address_is_the_invoice_address": false, "tax_number": "732604335RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (jaimemaville.com) + name)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@jaimemaville.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: municipality: GST/HST applies to supplies to it — a municipalit
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 61
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; AP phone or AP contact; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["comptabilite@jaimemaville.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://jaimemaville.com/", "quote: \"n-form/fdc3299f-c4bc-4fef-8a9b-a940ba9d9506?modal=true\" class=\"btn__dons btn__nonBlurable\"> Faire un don en ligne </a> <!-- <a href=\"mailto:comptabilite@jaimema\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF ~all (soft fail); mail handled by Google Workspace", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-04303"], "buyer_facts": ["address and phone: the buyer's own site, https://jaimemaville.com/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment or listing record))", "BN9: printed on the organisation's own page (https://www.hydroquebec.com/suppliers/invoicing-payment/prep

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://jaimemaville.com/ | 2026-11-08 | ok |  |  |  |  |  |  |  |  |  |

## Buyer site facts (org_extras, jaimemaville.com)
- **status**: ok
- **pages**: 1
- **language**: fr
- **logo_url**: https://jaimemaville.com/wp-content/themes/jaimemaville-wp-theme/images/logoPin.png
- **logo_basis**: logo image in the site header
- **domain**: jaimemaville.com
- **key**: cra:732604335
- **name**: ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION
- **website**: https://jaimemaville.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **mentions**: {'payment_method': {'text': 'Virement Interac ou Chèque Pour faire un don par Virement Interac ou par chèque, veuille', 'url': 'https://jaimemaville.com/', 'quote': 'Faire un don en ligne Faire un don autrement --> Contribuez autrement Contribuez autrement Don par Virement Interac ou Chèque Pour faire un don par Virement Interac ou par chèque, veuillez contacter [email protected] et ils communiqueront avec vous la procédu'}}
- **tel_links**: 514 532-1105

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 1, "address": "12025 Rue Dépatie, Montréal, QC H4J1W8", "address_country": "CA", "address_url": "https://jaimemaville.com/", "address_method": "pattern", "address_quote": "'inscrire --> J’aime Montréal [email protected] 12025 Rue Dépatie, Montréal, QC H4J1W8 J’aime Gatineau [email protected] Facebook Instagram À propos Mission: L’organi", "phone": "514 532-1105", "phone_url": "https://jaimemaville.com/", "emails": "comptabilite@jaimemaville.com", "emails_url": "https://jaimemaville.com/", "domain": "jaimemaville.com", "key": "cra:732604335", "name": "ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION", "website": "https://jaimemaville.com/", "kind": "buyer", "date": "2026-11-03"}

## Vendor site facts (org_extras, hydroquebec.com)
- **status**: ok
- **pages**: 1
- **language**: fr
- **domain**: hydroquebec.com
- **key**: b:43240b176b1f24b7
- **name**: Hydro-Québec
- **website**: https://hydroquebec.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2

## Vendor role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 4, "address": "75, boulevard René-Lévesque Ouest, Montréal, QC, H2Z 1A4", "address_country": "CA", "address_url": "https://www.hydroquebec.com/nous-joindre/", "address_method": "json-ld", "address_quote": "social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4 Fermé pour rénovation jusqu'en 2029 En savoir plus Sujets connexes Commentaire", "phone": "+1-888-858-7927", "phone_url": "https://www.hydroquebec.com/nous-joindre/", "domain": "hydroquebec.com", "key": "vd:hydroquebec.com", "name": "Hydro-Québec.", "website": "https://hydroquebec.com/", "kind": "vendor", "date": "2026-11-03"}

## Registry records (Canada's Business Registries lookups)
_none_

## Registry records (REQ / Corporations Canada bulk match)
_none_

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Hydro-Québec | Q167840 | official website on the organisation's domain (http://www.hydroquebec.com/) + name |  | Hydro-Quebec | Hydro-Québec | Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity | Crown corporation | Canada | 1944-04-14 | Hydro-Québec Building |
| b | ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION |  |  |  |  |  |  |  |  |  |  |
| v | Hydro-Québec Développement énergétique inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:732604335",
 "ap_contact_team": {
  "emails": [
   "comptabilite@jaimemaville.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "comptabilite@jaimemaville.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://jaimemaville.com/",
    "quote": "n-form/fdc3299f-c4bc-4fef-8a9b-a940ba9d9506?modal=true\" class=\"btn__dons btn__nonBlurable\"> Faire un don en ligne </a> <!-- <a href=\"mailto:comptabilite@jaimemaville.com?subject=Faire un don à JMV&body=Bonjour, j'aimerais faire un don à J'aime ma ville par Virement Interac ou par chèque. P",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "ORGANISATION COMMUNAUTAIRE J'AIME MA VILLE / I LOVE MY CITY COMMUNITY ORGANIZATION",
    "task_id": "CL-CRA-04303"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of jaimemaville.com (7 pages, robots.txt respected), no AI, no search engine"
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

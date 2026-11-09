# S2-26 — MAISON DE LA FAMILLE ÉVEIL-NAISSANCE ⇄ inferred: Hydro-Québec

Stratum: **S2_complete_no_published_PO_rule** · pay on sight: yes — reference rule not published (quote the buyer's PO / order number when one is issued) · channel tier 2 · AP grade C · missing: (reference rule not published)

## 1. Draft invoice header (from the row)
```
DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json)
BILL TO: Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name) — 415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1 — buyer tax no. 120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)
SUBMIT TO: comptabilite@eveilnaissance.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee)
REFERENCE: none in the record | PO rule: not published
FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9)
TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY: DERIVED: 
```

## Relationship
- **rank_group**: I3
- **data_quality_score**: 48
- **ship_ready**: no (relationship not dated / active)
- **sensitivity_flag**: no
- **evidence_age_days**: 8
- **reverify_due**: no
- **inference_confidence**: MEDIUM (typical supplier for this type of organisation)
- **relationship_detail**: MAISON DE LA FAMILLE ÉVEIL-NAISSANCE (organisation (type not stated in the record), QC) — inferred: no record; the organisation's type and province make a Canadian supplier relationship near-certain: inferred: Hydro-Québec | published by: inference from the buyer's type and province (no contract, payment or listing record) | vendor in Canada because: the vendor's own site, https://www.hydroquebec.com/nous-joindre/: 'Siège social Édifice Jean-Lesage 75, boulevard René‑Lévesque Ouest Montréal (Québec) H2Z 1A4' | status rule: inferred relationship (no record): medium confidence; the buyer is an organisation in Québec (province from its registered address in the CRA List of charities 2024 (open.canada.ca)); Hydro-Québec holds the exclusive rig
- **how_relationship_was_found**: no record; tools/org_lists.py / osm_orgs.py / the crawlers placed the organisation in Canada by type and province; the vendor named is the Canada-located supplier such bodies almost always pay (see `vendor_country_basis`)
- **keys**: cra:120851332
- **tier**: I
- **grade**: 3

## Buyer
- **buyer**: MAISON DE LA FAMILLE ÉVEIL-NAISSANCE
- **buyer_website**: https://eveilnaissance.com
- **buyer_address**: 415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1
- **buyer_contact_evidence_url**: https://eveilnaissance.com/contact/
- **buyer_legal_name_as_published**: Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)
- **buyer_bn_as_published**: 120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)
- **buyer_bn_program**: program not stated with the number
- **buyer_gst_hst_derived**: 120851332RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_logo_url**: https://eveilnaissance.com/wp-content/themes/eveilnaissance/asset/img/opengraph_img.jpg
- **buyer_website_status**: site answers
- **buyer_registry_id**: NEQ 1142847327 (Registraire des entreprises du Québec (open data); https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx)
- **buyer_type**: organisation (type not stated in the record)
- **buyer_sector**: not stated
- **buyer_charity_status**: registered (listed) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)
- **buyer_charity_designation**: C; 0100
- **buyer_legal_form**: APE (personne morale sans but lucratif / de droit public) (Registraire des entreprises du Québec (open data), NEQ 1142847327, 2026-11-08)
- **buyer_facts_provenance**: address and phone: the buyer's own site, https://eveilnaissance.com/contact/ (tools/org_contacts.py: JSON-LD / contact page; no AI); legal name: the site's copyright / footer line (tools/org_extras.py); BN: as printed on the buyer's site (see buyer_bn_as_published for the page); GST/HST derived as BN9 + RT0001, not confirmed; logo: og:image / logo image of the buyer's site; website: site answers; AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI; URL and date in the cell)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **buyer_keys**: 1

## Submit-to / AP
- **peppol_registered**: not listed in the Peppol Directory (country=CA search on 2026-11-06: 77 Canadian participants in total)
- **email**: comptabilite@eveilnaissance.com
- **email_type**: finance/accounting dept or supplier-payment office
- **email_check**: confirmed
- **mailbox_confidence**: verified by the referee (page re-fetched); finance mailbox
- **email_evidence_url**: https://eveilnaissance.com/contact/
- **email_evidence_quote**: 418 275-6581 poste 206 Joanie Milot Adjointe administrative comptabilite@eveilnaissance.com 418 275-6581 poste 201 Marie-Pier Naud Intervenante famille & responsable SDA marie-pier.naud@eveilnaissance.com 418 2
- **email_evidence_context**: 05 Louise Bonneau Intervenante famille & en allaitement louise.bonneau@eveilnaissance.com 418 275-6581 poste 202 Patricia Girard Coordonnatrice des activités coordination@eveilnaissance.com 418 275-6581 poste 206 Joanie Milot Adjointe administrative comptabilite@eveilnaissance.com 418 275-6581 poste 201 Marie-Pier Naud Intervenante famille & responsable SDA marie-pier.naud@eveilnaissance.com 418 275-6581 poste 203 Johan-Eve Perron Intervenante famille & en allaitement johan-eve.perron@eveilnaissance.com 418 275-6581 poste 210 (page text around the mailbox, re-read 2026-11-08)
- **mailbox_recheck_note**: mailbox seen again on the page when re-read 2026-11-08
- **mailbox_provenance**: comptabilite@eveilnaissance.com (finance/accounting dept or supplier-payment office) | found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01 | page: https://eveilnaissance.com/contact/ | quote: "418 275-6581 poste 206 Joanie Milot Adjointe administrative comptabilite@eveilnaissance.com 418 275-6581 poste 201 Marie-Pier Naud Intervenante famille & respon" | verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z) | DNS: domain publishes a mail server (MX) | EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365 | lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-03772
- **email_deliverability**: domain publishes a mail server (MX)
- **email_security_posture**: EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365
- **dmarc_policy**: v=DMARC1; p=none (monitor only, no enforcement)
- **dmarc_record**: v=DMARC1; p=none
- **dmarc_record_domain**: eveilnaissance.com
- **spf_policy**: SPF -all (hard fail)
- **spf_record**: v=spf1 mx a include:spf.protection.outlook.com  include:no-ip.com ip4:198.27.80.203 ip4:158.85.89.116 ip4:158.85.77.121  -all
- **mta_sts**: no MTA-STS record
- **tls_rpt**: no TLS-RPT record
- **bimi**: no BIMI record
- **ap_phone**: 418 275-6581 poste 202 (as printed on https://eveilnaissance.com/contact/, re-read 2026-11-08)
- **invoicing_requirements_structured**: {"submission_channel": "e-mail", "ap_phone": "418 275-6581 poste 202 (as printed on https://eveilnaissance.com/contact/, re-read 2026-11-08)"}
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **channel_tier**: 2
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name) — 415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1 — buyer tax no. 120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name) ⏎ SUBMIT TO: comptabilite@eveilnaissance.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY:
- **invoice_card_json**: {"bill_to": {"legal_name": "Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)", "legal_name_is_published": true, "address": "415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1", "address_is_the_invoice_address": false, "tax_number": "120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@eveilnaissance.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption publis
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
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
- **buyer_gst_hst_derived**: 120851332RT0001 (derived from the charity's BN9; an RT account is not confirmed by the CRA list)
- **buyer_tax_status_derived**: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their own rebate afterwards (ETA s. 259); a registrant buyer recovers tax through ITCs
- **tax_rate_indicative_derived**: GST 5% (QC) — indicative rate for a supply made in the buyer's province (GST/HST Memorandum 18-2 'GST/HST rates', https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/18-2/provincial-governments.html, read 2026-11-08: "The HST applies in the participating provinces at the following rates: 13% in Ontario and 15% in New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island. The GST applies in the rest of Canada at the rate of 5%"); the place-of-supply rules decide (Memorandum 3-3-2); provincial sales taxes (QST, PST) are not covered here
- **invoice_currency_derived**: CAD (derived: the buyer is in Canada and the row has no contract record stating a currency; the invoice would be in Canadian dollars unless the vendor and buyer agreed otherwise)
- **vendor_gst_hst_derived**: 119449775RT0001 (119449775 RT0001; QST 1000042605 TQ0020)

## Pay on sight / grades
- **pay_on_sight**: yes — reference rule not published (quote the buyer's PO / order number when one is issued)
- **pay_on_sight_missing**: (reference rule not published)
- **invoice_text**: DRAFT INVOICE HEADER — built only from the row's sourced and labelled-derived columns (provenance in facts_provenance_json) ⏎ BILL TO: Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name) — 415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1 — buyer tax no. 120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name) ⏎ SUBMIT TO: comptabilite@eveilnaissance.com (finance/accounting dept or supplier-payment office mailbox, confirmed by the referee) ⏎ REFERENCE: none in the record | PO rule: not published ⏎ FROM / REMIT TO: Hydro-Québec — 75, boulevard René-Lévesque Ouest, Montréal (Québec) H2Z 1A4 | GST/HST 119449775 (GST/HST registration number printed by the organisation itself: https://www.hydroquebec.com/suppliers/invoicing-payment/preparing-submitting-invoice.html, 2026-11-08)RT0001 (account derived from the BN9) ⏎ TAX: DERIVED: taxable purchaser presumed (no exemption published); charge GST/HST at the place-of-supply rate of QC on the invoice; public service bodies claim their | CURRENCY:
- **invoice_card_json**: {"bill_to": {"legal_name": "Maison de la famille Éveil-Naissance (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)", "legal_name_is_published": true, "address": "415 AVENUE F.X. BOUCHARD, Roberval, QC, G8H3R1", "address_is_the_invoice_address": false, "tax_number": "120851332RR0001 — charity registration number (RR program account) (CRA list of registered charities, https://open.canada.ca/data/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8/resource/694fdc72-eae4-4ee0-83eb-832ab7b230e3/download/ident_2024_updated.csv, 2026-11-08; matched by website domain (eveilnaissance.com) + name)", "language": "fr (Québec buyer; French first)"}, "submit_to": {"email": "comptabilite@eveilnaissance.com", "email_type": "finance/accounting dept or supplier-payment office", "supplier_setup_url": "", "portal_url": "", "portal_kind": "", "mailing_address": "", "format": "", "system": "", "e_invoicing_peppol": "", "portal_is_invoice_channel": false, "portal_class": ""}, "references_required": {"po_required": "", "po_number": "", "contract_or_agreement_number": "", "vendor_id_with_buyer": "", "reference_hint": ""}, "terms": {"payment_terms": "", "payment_method": "", "payment_cycle": "", "e_signature": ""}, "tax": {"buyer_tax_status": "DERIVED: DERIVED: taxable purchaser presumed (no exemption publis
- **invoice_readiness**: 7/11 invoice elements present
- **invoice_missing**: PO rule; reference to quote (PO / contract / vendor id); payment terms; vendor legal name
- **ap_grade**: C
- **ap_score**: 63
- **ap_grade_basis**: met: finance mailbox; referee-confirmed mailbox; mailbox seen again within 60 days; mailbox on the buyer's own domain (or published on the buyer's own site); domain publishes a mail server (MX); bill-to legal name published; invoice or billing address; currency known; AP phone or AP contact | missing: invoicing / AP mailbox; PO rule published; payment terms published; invoice format / requirements published; payment cycle or method published (plausibility) | notes: buyer domain without DMARC enforcement (mail-security posture; see email_security_posture)
- **ap_gap_to_A**: an invoicing / AP mailbox (not finance / procurement / general); published PO rule; published payment terms
- **ap_payability**: not yet payable — missing: the buyer's PO / reference rule
- **facts_provenance_json**: {"mailbox": ["comptabilite@eveilnaissance.com (finance/accounting dept or supplier-payment office)", "found by the no-AI crawler tools/ap_crawler.py reading the buyer's own site (contact / finance / supplier pages) on 2026-11-01", "page: https://eveilnaissance.com/contact/", "quote: \"418 275-6581 poste 206 Joanie Milot Adjointe administrative comptabilite@eveilnaissance.com 418 275-6581 poste 201 Marie-Pier Naud Intervenante famille & respon\"", "verified: the referee (verify-and-merge workflow) re-fetched the page and saw the address (report 2026-11-09T14:16:08Z)", "DNS: domain publishes a mail server (MX)", "EXPOSED to sender spoofing: v=DMARC1; p=none (monitor only, no enforcement); SPF -all (hard fail); mail handled by Microsoft 365", "lane file: claude/claude_buyer_ap_results_crawl01.csv task CL-CRA-03772"], "buyer_facts": ["address and phone: the buyer's own site, https://eveilnaissance.com/contact/ (tools/org_contacts.py: JSON-LD / contact page", "no AI)", "legal name: the site's copyright / footer line (tools/org_extras.py)", "BN: as printed on the buyer's site (see buyer_bn_as_published for the page)", "GST/HST derived as BN9 + RT0001, not confirmed", "logo: og:image / logo image of the buyer's site", "website: site answers", "AP phone: the mailbox's evidence page re-read in full by tools/ap_terms.py (no AI", "URL and date in the cell)"], "vendor_facts": ["name and address: the record's vendor block (inference from the buyer's type and province (no contract, payment

## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)
| evidence_url | retrieved_date | status | payment_terms | po_required | portal_name | ap_phone | invoice_mailing_address | invoice_format | ap_system | payment_terms_quote | po_quote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://eveilnaissance.com/contact/ | 2026-11-08 | ok |  |  |  | 418 275-6581 poste 202 |  |  |  |  |  |

## Buyer site facts (org_extras, eveilnaissance.com)
- **status**: ok
- **pages**: 3
- **language**: fr
- **logo_url**: https://eveilnaissance.com/wp-content/themes/eveilnaissance/asset/img/opengraph_img.jpg
- **logo_basis**: og:image of the home page (looks like a photo, not a logo: check before use)
- **domain**: eveilnaissance.com
- **key**: cra:120851332
- **name**: MAISON DE LA FAMILLE ÉVEIL-NAISSANCE
- **website**: https://eveilnaissance.com/
- **kind**: buyer
- **date**: 2026-11-08
- **v**: 2
- **legal_name_stated**: MRC du Domaine-du-Roy
- **legal_name_stated_url**: https://eveilnaissance.com/
- **legal_name_stated_quote**: autaire autonome, la Maison de la famille Éveil-Naissance accueille les parents de l’ensemble de la MRC du Domaine-du-Roy et leurs enfants. Ayant à cœur le bien-être de l'enfant, elle considère que le parent en est le tou

## Buyer role mailboxes found on its site (org_contacts)
- {"status": "ok", "pages": 2, "emails": "comptabilite@eveilnaissance.com; direction@eveilnaissance.com", "emails_url": "https://eveilnaissance.com/contact/", "domain": "eveilnaissance.com", "key": "cra:120851332", "name": "MAISON DE LA FAMILLE ÉVEIL-NAISSANCE", "website": "https://eveilnaissance.com/", "kind": "buyer", "date": "2026-11-03"}

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
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | ui_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | MAISON DE LA FAMILLE ÉVEIL-NAISSANCE | not_found |  |  |  |  |  |  |  |  |  |  | https://ised-isde.canada.ca/cbr-rec/en/search?q=MAISON%20DE%20LA%20FAMILLE%20%C3%89VEIL-NAISSANCE | 2026-11-08 |

## Registry records (REQ / Corporations Canada bulk match)
| kind | name | status | matched_name | bn9 | juri_id | registry_source | entity_type | status_state | date_incorporated | reg_office_city | reg_office_province | reg_office_address | api_url | retrieved_date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buyer | MAISON DE LA FAMILLE ÉVEIL-NAISSANCE | found | MAISON DE LA FAMILLE ÉVEIL-NAISSANCE |  | NEQ 1142847327 | Registraire des entreprises du Québec (open data) | APE (personne morale sans but lucratif / de droit public) | immatriculée | 1995-02-22 | Roberval | QC | 415, AV. François-Xavier Bouchard, Roberval (Québec), G8H3R1 | https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises | 2026-11-08 |

## Wikidata
| side | name | qid | match_basis | official_name | label_en | label_fr | instance_of | legal_form | country | inception | headquarters |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b | Hydro-Québec | Q167840 | official website on the organisation's domain (http://www.hydroquebec.com/) + name |  | Hydro-Quebec | Hydro-Québec | Crown corporation; public utility; transmission system operator for electricity; distribution network operator for electricity | Crown corporation | Canada | 1944-04-14 | Hydro-Québec Building |
| b | MAISON DE LA FAMILLE ÉVEIL-NAISSANCE |  |  |  |  |  |  |  |  |  |  |
| v | Hydro-Québec Développement énergétique inc. |  |  |  |  |  |  |  |  |  |  |

## Lanes' verified findings for this buyer (team_buyers)
```
{
 "buyer_key": "cra:120851332",
 "ap_contact_team": {
  "emails": [
   "comptabilite@eveilnaissance.com"
  ],
  "invoice_portal": null,
  "phone": null,
  "mailing_address": null,
  "invoicing_requirements": null,
  "evidence": [
   {
    "email": "comptabilite@eveilnaissance.com",
    "type": "general",
    "invoice_portal": null,
    "phone": null,
    "mailing_address": null,
    "requirements": null,
    "applies_to": "whole_organisation",
    "page_url": "https://eveilnaissance.com/contact/",
    "quote": "418 275-6581 poste 206 Joanie Milot Adjointe administrative comptabilite@eveilnaissance.com 418 275-6581 poste 201 Marie-Pier Naud Intervenante famille & responsable SDA marie-pier.naud@eveilnaissance.com 418 2",
    "retrieved_date": "2026-11-01",
    "found_by": "claude",
    "verification": "verified",
    "source_file": "claude_buyer_ap_results_crawl01.csv",
    "org": "MAISON DE LA FAMILLE ÉVEIL-NAISSANCE",
    "task_id": "CL-CRA-03772"
   }
  ]
 },
 "research_status": {
  "found": 1
 },
 "queries_tried": [
  "site crawl of www.eveilnaissance.com (18 pages, robots.txt respected), no AI, no search engine"
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

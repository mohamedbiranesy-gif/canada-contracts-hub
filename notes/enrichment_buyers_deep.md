# Buyer deep AP / invoicing search (W3) — buyers_deep.jsonl

Generated 2026-10-26T03:44:52Z by `scripts/enrichment_buyers_deep/notes_deep.py` after `assemble_deep.py` (assembled 2026-10-26T03:43:37Z). Output: `enrichment/v2/buyers_deep.jsonl` — one line per buyer_key with something new: for `ap_deep` buyers the FULL merged record (the previous record from `enrichment/buyers_enriched.jsonl` / `enrichment/v2/buyers_enriched_v2.jsonl`, which holds the `_known` facts, plus this pass's findings), for the 104 `full_enrichment_new_buyer` keys a full record (always written). Same layout as `buyers_enriched.jsonl`; `extras.deep_pass` lists `new_fields` and `sources` for every line, `extras.ap_inherited_from` marks facts taken from a parent organisation. Pipeline: `scripts/enrichment_buyers_deep/` (copies of the v2 scripts + new `groups.py`, `deep3.py`, `deep4.py`, `newbuyers.py`, `assemble_deep.py`, `notes_deep.py`); earlier scripts and outputs untouched. Work files: `enrichment/work_buyers_deep/`; raw copies of targeted pages: `downloads/enrichment_buyers_deep/pages/`.

## Coverage

Input: 4830 `ap_deep` buyers (415483 contract records) with no AP mailbox and no invoice portal, 104 new buyers (1465 records). Grouped into 4612 organisations (`groups.py`: canonical name from the previous enrichment, explicit merge rules for historical CSSS/CISSS names, union of keys sharing the same official website URL when the names are compatible, e.g. "Halifax Transit (Halifax Regional Municipality)" → HRM, "Newfoundland Labrador Hydro" → NL Hydro); every finding is applied to all keys of its organisation.

| result (ap_deep buyers) | buyer keys | contract records |
|---|---|---|
| gained an AP mailbox or invoice portal | 104 | 39120 |
| gained any AP fact (mailbox, portal, AP phone, invoice mailing address or invoicing requirements) | 208 | 65809 |
| lines written (any new fact) | 440 | 134253 |

Organisations (groups) gaining an AP mailbox/portal: 94.

New facts per field, ap_deep buyers (buyer keys / contract records):

| field | keys | records |
|---|---|---|
| general_contact.emails | 180 | 50849 |
| ap_contact.invoicing_requirements | 176 | 57777 |
| procurement_contact.url | 123 | 30134 |
| ap_contact.emails | 104 | 39120 |
| procurement_contact.emails | 69 | 28483 |
| ap_contact.phone | 67 | 19235 |
| official_website | 67 | 13006 |
| ap_contact.mailing_address | 62 | 18989 |
| extras.finance_role_mailboxes | 17 | 4670 |
| procurement_contact.phone | 6 | 2277 |
| extras.jurisdiction_candidates.ap_emails | 6 | 1206 |
| procurement_contact.supplier_portal | 4 | 954 |
| ap_contact.invoice_portal | 1 | 565 |

New buyers (104, full enrichment) — fill counts (buyer keys / records):

| field | keys | records |
|---|---|---|
| address_any | 54 | 147 |
| website | 45 | 1258 |
| general_email | 25 | 134 |
| address_line1 | 22 | 70 |
| identifiers_directory | 22 | 70 |
| procurement_url | 10 | 158 |
| procurement_email | 5 | 105 |
| invoicing_requirements | 4 | 46 |
| ap_email | 1 | 12 |

## Methods and sources

1. **Automated crawler passes** (UA `contracts-research/1.0 (public-procurement dataset enrichment; polite crawler)`, robots.txt honoured, one queue per host, 0.7 s spacing ≈ 1.4 req/s, a 403/429/503 or bot-challenge page stops the site and is never retried around):
   - `deep2.py` (sitemap-ranked French/English invoicing keywords, ≤16 pages + linked PDFs) over the own websites of all groups with ≥15 records (1,066 sites);
   - `deep3.py` (best-first walk through supplier / finance / procurement / contact sections, depth ≤3, ≤45 HTML + ≤14 PDFs, also records phone numbers printed next to an accounts-payable heading) over the 550 largest sites (`deep3.jsonl`), over 89 websites newly mapped for groups that had none (`deep3b.jsonl`, CEGEPs, museums, agencies, NS/ON/SK bodies; a website is asserted only when its homepage loaded and the title/domain carries a distinctive token of the name) and over 88 candidate websites of the new buyers (`deep3c.jsonl`);
   - `deep4.py` (sitemap scan for Canada Post labour-disruption notices 2024–2025 — municipalities listed the e-mail suppliers should use for invoices while mail was suspended — and invoicing / direct-deposit / PO-terms URLs not opened before).
   Run statistics (file, status: sites): deep2.jsonl blocked_or_challenged: 3, deep2.jsonl no_sitemap_fallback: 188, deep2.jsonl ok: 814, deep2.jsonl partially_blocked: 11, deep2.jsonl unreachable: 50, deep3.jsonl ok: 459, deep3.jsonl partially_blocked: 11, deep3b.jsonl blocked_or_challenged: 4, deep3b.jsonl ok: 84, deep3b.jsonl partially_blocked: 1, deep3c.jsonl blocked_or_challenged: 4, deep3c.jsonl ok: 79, deep3c.jsonl partially_blocked: 4, deep4a.jsonl blocked_or_challenged: 2, deep4a.jsonl ok: 500; pages/PDFs fetched by these passes: 11234.
2. **Targeted research** (WebSearch in French/English to locate candidate pages — mostly ineffective for French-language Quebec pages, as noted in v1 — then the page itself fetched with `probe.py`, raw copy saved; `add_manual.py` refuses an e-mail that is not in the fetched copy of the cited URL). 89 fetches logged in `enrichment/work_buyers_deep/probe_log.jsonl`; 11 curated findings in `enrichment/work_buyers_deep/manual_ap.jsonl`:
   - `halifax_regional_municipality` — https://www.halifax.ca/media/76815 (retrieved 2026-10-26T03:19:04Z): AP hrmaplink@halifax.ca
   - `ville_de_saguenay` — https://ville.saguenay.ca/files/medias/communiques/2025/Suspension-de-livraison-de-courrier.pdf (retrieved 2026-10-26T03:02:16Z): AP tresorerie@ville.saguenay.qc.ca
   - `centre_de_services_scolaire_de_montreal` — https://www.cssdm.gouv.qc.ca/wp-content/uploads/Fournisseurs_de_biens_et_services.pdf (retrieved 2026-10-26T03:01:39Z): AP —; procurement: approv@cssdm.gouv.qc.ca
   - `the_city_of_winnipeg` — https://legacy.winnipeg.ca/francais/finance/files/Direct_Deposit_Form.pdf (retrieved 2026-10-26T03:23:14Z): AP fin-eft-advice@winnipeg.ca
   - `gov_SK` — https://publications.saskatchewan.ca/api/v1/products/195/formats/195/download (retrieved 2026-10-26T03:25:39Z): AP mhd@gov.sk.ca; basis: parent (Government of Saskatchewan)
   - `gov_NS` — https://novascotia.ca/lae/lampss/documents/04-EFT-Direct-Deposit-Form.pdf (retrieved 2026-10-26T03:25:38Z): AP gaaccountingservices@novascotia.ca; basis: parent (Government of Nova Scotia)
   - `city_of_burnaby` — https://www.burnaby.ca/sites/default/files/acquiadam/2021-10/Invoice-Processing-at-the-City.pdf (retrieved 2026-10-26T03:28:31Z): AP ap-noreply@burnaby.ca, accounts.payable@burnaby.ca; procurement: purchasing@burnaby.ca
   - `sante_quebec_monteregie_ouest` — https://extranet.santemonteregie.qc.ca/partenaires-daffaires-et-fournisseurs/ (retrieved 2026-10-26T03:33:26Z): AP payables.cisssmo16@ssss.gouv.qc.ca; procurement: achats.cisssmo16@ssss.gouv.qc.ca
   - `universite_laval` — https://www.sf.ulaval.ca/zone-fournisseurs/facturation-et-paiement (retrieved 2026-10-26T03:34:48Z): AP bc_payable@sf.ulaval.ca
   - `universite_laval` — https://www.sf.ulaval.ca/zone-fournisseurs (retrieved 2026-10-26T03:34:39Z): AP —; procurement: accueil.appro@sf.ulaval.ca
   - `universite_de_montreal` — https://finances.umontreal.ca/qui-sommes-nous/nous-joindre/ (retrieved 2026-10-26T03:36:32Z): AP comptesapayer@fin.umontreal.ca; procurement: achats@dagc.umontreal.ca
3. **Parent-organisation inheritance**: central supplier-payment facts of a government apply to its departments only where the government publishes them for all ministries — Government of Saskatchewan (Provincial Comptroller direct-deposit form M221: applies to all ministries; `mhd@gov.sk.ca` is the remittance/direct-deposit box, invoices go to the ordering ministry) → 33 SK ministry keys; Province of Nova Scotia (Service Nova Scotia vendor master, EFT form) → 27 NS department keys. Multi-government bare names ("Infrastructure", "Education", …) get the facts inside their `extras.jurisdiction_candidates` entries only.
4. **New buyers** (`newbuyers.py`): same organisation already enriched under another key (normalized name) → facts copied with `extras.same_organisation_as`; CRA registered-charity list (downloads/cra_charities/ident_2024.csv + weburl_2024.csv, T3010 open data 2024, downloaded by the vendor worker 2026-10-26T02:46Z) → BN (RR account), registered address (exact normalized operating/legal name, province must agree; a charity whose operating name differs from the legal name — e.g. "CITY OF SURREY" operating as Surrey Public Library — is NOT used); candidate official websites crawled and asserted only when verified; locations as published in the notices.

## E-mail rules (unchanged from v1/v2, precision over recall)
- Only role mailboxes copied from the organisation's own pages/documents, each with page URL + retrieval time + snippet in `*.evidence` (`source` says crawler or targeted). No personal mailboxes (first.last, initial+surname, names; personal contacts listed next to role boxes on finance pages were ignored), no pattern-constructed addresses, no decoding of Cloudflare-protected addresses (TDSB, NS Public Works contact page).
- Crawler e-mails must be on the organisation's own domain (or the page's domain / a jurisdiction-consistent government domain); receivable/billing/tax/customer boxes are never AP (new in this pass: `recevoir`, `cashmgmt`, `revenue` tokens); a mailbox whose AP signal comes only from "payment/paiement" needs supplier/invoice context; an `ap_context` box (finance/comptabilité/fournisseurs) is AP only on an invoice/payables/direct-deposit page or next to "send invoices to" wording.
- Supplier-payment boxes that are not invoice-submission addresses (vendor master / EFT / direct-deposit / remittance boxes: Halifax hrmaplink, Winnipeg FIN-EFT-Advice, Saskatchewan mhd, Nova Scotia GAAccountingServices) are kept in `ap_contact.emails` with the wording of the source in `invoicing_requirements`/`notes`, as in v2.

## Blockers and gaps

- Targeted pages that answered 403 / bot challenge (skipped, never retried around): https://princeedwardisland.ca/en/topic/pei-government-tendering-process, https://servicesfinanciers.uqam.ca/, https://www.cisss-lanaudiere.gouv.qc.ca/liste-de-soins-et-services/liste-par-clientele/partenaires/entreprises-et-fournisseurs/coordonnees-du-service-de-la-comptabilite-comptes-a-payer, https://www.ciussswestcentral.ca/test-page-3768/sub-page, https://www.fs.utoronto.ca/?p=948, https://www.polymtl.ca/, https://www.princeedwardisland.ca/en/information/finance-and-affordability/register-as-a-government-vendor, https://www.ramq.gouv.qc.ca/fr/node/5378386, https://yukon.ca/sites/yukon.ca/files/fin/fin-forms/yg4980_02_2020_b_secured-fr.pdf
- Crawler sites that answered with a block/challenge (40): http://www.richmondhill.ca/, http://www.stcatharines.ca/, http://www.townofmahonebay.ca/, https://agencemobilitedurable.ca/, https://cisss-outaouais.gouv.qc.ca/, https://cmm.qc.ca/, https://cssc.gouv.qc.ca/, https://cssdlj.gouv.qc.ca/, https://lacity.gov/, https://macm.org/, https://mrcminganie.com/, https://societe.lotoquebec.com/, https://umq.qc.ca/, https://uqam.ca/, https://www.ab-conservation.com/, https://www.abbotsford.ca/, https://www.ae.ca/, https://www.amo.on.ca/, https://www.baiesaintpaul.com/, https://www.banq.qc.ca/, https://www.carm.ca/, https://www.cisss-cotenord.gouv.qc.ca/, https://www.cmaisonneuve.qc.ca/, https://www.collegeahuntsic.qc.ca/, https://www.drummondville.ca/, https://www.finances.gouv.qc.ca/, https://www.georgebrown.ca/, https://www.hamilton.ca/, https://www.hec.ca/, https://www.marchofdimes.ca/, https://www.mrchr.qc.ca/, https://www.papineauville.ca/, https://www.placer.ca.gov/, https://www.quartierdesspectacles.com/, https://www.santelaurentides.gouv.qc.ca/, https://www.src.sk.ca/, https://www.stfx.ca/, https://www.telequebec.tv/, https://www.ttc.ca/, https://www.waa.ca/
- Sites blocked in earlier passes were not crawled again (e.g. transports.gouv.qc.ca, revenuquebec.ca, saaq.gouv.qc.ca, laval.ca, terrebonne.ca, justice.gouv.qc.ca, santequebec.ca, yukon.ca, princeedwardisland.ca, vaughan.ca, guelph.ca, burlington.ca).
- bids&tenders / MERX / SEAO tender documents require supplier registration or a paid account: not downloaded (registration-gated, not "publicly downloadable"), even where a direct document link exists.
- Most Quebec public bodies (ministries, CIUSSS/CISSS, cities, school service centres) publish no supplier-invoicing mailbox on their public sites; invoicing instructions are in contract/PO documents distributed through SEAO. Santé Québec has no central supplier-invoicing page reachable (santequebec.ca answers 403). The Quebec government supplier direct-deposit form formerly at cdn-contenu.quebec.ca (FO_adhesion_depotdirect.pdf) now answers 404.
- Government of British Columbia: no central supplier-invoice or vendor-master mailbox found (FIN 312 direct-deposit form has none; the forests invoice page is disallowed by robots.txt); BC ministry keys keep their previous facts.
- WebSearch returned mostly job ads / unrelated pages for French queries; English queries worked better for English-language organisations.

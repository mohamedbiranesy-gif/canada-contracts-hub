# canada_federal — Government of Canada contracts with Canadian vendors, ongoing on 2026-10-25

Source key: `canada_federal` · Output: `/home/claude/contracts/normalized/canada_federal.jsonl` (42,193 records, 596,377,108 bytes, md5 `af17726eeb2dfe8496a5056443f6d37e`) · Built 2026-10-25 13:44 UTC by `/home/claude/contracts/scripts/canada_federal/build.py`.

## 1. Result summary

| status | records |
|---|---|
| `ongoing` | 39,862 |
| `end_date_unknown` | 2,331 |
| `ongoing_inferred` | 0 (not used; no source gives a duration without an end date) |
| **total** | **42,193** |

By source combination (pd = Proactive Publication contracts over $10K; ch = CanadaBuys contract history; an = CanadaBuys award notices; tn = CanadaBuys tender notice attached for enrichment):

| combination | records | of which end_date_unknown |
|---|---|---|
| pd | 28,216 | 267 |
| pd+tn | 242 | 0 |
| pd+an+tn | 1,433 | 0 |
| pd+an | 152 | 0 |
| pd+ch+an+tn | 262 | 0 |
| pd+ch+an | 125 | 0 |
| pd+ch | 2 | 0 |
| ch+an+tn | 4,201 | 0 |
| ch+an | 2,376 | 0 |
| ch | 105 | 0 |
| an+tn | 2,828 | 800 |
| an | 2,251 | 1,264 |

Records carrying proactive-disclosure data: 30,432 (covering 45,494 proactive-disclosure rows). Records carrying CanadaBuys contract history: 7,071. Records carrying a CanadaBuys award notice: 13,628. Records with an attached tender notice: 8,966. Sum of normalized `contract.value` where present: ≈ CAD 229 billion over 36,883 records (844 records have no usable value: CanadaBuys rows with blank/0 amounts, mostly standing offers and supply arrangements, which are reported at $0 by design).

Distinct buyers: 332 (99 proactive-disclosure `owner_org`s; 274 distinct CanadaBuys contracting/end-user entity spellings for CanadaBuys-only records — these are *not* normalized to a canonical department list; the same department appears under several spellings, e.g. "Department of National Defence (DND)" / "National Defence").

## 2. What was downloaded (all 2026-10-25 UTC, via curl `-L -C -`, User-Agent `contracts-research/1.0`, through the configured proxy; log: `scripts/canada_federal/logs/download.log`)

| file (in `/home/claude/contracts/downloads/canada_federal/`) | URL | retrieved (UTC) | bytes | rows (excl. header) | md5 |
|---|---|---|---|---|---|
| `contracts.csv` | https://open.canada.ca/data/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305/download/contracts.csv | 12:07:44 | 641,938,119 | 1,313,552 | 4b498f466034bcf8193f0bf908f91e95 |
| `contracts-nil.csv` (Nothing to Report) | …/resource/fa4ff6c4-e9af-4491-9d4e-2b468e415a68/download/contracts-nil.csv | 12:06:45 | 11,018 | — | 9ca5eab904e4734a3730834a2d556a24 |
| `contractsa.csv` (Aggregated $10K-and-under totals) | …/resource/2e9a82e2-bb18-4bff-a61e-59af3b429672/download/contractsa.csv | 12:06:46 | 106,872 | — | 8101571dbbee26301f365044097c2052 |
| `load-contracts-2020-10-01.csv` (Legacy Data resource) | …/resource/7f9b18ca-f627-4852-93d5-69adeb9437d6/download/load-contracts-2020-10-01.csv | 12:31 | 957,109 | 2,470 | 656381ac803322fc9d93cecdccdd1014 |
| `contracts_schema.json` (recombinant field schema) | https://open.canada.ca/data/recombinant-published-schema/contracts.json | 12:06:41 | 188,118 | — | — |
| `contracts_data_dictionary.xlsx` | https://open.canada.ca/data/recombinant-published-dictionary/contracts | 12:06:43 | 69,245 | — | — |
| `contractHistoryComplete-contratsOctroyesComplet.csv` | https://canadabuys.canada.ca/opendata/pub/contractHistoryComplete-contratsOctroyesComplet.csv | 12:06:48 | 61,707,854 | 23,238 | cf2de2a384bc4d174388105825443fb4 |
| `awardNoticeComplete-avisAttributionComplet.csv` | https://canadabuys.canada.ca/opendata/pub/awardNoticeComplete-avisAttributionComplet.csv | 12:06:52 | 104,081,268 | 29,000 | ce11a3283b44c33efe089ef227d63ed5 |
| `tenderNoticeComplete-avisAppelOffresComplet.csv` | https://canadabuys.canada.ca/opendata/pub/tenderNoticeComplete-avisAppelOffresComplet.csv | 12:06:55 | 187,416,011 | 30,858 | 4c4571a79af8404b75ab2bf55f086c68 |
| `canadabuys_data_dictionary.xml` | https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/achatscanada-canadabuys-dd.xml | 12:06:43 | 60,478 | 67 field headings | — |
| `canadabuys_contract_history_support_eng.html`, `canadabuys_notices_support_eng.html` | https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/COsoutien-CHsupport-eng.html, …/soutien-support-eng.html | 12:06:44 | 16,855 / 23,491 | — | — |
| `package_show_<id>.json` ×4 | https://open.canada.ca/data/api/3/action/package_show?id=… for d8f85d91…, 4fe645a1…, a1acb126…, 6abd20d4… | 12:05:5x | 17–41 KB | — | — |

Dataset landing pages: Proactive Publication – Contracts https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b (TBS; `metadata_modified` 2026-10-25T12:00:54; contracts.csv `last_modified` 2026-10-25T06:52); CanadaBuys contract history https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 (PSPC; complete file `last_modified` 2026-09-28); CanadaBuys award notices https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb (daily; 2026-10-24); CanadaBuys tender notices https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2 (daily; 2026-10-24).

Notes on the extra files: `contracts-nil.csv` lists (reporting_period, owner_org) pairs with nothing to report — no contract rows, kept only as context. `contractsa.csv` holds yearly aggregate counts/values of contracts ≤ $10K — no vendor-level rows, so nothing to extract. The "Legacy Data" file (2,470 rows, same columns plus `aboriginal_business*`, `record_created/modified`, `user_modified`) contains **0** rows with a Canadian vendor and delivery_date ≥ 2026-10-25, so it contributes nothing; it was checked and not used. The legacy CanadaBuys files (contract history 2009–2023-05, award notices 2012–2022-08, tender notices 2009–2022) were not downloaded: the task scoped CanadaBuys to the "complete" files, and any pre-2023 contract that is still running is captured by the proactive-disclosure file (reported since 2004).

All CSVs are UTF-8 with a BOM (read with `encoding="utf-8-sig"`); every file was processed with pandas in 100k-row chunks (`dtype=str, keep_default_na=False`).

## 3. Field semantics (from the schemas; confirmed on data)

**Proactive disclosure (`contracts.csv`, 43 columns).** From `contracts_schema.json`: `reference_number` = unique id of the *line item* (per organization; format `C-YYYY-YYYY-Qn-NNNNN`, with departmental variants); `procurement_id` = "recommended to be the contract number" (else commitment/requisition number); `contract_date` = award (or hard-commitment) date; `contract_period_start` = start of the service period / call-up window; `delivery_date` = "Contract Period End Date or Delivery Date" (= contract end); `contract_value` = total value incl. all amendments; `original_value`; `amendment_value` (value of *this* amendment row; multiple amendments in a quarter may be combined); `instrument_type` ∈ {C = contract or call-up, A = amendment, SOSA = standing offer / supply arrangement agreement}; `country_of_vendor` = ISO 3166 alpha-2 of the vendor's address in the contract; `vendor_postal_code` = first three characters (FSA) of the vendor postal code, "NA" if vendor outside Canada; `standing_offer_number` = SO/SA number the contract was issued against; `economic_object_code` (chart of accounts), `commodity_code` (GSIN), `commodity_type` ∈ {G,S,C}; `contracting_entity` ∈ {DC, DSOSA, OGDC, PWC, PWSOSA, SSCC, SSCSOSA}; `buyer_name` = contracting authority (a person); `reporting_period` = fiscal quarter in which the row was published; `owner_org` / `owner_org_title` = reporting organization. Code lists for `trade_agreement`, `land_claims`, `limited_tendering_reason`, `trade_agreement_exceptions`, `solicitation_procedure`, `award_criteria`, `intellectual_property`, etc. are in the schema and were used to label codes in the normalized layer (raw keeps the codes).

**CanadaBuys (data dictionary XML).** Contract history (91 cols) and award notices (80 cols) share: `referenceNumber` (internal id; CW#/WS#/ACM#), `solicitationNumber` (GETS solicitation id), `contractNumber` (= contract workspace CW# or legacy contract number `XXXXX-XXXXXX/001/XX`), `contractAwardDate`, `contractStartDate` ("date on which an awarded contract legally comes into effect"), `contractEndDate` ("last date on which an awarded contract is considered valid"), `contractAmount` (this row's amount), `totalContractValue` (cumulative), `amendmentNumber`, `amendmentDate`, `amendmentType` ∈ {Original, Amendment, Administrative amendment, Termination}, `instrumentType` ∈ {Contract, Contract against SA, Standing Offer, Supply Arrangement, Task Authorization Based Contract}, supplier legal/operating/standardized names, `supplierAddress{Line,City,Province,PostalCode,Country}`, contracting entity and end-user entity names/addresses, contact info. Contract history additionally has `procurementNumber` (WS#), `numberOfRecords`, `contractStatus` ∈ {Active, Cancelled, Expired}; award notices have `awardStatus` with the same values. Tender notices (67 cols) have `expectedContractStartDate/EndDate`, `tenderClosingDate`, `tenderStatus` ∈ {Open, Cancelled, Expired}, `noticeURL` (points at Ariba/MERX, *not* CanadaBuys). `supplierAddressCountry` is free text in award notices.

## 4. How "Canadian vendor" was determined

Proactive disclosure: `country_of_vendor` (ISO 3166-1 alpha-2). Distinct values seen over all 1,313,552 rows: 190 codes + blank; the top ones are `CA` 836,832 · blank 419,770 · `US` 28,868 · `GB` 4,506 · `DE` 2,029 · `FR` 1,559 · `MX` 735 · `JP` 717 · `CN` 716 · `IT` 639 · `IN` 627 … (full list in `scripts/canada_federal/logs/build_stats.json` → `pd_country_values`). **Only `CA` was mapped to Canada.** `NA` (7 rows) was *not* treated as "not applicable"/Canada — in ISO 3166 it is Namibia and the schema's code list confirms that; the field is otherwise clean (every value is an upper-case 2-letter code or blank). Among the 419,770 blank-country rows only 815 have a Canadian-looking postal code and **none** of those has a delivery date ≥ 2026-10-25 (the 92 blank-country live rows all have blank or `NA` postal codes and are almost all old rows with implausible end years like 2099/2201), so the agreed fallback rule — blank country + `vendor_postal_code` matching `A1A[ 1A1]` → `vendor.country_basis = "vendor_postal_code pattern (country_of_vendor blank)"` — is implemented but produced **0** records. For a contract with several rows the *latest* row's country decides; 9 records have a note in `country_basis` that an earlier row reported another country (e.g. US → CA after a vendor name change).

CanadaBuys contract history: `supplierAddressCountry-fournisseurAdressePays-eng/-fra`; values seen: `CA` 12,099 · `Canada` 649 · `US` 961 · `United States` 151 · `GB` 98 · … · blank 2 · `N/A` 1. Mapped to Canada: `CA`, `Canada`.

CanadaBuys award notices (free text): `CA` 16,253 · `Canada` 8,336 · `CANADA` 583 · `canada` 49 · `CAN` 21 · `Cananda` 4 · `Ca` 2 · `ca` 2 · `Canada.` 2 · `Canda` 1 · `Canana` 1 · `Canad` 1 — all mapped to Canada (after stripping spaces/punctuation, case-insensitive; the four typo forms were added explicitly). Not mapped: `US`/`USA`/`United States`/`UNITED STATES`/`United States of America`, `UK`/`GB`/`Great Britain`, `TÜRKIYE`, etc., and blank (1,022). Blank country + `supplierAddressPostalCode` matching the Canadian pattern → included with `country_basis = "supplierAddressPostalCode pattern (supplierAddressCountry blank)"` (706 records, all award notices). `vendor.country_basis` on every record names the field and value used.

## 5. How "ongoing" was determined

Reference date 2026-10-25. One record per contract; dates come from the **latest row** of the primary source (priority proactive disclosure > contract history > award notice).

- Proactive disclosure: end = `delivery_date`; start = `contract_period_start`, else `contract_date`. Rows sorted by reporting period (taken from `reporting_period`, or parsed from `reference_number` when `reporting_period` is malformed — 277,657 rows, mostly DND/ECCC/CRA, have values like `C`, `Q1`, blank), then `contract_date`, then `reference_number`.
- Contract history: end = `contractEndDate`; start = `contractStartDate`, else `contractAwardDate`; rows sorted by `amendmentNumber` (numeric, `T01`/`S01` last) then `publicationDate`.
- Award notices: end = `contractEndDate`; start = `contractStartDate`, else `contractAwardDate`.
- `ongoing` ⇔ end ≥ 2026-10-25 and start ≤ 2026-10-25. Excluded: end < 2026-10-25 (12,678 clusters), start > 2026-10-25 (121 clusters, e.g. contracts awarded in 2026 for a 2027 start — the schema's "ongoing" rule requires start ≤ today), contract history whose latest row is `amendmentType = Termination` or `contractStatus = Cancelled` (35), award notices with `awardStatus = Cancelled` when no other source confirms the contract (86; cancelled award rows are kept in `raw` and noted in `status_basis` when a matched source is live), and award rows whose supplier field is a cancellation note ("No contract awarded, requirement cancelled").
- `end_date_unknown` ⇔ no parseable end date in any matched source: 267 proactive-disclosure contracts (blank `delivery_date`; all with contract dates 2010–2018 — 235 of them CBSA 2016 — so most are very probably finished, but the source gives nothing usable) and 2,064 award notices with blank `contractEndDate` (1,223 awarded in 2022 and 600 in 2023, mostly legacy GETS-style notices; `awardStatus = Active` for all of them, but CanadaBuys appears not to maintain that status for legacy notices, so it was not used as evidence of ongoing).
- Award notices with `awardStatus = Expired` all have end < 2026-10-25, so they drop out on the date rule anyway. `contractStatus`/`awardStatus = Active` is recorded in `status_basis` but is **not** by itself sufficient (5,291 "Active" award notices have end dates in the past).
- 81 records have end years > 2100 (e.g. 2121-09-30, 2201-07-30, 9999-12-31); they satisfy the rule literally, are kept as `ongoing`, and `status_basis` carries "NOTE end date year > 2100 looks like a data-entry error". 1,231 records end in 2031 and 341 in 2036–2100, which is plausible for long-term leases, standing offers and supply arrangements.

`status_basis` on every record states the source, field, value and comparison used, e.g. `ongoing: proactive disclosure latest row delivery_date 2027-06-29 >= 2026-10-25 and proactive disclosure contract_period_start (else contract_date) 2017-06-30 <= 2026-10-25`.

## 6. Grouping rows into contracts

Proactive disclosure: rows are grouped per `owner_org` by normalized `procurement_id` (upper-case, whitespace removed). Degenerate ids (blank, `NULL`, `N/A`, `0`, `ACQUISITION CARD`, <3 chars …) fall back to the row's own `reference_number` (one row = one contract). 30,720 candidate groups (46,349 rows) were collected in a second pass so that *all* rows of a live contract — including old rows with past delivery dates and amendments — are under `raw.proactive_disclosure.rows` (chronological) and `raw.proactive_disclosure.row_urls`. Normalized values come from the latest row; `contract.value_detail` also carries `pd_original_value`, `pd_latest_amendment_value` and the sum of `amendment_value` over the rows. 63 groups contain vendor names that do not look alike (vendor name changes/assignments, e.g. IBM Canada → Kyndryl Canada, Veritaaq → Experis); they are kept as one contract because the department reports them under one procurement id, and all names are listed under `vendor.identifiers.pd_vendor_name_variants`. `dates.amended_last` for proactive disclosure is the last day of the reporting quarter of the latest amendment row (the file has no amendment date); `dates.amended_last_basis` says so.

Contract history: grouped by `referenceNumber` (= `contractNumber`, unique per contract; 14,196 contracts, up to 36 rows). Award notices: `referenceNumber` is unique per row (29,000 rows); rows that share solicitation + supplier + non-degenerate `contractNumber` are treated as versions of one award (28,939 groups).

## 7. Cross-source matching (dedup/merge)

Identifiers were normalized (upper-case, whitespace removed, and an alphanumeric-only form for comparison). Two passes over a union-find:

1. **Contract-level ids** — proactive `procurement_id` ↔ CanadaBuys `contractNumber`/`referenceNumber` (CW numbers or legacy `W8482-…/001/XX` numbers), and contract history ↔ award notice on `contractNumber`. Merge if the vendor names agree (share a distinctive token or a 10-char alphanumeric prefix; token distinctiveness is measured over all 55k distinct vendor names so words like INC, SERVICES, AUDIO, VISUAL, UNIVERSITY never count), **or** the id is a strong structured contract number (`CW#######`, `W8482-123456[/001/XX]`, `E60ZT-180025/…`) even if the names differ (39 pd–ch, 50 pd–an, 35 ch–an cases, e.g. "UNIVERSITE DU QUEBEC A MONTREAL" vs "Université du Québec à Montréal", "C-CORE" vs "C-COREBARTLETT BLDG…"), **or** — for weak numeric ids such as SAP PO numbers `3000805629` that collide across departments — the buyer agrees (proactive `owner_org` aliases vs CanadaBuys contracting/end-user entity) (68 pd–an, 1 pd–ch). 28 weak-id pairs with differing vendor *and* buyer were rejected.
2. **Solicitation-level ids** (WS numbers, `solicitationNumber`, `procurementNumber`, and proactive `procurement_id` values that are really solicitation numbers) are shared by *every* award under a standing offer / supply arrangement / multi-award RFP (one WS number spans up to 112 awards), so they are used only for nodes without a contract-level match, require strict vendor-name agreement (core token sets nest), and require a unique counterpart on both sides (14 merges; 143 rejections).

Result: 58,040 clusters, none containing two different contract-history contract numbers, and no cluster contains more than one proactive-disclosure group except `canada_federal:nserc-crsng:CW2445799`, where NSERC and SSHRC each reported the same CW2445799 Orangutech contract (identical vendor, dates, value) — emitted once with the second group under `raw.proactive_disclosure.additional_groups` and `contract.identifiers.pd_additional_groups`. `raw.merge.basis` lists the exact field/value/reason for every merge. 1,974 proactive-disclosure contracts were matched to CanadaBuys data; the low rate is expected: most departments report PO/commitment numbers in `procurement_id`, not PSPC contract numbers, and CanadaBuys contract history only covers PSPC-issued contracts from 2023-06.

**Known limitation:** two sources describing the same contract under different identifiers (e.g. a department's PO number vs PSPC's CW number) cannot be linked and appear as two records (one `canada_federal:<org>:…`, one `canada_federal:cb:…`). Conversely, CanadaBuys award notices sometimes publish several notices for one contract (e.g. `21301-27-5330518-01` and `-02` for Shaw Satellite, two notices per Mi Casa Rentals award with different contract numbers); these are kept as separate records because their contract numbers differ (62 such solicitation+supplier pairs, 148 records).

## 8. Record identity and URLs

- `record_id`: `canada_federal:<owner_org>:<procurement_id normalized>` for records with proactive-disclosure data (falls back to the latest `reference_number` when `procurement_id` is degenerate); `canada_federal:cb:<contract history referenceNumber>` or `canada_federal:cb:<award notice referenceNumber>` for CanadaBuys-only records. No collisions.
- `source.record_url` (proactive disclosure): `https://search.open.canada.ca/contracts/record/<owner_org>,<reference_number>` (comma may be literal or `%2C`; both verified). Discovered from the result links on https://search.open.canada.ca/contracts/ (`/contracts/record/cbsa-asfc%2CC-2025-2026-Q3-908`). Verified example: https://search.open.canada.ca/contracts/record/ssc-spc,C-2025-2026-Q4-00028 → HTTP 200, page titled "Contract Details: 2B0KB18078" showing Vendor Name "TELUS COMMUNICATIONS COMPANY", Contract Period End 2027-06-29, value $90,393,350.01 (saved as `downloads/canada_federal/record_test_1.html`). Also verified for `pwgsc-tpsgc,C-2024-2025-Q1-01779` (PARSONS INC), `csc-scc,C-2026-2027-Q1-00219`, and a reference number containing U+2011 non-breaking hyphens (`esdc-edsc,C-2025‑2026‑Q2‑00044`, percent-encoded) — all 200 with the right vendor. A non-existent reference returns 200 with an empty record page, so a 200 alone is not proof of existence. Note the portal only shows the *latest* row per reference; `raw.proactive_disclosure.row_urls` gives one URL per row.
- CanadaBuys notice URLs: `https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/<referenceNumber lower-cased>` and `…/award-notice/<referenceNumber lower-cased>`. Verified by fetching: tender `ws5938553031-doc5945464169` (200, h1 "W6890-270095 Playground Inspection", solicitation WS5938553031), tender `cb-50-83063359` (200), tender `mx-444085720081` (200), award `cw2437072` (200, Zetron Inc), award `cb-867-73443244` (200, PLAN GROUP INC.), award `mx-243100604603` (200, Habanero Consulting Inc.), award `pw-22-00998342-1009635` (200). The CanadaBuys site sits behind an Azure Application Gateway WAF that intermittently returns HTTP 403 to this client even for valid pages (the same URL gave 403 then 200 on retry), so unverifiable slug families were *not* given a URL: legacy references with `:`/`/` (`08112-220034:001:CZ`, `W8486-088630/001/BLB`, `E60ZT-180025:402:ZT` — 404 with `-`, `:` or `/` separators) and `SSC-26-00035000:T` / `PW-__ML-065-29485` tender references (404). Therefore `contract.related.tender_notice_url` is set for 8,553 of the 8,966 attached tender notices (missing for 238 `SSC-…:T` and 175 `PW-_XXX-…` legacy references) and `related.award_notice_url` only for `cb-`, `mx-`, `pw-NN-NNNNNNNN`, `cw` and `ws` reference families; CanadaBuys-only records built from legacy award references therefore have `record_url = null`. The tender notice's own `noticeURL` (Ariba / MERX) is kept as `related.tender_notice_external_url`.

## 9. Tender-notice enrichment

30,858 tender notices (2022-08-08 →). A notice is attached when the record's CanadaBuys `solicitationNumber`/`procurementNumber` (8,724 cases) or the proactive `procurement_id` (242 cases) equals a tender `solicitationNumber`. For the proactive route, weak ids (e.g. `P2500097`, which several small agencies reuse) are accepted only when the tender's contracting/end-user entity matches the reporting organization (48 strong-id + 194 buyer-agreement acceptances; 24 rejected). When a solicitation has several notice rows (amendments; up to 14), the latest row is `raw.related_tender_notice` and all rows are `raw.related_tender_notice_rows`. The match basis is in `contract.related.tender_notice_match_basis` and `raw.related_tender_notice_meta`.

## 10. Other decisions and ambiguities

- **Buyer naming.** For proactive-disclosure records `buyer.name` = English part of `owner_org_title`; `buyer.identifiers` keeps `owner_org`, the full bilingual title, `contracting_entity` (code + label) and the CanadaBuys entity names when matched; the contracting authority person (`buyer_name`) is in `buyer.contact.contracting_authority_name` (`NA` → null). For CanadaBuys-only records `buyer.name` = `endUserEntitiesName` (the client department), else `contractingEntityName` (usually PSPC). Six award notices have a person's name in `contractingEntityName` and no end user; they are labelled "Government of Canada organization (contact e-mail domain csc-scc.gc.ca)" / "(contracting officer Teri Fraser)" with `buyer.name_note` explaining. `buyer.type` is "crown corporation" (571 records: BDC, FCC, EDC, Canada Post, CDIC, Marine Atlantic, Bank of Canada, NCC, Canada Lands, VIA HFR, Telefilm, …) or "federal department or agency" by name pattern. No provincial/municipal buyers were found in the CanadaBuys complete files (the task anticipated some; the MX-prefixed MERX-sourced rows are all Crown corporations and Defence Construction Canada).
- **Instrument type.** Proactive disclosure has no direct field: records whose rows include an `SOSA` row → "standing offer / supply arrangement agreement"; rows with a `standing_offer_number` or a `*SOSA` contracting entity → "call-up / contract against standing offer or supply arrangement"; else "contract". CanadaBuys `instrumentType` is used directly for CanadaBuys-only records and always kept as `contract.canadabuys_instrument_type`. 4,030 records (legacy-style award notices) have no instrument type.
- **Values.** Proactive `contract_value` (CAD, taxes included) is preferred; otherwise CanadaBuys `totalContractValue` if non-zero, else `contractAmount`; `value_detail.value_source` says which. Standing offers/supply arrangements are legitimately $0.
- **Currency.** Proactive disclosure is CAD by policy; CanadaBuys has `contractCurrency` (all CAD in contract history; 621 USD / 41 EUR / … in award notices, but almost all of those are non-Canadian suppliers and are excluded).
- **Record size.** Records are at most 352 KB (mean 14 KB) because `raw` holds every row verbatim; the whole file is 596 MB.
- **Not done / gaps.** (a) Pre-2022 CanadaBuys legacy files were not pulled (see §2). (b) The proactive-disclosure source only lists contracts > $10K and amendments > $10K; smaller contracts are only in the aggregate file. (c) Departments' `country_of_vendor` is the country of the address *in the contract*; Canadian subsidiaries of foreign firms count as Canadian, foreign branches of Canadian firms do not. (d) `end_date_unknown` records with award dates ≤ 2018 are most likely finished; nothing in the sources says so, so they are kept as the schema requires. (e) Records with end dates after 2100 are kept but flagged in `status_basis`. (f) Buyer names for CanadaBuys-only records are not canonicalized across spellings.

## 11. Scripts and logs

`/home/claude/contracts/scripts/canada_federal/`: `download.sh` (all downloads, resume+retry), `profile_pd.py` / `profile_pd2.py` / `profile_cb.py` / `match_analysis.py` (profiling used to decide the rules; outputs in `logs/*.json`), `build.py` (the builder; writes the JSONL progressively, flushing every 5,000 records; `logs/build.log`, `logs/build_stats.json` with all counters, merge decisions, country value distributions and five sample records), `validate.py` (schema/date/URL checks; `logs/validate.json` — 0 issues), `probe_urls.sh` / `probe_urls2.sh` (URL verification; `logs/probe_urls.log`; fetched pages in `downloads/canada_federal/urlcheck/`).

## 12. Five sample records (`raw` summarized to its keys and row counts; long lists trimmed)

#### `canada_federal:ssc-spc:2B0KB18078`

raw keys: `{"proactive_disclosure": "21 row(s)"}`

```json
{
 "record_id": "canada_federal:ssc-spc:2B0KB18078",
 "source": {
  "key": "canada_federal",
  "name": "Proactive Publication – Contracts over $10,000",
  "publisher": "Treasury Board of Canada Secretariat / reporting federal organizations (open.canada.ca)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b",
  "dataset_urls": {
   "pd": "https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b"
  },
  "record_url": "https://search.open.canada.ca/contracts/record/ssc-spc,C-2026-2027-Q1-00022",
  "retrieved_at": "2026-10-25T12:07:44Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: proactive disclosure latest row delivery_date 2027-06-29 >= 2026-10-25 and proactive disclosure contract_period_start (else contract_date) 2017-06-30 <= 2026-10-25",
 "contract": {
  "identifiers": {
   "pd_owner_org": "ssc-spc",
   "pd_procurement_id": "2B0KB18078",
   "pd_reference_number_latest": "C-2026-2027-Q1-00022",
   "pd_reference_numbers": [
    "C-2017-2018-Q1-00618",
    "C-2023-2024-Q1-00425",
    "C-2023-2024-Q3-00525",
    "... (21 total)"
   ],
   "pd_standing_offer_number": "2B0KB18078"
  },
  "title": "Data Communications Services",
  "description": "This contract was competitively sourced through Traditional Competitive.\r\nThis contract includes one or more amendments.\r\nThis is a multi-year contract.",
  "instrument_type": "call-up / contract against standing offer or supply arrangement",
  "instrument_type_source_code": "Amendment",
  "solicitation_procedure": "Competitive – Traditional",
  "procurement_method": "Competitive – Traditional",
  "limited_tendering_reason": [
   "Goods purchased on a commodity market"
  ],
  "award_criteria": "Not applicable",
  "number_of_bids": 1,
  "trade_agreements": [
   "Canadian Free Trade Agreement",
   "Canada-Chile Free Trade Agreement",
   "Canada-Colombia Free Trade Agreement",
   "World Trade Organization – Agreement on Government Procurement",
   "Canada-Honduras Free Trade Agreement",
   "Canada-Korea Free Trade Agreement",
   "Canada-Panama Free Trade Agreement",
   "Canada-Peru Free Trade Agreement",
   "Canada-Ukraine Free Trade Agreement"
  ],
  "commodity": {
   "gsin": "D399B",
   "commodity_type": "Service",
   "economic_object_code": "231",
   "economic_object_description": "Data Communications Services"
  },
  "value": 95287363.11,
  "currency": "CAD",
  "value_detail": {
   "pd_total_contract_value": 95287363.11,
   "pd_original_value": 23814286.98,
   "pd_latest_amendment_value": 150503.1,
   "pd_sum_of_amendment_values_in_rows": 66107504.62,
   "value_source": "proactive disclosure contract_value (latest row)"
  },
  "dates": {
   "published": null,
   "signed": "2017-06-30",
   "start": "2017-06-30",
   "end": "2027-06-29",
   "amended_last": "2026-06-30",
   "amended_last_basis": "last day of the reporting quarter of the latest amendment row (proactive disclosure has no amendment date field)",
   "last_reported_period": "2026-2027-Q1",
   "first_reported_period": "2017-2018-Q1"
  },
  "related": {
   "parent_idv_id": "2B0KB18078",
   "proactive_disclosure_record_url": "https://search.open.canada.ca/contracts/record/ssc-spc,C-2026-2027-Q1-00022"
  }
 },
 "buyer": {
  "name": "Shared Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "owner_org": "ssc-spc",
   "owner_org_title": "Shared Services Canada | Services partagés Canada",
   "contracting_entity_code": "PWC",
   "contracting_entity": "Contract or Call-up awarded by PSPC on behalf of the client department.",
   "ministers_office": "No"
  },
  "address": {},
  "contact": {
   "contracting_authority_name": null
  }
 },
 "vendor": {
  "name": "TELUS COMMUNICATIONS COMPANY",
  "country": "CA",
  "country_basis": "country_of_vendor = 'CA' (latest row C-2026-2027-Q1-00022)",
  "identifiers": {
   "pd_vendor_name_latest": "TELUS COMMUNICATIONS COMPANY",
   "pd_former_public_servant": "No",
   "pd_indigenous_business": "None",
   "pd_indigenous_business_excluding_psib": "No"
  },
  "address": {
   "postal_code_fsa": "V6B",
   "country": "CA"
  },
  "contact": {}
 }
}
```

#### `canada_federal:cgc-ccg:CW2414933`

raw keys: `{"proactive_disclosure": "1 row(s)", "canadabuys_contract_history": "1 row(s)", "canadabuys_award_notice": "1 row(s)", "related_tender_notice": "dict", "related_tender_notice_meta": "dict", "merge": "dict"}`

```json
{
 "record_id": "canada_federal:cgc-ccg:CW2414933",
 "source": {
  "key": "canada_federal",
  "name": "Proactive Publication – Contracts over $10,000 + CanadaBuys contract history + CanadaBuys award notices (+ CanadaBuys tender notice)",
  "publisher": "Treasury Board of Canada Secretariat / reporting federal organizations (open.canada.ca); Public Services and Procurement Canada (CanadaBuys)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b",
  "dataset_urls": {
   "pd": "https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b",
   "ch": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
   "an": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
   "tn": "https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2"
  },
  "record_url": "https://search.open.canada.ca/contracts/record/cgc-ccg,C-2025-2026-Q4-00027",
  "retrieved_at": "2026-10-25T12:07:44Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: proactive disclosure latest row delivery_date 2027-04-30 >= 2026-10-25 and proactive disclosure contract_period_start (else contract_date) 2026-01-30 <= 2026-10-25",
 "contract": {
  "identifiers": {
   "pd_owner_org": "cgc-ccg",
   "pd_procurement_id": "CW2414933",
   "pd_reference_number_latest": "C-2025-2026-Q4-00027",
   "pd_reference_numbers": [
    "C-2025-2026-Q4-00027"
   ],
   "pd_standing_offer_number": null,
   "ch_reference_number": "CW2414933",
   "ch_contract_number": "CW2414933",
   "ch_procurement_number": "WS5316660815",
   "ch_solicitation_number": "WS5316660815",
   "an_reference_number_latest": "CW2414933",
   "an_reference_numbers": [
    "CW2414933"
   ],
   "an_contract_number": "CW2414933",
   "an_solicitation_number": "WS5316660815",
   "tn_reference_number": "WS5316660815-Doc5317787617",
   "tn_solicitation_number": "WS5316660815"
  },
  "title": "Printed matter, including books, newspapers, pictures, manuscripts and forms",
  "description": "The Canadian Grain Commission (CGC), Harvest Sample Program (HSP), requires the design, manufacture, printing, supply and delivery of 27,500 grain envelopes delivered by May 01, 2026.",
  "instrument_type": "contract",
  "instrument_type_source_code": "Contract",
  "solicitation_procedure": "Competitive – Open Bidding (GETS)",
  "procurement_method": "Competitive - Open bidding",
  "limited_tendering_reason": [
   "None"
  ],
  "award_criteria": "Highest Technical Merit within a Stipulated Maximum Budget",
  "number_of_bids": 2,
  "trade_agreements": [
   "Canadian Free Trade Agreement"
  ],
  "commodity": {
   "gsin": "N8105J",
   "commodity_type": "Good",
   "economic_object_code": "1143",
   "economic_object_description": "Printed matter, including books, newspapers, pictures, manuscripts and forms",
   "gsin_description": null,
   "unspsc": "44121500",
   "unspsc_description": "Mailing supplies",
   "procurement_category": "GD"
  },
  "value": 104383.13,
  "currency": "CAD",
  "value_detail": {
   "pd_total_contract_value": 104383.13,
   "pd_original_value": 104383.13,
   "pd_latest_amendment_value": 0.0,
   "pd_sum_of_amendment_values_in_rows": 0,
   "value_source": "proactive disclosure contract_value (latest row)",
   "ch_total_contract_value": 104383.13,
   "ch_latest_row_contract_amount": 104383.13,
   "ch_original_contract_amount": 104383.13,
   "ch_currency": "CAD",
   "ch_number_of_records": "1",
   "an_total_contract_value": 104383.13,
   "an_contract_amount": 104383.13,
   "an_currency": "CAD"
  },
  "dates": {
   "published": "2026-09-14",
   "signed": "2026-01-30",
   "start": "2026-01-30",
   "end": "2027-04-30",
   "amended_last": null,
   "amended_last_basis": null,
   "last_reported_period": "2025-2026-Q4",
   "first_reported_period": "2025-2026-Q4",
   "ch_end_date": "2027-04-30",
   "an_end_date": "2027-04-30"
  },
  "canadabuys_instrument_type": "Contract",
  "selection_criteria": "Lowest Price",
  "notice_type": "Request for Proposal",
  "related": {
   "proactive_disclosure_record_url": "https://search.open.canada.ca/contracts/record/cgc-ccg,C-2025-2026-Q4-00027",
   "regions_of_delivery": [
    "Manitoba"
   ],
   "award_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cw2414933",
   "tender_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/ws5316660815-doc5317787617",
   "tender_notice_external_url": "https://discovery.ariba.com/rfx/23462493?extsite=MjM0NjI0OTNfQU4wMTQ4NDA1MDk5Mg==",
   "tender_notice_match_basis": "CanadaBuys ch solicitation/procurement number matches tender solicitationNumber 'WS5316660815'",
   "tender_notice_status": "Expired",
   "tender_notice_closing_date": "2025-11-07T14:00:00"
  }
 },
 "buyer": {
  "name": "Canadian Grain Commission",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "owner_org": "cgc-ccg",
   "owner_org_title": "Canadian Grain Commission | Commission canadienne des grains",
   "contracting_entity_code": "PWC",
   "contracting_entity": "Contract or Call-up awarded by PSPC on behalf of the client department.",
   "ministers_office": "No",
   "canadabuys_contracting_entity": "Department of Public Works and Government Services (PSPC)",
   "canadabuys_end_user_entity": "Canadian Grain Commission (CGC)"
  },
  "address": {},
  "contact": {
   "contracting_authority_name": "Ramos, Gerlie"
  }
 },
 "vendor": {
  "name": "DATA COMMUNICATIONS MANAGEMENT",
  "country": "CA",
  "country_basis": "country_of_vendor = 'CA' (latest row C-2025-2026-Q4-00027)",
  "identifiers": {
   "pd_vendor_name_latest": "DATA COMMUNICATIONS MANAGEMENT",
   "pd_former_public_servant": "No",
   "pd_indigenous_business": "None",
   "pd_indigenous_business_excluding_psib": "No",
   "canadabuys_legal_name": "DATA COMMUNICATIONS MANAGEMENT CORP. GESTION DES COMMUNICAT IONS DATA CORP.",
   "canadabuys_operating_name": "DATA Communications Management",
   "canadabuys_standardized_name": "DCM"
  },
  "address": {
   "postal_code_fsa": "L6S",
   "line1": "9195 Torbram Rd",
   "city": "Brampton",
   "region": "Ontario",
   "postal_code": "L6S 6H2",
   "country": "CA"
  },
  "contact": {},
  "employee_count": "1601"
 }
}
```

#### `canada_federal:cb:21107-233006/001/QF`

raw keys: `{"canadabuys_contract_history": "1 row(s)", "canadabuys_award_notice": "1 row(s)", "related_tender_notice": "dict", "related_tender_notice_meta": "dict", "merge": "dict"}`

```json
{
 "record_id": "canada_federal:cb:21107-233006/001/QF",
 "source": {
  "key": "canada_federal",
  "name": "CanadaBuys contract history + CanadaBuys award notices (+ CanadaBuys tender notice)",
  "publisher": "Public Services and Procurement Canada (CanadaBuys)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
  "dataset_urls": {
   "ch": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
   "an": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
   "tn": "https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2"
  },
  "record_url": null,
  "retrieved_at": "2026-10-25T12:06:52Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: CanadaBuys contract history latest row contractEndDate 2027-02-06 >= 2026-10-25 and CanadaBuys contract history contractStartDate (else contractAwardDate) 2024-02-08 <= 2026-10-25; contractStatus blank",
 "contract": {
  "identifiers": {
   "ch_reference_number": "21107-233006/001/QF",
   "ch_contract_number": "21107-233006/001/QF",
   "ch_procurement_number": "21107-233006",
   "ch_solicitation_number": null,
   "an_reference_number_latest": "21107-233006:001:QF",
   "an_reference_numbers": [
    "21107-233006:001:QF"
   ],
   "an_contract_number": "21107-233006/001/QF",
   "an_solicitation_number": "21107-233006/B",
   "tn_reference_number": "PW-__QF-134-29249",
   "tn_solicitation_number": "21107-233006/B"
  },
  "title": "AGENCE GRAVEL INC (21107-233006/001/QF~000)",
  "description": "Trade Agreement: Canadian Free Trade Agreement (CFTA)\nComprehensive Land Claim Agreement: No\nNotification Method: Public Advertising\nContract Award Procedure (Procurement Strategy): Lowest/Lower Bid\nGSIN Description: \nOptical Sighting and R…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": "Lowest Price",
  "limited_tendering_reason": null,
  "trade_agreements": [
   "Canadian Free Trade Agreement (CFTA)"
  ],
  "commodity": {
   "gsin": "N1240",
   "gsin_description": "Optical Sighting and Ranging Equipment",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "GD"
  },
  "value_detail": {
   "ch_total_contract_value": 202722.0,
   "ch_latest_row_contract_amount": 202722.0,
   "ch_original_contract_amount": 202722.0,
   "ch_currency": "CAD",
   "ch_number_of_records": "1",
   "value_source": "CanadaBuys contract history totalContractValue (latest row)",
   "an_total_contract_value": null,
   "an_contract_amount": 202722.0,
   "an_currency": "CAD"
  },
  "value": 202722.0,
  "currency": "CAD",
  "dates": {
   "published": "2024-03-05",
   "signed": "2024-02-08",
   "start": "2024-02-08",
   "end": "2027-02-06",
   "amended_last": null,
   "ch_end_date": "2027-02-06",
   "an_end_date": null
  },
  "notice_type": null,
  "related": {
   "tender_notice_match_basis": "CanadaBuys an solicitation/procurement number matches tender solicitationNumber '21107-233006/B'",
   "tender_notice_status": "Expired",
   "tender_notice_closing_date": "2024-02-02T14:00:00"
  }
 },
 "buyer": {
  "name": "Correctional Service of Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_entity": "Correctional Service of Canada",
   "canadabuys_end_user_office": "PWGSC TB CONFERENCE INTERPRETN"
  },
  "address": {
   "line1": null,
   "city": null,
   "region": null,
   "postal_code": null,
   "country": null,
   "end_user_address": "5TH<br>975 ST JOSEPH BLVD,GATINEAU,Quebec,K1A0S5,Canada"
  },
  "contact": {
   "name": null,
   "email": null,
   "phone": null,
   "fax": null,
   "address": null
  }
 },
 "vendor": {
  "name": "AGENCE GRAVEL INC.",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'Canada'",
  "identifiers": {
   "canadabuys_legal_name": "AGENCE GRAVEL INC.",
   "canadabuys_operating_name": "AGENCE GRAVEL INC.",
   "canadabuys_standardized_name": "AGENCE GRAVEL INC"
  },
  "address": {
   "line1": "5175 John Molson",
   "city": "QUEBEC",
   "region": "Quebec",
   "postal_code": "G1X3X4",
   "country": "Canada"
  },
  "contact": {},
  "employee_count": "20 to 49 employees"
 }
}
```

#### `canada_federal:cb:01804-230555:001:HAL`

raw keys: `{"canadabuys_award_notice": "1 row(s)", "related_tender_notice": "dict", "related_tender_notice_meta": "dict"}`

```json
{
 "record_id": "canada_federal:cb:01804-230555:001:HAL",
 "source": {
  "key": "canada_federal",
  "name": "CanadaBuys award notices (+ CanadaBuys tender notice)",
  "publisher": "Public Services and Procurement Canada (CanadaBuys)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
  "dataset_urls": {
   "an": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
   "tn": "https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2"
  },
  "record_url": null,
  "retrieved_at": "2026-10-25T12:06:52Z"
 },
 "status": "end_date_unknown",
 "status_basis": "end_date_unknown: CanadaBuys award notice 01804-230555:001:HAL has blank contractEndDate; awardStatus Active; award date 2022-11-25",
 "contract": {
  "identifiers": {
   "an_reference_number_latest": "01804-230555:001:HAL",
   "an_reference_numbers": [
    "01804-230555:001:HAL"
   ],
   "an_contract_number": "01804-230555/001/HAL",
   "an_solicitation_number": "01804-230555/A",
   "tn_reference_number": "PW-_HAL-420-11576",
   "tn_solicitation_number": "01804-230555/A"
  },
  "title": "Irrigation Equipment",
  "description": "Trade Agreement: Canadian Free Trade Agreement (CFTA)\nComprehensive Land Claim Agreement: No\nNotification Method: Public Advertising\nContract Award Procedure (Procurement Strategy): Lowest/Lower Bid\nGSIN Description: \nPower and Hand Pumps\nQ…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Selective tendering",
  "solicitation_procedure": "Competitive - Selective tendering",
  "selection_criteria": "Lowest Price",
  "limited_tendering_reason": null,
  "trade_agreements": null,
  "notice_type": null,
  "commodity": {
   "gsin": "N4320",
   "gsin_description": "Power and Hand Pumps",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "GD"
  },
  "value_detail": {
   "an_total_contract_value": null,
   "an_contract_amount": 103617.12,
   "an_currency": "CAD",
   "value_source": "CanadaBuys award notice contractAmount"
  },
  "value": 103617.12,
  "currency": "CAD",
  "dates": {
   "published": "2022-11-28",
   "signed": "2022-11-25",
   "start": "2022-11-25",
   "end": null,
   "amended_last": null,
   "an_end_date": null
  },
  "related": {
   "tender_notice_match_basis": "CanadaBuys an solicitation/procurement number matches tender solicitationNumber '01804-230555/A'",
   "tender_notice_status": "Expired",
   "tender_notice_closing_date": "2022-11-03T13:00:00"
  }
 },
 "buyer": {
  "name": "Agriculture and Agri-Food Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_entity": "Agriculture and Agri-Food Canada",
   "canadabuys_end_user_office": null
  },
  "address": {
   "line1": "11 Laurier St, Phase III, Place du Portage",
   "city": "Gatineau",
   "region": "Quebec",
   "postal_code": "K1A 0S5",
   "country": "Canada",
   "end_user_address": "1341 Baseline Road,Ottawa,Ontario,K1A0C5,Canada"
  },
  "contact": {
   "name": "AGRICULTURE AND AGRI-FOOD CANADA",
   "email": null,
   "phone": null,
   "fax": null,
   "address": "RESEARCH STN KENTVILLE NS B4N1J5 CAN"
  }
 },
 "vendor": {
  "name": "DUBOIS AGRINOVATION INC.",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'Canada'",
  "identifiers": {
   "canadabuys_legal_name": "DUBOIS AGRINOVATION INC."
  },
  "address": {
   "line1": "478 Notre-Dame<br>BP 3550",
   "city": "St-Remi",
   "region": "Quebec",
   "postal_code": "J0L2L0",
   "country": "Canada"
  },
  "contact": {}
 }
}
```

#### `canada_federal:cb:cb-94-49080121`

raw keys: `{"canadabuys_award_notice": "1 row(s)", "related_tender_notice": "dict", "related_tender_notice_meta": "dict"}`

```json
{
 "record_id": "canada_federal:cb:cb-94-49080121",
 "source": {
  "key": "canada_federal",
  "name": "CanadaBuys award notices (+ CanadaBuys tender notice)",
  "publisher": "Public Services and Procurement Canada (CanadaBuys)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
  "dataset_urls": {
   "an": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
   "tn": "https://open.canada.ca/data/en/dataset/6abd20d4-7a1c-4b38-baa2-9525d0bb2fd2"
  },
  "record_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-94-49080121",
  "retrieved_at": "2026-10-25T12:06:52Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: CanadaBuys award notice latest row contractEndDate 2029-07-31 >= 2026-10-25 and CanadaBuys award notice contractStartDate (else contractAwardDate) 2026-08-01 <= 2026-10-25; awardStatus Active",
 "contract": {
  "identifiers": {
   "an_reference_number_latest": "cb-94-49080121",
   "an_reference_numbers": [
    "cb-94-49080121"
   ],
   "an_contract_number": "21301-27-5330518-01",
   "an_solicitation_number": "21301-27-5330518",
   "tn_reference_number": "cb-928-82292696",
   "tn_solicitation_number": "21301-27-5330518"
  },
  "title": "Cable or Relay Television Distribution Service",
  "description": "21301-27-5330518_Cable or Relay Television Distribution Service - FTC600\r\n\r\nThis requirement is for: The Correctional Service of Canada for the following institutions within the Quebec Region: \r\n\r\nFederal Training Centre (Min)\r\nFederal Trai…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": "Lowest Price",
  "limited_tendering_reason": null,
  "trade_agreements": [
   "None"
  ],
  "notice_type": "Request for Proposal",
  "commodity": {
   "gsin": null,
   "gsin_description": null,
   "unspsc": "72151601 | 83111800 | 83111801",
   "unspsc_description": "Cable television installation service | Television services | Cable television services",
   "procurement_category": "SRV"
  },
  "value_detail": {
   "an_total_contract_value": 176990.68,
   "an_contract_amount": 0.0,
   "an_currency": "CAD",
   "value_source": "CanadaBuys award notice totalContractValue"
  },
  "value": 176990.68,
  "currency": "CAD",
  "dates": {
   "published": "2026-08-18",
   "signed": "2026-08-01",
   "start": "2026-08-01",
   "end": "2029-07-31",
   "amended_last": null,
   "an_end_date": "2029-07-31"
  },
  "related": {
   "award_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/cb-94-49080121",
   "regions_of_delivery": [
    "Quebec (except NCR)"
   ],
   "tender_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/tender-notice/cb-928-82292696",
   "tender_notice_match_basis": "CanadaBuys an solicitation/procurement number matches tender solicitationNumber '21301-27-5330518'",
   "tender_notice_status": "Expired",
   "tender_notice_closing_date": "2026-04-21T14:00:00"
  }
 },
 "buyer": {
  "name": "Correctional Service of Canada (CSC)",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Correctional Service of Canada (CSC)",
   "canadabuys_end_user_entity": null,
   "canadabuys_end_user_office": null
  },
  "address": {
   "line1": "250 Montée St-François",
   "city": "Laval",
   "region": "Québec",
   "postal_code": "H7C 1S5",
   "country": "Canada",
   "end_user_address": null
  },
  "contact": {
   "name": "Eloïse Clément",
   "email": "eloise.clement@csc-scc.gc.ca",
   "phone": "(450) 506-2965",
   "fax": null,
   "address": "250 Montée St-François Laval Québec H7C 1S5 Canada"
  }
 },
 "vendor": {
  "name": "Shaw Satellite Services Inc.",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'Canada'",
  "identifiers": {
   "canadabuys_legal_name": "Shaw Satellite Services Inc."
  },
  "address": {
   "line1": "Suite 100, 2400 32 nd Avenue NE",
   "city": "Calgary",
   "region": "Alberta",
   "postal_code": "T2E9A7",
   "country": "Canada"
  },
  "contact": {}
 }
}
```

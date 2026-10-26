# ted_eu — TED (Tenders Electronic Daily, EU/EEA) contract awards to Canadian suppliers

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/ted_eu.jsonl` (584 records, one per notice × Canadian contractor/tender; 538 distinct notices). Scripts in `/home/claude/contracts/scripts/ted_eu/`, downloads in `/home/claude/contracts/downloads/ted_eu/`.

## What was downloaded (all retrieved 2026-10-25, 12:06–13:11 UTC)

| Source | URL | What | Size / rows |
|---|---|---|---|
| TED API spec | https://api.ted.europa.eu/api-v3.yaml | OpenAPI 3 spec; `PublicExpertSearchRequestV1` + `NoticeResponse` (1 830 retrievable field names, saved to `notice_response_fields.json`) | 456 KB |
| TED Search API | `POST https://api.ted.europa.eu/v3/notices/search` | eForms-era notices, query `(winner-country=CAN OR organisation-country-tenderer=CAN OR organisation-country-subcontractor=CAN)`, scope ALL, ITERATION mode, **all 1 830 fields** requested (5 notices/page to stay under the 10 000 fields/page limit) | 280 notices → `api_eforms/*.json` (12 MB) |
| TED Search API | same endpoint, `ND IN (...)` batches of 5 | legacy-schema notices identified via CSV (below), all fields | 557 of 647 found → `api_legacy/*.json`; 90 (47×2015, 43×early-2016) are not in the API index (index starts late 2016) → `_missing.json` |
| data.europa.eu TED CSV | https://data.europa.eu/api/hub/store/data/ted-contract-award-notices-{2015,2016,2017,2018-2023}.zip (301 → `/data-management/store/api/legacy/data/...`) | open-data CAN (contract award notice) CSV export; filtered on `WIN_COUNTRY_CODE` containing `CA` | 47 MB / 553 204 rows (49 CA rows); 47 MB / 556 084 (58); 63 MB / 702 825 (74); 560 MB / 6 198 063 (535) → 716 award rows, 647 distinct notices |
| data.europa.eu TED CSV | ted-contract-notices-{2013,2014,2015,2016,2017,2018-2023}.zip | contract-notice (CFC) CSV, rows whose `FUTURE_CAN_ID` is one of our 647 award notices (gives `DURATION`, `CONTRACT_START`, `CONTRACT_COMPLETION`) | 1 436 CN rows for 403 award notices |
| TED daily packages | https://ted.europa.eu/packages/daily/<yyyy><nnnnn> (nnnnn = zero-padded OJ S issue; e.g. OJ 177/2023 → 202300177) | tar.gz of every notice XML of the issue; only wanted XMLs extracted, tarball deleted | eForms: 229 packages / 3.97 GB → 280 XML; legacy: 451+65 packages / 4.26 GB → 557 XML; plus 168 packages probed by binary search over notice numbers for the 90 pre-index notices → 83 XML (all 90 found: 647/647 legacy XML) |

The TED website itself (https://ted.europa.eu/en/notice/... HTML/XML/PDF links) is behind an AWS WAF JavaScript challenge (HTTP 202, `x-amzn-waf-action: challenge`) for scripted clients, so per-notice XML was taken from the daily packages instead. The CSV exports end 31-12-2023 (no further updates planned by DG GROW); eForms (Nov-2023 →) coverage comes from the API.

## How "Canadian vendor" was determined
* eForms (2023-11 → 2026): API field `winner-country = CAN` (ISO-3166 alpha-3 in the eForms `country` codelist; `CA`/`Canada` are rejected by the API) OR `organisation-country-tenderer = CAN`. In the XML the record is built per **winning tender** (`efac:LotResult/cbc:TenderResultCode = selec-w`) whose `efac:TenderingParty/efac:Tenderer` organization has `efac:Company/cac:PostalAddress/cac:Country/cbc:IdentificationCode = CAN` (BT-514). One notice (76538-2026) where the Canadian firm is only a subcontractor (BT-514-Organization-Company under `efac:SubContractor`) is excluded and listed in `normalize_stats.json`.
* Legacy (2015 → 2023): open-data CSV `WIN_COUNTRY_CODE` (alpha-2, `---`-separated for joint awards) contains `CA`; then confirmed in the notice XML: `AWARD_CONTRACT/AWARDED_CONTRACT/CONTRACTORS/CONTRACTOR/ADDRESS_CONTRACTOR/COUNTRY@VALUE = CA` (R2.0.9 F03/F06/F21), `.../AWARDED_CONTRACT/CONTRACTOR/...` (R2.0.9.S01 2016-17 layout), or `ECONOMIC_OPERATOR_NAME_ADDRESS/.../COUNTRY@VALUE = CA` / `CONTACT_DATA_WITHOUT_RESPONSIBLE_NAME_CHP` (R2.0.8 CONTRACT_AWARD / _UTILITIES / _DEFENCE forms). Group awards (e.g. "Candu Energy – Canadian Commercial Corporation", FR/CA consortia) are kept when at least one member is in Canada; `vendor.group_members` lists all members.
* Full-text sanity check: `FT=Canada AND TD=7` (1 837 legacy award notices mentioning Canada) was not used as a filter — most are buyers mentioning Canada as place of performance; the structured country code is authoritative.

## How "ongoing" was determined
* eForms: lot `cac:PlannedPeriod` `StartDate` (BT-536) / `EndDate` (BT-537) → `ongoing` when end ≥ 2026-10-25 and start (or `SettledContract/AwardDate`, BT-145) ≤ today. Else `DurationMeasure` (BT-36, MONTH/YEAR/DAY/WEEK) added to the start date, or to the contract AwardDate when no start → `ongoing_inferred` (computation written in `status_basis`). Else `end_date_unknown`.
* Legacy: `OBJECT_DESCR/DURATION|DATE_START|DATE_END` of the awarded lot in the CAN XML when present; otherwise the linked contract notice's CSV columns `CONTRACT_COMPLETION` (explicit end → `ongoing`) or `DURATION` (months) + `CONTRACT_START`, added to the award `DATE_CONCLUSION_CONTRACT` (→ `ongoing_inferred`). `end_date_unknown` when neither exists (most legacy F03 award notices do not restate duration).
* Excluded (459, listed in `downloads/ted_eu/normalize_stats.json`): computed/explicit end < 2026-10-25 (457), lot result `clos-nw` (1), subcontractor-only (1). `veat` (voluntary ex-ante transparency) and `can-modif` (modification) notices are kept and flagged in `status_basis`/`raw.search_api_notice.notice-type`.

## Counts
| status | records |
|---|---|
| ongoing | 28 |
| ongoing_inferred | 103 |
| end_date_unknown | 453 |
| **total** | **584** (538 notices; 268 eForms-schema, 316 legacy-schema) |

By publication year: 2015 29, 2016 37, 2017 35, 2018 27, 2019 27, 2020 33, 2021 31, 2022 48, 2023 52, 2024 73, 2025 86, 2026 105. Buyer countries: DE 103, FR 75, RO 52, GB 45, IE 42, DK 42, NL 33, SE 23, ES 19, IT 16, NO 15, BE 15, HR 14, FI 14, EE 12, CZ 10, AT 9, PT 7, CH 6, … (29 countries; EU institutions appear as their seat country).

## record_url
`https://ted.europa.eu/en/notice/-/detail/<publication-number>` — verified: https://ted.europa.eu/en/notice/-/detail/553483-2023 returns HTTP 200 `<title>553483-2023 - Result - TED</title>` with a browser User-Agent (scripted UAs get the WAF 202 challenge page). `contract.related` also carries `/xml` and `/pdf` links and, for legacy notices, the original `ted.europa.eu/udl?uri=TED:NOTICE:<n>-<yyyy>:TEXT:EN:HTML` URL and the linked contract-notice URLs.

## raw layer
`raw.search_api_notice` = every field the Search API returns for the notice (legacy notices: ~60 coded fields; eForms: 200+ incl. all BT-xxx), `raw.notice_xml` = parsed notice XML (organizations, lots, lot results, tenders, settled contracts, tendering parties, contract modifications for eForms; coded data section + full ORIGINAL form as a dict for legacy), `raw.opendata_csv_award_rows` (all 76 CSV columns), `raw.opendata_csv_contract_notice_rows`, plus `matched_*` pointers to the exact lot/tender/contract the record describes.

## Known gaps / limits
* Legacy notices rarely state duration; 453 records are `end_date_unknown`, of which many (2015-2019 awards) are probably finished — kept per the schema rule, flagged.
* Values: `contract.value` is the tender/award amount in notice currency; some buyers publish `1` or `0` placeholders (kept verbatim; `value_detail` carries estimated/notice totals and the open-data EUR conversions).
* The TED Search API index starts with OJ S of late 2016; 2015/early-2016 notices come only from the CSV + XML packages (API fields null for them). Notices before 2015 were out of scope.
* Multi-lot legacy notices where the Canadian firm won one lot: duration fallback uses the contract-notice row of the same `ID_LOT` when available, otherwise only when all CN rows agree.
* `buyer.type` uses the eForms `buyer-legal-type` codelist or legacy `AA_AUTHORITY_TYPE` code (decoded); EU institutions carry their seat country code.

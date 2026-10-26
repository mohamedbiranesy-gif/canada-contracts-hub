# canada_federal_legacy — CanadaBuys legacy contract history (2009-01→2023-05) and legacy award notices (2012→2022-08)

Source key: `canada_federal_legacy` · Outputs:
- `/home/claude/contracts/normalized/canada_federal_legacy.jsonl`: **12,668 records** (md5 `c96f3b3d44d0853a07eefe2b04833dfa`)
- `/home/claude/contracts/normalized/canada_federal_legacy_buyer_unidentified.jsonl`: 154 records where the notice names no buyer organization (W1 rule: named buyer required, so they are kept apart)

Built 2026-10-26 03:30 UTC by `/home/claude/contracts/scripts/canada_federal_legacy/build.py` (logs, stats and profiles in `scripts/canada_federal_legacy/logs/`). This is workstream W1a. It extends `canada_federal` and does not repeat it.

## 1. Result

| status | records |
|---|---|
| `ongoing` | 2,847 |
| `end_date_unknown` | 9,821 |
| `ongoing_inferred` | 0 |
| **total** | **12,668** (all `vendor.country = CA`) |

By file combination:

| source of the record | ongoing | end_date_unknown |
|---|---|---|
| legacy contract history + legacy award notice(s) | 2,618 | 1,523 |
| legacy contract history only | 227 | 863 |
| legacy award notices only | 2 | 7,435 |

Instrument types (CanadaBuys `instrumentType`): supply arrangement 1,582 · standing offer 148 · contract 238 · task-authorization contract 52 · contract against SA 20 · blank 10,628 (legacy rows mostly leave it blank). End years of the `ongoing` records: 2026 141 · 2027 453 · 2028 1,362 · 2029 151 · 2030 493 · 2031 121 · 2032–2099 126. Distinct buyer spellings: 117 (top: PWGSC 5,207, "Department of Public Works and Government Services (PSPC)" 1,839, DND 1,143, Parks Canada 907, AAFC 540, RCMP 471, CSC 306). PWGSC as buyer usually means a government-wide instrument (supply arrangement/standing offer) run by PSPC.

## 2. Downloads (2026-10-26 UTC, curl `-L -C -`, UA `contracts-research/1.0`; `downloads/canada_federal_legacy/download.log`)

| file (`downloads/canada_federal_legacy/`) | URL | retrieved | bytes (uncompressed) | rows | md5 (before gzip) |
|---|---|---|---|---|---|
| `2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv(.gz)` | https://canadabuys.canada.ca/opendata/pub/2009-2023-contractHistoryHistorical-contratsOctroyesHistorique.csv | 02:59:40Z | 833,518,040 | 486,151 (210,543 contracts by `referenceNumber`) | 74674fff14604ccf6d74f7ca1e6472d0 |
| `2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv(.gz)` | https://canadabuys.canada.ca/opendata/pub/2012-2022-awardNoticeHistorical-avisAttributionHistorique.csv | 02:59:50Z | 270,567,716 | 106,416 (106,261 notice groups) | cd32da05f9148e03fe6b5f3a00622cf4 |

Datasets: CanadaBuys contract history https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4 (resource "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)") and CanadaBuys award notices https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb (resource "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"). Same column layout as the "complete" files used by `canada_federal` (bilingual headers, data dictionary `downloads/canada_federal/canadabuys_data_dictionary.xml`). Both files were gzipped after the build (2026-10-26 04:36Z); the scripts read `.csv` or `.csv.gz`.

## 3. Canadian vendor
`supplierAddressCountry-fournisseurAdressePays-eng`, case/space/punctuation-normalised. Values mapped to Canada: `Canada`, `CA`, `CANADA`, `CAN`, plus the typo forms seen in `canada_federal` (`Canda`, `Cananda`, `Canana`, `Canad`). When the country is blank, a Canadian postal-code pattern in `supplierAddressPostalCode` is accepted (`country_basis` says so). Values seen: contract history `Canada` 421,887 · `United States` 34,757 · `CA` 16,992 · `Germany` 3,429 · `United Kingdom` 2,788 …; award notices `Canada` 76,773 · blank 12,162 · `United States` 7,921 · `CA` 5,611 … (full lists in `logs/profile_ch.json`, `logs/profile_an.json`). Non-Canadian suppliers excluded: 27,341 contract-history contracts, 15,138 award-notice groups. `vendor.country_basis` gives the field and value on every record.

## 4. Ongoing / status logic (reference 2026-10-25)
- Contract history (CHL): latest row per `referenceNumber` (sort: `amendmentNumber` numeric, then `publicationDate`). `ongoing` ⇔ `contractEndDate` ≥ 2026-10-25 and `contractStartDate` (else `contractAwardDate`) ≤ 2026-10-25. Excluded: latest row `amendmentType = Termination` (53), `contractStatus = Cancelled`, end < ref (176,720), future start.
- **Placeholder end dates**: CHL uses `2100-…` (8,168 Canadian rows) and other years ≥ 2100 (`9999`, `2121`, `3014` …) for open-ended instruments. These are treated as *not a usable end date* → `end_date_unknown`, and `status_basis` says "placeholder value (year >= 2100 …)". `dates.end` is then null and the original stays in `raw`.
- Award notices (ANL): rows that share solicitation + supplier + contract number are treated as one award (latest row decides). `awardStatus = Cancelled` (338), Termination (56) and supplier fields that are cancellation notes (8) are excluded. End blank → `end_date_unknown` (85,529 groups, before dedupe). The legacy notices almost never carry an end date: of the Canadian groups with blank end, award years are 2012–2022, roughly 6–10k per year.
- An ANL group linked to a CHL contract (same contract number, vendor names agreeing) is resolved by the CHL contract's dates: 71,215 ANL groups were dropped because their CHL contract ended. 4,127 ANL candidates were merged into CHL candidates as `raw.legacy_award_notice_rows`.

## 5. De-duplication against existing data (drop rules, in order)
1. **Already in `canada_federal`**: compact id index of `normalized/canada_federal.jsonl` (`scripts/canada_federal_legacy/index_existing.py` → `work/canada_federal_legacy/cf_index.jsonl.gz`; contract-level ids only: pd_procurement_id, pd_reference_numbers, ch/an reference + contract numbers). A legacy unit is a duplicate when an identifier matches (alphanumeric-normalised) **and** either the vendor names agree (distinctive shared token / 10-char prefix) or the id is a strong structured contract number (`W8482-123456/001/XX`, `CW#######` …): **1,207 dropped** (1,104 CHL, 103 ANL). 59 id matches were rejected because the vendors differ.
2. **Superseded by the CanadaBuys complete files** (same contract number + vendor in contractHistoryComplete / awardNoticeComplete, newer data): 69 dropped (61 CHL, 8 ANL).
3. **Proactive disclosure says the contract ended**: the unit's contract number equals a PD `procurement_id` (vendor agreeing), and the latest PD row's `delivery_date` < ref: 4,628 dropped. Exception: 50 cases where the legacy row is newer than the PD report, so the legacy end date is kept and the PD row is cited in `status_basis`. Also dropped: PD reports a non-Canadian vendor (2), and PD says the contract is live but it is not in canada_federal (1, which avoids a duplicate).
4. ANL-only groups whose buyer cannot be identified (no contracting or end-user entity, or a person's name only) → `_buyer_unidentified.jsonl` (154).

Survivors: 12,822 units, minus the 154 with an unidentified buyer, = 12,668 records.

## 6. Record identity, URL, fields
- `record_id`: `canada_federal_legacy:<CHL referenceNumber>` for contract-history units, `canada_federal_legacy:an:<ANL referenceNumber>` for award-notice-only units.
- `source.record_url`: the CanadaBuys award-notice page `https://canadabuys.canada.ca/en/tender-opportunities/award-notice/<referenceNumber lower-cased>`. It is set only for the reference families verified in `canada_federal` (`cw…`, `pw-NN-NNNNNNNN…`, `cb-`, `mx-`, `ws`), which gives 5,082 records. Legacy references with `/` or `:` have no URL (7,586). Verified 2026-10-26 03:25Z: `…/award-notice/cw2226597` (HTTP 200, shows "12941139 Canada Ltd.") and `…/award-notice/pw-13-00123476` (HTTP 200). Saved in `downloads/canada_federal_legacy/urlcheck/`.
- Normalized layer: same field mapping as `canada_federal` (title, description, GSIN/UNSPSC, procurement method, trade agreements, `totalContractValue` else `contractAmount`, CAD, award/start/end/amendment dates, supplier legal/operating/standardized names and full address, contracting and end-user entity with address and contact). `raw` keeps **every row verbatim**: `legacy_contract_history_rows` (all amendments), `legacy_award_notice_rows`, plus PD match notes and merge bases.

## 7. Known gaps / caveats
- 9,821 `end_date_unknown` records are mostly 2012–2022 award notices without an end date (the legacy notice format had no end-date field). Many are probably finished, but the source gives nothing usable, so they are kept as the schema requires. Downstream users should treat them as low confidence.
- Buyer names are not canonicalised (e.g. "Public Works and Government Services Canada" vs "Department of Public Works and Government Services (PSPC)").
- A legacy contract reported in PD under a departmental PO number (not the PSPC contract number) cannot be linked. If it is live in PD it may appear twice (once here, once in `canada_federal`). The id-based dedupe only catches shared contract numbers.
- Legacy tender notices (2009–2022) were not used: they hold no supplier information.

## 8. Five sample records (raw summarized; long strings trimmed)

#### `canada_federal_legacy:CW2229830` (ongoing; CHL + ANL; DND; United Rotary Brush Corporation, Barrie ON; 2022-01-21 → 2027-01-20)
#### `canada_federal_legacy:CW2226597` (ongoing; 12941139 Canada Ltd., Mount Pearl NL; 2022-01-14 → 2027-01-14; URL verified)
#### `canada_federal_legacy:CW2231064` (ongoing; Nitam Solutions Inc, Ottawa; ECCC; 2022-05-25 → 2032-05-25)
#### `canada_federal_legacy:an:PW-13-00123476` (end_date_unknown; legacy award notice; URL verified)
#### `canada_federal_legacy:EN578-172870/018/ZN` (supply arrangement; see build_stats samples)

Full JSON of five spread-out records (generated by `scripts/w1_common/samples.py`):

#### `canada_federal_legacy:EN439-202866/001/PQ`

raw keys: `{"canadabuys_legacy_contract_history": "dict", "canadabuys_legacy_award_notice": "dict", "dedupe_checks": "dict"}`

```json
{
 "record_id": "canada_federal_legacy:EN439-202866/001/PQ",
 "source": {
  "key": "canada_federal_legacy",
  "name": "CanadaBuys legacy contract history 2009-01 to 2023-05 + legacy award notices 2012-2022",
  "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
  "record_url": null,
  "retrieved_at": "2026-10-26T02:59:40Z",
  "resource_names": [
   "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)",
   "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"
  ]
 },
 "status": "ongoing",
 "status_basis": "ongoing: CanadaBuys legacy contract history latest row (amendment 001) contractEndDate 2030-06-18 >= 2026-10-25 and contractStartDate (else contractAwardDate…",
 "contract": {
  "identifiers": {
   "ch_reference_number": "EN439-202866/001/PQ",
   "ch_contract_number": "EN439-202866/001/PQ",
   "ch_procurement_number": "EN439-202866",
   "ch_solicitation_number": null,
   "ch_amendment_numbers": [
    "000",
    "001"
   ],
   "an_reference_numbers": [
    "EN439-202866:001:PQ"
   ],
   "an_contract_number": "EN439-202866/001/PQ",
   "an_solicitation_number": "EN439-202866/A"
  },
  "title": "CAPITAL OFFICE INTERIORS LTD (EN439-202866/001/PQ~001)",
  "description": "Trade Agreement: NAFTA / CFTA / FTAs with Peru / Colombia / Panama / Korea\nComprehensive Land Claim Agreement: No\nNotification Method: Public Advertising\nCon…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": "Lowest Price",
  "limited_tendering_reason": null,
  "trade_agreements": [
   "Canada-Chile Free Trade Agreement (CCFTA)",
   "Other trade agreements not listed here may apply",
   "Canada-Colombia Free Trade Agreement",
   "Canada-Peru Free Trade Agreement (CPFTA)",
   "... (6 total)"
  ],
  "notice_type": null,
  "commodity": {
   "gsin": "N7110",
   "gsin_all": "N7110",
   "gsin_description": "Office Furniture",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "GD"
  },
  "value": 162375.0,
  "currency": "CAD",
  "value_detail": {
   "ch_total_contract_value": 162375.0,
   "ch_latest_row_contract_amount": 4273.0,
   "ch_original_contract_amount": 158102.0,
   "ch_number_of_records": "2",
   "value_source": "CanadaBuys legacy contract history totalContractValue (latest row)",
   "an_contract_amount": 158101.8,
   "an_total_contract_value": null
  },
  "dates": {
   "published": "2020-06-19",
   "signed": "2020-06-18",
   "start": "2020-06-18",
   "end": "2030-06-18",
   "amended_last": "2020-07-31"
  },
  "related": {
   "anl_chl_link_basis": [
    "ANL contractNumber 'EN439-202866/001/PQ' = CHL contract 'EN439-202866/001/PQ'"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_office": "OFFICE ACCOMMODATION SERV."
  },
  "address": {
   "line1": null,
   "city": null,
   "region": null,
   "postal_code": null,
   "country": null,
   "end_user_address": "TERRASSES DE LA CHAUDIERE<br>25 EDDY ST RM 226,Gatineau,Quebec,K1A0M5,Canada"
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
  "name": "Capital Office Interiors Ltd",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'Canada' (CanadaBuys legacy contract history latest row, amendment 001)",
  "identifiers": {
   "canadabuys_legal_name": "Capital Office Interiors Ltd",
   "canadabuys_operating_name": "Capital Office Interiors Ltd",
   "canadabuys_standardized_name": "CAPITAL OFFICE INTERIORS LTD"
  },
  "address": {
   "line1": "16 Antares Drive",
   "city": "Nepean",
   "region": "Ontario",
   "postal_code": "K2E7Y7",
   "country": "Canada"
  },
  "contact": {},
  "employee_count": "20 to 49 employees"
 }
}
```

#### `canada_federal_legacy:EN578-170432/318/EI`

raw keys: `{"canadabuys_legacy_contract_history": "dict", "canadabuys_legacy_award_notice": "dict", "dedupe_checks": "dict"}`

```json
{
 "record_id": "canada_federal_legacy:EN578-170432/318/EI",
 "source": {
  "key": "canada_federal_legacy",
  "name": "CanadaBuys legacy contract history 2009-01 to 2023-05 + legacy award notices 2012-2022",
  "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
  "record_url": null,
  "retrieved_at": "2026-10-26T02:59:40Z",
  "resource_names": [
   "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)",
   "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"
  ]
 },
 "status": "end_date_unknown",
 "status_basis": "end_date_unknown: CanadaBuys legacy contract history latest row (amendment 001) contractEndDate 2100-01-31 is a placeholder value (year >= 2100, used for ope…",
 "contract": {
  "identifiers": {
   "ch_reference_number": "EN578-170432/318/EI",
   "ch_contract_number": "EN578-170432/318/EI",
   "ch_procurement_number": "EN578-170432",
   "ch_solicitation_number": null,
   "ch_amendment_numbers": [
    "001"
   ],
   "an_reference_numbers": [
    "EN578-170432:318:EI"
   ],
   "an_contract_number": "EN578-170432/318/EI",
   "an_solicitation_number": "EN578-170432/A"
  },
  "title": "CONFLUENCE CONSULTING INC IN JOINT VENTURE WITH CORPORATE RENAISSANCE GROUP INC (EN578-170432/318/EI~001)",
  "description": "Trade Agreement: NAFTA/AIT/Canada FTAs with Peru/Colombia/Panama\nComprehensive Land Claim Agreement: No\nNotification Method: Public Advertising\nContract Awar…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": "Highest Combined Rating of Technical Merit and Price",
  "limited_tendering_reason": null,
  "trade_agreements": [
   "Canada-Chile Free Trade Agreement (CCFTA)",
   "Canada-Colombia Free Trade Agreement",
   "Other trade agreements not listed here may apply",
   "Canada-Peru Free Trade Agreement (CPFTA)",
   "... (6 total)"
  ],
  "notice_type": null,
  "commodity": {
   "gsin": "D302A",
   "gsin_all": "D302A",
   "gsin_description": "Informatics Professional Services",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "SRV"
  },
  "value": 0.0,
  "currency": "CAD",
  "value_detail": {
   "ch_total_contract_value": 0.0,
   "ch_latest_row_contract_amount": 0.0,
   "ch_original_contract_amount": 0.0,
   "ch_number_of_records": "2",
   "value_source": "CanadaBuys legacy contract history contractAmount (latest row)",
   "an_contract_amount": 0.0,
   "an_total_contract_value": null
  },
  "dates": {
   "published": "2024-01-31",
   "signed": null,
   "start": null,
   "end": null,
   "amended_last": "2019-08-13",
   "end_as_published": "2100-01-31"
  },
  "related": {
   "anl_chl_link_basis": [
    "ANL contractNumber 'EN578-170432/318/EI' = CHL contract 'EN578-170432/318/EI'"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_entity": "Public Works and Government Services Canada",
   "canadabuys_end_user_office": "ACQUISITIONS PROGRAM"
  },
  "address": {
   "line1": null,
   "city": null,
   "region": null,
   "postal_code": null,
   "country": null,
   "end_user_address": "Phase III, Place du Portage<br>11 Laurier St,Gatineau,Quebec,K1A0S5,Canada"
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
  "name": "Confluence Consulting Inc. in Joint Venture with Corporate Renaissance Group Inc.",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'Canada' (CanadaBuys legacy contract history latest row, amendment 001)",
  "identifiers": {
   "canadabuys_legal_name": "Confluence Consulting Inc. in Joint Venture with Corporate Renaissance Group Inc.",
   "canadabuys_operating_name": "Confluence Consulting Inc. in Joint Venture with Corporate Renaissance Group Inc.",
   "canadabuys_standardized_name": "CONFLUENCE CONSULTING INC IN JOINT VENTURE WITH CORPORATE RENAISSANCE GROUP INC"
  },
  "address": {
   "line1": "81 Metcalfe Street, Suite 510",
   "city": "Ottawa",
   "region": "Ontario",
   "postal_code": "K1P6K7",
   "country": "Canada"
  },
  "contact": {},
  "employee_count": "10 to 19 employees"
 }
}
```

#### `canada_federal_legacy:E60ZT-180027/026/ZT`

raw keys: `{"canadabuys_legacy_contract_history": "dict", "canadabuys_legacy_award_notice": "dict", "dedupe_checks": "dict"}`

```json
{
 "record_id": "canada_federal_legacy:E60ZT-180027/026/ZT",
 "source": {
  "key": "canada_federal_legacy",
  "name": "CanadaBuys legacy contract history 2009-01 to 2023-05 + legacy award notices 2012-2022",
  "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/4fe645a1-ffcd-40c1-9385-2c771be956a4",
  "record_url": null,
  "retrieved_at": "2026-10-26T02:59:40Z",
  "resource_names": [
   "Legacy contract history, 2009-01 to 2023-05 (prior to CanadaBuys)",
   "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"
  ]
 },
 "status": "ongoing",
 "status_basis": "ongoing: CanadaBuys legacy contract history latest row (amendment 001) contractEndDate 2028-07-04 >= 2026-10-25 and contractStartDate (else contractAwardDate…",
 "contract": {
  "identifiers": {
   "ch_reference_number": "E60ZT-180027/026/ZT",
   "ch_contract_number": "E60ZT-180027/026/ZT",
   "ch_procurement_number": "E60ZT-180027",
   "ch_solicitation_number": "E60ZT-180027",
   "ch_amendment_numbers": [
    "001"
   ],
   "an_reference_numbers": [
    "E60ZT-180027:026:ZT"
   ],
   "an_contract_number": "E60ZT-180027/026/ZT",
   "an_solicitation_number": "E60ZT-180027"
  },
  "title": "ProServices SA - The Social Research and Demonstration Corporation",
  "description": "Amend 001",
  "instrument_type": "supply arrangement",
  "canadabuys_instrument_type": "Supply Arrangement",
  "procurement_method": null,
  "solicitation_procedure": null,
  "selection_criteria": null,
  "limited_tendering_reason": [
   "None"
  ],
  "trade_agreements": [
   "Canada-Chile Free Trade Agreement (CCFTA)",
   "World Trade Organization Agreement on Government Procurement (WTO GPA)",
   "Canada-Colombia Free Trade Agreement",
   "Canadian Free Trade Agreement (CFTA)",
   "... (12 total)"
  ],
  "notice_type": "Request for Supply Arrangement",
  "commodity": {
   "gsin": "D302A",
   "gsin_all": "D302A",
   "gsin_description": "Informatics Professional Services",
   "unspsc": "80122001 | 80160000 | 81110000 | 85101600 | 85101700 | 85270000 | 86132204",
   "unspsc_description": "Independent dispute mediation or arbitration service | Business administration services | Computer services | Healthcare provider support persons | Health ad…",
   "procurement_category": "SRV"
  },
  "value": 0.0,
  "currency": "CAD",
  "value_detail": {
   "ch_total_contract_value": 0.0,
   "ch_latest_row_contract_amount": 0.0,
   "ch_original_contract_amount": 0.0,
   "ch_number_of_records": "1",
   "value_source": "CanadaBuys legacy contract history contractAmount (latest row)",
   "an_contract_amount": 0.0,
   "an_total_contract_value": 0.0
  },
  "dates": {
   "published": "2024-11-07",
   "signed": "2018-03-27",
   "start": "2018-04-03",
   "end": "2028-07-04",
   "amended_last": "2024-11-07"
  },
  "related": {
   "anl_chl_link_basis": [
    "ANL contractNumber 'E60ZT-180027/026/ZT' = CHL contract 'E60ZT-180027/026/ZT'"
   ]
  }
 },
 "buyer": {
  "name": "Department of Public Works and Government Services (PSPC)",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Department of Public Works and Government Services (PSPC)",
   "canadabuys_end_user_entity": "Department of Public Works and Government Services (PSPC)",
   "canadabuys_end_user_office": null
  },
  "address": {
   "line1": "11 Laurier St, Phase III, Place du Portage",
   "city": "Gatineau",
   "region": "Quebec",
   "postal_code": "K1A 0S5",
   "country": "Canada",
   "end_user_address": "11 Laurier St, Phase III, Place du Portage,Gatineau,Quebec,K1A 0S5,Canada"
  },
  "contact": {
   "name": "Fevry, Naomie (SPAC/PSPC) (elle-la / she-her)",
   "email": "naomie.fevry@tpsgc-pwgsc.gc.ca",
   "phone": null,
   "fax": null,
   "address": null
  }
 },
 "vendor": {
  "name": "Social Research and Demonstration Corporation",
  "country": "CA",
  "country_basis": "supplierAddressCountry-fournisseurAdressePays-eng = 'CA' (CanadaBuys legacy contract history latest row, amendment 001)",
  "identifiers": {
   "canadabuys_legal_name": "Social Research and Demonstration Corporation",
   "canadabuys_operating_name": "SRDC",
   "canadabuys_standardized_name": null
  },
  "address": {
   "line1": "55 Murray St \nSuite 400",
   "city": "Ottawa",
   "region": "Ontario",
   "postal_code": "K1N 5M3",
   "country": "CA"
  },
  "contact": {},
  "employee_count": "61"
 }
}
```

#### `canada_federal_legacy:an:PW-16-00723776-726324`

raw keys: `{"canadabuys_legacy_award_notice": "dict", "dedupe_checks": "dict"}`

```json
{
 "record_id": "canada_federal_legacy:an:PW-16-00723776-726324",
 "source": {
  "key": "canada_federal_legacy",
  "name": "CanadaBuys legacy award notices 2012-2022",
  "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
  "record_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00723776-726324",
  "retrieved_at": "2026-10-26T02:59:50Z",
  "resource_names": [
   "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"
  ]
 },
 "status": "end_date_unknown",
 "status_basis": "end_date_unknown: CanadaBuys legacy award notice PW-16-00723776-726324 has blank contractEndDate (award date 2016-03-10; awardStatus Active, not maintained f…",
 "contract": {
  "identifiers": {
   "an_reference_number_latest": "PW-16-00723776-726324",
   "an_reference_numbers": [
    "PW-16-00723776-726324"
   ],
   "an_contract_number": "30-7013301",
   "an_solicitation_number": "9F030-20150928"
  },
  "title": "CORRIDOR SMOKE EVACUATION SYSTEM at the Canadian Space Agency (CSA) in Saint-Hubert",
  "description": "The purpose of this Request for Proposal (RFP) is to solicit bids from interested Canadian organizations to provide work on corridor smoke evacuation system …",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": null,
  "limited_tendering_reason": null,
  "trade_agreements": null,
  "notice_type": null,
  "commodity": {
   "gsin": "5159B",
   "gsin_all": "5159B",
   "gsin_description": "Other Special Trade Construction Work",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "CNST"
  },
  "value": 94555.0,
  "currency": "CAD",
  "value_detail": {
   "an_total_contract_value": null,
   "an_contract_amount": 94555.0,
   "value_source": "CanadaBuys legacy award notice contractAmount"
  },
  "dates": {
   "published": "2016-03-11",
   "signed": "2016-03-10",
   "start": "2016-03-10",
   "end": null,
   "amended_last": null
  },
  "related": {
   "award_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-16-00723776-726324"
  }
 },
 "buyer": {
  "name": "Canadian Space Agency",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Canadian Space Agency",
   "canadabuys_end_user_entity": "Canadian Space Agency",
   "canadabuys_end_user_office": null
  },
  "address": {
   "line1": "6767 Route de l'Aéroport",
   "city": "Saint-Hubert",
   "region": "Quebec",
   "postal_code": "J3Y 8Y9",
   "country": "Canada",
   "end_user_address": "6767 Route de l'Aéroport,Saint-Hubert,Quebec,J3Y 8Y9,Canada"
  },
  "contact": {
   "name": "Morin, Claudine",
   "email": null,
   "phone": "450-926-4427",
   "fax": null,
   "address": "6767 route de l'aéroport Saint-Hubert QC J3Y 8Y9 CA"
  }
 },
 "vendor": {
  "name": "Polyval Construction Inc.",
  "country": "CA",
  "country_basis": "supplierAddressPostalCode-fournisseurAdresseCodePostal pattern 'J3Y 8Y5' (supplierAddressCountry-fournisseurAdressePays-eng blank) (CanadaBuys legacy award n…",
  "identifiers": {
   "canadabuys_legal_name": "Polyval Construction Inc.",
   "canadabuys_legal_name_fr": "Polyval Construction Inc."
  },
  "address": {
   "line1": "3350, 1ère Rue, Parc Industriel L.G. Leclerc, local 101",
   "city": "St-Hubert",
   "region": "Québec",
   "postal_code": "J3Y 8Y5",
   "country": null
  },
  "contact": {}
 }
}
```

#### `canada_federal_legacy:an:PW-19-00869145-885011`

raw keys: `{"canadabuys_legacy_award_notice": "dict", "dedupe_checks": "dict"}`

```json
{
 "record_id": "canada_federal_legacy:an:PW-19-00869145-885011",
 "source": {
  "key": "canada_federal_legacy",
  "name": "CanadaBuys legacy award notices 2012-2022",
  "publisher": "Public Services and Procurement Canada (CanadaBuys open data, legacy files)",
  "dataset_url": "https://open.canada.ca/data/en/dataset/a1acb126-9ce8-40a9-b889-5da2b1dd20cb",
  "record_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-19-00869145-885011",
  "retrieved_at": "2026-10-26T02:59:50Z",
  "resource_names": [
   "Legacy award notices, 2012 to 2022-08 (prior to CanadaBuys)"
  ]
 },
 "status": "end_date_unknown",
 "status_basis": "end_date_unknown: CanadaBuys legacy award notice PW-19-00869145-885011 has blank contractEndDate (award date 2019-06-04; awardStatus Active, not maintained f…",
 "contract": {
  "identifiers": {
   "an_reference_number_latest": "PW-19-00869145-885011",
   "an_reference_numbers": [
    "PW-19-00869145-885011"
   ],
   "an_contract_number": "5P420-18-0507",
   "an_solicitation_number": "5P420-18-0507/A"
  },
  "title": "Indigenous Exhibit – Jasper National Park",
  "description": "Requirement:\nParks Canada Agency (PCA) is inviting firms to submit Proposals to provide a full range of professional services for architectural, landscaping,…",
  "instrument_type": null,
  "canadabuys_instrument_type": null,
  "procurement_method": "Competitive - Open bidding",
  "solicitation_procedure": "Competitive - Open bidding",
  "selection_criteria": null,
  "limited_tendering_reason": null,
  "trade_agreements": null,
  "notice_type": null,
  "commodity": {
   "gsin": "C129A",
   "gsin_all": "C129A",
   "gsin_description": "Architectural & EngineeringServices - Other Non-Building Structures",
   "unspsc": null,
   "unspsc_description": null,
   "procurement_category": "SRV"
  },
  "value": 338703.75,
  "currency": "CAD",
  "value_detail": {
   "an_total_contract_value": null,
   "an_contract_amount": 338703.75,
   "value_source": "CanadaBuys legacy award notice contractAmount"
  },
  "dates": {
   "published": "2019-08-09",
   "signed": "2019-06-04",
   "start": "2019-06-04",
   "end": null,
   "amended_last": null
  },
  "related": {
   "award_notice_url": "https://canadabuys.canada.ca/en/tender-opportunities/award-notice/pw-19-00869145-885011"
  }
 },
 "buyer": {
  "name": "Parks Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "canadabuys_contracting_entity": "Parks Canada",
   "canadabuys_end_user_entity": "Parks Canada",
   "canadabuys_end_user_office": null
  },
  "address": {
   "line1": "30 Victoria Street",
   "city": "Gatineau",
   "region": "Quebec",
   "postal_code": "J8X 0B3",
   "country": "Canada",
   "end_user_address": "30 Victoria Street,Gatineau,Quebec,J8X 0B3,Canada"
  },
  "contact": {
   "name": "Maheu, Jennifer",
   "email": null,
   "phone": "587-432-8458",
   "fax": null,
   "address": "220 - 4 Avenue S.E., Suite 720 Calgary Alberta T2G 4X3 CA"
  }
 },
 "vendor": {
  "name": "Panther Creative Inc.",
  "country": "CA",
  "country_basis": "supplierAddressPostalCode-fournisseurAdresseCodePostal pattern 'V3C 6P3' (supplierAddressCountry-fournisseurAdressePays-eng blank) (CanadaBuys legacy award n…",
  "identifiers": {
   "canadabuys_legal_name": "Panther Creative Inc.",
   "canadabuys_legal_name_fr": "Panther Creative Inc."
  },
  "address": {
   "line1": "1533 Broadway St, #112",
   "city": "Port Coquitlam",
   "region": "BC",
   "postal_code": "V3C 6P3",
   "country": null
  },
  "contact": {}
 }
}
```



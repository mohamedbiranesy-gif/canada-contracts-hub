# canada_sosa — PSPC active Standing Offers and Supply Arrangements (SOSA)

Source key: `canada_sosa` · Outputs:
- `/home/claude/contracts/normalized/canada_sosa.jsonl`: **906 records**, all `ongoing` (md5 `dda0f8f9086842fff74388f1f36a2ebd`)
- `/home/claude/contracts/normalized/canada_sosa_unverified_country.jsonl`: 186 records (`ongoing`), with no supplier location published anywhere for that instrument

Built 2026-10-26 03:37 UTC by `/home/claude/contracts/scripts/canada_sosa/build.py` (`scripts/canada_sosa/logs/build_stats.json`). Workstream W1a.

## 1. Source
- Dataset: "Standing Offers and Supply Arrangements" (PSPC), https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e (`metadata_modified` 2026-10-25T05:13). It is weekly and lists every **currently active** SO/SA.
- Resource: https://sosa.canadabuys.canada.ca/cds/opendata/tpsgc-pwgsc_ocama-sosa.csv. Saved as `downloads/canada_sosa/tpsgc-pwgsc_ocama-sosa.csv` (3,994,427 bytes, retrieved 2026-10-26T03:02:25Z; `date-file-published` in the rows: 2026-10-24 20:58:02). 6,823 rows = 3,966 distinct `agreement-number`s (one row per delivery point/commodity). A re-fetch at 03:21:54Z failed TLS verification at the proxy (`curl: (60)`), so the 03:02 copy is used.
- Data dictionary: https://donnees-data.tpsgc-pwgsc.gc.ca/ba2/ac-cb/ocama-sosa-dd.xml (`downloads/canada_sosa/ocama-sosa-dd.xml`). Package metadata for f5c8a5a0…, 53753f06… and 8786c760… is saved as `package_show_*.json`.
- Columns: sosa-description_en/fr, commodity-description_en/fr, commodity (UNSPSC), supplier-standardized-name, supplier-legal-name, supplier-operating-name, end-user-entity_en/fr, award-date, expiry-date, delivery-point-code, delivery-point_en/fr, agreement-type_en/fr (SA, NMSO, RISO, NISO, DISO, RMSO), agreement-number, date-file-published. **No supplier address and no value.**

## 2. Canadian vendor (two tiers, labelled)
1. **Same instrument** (38 records): the agreement number (or its `CW#######` prefix) appears in CanadaBuys contract history / award notices (complete files + legacy files) with a supplier name that agrees. The latest such row's `supplierAddressCountry` (or a Canadian postal code when the country is blank) gives the country and the full address. `country_basis` names the file, row and value.
2. **Same supplier elsewhere in CanadaBuys** (868 records; `vendor.country_basis_type = "registry_match"`). This is a W1e-style match. The SOSA supplier-standardized-name or legal name matches exactly (case/space-insensitive, at least 6 characters) the supplier name on CanadaBuys rows for other instruments, and **every** matched row with an address must be Canadian. The address of the latest matching row is used (`vendor.address.address_source`), and up to 10 evidence rows are kept in `raw.supplier_address_evidence_same_supplier`. 87 agreements were refused because the matched rows include a foreign address. 99 agreements had no rows at all.
- Excluded as non-Canadian: 119 agreements (US 89, GB 10, DE 3, AU 2, others 1 each).
- 186 agreements with no address anywhere go to `_unverified_country.jsonl` with `vendor.country = null` and `country_basis = "not published: …"`.

## 3. Status logic
- `ongoing`: earliest `award-date` ≤ 2026-10-25 ≤ latest `expiry-date`. All 906 are `ongoing` (expiry years 2026: 116, 2027: 355, 2028: 127, 2029–2031: 256, 2032–2099: 52). Being listed in the weekly "active" file confirms the status, and `status_basis` cites `date-file-published`.
- Expiry year ≥ 2100 would be `ongoing_inferred` (placeholder); none survived. Expiry < ref (86 agreements still in the file after expiry) and future award dates are excluded.

## 4. De-duplication
- Against `normalized/canada_federal.jsonl` (id index `work/canada_federal_legacy/cf_index.jsonl.gz`): agreement number / CW number equal to a contract-level id and the supplier names agree, **2,667 agreements dropped**. Most active SOs/SAs issued since 2023 are already in CanadaBuys contract history.
- Against `normalized/canada_federal_legacy.jsonl` (CHL/ANL reference and contract numbers): 2 dropped.
- Note: call-ups *against* these SO/SAs that departments report in proactive disclosure (`standing_offer_number`) are separate contracts and stay in `canada_federal`.

## 5. Record identity / URL
- `record_id = canada_sosa:<agreement-number>`, e.g. `canada_sosa:CW2307444-ACM_164145619`.
- `source.record_url = null`. The SOSA search application has no stable per-agreement URL that could be verified (its host also failed TLS through the proxy).
- `buyer.name` = `end-user-entity_en`. "Public Works and Government Services Canada" (701 records) means a government-wide instrument put in place by PSPC (`buyer.name_note`). `raw.sosa_rows` keeps every SOSA row of the agreement verbatim (all delivery points/commodities).

## 6. Counts
| file | ongoing | total |
|---|---|---|
| canada_sosa.jsonl | 906 | 906 (supply arrangements 456, standing offers 450) |
| canada_sosa_unverified_country.jsonl | 186 | 186 |

Top buyers: PWGSC 701, DND 64, Transport Canada 32, DFO 25, NRCan 19, Canadian Coast Guard 14.

## 7. Gaps
- No value field (SO/SA are framework instruments). Value comes from the CanadaBuys row only when a same-instrument row exists.
- Tier-2 country rests on an exact supplier-name match to other CanadaBuys records. It is labelled `registry_match` so that assembly can tell it apart from an address on the instrument itself.

## 8. Sample records

#### `canada_sosa:CW2307444-ACM_164145619`

raw keys: `{"sosa_rows": "1 row(s)", "resource_url": "str", "retrieved_at": "str", "supplier_address_evidence_same_supplier": "8 row(s)"}`

```json
{
 "record_id": "canada_sosa:CW2307444-ACM_164145619",
 "source": {
  "key": "canada_sosa",
  "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
  "publisher": "Public Services and Procurement Canada",
  "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
  "record_url": null,
  "retrieved_at": "2026-10-26T03:02:25Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: SOSA award-date 2023-05-30 <= 2026-10-25 and expiry-date 2028-05-31 >= 2026-10-25 (listed in the weekly active-SOSA file, date-file-published 2026-1…",
 "contract": {
  "identifiers": {
   "sosa_agreement_number": "CW2307444-ACM_164145619",
   "cw_number": "CW2307444"
  },
  "title": "EN578-231556 Aircraft Charter Services",
  "title_fr": "EN578-231556 services d'affrètement aérien",
  "description": "78142001 - 78142001 - Rental of freight aircraft with operator",
  "instrument_type": "standing offer",
  "agreement_type": "National Master Standing Offer (NMSO)",
  "procurement_method": null,
  "solicitation_procedure": null,
  "commodity": {
   "unspsc": "78142001",
   "unspsc_description": "78142001 - Rental of freight aircraft with operator"
  },
  "value": null,
  "currency": null,
  "value_detail": {},
  "dates": {
   "published": "2026-10-24",
   "signed": "2023-05-30",
   "start": "2023-05-30",
   "end": "2028-05-31",
   "amended_last": null
  },
  "related": {
   "regions_of_delivery": [
    "CA Canada"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "sosa_end_user_entity_en": "Public Works and Government Services Canada",
   "sosa_end_user_entity_fr": "Travaux publics et Services gouvernementaux Canada",
   "issuing_authority": "Public Services and Procurement Canada"
  },
  "address": {},
  "contact": {},
  "name_note": "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
 },
 "vendor": {
  "name": "Vision Air Services Inc.",
  "country": "CA",
  "country_basis": "same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name (supplierStandardizedName) to 8 CanadaBuys row(s), all with a Canadian supplierAddre…",
  "identifiers": {
   "sosa_supplier_legal_name": "Vision Air Services Inc.",
   "sosa_supplier_standardized_name": "VISION AIR SERVICES INC",
   "sosa_supplier_operating_name": null
  },
  "address": {
   "line1": "16 Meadowvale Lane",
   "city": "Oakfield",
   "region": "Nova Scotia",
   "postal_code": "B2T1B3",
   "country": "Canada",
   "address_source": "canadabuys_legacy_contract_history row E60SQ-020001/260/ZL (same supplier, other instrument)"
  },
  "contact": {},
  "country_basis_type": "registry_match"
 }
}
```

#### `canada_sosa:CW2246331`

raw keys: `{"sosa_rows": "1 row(s)", "resource_url": "str", "retrieved_at": "str", "supplier_address_evidence_same_supplier": "10 row(s)"}`

```json
{
 "record_id": "canada_sosa:CW2246331",
 "source": {
  "key": "canada_sosa",
  "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
  "publisher": "Public Services and Procurement Canada",
  "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
  "record_url": null,
  "retrieved_at": "2026-10-26T03:02:25Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: SOSA award-date 2022-09-06 <= 2026-10-25 and expiry-date 2027-03-31 >= 2026-10-25 (listed in the weekly active-SOSA file, date-file-published 2026-1…",
 "contract": {
  "identifiers": {
   "sosa_agreement_number": "CW2246331",
   "cw_number": "CW2246331"
  },
  "title": "Multidisciplinary Environmental Ser",
  "title_fr": "Multidisciplinary Environmental Ser",
  "description": "76100000; 77000000 - 76100000 - Decontamination services; 77000000 - Environmental Services",
  "instrument_type": "standing offer",
  "agreement_type": "Departmental Individual Standing Offer (DISO)",
  "procurement_method": null,
  "solicitation_procedure": null,
  "commodity": {
   "unspsc": "76100000; 77000000",
   "unspsc_description": "76100000 - Decontamination services; 77000000 - Environmental Services"
  },
  "value": null,
  "currency": null,
  "value_detail": {},
  "dates": {
   "published": "2026-10-24",
   "signed": "2022-09-06",
   "start": "2022-09-06",
   "end": "2027-03-31",
   "amended_last": null
  },
  "related": {
   "regions_of_delivery": [
    "CA-NU Nunavut"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "sosa_end_user_entity_en": "Public Works and Government Services Canada",
   "sosa_end_user_entity_fr": "Travaux publics et Services gouvernementaux Canada",
   "issuing_authority": "Public Services and Procurement Canada"
  },
  "address": {},
  "contact": {},
  "name_note": "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
 },
 "vendor": {
  "name": "OUTCOME CONSULTANTS INC.",
  "country": "CA",
  "country_basis": "same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name (supplierLegalName) to 43 CanadaBuys row(s), all with a Canadian supplierAddressCoun…",
  "identifiers": {
   "sosa_supplier_legal_name": "OUTCOME CONSULTANTS INC.",
   "sosa_supplier_standardized_name": "OUTCOME CONSULTANTS INC",
   "sosa_supplier_operating_name": null
  },
  "address": {
   "line1": "151 Holland Avenue \nSuite 200",
   "city": "Ottawa",
   "region": "Ontario",
   "postal_code": "K1Y 0Y2",
   "country": "CA",
   "address_source": "canadabuys_legacy_contract_history row EW699-220414/011/NCS (same supplier, other instrument)"
  },
  "contact": {},
  "country_basis_type": "registry_match"
 }
}
```

#### `canada_sosa:CW2332554`

raw keys: `{"sosa_rows": "1 row(s)", "resource_url": "str", "retrieved_at": "str", "supplier_address_evidence_same_supplier": "5 row(s)"}`

```json
{
 "record_id": "canada_sosa:CW2332554",
 "source": {
  "key": "canada_sosa",
  "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
  "publisher": "Public Services and Procurement Canada",
  "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
  "record_url": null,
  "retrieved_at": "2026-10-26T03:02:25Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: SOSA award-date 2023-11-16 <= 2026-10-25 and expiry-date 2026-11-30 >= 2026-10-25 (listed in the weekly active-SOSA file, date-file-published 2026-1…",
 "contract": {
  "identifiers": {
   "sosa_agreement_number": "CW2332554",
   "cw_number": "CW2332554"
  },
  "title": "Gender-Based Analysis (GBA) Plus Consultancy Services - E60ZG-212007-016. Legacy agreement: SEASONOVA GROUP INC (CW2332072-ACM_173278076).",
  "title_fr": "Services-conseil sur l'analyse comparative entre les sexes (ACS) Plus - E60ZG-212007-016. Ancien accord : SEASONOVA GROUP INC (CW2332072-ACM_173278076).",
  "description": "80110000 - 80110000 - Human resources services",
  "instrument_type": "standing offer",
  "agreement_type": "National Master Standing Offer (NMSO)",
  "procurement_method": null,
  "solicitation_procedure": null,
  "commodity": {
   "unspsc": "80110000",
   "unspsc_description": "80110000 - Human resources services"
  },
  "value": null,
  "currency": null,
  "value_detail": {},
  "dates": {
   "published": "2026-10-24",
   "signed": "2023-11-16",
   "start": "2023-11-16",
   "end": "2026-11-30",
   "amended_last": null
  },
  "related": {
   "regions_of_delivery": [
    "CA Canada"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "sosa_end_user_entity_en": "Public Works and Government Services Canada",
   "sosa_end_user_entity_fr": "Travaux publics et Services gouvernementaux Canada",
   "issuing_authority": "Public Services and Procurement Canada"
  },
  "address": {},
  "contact": {},
  "name_note": "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
 },
 "vendor": {
  "name": "SEASONOVA Group Inc.",
  "country": "CA",
  "country_basis": "same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name (supplierLegalName) to 5 CanadaBuys row(s), all with a Canadian supplierAddressCount…",
  "identifiers": {
   "sosa_supplier_legal_name": "SEASONOVA Group Inc.",
   "sosa_supplier_standardized_name": "SEASONOVA GROUP INC",
   "sosa_supplier_operating_name": null
  },
  "address": {
   "line1": "316 Sweetclover Way",
   "city": "Ottawa",
   "region": "Ontario",
   "postal_code": "K4A 1E5",
   "country": "CA",
   "address_source": "canadabuys_award_notices_complete row CW2343477 (same supplier, other instrument)"
  },
  "contact": {},
  "country_basis_type": "registry_match"
 }
}
```

#### `canada_sosa:CW2420552`

raw keys: `{"sosa_rows": "1 row(s)", "resource_url": "str", "retrieved_at": "str", "supplier_address_evidence_same_supplier": "10 row(s)"}`

```json
{
 "record_id": "canada_sosa:CW2420552",
 "source": {
  "key": "canada_sosa",
  "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
  "publisher": "Public Services and Procurement Canada",
  "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
  "record_url": null,
  "retrieved_at": "2026-10-26T03:02:25Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: SOSA award-date 2025-10-10 <= 2026-10-25 and expiry-date 2027-07-31 >= 2026-10-25 (listed in the weekly active-SOSA file, date-file-published 2026-1…",
 "contract": {
  "identifiers": {
   "sosa_agreement_number": "CW2420552",
   "cw_number": "CW2420552"
  },
  "title": "E6TOR-24RM04 - 003 - Language Training Services -",
  "title_fr": "E6TOR-24RM04 - 003 - Services de formation linguistique",
  "description": "86111700 - 86111700 - Language schooling",
  "instrument_type": "standing offer",
  "agreement_type": "Regional Master Standing Offer (RMSO)",
  "procurement_method": null,
  "solicitation_procedure": null,
  "commodity": {
   "unspsc": "86111700",
   "unspsc_description": "86111700 - Language schooling"
  },
  "value": null,
  "currency": null,
  "value_detail": {},
  "dates": {
   "published": "2026-10-24",
   "signed": "2025-10-10",
   "start": "2025-10-10",
   "end": "2027-07-31",
   "amended_last": null
  },
  "related": {
   "regions_of_delivery": [
    "CA-ON Ontario"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "sosa_end_user_entity_en": "Public Works and Government Services Canada",
   "sosa_end_user_entity_fr": "Travaux publics et Services gouvernementaux Canada",
   "issuing_authority": "Public Services and Procurement Canada"
  },
  "address": {},
  "contact": {},
  "name_note": "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
 },
 "vendor": {
  "name": "Berlitz Canada Inc",
  "country": "CA",
  "country_basis": "same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name (supplierStandardizedName) to 58 CanadaBuys row(s), all with a Canadian supplierAddr…",
  "identifiers": {
   "sosa_supplier_legal_name": "Berlitz Canada Inc",
   "sosa_supplier_standardized_name": "BERLITZ CANADA INC",
   "sosa_supplier_operating_name": null
  },
  "address": {
   "line1": "350 Sparks Street, Suite 1001",
   "city": "Ottawa",
   "region": "Ontario",
   "postal_code": "K1R7S8",
   "country": "Canada",
   "address_source": "canadabuys_legacy_contract_history row EN578-093429/005/ZF (same supplier, other instrument)"
  },
  "contact": {},
  "country_basis_type": "registry_match"
 }
}
```

#### `canada_sosa:CW2253799`

raw keys: `{"sosa_rows": "1 row(s)", "resource_url": "str", "retrieved_at": "str", "supplier_address_evidence_same_supplier": "6 row(s)"}`

```json
{
 "record_id": "canada_sosa:CW2253799",
 "source": {
  "key": "canada_sosa",
  "name": "Standing Offers and Supply Arrangements (SOSA) - Active Standing Offers and Supply Arrangements",
  "publisher": "Public Services and Procurement Canada",
  "dataset_url": "https://open.canada.ca/data/en/dataset/f5c8a5a0-354d-455a-99ab-8276aa38032e",
  "record_url": null,
  "retrieved_at": "2026-10-26T03:02:25Z"
 },
 "status": "ongoing",
 "status_basis": "ongoing: SOSA award-date 2019-10-22 <= 2026-10-25 and expiry-date 2036-03-31 >= 2026-10-25 (listed in the weekly active-SOSA file, date-file-published 2026-1…",
 "contract": {
  "identifiers": {
   "sosa_agreement_number": "CW2253799",
   "cw_number": "CW2253799"
  },
  "title": "Amend 002 - Schedule Transportation Service - Urban Valley Transport Ltd.",
  "title_fr": "Modif 002 - Transport - Urban Valley Transport Ltd.",
  "description": "78140000 - 78140000 - Transport services",
  "instrument_type": "supply arrangement",
  "agreement_type": "Supply Arrangement (SA)",
  "procurement_method": null,
  "solicitation_procedure": null,
  "commodity": {
   "unspsc": "78140000",
   "unspsc_description": "78140000 - Transport services"
  },
  "value": null,
  "currency": null,
  "value_detail": {},
  "dates": {
   "published": "2026-10-24",
   "signed": "2019-10-22",
   "start": "2019-10-22",
   "end": "2036-03-31",
   "amended_last": null
  },
  "related": {
   "regions_of_delivery": [
    "CA Canada"
   ]
  }
 },
 "buyer": {
  "name": "Public Works and Government Services Canada",
  "country": "CA",
  "type": "federal department or agency",
  "identifiers": {
   "sosa_end_user_entity_en": "Public Works and Government Services Canada",
   "sosa_end_user_entity_fr": "Travaux publics et Services gouvernementaux Canada",
   "issuing_authority": "Public Services and Procurement Canada"
  },
  "address": {},
  "contact": {},
  "name_note": "PSPC/PWGSC as end user = government-wide instrument put in place by PSPC for use by federal organizations"
 },
 "vendor": {
  "name": "Urban Valley Transport Ltd.",
  "country": "CA",
  "country_basis": "same supplier elsewhere in CanadaBuys: exact match of SOSA supplier name (supplierLegalName) to 6 CanadaBuys row(s), all with a Canadian supplierAddressCount…",
  "identifiers": {
   "sosa_supplier_legal_name": "Urban Valley Transport Ltd.",
   "sosa_supplier_standardized_name": "URBAN VALLEY TRANSPORT LTD",
   "sosa_supplier_operating_name": "Urban Valley Transport Ltd."
  },
  "address": {
   "line1": "7252 River Place \nUnit 3",
   "city": "MISSION",
   "region": "British Columbia",
   "postal_code": "V4S 0A2",
   "country": "CA",
   "address_source": "canadabuys_legacy_contract_history row EN578-200920/008/LS (same supplier, other instrument)"
  },
  "contact": {},
  "country_basis_type": "registry_match"
 }
}
```



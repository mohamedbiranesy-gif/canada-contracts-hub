# py_dncp — Paraguay – DNCP Contrataciones Abiertas (OCDS records via OCP Data Registry)

Reference date 2026-10-25. Publisher: Dirección Nacional de Contrataciones Públicas (DNCP), Paraguay. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 63: https://data.open-contracting.org/en/publication/63 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/63 (origin: https://contrataciones.gov.py/datos/api/v3/doc/).

Output: `/home/claude/contracts/normalized/py_dncp.jsonl` — **1 records** {'end_date_unknown': 1}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/py_dncp/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T18:22:11Z | 5382 | 1 |
| 2025 | 2026-10-25T18:22:41Z | 10876 | 3 |
| 2024 | 2026-10-25T18:23:49Z | 12470 | 0 |
| 2023 | 2026-10-25T18:24:18Z | 12657 | 1 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 3216 supplier parties, 3216 with an address, **3216 with a country value**; address keys {'countryName': 3216, 'streetAddress': 3216, 'locality': 3131, 'region': 3079}; most common country values {'Paraguay': 3216}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'Canadá'": 1}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source py_dncp --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 5, "units": 5, "excluded_ended": 4, "status_end_date_unknown": 1}`; excluded examples: [['ocds-03ad3f-405010-1', 'end 2022-04-28 < ref'], ['ocds-03ad3f-428215-1', 'end 2026-09-16 < ref'], ['ocds-03ad3f-407915-1', 'end 2025-03-23 < ref'], ['ocds-03ad3f-360215-1', 'end 2021-05-22 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 1}.
Buyers: {'Banco Central del Paraguay (BCP)': 1}.

`record_url`: template `https://www.contrataciones.gov.py/datos/api/v3/doc/ocds/record/{ocid}`; example https://www.contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-479495-1

## Five sample records
- `py_dncp:ocds-03ad3f-479495-1` | Canadian Banknote Company, Limited (Ottawa) | Banco Central del Paraguay (BCP) | LPI N° 4PM/2026 - SERVICIO DE IMPRESIÓN Y PROVISIÓN DE BILLETES DE DENOMINACIÓN  | USD 9439424.0 | 2026-05-07 → None | end_date_unknown | https://www.contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-479495-1

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- record_url verified: https://www.contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-479495-1 -> HTTP 200 naming Canadian Banknote Company. DNCP releases rarely carry contract periods (0 of 3,000 sampled) -> `end_date_unknown` unless the contract block has a period.

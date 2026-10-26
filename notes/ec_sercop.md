# ec_sercop — Ecuador – SERCOP Datos Abiertos OCDS (bulk via OCP Data Registry)

Reference date 2026-10-25. Publisher: Servicio Nacional de Contratación Pública (SERCOP), Ecuador. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 110: https://data.open-contracting.org/en/publication/110 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/110 (origin: https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/datos-abiertos).

Output: `/home/claude/contracts/normalized/ec_sercop.jsonl` — **1 records** {'ongoing': 1}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/ec_sercop/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T18:25:20Z | 121705 | 1 |
| 2025 | 2026-10-25T18:25:33Z | 197502 | 0 |
| 2024 | 2026-10-25T18:25:50Z | 217422 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2584 supplier parties, 2584 with an address, **2584 with a country value**; address keys {'countryName': 2584, 'streetAddress': 2582, 'region': 2537, 'locality': 2537, 'postalCode': 939}; most common country values {'ECUADOR': 2583, 'ESTADOS UNIDOS': 1}; contracts with `period.endDate`: 2271.

Values seen on kept records: {"parties[].address.countryName = 'CANADA'": 1}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source ec_sercop --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 1, "units": 1, "status_ongoing": 1}`; excluded examples: []

## Result / verdict
Counts by status: {'ongoing': 1}.
Buyers: {'INSTITUTO OCEANOGRÁFICO Y ANTÁRTICO DE LA ARMADA': 1}.

`record_url`: template `https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid={ocid}`; example https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid=ocds-5wno2w-CPC-INOCAR-2026-003-1006003

## Five sample records
- `ec_sercop:ocds-5wno2w-CPC-INOCAR-2026-003-1006003` | CARRERA  GALO (None) | INSTITUTO OCEANOGRÁFICO Y ANTÁRTICO DE LA ARMADA | CPC-INOCAR-2026-003-1006003 | USD 130000.0 | 2026-08-17 → 2027-01-14 | ongoing | https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid=ocds-5wno2w-CPC-INOCAR-2026-003-1006003

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- record_url (OCDS record API) verified: https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid=ocds-5wno2w-CPC-INOCAR-2026-003-1006003 -> HTTP 200 JSON naming CARRERA GALO. The supplier is a natural person whose address country is CANADA.

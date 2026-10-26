# pe_oece — Perú – Contrataciones Abiertas OECE/SEACE (OCDS bulk via OCP Data Registry)

Reference date 2026-10-25. Publisher: Organismo Especializado para las Contrataciones Públicas Eficientes (OECE, ex-OSCE), Peru; mirrored by Open Contracting Partnership Data Registry. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 135: https://data.open-contracting.org/en/publication/135 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/135 (origin: https://contratacionesabiertas.oece.gob.pe/descargas).

Output: `/home/claude/contracts/normalized/pe_oece.jsonl` — **11 records** {'end_date_unknown': 6, 'ongoing': 5}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/pe_oece/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T17:38:02Z | 134917 | 42 |
| 2025 | 2026-10-25T17:38:50Z | 124538 | 57 |
| 2024 | 2026-10-25T17:45:20Z | 108451 | 48 |
| 2023 | 2026-10-25T18:00:06Z | 46116 | 26 |
| 2022 | 2026-10-25T18:00:25Z | 59922 | 21 |
| 2021 | 2026-10-25T18:00:44Z | 61296 | 38 |
| 2020 | 2026-10-25T18:02:03Z | 65097 | 24 |
| 2019 | 2026-10-25T18:02:21Z | 64301 | 53 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2345 supplier parties, 806 with an address, **806 with a country value**; address keys {'countryName': 806}; most common country values {'PERU': 756, 'ESTADOS UNIDOS': 16, 'ESPAÑA': 6, 'ARGENTINA': 5, 'MEXICO': 4, 'COLOMBIA': 4, 'CHILE': 3, 'REINO UNIDO': 3}; contracts with `period.endDate`: 2168.

Values seen on kept records: {"parties[].address.countryName = 'CANADA'": 11}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source pe_oece --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 309, "units": 320, "excluded_ended": 308, "status_end_date_unknown": 6, "status_ongoing": 5, "excluded_contract_cancelled": 1}`; excluded examples: [['ocds-dgv273-seacev3-2019-15-29', 'end 2019-03-05 < ref'], ['ocds-dgv273-seacev3-2019-15-30', 'end 2019-03-05 < ref'], ['ocds-dgv273-seacev3-2019-15-28', 'end 2019-03-05 < ref'], ['ocds-dgv273-seacev3-2019-1947-79', 'end 2019-03-15 < ref'], ['ocds-dgv273-seacev3-507564', 'end 2019-03-29 < ref'], ['ocds-dgv273-seacev3-507577', 'end 2019-03-29 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 6, 'ongoing': 5}.
Buyers: {'COMISION DE PROMOCION DEL PERU PARA LA EXPORTACION Y EL TURISMO - PROMPERU': 5, 'PERUPETRO S.A.': 1, 'CAJA DE PENSIONES MILITAR - POLICIAL': 1, 'MINISTERIO DE COMERCIO EXTERIOR Y TURISMO': 1, 'AGENCIA DE PROMOCION DE LA INVERSION PRIVADA - PROINVERSION': 1, 'AGENCIA DE COMPRAS DE LAS FUERZAS ARMADAS': 1, 'PROGRAMA SUBSECTORIAL DE IRRIGACIONES - PSI': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `pe_oece:ocds-dgv273-seacev3-771105` | GEOSOFT INC (None) | PERUPETRO S.A. | INTER-PROC-10-2021-PERUPETRO-1 | USD 49649.85 | 2021-12-29 → None | end_date_unknown | None
- `pe_oece:ocds-dgv273-seacev3-2024-1947-287` | FEVER PITCH MARKETING COMMUNICATIONS INC. (None) | COMISION DE PROMOCION DEL PERU PARA LA EXPORTACION Y EL TURISMO - PROMPERU | INTER-PROC-364-2024-PROMPERU-1 | USD 69000.0 | 2024-11-08 → None | end_date_unknown | None
- `pe_oece:ocds-dgv273-seacev3-1152188` | TOURRADAR GMBH (None) | COMISION DE PROMOCION DEL PERU PARA LA EXPORTACION Y EL TURISMO - PROMPERU | INTER-PROC-444-2025-PROMPERU-1 | USD 30000.0 | 2025-09-17 → None | end_date_unknown | None
- `pe_oece:ocds-dgv273-seacev3-2025-243393-3` | MRB PARTNERS (None) | CAJA DE PENSIONES MILITAR - POLICIAL | INTER-PROC-1-2025-CPMP-1 | PEN 158022.42 | 2025-04-15 → 2028-04-15 | ongoing | None
- `pe_oece:ocds-dgv273-seacev3-169053` | TRADELAWGUIDE LIMITED (None) | MINISTERIO DE COMERCIO EXTERIOR Y TURISMO | INTER-PROC-6-2015-MINCETUR-1 | USD 2491.0 | 2015-09-15 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- Years 2019–2026 streamed; 2010–2018 not streamed (most awards of that era would have ended).
- OCDS record API `https://contratacionesabiertas.oece.gob.pe/api/v1/record/<ocid>` returned HTTP 403 to our client on 2026-10-25 (not bypassed), so record_url = null; template kept in `contract.related.ocds_record_url`.
- Only ~1/3 of supplier parties carry a country (806 of 2,345 in the sample); domestic suppliers mostly have no address, foreign ones (registered as 'no domiciliado') usually do.

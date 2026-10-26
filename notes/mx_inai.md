# mx_inai — Mexico – INAI (federal transparency institute) contracting OCDS

Reference date 2026-10-25. Publisher: Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 31: https://data.open-contracting.org/en/publication/31 .

Output: `/home/claude/contracts/normalized/mx_inai.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/mx_inai/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:31:59Z | 1274 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 1357 supplier parties, 1289 with an address, **1052 with a country value**; address keys {'region': 1273, 'locality': 1271, 'countryName': 1052, 'postalCode': 1007, 'streetAddress': 992}; most common country values {'México': 924, 'México ': 35, 'MÉXICO': 33, 'Estados Unidos de América': 23, 'MEXICO': 17, 'Mexico': 7, 'Australia': 3, 'Switzerland ': 1}; contracts with `period.endDate`: 1320.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
Supplier country field IS published (see probe) but 0 releases had a supplier whose address country denotes Canada in the files streamed. **Checked, 0 Canadian-supplier records.**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.

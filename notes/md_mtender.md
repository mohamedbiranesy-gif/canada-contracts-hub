# md_mtender — Moldova – MTender (Ministry of Finance) OCDS

Reference date 2026-10-25. Publisher: Ministry of Finance, Republic of Moldova. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 34: https://data.open-contracting.org/en/publication/34 .

Output: `/home/claude/contracts/normalized/md_mtender.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/md_mtender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T19:30:55Z | 47356 | 0 |
| 2025 | 2026-10-25T19:31:11Z | 46999 | 0 |
| 2024 | 2026-10-25T19:31:13Z | 16051 | 0 |
| 2023 | 2026-10-25T19:31:15Z | 6741 | 0 |
| 2022 | 2026-10-25T19:31:16Z | 2248 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 321 supplier parties, 321 with an address, **0 with a country value**; address keys {'postalCode': 321, 'streetAddress': 321, 'addressDetails': 321}; most common country values {}; contracts with `period.endDate`: 0.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
Supplier country is published, but in a non-standard place: `address.addressDetails.country.id` (ISO alpha-2, e.g. 'MD'). The structural filter does not read `addressDetails`, so the prefiltered lines (all lines containing a 'CA'/Canada token) were re-checked directly on 2026-10-25: 0 parties with `addressDetails.country.id` = 'CA' in 2022–2026. **Checked, 0 Canadian-supplier records.**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.

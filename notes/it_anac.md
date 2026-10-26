# it_anac — Italy – ANAC BDNCP OCDS

Reference date 2026-10-25. Publisher: Autorità Nazionale Anticorruzione (ANAC). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 117: https://data.open-contracting.org/en/publication/117 .

Output: `/home/claude/contracts/normalized/it_anac.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/it_anac/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2025 | 2026-10-25T17:41:19Z | 97233 | 0 |
| 2024 | 2026-10-25T17:41:28Z | 118688 | 0 |
| undated | 2026-10-25T17:41:33Z | 34238 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2675 supplier parties, 2 with an address, **2 with a country value**; address keys {'locality': 2, 'postalCode': 2, 'countryName': 2, 'streetAddress': 2}; most common country values {'ITALY': 2}; contracts with `period.endDate`: 483.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
Only 2 of 2,675 supplier parties in a sample carry an address (both ITALY); ANAC identifies suppliers by codice fiscale only. 0 matches 2024, 2025, undated. **Rejected: supplier country essentially never published.**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- ANAC's own open-data portal (dataset `aggiudicatari`, https://dati.anticorruzione.it/opendata/dataset/aggiudicatari) answered **'Request Rejected'** (F5 WAF page, HTTP 200/269 bytes) on 2026-10-25 ~19:59 UTC — not bypassed; its awardee files are in any case keyed by codice fiscale without a country column.

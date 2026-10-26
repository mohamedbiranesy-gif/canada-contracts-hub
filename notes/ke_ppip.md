# ke_ppip — Kenya – PPIP OCDS

Reference date 2026-10-25. Publisher: Public Procurement Regulatory Authority (PPRA), Kenya. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 147: https://data.open-contracting.org/en/publication/147 .

Output: `/home/claude/contracts/normalized/ke_ppip.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/ke_ppip/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T17:36:01Z | 23098 | 0 |
| 2025 | 2026-10-25T17:41:47Z | 33258 | 0 |
| 2024 | 2026-10-25T17:41:51Z | 58971 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 7278 supplier parties, 7278 with an address, **7278 with a country value**; address keys {'region': 7278, 'locality': 7278, 'countryName': 7278, 'streetAddress': 1762, 'postalCode': 1729}; most common country values {'KENYA': 7278}; contracts with `period.endDate`: 1579.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
Supplier country field IS published (see probe) but 0 releases had a supplier whose address country denotes Canada in the files streamed. **Checked, 0 Canadian-supplier records.**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.

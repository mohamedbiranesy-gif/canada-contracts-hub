# zm_zppa — Zambia – ZPPA e-GP OCDS record packages (via OCP Data Registry)

Reference date 2026-10-25. Publisher: Zambia Public Procurement Authority (ZPPA). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 3: https://data.open-contracting.org/en/publication/3 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/3 (origin: https://www.zppa.org.zm/record-packages).

Output: `/home/claude/contracts/normalized/zm_zppa.jsonl` — **1 records** {'end_date_unknown': 1}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/zm_zppa/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T17:43:18Z | 178732 | 1 |
| 2025 | 2026-10-25T18:01:36Z | 84954 | 0 |
| 2024 | 2026-10-25T18:01:42Z | 47224 | 1 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2024`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 890 supplier parties, 890 with an address, **890 with a country value**; address keys {'region': 890, 'locality': 890, 'postalCode': 890, 'countryName': 890, 'streetAddress': 890}; most common country values {'Zambia': 887, 'Canada': 1, 'Greece': 1, 'Cyprus': 1}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'Canada'": 1}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source zm_zppa --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 1, "units": 1, "status_end_date_unknown": 1}`; excluded examples: []

## Result / verdict
Counts by status: {'end_date_unknown': 1}.
Buyers: {'Zambia Medicines and Medical Supplies Agency': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `zm_zppa:ocds-23g63a01-4777933` | Oneworld Accuracy Inc. (VANCOUVER) | Zambia Medicines and Medical Supplies Agency | PROVISION OF EXTERNAL QUALITY ASSRANCE SERVICES  | ZMW 3143647.23 | 2024-03-06 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- 'full' file (178,732 releases) plus 2024/2025 files streamed; the one Canadian supplier appears in both 'full' and 2024 (deduplicated by ocid).

# rw_umucyo — Rwanda – Umucyo e-procurement OCDS (bulk via OCP Data Registry)

Reference date 2026-10-25. Publisher: Rwanda Public Procurement Authority (RPPA). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 145: https://data.open-contracting.org/en/publication/145 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/145 (origin: https://ocds.umucyo.gov.rw/OpenData).

Output: `/home/claude/contracts/normalized/rw_umucyo.jsonl` — **3 records** {'end_date_unknown': 3}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/rw_umucyo/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T17:42:26Z | 4144 | 0 |
| 2025 | 2026-10-25T17:42:45Z | 6962 | 3 |
| 2024 | 2026-10-25T18:01:23Z | 5544 | 2 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 3370 supplier parties, 3370 with an address, **3370 with a country value**; address keys {'locality': 3370, 'countryName': 3370, 'streetAddress': 3370, 'postalCode': 1823, 'region': 27}; most common country values {'Rwanda': 3306, 'India': 9, 'Kenya': 8, 'United States': 6, 'France': 4, 'Tunisia': 3, 'Italy': 3, 'United Kingdom': 3}; contracts with `period.endDate`: 3256.

Values seen on kept records: {"parties[].address.countryName = 'Canada'": 3}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source rw_umucyo --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 5, "units": 6, "excluded_ended": 3, "status_end_date_unknown": 3}`; excluded examples: [['ocds-ozzobm-000006/NC/IRT/2023/2024/0500000000', 'end 2025-06-19 < ref'], ['ocds-ozzobm-000026/C/NCB/2022/2023/1200001000', 'end 2024-06-25 < ref'], ['ocds-ozzobm-000003/C/ICB/2022/2023/1400000000', 'end 2026-09-04 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 3}.
Buyers: {'RWANDA DEVELOPMENT BOARD (RDB)': 2, 'SPIU MINECOFIN': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `rw_umucyo:ocds-ozzobm-000026/C/NCB/2022/2023/1200001000:a4d012aa-2661-4cbd-a465-a86b8b6f9c25` | Mutalikanwa Umutesi Nathalie (CAN) | SPIU MINECOFIN | 000026/C/NCB/2022/2023/SPIU MINECOFIN | USD 83490.0 | 2023-01-16 → None | end_date_unknown | None
- `rw_umucyo:ocds-ozzobm-000009/C/NCB/2023/2024/0108000000` | 1379684 Ontario Ltd (CAN) | RWANDA DEVELOPMENT BOARD (RDB) | 000009/C/NCB/2023/2024/RDB | RWF 985999.0 | 2024-12-31 → None | end_date_unknown | None
- `rw_umucyo:ocds-ozzobm-000033/NC/SS/2024/2025/0108000000` | Greenheart Canopy Walkway Company Ltd. (CAN) | RWANDA DEVELOPMENT BOARD (RDB) | 000033/NC/SS/2024/2025/RDB | RWF 725825429.28 | 2025-05-09 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- One kept vendor is a natural person (Mutalikanwa Umutesi Nathalie) with address country Canada; kept as published.

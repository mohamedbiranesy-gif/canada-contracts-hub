# it_mit — Italy – Ministry of Infrastructure and Transport OCDS (2022–2024)

Reference date 2026-10-25. Publisher: Ministero delle Infrastrutture e dei Trasporti, Italy. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 141: https://data.open-contracting.org/en/publication/141 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/141.

Output: `/home/claude/contracts/normalized/it_mit.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/it_mit/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T20:01:42Z | 9155 | 1 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2148 supplier parties, 903 with an address, **439 with a country value**; address keys {'region': 758, 'countryName': 439}; most common country values {'IT': 432, 'DE': 2, 'IE': 2, 'LV': 1, 'FR': 1, 'NL': 1}; contracts with `period.endDate`: 0.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source it_mit --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 1, "units": 1, "status_end_date_unknown": 1}`; excluded examples: []

## Result / verdict
Supplier country field IS published (see probe) but 0 releases had a supplier whose address country denotes Canada in the files streamed. **Checked, 0 Canadian-supplier records.**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- 1 Canadian-supplier release found (GIRO Inc., Montreal, country CA): ocds-8mw9gh-scp-1562025, 'CANONE ANNUALE MANUTENZIONE ED ASSISTENZA ATTINENTE IL SISTEMA HASTUS 2022', award 2021-12-26, EUR 74,691 (buyer via Liguria regional platform). No period published, but the title states the annual fee is for 2022 → inferred end 2022-12-31 < 2026-10-25 → **excluded** (same convention as FAO 'for <year>' POs). No output file written.

# is_opentender — Iceland – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (source mainly TED). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 57: https://data.open-contracting.org/en/publication/57 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/57 (origin: https://opentender.eu/).

Output: `/home/claude/contracts/normalized/is_opentender.jsonl` — **2 records** {'end_date_unknown': 2}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/is_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:49:05Z | 3959 | 6 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 2}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source is_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 6, "units": 7, "status_end_date_unknown": 5, "excluded_inferred_ended": 2}`; excluded examples: [['ocds-70d2nz-c8be0908-5842-4e5f-ad66-032f280eba83', 'inferred end 2022-08-07 < ref'], ['ocds-70d2nz-c8be0908-5842-4e5f-ad66-032f280eba83', 'inferred end 2022-08-07 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 2}.
Buyers: {'Rikiskaup (The State Trading Centre)': 2}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `is_opentender:ocds-70d2nz-56b06167-3dc2-4374-b2aa-ce1317853d2f` | Field Aviation Company Inc. (None) | Rikiskaup (The State Trading Centre) |  | None None | 2007-05-07 → None | end_date_unknown | None
- `is_opentender:ocds-70d2nz-8571df7b-2868-469e-9692-ed80ed9fce76` | Atlantic Industries (None) | Rikiskaup (The State Trading Centre) |  | None None | 2006-12-08 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Iceland: 5 → 0 (pass 1) → 3 (pass 2) → 2 kept.

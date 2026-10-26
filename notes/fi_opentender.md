# fi_opentender — Finland – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (source mainly TED). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 51: https://data.open-contracting.org/en/publication/51 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/51 (origin: https://opentender.eu/).

Output: `/home/claude/contracts/normalized/fi_opentender.jsonl` — **4 records** {'end_date_unknown': 4}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/fi_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:48:49Z | 87649 | 15 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 4}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source fi_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 15, "units": 15, "status_end_date_unknown": 12, "excluded_inferred_ended": 1, "excluded_ended": 2}`; excluded examples: [['ocds-70d2nz-556f0010-5d45-4b5f-9110-b3032f332870', 'inferred end 2016-08-12 < ref'], ['ocds-70d2nz-84c14027-1aae-45dc-b098-ef9027428f2b', 'end 2020-12-31 < ref'], ['ocds-70d2nz-948c98c5-cd68-4bb7-a2ce-c062b75309ac', 'end 2008-03-31 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 4}.
Buyers: {'Ministry for Foreign Affairs of Finland': 1, 'Oulun yliopisto': 1, 'Geologian tutkimuskeskus': 1, 'Näkövammaisten Keskusliitto ry': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `fi_opentender:ocds-70d2nz-18eacf60-2086-4c42-adc7-1828c0df1fe8:award-3` | The Universalia Management Group Limited (None) | Ministry for Foreign Affairs of Finland | Framework Agreement on the performance of meta-evaluations, syntheses, reviews,  | EUR None | 2013-03-29 → None | end_date_unknown | None
- `fi_opentender:ocds-70d2nz-6b5056d3-7076-4bc6-ab29-653b83dbc385` | Visual Sonics (None) | Oulun yliopisto |  | EUR 273300.0 | 2009-09-10 → None | end_date_unknown | None
- `fi_opentender:ocds-70d2nz-b39683b7-a7b1-4d90-aabe-d7a807af6c9f` | Fugro Airborne Surveys Corp. (None) | Geologian tutkimuskeskus | Airborne gravity survey. | EUR 295000.0 | 2011-06-08 → None | end_date_unknown | None
- `fi_opentender:ocds-70d2nz-c54bcc02-b4cb-42cf-b23b-6852513417f3` | Technologies HumanWare Canada Inc. (None) | Näkövammaisten Keskusliitto ry |  | EUR 456300.0 | 2008-04-21 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Finland: 12 → 6 (pass 1) → 2 (pass 2) → 4 kept.

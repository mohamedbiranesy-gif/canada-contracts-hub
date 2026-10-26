# se_opentender — Sweden – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (source mainly TED). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 90: https://data.open-contracting.org/en/publication/90 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/90 (origin: https://opentender.eu/).

Output: `/home/claude/contracts/normalized/se_opentender.jsonl` — **8 records** {'end_date_unknown': 8}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/se_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:48:26Z | 163041 | 53 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 8}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source se_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 53, "units": 58, "status_end_date_unknown": 54, "excluded_ended": 2, "excluded_inferred_ended": 2}`; excluded examples: [['ocds-70d2nz-0e714476-e842-40f8-bef3-4732ac2674a5', 'end 2009-12-31 < ref'], ['ocds-70d2nz-1cfbb127-eb1e-411b-b139-7df6e0c2d28f', 'inferred end 2026-05-31 < ref'], ['ocds-70d2nz-50a32e5e-cc7c-446f-be45-0e08dfcf2262', 'inferred end 2015-05-05 < ref'], ['ocds-70d2nz-681eb372-b4b5-4c25-95e5-537df3e61326', 'end 2011-12-31 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 8}.
Buyers: {'Sveriges Television Aktiebolag': 1, 'AB Storstockholms Lokaltrafik': 1, 'AB Svenska Spel': 1, 'Uppsala universitet': 1, 'Umeå universitet': 1, 'Swedish Road Adm., Ferry Operations': 1, 'Högskolan Väst': 1, 'Luleå tekniska universitet': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `se_opentender:ocds-70d2nz-251a7378-abef-487e-9717-38dbc3f6b971` | Vimsoft (None) | Sveriges Television Aktiebolag | Advanced Planning and Sceduling System. | None None | 2011-06-10 → None | end_date_unknown | None
- `se_opentender:ocds-70d2nz-279aee0b-ca60-48ab-82d7-f0b504f07520` | Visual Defence Inc (None) | AB Storstockholms Lokaltrafik |  | None None | 2006-02-28 → None | end_date_unknown | None
- `se_opentender:ocds-70d2nz-312d002a-c887-47a7-8c98-568346c4498d:award-2` | 4028546 Canada Inc. (None) | AB Svenska Spel | Visitor Registration System & Incident Management System. | None None | 2012-04-27 → None | end_date_unknown | None
- `se_opentender:ocds-70d2nz-435fe271-cdd9-479d-ae8f-57b61351559f` | LTG LaserTech Group Inc. (None) | Uppsala universitet | Contract award notice for a near IR, tuneable laser system. | USD 107015.0 | 2010-06-30 → None | end_date_unknown | None
- `se_opentender:ocds-70d2nz-594182b8-f04d-44bc-b67a-c12919fa6c7c` | S&P Robotics Inc. (None) | Umeå universitet | Upphandling - Robotic handling device | SEK 1830855.0 | 2024-03-05 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Sweden: 54 → 15 (pass 1) → 31 (pass 2) → 8 kept.

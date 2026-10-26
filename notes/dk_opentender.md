# dk_opentender — Denmark – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (source mainly TED). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 49: https://data.open-contracting.org/en/publication/49 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/49 (origin: https://opentender.eu/).

Output: `/home/claude/contracts/normalized/dk_opentender.jsonl` — **9 records** {'end_date_unknown': 9}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/dk_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:49:04Z | 56287 | 54 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 9}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source dk_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 54, "units": 55, "status_end_date_unknown": 42, "excluded_inferred_ended": 10, "excluded_ended": 3}`; excluded examples: [['ocds-70d2nz-1745c84f-6047-48f2-9e22-bc580a07ccc2', 'inferred end 2015-06-20 < ref'], ['ocds-70d2nz-1b9d3210-a3e5-499c-8924-143530ac1f82', 'inferred end 2025-04-20 < ref'], ['ocds-70d2nz-31a70654-a795-429e-9f73-c688e6d59457', 'inferred end 2025-04-30 < ref'], ['ocds-70d2nz-460370a9-c04d-4a31-b349-5573d6cdbefb', 'inferred end 2015-07-01 < ref'], ['ocds-70d2nz-47e4501d-c5ef-4cde-807d-91aec5130bc4', 'end 2008-10-31 < ref'], ['ocds-70d2nz-51e2522c-5b27-4b5f-9d82-3eb04e9c0adf', 'inferred end 2013-01-19 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 9}.
Buyers: {'Forsvarsministeriets Materiel- og Indkøbsstyrelse': 2, 'Danske Spil A/S': 2, 'Medicoteknik, Region Syddanmark': 1, 'Geological Survey of Denmark and Greenland (GEUS)': 1, 'Naviair': 1, 'Technical University of Denmark': 1, 'Silkeborg Kraftvarmeværk, SKVV': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `dk_opentender:ocds-70d2nz-25911ce6-4eac-4b56-958a-64a0a61b099c` | Offshore Systems Ltd. (None) | Forsvarsministeriets Materiel- og Indkøbsstyrelse | Purchase of ECPINS v. 6.0. | None None | 2012-01-20 → None | end_date_unknown | None
- `dk_opentender:ocds-70d2nz-317dd4f1-159d-435c-9c0d-7979a14a3d28` | Pollard Banknote Limited (None) | Danske Spil A/S |  | None None | 2008-01-18 → None | end_date_unknown | None
- `dk_opentender:ocds-70d2nz-3a7d5807-72eb-438b-a914-23d93eef8d4a` | GenoLogics Life Sciences Software, (None) | Medicoteknik, Region Syddanmark | Indkøb af LIMS til kræftlaboratoriet på Vejle sygehus. | DKK 1572000.0 | 2012-12-12 → None | end_date_unknown | None
- `dk_opentender:ocds-70d2nz-3af7e55f-f549-4712-ac68-b0ac2bf06077` | Pollard Banknote Limited (None) | Danske Spil A/S | Trykning af skrabelodder. | None None | 2012-10-08 → None | end_date_unknown | None
- `dk_opentender:ocds-70d2nz-48b412bc-2383-40f2-8196-8abcb810ed61:award-1` | EON Geosciences Inc. (None) | Geological Survey of Denmark and Greenland (GEUS) | Aeromag 2012-2013. | None None | 2012-04-16 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Denmark: 42 → 28 (pass 1) → 5 (pass 2) → 9 kept.

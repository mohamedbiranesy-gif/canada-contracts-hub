# eu_institutions_opentender — EU institutions – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (source mainly TED). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 94: https://data.open-contracting.org/en/publication/94 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/94 (origin: https://opentender.eu/).

Output: `/home/claude/contracts/normalized/eu_institutions_opentender.jsonl` — **10 records** {'end_date_unknown': 10}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/eu_institutions_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:49:11Z | 22433 | 42 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 10}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source eu_institutions_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 42, "units": 43, "status_end_date_unknown": 25, "excluded_inferred_ended": 18}`; excluded examples: [['ocds-70d2nz-3094c79e-878a-48ca-a65a-43fc34d475d7', 'inferred end 2017-12-06 < ref'], ['ocds-70d2nz-50943e6e-bf8d-470f-9aee-5e895ab2fe78', 'inferred end 2025-11-16 < ref'], ['ocds-70d2nz-4a9fadb4-7b4a-4bc3-9dd8-9f55db8eb6ef', 'inferred end 2014-12-02 < ref'], ['ocds-70d2nz-8f0b1eb1-76cf-4acd-a204-4cf57f1c5c67', 'inferred end 2021-03-07 < ref'], ['ocds-70d2nz-7a38c319-c177-49fb-befa-dadd88be046b', 'inferred end 2017-11-14 < ref'], ['ocds-70d2nz-77fc97bf-37eb-4832-a795-47182e8082bc', 'inferred end 2021-06-21 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 10}.
Buyers: {'European Commission, Directorate-General for Energy': 2, 'European Maritime Safety Agency': 1, 'European Commission, Directorate-General for Research and Innovation': 1, 'European Commission, Directorate-General for Humanitarian Aid (ECHO), Unit A1 — AN88 04/055': 1, 'Europol': 1, 'European Commission, Directorate-General for Research and Innovation, Directorate B, Unit B.7': 1, 'European Commission, OLAF': 1, 'European Commission, Joint Research Centre, Institute for Energy': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `eu_institutions_opentender:ocds-70d2nz-e50398fe-dec6-4963-a052-122d0d5169c1` | McDonald Dettwiller Associates Geospatial Services Inc. (MDA GSI Inc.) (None) | European Maritime Safety Agency | Framework service contract for multi-user licence for Radarsat-2 for EMSA earth  | EUR 5000000.0 | 2013-12-31 → None | end_date_unknown | None
- `eu_institutions_opentender:ocds-70d2nz-1f5c3ba7-a84a-4de5-aeec-0e67ced3f227:award-1` | Science Metrix (None) | European Commission, Directorate-General for Research and Innovation | Call for tenders for a framework contract for the provision of services to the C | EUR 6500000.0 | 2012-08-31 → None | end_date_unknown | None
- `eu_institutions_opentender:ocds-70d2nz-538c9489-d13f-4d11-b3bf-f94dea9d673f` | DAC International Aviation Limited (None) | European Commission, Directorate-General for Humanitarian Aid (ECHO), Unit A1 — AN88 04/055 |  | EUR 8100000.0 | 2009-12-14 → None | end_date_unknown | None
- `eu_institutions_opentender:ocds-70d2nz-c240605d-d3ca-4d76-9c9a-9e436ea1374c` | Amita Corporation (None) | Europol |  | EUR 540000.0 | 2009-11-12 → None | end_date_unknown | None
- `eu_institutions_opentender:ocds-70d2nz-e3733d06-7c1e-4977-a28e-44009662b587` | Science-Metrix Inc. (None) | European Commission, Directorate-General for Research and Innovation, Directorate B, Unit B.7 | 'She Figures 2015'_RTD-B6-PP-00963-2013. | EUR 474890.0 | 2014-09-24 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- EU institutions (Commission, agencies, etc.): 25 → 11 (pass 1) → 4 (pass 2) → 10 kept; buyer.country null (institution seat not mapped).

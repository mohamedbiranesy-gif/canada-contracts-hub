# ch_opentender — Switzerland – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (sources: TED and SIMAP). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 91: https://data.open-contracting.org/en/publication/91 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/91 (origin: https://opentender.eu/ch/).

Output: `/home/claude/contracts/normalized/ch_opentender.jsonl` — **8 records** {'end_date_unknown': 8}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/ch_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:30:53Z | 149176 | 13 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 883 supplier parties, 663 with an address, **663 with a country value**; address keys {'postalCode': 663, 'countryName': 663, 'street': 660}; most common country values {'CH': 617, 'DE': 22, 'AT': 5, 'FR': 5, 'CZ': 2, 'MD': 2, 'FI': 2, 'IT': 2}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 8}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source ch_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 13, "units": 13, "status_end_date_unknown": 12, "excluded_inferred_ended": 1}`; excluded examples: [['ocds-70d2nz-5b525df7-678a-4fe2-9572-e50987c7e053', 'inferred end 2015-03-09 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 8}.
Buyers: {'Eidgenössisch Technische Hochschule Zürich Schweizerischer Erdbebendienst': 2, 'Paul Scherrer Institut': 2, 'Eidgenössische Technische Hochschule Zürich Schweizerischer Erdbebendienst': 1, 'Faculté des sciences de la vie': 1, 'École Polytechnique Fédérale de Lausanne (EPFL) SV – Flow Cytometry Core Facility (PTCF)': 1, 'Armasuisse Ausrüstung und Bekleidung': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `ch_opentender:ocds-70d2nz-07e1fd2a-616b-4fb1-a0ec-e91bcbfc315a` | Nanometrics Inc. (None) | Eidgenössische Technische Hochschule Zürich Schweizerischer Erdbebendienst |  | None None | 2010-03-25 → None | end_date_unknown | None
- `ch_opentender:ocds-70d2nz-09fb5699-33e9-432d-a000-65f1a981b541` | Visual Sonics (None) | Faculté des sciences de la vie |  | None None | 2009-09-25 → None | end_date_unknown | None
- `ch_opentender:ocds-70d2nz-221c27a0-0a9b-422b-a560-f2caafd445c4:award-2` | Nanometrics INC. (None) | Eidgenössisch Technische Hochschule Zürich Schweizerischer Erdbebendienst | Capteurs et enregistreurs pour le réseau sismique digital Suisse SDSNet. | None None | 2014-06-04 → None | end_date_unknown | None
- `ch_opentender:ocds-70d2nz-36aa6f2a-3d16-4ab6-8dcd-01580bae0a14` | Ontario Power Generation Inc. (None) | Paul Scherrer Institut |  | EUR 394244.23 | 2007-09-20 → None | end_date_unknown | None
- `ch_opentender:ocds-70d2nz-62176ee3-f270-4f9e-a8c1-15cf77cca885:award-2` | Nanometrics INC. (None) | Eidgenössisch Technische Hochschule Zürich Schweizerischer Erdbebendienst | Capteurs et enregistreurs pour le réseau (sismique) accérélométrique Suisse SSMN | None None | 2014-03-28 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Switzerland: 12 → 2 dropped (pass 1) → 2 dropped (pass 2) → 8 kept. SIMAP national notices are covered separately by `ch_simap`.

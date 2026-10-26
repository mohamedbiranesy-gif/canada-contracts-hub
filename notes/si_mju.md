# si_mju — Slovenia – Ministry of Public Administration e-JN / ENAROČANJE OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Ministrstvo za javno upravo (Ministry of Public Administration), Slovenia. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 82: https://data.open-contracting.org/en/publication/82 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/82 (origin: https://www.enarocanje.si/).

Output: `/home/claude/contracts/normalized/si_mju.jsonl` — **10 records** {'end_date_unknown': 10}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/si_mju/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:32:06Z | 25142 | 10 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 5389 supplier parties, 5389 with an address, **5389 with a country value**; address keys {'region': 5389, 'locality': 5389, 'postalCode': 5389, 'countryName': 5389, 'streetAddress': 5389}; most common country values {'Slovenija': 5209, 'Hrvaška': 48, 'Nemčija': 25, 'Združene države Amerike': 18, 'Avstrija': 17, 'Francija': 11, 'Švedska': 8, 'Španija': 8}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'Kanada'": 10}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source si_mju --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 10, "units": 10, "status_end_date_unknown": 10}`; excluded examples: []

## Result / verdict
Counts by status: {'end_date_unknown': 10}.
Buyers: {'UNIVERZA V MARIBORU': 6, 'Akademska in raziskovalna mreža Slovenije': 2, 'NUKLEARNA ELEKTRARNA KRŠKO d.o.o.': 1, 'UNIVERZA V LJUBLJANI, FAKULTETA ZA STROJNIŠTVO': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `si_mju:ocds-mnnhvj-JN000434/2023-C01:JN000434/2023-C01-1007418` | Canadian Internet Registration Authority (Ottawa, Ontario) | Akademska in raziskovalna mreža Slovenije | Anycast 2022/pogajanja | EUR 25830.0 | 2023-01-30 → None | end_date_unknown | None
- `si_mju:ocds-mnnhvj-JN000434/2023-C02:JN000434/2023-C02-1007704` | Canadian Internet Registration Authority (Ottawa, Ontario) | Akademska in raziskovalna mreža Slovenije | Anycast 2022/pogajanja | EUR 17912.17 | 2023-01-30 → None | end_date_unknown | None
- `si_mju:ocds-mnnhvj-JN004363/2021-C01` | Intlvac Inc. (Georegetown) | UNIVERZA V MARIBORU | Nabava sistema za depozicijo tankih plasti | EUR 583000.0 | 2021-11-29 → None | end_date_unknown | None
- `si_mju:ocds-mnnhvj-JN004363/2021-Q02` | Intlvac Inc. (Georegetown) | UNIVERZA V MARIBORU | Nabava sistema za depozicijo tankih plasti | EUR 583000.0 | 2021-11-29 → None | end_date_unknown | None
- `si_mju:ocds-mnnhvj-JN004363/2021-Q01` | Intlvac Inc. (Georegetown) | UNIVERZA V MARIBORU | Nabava sistema za depozicijo tankih plasti | EUR 583000.0 | 2021-11-29 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- Slovenian e-JN OCDS publishes supplier address with country names in Slovene ('Kanada'). No contract periods → all `end_date_unknown`.

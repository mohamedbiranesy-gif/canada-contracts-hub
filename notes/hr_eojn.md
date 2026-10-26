# hr_eojn — Croatia – EOJN RH contract register (OCDS, via OCP Data Registry)

Reference date 2026-10-25. Publisher: Narodne novine d.d. (Elektronički oglasnik javne nabave RH). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 80: https://data.open-contracting.org/en/publication/80 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/80 (origin: https://eojn.nn.hr/SPIN/application/ipn/Oglasnik/PreuzimanjeUgovoraOCD.aspx).

Output: `/home/claude/contracts/normalized/hr_eojn.jsonl` — **6 records** {'end_date_unknown': 6}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/hr_eojn/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T17:41:44Z | 302465 | 6 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 3000 supplier parties, 3000 with an address, **2997 with a country value**; address keys {'locality': 3000, 'postalCode': 3000, 'streetAddress': 3000, 'countryName': 2997}; most common country values {'HRV': 2779, 'HR ': 185, 'AUT': 5, 'DEU': 5, 'USA': 4, 'UK ': 4, 'SVN': 3, 'CZE': 2}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'CAN'": 6}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source hr_eojn --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 6, "units": 6, "status_end_date_unknown": 6}`; excluded examples: []

## Result / verdict
Counts by status: {'end_date_unknown': 6}.
Buyers: {'MINISTARSTVO UNUTARNJIH POSLOVA': 4, 'HRVATSKI GEOLOŠKI INSTITUT': 1, 'Zadarska županija': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `hr_eojn:ocds-lae55o-1062892` | Phoenix Geophysics Limited (ZAGREB) | HRVATSKI GEOLOŠKI INSTITUT | Nabava opreme za magnetnoteleuriku i audiomagnetoteluriku | HRK 1384785.0 | 2018-06-04 → None | end_date_unknown | None
- `hr_eojn:ocds-lae55o-1167506` | Ultra Electronics Forensic Technology Inc (Zagreb) | MINISTARSTVO UNUTARNJIH POSLOVA | Usluga održavanja i servisiranja opreme i softvera balističkog sustava IBIS | HRK 83814.0 | 2018-12-19 → None | end_date_unknown | None
- `hr_eojn:ocds-lae55o-1836240` | Ultra Electronics Forensic Technology Inc (Zagreb) | MINISTARSTVO UNUTARNJIH POSLOVA | Usluga održavanja i servisiranja opreme i softvera balističkog sustava IBIS | HRK 89635.0 | 2021-07-01 → None | end_date_unknown | None
- `hr_eojn:ocds-lae55o-2037808` | Ultra Electronics Forensic Technology Inc (Zagreb) | MINISTARSTVO UNUTARNJIH POSLOVA | Usluga održavanja i servisiranja balističkog sustava IBIS | HRK 95102.0 | 2022-04-14 → None | end_date_unknown | None
- `hr_eojn:ocds-lae55o-2087948` | Industrial Plankton Inc. (Zadar) | Zadarska županija | Nabava opreme za recirkulacijsku akvakulturu školjkaša  u sklopu prekograničnog  | HRK 589000.0 | 2022-07-27 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- Croatian EOJN contract register records Canadian suppliers with country CAN but often a Croatian locality (e.g. Ultra Electronics Forensic Technology Inc, locality ZAGREB) - kept as published; country field is authoritative per brief.
- EOJN publishes no contract end dates in OCDS -> all `end_date_unknown`.

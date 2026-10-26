# nl_tenderned — Netherlands – TenderNed open data (OCDS, via OCP Data Registry)

Reference date 2026-10-25. Publisher: Ministry of Economic Affairs and Climate Policy / TenderNed (PIANOo), Netherlands. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 133: https://data.open-contracting.org/en/publication/133 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/133 (origin: https://www.tenderned.nl/cms/nl/aanbesteden-in-cijfers/datasets-aanbestedingen).

Output: `/home/claude/contracts/normalized/nl_tenderned.jsonl` — **27 records** {'end_date_unknown': 21, 'ongoing': 2, 'ongoing_inferred': 4}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/nl_tenderned/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T17:42:12Z | 139654 | 29 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 3883 supplier parties, 3883 with an address, **3883 with a country value**; address keys {'countryName': 3883, 'locality': 3882, 'postalCode': 3502, 'streetAddress': 3501, 'streetAddressDetails': 62}; most common country values {'Nederland': 2993, 'NL': 815, 'Duitsland': 19, 'België': 11, 'Verenigde Staten': 8, 'Verenigd Koninkrijk': 8, 'Frankrijk': 4, 'Zwitserland': 3}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'Canada'": 27}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source nl_tenderned --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 29, "units": 31, "status_end_date_unknown": 21, "excluded_inferred_ended": 3, "status_ongoing": 2, "status_ongoing_inferred": 4, "excluded_ended": 1}`; excluded examples: [['ocds-1l04xe-283211', 'inferred end 2022-12-06 < ref'], ['ocds-1l04xe-373095', 'inferred end 2023-02-27 < ref'], ['ocds-1l04xe-374047', 'inferred end 2023-03-10 < ref'], ['ocds-1l04xe-470862', 'end 2025-12-31 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 21, 'ongoing': 2, 'ongoing_inferred': 4}.
Buyers: {'Technische Universiteit Delft': 5, 'Ministerie van Infrastructuur en Waterstaat': 4, 'TenneT TSO': 3, 'Brabant Water NV': 3, 'Commando Materieel en iT (COMMIT)': 2, 'HTM Personenvervoer N.V.': 1, 'Erasmus MC': 1, 'Enexis Netbeheer BV/Enexis Personeel BV': 1}.

`record_url`: template `['tenderNotice']`; example https://www.tenderned.nl/aankondigingen/overzicht/164473

## Five sample records
- `nl_tenderned:ocds-1l04xe-133794:Liftking Manufacturing Corp.` | Liftking Manufacturing Corp. (Woodbridge) | Commando Materieel en iT (COMMIT) | European public procurement Container Lifting Trucks and Spreaders | EUR 1.0 | 2019-04-19 → None | end_date_unknown | https://www.tenderned.nl/aankondigingen/overzicht/164473
- `nl_tenderned:ocds-1l04xe-167213` | RTDS Technologies Inc (Winnipeg) | Technische Universiteit Delft | Real-Time Power system simulation tool | EUR 347400.0 | 2017-11-10 → None | end_date_unknown | https://www.tenderned.nl/aankondigingen/overzicht/126564
- `nl_tenderned:ocds-1l04xe-260393` | Giro Inc. (Montreal) | HTM Personenvervoer N.V. | Operationeel planningsysteem | EUR 1600000.0 | 2020-03-14 → None | end_date_unknown | https://www.tenderned.nl/aankondigingen/overzicht/246328
- `nl_tenderned:ocds-1l04xe-283566:-2` | Nanometrics Inc (Kanata) | Ministerie van Infrastructuur en Waterstaat | Procurement of E-TEST Equipment | EUR None | 2021-06-24 → None | end_date_unknown | https://www.tenderned.nl/aankondigingen/overzicht/231732
- `nl_tenderned:ocds-1l04xe-283566:-1` | Nanometrics Inc (Kanata) | Ministerie van Infrastructuur en Waterstaat | Procurement of E-TEST Equipment | EUR None | 2021-06-24 → None | end_date_unknown | https://www.tenderned.nl/aankondigingen/overzicht/231732

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- record_url built from the tenderNotice document link, rewritten to `https://www.tenderned.nl/aankondigingen/overzicht/<id>`; verified https://www.tenderned.nl/aankondigingen/overzicht/126564 -> HTTP 200 (SPA).
- The registry file is a single 'full' file (139,654 releases, 2016–present).
- European (above-threshold) TenderNed notices are also in TED: possible overlap with `ted_eu` — de-duplicate at merge.

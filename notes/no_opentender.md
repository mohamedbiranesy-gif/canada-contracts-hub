# no_opentender — Norway – OpenTender (DIGIWHIST/Government Transparency Institute) procurement data as OCDS, via OCP Data Registry

Reference date 2026-10-25. Publisher: Government Transparency Institute / opentender.eu (sources: TED and Doffin). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 72: https://data.open-contracting.org/en/publication/72 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/72 (origin: https://opentender.eu/no/).

Output: `/home/claude/contracts/normalized/no_opentender.jsonl` — **22 records** {'end_date_unknown': 22}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/no_opentender/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| full | 2026-10-25T19:30:29Z | 82893 | 49 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `full`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2252 supplier parties, 2251 with an address, **2247 with a country value**; address keys {'countryName': 2247, 'postalCode': 2095, 'street': 1954}; most common country values {'NO': 2151, 'SE': 31, 'DK': 14, 'DE': 10, 'UK': 8, 'IS': 5, 'US': 4, 'FI': 3}; contracts with `period.endDate`: 0.

Values seen on kept records: {"parties[].address.countryName = 'CA'": 22}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source no_opentender --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 49, "units": 51, "status_end_date_unknown": 40, "excluded_inferred_ended": 5, "excluded_ended": 6}`; excluded examples: [['ocds-70d2nz-27dbbc99-4af5-4a99-ae5e-0318daf95f8a', 'inferred end 2022-06-27 < ref'], ['ocds-70d2nz-45a81231-015a-4f31-b686-0f944354665a', 'end 2020-02-28 < ref'], ['ocds-70d2nz-668a2f36-d3c7-4139-8117-bbc52d709bbc', 'end 2018-03-31 < ref'], ['ocds-70d2nz-69bb25a1-88fd-43eb-b08f-e84ffc0f7aa8', 'end 2016-07-15 < ref'], ['ocds-70d2nz-7c782a7c-8497-42ef-a6f3-3f648c00b12a', 'inferred end 2017-09-16 < ref'], ['ocds-70d2nz-96c00fb7-5ce8-45d3-b439-f390dc7d735d', 'inferred end 2019-05-17 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 22}.
Buyers: {'Geological Survey of Norway (NGU)': 5, 'Norsk Polarinstitutt (Norwegian Polar Institute)': 3, 'Forsvarets logistikkorganisasjon (FLO)/Forsyningsavdeling Østlandet/Innkjøpsseksjonen': 2, 'The Geological Survey of Norway (NGU)': 2, 'Forsvarets forskningsinstitutt': 1, 'Norges Bank – NBIM': 1, 'Norsk Tipping AS': 1, 'Jernbaneverket': 1}.

`record_url`: null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists).

## Five sample records
- `no_opentender:ocds-70d2nz-029c62e8-6318-44ae-a1d1-d52bf26f64d4` | Telops Inc. (None) | Forsvarets forskningsinstitutt | 30-2011. Imaging Fourier-transform infrared spectrometer. | None None | 2011-12-19 → None | end_date_unknown | None
- `no_opentender:ocds-70d2nz-13e3c5bf-16bb-40f3-80a4-08868049b143` | QuIC Financial Technologies (None) | Norges Bank – NBIM |  | EUR 400000.0 | 2009-03-27 → None | end_date_unknown | None
- `no_opentender:ocds-70d2nz-1737bac1-63d4-438b-8af1-2438e374863b` | Satlantic Inc (None) | Norsk Polarinstitutt (Norwegian Polar Institute) | Nitrate Sensor. | None None | 2011-08-12 → None | end_date_unknown | None
- `no_opentender:ocds-70d2nz-199f3267-df07-40c1-acdb-2bbc762cde18` | ASL Environmental Sciences (None) | Norsk Polarinstitutt (Norwegian Polar Institute) | Processing of ASL IPS5 data, as well as older CMR ES300 data. | NOK 2900000.0 | 2011-08-26 → None | end_date_unknown | None
- `no_opentender:ocds-70d2nz-2cdbd070-6c1d-4cba-ab24-34ff7d224269` | Pollard Banknote Ltd (None) | Norsk Tipping AS | Production of scratch tickets with accompanying consultancy services. | None None | 2011-01-04 → None | end_date_unknown | None

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.
- Registry data ends Dec 2024; normalize stats below are before de-duplication.
- Norway: 40 normalised → 6 dropped (pass 1) → 12 dropped (pass 2) → 22 kept. Doffin itself not crawled (API key required, see notes/no_doffin.md).

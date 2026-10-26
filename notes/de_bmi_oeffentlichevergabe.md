# de_bmi_oeffentlichevergabe — Germany – oeffentlichevergabe.de (Datenservice Öffentlicher Einkauf) eForms notices as OCDS (bulk via OCP Data Registry)

Reference date 2026-10-25. Publisher: Beschaffungsamt des Bundesministeriums des Innern (BMI), Germany. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 136: https://data.open-contracting.org/en/publication/136 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/136 (origin: https://www.oeffentlichevergabe.de/documentation/swagger-ui/opendata/index.html).

Output: `/home/claude/contracts/normalized/de_bmi_oeffentlichevergabe.jsonl` — **32 records** {'end_date_unknown': 23, 'ongoing': 6, 'ongoing_inferred': 3}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/de_bmi_oeffentlichevergabe/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T17:40:34Z | 170876 | 13 |
| 2025 | 2026-10-25T17:41:09Z | 220282 | 12 |
| 2024 | 2026-10-25T18:00:52Z | 220154 | 26 |
| 2023 | 2026-10-25T18:01:12Z | 186855 | 2 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2231 supplier parties, 2231 with an address, **2231 with a country value**; address keys {'locality': 2231, 'countryName': 2231, 'postalCode': 2230, 'region': 2227, 'streetAddress': 1948}; most common country values {'DEU': 2202, 'NLD': 10, 'AUT': 6, 'GBR': 4, 'IRL': 2, 'DNK': 2, 'CHE': 2, 'ALB': 1}; contracts with `period.endDate`: 0.

Values seen on kept records: {"awards[].suppliers[].address.countryName = 'CAN'": 3, "parties[].address.countryName = 'CAN'": 29}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source de_bmi_oeffentlichevergabe --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 40, "units": 40, "status_end_date_unknown": 23, "excluded_inferred_ended": 4, "excluded_ended": 4, "status_ongoing": 6, "status_ongoing_inferred": 3}`; excluded examples: [['ocds-mnwr74-00440745-f0fe-43ad-84d6-a16158d48a17', 'inferred end 2025-03-16 < ref'], ['ocds-mnwr74-018f9f8f-60b7-4230-a039-48d80fc4ae4d', 'end 2024-11-05 < ref'], ['ocds-mnwr74-1ff8408e-a6f3-4527-9e60-85c97511f185', 'inferred end 2025-12-16 < ref'], ['ocds-mnwr74-dbd27cbf-c8b2-4edd-9258-a246f8aeb182', 'end 2026-03-31 < ref'], ['ocds-mnwr74-02fc6ee5-04ad-4502-9779-73b393de1f4e', 'end 2025-12-31 < ref'], ['ocds-mnwr74-2ae47a29-52a4-44d4-af91-28f742d7e015', 'inferred end 2026-01-10 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 23, 'ongoing': 6, 'ongoing_inferred': 3}.
Buyers: {'Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ) GmbH': 4, 'Bundesamt für Wirtschaft und Ausfuhrkontrolle (BAFA)': 4, 'Bundesamt für Ausrüstung, Informationstechnik und Nutzung der Bundeswehr': 1, 'Bundesanstalt für Geowissenschaften und Rohstoffe': 1, 'Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e. V.': 1, 'Julius-Maximilians-Universität Würzburg als staatliche Einrichtung in Vertretung des FS Bayern': 1, 'Freie Universität Berlin Abteilung II: Finanzen, Einkauf und Stellenwirtschaft Referat II C - Zentraler Einkauf': 1, 'Technische Universität München': 1}.

`record_url`: template `https://www.oeffentlichevergabe.de/ui/de/search/details/{tender_id}`; example https://www.oeffentlichevergabe.de/ui/de/search/details/0e127264-cf01-43e8-a082-52bd7c0bfe69

## Five sample records
- `de_bmi_oeffentlichevergabe:ocds-mnwr74-0e127264-cf01-43e8-a082-52bd7c0bfe69` | Rheinmetall Canada Inc (Saint-Jean-sur-Richelieu) | Bundesamt für Ausrüstung, Informationstechnik und Nutzung der Bundeswehr | Instandhaltung von Air Startern für diverse Lfz im Werk des UAN in Deutschland | None None | 2023-03-26 → None | end_date_unknown | https://www.oeffentlichevergabe.de/ui/de/search/details/0e127264-cf01-43e8-a082-52bd7c0bfe69
- `de_bmi_oeffentlichevergabe:ocds-mnwr74-75ce8117-4d1f-4fe8-be3b-0c28512c8e95` | Canadian Scientific Submersible Facility (NORTH SAANICH BC) | Bundesanstalt für Geowissenschaften und Rohstoffe | Charterung eines ROV-Systems | None None | 2023-05-15 → None | end_date_unknown | https://www.oeffentlichevergabe.de/ui/de/search/details/75ce8117-4d1f-4fe8-be3b-0c28512c8e95
- `de_bmi_oeffentlichevergabe:ocds-mnwr74-0b662268-fa62-4e38-b234-6bb1c37f59c9` | CPCS Transcom Limited (Ottawa) | Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ) GmbH | Contract Award CPCS Transcom Limited | None None | 2023-11-24 → None | end_date_unknown | https://www.oeffentlichevergabe.de/ui/de/search/details/0b662268-fa62-4e38-b234-6bb1c37f59c9
- `de_bmi_oeffentlichevergabe:ocds-mnwr74-1a692001-0c7c-40b5-96b8-985f86ce057b` | Square Peg Communications Inc. (Ottawa, Ontario) | Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e. V. | PR780069 - Satellite Chanel Emulator | EUR 80730.0 | 2024-09-30 → None | end_date_unknown | https://www.oeffentlichevergabe.de/ui/de/search/details/1a692001-0c7c-40b5-96b8-985f86ce057b
- `de_bmi_oeffentlichevergabe:ocds-mnwr74-27567748-9f19-45c8-88ef-dfa085545a45` | Angstrom Engineering, Inc. (Cambridge, Ontario) | Julius-Maximilians-Universität Würzburg als staatliche Einrichtung in Vertretung des FS Bayern | Dual-Ionenstrahlanlage Technische Physik 2024 | EUR None | 2024-05-12 → None | end_date_unknown | https://www.oeffentlichevergabe.de/ui/de/search/details/27567748-9f19-45c8-88ef-dfa085545a45

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- record_url `https://www.oeffentlichevergabe.de/ui/de/search/details/<notice uuid>` returns HTTP 200 (single-page app shell, content rendered client-side); verified for 1a692001-0c7c-40b5-96b8-985f86ce057b on 2026-10-25.
- eForms data starts 2023 (German eForms go-live); 2023 file covers only part of the year.
- Above-threshold German notices are also published in TED: some records may duplicate `ted_eu` (e.g. GIZ, BAAINBw awards) — de-duplicate at merge on buyer + vendor + title/notice id.

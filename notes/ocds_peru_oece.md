# ocds_peru_oece - Peru: Organismo Especializado para las Contrataciones Públicas Eficientes (OECE)

Source: OCP Data Registry publication 135, https://data.open-contracting.org/en/publication/135 . Files streamed (never stored whole) on 2026-11-12 from
`https://data.open-contracting.org/en/publication/135/download?name=<file>` : 2022.jsonl.gz,2023.jsonl.gz,2024.jsonl.gz,2025.jsonl.gz,2026.jsonl.gz (compiled OCDS releases, one per line, gzip).
Script: contrib/claude/ocds_peru_oece/harvest.py (wrapper over contrib/claude/ocds_common/ocds_harvest.py).

## Counts (reference date 2026-11-12)
- Releases seen in those files: 473944
- Releases with a Canada-addressed party: 246
- Awards to Canadian suppliers (supplier linked to a Canada-addressed party): 194
- Dropped: ended before reference date 184; no end date and award/contract older than 2024-11-12 2; cancelled/unsuccessful 1; buyer unnamed 0
- Records written: 7 (ongoing 5, end_date_unknown 2); distinct buyers 4

## How Canada was determined
A party in `parties[]` whose own `address.countryName` (or `address.country`) is Canada / CA / CAN / Canada (accented or Spanish forms), with role `supplier`, linked to an award through `awards[].suppliers[].id`.
Where the release's awards carry no supplier list at all (eForms-style publications), the party with role `supplier` and a Canadian address is used and the record's `vendor.country_basis` says so.
No name-based inference. The exact field and value are written in `vendor.country_basis`.

## How status was determined
`ongoing`: contracts[].period.endDate (else awards[].contractPeriod.endDate) >= 2026-11-12 and start / signing / award date <= 2026-11-12.
`end_date_unknown`: no end date in the release and the award/contract date is 2024-11-12 or later (older ones dropped). Ended ones dropped.

## Records
One per (award, Canadian supplier). Whole matching release under `raw.release`. `link` = first `sources[].url` of the release if present, else the registry publication page. Buyer country (PE) is the publisher's country; buyer identifiers/address/contact from the buyer party.
Latest end date in the file: 2028-04-15. Possible overlap: publications derived from EU/TED notices (e.g. German BMI eForms) may duplicate rows from the TED source.

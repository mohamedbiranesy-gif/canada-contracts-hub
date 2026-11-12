# ocds_netherlands_ministry_of_economic_affairs_a - Netherlands: Ministry of Economic Affairs and Climate Policy

Source: OCP Data Registry publication 133, https://data.open-contracting.org/en/publication/133 . Files streamed (never stored whole) on 2026-11-12 from
`https://data.open-contracting.org/en/publication/133/download?name=<file>` : 2022.jsonl.gz,2023.jsonl.gz,2024.jsonl.gz,2025.jsonl.gz,2026.jsonl.gz (compiled OCDS releases, one per line, gzip).
Script: contrib/claude/ocds_netherlands_ministry_of_economic_affairs_a/harvest.py (wrapper over contrib/claude/ocds_common/ocds_harvest.py).

## Counts (reference date 2026-11-12)
- Releases seen in those files: 79327
- Releases with a Canada-addressed party: 22
- Awards to Canadian suppliers (supplier linked to a Canada-addressed party): 23
- Dropped: ended before reference date 0; no end date and award/contract older than 2024-11-12 15; cancelled/unsuccessful 0; buyer unnamed 0
- Records written: 8 (ongoing 0, end_date_unknown 8); distinct buyers 6

## How Canada was determined
A party in `parties[]` whose own `address.countryName` (or `address.country`) is Canada / CA / CAN / Canada (accented or Spanish forms), with role `supplier`, linked to an award through `awards[].suppliers[].id`.
Where the release's awards carry no supplier list at all (eForms-style publications), the party with role `supplier` and a Canadian address is used and the record's `vendor.country_basis` says so.
No name-based inference. The exact field and value are written in `vendor.country_basis`.

## How status was determined
`ongoing`: contracts[].period.endDate (else awards[].contractPeriod.endDate) >= 2026-11-12 and start / signing / award date <= 2026-11-12.
`end_date_unknown`: no end date in the release and the award/contract date is 2024-11-12 or later (older ones dropped). Ended ones dropped.

## Records
One per (award, Canadian supplier). Whole matching release under `raw.release`. `link` = first `sources[].url` of the release if present, else the registry publication page. Buyer country (NL) is the publisher's country; buyer identifiers/address/contact from the buyer party.
Latest end date in the file: n/a. Possible overlap: publications derived from EU/TED notices (e.g. German BMI eForms) may duplicate rows from the TED source.

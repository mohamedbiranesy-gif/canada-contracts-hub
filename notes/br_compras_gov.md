# br_compras_gov — Brazil – Compras.gov.br (federal) OCDS

Reference date 2026-10-25. Publisher: Ministério da Gestão e da Inovação em Serviços Públicos, Brazil. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 157: https://data.open-contracting.org/en/publication/157 .

Output: `/home/claude/contracts/normalized/br_compras_gov.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/br_compras_gov/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T18:23:12Z | 187568 | 0 |
| 2025 | 2026-10-25T18:23:48Z | 293131 | 0 |
| 2024 | 2026-10-25T18:26:45Z | 279205 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 3697 supplier parties, 0 with an address, **0 with a country value**; address keys {}; most common country values {}; contracts with `period.endDate`: 0.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
Supplier parties carry NO address at all (0 of 3,697 supplier parties in a 3,000-release sample have `address`); suppliers identified only by CNPJ/CPF. Foreign suppliers cannot be identified structurally. 0 matches in 2024–2026 files. **Rejected: no supplier country/address field.** (The federal PNCP contracts API marks foreign suppliers only with `tipoPessoa`=PE (pessoa estrangeira) — no country — so it cannot establish Canada either.)

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.

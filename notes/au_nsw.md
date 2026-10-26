# au_nsw — Australia – New South Wales eTendering (NSW Treasury) OCDS

Reference date 2026-10-25. Publisher: NSW Treasury / NSW Procurement (buy.nsw). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 11: https://data.open-contracting.org/en/publication/11 .

Output: `/home/claude/contracts/normalized/au_nsw.jsonl` — **0 records** (none written).

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/au_nsw/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2024 | 2026-10-25T19:29:53Z | 9174 | 0 |
| 2023 | 2026-10-25T19:29:55Z | 3763 | 0 |
| 2022 | 2026-10-25T19:29:58Z | 2365 | 0 |
| 2025 | 2026-10-25T19:29:59Z | 3019 | 0 |
| 2021 | 2026-10-25T19:30:01Z | 2091 | 0 |
| 2020 | 2026-10-25T19:30:03Z | 1469 | 0 |
| 2019 | 2026-10-25T19:30:04Z | 1430 | 0 |
| 2018 | 2026-10-25T19:30:06Z | 1507 | 0 |
| 2017 | 2026-10-25T19:30:08Z | 1313 | 0 |
| 2016 | 2026-10-25T19:30:10Z | 1490 | 0 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

## How "ongoing" was determined
Not applicable (no Canadian-supplier releases).

## Result / verdict
The registry copy of NSW eTendering contains planning/tender releases and awards whose `suppliers[]` carry only name + ABN (+ `ABNExempt` flag) — **no supplier address** (8,243 award suppliers in the 2024 file, all without address). 0 matches 2016–2025. The live NSW eTendering contract-notice API (`https://tenders.nsw.gov.au/?event=public.api.contract.search`) now redirects to `https://buy.nsw.gov.au/`, which returned **HTTP 403 (CloudFront 'Request blocked')** on 2026-10-25 19:3x UTC — not bypassed. **Rejected (no country in open copy; live portal blocked).**

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.

# ca_alberta_apc — Alberta Purchasing Connection (APC), awarded opportunities

Status: COMPLETE (crawl finished 2026-10-25T18:59:46Z; normalized 2026-10-25T19:02Z, 6,484 records).

## Source
- Portal: https://purchasing.alberta.ca (Government of Alberta; covers GoA ministries, agencies, municipalities,
  school boards, Alberta Health Services, post-secondaries and other Alberta public bodies posting on APC).
- Public JSON API (no login, no bot challenge):
  - Search: `POST https://purchasing.alberta.ca/api/opportunity/search` with filter `statuses=[{value:"AWARD"}]`,
    `postDateRange=$$custom`, monthly `postDateStart/postDateEnd` windows 2010-01 .. 2026-10 (windows > 1,000 hits
    split into daily windows; API refuses offsets >= 1,000). 10,694 distinct awarded reference numbers
    (`downloads/ca_alberta_apc/search_hits.jsonl`, 31 MB). Phase 1 ran 2026-10-25T17:34:41Z–17:37:28Z.
  - Detail: `GET https://purchasing.alberta.ca/api/opportunity/public/{year}/{number}` for each `AB-YYYY-NNNNN`
    -> `downloads/ca_alberta_apc/details/AB-YYYY-NNNNN.json` (10,694 files, ~580 MB, 0 failures).
    Phase 2 ran 17:37Z–18:59Z (three passes: forward, reverse, reverse; resumable, skips files on disk).
- Script: `scripts/ca_alberta_apc/crawl_apc.py` (≈3 req/s), normaliser `scripts/ca_alberta_apc/normalize_apc.py`
  (stats in `downloads/ca_alberta_apc/normalize_stats.json`).

## Canadian vendor
`awards[].address.country` (values seen: `CA`/`Canada` kept; `US` 634, `United States` 296, `DE` 8, `GB` 11,
`ZZ` 7, others ≤4 excluded). Province from `awards[].address.stateProvince` (e.g. `CA-AB` -> `AB`), city and postal code
from the same address block. `vendor.country_basis` records the exact value. No record lacked a country, so there
is no `_unverified_country` file.

## Ongoing logic
- `ongoing`: `opportunity.deliveryStartDate` ≤ 2026-10-25 ≤ `opportunity.deliveryEndDate` (contract/delivery
  period published on the posting); or only `deliveryEndDate` ≥ ref with award date ≤ ref.
- `end_date_unknown`: no delivery dates on the posting (award date shown in status_basis).
- Excluded: delivery end < ref (6,433 award rows), not started (47), cancelled, non-CA vendors (~990).
- One record per award row (an opportunity can have several suppliers): `record_id = ca_alberta_apc:<ref>:<award uuid>`.

## Counts
13,955 award rows on 10,694 opportunities -> **ongoing 5,617; end_date_unknown 867** (total 6,484).

## record_url
`https://purchasing.alberta.ca/posting/<AB-YYYY-NNNNN>` — verified 2026-10-25: `/posting/AB-2025-04827` HTTP 200
(SPA shell, 108 KB); the matching API detail `/api/opportunity/public/2025/4827` HTTP 200 (14.7 KB JSON).

## raw
`raw.search_hit` (full search row), `raw.detail` (complete detail JSON incl. all awards, commodity codes, contacts,
documents metadata, amendments fields), `raw.award` (the award row this record is about).

## Samples
- ca_alberta_apc:AB-2024-06808:… | ongoing | Infrastructure | THE WORKUN GARRICK PARTNERSHIP Architecture and Interior Design Inc., Edmonton AB | 4,298,000 | 2024-08-30 – 2028-12-31
- ca_alberta_apc:AB-2025-01973:… | ongoing | Town of Stony Plain | The Inspections Group Inc., Edmonton AB | 356,000 | 2025-05-09 – 2028-05-08
- ca_alberta_apc:AB-2025-06464:… | ongoing | Canadian Centre of Recovery Excellence | Shift Consulting Inc., Banff AB | 890,000 | 2025-11-17 – 2028-11-17
- ca_alberta_apc:AB-2026-02044:… | ongoing | Jobs, Economy, Trade and Immigration | Bredin Centre for Career Advancement, Edmonton AB | 664,990 | 2026-07-01 – 2029-12-31
- ca_alberta_apc:AB-2015-00540:… | end_date_unknown | Service Alberta and Red Tape Reduction | WALDALE MANUFACTURING LIMITED, Amherst NS | 0 (standing offer)

## Known gaps
- Only postings with status AWARD; postings closed/"evaluation" without published award are not included.
- Delivery dates are the posting's planned contract period, not amendments/extensions after award.
- Award amount 0 is common for standing offers / rate-based awards (kept as published).
- Sole-source/direct awards are separately in `ca_alberta_sole_source` (Open Alberta CSV); some overlap possible.

## Storage note (2026-10-25T20:05Z)
The shared disk filled up; to free space the 10,694 detail files were gzipped in place
(`downloads/ca_alberta_apc/details/AB-YYYY-NNNNN.json.gz`, content unchanged). `normalize_apc.py` now reads both
`.json` and `.json.gz`. `crawl_apc.py` checks for `.json` only, so a re-crawl would refetch — not needed (crawl complete).

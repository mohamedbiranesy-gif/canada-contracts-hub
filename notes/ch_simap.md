# ch_simap — simap.ch (Switzerland) award publications, vendor address in Canada

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/ch_simap.jsonl`: **2 records** {'end_date_unknown': 2}.

## What was downloaded
Public API of the new simap.ch (OpenAPI spec https://www.simap.ch/api/specifications/simap.yaml, Swagger UI https://www.simap.ch/api-doc/). Listing: `GET https://www.simap.ch/api/publications/v2/project/project-search?newestPubTypes=award_tender&newestPubTypes=award_study_contract&newestPubTypes=award_competition&newestPublicationFrom=<month start>&newestPublicationUntil=<month end>[&lastItem=<cursor>]` (20 per page). Detail of every listed award: `GET https://www.simap.ch/api/publications/v1/project/<projectId>/publication-details/<publicationId>`. For matches only, the referenced tender publication (`referencingPub`) is fetched the same way (cache `downloads/ch_simap/ref_cache/`). Crawler `scripts/ch_simap/crawl.py` (3 workers on disjoint months, ≈3 req/s total), started 2026-10-25 19:49 UTC; listing of every award seen `downloads/ch_simap/listing.jsonl`; matches (full JSON) `downloads/ch_simap/matches.jsonl`; per-month log `downloads/ch_simap/crawl.log`. **Direct awards (`direct_award`, freihändige Vergabe) were not crawled** (volume/time; a first test run included them).

Months completed (award publications seen / with Canadian vendor):

| month | finished (UTC) | awards | Canadian |
|---|---|---|---|
| 2026-10 | 2026-10-25T19:54:37Z | 595 | 0 |
| 2026-09 | 2026-10-25T19:58:09Z | 861 | 1 |
| 2026-08 | 2026-10-25T19:56:34Z | 741 | 1 |

Total awards examined: 2197. **Months not completed in the time box: 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-08, 2024-09, 2024-10, 2024-11, 2024-12, 2025-01, 2025-02, 2025-03, 2025-04, 2025-05, 2025-06, 2025-07, 2025-08, 2025-09, 2025-10, 2025-11, 2025-12, 2026-01, 2026-02, 2026-03, 2026-04, 2026-05, 2026-06, 2026-07.**

## Canadian vendor
`decision.vendors[].vendorAddress.countryId` = `CA` (structured ISO code; street, city, postal code kept in `vendor.address`). Names never used.

## Ongoing
Award publications carry only `decision.awardDecisionDate`; contract periods are, at best, in the referenced tender publication (`procurement.contractDeadlineType`/`executionDeadlineType` and period/duration fields). `scripts/ch_simap/normalize.py` reads any period start/end found there; when none is given (typically `not_specified`) the record is `end_date_unknown` with the award decision date as anchor.

normalize stats: `{"end_date_unknown": 2}`

## record_url
`https://www.simap.ch/en/project-detail/<projectId>#<publicationId>` — verified for project c2262a97-8ba9-4579-a65b-96456ff95b3a (HTTP 200, single-page app). API detail URL is reproducible from `contract.identifiers`.

## Records
- `ch_simap:37665-02:Photon_Etc_Inc` | Photon Etc. Inc (Montréal) | Empa zentraler Einkauf | Hyperspectral Photoluminescence Imaging System | USD 479560.0 | award 2026-09-29 | end_date_unknown
- `ch_simap:35112-03:NOSOTECH_inc_` | NOSOTECH inc. (Rimouski) | Swissnoso, Nationales Zentrum für Infektionsprävention | IPC Platform ‘Surveillance and Prevention of Healthcare-Associated Infections’ | CHF 4809437.21 | award 2026-08-13 | end_date_unknown

## Known gaps
- Direct awards and months listed as not completed are missing.
- Publications from the old simap (pre-2024 platform) that were migrated as 'external' may lack vendor addresses.
- Above-threshold Swiss awards are not in TED (CH is not EU); `ch_opentender` (TED-derived) is a different, older population.

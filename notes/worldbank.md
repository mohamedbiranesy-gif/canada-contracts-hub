# worldbank — World Bank (IBRD/IDA) contract awards to Canadian suppliers

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/worldbank.jsonl` (310 records). Scripts: `/home/claude/contracts/scripts/worldbank/{fetch_wb.py,normalize_wb.py}`. Downloads: `/home/claude/contracts/downloads/worldbank/`.

## Source situation
The Socrata dataset **kdui-wcs3** ("Major Contract Awards") named in the task no longer exists: `https://finances.worldbank.org/resource/kdui-wcs3.json` → 302 → `https://financesone.worldbank.org/resource/kdui-wcs3.json`, which is the Finances One single-page app (HTML, no SODA API). Finances One replaced it with three IPF contract-award datasets plus an API documented at https://financesone.worldbank.org/api-explorer?id=DS00005 (base `https://datacatalogapi.worldbank.org/dexapps/fone/api/apiservice`, params `datasetId`, `resourceId`, `top` ≤ 1000, `skip`, `type=json`, `filter=<SQL-like>`). Resource IDs were taken from the API-explorer pages (they are not in the metadata endpoint).

## What was downloaded (2026-10-25 12:48 UTC)
| Dataset | API call | Rows (Canada) | File |
|---|---|---|---|
| DS01004 / RS00934 "Contract Awards in Investment Project Financing (since FY 2001 - FY 2016)" (data as of 11-Mar-2022, frozen) | `...apiservice?datasetId=DS01004&resourceId=RS00934&type=json&filter=supplier_country='Canada'&top=1000&skip=N` | 1 158 | `fone_DS01004_RS00934_canada.json` (901 KB) |
| DS04691 / RS03933 "… (since FY 2017 - FY 2019)" (as of 25-Oct-2026) | same pattern | 217 | `fone_DS04691_RS03933_canada.json` |
| DS00005 / RS00005 "… (Since FY 2020)" (as of 25-Oct-2026; 296 098 rows total) | same pattern | 614 | `fone_DS00005_RS00005_canada.json` |
| DS00028 / RS00025 "Corporate Procurement Contract Awards" (WBG itself as buyer; as of 30-Jun-2026) | same pattern | 79 | `fone_DS00028_RS00025_canada.json` |
| Metadata | `https://datacatalogapi.worldbank.org/dexapps/fone/api/metadata?assetId=<DS>` | — | `meta_DS*.json` |
| Projects API | `https://search.worldbank.org/api/v2/projects?format=json&id=<P1,P2,…20>&fl=id,project_name,status,closingdate,boardapprovaldate,countryshortname,countrycode,totalamt,url,impagency,borrower,lendprojectcost,approvalfy,regionname,projectstatusdisplay,lendinginstr,…` | 1 072 distinct project ids, 1 072 answered, 992 with a status (80 very old projects return only `id`+`url`) | `projects.json` (2.4 MB) |
| Procurement notices API | `https://search.worldbank.org/api/v2/procnotices?format=json&notice_type=Contract Award&qterm="Country: Canada"&rows=100&os=N&srt=noticedate&order=desc` | 1 245 Contract Award notices mentioning "Country: Canada" (436 with a Canadian **awarded** firm/bidder; the rest list Canadian firms only as evaluated/rejected bidders) | `procnotices_canada.json` (5.8 MB) |

All columns of every row are kept verbatim in `raw.finances_one_row`; the project record in `raw.project`; the matched procurement notice (full HTML `notice_text` + parsed fields) in `raw.procurement_notice*`.

## How "Canadian vendor" was determined
`supplier_country = 'Canada'` (server-side filter; `supplier_country_code = CA` where present). Per the dataset description this is the *place of supplier registration*, and joint-venture amounts are split equally among members. For the procurement-notice feed: the `Country: Canada` line under **Awarded Firm(s)/Awarded Bidder(s)** in the notice text (notices where Canada appears only under Evaluated/Rejected firms are ignored: 810). Corporate procurement: `supplier_country = 'Canada'`.

## How "ongoing" was determined (status_basis states which rule fired)
1. **Duration from the matching procurement notice** — IPF rows were matched to Contract Award notices on `project_id` + `borrower_contract_reference_number == bid_reference_no` (37 matches; 103 notices with a Canadian awardee had no feed row and were emitted as their own `worldbank:procnotice:<id>` records). Notices state "Duration of Contract: N Month(s)/Week(s)/Day(s)/Year(s)" → computed end = `contract_signing_date` (or award-notification date) + duration → `ongoing_inferred` if ≥ 2026-10-25, else excluded (398 excluded).
2. **Project status/closing date** (Projects API) — status `Active` and `closingdate` ≥ 2026-10-25 → `ongoing_inferred` (the project closing date bounds disbursement under the contract); `Closed`/`Dropped`, or `Active` with closing date already passed → excluded (1 336 + 130); `Active` without closing date, `Pipeline`, or project record empty/not found → `end_date_unknown`.
3. Corporate procurement rows (award date and amount only) → `end_date_unknown`.
Rows signed after the reference date (FY2027 rows, 20) are kept as `end_date_unknown` with a note.

## Counts
| status | records |
|---|---|
| ongoing_inferred | 112 (99 FY2020+ feed, 2 FY2001-16 feed, 1 FY2017-19 feed, 10 procurement-notice-only) |
| end_date_unknown | 198 (49 FY2001-16, 35 FY2017-19, 33 FY2020+, 2 procurement-notice-only, 79 corporate procurement) |
| **total** | **310** |
Excluded: 1 864 (reasons in `downloads/worldbank/normalize_stats.json`).

## record_url / dataset_url
Finances One has no per-row page → `source.record_url = null`; `contract.related.project_url = https://projects.worldbank.org/en/projects-operations/project-detail/<PID>` (verified pattern returned by the Projects API `url` field, e.g. https://projects.worldbank.org/en/projects-operations/project-detail/P151416), `contract.related.dataset_api` = the exact API call. Procurement-notice records: `record_url = https://projects.worldbank.org/en/projects-operations/procurement-detail/<OP id>`. `source.dataset_url = https://financesone.worldbank.org/d/<DS id>`.

## Buyer
`buyer.name` = Projects API `borrower` / `impagency` (implementing agency) when available, else "<borrower country> (borrower; implementing agency not published)"; `buyer.country` = ISO-3166 alpha-2 mapped from the borrower country name (World Bank's own codes such as ZR, YF, 3W are kept in `buyer.identifiers.wb_borrower_country_code`; regional programmes → null). The World Bank is the financier, not the buyer, except in the corporate-procurement feed where `buyer` = World Bank Group unit (type IGO).

## Known gaps / limits
* No contract end dates anywhere in the feeds; `ongoing_inferred` relies on either the notice duration or the project closing date (which can be later than the contract's real end).
* Suppliers have no address beyond "Canada" in the feed (notice address captured when a notice matched).
* `supplier_contract_amount(_usd)` is a USD equivalent; the notice's signed price in original currency is in `value_detail.signed_contract_price_notice` when matched.
* 80 of 1 072 projects (pre-2010) return no status from the Projects API → `end_date_unknown`.
* The procnotices search is full-text (`qterm="Country: Canada"`); notices that spell the country differently would be missed.

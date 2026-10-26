# other_igo — other international organizations / development banks (IDB, EBRD; ADB, AfDB, NSPA, ESA attempted)

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/other_igo.jsonl` (11 records: 10 IDB, 1 EBRD). Scripts: `/home/claude/contracts/scripts/other_igo/{fetch_ebrd.py,normalize_igo.py}`. Downloads: `/home/claude/contracts/downloads/other_igo/<org>/`. `source.name` identifies the organization per record.

## Inter-American Development Bank (IDB) — done
* Dataset: "IDB Project Procurement Contract Awards Data" (CKAN package `idb-project-procurement-contract-awards-data`, DOI https://doi.org/10.60966/coo0rbyd, temporal coverage 2010 → 2024+, metadata modified 2026-10-01). Landing: https://data.iadb.org/dataset/idb-project-procurement-contract-awards-data. Datastore resource `dd09c605-9cd8-49c5-92dc-191ff6ecdd58`.
* Retrieval (2026-10-25 13:28 UTC): `https://data.iadb.org/api/3/action/datastore_search?resource_id=dd09c605-9cd8-49c5-92dc-191ff6ecdd58&filters={"awarded_firm_country_name":"CANADA"}&limit=1000&include_total=true` → 383 rows (`idb/idb_contract_awards_canada.json`, 449 KB). Fields: contract_id, contract_type, project_number/name, status (ACTIVE/EXITED), operation_number/type, operation_country, sector, procurement_type, idb_amount, total_amount, borrower, executing_agency, awarded_firm_country_code/name, awarded_firm_city/address/name, contract_year, signature_date, entry_date, last_modification_date, start_date, stop_date, source. All kept in `raw.idb_row`.
* Canadian vendor: `awarded_firm_country_name = 'CANADA'`. **Caution:** IDB's `awarded_firm_country_code` for Canada is `CD`; code `CA` means "Central American sub-region" (2 rows, not Canadian, excluded by filtering on the name). 138 of 383 rows are individual consultants / "Not Available" names.
* Ongoing: `start_date ≤ today and stop_date ≥ 2026-10-25` → `ongoing` (5); no stop_date but `status = ACTIVE` → `ongoing_inferred` (5); stop_date passed (324) or EXITED without stop (49) → excluded (listed in `normalize_stats.json`).
* Buyer = `borrower_name / executing_agency`, country from `operation_country_name` (ISO2 mapped). `record_url` null (no per-row page); `contract.related.project_url = https://www.iadb.org/en/project/<project_number>`.
* The second IDB dataset ("bidding notices and notification of contract awards", resource `856aabfd-…`) has no supplier fields → not used.

## European Bank for Reconstruction and Development (EBRD) — done
* ECEPP notice search https://ecepp.ebrd.com/delta/noticeSearch.html embeds all 4 118 public notices server-side (3.9 MB; 2026-10-25 13:26 UTC) → 1 134 "Contract Award Notice" rows (2016 → 2026) listed in `ebrd/award_list.json`; every award notice page `https://ecepp.ebrd.com/delta/viewNotice.html?displayNoticeId=<id>` downloaded to `ebrd/notices/<id>.html` (1 134 files, 23.7 MB).
* Canadian vendor: address block of the awarded party ("2. Contracting Party" in the 2023+ layout; "Awarded Tenderer(s)" in the older layout) ends with `Canada`, or a JVCA partner address contains ", Canada". Only **2** awards went to a Canadian-addressed party: 10424900 (IATA, Montreal → Tajik Air Navigation, 2020, no duration → `end_date_unknown`, kept) and 8800636 (Manitoba Hydro International JV → Moldelectrica, award 2019-09-09, "Duration of Contract: 48" months → computed end 2023-09-09 → excluded). Nine other notices mention Canadian firms only as evaluated (losing) bidders or JV partners of non-awarded bidders.
* Ongoing rule: "Contract Scheduled Completion Date" (new layout) → `ongoing`; else "Duration of Contract" + "Contract Award Date" → `ongoing_inferred`/excluded; else `end_date_unknown`.
* Note: EBRD award notices cover EBRD-financed public-sector projects only (clients are municipalities, utilities, ministries); EBRD's own corporate procurement is not published per award.

## Attempted, blocked or not usable within the time-box
| Organization | What was tried | Result |
|---|---|---|
| **Asian Development Bank** | data.adb.org (search, dataset pages, `/media/<id>/download`) | Cloudflare JS challenge → HTTP 403 for every URL. adb.org "procurement statistics" page offers only aggregates; contract-level awards exist only in per-project Procurement Plan PDFs (not scalable in the time-box). |
| **African Development Bank** | afdb.org procurement / contract-awards pages | Cloudflare → HTTP 403. No open data API found. |
| **NATO Support and Procurement Agency (NSPA)** | nspa.nato.int contract-award pages (403, Cloudflare); eportal.nspa.nato.int → redirects to login (`idp.nspa.nato.int/my.logout.php3?errorcode=19`) | Awards are only visible to registered suppliers. |
| **European Space Agency (esa-star)** | https://esastar-publication-ext.sso.esa.int/ESATenderActions | Angular SPA; the 4.9 MB `main-es2015` bundle downloads at <20 KB/s through the proxy (timed out at 1 MB) so the JSON API behind it could not be identified. Contract award lists ("Contracts awarded" per ITT) are also only exposed inside the app. |
| World Bank | — | covered separately in `worldbank.md` |
| UN agencies | — | covered separately in `ungm.md` |

## Counts
| org | status | records |
|---|---|---|
| IDB | ongoing | 5 |
| IDB | ongoing_inferred | 5 |
| EBRD | end_date_unknown | 1 |
| **total** | | **11** |

Excluded: IDB 373 (324 stop_date passed, 49 EXITED without stop date), EBRD 1 (duration elapsed).

## record_url
IDB: none per row (`record_url = null`; dataset landing page in `dataset_url`; project page in `contract.related.project_url`, e.g. https://www.iadb.org/en/project/HA-J0005). EBRD: `https://ecepp.ebrd.com/delta/viewNotice.html?displayNoticeId=10424900` — verified HTTP 200, "Tajikistan: … Ebrd Contract Award Notice … International Air Transport Association, 800 Place Victoria, Montreal, Canada".

# private_press — publicly announced commercial contracts of Canada-based vendors (press releases)

Reference date 2026-10-25. Output `normalized/private_press.jsonl` — **216 records: 27 `ongoing`, 58 `ongoing_inferred`, 131 `end_date_unknown`**. Built 2026-10-25 between ~08:00 and 10:36 local by an earlier worker; this note was reconstructed afterwards from its scripts (`scripts/private_press/`), downloads (`downloads/private_press/`) and outputs, because that worker was stopped before writing it.

## What was collected
- Candidate discovery (all files in `downloads/private_press/`):
  - newswire.ca (Cision CNW) "contracts" subject lists and category lists → `candidates_newswire.jsonl` (905 releases), fetched releases in `fetched_newswire.jsonl`, raw HTML in `html/`.
  - prnewswire.com lists (all + Canada) → `candidates_prnewswire.jsonl` (4,920) and `candidates_prnewswire_ca.jsonl` (225).
  - keyword search crawls across wires (GlobeNewswire, Business Wire, ACCESS Newswire, Newsfile) → `candidates_search.jsonl` (14,525 search hits); company newsroom crawls for large Canadian vendors (`company_slugs*.txt`) → `candidates_company_filtered.jsonl` (715); a later backlog `candidates_round3_backlog.jsonl` (1,119, not processed).
  - Supplier-award pages of Irving Shipbuilding ("Our Stories") and Canadian Commercial Corporation announcements.
- Filtering (`digest.py` + `extract_lib.py`): headline must contain a contract keyword (award, contract, agreement, selects, signs, wins, renews, supply, MSA, framework…); excluded financing, M&A, MOUs/LOIs/non-binding agreements, grants, results, appointments, etc.; excluded releases whose counterparty is unnamed ("a leading…", "undisclosed customer"); dateline must be a Canadian city/province or the vendor's "About" boilerplate must give a Canadian head office.
- Every kept release was reviewed and curated into `downloads/private_press/curated/batch01…07*.jsonl` (vendor, buyer, term/duration, value, dates, evidence), then turned into records by `build_records.py` / `build_records_webfetch.py` (for releases readable only through WebFetch).

## Canadian vendor
`vendor.country_basis` states the evidence per record: press-release dateline city/province and/or the "About <company>" boilerplate giving a Canadian head office; TSX/TSXV tickers kept in `vendor.identifiers`. Names are never used alone.

## Ongoing logic
- `ongoing`: the release states an end date (or start + explicit end) on/after 2026-10-25.
- `ongoing_inferred`: the release states a term ("three-year agreement", "five-year contract") → announce/start date + term ≥ 2026-10-25 (arithmetic in `status_basis`).
- `end_date_unknown`: signed contract announced, no term stated.
- Excluded: stated term already ended.

## Counts
216 records; sources: newswire.ca 115, GlobeNewswire 53, Business Wire 12, Irving Shipbuilding newsroom 12, CCC announcements 10, company newsrooms 5, others 9. Buyer countries: CA 95, US 68, GB 8, DE 6, AU 5, others. Announcement years: 2026 149, 2025 51, 2024 11, 2023 4, 2022 1.

## record_url
The press release URL itself (always present).

## Known gaps / limits
- A sample by construction, not a census: most business-to-business contracts are never announced, and announcements often omit the counterparty, value or term.
- Wire coverage is strongest for 2025–2026; older releases were only partly crawled; `candidates_round3_backlog.jsonl` (1,119 candidates) was never reviewed.
- SEDAR+ (Canadian securities filings, where material contracts are filed) could not be used: it serves a bot-check page (see `notes/sedar_plus.md`).

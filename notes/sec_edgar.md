# sec_edgar — material contracts of Canada-located SEC filers (EDGAR full-text search)

Reference date 2026-10-25. Output `normalized/sec_edgar.jsonl` — **28 records: 6 `ongoing`, 16 `ongoing_inferred`, 6 `end_date_unknown`**. Built 2026-10-25 (~09:30–10:21 local) by an earlier worker; this note was reconstructed from `scripts/sec_edgar/` and `downloads/sec_edgar/` because that worker was stopped before writing it.

## What was collected
- EDGAR full-text search API (efts.sec.gov/LATEST/search-index) queried for 8-K Item 1.01 ("Entry into a Material Definitive Agreement"), 6-K, 10-K/20-F/40-F exhibits (EX-10.x material contracts) with contract/supply/services/licence phrasing, restricted to filers whose business address is in Canada (`harvest_efts*.py`) → `downloads/sec_edgar/hits.jsonl` (13,655 hits).
- Shortlisted filings and exhibits fetched from www.sec.gov/Archives (`fetch_docs.py`, `fetch_more.py`, `fetch_sel.py`) → `downloads/sec_edgar/docs/`, indexed in `docs_index.jsonl` (890 documents).
- Each kept agreement was curated by hand (parties, effective date, term, end date, value where stated) into `downloads/sec_edgar/curated/`, then turned into records by `build_records.py`.

## Canadian vendor
The filer is the vendor/supplier party and its EDGAR business address is in Canada (state/country code of a Canadian province); `vendor.country_basis` says so. Agreements where the Canadian filer is the buyer were not kept.

## Ongoing logic (`build_records.py::status_for`)
- `ongoing`: exhibit states a fixed end date ≥ 2026-10-25.
- `ongoing_inferred`: no fixed end, but an initial term in years (effective/signed date + term ≥ 2026-10-25), or an evergreen/condition-based term clause with the agreement in force at filing.
- `end_date_unknown`: no term information.
- Excluded: stated or computed end before the reference date.

## record_url
The EDGAR filing / exhibit URL.

## Known gaps / limits
- Only Canadian companies that file with the SEC (cross-listed issuers) are covered; Canadian-only issuers file on SEDAR+, which is behind a bot check (not used).
- Exhibits are often redacted (prices, sometimes counterparty names); redacted counterparties were not kept.
- 28 curated agreements out of 13,655 search hits: precision-first manual curation, far from exhaustive.

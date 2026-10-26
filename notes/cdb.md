# cdb — Caribbean Development Bank: Contract Awards

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/cdb.jsonl`: **7 records** (2 `ongoing_inferred`, 5 `end_date_unknown`).

## Downloaded
`https://www.caribank.org/work-with-us/procurement/contract-awards?solr_publication_contract_awards_years_filter=<YYYY>&page=<n>` for 2012–2026 (57 page requests, 2026-10-25 19:33–19:34 UTC, ≤1.5 req/s; HTML in `downloads/cdb/awards_<year>_p<nn>.html`, log `downloads/cdb/fetch.log`). Script `scripts/cdb/fetch_parse.py` → `downloads/cdb/rows.json` (**434 award rows**). Normaliser `scripts/cdb/normalize.py`.

## Canadian vendor
The listing column **"Winning Bid"** is published as `<bidder country> - <firm> | <amount>` (e.g. `Canada - Le Groupe Conseil Baastel Ltée | USD 133,363.80`); rows whose winning bid starts with `Canada -` → 19 rows (Canada is the 4th most frequent bidder country after Belize, St Lucia, Jamaica). Firm names are not used for the decision.
One duplicate (Aecon Construction Group, Kingstown Port Modernisation, USD 155,303,809.73 + EUR 12.3 M, listed under 2022 and 2023) merged → 18 candidate records (other listing in `raw.rows`), 7 kept after the date check.

## Ongoing
The listing itself has no dates. Each row links a "Contract Award Information" notice (docx/pdf, `source.record_url`); 13 of the 18 have one. They were downloaded 2026-10-25 ~19:58 UTC to `downloads/cdb/docs/` (text extracted to `*.txt`; docx via word/document.xml, pdf via pdftotext) and the lines **"Commencement Date of Contract"** and **"Duration of Contract"** parsed (dateutil; "(n)" or digits + day/week/month/year). Commencement + duration ≥ 2026-10-25 → `ongoing_inferred` (arithmetic in `status_basis`, parsed text in `contract.related.award_notice_terms`); < 2026-10-25 → excluded (**11 excluded**, listed in `downloads/cdb/excluded_ended.json`, e.g. Aecon Kingstown port 2022-05-12 + 42 months = 2025-11-12; Stantec Montserrat 2019 + 38 months). The 5 rows without a linked notice (all 2022 listings) stay `end_date_unknown`. The notices also carry a "Country of Bidder" column, consistent with the listing's "Canada - " prefix.

## Buyer
CDB-financed contracts are procured by the borrowing government's executing agency (named in the linked award notice). `buyer.name` = "Government of <country> – executing agency of CDB-financed project '<project>'"; where the listing country is "CDB"/"Regional" (CDB's own or regional TA procurement) buyer = Caribbean Development Bank.

## Records
- Le Groupe Conseil Baastel Ltée | FORMULATION OF A MEDIUM-TERM DEVELOPMENT STRATEGY AND INVESTMENT PLAN (MTDSIP),  | Government of Saint Kitts and Nevis – executing agency of CDB-financed | USD 133363.8 | 2026-06-30 → 2026-12-30 | ongoing_inferred
- BAASTEL | GA 18/BHA Disaster Resilience Improvement Project | Government of The Bahamas – executing agency of CDB-financed project ' | USD 209035.0 | 2026-05-27 → 2027-11-27 | ongoing_inferred
- Tomopa Canada Ltd. | Regional Capacity Building in Municipal Finances | Caribbean Development Bank | USD 39400.0 | None → None | end_date_unknown
- Ozz Electric Inc. | Energy Efficiency Measures and Solar Photovoltaic Plant | Government of Saint Vincent and the Grenadines – executing agency of C | USD 1468364.94 | None → None | end_date_unknown
- CBCL Limited | Reconciliation and Rehabilitation Grant - Barbuda Energy Resilience Project | Government of Antigua and Barbuda – executing agency of CDB-financed p | USD 700317.0 | None → None | end_date_unknown
- Golota Isaac Lamah | Millennium Highway and West Coast Road Reconstruction Project | Government of Saint Lucia – executing agency of CDB-financed project ' | USD 128000.0 | None → None | end_date_unknown
- Christine Scott International Consulting Inc. | Philip Goldson Highway and Remate Bypass Upgrading Project | Government of Belize – executing agency of CDB-financed project 'Phili | USD 150362.0 | None → None | end_date_unknown

## Gaps
Rows without a linked award notice cannot be dated; amounts parsed from free text (currency as written); buyer is the borrower government, not the specific executing agency (not named in the notices).

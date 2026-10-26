# ungm — United Nations Global Marketplace contract awards to suppliers in Canada

Reference date: 2026-10-25. Output: `/home/claude/contracts/normalized/ungm.jsonl` (287 records). Scripts: `/home/claude/contracts/scripts/ungm/{fetch_ungm.py,normalize_ungm.py}`. Downloads: `/home/claude/contracts/downloads/ungm/`.

## What was downloaded (2026-10-25 13:16–13:40 UTC)
* `https://www.ungm.org/Public/ContractAward` (166 KB) — the public search page; provides the `__RequestVerificationToken` (hidden input + cookie) and the country picker, where **Canada = option value `2328`** (`#selContractAwardSupplierCountry`).
* `/Scripts/UNGM.js`, `/bundles/ungmcommon?v=w9iy…` (663 KB) — read to discover the search call: `UNGM.ContractAwardSearch.buildOptions()` → `POST https://www.ungm.org/Public/ContractAward/PublicSearch`, `Content-Type: application/json`, header `RequestVerificationToken: <token>`, body `{"PageIndex":n,"PageSize":15,"Title":"","Description":"","Reference":"","Supplier":"","UngmNumber":"","AwardFrom":"","AwardTo":"","Countries":[],"SupplierCountries":["2328"],"Agencies":[],"UNSPSCs":[],"SortField":"AwardDate","SortAscending":false}`. The server honours `PageSize` up to at least 500; crawl used 100 → 3 pages (`search_pages/page_000[0-2].html`), **288 award ids** (`search_summary.json`).
* `https://www.ungm.org/Public/ContractAward/<id>` for each of the 288 ids → `details/<id>.html` (full page; the `<main>` section is embedded in `raw.detail_main_html`). UNGM throttles detail pages (HTTP 429 above ~0.5 req/s); the crawler sleeps 2.5 s between requests and honours Retry-After.

## How "Canadian vendor" was determined
Server-side filter `SupplierCountries=["2328"]` (= Canada) — i.e. the supplier's country as registered in the UNGM vendor profile. The award detail page shows the vendor name but not its country, so the filter is the only country evidence (`vendor.country_basis` says so). A few names look foreign-registered (e.g. "Med-Eng, LLC", "Blossom Srl") but are kept because UNGM attributes them to Canada; the user can review `vendor.name`.

## How "ongoing" was determined
UNGM awards carry **Award date** and **Contract value (USD)** only; no start/end/duration fields. Status is therefore `end_date_unknown` for all 287 records. A conservative free-text scan of title+description for "duration of … N months/years" or "until <date>" found one award whose stated 1-year term from 2023-12-28 had ended → excluded (listed in `downloads/ungm/normalize_stats.json`); no record qualified for `ongoing_inferred`. LTAs (long-term agreements, typically 3–5 years) are recognisable by title but their term is not stated, so they stay `end_date_unknown`.

## Counts
| status | records |
|---|---|
| end_date_unknown | 287 |
| ongoing / ongoing_inferred | 0 |
| **total** | **287** (of 288 awards; 1 excluded) |

Award years: 2015 7, 2016 8, 2017 6, 2018 13, 2019 67, 2020 35, 2021 26, 2022 21, 2023 20, 2024 35, 2025 26, 2026 23. Buyers (UN organizations, `buyer.type` = IGO): UNOPS 126, ICAO 54, IAEA 24, UNESCO 17, UNFPA 12, UN Secretariat 11, UNICEF 7, ILO 6, WMO 5, UNIDO 5, CTBTO 4, UNHCR 3, others. 126 awards (mostly UNOPS/ICAO/IAEA LTAs) publish no contract value.

## record_url
`https://www.ungm.org/Public/ContractAward/<id>` — verified: https://www.ungm.org/Public/ContractAward/159709 returns HTTP 200 with the award "Request for Quotation - Development of Employer's Requirements … (UNOPS, RFQ/2026/64543, Les Services EXP Inc.)".

## raw layer
`raw.search_list_row/cells` (list row: supplier, award date, agency abbreviation, reference, destination), `raw.detail_parsed` (all General-tab label/value pairs, description HTML, beneficiary countries, vendor list, UN contact details), `raw.detail_main_html` (verbatim `<main>` HTML of the detail page). UNSPSC codes are loaded client-side on the public page and were empty in every fetched page.

## Known gaps / limits
* No end dates at all → nothing can be marked `ongoing`; recent awards (2024–2026) are the most likely to be live.
* `buyer.country` is null (UN organizations are supranational); the UN contact's telephone country code is in `buyer.contact`.
* Agency-level award pages (UNDP, UNICEF, WFP …) were not crawled separately — UNGM already aggregates them and the time-box was spent on the detail crawl; UNDP publishes its own awards at procurement-notices.undp.org (not covered).

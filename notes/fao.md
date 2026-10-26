# fao — FAO procurement statistics: vendors with POs over USD 100,000 (quarterly lists)

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/fao.jsonl`: **12 records (11 `end_date_unknown`, 1 `ongoing_inferred`)**.

## Downloaded
Statistics pages `https://www.fao.org/unfao/procurement/statistics/<YYYY>-statistics/en` (2021–2024, 2026) and `.../2025statistics/en` (saved `downloads/igo_portals/fao/page_*.html`), 130 PDF links (`pdf_links.json`), 50+ quarterly PDFs "502 vendor" (goods) and "507 service provider" lists 2021 Q1 → 2026 Q1, retrieved 2026-10-25 17:58–17:59 UTC (`downloads/igo_portals/fao/*.pdf`). Scripts `scripts/igo_portals/fetch_fao.py`, `parse_fao.py`; stats `downloads/igo_portals/fao/normalize_stats.json`: 7,494 PO groups, 15 Canadian.

## Canadian vendor
PDF column **"Vendor Country"** = `Canada`. Names never used.

## Ongoing
FAO lists PO number, project symbol(s), vendor, country, description and USD net ordered value per quarter — no PO date or term. Where the description states a service period or "for <year>", it is used: Cority Software "for 2026" → `ongoing_inferred` 2026-01-01 → 2026-12-31 (fao:377376); Cority 2024 and 2025 POs excluded as ended. Others `end_date_unknown` with the reporting quarter in `contract.dates.reporting_period`.

## Buyer
Food and Agriculture Organization of the United Nations (FAO) (single buyer; no office column).

## record_url
null (PDF lists).

## Samples
fao:347337 Guardian Helicopters Inc (helicopters, USD 948,539, 2021 Q1); fao:9304466 1324123 Ontario Ltd (grain sleeves for Ukraine, USD 761,040, 2022 Q3); fao:354813 exactEarth Ltd (AIS data, USD 102,710); fao:7951098 Union des producteurs agricoles (USD 141,606); fao:377376 Cority Software Inc (2026 licences, USD 116,850, ongoing_inferred).

## Gaps
Only POs ≥ USD 100k are published; earlier years (pre-2021) not fetched.

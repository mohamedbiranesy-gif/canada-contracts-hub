# us_county_miami_dade — Miami-Dade County "Purchase Orders (INFORMS)" 2025 + 2026 (ArcGIS Open Data)

Reference date 2026-10-25. Output: `/home/claude/contracts/normalized/us_county_miami_dade.jsonl` (**10 records**, all `end_date_unknown`). Script: `scripts/us_county_miami_dade/normalize.py`; puller `scripts/us_common/arcgis_pull.py`.

## What was downloaded (2026-10-25T19:29:33Z UTC, ArcGIS REST query, where `COUNTRY='CAN' OR STATE IN (province codes)`)
- https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/services/miamidade_procurement_data_informs_2026/FeatureServer/0 (28,576 PO lines; COUNTRY: USA 28,560, CAN 15, ESP 1) → `downloads/us_county_miami_dade/po_informs_2026_ca.jsonl` (15 rows).
- …/miamidade_procurement_data_informs_2025/FeatureServer/0 → `po_informs_2025_ca.jsonl` (13 rows).
- Fields: PO_NUMBER, PO_DATE, PO_AMOUNT, PO_LINE_NUMBER, INVOICE_ITEM_ID, PO_QUANTITY, UOM_SIZE, UNIT_COST, PHONE_*, **SUPPLIER_ADDRESS(2), CITY, STATE, POSTAL, COUNTRY**, SUPPLIER_NAME/SHORT_NAME, ITEM_DESCRIPTION, LONG_ITEM_DESCRIPTION, COUNTY, BUSINESS_UNIT, SUPPLIER_CONTRACT_ID, ITEM_PHYSICAL_NATURE, ITEM_CATEGORY, SUPPLIER_PO_TYPE, PO_YEAR. Found via ArcGIS Hub search (`scripts/us_discovery/arcgis_sweep.py`).

## Canadian vendor / ongoing
`COUNTRY = 'CAN'`. One record per (PO_YEAR, BUSINESS_UNIT, PO_NUMBER) with all lines in `raw.rows`; kept iff PO_DATE (epoch ms in 2026 layer, ISO string in 2025 layer) within 12 months before 2026-10-25 → all 10 POs. value = Σ PO_AMOUNT over distinct (line, item) pairs. SUPPLIER_CONTRACT_ID (master contract) kept in identifiers/related. `record_url` null (no per-PO page).

## Result: 10 end_date_unknown (USD 16.6 M)
New Flyer of America (Winnipeg; transit buses/parts for DTPW, 3 POs, ≈USD 10.9 M), GIRO Inc (Montréal; transit scheduling software modernization, USD 4.22 M), Pratt & Whitney Canada (Longueuil; AW139 engine warranty plans, Fire Rescue, 2 POs), Monoglass Inc (Vancouver), Altus Group US Inc (Toronto; P3 advisory for Solid Waste), Velocia Inc (Toronto; transit rewards), Gala Systems (St-Hubert QC; inspection & maintenance).

## Samples
- `us_county_miami_dade:2026-TP20040200-17080` GIRO Inc (Montreal QC H2S 3L5) — software system modernization (Req #37729 DTPW) — USD 4,218,581 — 2026-04-15
- `us_county_miami_dade:2026-FR03040200-12633` Pratt & Whitney Canada Corp (Longueuil J4G 1A1) — AW139 engine warranty plan — USD 294,000 — 2026-07-21 (contract 0000010487)
- `us_county_miami_dade:2026-SW12020200-6157` Altus Group US Inc (Toronto M5E 1G4) — financial and P3 advisory, Solid Waste — USD 70,340 — 2026-01-15
- `us_county_miami_dade:2026-CU05010000-1336` Gala Systems Inc (St-Hubert QC J3Y 8Y6) — inspection & maintenance — USD 7,150 — 2026-07-15
- `us_county_miami_dade:2026-TT01010000-58` Velocia Inc (Toronto M5E 1J8) — rewards — USD 24,000 — 2026-03-26

## Gaps
Buyer is identified by INFORMS business-unit code only (department names not published in the layer). Earlier years (2021–2024 INFORMS, ADPICS 2008–2021) not pulled (outside the 12-month window).

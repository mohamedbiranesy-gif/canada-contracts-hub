# cl_mercado_publico — Chile – Mercado Público OCDS API releases (bulk via OCP Data Registry)

Reference date 2026-10-25. Publisher: Dirección de Compras y Contratación Pública (ChileCompra). Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id 144: https://data.open-contracting.org/en/publication/144 .
Origin / dataset URL: https://data.open-contracting.org/en/publication/144 (origin: https://datos-abiertos.chilecompra.cl/descargas/procesos-ocds ; API https://api.mercadopublico.cl/APISOCDS/).

Output: `/home/claude/contracts/normalized/cl_mercado_publico.jsonl` — **17 records** {'end_date_unknown': 17}.

Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).

## What was downloaded
Script `/home/claude/contracts/scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|"CA"|"CAN"|"CDN"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/cl_mercado_publico/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.

| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |
|---|---|---|---|
| 2026 | 2026-10-25T18:22:10Z | 170406 | 0 |
| 2025 | 2026-10-25T18:22:54Z | 796574 | 4 |
| 2024 | 2026-10-25T18:25:39Z | 1437336 | 14 |
| 2023 | 2026-10-25T18:26:49Z | 28463 | 1 |

(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)

## How "Canadian vendor" was determined
`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.

Field probe (first 3,000 releases of `2025`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): 2938 supplier parties, 2896 with an address, **2735 with a country value**; address keys {'streetAddress': 2896, 'region': 2879, 'countryName': 2735}; most common country values {'Chile': 2735}; contracts with `period.endDate`: 1.

Values seen on kept records: {"parties[].address.countryName = 'Canadá'": 17}.

## How "ongoing" was determined
`scripts/ocp_registry/normalize_ocds.py --source cl_mercado_publico --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`.

normalize stats: `{"ocids": 19, "units": 19, "excluded_award_status_cancelled": 1, "status_end_date_unknown": 17, "excluded_ended": 1}`; excluded examples: [['ocds-70d2nz-1057062-422-AG22', 'award status cancelled'], ['ocds-70d2nz-5240-392-SE21', 'end 2024-12-31 < ref']]

## Result / verdict
Counts by status: {'end_date_unknown': 17}.
Buyers: {'DIRECCION DE ABASTECIMIENTO DE LA ARMADA | SERVICIO HIDROGRAFICO Y OCEANOGRAFICO': 9, 'DIRECCION GENERAL DE GENDARMERIA DE CHIL | Dirección Nacional': 3, 'DEFENSORIA PENAL PUBLICA | Defensoría Nacional': 2, 'I MUNICIPALIDAD DE SANTO DOMINGO | Departamento de Educación': 1, 'DIRECCION DE LOGISTICA DE CARABINEROS | Direccion de Compras Publicas de Carabineros': 1, 'CORP NACIONAL FORESTAL | Conaf - Oficina Central - Abastecimiento': 1}.

`record_url`: template `https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC={ocid_po}`; example https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=1876-264-SE24

## Five sample records
- `cl_mercado_publico:ocds-70d2nz-1876-264-SE24` | Lexum | Lexum (None) | DEFENSORIA PENAL PUBLICA | Defensoría Nacional | SERVICIO DE LICENCIAMIENTO Y SOPORTE ANUAL SOFTWARE LEXUM (QWERI Y DECISIA) | USD 15731.8 | 2024-10-29 → None | end_date_unknown | https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=1876-264-SE24
- `cl_mercado_publico:ocds-70d2nz-3073-246-SE24` | Teledyne Caris, a business unit of Teledyne Digita | Teledyne Geospatial (None) | DIRECCION DE ABASTECIMIENTO DE LA ARMADA | SERVICIO HIDROGRAFICO Y OCEANOGRAFICO | LICENCIAS CARIS | USD 45708.23 | 2024-05-10 → None | end_date_unknown | https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=3073-246-SE24
- `cl_mercado_publico:ocds-70d2nz-3073-430-SE24` | AXYS Technologies INC | AXYS Technologies INC (None) | DIRECCION DE ABASTECIMIENTO DE LA ARMADA | SERVICIO HIDROGRAFICO Y OCEANOGRAFICO | REPUESTOS BOYAS TRIAXYS | USD 15145.0 | 2024-08-23 → None | end_date_unknown | https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=3073-430-SE24
- `cl_mercado_publico:ocds-70d2nz-3073-443-SE24` | Teledyne Caris, a business unit of Teledyne Digita | Teledyne Geospatial (None) | DIRECCION DE ABASTECIMIENTO DE LA ARMADA | SERVICIO HIDROGRAFICO Y OCEANOGRAFICO | LICENCIAS CARIS | USD 45708.23 | 2024-08-08 → None | end_date_unknown | https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=3073-443-SE24
- `cl_mercado_publico:ocds-70d2nz-3073-52-SE24` | AXYS Technologies INC | AXYS Technologies INC (None) | DIRECCION DE ABASTECIMIENTO DE LA ARMADA | SERVICIO HIDROGRAFICO Y OCEANOGRAFICO | Servicio de transmisión satelital Iridium | USD 32970.0 | 2024-01-25 → None | end_date_unknown | https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=3073-52-SE24

## Known gaps
- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.
- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.
- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.
- record_url verified 2026-10-25 19:3x UTC: https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=1876-264-SE24 -> HTTP 200, page names LEXUM. Chile OCDS releases are purchase-order level (ocid suffix = PO code); no contract end dates published (only 1 of 3,000 sampled releases has period.endDate) -> all `end_date_unknown`.
- The 2023 file in the registry is small (28,463 releases vs 1.4 M for 2024), so 2023 coverage is partial; years before 2023 not streamed.

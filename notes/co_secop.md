# co_secop — Colombia SECOP II (datos.gov.co)

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/co_secop.jsonl`: **1 record (`end_date_unknown`)**.

## Downloaded (Socrata SODA API, User-Agent contracts-research/1.0)
- Supplier registry *SECOP II – Proveedores Registrados* `https://www.datos.gov.co/resource/qmzu-gj57.json?$where=pais in('CA','CAN','Canada','CANADA','Canadá','CANADÁ')` → **62 suppliers** with `pais` = `CA` (`downloads/co_secop/proveedores_pais_CA_all.json`, 2026-10-25 19:21 UTC; earlier copy `proveedores_CA.json` 17:42 UTC). Most have `tipo_empresa` = "Persona Jurídica Extranjera sin domicilio en Colombia" and address "No Provisto".
- Contracts *SECOP II – Contratos Electrónicos* `https://www.datos.gov.co/resource/jbjy-vk9h.json` queried by `codigo_proveedor in(<62 codes>)` and by `documento_proveedor` / supplier name → **0 rows** (foreign suppliers without Colombian NIT do not appear in this dataset). Files: `contratos_by_codigo_proveedor_CA.json`, `contratos_by_nit.json`, `contratos_CA_proveedores.json` (all `[]`).
- Processes *SECOP II – Procesos de Contratación* `https://www.datos.gov.co/resource/p6dx-8zbt.json?$where=codigoproveedor in(<62 codes>)` → **6 awarded processes** (`procesos_by_codigo_CA.json`; re-checked 19:4x UTC, still 6).
Scripts: `scripts/co_secop/fetch.py`, `scripts/co_secop/normalize.py`.

## Canadian vendor
Structured field `pais` = `CA` of the SECOP II supplier registry, joined to the awarded process by `codigoproveedor`. Names not used.

## Ongoing
Process `duracion` + `unidad_de_duracion` added to `fecha_adjudicacion`: 5 of 6 ended (MDA Systems ×3 2017–2019, Scintrex 2018, Geosoft 2020-21). The 6th (Forensic Technology, Medellín, CO1.REQ.4820230, awarded 2023-07-28, COP 3,096,247,180, IBIS SafeGuard renewal) has duration "0 día(s)" → kept as `end_date_unknown` (very likely ended; flagged in status_basis).

## record_url
`urlproceso.url` (SECOP II community OpportunityDetail page) e.g. `https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.NTC.4769355`.

## Gaps
SECOP I (pre-2016 / non-SECOP II entities) has no supplier country field — not used. Foreign suppliers that registered with a Colombian NIT and `pais`=CO would not be caught. Contract-level dates for foreign awardees are not published in the open contracts dataset.

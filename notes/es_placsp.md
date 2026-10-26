# es_placsp — Spain, Plataforma de Contratación del Sector Público (PLACSP) syndication feeds

Reference date 2026-10-25. Output `/home/claude/contracts/normalized/es_placsp.jsonl`: **11 records** {'ongoing_inferred': 7, 'ongoing': 4}.

Resumed after the reboot by a second worker (first worker's `s643_202604.zip` download was cut mid-flight; restarted 19:15 UTC, zips now staged in /dev/shm because the root disk is ~full, extracted and deleted one at a time — `scripts/es_placsp/resume_shm.sh`).

## What was downloaded
Open-data page: https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx . Feeds: `https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_<YYYYMM|YYYY>.zip` (contracting-authority profiles hosted on PLACSP) and `https://contrataciondelestado.es/sindicacion/sindicacion_1044/PlataformasAgregadasSinMenores_<YYYYMM>.zip` (aggregated regional platforms, excluding minor contracts). Each zip = CODICE Atom files; a monthly file holds every folder **updated** that month (latest state of the folder).

| zip | atom members | entries | Canadian-winner entries kept | bytes |
|---|---|---|---|---|
| s643_202610.zip | 93 | 46298 | 4 | 145295192 |
| s643_202609.zip | 193 | 95910 | 3 | 302945644 |
| s643_202608.zip | 104 | 51819 | 2 | 160085565 |
| s643_202607.zip | 121 | 60329 | 2 | 191755885 |
| s643_202606.zip | 136 | 67698 | 2 | 215948197 |
| s643_202605.zip | 125 | 62022 | 0 | 198346558 |
| s643_202604.zip | 117 | 57893 | 1 | 183076141 |
| s643_202603.zip | 122 | 60717 | 5 | 194593012 |
| s643_202602.zip | 105 | 52156 | 1 | 167977295 |
| s643_202601.zip | 99 | 48913 | 1 | 158979652 |
| s1044_202610.zip | 45 | 21148 | 0 | 11545352 |
| s1044_202609.zip | 76 | 34501 | 0 | 20082335 |
| s1044_202608.zip | 37 | 17181 | 0 | 10151362 |
| s1044_202607.zip | 57 | 26268 | 0 | 15108608 |
| s1044_202606.zip | 56 | 26118 | 0 | 14884226 |
| s1044_202605.zip | 51 | 23698 | 0 | 13487320 |
| s1044_202604.zip | 48 | 22460 | 0 | 13008468 |
| s1044_202603.zip | 54 | 24708 | 0 | 13426770 |
| s1044_202602.zip | 43 | 19939 | 0 | 11555599 |
| s1044_202601.zip | 46 | 20172 | 0 | 11947646 |
| s643_2025.zip | 1398 | 693088 | 15 | 2172595976 |

Download log `downloads/es_placsp/download.log` (timestamps UTC); extraction log `downloads/es_placsp/extract.log`; kept raw entries (full XML) in `downloads/es_placsp/matches.jsonl`.

## Canadian vendor
`scripts/es_placsp/extract.py` keeps an `<entry>` when a `cac:TenderResult/cac:WinningParty` has `cac:PhysicalLocation/cac:Address/cac:Country/cbc:IdentificationCode` = `CA` (code list CountryIdentificationCode-2.08; name attribute 'Canadá'). Names never used. (`cbc:AwardedOwnerNationalityCode` is ignored — it is often ES even for foreign winners.)

## Ongoing
`scripts/es_placsp/normalize.py`: one record per (folder entry, lot, Canadian winning party); versions of the same entry across monthly files grouped, latest kept, all listed in `raw.rows`. Excluded: folder status `ANUL`, result codes 3–7 (desierto/desistimiento/renuncia). End = lot or folder `cac:PlannedPeriod/cbc:EndDate`; otherwise anchor (TenderResult `StartDate` → PlannedPeriod `StartDate` → `cac:Contract/cbc:IssueDate` (formalisation) → `AwardDate`) + `PlannedPeriod/cbc:DurationMeasure` (DAY/MON/ANN) → `ongoing_inferred`; else `end_date_unknown`.

normalize stats: `{"units": 25, "ongoing_inferred": 7, "ongoing": 4, "excluded_inferred_ended": 12, "excluded_ended": 2, "entries": 25}`

## record_url
The entry's `<link href>` deeplink `https://contrataciondelestado.es/wps/poc?uri=deeplink:detalle_licitacion&idEvl=<id>` (public folder page).

## Records
- `es_placsp:20415740:0:FUJIFILM_VISUALSONICS` | FUJIFILM VISUALSONICS (Toronto) | Fundación del Sector Público Estatal Centro Nacional de Investigaciones Oncológicas Carlos III | Suministro e Instalación de Módulos de Software de Análisis Avanzado y Equipamiento para l | EUR 95500.0 | 2026-10-23 → 2027-04-23 | ongoing_inferred
- `es_placsp:20657983:0:BENT_HOLLOW_COMPAGNIE` | BENT HOLLOW COMPAGNIE (Montreal) | Madrid Destino Cultura Turismo y Negocio, S.A. | Actuación artística única de teatro denominada "Unarmoured" de Clara Furey para su exhibic | EUR 17374.0 | 2026-10-14 → 2026-10-30 | ongoing
- `es_placsp:20681963:0:The_Canadian_Corps_of_Commissi` | The Canadian Corps of Commissionaires Ottawa Division (Ottawa) | Dirección General del Servicio Exterior | OTTAWA EM Contrato de servicio de vigilancia | EUR 86516.55 | 2026-05-28 → 2028-05-28 | ongoing_inferred
- `es_placsp:20480283:0:TOTM_EXPOSITION_INC` | TOTM EXPOSITION INC (QUEBEC) | Dirección de Barcelona Supercomputing Center - Centro Nacional de Supercomputación (BSC-CNS) | servicio de creación del stand en formato isla en la International Conference for High Per | EUR 47000.0 | 2026-09-10 → 2026-12-10 | ongoing_inferred
- `es_placsp:20276263:0:GIRO_INC_LE_GROUPE_EN_INFORMAT` | GIRO INC./LE GROUPE EN INFORMATIQUE ET RECHERCHE OPÉRATIONNELLE (Montréal) | Gerencia de la Empresa Malagueña de Transportes S.A.M. | La contratación de los servicios de actualización y mantenimiento del software "Hastus V20 | EUR 487052.0 | 2026-09-21 → 2027-09-21 | ongoing_inferred
- `es_placsp:20050657:0:DE_HAVILLAND_OF_CANADA_LTD` | DE HAVILLAND OF CANADA LTD (CALGARY, AB T3J 4L2) | Dirección de Adquisiciones del Mando de Apoyo Logístico del Ejército del Aire y del Espacio | suministro y actualización durante un año de la documentación técnica de sistemas de armas | EUR 207618.81 | 2026-07-07 → 2027-07-07 | ongoing_inferred
- `es_placsp:19799111:0:DE_HAVILLAND_OF_CANADA_LTD` | DE HAVILLAND OF CANADA LTD (CALGARY, AB T3J 4L2) | Dirección de Adquisiciones del Mando de Apoyo Logístico del Ejército del Aire y del Espacio | 20262147 servicios para reparaciones estructurales para los aviones cl-215 (ud.13) y cl-41 | EUR 395936.8 | 2026-05-29 → 2026-11-30 | ongoing
- `es_placsp:18712824:0:AIRPORTS_COUNCIL_INTERNATIONAL` | AIRPORTS COUNCIL INTERNATIONAL-ACI (MONTREAL-QUEBEC H4Z 1G8) | Aena. Dirección de Contratación | Servicio Para La Obtención De Los Niveles De Calidad Y Elaboración De Informes Periódicos  | EUR 1778216.73 | 2026-01-01 → 2028-12-31 | ongoing
- `es_placsp:17526316:0:M5digital_products_LTD` | M5digital products, LTD (None) | Subsecretaría del Ministerio de Trabajo y Economía Social | Fotocopiadoras Ottawa | EUR 4359.84 | 2024-04-01 → 2028-04-01 | ongoing_inferred
- `es_placsp:17572403:0:EXPRETIO_TECHNOLOGIES_INC` | EXPRETIO TECHNOLOGIES INC (Montreal) | Dirección General de Renfe Viajeros Sociedad Mercantil Estatal, S.A. | Servicio soporte, mantenimiento, evolucion y utilizacion en modo saas del sistema revenue  | EUR 7719595.16 | 2025-06-26 → 2028-06-26 | ongoing_inferred
- `es_placsp:18210694:0:TINOCO_ZARATE` | TINOCO ZARATE (Ottawa) | Dirección General del Servicio Exterior | Servicio de limpieza. Embajada de España en Ottawa (Canadá). | EUR 94038.46 | 2025-10-01 → 2027-09-30 | ongoing

## Known gaps
- Monthly files cover folders updated Jan–Oct 2026 (643) and Jan–Oct 2026 (1044). Contracts awarded earlier and not updated in 2026 are only in the annual files: the 2025 annual 643 file (2.17 GB, 693,088 entries) was processed; the 2024 annual 643 file only if it appears in the table above (it was started 20:28 UTC); 2023-and-earlier annual files and all 1044 annual files were not processed (time/disk).
- Minor contracts (contratos menores) feed (sindicacion_1143) not processed.
- Above-threshold awards may also be in TED (`ted_eu`) — de-duplicate by expediente/folder id at merge.

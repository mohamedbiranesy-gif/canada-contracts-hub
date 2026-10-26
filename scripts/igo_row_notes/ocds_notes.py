#!/usr/bin/env python3
"""Generate notes/<key>.md for OCP-Data-Registry-streamed sources from logs/stats/outputs."""
import json, os, re, sys, collections
B = "."
cfg = json.load(open(B + "/scripts/ocp_registry/sources.json"))
probe = {}
for l in open(B + "/downloads/ocp_registry/field_probe.jsonl"):
    if l.startswith("{"):
        d = json.loads(l); probe[d["label"].split(":")[0]] = d
META = {  # key: (name, publisher, pub_id, verdict_text)
 "ar_mendoza": ("Argentina – Mendoza province COMPR.AR OCDS", "Dirección General de Contrataciones Públicas, Gobierno de Mendoza", 137),
 "br_compras_gov": ("Brazil – Compras.gov.br (federal) OCDS", "Ministério da Gestão e da Inovação em Serviços Públicos, Brazil", 157),
 "do_dgcp": ("Dominican Republic – DGCP OCDS", "Dirección General de Contrataciones Públicas (DGCP)", 22),
 "gh_ppa": ("Ghana – PPA OCDS", "Public Procurement Authority of Ghana", 85),
 "gt_guatecompras": ("Guatemala – Guatecompras OCDS", "Ministerio de Finanzas Públicas, Guatemala", 142),
 "hn_oncae": ("Honduras – ONCAE HonduCompras OCDS", "Oficina Normativa de Contratación y Adquisiciones del Estado (ONCAE)", 122),
 "hn_sefin": ("Honduras – SEFIN (SIAFI) OCDS", "Secretaría de Finanzas de Honduras", 123),
 "it_anac": ("Italy – ANAC BDNCP OCDS", "Autorità Nazionale Anticorruzione (ANAC)", 117),
 "ke_ppip": ("Kenya – PPIP OCDS", "Public Procurement Regulatory Authority (PPRA), Kenya", 147),
 "lr_ppcc": ("Liberia – PPCC OCDS", "Public Procurement and Concessions Commission, Liberia", 156),
 "mx_nuevo_leon": ("Mexico – Nuevo León state OCDS", "Gobierno del Estado de Nuevo León", 149),
 "ng_bpp": ("Nigeria – BPP NOCOPO OCDS", "Bureau of Public Procurement, Nigeria", 64),
 "tz_nest": ("Tanzania – NeST OCDS", "Public Procurement Regulatory Authority (PPRA), Tanzania", 152),
 "ug_ppda": ("Uganda – PPDA GPP OCDS", "Public Procurement and Disposal of Public Assets Authority, Uganda", 130),
 "al_ppc": ("Albania – Public Procurement Commission (PPC) OCDS", "Public Procurement Commission, Albania", 134),
 "gr_diavgis": ("Greece – Diavgeia (Diavgis) OCDS", "Ministry of Interior, Greece (Diavgeia transparency programme)", 161),
 "mx_inai": ("Mexico – INAI (federal transparency institute) contracting OCDS", "Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI)", 31),
 "uy_arce": ("Uruguay – ARCE (Agencia Reguladora de Compras Estatales) OCDS API", "Agencia Reguladora de Compras Estatales (ARCE), Uruguay", 43),
 "md_mtender": ("Moldova – MTender (Ministry of Finance) OCDS", "Ministry of Finance, Republic of Moldova", 34),
 "xk_pprc": ("Kosovo – PPRC e-procurement OCDS", "Public Procurement Regulatory Commission (PPRC), Kosovo", 115),
 "pa_dgcp": ("Panama – DGCP PanamaCompra OCDS", "Dirección General de Contrataciones Públicas, Panamá", 120),
 "es_zaragoza": ("Spain – Ayuntamiento de Zaragoza OCDS", "Ayuntamiento de Zaragoza", 1),
 "co_cce": ("Colombia – Colombia Compra Eficiente (SECOP I/II) OCDS", "Agencia Nacional de Contratación Pública – Colombia Compra Eficiente", 61),
 "fr_dinum": ("France – DECP données essentielles (DINUM) OCDS", "Direction interministérielle du numérique (DINUM), France", 23),
 "au_nsw": ("Australia – New South Wales eTendering (NSW Treasury) OCDS", "NSW Treasury / NSW Procurement (buy.nsw)", 11),
 "cr_poder_judicial": ("Costa Rica – Poder Judicial procurement OCDS", "Poder Judicial de Costa Rica", 16),
 "ge_spa": ("Georgia – State Procurement Agency (SPA) OCDS (2010–2019)", "State Procurement Agency of Georgia", 24),
 "bo_agetic": ("Bolivia – AGETIC procurement OCDS (2019–2020)", "Agencia de Gobierno Electrónico y TIC (AGETIC), Bolivia", 20),
 "it_mit": ("Italy – Ministry of Infrastructure and Transport OCDS (2022–2024)", "Ministero delle Infrastrutture e dei Trasporti, Italy", 141),
 "pe_perucompras": ("Peru – Central de Compras Públicas Perú Compras OCDS (2021–2023)", "Central de Compras Públicas – Perú Compras", 78),
 "ar_caba": ("Argentina – Ciudad de Buenos Aires (DGCyC) OCDS (2022)", "Dirección General de Compras y Contrataciones, Ciudad de Buenos Aires", 17),
 "ke_makueni": ("Kenya – Makueni County OCDS (2021–2022)", "Makueni County Government, Kenya", 13),
 "za_etenders": ("South Africa – eTenders OCDS", "National Treasury, South Africa", 143),
}
for k, v in cfg.items():
    META.setdefault(k, (v["name"], v["publisher"], int(re.search(r"publication/(\d+)", v["dataset_url"]).group(1))))

def streams(k):
    p = B + "/downloads/%s/stream.log" % k
    out = []
    if not os.path.exists(p): return out
    for l in open(p):
        m = re.match(r"(\S+) END \S+ \S+ (\S+) total_lines=(\d*) matches=(\d+)", l)
        if m: out.append(m.groups())
    return out

def samples(k, n=5):
    p = B + "/normalized/%s.jsonl" % k
    if not os.path.exists(p): return [], collections.Counter()
    R = [json.loads(l) for l in open(p) if l.strip()]
    return R, collections.Counter(r["status"] for r in R)

REJECT_REASON = {
 "al_ppc": "Releases in the sample carry no awards and no supplier parties (tender stage only). **Rejected: no award/supplier data.** 0 matches in the 'full' file (3,293 releases).",
 "gr_diavgis": "Supplier parties have no address at all (0 of 2,617 in sample; suppliers identified by AFM tax number only). 0 matches in 'full' (1,131,890 releases). **Rejected: no supplier country.**",
 "uy_arce": "Supplier parties have no address (0 of 4,800 in sample). 0 matches 2022–2026. **Rejected: no supplier country.**",
 "md_mtender": "Supplier country is published, but in a non-standard place: `address.addressDetails.country.id` (ISO alpha-2, e.g. 'MD'). The structural filter does not read `addressDetails`, so the prefiltered lines (all lines containing a 'CA'/Canada token) were re-checked directly on 2026-10-25: 0 parties with `addressDetails.country.id` = 'CA' in 2022–2026. **Checked, 0 Canadian-supplier records.**",
 "xk_pprc": "No awards and no supplier addresses in the sample (0/1,936). 0 matches. **Rejected: no supplier country.**",
 "pa_dgcp": "Supplier parties have no address (0/389 in sample). 0 matches 2021–2024 (registry data ends Apr 2024). **Rejected: no supplier country.**",
 "es_zaragoza": "Supplier parties have no address (0/2,768). 0 matches. **Rejected: no supplier country.** (Zaragoza contracts above threshold also appear in PLACSP/es_placsp.)",
 "fr_dinum": "DECP titulaires carry only an identifier (SIRET/TVA/HORS-UE) — no address/country (0/3,040 in sample). 0 matches 2022–2026 (2024–2026 registry files are near-empty: 1–4 releases). **Rejected: no supplier country field.**",
 "au_nsw": "The registry copy of NSW eTendering contains planning/tender releases and awards whose `suppliers[]` carry only name + ABN (+ `ABNExempt` flag) — **no supplier address** (8,243 award suppliers in the 2024 file, all without address). 0 matches 2016–2025. The live NSW eTendering contract-notice API (`https://tenders.nsw.gov.au/?event=public.api.contract.search`) now redirects to `https://buy.nsw.gov.au/`, which returned **HTTP 403 (CloudFront 'Request blocked')** on 2026-10-25 19:3x UTC — not bypassed. **Rejected (no country in open copy; live portal blocked).**",
 "ge_spa": "Georgia SPA OCDS (2010–2019, 275,439 releases): supplier `countryName` is published (Georgia, Italy, Ukraine … in the sample) but 0 Canadian suppliers. Data ends 2019. **Checked, 0 records.**",
 "bo_agetic": "Only 90 releases (2019–2020). 0 matches. **0 records.**",
 "ke_makueni": "796 releases (2021–2022), county-level, local suppliers. 0 matches. **0 records.**",
 "cr_poder_judicial": "Supplier addresses carry street only, no country (0 of 2,663 sampled supplier parties). 0 matches. **Rejected: no supplier country.**",
 "pe_perucompras": "Supplier parties have no address (0/3,000). 0 matches (framework-agreement purchase orders, 369,515 releases). **Rejected: no supplier country.**",
 "ar_caba": "Supplier parties have no address (0/865). 0 matches. **Rejected: no supplier country.**",
 "br_compras_gov": "Supplier parties carry NO address at all (0 of 3,697 supplier parties in a 3,000-release sample have `address`); suppliers identified only by CNPJ/CPF. Foreign suppliers cannot be identified structurally. 0 matches in 2024–2026 files. **Rejected: no supplier country/address field.** (The federal PNCP contracts API marks foreign suppliers only with `tipoPessoa`=PE (pessoa estrangeira) — no country — so it cannot establish Canada either.)",
 "hn_oncae": "Supplier `address` has only `streetAddress` (no country) in the sample; 0 matches 2025–2026. **Rejected: no supplier country field.**",
 "ug_ppda": "Supplier parties have no address (0/1,095 in sample). **Rejected: no supplier address/country.**",
 "tz_nest": "Releases in the sample contain no parties with supplier role and no awards (tender-stage data only). **Rejected: no award/supplier data.**",
 "it_anac": "Only 2 of 2,675 supplier parties in a sample carry an address (both ITALY); ANAC identifies suppliers by codice fiscale only. 0 matches 2024, 2025, undated. **Rejected: supplier country essentially never published.**",
 "ng_bpp": "Only 12 of 643 supplier parties carry `countryName`, and it is a numeric code (e.g. '166'), not a name/ISO code; the prefilter (Canada tokens / 'CA'/'CAN') cannot see a numeric Canada code, so this source is effectively unsearchable for Canadian suppliers. 0 matches. **Rejected (gap noted).**",
}
GENERIC_ZERO = "Supplier country field IS published (see probe) but 0 releases had a supplier whose address country denotes Canada in the files streamed. **Checked, 0 Canadian-supplier records.**"

EXTRA = {
 "it_mit": "- 1 Canadian-supplier release found (GIRO Inc., Montreal, country CA): ocds-8mw9gh-scp-1562025, 'CANONE ANNUALE MANUTENZIONE ED ASSISTENZA ATTINENTE IL SISTEMA HASTUS 2022', award 2021-12-26, EUR 74,691 (buyer via Liguria regional platform). No period published, but the title states the annual fee is for 2022 → inferred end 2022-12-31 < 2026-10-25 → **excluded** (same convention as FAO 'for <year>' POs). No output file written.",
 "it_anac": "- ANAC's own open-data portal (dataset `aggiudicatari`, https://dati.anticorruzione.it/opendata/dataset/aggiudicatari) answered **'Request Rejected'** (F5 WAF page, HTTP 200/269 bytes) on 2026-10-25 ~19:59 UTC — not bypassed; its awardee files are in any case keyed by codice fiscale without a country column.",
 "no_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Norway: 40 normalised → 6 dropped (pass 1) → 12 dropped (pass 2) → 22 kept. Doffin itself not crawled (API key required, see notes/no_doffin.md).",
 "ch_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Switzerland: 12 → 2 dropped (pass 1) → 2 dropped (pass 2) → 8 kept. SIMAP national notices are covered separately by `ch_simap`.",
 "se_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Sweden: 54 → 15 (pass 1) → 31 (pass 2) → 8 kept.",
 "fi_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Finland: 12 → 6 (pass 1) → 2 (pass 2) → 4 kept.",
 "dk_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Denmark: 42 → 28 (pass 1) → 5 (pass 2) → 9 kept.",
 "is_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- Iceland: 5 → 0 (pass 1) → 3 (pass 2) → 2 kept.",
 "eu_institutions_opentender": "- OpenTender (opentender.eu, DIGIWHIST) data is **TED-derived** (award documents link to ted.europa.eu notices; TED notice ids copied to `contract.related.ted_notice_ids`). Two de-duplication passes against the finished `ted_eu` source (which covers TED 2015→2026 with duration logic): (1) `scripts/ocp_registry/dedupe_ted.py` drops records whose TED notice is already a `ted_eu` record (`downloads/<key>/dropped_as_ted_eu_duplicates.json`); (2) `scripts/ocp_registry/dedupe_ted2.py` drops records whose TED notice `ted_eu` excluded as ended (`downloads/<key>/dropped_as_ended_per_ted_eu.json`). What remains is mostly pre-2015 TED award notices (outside ted_eu's window) with no end date → `end_date_unknown` — weak evidence of being ongoing; treat with caution.\n- Registry data ends Dec 2024; normalize stats below are before de-duplication.\n- EU institutions (Commission, agencies, etc.): 25 → 11 (pass 1) → 4 (pass 2) → 10 kept; buyer.country null (institution seat not mapped).",
 "si_mju": "- Slovenian e-JN OCDS publishes supplier address with country names in Slovene ('Kanada'). No contract periods → all `end_date_unknown`.",

 "cl_mercado_publico": "- record_url verified 2026-10-25 19:3x UTC: https://www.mercadopublico.cl/PurchaseOrder/Modules/PO/DetailsPurchaseOrder.aspx?codigoOC=1876-264-SE24 -> HTTP 200, page names LEXUM. Chile OCDS releases are purchase-order level (ocid suffix = PO code); no contract end dates published (only 1 of 3,000 sampled releases has period.endDate) -> all `end_date_unknown`.\n- The 2023 file in the registry is small (28,463 releases vs 1.4 M for 2024), so 2023 coverage is partial; years before 2023 not streamed.",
 "de_bmi_oeffentlichevergabe": "- record_url `https://www.oeffentlichevergabe.de/ui/de/search/details/<notice uuid>` returns HTTP 200 (single-page app shell, content rendered client-side); verified for 1a692001-0c7c-40b5-96b8-985f86ce057b on 2026-10-25.\n- eForms data starts 2023 (German eForms go-live); 2023 file covers only part of the year.\n- Above-threshold German notices are also published in TED: some records may duplicate `ted_eu` (e.g. GIZ, BAAINBw awards) — de-duplicate at merge on buyer + vendor + title/notice id.",
 "nl_tenderned": "- record_url built from the tenderNotice document link, rewritten to `https://www.tenderned.nl/aankondigingen/overzicht/<id>`; verified https://www.tenderned.nl/aankondigingen/overzicht/126564 -> HTTP 200 (SPA).\n- The registry file is a single 'full' file (139,654 releases, 2016–present).\n- European (above-threshold) TenderNed notices are also in TED: possible overlap with `ted_eu` — de-duplicate at merge.",
 "pe_oece": "- Years 2019–2026 streamed; 2010–2018 not streamed (most awards of that era would have ended).\n- OCDS record API `https://contratacionesabiertas.oece.gob.pe/api/v1/record/<ocid>` returned HTTP 403 to our client on 2026-10-25 (not bypassed), so record_url = null; template kept in `contract.related.ocds_record_url`.\n- Only ~1/3 of supplier parties carry a country (806 of 2,345 in the sample); domestic suppliers mostly have no address, foreign ones (registered as 'no domiciliado') usually do.",
 "ec_sercop": "- record_url (OCDS record API) verified: https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/api/record?ocid=ocds-5wno2w-CPC-INOCAR-2026-003-1006003 -> HTTP 200 JSON naming CARRERA GALO. The supplier is a natural person whose address country is CANADA.",
 "py_dncp": "- record_url verified: https://www.contrataciones.gov.py/datos/api/v3/doc/ocds/record/ocds-03ad3f-479495-1 -> HTTP 200 naming Canadian Banknote Company. DNCP releases rarely carry contract periods (0 of 3,000 sampled) -> `end_date_unknown` unless the contract block has a period.",
 "hr_eojn": "- Croatian EOJN contract register records Canadian suppliers with country CAN but often a Croatian locality (e.g. Ultra Electronics Forensic Technology Inc, locality ZAGREB) - kept as published; country field is authoritative per brief.\n- EOJN publishes no contract end dates in OCDS -> all `end_date_unknown`.",
 "rw_umucyo": "- One kept vendor is a natural person (Mutalikanwa Umutesi Nathalie) with address country Canada; kept as published.",
 "zm_zppa": "- 'full' file (178,732 releases) plus 2024/2025 files streamed; the one Canadian supplier appears in both 'full' and 2024 (deduplicated by ocid).",
}
for k, (name, publisher, pid) in META.items():
    st = streams(k)
    R, sc = samples(k)
    pr = probe.get(k)
    ns = B + "/downloads/%s/normalize_stats.json" % k
    nstats = json.load(open(ns)) if os.path.exists(ns) else None
    L = []
    L.append("# %s — %s\n" % (k, name))
    L.append("Reference date 2026-10-25. Publisher: %s. Accessed through the Open Contracting Partnership **OCP Data Registry** bulk files, publication id %d: https://data.open-contracting.org/en/publication/%d ." % (publisher, pid, pid))
    if k in cfg: L.append("Origin / dataset URL: %s." % cfg[k]["dataset_url"])
    L.append("\nOutput: `normalized/%s.jsonl` — **%d records** %s.\n" % (k, len(R), dict(sc) if R else "(none written)"))
    L.append("Note reconstructed on 2026-10-25 ~19:30 UTC by the resuming worker from scripts, logs and outputs (original worker was cut off by a machine reboot before writing notes).\n")
    L.append("## What was downloaded")
    L.append("Script `scripts/ocp_registry/stream_one.sh <key> <pub_id> <name>` streams `https://data.open-contracting.org/en/publication/<pub_id>/download?name=<YYYY|full>.jsonl.gz` (compiled OCDS releases, one per line) through `gunzip | grep` (case-insensitive prefilter `canad|kanada|…|\"CA\"|\"CAN\"|\"CDN\"`) and then `ocds_filter.py` (structural check, below). Only prefiltered lines are kept on disk (`downloads/%s/prefiltered_*.jsonl[.gz]`, when present) plus matches (`matches_*.jsonl`); totals in `lines_total_*.txt`, log `stream.log`, filter stats `stats.jsonl`.\n" % k)
    if st:
        L.append("| file (name=) | finished (UTC) | total releases | Canadian-supplier matches |\n|---|---|---|---|")
        seen = {}
        for ts, nm, tot, m in st: seen[nm] = (ts, tot, m)   # last run wins (several files were re-streamed after a filter fix)
        for nm, (ts, tot, m) in seen.items():
            L.append("| %s | %s | %s | %s |" % (nm, ts, tot or "?", m))
        L.append("\n(Where a file appears twice in `stream.log`, the later run — after the filter was extended to read supplier addresses embedded in `awards[].suppliers[]` — is the authoritative one; the table shows the last run.)\n")
    L.append("## How \"Canadian vendor\" was determined")
    L.append("`ocds_filter.py`: a party whose `roles` contain `supplier` (or whose id appears in `awards[].suppliers[]`/`contracts[].suppliers[]`) and whose `address.countryName` / `address.country` / `address.countryCode` (string or {id,name}) normalises to one of `canada, canadá, kanada, ca, can, cdn` (plus CJK/Cyrillic spellings), or whose `identifier.scheme` starts with `CA-`; also inline `awards[].suppliers[].address`. Names are never used.")
    if pr:
        L.append("\nField probe (first 3,000 releases of `%s`, run 2026-10-25 19:2x UTC by `scripts/ocp_registry/field_probe.py`): %d supplier parties, %d with an address, **%d with a country value**; address keys %s; most common country values %s; contracts with `period.endDate`: %d." % (
            pr["label"].split(":")[1], pr["supplier_parties"], pr["with_address"], pr["with_country"], pr["addr_keys"], pr["country_top"], pr["contracts_with_period_end"]))
    if R:
        L.append("\nValues seen on kept records: %s." % dict(collections.Counter(r["vendor"]["country_basis"] for r in R)))
    L.append("\n## How \"ongoing\" was determined")
    if R or nstats:
        L.append("`scripts/ocp_registry/normalize_ocds.py --source %s --config scripts/ocp_registry/sources.json`: releases grouped by `ocid`, latest release used; one record per (ocid, award with a Canadian supplier). End date = first of `contracts[].period.endDate` → `awards[].contractPeriod.endDate` → lot `contractPeriod` (via `awards[].relatedLots`) → `tender.contractPeriod.endDate`; `durationInDays` gives `ongoing_inferred` (anchor + duration ≥ 2026-10-25). Anchor = start → dateSigned → award.date → release.date. Excluded: award status cancelled/unsuccessful, all contracts cancelled, end < 2026-10-25, start > 2026-10-25. Otherwise `end_date_unknown`." % k)
        if nstats:
            L.append("\nnormalize stats: `%s`; excluded examples: %s" % (json.dumps({a: b for a, b in nstats.items() if a != "excluded_examples"}), nstats.get("excluded_examples", [])[:6]))
    else:
        L.append("Not applicable (no Canadian-supplier releases).")
    L.append("\n## Result / verdict")
    if R:
        L.append("Counts by status: %s." % dict(sc))
        L.append("Buyers: %s." % dict(collections.Counter(r["buyer"]["name"] for r in R).most_common(8)))
        ru = [r["source"]["record_url"] for r in R if r["source"].get("record_url")]
        L.append("\n`record_url`: %s" % (("template `%s`; example %s" % (cfg[k].get("record_url_template") or cfg[k].get("record_url_from_document"), ru[0])) if ru else "null — the portal has no stable public per-record URL usable from the OCDS identifiers (OCDS record API link kept in `contract.related.ocds_record_url` where one exists)."))
    else:
        L.append(REJECT_REASON.get(k, GENERIC_ZERO))
    if R:
        L.append("\n## Five sample records")
        for r in R[:5]:
            c = r["contract"]; d = c["dates"]
            L.append("- `%s` | %s (%s) | %s | %s | %s %s | %s → %s | %s | %s" % (r["record_id"], r["vendor"]["name"], (r["vendor"].get("address") or {}).get("city"), r["buyer"]["name"], (c.get("title") or "")[:80], c.get("currency"), c.get("value"), d.get("start") or d.get("signed") or d.get("award") or d.get("published"), d.get("end"), r["status"], r["source"].get("record_url")))
    L.append("\n## Known gaps")
    L.append("- Only the yearly files listed above were streamed (recent years first); older years not covered unless listed.\n- Prefilter is a text grep: a Canadian supplier whose country is encoded numerically or in an unexpected language would be missed.\n- Country is as entered by the publisher; obvious data-entry quirks (e.g. Canadian country with a local city) are kept as published and visible in `vendor.address`.")
    if k in EXTRA: L.append(EXTRA[k])
    tmpf = B + "/notes/.%s.md.tmp" % k
    open(tmpf, "w").write("\n".join(L) + "\n"); os.replace(tmpf, B + "/notes/%s.md" % k)
    print("wrote", k, len(R))

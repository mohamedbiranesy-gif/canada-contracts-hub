import json, re, collections
B = "."
R = [json.loads(l) for l in open(B + "/normalized/es_placsp.jsonl")]
st = json.load(open(B + "/downloads/es_placsp/normalize_stats.json"))
ex = [l.split() for l in open(B + "/downloads/es_placsp/extract.log") if " DONE " in l]
dlog = [l.strip() for l in open(B + "/downloads/es_placsp/download.log") if " END " in l and "size=" in l and not l.strip().endswith("size=")]
L = ["# es_placsp — Spain, Plataforma de Contratación del Sector Público (PLACSP) syndication feeds\n",
     "Reference date 2026-10-25. Output `normalized/es_placsp.jsonl`: **%d records** %s.\n" % (len(R), dict(collections.Counter(r["status"] for r in R))),
     "Resumed after the reboot by a second worker (first worker's `s643_202604.zip` download was cut mid-flight; restarted 19:15 UTC, zips now staged in /dev/shm because the root disk is ~full, extracted and deleted one at a time — `scripts/es_placsp/resume_shm.sh`).\n",
     "## What was downloaded",
     "Open-data page: https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/licitaciones_plataforma_contratacion.aspx . Feeds: `https://contrataciondelestado.es/sindicacion/sindicacion_643/licitacionesPerfilesContratanteCompleto3_<YYYYMM|YYYY>.zip` (contracting-authority profiles hosted on PLACSP) and `https://contrataciondelestado.es/sindicacion/sindicacion_1044/PlataformasAgregadasSinMenores_<YYYYMM>.zip` (aggregated regional platforms, excluding minor contracts). Each zip = CODICE Atom files; a monthly file holds every folder **updated** that month (latest state of the folder).",
     "\n| zip | atom members | entries | Canadian-winner entries kept | bytes |\n|---|---|---|---|---|"]
for e in ex:
    d = dict(x.split("=", 1) for x in e if "=" in x)
    L.append("| %s | %s | %s | %s | %s |" % (e[2].split("/")[-1], d.get("members"), d.get("entries"), d.get("kept"), d.get("zipbytes")))
L += ["\nDownload log `downloads/es_placsp/download.log` (timestamps UTC); extraction log `downloads/es_placsp/extract.log`; kept raw entries (full XML) in `downloads/es_placsp/matches.jsonl`.",
      "\n## Canadian vendor",
      "`scripts/es_placsp/extract.py` keeps an `<entry>` when a `cac:TenderResult/cac:WinningParty` has `cac:PhysicalLocation/cac:Address/cac:Country/cbc:IdentificationCode` = `CA` (code list CountryIdentificationCode-2.08; name attribute 'Canadá'). Names never used. (`cbc:AwardedOwnerNationalityCode` is ignored — it is often ES even for foreign winners.)",
      "\n## Ongoing",
      "`scripts/es_placsp/normalize.py`: one record per (folder entry, lot, Canadian winning party); versions of the same entry across monthly files grouped, latest kept, all listed in `raw.rows`. Excluded: folder status `ANUL`, result codes 3–7 (desierto/desistimiento/renuncia). End = lot or folder `cac:PlannedPeriod/cbc:EndDate`; otherwise anchor (TenderResult `StartDate` → PlannedPeriod `StartDate` → `cac:Contract/cbc:IssueDate` (formalisation) → `AwardDate`) + `PlannedPeriod/cbc:DurationMeasure` (DAY/MON/ANN) → `ongoing_inferred`; else `end_date_unknown`.",
      "\nnormalize stats: `%s`" % json.dumps({k: v for k, v in st.items() if k != "excluded_examples"}),
      "\n## record_url",
      "The entry's `<link href>` deeplink `https://contrataciondelestado.es/wps/poc?uri=deeplink:detalle_licitacion&idEvl=<id>` (public folder page).",
      "\n## Records"]
for r in R:
    c = r["contract"]; d = c["dates"]
    L.append("- `%s` | %s (%s) | %s | %s | EUR %s | %s → %s | %s" % (r["record_id"], r["vendor"]["name"], r["vendor"]["address"].get("city"), r["buyer"]["name"], (c["title"] or "")[:90], c["value"], d.get("start") or d.get("signed") or d.get("award"), d.get("end"), r["status"]))
L += ["\n## Known gaps",
      "- Monthly files cover folders updated Jan–Oct 2026 (643) and Jan–Oct 2026 (1044). Contracts awarded earlier and not updated in 2026 are only in the annual files: the 2025 annual 643 file (2.17 GB, 693,088 entries) was processed; the 2024 annual 643 file only if it appears in the table above (it was started 20:28 UTC); 2023-and-earlier annual files and all 1044 annual files were not processed (time/disk).",
      "- Minor contracts (contratos menores) feed (sindicacion_1143) not processed.",
      "- Above-threshold awards may also be in TED (`ted_eu`) — de-duplicate by expediente/folder id at merge."]
import os
tmp = B + "/notes/.es_placsp.md.tmp"; open(tmp, "w").write("\n".join(L) + "\n"); os.replace(tmp, B + "/notes/es_placsp.md")
print(len(R))

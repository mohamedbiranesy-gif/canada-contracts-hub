#!/usr/bin/env python3
"""SECOP II processes awarded to suppliers registered with pais=CA -> records (only those not ended by stated duration)."""
import json, re, datetime, sys
REF = datetime.date(2026, 10, 25)
dl = "downloads/co_secop/"
sup = {s["codigo"]: s for s in json.load(open(dl + "proveedores_pais_CA_all.json"))}
procs = json.load(open(dl + "procesos_by_codigo_CA.json"))
out = open("normalized/co_secop.jsonl", "w", encoding="utf-8"); stats = {"processes_awarded_to_CA_registered_suppliers": len(procs), "excluded": []}
def add(d, n, unit):
    u = unit.lower()
    if u.startswith("d"): return d + datetime.timedelta(days=n)
    if u.startswith("mes"): 
        m = d.month - 1 + n; y = d.year + m // 12; m = m % 12 + 1
        return datetime.date(y, m, min(d.day, 28))
    if u.startswith("a"): return datetime.date(d.year + n, d.month, min(d.day, 28))
    return None
for p in procs:
    s = sup.get(p["codigoproveedor"], {})
    ad = datetime.date.fromisoformat(p["fecha_adjudicacion"][:10])
    n = int(float(p.get("duracion") or 0)); unit = p.get("unidad_de_duracion") or ""
    end = add(ad, n, unit) if n > 0 else None
    if end and end < REF:
        stats["excluded"].append([p["id_del_proceso"], p["nombre_del_proveedor"], "award %s + %d %s = %s < ref" % (ad, n, unit, end)]); continue
    status = "end_date_unknown"
    basis = "SECOP II process duration published as '%s %s' (unusable); award date %s; no contract end date (supplier's contract not present in SECOP II contratos dataset jbjy-vk9h)" % (p.get("duracion"), unit, ad)
    rec = {"record_id": "co_secop:%s:%s" % (p["id_del_proceso"], p["id_adjudicacion"]),
      "source": {"key": "co_secop", "name": "Colombia SECOP II – Procesos de contratación (p6dx-8zbt) joined to Proveedores registrados (qmzu-gj57)", "publisher": "Agencia Nacional de Contratación Pública – Colombia Compra Eficiente (datos.gov.co)",
                 "dataset_url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt", "record_url": p["urlproceso"]["url"], "retrieved_at": "2026-10-25T17:45:13Z"},
      "status": status, "status_basis": basis,
      "contract": {"identifiers": {"id_del_proceso": p["id_del_proceso"], "referencia_del_proceso": p["referencia_del_proceso"], "id_adjudicacion": p["id_adjudicacion"], "id_del_portafolio": p["id_del_portafolio"], "ppi": p.get("ppi")},
        "title": p["nombre_del_procedimiento"], "description": p["descripci_n_del_procedimiento"], "instrument_type": "contract award (SECOP II process)", "procurement_method": p["modalidad_de_contratacion"], "solicitation_procedure": p.get("justificaci_n_modalidad_de"),
        "commodity": {"unspsc": p.get("codigo_principal_de_categoria")}, "value": float(p["valor_total_adjudicacion"]), "currency": "COP", "value_detail": {"valor_total_adjudicacion": float(p["valor_total_adjudicacion"]), "precio_base": float(p["precio_base"])},
        "dates": {"published": p["fecha_de_publicacion_del"][:10], "signed": None, "award": ad.isoformat(), "start": None, "end": None, "amended_last": None}, "related": {"tipo_de_contrato": p.get("tipo_de_contrato")}},
      "buyer": {"name": p["entidad"], "country": "CO", "type": "Colombian public entity", "identifiers": {"nit_entidad": p["nit_entidad"], "codigo_entidad": p.get("codigo_entidad")}, "address": {"city": p["ciudad_entidad"], "region": p["departamento_entidad"]}, "contact": {}},
      "vendor": {"name": p["nombre_del_proveedor"], "country": "CA", "country_basis": "SECOP II supplier registry (qmzu-gj57) field pais = '%s' for codigo %s" % (s.get("pais"), p["codigoproveedor"]),
                 "identifiers": {"secop_codigo_proveedor": p["codigoproveedor"], "nit_del_proveedor_adjudicado": p["nit_del_proveedor_adjudicado"], "registry_nit": s.get("nit")}, "address": {"line1": s.get("direccion"), "city": s.get("municipio"), "region": s.get("departamento"), "postal_code": None, "country": s.get("pais")}, "contact": {}},
      "raw": {"proceso": p, "proveedor_registro": s}}
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
json.dump(stats, open(dl + "normalize_stats.json", "w"), indent=1, ensure_ascii=False); print(stats)

#!/usr/bin/env python3
"""Match vendors to the AMP Registre des entreprises non admissibles aux contrats publics (RENA, Données Québec JSON).
Enterprise entries only (entries for natural persons are skipped) and personal fields (related person, majority shareholder,
municipality of residence of a person, natural-person name) are removed from raw.  Exact join on NEQ; name + city otherwise.
usage: python3 -I match_rena.py <rena.json> <retrieved_at>"""
import sys, os, re, json, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

FN, RETRIEVED = sys.argv[1], sys.argv[2]
DATASET = "https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises-non-admissibles-aux-contrats-publics-rena (rena.json)"
PAGE = "https://www.amp.quebec/rena/"
PERSONAL = ("Nom_personne_physique", "Nom_personne_liee", "Nom_de_lactionnaire_majoritaire", "Municipalite_de_residence_de_la_personne")
j = json.load(open(FN))["rena"]
pub = j.get("@attributes", {}).get("date")
vendors, meta = C.load_index()
need = C.need_map(vendors)
ents, by_neq, by_loose = {}, collections.defaultdict(set), collections.defaultdict(set)
skipped = 0
for i, x in enumerate(j["inscription"]):
    if (x.get("Nom_personne_physique") or "").strip() or not (x.get("Nom_entreprise") or "").strip():
        skipped += 1
        continue
    other = []
    m = re.search(r"Autres noms utilisés au Québec:\s*(.*)", x.get("Informations_complementaires") or "", re.S)
    if m:
        other = [s.strip() for s in m.group(1).split("\n") if s.strip()][:10]
    names = [x["Nom_entreprise"]] + other
    sk, lk = C.name_keys(names)
    addr = x.get("Adresse") or ""
    pm = re.search(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d", addr.upper())
    cm = re.search(r",\s*([^,()]+?)\s*\(([^)]+)\)", addr)
    neq = re.sub(r"\D", "", x.get("NEQ") or "")
    raw = {k: v for k, v in x.items() if k not in PERSONAL}
    ents[i] = {"sk": sk, "lk": lk, "postals": {C.norm_postal(pm.group(0))} if pm else set(), "cities": {C.norm_city(cm.group(1))} if cm else set(),
               "provs": {C.norm_prov(cm.group(2))} - {None} if cm else set(), "x": x, "raw": raw, "neq": neq, "other": other,
               "addr": {"full": addr, "city": cm.group(1) if cm else None, "region": C.norm_prov(cm.group(2)) if cm else None, "postal_code": pm.group(0) if pm else None}}
    if len(neq) == 10:
        by_neq[neq].add(i)
    for l in lk:
        if l in need:
            by_loose[l].add(i)
print("RENA entries", len(j["inscription"]), "enterprise entries", len(ents), "skipped natural persons", skipped, file=sys.stderr)
out = C.Out("amp_rena")
for v in vendors:
    cand = {}
    for neq, (conf, why) in v["ids"]["neq"].items():
        for i in by_neq.get(neq, ()):
            cand[i] = {"ent": i, "idmatch": (conf, "RENA NEQ %s equals the %s" % (neq, why))}
    C.resolve_id_ambiguity(cand)
    for l in v["lk"]:
        for i in by_loose.get(l, ()):
            cand.setdefault(i, {"ent": i, "idmatch": None})
    if not cand:
        continue
    cl = []
    for i, c in cand.items():
        E = ents[i]
        c.update({"strict": bool(v["sk"] & E["sk"]), "lkey_match": bool(v["lk"] & E["lk"]), "loc": C.loc_eval(v, E["postals"], E["cities"], E["provs"]),
                  "lkey": next(iter(E["lk"]), ""), "rec_provs": E["provs"]})
        if c["idmatch"] or c["lkey_match"]:
            cl.append(c)
    matches = []
    for c in C.grade(v, cl, local_dataset=True):  # sensitive flag: name-only matches need location agreement
        E = ents[c["ent"]]
        x = E["x"]
        end = x.get("Fin_inadmissibilite") or ""
        matches.append({"match_confidence": c["match_confidence"], "match_basis": c["basis"], "legal_name": x.get("Nom_entreprise"),
                        "identifiers": {"neq": E["neq"] or None}, "address": dict(E["addr"], country="CA"), "phones": [], "emails": [], "website": None,
                        "status": ("INELIGIBLE for Quebec public contracts until %s (RENA)" % end) if end >= "2026-10-25" else ("RENA inscription; ineligibility end date %s" % (end or "not stated")),
                        "extra": {"registered_on": x.get("Inscription_registre"), "ineligibility_end": end or None, "infraction": x.get("Infraction"),
                                  "amp_decision": x.get("Decision_AMP"), "category": x.get("Categorie"), "other_names_used_in_quebec": E["other"],
                                  "register_publication_date": pub, "personal_fields_removed": list(PERSONAL)},
                        "source_url": PAGE, "dataset_url": DATASET, "retrieved_at": RETRIEVED, "raw": E["raw"]})
    out.write(v, matches)
res = out.close()
res.update({"entries": len(j["inscription"]), "enterprise_entries": len(ents), "skipped_natural_persons": skipped, "register_date": pub})
json.dump(res, open(C.WORK + "/rena_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))

#!/usr/bin/env python3
"""Match vendors to (1) RBQ active-licence register (Quebec construction licences) and (2) CRA charities (2024 list).

Usage: python3 -I match_extra_rbq_charities.py <vendor_master.jsonl> <registry_v3.jsonl> <rbq_csv> <charities_ident_csv> <charities_weburl_csv> <outdir>
Writes <outdir>/vendors_extra_rbq.jsonl and <outdir>/vendors_extra_charities.jsonl (generic vendors_extra format, see PLAN.md).
"""
import sys, os, csv, json, re, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normname import strict_key, loose_key, norm_prov, norm_city, norm_postal  # noqa: E402

csv.field_size_limit(10 ** 9)
VM, REG, RBQ, CH_ID, CH_WEB, OUTD = sys.argv[1:7]
RBQ_DATASET = "https://www.donneesquebec.ca/recherche/dataset/licencesactives"
RBQ_RETRIEVED = "2026-10-25T07:14:51Z (dataset metadata_modified; downloaded 2026-10-26T02:46Z)"
CH_DATASET = "https://open.canada.ca/data/en/dataset/80c00cdb-1358-415c-bb8b-0de7f12675b8"
CH_RETRIEVED = "2026-10-26T02:46Z"
QC_POSTAL = re.compile(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d")

# ---------------- vendors ----------------
vendors = []
need = collections.defaultdict(set)
with open(VM, encoding="utf-8") as f:
    for i, line in enumerate(f):
        v = json.loads(line)
        names = [v.get("name")] + (v.get("name_variants") or [])
        sk, lk = set(), set()
        for n in names:
            if not n:
                continue
            for part in re.split(r"\s+(?:o/a|dba|d/b/a|operating as|faisant affaire sous|s/n)\s+", str(n), flags=re.I):
                for q in (part, re.sub(r"\(.*?\)", " ", part)):
                    s, l = strict_key(q), loose_key(q)
                    if l and len(l) >= 3 and not l.isdigit():
                        sk.add(s); lk.add(l)
        postals, fsas, cities, provs = set(), set(), set(), set()
        for a in v.get("addresses") or []:
            val = a.get("value") or {}
            if not isinstance(val, dict):
                continue
            p = norm_postal(val.get("postal_code"))
            if p:
                postals.add(p); fsas.add(p[:3])
            fo = str(val.get("postal_code_fsa") or "").strip().upper()
            if re.fullmatch(r"[A-Z]\d[A-Z]", fo):
                fsas.add(fo)
            c = norm_city(val.get("city"))
            if c:
                cities.add(c)
            pr = norm_prov(val.get("region"))
            if pr:
                provs.add(pr)
        neqs = {}
        for k, lst in (v.get("identifiers") or {}).items():
            if "neq" in k.lower():
                for e in lst:
                    q = re.sub(r"\D", "", str(e.get("value")))
                    if len(q) == 10:
                        neqs[q] = ("exact", "NEQ %s published for this vendor in the contract data" % q)
        vendors.append({"vendor_key": v["vendor_key"], "name": v.get("name"), "sk": sk, "lk": lk, "postals": postals, "fsas": fsas,
                        "cities": cities, "provs": provs, "neqs": neqs})
        for l in lk:
            need[l].add(i)
# add NEQ of exact/strong REQ match
with open(REG, encoding="utf-8") as f:
    for i, line in enumerate(f):
        d = json.loads(line)
        assert d["vendor_key"] == vendors[i]["vendor_key"]
        for m in d.get("registry_matches") or []:
            if m.get("registry") == "quebec_req" and m.get("match_confidence") in ("exact", "strong") and m.get("neq"):
                vendors[i]["neqs"].setdefault(m["neq"], (m["match_confidence"], "NEQ %s of the vendor's %s Quebec-registry match (%s)" % (m["neq"], m["match_confidence"], m.get("match_basis", "")[:120])))
                break
print("vendors", len(vendors), file=sys.stderr, flush=True)

# ---------------- RBQ ----------------
lic = {}
with open(RBQ, encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        num = row.get("Numéro de licence")
        if not num:
            continue
        L = lic.get(num)
        if L is None:
            L = lic[num] = {"row": {k: v for k, v in row.items() if k not in ("Categorie", "Sous-catégories")}, "categories": set(), "subcategories": set()}
        if row.get("Categorie"):
            L["categories"].add(row["Categorie"])
        if row.get("Sous-catégories"):
            L["subcategories"].add(row["Sous-catégories"])
by_neq = collections.defaultdict(list)
by_name = collections.defaultdict(list)
for num, L in lic.items():
    r = L["row"]
    q = re.sub(r"\D", "", r.get("NEQ") or "")
    if len(q) == 10:
        by_neq[q].append(num)
    for col in ("Nom de l'intervenant", "Autre nom"):
        if r.get(col):
            l = loose_key(r[col])
            if l in need:
                by_name[l].append(num)
print("rbq licences", len(lic), "with NEQ", len(by_neq), file=sys.stderr, flush=True)


def rbq_record(num, conf, basis):
    L = lic[num]; r = L["row"]
    individual = (r.get("Statut juridique") or "").lower().startswith("personne physique")
    addr = r.get("Adresse") or ""
    pc = QC_POSTAL.search(addr.upper())
    rec = {"match_confidence": conf, "match_basis": basis, "legal_name": r.get("Nom de l'intervenant"),
           "identifiers": {"rbq_licence_number": num, "neq": re.sub(r"\D", "", r.get("NEQ") or "") or None},
           "address": ({"line1": None, "city": r.get("Municipalité"), "region": "QC", "postal_code": pc.group(0) if pc else None, "country": "CA",
                        "note": "sole proprietor: street omitted for privacy"} if individual else
                       {"full": addr, "city": r.get("Municipalité"), "region": "QC", "postal_code": pc.group(0) if pc else None, "country": "CA"}),
           "phones": [] if individual or not r.get("Numéro de téléphone") else [re.sub(r"^(\d{3})(\d{3})(\d{4})$", r"\1-\2-\3", re.sub(r"\D", "", r["Numéro de téléphone"]))],
           "emails": [] if individual or not r.get("Courriel") else [{"email": r["Courriel"].strip().lower(), "label": "contact e-mail published in the RBQ licence register", "evidence_url": RBQ_DATASET}],
           "website": None, "status": r.get("Statut de la licence"),
           "extra": {"licence_type": r.get("Type de licence"), "issue_date": r.get("Date de délivrance"), "annual_payment_date": r.get("Date du paiement annuel"),
                     "restriction": r.get("Restriction"), "restriction_start": r.get("Date de début de la restriction") or None, "restriction_end": r.get("Date de fin de la restriction") or None,
                     "bond_provider": r.get("Association ou compagnie fournissant le cautionnement") or None, "bond_amount": r.get("Montant de la caution") or None,
                     "issuing_body": r.get("Mandataire"), "legal_status": r.get("Statut juridique"), "region": r.get("Région administrative"),
                     "categories": sorted(L["categories"]), "subcategories": sorted(L["subcategories"]), "subcategory_count": r.get("Nombre de sous-catégorie autorisées"),
                     "other_name": r.get("Autre nom") or None},
           "source_url": "https://www.rbq.gouv.qc.ca/ (licence %s; verify via RBQ licence search)" % num, "dataset_url": RBQ_DATASET, "retrieved_at": RBQ_RETRIEVED}
    raw = dict(r)
    if individual:
        for k in ("Courriel", "Numéro de téléphone", "Adresse"):
            raw.pop(k, None)
    raw["Categorie_all"] = sorted(L["categories"]); raw["Sous-catégories_all"] = sorted(L["subcategories"])
    rec["raw"] = raw
    return rec


n_rbq = 0
with open(os.path.join(OUTD, "vendors_extra_rbq.jsonl"), "w", encoding="utf-8") as out:
    for v in vendors:
        matches, seen = [], set()
        for q, (conf, basis) in v["neqs"].items():
            for num in by_neq.get(q, []):
                if num not in seen:
                    seen.add(num); matches.append(rbq_record(num, conf, basis))
        if not matches:
            cands = set()
            for l in v["lk"]:
                cands.update(by_name.get(l, []))
            good = []
            for num in cands:
                r = lic[num]["row"]
                sk = {strict_key(r.get("Nom de l'intervenant") or ""), strict_key(r.get("Autre nom") or "")} - {""}
                city = norm_city(r.get("Municipalité"))
                pc = QC_POSTAL.search((r.get("Adresse") or "").upper())
                pcn = norm_postal(pc.group(0)) if pc else None
                locok = (pcn and pcn in v["postals"]) or (city and city in v["cities"])
                if locok:
                    good.append((num, bool(sk & v["sk"]), "same postal code" if (pcn and pcn in v["postals"]) else "same municipality"))
            strict_good = [g for g in good if g[1]]
            pool = strict_good or good
            for num, strict, why in pool[:3]:
                conf = "strong" if (len(pool) == 1) else "weak"
                matches.append(rbq_record(num, conf, ("name equal after normalisation" if strict else "name equal except legal-form suffix") + "; " + why + "; no NEQ link available"))
        if matches:
            n_rbq += 1
            out.write(json.dumps({"vendor_key": v["vendor_key"], "name": v["name"], "source": "rbq_licences", "matches": matches}, ensure_ascii=False) + "\n")
print("rbq matched vendors", n_rbq, file=sys.stderr, flush=True)
del lic, by_neq, by_name

# ---------------- CRA charities ----------------
web = collections.defaultdict(list)
with open(CH_WEB, encoding="utf-8-sig", errors="replace", newline="") as f:
    for row in csv.DictReader(f):
        bn = (row.get("BN/NE") or "").strip()
        u = (row.get("Contact URL") or "").strip()
        if bn and u:
            web[bn].append(u if u.lower().startswith("http") else "http://" + u.lower())
ch_by_loose = collections.defaultdict(list)
charities = {}
with open(CH_ID, encoding="utf-8-sig", errors="replace", newline="") as f:
    for row in csv.DictReader(f):
        bn = (row.get("BN") or "").strip()
        hit = False
        for col in ("Legal Name", "Account Name"):
            if row.get(col):
                l = loose_key(row[col])
                if l in need:
                    ch_by_loose[l].append(bn); hit = True
        if hit:
            charities[bn] = dict(row)
print("charities candidate rows", len(charities), file=sys.stderr, flush=True)
n_ch = 0
with open(os.path.join(OUTD, "vendors_extra_charities.jsonl"), "w", encoding="utf-8") as out:
    for v in vendors:
        cands = set()
        for l in v["lk"]:
            cands.update(ch_by_loose.get(l, []))
        if not cands:
            continue
        scored = []
        for bn in cands:
            r = charities[bn]
            sk = {strict_key(r.get("Legal Name") or ""), strict_key(r.get("Account Name") or "")} - {""}
            p = norm_postal(r.get("Postal Code")); c = norm_city(r.get("City")); pr = norm_prov(r.get("Province"))
            strict = bool(sk & v["sk"])
            pe = bool(p and p in v["postals"]); fsa = bool(p and p[:3] in v["fsas"]) and not pe; city = bool(c and c in v["cities"])
            pa = bool(pr and pr in v["provs"]); pc = bool(v["provs"]) and bool(pr) and not pa
            score = (3 if strict else 1) + 4 * pe + 2 * fsa + 2 * city + pa - 3 * pc
            basis = ["name equal after normalisation" if strict else "name equal except legal-form suffix"]
            if pe: basis.append("same postal code")
            if fsa: basis.append("same postal FSA")
            if city: basis.append("same city")
            if pc: basis.append("PROVINCE CONFLICT")
            scored.append((score, strict, pe or fsa or city, pc, bn, basis))
        scored.sort(key=lambda t: -t[0])
        locgood = [s for s in scored if s[2] and not s[3]]
        strict_all = [s for s in scored if s[1] and not s[3]]
        matches = []
        for s in scored[:3]:
            score, strict, loc, pc, bn, basis = s
            if loc and not pc and len(locgood) == 1:
                conf = "exact" if strict else "strong"
            elif strict and not pc and len(strict_all) == 1 and not (v["postals"] or v["cities"]):
                conf = "strong"; basis.append("only charity with this name; no vendor location to compare")
            else:
                conf = "weak"
            r = charities[bn]
            bn9 = bn[:9] if re.fullmatch(r"\d{9}RR\d{4}", bn) else None
            matches.append({"match_confidence": conf, "match_basis": "; ".join(basis), "legal_name": r.get("Legal Name"),
                            "identifiers": {"charity_registration_number": bn, "business_number_bn9": bn9},
                            "address": {"line1": r.get("Address Line 1") or None, "line2": r.get("Address Line 2") or None, "city": r.get("City"),
                                        "region": r.get("Province"), "postal_code": r.get("Postal Code"), "country": r.get("Country")},
                            "phones": [], "emails": [], "website": (web.get(bn) or [None])[0], "status": "registered charity (2024 list)",
                            "extra": {"account_name": r.get("Account Name"), "category_code": r.get("Category"), "sub_category_code": r.get("Sub Category"),
                                      "designation_code": r.get("Designation"), "all_websites": web.get(bn) or []},
                            "source_url": "https://apps.cra-arc.gc.ca/ebci/hacc/srch/pub/dsplyRprtngPrd?q.srchNmFltr=&q.stts=0007&selectedCharityBn=%s" % bn,
                            "dataset_url": CH_DATASET, "retrieved_at": CH_RETRIEVED, "raw": r})
        if matches:
            n_ch += 1
            out.write(json.dumps({"vendor_key": v["vendor_key"], "name": v["name"], "source": "cra_charities", "matches": matches}, ensure_ascii=False) + "\n")
print("charity matched vendors", n_ch, file=sys.stderr, flush=True)

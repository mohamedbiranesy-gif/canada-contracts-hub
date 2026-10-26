#!/usr/bin/env python3
"""Match vendors to Corporations Canada (federal corporations, incl. Business Number) and the
Registraire des entreprises du Quebec (REQ) open data.

Usage: python3 -I match_registries.py <vendor_master.jsonl> <corporations_canada_dir> <req_zip> <out.jsonl> <stats.json>
"""
import sys, os, csv, json, re, io, zipfile, collections, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normname import strict_key, loose_key, norm_prov, norm_city, norm_postal, strip_accents  # noqa: E402

csv.field_size_limit(10 ** 9)
VM, CCDIR, REQZIP, OUT, STATS = sys.argv[1:6]
CC_RETRIEVED = "2026-10-25T18:56:02Z"
REQ_RETRIEVED = "2026-10-25T18:56:27Z"
CC_DATASET = "https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2"
REQ_DATASET = "https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises"
CC_DETAIL = "https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId={}"

SPLIT_RE = re.compile(r"\s+(?:o/a|o\.a\.|dba|d/b/a|d\.b\.a\.|operating as|doing business as|carrying on business as|c\.o\.b\.|cob|faisant affaire sous(?: le nom de)?|f\.a\.s\.|s/n|sous le nom de|aka|a\.k\.a\.|t/a|trading as)\s+", re.I)
PAREN_RE = re.compile(r"\([^)]*\)")
NUMBERED_RE = re.compile(r"^\d{4,}[\s-]?\d*\s+(QUEBEC|CANADA|ONTARIO|ALBERTA|BC|B C|NOVA SCOTIA|MANITOBA|SASKATCHEWAN|NEW BRUNSWICK)\b")
GENERIC = {"SERVICES", "CONSULTING", "CONSTRUCTION", "SOLUTIONS", "TECHNOLOGIES", "GROUP", "GROUPE", "ENTERPRISES", "ENTREPRISES",
           "HOLDINGS", "INDUSTRIES", "SYSTEMS", "INTERNATIONAL", "CANADA", "MANAGEMENT", "ASSOCIATES", "INC", "LTD", "CORP"}


def variants(names):
    out = []
    for n in names:
        if not n:
            continue
        n = str(n)
        parts = [n] + SPLIT_RE.split(n)
        for p in parts:
            p = p.strip(" ,;-")
            if p:
                out.append(p)
                q = PAREN_RE.sub(" ", p).strip()
                if q and q != p:
                    out.append(q)
    seen, res = set(), []
    for v in out:
        if v not in seen:
            seen.add(v)
            res.append(v)
    return res[:16]


def distinctive(lkey):
    toks = lkey.split()
    if NUMBERED_RE.match(lkey):
        return True
    non_generic = [t for t in toks if t not in GENERIC and len(t) > 2]
    return len(non_generic) >= 2 or (len(non_generic) == 1 and len(non_generic[0]) >= 6 and len(toks) >= 2)


# ---------------- load vendors ----------------
vendors = []
need_loose = collections.defaultdict(set)   # loose key -> vendor idx
need_neq = collections.defaultdict(set)
with open(VM, encoding="utf-8") as f:
    for i, line in enumerate(f):
        v = json.loads(line)
        names = [v.get("name")] + (v.get("name_variants") or [])
        vs = variants(names)
        skeys, lkeys = set(), set()
        for n in vs:
            s, l = strict_key(n), loose_key(n)
            if l and len(l) >= 3 and not l.isdigit():
                skeys.add(s)
                lkeys.add(l)
        postals, fsas, cities, provs = set(), set(), set(), set()
        for a in v.get("addresses") or []:
            val = a.get("value") or {}
            if not isinstance(val, dict):
                continue
            p = norm_postal(val.get("postal_code"))
            if p:
                postals.add(p)
                fsas.add(p[:3])
            fsa_only = str(val.get("postal_code_fsa") or "").strip().upper()
            if re.fullmatch(r"[A-Z]\d[A-Z]", fsa_only):
                fsas.add(fsa_only)
            c = norm_city(val.get("city"))
            if c:
                cities.add(c)
            pr = norm_prov(val.get("region"))
            if pr:
                provs.add(pr)
        neqs = set()
        ids = v.get("identifiers") or {}
        for k, lst in ids.items():
            if "neq" in k.lower():
                for e in lst:
                    val = re.sub(r"\D", "", str(e.get("value")))
                    if len(val) == 10:
                        neqs.add(val)
        rec = {"vendor_key": v["vendor_key"], "name": v.get("name"), "variants": vs, "skeys": skeys, "lkeys": lkeys,
               "postals": postals, "fsas": fsas, "cities": cities, "provs": provs, "neqs": neqs,
               "ids": ids, "record_count": v.get("record_count"), "rc_hm": v.get("record_count_high_or_medium"),
               "countries": [c.get("value") for c in (v.get("countries") or [])]}
        vendors.append(rec)
        for l in lkeys:
            need_loose[l].add(i)
        for q in neqs:
            need_neq[q].add(i)
print("vendors", len(vendors), "loose keys", len(need_loose), "neqs", len(need_neq), file=sys.stderr, flush=True)

# ---------------- Corporations Canada ----------------
cc = {}                                   # corp number -> row dict (+file)
cc_by_loose = collections.defaultdict(set)
for fn in sorted(os.listdir(CCDIR)):
    if not fn.endswith(".csv"):
        continue
    with open(os.path.join(CCDIR, fn), encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            hit = False
            for col in ("Corporate name - form 1", "Corporate name - form 2"):
                nm = row.get(col)
                if not nm:
                    continue
                l = loose_key(nm)
                if l in need_loose:
                    cc_by_loose[l].add(row["Corporation number"])
                    hit = True
            if hit:
                row = dict(row)
                row["_file"] = fn
                prev = cc.get(row["Corporation number"])
                if prev is None or (prev.get("Status") != "Active" and row.get("Status") == "Active"):
                    cc[row["Corporation number"]] = row
    print("cc file", fn, len(cc), file=sys.stderr, flush=True)

# ---------------- REQ ----------------
z = zipfile.ZipFile(REQZIP)
dom = collections.defaultdict(dict)
with z.open("DomaineValeur.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig")):
        dom[row["TYP_DOM_VAL"]][row["COD_DOM_VAL"]] = row["VAL_DOM_FRAN"]

req_names = collections.defaultdict(list)    # neq -> name rows
req_by_loose = collections.defaultdict(set)
with z.open("Nom.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace")):
        neq = row["NEQ"]
        hit = neq in need_neq
        for col in ("NOM_ASSUJ", "NOM_ASSUJ_LANG_ETRNG"):
            nm = row.get(col)
            if nm:
                l = loose_key(nm)
                if l in need_loose:
                    req_by_loose[l].add(neq)
                    hit = True
        if hit:
            req_names[neq].append(row)
print("req names matched entities", len(req_names), file=sys.stderr, flush=True)
want = set(req_names) | set(need_neq)
# second pass to collect ALL names (current + former) of matched entities
allnames = collections.defaultdict(list)
with z.open("Nom.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace")):
        if row["NEQ"] in want:
            allnames[row["NEQ"]].append(row)
ent = {}
with z.open("Entreprise.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace")):
        if row["NEQ"] in want:
            ent[row["NEQ"]] = row
etab = collections.defaultdict(list)
with z.open("Etablissements.csv") as fh:
    for row in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace")):
        if row["NEQ"] in want and len(etab[row["NEQ"]]) < 25:
            etab[row["NEQ"]].append(row)
print("req entreprises", len(ent), "with establishments", len(etab), file=sys.stderr, flush=True)

QC_POSTAL = re.compile(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d")


def req_locs(neq):
    e = ent.get(neq) or {}
    postals, cities, provs = set(), set(), set()
    lines = [e.get("ADR_DOMCL_LIGN%d_ADR" % i) for i in range(1, 5)]
    for et in etab.get(neq, []):
        lines += [et.get("LIGN%d_ADR" % i) for i in range(1, 5)]
    for ln in lines:
        if not ln:
            continue
        m = QC_POSTAL.search(ln.upper())
        if m:
            postals.add(norm_postal(m.group(0)))
        m2 = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", ln.strip())
        if m2:
            c = norm_city(m2.group(1))
            if c:
                cities.add(c)
            p = norm_prov(m2.group(2))
            if p:
                provs.add(p)
    postals.discard(None)
    return postals, {p[:3] for p in postals}, cities, provs


def cc_locs(row):
    p = norm_postal(row.get("Postal code"))
    c = norm_city(row.get("City/town"))
    pr = norm_prov(row.get("Province/territory"))
    return ({p} if p else set()), ({p[:3]} if p else set()), ({c} if c else set()), ({pr} if pr else set())


def score(v, skeys_e, locs, active):
    postals, fsas, cities, provs = locs
    strict = bool(v["skeys"] & skeys_e)
    pe = bool(v["postals"] & postals)
    fsa = bool(v["fsas"] & fsas) and not pe
    city = bool(v["cities"] & cities)
    pa = bool(v["provs"] & provs)
    pc = bool(v["provs"]) and bool(provs) and not pa
    s = (3 if strict else 1) + (4 if pe else 0) + (2 if fsa else 0) + (2 if city else 0) + (1 if pa else 0) - (3 if pc else 0) + (1 if active else 0)
    basis = []
    basis.append("name equal after normalisation" if strict else "name equal except legal-form suffix")
    if pe: basis.append("same postal code")
    if fsa: basis.append("same postal FSA")
    if city: basis.append("same city")
    if pa and not (pe or city): basis.append("same province")
    if pc: basis.append("PROVINCE CONFLICT (vendor %s vs registry %s)" % ("/".join(sorted(v["provs"])), "/".join(sorted(provs))))
    if not (v["postals"] or v["cities"] or v["provs"]): basis.append("no vendor location in contract data")
    return s, strict, (pe or fsa or city), pc, basis


def grade(cands, v):
    """cands: list of dicts with score, strict, locagree, pc. returns list sorted with confidence"""
    if not cands:
        return []
    cands.sort(key=lambda c: -c["_score"])
    strict_c = [c for c in cands if c["_strict"]]
    loc_c = [c for c in cands if c["_locagree"] and not c["_pc"]]
    for c in cands:
        conf = "weak"
        if c.get("_idmatch"):
            conf = "exact"
        elif c["_strict"] and c["_locagree"] and not c["_pc"]:
            conf = "exact" if len([x for x in strict_c if x["_locagree"]]) == 1 else "strong"
        elif c["_locagree"] and not c["_pc"] and len(loc_c) == 1:
            conf = "strong"
        elif c["_strict"] and len(strict_c) == 1 and not c["_pc"]:
            if v["provs"] and not (c["_provs"] & v["provs"]) and c["_provs"]:
                conf = "weak"
            elif v["postals"] or v["cities"] or v["provs"]:
                conf = "strong"
            else:
                conf = "strong" if distinctive(c["_lkey"]) else "weak"
        c["match_confidence"] = conf
    order = {"exact": 0, "strong": 1, "weak": 2}
    cands.sort(key=lambda c: (order[c["match_confidence"]], -c["_score"]))
    return cands[:6]


def cc_record(row):
    corp = row["Corporation number"]
    bn = re.sub(r"\D", "", row.get("Business number (BN)") or "")
    return {"registry": "corporations_canada", "legal_name": row.get("Corporate name - form 1"),
            "other_names": [x for x in [row.get("Corporate name - form 2")] if x],
            "corporation_number": corp, "business_number_bn9": bn if len(bn) == 9 else None,
            "jurisdiction": "Canada (federal)", "governing_legislation": row.get("Governing legislation"),
            "status": row.get("Status"), "status_detail": row.get("Status Detail") or None,
            "anniversary_date": row.get("Anniversary date") or None, "year_of_last_annual_filing": row.get("Year of last annual filing") or None,
            "registered_office": {"line1": row.get("Street") or None, "line2": row.get("Street 2") or None, "city": row.get("City/town") or None,
                                  "region": row.get("Province/territory") or None, "postal_code": row.get("Postal code") or None, "country": row.get("Country") or None},
            "directors_min_max": [row.get("Minimum number of directors"), row.get("Maximum number of directors")],
            "source_url": CC_DETAIL.format(corp), "dataset_url": CC_DATASET, "retrieved_at": CC_RETRIEVED,
            "raw": {k: v for k, v in row.items()}}


def req_record(neq):
    e = ent.get(neq) or {}
    names = allnames.get(neq) or req_names.get(neq) or []
    cur = [n["NOM_ASSUJ"] for n in names if n.get("STAT_NOM") == "V"]
    legal = next((n["NOM_ASSUJ"] for n in names if n.get("STAT_NOM") == "V" and n.get("TYP_NOM_ASSUJ") in ("M", "N")), cur[0] if cur else (names[0]["NOM_ASSUJ"] if names else None))
    form = e.get("COD_FORME_JURI")
    individual = form == "IND"
    addr_lines = [e.get("ADR_DOMCL_LIGN%d_ADR" % i) for i in range(1, 5)]
    addr = {"lines": [x for x in addr_lines if x]}
    ests = []
    for et in etab.get(neq, []):
        lines = [et.get("LIGN%d_ADR" % i) for i in range(1, 5) if et.get("LIGN%d_ADR" % i)]
        ests.append({"suffix": et.get("NO_SUF_ETAB"), "principal": et.get("IND_ETAB_PRINC") == "O", "name": et.get("NOM_ETAB") or None,
                     "address_lines": lines if not individual else [l for l in lines if "(" in l or QC_POSTAL.search(l.upper() or "")],
                     "activity": et.get("DESC_ACT_ECON_ETAB") or dom["ACT_ECON"].get(et.get("COD_ACT_ECON") or "", None),
                     "activity_code_cae": et.get("COD_ACT_ECON") or None})
    if individual:
        addr = {"lines": [l for l in addr_lines if l and ("(" in l or QC_POSTAL.search(l.upper()))],
                "note": "sole proprietorship: street line omitted for privacy (city/postal code kept)"}
    raw_e = dict(e)
    if individual:
        for i in (1, 2):
            raw_e.pop("ADR_DOMCL_LIGN%d_ADR" % i, None)
    return {"registry": "quebec_req", "legal_name": legal, "other_names": sorted({n["NOM_ASSUJ"] for n in names if n.get("NOM_ASSUJ") and n["NOM_ASSUJ"] != legal})[:15],
            "neq": neq, "business_number_bn9": None, "jurisdiction": dom["REGIM_JURI"].get(e.get("COD_REGIM_JURI") or "", e.get("COD_REGIM_JURI")),
            "jurisdiction_of_constitution": dom["REGIM_JURI"].get(e.get("COD_REGIM_JURI_CONSTI") or "", e.get("COD_REGIM_JURI_CONSTI")),
            "legal_form": dom["FORM_JURI"].get(form or "", form), "status": dom["STAT_IMMAT"].get(e.get("COD_STAT_IMMAT") or "", e.get("COD_STAT_IMMAT")),
            "status_date": e.get("DAT_STAT_IMMAT") or None, "registration_date": e.get("DAT_IMMAT") or None, "constitution_date": e.get("DAT_CONSTI") or None,
            "bankruptcy_flag": e.get("IND_FAIL") or None,
            "employees_in_quebec": dom["INTVAL_EMPLO_QUE"].get(e.get("COD_INTVAL_EMPLO_QUE") or "", e.get("COD_INTVAL_EMPLO_QUE")),
            "main_activity": e.get("DESC_ACT_ECON_ASSUJ") or dom["ACT_ECON"].get(e.get("COD_ACT_ECON_CAE") or "", None),
            "main_activity_code_cae": e.get("COD_ACT_ECON_CAE") or None,
            "secondary_activity": e.get("DESC_ACT_ECON_ASSUJ2") or dom["ACT_ECON"].get(e.get("COD_ACT_ECON_CAE2") or "", None),
            "last_annual_declaration_year": e.get("AN_DECL") or None,
            "domicile_address": addr, "establishments": ests,
            "names_history": [{"name": n.get("NOM_ASSUJ"), "foreign_language_name": n.get("NOM_ASSUJ_LANG_ETRNG") or None,
                               "status": dom["STAT_NOM"].get(n.get("STAT_NOM") or "", n.get("STAT_NOM")), "type": dom["TYP_NOM"].get(n.get("TYP_NOM_ASSUJ") or "", n.get("TYP_NOM_ASSUJ")),
                               "from": n.get("DAT_INIT_NOM_ASSUJ") or None, "to": n.get("DAT_FIN_NOM_ASSUJ") or None} for n in names[:30]],
            "source_url": REQ_DATASET, "lookup_hint": "search NEQ %s in the Registraire des entreprises online search" % neq,
            "dataset_url": REQ_DATASET, "retrieved_at": REQ_RETRIEVED, "raw": {"entreprise": raw_e}}


stats = collections.Counter()
with open(OUT, "w", encoding="utf-8") as out:
    for i, v in enumerate(vendors):
        # --- CC candidates
        cands = []
        ids = set()
        for l in v["lkeys"]:
            ids |= cc_by_loose.get(l, set())
        for corp in ids:
            row = cc[corp]
            sk = {strict_key(row.get("Corporate name - form 1") or ""), strict_key(row.get("Corporate name - form 2") or "")} - {""}
            locs = cc_locs(row)
            s, strict, la, pc, basis = score(v, sk, locs, row.get("Status") == "Active")
            if row.get("Status") != "Active":
                basis.append("registry status: %s" % row.get("Status"))
            cands.append({"_score": s, "_strict": strict, "_locagree": la, "_pc": pc, "_provs": locs[3], "_lkey": loose_key(row.get("Corporate name - form 1") or ""),
                          "_basis": basis, "_ref": ("cc", corp)})
        cc_g = grade(cands, v)
        # --- REQ candidates
        cands = []
        neqs = set(v["neqs"])
        for l in v["lkeys"]:
            neqs |= req_by_loose.get(l, set())
        for neq in neqs:
            if neq not in ent and neq not in allnames:
                continue
            names = allnames.get(neq) or req_names.get(neq) or []
            sk = set()
            for n in names:
                for col in ("NOM_ASSUJ", "NOM_ASSUJ_LANG_ETRNG"):
                    if n.get(col):
                        sk.add(strict_key(n[col]))
            locs = req_locs(neq)
            e = ent.get(neq) or {}
            s, strict, la, pc, basis = score(v, sk, locs, e.get("COD_STAT_IMMAT") == "IM")
            idm = neq in v["neqs"]
            if idm:
                basis.insert(0, "NEQ published in the contract data equals registry NEQ")
                s += 10
            if e.get("COD_STAT_IMMAT") and e.get("COD_STAT_IMMAT") != "IM":
                basis.append("registry status: %s" % dom["STAT_IMMAT"].get(e.get("COD_STAT_IMMAT"), e.get("COD_STAT_IMMAT")))
            lk = loose_key(names[0]["NOM_ASSUJ"]) if names else ""
            cands.append({"_score": s, "_strict": strict or idm, "_locagree": la or idm, "_pc": pc and not idm, "_provs": locs[3], "_lkey": lk,
                          "_basis": basis, "_ref": ("req", neq), "_idmatch": idm})
        req_g = grade(cands, v)
        matches = []
        for c in cc_g + req_g:
            kind, ref = c["_ref"]
            m = cc_record(cc[ref]) if kind == "cc" else req_record(ref)
            m["match_confidence"] = c["match_confidence"]
            m["match_basis"] = "; ".join(c["_basis"])
            m["match_score"] = c["_score"]
            matches.append(m)
        best_cc = next((m for m in matches if m["registry"] == "corporations_canada" and m["match_confidence"] in ("exact", "strong")), None)
        best_req = next((m for m in matches if m["registry"] == "quebec_req" and m["match_confidence"] in ("exact", "strong")), None)
        bn9 = best_cc["business_number_bn9"] if best_cc else None
        tax = {"bn9": bn9,
               "bn9_source": ("Corporations Canada federal corporation %s (%s match: %s)" % (best_cc["corporation_number"], best_cc["match_confidence"], best_cc["match_basis"])) if bn9 else None,
               "gst_hst_account_derived": (bn9 + "RT0001") if bn9 else None,
               "gst_hst_derivation_note": ("DERIVED, not published: a business's first GST/HST program account is normally BN9 + RT0001; only valid if the business is GST/HST-registered. Confirm in the CRA GST/HST Registry before relying on it.") if bn9 else None,
               "cra_registry_check": {"result": "not_checked"}}
        stats["vendors"] += 1
        stats["cc_any"] += bool(cc_g)
        stats["req_any"] += bool(req_g)
        if best_cc: stats["cc_" + best_cc["match_confidence"]] += 1
        if best_req: stats["req_" + best_req["match_confidence"]] += 1
        if bn9: stats["bn9"] += 1
        if best_cc or best_req: stats["any_strong_or_exact"] += 1
        if v["rc_hm"]:
            stats["hm_vendors"] += 1
            if best_cc or best_req: stats["hm_any_strong_or_exact"] += 1
            if bn9: stats["hm_bn9"] += 1
        out.write(json.dumps({"vendor_key": v["vendor_key"], "name": v["name"], "name_variants_used": v["variants"],
                              "registry_matches": matches,
                              "best_match": {"corporations_canada": best_cc["corporation_number"] if best_cc else None,
                                             "quebec_req": best_req["neq"] if best_req else None},
                              "registered_address_best": (best_cc or {}).get("registered_office") or ((best_req or {}).get("domicile_address")),
                              "tax": tax}, ensure_ascii=False) + "\n")
        if i % 20000 == 0:
            print("matched", i, dict(stats), file=sys.stderr, flush=True)
with open(STATS, "w") as f:
    json.dump(dict(stats), f, indent=1)
print(json.dumps(dict(stats), indent=1))

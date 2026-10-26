"""Shared helpers for the vendors_extra_<source> matchers (GLEIF, Wikidata, Health Canada, lobbyists, CID, city licences ...).

Re-uses ../enrichment_vendors/normname.py.  The vendor index (names, locations, registry identifiers) is built once from
vendor_master_input.jsonl + vendors_registry_v3.jsonl (+ BC OrgBook shards present at build time) and cached as a pickle.
"""
import sys, os, re, json, glob, pickle, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "enrichment_vendors"))
from normname import strict_key, loose_key, norm_prov, norm_city, norm_postal, strip_accents, tokens  # noqa: E402,F401

ROOT = "."
V2 = ROOT + "/enrichment/v2"
WORK = ROOT + "/work/vextra"
UA = "contracts-research/1.0 (public-sector contract vendor enrichment)"

SPLIT_RE = re.compile(r"\s+(?:o/a|o\.a\.|dba|d/b/a|d\.b\.a\.|operating as|doing business as|carrying on business as|c\.o\.b\.|cob|faisant affaire sous(?: le nom de)?|f\.a\.s\.|s/n|sous le nom de|aka|a\.k\.a\.|t/a|trading as)\s+", re.I)
PAREN_RE = re.compile(r"\([^)]*\)")
NUMBERED_RE = re.compile(r"^\d{4,}[\s-]?\d*\s+(QUEBEC|CANADA|ONTARIO|ALBERTA|BC|B C|NOVA SCOTIA|MANITOBA|SASKATCHEWAN|NEW BRUNSWICK)\b")
GENERIC = {"SERVICES", "CONSULTING", "CONSTRUCTION", "SOLUTIONS", "TECHNOLOGIES", "GROUP", "GROUPE", "ENTERPRISES", "ENTREPRISES",
           "HOLDINGS", "INDUSTRIES", "SYSTEMS", "INTERNATIONAL", "CANADA", "MANAGEMENT", "ASSOCIATES", "INC", "LTD", "CORP", "AND",
           "OF", "THE", "DE", "DU", "DES", "ET", "SERVICE", "COMPANY", "CO", "LTEE", "CIE", "LIMITED", "CORPORATION"}
ORG_MARKERS = {"INC", "LTD", "LTEE", "CORP", "CO", "CIE", "LLC", "LLP", "LP", "ULC", "SENC", "SENCRL", "ENR", "PLC", "GMBH", "SA", "SAS",
               "GROUP", "GROUPE", "SERVICES", "SERVICE", "SOLUTIONS", "CONSULTING", "CONSTRUCTION", "ASSOCIATES", "ENTERPRISES",
               "ENTREPRISES", "INDUSTRIES", "SYSTEMS", "TECHNOLOGIES", "TECHNOLOGY", "HOLDINGS", "PARTNERS", "CANADA", "INTERNATIONAL",
               "MANAGEMENT", "SOCIETY", "SOCIETE", "ASSOCIATION", "FOUNDATION", "FONDATION", "UNIVERSITY", "UNIVERSITE", "COLLEGE",
               "INSTITUTE", "INSTITUT", "COUNCIL", "CONSEIL", "CLUB", "CENTRE", "CENTER", "AGENCY", "AGENCE", "MEDIA", "LABS", "LAB",
               "LABORATORIES", "LABORATOIRE", "LABORATOIRES", "CONSULTANTS", "ENGINEERING", "INGENIERIE", "SUPPLY", "SUPPLIES", "EQUIPMENT",
               "PRODUCTS", "PRODUITS", "DISTRIBUTION", "DISTRIBUTORS", "MANUFACTURING", "LIMITED", "INCORPORATED", "CORPORATION",
               "COMPANY", "COMPAGNIE", "TRUST", "BANK", "BANQUE", "COOP", "COOPERATIVE", "NETWORK", "RESEARCH", "MARKETING", "DESIGN",
               "STUDIO", "STUDIOS", "PRODUCTIONS", "TRANSPORT", "LOGISTICS", "ELECTRIC", "ELECTRIQUE", "MECHANICAL", "PLUMBING",
               "HEATING", "ROOFING", "PAVING", "LANDSCAPING", "CLEANING", "SECURITY", "SECURITE", "SOFTWARE", "INFORMATIQUE", "MOTORS",
               "SALES", "RENTALS", "RENTAL", "LOCATION", "TRANSPORTS", "EXCAVATION", "CONTRACTING", "CONTRACTORS", "BUILDERS", "HOMES",
               "PHARMACY", "PHARMACIE", "CLINIC", "CLINIQUE", "HOSPITAL", "HOTEL", "RESTAURANT", "INN", "FARMS", "FARM", "FERME",
               "MARINE", "AVIATION", "ENERGY", "ENERGIE", "POWER", "ENVIRONMENTAL", "ENVIRONNEMENT", "GLOBAL", "NORTH", "WEST", "EAST"}


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def variants(names):
    out = []
    for n in names:
        if not n:
            continue
        n = str(n)
        for p in [n] + SPLIT_RE.split(n):
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


def name_keys(names):
    sk, lk = set(), set()
    for n in variants(names):
        s, l = strict_key(n), loose_key(n)
        if l and len(l) >= 3 and not l.isdigit():
            sk.add(s)
            lk.add(l)
    return sk, lk


def distinctive(lkey):
    toks = lkey.split()
    if NUMBERED_RE.match(lkey):
        return True
    non_generic = [t for t in toks if t not in GENERIC and len(t) > 2]
    return len(non_generic) >= 2 or (len(non_generic) == 1 and len(non_generic[0]) >= 6 and len(toks) >= 2)


_LEX = None
LEX_PATH = WORK + "/name_lexicon.json"
TORONTO_CSV = ROOT + "/downloads/city_business_licences/toronto_business_licences_data.csv"
COMMA_PERSON_RE = re.compile(r"^[A-Za-zÀ-ÿ'\-\. ]+,\s*[A-Za-zÀ-ÿ'\-\. ]+$")


def name_lexicon():
    """given names / surnames learned from the City of Toronto licence file, where individual licensees are written 'SURNAME, GIVEN [MIDDLE]'."""
    global _LEX
    if _LEX is not None:
        return _LEX
    if os.path.exists(LEX_PATH):
        d = json.load(open(LEX_PATH))
    else:
        import csv
        given, sur = collections.Counter(), collections.Counter()
        if os.path.exists(TORONTO_CSV):
            for r in csv.DictReader(open(TORONTO_CSV, encoding="utf-8", errors="replace")):
                s = (r.get("Client Name") or "").strip()
                if COMMA_PERSON_RE.match(s):
                    a, b = s.split(",", 1)
                    ta, tb = tokens(a), tokens(b)
                    if any(x in ORG_MARKERS for x in ta + tb):
                        continue
                    for x in ta:
                        if len(x) > 1:
                            sur[x] += 1
                    for x in tb:
                        if len(x) > 1:
                            given[x] += 1
        d = {"given": sorted(k for k, n in given.items() if n >= 1), "surname": sorted(k for k, n in sur.items() if n >= 1)}
        os.makedirs(WORK, exist_ok=True)
        json.dump(d, open(LEX_PATH, "w"))
    _LEX = {"given": set(d["given"]), "surname": set(d["surname"])}
    return _LEX


def looks_like_person(name):
    """True when a licence-holder name looks like an individual ('SMITH, JOHN', 'John A. Smith', 'DHAMI DEVINDER') rather than an organisation:
    'SURNAME, GIVEN' format, or 2-4 tokens that are all known given names/surnames/initials (lexicon from Toronto individual licensees)
    with at least one given name, and no organisational marker or digit."""
    if not name:
        return False
    s = str(name).strip()
    t = tokens(s)
    if not t:
        return False
    if any(x in ORG_MARKERS for x in t) or any(ch.isdigit() for ch in s):
        return False
    if COMMA_PERSON_RE.match(s) and len(t) <= 5:
        return True
    lex = name_lexicon()
    if 2 <= len(t) <= 4 and all(x.isalpha() for x in t):
        known = [x in lex["given"] or x in lex["surname"] or len(x) == 1 for x in t]
        if all(known) and any(x in lex["given"] for x in t) and sum(len(x) > 1 for x in t) >= 2:
            return True
    return False


STREETNUM_RE = re.compile(r"^\s*(?:(?:SUITE|UNIT|BUREAU|STE|APT|#)\s*[\w-]+[\s,]+)?(\d+[A-Z]?)(?:\s*-\s*(\d+[A-Z]?))?\b", re.I)


def street_numbers(line):
    """house/civic numbers at the start of an address line ('400-5560 Explorer Drive' -> {'400','5560'})."""
    if not line:
        return set()
    m = STREETNUM_RE.match(str(line))
    if not m:
        return set()
    return {g.lstrip("0") or "0" for g in m.groups() if g}


def norm_phone(p):
    if not p:
        return None
    d = re.sub(r"\D", "", str(p))
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    if len(d) != 10:
        return None
    return "%s-%s-%s" % (d[:3], d[3:6], d[6:])


# ------------------------------------------------------------------ vendor index
def build_index(path_pkl):
    VM = V2 + "/vendor_master_input.jsonl"
    REG = V2 + "/vendors_registry_v3.jsonl"
    vendors = []
    with open(VM, encoding="utf-8") as f:
        for i, line in enumerate(f):
            v = json.loads(line)
            names = [v.get("name")] + (v.get("name_variants") or [])
            sk, lk = name_keys(names)
            postals, fsas, cities, provs, streets = set(), set(), set(), set(), set()
            for a in v.get("addresses") or []:
                val = a.get("value") or {}
                if not isinstance(val, dict):
                    continue
                p = norm_postal(val.get("postal_code"))
                if p:
                    postals.add(p)
                    fsas.add(p[:3])
                    for sn in street_numbers(val.get("line1")):
                        streets.add((sn, p))
                fo = str(val.get("postal_code_fsa") or "").strip().upper()
                if re.fullmatch(r"[A-Z]\d[A-Z]", fo):
                    fsas.add(fo)
                c = norm_city(val.get("city"))
                if c:
                    cities.add(c)
                pr = norm_prov(val.get("region"))
                if pr:
                    provs.add(pr)
            ids = {"neq": {}, "cc": {}, "bn9": {}, "bc": {}, "lei": {}, "ticker": {}}
            for k, lst in (v.get("identifiers") or {}).items():
                kl = k.lower()
                for e in lst:
                    val = str(e.get("value"))
                    if "neq" in kl:
                        q = re.sub(r"\D", "", val)
                        if len(q) == 10:
                            ids["neq"][q] = ("exact", "NEQ %s published for this vendor in the contract data" % q)
                    elif kl == "ticker":
                        for t in val.split(","):
                            if t.strip():
                                ids["ticker"][t.strip().upper()] = ("exact", "ticker published for this vendor in the contract data")
                    elif kl in ("lei",) and re.fullmatch(r"[A-Z0-9]{18}\d\d", val):
                        ids["lei"][val] = ("exact", "LEI published for this vendor in the contract data")
            vendors.append({"vendor_key": v["vendor_key"], "name": v.get("name"), "sk": sk, "lk": lk, "postals": postals, "fsas": fsas,
                            "cities": cities, "provs": provs, "streets": streets, "ids": ids,
                            "rc": v.get("record_count") or 0, "rc_hm": v.get("record_count_high_or_medium") or 0,
                            "reg_postals": set(), "reg_cities": set(), "reg_provs": set()})
    with open(REG, encoding="utf-8") as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            v = vendors[i]
            assert d["vendor_key"] == v["vendor_key"]
            for m in d.get("registry_matches") or []:
                conf = m.get("match_confidence")
                if conf not in ("exact", "strong"):
                    continue
                basis = "%s match (%s: %s)" % (conf, m.get("registry"), (m.get("match_basis") or "")[:100])
                if m.get("registry") == "corporations_canada" and m.get("corporation_number"):
                    v["ids"]["cc"].setdefault(m["corporation_number"], (conf, "federal corporation number %s of the vendor's Corporations Canada %s" % (m["corporation_number"], basis)))
                    if m.get("business_number_bn9"):
                        v["ids"]["bn9"].setdefault(m["business_number_bn9"], (conf, "BN9 %s of the vendor's Corporations Canada %s" % (m["business_number_bn9"], basis)))
                    ro = m.get("registered_office") or {}
                    p = norm_postal(ro.get("postal_code"))
                    if p:
                        v["reg_postals"].add(p)
                    c = norm_city(ro.get("city"))
                    if c:
                        v["reg_cities"].add(c)
                    pr = norm_prov(ro.get("region"))
                    if pr:
                        v["reg_provs"].add(pr)
                elif m.get("registry") == "quebec_req" and m.get("neq"):
                    v["ids"]["neq"].setdefault(m["neq"], (conf, "NEQ %s of the vendor's Quebec REQ %s" % (m["neq"], basis)))
                    for ln in (m.get("domicile_address") or {}).get("lines") or []:
                        mm = re.search(r"[A-Z]\d[A-Z]\s?\d[A-Z]\d", ln.upper())
                        if mm:
                            v["reg_postals"].add(norm_postal(mm.group(0)))
                        m2 = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", ln.strip())
                        if m2:
                            c = norm_city(m2.group(1))
                            if c:
                                v["reg_cities"].add(c)
                            pr = norm_prov(m2.group(2))
                            if pr:
                                v["reg_provs"].add(pr)
    pos = {v["vendor_key"]: i for i, v in enumerate(vendors)}
    nob = 0
    for fn in sorted(glob.glob(V2 + "/vendors_orgbook.jsonl*")):
        with open(fn, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                i = pos.get(d.get("vendor_key"))
                if i is None:
                    continue
                for m in d.get("matches") or []:
                    if m.get("match_confidence") in ("exact", "strong") and m.get("registration_number"):
                        conf = m["match_confidence"]
                        vendors[i]["ids"]["bc"].setdefault(m["registration_number"], (conf, "BC registration %s of the vendor's BC OrgBook %s match (%s)" % (m["registration_number"], conf, (m.get("match_basis") or "")[:100])))
                        if m.get("business_number_bn9"):
                            vendors[i]["ids"]["bn9"].setdefault(m["business_number_bn9"], (conf, "BN9 %s of the vendor's BC OrgBook %s match" % (m["business_number_bn9"], conf)))
                        nob += 1
    meta = {"built_at": now_utc(), "orgbook_matches_used": nob, "vendors": len(vendors)}
    with open(path_pkl, "wb") as f:
        pickle.dump((vendors, meta), f, protocol=pickle.HIGHEST_PROTOCOL)
    return vendors, meta


def load_index(path_pkl=WORK + "/vendors_index.pkl"):
    if not os.path.exists(path_pkl):
        return build_index(path_pkl)
    with open(path_pkl, "rb") as f:
        return pickle.load(f)


def need_map(vendors):
    need = collections.defaultdict(set)
    for i, v in enumerate(vendors):
        for l in v["lk"]:
            need[l].add(i)
    return need


# ------------------------------------------------------------------ scoring / grading
def loc_eval(v, rec_postals, rec_cities, rec_provs, rec_streets=(), use_registry_addr=True):
    """compare a vendor's contract-data locations (and, secondarily, its registry addresses) with a source record's locations"""
    rec_postals = {p for p in rec_postals if p}
    rec_cities = {c for c in rec_cities if c}
    rec_provs = {p for p in rec_provs if p}
    st = bool(v["streets"] & set(rec_streets))
    pe = bool(v["postals"] & rec_postals)
    fsa = bool(v["fsas"] & {p[:3] for p in rec_postals}) and not pe
    city = bool(v["cities"] & rec_cities)
    pa = bool(v["provs"] & rec_provs)
    pc = bool(v["provs"]) and bool(rec_provs) and not pa
    rpe = rcity = False
    if use_registry_addr and not (pe or city):
        rpe = bool(v["reg_postals"] & rec_postals)
        rcity = bool(v["reg_cities"] & rec_cities) and not rpe
    basis = []
    if st:
        basis.append("same civic number and postal code")
    elif pe:
        basis.append("same postal code")
    if fsa:
        basis.append("same postal FSA")
    if city:
        basis.append("same city")
    if rpe:
        basis.append("same postal code as the vendor's registry (CC/REQ) address")
    if rcity:
        basis.append("same city as the vendor's registry (CC/REQ) address")
    if pa and not (pe or city or fsa):
        basis.append("same province")
    if pc and not (pe or rpe):
        basis.append("PROVINCE CONFLICT (vendor %s vs source %s)" % ("/".join(sorted(v["provs"])), "/".join(sorted(rec_provs))))
    if not (v["postals"] or v["cities"] or v["provs"]):
        basis.append("no vendor location in contract data")
    score = 4 * pe + 2 * st + 2 * fsa + 2 * city + 2 * rpe + 1 * rcity + pa - 3 * (pc and not (pe or rpe))
    locagree = pe or fsa or city or rpe or rcity
    return {"score": score, "locagree": locagree, "pc": pc and not (pe or rpe), "pe": pe or st, "city": city, "pa": pa, "basis": basis}


def grade(v, cands, local_dataset=False):
    """cands: list of dicts with keys ent (entity id), strict (bool), loc (loc_eval result), idmatch (None or (conf, basis)), lkey.
    Returns the candidates with 'match_confidence' and 'basis' set, best first (max 5).
    local_dataset=True (city/municipal data): a name-only match without location agreement is never better than weak."""
    if not cands:
        return []
    strict_c = {c["ent"] for c in cands if c["strict"]}
    strictloc_c = {c["ent"] for c in cands if c["strict"] and c["loc"]["locagree"] and not c["loc"]["pc"]}
    loc_c = {c["ent"] for c in cands if c["loc"]["locagree"] and not c["loc"]["pc"]}
    for c in cands:
        b = []
        if c.get("idmatch"):
            b.append(c["idmatch"][1])
        b.append("name equal after normalisation" if c["strict"] else ("name equal except legal-form suffix" if c.get("lkey_match", True) else "name differs"))
        b += c["loc"]["basis"]
        conf = "weak"
        if c.get("idmatch"):
            conf = c["idmatch"][0]
        elif c["strict"] and c["loc"]["locagree"] and not c["loc"]["pc"]:
            conf = "exact" if (len(strictloc_c) == 1 and (c["loc"]["pe"] or c["loc"]["city"])) else "strong"
            if len(strictloc_c) > 3:
                conf = "weak"
                b.append("%d source entities share name and location (chain/franchise or duplicates: ambiguous)" % len(strictloc_c))
            elif len(strictloc_c) > 1:
                b.append("%d source entities share name and location" % len(strictloc_c))
        elif c["loc"]["locagree"] and not c["loc"]["pc"] and len(loc_c) == 1:
            conf = "strong"
        elif c["strict"] and len(strict_c) == 1 and not c["loc"]["pc"] and not local_dataset:
            rp = c.get("rec_provs") or set()
            if v["provs"] and rp and not (rp & v["provs"]):
                conf = "weak"
            elif v["postals"] or v["cities"] or v["provs"]:
                conf = "strong"
                b.append("only source entity with this name")
            else:
                conf = "strong" if distinctive(c["lkey"]) else "weak"
                b.append("only source entity with this name; no vendor location to compare")
        if conf == "weak" and len(strict_c) > 1 and not c.get("idmatch"):
            b.append("%d source entities share this name" % len(strict_c))
        c["match_confidence"] = conf
        c["basis"] = "; ".join(dict.fromkeys(b))
        c["_score"] = (10 if c.get("idmatch") else 0) + (3 if c["strict"] else 1) + c["loc"]["score"]
    order = {"exact": 0, "strong": 1, "weak": 2}
    cands.sort(key=lambda c: (order[c["match_confidence"]], -c["_score"]))
    # one entry per entity
    seen, out = set(), []
    for c in cands:
        if c["ent"] in seen:
            continue
        seen.add(c["ent"])
        out.append(c)
    return out[:5]


def resolve_id_ambiguity(cand):
    """cand: {ent: {"idmatch": (conf, basis) or None, ...}}.  Identifier joins inherit the confidence of the vendor's upstream registry
    match; when they reach several source entities the non-exact ones are ambiguous: if an exact join exists, other (strong) joins are
    downgraded to weak; if only strong joins exist and they reach more than one entity, all of them become weak."""
    ex = [e for e, c in cand.items() if c.get("idmatch") and c["idmatch"][0] == "exact"]
    st = [e for e, c in cand.items() if c.get("idmatch") and c["idmatch"][0] == "strong"]
    if ex:
        for e in st:
            cand[e]["idmatch"] = ("weak", cand[e]["idmatch"][1] + "; ANOTHER source entity is joined through an identifier published for this vendor, so this join (via an upstream strong registry match) is ambiguous")
    elif len(st) > 1:
        for e in st:
            cand[e]["idmatch"] = ("weak", cand[e]["idmatch"][1] + "; the vendor's upstream registry matches lead to %d different source entities (ambiguous)" % len(st))
    return cand


class Out:
    """incremental writer for vendors_extra_<source>.jsonl"""

    def __init__(self, source):
        self.source = source
        self.path = V2 + "/vendors_extra_%s.jsonl" % source
        self.f = open(self.path + ".tmp", "w", encoding="utf-8")
        self.n = 0
        self.conf = collections.Counter()

    def write(self, v, matches):
        if not matches:
            return
        self.n += 1
        self.conf[matches[0]["match_confidence"]] += 1
        self.f.write(json.dumps({"vendor_key": v["vendor_key"], "name": v["name"], "source": self.source, "matches": matches}, ensure_ascii=False) + "\n")
        if self.n % 500 == 0:
            self.f.flush()

    def close(self):
        self.f.close()
        os.replace(self.path + ".tmp", self.path)
        return {"vendors_matched": self.n, "best_confidence": dict(self.conf)}

#!/usr/bin/env python3
"""Offline registry match of the ranked buyers and vendors against two bulk registries — fast, deterministic, no per-name requests:
  * Registraire des entreprises du Québec open data (Données Québec `registre-des-entreprises`, JeuDonnees.zip: Nom.csv, Entreprise.csv):
    NEQ, legal name, legal form, registration status, domicile address — for organisations located in Québec (public bodies included:
    "VILLE DE …", CISSS, centres de services scolaires, universities are all registered).
  * Corporations Canada federal corporations (open.canada.ca dataset 0032ce54-c5dd-4b66-99a0-320a7b5e99f2, four CSVs on cloudfront):
    corporation number, **Business Number**, status, governing legislation, registered office.
Match rule (the same strictness as tools/registry_lookup.py): the organisation's name, normalised (accents, punctuation, legal-form words),
equals a CURRENT legal name in the registry; one registered body → found; several → the city or postal code of the organisation's address
decides; otherwise `ambiguous`. A registry "other name" (trade name) counts only with city / postal-code agreement. Québec matching only
for organisations located in Québec (province from the row, the postal code, a .qc.ca site or a French public-body name).
Output: <repo>/data/incoming/claude/claude_registry_bulk.csv in the claude_registry_lookup.csv column format (+ reg_office_address),
read by rank.py after the Canada's Business Registries rows (those win when both exist). Every row carries the file's URL, the date and a
quote of the matched record (≤ 300 chars).
  python3 tools/bulk_registry_match.py --ranked coord/results/ranked/ranked_buyers.csv.gz --req JeuDonnees.zip --cc corporations-*.csv [--repo .]
"""
import argparse, collections, csv, datetime, glob, gzip, io, os, re, sys, unicodedata, zipfile

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry_lookup import COLS, LEGAL, norm, pcode, prov_of, form_class, GOV_RX  # noqa: E402
import registry_names as RN  # noqa: E402

TODAY = datetime.date.today().isoformat()
REQ_URL = "https://www.donneesquebec.ca/recherche/dataset/registre-des-entreprises"
CC_URL = "https://open.canada.ca/data/en/dataset/0032ce54-c5dd-4b66-99a0-320a7b5e99f2"
STAT_IMMAT = {"AI": "avis d'intention de constitution", "IM": "immatriculée", "NI": "non immatriculée", "RD": "radiée sur demande", "RO": "radiée d'office", "RX": "radiée d'office (article 59)"}
OUT_COLS = COLS + ["reg_office_address"]
FORME = {"CIE": "société par actions (compagnie)", "APE": "personne morale sans but lucratif / de droit public", "SENC": "société en nom collectif", "SEC": "société en commandite", "COP": "coopérative",
         "PP": "personne physique (entreprise individuelle)", "SOC": "société", "SEP": "société en participation", "FID": "fiducie", "SYN": "syndicat de copropriété"}
_PLACE = {"canada", "quebec", "ontario", "alberta", "manitoba", "saskatchewan", "british", "columbia", "colombie", "britannique", "nova", "scotia", "nouvelle", "ecosse", "new", "brunswick",
          "nouveau", "newfoundland", "labrador", "terre", "neuve", "yukon", "nunavut", "prince", "edward", "island", "montreal", "toronto", "vancouver", "ottawa", "calgary", "edmonton",
          "winnipeg", "halifax", "laval", "gatineau", "sherbrooke", "usa", "us", "united", "states", "america", "amerique", "nord", "north", "international", "global", "mondial", "world",
          "france", "europe", "uk", "kingdom", "est", "ouest", "sud", "east", "west", "south", "region", "division", "head", "office", "siege", "social"}


def PLACE_ONLY(s):
    """a bracketed part that names only a place or a scope ("Canada", "Québec", "North America", "International") — not a name"""
    toks = norm(s).split()
    return not toks or all(t in _PLACE for t in toks)


QC_WORDS = re.compile(r"\b(ville|municipalit[ée]|canton|paroisse|village|cisss|ciusss|centre de services scolaire|commission scolaire|c[ée]gep|universit[ée] du qu[ée]bec|soci[ée]t[ée] de transport|mrc|r[ée]gie|office municipal|soci[ée]t[ée] qu[ée]b[ée]coise|minist[èe]re|qu[ée]bec)\b", re.I)


def city_norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\((?:quebec|qc)\)|\bquebec\b|\bqc\b|\bcanada\b", " ", s)
    s = re.sub(r"\bst[e]?[- ]", lambda m: "sainte-" if m.group(0).startswith("ste") else "saint-", s)
    return " ".join(re.findall(r"[a-z][a-z-]+", s))


def pc_of(s):
    m = re.search(r"\b([A-Za-z]\d[A-Za-z])\s?(\d[A-Za-z]\d)\b", s or "")
    return (m.group(1) + m.group(2)).upper() if m else ""


def in_quebec(name, prov, website, address):
    if prov == "QC":
        return True
    if prov and prov != "QC":
        return False
    return bool(re.search(r"\.qc\.ca", website or "", re.I) or re.search(r"\b[GHJ]\d[A-Z]\s?\d[A-Z]\d\b", address or "") or QC_WORDS.search(name or ""))


def wanted_orgs(ranked):
    """(kind, key, name, prov, website, address) for every delivered buyer and vendor, once each"""
    out, seen = [], set()
    op = gzip.open if ranked.endswith(".gz") else open
    with op(ranked, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not r.get("email"):
                continue
            k = (r.get("keys") or "").split("|")[0]
            b = RN.lookup_name(r)[0]  # the legal person the buyer's own site states, when it does; else the name it trades under
            if k and b and ("buyer", k) not in seen:
                seen.add(("buyer", k))
                out.append(("buyer", k, b, prov_of(r.get("jurisdiction") or "", r.get("buyer_address") or ""), r.get("buyer_website") or "", r.get("buyer_address") or ""))
            v = (r.get("vendor") or "").strip()
            if v and not v.startswith("inferred") and ("vendor", v.lower()) not in seen:
                seen.add(("vendor", v.lower()))
                out.append(("vendor", v, v, prov_of(r.get("vendor_address") or "", r.get("vendor_registered_address") or "", r.get("vendor_country_basis") or ""), r.get("vendor_website") or "", (r.get("vendor_address") or "") + " " + (r.get("vendor_registered_address") or "")))
    return out


def match_req(orgs, zpath, done):
    z = zipfile.ZipFile(zpath)
    wanted = collections.defaultdict(list)  # normalised name -> orgs
    for o in orgs:
        if (o[0], o[1]) in done or not in_quebec(o[2], o[3], o[4], o[5]):
            continue
        n = norm(o[2])
        if len(n) >= 4:
            wanted[n].append(o)
        m = re.search(r"\(([^()]{3,80})\)", o[2])
        # the name in brackets is often the registered name ("Thermofin (3075109 Canada Inc)") — never when it is a place: Wikidata's batch items
        # are all labelled "X (Canada)", and 53 organisations were given the registry identity of a company named "CANADA INC." (2026-11-10)
        if m and len(norm(m.group(1))) >= 4 and not PLACE_ONLY(m.group(1)):
            wanted[norm(m.group(1))].append(o)
    print("REQ: %d names wanted" % len(wanted), flush=True)
    legal, other = collections.defaultdict(set), collections.defaultdict(set)  # normalised name -> NEQs
    name_of, legal_name_of = {}, {}  # first current name seen / the current dénomination sociale (TYP M or N) of each NEQ
    with z.open("Nom.csv") as fh:
        for r in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace", newline="")):
            if r.get("STAT_NOM") != "V":
                continue
            n = norm(r.get("NOM_ASSUJ") or "")
            typ = r.get("TYP_NOM_ASSUJ")
            if n not in wanted:
                n2 = norm(r.get("NOM_ASSUJ_LANG_ETRNG") or "")
                if n2 and n2 in wanted and typ in ("M", "N", "V"):
                    legal[n2].add(r["NEQ"]); name_of.setdefault(r["NEQ"], r.get("NOM_ASSUJ") or "")
                continue
            if typ in ("M", "N", "V"):
                legal[n].add(r["NEQ"]); name_of.setdefault(r["NEQ"], r.get("NOM_ASSUJ") or "")
            elif typ == "A":
                other[n].add(r["NEQ"]); name_of.setdefault(r["NEQ"], r.get("NOM_ASSUJ") or "")
    neqs = set().union(*legal.values()) | set().union(*other.values()) if (legal or other) else set()
    with z.open("Nom.csv") as fh:  # second pass: the current dénomination sociale of every hit NEQ (the hit may have been an other name or the English version)
        for r in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace", newline="")):
            if r["NEQ"] in neqs and r.get("STAT_NOM") == "V" and r.get("TYP_NOM_ASSUJ") in ("M", "N") and r["NEQ"] not in legal_name_of:
                legal_name_of[r["NEQ"]] = r.get("NOM_ASSUJ") or ""
    for q in neqs:
        if q in legal_name_of:
            name_of[q] = legal_name_of[q]
    print("REQ: %d legal-name hits, %d other-name hits, %d NEQs to read" % (len(legal), len(other), len(neqs)), flush=True)
    ent = {}
    with z.open("Entreprise.csv") as fh:
        for r in csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace", newline="")):
            if r["NEQ"] in neqs:
                ent[r["NEQ"]] = r
    # legal names of the NEQs we kept (name_of has the first current name seen; prefer the M/N one)
    rows = []
    for n, lst in wanted.items():
        cands = [(q, "legal") for q in legal.get(n, ())] + [(q, "other") for q in other.get(n, ())]
        cands = [(q, t) for q, t in cands if q in ent]
        for o in lst:
            kind, key, name, prov, website, address = o
            if (kind, key) in done:
                continue
            if not cands:
                continue
            ocity, opc = city_norm(address), pc_of(address)
            def agrees(q):
                e = ent[q]
                ecity, epc = city_norm(e.get("ADR_DOMCL_LIGN2_ADR") or ""), pc_of(" ".join(e.get(c) or "" for c in ("ADR_DOMCL_LIGN3_ADR", "ADR_DOMCL_LIGN4_ADR", "ADR_DOMCL_LIGN2_ADR")))
                return bool((opc and epc and opc == epc) or (ocity and ecity and (ocity in ecity or ecity in ocity)))
            fc = form_class(name)
            pool = [(q, t) for q, t in cands if t == "legal" and (not fc or not form_class(name_of.get(q, "")) or form_class(name_of.get(q, "")) == fc)]
            basis = "registered name equals the organisation's name (REQ open data)"
            if not pool:
                pool = [(q, t) for q, t in cands if t == "other" and agrees(q)]
                basis = "a current other name in the registry equals the organisation's name and the city / postal code agrees (REQ open data)"
            if not pool:
                rows.append(dict(kind=kind, key=key, name=name, status="ambiguous" if cands else "not_found", candidates="; ".join("%s %s" % (name_of.get(q, ""), q) for q, _ in cands[:5])[:400], registry_source="Registraire des entreprises du Québec (open data)", api_url=REQ_URL, retrieved_date=TODAY, match_basis="other name without city / postal agreement, or legal form differs"))
                done.add((kind, key)); continue
            active = [(q, t) for q, t in pool if ent[q].get("COD_STAT_IMMAT") in ("IM", "NI")]  # NI = public bodies listed without a registration duty
            if not active and kind == "buyer":
                rows.append(dict(kind=kind, key=key, name=name, status="not_found", candidates="; ".join("%s %s (%s)" % (name_of.get(q, ""), q, ent[q].get("COD_STAT_IMMAT")) for q, _ in pool[:5])[:400], registry_source="Registraire des entreprises du Québec (open data)", api_url=REQ_URL, retrieved_date=TODAY, match_basis="only a struck-off (radiée) registration carries this name"))
                done.add((kind, key)); continue
            pool2 = active or pool
            if len(pool2) > 1:
                ag = [(q, t) for q, t in pool2 if agrees(q)]
                if len(ag) == 1:
                    pool2 = ag; basis += "; city / postal code agrees"
                else:
                    rows.append(dict(kind=kind, key=key, name=name, status="ambiguous", candidates="; ".join("%s %s" % (name_of.get(q, ""), q) for q, _ in pool2[:5])[:400], registry_source="Registraire des entreprises du Québec (open data)", api_url=REQ_URL, retrieved_date=TODAY, match_basis="%d registered bodies carry this name; no city / postal code to decide" % len(pool2)))
                    done.add((kind, key)); continue
            q, t = pool2[0]
            e = ent[q]
            if prov == "QC" or agrees(q):
                basis += "; organisation located in Québec"
            addr = ", ".join(v for v in (e.get("ADR_DOMCL_LIGN1_ADR"), e.get("ADR_DOMCL_LIGN2_ADR"), e.get("ADR_DOMCL_LIGN3_ADR"), e.get("ADR_DOMCL_LIGN4_ADR")) if v)
            if (e.get("COD_FORME_JURI") or "") in ("PP",) or re.search(r"personne physique", e.get("COD_FORME_JURI") or "", re.I):
                addr = ""  # sole proprietorships: no street address (privacy, PIPELINE_KNOWLEDGE)
            st = STAT_IMMAT.get(e.get("COD_STAT_IMMAT") or "", e.get("COD_STAT_IMMAT") or "")
            notes = ""
            if (e.get("COD_STAT_IMMAT") or "").startswith("R"):
                notes = "radiée — no longer registered"
            elif e.get("COD_STAT_IMMAT") == "NI" and (e.get("COD_FORME_JURI") or "") == "APE":
                notes = "public body listed with an NEQ; registration itself is not required of it (status 'non immatriculée' is normal for municipalities, school service centres and health bodies)"
            lines = [e.get(c) or "" for c in ("ADR_DOMCL_LIGN2_ADR", "ADR_DOMCL_LIGN3_ADR")]
            city_line = next((l for l in lines if re.search(r"\(.*\)", l)), next((l for l in reversed(lines) if l and not re.fullmatch(r"[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d", l.strip())), ""))
            rows.append(dict(kind=kind, key=key, name=name, status="found", matched_name=name_of.get(q, ""), bn9="", juri_id="NEQ " + q, registry_source="Registraire des entreprises du Québec (open data)", entity_type=("%s (%s)" % (e.get("COD_FORME_JURI"), FORME[e["COD_FORME_JURI"]])) if e.get("COD_FORME_JURI") in FORME else (e.get("COD_FORME_JURI") or ""),
                             status_state=st, status_notes=notes, date_incorporated=(e.get("DAT_IMMAT") or "")[:10],
                             reg_office_city=re.sub(r"\s*\((?:QU[ÉE]BEC|QC)\)\s*", "", city_line, flags=re.I), reg_office_province="QC", reg_office_address=addr, alternate_names="", candidates="",
                             match_basis=basis, api_url=REQ_URL, ui_url="https://www.registreentreprises.gouv.qc.ca/RQAnonymeGR/GR/GR03/GR03A2_19A_PIU_RechEnt_PC/PageRechSimple.aspx", retrieved_date=TODAY,
                             source_quote=("Nom.csv: %s | Entreprise.csv NEQ %s: statut %s, forme %s, immatriculée %s, domicile %s" % (name_of.get(q, ""), q, e.get("COD_STAT_IMMAT"), e.get("COD_FORME_JURI"), (e.get("DAT_IMMAT") or "")[:10], addr))[:300]))
            done.add((kind, key))
    return rows


def match_cc(orgs, paths, done):
    wanted = collections.defaultdict(list)
    for o in orgs:
        if (o[0], o[1]) in done:
            continue
        n = norm(o[2])
        if len(n) >= 4:
            wanted[n].append(o)
    hits = collections.defaultdict(list)  # normalised name -> rows
    nrows = 0
    for p in paths:
        with open(p, encoding="utf-8-sig", errors="replace", newline="") as fh:
            for r in csv.DictReader(fh):
                nrows += 1
                for c in ("Corporate name - form 1", "Corporate name - form 2"):
                    n = norm(r.get(c) or "")
                    if n in wanted:
                        hits[n].append(r)
    print("Corporations Canada: %d rows read, %d names hit" % (nrows, len(hits)), flush=True)
    rows = []
    for n, lst in wanted.items():
        cands = hits.get(n) or []
        for o in lst:
            kind, key, name, prov, website, address = o
            if (kind, key) in done or not cands:
                continue
            fc = form_class(name)
            pool = [r for r in cands if not fc or not form_class(r.get("Corporate name - form 1") or "") or form_class(r.get("Corporate name - form 1") or "") == fc]
            if not pool:
                rows.append(dict(kind=kind, key=key, name=name, status="ambiguous", candidates="; ".join("%s [%s %s]" % (r.get("Corporate name - form 1"), r.get("Corporation number"), r.get("Province/territory")) for r in cands[:5])[:400], registry_source="Corporations Canada (open data)", api_url=CC_URL, retrieved_date=TODAY, match_basis="the federal corporation of this name has a different legal form"))
                done.add((kind, key)); continue
            active = [r for r in pool if (r.get("Status") or "").startswith("Active")]
            if not active and kind == "buyer":  # a dissolved or inactive federal corporation is not a reliable identity for a live buyer
                rows.append(dict(kind=kind, key=key, name=name, status="not_found", candidates="; ".join("%s [%s %s %s]" % (r.get("Corporate name - form 1"), r.get("Corporation number"), r.get("Status"), r.get("Province/territory")) for r in pool[:5])[:400], registry_source="Corporations Canada (open data)", api_url=CC_URL, retrieved_date=TODAY, match_basis="only an inactive / dissolved federal corporation carries this name"))
                done.add((kind, key)); continue
            active = active or pool
            if len(active) > 1:
                same = [r for r in active if prov and pcode(r.get("Province/territory") or "") == prov]
                if len(same) != 1:
                    rows.append(dict(kind=kind, key=key, name=name, status="ambiguous", candidates="; ".join("%s [%s %s]" % (r.get("Corporate name - form 1"), r.get("Corporation number"), r.get("Province/territory")) for r in active[:5])[:400], registry_source="Corporations Canada (open data)", api_url=CC_URL, retrieved_date=TODAY, match_basis="%d federal corporations carry this name" % len(active)))
                    done.add((kind, key)); continue
                active = same
            r = active[0]
            rp = pcode(r.get("Province/territory") or "")
            if prov and rp and rp != prov:
                rows.append(dict(kind=kind, key=key, name=name, status="not_found", candidates="%s [%s %s]" % (r.get("Corporate name - form 1"), r.get("Corporation number"), rp), registry_source="Corporations Canada (open data)", api_url=CC_URL, retrieved_date=TODAY, match_basis="the only federal corporation of this name has its registered office in %s; the organisation is in %s" % (rp, prov)))
                done.add((kind, key)); continue
            addr = ", ".join(v for v in (r.get("Street"), r.get("Street 2"), r.get("City/town"), r.get("Province/territory"), r.get("Postal code")) if v)
            basis = "registered corporate name equals the organisation's name (Corporations Canada open data)" + ("; registered-office province agrees" if prov and rp == prov else ("; no province known for the organisation, so not checked" if not prov else ""))
            rows.append(dict(kind=kind, key=key, name=name, status="found", matched_name=r.get("Corporate name - form 1") or "", bn9=re.sub(r"\D", "", r.get("Business number (BN)") or "")[:9], juri_id="corporation number " + (r.get("Corporation number") or ""),
                             registry_source="Corporations Canada (open data)", entity_type=r.get("Governing legislation") or "", status_state=r.get("Status") or "", status_notes=r.get("Status Detail") or "", date_incorporated=(r.get("Anniversary date") or "")[:10],
                             reg_office_city=r.get("City/town") or "", reg_office_province=rp, reg_office_address=addr, alternate_names=r.get("Corporate name - form 2") or "", candidates="", match_basis=basis, api_url=CC_URL,
                             ui_url="https://ised-isde.canada.ca/cc/lgcy/fdrlCrpDtls.html?corpId=%s" % (r.get("Corporation number") or ""), retrieved_date=TODAY,
                             source_quote=("%s; BN %s; %s; %s; %s" % (r.get("Corporate name - form 1"), r.get("Business number (BN)"), r.get("Status"), r.get("Governing legislation"), addr))[:300]))
            done.add((kind, key))
    return rows


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", required=True)
    a.add_argument("--req", default="", help="JeuDonnees.zip of the Registraire des entreprises du Québec")
    a.add_argument("--cc", nargs="*", default=[], help="Corporations Canada CSVs (corporations-*-en.csv)")
    a.add_argument("--repo", default=".")
    a.add_argument("--kinds", default="buyer,vendor")
    a = a.parse_args()
    orgs = [o for o in wanted_orgs(a.ranked) if o[0] in a.kinds.split(",")]
    print("organisations: %d (%d buyers, %d vendors)" % (len(orgs), sum(o[0] == "buyer" for o in orgs), sum(o[0] == "vendor" for o in orgs)), flush=True)
    done, rows = set(), []
    if a.req:
        rows += match_req(orgs, a.req, done)
        print("REQ:", collections.Counter(r["status"] for r in rows), flush=True)
    cc = [p for pat in a.cc for p in sorted(glob.glob(pat))]
    if cc:
        n0 = len(rows)
        rows += match_cc(orgs, cc, done)
        print("Corporations Canada:", collections.Counter(r["status"] for r in rows[n0:]), flush=True)
    out = os.path.join(a.repo, "data/incoming/claude/claude_registry_bulk.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore"); w.writeheader()
        for r in sorted(rows, key=lambda d: (d["kind"], d["key"])):
            w.writerow({c: r.get(c, "") or "" for c in OUT_COLS})
    print("wrote", out, len(rows), "rows;", "found:", sum(r["status"] == "found" for r in rows), flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build (or load) a compact matching index of the 119k vendors for the vendors_extra_<source> matchers.

Usage (build): python3 -I vendor_index.py <vendor_master_input.jsonl> <vendors_registry_v3.jsonl> <enrichment_v2_dir> <out.pkl>
Library:       from vendor_index import load_index, Matcher

Index content per vendor (list position = line number in vendor_master_input.jsonl):
  vendor_key, name, rc, rc_hm, sk (strict keys), lk (loose keys), postals, fsas, cities, provs,
  phones (10-digit, from contract-data contacts), domains (from contract-data e-mails/websites + verified vendor_web sites),
  ids: {"corp": {num: (conf, basis)}, "neq": {...}, "bn9": {...}, "bcreg": {...}}
Identifiers come from: NEQ published in the contract data (exact); Corporations Canada / REQ matches graded exact/strong in
vendors_registry_v3.jsonl (conf inherited); BC OrgBook matches graded strong (vendors_orgbook*.jsonl*); CRA charity BN9 of exact/strong
charity matches (vendors_extra_charities.jsonl).
"""
import sys, os, re, json, glob, pickle, collections

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enrichment_vendors"))
from normname import strict_key, loose_key, norm_prov, norm_city, norm_postal, strip_accents  # noqa: E402

SPLIT_RE = re.compile(r"\s+(?:o/a|o\.a\.|dba|d/b/a|d\.b\.a\.|operating as|doing business as|carrying on business as|c\.o\.b\.|cob|faisant affaire sous(?: le nom de)?|f\.a\.s\.|s/n|sous le nom de|aka|a\.k\.a\.|t/a|trading as)\s+", re.I)
PAREN_RE = re.compile(r"\([^)]*\)")
NUMBERED_RE = re.compile(r"^\d{4,}[\s-]?\d*\s+(QUEBEC|CANADA|ONTARIO|ALBERTA|BC|B C|NOVA SCOTIA|MANITOBA|SASKATCHEWAN|NEW BRUNSWICK)\b")
GENERIC = {"SERVICES", "SERVICE", "CONSULTING", "CONSTRUCTION", "SOLUTIONS", "TECHNOLOGIES", "TECHNOLOGY", "GROUP", "GROUPE", "ENTERPRISES",
           "ENTREPRISES", "HOLDINGS", "INDUSTRIES", "SYSTEMS", "INTERNATIONAL", "CANADA", "MANAGEMENT", "ASSOCIATES", "INC", "LTD", "CORP",
           "AND", "THE", "OF", "DE", "DU", "DES", "ET", "LA", "LE", "LES", "CO", "CIE", "LTEE", "ENR", "COMPANY", "SUPPLY", "SUPPLIES",
           "CONSULTANTS", "PARTNERS", "ASSOCIATION", "SOCIETY", "NORTH", "AMERICA", "GLOBAL", "NATIONAL", "CANADIAN", "INTERNATIONALE"}
FREE_MAIL = {"gmail.com", "hotmail.com", "hotmail.ca", "yahoo.com", "yahoo.ca", "outlook.com", "live.com", "live.ca", "msn.com", "icloud.com",
             "me.com", "aol.com", "videotron.ca", "bell.net", "sympatico.ca", "rogers.com", "shaw.ca", "telus.net", "cogeco.ca", "eastlink.ca",
             "globetrotter.net", "mail.com", "protonmail.com", "gmx.com", "sasktel.net", "mts.net", "nb.sympatico.ca", "bellnet.ca", "xplornet.com",
             "tbaytel.net", "personainternet.com", "outlook.fr", "hotmail.fr", "yahoo.fr", "videotron.qc.ca", "qc.aira.com", "derytele.com",
             "cgocable.ca", "ymail.com", "rocketmail.com", "googlemail.com", "canada.ca", "gc.ca", "gov.on.ca", "gouv.qc.ca"}


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
    return res[:20]


def name_keys(names):
    sk, lk = set(), set()
    for n in variants(names):
        s, l = strict_key(n), loose_key(n)
        if l and len(l) >= 3 and not l.isdigit():
            sk.add(s)
            lk.add(l)
    return sk, lk


def distinctive(lkey):
    if not lkey:
        return False
    toks = lkey.split()
    if NUMBERED_RE.match(lkey):
        return True
    non_generic = [t for t in toks if t not in GENERIC and len(t) > 2]
    return len(non_generic) >= 2 or (len(non_generic) == 1 and len(non_generic[0]) >= 6 and len(toks) >= 2)


def norm_phone(s):
    if not s:
        return None
    d = re.sub(r"\D", "", str(s))
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    if len(d) > 10:  # extension appended: take first 10 if plausible
        m = re.match(r"\D*1?\D*(\d{3})\D*(\d{3})\D*(\d{4})", str(s))
        d = "".join(m.groups()) if m else None
    if d and len(d) == 10 and d[0] in "23456789":
        return d
    return None


def fmt_phone(d):
    return "%s-%s-%s" % (d[:3], d[3:6], d[6:]) if d and len(d) == 10 else d


def domain_of(s):
    if not s:
        return None
    s = str(s).strip().lower()
    if "@" in s:
        s = s.split("@", 1)[1]
    s = re.sub(r"^[a-z]+://", "", s)
    s = s.split("/")[0].split("?")[0].split(":")[0].strip(".")
    if s.startswith("www."):
        s = s[4:]
    if not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", s or ""):
        return None
    return s


def reg_domain(d):
    """registrable-ish domain: last two labels (or three for *.qc.ca / *.on.ca style and co.uk)."""
    if not d:
        return None
    parts = d.split(".")
    if len(parts) >= 3 and (parts[-2] in ("qc", "on", "bc", "ab", "mb", "sk", "ns", "nb", "nl", "pe", "co", "com", "gc", "gouv", "gov") and len(parts[-1]) == 2):
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def build(vm, reg, v2dir, out):
    vendors = []
    with open(vm, encoding="utf-8") as f:
        for i, line in enumerate(f):
            v = json.loads(line)
            names = [v.get("name")] + (v.get("name_variants") or [])
            ids = v.get("identifiers") or {}
            for k in ("canadabuys_legal_name", "canadabuys_operating_name", "pd_vendor_name_latest"):
                for e in ids.get(k) or []:
                    if e.get("value"):
                        names.append(e["value"])
            sk, lk = name_keys(names)
            postals, fsas, cities, provs = set(), set(), set(), set()
            for a in v.get("addresses") or []:
                val = a.get("value") or {}
                if not isinstance(val, dict):
                    continue
                p = norm_postal(val.get("postal_code"))
                if p:
                    postals.add(p)
                    fsas.add(p[:3])
                c = norm_city(val.get("city"))
                if c:
                    cities.add(c)
                pr = norm_prov(val.get("region"))
                if pr:
                    provs.add(pr)
            phones, domains = set(), set()
            for c in v.get("contacts") or []:
                val = c.get("value") if isinstance(c, dict) else None
                if not isinstance(val, dict):
                    continue
                for k in ("phone", "telephone"):
                    p = norm_phone(val.get(k))
                    if p:
                        phones.add(p)
                for k in ("email", "website", "url", "web"):
                    d = domain_of(val.get(k))
                    if d and d not in FREE_MAIL and reg_domain(d) not in FREE_MAIL:
                        domains.add(reg_domain(d))
            idx = {"corp": {}, "neq": {}, "bn9": {}, "bcreg": {}}
            for k, lst in ids.items():
                if "neq" in k.lower():
                    for e in lst:
                        q = re.sub(r"\D", "", str(e.get("value")))
                        if len(q) == 10:
                            idx["neq"][q] = ("exact", "NEQ %s published for this vendor in the contract data" % q)
            vendors.append({"vendor_key": v["vendor_key"], "name": v.get("name"), "rc": v.get("record_count"), "rc_hm": v.get("record_count_high_or_medium"),
                            "sk": sk, "lk": lk, "postals": postals, "fsas": fsas, "cities": cities, "provs": provs,
                            "phones": phones, "domains": domains, "ids": idx})
    pos = {v["vendor_key"]: i for i, v in enumerate(vendors)}
    print("vendors", len(vendors), file=sys.stderr, flush=True)
    with open(reg, encoding="utf-8") as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            v = vendors[pos[d["vendor_key"]]]
            for m in d.get("registry_matches") or []:
                conf = m.get("match_confidence")
                if conf not in ("exact", "strong"):
                    continue
                basis = (m.get("match_basis") or "")[:160]
                if m.get("registry") == "corporations_canada" and m.get("corporation_number"):
                    v["ids"]["corp"].setdefault(m["corporation_number"], (conf, "Corporations Canada corporation %s = vendor's %s registry match (%s)" % (m["corporation_number"], conf, basis)))
                    if m.get("business_number_bn9"):
                        v["ids"]["bn9"].setdefault(m["business_number_bn9"], (conf, "BN9 %s of the vendor's %s Corporations Canada match %s" % (m["business_number_bn9"], conf, m["corporation_number"])))
                if m.get("registry") == "quebec_req" and m.get("neq"):
                    v["ids"]["neq"].setdefault(m["neq"], (conf, "NEQ %s of the vendor's %s Quebec REQ match (%s)" % (m["neq"], conf, basis)))
    print("registry loaded", file=sys.stderr, flush=True)
    for fn in [os.path.join(v2dir, "vendors_orgbook.jsonl")] + sorted(glob.glob(os.path.join(v2dir, "vendors_orgbook.jsonl.*"))):
        with open(fn, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("vendor_key") not in pos:
                    continue
                v = vendors[pos[d["vendor_key"]]]
                for m in d.get("matches") or []:
                    if m.get("match_confidence") in ("exact", "strong") and m.get("registration_number"):
                        v["ids"]["bcreg"].setdefault(m["registration_number"], (m["match_confidence"], "BC registration %s of the vendor's %s BC OrgBook match" % (m["registration_number"], m["match_confidence"])))
                        if m.get("business_number_bn9"):
                            v["ids"]["bn9"].setdefault(m["business_number_bn9"], (m["match_confidence"], "BN9 %s of the vendor's %s BC OrgBook match %s" % (m["business_number_bn9"], m["match_confidence"], m["registration_number"])))
    fn = os.path.join(v2dir, "vendors_extra_charities.jsonl")
    if os.path.exists(fn):
        with open(fn, encoding="utf-8") as f:
            for line in f:
                d = json.loads(line)
                if d.get("vendor_key") not in pos:
                    continue
                v = vendors[pos[d["vendor_key"]]]
                for m in d.get("matches") or []:
                    bn9 = (m.get("identifiers") or {}).get("business_number_bn9")
                    if m.get("match_confidence") in ("exact", "strong") and bn9:
                        v["ids"]["bn9"].setdefault(bn9, (m["match_confidence"], "BN9 %s of the vendor's %s CRA charity match" % (bn9, m["match_confidence"])))
    for fn in sorted(glob.glob(os.path.join(v2dir, "vendors_web.jsonl*"))):
        with open(fn, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("vendor_key") in pos and d.get("website") and ((d.get("website_verification") or {}).get("confidence") or "").startswith("verified"):
                    dm = reg_domain(domain_of(d["website"]))
                    if dm:
                        vendors[pos[d["vendor_key"]]]["domains"].add(dm)
    c = collections.Counter()
    for v in vendors:
        for k, dct in v["ids"].items():
            if dct:
                c[k] += 1
        c["phones"] += bool(v["phones"])
        c["domains"] += bool(v["domains"])
    print("id coverage", dict(c), file=sys.stderr, flush=True)
    with open(out, "wb") as f:
        pickle.dump(vendors, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_index(pkl):
    with open(pkl, "rb") as f:
        return pickle.load(f)


class Matcher:
    """Generic name(+location/phone/domain/identifier) matcher.

    scope: 'local' (city-level source: strong needs a location/phone/domain agreement) or 'national' (unique strict name with no
    province conflict can be strong, as in match_registries.py)."""

    def __init__(self, vendors, scope="national"):
        self.v = vendors
        self.scope = scope
        self.by_loose = collections.defaultdict(list)
        self.by_id = {"corp": collections.defaultdict(list), "neq": collections.defaultdict(list), "bn9": collections.defaultdict(list), "bcreg": collections.defaultdict(list)}
        self.by_phone = collections.defaultdict(list)
        self.by_domain = collections.defaultdict(list)
        for i, v in enumerate(vendors):
            for l in v["lk"]:
                self.by_loose[l].append(i)
            for k, dct in v["ids"].items():
                for val in dct:
                    self.by_id[k][val].append(i)
            for p in v["phones"]:
                self.by_phone[p].append(i)
            for d in v["domains"]:
                self.by_domain[d].append(i)

    def candidates_for(self, rec):
        """rec: {'lk': set, 'ids': {'corp': set, 'neq': set, 'bn9': set, 'bcreg': set}, 'phones': set, 'domains': set} -> vendor idx set"""
        out = set()
        for l in rec.get("lk") or ():
            out.update(self.by_loose.get(l, ()))
        for k, vals in (rec.get("ids") or {}).items():
            for val in vals:
                out.update(self.by_id[k].get(val, ()))
        return out

    @staticmethod
    def evidence(v, rec):
        """compare vendor v with a source record. rec keys: sk, lk, postals, cities, provs, phones, domains, ids"""
        e = {}
        idm = None
        for k, vals in (rec.get("ids") or {}).items():
            for val in vals:
                if val in v["ids"][k]:
                    conf, basis = v["ids"][k][val]
                    if idm is None or (idm[0] != "exact" and conf == "exact"):
                        idm = (conf, basis)
        e["idmatch"] = idm
        e["strict"] = bool(v["sk"] & (rec.get("sk") or set()))
        e["loose"] = bool(v["lk"] & (rec.get("lk") or set()))
        rp = rec.get("postals") or set()
        e["pe"] = bool(v["postals"] & rp)
        e["fsa"] = bool(v["fsas"] & {p[:3] for p in rp}) and not e["pe"]
        e["city"] = bool(v["cities"] & (rec.get("cities") or set()))
        e["phone"] = bool(v["phones"] & (rec.get("phones") or set()))
        e["domain"] = bool(v["domains"] & (rec.get("domains") or set()))
        rprov = rec.get("provs") or set()
        e["pa"] = bool(v["provs"] & rprov)
        e["pc"] = bool(v["provs"]) and bool(rprov) and not e["pa"]
        e["locagree"] = e["pe"] or e["city"] or e["phone"] or e["domain"]
        return e

    @staticmethod
    def basis_text(e, v):
        b = []
        if e["idmatch"]:
            b.append(e["idmatch"][1])
        if e["strict"]:
            b.append("name equal after normalisation")
        elif e["loose"]:
            b.append("name equal except legal-form suffix")
        if e["pe"]:
            b.append("same postal code")
        if e["fsa"]:
            b.append("same postal FSA")
        if e["city"]:
            b.append("same city")
        if e["phone"]:
            b.append("same phone number as in contract data")
        if e["domain"]:
            b.append("same web/e-mail domain as known for the vendor")
        if e["pa"] and not (e["pe"] or e["city"]):
            b.append("same province")
        if e["pc"]:
            b.append("PROVINCE CONFLICT (vendor %s)" % "/".join(sorted(v["provs"])))
        if not (v["postals"] or v["cities"] or v["provs"]):
            b.append("no vendor location in contract data")
        return b

    def grade(self, v, cands, max_keep=3):
        """cands: list of (rec_id, evidence dict, lkey_of_record). Returns list of (rec_id, conf, basis list) best first."""
        if not cands:
            return []
        strict_loc = [c for c in cands if c[1]["strict"] and c[1]["locagree"] and not c[1]["pc"]]
        loc = [c for c in cands if (c[1]["strict"] or c[1]["loose"]) and c[1]["locagree"] and not c[1]["pc"]]
        strict_all = [c for c in cands if c[1]["strict"] and not c[1]["pc"]]
        out = []
        for rid, e, lkey in cands:
            b = self.basis_text(e, v)
            if e["idmatch"]:
                conf = e["idmatch"][0]
            elif e["strict"] and e["locagree"] and not e["pc"]:
                conf = "exact" if len(strict_loc) == 1 else "strong"
                if len(strict_loc) > 1:
                    b.append("%d source records share this name and location" % len(strict_loc))
            elif e["loose"] and e["locagree"] and not e["pc"] and len(loc) == 1:
                conf = "strong"
            elif self.scope == "national" and e["strict"] and len(strict_all) == 1 and not e["pc"]:
                if v["provs"] and e["pa"]:
                    conf = "strong" if distinctive(lkey) else "weak"
                elif not (v["postals"] or v["cities"] or v["provs"]):
                    conf = "strong" if distinctive(lkey) else "weak"
                    if conf == "strong":
                        b.append("only source record with this distinctive name")
                else:
                    conf = "weak"
            else:
                conf = "weak"
                if len(strict_all) > 1:
                    b.append("%d source records share this name" % len(strict_all))
            score = (10 if e["idmatch"] else 0) + (3 if e["strict"] else 1) + 4 * e["pe"] + 2 * e["fsa"] + 2 * e["city"] + 3 * e["phone"] + 3 * e["domain"] + e["pa"] - 3 * e["pc"]
            out.append((rid, conf, b, score))
        order = {"exact": 0, "strong": 1, "weak": 2}
        out.sort(key=lambda t: (order[t[1]], -t[3]))
        return [(r, c, b) for r, c, b, s in out[:max_keep]]


def rec_keys(names, postals=(), cities=(), provs=(), phones=(), domains=(), ids=None):
    sk, lk = name_keys(names)
    return {"sk": sk, "lk": lk,
            "postals": {p for p in (norm_postal(x) for x in postals) if p},
            "cities": {c for c in (norm_city(x) for x in cities) if c},
            "provs": {p for p in (norm_prov(x) for x in provs) if p},
            "phones": {p for p in (norm_phone(x) for x in phones) if p},
            "domains": {d for d in (reg_domain(domain_of(x)) for x in domains) if d},
            "ids": ids or {}}


if __name__ == "__main__":
    build(*sys.argv[1:5])

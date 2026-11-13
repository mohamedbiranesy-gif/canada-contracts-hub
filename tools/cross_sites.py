#!/usr/bin/env python3
"""One legal person, two Canadian registers: a site the patent lane tied to an owner is that owner's site in the trademark lane too, and the reverse.

The Canadian patents register and the Canadian trademarks register name the same companies (3D Systems, Inc.; ADC Therapeutics SA …), each with
its address, and each lane looks for the owner's site by itself (tools/tm_register.py sites, tools/pt_register.py). When one lane has tied a site
to an owner by its own tests (the site's own pages state the owner's name with the register's postal code, or its full legal name with its legal
form), an owner of the other register with the SAME legal name (legal form included, compared without case, accents or punctuation), in the
SAME country and at the SAME postal code (U.S.: the ZIP code; where neither register gives a postal code: the same address) is the same legal
person, and the site is its site. Kept only when that name, country and postal code lead to one site, when the owner has no site of its own in
its lane yet, and when no other owner of its lane holds that site. Nothing is fetched.

  python3 tools/cross_sites.py        appends the ties to data/incoming/claude/tm/tm_sites_found.csv and data/incoming/claude/pt/pt_sites_found.csv
"""
import collections, csv, gzip, os, re, sys, time, unicodedata

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
LANES = {"tm": ("trademark", [os.path.join(INC, "tm/tm_owners_abroad.csv.gz"), os.path.join(INC, "tm/tm_owners_ca.csv.gz")], os.path.join(INC, "tm/tm_sites_found.csv")),
         "pt": ("patent", [os.path.join(INC, "pt/pt_owners_abroad.csv.gz"), os.path.join(INC, "pt/pt_owners_ca.csv.gz")], os.path.join(INC, "pt/pt_sites_found.csv"))}
TODAY = time.strftime("%Y-%m-%d")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def place_key(r):
    c = (r.get("country") or "CA").strip().upper()
    pc = re.sub(r"[^A-Z0-9]", "", (r.get("postal_code") or "").upper())
    if not pc and c == "US":
        m = re.search(r"\b(\d{5})(?:-\d{4})?\s*$", r.get("address") or "")
        pc = m.group(1) if m else ""
    if c == "US":
        pc = pc[:5]
    return c, (pc or ("addr:" + norm(r.get("address") or "")))


def owners(paths):
    out = {}
    for p in paths:
        if not os.path.exists(p):
            continue
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for r in csv.DictReader(f):
                n = norm(r.get("owner_name"))
                if n and len(n) >= 4:
                    c, pk = place_key(r)
                    out[r["owner_key"]] = (n, c, pk, r.get("owner_name") or "", r.get("postal_code") or "")
    return out


def read_found(path):
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd)


def main():
    own = {k: owners(v[1]) for k, v in LANES.items()}
    found = {}
    for k, v in LANES.items():
        found[k] = read_found(v[2])
    by_owner = {k: {r["owner_key"]: r for r in found[k][1] if r.get("owner_key")} for k in LANES}
    sites_held = {k: {r["site"] for r in found[k][1]} for k in LANES}
    for tgt, src in (("tm", "pt"), ("pt", "tm")):
        ix = collections.defaultdict(dict)
        for ok, r in by_owner[src].items():
            o = own[src].get(ok)
            if o:
                ix[o[:3]][r["site"]] = r
        cols, rows = found[tgt]
        add, used = [], set()
        for ok, o in own[tgt].items():
            if ok in by_owner[tgt]:
                continue
            hits = ix.get(o[:3]) or {}
            if len(hits) != 1:
                continue
            site, r = next(iter(hits.items()))
            if site in sites_held[tgt] or site in used:
                continue
            used.add(site)
            where = ("postal code %s" % o[4]) if o[4] else ("ZIP code %s" % o[2]) if o[1] == "US" and not o[2].startswith("addr:") else "the same address"
            tied = ("the same legal person on both Canadian registers (“%s”, %s, %s): the %s lane tied this site to it — %s"
                    % (o[3], o[1], where, LANES[src][0], r.get("tied_by") or ""))[:600]
            line = {c: "" for c in cols}
            line.update(site=site, owner_key=ok, owner_name=o[3], postal_code=o[4], tied_by=tied, site_facts_from=r.get("site_facts_from") or "",
                        site_states=r.get("site_states") or "", read=r.get("read") or TODAY)
            add.append(line)
        if add:
            with open(LANES[tgt][2], "a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=cols)
                for line in add:
                    w.writerow(line)
        print("cross-sites: %d %s owners tied to the site the %s lane tied to the same legal person" % (len(add), LANES[tgt][0], LANES[src][0]))


if __name__ == "__main__":
    sys.exit(main())

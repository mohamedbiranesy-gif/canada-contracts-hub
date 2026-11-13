#!/usr/bin/env python3
"""Companies abroad that a Canadian company owns, as the Legal Entity Identifier register states it (GLEIF golden copy, CC0; no AI).

Every legal entity with an LEI reports its direct and ultimate accounting-consolidating parent to the Global LEI Foundation's register (Level 2
"who owns whom", relationship records validated by the issuing organisation). A child abroad whose ultimate parent's legal address is in Canada
is a company a Canadian company owns: the register links them (the owner's test for a subsidiary, 2026-11-13 08:07 EST: "you need to be able to
find a subsidiary … as accurate as possible" — only when a register or the parent's own site states the tie). Owner's rule 18 (2026-11-13 09:46
EST) counts a U.S. power company owned by a Canadian company as a Canadian vendor; this list is where such companies are found by the register.

  pull  --work DIR    the latest golden copy: entity records (lei2, ~490 MB zipped) and relationship records (rr) -> DIR
  build --work DIR    -> data/incoming/claude/canadian_owned/subsidiaries_abroad.csv.gz: child LEI, legal name, other names, country, legal and
                      headquarters address, status; parent LEI, parent legal name, parent city and province; relationship (ultimate / direct),
                      its status and period; the register's own record URL for each side
"""
import argparse, collections, csv, gzip, io, json, os, re, sys, time, urllib.request, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "data/incoming/claude/canadian_owned/subsidiaries_abroad.csv.gz")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://goldencopy.gleif.org/api/v2/golden-copies/publishes/latest"
REC = "https://search.gleif.org/#/record/%s"
COLS = ["child_lei", "child_name", "child_other_names", "child_country", "child_legal_address", "child_hq_address", "child_status", "child_legal_form",
        "parent_lei", "parent_name", "parent_city", "parent_region", "relationship", "relationship_status", "period_start", "child_url", "parent_url", "read"]


def get(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as r, open(path + ".part", "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    os.replace(path + ".part", path)


def cmd_pull(a):
    os.makedirs(a.work, exist_ok=True)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(API, headers={"User-Agent": UA}), timeout=120).read())["data"]
    for kind in ("lei2", "rr"):
        url = d[kind]["full_file"]["csv"]["url"].replace("\\/", "/")
        path = os.path.join(a.work, "%s.csv.zip" % kind)
        t0 = time.time()
        get(url, path)
        print("%s: %s (%.0f MB, %.0f s)" % (kind, url, os.path.getsize(path) / 1e6, time.time() - t0), flush=True)
    json.dump({"publish_date": d.get("publish_date")}, open(os.path.join(a.work, "publish.json"), "w"))


def _rows(path):
    z = zipfile.ZipFile(path)
    name = [n for n in z.namelist() if n.endswith(".csv")][0]
    with z.open(name) as fh:
        yield from csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8", errors="replace", newline=""))


def _addr(r, pre):
    parts = [r.get("%s.FirstAddressLine" % pre), r.get("%s.AdditionalAddressLine.1" % pre), r.get("%s.City" % pre), r.get("%s.Region" % pre),
             r.get("%s.PostalCode" % pre), r.get("%s.Country" % pre)]
    return ", ".join(p for p in parts if p)


def cmd_build(a):
    pub = json.load(open(os.path.join(a.work, "publish.json"))).get("publish_date", "")
    # 1. relationships: child -> (parent, type) for the ACTIVE accounting-consolidation links
    rel = {}
    n = collections.Counter()
    for r in _rows(os.path.join(a.work, "rr.csv.zip")):
        t = r.get("Relationship.RelationshipType") or ""
        if t not in ("IS_ULTIMATELY_CONSOLIDATED_BY", "IS_DIRECTLY_CONSOLIDATED_BY"):
            continue
        if (r.get("Relationship.RelationshipStatus") or "") != "ACTIVE":
            n["relationship not active"] += 1
            continue
        c, p = r.get("Relationship.StartNode.NodeID"), r.get("Relationship.EndNode.NodeID")
        if not c or not p:
            continue
        kind = "ultimate" if t.startswith("IS_ULT") else "direct"
        start = next((r.get(k) for k in r if k and k.endswith("StartDate") and r.get(k)), "")
        if kind == "ultimate" or c not in rel:
            rel[c] = (p, kind, r.get("Relationship.RelationshipStatus") or "", start or "")
        n["relationships (%s)" % kind] += 1
    print("active consolidation links: %d children; %s" % (len(rel), dict(n)), flush=True)
    need = set(rel) | {v[0] for v in rel.values()}
    ent = {}
    for r in _rows(os.path.join(a.work, "lei2.csv.zip")):
        lei = r.get("LEI")
        if lei in need:
            ent[lei] = {"name": r.get("Entity.LegalName") or "", "other": "; ".join(v for k, v in r.items() if k and k.startswith("Entity.OtherEntityNames.OtherEntityName.") and k.endswith("1") and v)[:300],
                        "country": r.get("Entity.LegalAddress.Country") or "", "legal": _addr(r, "Entity.LegalAddress"), "hq": _addr(r, "Entity.HeadquartersAddress"),
                        "status": r.get("Entity.EntityStatus") or "", "form": r.get("Entity.LegalForm.EntityLegalFormCode") or "",
                        "city": r.get("Entity.LegalAddress.City") or "", "region": r.get("Entity.LegalAddress.Region") or ""}
    out, m = [], collections.Counter()
    for c, (p, kind, st, start) in rel.items():
        pe, ce = ent.get(p), ent.get(c)
        if not pe or not ce or pe["country"] != "CA" or ce["country"] == "CA":
            continue
        if ce["status"] != "ACTIVE":
            m["child not active"] += 1
            continue
        out.append([c, ce["name"], ce["other"], ce["country"], ce["legal"], ce["hq"], ce["status"], ce["form"], p, pe["name"], pe["city"], pe["region"], kind, st, start,
                    REC % c, REC % p, pub[:10]])
        m["child abroad of a parent in Canada (%s)" % ce["country"]] += 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with gzip.open(OUT, "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        for x in sorted(out, key=lambda x: (x[9], x[3], x[1])):
            w.writerow(x)
    top = collections.Counter(x[3] for x in out).most_common(12)
    print("companies abroad that a company in Canada consolidates: %d (by country %s) -> %s" % (len(out), top, OUT), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["pull", "build"])
    ap.add_argument("--work", default="/tmp/gleif")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build}[a.cmd](a)


if __name__ == "__main__":
    main()

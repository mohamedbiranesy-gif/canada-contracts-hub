#!/usr/bin/env python3
"""Where an organisation is, by the head office it declares to a business register: the organisations with a confirmed role mailbox that no pass on
their own pages, no places dataset and no telephone listing located (no AI).

An organisation declares its head office (domicile, registered office) to its business register; the Registraire des entreprises du Québec and
Corporations Canada publish theirs as open data (tools/bulk_registry_match.py reads the same two files for the rows of the table). For an
organisation still unlocated, its name as its own home page gives it is matched to the registers with the matcher's rules — the very same name
(accents, punctuation and legal forms aside) as ONE current registered body; several, or a struck-off one only: nothing — and, here, only when the
organisation's province is known and agrees: its own telephone number's area code (site_facts/phones.tsv), a .qc.ca site for Québec. A sole
proprietorship (a natural person) gives no address. The head office names the electricity distributor of its address (tools/by_location.py) and
the row says the address is the one declared to the register.

  targets                 -> out/locate_targets.csv (key, site, name, prov)
  match --req ZIP --cc G  -> data/incoming/claude/site_facts/facts_<stamp>g.gz (address_how "registry") + site_facts/registry_locate_done.tsv
"""
import argparse, collections, csv, glob, gzip, json, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
FACTS = os.path.join(INC, "site_facts")
DONE = os.path.join(FACTS, "registry_locate_done.tsv")
TARGETS = os.path.join(ROOT, "out", "locate_targets.csv")
TODAY = time.strftime("%Y-%m-%d")
AC = {"QC": "418 438 450 514 579 581 819 873 367 354 263 468", "ON": "226 249 289 343 365 416 437 519 548 613 647 683 705 742 753 807 905 382",
      "BC": "236 250 257 604 672 778", "AB": "368 403 587 780 825", "MB": "204 431 584", "SK": "306 474 639", "NS": "782 902", "NB": "428 506", "NL": "709 879"}
PROV_OF_AC = {a: p for p, L in AC.items() for a in L.split()}
# the matching rules' version, written on every done line: an organisation the registers did not locate is tried again when the rules change
# (v1 2026-11-13 12Z: very same name as ONE current body; v2 2026-11-13 14Z: and, in Québec, a current OTHER name declared by one body only)
RULES = "v2"


def cmd_targets(a):
    last = {}
    with open(os.path.join(FACTS, "addr_reread_done.tsv"), encoding="utf-8") as f:
        for l in f:
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2:
                last[q[0]] = q[1]
    unl = {k for k, s in last.items() if s in ("city_nothing", "legal_nothing", "nothing")}
    for p in (os.path.join(INC, "overture", "phone_places.csv"), os.path.join(INC, "fsq", "phone_places.csv")):
        if os.path.exists(p):
            unl -= {r["key"] for r in csv.DictReader(open(p, encoding="utf-8", newline=""))}
    done = {}
    if os.path.exists(DONE):
        for l in open(DONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2 and q[0]:
                done[q[0]] = (q[1], q[3] if len(q) >= 4 else "v1")  # the latest line of a key counts
    done = {k for k, (st, ver) in done.items() if st == "found" or ver == RULES}
    unl -= done
    ph = {}
    if os.path.exists(os.path.join(FACTS, "phones.tsv")):
        for l in open(os.path.join(FACTS, "phones.tsv"), encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2 and q[0] in unl:
                ph[q[0]] = q[1]
    name, site = {}, {}
    for p in sorted(glob.glob(os.path.join(FACTS, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                k = d.get("key")
                if k in unl:
                    if d.get("site_name") and k not in name:
                        name[k] = d["site_name"]
                    if d.get("site") and k not in site:
                        site[k] = d["site"]
    n = collections.Counter()
    os.makedirs(os.path.dirname(TARGETS), exist_ok=True)
    with open(TARGETS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "site", "name", "prov"])
        for k in sorted(unl):
            nm, st = name.get(k, ""), site.get(k, "")
            prov = PROV_OF_AC.get((ph.get(k) or "")[:3], "")
            if not prov and re.search(r"\.qc\.ca(?:/|$)", st or ""):
                prov = "QC"
            if not nm or not prov:
                n["no name of its own" if not nm else "no province known (no telephone number, not .qc.ca)"] += 1
                continue
            w.writerow([k, st, nm, prov])
            n["target (%s)" % prov] += 1
    print("registry-locate targets: %d unlocated; %s -> %s" % (len(unl), dict(n), TARGETS), flush=True)


def cmd_match(a):
    import bulk_registry_match as BRM
    import by_location as BL
    tg = list(csv.DictReader(open(a.targets, encoding="utf-8", newline="")))
    orgs = [("buyer", t["key"], t["name"], t["prov"], t["site"], "") for t in tg]
    done, rows = set(), []
    if a.req:
        rows += BRM.match_req([o for o in orgs if o[3] == "QC"], a.req, done, other_unique=True)
    cc = [p for pat in a.cc for p in sorted(glob.glob(pat))]
    if cc:
        rows += BRM.match_cc([o for o in orgs if o[3]], cc, done)
    site = {t["key"]: t["site"] for t in tg}
    prov_of = {t["key"]: t["prov"] for t in tg}
    n, out = collections.Counter(), []
    for r in rows:
        if r.get("status") != "found":
            n[r.get("status") or "?"] += 1
            continue
        addr = (r.get("reg_office_address") or "").strip()
        if not BL.fsa_of(addr):
            n["found, no address with a postal code (a sole proprietor's, or none)"] += 1
            continue
        if r.get("reg_office_province") and r["reg_office_province"] != prov_of.get(r["key"], r["reg_office_province"]):
            n["found, the head office is in another province"] += 1
            continue
        reg = "the Registraire des entreprises du Québec" if "Québec" in (r.get("registry_source") or "") else "Corporations Canada"
        out.append({"key": r["key"], "site": site.get(r["key"], ""), "date": TODAY, "address_country": "CA", "address": addr[:200],
                    "address_quote": ("%s, %s: %s" % (reg, r.get("juri_id") or "", r.get("source_quote") or ""))[:300],
                    "address_url": r.get("api_url") or "", "address_how": "registry",
                    "registry_name": r.get("matched_name") or "", "registry_id": r.get("juri_id") or ""})
        n["located (%s)" % reg] += 1
    os.makedirs(FACTS, exist_ok=True)
    if out:
        p = os.path.join(FACTS, "facts_%sg.gz" % a.stamp)
        with gzip.open(p, "wt", encoding="utf-8") as f:
            for o in out:
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
    with open(DONE, "a", encoding="utf-8") as f:
        got = {o["key"] for o in out}
        for t in tg:
            f.write("%s\t%s\t%s\t%s\n" % (t["key"], "found" if t["key"] in got else "registry_nothing", TODAY, RULES))
    print("registry-locate: %d targets, %d located by the head office declared to a register; %s" % (len(tg), len(out), dict(n)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["targets", "match"])
    ap.add_argument("--targets", default=TARGETS)
    ap.add_argument("--req", default="")
    ap.add_argument("--cc", nargs="*", default=[])
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    a = ap.parse_args()
    {"targets": cmd_targets, "match": cmd_match}[a.cmd](a)


if __name__ == "__main__":
    main()

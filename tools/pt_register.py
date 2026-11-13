#!/usr/bin/env python3
"""The Canadian patents register as a relationship source (2026-11-12): owners of Canadian patents and applications, and the Canadian patent
agent of record that acts for each one before the Canadian Intellectual Property Office.

The Office publishes its patent register as open data (researcher datasets, CSV; the extract of 2024-05-22 is the one published as CSV):
PT_main gives each patent or application its status, filing date and grant date; PT_interested_party names its parties — the current OWNER
(name, full address, country) and the AGENT of record, a Canadian patent agent firm. A patent in force (status GR) or an application still
alive (CO filed, ER examination requested, RP report to answer, AL allowed, PG grant pending, AA, PI) has an agent who prosecutes it, pays its
yearly maintenance fees and bills the owner for both. 386,885 such patents and applications in the extract; 67,430 organisations own one
with a Canadian agent of record — 28,150 in the United States, 8,879 in Canada, 3,621 in the United Kingdom, 3,600 in Germany … — and 49,831
of them are not trademark owners on the trademarks register under the same name (tools/tm_register.py has those).

The register gives names and addresses, never websites. The owner's own site is found and tied by exactly the tests of the trademarks lane
(tools/tm_register.py: the sites on file that print the owner's postal code under a name that agrees; for owners abroad, a domain name made of
the owner's own name, an Overture Maps listing or the name autocomplete — kept only when the site prints the register's postal code under the
same name, or states the owner's legal person with its legal form in the owner's state). The mailbox comes from that site, like every lead's.
Natural persons are left out (organisations only).

  build  [--work DIR]       download the two tables, keep live patents and applications -> data/incoming/claude/pt/pt_owners_ca.csv.gz,
                            pt_owners_abroad.csv.gz (the trademarks lane's owner columns; "marks" read "patents")
  match                     owners in Canada x the sites on file (tools/tm_register.py match, on these files) -> pt_matches.csv
  sites --shard K/N [...]   owners without a site (tools/tm_register.py sites, on these files; --abroad, --clearbit as there)
  merge-sites DIR           shard files -> pt_sites_found.csv, pt_sites_done.tsv.gz
  leads --stamp S           matches -> lead shards (tools/lead_store.py, engine pt)
"""
import argparse, collections, csv, gzip, hashlib, io, os, re, subprocess, sys, time, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_register as T  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "pt")
SNAP, SNAP_DATE = "Patent_CSV_2024_05_22", "2024-05-22"
BASE = "https://opic-cipo.ca/cipo/client_downloads/%s/" % SNAP
FILES = {"main": "PT_main.zip", "party": "PT_interested_party.zip"}
OFFICE = T.OFFICE
LIVE = {"GR": "granted, in force", "CO": "filed, examination not yet requested", "ER": "examination requested", "RP": "examiner's report to answer",
        "AL": "allowed", "PG": "grant pending", "AA": "pending", "PI": "pending"}
OWN_CA, OWN_XX = os.path.join(DIR, "pt_owners_ca.csv.gz"), os.path.join(DIR, "pt_owners_abroad.csv.gz")
MATCHES = os.path.join(DIR, "pt_matches.csv")
FOUND, SDONE = os.path.join(DIR, "pt_sites_found.csv"), os.path.join(DIR, "pt_sites_done.tsv.gz")
COLS = T.OWNER_COLS + ["titles", "agent_address_source"]
TM_AGENTS = os.path.join(INC, "tm", "tm_agents.csv")


def agent_addresses():
    """the patent register names the agent of record without its address; the trademarks register of the same Office prints each agent
    firm's address (tools/tm_register.py: tm_agents.csv). A patent agent is looked up there under its very name, else under the one firm
    whose name begins with the same first words ("ROBIC" -> "ROBIC AGENCE PI S.E.C./ ROBIC IP AGENCY LP"); the entry with the most marks wins."""
    by = collections.defaultdict(list)
    if os.path.exists(TM_AGENTS):
        for r in csv.DictReader(open(TM_AGENTS, encoding="utf-8", newline="")):
            if r.get("country") == "CA" and (r.get("address") or "").strip():
                by[T.nkey(r["agent_name"])].append(r)
                # an agent who is a person works in a firm the register prints in brackets at the head of the address: "(RIDOUT & MAYBEE LLP),
                # 250 University Avenue, 5th Floor, Toronto" — the firm, at that address
                m = re.match(r"\s*\(([^()]{3,90})\)\s*,?\s*(.+)$", r["address"])
                if m:
                    by[T.nkey(m.group(1))].append(dict(r, agent_name=m.group(1).strip(), address=m.group(2).strip()))
    best = {k: max(v, key=lambda r: int(r.get("marks") or 0)) for k, v in by.items()}
    keys = sorted(best)

    def look(name):
        k = T.nkey(name)
        if k in best:
            return best[k], "the same name"
        w = k.split()
        for n in (3, 2, 1):
            if len(w) < n or (n == 1 and len(w[0]) < 5):
                continue
            pre = " ".join(w[:n]) + " "
            hits = [x for x in keys if (x + " ").startswith(pre)]
            if len({best[x]["agent_name"] for x in hits}) == 1:
                return best[hits[0]], "the one agent firm whose name begins with “%s”" % " ".join(w[:n])
        # "BCF LLP" -> "BCF S.E.N.C.R.L./BCF LLP": every word of the patent register's name in one firm's name, and no other firm's
        hits = [x for x in keys if set(w) <= set(x.split()) and len(w) >= 2]
        if len({best[x]["agent_name"] for x in hits}) == 1:
            return best[hits[0]], "the one agent firm whose name holds every word of “%s”" % name
        return None, ""
    return look
UA = T.UA
TODAY = time.strftime("%Y-%m-%d")


def use_pt_files():
    """point the trademarks lane's functions at the patent owners' files (they read these module names at call time)"""
    T.DIR, T.OWN_CA, T.OWN_XX, T.MATCHES, T.FOUND, T.SDONE = DIR, OWN_CA, OWN_XX, MATCHES, FOUND, SDONE
    # 2026-11-13: the patent owners' own Overture candidates (under their name; at their address) — the trademark owners' file has other keys
    T.OVT_SITES, T.OVT_ADDR = os.path.join(DIR, "pt_overture_sites.csv"), os.path.join(DIR, "pt_overture_addr_sites.csv")
    T.OVT_ADDR_CA = os.path.join(DIR, "pt_overture_addr_ca_sites.csv")
    T.ROR_SITES = os.path.join(DIR, "pt_ror_sites.csv")  # 2026-11-13: tools/ror_sites.py
    os.makedirs(DIR, exist_ok=True)


def fetch(work):
    os.makedirs(work, exist_ok=True)
    ca = T.ca_file(work)
    out = {}
    for k, name in FILES.items():
        p = os.path.join(work, name)
        if not (os.path.exists(p) and os.path.getsize(p) > 50_000_000):
            subprocess.run(["curl", "-sS", "-L", "--fail", "--retry", "5", "--retry-delay", "10", "--cacert", ca, "-A", UA, "-o", p + ".part", BASE + name], check=True)
            os.replace(p + ".part", p)
            time.sleep(1)
        out[k] = p
    return out


def rows_of(zpath):
    with zipfile.ZipFile(zpath) as z:
        with z.open(z.namelist()[0]) as fh:
            f = io.TextIOWrapper(fh, encoding="utf-8", errors="replace", newline="")
            next(f)
            for line in f:
                yield line.rstrip("\r\n").split("|")


def clean(v):
    v = (v or "").strip()
    return "" if v in ("NULL", "-1", "N/A", "Unknown", "UNKNOWN") else re.sub(r"\s+", " ", v)


def one_line(q, cc):
    """the party's address in one line, as the trademarks lane's readers expect it ("767 Fifth Avenue, New York, NY 10153")"""
    lines = [clean(x) for x in q[8:13] if clean(x)]
    city, prov_code, prov, postal = clean(q[13]), clean(q[14]), clean(q[15]), clean(q[16])
    tail = " ".join(x for x in ((prov_code if cc in ("US", "AU") and len(prov_code) <= 3 else prov), postal) if x)
    return ", ".join(x for x in lines + [city, tail] if x)


def build(a):
    t0 = time.time()
    tabs = fetch(a.work)
    live = {}
    for q in rows_of(tabs["main"]):
        if len(q) < 8:
            continue
        st = q[3].strip()
        if st in LIVE:
            live[q[0].strip()] = (st, clean(q[1])[:10], clean(q[2])[:10], clean(q[5])[:90])
    print("patents and applications alive in the extract of %s: %d (granted %d) [%.0fs]" % (SNAP_DATE, len(live), sum(1 for v in live.values() if v[0] == "GR"), time.time() - t0), flush=True)
    owners, agent = collections.defaultdict(list), {}
    for q in rows_of(tabs["party"]):
        if len(q) < 19:
            continue
        pn = q[0].strip()
        if pn not in live:
            continue
        typ = q[3].strip()
        if typ == "OWNR" and clean(q[6]) == "":
            cc = clean(q[17]) or "??"
            owners[pn].append((clean(q[7]), one_line(q, cc), clean(q[15]), cc, clean(q[16])))
        elif typ == "AGNT" and clean(q[7]) and clean(q[7]) != "NA":
            cc = clean(q[17])
            agent[pn] = (clean(q[7]), one_line(q, cc), cc, T.pc6(clean(q[16])))
    print("live patents with a current owner: %d; with an agent of record: %d [%.0fs]" % (len(owners), len(agent), time.time() - t0), flush=True)
    groups = {}
    for pn, lst in owners.items():
        st, filed, granted, title = live[pn]
        ag = agent.get(pn)
        for name, addr, prov, cc, postal in lst:
            if len(T.nkey(name)) < 2:
                continue
            key = "%s|%s" % (T.nkey(name), T.pc6(postal) if cc == "CA" else cc)
            g = groups.setdefault(key, {"names": collections.Counter(), "addr": (name, addr, prov, cc, postal), "G": 0, "P": 0, "first": "", "agents": collections.Counter(),
                                        "ag": {}, "ex": [], "titles": []})
            g["names"][name] += 1
            if st == "GR":
                g["G"] += 1
                if granted:
                    g["first"] = min(g["first"] or granted, granted)
            else:
                g["P"] += 1
            if len(g["ex"]) < 3:
                g["ex"].append("%s;%s;;%s;" % (pn, granted if st == "GR" else "", filed))  # the third field stays empty: a title is not a name to look a domain up by
            if len(g["titles"]) < 3 and title:
                g["titles"].append("%s: %s (%s)" % (pn, title, LIVE[st]))
            if ag and ag[2] == "CA":
                g["agents"][ag[0]] += 1
                g["ag"][ag[0]] = ag
    os.makedirs(DIR, exist_ok=True)
    n_ca = n_xx = n_ag = n_addr = 0
    look, memo = agent_addresses(), {}
    with gzip.open(OWN_CA, "wt", encoding="utf-8", newline="") as fc, gzip.open(OWN_XX, "wt", encoding="utf-8", newline="") as fx:
        wc, wx = csv.DictWriter(fc, fieldnames=COLS), csv.DictWriter(fx, fieldnames=COLS)
        wc.writeheader(); wx.writeheader()
        for key in sorted(groups):
            g = groups[key]
            name, addr, prov, cc, postal = g["addr"]
            name = g["names"].most_common(1)[0][0]
            an, n_with = (g["agents"].most_common(1) or [("", 0)])[0]
            ag = g["ag"].get(an) or ("", "", "", "")
            if an and not ag[1]:
                if an not in memo:
                    memo[an] = look(an)
                hit, how = memo[an]
                if hit:
                    ag = (an, "%s, %s %s" % (hit["address"].strip(" ,"), hit.get("province") or "", hit.get("postal_code") or ""), "CA", T.pc6(hit.get("postal_code")))
                    src = "the Canadian trademarks register's entry for this agent firm (%s, %s; %s)" % (hit["agent_name"], T.BASE + T.FILES["party"], how)
                else:
                    src = ""
            else:
                src = "the patent register's own entry" if ag[1] else ""
            n_addr += bool(src)
            row = {"owner_key": "pt:" + hashlib.sha1(key.encode()).hexdigest()[:14], "owner_name": name, "address": addr, "province": prov, "country": cc,
                   "postal_code": T.pc6(postal) if cc == "CA" else postal, "marks_in_force": g["G"], "marks_pending": g["P"], "first_registered": g["first"],
                   "latest_renewal_due": "", "agent_name": an, "agent_number": "", "agent_address": ag[1], "agent_postal_code": ag[3], "marks_with_this_agent": n_with,
                   "examples": " | ".join(g["ex"]), "titles": " | ".join(g["titles"]), "agent_address_source": src}
            (wc if cc == "CA" else wx).writerow(row)
            n_ca += cc == "CA"
            n_xx += cc != "CA"
            n_ag += bool(an)
    print("owners: %d in Canada, %d abroad; with a Canadian agent of record: %d (its address found: %d) [%.0fs]" % (n_ca, n_xx, n_ag, n_addr, time.time() - t0), flush=True)


def T_no_mail(t):
    import hc_registers as HR
    return HR.no_mail(t or "")


def leads(a):
    import lead_store as LS
    owners = {}
    want = {m["owner_key"] for m in csv.DictReader(open(MATCHES, encoding="utf-8", newline=""))} if os.path.exists(MATCHES) else set()
    for path in (OWN_CA, OWN_XX):
        with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r["owner_key"] in want:
                    owners[r["owner_key"]] = r
    prev, pdet = LS.load(exclude=("pt", a.stamp))
    snap = LS.snapshot(prev, pdet)
    mine = {k for k, d in pdet.items() if d.get("platform") == "pt_register"}
    kept = set()
    agsite = T.agent_site_table()
    page = BASE + FILES["party"]
    for m in (csv.DictReader(open(MATCHES, encoding="utf-8", newline="")) if os.path.exists(MATCHES) else ()):
        o = owners.get(m["owner_key"])
        if not o or not o["agent_name"] or not int(o["marks_with_this_agent"] or 0) or not o["agent_address"]:
            continue  # the relationship is the agent's: no Canadian agent of record, or an agent whose printed address was not found, makes no row here
        dom = m["site"]
        key = "lead:" + hashlib.sha1(("%s|pt" % dom).encode()).hexdigest()[:16]
        ex = [x.split(";") for x in (o["examples"] or "").split(" | ") if x.count(";") == 4]
        ref = ex[0] if ex else ["", "", "", "", ""]
        pc_ = o["agent_postal_code"]
        vaddr = "%s%s" % (o["agent_address"], "" if (pc_ and pc_[:3] in (o["agent_address"] or "").replace(" ", "")) or not pc_ else ", " + pc_[:3] + " " + pc_[3:])
        vaddr = vaddr if re.search(r"canada", vaddr, re.I) else vaddr + ", Canada"
        g, p = int(o["marks_in_force"] or 0), int(o["marks_pending"] or 0)
        rel = "client of the Canadian patent agent of record (%s)" % OFFICE["name"]
        m = dict(m, tied_by=T_no_mail(m.get("tied_by")), site_states=T_no_mail(m.get("site_states")), site_facts_from=T_no_mail(m.get("site_facts_from")))
        own_addr = o["address"] if not o["postal_code"] or o["postal_code"].replace(" ", "") in o["address"].replace(" ", "") else "%s %s" % (o["address"], o["postal_code"])
        quote = "patent %s | owner %s, %s | agent of record %s, %s" % (ref[0], o["owner_name"], o["address"][:80], o["agent_name"], o["agent_address"][:70])
        prev[key] = {"buyer_key": key, "buyer_name": o["owner_name"], "website": "https://%s/" % dom, "canadian_vendor_rows": 1, "example_vendor": o["agent_name"],
                     "canada_field_value": "membership / statutory fee relationship: %s=%s (%s); register: “%s” (the patent register, extract of %s, %s)" % (
                         rel, vaddr, o.get("agent_address_source") or "the register's own entry", quote[:240], SNAP_DATE, page),
                     "evidence_dataset": page, "latest_record_date": SNAP_DATE}
        pdet[key] = {"key": key, "platform": "pt_register", "record_url": page, "vendor": o["agent_name"], "record_date": SNAP_DATE, "start": o["first_registered"], "end": "",
                     "reference": "patent %s" % ref[0] if ref[0] else "",
                     "title": "Canadian patent%s %s — %d in force, %d applications pending, %d with this agent of record (extract of %s)" % (
                         "" if g + p == 1 else "s", ref[0], g, p, int(o["marks_with_this_agent"] or 0), SNAP_DATE),
                     "vendor_address": "%s (%s)" % (vaddr, o.get("agent_address_source") or page),
                     "vendor_site": agsite.get(T.nkey(o["agent_name"]), ("", ""))[0], "vendor_site_basis": agsite.get(T.nkey(o["agent_name"]), ("", ""))[1],
                     "member_address_quote": own_addr,
                     "register_label": "the Canadian patents register of the Canadian Intellectual Property Office, which names as agent of record",
                     "pt_agent_of_record": o["agent_name"], "pt_agent_address": o["agent_address"], "pt_in_force": g, "pt_pending": p,
                     "pt_with_this_agent": int(o["marks_with_this_agent"] or 0), "pt_examples": o["titles"], "pt_first_granted": o["first_registered"], "pt_extract": SNAP_DATE,
                     "buyer_register": {"legal_name": o["owner_name"], "trade_names": [], "registry_id": "", "legal_form": "", "phone": "",
                                        "address": own_addr,
                                        "label": "the Canadian patents register (owner of record), extract of %s, %s" % (SNAP_DATE, page)},
                     "dataset_basis": "Canadian Intellectual Property Office, patent researcher datasets (CSV extract of %s): PT_main (status: %s) and PT_interested_party (party types OWNR, AGNT)" % (
                         SNAP_DATE, ", ".join("%s %s" % kv for kv in LIVE.items())),
                     "site_tied_to_holder_by": m["tied_by"], "site_page": "https://%s/" % dom, "site_quote": m["site_states"], "site_facts_from": m["site_facts_from"]}
        kept.add(key)
    gone = 0
    for k in mine - kept:
        prev.pop(k, None); pdet.pop(k, None); gone += 1
    nu, nd, ng = LS.save("pt", a.stamp, prev, pdet, snap)
    print("patent leads: %d sites tied to an owner with a Canadian agent of record; withdrawn %d; shards: %d rows, %d details, %d gone" % (len(kept), gone, nu, nd, ng))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "match", "sites", "merge-sites", "leads", "overture-sites"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--work", default=os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "pt_work"))
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    ap.add_argument("--abroad", action="store_true")
    ap.add_argument("--overture", action="store_true")
    ap.add_argument("--clearbit", action="store_true")
    ap.add_argument("--release", default="")
    ap.add_argument("--legal", action="store_true")
    ap.add_argument("--ror", action="store_true")
    a = ap.parse_args()
    use_pt_files()
    if a.cmd == "build":
        build(a)
    elif a.cmd == "match":
        T.match(a)
    elif a.cmd == "sites":
        T.sites(a)
    elif a.cmd == "merge-sites":
        T.merge_sites(a)
    elif a.cmd == "leads":
        leads(a)
    elif a.cmd == "overture-sites":
        T.overture_sites(a)  # -> pt_overture_sites.csv


if __name__ == "__main__":
    main()

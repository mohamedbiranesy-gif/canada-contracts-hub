#!/usr/bin/env python3
"""The Canadian trademarks register as a relationship source (2026-11-10).

Owner 2026-11-09: "some Canadian entity receives money for a service they provided, and that relationship is established online". The
Canadian Intellectual Property Office publishes its whole register as open data (researcher datasets, CSV): every application and
registration with its CURRENT OWNER (legal name, full address) and, when the owner appointed one, its AGENT OF RECORD — a Canadian trademark
agent firm, with the firm's address. Extract of 2025-01-28 (the latest CSV extract the Office has published; the weekly XML is newer):
837,000 marks in force or pending, 258,000 distinct owners, 182,000 of them represented by one of 888 Canadian agent firms.

Two paid relationships, both named by the register itself:
  owner -> its agent of record   a Canadian firm acts for the owner before the Office (professional fees; for an owner abroad they are often
                                 billed through the owner's own counsel — said on the row)
  owner -> the Office            official fees to register and to renew every ten years (the registration is in force until its renewal date)
The register gives names and addresses, not websites. A lead is made only for an owner whose OWN SITE is on file and is tied to the owner by
its postal code and its name (the name the site states for itself: schema.org legalName, the copyright line, the site name). The mailbox
comes from that site, like every other lead's. Nothing is inferred from a mark or from a name alone.

  build  [--work DIR]     download the two tables (application main, interested parties), keep marks in force or pending
                          -> data/incoming/claude/tm/tm_owners_ca.csv.gz, tm_owners_abroad.csv.gz, tm_agents.csv
  match                   owners in Canada x the sites on file (scan detector 5 name facts, the lead readers' site facts, the ranked table)
                          -> data/incoming/claude/tm/tm_matches.csv
  leads --stamp S         matches -> lead shards (tools/lead_store.py, engine tm)
The Office's server sends its certificate without the intermediate that signed it; tools/certs/ holds that intermediate (public, from the
address the certificate itself names) and the download verifies the chain with it. TLS verification is never switched off.
"""
import argparse, collections, csv, glob, gzip, hashlib, io, json, os, re, subprocess, sys, time, unicodedata, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "tm")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
SNAP, SNAP_DATE = "TM_CSV_2025_01_28", "2025-01-28"
BASE = "https://opic-cipo.ca/cipo/client_downloads/%s/" % SNAP
FILES = {"main": "TM_application_main_%s.zip" % SNAP_DATE, "party": "TM_interested_party_%s.zip" % SNAP_DATE}
PAGE = ("https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/canadian-intellectual-property-statistics/"
        "trademarks-researcher-datasets-applications-and-registrations-csv-and-txt")
DICT = "https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/trademarks-researcher-datasets-data-dictionary"
OFFICE = {"name": "Canadian Intellectual Property Office", "address": "Place du Portage I, 50 Victoria Street, Gatineau, Quebec K1A 0C9", "site": "https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en"}
TODAY = time.strftime("%Y-%m-%d")
OWN_CA, OWN_XX, AGENTS, MATCHES = (os.path.join(DIR, x) for x in ("tm_owners_ca.csv.gz", "tm_owners_abroad.csv.gz", "tm_agents.csv", "tm_matches.csv"))
OWNER_COLS = ["owner_key", "owner_name", "address", "province", "country", "postal_code", "marks_in_force", "marks_pending", "first_registered", "latest_renewal_due",
              "agent_name", "agent_number", "agent_address", "agent_postal_code", "marks_with_this_agent", "examples"]
# CIPO status codes (data dictionary): 12 registered; pending / in process: 1 pre-formalized, 2 formalized, 7 approved, 8 accepted for publication, 9 advertised, 10 opposed, 11 allowed, 40 registration pending
PENDING = {"1", "2", "7", "8", "9", "10", "11", "40"}
FORM = re.compile(r"\b(inc|incorporated|incorporee|ltd|ltee|limited|limitee|corp|corporation|co|company|compagnie|cie|llc|llp|lp|sencrl|senc|srl|enr|reg|regd|ulc|plc|gmbh|sa|sas|ag|bv|nv|pty|the|la|le|les|l)\b")
GENERIC = set("canada canadian canadien canadienne quebec ontario alberta manitoba saskatchewan british columbia nova scotia new brunswick toronto montreal vancouver calgary ottawa edmonton winnipeg "
              "group groupe holdings holding enterprises entreprises international services service solutions systems products produits industries associates associes management gestion "
              "and et of de du des for pour north american national global consulting consultants construction".split())


# an owner is taken as an organisation only when its name carries a legal form or an organisation word (the same test as tools/biz_licences.py):
# natural persons who hold a mark are left out, as on every register this project reads
ORG_FORM = re.compile(r"\b(inc|incorporated|incorporee|ltd|limited|ltee|limitee|corp|corporation|co|company|compagnie|cie|ulc|llp|llc|lp|plc|gmbh|senc|sencrl|s e n c|societe|society|association|assn|"
                      r"foundation|fondation|club|church|eglise|trust|fiducie|cooperative|coop|co-op|partnership|holdings|group|groupe|enterprises|entreprises|services|canada|ontario|quebec|"
                      r"university|universite|college|school|ecole|hospital|hopital|centre|center|institute|institut|council|conseil|board|bank|banque|authority|agency|agence|ville|city|town|"
                      r"municipality|municipalite|\d{4} \d{4} quebec|\d{6,} (?:ontario|canada|alberta|b c|manitoba|nova scotia|saskatchewan))\b")


def is_org(name):
    k = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    return bool(ORG_FORM.search(re.sub(r"[^a-z0-9 -]+", " ", k)))


OTHER_BODY = set("fondation foundation amis friends association syndicat union club alumni auxiliary auxiliaire society societe employees employes students etudiants parents retraites retirees fund fonds trust fiducie".split())


def nkey(s):
    """a name without accents, punctuation and legal-form words: 'Acme Plumbing & Heating Ltd.' -> 'acme plumbing and heating'"""
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", FORM.sub(" ", s)).strip()


_FORMS = (("inc", r"inc|incorporated|incorporee"), ("ltd", r"ltd|limited|ltee|limitee"), ("corp", r"corp|corporation"), ("llp", r"llp|s e n c r l|sencrl"), ("ulc", r"ulc"),
          ("coop", r"cooperative|coop|co-op"), ("llc", r"llc"), ("lp", r"lp|s e c|sec"), ("foreign", r"pty|gmbh|plc|sas|sarl|bv|nv|ag|oy|ab|kk|srl|spa|aps|as|sa"))


def forms(name):
    """the legal forms a name carries, by kind: 'Dresden Optics Pty Ltd' -> {foreign, ltd}; 'Hewitt's Dairy Limited' -> {ltd}"""
    k = " " + re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()) + " "
    return frozenset(f for f, rx in _FORMS if re.search(r" (?:%s) " % rx, k))


def pc6(s):
    p = re.sub(r"[^A-Z0-9]", "", (s or "").upper())
    return p if re.fullmatch(r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\d[ABCEGHJ-NPRSTV-Z]\d", p) else ""


# ------------------------------------------------------------------------------------------------------------------- build
def ca_file(work):
    """the default CA bundle plus the intermediate the Office's server leaves out (tools/certs/RapidSSLTLSRSACAG1.pem, issued by DigiCert Global Root G2)"""
    import ssl
    base = os.environ.get("SSL_CERT_FILE") or os.environ.get("CURL_CA_BUNDLE") or ssl.get_default_verify_paths().cafile or "/etc/ssl/certs/ca-certificates.crt"
    out = os.path.join(work, "ca_plus.pem")
    with open(out, "wb") as f:
        f.write(open(base, "rb").read() + b"\n" + open(os.path.join(ROOT, "tools/certs/RapidSSLTLSRSACAG1.pem"), "rb").read())
    return out


def fetch_tables(work):
    os.makedirs(work, exist_ok=True)
    ca = ca_file(work)
    out = {}
    for k, name in FILES.items():
        p = os.path.join(work, name)
        if not (os.path.exists(p) and os.path.getsize(p) > 10_000_000):
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


def build(a):
    t0 = time.time()
    tabs = {"main": a.main, "party": a.party} if a.main and a.party else fetch_tables(a.work)
    active = {}
    for q in rows_of(tabs["main"]):
        if len(q) < 54 or q[0] in active:
            continue
        cat, cs, term, exp = q[20].strip(), q[53].strip().lstrip("0"), q[14].strip(), q[13].strip()
        if cat == "Mark":
            continue  # official and prohibited marks (section 9): published once, never renewed — no fee relationship in force
        if cs == "12" and not term and exp >= TODAY:
            active[q[0]] = ("R", q[3].strip(), exp, q[8].strip(), re.sub(r"\s+", " ", q[26]).strip()[:60])
        elif cs in PENDING and not term and not q[52].strip():
            active[q[0]] = ("P", q[1].strip(), "", "", re.sub(r"\s+", " ", q[26]).strip()[:60])
    print("marks in force or pending on %s: %d (registered and not past their renewal date today: %d) [%.0fs]" % (
        SNAP_DATE, len(active), sum(1 for v in active.values() if v[0] == "R"), time.time() - t0), flush=True)
    owner, applicant, agent = {}, {}, {}
    for q in rows_of(tabs["party"]):
        if len(q) < 22 or q[0] not in active:
            continue
        rec = (re.sub(r"\s+", " ", q[3]).strip(), ", ".join(x.strip() for x in q[4:9] if x.strip()), q[9].strip(), q[10].strip(), q[11].strip(), q[21].strip())
        if q[1] == "10":
            owner[q[0]] = rec
        elif q[1] == "1":
            applicant[q[0]] = rec
        elif q[1] == "11":
            agent[q[0]] = rec
    print("with a current owner: %d; with an applicant only: %d; with an agent of record: %d [%.0fs]" % (len(owner), len(set(applicant) - set(owner)), len(agent), time.time() - t0), flush=True)
    groups = {}
    for app, st in active.items():
        o = owner.get(app) or applicant.get(app)
        if not o or len(nkey(o[0])) < 2:
            continue
        cc = o[3] or "??"
        key = "%s|%s" % (nkey(o[0]), pc6(o[4]) if cc == "CA" else cc)
        g = groups.setdefault(key, {"names": collections.Counter(), "addr": o, "R": 0, "P": 0, "first": "", "last": "", "agents": collections.Counter(), "ag": {}, "ex": []})
        g["names"][o[0]] += 1
        g[st[0]] += 1
        if st[0] == "R":
            g["first"] = min(g["first"] or st[1], st[1] or g["first"]) if st[1] else g["first"]
            g["last"] = max(g["last"], st[2])
            if len(g["ex"]) < 3:
                g["ex"].append("%s;%s;%s;%s;%s" % (app, st[3], st[4].replace(";", ","), st[1], st[2]))
        ag = agent.get(app)
        if ag and ag[3] == "CA":
            ak = ag[5] if ag[5] not in ("", "-1") else nkey(ag[0])
            g["agents"][ak] += 1
            g["ag"][ak] = ag
    os.makedirs(DIR, exist_ok=True)
    n_ca = n_xx = 0
    agents = collections.defaultdict(lambda: [None, 0, 0])
    with gzip.open(OWN_CA, "wt", encoding="utf-8", newline="") as fc, gzip.open(OWN_XX, "wt", encoding="utf-8", newline="") as fx:
        wc, wx = csv.DictWriter(fc, fieldnames=OWNER_COLS), csv.DictWriter(fx, fieldnames=OWNER_COLS)
        wc.writeheader(); wx.writeheader()
        for key in sorted(groups):
            g = groups[key]
            o = g["addr"]
            ak, n_ag = (g["agents"].most_common(1) or [("", 0)])[0]
            ag = g["ag"].get(ak)
            if ag:
                agents[ak][0] = ag; agents[ak][1] += 1; agents[ak][2] += n_ag
            row = {"owner_key": "tm:" + hashlib.sha1(key.encode()).hexdigest()[:14], "owner_name": g["names"].most_common(1)[0][0], "address": o[1], "province": o[2], "country": o[3],
                   "postal_code": pc6(o[4]) if o[3] == "CA" else ("" if o[4] in ("Unknown", "-1") else o[4]), "marks_in_force": g["R"], "marks_pending": g["P"], "first_registered": g["first"],
                   "latest_renewal_due": g["last"], "agent_name": ag[0] if ag else "", "agent_number": (ag[5] if ag and ag[5] != "-1" else ""), "agent_address": ("%s, %s" % (ag[1], ag[2])) if ag else "",
                   "agent_postal_code": pc6(ag[4]) if ag else "", "marks_with_this_agent": n_ag if ag else 0, "examples": " | ".join(g["ex"])}
            if o[3] == "CA":
                wc.writerow(row); n_ca += 1
            else:
                wx.writerow(row); n_xx += 1
    with open(AGENTS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["agent_number_or_key", "agent_name", "address", "province", "country", "postal_code", "owners", "marks"])
        for ak, (ag, n_o, n_m) in sorted(agents.items(), key=lambda kv: -kv[1][1]):
            w.writerow([ak, ag[0], ag[1], ag[2], ag[3], pc6(ag[4]), n_o, n_m])
    print("owners: %d in Canada, %d abroad; with a Canadian agent of record: %d; agent firms: %d [%.0fs]" % (
        n_ca, n_xx, sum(1 for g in groups.values() if g["agents"]), len(agents), time.time() - t0), flush=True)


# ------------------------------------------------------------------------------------------------------------------- match
RURAL = re.compile(r"^[A-Z]0")  # a rural postal code covers a whole village: the name must be the same, not merely alike


def site_index():
    """(domain, {name kind: name}, postal code, where the facts were read) for every site on file that states a Canadian postal code"""
    import ap_crawler as C
    reg = C.registrable
    host = lambda u: (re.sub(r"^https?://", "", (u or "").strip().lower()).split("/")[0]).removeprefix("www.")
    seen = set()
    try:  # 1. the scan's detector-5 lines: site, embedded, links, "site name|copyright name|legalName|postal code"
        import credit_scan as CS
        for l in CS.state_lines("links"):
            q = l.split("\t")
            if len(q) < 4:
                continue
            nm = q[3].split("|")
            if len(nm) == 4 and (pc6(nm[3]) or nm[1] or nm[2]):
                seen.add(q[0])
                yield q[0], {"site name": nm[0], "copyright line": nm[1], "legalName": nm[2]}, pc6(nm[3]), "its home page (scan, detector 5)"
    except Exception as e:
        print("scan name facts not read: %s" % e, flush=True)
    try:  # 2. what the lead readers kept of each site they read (name, address)
        import lead_crawl as LC
        for o in LC.facts_records():
            d = host(o.get("site"))
            m = re.search(r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][  -]?\d[ABCEGHJ-NPRSTV-Z]\d", (o.get("address") or o.get("address_quote") or "").upper())
            if d and m and d not in seen and (o.get("address_country") or "CA") == "CA":
                seen.add(d)
                yield d, {"site name": o.get("site_name") or ""}, pc6(m.group(0)), "its own pages (lead reader, %s)" % (o.get("address_url") or o.get("site") or "")
    except Exception as e:
        print("lead site facts not read: %s" % e, flush=True)
    try:  # 3. the delivered table: the row's name, the legal name it carries, its address
        import ranked_io
        for r in ranked_io.rows():
            d = host(r.get("buyer_website"))
            m = re.search(r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][  -]?\d[ABCEGHJ-NPRSTV-Z]\d", ((r.get("buyer_address") or "") + " " + (r.get("invoice_mailing_address") or "")).upper())
            lp = r.get("buyer_legal_name_as_published") or ""
            # a legal name the row took from the site itself (its structured data, its legal page, its copyright line) — not one a register gave it
            ln = re.sub(r"\s*\([^()]*(?:\([^()]*\)[^()]*)*\)\s*$", "", lp) if (re.search(r"\((?:schema\.org|stated on)", lp) or (lp and "(" not in lp)) else ""
            if d and d not in seen and (m or ln):
                seen.add(d)
                yield d, {"site name": r.get("buyer") or "", "legalName": ln}, pc6(m.group(0)) if m else "", "the delivered row (its name, legal-name and address cells)"
    except Exception as e:
        print("ranked table not read: %s" % e, flush=True)


def same_name(owner_k, names, pc):
    """'' or how the site's own name agrees with the owner's legal name (both stripped of legal-form words)"""
    ot = owner_k.split()
    for kind in ("legalName", "copyright line", "site name"):
        sk = nkey(names.get(kind) or "")
        if not sk:
            continue
        if sk == owner_k and (len(ot) >= 2 or len(owner_k) >= 5):
            return "the same name (%s) and the same postal code" % kind
    if RURAL.match(pc):
        return ""
    for kind in ("legalName", "copyright line", "site name"):
        st = nkey(names.get(kind) or "").split()
        if len(st) < 2 or len(ot) < 2:
            continue
        short, long_ = (st, ot) if len(st) <= len(ot) else (ot, st)
        extra = set(long_) - set(short)
        # the words the longer name adds must be everyday ones ("Canada", "Group", "Products") or an abbreviation: "Fondation du Musée X",
        # "Les Amis de X", "X Employees' Association" at the same address are other legal persons than X
        if len(short) >= 2 and set(short) <= set(long_) and any(t not in GENERIC and len(t) >= 4 for t in short) and len(extra) <= 2 and all(t in GENERIC or len(t) <= 3 for t in extra) and not (extra & OTHER_BODY):
            return "every word of the shorter name in the longer one (%s) and the same postal code" % kind
    return ""


def match(a):
    by_pc, by_name, n_person = collections.defaultdict(list), collections.defaultdict(list), 0
    with gzip.open(OWN_CA, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not is_org(r["owner_name"]):
                n_person += 1
                continue
            by_name[nkey(r["owner_name"])].append(r)
            if r["postal_code"]:
                by_pc[r["postal_code"]].append(r)
    print("owners in Canada with a postal code and an organisation's name: %d (%d postal codes); natural persons / names without a legal form left out: %d" % (
        sum(len(v) for v in by_pc.values()), len(by_pc), n_person), flush=True)
    out, n_sites, why = {}, 0, collections.Counter()
    sites = list(site_index())
    # a legal name that several sites state is a platform's, an agency's or a franchisor's line: it ties none of them to an owner
    stated = collections.Counter()
    for dom, names, pc, where in sites:
        for sk in {nkey(names.get(kind) or "") for kind in ("legalName", "copyright line")} - {""}:
            stated[sk] += 1
    for dom, names, pc, where in sites:
        n_sites += 1
        best = None
        for o in by_pc.get(pc, ()) if pc else ():
            how = same_name(nkey(o["owner_name"]), names, pc)
            if how:
                cand = (0 if how.startswith("the same name") else 1, -int(o["marks_in_force"] or 0), o, how)
                if best is None or cand[:2] < best[:2]:
                    best = cand
        if not best:
            # no postal code in common (the site prints none, or the owner moved): the site itself states a legal person — a name with its
            # legal form — that is word for word the name of ONE owner on the register, and no other site states that name
            for kind in ("legalName", "copyright line"):
                raw = names.get(kind) or ""
                sk = nkey(raw)
                toks = sk.split()
                if (raw and is_org(raw) and len(toks) >= 2 and any(t not in GENERIC and len(t) >= 4 for t in toks) and stated[sk] == 1 and len(by_name.get(sk, ())) == 1
                        and (dom.endswith(".ca") or pc)                                   # a site in Canada: a .ca name, or a Canadian postal code of its own
                        and forms(raw) and "foreign" not in forms(raw) and forms(raw) == forms(by_name[sk][0]["owner_name"])):  # the same kind of legal person, not a namesake abroad
                    o = by_name[sk][0]
                    best = (2, 0, o, "the same legal name, which the site itself states with its legal form (%s) and one owner on the register bears; no postal code in common" % kind)
                    break
        if best:
            out[dom] = (best[2], best[3], where, names)
            why[best[3].split(" (")[0]] += 1
    os.makedirs(DIR, exist_ok=True)
    with open(MATCHES, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["site", "owner_key", "owner_name", "postal_code", "tied_by", "site_facts_from", "site_states"])
        for dom in sorted(out):
            o, how, where, names = out[dom]
            w.writerow([dom, o["owner_key"], o["owner_name"], o["postal_code"], how, where, "; ".join("%s: %s" % kv for kv in names.items() if kv[1])[:200]])
    print("sites on file that state a Canadian postal code: %d; tied to a trademark owner: %d %s" % (n_sites, len(out), dict(why)))


# ------------------------------------------------------------------------------------------------------------------- leads
def leads(a):
    import lead_store as LS
    owners = {}
    with gzip.open(OWN_CA, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            owners[r["owner_key"]] = r
    prev, pdet = LS.load(exclude=("tm", a.stamp))
    snap = LS.snapshot(prev, pdet)
    mine = {k for k, d in pdet.items() if d.get("platform") == "tm_register"}
    kept, n_agent, n_office = set(), 0, 0
    for m in csv.DictReader(open(MATCHES, encoding="utf-8", newline="")):
        o = owners.get(m["owner_key"])
        if not o or not (int(o["marks_in_force"] or 0) or int(o["marks_pending"] or 0)):
            continue
        dom = m["site"]
        key = "lead:" + hashlib.sha1(("%s|tm" % dom).encode()).hexdigest()[:16]
        ex = [x.split(";") for x in (o["examples"] or "").split(" | ") if x.count(";") == 4]
        ref = ex[0] if ex else ["", "", "", "", ""]
        with_agent = bool(o["agent_name"]) and int(o["marks_with_this_agent"] or 0) > 0
        if not with_agent and not int(o["marks_in_force"] or 0):
            continue  # an application still pending, filed without an agent: no registration in force yet and no Canadian firm named
        vendor = o["agent_name"] if with_agent else OFFICE["name"]
        pc_ = o["agent_postal_code"]
        vaddr = ("%s%s, Canada" % (o["agent_address"], (" %s %s" % (pc_[:3], pc_[3:])) if pc_ else "")) if with_agent else OFFICE["address"] + ", Canada"
        rel = ("client of the Canadian trademark agent of record (%s)" % OFFICE["name"]) if with_agent else ("trademark registration holder of the Canadian body (%s)" % OFFICE["name"])
        quote = "%s | owner %s, %s %s | %s" % (ref[1] or ref[0], o["owner_name"], o["address"][:80], o["postal_code"], ("agent of record %s, %s" % (o["agent_name"], o["agent_address"][:70])) if with_agent else "no agent of record")
        prev[key] = {"buyer_key": key, "buyer_name": o["owner_name"], "website": "https://%s/" % dom, "canadian_vendor_rows": 1, "example_vendor": vendor,
                     "canada_field_value": "membership / statutory fee relationship: %s=%s (the register's own entry, extract of %s, %s); register: “%s” (%s)" % (rel, vaddr, SNAP_DATE, BASE + FILES["party"], quote[:240], PAGE),
                     "evidence_dataset": PAGE, "latest_record_date": SNAP_DATE}
        pdet[key] = {"key": key, "platform": "tm_register", "record_url": PAGE, "vendor": vendor, "record_date": SNAP_DATE, "start": o["first_registered"], "end": o["latest_renewal_due"],
                     "reference": ref[1] or ("application %s" % ref[0] if ref[0] else ""), "title": "Trademark %s%s — %d in force, %d pending on the Canadian register (extract of %s)" % (
                         ("“%s” " % ref[2]) if ref[2] else "", ("registration %s" % ref[1]) if ref[1] else "", int(o["marks_in_force"] or 0), int(o["marks_pending"] or 0), SNAP_DATE),
                     "vendor_address": "%s (the register's own entry for the %s, %s)" % (vaddr, "agent of record" if with_agent else "Office", BASE + FILES["party"] if with_agent else OFFICE["site"]),
                     "vendor_site": "" if with_agent else OFFICE["site"], "member_address_quote": "%s %s" % (o["address"], o["postal_code"]),
                     "register_label": "the Canadian trademarks register of the Canadian Intellectual Property Office, which names as agent of record" if with_agent else "the Canadian trademarks register published by",
                     "tm_relationship": "agent of record" if with_agent else "registration",
                     "tm_agent_of_record": o["agent_name"], "tm_agent_number": o["agent_number"], "tm_agent_address": o["agent_address"], "tm_marks_in_force": int(o["marks_in_force"] or 0),
                     "tm_marks_pending": int(o["marks_pending"] or 0), "tm_marks_with_this_agent": int(o["marks_with_this_agent"] or 0), "tm_examples": o["examples"],
                     "tm_first_registered": o["first_registered"], "tm_latest_renewal_due": o["latest_renewal_due"], "tm_extract": SNAP_DATE,
                     "buyer_register": {"legal_name": o["owner_name"], "trade_names": [], "registry_id": "", "legal_form": "", "phone": "",
                                        "address": "%s %s" % (o["address"], o["postal_code"]),
                                        "label": "the Canadian trademarks register (owner of record), extract of %s, %s" % (SNAP_DATE, PAGE)},
                     "dataset_basis": "Canadian Intellectual Property Office, trademarks researcher datasets (%s; data dictionary %s): table TM_interested_party, party type 10 current owner%s" % (
                         PAGE, DICT, ", party type 11 agent" if with_agent else ""),
                     "site_tied_to_holder_by": m["tied_by"], "site_page": "https://%s/" % dom, "site_quote": m["site_states"], "site_facts_from": m["site_facts_from"]}
        kept.add(key)
        n_agent += with_agent
        n_office += not with_agent
    gone = 0
    for k in mine - kept:  # a site no longer tied to an owner (a stricter rule, a changed site): its lead goes
        prev.pop(k, None); pdet.pop(k, None); gone += 1
    nu, nd, ng = LS.save("tm", a.stamp, prev, pdet, snap)
    print("trademark leads: %d sites tied to an owner (%d with a Canadian agent of record, %d holding registrations without one); withdrawn %d; shards: %d rows, %d details, %d gone" % (
        len(kept), n_agent, n_office, gone, nu, nd, ng))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "match", "leads"])
    ap.add_argument("--work", default=os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "tm_work"))
    ap.add_argument("--main", default="", help="build: a local copy of the application-main zip (tests)")
    ap.add_argument("--party", default="", help="build: a local copy of the interested-party zip (tests)")
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    a = ap.parse_args()
    {"build": build, "match": match, "leads": leads}[a.cmd](a)


if __name__ == "__main__":
    main()

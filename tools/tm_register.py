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
  sites --shard K/N       owners in Canada without a site on file: a few domain names made of the owner's own name (and marks) are resolved,
                          the home page of those that answer is read, and the site is kept only when its own pages tie it to the owner
                          -> out/tm_sites_<K>.csv, out/tm_sites_done_<K>.tsv; `merge-sites DIR` -> tm_sites_found.csv, tm_sites_done.tsv.gz
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


# the legal forms of the European countries of ABROAD, for owners there ("SIEMENS AKTIENGESELLSCHAFT" is "Siemens AG" on its site and in a
# places dataset): one more pass over a key nkey() made — the same pattern in Python and in DuckDB (RE2)
EU_FORMS = (r"\b(aktiengesellschaft|gesellschaft mit beschrankter haftung|kommanditgesellschaft|kgaa|kg|se|spa|s p a|sarl|s a r l|sas|sasu|sl|s l|slu|"
            r"s r l|srls|scarl|sapa|snc|eurl|ab|publ|oy|oyj|as|a s|aps|bvba|sprl|nv|bv|b v|n v|gmbh|ag|sa|s a|cie|et cie)\b")


def nkey_raw(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and "))).strip()


def nkey_x(s):
    """nkey() with the European legal forms left out as well: 'Siemens Aktiengesellschaft' -> 'siemens'"""
    return re.sub(r"\s+", " ", re.sub(EU_FORMS, " ", nkey(s))).strip()


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
            ln = re.sub(r"\s*\([^()]*(?:\([^()]*\)[^()]*)*\)\s*$", "", lp) if (re.search(r"\((?:schema\.org|stated on|printed with its legal form)", lp) or (lp and "(" not in lp)) else ""
            if d and d not in seen and (m or ln):
                seen.add(d)
                yield d, {"site name": r.get("buyer") or "", "legalName": ln}, pc6(m.group(0)) if m else "", "the delivered row (its name, legal-name and address cells)"
    except Exception as e:
        print("ranked table not read: %s" % e, flush=True)


def same_name(owner_k, names, pc, key=None):
    """'' or how the site's own name agrees with the owner's legal name (both stripped of legal-form words; key: nkey, or nkey_x abroad)"""
    key = key or nkey
    ot = owner_k.split()
    for kind in ("legalName", "copyright line", "site name"):
        sk = key(names.get(kind) or "")
        if not sk:
            continue
        if sk == owner_k and (len(ot) >= 2 or len(owner_k) >= 5):
            return "the same name (%s) and the same postal code" % kind
    if RURAL.match(pc):
        return ""
    for kind in ("legalName", "copyright line", "site name"):
        st = key(names.get(kind) or "").split()
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
    n_found = 0
    with open(MATCHES, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["site", "owner_key", "owner_name", "postal_code", "tied_by", "site_facts_from", "site_states"])
        for dom in sorted(out):
            o, how, where, names = out[dom]
            w.writerow([dom, o["owner_key"], o["owner_name"], o["postal_code"], how, where, "; ".join("%s: %s" % kv for kv in names.items() if kv[1])[:200]])
        if os.path.exists(FOUND):  # the owners' own sites found under their name (tm_register.py sites): tied when they were read, by the same tests
            for r in csv.DictReader(open(FOUND, encoding="utf-8", newline="")):
                if r["site"] not in out:
                    w.writerow([r["site"], r["owner_key"], r["owner_name"], r["postal_code"], r["tied_by"], r["site_facts_from"], r["site_states"]])
                    n_found += 1
    if n_found:
        print("plus %d owner sites found under their own name" % n_found)
    print("sites on file that state a Canadian postal code: %d; tied to a trademark owner: %d %s" % (n_sites, len(out), dict(why)))


# ------------------------------------------------------------------------------------------------------------------- sites of owners not on file
FOUND, SDONE = os.path.join(DIR, "tm_sites_found.csv"), os.path.join(DIR, "tm_sites_done.tsv.gz")
FOUND_COLS = ["site", "owner_key", "owner_name", "postal_code", "tied_by", "site_facts_from", "site_states", "read"]
_STOPW = {"and", "et", "of", "de", "du", "des", "the", "la", "le", "les", "for", "pour"}
_CONTACT = re.compile(r"contact|nous-joindre|joindre|coordonn|about|a-propos|propos", re.I)
# 2026-11-13: the pages where a site says which legal person runs it (terms, privacy, legal notice, imprint)
_LEGAL = re.compile(r"privacy|terms|legal|imprint|impressum|conditions|disclaimer|mentions-legales|aviso-legal|datenschutz|cookie", re.I)


def _legal_norm(s):
    """a legal name or a page's text for a verbatim comparison: '(a Delaware corporation)' left out, 'L.L.C.' -> 'llc', '&' -> 'and'"""
    s = re.sub(r"\([^)]{0,60}\)", " ", s or "")
    s = re.sub(r"\b([A-Za-z])\.(?=[A-Za-z]\b\.?)", r"\1", s)
    return " %s " % nkey_raw(s.replace(".", " "))


def other_body(org_name, text):
    """the text names another legal person built on the organisation's name: a foundation, an association, a union, friends or alumni of it
    ('Royal University Hospital Foundation' for the hospital) — the words of OTHER_BODY the text has and the organisation's name has not"""
    t_org = set(nkey_raw(org_name).split())
    t_txt = set(nkey_raw(text).split())
    return bool((t_txt & OTHER_BODY) - t_org)


def place_fits(org_name, place_name):
    """a place's name that is the organisation's — the test a place at the organisation's own ADDRESS must pass before the postal code printed on
    its site can count (every tenant of a building prints that code: 2026-11-13, 'NOVARTIS PHARMACEUTICALS CANADA INC' and a fitness club at the
    same postal code)"""
    # 2026-11-13, second look: ONE shared word is not enough ("Business Haldimand", the county's site, against the dealer "Haldimand Motors").
    # Third look, the same day (radio licensees, 309 of 784 such ties): TWO shared words are not enough either — "Northwest Properties Ltd. DBA
    # Country Club" against "Country Club Dental Centre", "Municipalité de Sainte-Hélène-de-Chester" against "Le Sainte-Hélène Auberge & Spa
    # Nordique", the City of Port Coquitlam against its firefighters' union: a tenant or a business named after the place. The place's name must
    # be the organisation's: all of it in the organisation's name, or its extra words generic or formal ones (tools/biz_licences.py agree_asym).
    import biz_licences as BL_
    if other_body(org_name, place_name):
        return False
    if nkey_x(org_name) and nkey_x(org_name) == nkey_x(place_name):
        return True  # the very name, legal form aside ("Cb Medical Inc." / "CB Medical"): agree_asym asks a short or generic name to identify more
    return BL_.agree_asym(org_name or "", place_name or "")

def legal_name_page(raw, final, fdom, owner_name, cache):
    """(url, the words around it, pages read) when one of the site's own terms / privacy / legal-notice pages linked from its home page prints
    the owner's full legal name WITH its legal form (at least three words: 'Zoetis Services LLC', 'Merck Sharp & Dohme LLC'), else ("", "", n)"""
    import credit_scan as CS_
    import ap_crawler as C_
    import tech_relationships as T_
    own = _legal_norm(owner_name)
    if len(own.split()) < 3 or not forms(owner_name):
        return "", "", 0
    links, n = [], 0
    for u, lab, *_ in T_.anchors_of(raw, final):
        if (_LEGAL.search(u.rsplit("/", 2)[-1] + " " + (lab or "")) and C_.registrable((CS_.host_of(u) or "").lower()) == fdom
                and u.split("#")[0] not in links and not re.search(r"\.(?:pdf|jpe?g|png|gif|zip|docx?)(?:$|\?)", u, re.I)):
            links.append(u.split("#")[0])
    for u in links[:2]:
        time.sleep(0.6)
        try:
            r2, f2, raw2 = CS_.get_page(u, True, cache)
        except Exception:
            continue
        n += 1
        if r2 != "ok":
            continue
        import cc_clients as CCL_
        txt = CCL_.visible(raw2)
        if own in _legal_norm(txt):
            words = own.strip().split()
            rx = r"(?i)" + r"[\W_]+".join("(?:and|&)" if w == "and" else r"\.?".join(re.escape(ch) for ch in w) if len(w) <= 4 else re.escape(w) for w in words)
            m = re.search(rx, txt)
            return f2 or u, (txt[max(0, m.start() - 60): m.end() + 60] if m else " ".join(words)).strip()[:200], n
    return "", "", n


# ---- owners abroad (2026-11-10): 134,458 owners outside Canada, 109,538 of them with a Canadian agent of record — a foreign company that
# pays a Canadian firm to hold its marks here. The register prints their address in one line ("767 Fifth Avenue, New York, NY 10153"); the
# postal code is its last token. Looked for in the three countries whose addresses the readers recognise.
ABROAD = {"US": ("United States", (".com", ".us")), "GB": ("United Kingdom", (".co.uk", ".com")), "AU": ("Australia", (".com.au", ".com"))}
# 2026-11-12: and the European countries with the most owners (FR 6,502 · DE 6,011 · IT 4,392 · CH 2,512 · ES 1,967 · NL 1,855 · SE 1,465 …),
# whose sites print their postal address by law (an Impressum, mentions légales, note legali, aviso legal): the register's postal code
# printed on the site ties it, as a ZIP code does
EU_CODE = {"FR": (r"(?<![\d-])(?:F-?\s?)?(\d{5})(?!\d)", "France", (".fr", ".com")), "DE": (r"(?<![\d-])(?:D-?\s?)?(\d{5})(?!\d)", "Deutschland|Germany|Allemagne", (".de", ".com")),
           "IT": (r"(?<![\d-])(?:I-?\s?)?(\d{5})(?!\d)", "Italia|Italy|Italie", (".it", ".com")), "ES": (r"(?<![\d-])(?:E-?\s?)?(\d{5})(?!\d)", "España|Espana|Spain|Espagne", (".es", ".com")),
           "CH": (r"(?<![\d-])(?:CH-?\s?)?(\d{4})(?!\d)", "Schweiz|Suisse|Svizzera|Switzerland", (".ch", ".com")), "AT": (r"(?<![\d-])(?:A-?\s?)?(\d{4})(?!\d)", "Österreich|Osterreich|Austria|Autriche", (".at", ".com")),
           "BE": (r"(?<![\d-])(?:B-?\s?)?(\d{4})(?!\d)", "Belgique|België|Belgie|Belgium|Belgien", (".be", ".com")), "DK": (r"(?<![\d-])(?:DK-?\s?)?(\d{4})(?!\d)", "Danmark|Denmark", (".dk", ".com")),
           "NL": (r"(?<![\d-])(\d{4}\s?[A-Z]{2})(?![A-Za-z])", "Nederland|Netherlands|Pays-Bas", (".nl", ".com")), "SE": (r"(?<![\d-])(?:S-?|SE-?)?(\d{3}\s?\d{2})(?!\d)", "Sverige|Sweden|Suède", (".se", ".com"))}
_EU_NAME = {"FR": "France", "DE": "Germany", "IT": "Italy", "ES": "Spain", "CH": "Switzerland", "AT": "Austria", "BE": "Belgium", "DK": "Denmark", "NL": "Netherlands", "SE": "Sweden"}
for _cc, (_rx, _nm, _tl) in EU_CODE.items():
    ABROAD[_cc] = (_EU_NAME[_cc], _tl)


def is_org_abroad(name, cc):
    """is_org(), and for an owner in one of the European countries of ABROAD a name that carries that country's legal form (AG, S.p.A., SARL, AB …)"""
    return is_org(name) or (cc in EU_CODE and bool(re.search(EU_FORMS, nkey_raw(name))))
_US_STATES = dict(zip("alabama alaska arizona arkansas california colorado connecticut delaware florida georgia hawaii idaho illinois indiana iowa kansas kentucky louisiana maine maryland "
                      "massachusetts michigan minnesota mississippi missouri montana nebraska nevada newhampshire newjersey newmexico newyork northcarolina northdakota ohio oklahoma oregon "
                      "pennsylvania rhodeisland southcarolina southdakota tennessee texas utah vermont virginia washington westvirginia wisconsin wyoming districtofcolumbia".split(),
                      "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC".split()))


def place_abroad(address, country):
    """(postal code, state) the register's one-line address ends with: ('10153', 'NY'), ('SW1A1AA', ''), ('2000', 'NSW'); ('', '') when unclear"""
    a = re.sub(r"\s+", " ", (address or "").strip(" ,.")).strip()
    a = re.sub(r",?\s*(?:U\.?S\.?A\.?|United States(?: of America)?|United Kingdom|U\.?K\.?|England|Scotland|Wales|Australia)$", "", a, flags=re.I).strip(" ,.")
    if country == "US":
        m = re.search(r"(?:,|\s)\s*([A-Za-z][A-Za-z. ]{1,20}?)\.?,?\s+(\d{5})(?:-\d{4})?$", a)
        if not m:
            return "", ""
        st = re.sub(r"[^a-z]", "", m.group(1).lower())
        st = st.upper() if len(st) == 2 and st.upper() in _US_STATES.values() else _US_STATES.get(st, "")
        if not st:  # "New York, NEW YORK 10003": the state is the last one or two words before the code
            w = re.sub(r"[^a-z ]", "", m.group(1).lower()).split()
            st = _US_STATES.get("".join(w[-2:]), "") or _US_STATES.get("".join(w[-1:]), "")
        return m.group(2), st
    if country == "GB":
        m = re.search(r"\b([A-Z]{1,2}\d[A-Z\d]?)\s?(\d[A-Z]{2})$", a.upper())
        return (m.group(1) + m.group(2), "") if m else ("", "")
    if country == "AU":
        m = re.search(r"\b(NSW|VIC|QLD|TAS|ACT|WA|SA|NT|New South Wales|Victoria|Queensland|Tasmania|Western Australia|South Australia)\.?,?\s+(\d{4})$", a, re.I)
        if not m:
            return "", ""
        st = {"new south wales": "NSW", "victoria": "VIC", "queensland": "QLD", "tasmania": "TAS", "western australia": "WA", "south australia": "SA"}.get(m.group(1).lower(), m.group(1).upper())
        return m.group(2), st
    if country in EU_CODE:  # the LAST postal code of the one-line address ("Hauptstraße 12, 80331 München": 80331)
        ms = list(re.finditer(EU_CODE[country][0], a.upper() if country == "NL" else a))
        return (re.sub(r"\s", "", ms[-1].group(1)), "") if ms else ("", "")
    return "", ""


def printed_abroad(text, country, code, state):
    """(the register's postal code printed in an address of that country, the same state / country printed in an address) on a page's text"""
    import lead_crawl as LC
    same_code = same_state = False
    if country == "US":
        for m in LC.US_ADDR.finditer(text):
            same_state = same_state or (bool(state) and m.group(2) == state)
            same_code = same_code or (bool(code) and m.group(3) == code)
    elif country == "GB":
        for m in LC.GB_ADDR.finditer(text):
            same_state = True
            same_code = same_code or (bool(code) and re.sub(r"\s", "", m.group(2)) == code)
    elif country == "AU":
        for m in re.finditer(r"(?<![A-Za-z0-9])(NSW|VIC|QLD|TAS|ACT|WA|SA|NT)\s+(\d{4})(?!\d)", text):
            same_state = same_state or (bool(state) and m.group(1) == state)
            same_code = same_code or (bool(code) and m.group(2) == code and (not state or m.group(1) == state))
    elif country in EU_CODE:
        # the register's postal code followed by a place name ("80331 München", "75008 Paris", "1012 AB Amsterdam"), as an address prints it;
        # "the same state" here is the country's own name printed on the site
        rx, names_, _ = EU_CODE[country]
        for m in re.finditer(rx + r"[ ,]+[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’.-]{2,}", text):
            same_code = same_code or (bool(code) and re.sub(r"\s", "", m.group(1)).upper() == code)
        same_state = bool(re.search(r"\b(?:%s)\b" % names_, text))
    return same_code, same_state


def labels_of(name, marks):
    """[(label, kind)] — the few domain labels an organisation would plausibly hold: its own name written in one word, with and without its
    everyday words (kind "name"), its first two words ("short"), then its marks ("mark"). A label is only where to LOOK: a site counts when
    its own pages state the owner's name (and, for a "short" or "mark" label, its postal code)."""
    toks = nkey(name).split()
    out = []

    def add(x, kind):
        x = re.sub(r"[^a-z0-9-]", "", x).strip("-")
        if 4 <= len(x) <= 32 and x not in [o[0] for o in out]:
            out.append((x, kind))
    core = [t for t in toks if t not in _STOPW]
    if core and re.fullmatch(r"\d{5,}", core[0]):
        core = []  # a numbered company is not found under its number: its marks only
    add("".join(core), "name")
    spec = [t for t in core if t not in GENERIC]
    if len(spec) >= 2 or (len(spec) == 1 and len(spec[0]) >= 8):
        add("".join(spec), "name")
    if 2 <= len(core) <= 3:
        add("-".join(core), "name")
    if len(core) >= 3:
        add("".join(core[:2]), "short")
    for m in marks[:3]:
        mk = nkey(m).split()
        if 1 <= len(mk) <= 4:
            add("".join(t for t in mk if t not in _STOPW), "mark")
    return out[:5]


def sites(a):
    """look for the own site of owners in Canada that no site on file is tied to: resolve the few labels of labels_of() on .ca and .com, read
    the home page of those that answer (robots.txt obeyed, one more page when the home page links its contact page and prints no postal
    code), keep the site only when same_name() ties it — the same tests as for the sites on file. -> out/tm_sites_<k>.csv, out/tm_sites_done_<k>.tsv"""
    import socket
    import threading
    from concurrent.futures import ThreadPoolExecutor
    import ap_crawler as C
    import cc_clients as CCL
    import credit_scan as CS
    import lead_crawl as LC
    import tech_relationships as T
    CS._fetch = CS.fast_fetch
    k, n = (int(x) for x in (a.shard.split("/") + ["1"])[:2])
    os.makedirs("out", exist_ok=True)
    tied = {r["owner_key"] for r in csv.DictReader(open(MATCHES, encoding="utf-8", newline=""))} if os.path.exists(MATCHES) else set()
    done, done_ovt, done_cb, done_legal, marks_of = set(), set(), set(), set(), {}
    done_ror = set()
    use_ror = bool(getattr(a, "ror", False))
    # 2026-11-13: with --overture --legal, the owners whose listed sites were read before are read again — only the listed sites — with the
    # legal-page test added (the site's own terms / privacy / legal notice printing the owner's full legal name with its legal form)
    use_legal = bool(getattr(a, "legal", False)) and bool(getattr(a, "overture", False))
    if os.path.exists(SDONE):
        with gzip.open(SDONE, "rt", encoding="utf-8") as f:
            for l in f:
                q = l.rstrip("\n").split("\t")
                done.add(q[0])
                mk = set(q[5].split(",")) if len(q) > 5 and q[5] else set()
                marks_of[q[0]] = mk
                if "overture" in mk:
                    done_ovt.add(q[0])
                if "clearbit" in mk:
                    done_cb.add(q[0])
                if "legal" in mk:
                    done_legal.add(q[0])
                if "ror2" in mk:
                    done_ror.add(q[0])  # (2026-11-13 07:32Z: owners read under the first ROR rule, mark "ror", are read once more under the second)
    # 2026-11-12: with --clearbit (owners abroad), the domains the company-name autocomplete gives under the owner's very name are read too —
    # also for an owner looked for before under domain names made of its name. A domain is kept by the same tests as any other: the register's
    # postal code printed in an address on the site under the same name, or the legal person stated with its legal form on a site of the owner's
    # state. The autocomplete alone ties nothing.
    use_cb = bool(getattr(a, "clearbit", False)) and bool(getattr(a, "abroad", False))
    if use_cb:
        import hc_registers as HR
        cb_lock = threading.Lock()
    by_name, by_name_x = collections.Counter(), collections.Counter()
    owners = []
    abroad = bool(getattr(a, "abroad", False))
    # 2026-11-12: with --overture, the owners for whom an Overture Maps place lists a website under their name (tm_overture_sites.csv) — read
    # first, also when the owner was looked for before under domain names made of its name
    ovt = collections.defaultdict(list)
    if not abroad and getattr(a, "overture", False) and os.path.exists(OVT_ADDR_CA):
        for r in csv.DictReader(open(OVT_ADDR_CA, encoding="utf-8", newline="")):
            ovt[r["owner_key"]].append(r)
    if abroad and getattr(a, "overture", False):
        for p_ in (OVT_SITES, OVT_ADDR):
            if os.path.exists(p_):
                for r in csv.DictReader(open(p_, encoding="utf-8", newline="")):
                    ovt[r["owner_key"]].append(r)
    if use_ror:  # the registries' listed websites: ROR, then Wikidata (each row says its source)
        for p_, src_ in ((ROR_SITES, "ror"), (WD_SITES, "wikidata")):
            if os.path.exists(p_):
                for r in csv.DictReader(open(p_, encoding="utf-8", newline="")):
                    r["source"] = r.get("source") or src_
                    ovt[r["owner_key"]].append(r)
    use_ovt = bool(ovt)
    for path, here in ((OWN_CA, True), (OWN_XX, False)):  # "one owner of that name on the register" counts both files
        with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if not (is_org(r["owner_name"]) if here else is_org_abroad(r["owner_name"], r["country"])):
                    continue
                by_name[nkey(r["owner_name"])] += 1
                by_name_x[nkey_x(r["owner_name"])] += 1
                if r["owner_key"] in tied or int(hashlib.sha1(r["owner_key"].encode()).hexdigest(), 16) % n != k:
                    continue
                if (r["owner_key"] in done_legal) if use_legal else (all(REG_SRC.get(v.get("source"), ("", "?"))[1] in marks_of.get(r["owner_key"], set()) for v in ovt.get(r["owner_key"], ()))) if use_ror else (r["owner_key"] in done_ovt) if use_ovt else (r["owner_key"] in done_cb) if use_cb else (r["owner_key"] in done):
                    continue
                if use_ovt and r["owner_key"] not in ovt:
                    continue
                if here and not abroad and r["postal_code"]:
                    owners.append(r)
                elif not here and abroad and r["country"] in ABROAD and (int(r["marks_in_force"] or 0) or (r["agent_name"] and int(r["marks_with_this_agent"] or 0))):
                    r["_code"], r["_state"] = place_abroad(r["address"], r["country"])
                    if r["_code"]:
                        owners.append(r)
    owners.sort(key=lambda r: (-int(r["marks_in_force"] or 0), r["owner_key"]))
    if a.limit:
        owners = owners[:a.limit]
    print("shard %d/%d: %d owners %s without a site on file (%d looked for before)" % (k, n, len(owners), ("abroad (%s)" % ", ".join(sorted(ABROAD))) if abroad else "in Canada", len(done)), flush=True)
    deadline = time.time() + a.minutes * 60
    lock, stats, notes = threading.Lock(), collections.Counter(), []
    ff = open("out/tm_sites_%d.csv" % k, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(ff, fieldnames=FOUND_COLS)
    w.writeheader()
    fd = open("out/tm_sites_done_%d.tsv" % k, "a", encoding="utf-8")

    def resolves(h):
        try:
            socket.getaddrinfo(h, 443, type=socket.SOCK_STREAM)
            return True
        except Exception:
            return False

    def facts(raw, final):
        fhost = (CS.host_of(final) or "").lower()
        title, meta = T.page_meta(raw)
        name = LC.site_name_for(fhost, meta.get("og:site_name"), title, T)
        text = CCL.visible(raw)
        m = CCL.ADDR.search(text)
        nf = CS.name_facts(raw, name, text[max(0, m.start() - 60):m.end()] if m else "").split("|")
        return {"site name": nf[0], "copyright line": nf[1], "legalName": nf[2]}, nf[3]

    def one(o):
        if time.time() > deadline:
            return
        cc = o["country"] if abroad else "CA"
        kf = nkey_x if cc in EU_CODE else nkey  # an owner in Europe: its legal form (AG, S.p.A., SARL …) left out too
        bn = by_name_x if cc in EU_CODE else by_name
        ok_ = kf(o["owner_name"])
        marks = [x.split(";")[2] for x in (o["examples"] or "").split(" | ") if x.count(";") == 4 and x.split(";")[2]]
        kind_of = {lab + tld: kind for lab, kind in labels_of(o["owner_name"], marks) for tld in (ABROAD[cc][1] if abroad else (".ca", ".com"))}
        cands = list(kind_of)
        listed = {}
        for r_ in ovt.get(o["owner_key"], ()):  # published websites first: an Overture place under the owner's name at its postal code / in its state
            listed[r_["site"]] = r_
            kind_of.setdefault(r_["site"], "listed")
        cands = list(listed) + [h for h in cands if h not in listed]
        if use_legal:
            cands = list(listed)  # the legal-page pass reads only the sites a place lists
        cbs = []
        if use_cb:
            core_ = HR.core(o["owner_name"])
            if len(core_) >= 4 and not (len(core_.split()) == 1 and len(core_) < 6):
                with cb_lock:  # one request a second for the whole runner
                    sug = HR.suggest(core_) or []
                cbs = [d for d, sn in (((x_.get("domain") or "").lower().strip(), HR.core(x_.get("name") or "")) for x_ in sug[:5])
                       if d and sn == core_ and not HR.BAD.search(d) and HR.domain_fits(d, core_, cc)]
            for d in cbs:
                kind_of.setdefault(d, "clearbit")
            # an owner looked for before under its own name: only the autocomplete's domains are new
            cands = cbs + [h for h in cands if h not in cbs and o["owner_key"] not in done]
        live = [h for h in cands if resolves(h)][:4 + len(listed) + len(cbs)]
        hit, n_read = None, 0
        for h in live:
            cache = {}
            try:
                res, final, raw = CS.get_page("https://%s/" % h, True, cache)
            except Exception:
                continue
            n_read += 1
            if res != "ok":
                continue
            fdom = C.registrable((CS.host_of(final) or h).lower())
            names, pc = facts(raw, final)
            if abroad:
                # An owner abroad: the same tests with the owner's own country in the place of Canada. (1) the same name and the register's
                # postal code printed in an address on the site; (2) the owner's legal person stated with its legal form, one owner of that
                # name, an address of the owner's state (or country) on the site; (3) the domain name is the owner's name written out, the
                # site names itself so, one owner of that name, an address of the owner's state on the site.
                where, text = final, CCL.visible(raw)
                code_ok, state_ok = printed_abroad(text, cc, o["_code"], o["_state"])
                if not code_ok:
                    link = next((u for u, lab, *_ in T.anchors_of(raw, final) if _CONTACT.search(u.rsplit("/", 2)[-1] + " " + (lab or "")) and C.registrable((CS.host_of(u) or "").lower()) == fdom), "")
                    if link:
                        time.sleep(0.6)
                        try:
                            r2, f2, raw2 = CS.get_page(link.split("#")[0], True, cache)
                        except Exception:
                            r2 = ""
                        n_read += 1
                        if r2 == "ok":
                            c2, s2 = printed_abroad(CCL.visible(raw2), cc, o["_code"], o["_state"])
                            if c2:
                                code_ok, where = True, f2
                            state_ok = state_ok or s2
                sn = same_name(ok_, names, "M5V2T6", key=kf)
                what = {"US": "ZIP code", "GB": "postcode", "AU": "postcode"}.get(cc, "postal code")
                how = ""
                if sn and code_ok:
                    how = sn.replace("the same postal code", "the same %s (%s, printed in an address on the site)" % (what, o["_code"]))
                if not how and state_ok:
                    for kind in ("legalName", "copyright line"):
                        raw_n = names.get(kind) or ""
                        if (raw_n and kf(raw_n) == ok_ and bn[ok_] == 1 and len(ok_.split()) >= 2 and any(t not in GENERIC and len(t) >= 4 for t in ok_.split())
                                and forms(raw_n) and forms(raw_n) == forms(o["owner_name"])):
                            how = "the same legal name, which the site itself states with its legal form (%s) and one owner on the register bears; a site in the owner's %s (%s)" % (
                                kind, "state" if o["_state"] else "country", o["_state"] or ABROAD[cc][0])
                            break
                if (not how and state_ok and o["_state"] and kind_of.get(h) == "name" and bn[ok_] == 1 and sn.startswith("the same name") and len(ok_.split()) >= 2
                        and any(t not in GENERIC and len(t) >= 4 for t in ok_.split())
                        and fdom.split(".")[0].replace("-", "") in {lab.replace("-", "") for lab, kd in labels_of(o["owner_name"], marks) if kd == "name"}):
                    how = "the same name (%s), on a domain name that is the owner's name written out; a site in the owner's state (%s, %s); one owner of that name on the register" % (
                        "site name" if kf(names.get("site name") or "") == ok_ else "its own statement", o["_state"], ABROAD[cc][0])
                _l = listed.get(h)
                if not how and _l and _l.get("source") in REG_SRC and sn.startswith("the same name") and (state_ok or code_ok) and len(ok_.split()) + len(ok_) >= 7:
                    # 2026-11-13: two sources agree — the Research Organization Registry lists THIS website for the organisation of the owner's very
                    # name in its country, and the site's own pages state that name with an address of the owner's state (or country)
                    how = "the same name (%s) and an address of the owner's %s (%s) on the site; " + REG_SRC[_l["source"]][0] + " the organisation of that name in %s (%s)"
                    how = how % (
                        sn.split("(", 1)[1].split(")")[0], "state" if o["_state"] else "country", o["_state"] or ABROAD[cc][0], ABROAD[cc][0], _l["place_id"])
                if (not how and _l and _l.get("source") in REG_SRC and sn.startswith("the same name") and len(ok_.split()) >= 2 and len(ok_) >= 10
                        and any(t not in GENERIC and len(t) >= 4 for t in ok_.split()) and bn[ok_] == 1):
                    # 2026-11-13 07:32Z: three sources agree — the register's owner name, the Research Organization Registry's record of that very name
                    # in the owner's country with THIS website, and the site's own statement of that name (no address of the owner's state read on
                    # its pages: a university's or an institute's site often prints none on its home page); one owner of that name on the register
                    how = ("the same name (%s) on the site; " + REG_SRC[_l["source"]][0] + " the organisation of that very name in %s (%s); one owner of that name on the register") % (
                        sn.split("(", 1)[1].split(")")[0], ABROAD[cc][0], _l["place_id"])
                if not how and _l and _l.get("source") not in REG_SRC and sn and (sn.startswith("the same name") or _l["how"].startswith("the owner's own ")) and len(ok_.split()) + len(ok_) >= 7:
                    # 2026-11-12: two sources agree — an Overture Maps place lists THIS website under the owner's name at the register's postal
                    # code (or in its state, and the site prints an address of that state), and the site's own pages state that name
                    if _l["how"].startswith("the same name at the same"):
                        how = "the same name (%s); an Overture Maps place lists this website under the owner's name at the register's %s (%s, place %s)" % (
                            sn.split("(", 1)[1].split(")")[0], what, o["_code"], _l["place_id"])
                    elif _l["how"].startswith("the owner's own "):
                        # 2026-11-13: an Overture Maps place AT the register's street address (street number, street and ZIP code) or UK postcode
                        # lists this website, and the site's own pages state the owner's name
                        # (the name test as for an owner in Canada: the same name, or every word of the shorter name in the longer one with only
                        # everyday words added — the second fact being the place at the owner's own street address instead of a postal code)
                        _kind, _, _at = _l["how"][len("the owner's own "):].partition(" (")
                        how = "%s (%s); an Overture Maps place at the owner's own %s on the register (%s) lists this website (place %s)" % (
                            "the same name" if sn.startswith("the same name") else "every word of the shorter name in the longer one",
                            sn.split("(", 1)[1].split(")")[0], _kind, _at.rstrip(")"), _l["place_id"])
                    elif state_ok and sn.startswith("the same name"):
                        how = "the same name (%s) and an address of the owner's state (%s) on the site; an Overture Maps place lists this website under the owner's name in that state (place %s)" % (
                            sn.split("(", 1)[1].split(")")[0], o["_state"] or ABROAD[cc][0], _l["place_id"])
                if not how and _l:
                    # 2026-11-13: a site that an Overture Maps place lists (under the owner's name, or at the owner's own street address) and whose own
                    # terms / privacy / legal-notice page prints the owner's full legal name with its legal form: the site says which legal person
                    # runs it, and the place's listing is the second fact (a subsidiary on its group's site: "Zoetis Services LLC" on zoetis.com)
                    _lu, _lq, _ln = legal_name_page(raw, final, fdom, o["owner_name"], cache)
                    n_read += _ln
                    if _lu and _l.get("source") in REG_SRC:
                        how = ("the owner's full legal name with its legal form on the site's own legal page (%s: “%s”); " + REG_SRC[_l["source"]][0] + " the organisation of that name (%s)") % (
                            _lu, _lq, _l["place_id"])
                    elif _lu:
                        how = "the owner's full legal name with its legal form on the site's own legal page (%s: “%s”); an Overture Maps place %s lists this website (place %s)" % (
                            _lu, _lq, "at the owner's own %s on the register" % _l["how"][len("the owner's own "):].partition(" (")[0]
                            if _l["how"].startswith("the owner's own ") else "under the owner's name", _l["place_id"])
                        where = _lu
                        with lock:
                            stats["tied by the legal name on the site's own legal page"] += 1
                if not how:
                    with lock:
                        stats["read, not tied: " + ("name agrees, " + ("the owner's state, another postal code" if state_ok else "no address of the owner's state on its pages") if sn else "its name is another")] += 1
                else:
                    _lst = listed.get(h)
                    hit = {"site": fdom, "owner_key": o["owner_key"], "owner_name": o["owner_name"], "postal_code": o["_code"], "tied_by": how,
                           "site_facts_from": ("its own pages (%s), found as the website %s lists for the owner's name in its country (“%s”, %s; data of %s)" % (
                               where, REG_SRC[_lst["source"]][2], _lst["place_name"], _lst["place_id"], _lst["release"]) if _lst and _lst.get("source") in REG_SRC else
                                               "its own pages (%s), found as the website an Overture Maps place lists %s (“%s”, %s; %s, release %s)" % (
                               where, "at the owner's own address" if _lst["how"].startswith("the owner's own ") else "for the owner's name",
                               _lst["place_name"], _lst["place_postcode"], _lst["how"], _lst["release"]) if _lst else
                                               "its own pages (%s), found as the domain the company-name autocomplete (Clearbit) gives under the owner's very name" % where
                                               if kind_of.get(h) == "clearbit" else
                                               "its own pages (%s), found under a domain name made of the owner's name or mark" % where),
                           "site_states": "; ".join("%s: %s" % kv for kv in names.items() if kv[1])[:200], "read": TODAY}
                    break
                continue
            how = same_name(ok_, names, pc) if pc == o["postal_code"] else ""
            where = final
            if not how and not pc:  # the home page prints no postal code: its contact page, when the home page links one
                link = next((u for u, lab, *_ in T.anchors_of(raw, final) if _CONTACT.search(u.rsplit("/", 2)[-1] + " " + (lab or "")) and C.registrable((CS.host_of(u) or "").lower()) == fdom), "")
                if link:
                    time.sleep(0.6)
                    try:
                        r2, f2, raw2 = CS.get_page(link.split("#")[0], True, cache)
                    except Exception:
                        r2 = ""
                    n_read += 1
                    if r2 == "ok":
                        n2, pc2 = facts(raw2, f2)
                        if pc2 == o["postal_code"]:
                            how, where, pc = same_name(ok_, names, pc2), f2, pc2
            if not how:  # no postal code in common: the site states the owner's legal person with its legal form (one owner of that name)
                for kind in ("legalName", "copyright line"):
                    raw_n = names.get(kind) or ""
                    if (raw_n and nkey(raw_n) == ok_ and by_name[ok_] == 1 and len(ok_.split()) >= 2 and any(t not in GENERIC and len(t) >= 4 for t in ok_.split())
                            and (fdom.endswith(".ca") or pc) and forms(raw_n) and "foreign" not in forms(raw_n) and forms(raw_n) == forms(o["owner_name"])):
                        how = "the same legal name, which the site itself states with its legal form (%s) and one owner on the register bears; no postal code in common" % kind
                        break
            if (not how and kind_of.get(h) == "name" and by_name[ok_] == 1 and (fdom.endswith(".ca") or pc) and same_name(ok_, names, "M5V2T6").startswith("the same name")
                    and len(ok_.split()) >= 2 and fdom.split(".")[0].replace("-", "") in {lab.replace("-", "") for lab, kd in labels_of(o["owner_name"], marks) if kd == "name"}):
                # three things agree: the domain name is the owner's own name written out, the site names itself by that name, and the site is in
                # Canada (a .ca name, or a Canadian postal code on its pages — another one than the register's: an office moved, a second address).
                # One owner of that name on the register.
                how = "the same name (%s), on a domain name that is the owner's name written out; a site in Canada (%s); one owner of that name on the register" % (
                    "site name" if nkey(names.get("site name") or "") == ok_ else "its own statement", ("it prints the postal code %s, the register has %s" % (pc, o["postal_code"])) if pc else "a .ca name, no postal code on the pages read")
            if (not how and listed.get(h) and listed[h].get("source") in REG_SRC and pc and len(ok_.split()) + len(ok_) >= 7
                    and same_name(ok_, names, "M5V2T6").startswith("the same name")):
                # 2026-11-13: two sources agree — the Research Organization Registry lists THIS website for the organisation of the owner's very
                # name in Canada, and the site's own pages state that name with a Canadian postal code
                how = ("the same name (%s) and a Canadian postal code on the site (%s; the register has %s); " + REG_SRC[listed[h]["source"]][0] + " the organisation of that name in Canada (%s)") % (
                    same_name(ok_, names, "M5V2T6").split("(", 1)[1].split(")")[0], pc, o["postal_code"], listed[h]["place_id"])
            if (not how and listed.get(h) and listed[h].get("source") in REG_SRC and not pc and len(ok_.split()) >= 2 and len(ok_) >= 10
                    and any(t not in GENERIC and len(t) >= 4 for t in ok_.split()) and by_name[ok_] == 1
                    and same_name(ok_, names, "M5V2T6").startswith("the same name")):
                # three sources agree (the register, ROR's record of that very name in Canada with THIS website, the site's own statement); no
                # postal code on the pages read; one owner of that name on the register
                how = ("the same name (%s) on the site; " + REG_SRC[listed[h]["source"]][0] + " the organisation of that very name in Canada (%s); one owner of that name on the register") % (
                    same_name(ok_, names, "M5V2T6").split("(", 1)[1].split(")")[0], listed[h]["place_id"])
            if not how and listed.get(h):
                # 2026-11-13: a site an Overture Maps place at the owner's own postal code lists, whose own terms / privacy / legal page prints
                # the owner's full legal name with its legal form
                _lu, _lq, _ln = legal_name_page(raw, final, fdom, o["owner_name"], cache)
                n_read += _ln
                if _lu:
                    how = "the owner's full legal name with its legal form on the site's own legal page (%s: “%s”); %s (%s)" % (
                        _lu, _lq, (REG_SRC[listed[h]["source"]][0] + " the organisation of that name") if listed[h].get("source") in REG_SRC
                        else "an Overture Maps place at the owner's own postal code on the register lists this website (place", listed[h]["place_id"]) + ("" if listed[h].get("source") in REG_SRC else ")")
                    where = _lu
            if not how:
                # what stood between this site and a tie (counted, for the rule's next look)
                nm_ok = bool(same_name(ok_, names, "M5V2T6"))  # the name test alone (an urban code)
                with lock:
                    stats["read, not tied: " + ("name agrees, " + ("another postal code" if pc else "no postal code on its pages") if nm_ok else "its name is another")] += 1
                    if nm_ok and len(notes) < 60:
                        notes.append((o["owner_name"], o["postal_code"], fdom, pc, "; ".join("%s: %s" % kv for kv in names.items() if kv[1])[:90]))
            if how:
                hit = {"site": fdom, "owner_key": o["owner_key"], "owner_name": o["owner_name"], "postal_code": o["postal_code"], "tied_by": how,
                       "site_facts_from": ("its own pages (%s), found as the website %s lists for the owner's name in Canada (“%s”, %s; data of %s)" % (
                           where, REG_SRC[listed[h]["source"]][2], listed[h]["place_name"], listed[h]["place_id"], listed[h]["release"]) if listed.get(h) and listed[h].get("source") in REG_SRC else
                                           "its own pages (%s), found as the website an Overture Maps place lists at the owner's own address (“%s”, %s; release %s)" % (
                           where, listed[h]["place_name"], listed[h]["place_postcode"], listed[h]["release"]) if listed.get(h) else
                                           "its own pages (%s), found under a domain name made of the owner's name or mark" % where),
                       "site_states": "; ".join("%s: %s" % kv for kv in names.items() if kv[1])[:200], "read": TODAY}
                break
        with lock:
            stats["owners"] += 1
            stats["with_a_name_that_resolves"] += bool(live)
            stats["pages_read"] += n_read
            stats["site_found"] += bool(hit)
            if hit:
                w.writerow(hit)
                stats[hit["tied_by"].split(" (")[0]] += 1
            mk = (set(marks_of.get(o["owner_key"], set())) | ({"overture"} if any(v.get("source") not in REG_SRC for v in listed.values()) else set())
                  | {REG_SRC[v["source"]][1] for v in listed.values() if v.get("source") in REG_SRC} | ({"clearbit"} if use_cb else set()) | ({"legal"} if use_legal and listed else set()))
            fd.write("%s\t%s\t%d\t%d\t%s%s\n" % (o["owner_key"], TODAY, len(cands), len(live), hit["site"] if hit else "", ("\t" + ",".join(sorted(mk))) if mk else ""))
            stats["autocomplete domains read"] += len(cbs)
            stats["owners with a listed website"] += bool(listed)
            if stats["owners"] % 500 == 0:
                ff.flush(); fd.flush()
                print(time.strftime("%H:%M:%S"), dict(stats), flush=True)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, owners))
    ff.close(); fd.close()
    print("finished", dict(stats), flush=True)
    for x in notes:
        print("  name agrees, not tied: %-40s %s | %-28s %-7s | %s" % (x[0][:40], x[1], x[2], x[3], x[4]))


def merge_sites(a):
    """shard files -> tm_sites_found.csv (one line per site, the newest wins) and tm_sites_done.tsv.gz"""
    found = {}
    if os.path.exists(FOUND):
        for r in csv.DictReader(open(FOUND, encoding="utf-8", newline="")):
            found[r["site"]] = r
    n0 = len(found)
    for p in sorted(glob.glob(os.path.join(a.dir, "tm_sites_[0-9]*.csv"))):
        for r in csv.DictReader(open(p, encoding="utf-8", newline="")):
            if r.get("site") and r["site"] != "site":
                found[r["site"]] = r
    with open(FOUND, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FOUND_COLS)
        w.writeheader()
        for k in sorted(found):
            w.writerow({c: found[k].get(c, "") for c in FOUND_COLS})
    lines = {}
    if os.path.exists(SDONE):
        with gzip.open(SDONE, "rt", encoding="utf-8") as f:
            for l in f:
                lines[l.split("\t", 1)[0]] = l.rstrip("\n")
    for p in sorted(glob.glob(os.path.join(a.dir, "tm_sites_done_*.tsv"))):
        for l in open(p, encoding="utf-8"):
            if l.strip():
                lines[l.split("\t", 1)[0]] = l.rstrip("\n")
    with gzip.open(SDONE, "wt", encoding="utf-8") as f:
        f.write("\n".join(lines[k] for k in sorted(lines)) + "\n")
    print("owner sites found under their own name: %d (+%d this run); owners looked for so far: %d" % (len(found), len(found) - n0, len(lines)))


# ------------------------------------------------------------------------------------------------------------------- the agent firms' own sites
AGENT_CAND = os.path.join(ROOT, "tools/data/tm_agent_site_candidates.csv")
AGENT_SITES = os.path.join(DIR, "tm_agent_sites.csv")
AGENT_SITE_COLS = ["agent_name", "postal_code", "site", "evidence_url", "quote", "read"]
_OFFICE_LINK = re.compile(r"contact|office|bureau|location|emplacement|nous-joindre|joindre|coordonn|about|a-propos|propos|where|trouver|payment|paiement|invoice|facture", re.I)


def agent_sites(a):
    """The register names the agent of record with its address and no website. A firm's site is where it says how its invoices are paid (the
    owner's rule: on invoice, by bank transfer), so the vendor reader needs it. A candidate site (tools/data/tm_agent_site_candidates.csv:
    the register's own spelling of the firm, a site) is accepted only when a page of that site prints a postal code the register gives for
    that firm; the page and the words around the postal code are kept. A candidate that prints none of them is not used."""
    import ap_crawler as C
    import html as _html
    import urllib.parse
    cand = {}
    for r in csv.DictReader(open(AGENT_CAND, encoding="utf-8", newline="")):
        cand[nkey(r["agent_name"])] = (r["agent_name"], r["site"].strip())
    pcs, cities = collections.defaultdict(set), collections.defaultdict(set)
    for r in csv.DictReader(open(AGENTS, encoding="utf-8", newline="")):
        if nkey(r["agent_name"]) in cand and pc6(r["postal_code"]):
            pcs[nkey(r["agent_name"])].add(pc6(r["postal_code"]))
            city = nkey((r["address"] or "").rstrip(", ").rsplit(",", 1)[-1])
            if len(city) >= 4:
                cities[nkey(r["agent_name"])].add(city.replace(" ", "-"))
    have = {}
    if os.path.exists(AGENT_SITES):
        for r in csv.DictReader(open(AGENT_SITES, encoding="utf-8", newline="")):
            have[(nkey(r["agent_name"]), r["postal_code"])] = r
    n = collections.Counter()
    for k, (name, site) in sorted(cand.items()):
        want = {p for p in pcs.get(k, ()) if (k, p) not in have}
        if not pcs.get(k):
            n["the register has no such agent name with a postal code"] += 1
            continue
        if not want:
            n["already tied"] += 1
            continue
        host = (urllib.parse.urlparse(site).hostname or "").lower()
        dom = C.registrable(host)
        queue, seen, found, alltext = [site], set(), {}, ""
        toks = [t for t in nkey(name).split() if len(t) >= 3 and t not in GENERIC and t not in ("and", "agence", "agency", "intellectual", "property", "services", "law", "group", "trademark",
                                                                                              "lawyers", "avocats", "avocat", "legal")]
        cap = 14 + 4 * min(4, len(want))
        while queue and len(seen) < cap and len(found) < len(want):
            # the page of an office in a city the register names comes first (a firm with twenty offices has one page for each)
            queue.sort(key=lambda q: not any(c in q.lower() or c.replace("-", "") in q.lower() for c in cities.get(k, ())))
            u = queue.pop(0)
            if u in seen or not C.allowed(u):
                continue
            seen.add(u)
            st, ct, data, final = C.fetch(u)
            time.sleep(1.0)
            if st != 200 or not data or data[:5] == b"%PDF-":
                continue
            raw = _html.unescape(data.decode("utf-8", "replace"))
            text = re.sub(r"\s+", " ", C.visible(C.quote_attrs(raw)))
            tm_ = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
            alltext += " " + nkey((tm_.group(1) if tm_ else "") + " " + text[:200000])
            if len(seen) == 1 and final:
                fh = (urllib.parse.urlparse(final).hostname or "").lower()
                if fh and C.registrable(fh) != dom:
                    dom, host = C.registrable(fh), fh  # the firm's site moved to another name of its own: the pages are read there
            for p in want - set(found):
                m = re.search(r"(?<![A-Za-z0-9])%s[ \u00a0-]?%s(?![A-Za-z0-9])" % (p[:3], p[3:]), text, re.I)
                if m:
                    found[p] = (final or u, text[max(0, m.start() - 150): m.end() + 20].strip()[:290])
            base = final or u
            for m in re.finditer(r'href="([^"#]+)"[^>]*>(.*?)</a>', raw, re.S | re.I):
                link = urllib.parse.urljoin(base, m.group(1).strip())
                h2 = (urllib.parse.urlparse(link).hostname or "").lower()
                if link.startswith("http") and C.registrable(h2) == dom and _OFFICE_LINK.search(m.group(1) + " " + re.sub(r"<[^>]+>", " ", m.group(2))) and link not in seen and link not in queue and len(queue) < 40:
                    queue.append(link)
        # the postal code of an office tower is shared by its tenants: the site must print the firm's own name as well (every word of it that is a name)
        named = bool(toks) and all((" " + t + " ") in (alltext + " ") for t in toks)
        if found and not named:
            n["the site prints the postal code but not the firm's name: not tied"] += 1
            print("  %-52s %-28s NOT tied: the postal code is on the site, the name (%s) is not" % (name[:52], host, " ".join(toks)), flush=True)
            continue
        for p, (url, quote) in found.items():
            have[(k, p)] = {"agent_name": name, "postal_code": p, "site": "https://%s/" % host, "evidence_url": url, "quote": quote, "read": TODAY}
        n["tied now" if found else "the candidate site prints none of the register's postal codes for the firm"] += 1
        print("  %-52s %-28s %s" % (name[:52], host, ("%d of %d postal codes on its pages" % (len(found), len(want))) if found else "NOT tied (%d pages read)" % len(seen)), flush=True)
    with open(AGENT_SITES, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=AGENT_SITE_COLS, lineterminator="\n")
        w.writeheader()
        for key in sorted(have):
            w.writerow({c: have[key].get(c, "") for c in AGENT_SITE_COLS})
    print("agent firms' own sites: %d (firm, postal code) pairs tied to a site, %d firms; this run: %s" % (len(have), len({k for k, _ in have}), dict(n)))


def agent_site_table():
    """{name key: (site, evidence)} — a firm whose site prints one of its register addresses is that firm at all of them (the register's spelling of the firm is the key)"""
    out = {}
    if os.path.exists(AGENT_SITES):
        for r in csv.DictReader(open(AGENT_SITES, encoding="utf-8", newline="")):
            out.setdefault(nkey(r["agent_name"]), (r["site"], "the firm's own site prints the register's address for it: “%s” (%s, read %s)" % (r["quote"][:200], r["evidence_url"], r["read"])))
    return out


# ------------------------------------------------------------------------------------------------------------------- leads
def leads(a):
    import lead_store as LS
    owners = {}
    want = {m["owner_key"] for m in csv.DictReader(open(MATCHES, encoding="utf-8", newline=""))}
    for path in (OWN_CA, OWN_XX):  # an owner abroad is delivered the same way: the register names it, its address, and the Canadian agent it appointed
        with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r["owner_key"] in want:
                    owners[r["owner_key"]] = r
    prev, pdet = LS.load(exclude=("tm", a.stamp))
    snap = LS.snapshot(prev, pdet)
    mine = {k for k, d in pdet.items() if d.get("platform") == "tm_register"}
    kept, n_agent, n_office = set(), 0, 0
    agsite = agent_site_table()
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
                     "vendor_site": agsite.get(nkey(o["agent_name"]), ("", ""))[0] if with_agent else OFFICE["site"],
                     "vendor_site_basis": agsite.get(nkey(o["agent_name"]), ("", ""))[1] if with_agent else "",
                     "member_address_quote": ("%s %s" % (o["address"], o["postal_code"])).strip(),
                     "register_label": "the Canadian trademarks register of the Canadian Intellectual Property Office, which names as agent of record" if with_agent else "the Canadian trademarks register published by",
                     "tm_relationship": "agent of record" if with_agent else "registration",
                     "tm_agent_of_record": o["agent_name"], "tm_agent_number": o["agent_number"], "tm_agent_address": o["agent_address"], "tm_marks_in_force": int(o["marks_in_force"] or 0),
                     "tm_marks_pending": int(o["marks_pending"] or 0), "tm_marks_with_this_agent": int(o["marks_with_this_agent"] or 0), "tm_examples": o["examples"],
                     "tm_first_registered": o["first_registered"], "tm_latest_renewal_due": o["latest_renewal_due"], "tm_extract": SNAP_DATE,
                     "buyer_register": {"legal_name": o["owner_name"], "trade_names": [], "registry_id": "", "legal_form": "", "phone": "",
                                        "address": ("%s %s" % (o["address"], o["postal_code"])).strip(),
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


# ---- owners abroad: the website an Overture Maps place lists for the owner's name at its postal code (2026-11-12) ----------------------------
# Guessing a domain name from the owner's name found 2,572 sites for 44,294 owners in the United States (5.8 %). The Overture Maps places
# (open data, a release a month) list, for tens of millions of businesses, a name, an address and a website — published, not guessed. An owner
# whose name (legal forms left out) and postal code (US ZIP, GB postcode, AU postcode) are those of a place gets that place's website as the
# FIRST site to read; the site counts only when its own pages tie it to the owner by the same tests as before (sites --abroad --overture).
OVT_SITES = os.path.join(DIR, "tm_overture_sites.csv")
# 2026-11-13: the websites Overture places list AT the owner's own address (street number, street and ZIP code; a UK postcode), under any name
# (tools/overture_names.py addr) — read like the name candidates; a site counts only when its own pages state the owner's name
OVT_ADDR = os.path.join(DIR, "tm_overture_addr_sites.csv")
OVT_ADDR_CA = os.path.join(DIR, "tm_overture_addr_ca_sites.csv")  # 2026-11-13: owners in Canada, places at the register's full postal code
# 2026-11-13: the website the Research Organization Registry (ROR, open data, CC0) lists for an organisation of the owner's very name in its country
# (tools/ror_sites.py) — read like the Overture candidates; a site counts only when its own pages state the owner's name (with an address of the
# owner's state or country, or a Canadian postal code for an owner in Canada), or print its full legal name on the site's own legal page
ROR_SITES = os.path.join(DIR, "tm_ror_sites.csv")
WD_SITES = os.path.join(DIR, "tm_wd_sites.csv")  # 2026-11-13: Wikidata's official website (P856) of an item of the owner's very name in its country (tools/wikidata_sites.py)
REG_SRC = {"ror": ("the Research Organization Registry lists this website for", "ror2", "the Research Organization Registry"),
           "wikidata": ("Wikidata gives this website as the official website of", "wd", "Wikidata")}
OVT_BUCKET = "https://overturemaps-us-west-2.s3.amazonaws.com"
_SQL_FORMS = (r"\b(inc|incorporated|incorporee|ltd|ltee|limited|limitee|corp|corporation|co|company|compagnie|cie|llc|llp|lp|sencrl|senc|srl|enr|reg|regd|ulc|plc|"
              r"gmbh|sa|sas|ag|bv|nv|pty|the|la|le|les|l)\b")  # FORM, as RE2 reads it (DuckDB string literals keep the backslash)


def overture_sites(a):
    """owners abroad (United States, United Kingdom, Australia) x the Overture Maps places of those countries that list a website: the same
    name (legal forms left out) at the same postal code, or failing that in the same state -> data/incoming/claude/tm/tm_overture_sites.csv.
    a.dir: a glob of local parquet files with the columns name, website, postcode, region, country, id (tests), else the newest release."""
    import duckdb
    import ap_crawler as C
    owners = {}
    with gzip.open(OWN_XX, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["country"] not in ABROAD or not (is_org(r["owner_name"]) or (r["country"] in EU_CODE and re.search(EU_FORMS, nkey_raw(r["owner_name"])))):
                continue
            if not (int(r["marks_in_force"] or 0) or (r["agent_name"] and int(r["marks_with_this_agent"] or 0))):
                continue
            code, st = place_abroad(r["address"], r["country"])
            nk = nkey_x(r["owner_name"])
            if nk and len(nk) >= 4 and (code or (st and r["country"] in ("US", "AU"))):
                owners[r["owner_key"]] = (r["country"], nk, code, st)
    con = duckdb.connect()
    con.execute("SET enable_progress_bar=false;")
    con.execute("CREATE TABLE own (k VARCHAR, cc VARCHAR, nk VARCHAR, code VARCHAR, st VARCHAR)")
    con.executemany("INSERT INTO own VALUES (?, ?, ?, ?, ?)", [(k, *v) for k, v in owners.items()])
    if a.dir and a.dir != "shards" and glob.glob(a.dir):
        src, release = "read_parquet('%s')" % a.dir, (getattr(a, "release", "") or "a local copy")
        cols = "name, website, postcode, region, country, id"
    else:
        import urllib.request
        ls = lambda prefix: urllib.request.urlopen(urllib.request.Request("%s/?list-type=2&prefix=%s&delimiter=/" % (OVT_BUCKET, prefix), headers={"User-Agent": UA}), timeout=120).read().decode()
        rel = sorted(re.findall(r"<Prefix>(release/[0-9]{4}-[0-9]{2}-[0-9]{2}\.[0-9]+/)</Prefix>", ls("release/")))[-1]
        keys = re.findall(r"<Key>([^<]+\.parquet)</Key>", ls(rel + "theme=places/type=place/"))
        con.execute("INSTALL httpfs; LOAD httpfs;")
        src = "read_parquet([%s])" % ", ".join("'%s/%s'" % (OVT_BUCKET, k_) for k_ in keys)
        release = rel.rstrip("/").rsplit("/", 1)[-1]
        cols = 'names."primary" AS name, websites[1] AS website, addresses[1].postcode AS postcode, addresses[1].region AS region, addresses[1].country AS country, id'
    t0 = time.time()
    norm_sql = ("trim(regexp_replace(regexp_replace(regexp_replace(regexp_replace(replace(lower(strip_accents(coalesce(p.name, ''))), '&', ' and '), '[^a-z0-9 ]+', ' ', 'g'), "
                "'%s', ' ', 'g'), '%s', ' ', 'g'), '\\s+', ' ', 'g'))" % (_SQL_FORMS, EU_FORMS))
    ccs = ", ".join("'%s'" % c_ for c_ in sorted(ABROAD))
    rows = con.execute("""WITH p AS (SELECT %s FROM %s WHERE websites IS NOT NULL AND len(websites) > 0 AND addresses[1].country IN (%s))
                          SELECT o.k, o.cc, o.code, o.st, p.name, p.website, p.postcode, p.region, p.id FROM p JOIN own o ON o.cc = p.country AND o.nk = %s""".replace(
        "websites IS NOT NULL AND len(websites) > 0 AND addresses[1].country", "website IS NOT NULL AND country" if src.startswith("read_parquet('") else "websites IS NOT NULL AND len(websites) > 0 AND addresses[1].country") % (
        cols, src, ccs, norm_sql)).fetchall()
    print("Overture places with the name of an owner abroad: %d (%.0f s, %s)" % (len(rows), time.time() - t0, release), flush=True)
    best, n = {}, collections.Counter()
    for k, cc, code, st, name, web, pcode, region, pid in rows:
        host = (re.sub(r"^https?://", "", (web or "").strip().lower()).split("/")[0].split(":")[0])
        host = host[4:] if host.startswith("www.") else host
        if not host or "." not in host or nkey_x(name) != owners[k][1]:
            continue
        d = C.registrable(host)
        pc = re.sub(r"[^A-Z0-9]", "", (pcode or "").upper())
        pc = pc[:5] if cc == "US" else re.sub(r"^(?:CH|DK|SE|D|F|I|E|A|B)(?=\d)", "", pc) if cc in EU_CODE else pc
        reg = (region or "").upper().split("-")[-1]
        rank = 0 if (code and pc == code) else 1 if (st and reg == st) else 9
        if rank == 9:
            continue
        cur = best.setdefault(k, {})
        if d not in cur or rank < cur[d][0]:
            cur[d] = (rank, name, pcode or "", pid or "")
    with open(OVT_SITES, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["owner_key", "site", "how", "place_name", "place_postcode", "place_id", "release"])
        for k in sorted(best):
            for d, (rank, name, pcode, pid) in sorted(best[k].items(), key=lambda kv: kv[1][0])[:3]:
                w.writerow([k, d, ("the same name at the same %s" % ("ZIP code" if owners[k][0] == "US" else "postcode" if owners[k][0] in ("GB", "AU") else "postal code")) if rank == 0 else "the same name in the same state",
                            name, pcode, pid, release])
                n[rank] += 1
    print("owners abroad with a website an Overture place lists for their name: %d (%d sites at the same postal code, %d in the same state) -> %s" % (
        len(best), n[0], n[1], OVT_SITES), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "match", "leads", "sites", "merge-sites", "agent-sites", "overture-sites"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--work", default=os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "tm_work"))
    ap.add_argument("--main", default="", help="build: a local copy of the application-main zip (tests)")
    ap.add_argument("--party", default="", help="build: a local copy of the interested-party zip (tests)")
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    ap.add_argument("--abroad", action="store_true", help="sites: the owners outside Canada (the United States, the United Kingdom, Australia and ten European countries: ABROAD) instead of the owners in Canada")
    ap.add_argument("--release", default="", help="overture-sites with local parquet files: the Overture release they were taken from")
    ap.add_argument("--overture", action="store_true", help="sites --abroad: the owners for whom an Overture Maps place lists a website (tm_overture_sites.csv), that site read first")
    ap.add_argument("--legal", action="store_true", help="sites --abroad --overture: read again the listed sites of owners read before, with the legal-page test (mark 'legal')")
    ap.add_argument("--clearbit", action="store_true", help="sites --abroad: also the domains the company-name autocomplete gives under the owner's very name (owners looked for before included)")
    ap.add_argument("--ror", action="store_true", help="sites: only the owners for whom the Research Organization Registry lists a website under their name in their country (tm_ror_sites.csv), that site read first")
    a = ap.parse_args()
    {"build": build, "match": match, "leads": leads, "sites": sites, "merge-sites": merge_sites, "agent-sites": agent_sites, "overture-sites": overture_sites}[a.cmd](a)


if __name__ == "__main__":
    main()

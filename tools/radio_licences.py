#!/usr/bin/env python3
"""ISED's radio licensees -> relationship leads (cloud; no AI, no search engine).

Every holder of a radio licence in Canada is invoiced by Innovation, Science and Economic Development Canada (ISED) every year:
"Renewal of renewable radio licences: The annual fee for the renewal of a radio licence is payable before the radio licence expires on March 31 of
each year" and the fees "are used to calculate licence renewal invoices" (RIC-42, Guide for Calculating Radio Licence Fees, Issue 16, April 2026);
"Innovation, Science and Economic Development Canada will calculate the amount on your invoice using the individually adjusted fee rates" (ISED's
questions and answers on the yearly adjustment). The invoice is paid by wire transfer or direct deposit to the Receiver General for Canada, by cheque,
or online (ISED's "Pay online" page). ISED publishes every month, as open data, the Spectrum Management System's authorization data extract: each
frequency record of every granted or pending authorization, with the licensee's name, its address, its client account number, the authorization
number, its service, its status, its in-service date and its stations. A licensee with a granted, fee-paying authorization in this month's extract
is therefore a current, yearly, invoiced relationship between a named organisation and a Canadian public body, published by the body that bills.

What a row needs beyond the register is the licensee's role mailbox, read on the licensee's OWN site by the ordinary mailbox crawl
(tools/lead_crawl.py reads lead_shards/). The site is tied the way tools/hc_registers.py ties a company: a site on file that prints the licensee's
postal code under a name that agrees, else the company-name autocomplete under the licensee's very name, kept only when the site's own home page
carries that name. Natural persons are left out (organisations only), and so are federal departments (they settle with ISED between departments,
not by invoice). The register's account number is ISED's own published client number; no e-mail is read from the register (it has none).

  pull --work W            the extract (one zip of ~64 MB; www.ic.gc.ca asks a 20-second crawl delay: one request) when ISED has a newer one
  build --work W           -> data/incoming/claude/radio/radio_licensees.csv.gz (one line per licensee account that is an organisation)
  sites --minutes M        each licensee's own site -> radio_sites.csv (+ radio_sites_done.tsv: names the autocomplete was asked)
  leads --stamp S          -> lead_shards/leads_radio_S.gz + details_radio_S.gz (new leads only)
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, sys, threading, time, urllib.parse, urllib.request, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hc_registers as HR  # noqa: E402  (the site finder: names, postal codes, the autocomplete, the home-page check)

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "radio")
SHARDS = os.path.join(INC, "lead_shards")
UA = HR.UA
TODAY = time.strftime("%Y-%m-%d")
READ = "2026-11-12"
EXTRACT = "https://www.ic.gc.ca/engineering/SMS_TAFL_Files/TAFL_LTAF.zip"
EXTRACT_PAGE = "https://open.canada.ca/data/en/dataset/508040d7-6fa9-46e4-afbc-aa61f3ca317e"
RIC42 = ("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/"
         "ric-42-guide-calculating-radio-licence-fees")
RIC42_TABLES = ("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/sites/default/files/documents/"
                "DGSO-DOS%202026-2027%20RIC-42%20Radio%20Licence%20Fees.xlsx")
QA = ("https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/licence-fees/"
      "annual-adjustments-spectrum-and-telecommunications-fees-questions-and-answers")
PAY = "https://ised-isde.canada.ca/site/spectrum-management-system/en/pay-online"
SMS_SITE = "https://ised-isde.canada.ca/site/spectrum-management-system/en"
ISED = "Innovation, Science and Economic Development Canada"
# ISED's own sentences, as its pages print them (read 2026-11-12)
RENEW_Q = ("Renewal of renewable radio licences: The annual fee for the renewal of a radio licence is payable before the radio licence expires on March 31 "
           "of each year.")
INV2_Q = "They are used to calculate licence renewal invoices and for any new or amended licences issued throughout the fiscal year."
INVOICE_Q = "Innovation, Science and Economic Development Canada will calculate the amount on your invoice using the individually adjusted fee rates"
WIRE_Q = ("Other payment options Wire transfer Use the following information to complete a wire transfer payment: Bank Name : The Bank of Nova Scotia "
          "4715 Tahoe Blvd, Mississauga ON L4W 0B4")
CHEQUE_Q = ("For payment by cheque or money order made payable to the Receiver General for Canada, include your account number and the invoice number, both "
            "available on your invoice or on your email notification")
ADDRESS = "ISED – Spectrum Revenue Centre, 235 Queen Street, Room 643A, Ottawa ON K1A 0H5"
ADDRESS_Q = "By courier to the following address: ISED – Spectrum Revenue Centre 235 Queen Street, Room 643A Ottawa ON K1A 0H5"
# the lowest yearly fee of ISED's tables (RIC-42 annexes A and D, effective April 1, 2026) for each kind of station, as the tables' rows print them
FEE = {"lm_fixed": (66.40, "land mobile fixed station (the fee outside a metropolitan area; C$145.32 inside one)", "FIXED Land Mobile – Other Area TX or RX (63, 64) 66.4 5.51"),
       "fixed_other": (51.36, "fixed station of the aeronautical, maritime or another service", "FIXED Other Fixed Stations Not Otherwise described (72) 51.36 4.25"),
       "mobile": (51.36, "mobile or transportable station", "MOBILE All Other Mobile Stations (60 (3) (4) (5) (6)) 51.36 4.25"),
       "craft": (45.09, "aircraft or ship station", "MOBILE Aircraft / Ship 60(1)) 45.09 3.76"),
       "p2p": (42.14, "fixed point-to-point station (at least the remote-zone minimum; per MHz of spectrum above it)", "Minimum fees 42.14 3.52 (Table D3: Remote fees in the fixed point-to-point service)")}
# Table D3 (remote zone), C$ a year per MHz of assigned spectrum: the lowest of the three zones
P2P = [(890, 1655.72), (960, 83.09), (4200, 27.09), (8500, 20.48), (15350, 14.44), (24250, 9.63), (52600, 6.02), (10 ** 9, 0.31)]
FIXED_TYPES = {"1", "6", "8", "10", "11", "13", "15", "17", "18"}
CRAFT_TYPES = {"4", "5"}
NO_FEE = {"1", "2", "3", "5", "6", "9"}  # station cost category: no fee, domestic ghost, foreign, passive repeater, passive reflector, not licensed
GRANTED = {"G", "1", "11", "3"}
SERVICES = {"1": "broadcasting", "2": "fixed", "3": "land mobile", "5": "maritime", "8": "aeronautical", "9": "satellite (earth stations)",
            "85": "spectrum licence", "35": "other"}
ORG = re.compile(r"\b(inc|incorporated|ltd|ltée|ltee|limited|limitée|limitee|corp|corporation|co|company|compagnie|cie|société|societe|s\.?e\.?n\.?c|"
                 r"llp|lp|ulc|group|groupe|association|assn|city|ville|town|village|township|municipal|municipalité|municipalite|municipality|county|comté|"
                 r"district|region|régie|regie|regional|régional|hydro|energy|énergie|energie|power|électrique|electrique|electric|services|service|systems|"
                 r"solutions|communications|telecom|télécom|wireless|network|networks|réseau|reseau|radio|broadcasting|university|université|universite|"
                 r"college|collège|cegep|cégep|school|école|ecole|academy|académie|institute|institut|board|commission|authority|autorité|police|fire|"
                 r"incendie|pompiers|ambulance|paramedic|hospital|hôpital|hopital|health|santé|sante|clinic|clinique|church|église|eglise|parish|paroisse|"
                 r"diocese|diocèse|club|society|société|foundation|fondation|cooperative|coopérative|cooperative|co-op|coop|caisse|credit union|bank|"
                 r"enterprises|entreprises|industries|holdings|transport|transports|trucking|camionnage|transit|bus|taxi|cab|towing|remorquage|"
                 r"construction|contracting|paving|excavation|excavating|ready-mix|concrete|béton|beton|aggregates|gravel|sand|mining|mines|minière|"
                 r"miniere|resources|ressources|farms|farm|ferme|ranch|ranches|feedlot|dairy|orchards|vineyard|winery|airport|aéroport|aeroport|airlines|"
                 r"aviation|air|helicopters|hélicoptères|marine|ferries|shipping|navigation|rail|railway|pipeline|gas|oil|petroleum|energy|forest|forestry|"
                 r"lumber|logging|sawmill|timber|logistics|security|sécurité|securite|motors|equipment|équipement|technologies|technology|tech|"
                 r"manufacturing|fabrication|mill|mills|plant|works|foods|aliments|fisheries|pêcheries|pecheries|seafood|hotel|hôtel|inn|resort|lodge|"
                 r"camp|camps|golf|ski|marina|provincial park|parc|centre|center|museum|musée|library|bibliothèque|gallery|theatre|théâtre|festival|arena|"
                 r"stadium|casino|raceway|speedway|nation|first nations|band|bande|council|conseil|tribal|métis|metis|inuit|government|gouvernement|"
                 r"ministry|ministère|ministere|department|agency|agence|office|bureau|province|provincial|federation|fédération|union|syndicat|league|"
                 r"ligue|alliance|partners|partnership|associates|consulting|consultants|engineering|ingénierie|ingenierie|environmental|"
                 r"environnement|waste|recycling|water|eau|utilities|utility|cable|câble|internet|media|médias|news|productions|studios|events|"
                 r"rentals|location|supply|supplies|distribution|distributors|wholesale|grossiste|retail|stores|magasin|pharmacy|pharmacie|dental|"
                 r"dentaire|veterinary|vétérinaire|care|soins|manor|villa|residence|résidence|community|communauté|communaute|cemetery|cimetière|"
                 r"funeral|funéraire|ministries|mission|camp|scouts|guides|legion|légion|fair|exhibition|agricultural|agricole|grain|elevator|seeds)\b",
                 re.I)
FEDERAL = re.compile(r"\b(government of canada|gouvernement du canada|her majesty|his majesty|sa majest[ée]|the crown in right of canada|royal canadian mounted police|"
                     r"rcmp|gendarmerie royale|national defence|d[ée]fense nationale|department of national|canadian forces|forces canadiennes|parks canada|"
                     r"parcs canada|canadian coast guard|garde c[ôo]ti[èe]re|fisheries and oceans|p[êe]ches et oc[ée]ans|environment (and climate change )?canada|"
                     r"environnement (et changement climatique )?canada|natural resources canada|ressources naturelles canada|transport canada|transports canada|"
                     r"public safety canada|s[ée]curit[ée] publique canada|correctional service|service correctionnel|canada border services|"
                     r"agence des services frontaliers|health canada|sant[ée] canada|indigenous services canada|services aux autochtones canada|"
                     r"industry canada|industrie canada|innovation, science|public services and procurement|services publics et approvisionnement|"
                     r"shared services canada|services partag[ée]s canada|canadian space agency|agence spatiale canadienne|statistics canada|"
                     r"agriculture and agri-food canada|agriculture et agroalimentaire canada|global affairs canada|affaires mondiales canada|"
                     r"department of fisheries|ministère des pêches|employment and social development canada|national research council|"
                     r"conseil national de recherches|canadian food inspection agency|agence canadienne d.inspection des aliments)\b", re.I)
PERSON = re.compile(r"^(?:(?:[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\-]+|[A-Z]\.?)\s+){1,3}[A-ZÀ-Ý][A-Za-zÀ-ÿ'’\-]+$")
COMPANIES = os.path.join(DIR, "radio_licensees.csv.gz")
SITES = os.path.join(DIR, "radio_sites.csv")
SDONE = os.path.join(DIR, "radio_sites_done.tsv")
OVT_ADDR = os.path.join(INC, "overture", "radio_addr_candidates.csv")  # 2026-11-13: places at the licensee's own postal code (tools/overture_names.py addr)
ADONE = os.path.join(DIR, "radio_addr_done.tsv")
INFO = os.path.join(DIR, "extract_info.json")
COLS = ["key", "account", "name", "address", "postal_code", "province", "authorizations", "auth_examples", "stations", "fee_floor", "fee_parts",
        "services", "first_in_service", "last_in_service", "examples", "extract_date", "fleet_not_counted"]


def is_org(name):
    n = " ".join((name or "").split())
    if not n or FEDERAL.search(n):
        return False
    if ORG.search(n):
        return True
    return False  # neither a word of an organisation nor a legal form: left out (a person's name, or a name that says nothing)


def p2p_fee(freq_mhz, bw_khz):
    try:
        f, b = float(freq_mhz), float(bw_khz) / 1000.0
    except (TypeError, ValueError):
        return FEE["p2p"][0]
    rate = next(r for top, r in P2P if f <= top)
    return max(FEE["p2p"][0], rate * b)


def head_last_modified():
    req = urllib.request.Request(EXTRACT, method="HEAD", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.headers.get("Last-Modified") or ""


def cmd_pull(a):
    os.makedirs(a.work, exist_ok=True)
    info = json.load(open(INFO)) if os.path.exists(INFO) else {}
    try:
        lm = head_last_modified()
    except Exception as e:
        if os.path.exists(COMPANIES) and not a.force:
            print("the extract's date could not be read (%s): the list on file is kept" % str(e)[:120])
            return
        raise
    if lm and lm == info.get("last_modified") and os.path.exists(COMPANIES) and not a.force:
        print("extract unchanged since %s: not pulled" % lm)
        return
    time.sleep(21)  # www.ic.gc.ca: "Crawl-delay: 20"
    req = urllib.request.Request(EXTRACT, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as r, open(os.path.join(a.work, "TAFL_LTAF.zip"), "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    with open(os.path.join(a.work, "last_modified.txt"), "w") as f:
        f.write(lm)
    print("pulled the extract (%s)" % lm)


def cmd_build(a):
    z = os.path.join(a.work, "TAFL_LTAF.zip")
    if not os.path.exists(z):
        print("no new extract in %s: nothing to build" % a.work)
        return
    lm = open(os.path.join(a.work, "last_modified.txt")).read().strip() if os.path.exists(os.path.join(a.work, "last_modified.txt")) else ""
    zf = zipfile.ZipFile(z)
    name = [n for n in zf.namelist() if n.lower().endswith(".csv")][0]
    ext_date = "%04d-%02d-%02d" % zf.getinfo(name).date_time[:3]
    acc = {}
    cnt = collections.Counter()
    import io
    with zf.open(name) as raw:
        for row in csv.reader(io.TextIOWrapper(raw, encoding="utf-8-sig", errors="replace", newline="")):
            if len(row) < 57:
                continue
            cnt["frequency records"] += 1
            if row[51] not in GRANTED:
                continue
            if row[36] in NO_FEE:
                cnt["no-fee station"] += 1
                continue
            a_ = row[53].strip()
            if not a_:
                continue
            d = acc.get(a_)
            if d is None:
                d = acc[a_] = {"name": " ".join(row[54].split()), "address": " ".join(row[55].split()), "auth": [], "auth_set": set(), "stations": 0,
                               "fee": 0.0, "parts": collections.Counter(), "svc": collections.Counter(), "prov": collections.Counter(),
                               "first": "", "last": "", "examples": [], "fleets": {}, "fixed": set()}
            if row[47] not in d["auth_set"]:
                d["auth_set"].add(row[47]); d["auth"].append(row[47])
            d["svc"][row[48]] += 1
            d["prov"][row[39]] += 1
            if row[52] and (not d["first"] or row[52] < d["first"]):
                d["first"] = row[52]
            if row[52] and row[52] > d["last"]:
                d["last"] = row[52]
            try:
                k = max(1, int(float(row[37] or 1)))
            except ValueError:
                k = 1
            if len(d["examples"]) < 3 and row[31] and row[31][:80] not in d["examples"]:
                d["examples"].append(row[31][:80])
            svc, typ = row[48], row[34]
            if svc in ("3", "5", "8") and typ not in FIXED_TYPES:
                # a fleet (mobiles, handhelds, transportables, aircraft, ships): one authorization lists it once per frequency — counted once, at its
                # largest record, and a record of more than 1,000 identical stations (meters, province-wide fleets) is not counted at all: the
                # fee rule of so large a fleet is not read here, and leaving stations out keeps "at least" true
                part = "craft" if typ in CRAFT_TYPES else "mobile"
                if k > 1000:
                    d["fleet_not_counted"] = max(d.get("fleet_not_counted", 0), k)
                    continue
                fk = (row[47], typ, part)
                d["fleets"][fk] = max(d["fleets"].get(fk, 0), k)
                continue
            sid = (row[47], row[33], row[31], row[40], row[41], typ)
            if sid in d["fixed"]:
                continue  # one station, several frequencies: one fee (a point-to-point station's other channels would add to it: not counted)
            d["fixed"].add(sid)
            k = 1 if k > 1000 else k
            if svc == "3":
                part, fee = "lm_fixed", FEE["lm_fixed"][0]
            elif svc in ("5", "8"):
                part, fee = "fixed_other", FEE["fixed_other"][0]
            elif svc == "2":
                part, fee = "p2p", p2p_fee(row[1], row[10])
            else:
                part, fee = "other:" + svc, 0.0
            d["parts"][part] += k
            d["stations"] += k
            d["fee"] += fee * k
    for a_, d in acc.items():
        for (au, typ, part), k in d["fleets"].items():
            d["parts"][part] += k
            d["stations"] += k
            d["fee"] += FEE[part][0] * k
    out, why = [], collections.Counter()
    for a_, d in acc.items():
        if d["fee"] <= 0:
            why["only broadcasting, spectrum-licence or earth-station authorizations (billed under other fee orders, not read): left out"] += 1
            continue
        if not is_org(d["name"]):
            why["a person's name, a federal department or no word of an organisation: left out"] += 1
            continue
        m = re.search(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b", d["address"].upper())
        out.append({"key": "radio:" + a_, "account": a_, "name": d["name"], "address": d["address"], "postal_code": (m.group(1) + " " + m.group(2)) if m else "",
                    "province": d["prov"].most_common(1)[0][0] if d["prov"] else "", "authorizations": len(d["auth"]), "auth_examples": " ".join(d["auth"][:3]),
                    "stations": d["stations"], "fee_floor": "%.2f" % d["fee"], "fee_parts": json.dumps(dict(d["parts"]), sort_keys=True),
                    "services": json.dumps(dict(d["svc"]), sort_keys=True), "first_in_service": d["first"], "last_in_service": d["last"],
                    "examples": " | ".join(d["examples"]), "extract_date": ext_date, "fleet_not_counted": d.get("fleet_not_counted", 0)})
        why["organisation kept"] += 1
    os.makedirs(DIR, exist_ok=True)
    out.sort(key=lambda o: -float(o["fee_floor"]))
    with gzip.open(COMPANIES, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out)
    json.dump({"last_modified": lm, "extract_date": ext_date, "built": TODAY, "accounts": len(acc), "kept": len(out)}, open(INFO, "w"), indent=1)
    print("extract of %s: %d frequency records, %d licensee accounts with a granted, fee-paying authorization; %s" % (ext_date, cnt["frequency records"], len(acc), dict(why)))


def companies():
    with gzip.open(COMPANIES, "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


def cmd_sites(a):
    import queue
    os.makedirs(DIR, exist_ok=True)
    cos = companies()
    have = sites_on_file()
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=HR.SITE_COLS)
    if new:
        w.writeheader()
    n_file = 0
    for k, r in HR.tie_on_file([o for o in cos if o["key"] not in have]).items():
        w.writerow(r); have[k] = r; n_file += 1
    f.flush()
    # 2026-11-13: the websites an Overture place at the licensee's own postal code lists, kept on its name on the home page or its full legal
    # name on the site's own legal page (the postal code only when the place bears the licensee's name) — tools/hc_registers.py addr_pass
    HR.addr_pass(cos, have, w, f, getattr(a, "addr_minutes", 30), a.threads, ovt_addr=OVT_ADDR, adone=ADONE)
    done = set()
    if os.path.exists(SDONE):
        done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")}
    todo = [o for o in cos if o["key"] not in have and o["key"] not in done]
    t_end = time.time() + 60 * a.minutes
    lock, q, cnt = threading.Lock(), queue.Queue(maxsize=64), collections.Counter()
    dn = open(SDONE, "a", encoding="utf-8")

    def producer():  # the autocomplete, one request a second
        for o in todo:
            if time.time() > t_end:
                break
            n = HR.core(o["name"])
            if len(n) < 3 or (len(n.split()) == 1 and len(n) < 5):
                with lock:
                    dn.write("%s\t\n" % o["key"]); dn.flush()
                continue
            cands = [((s_.get("domain") or "").lower().strip(), HR.core(s_.get("name") or "")) for s_ in (HR.suggest(n) or [])[:5]]
            # a licensee whose name says Canada (Bell Canada, Rogers Communications Canada) is the Canadian entity: only a .ca site under its very name
            ca_only = bool(re.search(r"\bcanad", o["name"], re.I))
            q.put((o, n, [d for d, sn in cands if d and not HR.BAD.search(d) and sn == n and (not ca_only or d.endswith(".ca")) and HR.domain_fits(d, n, "canada")]))
            cnt["looked up"] += 1
        for _ in range(a.threads):
            q.put(None)

    def worker():  # each candidate's own home page (the reader's own politeness per host)
        while True:
            it = q.get()
            if it is None:
                return
            o, n, doms = it
            hit, said = "", ""
            for d in doms:
                try:
                    said = HR.home_says(d, n)
                except Exception:
                    said = ""
                if said:
                    hit = d
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit)); dn.flush()
                if hit:
                    w.writerow({"key": o["key"], "site": "https://%s/" % hit, "read": TODAY, "quote": said,
                                "tied_by": "the company-name autocomplete (Clearbit) proposes %s under the licensee's very name (%s, legal forms aside), and the site's own home page carries it: “%s”" % (hit, n, said)})
                    f.flush(); cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(a.threads)]
    for t in ts:
        t.start()
    producer()
    for t in ts:
        t.join()
    dn.close(); f.close()
    print("sites: %d on file before the autocomplete (+%d from sites on file); the autocomplete: %d names looked up, %d sites tied"
          % (len(have), n_file, cnt["looked up"], cnt["found"]), flush=True)


def money(v):
    return "C$" + format(v, ",.2f")


def lead_of(o, s):
    key = "lead:" + hashlib.sha1(("radio|%s" % o["account"]).encode()).hexdigest()[:16]
    parts = json.loads(o["fee_parts"] or "{}")
    svcs = json.loads(o["services"] or "{}")
    floor = float(o["fee_floor"] or 0)
    shown = ["%d × %s (%s)" % (v, money(FEE[p][0]), FEE[p][1]) if p != "p2p" else "%d %s" % (v, FEE[p][1]) for p, v in sorted(parts.items(), key=lambda kv: -kv[1]) if p in FEE]
    other = sorted({SERVICES.get(p.split(":")[1], "other") for p in parts if p.startswith("other:")})
    n_auth, n_st = int(o["authorizations"] or 0), int(o["stations"] or 0)
    what = "%d radio authorization%s (%d station%s counted: %s)" % (n_auth, "" if n_auth == 1 else "s", n_st, "" if n_st == 1 else "s",
                                                          ", ".join(SERVICES.get(k, "other") for k in sorted(svcs, key=lambda k: -svcs[k])))
    unit = max((p for p in parts if p in FEE), key=lambda p: parts[p], default="")
    calc = ""
    if floor > 0:
        calc = ("calculated — at least %s a year: %s — the lowest yearly fees of ISED's tables (RIC-42, annexes A and D, effective April 1, 2026; %s, read %s) for the stations "
                "this licensee holds in ISED's authorization data extract of %s; ISED calculates its invoice station by station and it may be higher (a station in a "
                "metropolitan area or a busier zone pays more)%s"
                % (money(floor), " + ".join(shown), RIC42_TABLES, READ, o["extract_date"],
                   ("; its %s authorizations are billed under their own fee orders and are not counted here" % " and ".join(other)) if other else "")
                + ("; a record of %s identical stations (meters or a province-wide fleet) is not counted either" % format(int(o.get("fleet_not_counted") or 0), ",")
                   if int(o.get("fleet_not_counted") or 0) else ""))
    s = dict(s, tied_by=HR.no_mail(s.get("tied_by")), quote=HR.no_mail(s.get("quote")))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": ISED,
           "canada_field_value": "membership / statutory fee relationship: licence holder of the Canadian body (%s)=%s (as printed on %s, read %s); ISED: “%s” (%s)"
                                 % (ISED, ADDRESS, PAY, READ, RENEW_Q, RIC42),
           "evidence_dataset": EXTRACT_PAGE, "latest_record_date": o["extract_date"]}
    det = {"key": key, "platform": "radio_register", "record_url": EXTRACT_PAGE, "vendor": ISED, "record_date": o["extract_date"],
           "start": o.get("first_in_service") or "", "end": "", "reference": o["auth_examples"].split(" ")[0] if o["auth_examples"] else "",
           "title": "Radio licence(s): %s — e.g. %s" % (what, o["examples"][:160]),
           "vendor_address": "%s (as printed on %s, read %s)" % (ADDRESS_Q, PAY, READ), "vendor_site": SMS_SITE,
           "member_address_quote": o["address"], "register_label": "ISED's Spectrum Management System authorization data extract (each licensee, its address, its authorizations and stations)",
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "ISED client account %s (published in the extract)" % o["account"],
                              "label": "ISED's Spectrum Management System authorization data extract of %s" % o["extract_date"]},
           "radio_account": o["account"], "radio_authorizations": o["auth_examples"], "radio_stations": n_st, "radio_parts": parts, "radio_services": svcs,
           "fee_unit": ("%s a year for each %s (as of April 1, 2026)" % (money(FEE[unit][0]), FEE[unit][1])) if unit else "",
           "fee_unit_basis": ("ISED's fee table (RIC-42, effective April 1, 2026): “%s” (%s, read %s)" % (FEE[unit][2], RIC42_TABLES, READ)) if unit else "",
           "fee_calculated": calc,
           "bill_delivery": "an invoice from ISED every year for the licence year that starts April 1: “%s” “%s” (%s, read %s) — “%s” (%s, read %s)"
                            % (INV2_Q, RENEW_Q, RIC42, READ, INVOICE_Q, QA, READ),
           "bill_terms": "before the licence expires on March 31: “%s” (%s, read %s)" % (RENEW_Q, RIC42, READ),
           "bill_items": "the yearly renewal fee of %s" % what,
           "fee_basis": "%s (%s)" % (RENEW_Q, RIC42), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    cos, sites = companies(), sites_on_file()
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_radio_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    hosts = collections.Counter(urllib.parse.urlparse(s["site"]).hostname for s in sites.values() if s.get("site"))
    rows, dets, by = [], [], collections.Counter()
    for o in cos:
        s = sites.get(o["key"])
        if not s or not s.get("site"):
            continue
        if hosts[urllib.parse.urlparse(s["site"]).hostname] > 3:
            by["site shared by more than three licensees (a group's or a host's site): left out"] += 1
            continue
        row, det = lead_of(o, s)
        if row["buyer_key"] in have:
            continue
        have.add(row["buyer_key"]); rows.append(row); dets.append(det); by["new lead"] += 1
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_radio_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_radio_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("radio licensee leads on file: %d (+%d this run: %s)" % (len(have), len(rows), dict(by)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--work", required=True); p.add_argument("--force", action="store_true")
    p = sub.add_parser("build"); p.add_argument("--work", required=True)
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=60); p.add_argument("--threads", type=int, default=12); p.add_argument("--addr-minutes", type=float, default=30)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""US employers whose benefit plans pay a Canadian company, from the Form 5500 filings the US Department of Labor publishes. No AI.

Every US employee-benefit plan with 100 or more participants files a Form 5500 each year; the Department of Labor (EBSA) publishes every filing
as open data (https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/public-disclosure/foia/form-5500-datasets: one zip a year per
schedule, refreshed every month). Two schedules name a Canadian company that bills the plan's sponsor:
  Schedule A (insurance information): each insurance contract of the plan — the insurer's name, EIN and NAIC code, the contract (policy)
    number, the policy period, the persons covered, the kinds of benefit (life, disability, dental, stop-loss …), the commissions the insurer
    paid on it and, for an experience-rated contract, the premiums it received. SUN LIFE ASSURANCE COMPANY OF CANADA (NAIC 80802 — the U.S.
    branch of the Canadian insurer, head office 1 York Street, Toronto) insures the plans of some 4,000 US employers in the 2024 filings.
  Schedule C (service-provider information), item 2: every person paid $5,000 or more by the plan, with its address — a foreign address with
    country CA is a provider located in Canada (investment managers, actuaries, law firms, health-program vendors), with what it was paid.
The sponsor (name, EIN, address, phone, plan name) comes from the Form 5500 itself. Natural persons (signers, "care of" names) are never read.

  pull  [--years 2024,2025]   the three zips of each year -> data/incoming/claude/f5500/<year>_{scha,schc,sponsors}.csv.gz (only the lines
                              that name a Canadian insurer or provider, and their filings' sponsors)
  build                       -> data/incoming/claude/f5500/f5500_buyers.csv.gz: one line per sponsor (EIN), its newest filing
  sites [--minutes M]         the sponsor's own site: an Overture Maps place of the same name at the same ZIP code (tools/overture_names.py,
                              lane f55), then the sponsor's very name as a .com domain — kept ONLY when the site's own home or contact page
                              prints the sponsor's ZIP code after its state (or its name in its title, for a place-dataset candidate)
  leads [--stamp S]           sponsors with a site -> data/incoming/claude/lead_shards/leads_f55_<S>.gz + details_f55_<S>.gz
"""
import argparse, collections, csv, glob, gzip, hashlib, io, json, os, re, socket, sys, time, urllib.request, zipfile

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "f5500")
SHARDS = os.path.join(INC, "lead_shards")
BUYERS = os.path.join(DIR, "f5500_buyers.csv.gz")
SITES = os.path.join(DIR, "f5500_sites.csv")
SDONE = os.path.join(DIR, "f5500_sites_done.tsv")
OVT = os.path.join(INC, "overture", "f55_candidates.csv")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
BASE = "https://askebsa.dol.gov/FOIA%20Files/{y}/All/{f}_{y}_All.zip"
LANDING = "https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/public-disclosure/foia/form-5500-datasets"
TODAY = time.strftime("%Y-%m-%d")
SUN_ADDR_Q = "Our corporate head office is located at: 1 York Street Toronto, Ontario M5J 0B6 Canada"
SUN_ADDR_URL = "https://www.sunlife.com/en/contact-us/"
SPON_COLS = ["ACK_ID", "FORM_PLAN_YEAR_BEGIN_DATE", "FORM_TAX_PRD", "PLAN_NAME", "SPONS_DFE_PN", "SPONSOR_DFE_NAME", "SPONS_DFE_DBA_NAME",
             "SPONS_DFE_MAIL_US_ADDRESS1", "SPONS_DFE_MAIL_US_ADDRESS2", "SPONS_DFE_MAIL_US_CITY", "SPONS_DFE_MAIL_US_STATE", "SPONS_DFE_MAIL_US_ZIP",
             "SPONS_DFE_LOC_US_ADDRESS1", "SPONS_DFE_LOC_US_CITY", "SPONS_DFE_LOC_US_STATE", "SPONS_DFE_LOC_US_ZIP", "SPONS_DFE_EIN", "SPONS_DFE_PHONE_NUM",
             "BUSINESS_CODE", "TOT_PARTCP_BOY_CNT", "TOT_ACTIVE_PARTCP_CNT"]
A_COLS = ["ACK_ID", "SCH_A_PLAN_YEAR_BEGIN_DATE", "SCH_A_PLAN_YEAR_END_DATE", "SCH_A_PLAN_NUM", "SCH_A_EIN", "INS_CARRIER_NAME", "INS_CARRIER_EIN",
          "INS_CARRIER_NAIC_CODE", "INS_CONTRACT_NUM", "INS_PRSN_COVERED_EOY_CNT", "INS_POLICY_FROM_DATE", "INS_POLICY_TO_DATE", "INS_BROKER_COMM_TOT_AMT",
          "INS_BROKER_FEES_TOT_AMT", "WLFR_PREMIUM_RCVD_AMT", "WLFR_TOT_EARNED_PREM_AMT", "WLFR_BNFT_HEALTH_IND", "WLFR_BNFT_DENTAL_IND", "WLFR_BNFT_VISION_IND",
          "WLFR_BNFT_LIFE_INSUR_IND", "WLFR_BNFT_TEMP_DISAB_IND", "WLFR_BNFT_LONG_TERM_DISAB_IND", "WLFR_BNFT_STOP_LOSS_IND", "WLFR_BNFT_DRUG_IND",
          "WLFR_BNFT_OTHER_IND", "WLFR_TYPE_BNFT_OTH_TEXT", "PENSION_PREM_PAID_TOT_AMT"]
C_COLS = ["ACK_ID", "ROW_ORDER", "PROVIDER_OTHER_NAME", "PROVIDER_OTHER_EIN", "PROV_OTHER_FOREIGN_ADDRESS1", "PROV_OTHER_FOREIGN_ADDRESS2",
          "PROV_OTHER_FOREIGN_CITY", "PROV_OTHER_FOREIGN_PROV_STATE", "PROV_OTHER_FOREIGN_CNTRY", "PROV_OTHER_FOREIGN_POSTAL_CD", "PROVIDER_OTHER_SRVC_CODES",
          "PROVIDER_OTHER_RELATION", "PROVIDER_OTHER_DIRECT_COMP_AMT", "PROV_OTHER_TOT_IND_COMP_AMT"]
BENEFIT = {"WLFR_BNFT_HEALTH_IND": "health", "WLFR_BNFT_DENTAL_IND": "dental", "WLFR_BNFT_VISION_IND": "vision", "WLFR_BNFT_LIFE_INSUR_IND": "life insurance",
           "WLFR_BNFT_TEMP_DISAB_IND": "short-term disability", "WLFR_BNFT_LONG_TERM_DISAB_IND": "long-term disability", "WLFR_BNFT_STOP_LOSS_IND": "stop-loss",
           "WLFR_BNFT_DRUG_IND": "prescription drugs", "WLFR_BNFT_OTHER_IND": "other"}


def canadian_insurer(name, naic):
    """the Canadian legal entities among the insurers: Sun Life Assurance Company of Canada (its U.S. branch, NAIC 80802 / 80926) and The Canada
    Life Assurance Company (NAIC 80659). "Sun Life and Health Insurance Company (U.S.)" is a US company and is not one."""
    n = re.sub(r"[^A-Z]", "", (name or "").upper())
    if "HEALTHINSURANCE" in n or "US" == n[-2:] and "CANADA" not in n:
        return ""
    if (n.startswith("SUNLIFE") and "CANADA" in n) or (naic or "").strip() in ("80802", "80926") and n.startswith("SUN"):
        return "Sun Life Assurance Company of Canada"
    if n.startswith(("THECANADALIFEASSURANCE", "CANADALIFEASSURANCE")) or (naic or "").strip() == "80659":
        return "The Canada Life Assurance Company"
    return ""


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def fetch_zip(url, dest):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=600) as r, open(dest, "wb") as f:
        while True:
            b = r.read(4 << 20)
            if not b:
                break
            f.write(b)


def rows_of(zpath):
    with zipfile.ZipFile(zpath) as z:
        name = [m for m in z.namelist() if m.lower().endswith(".csv")][0]
        with z.open(name) as fh:
            yield from csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1", newline=""))


def cmd_pull(a):
    os.makedirs(DIR, exist_ok=True)
    tmp = os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "f5500")
    os.makedirs(tmp, exist_ok=True)
    for y in a.years.split(","):
        acks, n_a, n_c = set(), 0, 0
        za = os.path.join(tmp, "a%s.zip" % y)
        fetch_zip(BASE.format(y=y, f="F_SCH_A"), za)
        with gzip.open(os.path.join(DIR, "%s_scha.csv.gz" % y), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=A_COLS + ["insurer"], extrasaction="ignore")
            w.writeheader()
            for r in rows_of(za):
                ins = canadian_insurer(r.get("INS_CARRIER_NAME"), r.get("INS_CARRIER_NAIC_CODE"))
                if ins:
                    r["insurer"] = ins
                    w.writerow(r); acks.add(r["ACK_ID"]); n_a += 1
        os.remove(za)
        zc = os.path.join(tmp, "c%s.zip" % y)
        fetch_zip(BASE.format(y=y, f="F_SCH_C_PART1_ITEM2"), zc)
        with gzip.open(os.path.join(DIR, "%s_schc.csv.gz" % y), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=C_COLS, extrasaction="ignore")
            w.writeheader()
            for r in rows_of(zc):
                if (r.get("PROV_OTHER_FOREIGN_CNTRY") or "").strip().upper() in ("CA", "CAN", "CANADA") and num(r.get("PROVIDER_OTHER_DIRECT_COMP_AMT")) + num(r.get("PROV_OTHER_TOT_IND_COMP_AMT")) > 0:
                    w.writerow(r); acks.add(r["ACK_ID"]); n_c += 1
        os.remove(zc)
        zm = os.path.join(tmp, "m%s.zip" % y)
        fetch_zip(BASE.format(y=y, f="F_5500"), zm)
        n_s = 0
        with gzip.open(os.path.join(DIR, "%s_sponsors.csv.gz" % y), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=SPON_COLS, extrasaction="ignore")
            w.writeheader()
            for r in rows_of(zm):
                if r["ACK_ID"] in acks:
                    w.writerow(r); n_s += 1
        os.remove(zm)
        print("%s: %d contract lines of a Canadian insurer, %d payments to a provider in Canada, %d filings' sponsors" % (y, n_a, n_c, n_s), flush=True)


def is_person(name):
    import dian_cloud as DC
    return DC.is_person(name)


BUYER_COLS = ["key", "ein", "name", "dba", "address", "city", "state", "zip", "phone", "plan_names", "business_code", "participants", "plan_year",
              "insurer", "contracts", "policy_numbers", "policy_to", "persons_covered", "benefits", "commissions_usd", "premiums_usd",
              "providers", "provider_comp_usd", "provider_addresses", "ack_ids", "years"]


def cmd_build(a):
    spon, cnt = {}, collections.Counter()
    for p in sorted(glob.glob(os.path.join(DIR, "*_sponsors.csv.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                spon[r["ACK_ID"]] = r
    by = {}
    for p in sorted(glob.glob(os.path.join(DIR, "*_scha.csv.gz"))):
        y = os.path.basename(p)[:4]
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                s = spon.get(r["ACK_ID"])
                if not s:
                    cnt["contract without its filing"] += 1; continue
                ein = re.sub(r"\D", "", s.get("SPONS_DFE_EIN") or "")
                if not ein or is_person(s.get("SPONSOR_DFE_NAME") or ""):
                    cnt["no EIN or a person's name"] += 1; continue
                o = by.setdefault(ein, {"s": s, "ins": collections.Counter(), "c": [], "p": [], "acks": set(), "years": set()})
                if (s.get("FORM_PLAN_YEAR_BEGIN_DATE") or "") >= (o["s"].get("FORM_PLAN_YEAR_BEGIN_DATE") or ""):
                    o["s"] = s
                o["ins"][r["insurer"]] += 1; o["c"].append((y, r)); o["acks"].add(r["ACK_ID"]); o["years"].add(y)
    for p in sorted(glob.glob(os.path.join(DIR, "*_schc.csv.gz"))):
        y = os.path.basename(p)[:4]
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                s = spon.get(r["ACK_ID"])
                if not s or is_person(r.get("PROVIDER_OTHER_NAME") or "") or is_person(s.get("SPONSOR_DFE_NAME") or ""):
                    cnt["provider line skipped (no filing, or a person)"] += 1; continue
                ein = re.sub(r"\D", "", s.get("SPONS_DFE_EIN") or "")
                if not ein:
                    continue
                o = by.setdefault(ein, {"s": s, "ins": collections.Counter(), "c": [], "p": [], "acks": set(), "years": set()})
                o["p"].append((y, r)); o["acks"].add(r["ACK_ID"]); o["years"].add(y)
    with gzip.open(BUYERS + ".tmp", "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(BUYER_COLS)
        for ein, o in sorted(by.items()):
            s = o["s"]
            newest = max([y for y, _ in o["c"]] + [y for y, _ in o["p"]])
            cs = [r for y, r in o["c"] if y == newest] or [r for _, r in o["c"]]
            ps = [r for y, r in o["p"] if y == newest] or [r for _, r in o["p"]]
            bens = sorted({BENEFIT[k] for r in cs for k in BENEFIT if (r.get(k) or "").strip() in ("1", "Y", "X")})
            w.writerow(["f55:%s" % ein, ein, s.get("SPONSOR_DFE_NAME", "").strip(), s.get("SPONS_DFE_DBA_NAME", "").strip(),
                        " ".join(x for x in (s.get("SPONS_DFE_MAIL_US_ADDRESS1"), s.get("SPONS_DFE_MAIL_US_ADDRESS2")) if x).strip(),
                        s.get("SPONS_DFE_MAIL_US_CITY", ""), s.get("SPONS_DFE_MAIL_US_STATE", ""), (s.get("SPONS_DFE_MAIL_US_ZIP") or "")[:5],
                        s.get("SPONS_DFE_PHONE_NUM", ""), "; ".join(sorted({r_["PLAN_NAME"] for r_ in [s] if r_.get("PLAN_NAME")})), s.get("BUSINESS_CODE", ""),
                        s.get("TOT_PARTCP_BOY_CNT", ""), "%s to %s" % (cs[0].get("SCH_A_PLAN_YEAR_BEGIN_DATE", "") if cs else s.get("FORM_PLAN_YEAR_BEGIN_DATE", ""),
                                                                       cs[0].get("SCH_A_PLAN_YEAR_END_DATE", "") if cs else ""),
                        o["ins"].most_common(1)[0][0] if o["ins"] else "", len(cs), "; ".join(sorted({r["INS_CONTRACT_NUM"].strip() for r in cs if r.get("INS_CONTRACT_NUM")}))[:200],
                        max([r.get("INS_POLICY_TO_DATE") or "" for r in cs] or [""]), max([int(num(r.get("INS_PRSN_COVERED_EOY_CNT"))) for r in cs] or [0]),
                        ", ".join(bens), "%.2f" % sum(num(r.get("INS_BROKER_COMM_TOT_AMT")) for r in cs),
                        "%.2f" % sum(max(num(r.get("WLFR_PREMIUM_RCVD_AMT")), num(r.get("WLFR_TOT_EARNED_PREM_AMT"))) for r in cs),
                        "; ".join(sorted({r["PROVIDER_OTHER_NAME"].strip() for r in ps}))[:300],
                        "%.2f" % sum(num(r.get("PROVIDER_OTHER_DIRECT_COMP_AMT")) + num(r.get("PROV_OTHER_TOT_IND_COMP_AMT")) for r in ps),
                        " | ".join(sorted({", ".join(x for x in (r.get("PROV_OTHER_FOREIGN_ADDRESS1"), r.get("PROV_OTHER_FOREIGN_CITY"), r.get("PROV_OTHER_FOREIGN_PROV_STATE"),
                                                                 r.get("PROV_OTHER_FOREIGN_POSTAL_CD"), "Canada") if x) for r in ps}))[:400],
                        ";".join(sorted(o["acks"]))[:400], ";".join(sorted(o["years"]))])
            cnt["sponsors"] += 1
            cnt["with a Canadian insurer" if cs else "with a provider in Canada only"] += 1
    os.replace(BUYERS + ".tmp", BUYERS)
    print("f5500 buyers: %s" % dict(cnt), flush=True)


def buyers():
    if not os.path.exists(BUYERS):
        return []
    with gzip.open(BUYERS, "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


def cmd_sites(a):
    import queue, threading
    import hc_registers as HR
    bs = buyers()
    have = sites_on_file()
    done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")} if os.path.exists(SDONE) else set()
    ovt = collections.defaultdict(list)
    if os.path.exists(OVT):
        for r in csv.DictReader(open(OVT, encoding="utf-8", newline="")):
            ovt[r["key"]].append(r)
    todo = [b for b in bs if b["key"] not in have and b["key"] not in done and re.fullmatch(r"\d{5}", b.get("zip") or "")]
    todo.sort(key=lambda b: -(num(b["commissions_usd"]) + num(b["premiums_usd"]) + num(b["provider_comp_usd"])))
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
    if new:
        w.writeheader()
    dn = open(SDONE, "a", encoding="utf-8")
    t_end, lock, q, cnt = time.time() + 60 * a.minutes, threading.Lock(), queue.Queue(), collections.Counter()
    for b in todo:
        q.put(b)

    def guesses(name):
        words = [x for x in HR.core(name).split() if x not in ("the", "and", "of", "inc", "llc", "corp", "co", "company")]
        out = []
        for st in ("".join(words), "".join(words[:2]), words[0] if words else ""):
            st = re.sub(r"[^a-z0-9]", "", st)
            if len(st) >= 5 and st + ".com" not in out:
                out.append(st + ".com")
        return out[:3]

    def one(b):
        n = HR.core(b["name"])
        for c in ovt.get(b["key"], ()):
            d = c["site"]
            if HR.BAD.search(d):
                continue
            said = HR.home_says(d, n)
            pcs = "" if said else HR.pc_on_home(d, b["zip"], "united states", contact=True)
            if said or pcs:
                how = ("carries the sponsor's name: “%s”" % said) if said else ("prints the sponsor's ZIP code: “%s”" % HR.no_mail(pcs))
                return d, "an Overture Maps place lists %s under the sponsor's name at its ZIP code %s (“%s”, place %s; Overture Maps Foundation open data, release %s), and the site's own home page %s" % (
                    d, b["zip"], c["place_name"], c["place_id"], c["release"], how), (said or HR.no_mail(pcs))
        for d in guesses(b["name"]):
            try:
                socket.getaddrinfo(d, 443)
            except Exception:
                continue
            pcs = HR.pc_on_home(d, b["zip"], "united states", contact=True)
            if pcs:
                return d, "the sponsor's very name as a domain (%s), whose own pages print the sponsor's ZIP code %s after its state: “%s”" % (d, b["zip"], HR.no_mail(pcs)[:200]), HR.no_mail(pcs)
        return None

    def worker():
        socket.setdefaulttimeout(6)
        while time.time() < t_end:
            try:
                b = q.get_nowait()
            except queue.Empty:
                return
            try:
                hit = one(b)
            except Exception:
                hit = None
            with lock:
                dn.write("%s\t%s\n" % (b["key"], hit[0] if hit else "")); dn.flush()
                cnt["asked"] += 1
                if hit:
                    w.writerow({"key": b["key"], "site": "https://%s/" % hit[0], "read": TODAY, "quote": hit[2][:300], "tied_by": hit[1]})
                    f.flush(); cnt["tied"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(a.threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dn.close(); f.close()
    print("f5500 sites: %d on file before, %d sponsors without one; %s" % (len(have), len(todo), dict(cnt)), flush=True)


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    sites = sites_on_file()
    hosts = collections.Counter(re.sub(r"^https?://(www\.)?", "", s["site"]).split("/")[0] for s in sites.values() if s.get("site"))
    rows, dets, cnt = [], [], collections.Counter()
    for b in buyers():
        s = sites.get(b["key"])
        if not s or not s.get("site"):
            continue
        if hosts[re.sub(r"^https?://(www\.)?", "", s["site"]).split("/")[0]] > 2:
            cnt["site shared by more than two sponsors: left out"] += 1; continue
        ins = b["insurer"]
        key = "lead:" + hashlib.sha1(("f55|%s" % b["ein"]).encode()).hexdigest()[:16]
        year = b["years"].split(";")[-1]
        url = BASE.format(y=year, f="F_SCH_A" if ins else "F_SCH_C_PART1_ITEM2")
        if ins:
            vendor = ins
            vaddr = ("%s (the insurer's own page, %s; the policies of US plans are issued by its U.S. branch, NAIC 80802 — Form 5500 Schedule A)" % (
                SUN_ADDR_Q.split(": ", 1)[1], SUN_ADDR_URL)) if ins.startswith("Sun Life") else "the insurer's address is not read yet"
            cfv = ("insured benefit plan of a Canadian insurer — US Department of Labor, Form 5500 Schedule A, plan year %s: INS_CARRIER_NAME=%s; "
                   "INS_CARRIER_NAIC_CODE; head office %s" % (b["plan_year"], ins, SUN_ADDR_Q.split(": ", 1)[1] if ins.startswith("Sun Life") else ""))
        else:
            vendor = b["providers"].split("; ")[0]
            vaddr = "%s (the provider's address in Canada as the plan's Schedule C records it: PROV_OTHER_FOREIGN_ADDRESS1, CITY, PROV_STATE, POSTAL_CD, CNTRY)" % b["provider_addresses"].split(" | ")[0]
            cfv = ("service provider in Canada paid by the plan — US Department of Labor, Form 5500 Schedule C item 2, plan year %s: PROV_OTHER_FOREIGN_CNTRY=CA; "
                   "PROV_OTHER_FOREIGN_ADDRESS=%s" % (b["plan_year"], b["provider_addresses"].split(" | ")[0]))
        rows.append({"buyer_key": key, "buyer_name": b["name"], "website": s["site"], "canadian_vendor_rows": int(b["contracts"] or 0) + (1 if b["providers"] else 0),
                     "example_vendor": vendor, "canada_field_value": cfv, "evidence_dataset": url, "latest_record_date": (b["plan_year"].split(" to ")[-1] or TODAY)[:10]})
        dets.append({"key": key, "platform": "f5500_plan", "record_url": url, "record_date": (b["plan_year"].split(" to ")[-1] or TODAY)[:10], "vendor": vendor,
                     "vendor_address": vaddr, "reference": b["policy_numbers"] if ins else "", "start": b["plan_year"].split(" to ")[0], "end": b["policy_to"],
                     "title": ("group %s insurance (Form 5500 Schedule A)" % b["benefits"]) if ins else "services to the benefit plan (Form 5500 Schedule C)",
                     "f55_ein": b["ein"], "f55_plan_names": b["plan_names"], "f55_plan_year": b["plan_year"], "f55_insurer": ins, "f55_contracts": b["contracts"],
                     "f55_policy_numbers": b["policy_numbers"], "f55_policy_to": b["policy_to"], "f55_persons": b["persons_covered"], "f55_benefits": b["benefits"],
                     "f55_commissions": b["commissions_usd"], "f55_premiums": b["premiums_usd"], "f55_providers": b["providers"], "f55_provider_comp": b["provider_comp_usd"],
                     "f55_participants": b["participants"], "f55_acks": b["ack_ids"], "f55_years": b["years"], "dataset_page": LANDING,
                     "f55_sponsor_address": ", ".join(x for x in (b["address"], b["city"], b["state"], b["zip"]) if x),
                     "buyer_register": {"legal_name": b["name"], "trade_names": [b["dba"]] if b["dba"] else [], "registry_id": "EIN %s (US)" % b["ein"],
                                        "label": "the plan's Form 5500 filing (US Department of Labor), plan year %s" % b["plan_year"]},
                     "site_named_by": s.get("tied_by") or "", "site_tied_to_holder_by": s.get("tied_by") or "", "site_quote": s.get("quote") or ""})
        cnt["leads"] += 1
    old = {}
    for pth in sorted(glob.glob(os.path.join(SHARDS, "details_f55_*.gz"))):
        with gzip.open(pth, "rt", encoding="utf-8") as fh:
            for l in fh:
                d_ = json.loads(l); old[d_["key"]] = json.dumps(d_, sort_keys=True, ensure_ascii=False)
    keep = [i for i, d_ in enumerate(dets) if old.get(d_["key"]) != json.dumps(d_, sort_keys=True, ensure_ascii=False)]
    cnt["unchanged since the shards on file"] = len(rows) - len(keep)
    rows, dets = [rows[i] for i in keep], [dets[i] for i in keep]
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_f55_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_f55_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("f5500 leads written: %d (%s)" % (len(rows), dict(cnt)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--years", default="2024,2025")
    sub.add_parser("build")
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=60); p.add_argument("--threads", type=int, default=10)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Health Canada's product registers -> leads: the companies Health Canada invoices every year for the right to sell a product (no AI).

Drugs. Every drug sold in Canada carries a drug identification number (DIN); Health Canada's Drug Product Database (DPD) names the company that
owns each DIN and the drug's status. Health Canada's own guidance: “Every October 1 st , Health Canada sends invoices for the upcoming year …”,
“The person on record as owning the Drug Identification Number when the invoice is issued is responsible for payment.”, “Payment is due 30 days
from date of issuance.” Its fee page gives the annual fee of each drug as of April 1, 2026: disinfectant $1,760, non-prescription drug $3,391,
any other drug $5,626. A company with drugs on the market (status "Marketed") is a current, invoiced, yearly relationship with a Canadian public
body; what it is billed is the fees of its drugs on the market, calculated here from the published fees (a small business is billed 25 % less).
Medical devices. The Medical Devices Active Licence Listing (MDALL) names the manufacturer of every licensed device. Health Canada's fee page:
“The annual fee for the right to sell either a licensed Class II, III or IV medical device … $452 $460” (as of April 1, 2025 / 2026); its
guidance: “The fees are charged annually for the twelve month period beginning on November 1 of each year.” and “The invoices are mailed in
February for payment within 30 days.” A manufacturer with Class II-IV licences issued and not cancelled is billed $460 a licence.
How Health Canada is paid, from its own page: “Payments can be made by applying an existing credit, payment through a Canadian Financial
Institution (via Bill Payment Service - BPS), direct deposit, wire transfer, cheque, bank draft, money order, or credit card.”

The registers give each company's name and address (abroad for most device makers), never its website. A site is tied to a company only
  (1) when a site on file prints the same postal code and the names agree (the organisations whose own pages the contact reader read; the
      trademark owners' sites, tied by name and postal code — data/incoming/claude/tm/tm_sites_found.csv); or
  (2) when the company-name autocomplete (Clearbit, no key, one request a second) proposes a domain under the company's very name (legal forms
      aside) and that domain's own home page carries the name in its title or site name (tools/site_finder_names.py's test).
The mailbox comes from that site, like every other lead's (tools/lead_crawl.py reads lead_shards/). Natural persons are not in these registers.
Establishment licences (2026-11-12). Every importer or distributor of medical devices in Canada, here or abroad, holds a medical device establishment
licence (MDEL); Health Canada's MDEL listing names each holder of an active licence with its address. Its fee as of April 1, 2026 is $5,519 a year
(“Medical Device Establishment Licence $5,426 $5,519”); “We will issue an invoice after we receive and screen your ALR application for completeness.”
(the annual licence review); “Payment is due upon issuance of the invoice.” One line per licence; the fee is published, not calculated.

  pull  [--work DIR]              the six lists of the two APIs -> DIR (health-products.canada.ca; about 60 MB), and the medical device establishment
                                  licence listing (three searches of its own form, by activity)
  build [--work DIR]              -> data/incoming/claude/hc/hc_companies.csv.gz: one line per company and register, with its products and fee
  sites [--minutes M]             sites for the companies without one -> data/incoming/claude/hc/hc_sites.csv (append-only; done list beside it)
  leads [--stamp S]               companies with a site -> data/incoming/claude/lead_shards/leads_hc_<S>.gz + details_hc_<S>.gz
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "hc")
SHARDS = os.path.join(INC, "lead_shards")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
API = "https://health-products.canada.ca/api/%s/?lang=en&type=json"
LISTS = {"md_company": "medical-devices/company", "md_licence": "medical-devices/licence", "dpd_company": "drug/company",
         "dpd_product": "drug/drugproduct", "dpd_status": "drug/status", "dpd_schedule": "drug/schedule"}

READ = "2026-11-12"
DRUG_FEE_URL = ("https://www.canada.ca/en/health-canada/services/drugs-health-products/funding-fees/fees-respect-human-drugs-medical-devices/"
                "right-sell-drugs-funding-fees-drugs-health-products.html")
MD_FEE_URL = ("https://www.canada.ca/en/health-canada/services/drugs-health-products/funding-fees/fees-respect-human-drugs-medical-devices/"
              "right-sell-licensed-class-medical-devices-funding-fees-drugs.html")
PAY_URL = "https://www.canada.ca/en/health-canada/services/funding/cost-recovery-service-fees/how-pay-fees.html"
DRUG_GUIDE_URL = "https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/fees/right-to-sell-drugs-2019/document.html"
MD_GUIDE_URL = ("https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/application-information/guidance-documents/"
                "guidance-document-medical-device-licence-renewal-fees-right-sell-licensed.html")
FEE = {"rx": 5626.0, "otc": 3391.0, "dis": 1760.0, "md": 460.0, "mdel": 5519.0}
FEE_WORD = {"rx": "drug other than a disinfectant or a non-prescription drug", "otc": "non-prescription drug", "dis": "disinfectant", "md": "licensed Class II, III or IV medical device",
            "mdel": "medical device establishment licence"}
# Medical device establishment licences (MDEL): every importer or distributor of medical devices in Canada, here or abroad; the listing is the
# public search of active licences (one search by activity returns them all); Health Canada invoices the licence fee at each yearly review
MDEL_LIST = "https://health-products.canada.ca/mdel-leim/"
MDEL_ACTS = {"1": "Distribute", "2": "Import", "3": "Manufacture Devices for Distribution"}
MDEL_FEE_URL = ("https://www.canada.ca/en/health-canada/services/drugs-health-products/funding-fees/fees-respect-human-drugs-medical-devices/"
                "medical-device-establishment-licence-funding-fees-drugs-health-products.html")
MDEL_FEE_Q = "Fee category Fee as of April 1, 2025 Fee as of April 1, 2026 Medical Device Establishment Licence $5,426 $5,519"
MDEL_ALR_URL = ("https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/establishment-licences/"
                "medical-devices-compliance-bulletin/annual-licence-review-2023.html")
MDEL_ALR_Q = "We will issue an invoice after we receive and screen your ALR application for completeness."
MDEL_GUIDE_URL = "https://www.canada.ca/en/health-canada/services/drugs-health-products/funding-fees/review-medical-device-establishment-licence.html"
MDEL_INV_Q = ("Following preliminary examination and upon determination that the application is accepted for further review, Health Canada will issue "
              "a notice to the applicant and an invoice for the applicable fee.")
MDEL_DUE_Q = "Payment is due upon issuance of the invoice."
MDEL_LATE_Q = "Interest on overdue accounts begins to accrue 30 days from the date of invoice issuance."
DRUG_FEE_Q = ("Fee as of April 1, 2025 Fee as of April 1, 2026 Drugs (DINs) The annual fee for the right to sell a drug … 1 Disinfectant $1,730 $1,760 "
              "2 Non-prescription drug $3,334 $3,391 3 Drug other than one referred to in item 1 or 2 $5,531 $5,626")
MD_FEE_Q = ("Fee as of April 1, 2025 Fee as of April 1, 2026 Medical devices The annual fee for the right to sell either a licensed Class II, III or IV "
            "medical device or an authorized Class II, III or IV medical device that is not an urgent public health need (UPHN) medical device $452 $460")
DRUG_INV_Q = "Every October 1 st , Health Canada sends invoices for the upcoming year based on the information manufacturers have provided in the Annual Drug Notification Form."
DRUG_WHO_Q = "The person on record as owning the Drug Identification Number when the invoice is issued is responsible for payment."
DRUG_DUE_Q = "Payment is due 30 days from date of issuance."
DRUG_SMALL_Q = "Manufacturers that meet the above definition are eligible for a 25% reduction of the applicable right to sell a drug fee."
MD_PERIOD_Q = "The fees are charged annually for the twelve month period beginning on November 1 of each year."
MD_INV_Q = "The invoices are mailed in February for payment within 30 days."
PAY_Q = ("Payments can be made by applying an existing credit, payment through a Canadian Financial Institution (via Bill Payment Service - BPS), direct "
         "deposit, wire transfer, cheque, bank draft, money order, or credit card.")
REMIT_Q = ("Health Canada Accounts Receivable, Address Locator: 1918B 18th Floor, Room 1804B, Jeanne-Mance Building 161 Goldenrod Driveway, Tunney's "
           "Pasture Ottawa, Ontario K1A 0K9")
HC_ADDRESS = "Accounts Receivable, Address Locator: 1918B, 161 Goldenrod Driveway, Tunney's Pasture, Ottawa, Ontario K1A 0K9"
HC_SITE = "https://www.canada.ca/en/health-canada.html"
RX = {"PRESCRIPTION", "SCHEDULE D", "SCHEDULE C", "NARCOTICS (CDSA I)", "NARCOTICS (CDSA II)", "TARGETED SUBSTANCES (CDSA IV)", "CONTROLLED DRUGS (CDSA I)",
      "CONTROLLED DRUGS (CDSA III)", "CONTROLLED DRUGS (CDSA IV)", "PRESCRIPTION RECOMMENDED", "COVID-19 - IO - AUTHORIZATION"}
LEGAL = re.compile(r"\b(inc|incorporated|ltd|limited|llc|l l c|lp|llp|plc|corp|corporation|co|company|sa|s a|sas|s a s|ltda|gmbh|ag|bv|nv|spa|srl|oy|ab|as|"
                   r"pty|ulc|ltee|limitee|kk|k k|sarl|s a r l|gmbh co kg|kg|se|aps|a s|asa|oyj|sl|s l|sp z o o|z o o|pvt|private|the)\b")
BAD = re.compile(r"linkedin|facebook|wikipedia|crunchbase|bloomberg|zoominfo|dnb\.com|yelp|indeed|glassdoor|opencorporates|wix|squarespace|godaddy|"
                 r"shopify|wordpress|google|apple\.com|amazon|alibaba|made-in-china|tradeindia|indiamart|europages|kompass", re.I)
SDONE = os.path.join(DIR, "hc_sites_done.tsv")
SITES = os.path.join(DIR, "hc_sites.csv")
SITE_COLS = ["key", "site", "tied_by", "quote", "read"]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s)).strip()


def core(s):
    return re.sub(r"\s+", " ", LEGAL.sub(" ", norm(s))).strip()


def pc(s):
    s = re.sub(r"[^A-Z0-9]", "", (s or "").upper())
    return s[:5] if re.fullmatch(r"\d{9}", s) else s  # a US ZIP+4 is its ZIP


def get(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r, open(path, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)


def cmd_pull(a):
    os.makedirs(a.work, exist_ok=True)
    for k, ep in LISTS.items():
        p = os.path.join(a.work, k + ".json")
        get(API % ep, p)
        print("%s: %d bytes" % (k, os.path.getsize(p)), flush=True)
        time.sleep(1.0)
    pull_mdel(a.work)


def pull_mdel(work):
    """the MDEL listing: its own search form, one search by activity (every country) -> mdel_<activity>.html"""
    import http.cookiejar
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    for act in MDEL_ACTS:
        try:
            with op.open(urllib.request.Request(MDEL_LIST, headers={"User-Agent": UA}), timeout=120) as r:
                home = r.read().decode("utf-8", "replace")
            m = re.search(r'name="searchMdelForm" method="post" action="([^"]+)"', home)
            if not m:
                print("MDEL listing: no search form found"); return
            time.sleep(2.0)
            body = urllib.parse.urlencode({"licence": "", "companyId": "", "company": "", "activityId": act, "countryId": "", "regionId": "", "action": "Search"}).encode()
            req = urllib.request.Request(urllib.parse.urljoin(MDEL_LIST, m.group(1)), data=body, headers={"User-Agent": UA, "Referer": MDEL_LIST,
                                                                                                          "Content-Type": "application/x-www-form-urlencoded"})
            with op.open(req, timeout=300) as r, open(os.path.join(work, "mdel_%s.html" % act), "wb") as f:
                f.write(r.read())
            print("MDEL listing, %s: %d bytes" % (MDEL_ACTS[act], os.path.getsize(os.path.join(work, "mdel_%s.html" % act))), flush=True)
            time.sleep(3.0)
        except Exception as e:
            print("MDEL listing, %s: not read (%s)" % (MDEL_ACTS[act], str(e)[:120]))


def cmd_build(a):
    L = {k: json.load(open(os.path.join(a.work, k + ".json"), encoding="utf-8")) for k in LISTS}
    os.makedirs(DIR, exist_ok=True)
    out = []
    # drugs: the DIN owner's drugs on the market, by fee category
    status = {x["drug_code"]: x for x in L["dpd_status"]}
    sched = collections.defaultdict(set)
    for x in L["dpd_schedule"]:
        sched[x["drug_code"]].add(x.get("schedule_name") or "")
    comp = {x["company_name"]: x for x in L["dpd_company"]}
    per = collections.defaultdict(lambda: {"n": collections.Counter(), "dins": [], "first": ""})
    for x in L["dpd_product"]:
        st = status.get(x["drug_code"]) or {}
        if st.get("status") != "Marketed":
            continue
        cl, s = x.get("class_name") or "", sched.get(x["drug_code"], set())
        if cl == "Disinfectant":
            cat = "dis"
        elif cl in ("Human", "Radiopharmaceutical"):
            if "HOMEOPATHIC" in s and not (s & RX):
                continue  # a homeopathic medicine (DIN-HM) is a natural health product: no right-to-sell fee for drugs
            cat = "rx" if (s & RX) or cl == "Radiopharmaceutical" else "otc"
        else:
            continue  # veterinary drugs: a fee of their own, not read yet
        p = per[x["company_name"]]
        p["n"][cat] += 1
        p["dins"].append((x.get("drug_identification_number") or "", (x.get("brand_name") or "").strip()))
        md = (st.get("original_market_date") or "")[:10]
        if md and (not p["first"] or md < p["first"]):
            p["first"] = md
    for name, p in per.items():
        c = comp.get(name) or {}
        addr = ", ".join(v for v in (" ".join(v_ for v_ in (c.get("suite_number"), c.get("street_name")) if v_), c.get("post_office_box"), c.get("city_name"),
                                      c.get("province_name"), c.get("postal_code"), c.get("country_name")) if v and str(v).strip())
        fee = sum(FEE[k] * v for k, v in p["n"].items())
        out.append({"key": "hc:dpd:%s" % (c.get("company_code") or norm(name)[:40]), "register": "dpd", "name": name, "address": addr,
                    "postal_code": c.get("postal_code") or "", "city": c.get("city_name") or "", "country": c.get("country_name") or "",
                    "products": sum(p["n"].values()), "by_category": json.dumps(dict(p["n"]), sort_keys=True), "fee_total": "%.0f" % fee,
                    "examples": "; ".join("DIN %s %s" % d for d in sorted(p["dins"])[:5]), "first_on_market": p["first"],
                    "record_url": "https://health-products.canada.ca/dpd-bdpp/"})
    # medical devices: the manufacturer's Class II-IV licences issued (I) or issued with conditions (D), not cancelled
    cm = {x["company_id"]: x for x in L["md_company"]}
    mper = collections.defaultdict(lambda: {"n": 0, "lic": [], "first": ""})
    for x in L["md_licence"]:
        if x.get("licence_status") not in ("I", "D") or x.get("end_date") or x.get("appl_risk_class") not in (2, 3, 4):
            continue
        p = mper[x["company_id"]]
        p["n"] += 1
        p["lic"].append((x.get("original_licence_no"), (x.get("licence_name") or "").strip(), x.get("appl_risk_class")))
        d = (x.get("first_licence_status_dt") or "")[:10]
        if d and (not p["first"] or d < p["first"]):
            p["first"] = d
    for cid, p in mper.items():
        c = cm.get(cid) or {}
        if c.get("company_status") not in ("A", None):
            continue
        addr = ", ".join(v for v in (c.get("addr_line_1"), c.get("addr_line_2"), c.get("addr_line_3"), c.get("city"), c.get("region_cd"), c.get("postal_code"),
                                      c.get("country_cd")) if v and str(v).strip())
        out.append({"key": "hc:md:%s" % cid, "register": "mdall", "name": (c.get("company_name") or "").strip(), "address": addr, "postal_code": c.get("postal_code") or "",
                    "city": c.get("city") or "", "country": c.get("country_cd") or "", "products": p["n"], "by_category": json.dumps({"md": p["n"]}),
                    "fee_total": "%.0f" % (FEE["md"] * p["n"]),
                    "examples": "; ".join("licence %s %s (class %s)" % l for l in sorted(p["lic"], key=lambda l: l[0] or 0)[:5]), "first_on_market": p["first"],
                    "record_url": "https://health-products.canada.ca/mdall-limh/"})
    # medical device establishment licences: one line per active licence (its holder's name and address as the listing prints them)
    lic = {}
    for act, an in MDEL_ACTS.items():
        fp = os.path.join(a.work, "mdel_%s.html" % act)
        if not os.path.exists(fp):
            continue
        page = open(fp, encoding="utf-8", errors="replace").read()
        for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", page):
            cells = re.findall(r"(?is)<td[^>]*>(.*?)</td>", tr)
            if len(cells) < 3:
                continue
            txt = lambda h: " ".join(html.unescape(re.sub(r"<[^>]+>", " ", h)).split())
            no, cid = txt(cells[0]), txt(cells[1])
            if not no.isdigit():
                continue
            parts = [txt(x) for x in re.split(r"(?i)<br\s*/?>", cells[2])]
            parts = [x for x in parts if x]
            if not parts:
                continue
            d = lic.setdefault(no, {"no": no, "cid": cid, "name": parts[0], "lines": parts[1:], "acts": []})
            if an not in d["acts"]:
                d["acts"].append(an)
    for no, d in lic.items():
        last = d["lines"][-1] if d["lines"] else ""
        bits = [b.strip() for b in last.split(",")]
        country = bits[-2] if len(bits) >= 3 else ""
        postal = bits[-1] if len(bits) >= 3 else ""
        out.append({"key": "hc:mdel:%s" % no, "register": "mdel", "name": d["name"], "address": ", ".join(d["lines"]), "postal_code": postal,
                    "city": (bits[0] if bits else ""), "country": country, "products": 1, "by_category": json.dumps({"mdel": 1}),
                    "fee_total": "%.0f" % FEE["mdel"], "examples": "MDEL %s (company %s): %s" % (no, d["cid"], ", ".join(d["acts"])), "first_on_market": "",
                    "record_url": MDEL_LIST})
    out = [o for o in out if o["name"]]
    with gzip.open(os.path.join(DIR, "hc_companies.csv.gz"), "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    big = sum(1 for o in out if float(o["fee_total"]) >= 5000)
    print("companies: %d (drugs %d, devices %d, establishment licences %d); a yearly bill of $5,000 or more: %d; by country: %s"
          % (len(out), sum(o["register"] == "dpd" for o in out), sum(o["register"] == "mdall" for o in out), sum(o["register"] == "mdel" for o in out), big,
             collections.Counter(o["country"] for o in out).most_common(8)), flush=True)


def companies():
    with gzip.open(os.path.join(DIR, "hc_companies.csv.gz"), "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


_MAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def no_mail(t):
    """a quote of a page as evidence of a tie keeps no e-mail address (the mailbox of a row is read and checked elsewhere)"""
    return re.sub(r"\s{2,}", " ", _MAIL.sub("[e-mail]", t or ""))


def names_agree(a, b):
    """every word of the shorter core name is in the longer one, and what agrees identifies (two words, or one of six letters or more)"""
    ca, cb = core(a).split(), core(b).split()
    if not ca or not cb:
        return False
    s, l = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
    if not all(w in l for w in s):
        return False
    return len(s) >= 2 or len(s[0]) >= 6


def tie_on_file(cos):
    """sites on file that print the company's postal code under a name that agrees"""
    by_pc = collections.defaultdict(list)
    try:
        import state_io
        p = os.path.join(INC, "claude_org_contacts.jsonl.gz")
        state_io.ensure(p)
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                m = re.search(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b", (d.get("address") or "").upper())
                if m and d.get("website") and d.get("name"):
                    by_pc[m.group(1) + m.group(2)].append((d["name"], d["website"], "the contact reader's reading of its own page %s: “%s”" % (d.get("address_url") or d["website"], no_mail((d.get("address_quote") or d.get("address") or "").replace("\ufffd", ""))[:200])))
    except Exception as e:
        print("org contacts not read: %s" % str(e)[:100])
    tp = os.path.join(INC, "tm", "tm_sites_found.csv")
    if os.path.exists(tp):
        for r in csv.DictReader(open(tp, encoding="utf-8", newline="")):
            if r.get("postal_code") and r.get("site"):
                by_pc[pc(r["postal_code"])].append((r.get("owner_name") or "", "https://%s/" % r["site"], "the trademark register's owner of the same name and postal code, whose site was tied by: %s" % (r.get("tied_by") or "")[:200]))
    found = {}
    for o in cos:
        cands = [c for c in by_pc.get(pc(o["postal_code"]), []) if names_agree(c[0], o["name"])] if pc(o["postal_code"]) else []
        hosts = {urllib.parse.urlparse(c[1]).hostname for c in cands}
        if len(hosts) == 1:
            c = cands[0]
            found[o["key"]] = {"key": o["key"], "site": c[1], "tied_by": "the same postal code (%s) and names that agree (%s ~ %s): %s" % (o["postal_code"], o["name"][:60], c[0][:60], c[2]),
                               "quote": c[2][:300], "read": TODAY}
    return found


CC = {"canada": "ca", "united states": "us", "germany": "de", "united kingdom": "uk", "gb": "uk", "france": "fr", "switzerland": "ch", "ireland": "ie",
      "australia": "au", "india": "in", "netherlands": "nl", "sweden": "se", "china": "cn", "japan": "jp", "italy": "it", "spain": "es", "belgium": "be",
      "denmark": "dk", "israel": "il", "korea, republic of": "kr", "south korea": "kr", "austria": "at", "finland": "fi", "norway": "no", "taiwan": "tw",
      "singapore": "sg", "new zealand": "nz", "mexico": "mx", "brazil": "br", "poland": "pl", "czech republic": "cz", "portugal": "pt", "turkey": "tr"}
GENERIC = {"com", "net", "org", "health", "bio", "co", "io", "global", "info", "biz", "eu", "int", "care", "life", "group", "company", "tech", "science"}


def domain_fits(dom, n, country):
    """the domain IS the company's name (its label is the name, spaces aside) on a generic ending or the company's own country's"""
    parts = dom.lower().split(".")
    if len(parts) < 2:
        return False
    tld = parts[-1]
    label = parts[-3] if len(parts) >= 3 and parts[-2] in ("co", "com", "or", "ne", "ac") and len(parts[-1]) == 2 else parts[-2]
    c = norm(country)
    own = CC.get(c, c if len(c) == 2 else "")
    if own == "gb":
        own = "uk"
    if tld not in GENERIC and tld != own:
        return False
    flat = re.sub(r"[^a-z0-9]", "", label)
    words = n.split()
    if flat in (re.sub(r"[^a-z0-9]", "", n), re.sub(r"[^a-z0-9]", "", " ".join(words[:2]))) and len(flat) >= 4:
        return True
    # "Sivem Pharmaceuticals" at sivem.ca, "Otsuka Pharmaceutical" at otsuka.co.jp: a distinctive first word, and the rest only words of the trade
    return len(words) >= 2 and flat == words[0] and len(flat) >= 5 and all(w in TRADE_WORDS for w in words[1:])


TRADE_WORDS = set("""pharmaceutical pharmaceuticals pharma pharmaceutique pharmaceutiques laboratories laboratory laboratoires labs lab life sciences science
healthcare health medical medicals biotech biotechnology biologics bio therapeutics technologies technology systems devices diagnostics international
group holdings industries industry manufacturing products solutions medicine medicines""".split())


GROUPS = {}  # a group's name (group_key) -> the countries of the register's entities that bear it
_COMMON_FIRST = set("""advanced american applied general global international united national medical bio biomedical smith johnson universal premier
first new north south east west pacific atlantic royal standard central guardian sun star best pro alpha beta omega life health care""".split())


def group_key(n):
    """the name a group's entities share: its first word when that word is distinctive (Stryker, Abbott), else its first two (Advanced Bionics)"""
    w = n.split()
    return w[0] if (w and len(w[0]) >= 5 and w[0] not in _COMMON_FIRST) or len(w) == 1 else " ".join(w[:2])
_last = [0.0]


def suggest(q):
    wait = _last[0] + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    try:
        req = urllib.request.Request("https://autocomplete.clearbit.com/v1/companies/suggest?query=" + urllib.parse.quote(q[:80]), headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception:
        return []


def home_says(domain, n):
    import client_lists as CL
    site = "https://%s/" % domain
    if not CL.allowed(site):
        return ""
    page, final = CL.fetch(site)
    if not page:
        return ""
    head = page[:200_000]
    bits = re.findall(r"(?is)<title[^>]*>(.*?)</title>", head)[:1] + \
        re.findall(r"(?is)<meta[^>]+property\s*=\s*[\"']og:site_name[\"'][^>]+content\s*=\s*[\"']([^\"']+)", head)[:1]
    raw = re.sub(r"\s+", " ", html.unescape(" ".join(bits))).strip()
    text = norm(raw)
    words = [w for w in n.split() if len(w) >= 3] or n.split()
    if words and all(w in text.split() or w in text.replace(" ", "") for w in words[:3]):
        return raw[:200]
    return ""


OVT = os.path.join(INC, "overture", "hc_candidates.csv")
ODONE = os.path.join(DIR, "hc_overture_done.tsv")


def pc_on_home(domain, pcode, country, contact=False):
    """the register's postal code printed on the site's own home page: a Canadian code with or without its space, a US ZIP after the state's
    two letters, any other code as written -> the words around it, else """""
    import client_lists as CL
    site = "https://%s/" % domain
    if not pcode or not CL.allowed(site):
        return ""
    page, final = CL.fetch(site)
    if not page:
        return ""
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style).*?</\1>", " ", page[:400_000]))))
    p = re.sub(r"[^A-Z0-9]", "", pcode.upper())
    c = norm(country)
    if c in ("canada", "ca") and re.match(r"[A-Z]\d[A-Z]\d[A-Z]\d$", p):
        rx = r"(?i)\b%s\s?%s\b" % (p[:3], p[3:])
    elif c in ("united states", "us") and re.match(r"\d{5}", p):
        rx = r"\b[A-Z]{2},?\s+%s(?:-\d{4})?\b" % p[:5]
    elif len(p) >= 4:
        rx = r"(?i)(?<![A-Z0-9])%s(?![A-Z0-9])" % re.escape(pcode.strip())
    else:
        return ""
    m = re.search(rx, text)
    if m:
        return text[max(0, m.start() - 60): m.end() + 20].strip()
    if not contact:
        return ""
    base = final or site
    for h in re.findall(r"(?is)<a\b[^>]*href\s*=\s*[\"']([^\"'#]+)[\"']", page[:400_000]):
        u = urllib.parse.urljoin(base, html.unescape(h))
        hu = (urllib.parse.urlparse(u).hostname or "").lower()
        if not hu or hu.removeprefix("www.") != (urllib.parse.urlparse(base).hostname or "").lower().removeprefix("www."):
            continue
        if not re.search(r"contact|nous-joindre|joindre|coordonn|about|a-propos|location|find-us|trouver", u, re.I) or not CL.allowed(u):
            continue
        p2, f2 = CL.fetch(u)
        if p2:
            t2 = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style).*?</\1>", " ", p2[:400_000]))))
            m = re.search(rx, t2)
            if m:
                return "%s: %s" % (f2 or u, t2[max(0, m.start() - 60): m.end() + 20].strip())
        break  # one contact page at most
    return ""


GUESS_DONE = os.path.join(DIR, "hc_guess_done.tsv")


def guess_pass(cos, have, w, f, minutes, threads):
    """the company's very name as a domain (.ca for a company in Canada, then .com; .com for one in the United States), kept ONLY when the site's
    own home page or its contact page prints the register's postal code: a guessed domain is never tied on its name alone"""
    import queue, socket, threading
    done = {l.split("\t")[0] for l in open(GUESS_DONE, encoding="utf-8")} if os.path.exists(GUESS_DONE) else set()
    todo = [o for o in cos if o["key"] not in have and o["key"] not in done and norm(o.get("country") or "") in ("canada", "ca", "united states", "us")
            and o.get("postal_code")]
    todo.sort(key=lambda o: -float(o["fee_total"] or 0))
    if not GROUPS:
        for o in cos:
            c_ = core(o["name"])
            if c_:
                GROUPS.setdefault(group_key(c_), set()).add(norm(o.get("country") or ""))
    t_end = time.time() + 60 * minutes
    lock, q, cnt = threading.Lock(), queue.Queue(), collections.Counter()
    for o in todo:
        q.put(o)
    dn = open(GUESS_DONE, "a", encoding="utf-8")

    def doms(o):
        n = core(o["name"])
        words = [x for x in n.split() if x not in ("canada", "canadian", "inc", "ltd", "corp")]
        if not words:
            return []
        ca = norm(o.get("country") or "") in ("canada", "ca")
        # a name that a group's entities in other countries also bear (Stryker Canada, Stryker Corporation): its .com is the parent's — .ca only
        multi = len(GROUPS.get(group_key(n), set()) - {norm(o.get("country") or "")}) > 0
        stems = []
        for st in (re.sub(r"[^a-z0-9]", "", "".join(words)), re.sub(r"[^a-z0-9]", "", "".join(words[:2])), re.sub(r"[^a-z0-9]", "", words[0])):
            if len(st) >= 5 and st not in stems:
                stems.append(st)
        return ["%s.%s" % (st, t) for st in stems[:3] for t in ((("ca",) if multi else ("ca", "com")) if ca else ("com",))]

    def worker():
        socket.setdefaulttimeout(6)
        while time.time() < t_end:
            try:
                o = q.get_nowait()
            except queue.Empty:
                return
            hit = None
            for d in doms(o):
                if BAD.search(d):
                    continue
                try:
                    socket.getaddrinfo(d, 443)
                except Exception:
                    continue
                try:
                    pcs = pc_on_home(d, o["postal_code"], o.get("country") or "", contact=True)
                except Exception:
                    pcs = ""
                if pcs:
                    hit = (d, pcs)
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit[0] if hit else "")); dn.flush()
                cnt["asked"] += 1
                if hit:
                    d, pcs = hit
                    w.writerow({"key": o["key"], "site": "https://%s/" % d, "read": TODAY, "quote": no_mail(pcs)[:300],
                                "tied_by": "the company's very name as a domain (%s), whose own pages print the register's postal code %s: “%s”" % (d, o["postal_code"], no_mail(pcs)[:200])})
                    f.flush(); have[o["key"]] = True; cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dn.close()
    print("name as a domain: %d companies in Canada / the United States without a site, %d asked this run, %d sites tied" % (len(todo), cnt["asked"], cnt["found"]), flush=True)


OVT_ADDR = os.path.join(INC, "overture", "hc_addr_candidates.csv")  # 2026-11-13: places AT the company's own address (tools/overture_names.py addr)
ADONE = os.path.join(DIR, "hc_addr_done.tsv")


def addr_pass(cos, have, w, f, minutes, threads, ovt_addr=None, adone=None):
    """the companies for which an Overture Maps place AT their own address (Canada: the full postal code; United States: the street number,
    street and ZIP code) lists a website: kept when the site's own home page carries the company's name or prints the register's postal code,
    or its own terms / privacy / legal page prints the company's full legal name with its legal form; the same strict rule as overture_pass
    for a Canadian company on a site that is not .ca and for a name a group's entities abroad also bear (postal code or legal name only)"""
    import queue, threading
    import ap_crawler as C
    import tm_register as TM
    import credit_scan as CS
    ovt_addr, adone = ovt_addr or OVT_ADDR, adone or ADONE  # (the radio-licence lane passes its own files)
    if not os.path.exists(ovt_addr):
        print("addr: no candidates file (tools/overture_names.py addr)", flush=True)
        return 0
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(ovt_addr, encoding="utf-8", newline="")):
        by[r["key"]].append(r)
    done = {l.split("\t")[0] for l in open(adone, encoding="utf-8")} if os.path.exists(adone) else set()
    todo = [o for o in cos if o["key"] in by and o["key"] not in have and o["key"] not in done]
    todo.sort(key=lambda o: -float(o.get("fee_total") or o.get("fee_floor") or 0))
    GROUPS.clear()
    for o in cos:
        c_ = core(o["name"])
        if c_:
            GROUPS.setdefault(group_key(c_), set()).add(norm(o.get("country") or ""))
    t_end = time.time() + 60 * minutes
    lock, q, cnt = threading.Lock(), queue.Queue(), collections.Counter()
    for o in todo:
        q.put(o)
    dn = open(adone, "a", encoding="utf-8")

    def legal(d, name):
        cache = {}
        try:
            res, final, raw = CS.get_page("https://%s/" % d, True, cache)
        except Exception:
            return ""
        if res != "ok":
            return ""
        u, qt, _n = TM.legal_name_page(raw, final, C.registrable((CS.host_of(final) or d).lower()), name, cache)
        return ("%s: “%s”" % (u, qt)) if u else ""

    def worker():
        while time.time() < t_end:
            try:
                o = q.get_nowait()
            except queue.Empty:
                return
            n = core(o["name"])
            ca = norm(o.get("country") or "canada") in ("canada", "ca")
            multi = len(GROUPS.get(group_key(n), set()) - {norm(o.get("country") or "canada")}) > 0
            hit = None
            for c in by[o["key"]]:
                d = c["site"]
                if BAD.search(d):
                    continue
                strict = (ca and not d.endswith(".ca")) or (multi and d.rsplit(".", 1)[-1] in GENERIC)
                try:
                    said = "" if strict else home_says(d, n)
                    if said and TM.other_body(o["name"], said):
                        said = ""  # the site is a foundation's, an association's … built on the company's name
                    # the postal code printed counts only when the place at the address is under the company's own name (every tenant prints it)
                    pcs = "" if (said or not TM.place_fits(o["name"], c.get("place_name") or "")) else pc_on_home(d, o.get("postal_code") or "", o.get("country") or "canada", contact=True)
                    lg = "" if (said or pcs) else legal(d, o["name"])
                except Exception:
                    said, pcs, lg = "", "", ""
                if said or pcs or lg:
                    hit = (c, said, pcs, lg)
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit[0]["site"] if hit else "")); dn.flush()
                cnt["asked"] += 1
                if hit:
                    c, said, pcs, lg = hit
                    how = (("home page carries the company's name: “%s”" % said) if said else ("pages print the register's postal code: “%s”" % no_mail(pcs)) if pcs else
                           ("legal page prints the company's full legal name (%s)" % lg))
                    w.writerow({"key": o["key"], "site": "https://%s/" % c["site"], "read": TODAY, "quote": (said or no_mail(pcs) or lg)[:300],
                                "tied_by": "an Overture Maps place %s (“%s”, place %s; Overture Maps Foundation open data, release %s) lists %s, "
                                           "and the site's own %s" % (("at the company's own " + c["how"][len("the owner's own "):]) if c["how"].startswith("the owner's own ")
                                                                      else "under the company's name (%s)" % c.get("how", "")[:80],
                                                                      c["place_name"], c["place_id"], c["release"], c["site"], how)})
                    f.flush(); have[o["key"]] = True; cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dn.close()
    print("addr: %d companies with a place at their own address; %s" % (len(todo), dict(cnt)), flush=True)
    return cnt["found"]


def overture_pass(cos, have, w, f, minutes, threads):
    """the companies for which an Overture Maps place lists a website under their very name at their postal code
    (tools/overture_names.py): the site is kept when its own home page carries the company's name in its title / site name or prints the
    register's postal code. A company in Canada on a site that is not .ca, or one whose name a group's entities in other countries also bear,
    is kept only on its postal code printed on the site (the place may list the parent's worldwide site)."""
    import queue, threading
    if not os.path.exists(OVT):
        print("overture: no candidates file (tools/overture_names.py query)", flush=True)
        return 0
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(OVT, encoding="utf-8", newline="")):
        by[r["key"]].append(r)
    done = {l.split("\t")[0] for l in open(ODONE, encoding="utf-8")} if os.path.exists(ODONE) else set()
    todo = [o for o in cos if o["key"] in by and o["key"] not in have and o["key"] not in done]
    todo.sort(key=lambda o: -float(o["fee_total"] or 0))
    GROUPS.clear()
    for o in cos:
        c_ = core(o["name"])
        if c_:
            GROUPS.setdefault(group_key(c_), set()).add(norm(o.get("country") or ""))
    t_end = time.time() + 60 * minutes
    lock, q, cnt = threading.Lock(), queue.Queue(), collections.Counter()
    for o in todo:
        q.put(o)
    dn = open(ODONE, "a", encoding="utf-8")

    def worker():
        while time.time() < t_end:
            try:
                o = q.get_nowait()
            except queue.Empty:
                return
            n = core(o["name"])
            ca = norm(o.get("country") or "") in ("canada", "ca")
            multi = len(GROUPS.get(group_key(n), set()) - {norm(o.get("country") or "")}) > 0
            hit = None
            for c in by[o["key"]]:
                d = c["site"]
                if BAD.search(d):
                    continue
                strict = (ca and not d.endswith(".ca")) or (multi and d.rsplit(".", 1)[-1] in GENERIC)
                try:
                    said = "" if strict else home_says(d, n)
                    pcs = "" if said else pc_on_home(d, o.get("postal_code") or "", o.get("country") or "")
                except Exception:
                    said, pcs = "", ""
                if said or pcs:
                    hit = (c, said, pcs)
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit[0]["site"] if hit else "")); dn.flush()
                cnt["asked"] += 1
                if hit:
                    c, said, pcs = hit
                    how = ("carries the company's name: “%s”" % said) if said else ("prints the register's postal code: “%s”" % no_mail(pcs))
                    w.writerow({"key": o["key"], "site": "https://%s/" % c["site"], "read": TODAY, "quote": (said or no_mail(pcs))[:300],
                                "tied_by": "an Overture Maps place lists %s under the company's name at its postal code %s (“%s”, place %s; Overture Maps "
                                           "Foundation open data, release %s), and the site's own home page %s" % (
                                               c["site"], c["place_postcode"], c["place_name"], c["place_id"], c["release"], how)})
                    f.flush(); have[o["key"]] = True; cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(threads)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dn.close()
    print("overture: %d companies with a candidate site, %d asked this run, %d sites tied" % (len(todo), cnt["asked"], cnt["found"]), flush=True)
    return cnt["found"]


def wd_pass(cos, have, w, f, threads, only=None):
    """2026-11-13: Wikidata's official website (P856) of an item of the company's very name in its own country (tools/wikidata_sites.py), kept when the
    site's own home page carries the name — the same check as the autocomplete's. Returns the number of sites tied."""
    import threading
    import tm_register as TM
    import wikidata_sites as WDS
    from concurrent.futures import ThreadPoolExecutor
    iso = lambda c: ("CA" if not (c or "").strip() else {"uk": "GB"}.get(CC.get(norm(c), norm(c) if len(norm(c)) == 2 else ""), CC.get(norm(c), norm(c) if len(norm(c)) == 2 else "")).upper())
    todo = [o for o in cos if o["key"] not in have]
    want = {iso(o.get("country")) for o in todo} & set(WDS.QC.values())
    if only:
        want &= set(only)
    if not todo or not want:
        return 0
    idx = WDS.build_index(os.path.join(os.environ.get("RUNNER_TEMP") or "/tmp", "wikidata_parts"), only=want, parts=["en", "P1448"])
    used = {urllib.parse.urlparse(s_.get("site") or "").hostname for s_ in have.values() if s_.get("site")}
    cands = []
    for o in todo:
        cc = iso(o.get("country"))
        hits = idx.get((cc, TM.nkey_x(o["name"]))) or {}
        if len(hits) == 1:
            h, (it, nm) = next(iter(hits.items()))
            if h not in used and "www." + h not in used:
                cands.append((o, h, it, nm, cc))
    lock, n = threading.Lock(), [0]

    def one(c):
        o, h, it, nm, cc = c
        try:
            said = home_says(h, core(o["name"]))
        except Exception:
            said = ""
        if said:
            with lock:
                w.writerow({"key": o["key"], "site": "https://%s/" % h, "read": TODAY, "quote": said,
                            "tied_by": "Wikidata gives %s as the official website of the organisation of that very name (%s, https://www.wikidata.org/wiki/%s; %s), and the site's own home page carries it: “%s”"
                                       % (h, nm, it, cc, said)})
                f.flush(); have[o["key"]] = {"site": "https://%s/" % h}; n[0] += 1
    with ThreadPoolExecutor(max(4, threads)) as ex:
        list(ex.map(one, cands))
    print("wikidata pass: %d companies with one candidate, %d sites tied" % (len(cands), n[0]), flush=True)
    return n[0]


def cmd_sites(a):
    import queue, threading
    os.makedirs(DIR, exist_ok=True)
    cos = companies()
    have = sites_on_file()
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=SITE_COLS)
    if new:
        w.writeheader()
    n_file = 0
    for k, r in tie_on_file([o for o in cos if o["key"] not in have]).items():
        w.writerow(r); have[k] = r; n_file += 1
    f.flush()
    try:
        wd_pass(cos, have, w, f, a.threads)
    except Exception as e:
        print("wikidata pass: %s" % str(e)[:160], flush=True)
    if getattr(a, "overture", False):
        overture_pass(cos, have, w, f, a.overture_minutes, a.threads)
        addr_pass(cos, have, w, f, a.overture_minutes, a.threads)  # 2026-11-13: places at the company's own address
    if getattr(a, "guess", False):
        guess_pass(cos, have, w, f, a.guess_minutes, a.threads)
    done = set()
    if os.path.exists(SDONE):
        done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")}
    todo = [o for o in cos if o["key"] not in have and o["key"] not in done]
    todo.sort(key=lambda o: -float(o["fee_total"] or 0))  # the largest bills first
    t_end = time.time() + 60 * a.minutes
    GROUPS.clear()
    for o in cos:
        c_ = core(o["name"])
        if c_:
            GROUPS.setdefault(group_key(c_), set()).add(norm(o.get("country") or ""))
    lock, q, cnt = threading.Lock(), queue.Queue(maxsize=64), collections.Counter()
    dn = open(SDONE, "a", encoding="utf-8")

    def producer():  # the autocomplete, one request a second
        for o in todo:
            if time.time() > t_end:
                break
            n = core(o["name"])
            if len(n) < 3 or (len(n.split()) == 1 and len(n) < 5):
                with lock:
                    dn.write("%s\t\n" % o["key"]); dn.flush()
                continue
            cands = [((s_.get("domain") or "").lower().strip(), core(s_.get("name") or "")) for s_ in (suggest(n) or [])[:5]]
            # a company whose register address is in Canada is the Canadian company (Servier Canada Inc., ViiV Healthcare ULC): its parent's .com site and
            # mailbox are another organisation's — only a .ca site under its very name is taken
            ca = norm(o.get("country") or "") in ("canada", "ca")
            # one name, entities in several countries (Stryker GmbH in Switzerland, Stryker in the United States; Abbott GmbH, Abbott Laboratories):
            # the group's .com is the parent's — such an entity is tied only to a site on its own country's ending
            multi = len(GROUPS.get(group_key(n), set()) - {norm(o.get("country") or "")}) > 0
            q.put((o, n, [d for d, sn in cands if d and not BAD.search(d) and sn == n and (not ca or d.endswith(".ca")) and domain_fits(d, n, o.get("country") or "")
                          and not (multi and d.rsplit(".", 1)[-1] in GENERIC)]))
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
                    said = home_says(d, n)
                except Exception:
                    said = ""
                if said:
                    hit = d
                    break
            with lock:
                dn.write("%s\t%s\n" % (o["key"], hit)); dn.flush()
                if hit:
                    w.writerow({"key": o["key"], "site": "https://%s/" % hit, "read": TODAY, "quote": said,
                                "tied_by": "the company-name autocomplete (Clearbit) proposes %s under the company's very name (%s, legal forms aside), and the site's own home page carries it: “%s”" % (hit, n, said)})
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


def lead_of(o, s):
    reg = o["register"]
    cats = json.loads(o["by_category"] or "{}")
    key = "lead:" + hashlib.sha1(("hc|%s" % o["key"]).encode()).hexdigest()[:16]
    fee = float(o["fee_total"] or 0)
    parts = ["%d × $%s (%s)" % (v, format(FEE[c], ",.0f"), FEE_WORD[c]) for c, v in sorted(cats.items(), key=lambda kv: -FEE[kv[0]]) if v]
    if reg == "dpd":
        what = "%d drug%s on the Canadian market" % (o["products"] and int(o["products"]), "" if int(o["products"]) == 1 else "s")
        quote_period, period_url = DRUG_INV_Q, DRUG_GUIDE_URL
        unit_cat = "rx" if cats.get("rx") else "otc" if cats.get("otc") else "dis"
        unit_q, unit_url = DRUG_FEE_Q, DRUG_FEE_URL
        delivery = "an invoice from Health Canada every October 1 for the year to come: “%s” “%s” (%s, read %s)" % (DRUG_INV_Q, DRUG_WHO_Q, DRUG_GUIDE_URL, READ)
        terms = "“%s” (%s, read %s)" % (DRUG_DUE_Q, DRUG_GUIDE_URL, READ)
        calc = ("calculated — $%s a year in all: %s, the fees Health Canada publishes as of April 1, 2026 (%s, read %s) for the drugs this company has on the "
                "market in the Drug Product Database (status Marketed, read %s); a small business is billed 25%% less (“%s”, %s) — whether this company is one is not published"
                % (format(fee, ",.0f"), " + ".join(parts), DRUG_FEE_URL, READ, TODAY, DRUG_SMALL_Q, DRUG_GUIDE_URL))
        title = "Right to sell %s (Health Canada, Drug Product Database: %s)" % (what, o["examples"][:200])
        reg_label = "Health Canada's Drug Product Database (the owner of each drug identification number, its status today)"
    elif reg == "mdel":
        no = o["key"].split(":")[-1]
        acts = o["examples"].split(": ", 1)[-1]
        what = "a medical device establishment licence (MDEL %s: %s)" % (no, acts)
        quote_period, period_url = MDEL_ALR_Q, MDEL_ALR_URL
        unit_cat, unit_q, unit_url = "mdel", MDEL_FEE_Q, MDEL_FEE_URL
        delivery = ("an invoice from Health Canada at each yearly licence review: “%s” (%s, read %s) — “%s” (%s, read %s)"
                    % (MDEL_ALR_Q, MDEL_ALR_URL, READ, MDEL_INV_Q, MDEL_GUIDE_URL, READ))
        terms = "“%s” “%s” (%s, read %s)" % (MDEL_DUE_Q, MDEL_LATE_Q, MDEL_GUIDE_URL, READ)
        calc = ""  # the published fee of the one licence is the bill: no calculation
        title = "Medical device establishment licence %s (Health Canada, MDEL listing: %s)" % (no, acts)
        reg_label = "Health Canada's Medical Devices Establishment Licence listing (every holder of an active licence)"
    else:
        what = "%d licensed Class II-IV medical device%s" % (int(o["products"]), "" if int(o["products"]) == 1 else "s")
        quote_period, period_url = MD_PERIOD_Q, MD_GUIDE_URL
        unit_cat, unit_q, unit_url = "md", MD_FEE_Q, MD_FEE_URL
        delivery = "an invoice from Health Canada for the licences renewed each November 1: “%s” (%s, guidance of 2013-11-18, read %s)" % (MD_INV_Q, MD_GUIDE_URL, READ)
        terms = "within 30 days of the invoice: “%s” (%s, read %s)" % (MD_INV_Q, MD_GUIDE_URL, READ)
        calc = ("calculated — $%s a year in all: %s, the fee Health Canada publishes as of April 1, 2026 (%s, read %s) for each licence of this manufacturer issued and not "
                "cancelled in the Medical Devices Active Licence Listing (read %s)" % (format(fee, ",.0f"), " + ".join(parts), MD_FEE_URL, READ, TODAY))
        title = "Right to sell %s (Health Canada, Medical Devices Active Licence Listing: %s)" % (what, o["examples"][:200])
        reg_label = "Health Canada's Medical Devices Active Licence Listing (the manufacturer of each licensed device)"
    s = dict(s, tied_by=no_mail(s.get("tied_by")), quote=no_mail(s.get("quote")))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": "Health Canada",
           "canada_field_value": "membership / statutory fee relationship: %s of the Canadian body (Health Canada)=%s (as printed on %s, read %s); Health Canada: “%s” (%s)"
                                 % ("licence holder" if reg == "mdel" else "right-to-sell holder", HC_ADDRESS, PAY_URL, READ, quote_period, period_url),
           "evidence_dataset": o["record_url"], "latest_record_date": TODAY}
    det = {"key": key, "platform": "hc_register", "record_url": o["record_url"], "vendor": "Health Canada", "record_date": TODAY,
           "start": o.get("first_on_market") or "", "end": "", "reference": ("MDEL %s" % o["key"].split(":")[-1]) if reg == "mdel" else o["key"].split(":")[-1], "title": title,
           "vendor_address": "%s (as printed on %s)" % (REMIT_Q, PAY_URL), "vendor_site": HC_SITE,
           "member_address_quote": o["address"], "register_label": reg_label,
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": ("Health Canada MDEL %s, %s" % (o["key"].split(":")[-1], o["examples"].split(":")[0].split("(")[-1].rstrip(")")))
                              if reg == "mdel" else "Health Canada %s company %s" % ("DPD" if reg == "dpd" else "MDALL", o["key"].split(":")[-1]),
                              "label": "%s, read %s" % (reg_label, TODAY)},
           "hc_register": reg, "hc_products": int(o["products"]), "hc_by_category": cats, "hc_examples": o["examples"], "hc_what": what,
           "fee_unit": "C$%s a year for each %s (as of April 1, 2026)" % (format(FEE[unit_cat], ",.0f"), FEE_WORD[unit_cat]),
           "fee_unit_basis": "Health Canada's own fee page: “%s” (%s, read %s)" % (unit_q, unit_url, READ),
           "fee_calculated": calc, "bill_delivery": delivery, "bill_terms": terms,
           "bill_items": ("the yearly fee of %s, at its annual licence review" % what) if reg == "mdel" else
                         "the yearly fee for the right to sell %s%s (%s)" % (what, "" if reg == "dpd" else " in Canada", o["examples"][:200]),
           "fee_basis": "%s (%s)" % (unit_q, unit_url), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    cos, sites = companies(), sites_on_file()
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_hc_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    hosts = collections.Counter(urllib.parse.urlparse(s["site"]).hostname for s in sites.values() if s.get("site"))
    rows, dets, by = [], [], collections.Counter()
    for o in cos:
        s = sites.get(o["key"])
        if not s or not s.get("site"):
            continue
        if hosts[urllib.parse.urlparse(s["site"]).hostname] > 3:
            by["site shared by more than three companies (a group's site): left out"] += 1
            continue
        row, det = lead_of(o, s)
        if row["buyer_key"] in have:
            continue
        have.add(row["buyer_key"]); rows.append(row); dets.append(det); by["new lead (%s)" % o["register"]] += 1
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_hc_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_hc_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("Health Canada leads on file: %d (+%d this run: %s)" % (len(have), len(rows), dict(by)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--work", default=os.path.expanduser("~/cch-sources/hc"))
    p = sub.add_parser("build"); p.add_argument("--work", default=os.path.expanduser("~/cch-sources/hc"))
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=50); p.add_argument("--threads", type=int, default=12)
    p.add_argument("--overture", action="store_true", help="first the sites an Overture Maps place lists under the company's name at its postal code (tools/overture_names.py)")
    p.add_argument("--overture-minutes", type=float, default=40)
    p.add_argument("--guess", action="store_true", help="then the company's very name as a domain, kept only on the register's postal code printed on the site")
    p.add_argument("--guess-minutes", type=float, default=30)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()

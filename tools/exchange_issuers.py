#!/usr/bin/env python3
"""Companies listed on the Toronto Stock Exchange and the TSX Venture Exchange -> relationship leads (cloud; no AI, no search engine).

Every listed issuer pays its exchange an annual sustaining fee, on an invoice. Toronto Stock Exchange's Listing Fee Schedule (effective
August 1, 2025): "The annual sustaining fee is invoiced in February of each year and calculated on the basis of the Market Capitalization …";
for a corporate issuer: "$0 up to $100M $12,000 0.013% $100M up to $300M $25,000 0.011% $300M up to $700M $47,000 0.009% $700M and above
$83,000 0.007% Maximum fee $150,000". TSX Venture Exchange's fee schedule: "the annual sustaining fee is payable for each calendar year and
is equal to $5,500 plus 0.011% of the Issuer's Aggregate Market Capitalization … up to a maximum of $90,000", and "If an Issuer fails to
submit its annual sustaining fee by the remittance date specified by the Exchange in its invoice, an additional monthly fee of 1.5% …".
So every listed company is billed $5,500 a year at the least — over the $5,000 mark — on an invoice from a Canadian body. The exchanges
publish every month the list of their listed issuers (name, symbol, market capitalization, sector, head-office region, listing date), and
the issuer's website is the one the company-name autocomplete gives under its name, kept only when its own home page prints
its symbol on the exchange (or its name in its title). The bill's amount is calculated from the published fee and the market
capitalization the list gives (the fee itself uses the market capitalization of the last trading day of the year: an estimate, labelled).

Left out: exchange-traded products, closed-end funds and depositary receipts (their manager or a bank pays, per product), capital pool
companies and SPACs (shells). How the invoice is paid is not printed in the fee schedules: the row says it is by the kind of bill.

  pull --work W          the exchanges' list of listed companies (one workbook) -> W/listed.xlsx
  build --work W         -> data/incoming/claude/exchange/issuers.csv.gz
  sites --minutes M      each issuer's website (the name autocomplete, one request a second; the home page prints its symbol) -> issuer_sites.csv
  leads --stamp S        -> lead_shards/leads_xc_S.gz + details_xc_S.gz (new leads only)
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, sys, time, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "exchange")
SHARDS = os.path.join(INC, "lead_shards")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
READ = "2026-11-12"
LIST_URL = "https://www.tsx.com/en/resource/571"
LIST_PAGE = "https://www.tsx.com/en/listings/current-market-statistics"
TSX_FEES = "https://www.tsx.com/en/resource/2939"
TSXV_FEES = "https://www.tsx.com/en/resource/2937"
ADDR = "TMX Group, 300 – 100 Adelaide Street West, Toronto, Ontario M5H 1S3"
ADDR_Q = "Privacy Compliance Officer TMX Group 300 – 100 Adelaide Street West Toronto, Ontario Canada M5H 1S3"
ADDR_URL = "https://www.tmx.com/en/privacy-policy"
TSX_INV_Q = ("The annual sustaining fee is invoiced in February of each year and calculated on the basis of the Market Capitalization of all TSX listed "
             "securities that are issued and outstanding on the Closing Price of such securities as at the last trading day of the previous calendar year.")
TSX_TIER_Q = ("$0 up to $100M $12,000 0.013% $100M up to $300M $25,000 0.011% $300M up to $700M $47,000 0.009% $700M and above $83,000 0.007% "
              "Maximum fee $150,000")
TSXV_Q = ("the annual sustaining fee is payable for each calendar year and is equal to $5,500 plus 0.011% of the Issuer’s Aggregate Market Capitalization "
          "(plus applicable taxes) up to a maximum of $90,000 (plus applicable taxes).")
TSXV_INV_Q = ("If an Issuer fails to submit its annual sustaining fee by the remittance date specified by the Exchange in its invoice, an additional monthly "
              "fee of 1.5% of the outstanding annual sustaining fee will be payable by the Issuer for each full month that the annual sustaining fee remains unpaid.")
NAME = {"TSX": "Toronto Stock Exchange (TSX Inc., TMX Group)", "TSXV": "TSX Venture Exchange (TMX Group)", "CSE": "Canadian Securities Exchange (CNSX Markets Inc.)"}
# The Canadian Securities Exchange (2026-11-12): its own list of listed companies, the one its "Listed Companies" page loads (one request), names each
# issuer, its symbol, sector, listing date and its website; its fee page: a monthly maintenance fee, $1,000 a month at the least.
CSE_LIST = "https://thecse.com/api/webapi/listed-companies/"
CSE_LIST_PAGE = "https://thecse.com/listing/listed-companies/"
CSE_FEES = "https://thecse.com/listing/fees-policies-forms/"
CSE_ADDR = "Canadian Securities Exchange (CNSX Markets Inc.), 100 King Street West, Suite 7210, Toronto, ON M5X 1E1"
CSE_ADDR_Q = "100 King Street West, Suite 7210 Toronto, ON, M5X 1E1"
CSE_ADDR_URL = "https://thecse.com/en/contact-us/"
CSE_DUE_Q = "The monthly maintenance fee is due on the first business day of each month the Issuer is listed."
CSE_MIN_Q = "The first monthly fee for a Listed Issuer will be the minimum base fee of $1,000."
CSE_ASSESS_Q = ("Each listed issuer will be assessed a monthly fee calculated as a percentage of its daily average market capitalization for the first 9 months "
                "of the previous calendar year.")
CSE_TABLE_Q = ("the fee table's cells: Market Capitalization / Monthly Fee / Annual Cost — $10 million or less / $1,000 / $12,000; Greater than $10 million / "
               "Base Fee $1,250 / Rate 0.001% of Market Capitalization / Minimum $16,200 / Maximum $125,000")
NOT_ISSUER = {"ETP", "CDR", "Closed-End Funds", "SPAC", "CPC"}
ISSUERS = os.path.join(DIR, "issuers.csv.gz")
SITES = os.path.join(DIR, "issuer_sites.csv")
SDONE = os.path.join(DIR, "issuer_sites_done.tsv")
COLS = ["key", "co_id", "exchange", "name", "ticker", "market_cap", "sector", "hq_location", "hq_region", "listing_type", "listing_date", "fee", "list_month", "site_listed"]
BAD = re.compile(r"linkedin|facebook|twitter|x\.com|instagram|youtube|sedar|tmx\.com|tsx\.com|google|wikipedia", re.I)


def fee_of(ex, mcap):
    m = float(mcap or 0)
    if ex == "TSXV":
        return min(90000.0, 5500.0 + 0.00011 * m)
    for base, fee, rate in ((700e6, 83000.0, 0.00007), (300e6, 47000.0, 0.00009), (100e6, 25000.0, 0.00011), (0.0, 12000.0, 0.00013)):
        if m >= base:
            return min(150000.0, fee + rate * (m - base))
    return 12000.0


def cmd_pull(a):
    os.makedirs(a.work, exist_ok=True)
    req = urllib.request.Request(LIST_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r, open(os.path.join(a.work, "listed.xlsx"), "wb") as f:
        f.write(r.read())
    print("pulled the list of listed companies (%d bytes)" % os.path.getsize(os.path.join(a.work, "listed.xlsx")))
    req = urllib.request.Request(CSE_LIST, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r, open(os.path.join(a.work, "cse_listed.json"), "wb") as f:
        f.write(r.read())
    print("pulled the Canadian Securities Exchange's list of listed companies (%d bytes)" % os.path.getsize(os.path.join(a.work, "cse_listed.json")))


def cmd_build(a):
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(a.work, "listed.xlsx"), read_only=True, data_only=True)
    out, why = [], collections.Counter()
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        hi = next(i for i, r in enumerate(rows) if r and r[0] == "Co_ID")
        hdr = [re.sub(r"\s+", " ", str(h)).strip() if h else "" for h in rows[hi]]
        col = lambda r, *names: next((r[hdr.index(n)] for n in names if n in hdr), None)
        month = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})", ws.title)
        for r in rows[hi + 1:]:
            if not r or not r[0]:
                continue
            ex = (col(r, "Exchange") or "").strip()
            sector = (col(r, "Sector") or "").strip()
            if sector in NOT_ISSUER or ex not in ("TSX", "TSXV"):
                why["%s: left out" % (sector or "no sector")] += 1
                continue
            mcap = col(r, *[h for h in hdr if h.startswith("Market Cap")]) or 0
            ld = str(col(r, "Listing Date") or "")
            out.append({"key": "xc:%s" % r[0], "co_id": r[0], "exchange": ex, "name": (col(r, "Name") or "").strip(), "ticker": (col(r, "Root Ticker") or "").strip(),
                        "market_cap": "%.0f" % float(mcap or 0), "sector": sector, "hq_location": col(r, "HQ Location") or "", "hq_region": col(r, "HQ Region") or "",
                        "listing_type": col(r, "Listing Type") or "", "listing_date": ("%s-%s-%s" % (ld[:4], ld[4:6], ld[6:8])) if re.fullmatch(r"\d{8}", ld) else "",
                        "fee": "%.0f" % fee_of(ex, mcap), "list_month": "%s %s" % (month.group(1), month.group(2)) if month else ""})
            why["%s issuer kept" % ex] += 1
    cj = os.path.join(a.work, "cse_listed.json")
    if os.path.exists(cj):
        by_issuer = {}
        for r in json.load(open(cj, encoding="utf-8")):
            if (r.get("security_type") or "") != "Equity" or (r.get("status") or "") != "Active" or (r.get("listing_market") or "CSE") != "CSE":
                why["CSE %s: left out" % (r.get("security_type") or "?")] += 1
                continue
            iid = re.sub(r"\D", "", (r.get("sedar_filings") or "").rsplit("/", 1)[-1]) or (r.get("symbol") or "").split(".")[0]
            by_issuer.setdefault(iid, []).append(r)
        for iid, rs in by_issuer.items():
            r = min(rs, key=lambda x: (len(x.get("symbol") or ""), len(x.get("security_name") or "")))  # the issuer's main class: URB before URB.A
            out.append({"key": "xc:cse:%s" % iid, "co_id": "cse:%s" % iid, "exchange": "CSE", "name": re.sub(r"\s+", " ", r.get("security_name") or "").strip(),
                        "ticker": (r.get("symbol") or "").strip(), "market_cap": "", "sector": r.get("sector") or "", "hq_location": "", "hq_region": "",
                        "listing_type": "tier %s" % r.get("tier") if r.get("tier") else "", "listing_date": r.get("listing_date") or "", "fee": "12000",
                        "list_month": TODAY, "site_listed": (r.get("company_website_url") or "").strip()})
            why["CSE issuer kept"] += 1
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(ISSUERS, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore"); w.writeheader(); w.writerows(out)
    print("listed issuers: %s; a yearly fee of $5,000 or more (calculated): %d" % (dict(why), sum(1 for o in out if float(o["fee"]) >= 5000)))


def issuers():
    with gzip.open(ISSUERS, "rt", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def sites_on_file():
    out = {}
    if os.path.exists(SITES):
        for r in csv.DictReader(open(SITES, encoding="utf-8", newline="")):
            out[r["key"]] = r
    return out


EXCH_ON_PAGE = (r"(?:TSX[\s\-\.]?V(?:enture)?(?:\s+Exchange)?|TSXV|TSX Venture Exchange|Toronto Stock Exchange|TSX|Bourse de Toronto|Bourse de croissance TSX|"
                r"Bourse TSX(?: de croissance)?)")
# "TSX: ABC", "TSXV:ABC", "TSX-V: ABC", "(TSX.V: ABC)", "listed for trading on the Toronto Stock Exchange under the symbol ABC", "cotée à la Bourse de
# Toronto sous le symbole « ABC »" — the symbol in capitals, as the list gives it (the match is case-sensitive)
TICKER_ON_PAGE = (EXCH_ON_PAGE + r"\s*(?:[:：\-–]|\)?[^.;<>]{0,60}?\b(?:under|sous)\b[^.;<>]{0,25}?\b(?:symbol|ticker|symbole)s?\b|\(symbol)?\s*[:：]?\s*[\"“”'«]?\s*%s\b")


# a listed company's home page links its investors' pages or names its exchange: a test the namesakes fail (a consultancy called "Boyd Group Services",
# an airline's restaurant microsite, a lens maker's rewards site — each named under the issuer's name by the autocomplete in the test of 2026-11-12)
INVESTOR_ON_PAGE = re.compile(r"\binvestors?\b|\binvestisseurs?\b|\bshareholders?\b|\bactionnaires?\b|\bTSX\b|Toronto Stock Exchange|Bourse de Toronto|\bNYSE\b|\bNASDAQ\b|"
                              r"annual report|rapport annuel|investor relations|relations (?:avec les )?investisseurs", re.I)


def name_is_domain(domain, core_):
    """the domain's label is the issuer's name (CAE at cae.com, BRP at brp.com: a listed company's short name is its brand) or its first two words,
    on a generic ending or .ca — or hc_registers' own test (a distinctive first word, then only words of the trade)"""
    import hc_registers as HR
    parts = domain.lower().split(".")
    if len(parts) < 2 or (parts[-1] not in HR.GENERIC and parts[-1] != "ca"):
        return False
    flat = re.sub(r"[^a-z0-9]", "", parts[-2])
    w = core_.split()
    return flat in (re.sub(r"[^a-z0-9]", "", core_), re.sub(r"[^a-z0-9]", "", " ".join(w[:2]))) or HR.domain_fits(domain, core_, "canada")


def ticker_on_home(domain, ticker, name):
    """the issuer's own home page prints its symbol on its exchange ("TSX: ABC", "TSXV: ABC", "… on the Toronto Stock Exchange under the symbol ABC");
    failing that, the domain is the issuer's very name, the page's title names it and the page links its investors' pages"""
    import client_lists as CL
    import hc_registers as HR
    site = "https://%s/" % domain
    if not CL.allowed(site):
        return ""
    page, final = CL.fetch(site)
    if not page:
        return ""
    import html as _h
    text = re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style).*?</\1>", " ", page[:400_000]))))
    m = re.search(TICKER_ON_PAGE % re.escape(ticker), text)
    if m:
        return "its home page prints “%s”" % text[max(0, m.start() - 40): m.end() + 20].strip()
    core_ = HR.core(name)
    if not core_ or not name_is_domain(domain, core_):
        return ""
    said = HR.home_says(domain, core_)
    inv = INVESTOR_ON_PAGE.search(text)
    if said and inv:
        return "the domain is its name, its home page names it (“%s”) and links its investors' pages (“%s”)" % (said[:120], text[max(0, inv.start() - 30): inv.end() + 30].strip())
    return ""


OVT = os.path.join(INC, "overture", "xc_candidates.csv")
ODONE = os.path.join(DIR, "issuer_overture_done.tsv")


def overture_pass(have):
    """the issuers for which an Overture Maps place lists a website under their very name in the province / state of their head office
    (tools/overture_names.py): kept by the same test as the autocomplete's (ticker_on_home)"""
    if not os.path.exists(OVT):
        print("overture: no candidates file (tools/overture_names.py query)", flush=True)
        return
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(OVT, encoding="utf-8", newline="")):
        by[r["key"]].append(r)
    done = {l.split("\t")[0] for l in open(ODONE, encoding="utf-8")} if os.path.exists(ODONE) else set()
    todo = [o for o in issuers() if o["key"] in by and o["key"] not in have and o["key"] not in done]
    new = not os.path.exists(SITES)
    found = 0
    with open(SITES, "a", encoding="utf-8", newline="") as f, open(ODONE, "a", encoding="utf-8") as dn:
        w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
        if new:
            w.writeheader()
        for o in todo:
            hit, why, c = "", "", None
            for c in by[o["key"]]:
                d = c["site"]
                if BAD.search(d):
                    continue
                try:
                    why = ticker_on_home(d, o["ticker"], o["name"])
                except Exception:
                    why = ""
                if why:
                    hit = d
                    break
            dn.write("%s\t%s\n" % (o["key"], hit)); dn.flush()
            if hit:
                w.writerow({"key": o["key"], "site": "https://%s/" % hit, "read": TODAY, "quote": why[:300],
                            "tied_by": "an Overture Maps place lists %s under the issuer's name in %s, the province / state of its head office (“%s”, place %s; "
                                       "Overture Maps Foundation open data, release %s), and %s" % (hit, o["hq_location"], c["place_name"], c["place_id"], c["release"], why)})
                f.flush(); have[o["key"]] = True; found += 1
    print("overture: %d issuers with a candidate site, %d asked, %d sites tied" % (len(by), len(todo), found), flush=True)


GDONE = os.path.join(DIR, "issuer_guess_done.tsv")


def guess_pass(have, minutes):
    """the issuer's very name as a domain (.com, then .ca), kept ONLY when the site's own home page prints the issuer's symbol on its exchange
    ("TSXV: ABC", "TSX: ABC", "… under the symbol ABC") — never on the name alone"""
    import queue, socket, threading
    import hc_registers as HR
    done = {l.split("\t")[0] for l in open(GDONE, encoding="utf-8")} if os.path.exists(GDONE) else set()
    todo = [o for o in issuers() if o["key"] not in have and o["key"] not in done and o["exchange"] != "CSE" and o.get("ticker")]
    todo.sort(key=lambda o: -float(o["fee"]))
    t_end, lock, q, cnt = time.time() + 60 * minutes, threading.Lock(), queue.Queue(), collections.Counter()
    for o in todo:
        q.put(o)

    def doms(o):
        w = [x for x in HR.core(o["name"]).split() if x not in ("the",)]
        if not w:
            return []
        stems = []
        for st in ("".join(w), "".join(w[:2]), w[0] + "corp", w[0]):
            st = re.sub(r"[^a-z0-9]", "", st)
            if len(st) >= 4 and st not in stems:
                stems.append(st)
        return ["%s.%s" % (st, t) for st in stems[:4] for t in ("com", "ca")]

    def worker():
        socket.setdefaulttimeout(6)
        while time.time() < t_end:
            try:
                o = q.get_nowait()
            except queue.Empty:
                return
            hit = None
            for d in doms(o):
                try:
                    socket.getaddrinfo(d, 443)
                except Exception:
                    continue
                try:
                    import client_lists as CL
                    page, final = (CL.fetch("https://%s/" % d) if CL.allowed("https://%s/" % d) else ("", ""))
                except Exception:
                    page = ""
                if not page:
                    continue
                import html as _h
                text = re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style).*?</\1>", " ", page[:400_000]))))
                m = re.search(TICKER_ON_PAGE % re.escape(o["ticker"]), text)
                if m:
                    hit = (d, "its home page prints “%s”" % text[max(0, m.start() - 40): m.end() + 20].strip())
                    break
            with lock:
                with open(GDONE, "a", encoding="utf-8") as dn:
                    dn.write("%s\t%s\n" % (o["key"], hit[0] if hit else ""))
                cnt["asked"] += 1
                if hit:
                    new = not os.path.exists(SITES)
                    with open(SITES, "a", encoding="utf-8", newline="") as f:
                        w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
                        if new:
                            w.writeheader()
                        w.writerow({"key": o["key"], "site": "https://%s/" % hit[0], "read": TODAY, "quote": hit[1][:300],
                                    "tied_by": "the issuer's very name as a domain (%s), and %s" % (hit[0], hit[1])})
                    have[o["key"]] = True; cnt["found"] += 1

    ts = [threading.Thread(target=worker, daemon=True) for _ in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("name as a domain: %d issuers without a site, %d asked, %d sites tied (the symbol on the exchange printed on the home page)" % (len(todo), cnt["asked"], cnt["found"]), flush=True)


def cmd_sites(a):
    """each issuer's website: the company-name autocomplete (one request a second) proposes a domain under the issuer's very name, and the
    domain's own home page prints the issuer's symbol on its exchange, or its name in its title"""
    import hc_registers as HR
    os.makedirs(DIR, exist_ok=True)
    have = sites_on_file()
    done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")} if os.path.exists(SDONE) else set()
    fresh = []
    for o in issuers():
        u = (o.get("site_listed") or "").strip()
        if o["key"] in have or not u:
            continue
        u = u if re.match(r"(?i)https?://", u) else "https://" + u
        h = (urllib.parse.urlparse(u).hostname or "").lower()
        if not h or "." not in h or BAD.search(h):
            continue
        r0 = {"key": o["key"], "site": "https://%s/" % (h[4:] if h.startswith("www.") else h), "read": TODAY,
              "tied_by": "the exchange's own list of listed companies gives %s as the company's website (%s, read %s)" % (o["site_listed"], CSE_LIST_PAGE, TODAY),
              "quote": "company_website_url: %s" % o["site_listed"]}
        have[o["key"]] = r0
        fresh.append(r0)
    if fresh:
        new0 = not os.path.exists(SITES)
        with open(SITES, "a", encoding="utf-8", newline="") as f0:
            w0 = csv.DictWriter(f0, fieldnames=["key", "site", "tied_by", "quote", "read"])
            if new0:
                w0.writeheader()
            w0.writerows(fresh)
    print("issuer sites from the exchange's own list (Canadian Securities Exchange): %d new" % len(fresh), flush=True)
    if getattr(a, "overture", False):
        overture_pass(have)
    if getattr(a, "guess", False):
        guess_pass(have, a.guess_minutes)
    # 2026-11-13: Wikidata's official website of an item of the issuer's very name (its head office's country; Canada when the list names none),
    # kept when the site's own home page carries the name
    try:
        _cc = lambda o: "United States" if re.search(r"\b(?:USA|United States|U\.S\.)\b", (o.get("hq_region") or "") + " " + (o.get("hq_location") or "")) else (
            "United Kingdom" if re.search(r"\b(?:UK|United Kingdom|England)\b", (o.get("hq_region") or "") + " " + (o.get("hq_location") or "")) else
            "Australia" if re.search(r"\bAustralia\b", (o.get("hq_region") or "") + " " + (o.get("hq_location") or "")) else "Canada")
        new1 = not os.path.exists(SITES)
        with open(SITES, "a", encoding="utf-8", newline="") as f1:
            w1 = csv.DictWriter(f1, fieldnames=["key", "site", "tied_by", "quote", "read"])
            if new1:
                w1.writeheader()
            HR.wd_pass([dict(o, country=_cc(o)) for o in issuers()], have, w1, f1, 8, only={"CA", "US", "GB", "AU"})
    except Exception as e:
        print("wikidata pass: %s" % str(e)[:160], flush=True)
    todo = [o for o in issuers() if o["key"] not in have and o["key"] not in done and o["exchange"] != "CSE"]
    todo.sort(key=lambda o: -float(o["fee"]))
    new = not os.path.exists(SITES)
    f = open(SITES, "a", encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=["key", "site", "tied_by", "quote", "read"])
    if new:
        w.writeheader()
    dn = open(SDONE, "a", encoding="utf-8")
    t_end, n, found = time.time() + 60 * a.minutes, 0, 0
    for o in todo:
        if time.time() > t_end:
            break
        core_ = HR.core(o["name"])
        if len(core_) < 3:
            dn.write("%s\t\n" % o["key"]); dn.flush()
            continue
        cands = [((x.get("domain") or "").lower().strip(), HR.core(x.get("name") or "")) for x in (HR.suggest(core_) or [])[:5]]
        n += 1
        hit, why = "", ""
        for d, sn in cands:
            if not d or HR.BAD.search(d) or BAD.search(d):
                continue
            if sn != core_ and not (core_.startswith(sn + " ") and len(sn) >= 5):
                continue  # the autocomplete's company is another one
            try:
                why = ticker_on_home(d, o["ticker"], o["name"])
            except Exception:
                why = ""
            if why:
                hit = d
                break
        dn.write("%s\t%s\n" % (o["key"], hit)); dn.flush()
        if hit:
            w.writerow({"key": o["key"], "site": "https://%s/" % hit, "read": TODAY,
                        "tied_by": "the company-name autocomplete (Clearbit) proposes %s under the issuer's name (%s), and %s" % (hit, core_, why),
                        "quote": why[:300]})
            f.flush(); found += 1
    dn.close(); f.close()
    print("issuer sites: %d on file before; the autocomplete asked %d times this run, %d sites tied" % (len(have), n, found), flush=True)


def money(v):
    return "C$" + format(v, ",.0f")


def lead_of(o, s):
    key = "lead:" + hashlib.sha1(("xc|%s" % o["co_id"]).encode()).hexdigest()[:16]
    ex, fee, mcap = o["exchange"], float(o["fee"] or 0), float(o["market_cap"] or 0)
    biller = NAME[ex]
    short = biller.split(" (")[0]
    if ex == "CSE":
        addr, addr_q, addr_url, vsite, list_url, list_page = CSE_ADDR, CSE_ADDR_Q, CSE_ADDR_URL, "https://thecse.com/", CSE_LIST, CSE_LIST_PAGE
        cfv_q, unit_url = CSE_DUE_Q, CSE_FEES
        basis = "the Canadian Securities Exchange's listing fees: “%s” “%s” — %s (%s, read %s)" % (CSE_MIN_Q, CSE_ASSESS_Q, CSE_TABLE_Q, CSE_FEES, READ)
        calc = ("calculated — at least C$12,000 a year (C$1,000 a month): the exchange's published minimum monthly fee; above a market capitalization of $10 million "
                "the fee is $1,250 a month plus 0.001 %% of the market capitalization, C$16,200 to C$125,000 a year — the exchange's list gives no market capitalization (%s)" % CSE_FEES)
        fee_unit = "C$1,000 a month at the least (the exchange's published minimum base fee)"
        delivery = "a monthly maintenance fee, due on the first business day of each month: “%s” (%s, read %s)" % (CSE_DUE_Q, CSE_FEES, READ)
        terms = "due on the first business day of each month the issuer is listed: “%s” (%s, read %s)" % (CSE_DUE_Q, CSE_FEES, READ)
        items = "the monthly maintenance fee for the listing of %s on the Canadian Securities Exchange (symbol %s)" % (o["name"], o["ticker"])
        fee_words = "a monthly maintenance fee, due on the first business day of each month"
        reg_id = "CSE symbol %s (CSE issuer %s)" % (o["ticker"], o["co_id"].split(":")[-1])
        unit_q = "%s %s" % (CSE_MIN_Q, CSE_TABLE_Q)
    else:
        addr, addr_q, addr_url, vsite, list_url, list_page = ADDR, ADDR_Q, ADDR_URL, "https://www.tsx.com/", LIST_URL, LIST_PAGE
        if ex == "TSX":
            unit_q, unit_url, cfv_q = TSX_TIER_Q, TSX_FEES, TSX_INV_Q
            basis = "Toronto Stock Exchange's Listing Fee Schedule (effective August 1, 2025), annual sustaining fee of a corporate issuer: “%s” (%s, read %s)" % (TSX_TIER_Q, TSX_FEES, READ)
            more = "; an eligible international interlisted issuer pays 25 % less and an eligible secondary market issuer 50 % less, and $1,000 is added for each supplemental security — not known here"
        else:
            unit_q, unit_url, cfv_q = TSXV_Q, TSXV_FEES, TSXV_INV_Q
            basis = "TSX Venture Exchange's fee schedule: “%s” (%s, read %s)" % (TSXV_Q, TSXV_FEES, READ)
            more = ""
        calc = ("calculated — about %s a year: the exchange's published annual sustaining fee applied to the issuer's market capitalization of %s on %s as the exchange's "
                "own list gives it (%s); the fee is calculated on the market capitalization of the last trading day of the year, so the bill differs%s"
                % (money(fee), money(mcap), o["list_month"] or "the list's date", LIST_URL, more))
        fee_unit = "%s a year at the least (the exchange's published minimum: %s)" % ("C$12,000" if ex == "TSX" else "C$5,500", "the base fee of its first tier" if ex == "TSX" else "$5,500 plus 0.011 % of the market capitalization")
        delivery = "an invoice from the exchange every year: “%s” (%s, read %s)" % (cfv_q, unit_url, READ)
        terms = ("by the remittance date the exchange's invoice gives, 1.5 %% a month after it: “%s” (%s, read %s)" % (TSXV_INV_Q, TSXV_FEES, READ)) if ex == "TSXV" else ""
        items = "the annual sustaining fee for the listing of %s on %s (symbol %s)" % (o["name"], short, o["ticker"])
        fee_words = "an annual sustaining fee, on the exchange's invoice"
        reg_id = "%s symbol %s (TMX company id %s)" % (ex, o["ticker"], o["co_id"])
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": biller,
           "canada_field_value": "membership / statutory fee relationship: listed issuer of the Canadian body (%s)=%s (as printed on %s, read %s); %s: “%s” (%s)"
                                 % (biller, addr, addr_url, READ, short, cfv_q, unit_url),
           "evidence_dataset": list_page, "latest_record_date": TODAY}
    det = {"key": key, "platform": "exchange_register", "record_url": list_url, "vendor": biller, "record_date": TODAY, "start": o["listing_date"], "end": "",
           "reference": "symbol %s (%s)" % (o["ticker"], ex),
           "title": "Listing on %s, symbol %s — %s%s" % (short, o["ticker"], o["sector"], (", head office %s, %s" % (o["hq_location"], o["hq_region"])) if o.get("hq_location") else ""),
           "vendor_address": "%s (as printed on %s, read %s)" % (addr_q, addr_url, READ), "vendor_site": vsite,
           "member_address_quote": "", "register_label": "the exchange's list of listed companies (%s, %s)" % (o["list_month"], list_page),
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": reg_id, "label": "the list of companies listed on %s, %s" % (short, o["list_month"])},
           "xc_exchange": ex, "xc_ticker": o["ticker"], "xc_market_cap": mcap, "xc_sector": o["sector"], "xc_fee_words": fee_words,
           "fee_unit": fee_unit, "fee_unit_basis": basis, "fee_calculated": calc, "bill_delivery": delivery, "bill_terms": terms, "bill_items": items,
           "fee_basis": "%s (%s)" % (unit_q, unit_url), "site_named_by": s["tied_by"], "site_tied_to_holder_by": s["tied_by"], "site_quote": s.get("quote") or ""}
    return row, det


def cmd_leads(a):
    os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    sites = sites_on_file()
    have = set()
    for p in glob.glob(os.path.join(SHARDS, "leads_xc_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    hosts = collections.Counter(urllib.parse.urlparse(s["site"]).hostname for s in sites.values() if s.get("site"))
    rows, dets, by = [], [], collections.Counter()
    for o in issuers():
        s = sites.get(o["key"])
        if not s or not s.get("site"):
            continue
        if hosts[urllib.parse.urlparse(s["site"]).hostname] > 2:
            by["site shared by more than two issuers: left out"] += 1
            continue
        row, det = lead_of(o, s)
        if row["buyer_key"] in have:
            continue
        have.add(row["buyer_key"]); rows.append(row); dets.append(det); by["new lead (%s)" % o["exchange"]] += 1
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_xc_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        with gzip.open(os.path.join(SHARDS, "details_xc_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    print("exchange issuer leads on file: %d (+%d this run: %s)" % (len(have), len(rows), dict(by)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--work", required=True)
    p = sub.add_parser("build"); p.add_argument("--work", required=True)
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=60)
    p.add_argument("--overture", action="store_true", help="first the sites an Overture Maps place lists under the issuer's name in its province / state (tools/overture_names.py)")
    p.add_argument("--guess", action="store_true", help="then the issuer's very name as a domain, kept only on its symbol printed on the home page")
    p.add_argument("--guess-minutes", type=float, default=25)
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()

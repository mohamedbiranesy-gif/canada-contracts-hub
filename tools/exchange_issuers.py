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
NAME = {"TSX": "Toronto Stock Exchange (TSX Inc., TMX Group)", "TSXV": "TSX Venture Exchange (TMX Group)"}
NOT_ISSUER = {"ETP", "CDR", "Closed-End Funds", "SPAC", "CPC"}
ISSUERS = os.path.join(DIR, "issuers.csv.gz")
SITES = os.path.join(DIR, "issuer_sites.csv")
SDONE = os.path.join(DIR, "issuer_sites_done.tsv")
COLS = ["key", "co_id", "exchange", "name", "ticker", "market_cap", "sector", "hq_location", "hq_region", "listing_type", "listing_date", "fee", "list_month"]
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
    os.makedirs(DIR, exist_ok=True)
    with gzip.open(ISSUERS, "wt", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out)
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


def cmd_sites(a):
    """each issuer's website: the company-name autocomplete (one request a second) proposes a domain under the issuer's very name, and the
    domain's own home page prints the issuer's symbol on its exchange, or its name in its title"""
    import hc_registers as HR
    os.makedirs(DIR, exist_ok=True)
    have = sites_on_file()
    done = {l.split("\t")[0] for l in open(SDONE, encoding="utf-8")} if os.path.exists(SDONE) else set()
    todo = [o for o in issuers() if o["key"] not in have and o["key"] not in done]
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
    ex, fee, mcap = o["exchange"], float(o["fee"]), float(o["market_cap"] or 0)
    biller = NAME[ex]
    if ex == "TSX":
        unit_q, unit_url, inv_q = TSX_TIER_Q, TSX_FEES, TSX_INV_Q
        basis = "Toronto Stock Exchange's Listing Fee Schedule (effective August 1, 2025), annual sustaining fee of a corporate issuer: “%s” (%s, read %s)" % (TSX_TIER_Q, TSX_FEES, READ)
        more = "; an eligible international interlisted issuer pays 25 % less and an eligible secondary market issuer 50 % less, and $1,000 is added for each supplemental security — not known here"
    else:
        unit_q, unit_url, inv_q = TSXV_Q, TSXV_FEES, TSXV_INV_Q
        basis = "TSX Venture Exchange's fee schedule: “%s” (%s, read %s)" % (TSXV_Q, TSXV_FEES, READ)
        more = ""
    calc = ("calculated — about %s a year: the exchange's published annual sustaining fee applied to the issuer's market capitalization of %s on %s as the exchange's "
            "own list gives it (%s); the fee is calculated on the market capitalization of the last trading day of the year, so the bill differs%s"
            % (money(fee), money(mcap), o["list_month"] or "the list's date", LIST_URL, more))
    row = {"buyer_key": key, "buyer_name": o["name"], "website": s["site"], "canadian_vendor_rows": 1, "example_vendor": biller,
           "canada_field_value": "membership / statutory fee relationship: listed issuer of the Canadian body (%s)=%s (as printed on %s, read %s); %s: “%s” (%s)"
                                 % (biller, ADDR, ADDR_URL, READ, biller.split(" (")[0], inv_q, unit_url),
           "evidence_dataset": LIST_PAGE, "latest_record_date": TODAY}
    det = {"key": key, "platform": "exchange_register", "record_url": LIST_URL, "vendor": biller, "record_date": TODAY, "start": o["listing_date"], "end": "",
           "reference": "symbol %s (%s)" % (o["ticker"], ex), "title": "Listing on %s, symbol %s — %s, head office %s, %s" % (biller.split(" (")[0], o["ticker"], o["sector"], o["hq_location"], o["hq_region"]),
           "vendor_address": "%s (as printed on %s, read %s)" % (ADDR_Q, ADDR_URL, READ), "vendor_site": "https://www.tsx.com/",
           "member_address_quote": "", "register_label": "the exchange's list of listed companies (%s, %s)" % (o["list_month"], LIST_URL),
           "buyer_register": {"legal_name": o["name"], "trade_names": [], "registry_id": "%s symbol %s (TMX company id %s)" % (ex, o["ticker"], o["co_id"]),
                              "label": "the list of companies listed on %s, %s" % (biller.split(" (")[0], o["list_month"])},
           "xc_exchange": ex, "xc_ticker": o["ticker"], "xc_market_cap": mcap, "xc_sector": o["sector"],
           "fee_unit": "%s a year at the least (the exchange's published minimum: %s)" % ("C$12,000" if ex == "TSX" else "C$5,500", "the base fee of its first tier" if ex == "TSX" else "$5,500 plus 0.011 % of the market capitalization"),
           "fee_unit_basis": basis, "fee_calculated": calc,
           "bill_delivery": "an invoice from the exchange every year: “%s” (%s, read %s)" % (inv_q, unit_url, READ),
           "bill_terms": ("by the remittance date the exchange's invoice gives, 1.5 % a month after it: “%s” (%s, read %s)" % (TSXV_INV_Q, TSXV_FEES, READ)) if ex == "TSXV" else "",
           "bill_items": "the annual sustaining fee for the listing of %s on %s (symbol %s)" % (o["name"], biller.split(" (")[0], o["ticker"]),
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
    p = sub.add_parser("leads"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "build": cmd_build, "sites": cmd_sites, "leads": cmd_leads}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Listed companies that state their TSX / TSX Venture listing on their OWN website: a paid, active service of TMX Group
(Toronto). No AI.

An exchange listing is a service the issuer pays for every year (TSX Company Manual, annual sustaining fees), and almost
every issuer prints its ticker on its own site ("TSX: ABC"). That is the same buyer-published evidence of an active
service relationship as <org>.brightspace.com is for D2L (tools/tech_relationships.py), with TMX Group Limited as the
Canada-headquartered vendor: "Privacy Compliance Officer TMX Group 300 – 100 Adelaide Street West Toronto, Ontario
Canada M5H 1S3" (https://www.tmx.com/privacy-policy, read 2026-11-03).

Steps (all polite: robots.txt, tsx.com crawl-delay 15 s, 2 s between TMX quote calls, 1 request / second / issuer site)
  1. issuer symbols and names from tsx.com's public company directory (TSX and TSXV; funds, ETFs, CDRs, split
     corporations and capital pool companies are dropped);
  2. each issuer's website from TMX's public quote service (money.tmx.com, no key);
  3. the issuer's own home page (then up to 3 investor / about pages) must print the ticker: "TSX: ABC", "TSXV: ABC",
     "TSX-V: ABC", "TSX Venture Exchange ... ABC" within 40 characters;
  4. one lead per issuer -> ~/cch-leads/socrata_tech_exchange.jsonl (record date = the day the page was read; tier T in
     rank.py) and a crawl task list ~/cch-crawl-some/exchange_sites.csv for tools/crawl_some.py (its invoicing mailbox).
  python3 tools/exchange_listing.py [--limit N] [--workers 12] [--step symbols|sites|all]
"""
import argparse, csv, hashlib, html, json, os, re, sys, threading, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
LEADS = os.path.expanduser("~/cch-leads")
CACHE = os.path.expanduser("~/cch-sources/tech/exchange")
OUT = os.path.join(LEADS, "socrata_tech_exchange.jsonl")
TASKS = os.path.expanduser("~/cch-crawl-some/exchange_sites.csv")
TODAY = time.strftime("%Y-%m-%d")
TMX_HQ = "Privacy Compliance Officer TMX Group 300 – 100 Adelaide Street West Toronto, Ontario Canada M5H 1S3"
TMX_HQ_URL = "https://www.tmx.com/privacy-policy"
NOT_ISSUER = re.compile(r"\b(ETF|CDR|Index|Fund|Split Corp|Capital Pool|Acquisition Corp|SPAC|Portfolio|Trust Units|"
                        r"Preferred|Debentures?|Warrants?|Receipts?|Notes|Bond|Units)\b", re.I)
TICKER = re.compile(r"\b(TSX[\s\-]?V|TSXV|TSX Venture(?: Exchange)?|TSX|Toronto Stock Exchange|Bourse de Toronto|"
                    r"Bourse de croissance TSX)\s*(?:[:：\-–]|under the (?:stock )?symbol|sous le symbole|\(symbol)?\s*[\"“”']?\s*([A-Z]{1,6}(?:\.[A-Z]{1,3})?)\b")
TICKER2 = re.compile(r"\b(?:symbol|ticker|symbole)s?\s*[\"“”']?\s*([A-Z]{1,6}(?:\.[A-Z]{1,3})?)\s*[\"“”']?\s*(?:on|at|sur|à la)\s+(?:the\s+)?"
                     r"(TSX Venture Exchange|TSX[\s\-]?V|TSXV|Toronto Stock Exchange|TSX|Bourse de Toronto|Bourse de croissance TSX)\b")
INVEST = re.compile(r"invest|actionnaire|stock|share|\bir\b|about|a-propos|corporate|company|entreprise|financial", re.I)
lock = threading.Lock()


def get_json(url, gap, data=None, key=""):
    os.makedirs(CACHE, exist_ok=True)
    cp = os.path.join(CACHE, hashlib.sha1((key or url).encode()).hexdigest()[:20] + ".json")
    if os.path.exists(cp):
        return json.load(open(cp))
    with lock:
        time.sleep(gap)
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode("utf-8", "replace"))
    json.dump(d, open(cp, "w"))
    return d


def symbols():
    """[(exchange, symbol, name)] from tsx.com's directory (crawl-delay 15 s per its robots.txt)"""
    out = []
    for ex in ("tsx", "tsxv"):
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0":
            try:
                d = get_json("https://www.tsx.com/json/company-directory/search/%s/%s" % (ex, ch if ch != "0" else "0-9"), 15)
            except Exception as e:
                print("directory %s %s: %s" % (ex, ch, e), flush=True)
                continue
            for r in d.get("results", []):
                nm = r.get("name") or ""
                if nm and not NOT_ISSUER.search(nm):
                    out.append((ex.upper(), r.get("symbol") or "", nm))
    seen, res = set(), []
    for t in out:
        if t[1] and t[1] not in seen:
            seen.add(t[1]); res.append(t)
    print(time.strftime("%H:%M"), "issuers: %d" % len(res), flush=True)
    return res


def website(symbol):
    q = {"operationName": "getQuoteBySymbol", "variables": {"symbol": symbol, "locale": "en"},
         "query": "query getQuoteBySymbol($symbol: String, $locale: String) { getQuoteBySymbol(symbol: $symbol, locale: $locale) { symbol name website exchangeName } }"}
    try:
        d = get_json("https://app-money.tmx.com/graphql", 2, json.dumps(q).encode(), key="quote:" + symbol)
    except Exception as e:
        return "", ""
    g = (d.get("data") or {}).get("getQuoteBySymbol") or {}
    return (g.get("website") or "").strip(), g.get("exchangeName") or ""


def host_of(u):
    h = (urllib.parse.urlparse(u if "//" in u else "https://" + u).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def text_of(page):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", page[:1_500_000])
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", t)))


def ticker_on(page, symbol):
    text = text_of(page)
    for m in TICKER.finditer(text):
        if m.group(2).split(".")[0] == symbol.split(".")[0]:
            return text[max(0, m.start() - 120):m.end() + 120].strip()[:300], m.group(1)
    for m in TICKER2.finditer(text):
        if m.group(1).split(".")[0] == symbol.split(".")[0]:
            return text[max(0, m.start() - 120):m.end() + 120].strip()[:300], m.group(2)
    return "", ""


def check(ex, symbol, name, site):
    h = host_of(site)
    if not h or h in ("tsx.com", "tmx.com") or not site.startswith("http"):
        return None, "no site"
    site = "https://%s/" % h if not site.startswith("http") else site
    if not CL.allowed(site):
        return None, "robots"
    page, final = CL.fetch(site)
    if not page:
        return None, "unreachable"
    q, which = ticker_on(page, symbol)
    url = final
    if not q:
        tried = 0
        for href, label in CL.anchors(page, final):
            p = urllib.parse.urlparse(href)
            if host_of(href) != host_of(final) or not INVEST.search(p.path + " " + label) or re.search(r"\.(pdf|jpg|png)$", p.path, re.I):
                continue
            if not CL.allowed(href):
                continue
            pg, fu = CL.fetch(href)
            tried += 1
            if pg:
                q, which = ticker_on(pg, symbol)
                if q:
                    url = fu
                    break
            if tried >= 3:
                break
    if not q:
        return None, "ticker not shown"
    dom = host_of(url)
    return {"platform": "tech_exchange", "domain": dom, "dataset_id": "%s:%s" % (ex, symbol),
            "dataset": "issuer states its %s listing on its own website" % ("TSX Venture Exchange" if ex == "TSXV" else "Toronto Stock Exchange"),
            "dataset_url": url, "publisher": name, "buyer_unit": "", "website": "https://%s/" % host_of(site),
            "vendor": "TMX Group Limited", "canada_field": "service of a Canada-HQ vendor seen on the buyer's own site (tech)",
            "canada_value": TMX_HQ, "row": {"record_date": TODAY, "observed_date": TODAY, "exchange": ex, "symbol": symbol,
                                            "signature": q, "signature_kind": "exchange listing printed on the issuer's own site (%s)" % which,
                                            "vendor_hq_url": TMX_HQ_URL, "listing_service": "annual sustaining listing fee (TSX Company Manual Part VIII / TSXV Policy 1.3)"}}, "ok"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--workers", type=int, default=12)
    a.add_argument("--step", default="all")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True); os.makedirs(os.path.dirname(TASKS), exist_ok=True)
    iss = symbols()
    if a.limit:
        iss = iss[:a.limit]
    if a.step == "symbols":
        return
    done = set()
    if os.path.exists(OUT + ".done"):
        done = {l.split("\t")[0] for l in open(OUT + ".done", encoding="utf-8")}
    todo = [t for t in iss if t[1] not in done]
    print(time.strftime("%H:%M"), "issuers to read: %d (%d done)" % (len(todo), len(done)), flush=True)
    stats = {"ok": 0, "no site": 0, "robots": 0, "unreachable": 0, "ticker not shown": 0}
    new = not os.path.exists(TASKS)
    tf = open(TASKS, "a", newline="", encoding="utf-8")
    tw = csv.writer(tf)
    if new:
        tw.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                     "known_general_email", "known_procurement_email", "contracts_in_dataset"])
    def one(t):
        ex, sym, name = t
        site, exname = website(sym)
        lead, st = check(ex, sym, name, site) if site else (None, "no site")
        with lock:
            stats[st] = stats.get(st, 0) + 1
            with open(OUT + ".done", "a", encoding="utf-8") as f:
                f.write("%s\t%s\t%s\t%s\n" % (sym, ex, site, st))
            if lead:
                with open(OUT, "a", encoding="utf-8") as f:
                    f.write(json.dumps(lead, ensure_ascii=False) + "\n")
                key = "lead:" + hashlib.sha1(("%s|%s" % (lead["domain"], lead["publisher"].lower())).encode()).hexdigest()[:16]
                tw.writerow(["CL-EX-%s" % sym, "", key, name, "", "", lead["website"], "", "", 1]); tf.flush()
            n = sum(stats.values())
            if n % 100 == 0:
                print(time.strftime("%H:%M"), n, stats, flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    json.dump(stats, open(OUT + ".stats", "w"))
    print(time.strftime("%H:%M"), "finished", stats, flush=True)


if __name__ == "__main__":
    main()

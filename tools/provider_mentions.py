#!/usr/bin/env python3
"""Canada-headquartered service providers NAMED on the buyer's own website as its current provider: the group-benefits
carrier or employee-assistance programme on its HR / careers pages, the academic tools on a university's teaching
pages. No AI. Buyer-published evidence of an active paid service (tier T, like tools/tech_relationships.py).

For each organisation of a task CSV (buyer_key, buyer_name, website): home page, then up to --pages internal pages whose
link text / path says careers, employment, benefits, human resources, total rewards, employee assistance, teaching &
learning, library e-resources, software. A vendor counts only when its name sits within 160 characters of a context
word that says it is the provider ("benefits ... provided by Sun Life", "Employee and Family Assistance Program through
Homewood Health", "exams graded in Crowdmark"), and never on a page about donors, scholarships, sponsors or news.

Each vendor's location comes from its OWN site: `--verify-hq` opens the pages listed below and keeps only the vendors
whose page prints the expected Canadian address (the quote is stored with every lead). Vendors whose page does not
show it are disabled for the run (printed).
Output: ~/cch-leads/socrata_provider_mention.jsonl (bridge picks it up); progress .done; robots.txt, 1 req/s/site.
  python3 tools/provider_mentions.py --verify-hq
  python3 tools/provider_mentions.py <tasks.csv> [--workers 16] [--pages 6] [--limit N]
"""
import argparse, csv, hashlib, html, json, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

LEADS = os.path.expanduser("~/cch-leads")
STATE = os.path.expanduser("~/cch-crawler-state")
OUT = os.path.join(LEADS, "socrata_provider_mention.jsonl")
HQ_CACHE = os.path.join(STATE, "provider_hq.json")
TODAY = time.strftime("%Y-%m-%d")
CANADA_FIELD = "service of a Canada-HQ vendor seen on the buyer's own site (tech)"
lock = threading.Lock()

# vendor key: (legal name, name regex on the buyer's page, HQ page URL, regex the HQ page must print, kind)
VENDORS = {
    "homewood": ("Homewood Health Inc.", r"Homewood\s+Health", "https://homewoodhealth.com/corporate/contact-us",
                 r"Guelph,?\s+(?:ON|Ontario)", "eap"),
    "telushealth": ("TELUS Health (LifeWorks)", r"TELUS\s+Health|LifeWorks|Morneau\s+Shepell|Shepell", "https://www.telus.com/en/health/contact-us",
                    r"(?:Montr[ée]al|Toronto|Vancouver),?\s+(?:QC|ON|BC|Qu[ée]bec|Ontario|British Columbia)", "eap"),
    "sunlife": ("Sun Life Assurance Company of Canada", r"Sun\s+Life", "https://www.sunlife.ca/en/about-us/contact-us/",
                r"(?:1 York Street|Toronto|Waterloo),?\s+(?:ON|Ontario)", "benefits"),
    "manulife": ("The Manufacturers Life Insurance Company (Manulife)", r"Manulife", "https://www.manulife.ca/about-us/contact-us.html",
                 r"(?:200 Bloor Street East|Toronto|Waterloo),?\s+(?:ON|Ontario)", "benefits"),
    "canadalife": ("The Canada Life Assurance Company", r"Canada\s+Life|Great-West\s+Life", "https://www.canadalife.com/contact-us.html",
                   r"(?:100 Osborne Street North|Winnipeg),?\s+(?:MB|Manitoba)", "benefits"),
    "gsc": ("Green Shield Canada", r"Green\s+Shield(?:\s+Canada)?|\bGSC\b", "https://www.greenshield.ca/en-ca/contact-us",
            r"(?:8677 Anchor Drive|Windsor),?\s+(?:ON|Ontario)", "benefits"),
    "medavie": ("Medavie Blue Cross", r"Medavie(?:\s+Blue\s+Cross)?", "https://www.medaviebc.ca/en/contact-us",
                r"(?:644 Main Street|Moncton),?\s+(?:NB|New Brunswick)", "benefits"),
    "pbc": ("Pacific Blue Cross", r"Pacific\s+Blue\s+Cross", "https://www.pac.bluecross.ca/contact-us",
            r"(?:4250 Canada Way|Burnaby),?\s+(?:BC|British Columbia)", "benefits"),
    "abc": ("Alberta Blue Cross", r"Alberta\s+Blue\s+Cross", "https://www.ab.bluecross.ca/contact-us.php",
            r"(?:10009 108 Street|Edmonton),?\s+(?:AB|Alberta)", "benefits"),
    "desjardins": ("Desjardins Financial Security Life Assurance Company", r"Desjardins(?:\s+(?:Insurance|Assurances|Financial\s+Security|S[ée]curit[ée]\s+financi[eè]re))",
                   "https://www.desjardins.com/ca/contact-us/", r"L[ée]vis,?\s+(?:QC|Qu[ée]bec)", "benefits"),
    "beneva": ("Beneva Inc. (SSQ Insurance)", r"Beneva|SSQ\s+(?:Insurance|Assurance)", "https://www.beneva.ca/en/contact-us",
               r"Qu[ée]bec(?: City)?,?\s+(?:QC|Qu[ée]bec)", "benefits"),
    "ia": ("Industrial Alliance Insurance and Financial Services Inc. (iA Financial Group)", r"Industrial\s+Alliance|iA\s+Financial(?:\s+Group)?|iA\s+Groupe\s+financier",
           "https://ia.ca/contact-us", r"(?:1080,? Grande All[ée]e|Qu[ée]bec),?\s+(?:QC|Qu[ée]bec)", "benefits"),
    "equitable": ("The Equitable Life Insurance Company of Canada", r"Equitable\s+Life", "https://www.equitable.ca/en/contact-us",
                  r"(?:1 Westmount Road North|Waterloo),?\s+(?:ON|Ontario)", "benefits"),
    "empire": ("The Empire Life Insurance Company", r"Empire\s+Life", "https://www.empire.ca/contact-us",
               r"(?:259 King Street East|Kingston),?\s+(?:ON|Ontario)", "benefits"),
    "cooperators": ("Co-operators Life Insurance Company", r"Co-operators", "https://www.cooperators.ca/en/contact-us",
                    r"(?:130 Macdonell|Guelph),?\s+(?:ON|Ontario)", "benefits"),
    "crowdmark": ("Crowdmark, Inc.", r"Crowdmark", "https://www.crowdmark.com/privacy/", r"Toronto,?\s+(?:ON|Ontario)", "academic"),
    "maplesoft": ("Maplesoft (Waterloo Maple Inc.)", r"Maplesoft|Waterloo\s+Maple|Maple\s*T\.?A\.?|Maple\s+Learn", "https://www.maplesoft.com/contact/",
                  r"(?:615 Kumpf Drive|Waterloo),?\s+(?:ON|Ontario)", "academic"),
    "mobius": ("DigitalEd (Möbius)", r"M[öo]bius\s+(?:courseware|platform|by\s+DigitalEd)|DigitalEd", "https://www.digitaled.com/contact",
               r"Waterloo,?\s+Ontario", "academic"),
    "pressreader": ("PressReader Inc.", r"PressReader", "https://about.pressreader.com/contact-us/",
                    r"(?:13111 Vanier Place|Richmond),?\s+(?:BC|British Columbia)", "library"),
    "tumblebooks": ("Tumbleweed Press Inc. (TumbleBooks)", r"TumbleBook(?:s|Library|Cloud)", "https://www.tumblebooks.com/contact/",
                    r"(?:Toronto|Montr[ée]al),?\s+(?:ON|QC|Ontario|Qu[ée]bec)", "library"),
}
CTX = {"eap": r"employee(?:\s+and\s+family)?\s+assistance|\bE\.?F?\.?A\.?P\.?\b|programme?\s+d.aide\s+aux\s+employ|assistance\s+program|counselling|counseling|wellness|mental\s+health\s+support",
       "benefits": r"benefit|insurance|assurance|group\s+plan|extended\s+health|dental|carrier|insurer|administered|underwritten|coverage|r[ée]gime|avantages\s+sociaux|provided\s+(?:by|through)|through\s+our|our\s+provider|plan\s+member|policy\s+number|group\s+number",
       "academic": r"grad(?:e|ing)|assess|exam|course|student|instructor|licen[cs]e|site\s+licen[cs]e|available\s+to|campus|teaching|learning|software",
       "library": r"librar|e-?resource|database|access|subscri|magazine|newspaper|e-?book|digital\s+collection"}
PAGE_LINK = re.compile(r"career|employment|\bjobs?\b|benefit|human[-_ ]?resources|\bhr\b|total[-_ ]rewards|work(?:ing)?[-_ ](?:with|for|at)[-_ ]us|"
                       r"join[-_ ]our[-_ ]team|employee|staff|carri[eè]re|emploi|ressources[-_ ]humaines|avantages|personnel|"
                       r"teaching|learning|instructor|faculty|library|biblioth|e-?resources|software|technology|academic", re.I)
NOT_PAGE = re.compile(r"donor|donat|sponsor|scholarship|bourse|news|nouvelle|blog|press|media|event|alumni|foundation|fondation|"
                      r"giving|campaign|award|tender|rfp|bid|procure|login|\.pdf$|\.docx?$", re.I)


def text_of(page):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", page[:1_500_000])
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", t)))


def verify_hq():
    out = {}
    for k, (legal, nm, url, rx, kind) in VENDORS.items():
        q = ""
        if CL.allowed(url):
            page, final = CL.fetch(url)
            if page:
                text = text_of(page)
                m = re.search(rx, text)
                if m:
                    q = text[max(0, m.start() - 120):m.end() + 60].strip()[:220]
        out[k] = {"legal": legal, "hq_url": url, "hq_quote": q}
        print("%-12s %s %s" % (k, "OK  " if q else "MISS", q[:120] if q else url), flush=True)
    json.dump(out, open(HQ_CACHE, "w"), ensure_ascii=False, indent=1)
    return out


def scan(text, vendors_ok):
    hits = {}
    for k, (legal, nm, url, rx, kind) in VENDORS.items():
        if k not in vendors_ok:
            continue
        for m in re.finditer(nm, text):
            win = text[max(0, m.start() - 160):m.end() + 160]
            if re.search(CTX[kind], win, re.I) and not re.search(r"donor|donat|sponsor|scholarship|bourse|in memory|gift|pledge|stock|shares|TSX|invest", win, re.I):
                hits.setdefault(k, text[max(0, m.start() - 130):m.end() + 130].strip()[:300])
                break
    return hits


def one(t, vendors_ok, pages_max, done):
    site = (t.get("website") or "").strip()
    h = (urllib.parse.urlparse(site if "//" in site else "https://" + site).hostname or "").lower()
    if not h or h in done:
        return
    site = "https://%s/" % h
    rows, status = {}, "ok"
    if not CL.allowed(site):
        status = "robots"
    else:
        page, final = CL.fetch(site)
        if not page:
            status = "unreachable"
        else:
            for k, q in scan(text_of(page), vendors_ok).items():
                rows.setdefault(k, (q, final))
            n = 0
            for href, label in CL.anchors(page, final):
                p = urllib.parse.urlparse(href)
                ph = (p.hostname or "").lower()
                if not ph or (ph != (urllib.parse.urlparse(final).hostname or "").lower() and not ph.endswith("." + h) and ph != h):
                    continue
                blob = p.path + " " + label
                if not PAGE_LINK.search(blob) or NOT_PAGE.search(blob):
                    continue
                if not CL.allowed(href):
                    continue
                pg, fu = CL.fetch(href)
                n += 1
                if pg:
                    for k, q in scan(text_of(pg), vendors_ok).items():
                        rows.setdefault(k, (q, fu))
                if n >= pages_max:
                    break
    with lock:
        with open(OUT + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%s\t%d\n" % (h, status, len(rows)))
        if rows:
            with open(OUT, "a", encoding="utf-8") as f:
                for k, (q, url) in rows.items():
                    v = vendors_ok[k]
                    f.write(json.dumps({"platform": "provider_mention", "domain": h, "dataset_id": "%s:%s" % (k, h),
                                        "dataset": "buyer's own page names %s as its provider" % v["legal"], "dataset_url": url,
                                        "publisher": t.get("buyer_name") or h, "buyer_unit": "", "website": site, "vendor": v["legal"],
                                        "canada_field": CANADA_FIELD, "canada_value": v["hq_quote"],
                                        "row": {"record_date": TODAY, "observed_date": TODAY, "signature": q, "signature_kind": "provider named on the buyer's own page",
                                                "vendor_hq_url": v["hq_url"], "task_buyer_key": t.get("buyer_key", "")}}, ensure_ascii=False) + "\n")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("tasks", nargs="?")
    a.add_argument("--verify-hq", action="store_true")
    a.add_argument("--workers", type=int, default=16)
    a.add_argument("--pages", type=int, default=6)
    a.add_argument("--limit", type=int, default=0)
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True); os.makedirs(STATE, exist_ok=True)
    if a.verify_hq or not os.path.exists(HQ_CACHE):
        hq = verify_hq()
        if not a.tasks:
            return
    else:
        hq = json.load(open(HQ_CACHE))
    vendors_ok = {k: v for k, v in hq.items() if v.get("hq_quote")}
    print("vendors with a verified Canadian HQ: %d / %d" % (len(vendors_ok), len(VENDORS)), flush=True)
    tasks = list(csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")))
    if a.limit:
        tasks = tasks[:a.limit]
    done = {l.split("\t")[0] for l in open(OUT + ".done", encoding="utf-8")} if os.path.exists(OUT + ".done") else set()
    print("sites: %d (%d done)" % (len(tasks), len(done)), flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda t: one(t, vendors_ok, a.pages, done), tasks))
    n = sum(1 for _ in open(OUT, encoding="utf-8")) if os.path.exists(OUT) else 0
    print("finished; leads in file: %d" % n, flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Contract facts the proof record lacks, read from the BUYER'S OWN page about the award (council / board report, bid results, award notice):
value, dates / term, PO / contract / tender numbers, number of bids — only from the text around the vendor's name, each with a ≤300-char
quote and the page URL. Input: CSV/TSV of candidate pages proposed by search agents (row_key, buyer_key, buyer_name, website, vendor, url);
nothing is taken from the agents but the URL. Output <repo>/data/incoming/claude/claude_award_facts.csv, read by rank.py for the
buyer–vendor pair (row_key = buyer_key||vendor) and applied only to empty contract columns, labelled "as printed in the buyer's award
report". Politeness: ap_crawler.fetch (robots.txt, 1 request / second / host, identified UA); PDFs via pdftotext.
  python3 tools/award_facts.py --urls ~/cch-tasks/af01.csv [--repo ~/cch-crawler] [--workers 12]
"""
import argparse, csv, datetime, html, os, re, sys, threading, unicodedata
from concurrent.futures import ThreadPoolExecutor

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C
from org_contacts import strip_long, visible_keep_lines, flat

TODAY = datetime.date.today().isoformat()
COLS = ["row_key", "buyer_key", "vendor", "url", "final_url", "status", "retrieved_date", "vendor_seen", "contract_value", "currency", "value_quote", "start_date", "end_date", "term", "dates_quote",
        "po_number", "contract_number", "tender_number", "numbers_quote", "number_of_bids", "bids_quote", "page_kind"]
STOP = {"inc", "incorporated", "ltd", "limited", "ltee", "ltée", "corp", "corporation", "co", "company", "llc", "llp", "lp", "the", "and", "of", "de", "du", "des", "la", "le", "les", "et", "group", "groupe", "canada", "international", "services", "service", "solutions", "consulting", "construction", "enterprises", "entreprises"}
MONEY = re.compile(r"(?<![\w.])\$\s?(\d{1,3}(?:[,\s]\d{3})+(?:\.\d{2})?|\d{4,9}(?:\.\d{2})?)(\s?(?:million|M\b|k\b))?|(\d{1,3}(?:[,\s]\d{3})+(?:,\d{2})?)\s?\$", re.I)
MONEY_CTX = re.compile(r"award|contract|amount|value|total|price|bid|tender|cost|budget|sum of|not to exceed|upset|montant|valeur|contrat|soumission|octroi|adjug|co[uû]t|prix", re.I)
MONEY_NOISE = re.compile(r"per hour|/hr|hourly|per unit|each\b|per tonne|per km|per month|monthly|salary|fine of|fee of \$\d{1,3}\b", re.I)
PO = re.compile(r"\b(?:P\.?O\.?|purchase order)\s*(?:no\.?|number|#|№)?\s*[:#]?\s*([A-Z]{0,4}[-/]?\d{4,10}(?:[-/]\d{1,4})?)", re.I)
CONTRACT_NO = re.compile(r"\b(?:contract|agreement|contrat)\s*(?:no\.?|number|#|№|numéro)\s*[:#]?\s*([A-Z0-9][A-Z0-9\-/.]{3,24})", re.I)
TENDER_NO = re.compile(r"\b(?:RFP|RFQ|RFT|RFI|RFSQ|ITT|RFPQ|Tender|Bid|Quotation|Proposal|Appel d'offres|Soumission|AO|Call|Project)\s*(?:no\.?|number|#|№|numéro|n°)?\s*[:#]?\s*((?:\d{2,4}[-/])?[A-Z]{0,6}[-/]?\d{2,6}(?:[-/][A-Z0-9]{1,8}){0,3})", re.I)
BIDS = re.compile(r"\b(\d{1,3}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|deux|trois|quatre|cinq|sept|huit|neuf|dix)\s+(?:\(\d{1,3}\)\s+)?(?:compliant |qualified |complete |responsive |valid |conforming |eligible |competitive |formal )?(?:bids?|tenders?|proposals?|submissions?|quotations?|quotes|responses|soumissions?|offres?|propositions?)\s+(?:were |was |have been |ont [ée]t[ée] |furent |a [ée]t[ée] )?(?:received|submitted|opened|returned|evaluated|re[çc]ues?|d[ée]pos[ée]es?|obtenues?)", re.I)
WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "deux": "2", "trois": "3", "quatre": "4", "cinq": "5", "sept": "7", "huit": "8", "neuf": "9", "dix": "10"}
DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b|\b((?:January|February|March|April|May|June|July|August|September|October|November|December|janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+\d{1,2},?\s+20\d{2})\b|\b(\d{1,2}(?:er)?\s+(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+20\d{2})\b", re.I)
TERM = re.compile(r"\b(?:for a |for an |over a |initial |a |un |une |d'une )?(?:term|period|duration|contract period|durée|période)\s+(?:of |de |d')?\s*(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten)[- ]?(?:\(\d{1,2}\)\s*)?(years?|yrs?|months?|ans?|années?|mois)\b|\b(\d{1,2}|one|two|three|four|five)[- ]?(?:\(\d{1,2}\)\s*)?(?:year|yr|an|année)s?\s+(?:term|contract|agreement|period|contrat)\b|\b(?:commencing|starting|beginning|effective|from)\s+(?:on\s+)?(20\d{2}-\d{2}-\d{2}|[A-Z][a-zé]+\s+\d{1,2},?\s+20\d{2}|\d{1,2}\s+[a-zé]+\s+20\d{2})\b|\b(?:ending|expiring|expires|until|to|through|terminating|se terminant|jusqu'au)\s+(?:on\s+)?(20\d{2}-\d{2}-\d{2}|[A-Z][a-zé]+\s+\d{1,2},?\s+20\d{2}|\d{1,2}\s+[a-zé]+\s+20\d{2})\b", re.I)
MONTHS = {m: i + 1 for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"])}
MONTHS.update({m: i + 1 for i, m in enumerate(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"])})
KIND = [("council / committee report or minutes", r"council|committee|board|conseil|comit[ée]|minutes|proc[èe]s-verbal|agenda|ordre du jour|staff report|resolution|r[ée]solution"), ("bid results / awarded bids", r"bid result|awarded|award of|results of|adjudicat|octroi|r[ée]sultat"), ("award notice", r"award notice|notice of award|avis d'adjudication|avis d'attribution"), ("purchasing / procurement report", r"purchasing|procurement|approvisionnement|achats")]


def toks(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    return [t for t in re.findall(r"[a-z0-9]{2,}", s) if t not in STOP] or re.findall(r"[a-z0-9]{2,}", s)[:2]


def to_iso(s):
    s = (s or "").strip().rstrip(",")
    m = re.match(r"^(20\d{2})-(\d{2})-(\d{2})$", s)
    if m:
        return s
    m = re.match(r"^([A-Za-zéû]+)\s+(\d{1,2}),?\s+(20\d{2})$", s)
    if m and m.group(1).lower() in MONTHS:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(1).lower()], int(m.group(2)))
    m = re.match(r"^(\d{1,2})(?:er)?\s+([A-Za-zéû]+)\s+(20\d{2})$", s)
    if m and m.group(2).lower() in MONTHS:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2).lower()], int(m.group(1)))
    return ""


def q300(text, a, b):
    return flat(text[max(0, a - 110):b + 110])[:300]


def money_value(m):
    raw = (m.group(1) or m.group(3) or "").strip()
    if re.search(r",\d{2}$", raw) and not re.search(r"\.\d{2}$", raw):  # French decimals: "2 345 678,90"
        raw = raw[:-3].replace(",", "").replace(" ", "") + "." + raw[-2:]
    n = float(re.sub(r"[,\s]", "", raw)) if raw else 0.0
    unit = (m.group(2) or "").strip().lower()
    if unit.startswith("m"):
        n *= 1_000_000
    elif unit.startswith("k"):
        n *= 1_000
    return n


def read(url):
    if not C.allowed(url):
        return "robots", "", url
    st, ct, data, final = C.fetch(url, 6_000_000)
    if st in (401, 403, 429):
        return "blocked", "", final or url
    if st != 200 or not data:
        return "http_%s" % st, "", final or url
    is_pdf = "pdf" in (ct or "").lower() or data[:5] == b"%PDF-"
    if is_pdf:
        text = re.sub(r"\s+", " ", C.pdf_text(data) or "")
        return ("ok" if text.strip() else "pdf_no_text"), text, final or url
    raw = strip_long(data.decode("utf-8", "replace"))
    if len(raw) < 30000 and C.BLOCK_RX.search(raw[:5000]):  # a block page is a short page (a Wix page carries "captcha" in its settings)
        return "blocked", "", final or url
    return "ok", re.sub(r"\s+", " ", visible_keep_lines(raw)), final or url


def extract(vendor, text):
    out = {}
    low = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    want = toks(vendor)
    if not want:
        return out
    # every position where the vendor's core name appears (whole words, in order, up to 3 words apart)
    rx = re.compile(r"\b" + r"\W{1,3}(?:\w+\W{1,3}){0,2}?".join(re.escape(t) for t in want[:3]) + r"\b") if len(want) > 1 else re.compile(r"\b" + re.escape(want[0]) + r"\b")
    hits = [m.start() for m in rx.finditer(low)]
    if not hits:
        return out
    out["vendor_seen"] = str(len(hits))
    # windows around the vendor name
    best_money, best_bids, best_dates, nums = None, None, None, {}
    for h in hits[:40]:
        a, b = max(0, h - 700), min(len(text), h + 900)
        win = text[a:b]
        for m in MONEY.finditer(win):
            ctx = win[max(0, m.start() - 160):m.end() + 60]
            if not MONEY_CTX.search(ctx) or MONEY_NOISE.search(ctx):
                continue
            v = money_value(m)
            if v < 1000 or v > 5e9:
                continue
            dist = abs((a + m.start()) - h)
            if best_money is None or (v > best_money[0] and dist < 500) or dist < best_money[2] - 300:
                best_money = (v, q300(text, a + m.start(), a + m.end()), dist, "CAD" if re.search(r"\bCAD\b|\$\s?CA|CDN", ctx) or not re.search(r"\bUSD?\b|US\$", ctx) else "USD")
        for m in BIDS.finditer(win):
            n = WORDS.get(m.group(1).lower(), m.group(1))
            dist = abs((a + m.start()) - h)
            if best_bids is None or dist < best_bids[1]:
                best_bids = (n, dist, q300(text, a + m.start(), a + m.end()))
        for m in PO.finditer(win):
            nums.setdefault("po_number", (m.group(1), q300(text, a + m.start(), a + m.end())))
        for m in CONTRACT_NO.finditer(win):
            if not re.fullmatch(r"\d{1,3}", m.group(1)):
                nums.setdefault("contract_number", (m.group(1).rstrip(".,;"), q300(text, a + m.start(), a + m.end())))
        for m in TENDER_NO.finditer(win):
            val = m.group(1).rstrip(".,;")
            if re.search(r"\d{2}", val) and len(val) >= 4:
                nums.setdefault("tender_number", (val, q300(text, a + m.start(), a + m.end())))
        for m in TERM.finditer(win):
            g = m.groups()
            dist = abs((a + m.start()) - h)
            if dist > 900:
                continue
            start = to_iso(g[3]) if g[3] else ""
            end = to_iso(g[4]) if g[4] else ""
            term = ("%s %s" % (WORDS.get(g[0].lower(), g[0]), g[1])) if (g[0] and g[1]) else ("%s year(s)" % WORDS.get(g[2].lower(), g[2])) if g[2] else ""
            cur = best_dates or ["", "", "", "", 10 ** 9]
            if start and not cur[0]:
                cur[0] = start
            if end and not cur[1]:
                cur[1] = end
            if term and not cur[2]:
                cur[2] = term
            if dist < cur[4]:
                cur[3], cur[4] = q300(text, a + m.start(), a + m.end()), dist
            best_dates = cur
    if best_money:
        out.update(contract_value="%.2f" % best_money[0], currency=best_money[3], value_quote=best_money[1])
    if best_bids:
        out.update(number_of_bids=best_bids[0], bids_quote=best_bids[2])
    if best_dates and (best_dates[0] or best_dates[1] or best_dates[2]):
        out.update(start_date=best_dates[0], end_date=best_dates[1], term=best_dates[2], dates_quote=best_dates[3])
    if nums:
        out.update({k: v[0] for k, v in nums.items()})
        out["numbers_quote"] = " | ".join(v[1] for v in nums.values())[:300]
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--urls", required=True, nargs="+")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--workers", type=int, default=12)
    a.add_argument("--force", action="store_true")
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_award_facts.csv")
    prev = {}
    if os.path.exists(out):
        for r in csv.DictReader(open(out, encoding="utf-8", errors="replace")):
            prev[(r["row_key"], r["url"])] = r
    todo = []
    for p in a.urls:
        delim = "\t" if p.endswith(".tsv") else ","
        for r in csv.DictReader(open(p, encoding="utf-8", errors="replace"), delimiter=delim):
            k, u, v = (r.get("row_key") or "").strip(), (r.get("url") or "").strip(), (r.get("vendor") or "").strip()
            if not k or not v or not u.startswith("http"):
                continue
            if (k, u) in prev and not a.force:
                continue
            todo.append((k, (r.get("buyer_key") or "").strip(), v, u))
    print("pages to read: %d (known: %d)" % (len(todo), len(prev)), flush=True)
    lock = threading.Lock()
    n = {}

    def one(t):
        k, bk, v, u = t
        st, text, final = read(u)
        row = {c: "" for c in COLS}
        row.update(row_key=k, buyer_key=bk, vendor=v, url=u, final_url=final, status=st, retrieved_date=TODAY)
        if st == "ok":
            try:
                row.update(extract(v, text))
                row["page_kind"] = next((lab for lab, rx in KIND if re.search(rx, (final or u) + " " + text[:3000], re.I)), "buyer page")
                if not row.get("vendor_seen"):
                    row["status"] = "vendor_not_on_page"
            except Exception as e:
                row["status"] = "extract_error:" + type(e).__name__
        with lock:
            prev[(k, u)] = row
            n[row["status"][:14]] = n.get(row["status"][:14], 0) + 1
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore"); w.writeheader()
        for k in sorted(prev):
            w.writerow({c: (prev[k].get(c) or "").replace("\0", "").replace("\r", " ") for c in COLS})
    os.replace(out + ".tmp", out)
    print("wrote", out, len(prev), n, "filled:", {c: sum(1 for v in prev.values() if v.get(c)) for c in ("contract_value", "start_date", "end_date", "term", "po_number", "contract_number", "tender_number", "number_of_bids")}, flush=True)


if __name__ == "__main__":
    main()

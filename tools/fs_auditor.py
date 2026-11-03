#!/usr/bin/env python3
"""Auditor of record read from an organisation's OWN audited financial statements (owner, 2026-11-03: every route to a
dated relationship for organisations that already publish their own invoicing mailbox). No AI.

For each organisation of a task CSV (buyer_key,buyer_name,website), the crawler walks its own site (<= 25 pages,
robots.txt, <= 1 request / 1.1 s per host, project user agent; 401/403/429 or a challenge page = skipped), opens its
latest audited financial statements (PDF) and reads the independent auditor's report. A lead is written only when
  - the statements name the organisation (its name's words in the first pages),
  - the report is signed on or after WINDOW (12 months) and not after today,
  - the signature block prints the firm's city and province / "Canada" (the record itself proves the vendor, the audit
    firm the organisation engages and pays, is located in Canada), and the firm is named in the report.
Lead file: $CCH_LEADS/socrata_fs_auditor.jsonl (picked up by tools/lead_scanner.py --bridge). Per-site outcome log:
$CCH_SMALL_CACHE/fs_auditor_log.csv.
    python3 tools/fs_auditor.py <tasks.csv> [--workers 16] [--limit N]
"""
import argparse, csv, datetime as dt, hashlib, heapq, html, os, re, sys, threading, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import small_sources as S  # get (cache, robots, per-host gap, challenge check), pdf_text, quote, write_leads

WINDOW, TODAY = S.WINDOW, S.TODAY
MONTHS = S.MONTHS
FRM = {"janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7, "août": 8,
       "aout": 8, "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12, "decembre": 12}
EN_DATE = re.compile(r"\b(%s)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(20\d\d)\b" % MONTHS)
FR_DATE = re.compile(r"\b(\d{1,2})(?:er)?\s+(janvier|f[ée]vrier|mars|avril|mai|juin|juillet|ao[uû]t|septembre|octobre|"
                     r"novembre|d[ée]cembre)\s+(20\d\d)\b", re.I)
PROVS = (r"(Ontario|Alberta|British Columbia|B\.C\.|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland"
         r"(?: and Labrador)?|Prince Edward Island|P\.E\.I\.|Yukon|Northwest Territories|Nunavut|Qu[ée]bec|Canada|"
         r"Nouveau-Brunswick|Nouvelle-[ÉE]cosse|Colombie-Britannique|Ont\.|Alta\.|Sask\.|Man\.|ON|AB|BC|MB|SK|NS|NB|NL|"
         r"PE|YT|NT|NU|QC)")
CITY_PROV = re.compile(r"\b([A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+(?:[ \-][A-ZÀ-Ý][A-Za-zÀ-ÿ.'’\-]+){0,3}),?[ \t]+" + PROVS +
                       r"(?![A-Za-z])")
FIRM = re.compile(r"((?:[A-Z][A-Za-z&'’.\-]*[ \t]+(?:&[ \t]+)?){1,6}?(?:LLP|L\.L\.P\.|S\.E\.N\.C\.R\.L\.|s\.e\.n\.c\.r\.l\.|"
                  r"SENCRL|Professional Corporation|CPA[,]? (?:Inc|Ltd)\.?|Chartered Professional Accountants?,? "
                  r"(?:Inc|Ltd)\.?|Chartered Accountants?,? (?:Inc|Ltd)\.?)(?![A-Za-z]))")
NOT_FIRM = re.compile(r"^(?:Chartered|Licensed|Professional|Public|Accountants?|Independent|Auditors?|Signed|Original|"
                      r"Per|The|Our|Comptables|Report|Responsibilities|Opinion|Basis)\b", re.I)
REPORT = re.compile(r"INDEPENDENT\s+AUDITOR|Independent\s+Auditor|RAPPORT\s+DE\s+L.AUDITEUR\s+IND|Rapport\s+de\s+l.auditeur"
                    r"\s+ind", re.I)
END = re.compile(r"STATEMENTS? OF FINANCIAL POSITION|Statements? of Financial Position|CONSOLIDATED STATEMENTS? OF|"
                 r"Consolidated Statements? of|BALANCE SHEET|Balance Sheet|STATEMENTS? OF OPERATIONS|Statements? of "
                 r"Operations|[ÉE]TAT DE LA SITUATION FINANCI|[ÉE]tat de la situation financi|[ÉE]TATS? DES R[ÉE]SULTATS")
FS_LINK = re.compile(r"financial[-_ %20]*statements?|audited|consolidated[-_ %20]*financial|[ée]tats[-_ %20]*financiers|"
                     r"etats-financiers|rapport[-_ %20]*financier|annual[-_ %20]*report|\bfs[-_ ]?20(?:25|26)", re.I)
NAV = re.compile(r"financ|annual|report|rapport|budget|transparen|accountab|disclosure|governance|gouvernance|about|"
                 r"a-propos|publication|documents|council|conseil|administration|corporate|reports|finance", re.I)
SIDE = re.compile(r"librar|biblioth|trust fund|cemetery|cimeti|\bBIA\b|business improvement|police|foundation|fondation|"
                  r"hydro|pension|museum|mus[ée]e|housing|habitation|golf|arena", re.I)
STOP = {"the", "of", "and", "de", "du", "des", "la", "le", "les", "et", "inc", "ltd", "corporation", "society", "city",
        "town", "village", "county", "district", "municipality", "township", "association", "canada", "for", "in",
        "ville", "municipalite", "société", "societe", "limited", "ltée", "ltee"}
_lock = threading.Lock()


def iso(m, fr=False):
    try:
        if fr:
            return dt.date(int(m.group(3)), FRM[m.group(2).lower().replace("û", "u")], int(m.group(1))).isoformat()
        return dt.datetime.strptime("%s %s %s" % (m.group(1), m.group(2), m.group(3)), "%B %d %Y").date().isoformat()
    except Exception:
        return ""


def name_ok(name, txt):
    toks = [t for t in re.findall(r"[a-zà-ÿ0-9]+", (name or "").lower()) if len(t) >= 3 and t not in STOP]
    if not toks:
        return True
    low = txt.lower()
    return sum(t in low for t in toks) * 2 >= len(toks)


def candidates(site, max_pages=25):
    """FS-looking document links on the organisation's own site, best first: [(score, url, anchor)]"""
    heap, seen, hits, n = [(0, 0, site, 0)], set(), {}, 0
    host = S.host_of(site)
    while heap and len(seen) < max_pages:
        _, _, u, d = heapq.heappop(heap)
        if u in seen:
            continue
        seen.add(u)
        st, body, final, ct = S.get(u, limit=4_000_000)
        if st in (401, 403, 429) and len(seen) == 1:
            return None  # blocked at the door: rule 6
        if st != 200 or "html" not in (ct or ""):
            continue
        page = body.decode("utf-8", "replace")
        for href, inner in re.findall(r'<a\s[^>]*?href="([^"#]+)"[^>]*>(.*?)</a>', page, re.S | re.I):
            a = urllib.parse.urljoin(final, html.unescape(href)).split("#")[0]
            if not a.startswith("http"):
                continue
            txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", inner))).strip()[:200]
            blob = urllib.parse.unquote(a) + " " + txt
            same = S.host_of(a).split(".")[-2:] == host.split(".")[-2:]
            filelike = re.search(r"\.pdf(\?|$)|documentcenter/view|/download|/files/|/media/|/sites/default/|/assets/|"
                                 r"/uploads/|/docs?/|getmedia|/file/|/Modules/ShowDocument", a, re.I)
            if FS_LINK.search(blob) and filelike:
                yb = urllib.parse.unquote(a.split("?")[0].rsplit("/", 1)[-1]) + " " + txt
                sc = 3 if re.search(r"2026|2025[-_ /]?(?:20)?26|25[-_]26", yb) else 2 if "2025" in yb else \
                    0 if re.search(r"20(?:1\d|2[0-4])", yb) else 1
                if sc and not SIDE.search(yb):
                    sc += 0.5 if re.search(r"audited|consolidated|[ée]tats", yb, re.I) else 0
                    hits[a] = max(hits.get(a, (0, ""))[0], sc), txt
                continue
            if same and d < 3 and a not in seen and not re.search(r"\.(pdf|jpe?g|png|docx?|xlsx?|zip|mp4)(\?|$)", a, re.I):
                p = urllib.parse.urlparse(a).path + " " + txt
                sc = 0 if FS_LINK.search(p) else 1 if re.search(r"financ|annual|rapport|report", p, re.I) else \
                    2 if NAV.search(p) else 9
                if sc < 9:
                    n += 1
                    heapq.heappush(heap, (sc, n, a, d + 1))
        if any(v[0] >= 3 for v in hits.values()) and len(seen) >= 6:
            break
    return sorted(((v[0], u, v[1]) for u, v in hits.items()), key=lambda x: -x[0])


AUDITED_BY = re.compile(r"(?:audited by|examined by|external auditors?,?|independent auditors?,?|v[ée]rificateurs? externes?,?|"
                        r"auditeurs? ind[ée]pendants?,?)\s+(?:the\s+)?((?:[A-Z][A-Za-z&'’.\-]*[ \t,]+(?:&[ \t]+)?){0,6}?(?:LLP|"
                        r"S\.E\.N\.C\.R\.L\.|s\.e\.n\.c\.r\.l\.|Professional Corporation|CPA[,]? (?:Inc|Ltd)\.?|Chartered "
                        r"Professional Accountants?,? (?:Inc|Ltd)\.?)|KPMG|MNP|BDO Canada|Deloitte|PricewaterhouseCoopers|"
                        r"Ernst & Young|Grant Thornton|Raymond Chabot Grant Thornton|Mallette|Baker Tilly [A-Z][A-Za-z]+)")
ACCT = re.compile(r"chartered|accountants?|comptables?|CPA|auditor|auditeur", re.I)


def _firm(raw):
    f = re.sub(r"\s+", " ", raw).strip(" ,.")
    f = re.sub(r"^(?:\(?signed\)?|original signed by|per|by)\s+", "", f, flags=re.I)
    return "" if NOT_FIRM.search(f) or len(f) < 3 else f


def auditor(txt):
    """(firm, city_prov, date_iso, quote) from the independent auditor's report, or None"""
    starts = [m.start() for m in REPORT.finditer(txt)]
    i = next((x for x in starts if re.search(r"\bOpinion\b|We have audited|Nous avons effectu|avons audit", txt[x:x + 5000])), None)
    if i is None:
        return None
    body = txt[i:i + 20000]
    dates = sorted([(x.start(), iso(x)) for x in EN_DATE.finditer(body)] + [(x.start(), iso(x, True)) for x in FR_DATE.finditer(body)])
    cps = [(x.start(), x) for x in CITY_PROV.finditer(body)]
    best = None
    for p, d in dates:
        near = [(abs(cp - p), x) for cp, x in cps if abs(cp - p) <= 260] if d else []
        if near:
            best = (p, d, min(near, key=lambda t: t[0])[1])  # the first dated city-province pair = the signature block
            break
    if not best:
        return None
    p, d, cpm = best
    if not (WINDOW <= d <= TODAY):
        return ("", "", d, "")  # signed outside the window: reported, not kept
    firms = []
    for x in FIRM.finditer(body[:p + 400]):  # in the report, nearest the signature
        f = _firm(x.group(1))
        if f:
            firms.append((abs(x.start() - p), "report", x.start(), f))
    if not firms:  # letterhead above the report title
        for x in FIRM.finditer(txt[max(0, i - 2500):i]):
            f = _firm(x.group(1))
            if f:
                firms.append((10 ** 6, "letterhead", None, f))
    if not firms:  # management's responsibility page: "... audited by KPMG LLP, the external auditors ..."
        for x in AUDITED_BY.finditer(txt[:max(i + 20000, 40000)]):
            f = _firm(x.group(1))
            if f and ACCT.search(txt[max(0, x.start() - 200):x.end() + 200]):
                firms.append((2 * 10 ** 6, "statement", x.start(), f))
                break
    if not firms:
        return None
    dist, where, fp, firm = min(firms)
    cp = re.sub(r"\s+", " ", cpm.group(0)).strip()
    lo, hi = min(p, cpm.start()), max(p + 20, cpm.end())
    if where == "report" and dist <= 260:
        lo, hi = min(lo, fp), max(hi, fp + len(firm))
    q = re.sub(r"\s{2,}", " | ", body[max(0, lo - 10):hi + 10].strip())
    if firm.lower() not in q.lower():
        src = txt[max(0, i - 2500):i] if where == "letterhead" else txt[max(0, fp - 120):fp + len(firm) + 80] if fp is not None else ""
        src = re.sub(r"\s{2,}", " | ", src)
        j = src.lower().find(firm.lower())
        if j >= 0:
            q = S.quote(src[max(0, j - 80):j + len(firm) + 40], 150) + " ... " + q
    return firm, cp, d, S.quote(q)


def one(t):
    site = S.site_url(t.get("website") or "")
    if not site:
        return t, "no website", None
    try:
        cands = candidates(site)
    except Exception as ex:
        return t, "error %s" % type(ex).__name__, None
    if cands is None:
        return t, "blocked", None
    if not cands:
        return t, "no statements link", None
    seen_out = []
    for sc, url, anchor in cands[:4]:
        st, body, final, ct = S.get(url, limit=40_000_000)
        if st != 200 or not body.startswith(b"%PDF"):
            seen_out.append("not pdf")
            continue
        txt = S.pdf_text(body)
        if not re.search(r"financial statements|[ée]tats financiers", txt[:8000], re.I):
            seen_out.append("not statements")
            continue
        if not name_ok(t["buyer_name"], txt[:8000]):
            seen_out.append("other organisation")
            continue
        a = auditor(txt)
        if not a:
            seen_out.append("no auditor's report signature")
            continue
        firm, cp, d, q = a
        if not firm:
            seen_out.append("signed %s (outside window)" % d)
            continue
        lead = {"platform": "fs_auditor", "domain": S.host_of(site), "dataset_id": "FS-" + hashlib.sha1(final.encode()).hexdigest()[:10],
                "dataset": "audited financial statements: independent auditor's report signed %s (%s)" % (d, cp),
                "dataset_url": final, "publisher": t["buyer_name"], "buyer_unit": "", "website": site, "vendor": firm,
                "canada_field": "auditor of record (own audited financial statements, auditor's report signed in %s)" % cp,
                "canada_value": q, "row": {"record_date": d, "auditor": firm, "signed_at": cp, "statements_url": final,
                                           "statements_link_text": anchor, "task_buyer_key": t.get("buyer_key", "")}}
        return t, "kept %s %s %s" % (firm, cp, d), lead
    return t, "; ".join(seen_out) or "nothing", None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tasks")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    tasks = list(csv.DictReader(open(a.tasks, encoding="utf-8", errors="replace")))
    if a.limit:
        tasks = tasks[:a.limit]
    path = os.path.join(S.LEADS, "socrata_fs_auditor.jsonl")
    leads = {}
    if os.path.exists(path):  # resume: keep earlier leads (one per domain)
        import json
        for line in open(path, encoding="utf-8"):
            r = json.loads(line)
            leads[r["domain"]] = r
    os.makedirs(S.CACHE, exist_ok=True)
    logp = os.path.join(S.CACHE, "fs_auditor_log.csv")
    done = set()
    if os.path.exists(logp):
        done = {r["buyer_key"] for r in csv.DictReader(open(logp, encoding="utf-8"))}
    new = not os.path.exists(logp)
    lf = open(logp, "a", encoding="utf-8", newline="")
    w = csv.writer(lf)
    if new:
        w.writerow(["buyer_key", "buyer_name", "website", "outcome", "checked"])
    todo = [t for t in tasks if t.get("buyer_key") not in done]
    S.log("fs_auditor: %d tasks (%d already done), %d leads so far" % (len(todo), len(tasks) - len(todo), len(leads)))
    n = 0
    with ThreadPoolExecutor(a.workers) as ex:
        for t, outcome, lead in ex.map(one, todo):
            n += 1
            with _lock:
                w.writerow([t.get("buyer_key", ""), t.get("buyer_name", ""), t.get("website", ""), outcome, TODAY])
                lf.flush()
                if lead:
                    leads[lead["domain"]] = lead
                if lead or n % 50 == 0:
                    S.write_leads("fs_auditor", list(leads.values()))
    S.write_leads("fs_auditor", list(leads.values()))
    S.log("fs_auditor finished: %d sites, %d leads" % (n, len(leads)))


if __name__ == "__main__":
    main()

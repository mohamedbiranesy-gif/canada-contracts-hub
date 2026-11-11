#!/usr/bin/env python3
"""Read pages that a web search surfaced as invoicing / accounts-payable pages, and record each organisation's OWN role
mailbox (evidence or nothing). No AI: the search only located the addresses; this reader decides.

Mailbox-first discovery: instead of crawling organisations we already know, the pages themselves tell us which
organisations publish an invoicing mailbox. Input TSV (from the sonnet search agents, INSTRUCTIONS_APFIRST.md):
url<TAB>email_seen<TAB>title<TAB>snippet. For each URL (robots.txt, 1 request / second / host, PDFs read):
  - every role mailbox on the page that belongs to the page's own organisation (tools/ap_crawler.py:same_org against
    the page's host; never a contractor's, a software vendor's or a parent government's mailbox for another body);
  - classified by the words next to it (invoice_submission > accounts_payable > supplier_payment > procurement);
    general / finance mailboxes are kept only when nothing better is on the page;
  - the organisation's name from the page title / og:site_name, its key "ap:<sha1 of its registrable domain>".
Output: data/incoming/claude/claude_buyer_ap_results_apfirst01.csv (RETURN_FORMATS buyer_ap) in the crawler clone, so
the ingest workflow re-verifies every address; plus ~/cch-crawl-some/apfirst_orgs.csv (buyer_key, buyer_name, website)
for tools/fs_auditor.py / tools/news_match.py / tools/exchange_listing.py to find each organisation's dated record.
  python3 tools/ap_pages.py <urls.tsv> [...] [--workers 12]
"""
import argparse, csv, hashlib, html, os, re, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

REPO = os.path.expanduser("~/cch-crawler")
OUT = os.path.expanduser("~/cch-crawler-state/stage/claude_buyer_ap_results_apfirst01.csv")  # outside the clone; tools/stage_merge.py unions it in before each commit
ORGS = os.path.expanduser("~/cch-crawl-some/apfirst_orgs.csv")
DONE = os.path.expanduser("~/cch-crawler-state/ap_pages_done.tsv")
TODAY = time.strftime("%Y-%m-%d")
HDR = "task_id,buyer_key,org_name_as_found,ap_email,ap_email_type,invoice_portal_url,ap_phone,invoice_mailing_address,invoicing_requirements_summary,applies_to,evidence_url,evidence_quote,retrieved_date,status,queries_tried,notes".split(",")
BAD_TITLE = re.compile(r"^(home|accueil|contact|contact us|nous joindre|accounts payable|comptes payables|invoices?|factures?|suppliers?|vendors?|"
                       r"fournisseurs|finance|purchasing|procurement|page not found|404|untitled|login|sign in)$", re.I)
lock = threading.Lock()


def org_name(raw, host):
    """the organisation's name as the page shows it: og:site_name, else the title's last / first segment"""
    m = re.search(r"(?is)<meta[^>]+property\s*=\s*[\"']og:site_name[\"'][^>]+content\s*=\s*(?:\"([^\"]{2,120})|'([^']{2,120}))", raw)  # the value ends at the quote that opened it
    cands = [html.unescape(m.group(1) or m.group(2)).strip()] if m else []
    t = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
    if t:
        title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t.group(1)))).strip()
        parts = [p.strip(" -–—|:·•") for p in re.split(r"\s+[|–—·•]\s+|\s+-\s+|\s*\|\s*", title) if p.strip()]
        cands += parts[::-1]  # site name usually last
    for c in cands:
        if 3 <= len(c) <= 120 and not BAD_TITLE.match(c) and re.search(r"[A-Za-zÀ-ÿ]{3}", c):
            return c[:120]
    return host


def read(url):
    if not C.allowed(url):
        return url, "robots", []
    try:
        status, ctype, data, final = C.fetch(url)
    except Exception as e:
        return url, "error", []
    if status in (401, 403, 429):
        return url, "blocked", []
    if status != 200 or not data:
        return url, "http_%s" % status, []
    is_pdf = "pdf" in (ctype or "").lower() or data[:5] == b"%PDF-"
    raw = C.pdf_text(data) if is_pdf else html.unescape(data.decode("utf-8", "replace"))
    raw = re.sub(r"data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+|[A-Za-z0-9+/=_%-]{120,}", " ", raw[:3_000_000])  # the e-mail regex is quadratic on long tokens
    text = re.sub(r"\s+", " ", raw) if is_pdf else C.visible(raw)
    host = (urllib.parse.urlparse(final).hostname or "").lower()
    site = "https://%s/" % host
    name = host if is_pdf else org_name(raw, host)
    found = {}
    vis = set(x.lower().rstrip(".") for x in C.EMAIL_RX.findall(text))
    for e in set(x.lower().rstrip(".") for x in C.EMAIL_RX.findall(raw)):
        if e.split(".")[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp"):
            continue
        if e not in vis and any(v != e and v.endswith(e) for v in vis):
            continue
        if not C.same_org(e, site, name):
            continue
        q = C.quote_for(e, text, raw)
        i = C.find_tok(text, e)
        kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else q, True)
        if kind and q:
            found[e] = (C.RANK[kind], kind, q)
    if not found:
        return url, "no_own_mailbox", []
    best = sorted(found.items(), key=lambda kv: kv[1][0])
    top = best[0][1][0]
    keep = [kv for kv in best if kv[1][0] <= 2] or best[:1]  # AP-grade ones, else the single best (finance / procurement / general)
    rows = []
    for e, (rk, kind, q) in keep[:3]:
        rows.append({"task_id": "", "buyer_key": "ap:" + hashlib.sha1(C.registrable(host).encode()).hexdigest()[:16], "org_name_as_found": name,
                     "ap_email": e, "ap_email_type": "general" if kind == "finance" else kind, "invoice_portal_url": "", "ap_phone": "",
                     "invoice_mailing_address": "", "invoicing_requirements_summary": "", "applies_to": "whole_organisation",
                     "evidence_url": final, "evidence_quote": q, "retrieved_date": TODAY, "status": "found",
                     "queries_tried": "page located by a web search for invoicing pages, read by tools/ap_pages.py, no AI",
                     "notes": "" if kind in ("invoice_submission", "accounts_payable", "supplier_payment") else "no invoicing mailbox published on this page",
                     "_site": site})
    return url, "ok", rows


def main():
    a = argparse.ArgumentParser()
    a.add_argument("files", nargs="+")
    a.add_argument("--workers", type=int, default=12)
    a = a.parse_args()
    done = set()
    if os.path.exists(DONE):
        done = {l.split("\t")[0] for l in open(DONE, encoding="utf-8")}
    urls = []
    for f in a.files:
        for line in open(f, encoding="utf-8", errors="replace"):
            u = line.split("\t")[0].strip()
            if u.startswith("http") and u not in done and u not in urls:
                urls.append(u)
    print("urls: %d (%d done before)" % (len(urls), len(done)), flush=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True); os.makedirs(os.path.dirname(ORGS), exist_ok=True)
    new_out, new_orgs = not os.path.exists(OUT), not os.path.exists(ORGS)
    n = sum(1 for _ in open(OUT, encoding="utf-8")) if not new_out else 0
    stats = {}
    with open(OUT, "a", newline="", encoding="utf-8") as fo, open(ORGS, "a", newline="", encoding="utf-8") as fg, open(DONE, "a", encoding="utf-8") as fd:
        wo, wg = csv.DictWriter(fo, fieldnames=HDR), csv.writer(fg)
        if new_out:
            wo.writeheader()
        if new_orgs:
            wg.writerow(["buyer_key", "buyer_name", "website"])
        def one(u):
            nonlocal n
            url, st, rows = read(u)
            with lock:
                stats[st] = stats.get(st, 0) + 1
                fd.write("%s\t%s\t%d\n" % (url, st, len(rows))); fd.flush()
                seen_org = False
                for r in rows:
                    n += 1
                    r["task_id"] = "CL-APF-%06d" % n
                    site = r.pop("_site")
                    wo.writerow(r)
                    if not seen_org:
                        wg.writerow([r["buyer_key"], r["org_name_as_found"], site]); seen_org = True
                fo.flush(); fg.flush()
                if sum(stats.values()) % 100 == 0:
                    print(time.strftime("%H:%M"), stats, flush=True)
        with ThreadPoolExecutor(a.workers) as ex:
            list(ex.map(one, urls))
    print("finished", stats, flush=True)


if __name__ == "__main__":
    main()

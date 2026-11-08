#!/usr/bin/env python3
"""Confirm proposed vendor websites by reading them (evidence or nothing). Input: TSV lines `vendor_key, vendor_name, website, evidence_url,
evidence_quote, confidence` (search agents only PROPOSE a URL; nothing is taken from them). This tool opens the site's home page and the
evidence page, requires the company's core name tokens to appear in the page text (ap_crawler.same_org rules), records a ≤300-char quote
from the page it read, and writes <repo>/data/incoming/claude/claude_vendor_sites.csv — the only file rank.py reads (vendor_website when
empty, then org_contacts / org_extras read the site for phone, address, legal name, logo, BN). Politeness: robots.txt, 1 request / second / host.
  python3 tools/vendor_sites_check.py --in proposals.tsv [--repo ~/cch-crawler]
"""
import argparse, csv, datetime, html, os, re, sys, unicodedata, urllib.parse

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C
from org_contacts import strip_long, visible_keep_lines, flat

TODAY = datetime.date.today().isoformat()
COLS = ["vendor_key", "vendor_name", "website", "check_status", "evidence_url", "evidence_quote", "name_tokens_seen", "retrieved_date", "proposed_by"]
STOP = {"inc", "incorporated", "ltd", "limited", "ltee", "ltée", "corp", "corporation", "co", "company", "llc", "llp", "lp", "the", "and", "of", "de", "du", "des", "la", "le", "les", "et", "group", "groupe", "canada", "international", "services", "service", "solutions", "consulting", "t/a", "dba", "o/a", "doing", "business", "as", "l.p", "s.e.n.c.r.l", "sencrl", "senc"}
DIRECTORY = re.compile(r"opencorporates|zoominfo|dnb\.com|linkedin|facebook|yellowpages|canada411|bloomberg|crunchbase|glassdoor|indeed|merx|biddingo|bidsandtenders|sedar|wikipedia|yelp|bbb\.org|manta\.com|cylex|hotfrog|\.gov\b|\.gc\.ca|\.gouv\.qc\.ca|instagram|twitter|x\.com|youtube", re.I)


def toks(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    return [t for t in re.findall(r"[a-z0-9]{2,}", s) if t not in STOP]


def read(url):
    if not C.allowed(url):
        return "robots", "", ""
    st, ct, data, final = C.fetch(url, 3_000_000)
    if st in (401, 403, 429):
        return "blocked", "", final
    if st != 200 or not data or "html" not in (ct or "").lower():
        return "http_%s" % st, "", final
    raw = strip_long(data.decode("utf-8", "replace"))
    if C.BLOCK_RX.search(raw[:5000]):
        return "blocked", "", final
    return "ok", re.sub(r"\s+", " ", visible_keep_lines(raw) + " " + " ".join(re.findall(r'(?i)<(?:title|meta[^>]+content)="?([^"<>]{3,200})', raw))), final


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--in", dest="inp", required=True, nargs="+")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_vendor_sites.csv")
    prev = {}
    if os.path.exists(out):
        for r in csv.DictReader(open(out, encoding="utf-8")):
            prev[r["vendor_key"]] = r
    n = {"confirmed": 0, "name_not_on_site": 0, "unreadable": 0, "directory": 0, "skipped": 0}
    for path in a.inp:
        for r in csv.DictReader(open(path, encoding="utf-8", errors="replace"), delimiter="\t"):
            key, name, site = (r.get("vendor_key") or "").strip(), (r.get("vendor_name") or "").strip(), (r.get("website") or "").strip()
            if not key or not site or not site.startswith("http"):
                continue
            if key in prev and prev[key].get("check_status") == "confirmed":
                n["skipped"] += 1; continue
            if DIRECTORY.search(site):
                prev[key] = {"vendor_key": key, "vendor_name": name, "website": site, "check_status": "rejected: directory / social / government page, not the company's site", "evidence_url": "", "evidence_quote": "", "name_tokens_seen": "", "retrieved_date": TODAY, "proposed_by": os.path.basename(path)}
                n["directory"] += 1; continue
            want = toks(name)
            best = None
            site_host = (urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www.")
            pages = [site]
            ev = (r.get("evidence_url") or "").strip()
            if ev.startswith("http") and (urllib.parse.urlparse(ev).hostname or "").lower().removeprefix("www.").endswith(site_host.split(".", 1)[-1] if site_host.count(".") > 1 else site_host):
                pages.append(ev)  # only pages on the proposed site itself: a press release or directory on another host proves nothing about this site
            pages += [urllib.parse.urljoin(site, p) for p in ("about", "about-us", "contact", "contact-us", "a-propos", "nous-joindre")]
            for u in dict.fromkeys(pages):
                st, text, final = read(u)
                if st != "ok":
                    best = best or (st, u, "", [])
                    continue
                fh = (urllib.parse.urlparse(final or u).hostname or "").lower().removeprefix("www.")
                if not (fh == site_host or fh.endswith("." + site_host) or site_host.endswith("." + fh)):
                    continue  # redirected off the proposed site
                low = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
                seen = [t for t in want if re.search(r"\b" + re.escape(t) + r"\b", low)]  # whole words only ("mda" must not match "amdahl")
                exact = bool(want) and re.search(r"\b" + r"\W{0,3}".join(re.escape(t) for t in want) + r"\b", low) is not None
                core_ok = exact or (len(want) >= 2 and len(seen) >= 2 and seen[0] == want[0]) or (len(want) == 1 and seen and len(want[0]) >= 5)
                if core_ok:
                    i = low.find(seen[0]) if seen else -1
                    q = flat(text[max(0, i - 120):i + 180])[:300] if i >= 0 else ""
                    best = ("confirmed", final or u, q, seen); break
                best = ("name_not_on_site", final or u, "", seen)
                if u == site and len(pages) > 1:
                    continue
            st, eu, q, seen = best or ("unreadable", site, "", [])
            prev[key] = {"vendor_key": key, "vendor_name": name, "website": site if st == "confirmed" else "", "check_status": st, "evidence_url": eu if st == "confirmed" else "", "evidence_quote": q, "name_tokens_seen": " ".join(seen), "retrieved_date": TODAY, "proposed_by": os.path.basename(path)}
            n[st if st in n else "unreadable"] += 1
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(sorted(prev.values(), key=lambda d: d["vendor_key"]))
    os.replace(out + ".tmp", out)
    print("wrote", out, len(prev), n, flush=True)


if __name__ == "__main__":
    main()

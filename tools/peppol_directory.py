#!/usr/bin/env python3
"""Every Canadian participant of the Peppol Directory, matched to the ranked buyers (owner 2026-11-06, D8: "identify ALL Canadian
buyers with Peppol access points").

Reads the public Peppol Directory search API page by page (country=CA; 1 request/second, identified user agent) and keeps every
participant verbatim: participant identifier (scheme + value), registered names, country, geographic info, other identifiers,
websites, registration date, document types count. Then matches each participant to the ranked buyers by normalised name and by
website domain (exact matches only; no fuzzy guesses) and writes <repo>/data/incoming/claude/claude_peppol_participants.csv
with the API URL opened and a quote (the participant's own name line). rank.py fills `peppol_participant_id` /
`peppol_registered` from it. Also useful for vendors: a Canadian vendor with a Peppol id can e-invoice buyers that have one.
  python3 tools/peppol_directory.py [--repo ~/cch-crawler] [--ranked ranked_buyers.csv.gz] [--country CA]
"""
import argparse, csv, datetime, gzip, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://directory.peppol.eu/search/1.0/json"
TODAY = datetime.date.today().isoformat()
COLS = ["participant_id", "participant_scheme", "names", "country", "geo_info", "identifiers", "websites", "registration_date", "doc_types", "additional_info",
        "matched_buyer", "match_basis", "buyer_keys", "evidence_url", "evidence_quote", "retrieved_date", "public_page"]
STOP = {"the", "of", "de", "du", "des", "la", "le", "les", "and", "et", "inc", "ltd", "ltee", "ltée", "corp", "corporation", "limited", "incorporated", "co", "company", "llc", "ulc", "lp", "sencrl", "senc", "llp"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    toks = [t for t in re.findall(r"[a-z0-9]+", s) if t not in STOP]
    return " ".join(toks)


def dom(u):
    h = (urllib.parse.urlparse(u if "://" in (u or "") else "http://" + (u or "")).hostname or "").lower()
    h = h[4:] if h.startswith("www.") else h
    return h


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--ranked", default="")
    a.add_argument("--country", default="CA")
    a.add_argument("--page-size", type=int, default=100)
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_peppol_participants.csv")
    ranked = a.ranked or os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv.gz")
    by_name, by_dom = {}, {}
    opener = gzip.open if ranked.endswith(".gz") else open
    with opener(ranked, "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            n = norm(r.get("buyer") or "")
            if len(n) >= 6:
                by_name.setdefault(n, (r.get("buyer"), r.get("keys")))
            ln = norm((r.get("buyer_legal_name_as_published") or "").split(" (as")[0])
            if len(ln) >= 6:
                by_name.setdefault(ln, (r.get("buyer"), r.get("keys")))
            d = dom(r.get("buyer_website") or "")
            if d and d.count(".") >= 1 and not re.match(r"^(gov|gouv|gc|qc|on|ab|bc|sk|mb|ns|nb|nl|pe)\.(ca|qc\.ca)$", d):
                by_dom.setdefault(d, (r.get("buyer"), r.get("keys")))
    print("buyers: %d names, %d domains" % (len(by_name), len(by_dom)), flush=True)
    rows, page, total = [], 0, None
    while True:
        url = "%s?%s" % (API, urllib.parse.urlencode({"country": a.country, "resultPageCount": a.page_size, "resultPageIndex": page}))
        try:
            data = get(url)
        except Exception as e:
            print("page", page, "error", type(e).__name__, e, flush=True)
            if page == 0:
                sys.exit(2)
            time.sleep(10)
            try:
                data = get(url)
            except Exception:
                break
        total = data.get("total-result-count", total)
        matches = data.get("matches") or []
        for m in matches:
            pid = m.get("participantID") or {}
            ents = m.get("entities") or []
            names, idents, sites, geo, add, reg, cc = [], [], [], [], [], [], []
            for e in ents:
                for n in e.get("name") or []:
                    nm = n.get("name") if isinstance(n, dict) else str(n)
                    if nm and nm not in names:
                        names.append(nm)
                for i in e.get("identifiers") or []:
                    idents.append("%s:%s" % (i.get("scheme", ""), i.get("value", "")))
                for w in e.get("websites") or []:
                    sites.append(w if isinstance(w, str) else json.dumps(w))
                if e.get("geoInfo"):
                    geo.append(str(e["geoInfo"]))
                if e.get("additionalInfo"):
                    add.append(str(e["additionalInfo"]))
                if e.get("regDate"):
                    reg.append(str(e["regDate"]))
                if e.get("countryCode"):
                    cc.append(e["countryCode"])
            matched, basis, keys = "", "", ""
            for nm in names:
                hit = by_name.get(norm(nm))
                if hit:
                    matched, basis, keys = hit[0], "name (exact after normalisation): %s" % nm, hit[1]
                    break
            if not matched:
                for w in sites:
                    hit = by_dom.get(dom(w))
                    if hit:
                        matched, basis, keys = hit[0], "website domain: %s" % dom(w), hit[1]
                        break
            quote = ("%s %s — %s" % (pid.get("scheme", ""), pid.get("value", ""), "; ".join(names)))[:300]
            rows.append({"participant_id": pid.get("value", ""), "participant_scheme": pid.get("scheme", ""), "names": " | ".join(names)[:500], "country": ",".join(sorted(set(cc))),
                         "geo_info": " | ".join(geo)[:300], "identifiers": " | ".join(idents)[:500], "websites": " | ".join(sites)[:500], "registration_date": " | ".join(reg)[:60],
                         "doc_types": str(len(m.get("docTypes") or [])), "additional_info": " | ".join(add)[:300], "matched_buyer": matched or "", "match_basis": basis, "buyer_keys": keys or "",
                         "evidence_url": url, "evidence_quote": quote, "retrieved_date": TODAY,
                         "public_page": "https://directory.peppol.eu/public/locale-en_US/menuitem-search?q=" + urllib.parse.quote(pid.get("value", ""))})
        print("page %d: %d participants (total %s)" % (page, len(matches), total), flush=True)
        if not matches or (total is not None and (page + 1) * a.page_size >= int(total)):
            break
        page += 1
        time.sleep(1.0)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print("wrote", out, len(rows), "participants;", sum(1 for r in rows if r["matched_buyer"]), "matched to ranked buyers", flush=True)


if __name__ == "__main__":
    main()

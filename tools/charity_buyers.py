#!/usr/bin/env python3
"""CRA list of registered charities → buyers' Business Numbers (downstream §3.2 / §3.9): universities, hospitals, foundations, religious
and cultural bodies are registered charities, and the CRA publishes their BN (RR0001 account), legal name, address, designation,
category and fiscal period end as open data (dataset 80c00cdb-1358-415c-bb8b-0de7f12675b8 on open.canada.ca, T3010 files).

Downloads the latest "ident" (identification) and "weburl" files through the open-data CKAN API, then matches the ranked buyers by
exact normalised legal / account name (province must agree when known) or by website domain. Writes
<repo>/data/incoming/claude/claude_charity_buyers.csv with the file URL as evidence and the matched line as quote. rank.py fills
buyer_bn_as_published (labelled RR), buyer_legal_name_as_published, buyer_address, buyer_fiscal_year_end, buyer_charity_status.
  python3 tools/charity_buyers.py [--repo ~/cch-crawler] [--ranked ranked_buyers.csv.gz] [--workdir ~/cch-tasks/cra]
"""
import argparse, csv, datetime, glob, gzip, io, json, os, re, sys, unicodedata, urllib.parse, urllib.request, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
PKG = "https://open.canada.ca/data/api/3/action/package_show?id=80c00cdb-1358-415c-bb8b-0de7f12675b8"
TODAY = datetime.date.today().isoformat()
COLS = ["buyer_key", "buyer", "bn", "bn9", "legal_name", "account_name", "address", "city", "province", "postal_code", "designation", "category", "fiscal_period_end", "charity_status",
        "website", "match_basis", "source_url", "retrieved_date", "source_quote"]
STOP = {"the", "of", "de", "du", "des", "la", "le", "les", "l", "d", "and", "et", "inc", "incorporated", "corp", "corporation", "ltd", "ltee", "foundation", "fondation", "fund", "fonds"}
ORG_WORDS = {"the", "city", "town", "village", "township", "municipality", "municipal", "district", "county", "regional", "region", "rural", "ville", "municipalite", "mrc", "canton", "paroisse",
             "university", "universite", "college", "cegep", "school", "board", "hospital", "hopital", "health", "centre", "center", "services", "service", "society", "association", "foundation", "fondation",
             "public", "general", "canada", "canadian", "corporation", "corp", "inc", "ltd", "limited", "ltee", "of", "de", "du", "des", "la", "le", "les", "and", "et"}
SUB_RX = re.compile(r"\b(foundation|fondation|alumni|association|club|society|societe|auxiliary|friends|amis|parents|students|etudiants|union|trust|fund|fonds|endowment|booster|band|choir|team|league|church)\b")
PROV = {"ON": "ON", "QC": "QC", "BC": "BC", "AB": "AB", "SK": "SK", "MB": "MB", "NS": "NS", "NB": "NB", "NL": "NL", "PE": "PE", "YT": "YT", "NT": "NT", "NU": "NU"}


def norm(s, keep_type=True):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    toks = [t for t in re.findall(r"[a-z0-9]+", s) if t not in STOP]
    return " ".join(toks)


def host(u):
    h = (urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or "")).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    return dest


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--ranked", default="")
    a.add_argument("--workdir", default=os.path.expanduser("~/cch-tasks/cra"))
    a = a.parse_args()
    os.makedirs(a.workdir, exist_ok=True)
    pkg = json.loads(urllib.request.urlopen(urllib.request.Request(PKG, headers={"User-Agent": UA}), timeout=60).read())
    res = pkg["result"]["resources"]
    pick = {}
    for r in res:
        n = (r.get("name") or "") + " " + (r.get("url") or "")
        yr = re.search(r"(20\d\d)", n)
        for kind, rx in (("ident", r"ident"), ("weburl", r"web ?url|website")):
            if re.search(rx, n, re.I) and yr:
                if kind not in pick or int(yr.group(1)) > pick[kind][0]:
                    pick[kind] = (int(yr.group(1)), r["url"])
    print("resources:", {k: v for k, v in pick.items()}, flush=True)
    files = {}
    for kind, (yr, url) in pick.items():
        dest = os.path.join(a.workdir, "%s_%d%s" % (kind, yr, os.path.splitext(urllib.parse.urlparse(url).path)[1] or ".csv"))
        fetch(url, dest)
        if dest.endswith(".zip"):
            with zipfile.ZipFile(dest) as z:
                inner = [n for n in z.namelist() if n.lower().endswith(".csv")]
                z.extract(inner[0], a.workdir)
                dest = os.path.join(a.workdir, inner[0])
        files[kind] = dest
        print(kind, dest, os.path.getsize(dest), flush=True)
    web = {}
    if "weburl" in files:
        for r in csv.DictReader(open(files["weburl"], encoding="utf-8-sig", errors="replace", newline="")):
            bn = (r.get("BN/NE") or r.get("BN") or "").strip()
            u = (r.get("Contact URL") or r.get("URL") or "").strip()
            if bn and u:
                web.setdefault(bn, u)
    by_name, by_dom = {}, {}
    cols = None
    for r in csv.DictReader(open(files["ident"], encoding="utf-8-sig", errors="replace", newline="")):
        if cols is None:
            cols = list(r.keys()); print("ident columns:", cols[:30], flush=True)
        bn = (r.get("BN") or r.get("BN/NE") or "").strip()
        if not bn:
            continue
        r["_web"] = web.get(bn, "")
        for col in ("Legal Name", "Account Name"):
            k = norm(r.get(col))
            if len(k) >= 6:
                by_name.setdefault((k, (r.get("Province") or "").strip().upper()), r)
                by_name.setdefault((k, ""), r)
        if r["_web"]:
            by_dom.setdefault(host(r["_web"]), r)
    print("charities indexed:", len(by_dom), "with website;", len(by_name), "name keys", flush=True)
    ranked = a.ranked or os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv.gz")
    opener = gzip.open if ranked.endswith(".gz") else open
    out_rows, seen = [], set()
    src_url = pick["ident"][1]
    for x in csv.DictReader(opener(ranked, "rt", encoding="utf-8")):
        key = (x.get("keys") or "").split("|")[0]
        if key in seen:
            continue
        prov = PROV.get(x.get("jurisdiction") or "", "")
        d = host(x.get("buyer_website") or "") if x.get("buyer_website") else ""
        hit, basis = None, ""
        bname = x.get("buyer") or ""
        core = {t for t in norm(bname).split() if t not in ORG_WORDS and len(t) > 1}
        if d and d in by_dom:
            cand = by_dom[d]
            cn = norm(cand.get("Legal Name")) + " " + norm(cand.get("Account Name"))
            raw = ((cand.get("Legal Name") or "") + " " + (cand.get("Account Name") or "")).lower()  # norm() drops 'foundation' as a stop word; test the raw names
            # the charity on the organisation's domain must BE the organisation: same core name, and not a foundation / club / association of it
            if core and core <= set(cn.split()) and not (SUB_RX.search(raw) and not SUB_RX.search(bname.lower())):
                hit, basis = cand, "website domain (%s) + name" % d
        if not hit:
            for nm in (x.get("buyer"), (x.get("buyer_legal_name_as_published") or "").split(" (")[0]):
                k = norm(nm)
                if len(k) >= 6 and (k, prov) in by_name:
                    cand = by_name[(k, prov)]
                    raw = ((cand.get("Legal Name") or "") + " " + (cand.get("Account Name") or "")).lower()
                    if SUB_RX.search(raw) and not SUB_RX.search((nm or "").lower()):
                        continue
                    hit, basis = cand, "exact name%s" % (" + province" if prov else "")
                    break
        if not hit:
            continue
        seen.add(key)
        bn = (hit.get("BN") or hit.get("BN/NE") or "").strip()
        fpe = (hit.get("Fiscal Period End") or hit.get("FPE") or hit.get("Fiscal period end") or "").strip()
        addr = ", ".join(v.strip() for v in (hit.get("Address"), hit.get("Address Line 1"), hit.get("Address Line 2")) if v and v.strip())
        out_rows.append({"buyer_key": key, "buyer": x.get("buyer"), "bn": bn, "bn9": re.sub(r"\D", "", bn)[:9], "legal_name": (hit.get("Legal Name") or "").strip(), "account_name": (hit.get("Account Name") or "").strip(),
                         "address": addr, "city": (hit.get("City") or "").strip(), "province": (hit.get("Province") or "").strip(), "postal_code": (hit.get("Postal Code") or "").strip(),
                         "designation": (hit.get("Designation") or hit.get("Designation Code") or "").strip(), "category": (hit.get("Category") or hit.get("Category Code") or "").strip(),
                         "fiscal_period_end": fpe, "charity_status": (hit.get("Status") or hit.get("Charity Status") or "registered (listed)").strip(), "website": hit.get("_web") or "",
                         "match_basis": basis, "source_url": src_url, "retrieved_date": TODAY,
                         "source_quote": ("%s; %s; %s; %s %s; FPE %s" % (bn, hit.get("Legal Name") or "", hit.get("Account Name") or "", hit.get("City") or "", hit.get("Province") or "", fpe))[:300]})
    out = os.path.join(a.repo, "data/incoming/claude/claude_charity_buyers.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out_rows)
    print("wrote", out, len(out_rows), "buyers matched to registered charities", flush=True)


if __name__ == "__main__":
    main()

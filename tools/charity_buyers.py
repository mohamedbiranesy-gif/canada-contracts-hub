#!/usr/bin/env python3
"""CRA list of registered charities → buyers' Business Numbers (downstream §3.2 / §3.9): universities, hospitals, foundations, religious
and cultural bodies are registered charities, and the CRA publishes their BN (RR0001 account), legal name, address, designation,
category and fiscal period end as open data (dataset 80c00cdb-1358-415c-bb8b-0de7f12675b8 on open.canada.ca, T3010 files).

Downloads the latest "ident" (identification) and "weburl" files through the open-data CKAN API, then matches the ranked buyers by
exact normalised legal / account name (province must agree when known) or by website domain. Writes
<repo>/data/incoming/claude/claude_charity_buyers.csv with the file URL as evidence and the matched line as quote. rank.py fills
buyer_bn_as_published (labelled RR), buyer_legal_name_as_published, buyer_address, buyer_fiscal_year_end, buyer_charity_status.
2026-11-10: also writes the list itself in a compact form, <repo>/data/incoming/claude/claude_cra_charities.csv.gz (one line per registered
account: number, legal and account name, address, designation, category, web address), so that rank.py can join a row to the list by the
registration number the organisation prints on its own site — a tie neither the name nor the web address gives ("Ronald McDonald House Toronto"
is TORONTO CHILDREN'S CARE INC.). The file is written with the same bytes while the CRA's files do not change. Runs daily in the cloud
(claude-engines.yml, bulk_registry step); the ranked table is read through tools/ranked_io.py (a release asset since 2026-11-10).
  python3 tools/charity_buyers.py [--repo .] [--ranked ranked_buyers.csv.gz] [--workdir ~/cch-tasks/cra]
"""
import argparse, csv, datetime, glob, gzip, io, json, os, re, sys, unicodedata, urllib.parse, urllib.request, zipfile

csv.field_size_limit(1 << 30)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ranked_io as RIO  # noqa: E402
import registry_names as RN  # noqa: E402
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LIST_COLS = ["bn", "legal_name", "account_name", "address", "city", "province", "postal_code", "country", "designation", "category", "website", "source_url", "retrieved_date"]

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
COMMON_NAME = set("""church eglise chapel chapelle baptist united unie pentecostal presbyterian anglican lutheran catholic catholique gospel bible assembly assemblee tabernacle
fellowship christian chretienne first grace calvary trinity faith hope st saint sainte ste holy our lady notre dame redeemer emmanuel immanuel bethel zion parish paroisse mission temple
mosque masjid synagogue congregation legion branch lions rotary kiwanis club optimist optimiste chevaliers knights""".split())
INSTITUTION = set("hospital hopital school ecole college centre center community communautaire society association foundation fondation home maison care services service canada canadian".split())


def needs_place(name):
    """a name of the kind many bodies carry (a saint's, a denomination's, a service club's) with fewer than two words of its own"""
    toks = norm(name).split()
    return any(t in COMMON_NAME for t in toks) and len([t for t in toks if t not in COMMON_NAME and t not in INSTITUTION and len(t) > 2]) < 2


BODY_KIND = re.compile(r"\b(county|comt[ée]|city|ville|town|township|canton|village|municipality|municipalit[ée]|district|region|r[ée]gion|mrc|parish|paroisse)\b", re.I)
CA_PC = re.compile(r"(?<![A-Z0-9])[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s?\d[ABCEGHJ-NPRSTV-Z]\d(?![A-Z0-9])")
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
    a.add_argument("--repo", default=ROOT)
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
    src_url = pick["ident"][1]
    listed = []
    for r in csv.DictReader(open(files["ident"], encoding="utf-8-sig", errors="replace", newline="")):
        _bn = (r.get("BN") or r.get("BN/NE") or "").strip().upper().replace(" ", "")
        if re.fullmatch(r"\d{9}RR\d{4}", _bn):
            listed.append({"bn": _bn, "legal_name": re.sub(r"\s+", " ", r.get("Legal Name") or "").strip(), "account_name": re.sub(r"\s+", " ", r.get("Account Name") or "").strip(),
                           "address": ", ".join(v.strip() for v in (r.get("Address Line 1"), r.get("Address Line 2")) if v and v.strip()), "city": (r.get("City") or "").strip(),
                           "province": (r.get("Province") or "").strip(), "postal_code": (r.get("Postal Code") or "").strip(), "country": (r.get("Country") or "").strip(),
                           "designation": (r.get("Designation") or "").strip(), "category": (r.get("Category") or "").strip(), "website": web.get((r.get("BN") or r.get("BN/NE") or "").strip(), ""),
                           "source_url": src_url, "retrieved_date": ""})
        if cols is None:
            cols = list(r.keys()); print("ident columns:", cols[:30], flush=True)
        bn = (r.get("BN") or r.get("BN/NE") or "").strip()
        if not bn:
            continue
        r["_web"] = web.get(bn, "")
        for col in ("Legal Name", "Account Name"):
            k = norm(r.get(col))
            if len(k) >= 6:
                # every charity of that name is kept (2026-11-10: the first one found used to stand for all — "Grace Presbyterian Church" of Millerton, N.B.,
                # for a church of that name anywhere)
                by_name.setdefault((k, (r.get("Province") or "").strip().upper()), {})[bn] = r
                by_name.setdefault((k, ""), {})[bn] = r
        if r["_web"]:
            by_dom.setdefault(host(r["_web"]), r)
    print("charities indexed:", len(by_dom), "with website;", len(by_name), "name keys", flush=True)
    # the list itself, for the join by registration number in rank.py. The retrieval date changes only when the list's content does (the date of
    # the copy already in the repo is kept while the lines are the same), so that an unchanged list is an unchanged file in git.
    lp = os.path.join(a.repo, "data/incoming/claude/claude_cra_charities.csv.gz")
    listed.sort(key=lambda d: d["bn"])
    old_date, old_lines = "", None
    if os.path.exists(lp):
        try:
            with gzip.open(lp, "rt", encoding="utf-8", newline="") as f:
                old = list(csv.DictReader(f))
            old_date = old[0]["retrieved_date"] if old else ""
            old_lines = [{c: o.get(c, "") for c in LIST_COLS if c != "retrieved_date"} for o in old]
        except Exception as e:
            print("the list in the repo could not be read (%s): written anew" % e, flush=True)
    same = old_lines is not None and old_lines == [{c: d[c] for c in LIST_COLS if c != "retrieved_date"} for d in listed]
    for d in listed:
        d["retrieved_date"] = old_date if (same and old_date) else TODAY
    if not same:
        os.makedirs(os.path.dirname(lp), exist_ok=True)
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=LIST_COLS, lineterminator="\n"); w.writeheader(); w.writerows(listed)
        with open(lp, "wb") as f, gzip.GzipFile(filename="", mode="wb", fileobj=f, mtime=0) as g:
            g.write(buf.getvalue().encode("utf-8"))
    print("CRA list:", len(listed), "registered accounts;", "unchanged, file kept" if same else "written to " + lp, flush=True)
    ranked = a.ranked or os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv.gz")
    out_rows, seen = [], set()
    for x in RIO.rows(ranked):
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
            # 2026-11-10: a name alone names a charity when ONE charity carries it (several: the city of the organisation's address decides, or
            # nothing does — the first one found used to stand for all), and when the organisation is in Canada by its record, its .ca address or a
            # Canadian postal code: "City of Richmond" (California), "Victoria University" (Melbourne), "Trinity College" (Hartford) had been given
            # the numbers of their Canadian namesakes. The names tried: the organisation's own; the legal person its site states in so many words
            # (tools/registry_names.py); and the name in its legal-name cell — but a name read off a page that names another KIND of body than the
            # organisation's own name does is not tried ("County of Middlesex", on the about page of the Municipality of Middlesex Centre).
            addr_l = (x.get("buyer_address") or "").lower()
            in_canada = bool(prov) or (x.get("jurisdiction") or "") in ("CA", "FED") or d.endswith(".ca") or bool(CA_PC.search((x.get("buyer_address") or "").upper()))
            cell = (x.get("buyer_legal_name_as_published") or "").split(" (")[0].strip()
            kb = {w.lower() for w in BODY_KIND.findall(bname)}
            if cell and kb and BODY_KIND.search(cell) and not (kb & {w.lower() for w in BODY_KIND.findall(cell)}):
                cell = ""
            for nm in dict.fromkeys(n for n in (x.get("buyer"), RN.lookup_name(x)[0], cell) if n):
                k = norm(nm)
                cands = list((by_name.get((k, prov)) or {}).values()) if len(k) >= 6 else []
                # a foundation / club / association of that name is not the organisation, unless the organisation's name says it is one
                _raw = lambda c: ((c.get("Legal Name") or "") + " " + (c.get("Account Name") or "")).lower()
                _sub = {w.lower() for w in SUB_RX.findall((nm or "").lower())}
                cands = [c for c in cands if not (SUB_RX.search(_raw(c)) and not _sub)]
                if _sub and any(_sub & {w.lower() for w in SUB_RX.findall(_raw(c))} for c in cands):
                    # "Fondation du Cégep de La Pocatière" is the foundation, not the cégep (norm() leaves the word out of the key of both)
                    cands = [c for c in cands if _sub & {w.lower() for w in SUB_RX.findall(_raw(c))}]
                if not cands:
                    continue
                city_fits = lambda c: bool((c.get("City") or "").strip()) and bool(re.search(r"(?<![a-z])" + re.escape(c["City"].strip().lower()) + r"(?![a-z])", addr_l))
                how = ""
                if len({(c.get("BN") or c.get("BN/NE") or "")[:9] for c in cands}) > 1:
                    cands = [c for c in cands if city_fits(c)]
                    if len({(c.get("BN") or c.get("BN/NE") or "")[:9] for c in cands}) != 1:
                        continue
                    how = " + city of the organisation's address"
                elif (not in_canada or needs_place(nm)) and city_fits(cands[0]):
                    how = " + city of the organisation's address"
                elif not in_canada or needs_place(nm):
                    continue  # no sign of Canada on the row — or a name that many congregations and clubs carry ("Grace Community Church", "St. Joseph's
                              # Hospital"): one charity of that name in the list does not make it this one; the city of the address must agree
                hit, basis = sorted(cands, key=lambda c: (c.get("BN") or c.get("BN/NE") or ""))[0], "exact name%s%s" % (" + province" if prov else "", how)
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
    # a match that stands as it stood keeps the date it was first written with: the file changes in git by its new and changed lines only
    if os.path.exists(out):
        try:
            prev = {r["buyer_key"]: r for r in csv.DictReader(open(out, encoding="utf-8", errors="replace", newline=""))}
            for r in out_rows:
                o = prev.get(r["buyer_key"])
                if o and all((o.get(c) or "") == (r.get(c) or "") for c in COLS if c != "retrieved_date") and o.get("retrieved_date"):
                    r["retrieved_date"] = o["retrieved_date"]
        except Exception as e:
            print("the matches in the repo could not be read (%s): dates of today" % e, flush=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(out_rows)
    print("wrote", out, len(out_rows), "buyers matched to registered charities", flush=True)


if __name__ == "__main__":
    main()

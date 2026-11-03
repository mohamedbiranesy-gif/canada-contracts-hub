#!/usr/bin/env python3
"""Official US directories with each body's website, for resolving the names our portal / lead tools find (school
districts, colleges, public libraries) to their own sites. No AI. Bulk public files, downloaded once:
  - NCES CCD preliminary directory 2024-25 (LEA = school district: LEA_NAME, ST, WEBSITE)
  - IPEDS HD2023 (INSTNM, STABBR, WEBADDR)
  - IMLS Public Libraries Survey FY2022 administrative entities (LIBNAME, STABR, WEBADDR) when the URL still answers
Output ~/cch-crawler-state/us_directories.tsv: kind, name, state, website. Then `--resolve <lead.jsonl>...` fills the
`website` of lead rows whose publisher name equals a directory name (normalised: case, punctuation, "ISD" =
"Independent School District", "SD" = "School District", "Public Schools" = "School District"), writing
~/cch-crawler-state/websites.tsv rows (the file tools/ap_crawler.py and crawl_some.py already read) with basis
"nces:<kind>", and ~/cch-crawl-some/directory_sites.csv (task list for crawl_some).
  python3 tools/us_directories.py [--resolve ~/cch-leads/socrata_tech_*_cdx.jsonl ...]
"""
import argparse, csv, glob, hashlib, io, json, os, re, sys, time, urllib.parse, urllib.request, zipfile

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
STATE = os.path.expanduser("~/cch-crawler-state")
SRC = os.path.expanduser("~/cch-sources/us_directories")
OUT = os.path.join(STATE, "us_directories.tsv")
WEBSITES = os.path.join(STATE, "websites.tsv")
TASKS = os.path.expanduser("~/cch-crawl-some/directory_sites.csv")
FILES = {
    "ccd": "https://ies.ed.gov/sites/default/files/data-asset/ccd-common-core-data/2025/08/2024-25-common-core-data-ccd-preliminary-directory-files/2025046%20Preliminary%20Data%20Release%20CCD%20Nonfiscal_0.zip",
    "ipeds": "https://nces.ed.gov/ipeds/datacenter/data/HD2023.zip",
    "pls": "https://www.imls.gov/sites/default/files/2024-06/pls_fy2022_csv.zip",
}
LEGAL = re.compile(r"\b(the|of|and|inc|incorporated|ltd|llc|corp|corporation|co|company|limited|district|dist|public|schools?|"
                   r"independent|unified|consolidated|community|county|city|town|township|village|borough|board|education|"
                   r"isd|usd|cusd|csd|sd|ufsd|regional|central|area|local|free|union|college|university|libraries|library|system)\b")
ABBR = [(r"\bisd\b", "independent school district"), (r"\busd\b", "unified school district"), (r"\bcusd\b", "community unit school district"),
        (r"\bcsd\b", "community school district"), (r"\bufsd\b", "union free school district"), (r"\bsd\b", "school district"),
        (r"\bpublic schools\b", "school district"), (r"\bpublic school district\b", "school district"), (r"\bschools\b", "school district"),
        (r"\bco\b", "county"), (r"\bst\b", "saint"), (r"\bmt\b", "mount"), (r"\bft\b", "fort")]


def norm(s):
    s = re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    for a, b in ABBR:
        s = re.sub(a, b, s)
    return re.sub(r"\s+", " ", s).strip()


def fetch(url):
    os.makedirs(SRC, exist_ok=True)
    p = os.path.join(SRC, hashlib.sha1(url.encode()).hexdigest()[:12] + ".zip")
    if not os.path.exists(p):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=600) as r, open(p, "wb") as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
    return p


def rows_from_zip(p, want_cols):
    z = zipfile.ZipFile(p)
    for name in z.namelist():
        if not name.lower().endswith(".csv"):
            continue
        with z.open(name) as fh:
            txt = io.TextIOWrapper(fh, encoding="latin-1", errors="replace")
            rd = csv.DictReader(txt)
            cols = {c.upper(): c for c in rd.fieldnames or []}
            if not all(w in cols for w in want_cols):
                continue
            for r in rd:
                yield name, {w: (r.get(cols[w]) or "").strip() for w in want_cols}


def build():
    out = []
    try:
        for name, r in rows_from_zip(fetch(FILES["ccd"]), ["LEA_NAME", "ST", "WEBSITE"]):
            if r["WEBSITE"] and "lea" in name.lower():
                out.append(("district", r["LEA_NAME"], r["ST"], r["WEBSITE"]))
    except Exception as e:
        print("ccd:", e, flush=True)
    try:
        for name, r in rows_from_zip(fetch(FILES["ipeds"]), ["INSTNM", "STABBR", "WEBADDR"]):
            if r["WEBADDR"]:
                out.append(("college", r["INSTNM"], r["STABBR"], r["WEBADDR"]))
    except Exception as e:
        print("ipeds:", e, flush=True)
    try:
        for name, r in rows_from_zip(fetch(FILES["pls"]), ["LIBNAME", "STABR", "WEBADDR"]):
            if r["WEBADDR"]:
                out.append(("library", r["LIBNAME"], r["STABR"], r["WEBADDR"]))
    except Exception as e:
        print("pls:", e, flush=True)
    os.makedirs(STATE, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        for kind, nm, st, web in out:
            web = web.strip()
            if not re.match(r"https?://", web, re.I):
                web = "https://" + web.lstrip("/")
            f.write("%s\t%s\t%s\t%s\n" % (kind, nm.replace("\t", " "), st, web))
    print("directory entries: %d (%s)" % (len(out), {k: sum(1 for x in out if x[0] == k) for k in ("district", "college", "library")}), flush=True)


def resolve(files):
    idx = {}
    for line in open(OUT, encoding="utf-8"):
        kind, nm, st, web = line.rstrip("\n").split("\t")
        idx.setdefault(norm(nm), []).append((kind, st, web))
        idx.setdefault(norm(LEGAL.sub(" ", norm(nm))), []).append((kind, st, web))
    have = {l.split("\t")[0] for l in open(WEBSITES, encoding="utf-8")} if os.path.exists(WEBSITES) else set()
    new = not os.path.exists(TASKS)
    n_try = n_hit = 0
    with open(WEBSITES, "a", encoding="utf-8") as wf, open(TASKS, "a", newline="", encoding="utf-8") as tf:
        tw = csv.writer(tf)
        if new:
            tw.writerow(["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
                         "known_general_email", "known_procurement_email", "contracts_in_dataset"])
        for f in files:
            for line in open(f, encoding="utf-8", errors="replace"):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("website"):
                    continue
                name = (r["publisher"] if not r.get("buyer_unit") else "%s - %s" % (r["publisher"], r["buyer_unit"])).strip()
                key = "lead:" + hashlib.sha1(("%s|%s" % (r["domain"], name.lower())).encode()).hexdigest()[:16]
                if key in have:
                    continue
                n_try += 1
                cands = idx.get(norm(name)) or idx.get(norm(LEGAL.sub(" ", norm(name)))) or []
                webs = {c[2].lower().rstrip("/") for c in cands}
                if len(webs) != 1:
                    continue  # unknown, or the same name in several states: not resolved
                kind, st, web = cands[0]
                h = (urllib.parse.urlparse(web).hostname or "").lower()
                if not h:
                    continue
                have.add(key); n_hit += 1
                wf.write("%s\thttps://%s/\tnces:%s %s\n" % (key, h, kind, st))
                tw.writerow(["CL-DIR-%05d" % n_hit, "", key, name, "", "US", "https://%s/" % h, "", "", 1])
    print("names tried: %d, resolved: %d" % (n_try, n_hit), flush=True)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--resolve", nargs="*")
    a = a.parse_args()
    if not os.path.exists(OUT) or time.time() - os.path.getmtime(OUT) > 30 * 86400:
        build()
    if a.resolve:
        files = [p for g in a.resolve for p in glob.glob(os.path.expanduser(g))]
        resolve(files)

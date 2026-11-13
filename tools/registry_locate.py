#!/usr/bin/env python3
"""Where an organisation is, by the head office it declares to a business register: the organisations with a confirmed role mailbox that no pass on
their own pages, no places dataset and no telephone listing located (no AI).

An organisation declares its head office (domicile, registered office) to its business register; the Registraire des entreprises du Québec and
Corporations Canada publish theirs as open data (tools/bulk_registry_match.py reads the same two files for the rows of the table). For an
organisation still unlocated, its name as its own home page gives it is matched to the registers with the matcher's rules — the very same name
(accents, punctuation and legal forms aside) as ONE current registered body; several, or a struck-off one only: nothing — and, here, only when the
organisation's province is known and agrees: its own telephone number's area code (site_facts/phones.tsv), a .qc.ca site for Québec. A sole
proprietorship (a natural person) gives no address. The head office names the electricity distributor of its address (tools/by_location.py) and
the row says the address is the one declared to the register.

  targets                 -> out/locate_targets.csv (key, site, name, prov)
  match --req ZIP --cc G  -> data/incoming/claude/site_facts/facts_<stamp>g.gz (address_how "registry") + site_facts/registry_locate_done.tsv
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, sys, time, urllib.parse

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
FACTS = os.path.join(INC, "site_facts")
DONE = os.path.join(FACTS, "registry_locate_done.tsv")
TARGETS = os.path.join(ROOT, "out", "locate_targets.csv")
TODAY = time.strftime("%Y-%m-%d")
AC = {"QC": "418 438 450 514 579 581 819 873 367 354 263 468", "ON": "226 249 289 343 365 416 437 519 548 613 647 683 705 742 753 807 905 382",
      "BC": "236 250 257 604 672 778", "AB": "368 403 587 780 825", "MB": "204 431 584", "SK": "306 474 639", "NS": "782 902", "NB": "428 506", "NL": "709 879"}
PROV_OF_AC = {a: p for p, L in AC.items() for a in L.split()}
# the matching rules' version, written on every done line: an organisation the registers did not locate is tried again when the rules change
# (v1 2026-11-13 12Z: very same name as ONE current body; v2 2026-11-13 14Z: and, in Québec, a current OTHER name declared by one body only;
#  v3 2026-11-13 15Z: and the legal person the organisation's own home page prints — copyright line, operator sentence, schema.org legalName)
RULES = "v3"


def cmd_targets(a):
    last = {}
    with open(os.path.join(FACTS, "addr_reread_done.tsv"), encoding="utf-8") as f:
        for l in f:
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2:
                last[q[0]] = q[1]
    unl = {k for k, s in last.items() if s in ("city_nothing", "legal_nothing", "nothing")}
    for p in (os.path.join(INC, "overture", "phone_places.csv"), os.path.join(INC, "fsq", "phone_places.csv")):
        if os.path.exists(p):
            unl -= {r["key"] for r in csv.DictReader(open(p, encoding="utf-8", newline=""))}
    done = {}
    if os.path.exists(DONE):
        for l in open(DONE, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2 and q[0]:
                done[q[0]] = (q[1], q[3] if len(q) >= 4 else "v1")  # the latest line of a key counts
    done = {k for k, (st, ver) in done.items() if st == "found" or ver == RULES}
    unl -= done
    ph = {}
    if os.path.exists(os.path.join(FACTS, "phones.tsv")):
        for l in open(os.path.join(FACTS, "phones.tsv"), encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) >= 2 and q[0] in unl:
                ph[q[0]] = q[1]
    name, site = {}, {}
    for p in sorted(glob.glob(os.path.join(FACTS, "facts_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for l in f:
                try:
                    d = json.loads(l)
                except ValueError:
                    continue
                k = d.get("key")
                if k in unl:
                    if d.get("site_name") and k not in name:
                        name[k] = d["site_name"]
                    if d.get("site") and k not in site:
                        site[k] = d["site"]
    n = collections.Counter()
    os.makedirs(os.path.dirname(TARGETS), exist_ok=True)
    with open(TARGETS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "site", "name", "prov"])
        for k in sorted(unl):
            nm, st = name.get(k, ""), site.get(k, "")
            prov = PROV_OF_AC.get((ph.get(k) or "")[:3], "")
            if not prov and re.search(r"\.qc\.ca(?:/|$)", st or ""):
                prov = "QC"
            if not nm or not prov:
                n["no name of its own" if not nm else "no province known (no telephone number, not .qc.ca)"] += 1
                continue
            w.writerow([k, st, nm, prov])
            n["target (%s)" % prov] += 1
    print("registry-locate targets: %d unlocated; %s -> %s" % (len(unl), dict(n), TARGETS), flush=True)


LEGAL = os.path.join(FACTS, "legal_names.csv.gz")  # (2026-11-13) the legal person a target's own home page prints: key, name, how, url, quote, date


def legal_names():
    """{key: (legal name, how, url, quote)} — the names read by `names` (append-only file; the latest line of a key counts)"""
    out = {}
    if os.path.exists(LEGAL):
        with gzip.open(LEGAL, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r.get("name"):
                    out[r["key"]] = (r["name"], r.get("how") or "", r.get("url") or "", r.get("quote") or "")
    return out


_FORM = re.compile(r"\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|corp|corporation|llp|ulc|s\.?e\.?n\.?c\.?(?:r\.?l\.?)?|co-?op(?:erative)?|coop[ée]rative)\b\.?", re.I)
_GENERIC_W = set("the and des les une inc ltd ltee corp corporation limited limitee group groupe services service solutions canada quebec ontario company compagnie cie".split())


def _toks(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return {t for t in re.findall(r"[a-z0-9]{3,}", s) if t not in _GENERIC_W}


def fits(legal, name, host):
    """the legal person printed on the site is the site's own: it carries a legal form, and a distinctive word of it is in the site's own name or
    in the domain name (the domain's label read whole, or the word found inside it: "nighthawx" in nighthawx.ca)"""
    if not legal or not _FORM.search(legal) or len(legal) > 90 or re.search(r"\d{3}[ -]\d{3}[ -]\d{4}|association of|realtors|mls|acknowledg|territor", legal, re.I):
        return False
    lt = _toks(_FORM.sub(" ", legal))
    lab = re.sub(r"[^a-z0-9]", "", (host or "").lower().removeprefix("www.").split(".")[0])
    return bool(lt & _toks(name)) or any(len(t) >= 4 and t in lab for t in lt)


def cmd_names(a):
    """2026-11-13: an organisation whose site gives only its trade name ("Clarity Business Consulting") often prints the legal person in its
    footer ("© 2025 Clarity Business Consulting Inc."), in a sentence ("This website is operated by …") or in its schema.org legalName. The
    home page of each target is read once (robots.txt respected, identified user agent, one request a second a site) and that name kept, with
    the page and the line it stands in; `match` then looks it up as well as the site's own name."""
    import threading
    from concurrent.futures import ThreadPoolExecutor
    import ap_crawler as C
    import org_extras as OX
    k, n = (int(x) for x in a.shard.split("/"))
    tg = [t for t in csv.DictReader(open(a.targets, encoding="utf-8", newline="")) if int(hashlib.sha1(t["key"].encode()).hexdigest(), 16) % n == k]
    have = legal_names()
    tg = [t for t in tg if t["key"] not in have and t.get("site")]
    deadline = time.time() + a.minutes * 60
    os.makedirs("out", exist_ok=True)
    lock, stats = threading.Lock(), collections.Counter()
    fo = open("out/locate_names_%d.csv" % k, "w", encoding="utf-8", newline="")
    w = csv.writer(fo)
    w.writerow(["key", "name", "how", "url", "quote", "date"])

    def one(t):
        if time.time() > deadline:
            return
        url = t["site"] if t["site"].startswith("http") else "https://%s/" % t["site"]
        try:
            if not C.allowed(url):
                with lock:
                    stats["robots"] += 1
                return
            st, ct, body, final = C.fetch(url)
            raw = body.decode("utf-8", "replace") if isinstance(body, (bytes, bytearray)) else (body or "")
        except Exception:
            with lock:
                stats["unreachable"] += 1
            return
        if not raw:
            with lock:
                stats["no page"] += 1
            return
        host = (urllib.parse.urlparse(final or url).hostname or "").lower()
        text = C.visible(raw)
        got = None
        try:
            j = OX.jsonld_org(raw, host, t["name"]) or {}
            if j.get("legalName"):
                got = (j["legalName"], "schema.org legalName of its home page", j.get("legalName"))
        except Exception:
            pass
        if not got:
            op = OX.operator_name(text)
            if op:
                got = (op[0], "the operator its home page names", OX.quote_pos(text, op[1], op[0]))
        if not got:
            ln = OX.legal_name(text, host)
            if ln:
                got = (ln, "the copyright line of its home page", OX.quote_at(text, ln))
        if got and not fits(got[0], t["name"], host):
            # a third party in the footer ("the REALTORS® Association of Edmonton" of an MLS notice, a land acknowledgment, a photographer's credit):
            # the legal person must carry a legal form and share a distinctive word with the site's own name or its domain name
            with lock:
                stats["a name that is not the site's (left out)"] += 1
            got = None
        with lock:
            stats["read"] += 1
            if got:
                stats["legal name"] += 1
                w.writerow([t["key"], got[0][:120], got[1], final or url, (got[2] or "")[:300], TODAY])
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, tg))
    fo.close()
    print("registry-locate names, shard %d/%d: %d targets — %s" % (k, n, len(tg), dict(stats)), flush=True)


def cmd_merge_names(a):
    rows = []
    for p in sorted(glob.glob(os.path.join(a.dir, "locate_names_*.csv"))):
        rows += list(csv.DictReader(open(p, encoding="utf-8", newline="")))
    old = []
    if os.path.exists(LEGAL):
        with gzip.open(LEGAL, "rt", encoding="utf-8", newline="") as fh:
            old = list(csv.DictReader(fh))
    os.makedirs(FACTS, exist_ok=True)
    with gzip.open(LEGAL, "wt", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["key", "name", "how", "url", "quote", "date"])
        w.writeheader()
        for r in old + rows:
            w.writerow({c: r.get(c) or "" for c in ["key", "name", "how", "url", "quote", "date"]})
    print("legal names: %d new, %d on file -> %s" % (len(rows), len(old) + len(rows), LEGAL), flush=True)


def cmd_match(a):
    import bulk_registry_match as BRM
    import by_location as BL
    tg = list(csv.DictReader(open(a.targets, encoding="utf-8", newline="")))
    lnames = legal_names()
    # the legal person the site itself prints first (a register knows it under that name), then the site's own name
    orgs = [("buyer", t["key"], lnames[t["key"]][0], t["prov"], t["site"], "") for t in tg if t["key"] in lnames]
    orgs += [("buyer", t["key"], t["name"], t["prov"], t["site"], "") for t in tg]
    done, rows = set(), []
    if a.req:
        rows += BRM.match_req([o for o in orgs if o[3] == "QC"], a.req, done, other_unique=True)
    cc = [p for pat in a.cc for p in sorted(glob.glob(pat))]
    if cc:
        rows += BRM.match_cc([o for o in orgs if o[3]], cc, done)
    site = {t["key"]: t["site"] for t in tg}
    prov_of = {t["key"]: t["prov"] for t in tg}
    n, out = collections.Counter(), []
    for r in rows:
        if r.get("status") != "found":
            n[r.get("status") or "?"] += 1
            continue
        addr = (r.get("reg_office_address") or "").strip()
        if not BL.fsa_of(addr):
            n["found, no address with a postal code (a sole proprietor's, or none)"] += 1
            continue
        if r.get("reg_office_province") and r["reg_office_province"] != prov_of.get(r["key"], r["reg_office_province"]):
            n["found, the head office is in another province"] += 1
            continue
        reg = "the Registraire des entreprises du Québec" if "Québec" in (r.get("registry_source") or "") else "Corporations Canada"
        out.append({"key": r["key"], "site": site.get(r["key"], ""), "date": TODAY, "address_country": "CA", "address": addr[:200],
                    "address_quote": ("%s, %s: %s" % (reg, r.get("juri_id") or "", r.get("source_quote") or ""))[:300],
                    "address_url": r.get("api_url") or "", "address_how": "registry",
                    "registry_name": r.get("matched_name") or "", "registry_id": r.get("juri_id") or ""})
        n["located (%s)" % reg] += 1
    os.makedirs(FACTS, exist_ok=True)
    if out:
        p = os.path.join(FACTS, "facts_%sg.gz" % a.stamp)
        with gzip.open(p, "wt", encoding="utf-8") as f:
            for o in out:
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
    with open(DONE, "a", encoding="utf-8") as f:
        got = {o["key"] for o in out}
        for t in tg:
            f.write("%s\t%s\t%s\t%s\n" % (t["key"], "found" if t["key"] in got else "registry_nothing", TODAY, RULES))
    print("registry-locate: %d targets, %d located by the head office declared to a register; %s" % (len(tg), len(out), dict(n)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["targets", "names", "merge-names", "match"])
    ap.add_argument("dir", nargs="?", default="shards")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--minutes", type=float, default=100)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--targets", default=TARGETS)
    ap.add_argument("--req", default="")
    ap.add_argument("--cc", nargs="*", default=[])
    ap.add_argument("--stamp", default=time.strftime("%Y%m%dT%H%M%S", time.gmtime()))
    a = ap.parse_args()
    {"targets": cmd_targets, "names": cmd_names, "merge-names": cmd_merge_names, "match": cmd_match}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Public registers of Canada's delegated authorities -> relationship leads (cloud; no AI, no search engine).

A business that deals in motor vehicles in Ontario must be registered with the Ontario Motor Vehicle Industry Council; it pays the Council
a registration fee and a fee on every vehicle it sells. The Council's own public register names each registrant: legal name, business
name, registration number, class, the date it was first registered and the date its registration expires, its address, telephone and —
for about three in ten — its website. A registrant on the register today is therefore a current, dated, paid relationship between a named
business and a Canada-located body, published by the body that is paid. The same holds for the other delegated authorities
(coord/source_registry.csv, keys ca_*: builders, electrical contractors, travel agencies, retirement homes, funeral homes …): each gets an
entry in AUTH and three small functions (list, profile, lead facts); the rest of this file is shared.

What a row needs beyond the register is the registrant's role mailbox. It is found on the registrant's OWN site by the ordinary mailbox
crawl (tools/lead_crawl.py reads lead_shards/). The site is the one the register names, read once and kept ONLY when its home page shows
the registrant's telephone number or postal code as the register has them. The register's e-mail is never read (the page hides it behind
an obfuscation we leave alone) and never delivered. Sole proprietors are left out: organisations only.

  pull --only omvic                 the register's list -> out/reg_<auth>_list.jsonl (one line per registrant, as the register returns it)
  profiles --only omvic --minutes M each registrant's own page not read yet (or read more than --redo-days ago) -> out/reg_<auth>_profiles.jsonl
  sites --minutes M                 registrants whose profile names a website not checked yet -> out/reg_sites.jsonl
  merge DIR --stamp S               -> data/incoming/claude/registers/ (append-only shards: profiles, site checks) and
                                       lead_shards/leads_reg_<S>.gz + details_reg_<S>.gz
Politeness: one queue per authority, at most 1.6 requests a second; robots.txt respected; identified user agent.
"""
import argparse, collections, csv, glob, gzip, hashlib, html, json, os, re, sys, threading, time, urllib.parse

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402

INC = os.path.join(ROOT, "data/incoming/claude")
DIR = os.path.join(INC, "registers")
SHARDS = os.path.join(INC, "lead_shards")
TODAY = time.strftime("%Y-%m-%d")
MONTHS = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}

# Each authority: its own address and its own fee sentence, as its own pages print them (pages opened on the date given).
AUTH = {
    "omvic": dict(
        name="Ontario Motor Vehicle Industry Council (OMVIC)", short="OMVIC", site="https://www.omvic.ca/",
        address="65 Overlea Blvd. Suite 300 Toronto, ON M4H 1P1", address_url="https://www.omvic.ca/contact", read="2026-11-11",
        fee_quote="As part of the transaction fee program, dealers must submit a $22.00 fee per vehicle for sales, leases, fleets, or as-is transactions, "
                  "which is to be submitted with the registration renewal and fee.",
        fee_url="https://www.omvic.ca/selling/fees/transaction-fees/",
        register="https://www.omvic.ca/dealer-search/", what="registered motor vehicle dealer",
        register_label="the public register of registered motor vehicle dealers published by",
        search="https://www.omvic.ca/wp-admin/admin-ajax.php?action=searchDealerListAjax&dealershipName=%s&dealershipCity=&dealershipRegNumber=&activeRegistrationsOnly=true&disciplinaryActionOnly=false",
        profile="https://www.omvic.ca/dealer-search/dealership-profile/?entry-id=%s"),
}
# sites that are not a registrant's own: marketplaces, social pages, manufacturers' national sites named by their dealers
NOT_OWN = re.compile(r"(^|\.)(facebook|fb|instagram|twitter|x|linkedin|youtube|tiktok|kijiji|autotrader|carpages|cargurus|carfax|google|goo|yelp|yellowpages|canada411|"
                     r"craigslist|ebay|amazon|wixsite|weebly|wordpress|blogspot|godaddysites|square|linktr|bit|business)\.[a-z.]{2,7}$", re.I)
_gap = {"t": 0.0}
_gap_lock = threading.Lock()


def polite_get(url, limit=30_000_000, every=0.62):
    """one queue towards an authority's site, whatever the number of threads: 1.6 requests a second at most"""
    if not C.allowed(url):
        return -1, "", b"", url
    with _gap_lock:
        w = _gap["t"] + every - time.time()
        if w > 0:
            time.sleep(w)
        _gap["t"] = time.time()
    return C.fetch(url, limit)


def iso_date(s):
    """'Nov 12, 2009' -> '2009-11-12' ('' when it is not a date)"""
    m = re.match(r"\s*([A-Za-z]{3})[a-z]*\.?\s+(\d{1,2}),\s*(\d{4})", s or "")
    if not m or m.group(1).lower() not in MONTHS:
        return ""
    return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(1).lower()], int(m.group(2)))


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?s)<[^>]+>", " ", s or ""))).strip()


# ------------------------------------------------------------------------------------------------------------------ OMVIC
def omvic_list():
    """every registered dealer. The search returns the names that contain the letters asked, in one answer — 5,000 at most (measured
    2026-11-11: "a", "e", "i", "o" give exactly 5,000), and now and then nothing at all (its own page asks again when that happens).
    First every letter and digit on its own. A name that only the limited answers could hold is made of the limited letters alone, so each
    limited letter is asked again followed by each limited letter (or a space, a dot, an ampersand, an apostrophe, a hyphen); a pair still
    at the limit, with a third character. An empty answer to a single character is asked three times."""
    A, out, n, cap = AUTH["omvic"], {}, collections.Counter(), 5000

    def ask(q):
        ds = []
        for attempt in range(3):
            st, ct, data, final = polite_get(A["search"] % urllib.parse.quote(q))
            try:
                ds = (json.loads(data.decode("utf-8", "replace")).get("data") or {}).get("dealers") or []
            except Exception:
                ds = []
            if ds or len(q) > 1:
                break
            time.sleep(2)
        n["questions"] += 1
        for d in ds:
            if d.get("id") and (d.get("status") or "").lower() == "registered":
                out[d["id"]] = {"auth": "omvic", "id": d["id"], "legal_name": clean(d.get("legal_name")), "business_name": clean(d.get("business_name")),
                                "reg_number": clean(d.get("reg_number")), "city": clean(d.get("city")), "status": clean(d.get("status")), "listed": TODAY}
        return len(ds) >= cap

    limited = [q for q in "abcdefghijklmnopqrstuvwxyz0123456789" if ask(q)]
    n["single characters at the limit (%s)" % "".join(limited)] = len(limited)
    tail = limited + [" ", ".", "&", "'", "-"]
    pairs = [q + c for q in limited for c in tail if ask(q + c)]
    n["pairs at the limit"] = len(pairs)
    for q in pairs:
        for c in tail:
            if not (q.endswith(" ") and c == " ") and ask(q + c):
                n["three characters still at the limit"] += 1
    print("omvic: %d registered dealers in the register's answers; %s" % (len(out), dict(n)), flush=True)
    return out


def omvic_profile(rid):
    A = AUTH["omvic"]
    url = A["profile"] % rid
    st, ct, data, final = polite_get(url, 3_000_000)
    if st != 200 or not data:
        return {"auth": "omvic", "id": rid, "status_http": st, "date": TODAY, "url": url}
    raw = data.decode("utf-8", "replace")
    # the registrant's own two cards (profile, registration details): label / value pairs, as <dt>/<dd> or as two <span>s. What follows them —
    # its salespeople, its branches (each with a status and a city of its own), the page footer with the Council's address — is not read.
    own = re.split(r"dealer-salespeople-table|Associated Branches", raw)[0]
    f = {}
    for m in re.finditer(r"(?is)<(?:dt|span)[^>]*class=\"info-label[^\"]*\"[^>]*>(.*?)</(?:dt|span)>\s*<(?:dd|span)[^>]*class=\"info-value[^\"]*\"[^>]*>(.*?)</(?:dd|span)>", own):
        k = clean(m.group(1)).rstrip(":").lower()
        if k and k != "email" and k not in f:  # the register's e-mail is never read
            f[k] = clean(m.group(2))
    web = f.get("website") or ""
    return {"auth": "omvic", "id": rid, "status_http": 200, "date": TODAY, "url": url, "legal_name": f.get("legal name") or "", "legal_type": f.get("legal type") or "",
            "phone": re.sub(r"\D", "", f.get("business phone") or "")[:10], "website": "" if web.upper() in ("", "N/A", "NA", "NONE") else web,
            "address": "" if (f.get("address") or "").upper() in ("", "N/A") else f.get("address"), "class": f.get("dealer class") or "", "sub_class": f.get("dealer sub-class") or "",
            "reg_status": (f.get("registration status") or "").split(" Currently")[0][:40], "location_type": f.get("location type") or "",
            "first_registered": iso_date(f.get("original registration date")), "expires": iso_date(f.get("registration expiry date"))}


LISTS = {"omvic": omvic_list}
PROFILES = {"omvic": omvic_profile}


# ------------------------------------------------------------------------------------------------------------------ state
def shard_lines(prefix):
    for p in sorted(glob.glob(os.path.join(DIR, prefix + "_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
            for l in fh:
                try:
                    yield json.loads(l)
                except ValueError:
                    continue


def profiles_on_file(auth):
    """{registrant id: its latest profile record}"""
    out = {}
    for o in shard_lines(auth + "_profiles"):
        if o.get("id") and (o["id"] not in out or (o.get("date") or "") >= (out[o["id"]].get("date") or "")):
            out[o["id"]] = o
    return out


def sites_on_file():
    out = {}
    for o in shard_lines("sites"):
        if o.get("key"):
            out[o["key"]] = o
    return out


def site_host(w):
    w = (w or "").strip().lower()
    if not w or " " in w or "@" in w:
        return ""
    h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").strip(".")
    h = h[4:] if h.startswith("www.") else h
    return h if re.fullmatch(r"[a-z0-9.\-]+\.[a-z]{2,}", h) and not NOT_OWN.search(h) else ""


def postal_of(addr):
    m = re.search(r"\b([A-Z]\d[A-Z])\s?(\d[A-Z]\d)\b", (addr or "").upper())
    return (m.group(1), m.group(2)) if m else None


def tie(rec, text, raw=""):
    """how the page shows that it is this registrant's: its telephone number or its postal code as the register has them -> (by, quote)"""
    d = rec.get("phone") or ""
    if len(d) == 10:
        m = re.search(r"(?<!\d)\(?%s\)?[\s.\-–]{0,3}%s[\s.\-–]{0,3}%s(?!\d)" % (d[:3], d[3:6], d[6:]), text)
        if m:
            return "its telephone number", re.sub(r"\s+", " ", text[max(0, m.start() - 110):m.end() + 60]).strip()
        m = re.search(r"href\s*=\s*[\"']tel:\s*(?:\+?1)?[\s.\-()]{0,2}%s[\s.\-()]{0,3}%s[\s.\-]{0,2}%s[\"']" % (d[:3], d[3:6], d[6:]), raw)
        if m:
            return "its telephone number (the page's call link)", re.sub(r"\s+", " ", m.group(0))[:120]
    pc = postal_of(rec.get("address"))
    if pc:
        m = re.search(r"\b%s\s?%s\b" % pc, text, re.I)
        if m:
            return "its postal code", re.sub(r"\s+", " ", text[max(0, m.start() - 130):m.end() + 40]).strip()
    return "", ""


# ------------------------------------------------------------------------------------------------------------------ commands
def cmd_pull(a):
    os.makedirs("out", exist_ok=True)
    for auth in a.only.split(","):
        recs = LISTS[auth]()
        with open("out/reg_%s_list.jsonl" % auth, "w", encoding="utf-8") as f:
            for r in recs.values():
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


def cmd_profiles(a):
    import run_box
    os.makedirs("out", exist_ok=True)
    for auth in a.only.split(","):
        lst = [json.loads(l) for l in open("out/reg_%s_list.jsonl" % auth, encoding="utf-8")]
        have = profiles_on_file(auth)
        old = time.strftime("%Y-%m-%d", time.gmtime(time.time() - a.redo_days * 86400))
        todo = [r for r in lst if r["id"] not in have or (have[r["id"]].get("date") or "") < old or have[r["id"]].get("status_http") != 200]
        todo.sort(key=lambda r: (r["id"] in have, hashlib.md5(r["id"].encode()).hexdigest()))
        if a.limit:
            todo = todo[:a.limit]
        print("%s: %d registrants in the list, %d profiles on file, %d to read" % (auth, len(lst), len(have), len(todo)), flush=True)
        lock, st = threading.Lock(), collections.Counter()
        fo = open("out/reg_%s_profiles.jsonl" % auth, "a", encoding="utf-8")

        def one(r):
            try:
                p = PROFILES[auth](r["id"])
            except Exception as e:
                p = {"auth": auth, "id": r["id"], "status_http": 0, "date": TODAY, "error": str(e)[:80]}
            p.update(reg_number=r.get("reg_number") or "", business_name=r.get("business_name") or "", city=r.get("city") or "", legal_name=p.get("legal_name") or r.get("legal_name") or "",
                     reg_status=p.get("reg_status") or r.get("status") or "")
            with lock:
                st["read" if p.get("status_http") == 200 else "not read (HTTP %s)" % p.get("status_http")] += 1
                st["names a website"] += bool(p.get("website"))
                fo.write(json.dumps(p, ensure_ascii=False) + "\n"); fo.flush()

        whole = run_box.Box(a.minutes).run(one, todo, 3, grace=30)
        fo.close()
        print("%s profiles: %s%s" % (auth, dict(st), "" if whole else " — stopped by the time box, the rest next run"), flush=True)


def cmd_sites(a):
    """the site a profile names, read once: kept when its home page shows the registrant's telephone number or postal code"""
    import run_box
    os.makedirs("out", exist_ok=True)
    done = sites_on_file()
    recs = []
    for auth in AUTH:
        prof = profiles_on_file(auth)
        for p in glob.glob("out/reg_%s_profiles.jsonl" % auth):
            for l in open(p, encoding="utf-8"):
                try:
                    o = json.loads(l); prof[o["id"]] = o
                except (ValueError, KeyError):
                    pass
        recs += [p for p in prof.values() if p.get("status_http") == 200]
    todo, seen = [], set()
    for p in recs:
        h = site_host(p.get("website"))
        key = "%s:%s" % (p["auth"], p["id"])
        if h and key not in done and key not in seen and re.search(r"corporation|partnership|limited|inc", p.get("legal_type") or "", re.I):
            seen.add(key); todo.append((key, h, p))
    if a.limit:
        todo = todo[:a.limit]
    print("sites: %d registrants name a site of their own that was not checked yet (%d checked before)" % (len(todo), len(done)), flush=True)
    lock, st = threading.Lock(), collections.Counter()
    fo = open("out/reg_sites.jsonl", "a", encoding="utf-8")

    def one(t):
        key, h, p = t
        o = {"key": key, "host": h, "date": TODAY, "by": "", "quote": "", "final": "", "status": ""}
        try:
            u = "https://%s/" % h
            if not C.allowed(u):
                o["status"] = "robots"
            else:
                stc, ct, data, final = C.fetch(u, 3_000_000)
                if stc == 0 and not h.startswith("www."):
                    stc, ct, data, final = C.fetch("https://www.%s/" % h, 3_000_000)
                o["status"] = "http_%s" % stc
                if stc == 200 and data and "html" in (ct or "").lower():
                    fh = (urllib.parse.urlparse(final).hostname or "").lower()
                    fh = fh[4:] if fh.startswith("www.") else fh
                    o["final"] = final
                    if NOT_OWN.search(fh):
                        o["status"] = "leads to a site that is not its own"
                    else:
                        raw = data.decode("utf-8", "replace")
                        text = C.visible(raw)
                        o["by"], o["quote"] = tie(p, text, raw)
                        o["quote"] = o["quote"][:300]
                        o["status"] = "tied" if o["by"] else "the home page shows neither the telephone number nor the postal code of the register"
        except Exception as e:
            o["status"] = "error %s" % str(e)[:60]
        with lock:
            st[o["status"] if not o["status"].startswith("http_") else o["status"]] += 1
            fo.write(json.dumps(o, ensure_ascii=False) + "\n"); fo.flush()

    whole = run_box.Box(a.minutes).run(one, todo, a.workers, grace=30)
    fo.close()
    print("sites: %s%s" % (dict(st.most_common(8)), "" if whole else " — stopped by the time box"), flush=True)


def lead_of(p, s):
    A = AUTH[p["auth"]]
    key = "lead:" + hashlib.sha1(("%s|%s" % (p["auth"], p["id"])).encode()).hexdigest()[:16]
    trade = p.get("business_name") or ""
    fh = (urllib.parse.urlparse(s.get("final") or "").hostname or s["host"]).lower()
    row = {"buyer_key": key, "buyer_name": trade or p["legal_name"], "website": "https://%s/" % fh, "canadian_vendor_rows": 1, "example_vendor": A["name"],
           "canada_field_value": "membership / statutory fee relationship: registrant of the Canadian body (%s)=%s (as printed on %s, read %s); %s: “%s” (%s)"
                                 % (A["name"], A["address"], A["address_url"], A["read"], A["short"], A["fee_quote"], A["fee_url"]),
           "evidence_dataset": p["url"], "latest_record_date": p.get("date") or TODAY}
    ph = p.get("phone") or ""
    det = {"key": key, "platform": "authority_register", "record_url": p["url"], "vendor": A["name"], "record_date": p.get("date") or TODAY,
           "start": p.get("first_registered") or "", "end": p.get("expires") or "", "reference": p.get("reg_number") or "",
           "title": "%s registration no. %s (%s%s) — %s" % (A["short"], p.get("reg_number") or "?", p.get("class") or A["what"], ("; " + p["sub_class"]) if p.get("sub_class") else "",
                                                           p.get("reg_status") or "Registered"),
           "vendor_address": "%s (as printed on %s)" % (A["address"], A["address_url"]), "vendor_site": A["site"],
           "member_address_quote": p.get("address") or "", "register_label": A["register_label"], "buyer_phone_as_printed": ph,
           "buyer_register": {"legal_name": p["legal_name"], "trade_names": [trade] if trade and trade.lower() != p["legal_name"].lower() else [], "registry_id": "",
                              "legal_form": p.get("legal_type") or "", "phone": ("%s-%s-%s" % (ph[:3], ph[3:6], ph[6:])) if len(ph) == 10 else "",
                              "label": "%s's public register, the registrant's own entry %s, read %s" % (A["short"], p["url"], p.get("date") or TODAY)},
           "registration_first": p.get("first_registered") or "", "registration_expires": p.get("expires") or "", "registered_with": A["name"], "registration_class": p.get("class") or "",
           "fee_basis": "%s (%s)" % (A["fee_quote"], A["fee_url"]), "site_named_by": "the register (field Website: %s)" % (p.get("website") or ""),
           "site_tied_to_holder_by": s.get("by") or "", "site_page": s.get("final") or "", "site_quote": s.get("quote") or ""}
    return row, det


def cmd_merge(a):
    os.makedirs(DIR, exist_ok=True); os.makedirs(SHARDS, exist_ok=True)
    stamp = a.stamp or time.strftime("%Y%m%dT%H%M%S", time.gmtime())
    msg = []
    for auth in AUTH:
        new = []
        for p in sorted(glob.glob(os.path.join(a.dir, "reg_%s_profiles*.jsonl" % auth))):
            for l in open(p, encoding="utf-8"):
                try:
                    new.append(json.loads(l))
                except ValueError:
                    pass
        if new:
            with gzip.open(os.path.join(DIR, "%s_profiles_%s.gz" % (auth, stamp)), "wt", encoding="utf-8") as f:
                for o in new:
                    f.write(json.dumps(o, ensure_ascii=False) + "\n")
        prof = profiles_on_file(auth)
        ok = [p for p in prof.values() if p.get("status_http") == 200]
        msg.append("%s: %d profiles on file (+%d this run), %d name a website" % (auth, len(ok), len(new), sum(1 for p in ok if p.get("website"))))
    news = []
    for p in sorted(glob.glob(os.path.join(a.dir, "reg_sites*.jsonl"))):
        for l in open(p, encoding="utf-8"):
            try:
                news.append(json.loads(l))
            except ValueError:
                pass
    if news:
        with gzip.open(os.path.join(DIR, "sites_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for o in news:
                f.write(json.dumps(o, ensure_ascii=False) + "\n")
    sites = sites_on_file()
    have, old_det = set(), {}
    for p in glob.glob(os.path.join(SHARDS, "leads_reg_*.gz")):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            have |= {r["buyer_key"] for r in csv.DictReader(fh)}
    for p in sorted(glob.glob(os.path.join(SHARDS, "details_reg_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    d = json.loads(l); old_det[d["key"]] = d
                except (ValueError, KeyError):
                    pass
    rows, dets, by, n_fresh, hosts = [], [], collections.Counter(), 0, collections.Counter()
    tied = {k: s for k, s in sites.items() if s.get("by")}
    for s in tied.values():
        hosts[s["host"]] += 1
    for auth in AUTH:
        prof = profiles_on_file(auth)
        for rid, p in sorted(prof.items()):
            s = tied.get("%s:%s" % (auth, rid))
            if not s or p.get("status_http") != 200 or not p.get("legal_name"):
                continue
            if hosts[s["host"]] > 3:
                by["site shared by more than three registrants (a group's site): left out"] += 1
                continue
            row, det = lead_of(p, s)
            if row["buyer_key"] in have:
                od = old_det.get(row["buyer_key"])
                if od is not None and any((od.get(k) or "") != (det.get(k) or "") for k in ("start", "end", "title", "reference", "member_address_quote")):
                    dets.append(det); n_fresh += 1  # the register changed (a renewal moved the expiry date): a fresh details record, the lead row stays
                continue
            have.add(row["buyer_key"]); rows.append(row); dets.append(det); by["new lead, site tied by " + s["by"]] += 1
    if rows:
        with gzip.open(os.path.join(SHARDS, "leads_reg_%s.gz" % stamp), "wt", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    if dets:
        with gzip.open(os.path.join(SHARDS, "details_reg_%s.gz" % stamp), "wt", encoding="utf-8") as f:
            for d in dets:
                f.write(json.dumps(d, ensure_ascii=False) + "\n")
    st = collections.Counter(s.get("status") or "?" for s in sites.values())
    print("authority registers: %s; sites checked %d (%s); leads on file %d (+%d this run: %s); details refreshed %d"
          % ("; ".join(msg), len(sites), ", ".join("%s %d" % kv for kv in st.most_common(5)), len(have), len(rows), dict(by), n_fresh))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pull"); p.add_argument("--only", default="omvic")
    p = sub.add_parser("profiles"); p.add_argument("--only", default="omvic"); p.add_argument("--minutes", type=float, default=150); p.add_argument("--limit", type=int, default=0)
    p.add_argument("--redo-days", type=int, default=45, help="a profile older than this is read again (renewals move the expiry date)")
    p = sub.add_parser("sites"); p.add_argument("--minutes", type=float, default=40); p.add_argument("--workers", type=int, default=30); p.add_argument("--limit", type=int, default=0)
    p = sub.add_parser("merge"); p.add_argument("dir"); p.add_argument("--stamp", default="")
    a = ap.parse_args()
    {"pull": cmd_pull, "profiles": cmd_profiles, "sites": cmd_sites, "merge": cmd_merge}[a.cmd](a)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Canada's Business Registries (ISED's multi-jurisdictional registry search, https://ised-isde.canada.ca/cbr-rec/en/search) → the
registry facts of each vendor (and corporation-type buyer): Business Number, legal name as registered, registry id, jurisdiction,
entity type, status, incorporation date, registered-office city / province, alternate names. The service is a public federal search
with no login or CAPTCHA; its own front end calls GET https://ised-isde.canada.ca/cbr/srch/api/v1/search?q={name}&lang=en. One
request per second, identified user agent, every answer cached.
2026-11-11: the service was rebuilt between 2026-11-09 and 2026-11-11 — /api/v3/search (fq=keyword:{name}) answers 404, the new front end
(config.js: SEARCH_API_URL) calls /api/v1/search?q=. Same documents (Company_Name, BN, Juri_ID, Registry_Source, Reg_office_*, XP_TYPE,
hierarchy). The new front end carries the code of a Cloudflare Turnstile check with an empty site key: no check is shown and the search
answers a plain request. The day a key is set the search will refuse us, the lookup records `blocked` and stops (rule 6).

Match rule (evidence or nothing): the registered name (or an alternate name) must equal the vendor's name after normalisation
(accents, punctuation, legal-form words); when several registries return the same name, the one whose registered-office province
agrees with the vendor's known province wins; otherwise the vendor is `ambiguous` and nothing is filled. Output
<repo>/data/incoming/claude/claude_registry_lookup.csv, one row per organisation looked up, with the API URL and the matched
document as the quote; rank.py fills vendor_bn9 / legal name / registered office / status / incorporation date / legal form.
  python3 tools/registry_lookup.py --ranked ~/cch-tasks/ranked_latest.csv.gz [--kind vendor|buyer|both] [--limit N] [--repo ~/cch-crawler]
"""
import argparse, hashlib, csv, datetime, gzip, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import registry_names as RN  # noqa: E402  (the name a buyer is looked up under)

csv.field_size_limit(1 << 30)
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://ised-isde.canada.ca/cbr/srch/api/v1/search"
UI = "https://ised-isde.canada.ca/cbr-rec/en/search?q="
STATE = os.path.expanduser("~/cch-crawler-state")
RESUME = os.path.join(STATE, "registry_lookup.jsonl")
TODAY = datetime.date.today().isoformat()
COLS = ["kind", "key", "name", "status", "matched_name", "bn9", "juri_id", "registry_source", "mras_id", "entity_type", "status_state", "status_notes", "date_incorporated",
        "reg_office_city", "reg_office_province", "alternate_names", "candidates", "match_basis", "api_url", "ui_url", "retrieved_date", "source_quote"]
LEGAL = {"inc", "incorporated", "incorporee", "incorporée", "ltd", "limited", "ltee", "ltée", "limitee", "limitée", "corp", "corporation", "co", "company", "cie", "compagnie", "llc", "llp", "lp",
         "enr", "enrg", "senc", "sencrl", "sec", "ulc", "plc", "the", "la", "le", "les", "de", "du", "des", "and", "et", "&", "of"}  # single letters stay: "A.J. Stone" is not "J L Stone"
# legal-form class: a partnership (LLP / LP / SENC / SENCRL / s.e.c.) is never the corporation of the same name (Smythe LLP ≠ Smythe Inc.; MNP LLP ≠ MNP Ltd.)
FORM_CLASS = [(re.compile(r"\b(?:llp|l\.l\.p\.|lp|l\.p\.|senc|sencrl|s\.e\.n\.c\.|s\.e\.c\.|sec|partnership|soci[ée]t[ée] en nom collectif|soci[ée]t[ée] en commandite)\b", re.I), "partnership"),
              (re.compile(r"\b(?:inc|incorporated|incorpor[ée]e|ltd|limited|lt[ée]e|limit[ée]e|corp|corporation|ulc|llc|plc|s\.a\.|gmbh|ag|company|co|cie|compagnie)\b\.?", re.I), "corporation"),
              (re.compile(r"\b(?:enr|enrg|enregistr[ée]e|sole proprietor)\b", re.I), "sole proprietorship")]


GOV_RX = re.compile(r"\b(ville|city|town|village|municipalit|township|canton|county|comt[ée]|regional district|district municipality|MRC|government|gouvernement|ministry|minist[èe]re|department|d[ée]partement|agency|agence|school|[ée]cole|board|conseil|commission scolaire|centre de services scolaire|universit|college|coll[èe]ge|c[ée]gep|first nation|nation|band|tribal|province|state of|parliament|assembly|court|tribunal|library|biblioth|police|fire|ambulance|canada|qu[ée]bec|ontario|alberta|manitoba|saskatchewan|columbia|brunswick|scotia|newfoundland|yukon|nunavut|territories)\b", re.I)


def form_class(name):
    for rx, cls in FORM_CLASS:
        if rx.search(name or ""):
            return cls
    return ""
PROV = {"alberta": "AB", "british columbia": "BC", "colombie-britannique": "BC", "manitoba": "MB", "new brunswick": "NB", "nouveau-brunswick": "NB", "newfoundland and labrador": "NL", "newfoundland": "NL",
        "terre-neuve-et-labrador": "NL", "nova scotia": "NS", "nouvelle-ecosse": "NS", "nouvelle-écosse": "NS", "northwest territories": "NT", "nunavut": "NU", "ontario": "ON", "prince edward island": "PE",
        "ile-du-prince-edouard": "PE", "quebec": "QC", "québec": "QC", "saskatchewan": "SK", "yukon": "YT", "federal": "FED", "canada": "FED", "cc": "FED"}
PROV_RX = re.compile(r"\b(AB|BC|MB|NB|NL|NS|NT|NU|ON|PE|QC|SK|YT|Alberta|British Columbia|Colombie-Britannique|Manitoba|New Brunswick|Nouveau-Brunswick|Newfoundland(?: and Labrador)?|Nova Scotia|Nouvelle-[EÉ]cosse|Ontario|Prince Edward Island|Qu[eé]bec|Saskatchewan|Yukon)\b")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().replace("&", " and ")
    toks = [t for t in re.findall(r"[a-z0-9]+", s) if t not in LEGAL]
    return " ".join(toks)


def pcode(s):
    s = (s or "").strip()
    if len(s) == 2:
        return s.upper()
    k = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return PROV.get(k, PROV.get(s.lower(), ""))


def prov_of(*texts):
    for t in texts:
        for m in PROV_RX.finditer(t or ""):
            return pcode(m.group(1))
    return ""


def search(name):
    url = "%s?q=%s&lang=en" % (API, urllib.parse.quote(name, safe=""))
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace")), url
    except urllib.error.HTTPError as e:
        return e.code, None, url
    except Exception:
        return 0, None, url


def pick(name, docs, prov_hint):
    """the registered document that IS this organisation: equal normalised name (or alternate name); province decides ties"""
    wanted = {norm(name)}
    m = re.search(r"\(([^()]{3,80})\)", name or "")  # "Alstom Canada (Alstom Transport Canada Inc.)": the parenthesis names the legal entity
    if m and re.search(r"\b(inc|ltd|limited|lt[ée]e|corp|corporation|llc|llp|lp|senc|sencrl|ulc)\b\.?", m.group(1), re.I):
        wanted.add(norm(m.group(1)))
    wanted.add(norm(re.sub(r"\([^()]*\)", " ", name or "")))
    wanted = {w for w in wanted if len(w) >= 3}
    if not wanted:
        return None, "name too short", []
    exact, strong = [], []
    for d in docs or []:
        names = [d.get("Company_Name") or ""] + [a for a in (d.get("Alternate_Name") or []) if a]
        if any(norm(x) in wanted for x in names):
            exact.append(d)
        elif any(norm(x).replace(" ", "") in {w.replace(" ", "") for w in wanted} for x in names):
            strong.append(d)
    cands = exact or strong
    basis = "registered name equals the vendor's name" if exact else ("registered name equals the vendor's name (spacing differs)" if strong else "")
    if not cands:
        return None, "no registered name equals this name", docs[:3] if docs else []
    fc = form_class(name)
    if fc:  # both names carry a legal form: the classes must agree (Smythe LLP is not Smythe Inc.)
        kept = [d for d in cands if not form_class(d.get("Company_Name") or "") or form_class(d.get("Company_Name") or "") == fc]
        if not kept:
            return None, "the registered entity of this name has a different legal form (%s vs %s)" % (fc, "/".join(sorted({form_class(d.get("Company_Name") or "") for d in cands}))), cands[:3]
        cands = kept
        basis += "; same legal form (%s)" % fc
    if len(cands) > 1:
        home = [d for d in cands if (d.get("XP_TYPE") or "").upper() == "HJ"]  # the home-jurisdiction record; the others are extra-provincial registrations of the same body
        if len(home) == 1:
            return home[0], basis + "; home-jurisdiction registration (the other matches are extra-provincial registrations)", cands
        if home:
            cands = home
        same_prov = [d for d in cands if prov_hint and pcode(d.get("Reg_office_province")) == prov_hint]
        if len(same_prov) == 1:
            return same_prov[0], basis + "; registered-office province agrees with the vendor's address", cands
        bns = {d.get("BN") for d in cands if d.get("BN")}
        if len(bns) == 1 and bns != {None}:
            return cands[0], basis + "; the same Business Number in every matching registry", cands
        return None, "ambiguous: %d registered entities carry this name in different jurisdictions" % len(cands), cands
    d = cands[0]
    if prov_hint and pcode(d.get("Reg_office_province")) and pcode(d.get("Reg_office_province")) != prov_hint and (d.get("XP_TYPE") or "").upper() == "HJ":
        return None, "the only registered entity of this name is in %s; the vendor's address says %s" % (d.get("Reg_office_province"), prov_hint), cands
    if not prov_hint:
        basis += "; no province known for the vendor, so not checked"
    elif pcode(d.get("Reg_office_province")) == prov_hint:
        basis += "; registered-office province agrees with the vendor's address"
    return d, basis, cands


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.expanduser("~/cch-tasks/ranked_latest.csv.gz"))
    a.add_argument("--kind", default="vendor")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--shard", default="", help="K/N: only names whose hash falls in shard K of N (a second runner takes the other half; together never more than 2 requests / second to the registry)")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--rate", type=float, default=1.0, help="requests per second (polite ceiling for a government service)")
    a = a.parse_args()
    os.makedirs(STATE, exist_ok=True)
    done = {}
    if os.path.exists(RESUME):
        for l in open(RESUME, encoding="utf-8"):
            try:
                d = json.loads(l); done[(d["kind"], d["key"])] = d
            except Exception:
                pass
    op = gzip.open if a.ranked.endswith(".gz") else open
    tasks, seen, vend = [], set(), {}
    PR = {"GOLD": 0, "GOLD-T": 2, "GOLD-M": 2}
    with op(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if not r.get("email"):
                continue
            t, g = r.get("tier") or "", r.get("grade") or ""
            pr = PR.get(r.get("rank_group") or "", 1 if t in ("A", "B") and g in ("2", "3") else 3 if t in ("A", "B", "L") else 4 if t in ("C", "D", "E", "T", "M") else 6 if t == "I" else 5)
            if a.kind in ("vendor", "both"):
                v = (r.get("vendor") or "").strip()
                if v and not v.startswith("inferred") and not (r.get("vendor_bn9") or "").strip():
                    # 2026-11-11 (owner: "every single aspect within an invoice matters … the vendor"): one vendor's business number fills every row
                    # of that vendor (Web Hosting Canada: 10,007 rows, no number), so vendors are asked by the number of rows they carry, and under
                    # the legal name their own site states ("WHC Online Solutions Inc") when it states one — the registry does not know trade names.
                    o = vend.get(v.lower())
                    if o is None:
                        o = vend[v.lower()] = [pr, 0, v, "", prov_of(r.get("vendor_address"), r.get("vendor_registered_address"), r.get("vendor_country_basis"))]
                    o[0], o[1] = min(o[0], pr), o[1] + 1
                    if not o[3]:
                        ln = re.split(r"\s+\((?:stated on|as printed|printed with|schema\.org|the vendor's name|carried from|as it names|official name|as the )", (r.get("vendor_legal_name") or "").strip())[0].strip(" -")
                        if ln and ln != "not_published" and "(" not in ln and 3 <= len(ln) <= 90 and re.search(r"\b(?:inc|corp|corporation|ltd|limited|lt[ée]e|co|company|cie|llp|lp|ulc|s\.e\.n\.c|senc)\b\.?", ln, re.I):
                            o[3] = ln
            if a.kind in ("buyer", "both"):
                b, stated = RN.lookup_name(r)  # the legal person the buyer's own site states, when it does; else the name it trades under
                k = (r.get("keys") or "").split("|")[0] or (r.get("buyer") or "").strip()
                corp_like = re.search(r"\b(inc|corp|corporation|ltd|limited|lt[ée]e|hospital|h[ôo]pital|foundation|fondation|association|society|soci[ée]t[ée]|centre|center|institute|institut|coop|co-op|credit union|caisse|college|coll[èe]ge|c[ée]gep|health|sant[ée]|housing|transit|authority|commission)\b", b, re.I)
                # owner 2026-11-08 11:46 EST (every row needs its bill-to legal name): organisations whose name carries no legal form — a company or association
                # printed as "Acme Plumbing" on a vendor's client page — are looked up too, unless the name says it is a government body (not in the registries)
                org_like = (r.get("tier") or "") == "I" and not GOV_RX.search(b) and re.search(r"company|organisation \(type not stated|non-profit|association|religious|utility|hospital", r.get("buyer_type") or "", re.I)
                if b and ("buyer:" + k) not in seen and (corp_like or org_like or stated):
                    seen.add("buyer:" + k)
                    tasks.append((pr + (0.5 if corp_like else 0.8), "buyer", k, b, prov_of(r.get("jurisdiction") or "", r.get("buyer_address"))))
                elif b and ("buyer:" + k) not in seen and not GOV_RX.search(b):
                    # 2026-11-11: a PLAIN name (the name a business trades under, no legal form in it: 174,584 delivered rows) is looked up too, last, and
                    # only when the buyer's own province is known. Measured on the lookups on file against the legal name the buyer's own site spells:
                    # of 105 plain-name matches, 92 are the same name and about 8 more the same company written another way; the rest are a
                    # namesake or a parent. So a plain name is accepted only when the single registered entity of that name has its registered office
                    # in the buyer's own province (see below), and the ranker lets the site's own statement stand when the two disagree.
                    pv = prov_of(r.get("jurisdiction") or "", r.get("buyer_address"))
                    words = [w for w in re.findall(r"[A-Za-zÀ-ÿ0-9]{2,}", b)]
                    if pv and (len(words) >= 2 or (words and len(words[0]) >= 7)) and len(b) <= 70 and not re.search(r"\.(?:ca|com|org|net)\b", b, re.I):
                        seen.add("buyer:" + k)
                        tasks.append((pr + 10.9, "buyer", k, b, pv))
    for pr, n_rows, v, legal, pv in vend.values():
        tasks.append(((pr if n_rows < 20 else 0.5) - min(0.49, n_rows / 100000.0), "vendor", v, legal or v, pv))
    tasks.sort(key=lambda t: t[0])
    # a buyer's record is kept under the row's key, and a row's name changes (a lead first named after a line of its page, later after its own
    # home page): 2026-11-10, "VILLE DE QUÉBEC" was still the registered name of a row named "LES YMCA DU QUÉBEC" by then. A key is done only
    # for the name it was looked up under; under a new name it is looked up again and the new answer replaces the old one.
    _nm = lambda t: re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()).strip()
    n_renamed = sum(1 for t in tasks if (t[1], t[2]) in done and _nm(done[(t[1], t[2])].get("name")) != _nm(t[3]))
    # an answer that was no answer (the service did not reply, or replied with an error) is asked again: 2026-11-11, a run started before the
    # service's new address was known recorded "error_http_404" for every name it tried
    _failed = lambda d: (d.get("status") or "").startswith(("error_http", "blocked"))
    n_failed = sum(1 for t in tasks if (t[1], t[2]) in done and _failed(done[(t[1], t[2])]))
    tasks = [t for t in tasks if (t[1], t[2]) not in done or _nm(done[(t[1], t[2])].get("name")) != _nm(t[3]) or _failed(done[(t[1], t[2])])]
    print("asked before without an answer (service error), to ask again: %d" % n_failed, flush=True)
    print("looked up before under another name, to look up again: %d" % n_renamed, flush=True)
    if a.shard:
        k_, n_ = int(a.shard.split("/")[0]), int(a.shard.split("/")[1])
        tasks = [t for t in tasks if int(hashlib.md5(t[2].encode()).hexdigest(), 16) % n_ == k_]
    if a.limit:
        tasks = tasks[:a.limit]
    print("to look up: %d (%d done before)" % (len(tasks), len(done)), flush=True)
    out = os.path.join(a.repo, "data/incoming/claude/claude_registry_lookup.csv")
    stats, last = {}, time.time()

    def dump():
        rows = [d for d in done.values()]
        if os.path.exists(out):  # rows another runner (GitHub Actions shard, synced into this clone) wrote meanwhile are kept: union by key, this process's rows win
            try:
                import io as _io
                for r_ in csv.DictReader(_io.StringIO(open(out, encoding="utf-8", errors="replace").read().replace("\0", ""))):
                    if (r_.get("kind"), r_.get("key")) not in done and r_.get("kind") and r_.get("key"):
                        rows.append(r_)
            except Exception as e_:
                print("union with the on-disk file failed:", type(e_).__name__, e_, flush=True)
        tmp = out + ".%d.tmp" % os.getpid()
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore"); w.writeheader(); w.writerows(sorted(rows, key=lambda d: (d["kind"], d["key"])))
        os.replace(tmp, out)
        print(time.strftime("%H:%M"), "wrote", out, len(rows), dict(stats), flush=True)
    errs = 0
    for i, (pr, kind, key, name, prov) in enumerate(tasks):
        t0 = time.time()
        st, data, url = search(name[:170])
        errs = errs + 1 if (st != 200 or data is None) and st not in (401, 403, 429) else 0
        if errs >= 25:  # the service is down or has moved: 25 names in a row without an answer. Nothing more is asked (and nothing recorded for this name)
            print("no answer from the service for 25 names in a row (last: HTTP %s): stopping" % st, flush=True)
            break
        row = {"kind": kind, "key": key, "name": name, "api_url": url, "ui_url": UI + urllib.parse.quote(name[:170], safe=""), "retrieved_date": TODAY, "status": "", "candidates": ""}
        if st in (401, 403, 429):
            row["status"] = "blocked"
        elif st != 200 or data is None:
            row["status"] = "error_http_%s" % st
        else:
            docs = data.get("docs") or []
            d, basis, cands = pick(name, docs, prov)
            if not d and not cands and norm(name) and norm(name) != name.lower():  # "MALLETTE S.E.N.C.R.L.": the keyword search wants the plain words
                time.sleep(1.0 / a.rate)
                st2, data2, url2 = search(norm(name)[:170])
                if st2 == 200 and data2:
                    docs = data2.get("docs") or []
                    d, basis, cands = pick(name, docs, prov)
                    if d:
                        row["api_url"] = url2
            if d and pr >= 10 and "province agrees" not in basis:  # a plain name (priority 10+): only a match in the buyer's own province counts
                d, basis = None, "plain name: the registered entity of this name is not shown to be in the buyer's province (%s)" % basis[:120]
            row["candidates"] = "; ".join("%s [%s %s, %s]" % (c.get("Company_Name"), c.get("Registry_Source"), c.get("Juri_ID"), c.get("Reg_office_province") or "") for c in cands[:5])[:400]
            if d:
                row.update({"status": "found", "matched_name": d.get("Company_Name") or "", "bn9": re.sub(r"\D", "", d.get("BN") or "")[:9], "juri_id": d.get("Juri_ID") or "", "registry_source": d.get("Registry_Source") or "",
                            "mras_id": d.get("MRAS_ID") or "", "entity_type": d.get("Entity_Type") or "", "status_state": d.get("Status_State") or "", "status_notes": d.get("Status_Notes") or "",
                            "date_incorporated": (d.get("Date_Incorporated") or d.get("Date_Registered") or d.get("Display_Date") or "")[:10], "reg_office_city": d.get("Reg_office_city") or "",
                            "reg_office_province": d.get("Reg_office_province") or "", "alternate_names": "; ".join(x for x in (d.get("Alternate_Name") or []) if x)[:200], "match_basis": basis,
                            "source_quote": json.dumps({k: d.get(k) for k in ("Company_Name", "BN", "Juri_ID", "Registry_Source", "Entity_Type", "Status_State", "Date_Incorporated", "Reg_office_city", "Reg_office_province") if d.get(k)}, ensure_ascii=False)[:300]})
            else:
                row["status"] = "ambiguous" if basis.startswith("ambiguous") else "not_found"
                row["match_basis"] = basis
        stats[row["status"]] = stats.get(row["status"], 0) + 1
        done[(kind, key)] = row
        with open(RESUME, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        if time.time() - last > 300:
            last = time.time(); dump()
        if row["status"] == "blocked":
            print("blocked by the service (HTTP %s); stopping as the rules require" % st, flush=True); break
        time.sleep(max(0.0, 1.0 / a.rate - (time.time() - t0)))
    dump()
    print("finished", dict(stats), flush=True)


if __name__ == "__main__":
    main()

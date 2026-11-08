#!/usr/bin/env python3
"""Canada's Business Registries (ISED's multi-jurisdictional registry search, https://ised-isde.canada.ca/cbr-rec/en/search) → the
registry facts of each vendor (and corporation-type buyer): Business Number, legal name as registered, registry id, jurisdiction,
entity type, status, incorporation date, registered-office city / province, alternate names. The service is a public federal search
with no login or CAPTCHA; its own front end calls GET https://ised-isde.canada.ca/cbr/srch/api/v3/search?fq=keyword:{name}&lang=en&
queryaction=fieldquery&sortfield=score&sortorder=desc. One request per second, identified user agent, every answer cached.

Match rule (evidence or nothing): the registered name (or an alternate name) must equal the vendor's name after normalisation
(accents, punctuation, legal-form words); when several registries return the same name, the one whose registered-office province
agrees with the vendor's known province wins; otherwise the vendor is `ambiguous` and nothing is filled. Output
<repo>/data/incoming/claude/claude_registry_lookup.csv, one row per organisation looked up, with the API URL and the matched
document as the quote; rank.py fills vendor_bn9 / legal name / registered office / status / incorporation date / legal form.
  python3 tools/registry_lookup.py --ranked ~/cch-tasks/ranked_latest.csv.gz [--kind vendor|buyer|both] [--limit N] [--repo ~/cch-crawler]
"""
import argparse, csv, datetime, gzip, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

csv.field_size_limit(1 << 30)
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
API = "https://ised-isde.canada.ca/cbr/srch/api/v3/search"
UI = "https://ised-isde.canada.ca/cbr-rec/en/search?q="
STATE = os.path.expanduser("~/cch-crawler-state")
RESUME = os.path.join(STATE, "registry_lookup.jsonl")
TODAY = datetime.date.today().isoformat()
COLS = ["kind", "key", "name", "status", "matched_name", "bn9", "juri_id", "registry_source", "mras_id", "entity_type", "status_state", "status_notes", "date_incorporated",
        "reg_office_city", "reg_office_province", "alternate_names", "candidates", "match_basis", "api_url", "ui_url", "retrieved_date", "source_quote"]
LEGAL = {"inc", "incorporated", "incorporee", "incorporée", "ltd", "limited", "ltee", "ltée", "limitee", "limitée", "corp", "corporation", "co", "company", "cie", "compagnie", "llc", "llp", "lp",
         "enr", "enrg", "senc", "sencrl", "sec", "ulc", "plc", "the", "la", "le", "les", "l", "d", "de", "du", "des", "and", "et", "&", "of", "a"}
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
    q = "keyword:%7B" + urllib.parse.quote(name, safe="") + "%7D"
    url = "%s?fq=%s&lang=en&queryaction=fieldquery&sortfield=score&sortorder=desc" % (API, q)
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
    return cands[0], basis, cands


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ranked", default=os.path.expanduser("~/cch-tasks/ranked_latest.csv.gz"))
    a.add_argument("--kind", default="vendor")
    a.add_argument("--limit", type=int, default=0)
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
    tasks, seen = [], set()
    PR = {"GOLD": 0, "GOLD-T": 2, "GOLD-M": 2}
    with op(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if not r.get("email"):
                continue
            t, g = r.get("tier") or "", r.get("grade") or ""
            pr = PR.get(r.get("rank_group") or "", 1 if t in ("A", "B") and g in ("2", "3") else 3 if t in ("A", "B", "L") else 4 if t in ("C", "D", "E", "T", "M") else 6 if t == "I" else 5)
            if a.kind in ("vendor", "both"):
                v = (r.get("vendor") or "").strip()
                if v and not v.startswith("inferred") and v.lower() not in seen and not (r.get("vendor_bn9") or "").strip():
                    seen.add(v.lower())
                    tasks.append((pr, "vendor", v, v, prov_of(r.get("vendor_address"), r.get("vendor_registered_address"), r.get("vendor_country_basis"))))
            if a.kind in ("buyer", "both"):
                b = (r.get("buyer") or "").strip()
                k = (r.get("keys") or "").split("|")[0] or b
                if b and ("buyer:" + k) not in seen and re.search(r"\b(inc|corp|corporation|ltd|limited|lt[ée]e|hospital|h[ôo]pital|foundation|fondation|association|society|soci[ée]t[ée]|centre|center|institute|institut|coop|co-op|credit union|caisse|college|coll[èe]ge|c[ée]gep|health|sant[ée]|housing|transit|authority|commission)\b", b, re.I):
                    seen.add("buyer:" + k)
                    tasks.append((pr + 0.5, "buyer", k, b, prov_of(r.get("jurisdiction") or "", r.get("buyer_address"))))
    tasks.sort(key=lambda t: t[0])
    tasks = [t for t in tasks if (t[1], t[2]) not in done]
    if a.limit:
        tasks = tasks[:a.limit]
    print("to look up: %d (%d done before)" % (len(tasks), len(done)), flush=True)
    out = os.path.join(a.repo, "data/incoming/claude/claude_registry_lookup.csv")
    stats, last = {}, time.time()

    def dump():
        rows = [d for d in done.values()]
        tmp = out + ".%d.tmp" % os.getpid()
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore"); w.writeheader(); w.writerows(sorted(rows, key=lambda d: (d["kind"], d["key"])))
        os.replace(tmp, out)
        print(time.strftime("%H:%M"), "wrote", out, len(rows), dict(stats), flush=True)
    for i, (pr, kind, key, name, prov) in enumerate(tasks):
        t0 = time.time()
        st, data, url = search(name[:170])
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

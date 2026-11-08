#!/usr/bin/env python3
"""Wikidata, one organisation at a time (owner 2026-11-08: "search 60,000 individual companies if that is what it takes").

For every organisation in the ranked file (buyers first, then the vendors on delivered rows) that still lacks a published legal
name, address, phone or website, ask Wikidata's public search API for the name, fetch the candidate items and keep a match ONLY
when (a) the item's official website (P856) is on the organisation's own domain, or (b) the label equals the name exactly after
normalisation AND the item's country matches AND the item is not a person. Everything copied is a Wikidata claim with the item URL
as evidence and the claim text as quote; nothing is guessed. Polite: ≤ 2 requests/second in total, identified user agent, resumable.
Output: <repo>/data/incoming/claude/claude_wikidata_orgs.csv — rank.py fills blank cells from it with the provenance
"(Wikidata <Q>, <claim>; <date>)".
  python3 tools/wikidata_orgs.py [--repo ~/cch-crawler] [--ranked ranked_buyers.csv.gz] [--limit N] [--only-missing]
"""
import argparse, csv, datetime, gzip, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub; organisation facts) python-urllib"
API = "https://www.wikidata.org/w/api.php"
TODAY = datetime.date.today().isoformat()
COLS = ["key", "side", "name", "domain", "qid", "match_basis", "official_name", "label_en", "label_fr", "instance_of", "legal_form", "country", "inception", "headquarters",
        "street_address", "phone", "email", "website", "employees", "budget_or_revenue", "neq", "wikipedia", "evidence_url", "evidence_quote", "retrieved_date", "status"]
STOP = {"the", "of", "de", "du", "des", "la", "le", "les", "l", "d", "and", "et", "inc", "ltd", "ltee", "corp", "corporation", "limited", "incorporated", "co", "company", "llc", "ulc", "lp", "llp", "plc", "sa", "ag", "gmbh"}
COUNTRY_Q = {"CA": "Q16", "US": "Q30", "UK": "Q145", "GB": "Q145", "AU": "Q408", "NZ": "Q664", "IE": "Q27", "FR": "Q142", "DE": "Q183"}
PROPS = {"P856": "website", "P1448": "official_name", "P31": "instance_of", "P1454": "legal_form", "P17": "country", "P571": "inception", "P159": "headquarters", "P6375": "street_address",
         "P1329": "phone", "P968": "email", "P1128": "employees", "P2769": "budget", "P2139": "revenue"}
_last = [0.0]
NEQ_PID = ""


def pace():
    now = time.time()
    if now - _last[0] < 0.5:
        time.sleep(0.5 - (now - _last[0]))
    _last[0] = time.time()


def get(url):
    pace()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(10 * (attempt + 1)); continue
            return None
        except Exception:
            time.sleep(2)
    return None


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return " ".join(t for t in re.findall(r"[a-z0-9]+", s) if t not in STOP)


def host(u):
    h = (urllib.parse.urlparse(u if "//" in (u or "") else "https://" + (u or "")).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def same_domain(a, b):
    if not a or not b:
        return False
    return a == b or a.endswith("." + b) or b.endswith("." + a)


def claim_values(ent, pid):
    out = []
    for c in (ent.get("claims") or {}).get(pid, []):
        dv = ((c.get("mainsnak") or {}).get("datavalue") or {}).get("value")
        if dv is None:
            continue
        if isinstance(dv, dict):
            if "id" in dv:
                out.append(("item", dv["id"]))
            elif "time" in dv:
                out.append(("time", dv["time"][1:11]))
            elif "amount" in dv:
                out.append(("amount", dv["amount"].lstrip("+") + ((" " + dv["unit"].rsplit("/", 1)[-1]) if dv.get("unit") and dv["unit"] != "1" else "")))
            elif "text" in dv:
                out.append(("text", dv["text"] + (" [%s]" % dv.get("language", "") if dv.get("language") else "")))
        else:
            out.append(("str", str(dv)))
    return out


def labels_for(qids):
    res = {}
    for i in range(0, len(qids), 50):
        chunk = qids[i:i + 50]
        d = get("%s?action=wbgetentities&ids=%s&props=labels&languages=en|fr&format=json" % (API, "|".join(chunk)))
        for q, e in ((d or {}).get("entities") or {}).items():
            lab = (e.get("labels") or {})
            res[q] = (lab.get("en") or lab.get("fr") or {}).get("value", q)
    return res


def lookup(name, domain, country):
    """→ row dict or None"""
    cands = []
    for lang in ("en", "fr"):
        d = get("%s?action=wbsearchentities&search=%s&language=%s&uselang=%s&type=item&limit=7&format=json" % (API, urllib.parse.quote(name[:200]), lang, lang))
        for s in (d or {}).get("search") or []:
            if s["id"] not in [c["id"] for c in cands]:
                cands.append(s)
        if lang == "en" and not re.search(r"[àâçéèêëîïôûùüÿœ]|\b(de|du|des|la|le|les)\b", name, re.I):
            break
    if not cands:
        return None
    want_c = COUNTRY_Q.get(country or "")
    for s in cands[:7]:
        d = get("https://www.wikidata.org/wiki/Special:EntityData/%s.json" % s["id"])
        ent = ((d or {}).get("entities") or {}).get(s["id"])
        if not ent:
            continue
        inst = [q for k, q in claim_values(ent, "P31") if k == "item"]
        if "Q5" in inst:  # a person
            continue
        sites = [v for k, v in claim_values(ent, "P856") if k == "str"]
        site_hit = next((v for v in sites if same_domain(host(v), domain)), "") if domain else ""
        labels = ent.get("labels") or {}
        lab_en, lab_fr = (labels.get("en") or {}).get("value", ""), (labels.get("fr") or {}).get("value", "")
        aliases = [a.get("value", "") for l in ("en", "fr") for a in (ent.get("aliases") or {}).get(l, [])]
        countries = [q for k, q in claim_values(ent, "P17") if k == "item"]
        exact = norm(name) and norm(name) in {norm(x) for x in [lab_en, lab_fr] + aliases if x}
        if site_hit:
            basis = "official website on the organisation's domain (%s)" % site_hit
        elif exact and want_c and want_c in countries and (sites or claim_values(ent, "P159") or claim_values(ent, "P1454") or claim_values(ent, "P6375")):
            basis = "exact name match + country + organisation claims"
        else:
            continue
        item_q = sorted({q for p in ("P31", "P1454", "P17", "P159") for k, q in claim_values(ent, p) if k == "item"})
        lab = labels_for(item_q)
        off = [v for k, v in claim_values(ent, "P1448") if k == "text"]
        amounts = lambda p: "; ".join(v for k, v in claim_values(ent, p) if k == "amount")[:120]
        sl = ent.get("sitelinks") or {}
        wp = (sl.get("enwiki") or sl.get("frwiki") or {}).get("title", "")
        row = {"qid": s["id"], "match_basis": basis, "official_name": " | ".join(off)[:300], "label_en": lab_en, "label_fr": lab_fr,
               "instance_of": "; ".join(lab.get(q, q) for q in inst)[:200], "legal_form": "; ".join(lab.get(q, q) for k, q in claim_values(ent, "P1454") if k == "item")[:120],
               "country": "; ".join(lab.get(q, q) for q in countries)[:80], "inception": "; ".join(v for k, v in claim_values(ent, "P571") if k == "time")[:40],
               "headquarters": "; ".join(lab.get(q, q) for k, q in claim_values(ent, "P159") if k == "item")[:120], "street_address": "; ".join(v for k, v in claim_values(ent, "P6375") if k == "text")[:200],
               "phone": "; ".join(v for k, v in claim_values(ent, "P1329") if k == "str")[:80], "email": "; ".join(v.replace("mailto:", "") for k, v in claim_values(ent, "P968") if k == "str")[:120],
               "website": "; ".join(sites)[:200], "employees": amounts("P1128"), "budget_or_revenue": (("budget " + amounts("P2769")) if amounts("P2769") else "") + ((" revenue " + amounts("P2139")) if amounts("P2139") else ""),
               "neq": ("; ".join(v for k, v in claim_values(ent, NEQ_PID) if k == "str")[:40] if NEQ_PID else ""), "wikipedia": wp,
               "evidence_url": "https://www.wikidata.org/wiki/" + s["id"], "retrieved_date": TODAY, "status": "matched"}
        row["evidence_quote"] = ("%s — official name: %s; instance of: %s; country: %s; website: %s" % (s["id"], row["official_name"] or lab_en or lab_fr, row["instance_of"], row["country"], row["website"]))[:300]
        return row
    return None


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--ranked", default="")
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--only-missing", action="store_true", help="only organisations without a published legal name")
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_wikidata_orgs.csv")
    prev = {}
    if os.path.exists(out):
        for r in csv.DictReader(open(out, encoding="utf-8")):
            prev[(r["side"], r["key"])] = r
    ranked = a.ranked or os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv.gz")
    opener = gzip.open if ranked.endswith(".gz") else open
    tasks, seen = [], set()
    order = {"GOLD": 0, "GOLD-T": 0, "GOLD-M": 0}
    with opener(ranked, "rt", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            g = r.get("rank_group") or ""
            pri = order.get(g, 1 if (r.get("tier") in ("A", "B")) else 2 if r.get("tier") in ("T", "M", "L", "C", "D") else 3)
            bname = r.get("buyer") or ""
            key = (r.get("keys") or "").split("|")[0]
            if bname and not ("." in bname and " " not in bname) and ("b", key) not in prev and key not in seen:
                if not (a.only_missing and r.get("buyer_legal_name_as_published")):
                    seen.add(key)
                    tasks.append((pri, "b", key, bname, host(r.get("buyer_website") or ""), (r.get("jurisdiction") or "")[:2] if (r.get("jurisdiction") or "") in ("US", "UK", "AU", "NZ", "IE", "FR", "DE") else ("CA" if r.get("jurisdiction") else "")))
            vname = (r.get("vendor_legal_name") or "").split(" (")[0] or r.get("vendor") or ""
            vk = "v:" + norm(vname)
            if vname and not vname.startswith("inferred") and pri <= 2 and ("v", vk) not in prev and vk not in seen:
                seen.add(vk)
                tasks.append((pri + 0.5, "v", vk, vname, host(r.get("vendor_website") or ""), "CA"))
    # the Québec enterprise number property, looked up by its label so nothing is assumed about property ids
    global NEQ_PID
    NEQ_PID = ""
    d = get("%s?action=wbsearchentities&search=%s&language=en&type=property&limit=5&format=json" % (API, urllib.parse.quote("Quebec enterprise number")))
    for sres in (d or {}).get("search") or []:
        if re.search(r"qu[ée]bec enterprise number|num[ée]ro d'entreprise du qu[ée]bec|\bNEQ\b", (sres.get("label") or "") + " " + (sres.get("description") or ""), re.I):
            NEQ_PID = sres["id"]; break
    print("NEQ property:", NEQ_PID or "not found (column stays empty)", flush=True)
    tasks.sort(key=lambda t: t[0])
    if a.limit:
        tasks = tasks[:a.limit]
    print("organisations to look up: %d (known: %d)" % (len(tasks), len(prev)), flush=True)
    n = 0; hits = 0
    for pri, side, key, name, dom, country in tasks:
        try:
            row = lookup(name, dom, country)
        except Exception as e:
            row = None
        base = {"key": key, "side": side, "name": name, "domain": dom, "retrieved_date": TODAY}
        if row:
            hits += 1; base.update(row)
        else:
            base.update({"status": "no_match", "evidence_url": "%s?action=wbsearchentities&search=%s&language=en&type=item&format=json" % (API, urllib.parse.quote(name[:200]))})
        prev[(side, key)] = base
        n += 1
        if n % 100 == 0:
            print(n, "looked up,", hits, "matched", flush=True)
        if n % 500 == 0:
            write(out, prev)
    write(out, prev)
    print("done:", n, "looked up,", hits, "matched; file has", len(prev), flush=True)


def write(out, prev):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for k in sorted(prev):
            w.writerow({c: str(prev[k].get(c, "") or "").replace("\0", "") for c in COLS})
    os.replace(out + ".tmp", out)


if __name__ == "__main__":
    main()

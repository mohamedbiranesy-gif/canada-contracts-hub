#!/usr/bin/env python3
"""Match vendors to Canadian organisations on Wikidata (fetched by wikidata_fetch.py).
Exact joins: Québec Enterprise Number (P10503) = vendor NEQ, Corporation Number in Canada (P13850) = vendor federal corporation number,
Canada Business Number (P8860) = vendor BN9, LEI (P1278) = LEI of the vendor's exact/strong GLEIF match, stock ticker = ticker published
in the contract data.  Otherwise name (label/alias en/fr) + HQ city / postal code.
usage: python3 -I match_wikidata.py <wikidata_dir>"""
import sys, os, re, json, gzip, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vx_common as C  # noqa: E402

D = sys.argv[1]
RAW = os.path.join(D, "raw")
log = open(os.path.join(D, "fetch.log")).read().splitlines()
RETRIEVED = "%s to %s (WDQS queries)" % (log[0][:20], log[-1][:20]) if log else None
ENDPOINT = "https://query.wikidata.org/sparql (queries: scripts/enrichment_vendors_extra/wikidata_fetch.py)"
EXCH = {"Toronto Stock Exchange": "TSX", "TSX Venture Exchange": "TSXV", "New York Stock Exchange": "NYSE", "Nasdaq": "NASDAQ", "NASDAQ": "NASDAQ",
        "Canadian Securities Exchange": "CSE", "London Stock Exchange": "LSE", "NYSE American": "NYSE AMERICAN", "Cboe Canada": "CBOE CANADA", "Neo Exchange": "NEO"}
ROLE_RE = re.compile(r"^(info|information|contact|contactus|general|admin|office|hello|inquiries|enquiries|inquiry|service|services|sales|support|reception|media|communications|comms|accounts|accountspayable|ap|payable|payables|billing|invoices?|invoicing|procurement|purchasing|ventes|courrier|accueil|bureau|renseignements|admin\w*)@", re.I)

vendors, meta = C.load_index()
need = C.need_map(vendors)


def q(u):
    return u.rsplit("/", 1)[1] if isinstance(u, str) and u.startswith("http://www.wikidata.org/entity/") else None


items = collections.defaultdict(lambda: {"labels": {}, "aliases": collections.defaultdict(set), "props": collections.defaultdict(list), "tickers": [], "hq": []})
for fn in sorted(glob.glob(os.path.join(RAW, "labels_*.json.gz"))):
    for b in json.load(gzip.open(fn, "rt"))["results"]["bindings"]:
        it = items[q(b["item"]["value"])]
        if "l" in b:
            it["labels"][b["l"].get("xml:lang")] = b["l"]["value"]
        if "a" in b:
            it["aliases"][b["a"].get("xml:lang")].add(b["a"]["value"])
for fn in sorted(glob.glob(os.path.join(RAW, "props_*.json.gz"))):
    for b in json.load(gzip.open(fn, "rt"))["results"]["bindings"]:
        it = items[q(b["item"]["value"])]
        p = b["p"]["value"].rsplit("/", 1)[1]
        v = b["v"]["value"]
        it["props"][p].append({"value": q(v) or v, "label": (b.get("vl") or {}).get("value")})
for fn in sorted(glob.glob(os.path.join(RAW, "ticker_hq_*.json.gz"))):
    for b in json.load(gzip.open(fn, "rt"))["results"]["bindings"]:
        it = items[q(b["item"]["value"])]
        if "exch" in b:
            it["tickers"].append({"exchange_qid": q(b["exch"]["value"]), "exchange": (b.get("exchl") or {}).get("value"), "ticker": (b.get("ticker") or {}).get("value")})
        if "hq" in b:
            it["hq"].append({"qid": q(b["hq"]["value"]), "label": (b.get("hql") or {}).get("value"), "country_qid": q((b.get("hqc") or {}).get("value"))})
print("items", len(items), file=sys.stderr, flush=True)

# LEIs of exact/strong GLEIF matches
gleif_lei = collections.defaultdict(dict)
gp = C.V2 + "/vendors_extra_gleif.jsonl"
if os.path.exists(gp):
    for l in open(gp, encoding="utf-8"):
        d = json.loads(l)
        for m in d["matches"]:
            if m["match_confidence"] in ("exact", "strong"):
                gleif_lei[d["vendor_key"]].setdefault(m["identifiers"]["lei"], m["match_confidence"])

ents = {}
by_loose = collections.defaultdict(set)
by_id = collections.defaultdict(set)
for qid, it in items.items():
    P = it["props"]
    if any(x["value"] == "Q5" for x in P.get("P31", [])):
        continue  # human
    names = [it["labels"].get("en"), it["labels"].get("fr")] + sorted(it["aliases"].get("en", set()))[:15] + sorted(it["aliases"].get("fr", set()))[:10] + \
            [x["value"] for x in P.get("P1448", [])]
    names = [n for n in names if n]
    if not names:
        continue
    sk, lk = C.name_keys(names)
    cities = {C.norm_city(h["label"]) for h in it["hq"] if h.get("label") and h.get("country_qid") in (None, "Q16")} - {None}
    postals = {C.norm_postal(x["value"]) for x in P.get("P281", [])} - {None}
    ents[qid] = {"sk": sk, "lk": lk, "cities": cities, "postals": postals, "it": it, "names": names}
    for l in lk:
        if l in need:
            by_loose[l].add(qid)
    for x in P.get("P10503", []):
        by_id[("neq", re.sub(r"\D", "", x["value"]))].add(qid)
    for x in P.get("P13850", []):
        by_id[("cc", re.sub(r"\D", "", x["value"]).lstrip("0"))].add(qid)
    for x in P.get("P8860", []):
        m = re.match(r"\s*(\d{9})", re.sub(r"[\s-]", "", x["value"]))
        if m:
            by_id[("bn9", m.group(1))].add(qid)
    for x in P.get("P1278", []):
        by_id[("lei", x["value"].strip().upper())].add(qid)
    for t in it["tickers"]:
        if t.get("ticker"):
            ex = EXCH.get(t.get("exchange") or "", (t.get("exchange") or "").upper())
            by_id[("ticker", "%s:%s" % (ex, t["ticker"].upper()))].add(qid)
print("entities", len(ents), "name keys", len(by_loose), "id keys", len(by_id), file=sys.stderr, flush=True)


def vals(P, p, lab=False):
    return [(x["label"] or x["value"]) if lab else x["value"] for x in P.get(p, [])]


def record(qid, conf, basis):
    E = ents[qid]
    it = E["it"]
    P = it["props"]
    label = it["labels"].get("en") or it["labels"].get("fr") or E["names"][0]
    emails = []
    for e in vals(P, "P968"):
        e2 = e.replace("mailto:", "").strip()
        if ROLE_RE.match(e2):
            emails.append({"email": e2.lower(), "label": "organisational e-mail on the Wikidata item (P968)", "evidence_url": "https://www.wikidata.org/wiki/%s" % qid})
    phones = sorted({C.norm_phone(p) or p for p in vals(P, "P1329")})
    emp = []
    for x in vals(P, "P1128"):
        try:
            emp.append(int(float(x)))
        except Exception:
            pass
    tick = ["%s:%s" % (EXCH.get(t.get("exchange") or "", t.get("exchange")), t["ticker"]) for t in it["tickers"] if t.get("ticker")]
    ident = {"wikidata_qid": qid, "lei": sorted(set(vals(P, "P1278"))) or None, "tickers": sorted(set(tick)) or None,
             "neq": sorted(set(vals(P, "P10503"))) or None, "corporation_number": sorted(set(vals(P, "P13850"))) or None,
             "canada_business_number": sorted(set(vals(P, "P8860"))) or None}
    hq = [h for h in it["hq"] if h.get("label")]
    return {"match_confidence": conf, "match_basis": basis, "legal_name": (vals(P, "P1448") or [label])[0],
            "identifiers": {k: v for k, v in ident.items() if v},
            "address": {"line1": (vals(P, "P6375") or [None])[0], "city": hq[0]["label"] if hq else None, "postal_code": (vals(P, "P281") or [None])[0],
                        "country": "CA" if any(h.get("country_qid") == "Q16" for h in hq) or "Q16" in vals(P, "P17") else None,
                        "headquarters": [{"qid": h["qid"], "label": h["label"], "country_qid": h.get("country_qid")} for h in hq] or None},
            "phones": phones, "emails": emails, "website": (vals(P, "P856") or [None])[0],
            "status": ("dissolved/abolished %s" % vals(P, "P576")[0][:10]) if vals(P, "P576") else "Wikidata item",
            "extra": {"label_en": it["labels"].get("en"), "label_fr": it["labels"].get("fr"), "aliases": sorted(set().union(*it["aliases"].values()))[:20] if it["aliases"] else [],
                      "all_websites": sorted(set(vals(P, "P856"))), "instance_of": sorted(set(vals(P, "P31", True))), "industry": sorted(set(vals(P, "P452", True))),
                      "inception": sorted(set(v[:10] for v in vals(P, "P571"))) or None, "employees": max(emp) if emp else None, "employees_all_values": sorted(set(emp)) or None,
                      "parent_organization": [{"qid": x["value"], "label": x["label"]} for x in P.get("P749", [])] or None,
                      "owned_by": [{"qid": x["value"], "label": x["label"]} for x in P.get("P127", [])] or None,
                      "subsidiaries_count": len(P.get("P355", [])), "subsidiaries_sample": [x["label"] or x["value"] for x in P.get("P355", [])][:15],
                      "legal_form": sorted(set(vals(P, "P1454", True))) or None, "country": sorted(set(vals(P, "P17", True))),
                      "stock_exchanges": [t for t in it["tickers"]] or None, "revenue": vals(P, "P2139")[:3] or None,
                      "short_name": vals(P, "P1813")[:3] or None, "linkedin_company_id": vals(P, "P4264")[:2] or None, "x_twitter_username": vals(P, "P2002")[:2] or None,
                      "member_of_stock_index_or_other": None},
            "source_url": "https://www.wikidata.org/wiki/%s" % qid, "dataset_url": ENDPOINT, "retrieved_at": RETRIEVED,
            "raw": {"labels": it["labels"], "aliases": {k: sorted(v) for k, v in it["aliases"].items()}, "claims": {k: v for k, v in P.items()},
                    "stock_exchange_statements": it["tickers"], "headquarters": it["hq"]}}


out = C.Out("wikidata")
stats = collections.Counter()
LBL = {"neq": "Québec Enterprise Number (P10503)", "cc": "Corporation Number in Canada (P13850)", "bn9": "Canada Business Number (P8860)", "lei": "LEI (P1278)", "ticker": "stock ticker (P414/P249)"}
for v in vendors:
    cand = {}
    joins = [(k, val, cw) for k in ("neq", "cc", "bn9", "ticker") for val, cw in v["ids"][k].items()]
    joins += [("lei", lei, (c, "LEI %s of the vendor's %s GLEIF match" % (lei, c))) for lei, c in gleif_lei.get(v["vendor_key"], {}).items()]
    for kind, val, (conf, why) in joins:
        key = (kind, val.lstrip("0") if kind == "cc" else val)
        for qid in by_id.get(key, ()):
            E = ents[qid]
            vt = set(" ".join(v["lk"]).split()) - C.GENERIC
            et = set(" ".join(E["lk"]).split()) - C.GENERIC
            ok = bool(vt & et) or bool(v["lk"] & E["lk"])
            cand[qid] = {"ent": qid, "idmatch": (conf if ok else "weak", "Wikidata %s %s equals the %s; %s" % (LBL[kind], val, why, "names share tokens" if ok else "NAMES DIFFER"))}
    C.resolve_id_ambiguity(cand)
    for l in v["lk"]:
        for qid in by_loose.get(l, ()):
            cand.setdefault(qid, {"ent": qid, "idmatch": None})
    if not cand:
        continue
    cl = []
    for qid, c in cand.items():
        E = ents[qid]
        c["strict"] = bool(v["sk"] & E["sk"])
        c["lkey_match"] = bool(v["lk"] & E["lk"])
        c["loc"] = C.loc_eval(v, E["postals"], E["cities"], set())
        c["lkey"] = next(iter(E["lk"]), "")
        c["rec_provs"] = set()
        if not c["idmatch"] and not c["lkey_match"]:
            continue
        cl.append(c)
    graded = C.grade(v, cl)
    for c in graded:
        if c.get("idmatch") or c["match_confidence"] != "strong" or c["loc"]["locagree"]:
            continue
        E = ents[c["ent"]]
        mk = sorted(v["lk"] & E["lk"], key=len, reverse=True)
        if mk and not C.distinctive(mk[0]):
            c["match_confidence"] = "weak"
            c["basis"] += "; short/non-distinctive name (acronym or generic words) without location agreement"
        elif E["it"]["hq"] and not any(h.get("country_qid") in (None, "Q16") for h in E["it"]["hq"]):
            c["match_confidence"] = "weak"
            c["basis"] += "; Wikidata item headquartered outside Canada (%s)" % "/".join(sorted({h.get("label") or "?" for h in E["it"]["hq"]}))
        elif E["cities"] and (v["cities"] or v["reg_cities"]):
            c["match_confidence"] = "weak"
            c["basis"] += "; Wikidata HQ city (%s) differs from every vendor city" % "/".join(sorted(E["cities"]))
    order = {"exact": 0, "strong": 1, "weak": 2}
    graded.sort(key=lambda c: order[c["match_confidence"]])
    matches = [record(c["ent"], c["match_confidence"], c["basis"]) for c in graded]
    out.write(v, matches)
    if matches and matches[0]["match_confidence"] in ("exact", "strong"):
        m = matches[0]
        stats["es_website"] += bool(m["website"])
        stats["es_lei"] += bool(m["identifiers"].get("lei"))
        stats["es_ticker"] += bool(m["identifiers"].get("tickers"))
        stats["es_parent"] += bool(m["extra"]["parent_organization"])
        stats["es_phone"] += bool(m["phones"])
        stats["es_email"] += bool(m["emails"])
        stats["es_idjoin"] += "equals the" in m["match_basis"]
res = out.close()
res.update(stats)
res["items_fetched"] = len(items)
json.dump(res, open(C.WORK + "/wikidata_stats.json", "w"), indent=1)
print(json.dumps(res, indent=1))

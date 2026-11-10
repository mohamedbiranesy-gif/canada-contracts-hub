#!/usr/bin/env python3
"""Pilot dossiers (owner 2026-11-09 11:21 EST: "research everything about each company, each vendor … the other AI must have the most information possible").

Layer 1 — everything the repo already holds about the buyer, the vendor and the relationship of each sampled row, assembled into one file per row:
  - the delivered row itself (every non-empty column, grouped: relationship / buyer / AP / vendor / contract / tax-currency / pay-on-sight);
  - the AP pages read for the buyer's mailbox (tools/ap_terms.py rows: terms, PO rule, portal, phone, address, format — each with URL + quote);
  - site facts for the buyer's and the vendor's domains (org_extras: legal names, JSON-LD, BN, portals, logo, language; org_contacts: role mailboxes);
  - registry records (Canada's Business Registries lookups; REQ / Corporations Canada bulk match), Wikidata, the lanes' verified findings (team_buyers),
    PO-level open data, lead details;
  - every contract record in the dataset between the pair, the buyer's other Canadian vendors and the vendor's other buyers (history and scale).
Layer 2 — hand research (web search, fetched pages, with URL + date + quote) is appended under "## Web research" by the integrator over the week.
Output: coord/pilot/dossiers/<sample_id>__<slug>.md and .json (the raw joined data). Nothing here changes the pack.
  python3 tools/pilot_dossier.py [--sample coord/pilot/PILOT_SAMPLE_2026-11-09.csv] [--out coord/pilot/dossiers] [--contracts data/release/canadian_vendor_contracts.jsonl.gz]
"""
import argparse, collections, csv, gzip, json, os, re, sys, urllib.parse

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import hashlib, unicodedata  # the canonical keys of the dataset, copied from scripts/merge/finalize.py (which runs its argv at import)
LEGAL = re.compile(r"\b(inc|incorporated|ltd|ltee|ltée|limited|limitee|limitée|corp|corporation|co|company|compagnie|llc|lp|llp|plc|gmbh|ag|sa|s\.a|srl|bv|nv|pty|the|le|la|les|l|d|de|du|des|et|and|&|group|groupe|holdings|holding|international|intl|canada|canadian|canadienne|canadien)\b")
NONALNUM = re.compile(r"[^a-z0-9 ]+")
SPACES = re.compile(r"\s+")


def stem(name):
    if not name:
        return ""
    s = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode().lower()
    s = NONALNUM.sub(" ", s)
    s = LEGAL.sub(" ", s)
    return SPACES.sub(" ", s).strip()


def _key(prefix, *parts):
    return prefix + ":" + hashlib.sha1("|".join(p or "" for p in parts).encode()).hexdigest()[:16]


def vkey(rec):
    s = stem((rec.get("vendor") or {}).get("name"))
    return _key("v", s) if s else None


def bkey(rec):
    b = rec.get("buyer") or {}
    s = stem(b.get("name"))
    return _key("b", s, b.get("country") or "") if s else None

INC = os.path.join(ROOT, "data/incoming/claude")
GROUPS = [
    ("Relationship", r"^(rank_group|tier|grade|keys|how_relationship_was_found|relationship_detail|records_with_this_vendor|inference_confidence|evidence_age_days|reverify_due|sensitivity_flag|ship_ready|data_quality_score)$"),
    ("Buyer", r"^buyer"),
    ("Submit-to / AP", r"^(email|email_|mailbox|ap_|invoice_|invoicing_|po_required|po_number|payment_terms|supplier_setup|peppol|channel_tier|template_language|language_hint|dmarc|spf|mta_sts|tls_rpt|bimi|email_security|email_deliverability)"),
    ("Vendor", r"^vendor"),
    ("Contract", r"^(contract|solicitation|award|start_date|end_date|currency|commodity|number_of_bids|source|dataset|record|notice|po_)"),
    ("Tax / currency / terms (derived)", r"(_derived|_default_policy|tax_rate)"),
    ("Pay on sight / grades", r"^(pay_on_sight|ap_grade|ap_score|ap_gap|ap_payability|invoice_readiness|invoice_missing|invoice_text|invoice_card_json|facts_provenance_json)"),
]


def dom(w):
    if not w:
        return ""
    h = (urllib.parse.urlparse(w if "//" in w else "https://" + w).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:48]


def read_csv(path, gz=False):
    op = gzip.open if gz or path.endswith(".gz") else open
    if not os.path.exists(path):
        return []
    with op(path, "rt", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def read_jsonl(path):
    out = []
    if not os.path.exists(path):
        return out
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for l in fh:
            try:
                out.append(json.loads(l))
            except Exception:
                pass
    return out


def md_table(rows, cols, limit=60):
    if not rows:
        return ["_none_", ""]
    L = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows[:limit]:
        L.append("| " + " | ".join(str(r.get(c, "") or "").replace("|", "\\|").replace("\n", " ")[:220] for c in cols) + " |")
    if len(rows) > limit:
        L.append("| … %d more rows in the .json | %s" % (len(rows) - limit, "|" * (len(cols) - 1)))
    return L + [""]


def kv_block(row, rx):
    L = []
    for k, v in row.items():
        if v and re.search(rx, k):
            L.append("- **%s**: %s" % (k, str(v).replace("\n", " ⏎ ")[:1500]))
    return L or ["_nothing recorded_"]


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--sample", default=os.path.join(ROOT, "coord/pilot/PILOT_SAMPLE_2026-11-09.csv"))
    a.add_argument("--ranked", default=os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz"))
    a.add_argument("--contracts", default=os.path.join(ROOT, "data/release/canadian_vendor_contracts.jsonl.gz"))
    a.add_argument("--out", default=os.path.join(ROOT, "coord/pilot/dossiers"))
    a.add_argument("--only", default="", help="comma-separated sample_ids")
    a = a.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sample = read_csv(a.sample)
    if a.only:
        want = set(a.only.split(","))
        sample = [s for s in sample if s["sample_id"] in want]
    skeys = {s["keys"].split("|")[0] for s in sample}
    ranked = {}
    with gzip.open(a.ranked, "rt", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            k = (r.get("keys") or "").split("|")[0]
            if k in skeys and (k not in ranked or r.get("email")):
                ranked[k] = r
    print("sample rows %d, ranked rows found %d" % (len(sample), len(ranked)), flush=True)
    bdoms = {dom(s.get("buyer_website")) for s in sample} - {""}
    vdoms = {dom(s.get("vendor_website")) for s in sample} - {""}
    emails = {s["email"].lower() for s in sample if s.get("email")}
    vkeys = {vkey({"vendor": {"name": s["vendor"]}}) for s in sample}
    # engine outputs
    ap_terms = [r for r in read_csv(os.path.join(INC, "claude_ap_terms.csv")) if (r.get("email") or "").lower() in emails or dom(r.get("evidence_url")) in bdoms]
    extras = {d.get("domain"): d for d in read_jsonl(os.path.join(INC, "claude_org_extras.jsonl.gz")) if d.get("domain") in bdoms | vdoms}
    contacts = {d.get("domain"): d for d in read_jsonl(os.path.join(INC, "claude_org_contacts.jsonl.gz")) if d.get("domain") in bdoms | vdoms}
    reg = [r for r in read_csv(os.path.join(INC, "claude_registry_lookup.csv")) if r.get("key") in skeys | vkeys]
    regb = [r for r in read_csv(os.path.join(INC, "claude_registry_bulk.csv")) if r.get("key") in skeys | vkeys]
    wd = [r for r in read_csv(os.path.join(INC, "claude_wikidata_orgs.csv")) if r.get("key") in skeys | vkeys or r.get("domain") in bdoms | vdoms]
    try:
        import state_io
        state_io.ensure(os.path.join(ROOT, "coord/results/team_buyers.jsonl.gz"))
    except Exception:
        pass
    team = {d.get("buyer_key"): d for d in read_jsonl(os.path.join(ROOT, "coord/results/team_buyers.jsonl.gz")) if d.get("buyer_key") in skeys}
    bstems = {stem(s["buyer"]) for s in sample}
    po = [r for r in read_csv(os.path.join(INC, "claude_po_records.csv.gz")) if stem(r.get("buyer")) in bstems]
    leads = [d for d in read_jsonl(os.path.join(INC, "claude_lead_details.jsonl.gz")) if d.get("key") in skeys]
    print("joined: ap_terms %d, extras %d, contacts %d, registry %d+%d, wikidata %d, team %d, po %d, leads %d" % (len(ap_terms), len(extras), len(contacts), len(reg), len(regb), len(wd), len(team), len(po), len(leads)), flush=True)
    # contracts: one pass
    by_pair, by_buyer, by_vendor = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(list)
    n = 0
    if os.path.exists(a.contracts):
        with gzip.open(a.contracts, "rt", encoding="utf-8") as fh:
            for l in fh:
                n += 1
                try:
                    rec = json.loads(l)
                except Exception:
                    continue
                bk, vk = bkey(rec), vkey(rec)
                if bk in skeys or vk in vkeys:
                    c = rec.get("contract") or {}
                    slim = {"record_id": rec.get("record_id"), "source": (rec.get("source") or {}).get("key"), "status": rec.get("status"), "buyer": (rec.get("buyer") or {}).get("name"), "vendor": (rec.get("vendor") or {}).get("name"),
                            "title": (c.get("title") or c.get("description") or "")[:160], "value": c.get("value") or c.get("amount"), "currency": c.get("currency"), "start": c.get("start_date"), "end": c.get("end_date"),
                            "identifiers": json.dumps(c.get("identifiers") or {}, ensure_ascii=False)[:200], "link": rec.get("link"), "vendor_country_basis": (rec.get("vendor") or {}).get("country_basis"), "vendor_address": json.dumps((rec.get("vendor") or {}).get("address") or {}, ensure_ascii=False)[:200],
                            "buyer_address": json.dumps((rec.get("buyer") or {}).get("address") or {}, ensure_ascii=False)[:200], "buyer_contact": json.dumps((rec.get("buyer") or {}).get("contact") or {}, ensure_ascii=False)[:200]}
                    if bk in skeys and vk in vkeys:
                        by_pair[(bk, vk)].append(slim)
                    elif bk in skeys and len(by_buyer[bk]) < 300:
                        by_buyer[bk].append(slim)
                    elif vk in vkeys and len(by_vendor[vk]) < 300:
                        by_vendor[vk].append(slim)
                if n % 200000 == 0:
                    print("  contracts scanned", n, flush=True)
    print("contracts scanned %d; pair records %d; buyer-other %d; vendor-other %d" % (n, sum(map(len, by_pair.values())), sum(map(len, by_buyer.values())), sum(map(len, by_vendor.values()))), flush=True)
    CCOLS = ["record_id", "source", "status", "title", "value", "currency", "start", "end", "identifiers", "link"]
    for s in sample:
        k = s["keys"].split("|")[0]
        r = ranked.get(k, {})
        vk = vkey({"vendor": {"name": s["vendor"]}})
        bd, vd = dom(s.get("buyer_website")), dom(s.get("vendor_website"))
        pair = by_pair.get((k, vk), [])
        data = {"sample": s, "row": r, "ap_pages": [x for x in ap_terms if (x.get("email") or "").lower() == (s.get("email") or "").lower() or dom(x.get("evidence_url")) == bd],
                "buyer_site": extras.get(bd), "buyer_contacts": contacts.get(bd), "vendor_site": extras.get(vd), "vendor_contacts": contacts.get(vd),
                "registry": [x for x in reg if x.get("key") in (k, vk)], "registry_bulk": [x for x in regb if x.get("key") in (k, vk)], "wikidata": [x for x in wd if x.get("key") in (k, vk) or x.get("domain") in (bd, vd)],
                "team": team.get(k), "po_records": [x for x in po if stem(x.get("buyer")) == stem(s["buyer"])], "leads": [x for x in leads if x.get("key") == k],
                "contracts_pair": pair, "contracts_buyer_other": by_buyer.get(k, []), "contracts_vendor_other": by_vendor.get(vk, [])}
        base = os.path.join(a.out, "%s__%s" % (s["sample_id"], slug(s["buyer"])))
        json.dump(data, open(base + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        L = ["# %s — %s ⇄ %s" % (s["sample_id"], s["buyer"], s["vendor"]), "",
             "Stratum: **%s** · pay on sight: %s · channel tier %s · AP grade %s · missing: %s" % (s["stratum"], s.get("pay_on_sight"), s.get("channel_tier"), s.get("ap_grade"), s.get("pay_on_sight_missing") or "—"), "",
             "## 1. Draft invoice header (from the row)", "```", r.get("invoice_text") or s.get("invoice_text") or "", "```", ""]
        for title, rx in GROUPS:
            L += ["## %s" % title] + kv_block(r, rx) + [""]
        L += ["## AP pages read for this buyer (tools/ap_terms.py; every value with its quote)"] + md_table(data["ap_pages"], ["evidence_url", "retrieved_date", "status", "payment_terms", "po_required", "portal_name", "ap_phone", "invoice_mailing_address", "invoice_format", "ap_system", "payment_terms_quote", "po_quote"])
        for side, key_ in (("Buyer", "buyer_site"), ("Vendor", "vendor_site")):
            d = data[key_]
            L += ["## %s site facts (org_extras, %s)" % (side, (d or {}).get("domain") or "domain unknown")]
            L += ["- **%s**: %s" % (kk, str(vv)[:600]) for kk, vv in (d or {}).items() if vv and kk not in ("pages_read",)] or ["_not read_"]
            L.append("")
            c = data[key_.replace("site", "contacts")]
            L += ["## %s role mailboxes found on its site (org_contacts)" % side, "- " + json.dumps({kk: vv for kk, vv in (c or {}).items() if kk not in ("pages_read",)}, ensure_ascii=False)[:2500] if c else "_not read_", ""]
        L += ["## Registry records (Canada's Business Registries lookups)"] + md_table(data["registry"], ["kind", "name", "status", "matched_name", "bn9", "juri_id", "registry_source", "entity_type", "status_state", "date_incorporated", "reg_office_city", "reg_office_province", "reg_office_address", "ui_url", "retrieved_date"])
        L += ["## Registry records (REQ / Corporations Canada bulk match)"] + md_table(data["registry_bulk"], ["kind", "name", "status", "matched_name", "bn9", "juri_id", "registry_source", "entity_type", "status_state", "date_incorporated", "reg_office_city", "reg_office_province", "reg_office_address", "api_url", "retrieved_date"])
        L += ["## Wikidata"] + md_table(data["wikidata"], ["side", "name", "qid", "match_basis", "official_name", "label_en", "label_fr", "instance_of", "legal_form", "country", "inception", "headquarters"])
        t = data["team"]
        L += ["## Lanes' verified findings for this buyer (team_buyers)", "```", json.dumps(t, ensure_ascii=False, indent=1)[:6000] if t else "none", "```", ""]
        L += ["## PO-level open data naming this buyer"] + md_table(data["po_records"], ["kind", "id_label", "vendor_name", "po_number", "date", "amount", "description", "source_url", "retrieved_date"])
        L += ["## Contract records between the pair (dataset)"] + md_table(pair, CCOLS)
        L += ["## The buyer's other Canadian-vendor records (first 60 of %d)" % len(data["contracts_buyer_other"])] + md_table(data["contracts_buyer_other"], ["record_id", "vendor", "title", "value", "start", "end", "link"])
        L += ["## The vendor's other buyers in the dataset (first 60 of %d)" % len(data["contracts_vendor_other"])] + md_table(data["contracts_vendor_other"], ["record_id", "buyer", "title", "value", "start", "end", "link"])
        gaps = [g.strip() for g in (s.get("pay_on_sight_missing") or "").split(";") if g.strip()]
        L += ["## Open questions for hand research (layer 2)", ""] + ["- %s" % g for g in gaps] + [
            "- buyer: supplier registration / vendor setup process, invoice submission rules, AP system, fiscal year end, procurement policy, PO practice, recent budget / annual report mentions of this vendor, council or board minutes approving this contract (they carry PO / contract numbers)",
            "- vendor: legal name and registry ids, GST/HST number if printed anywhere public, remit-to address, AR contact, NAICS / line of business, other public-sector customers, news about this relationship", "",
            "## Web research (layer 2 — appended by the integrator; every fact with URL, date read and a quote ≤ 300 chars)", "", "_pending_", ""]
        open(base + ".md", "w", encoding="utf-8").write("\n".join(L))
    print("wrote %d dossiers to %s" % (len(sample), a.out))


if __name__ == "__main__":
    main()

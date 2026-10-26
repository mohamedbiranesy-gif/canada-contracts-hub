#!/usr/bin/env python3
"""Attach vendor + buyer enrichment to every record and write the deliverables.

Usage: python3 -I finalize.py <contracts_dir> <out_dir>
Reads  work/merged_ca.jsonl, work/merged_unverified.jsonl, normalized/*.jsonl,
       enrichment/v2/vendor_master_input.jsonl, enrichment/v2/vendors_registry.jsonl,
       enrichment/v2/vendors_orgbook.jsonl (optional), enrichment/buyers_enriched.jsonl,
       enrichment/v2/buyer_master_input.jsonl
Writes <out_dir>/canadian_vendor_contracts.jsonl.gz, vendor_country_unverified_contracts.jsonl.gz,
       full/<source>.jsonl.gz, vendors_enriched.jsonl.gz, buyers_enriched.jsonl.gz, summary.json
"""
import sys, os, json, re, gzip, hashlib, unicodedata, collections, datetime

BASE, OUT = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from identify import parties_identifiable
os.makedirs(os.path.join(OUT, "full"), exist_ok=True)
TODAY = "2026-10-25"
CRA_NOTE = ("not checked automatically: the CRA GST/HST Registry (https://apps.cra-arc.gc.ca/ebci/hacc/srch/pub/dsplyBscSrch) is protected by a CAPTCHA; "
            "confirm the derived number there (number + legal name + transaction date) before relying on it")

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


def key(prefix, *parts):
    return prefix + ":" + hashlib.sha1("|".join(p or "" for p in parts).encode()).hexdigest()[:16]


def vkey(rec):
    s = stem((rec.get("vendor") or {}).get("name"))
    return key("v", s) if s else None


def bkey(rec):
    b = rec.get("buyer") or {}
    s = stem(b.get("name"))
    return key("b", s, b.get("country") or "") if s else None


def year_of(d):
    try:
        return int(str(d)[:4])
    except Exception:
        return None


def confidence(rec):
    st = rec.get("status")
    basis = (rec.get("status_basis") or "").lower()
    k = (rec.get("source") or {}).get("key", "")
    dates = (rec.get("contract") or {}).get("dates") or {}
    if st == "ongoing":
        if "> 2100" in basis or "placeholder" in basis or "data-entry error" in basis:
            return "high_flagged_date", "explicit end date >= 2026-10-25 but it looks like a placeholder/data-entry error (see status_basis)"
        return "high", "source publishes an explicit end date >= 2026-10-25 and a start/award date <= 2026-10-25"
    if st == "end_date_unknown":
        return "unknown", "source publishes the award/contract but no end date, duration or closure signal"
    if st == "ongoing_inferred":
        if k == "seao_quebec" or "no final-information" in basis or "closure record" in basis:
            y = year_of(dates.get("signed") or dates.get("start") or dates.get("published"))
            if y is not None and y >= 2023:
                return "low", "only evidence is the absence of a closure (information finale) record; contract concluded in %d" % y
            return "very_low", "only evidence is the absence of a closure (information finale) record; contract concluded in %s; closure publication is incomplete and late, so many of these have probably ended" % (y if y else "an unknown year")
        return "medium", "end date computed from a stated duration/term, framework or project period, or the parent award's period (see status_basis)"
    return "unknown", "unrecognised status"


def best_link(rec):
    src = rec.get("source") or {}
    if src.get("record_url"):
        return src["record_url"], "record_page"
    rel = (rec.get("contract") or {}).get("related") or {}
    for k in ("award_notice_url", "tender_notice_url", "notice_url", "contract_url", "project_url", "prime_award_url", "document_url", "release_url"):
        v = rel.get(k)
        if isinstance(v, str) and v.startswith("http"):
            return v, k
    for k, v in rel.items():
        if isinstance(v, str) and v.startswith("http") and "url" in k.lower():
            return v, k
    if src.get("dataset_url"):
        return src["dataset_url"], "dataset_page (source has no per-record page; use the identifiers to find the record)"
    return None, None


# ---------------- vendor enrichment ----------------
ORDER = {"exact": 0, "strong": 1, "weak": 2}
ob = {}
import glob
for obp in sorted(glob.glob(os.path.join(BASE, "enrichment/v2/vendors_orgbook.jsonl*"))):
    with open(obp, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            ltoks = [t for t in re.sub(r"[^A-Z0-9 ]", " ", unicodedata.normalize("NFKD", str(d.get("name") or "")).encode("ascii", "ignore").decode().upper()).split()
                     if t not in ("INC", "LTD", "LIMITED", "CORP", "CORPORATION", "CO", "COMPANY", "LTEE", "ULC", "LLC", "THE")]
            for mm in d.get("matches") or []:
                if mm.get("match_confidence") == "strong" and len(ltoks) < 2:
                    mm["match_confidence"] = "weak"
                    mm["match_basis"] = (mm.get("match_basis") or "") + "; downgraded to weak: one-word vendor name is too generic to identify a company"
            ob[d["vendor_key"]] = d

vweb = {}
for wp in sorted(glob.glob(os.path.join(BASE, "enrichment/v2/vendors_web.jsonl.shard*"))):
    with open(wp, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("website") or d["vendor_key"] not in vweb:
                vweb[d["vendor_key"]] = d
vblock = {}
vstats = collections.Counter()
vtable_path = os.path.join(OUT, "vendors_enriched.jsonl.gz")
with gzip.open(vtable_path, "wt", encoding="utf-8", compresslevel=6) as vt:
    fvm = open(os.path.join(BASE, "enrichment/v2/vendor_master_input.jsonl"), encoding="utf-8")
    freg = open(os.path.join(BASE, "enrichment/v2/vendors_registry_v3.jsonl"), encoding="utf-8")
    for line_vm, line_reg in zip(fvm, freg):
        m = json.loads(line_vm)
        r = json.loads(line_reg)
        vk = m["vendor_key"]
        if r.get("vendor_key") != vk:
            raise SystemExit("vendor master and registry file are out of step at %s" % vk)
        o = ob.get(vk) or {}
        matches = list(r.get("registry_matches") or []) + list(o.get("matches") or [])
        matches.sort(key=lambda x: ORDER.get(x.get("match_confidence"), 3))
        good = [x for x in matches if x.get("match_confidence") in ("exact", "strong")]
        cc = next((x for x in good if x["registry"] == "corporations_canada"), None)
        bco = next((x for x in good if x["registry"] == "bc_orgbook"), None)
        req = next((x for x in good if x["registry"] == "quebec_req"), None)
        primary = good[0] if good else None
        bn_sources = []
        for x in (cc, bco):
            if x and x.get("business_number_bn9"):
                bn_sources.append((x["business_number_bn9"], x))
        bn9 = bn_sources[0][0] if bn_sources else None
        bn_conflict = len({b for b, _ in bn_sources}) > 1
        # identifiers already published in the contract data
        pub_ids = {k: [e.get("value") for e in lst][:3] for k, lst in (m.get("identifiers") or {}).items()}
        pub_bn = None
        for k, lst in pub_ids.items():
            if re.search(r"(^|_)(bn|business_number|gst|hst|numero_entreprise)", k.lower()):
                for val in lst:
                    digits = re.sub(r"\D", "", str(val))
                    if len(digits) >= 9:
                        pub_bn = digits[:9]
                        break
        if pub_bn and not bn9:
            bn9 = pub_bn
        regaddr = None
        if cc:
            regaddr = {"source": "Corporations Canada registered office", **(cc.get("registered_office") or {})}
        elif req:
            regaddr = {"source": "Quebec REQ domicile address", **(req.get("domicile_address") or {})}
        block = {
            "vendor_key": vk,
            "registry_match_level": primary["match_confidence"] if primary else ("weak_candidates_only" if matches else "no_match"),
            "legal_name": primary.get("legal_name") if primary else None,
            "registry_status": primary.get("status") if primary else None,
            "corporation_number_federal": cc.get("corporation_number") if cc else None,
            "neq_quebec": (req.get("neq") if req else None),
            "bc_registration_number": bco.get("registration_number") if bco else None,
            "business_number_bn9": bn9,
            "business_number_source": ("published in the contract data" if (pub_bn and bn9 == pub_bn) else
                                       ("%s %s (%s match)" % (bn_sources[0][1]["registry"], bn_sources[0][1].get("corporation_number") or bn_sources[0][1].get("registration_number"), bn_sources[0][1]["match_confidence"]) if bn_sources else None)),
            "business_number_conflict": [b for b, _ in bn_sources] if bn_conflict else None,
            "gst_hst_account_derived": (bn9 + "RT0001") if bn9 else None,
            "gst_hst_note": ("DERIVED, not published: a business's first GST/HST account is normally BN9 + RT0001 and exists only if the business is GST/HST-registered. " + CRA_NOTE) if bn9 else None,
            "registered_address": regaddr,
            "incorporation_or_registration_date": (cc or {}).get("anniversary_date") or (req or {}).get("constitution_date") or (req or {}).get("registration_date") or (bco or {}).get("registration_date"),
            "governing_legislation_or_regime": (cc or {}).get("governing_legislation") or (req or {}).get("jurisdiction") or ((bco or {}).get("entity_type")),
            "legal_form_quebec": (req or {}).get("legal_form"),
            "employees_in_quebec": (req or {}).get("employees_in_quebec"),
            "main_activity": (req or {}).get("main_activity"),
            "website": (vweb.get(vk) or {}).get("website"),
            "website_verification": (vweb.get(vk) or {}).get("website_verification"),
            "contact_emails_published": [{"email": e["email"], "page_url": e["page_url"], "retrieved_at": e.get("retrieved_at")} for e in ((vweb.get(vk) or {}).get("emails") or [])],
            "phones_published": (vweb.get(vk) or {}).get("phones") or [],
            "website_lookup_status": ("not yet looked up" if vk not in vweb else ("found" if (vweb.get(vk) or {}).get("website") else "no verified website found")),
            "matches": [{"registry": x["registry"], "id": x.get("corporation_number") or x.get("neq") or x.get("registration_number"),
                         "legal_name": x.get("legal_name"), "status": x.get("status"), "business_number_bn9": x.get("business_number_bn9"),
                         "match_confidence": x.get("match_confidence"), "match_basis": x.get("match_basis"), "source_url": x.get("source_url")}
                        for x in matches[:5]],
            "full_detail": "vendors_enriched.jsonl.gz -> vendor_key %s" % vk,
        }
        vblock[vk] = block
        vstats["vendors"] += 1
        vstats["level_" + block["registry_match_level"]] += 1
        if bn9:
            vstats["with_bn9"] += 1
        if block["website"]:
            vstats["with_website"] += 1
        if block["contact_emails_published"]:
            vstats["with_contact_email"] += 1
        if vk in vweb:
            vstats["website_looked_up"] += 1
        vt.write(json.dumps({"vendor_key": vk, "name": m.get("name"), "name_variants": m.get("name_variants"), "countries_in_data": m.get("countries"),
                             "addresses_in_contract_data": m.get("addresses"), "identifiers_in_contract_data": m.get("identifiers"),
                             "contacts_in_contract_data": m.get("contacts"), "sources": m.get("sources"), "record_count": m.get("record_count"),
                             "record_count_high_or_medium": m.get("record_count_high_or_medium"), "summary": block,
                             "registry_matches_full": matches, "tax": r.get("tax"), "orgbook_queried": o.get("queried"), "website_lookup": vweb.get(vk)}, ensure_ascii=False) + "\n")
print("vendor table done", dict(vstats), file=sys.stderr, flush=True)
del ob

# ---------------- buyer enrichment ----------------
be = {}
for bep in ("enrichment/buyers_enriched.jsonl", "enrichment/v2/buyers_enriched_v2.jsonl"):
    if not os.path.exists(os.path.join(BASE, bep)):
        continue
    with open(os.path.join(BASE, bep), encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            be.setdefault(d["buyer_key"], d)
bm = {}
with open(os.path.join(BASE, "enrichment/v2/buyer_master_input.jsonl"), encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        bm[d["buyer_key"]] = d
bblock = {}
bstats = collections.Counter()
with gzip.open(os.path.join(OUT, "buyers_enriched.jsonl.gz"), "wt", encoding="utf-8") as bt:
    for bk, m in bm.items():
        d = be.get(bk)
        if d:
            ap = d.get("ap_contact") or {}
            block = {"buyer_key": bk, "enrichment_status": "enriched", "canonical_name": d.get("canonical_name"), "official_website": d.get("official_website"),
                     "organisation_type": d.get("organisation_type"), "identifiers": d.get("identifiers"), "address": d.get("address"),
                     "ap_contact": ap, "procurement_contact": d.get("procurement_contact"), "general_contact": d.get("general_contact"),
                     "notes": d.get("notes"), "full_detail": "buyers_enriched.jsonl.gz -> buyer_key %s" % bk}
            bstats["enriched"] += 1
            if ap.get("emails"):
                bstats["with_ap_email"] += 1
            bt.write(json.dumps({**d, "record_count": m.get("record_count"), "sources": m.get("sources")}, ensure_ascii=False) + "\n")
        else:
            block = {"buyer_key": bk, "enrichment_status": "not_yet_enriched", "official_website": None, "ap_contact": None}
            bstats["not_enriched"] += 1
            bt.write(json.dumps({"buyer_key": bk, "name": m.get("name"), "country": m.get("country"), "enrichment_status": "not_yet_enriched",
                                 "names_in_data": m.get("name_variants"), "identifiers_in_data": m.get("identifiers"), "addresses_in_data": m.get("addresses"),
                                 "contacts_in_data": m.get("contacts"), "record_count": m.get("record_count"), "sources": m.get("sources")}, ensure_ascii=False) + "\n")
        bblock[bk] = block
print("buyer table done", dict(bstats), file=sys.stderr, flush=True)
del be

# ---------------- slim merged outputs ----------------
rstats = collections.Counter()
xmatch = {}
badf = gzip.open(os.path.join(OUT, "parties_not_identified_contracts.jsonl.gz"), "wt", encoding="utf-8")
for bucket, src, dst in (("ca", "work/merged_ca.jsonl", "canadian_vendor_contracts.jsonl.gz"),
                         ("unverified", "work/merged_unverified.jsonl", "vendor_country_unverified_contracts.jsonl.gz")):
    with open(os.path.join(BASE, src), encoding="utf-8") as fin, gzip.open(os.path.join(OUT, dst), "wt", encoding="utf-8", compresslevel=6) as fout:
        for line in fin:
            rec = json.loads(line)
            vk, bk = vkey(rec), bkey(rec)
            rec["vendor_enrichment"] = vblock.get(vk) if vk else None
            rec["buyer_enrichment"] = bblock.get(bk) if bk else None
            if rec.get("cross_source_matches"):
                xmatch[rec["record_id"]] = rec["cross_source_matches"]
            ok, why = parties_identifiable(rec)
            if not ok:
                rec["parties_identifiable"], rec["parties_identifiable_reason"] = False, why
                badf.write(json.dumps(rec, ensure_ascii=False) + "\n")
                rstats[bucket + "_moved_not_identifiable"] += 1
                continue
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            rstats[bucket + "_records"] += 1
            ve, bb = rec["vendor_enrichment"] or {}, rec["buyer_enrichment"] or {}
            if ve.get("registry_match_level") in ("exact", "strong"):
                rstats[bucket + "_vendor_registry_match"] += 1
            if ve.get("business_number_bn9"):
                rstats[bucket + "_vendor_bn9"] += 1
            if ve.get("website"):
                rstats[bucket + "_vendor_website"] += 1
            if ve.get("contact_emails_published") or (rec.get("vendor") or {}).get("contact"):
                rstats[bucket + "_vendor_contact_any"] += 1
            if bb.get("enrichment_status") == "enriched":
                rstats[bucket + "_buyer_enriched"] += 1
            if (bb.get("ap_contact") or {}).get("emails"):
                rstats[bucket + "_buyer_ap_email"] += 1
            if (bb.get("ap_contact") or {}).get("invoice_portal"):
                rstats[bucket + "_buyer_invoice_portal"] += 1
            if bb.get("official_website"):
                rstats[bucket + "_buyer_website"] += 1
    print("slim done", bucket, dict(rstats), file=sys.stderr, flush=True)
badf.close()

# ---------------- full per-source outputs ----------------
nd = os.path.join(BASE, "normalized")
for fn in sorted(os.listdir(nd)):
    if not fn.endswith(".jsonl") or os.path.getsize(os.path.join(nd, fn)) == 0:
        continue
    seen = set()
    with open(os.path.join(nd, fn), encoding="utf-8", errors="replace") as fin, gzip.open(os.path.join(OUT, "full", fn + ".gz"), "wt", encoding="utf-8", compresslevel=6) as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            rid = rec.get("record_id")
            if rid in seen:
                continue
            seen.add(rid)
            c, cb = confidence(rec)
            rec["status_confidence"], rec["status_confidence_basis"] = c, cb
            rec["link"], rec["link_type"] = best_link(rec)
            vd = rec.get("vendor") or {}
            rec["vendor_country_verified"] = (vd.get("country") or "").upper() in ("CA", "CAN", "CANADA")
            rec["cross_source_matches"] = xmatch.get(rid, [])
            _ok, _why = parties_identifiable(rec)
            rec["parties_identifiable"], rec["parties_identifiable_reason"] = _ok, _why
            vk, bk = vkey(rec), bkey(rec)
            rec["vendor_enrichment"] = vblock.get(vk) if vk else None
            rec["buyer_enrichment"] = bblock.get(bk) if bk else None
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("full done", fn, file=sys.stderr, flush=True)

summary = {"reference_date": TODAY, "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "record_enrichment_coverage": dict(rstats), "vendor_table": dict(vstats), "buyer_table": dict(bstats)}
with open(os.path.join(OUT, "enrichment_summary.json"), "w") as f:
    json.dump(summary, f, indent=1)
print(json.dumps(summary, indent=1))

#!/usr/bin/env python3
"""Rebuild step: bring the published dataset up to date without re-running the full pipeline.

Usage: python3 tools/patch_dataset.py <release_dir> <out_dir>
Inputs in <release_dir> (download from the releases first; all optional except the dataset):
  canadian_vendor_contracts.jsonl.gz      dataset-latest (required)
  vendors_enriched.jsonl.gz               dataset-latest (to enrich new-source records)
  buyers_enriched.jsonl.gz                dataset-latest (to enrich new-source records)
  seao_api_notices.jsonl.gz               harvest-state  (planned end dates of Québec contracts)
  vendors_web_progress.jsonl.gz           harvest-state  (verified vendor websites, role e-mails, phones)
  vendors_orgbook_xp_progress.jsonl.gz    harvest-state  (BC OrgBook extraprovincial registrations)
Also reads coord/results/team_buyers.jsonl, coord/results/team_vendors.jsonl (verified team findings) and
data/incoming/*/records_*.jsonl.gz (validated new-source records).
Writes <out_dir>/canadian_vendor_contracts.jsonl.gz, <out_dir>/ended_since_last_build.jsonl.gz,
<out_dir>/patch_report.json and refreshes coord/dataset_summary.json. Streams the dataset; modest memory.
"""
import collections, datetime, glob, gzip, json, os, re, subprocess, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "enrichment_vendors"))
from normname import strict_key, norm_prov  # noqa: E402

REL, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
REF = json.load(open("coord/config.json"))["reference_date"]
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
rep, fill = collections.Counter(), collections.Counter()


def jl(p):
    if not os.path.exists(p):
        return
    op = gzip.open if p.endswith(".gz") else open
    with op(p, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


# ---------- update sources ----------
tb = {r["buyer_key"]: r["ap_contact_team"] for r in jl("coord/results/team_buyers.jsonl")
      if (r.get("ap_contact_team") or {}).get("emails") or (r.get("ap_contact_team") or {}).get("invoice_portal")}
tv = {r["vendor_key"]: r for r in jl("coord/results/team_vendors.jsonl")}
seao = {}
for r in jl(os.path.join(REL, "seao_api_notices.jsonl.gz")):
    ends = [d["datePrevueFinContratUtc"][:10] for d in r.get("dates") or [] if d.get("datePrevueFinContratUtc")]
    if ends:
        seao[r["uuid"]] = (max(ends), r.get("api_url"))
web = {r["vendor_key"]: r for r in jl(os.path.join(REL, "vendors_web_progress.jsonl.gz")) if r.get("website")}
obx = {}
for r in jl(os.path.join(REL, "vendors_orgbook_xp_progress.jsonl.gz")):
    m = next((m for m in r.get("matches") or [] if m.get("registration_number")), None)
    if m:
        obx[r["vendor_key"]] = m
rep.update({"team_buyers_verified": len(tb), "team_vendors": len(tv), "seao_api_end_dates": len(seao),
            "web_vendors_with_site": len(web), "orgbook_xp_matches": len(obx)})


def enrich(r):
    """Apply every verified update to one record (existing or new)."""
    be = r.get("buyer_enrichment") or {}
    ve = r.get("vendor_enrichment") or {}
    r["buyer_enrichment"], r["vendor_enrichment"] = be, ve
    t = tb.get(be.get("buyer_key"))
    if t:
        ap = be.get("ap_contact") or {}
        be["ap_contact"] = ap
        before = bool(ap.get("emails") or ap.get("invoice_portal"))
        ap["emails"] = list(dict.fromkeys((t.get("emails") or []) + (ap.get("emails") or [])))
        ap["invoice_portal"] = ap.get("invoice_portal") or t.get("invoice_portal")
        ap["team_evidence"] = [e for e in t.get("evidence") or [] if e.get("verification") == "verified"][:5]
        rep["records_ap_added" if not before else "records_ap_extended"] += 1
    vk = ve.get("vendor_key")
    w = web.get(vk)
    if w and not ve.get("website"):
        ve["website"], ve["website_verification"], ve["website_lookup_status"] = w["website"], w.get("website_verification"), "found"
        if not ve.get("contact_emails_published"):
            ve["contact_emails_published"] = [{k: v for k, v in (e if isinstance(e, dict) else {"email": e}).items() if k != "snippet"}
                                              for e in w.get("emails") or []]
        if not ve.get("phones_published"):
            ve["phones_published"] = w.get("phones") or []
        rep["records_web_added"] += 1
    ob = obx.get(vk)
    if ob and not ve.get("bc_registration_number"):
        ve["bc_registration_number"] = ob["registration_number"]
        ve["bc_registration_source"] = ob.get("source_url")
        ve["bc_registration_detail"] = {k: ob.get(k) for k in ("legal_name", "entity_type", "status", "registration_date", "home_jurisdiction")}
        rep["records_orgbook_added"] += 1
    v = tv.get(vk)
    if v:
        have = {(e.get("email") if isinstance(e, dict) else e) for e in ve.get("contact_emails_published") or []}
        for e in v.get("evidence") or []:
            if e.get("verification") == "verified" and e.get("email") and e["email"] not in have:
                ve.setdefault("contact_emails_published", []).append({"email": e["email"], "page_url": e.get("page_url"),
                                                                      "found_by": e.get("found_by"), "kind": e.get("kind")})
                have.add(e["email"])
        if v.get("website") and not ve.get("website"):
            ve["website"], ve["website_verification"] = v["website"], "team (%s): %s" % (v.get("found_by"), v.get("website_verification") or "")
        if v.get("main_phone") and not ve.get("phones_published"):
            ve["phones_published"] = [v["main_phone"]]
        rep["records_vendor_patched"] += 1
    src = r.get("source") or {}
    if src.get("key") == "seao_quebec" and r.get("status") != "ongoing":
        m = re.search(r"ItemId=([0-9a-f-]{36})", src.get("record_url") or "")
        if m and m.group(1) in seao:
            end, url = seao[m.group(1)]
            r.setdefault("contract", {}).setdefault("dates", {})["end"] = end
            r["status"], r["status_confidence"] = "ongoing", "high"
            r["status_basis"] = "SEAO API datePrevueFinContratUtc %s (%s)" % (end, url)
            rep["seao_status_upgraded"] += 1


def count(r):
    be, ve = r.get("buyer_enrichment") or {}, r.get("vendor_enrichment") or {}
    ap = be.get("ap_contact") or {}
    fill["records"] += 1
    fill["status_" + (r.get("status") or "")] += 1
    fill["ca_buyer_ap_email"] += bool(ap.get("emails"))
    fill["ca_buyer_invoice_portal"] += bool(ap.get("invoice_portal"))
    fill["ca_buyer_website"] += bool(be.get("official_website"))
    fill["ca_vendor_website"] += bool(ve.get("website"))
    fill["ca_vendor_bn9"] += bool(ve.get("business_number_bn9"))
    fill["ca_vendor_registry_match"] += ve.get("registry_match_level") not in (None, "no_match") or bool(ve.get("bc_registration_number"))
    fill["ca_vendor_contact_any"] += bool(ve.get("website") or ve.get("contact_emails_published") or ve.get("phones_published"))


fo = gzip.open(os.path.join(OUT, "canadian_vendor_contracts.jsonl.gz"), "wt", encoding="utf-8")
fe = gzip.open(os.path.join(OUT, "ended_since_last_build.jsonl.gz"), "wt", encoding="utf-8")


def emit(r):
    d = (r.get("contract") or {}).get("dates") or {}
    if r.get("status") == "ongoing" and d.get("end") and d["end"] < REF:
        r["status"] = "ended"
        r["status_basis"] = "end date %s is before reference date %s (rebuild %s)" % (d["end"], REF, now[:10])
        fe.write(json.dumps(r, ensure_ascii=False) + "\n")
        rep["moved_to_ended"] += 1
        return
    count(r)
    fo.write(json.dumps(r, ensure_ascii=False) + "\n")


seen = set()
for r in jl(os.path.join(REL, "canadian_vendor_contracts.jsonl.gz")):
    seen.add(r.get("record_id"))
    enrich(r)
    emit(r)

# ---------- new-source records contributed by the team ----------
new_files = sorted(glob.glob("data/incoming/*/records_*.jsonl.gz"))
if new_files:
    vidx, vamb, bidx = {}, set(), {}
    for v in jl(os.path.join(REL, "vendors_enriched.jsonl.gz")):
        provs = {norm_prov((a.get("value") or {}).get("region")) for a in v.get("addresses_in_contract_data") or []} - {None, ""}
        for n in {v.get("name")} | set((v.get("name_variants") or [])[:4]):
            k = strict_key(n or "")
            if not k:
                continue
            for p in provs or {""}:
                key = (k, p)
                if key in vidx and vidx[key]["vendor_key"] != v["vendor_key"]:
                    vamb.add(key)
                vidx[key] = v.get("summary") or {"vendor_key": v["vendor_key"]}
    for b in jl(os.path.join(REL, "buyers_enriched.jsonl.gz")):
        for n in {b.get("name"), b.get("canonical_name")}:
            if n:
                bidx.setdefault((strict_key(n), b.get("country") or ""), b)
    for p in new_files:
        res = subprocess.run([sys.executable, "tools/validate_records.py", "--allow-ended", p], capture_output=True, text=True)
        if res.returncode != 0:
            rep["new_source_files_rejected"] += 1
            rep["rejected:" + p] = (res.stdout or "")[-300:]
            continue
        for r in jl(p):
            if r.get("record_id") in seen:
                rep["new_records_duplicate"] += 1
                continue
            seen.add(r["record_id"])
            vend, buy = r.get("vendor") or {}, r.get("buyer") or {}
            vkey = (strict_key(vend.get("name") or ""), norm_prov((vend.get("address") or {}).get("region")) or "")
            if vkey in vidx and vkey not in vamb:
                r["vendor_enrichment"] = dict(vidx[vkey], match_basis="vendor name + province match to existing vendor (rebuild %s)" % now[:10])
                rep["new_records_vendor_matched"] += 1
            elif not r.get("vendor_enrichment"):
                r["vendor_enrichment"] = {"enrichment_status": "pending"}
            bkey = (strict_key(buy.get("name") or ""), buy.get("country") or "")
            b = bidx.get(bkey)
            if b:
                r["buyer_enrichment"] = {k: b.get(k) for k in ("buyer_key", "canonical_name", "official_website", "organisation_type", "identifiers",
                                                               "address", "ap_contact", "procurement_contact", "general_contact")}
                r["buyer_enrichment"]["enrichment_status"] = "matched_existing_buyer"
                rep["new_records_buyer_matched"] += 1
            elif not r.get("buyer_enrichment"):
                r["buyer_enrichment"] = {"enrichment_status": "pending"}
            r["contributed_by"] = p.split(os.sep)[-2]
            enrich(r)
            rep["new_records_added"] += 1
            emit(r)
fo.close()
fe.close()

report = dict(rep, built_at=now, reference_date=REF)
json.dump({"report": report, "fill": fill}, open(os.path.join(OUT, "patch_report.json"), "w"), indent=1)
s = json.load(open("coord/dataset_summary.json")) if os.path.exists("coord/dataset_summary.json") else {}
s["reference_date"] = REF
s["verified_ca_records"] = fill["records"]
s["status_verified_ca"] = {k[7:]: v for k, v in fill.items() if k.startswith("status_")}
s.setdefault("enrichment", {}).setdefault("record_enrichment_coverage", {}).update({k: v for k, v in fill.items() if k.startswith("ca_")})
s["last_rebuild"] = now
s["last_rebuild_report"] = {k: v for k, v in report.items() if not k.startswith("rejected:")}
json.dump(s, open("coord/dataset_summary.json", "w"), indent=1)
print(json.dumps(report, indent=1))
print(json.dumps(fill, indent=1))

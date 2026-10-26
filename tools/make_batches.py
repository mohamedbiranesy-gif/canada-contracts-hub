#!/usr/bin/env python3
"""Refill work queues from the release tables. Run from repo root after:
   gh release download dataset-latest -D data/release -p 'buyers_enriched.jsonl.gz' -p 'vendors_enriched.jsonl.gz'
Usage: python3 tools/make_batches.py data/release [--batches 5]
Adds the next N batches (100 rows) per lane for buyer AP contacts and vendor contacts, largest first, skipping
entities already queued anywhere or already holding a verified contact. Lanes: Québec -> gemini, rest of
Canada + US -> chatgpt, elsewhere -> codex."""
import csv, glob, gzip, json, os, re, sys, collections

REL = sys.argv[1]
NB = int(sys.argv[sys.argv.index("--batches") + 1]) if "--batches" in sys.argv else 5
queued = set()
for p in glob.glob("coord/tasks/*/*.csv"):
    for r in csv.DictReader(open(p, encoding="utf-8-sig", newline="")):
        queued.add(r.get("buyer_key") or r.get("vendor_key") or "")
for p in ("coord/results/team_buyers.jsonl", "coord/results/team_vendors.jsonl"):
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            d = json.loads(l)
            queued.add(d.get("buyer_key") or d.get("vendor_key") or "")


def jl(name):
    with gzip.open(os.path.join(REL, name), "rt", encoding="utf-8") as f:
        for l in f:
            yield json.loads(l)


def next_num(lane, kind):
    nums = [int(m.group(1)) for p in glob.glob("coord/tasks/%s/%s_%s_batch*.csv" % (lane, lane, kind)) for m in [re.search(r"batch(\d+)", p)] if m]
    return max(nums or [0]) + 1


def write(lane, kind, header, rows, prefix):
    n0, made = next_num(lane, kind), 0
    existing = sum(1 for p in glob.glob("coord/tasks/%s/%s_%s_batch*.csv" % (lane, lane, kind)) for _ in open(p)) 
    os.makedirs("coord/tasks/%s" % lane, exist_ok=True)
    for b in range(NB):
        chunk = rows[b * 100:(b + 1) * 100]
        if not chunk:
            break
        with open("coord/tasks/%s/%s_%s_batch%02d.csv" % (lane, lane, kind, n0 + b), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            for i, row in enumerate(chunk, 1):
                w.writerow(["%s-%05d" % (prefix, existing + b * 100 + i)] + row)
        made += 1
    print(lane, kind, "batches added:", made, "(candidates left: %d)" % max(0, len(rows) - NB * 100))


# buyers without AP e-mail or invoice portal
bl = collections.defaultdict(list)
for b in jl("buyers_enriched.jsonl.gz"):
    ap = b.get("ap_contact") or {}
    if b["buyer_key"] in queued or ap.get("emails") or ap.get("invoice_portal"):
        continue
    if re.search(r"not disclosed|undisclosed|withheld|confidential|identity not|unknown buyer", b.get("canonical_name") or b.get("name") or "", re.I):
        continue
    srcs = {s["value"] for s in b.get("sources") or []}
    c = b.get("country") or ""
    lane = "gemini" if (c == "CA" and "seao_quebec" in srcs) else ("chatgpt" if c in ("CA", "US") else "codex")
    gc, pc = b.get("general_contact") or {}, b.get("procurement_contact") or {}
    bl[lane].append((b.get("record_count") or 0, [re.sub(r"\s+", " ", (b.get("canonical_name") or b.get("name") or "").lower()), b["buyer_key"], b.get("canonical_name") or b.get("name"), "", c,
                     b.get("official_website") or "", ", ".join((gc.get("emails") or [])[:2]), ", ".join((pc.get("emails") or [])[:2]), b.get("record_count") or 0]))
hdr = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website", "known_general_email", "known_procurement_email", "contracts_in_dataset"]
for lane, rows in bl.items():
    rows.sort(key=lambda x: -x[0])
    write(lane, "buyer_ap", hdr, [r for _, r in rows], lane[:2].upper() + "-AP")

# vendors without website and without any published contact
vl = collections.defaultdict(list)
for v in jl("vendors_enriched.jsonl.gz"):
    s = v.get("summary") or {}
    if v["vendor_key"] in queued or s.get("website") or s.get("contact_emails_published") or s.get("phones_published"):
        continue
    addr = next(((a.get("value") or {}) for a in v.get("addresses_in_contract_data") or [] if (a.get("value") or {}).get("region") or (a.get("value") or {}).get("city")), {})
    prov = (addr.get("region") or s.get("registered_address", {}).get("region") if isinstance(s.get("registered_address"), dict) else addr.get("region")) or ""
    lane = "gemini" if str(prov).upper() in ("QC", "QUEBEC", "QUÉBEC") else "chatgpt"
    tried = " ".join(c.get("domain", "") for c in ((v.get("website_lookup") or {}).get("candidates_checked") or []))
    vl[lane].append((v.get("record_count_high_or_medium") or 0, v.get("record_count") or 0, [v["vendor_key"], v.get("name"), s.get("legal_name") or "",
                     s.get("neq_quebec") or s.get("corporation_number_federal") or s.get("bc_registration_number") or "", addr.get("city") or "", prov,
                     addr.get("postal_code") or "", v.get("record_count") or 0, v.get("record_count_high_or_medium") or 0, tried]))
vhdr = ["task_id", "vendor_key", "vendor_name", "legal_name_in_registry", "registry_id", "city", "province", "postal_code", "contracts_in_dataset", "contracts_high_or_medium_confidence", "domains_already_tried"]
for lane, rows in vl.items():
    rows.sort(key=lambda x: (-x[0], -x[1]))
    write(lane, "vendor_contacts", vhdr, [r for _, _, r in rows], lane[:2].upper() + "-VC")

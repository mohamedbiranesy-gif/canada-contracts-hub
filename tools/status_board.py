#!/usr/bin/env python3
"""Regenerate coord/STATUS_BOARD.md from the dataset summary, team results, source registry and harvest state."""
import csv, glob, json, os, collections, datetime

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
L = ["# STATUS BOARD (auto-generated %s — do not edit by hand)\n" % now]
s = json.load(open("coord/dataset_summary.json")) if os.path.exists("coord/dataset_summary.json") else {}
e = (s.get("enrichment") or {}).get("record_enrichment_coverage") or {}
if s:
    n = s.get("verified_ca_records") or 0
    pct = lambda k: "%d (%.0f%%)" % (e.get(k, 0), 100.0 * e.get(k, 0) / n) if n else "-"
    L += ["## Dataset (release `dataset-latest`, reference date %s)" % s.get("reference_date"),
          "| metric | value |", "|---|---|",
          "| contracts, vendor verified in Canada | %s |" % format(n, ","),
          "| contracts, vendor country unverified | %s |" % format(s.get("unverified_records") or 0, ","),
          "| sources with records / checked without | %s / %s |" % (s.get("sources_with_records"), s.get("sources_checked_without_records")),
          "| status: ongoing (explicit end date) | %s |" % format((s.get("status_verified_ca") or {}).get("ongoing", 0), ","),
          "| status: ongoing_inferred | %s |" % format((s.get("status_verified_ca") or {}).get("ongoing_inferred", 0), ","),
          "| status: end_date_unknown | %s |" % format((s.get("status_verified_ca") or {}).get("end_date_unknown", 0), ","),
          "| buyer AP e-mail | %s |" % pct("ca_buyer_ap_email"), "| buyer invoice portal | %s |" % pct("ca_buyer_invoice_portal"),
          "| buyer website | %s |" % pct("ca_buyer_website"), "| vendor registry match | %s |" % pct("ca_vendor_registry_match"),
          "| vendor Business Number (BN9) | %s |" % pct("ca_vendor_bn9"), "| vendor website | %s |" % pct("ca_vendor_website"),
          "| vendor any contact | %s |" % pct("ca_vendor_contact_any"), ""]
L += ["## Team research progress (rows returned → verified)", "| lane | task | rows | found | not_published | blocked | other |", "|---|---|---|---|---|---|---|"]
for p in sorted(glob.glob("data/incoming/*/*.csv")):
    lane = p.split(os.sep)[-2]
    kind = next((k for k in ("buyer_ap", "vendor_contact", "qa", "source_scouting") if k in os.path.basename(p)), "?")
    st = collections.Counter((r.get("status") or "").strip() for r in csv.DictReader(open(p, encoding="utf-8-sig", newline="")))
    L.append("| %s | %s | %d | %d | %d | %d | %d |" % (lane, os.path.basename(p), sum(st.values()), st["found"] + st["portal_only"] + st["website_only"],
                                                    st["not_published"] + st["not_found"], st["blocked"], sum(st.values()) - st["found"] - st["portal_only"] - st["website_only"] - st["not_published"] - st["not_found"] - st["blocked"]))
for name in ("team_buyers", "team_vendors"):
    p = "coord/results/%s.jsonl" % name
    if os.path.exists(p):
        rows = [json.loads(l) for l in open(p, encoding="utf-8")]
        ver = sum(1 for r in rows if (r.get("ap_contact_team") or {}).get("emails") or (r.get("ap_contact_team") or {}).get("invoice_portal") or r.get("verified_emails"))
        L.append("\n**%s**: %d entities researched, %d with at least one verified contact." % (name, len(rows), ver))
L.append("")
if os.path.exists("coord/source_registry.csv"):
    reg = list(csv.DictReader(open("coord/source_registry.csv", encoding="utf-8")))
    c = collections.Counter((r["lane"], r["status"]) for r in reg)
    L += ["## Source registry (`coord/source_registry.csv`)", "| lane | todo | in_progress | done | blocked |", "|---|---|---|---|---|"]
    for lane in sorted({r["lane"] for r in reg}):
        L.append("| %s | %d | %d | %d | %d |" % (lane, c[(lane, "todo")], c[(lane, "in_progress")], c[(lane, "done")], c[(lane, "blocked")]))
    L.append("")
if os.path.exists("coord/harvest_state.json"):
    h = json.load(open("coord/harvest_state.json"))
    L += ["## Harvesters (state in release `harvest-state`)", "| harvester | done | total | updated |", "|---|---|---|---|"]
    for k, v in h.items():
        L.append("| %s | %s | %s | %s |" % (k, format(v.get("done", 0), ","), format(v.get("total", 0), ",") if v.get("total") else "?", v.get("updated", "")))
    L.append("")
if os.path.exists("coord/INGEST_REPORT.md"):
    L += ["## Last ingest", open("coord/INGEST_REPORT.md", encoding="utf-8").read().split("\n", 1)[-1].strip(), ""]
L += ["## Where to look", "- Next work per lane: `coord/NEXT.md`", "- Messages: `coord/inbox/`", "- Decisions: `coord/DECISIONS.md`"]
open("coord/STATUS_BOARD.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L[:30]))

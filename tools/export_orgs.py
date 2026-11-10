#!/usr/bin/env python3
"""Owner deliverable: one row per organisation with its best published mailbox (run by the referee after ingest).
Writes coord/results/org_mailboxes.csv and coord/results/ORG_MAILBOXES.md (counts).
Best = accepted by the referee first (verified, cross_verified), then waiting, then the rest; within that
invoice_submission > accounts_payable > supplier_payment > procurement > general.
Proof of a Canadian supplier: b: buyers have a contract in the dataset; lead: buyers a payment/subaward record."""
import csv, collections, glob, os
RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "procurement": 3, "general": 4}
STATE = {"verified": 0, "cross_verified": 0, "pending_verification": 1}
outcome = {}
import sys as _sys0
_sys0.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parted_csv as _PC  # the log: the team lanes' file, then the claude lane's file and its parts (tools/ingest_results.py, 2026-11-10)
for _lp0 in ("coord/results/verification_log.csv", "coord/results/verification_log_claude.csv"):
    for r in _PC.rows(_lp0):
        outcome[(r["buyer_key"], r["value"].lower(), r["page_url"])] = r["outcome"]
leads = {}
for _lp in ("data/incoming/claude/claude_buyer_leads.csv", "data/incoming/claude/claude_buyer_leads_cc.csv"):  # the second file: cloud row factory (tools/cc_clients.py)
    if os.path.exists(_lp):
        import sys as _sys
        _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
        import lead_store as _LS  # the cloud leads file is read with its shards (lead_shards/: rows added, changed or withdrawn since the base file)
        for r in _LS.reader(_lp):
            leads.setdefault(r["buyer_key"], r)
import gzip
for _lp in sorted(glob.glob("data/incoming/claude/tenant_state/leads_*.gz")):  # tenant leads accepted by the candidate crawl (append-only shards)
    with gzip.open(_lp, "rt", encoding="utf-8", newline="") as _fh:
        for r in csv.DictReader(_fh):
            leads.setdefault(r["buyer_key"], r)
best = {}
for path in glob.glob("data/incoming/*/*buyer_ap_results*.csv"):
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        k, e = (r.get("buyer_key") or "").strip(), (r.get("ap_email") or "").strip().lower()
        if not k or not e:
            continue
        o = outcome.get((k, e, r.get("evidence_url") or ""), "not_checked")
        t = (r.get("ap_email_type") or "").lower()  # agents sometimes write their own labels (ap_dedicated, general_info ...)
        t = t if t in RANK else ("invoice_submission" if "invoic" in t else "accounts_payable" if ("ap" in t.split("_") or "payable" in t or "finance" in t or "account" in t)
             else "procurement" if ("procure" in t or "purchas" in t) else "general")
        r = dict(r, ap_email_type=t)
        score = (STATE.get(o, 2), RANK[t])
        if k not in best or score < best[k][0]:
            best[k] = (score, r, o, os.path.basename(os.path.dirname(path)))
# vendors (Canadian companies) researched by the agents: their general role mailbox counts as an organisation mailbox
import json
vver = {}
if os.path.exists("coord/results/team_vendors.jsonl"):
    for line in open("coord/results/team_vendors.jsonl", encoding="utf-8"):
        o = json.loads(line)
        vver[o["vendor_key"]] = {e.lower() for e in o.get("verified_emails") or []}
for path in glob.glob("data/incoming/*/*vendor_contacts_results*.csv"):
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        k, e = (r.get("vendor_key") or "").strip(), (r.get("general_email") or "").strip().lower()
        if not k or not e:
            continue
        o = "verified" if e in vver.get(k, set()) else "not_checked"
        score = (STATE.get(o, 2), RANK["general"])
        row = {"org_name_as_found": r.get("vendor_name") or r.get("legal_name") or r.get("official_website"), "ap_email": e,
               "ap_email_type": "general", "evidence_url": r.get("evidence_url"), "evidence_quote": r.get("evidence_quote")}
        if k not in best or score < best[k][0]:
            best[k] = (score, row, o, os.path.basename(os.path.dirname(path)))
kind = lambda k: {"b": "contract with a Canada-located supplier (dataset)", "lead": "relationship record with a Canada-located supplier (payment, subaward, or client listing on the supplier's own site)"}.get(k.split(":")[0], "none (organisation located in Canada)")
os.makedirs("coord/results", exist_ok=True)
counts = collections.Counter()
# 2026-11-10: the file was 42 MB at 90,000 organisations and GitHub refuses files over 100 MB. It is written in parts of at most ~45 MB:
# org_mailboxes.csv (with the header), then org_mailboxes.part02.csv, .part03.csv … (rows only). Read them in order as one CSV.
for _old in glob.glob("coord/results/org_mailboxes.part*.csv"):
    os.remove(_old)
PART_BYTES = 45 * 1024 * 1024
if True:
    _part = 1
    f = open("coord/results/org_mailboxes.csv", "w", newline="", encoding="utf-8")
    w = csv.writer(f)
    w.writerow(["org_key", "org_name", "mailbox", "mailbox_type", "check_status", "evidence_url", "evidence_quote", "found_by",
                "canadian_supplier_proof", "proof_detail"])
    for _n, (k, (score, r, o, lane)) in enumerate(sorted(best.items(), key=lambda kv: kv[1][0])):
        if _n % 2000 == 0 and f.tell() > PART_BYTES:
            f.close()
            _part += 1
            f = open("coord/results/org_mailboxes.part%02d.csv" % _part, "w", newline="", encoding="utf-8")
            w = csv.writer(f)
        L = leads.get(k, {})
        w.writerow([k, r.get("org_name_as_found"), r.get("ap_email"), r.get("ap_email_type"), o, r.get("evidence_url"),
                    (r.get("evidence_quote") or "")[:300], lane, kind(k),
                    ("%s; %s" % (L.get("canada_field_value"), L.get("evidence_dataset"))[:600]) if L else ""])
        acc = "accepted" if score[0] == 0 else ("waiting" if score[0] == 1 else "not accepted")
        tier = "invoicing/AP" if score[1] <= 2 else ("purchasing" if score[1] == 3 else "general")
        counts[(acc, tier)] += 1
        counts[("proof", kind(k))] += 1
f.close()
with open("coord/results/ORG_MAILBOXES.md", "w", encoding="utf-8") as f:
    f.write("# Organisations with a published mailbox (auto-generated by the referee)\n\nOne row per organisation in "
            "`org_mailboxes.csv`. Total organisations: **%d**.\n\n| referee status | invoicing/AP | purchasing | general |\n|---|---|---|---|\n" % len(best))
    for acc in ("accepted", "waiting", "not accepted"):
        f.write("| %s | %d | %d | %d |\n" % (acc, counts[(acc, "invoicing/AP")], counts[(acc, "purchasing")], counts[(acc, "general")]))
    f.write("\n| proof of a Canada-located supplier | organisations |\n|---|---|\n")
    for (a, b), n in sorted(counts.items()):
        if a == "proof":
            f.write("| %s | %d |\n" % (b, n))
print(open("coord/results/ORG_MAILBOXES.md").read())

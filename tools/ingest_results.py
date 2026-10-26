#!/usr/bin/env python3
"""Ingest team research results, verify evidence, write enrichment files the assembly consumes.

Reads   data/incoming/**/*.csv   (formats: docs/RETURN_FORMATS.md; file name says the kind and the author)
Writes  coord/results/team_buyers.jsonl, coord/results/team_vendors.jsonl, coord/results/qa_results.jsonl,
        coord/tasks/<other lane>/<other>_verify_buyer_ap_batch01.csv (pages we could not fetch), coord/source_registry.csv, coord/INGEST_REPORT.md
Usage   python3 tools/ingest_results.py [--no-fetch]      (run from the repo root; idempotent)
Verification: each cited page is fetched once (cached in work/evidence_cache/) and the e-mail/portal must appear in it.
"""
import csv, glob, hashlib, html, json, os, re, subprocess, sys, time, urllib.request, collections, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import EMAIL, PERSONAL, ROLE_HINT

NOFETCH = "--no-fetch" in sys.argv
CACHE = "work/evidence_cache"
os.makedirs(CACHE, exist_ok=True)
os.makedirs("coord/results", exist_ok=True)
os.makedirs("coord", exist_ok=True)
UA = {"User-Agent": "contracts-research/1.0 (evidence verification)"}
RANK = {"invoice_submission": 0, "accounts_payable": 1, "supplier_payment": 2, "procurement": 3, "general": 4}


def page_text(url):
    """Fetched text of a page (cached). None if unavailable."""
    if not url or not url.startswith("http"):
        return None
    p = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest())
    if os.path.exists(p):
        return open(p, encoding="utf-8", errors="replace").read()
    if NOFETCH:
        return None
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            data = r.read(5_000_000)
            ctype = r.headers.get("content-type", "")
    except Exception:
        return None
    if "pdf" in ctype.lower() or url.lower().endswith(".pdf"):
        tmp = p + ".pdf"
        open(tmp, "wb").write(data)
        try:
            txt = subprocess.run(["pdftotext", "-layout", tmp, "-"], capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        except Exception:
            txt = data.decode("latin-1", "replace")
    else:
        txt = html.unescape(data.decode("utf-8", "replace"))
    txt = txt.replace("&#64;", "@").replace("[at]", "@").replace("(at)", "@")
    open(p, "w", encoding="utf-8").write(txt)
    time.sleep(0.5)
    return txt


def bad_email(e):
    return bool(e) and ("@" in e) and (not EMAIL.match(e) or (PERSONAL.match(e.split("@")[0]) and not ROLE_HINT.search(e.split("@")[0])))


def verify(value, url):
    if not value:
        return None
    if bad_email(value):
        return "rejected_personal_or_invalid"
    t = page_text(url)
    if t is None:
        return "unverified_page_unavailable"
    return "verified" if value.lower() in t.lower() else "not_found_on_page"


LANES = ("gemini", "chatgpt", "jules", "codex", "claude")
OTHER = {"gemini": "chatgpt", "chatgpt": "gemini", "jules": "codex", "codex": "jules", "claude": "gemini", "unknown": "gemini"}


def author(path):
    parts = path.replace("\\", "/").split("/")
    if len(parts) >= 2 and parts[-2] in LANES:
        return parts[-2]
    b = os.path.basename(path).lower()
    return next((a for a in LANES if b.startswith(a)), "unknown")


buyers = collections.defaultdict(lambda: {"evidence": [], "statuses": collections.Counter(), "queries": []})
vendors = collections.defaultdict(lambda: {"evidence": [], "statuses": collections.Counter()})
qa_rows, scout_rows, report = [], [], collections.Counter()

for path in sorted(glob.glob("data/incoming/**/*.csv", recursive=True)):
    name, who = os.path.basename(path).lower(), author(path)
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    report["files"] += 1
    if "buyer_ap" in name:
        for r in rows:
            k = (r.get("buyer_key") or "").strip()
            if not k:
                continue
            b = buyers[k]
            b["statuses"][r.get("status") or ""] += 1
            if r.get("queries_tried"):
                b["queries"].append(r["queries_tried"][:300])
            email, portal = (r.get("ap_email") or "").strip(), (r.get("invoice_portal_url") or "").strip()
            if email or portal:
                v = verify(email or portal, r.get("evidence_url"))
                report["buyer_findings_" + (v or "none")] += 1
                b["evidence"].append({"email": email or None, "type": r.get("ap_email_type") or None, "invoice_portal": portal or None,
                                      "phone": r.get("ap_phone") or None, "mailing_address": r.get("invoice_mailing_address") or None,
                                      "requirements": r.get("invoicing_requirements_summary") or None, "applies_to": r.get("applies_to") or None,
                                      "page_url": r.get("evidence_url"), "quote": (r.get("evidence_quote") or "")[:300],
                                      "retrieved_date": r.get("retrieved_date"), "found_by": who, "verification": v, "source_file": name})
    elif "vendor_contact" in name:
        for r in rows:
            k = (r.get("vendor_key") or "").strip()
            if not k:
                continue
            vd = vendors[k]
            vd["statuses"][r.get("status") or ""] += 1
            for col in ("general_email", "billing_or_ar_email"):
                e = (r.get(col) or "").strip()
                if e:
                    v = verify(e, r.get("evidence_url"))
                    report["vendor_emails_" + (v or "none")] += 1
                    vd["evidence"].append({"email": e, "kind": col, "page_url": r.get("evidence_url"), "verification": v, "found_by": who})
            if r.get("official_website"):
                vd.setdefault("website", r["official_website"].strip())
                vd.setdefault("website_verification", r.get("website_verification"))
            for col in ("main_phone", "address_on_site", "business_number_if_published", "other_identifiers"):
                if r.get(col):
                    vd.setdefault(col, r[col].strip())
            vd["found_by"] = who
    elif "qa" in name:
        for r in rows:
            r["_file"] = name
            qa_rows.append(r)
    elif "scouting" in name:
        for r in rows:
            r["found_by"] = who
            scout_rows.append(r)

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open("coord/results/team_buyers.jsonl", "w", encoding="utf-8") as f:
    for k, b in buyers.items():
        ev = sorted(b["evidence"], key=lambda e: (e["verification"] != "verified", RANK.get(e["type"] or "", 9)))
        good = [e for e in ev if e["verification"] == "verified"]
        ap = {"emails": list(dict.fromkeys(e["email"] for e in good if e["email"])),
              "invoice_portal": next((e["invoice_portal"] for e in good if e["invoice_portal"]), None),
              "phone": next((e["phone"] for e in ev if e["phone"]), None),
              "mailing_address": next((e["mailing_address"] for e in ev if e["mailing_address"]), None),
              "invoicing_requirements": next((e["requirements"] for e in ev if e["requirements"]), None),
              "evidence": ev}
        f.write(json.dumps({"buyer_key": k, "ap_contact_team": ap, "research_status": dict(b["statuses"]),
                            "queries_tried": b["queries"][:5], "ingested_at": now}, ensure_ascii=False) + "\n")
with open("coord/results/team_vendors.jsonl", "w", encoding="utf-8") as f:
    for k, vd in vendors.items():
        vd["statuses"] = dict(vd["statuses"])
        vd["verified_emails"] = list(dict.fromkeys(e["email"] for e in vd["evidence"] if e["verification"] == "verified"))
        f.write(json.dumps({"vendor_key": k, **vd, "ingested_at": now}, ensure_ascii=False) + "\n")
with open("coord/results/qa_results.jsonl", "w", encoding="utf-8") as f:
    for r in qa_rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
if scout_rows:
    have = set()
    if os.path.exists("coord/source_registry.csv"):
        have = {r.get("url") for r in csv.DictReader(open("coord/source_registry.csv", encoding="utf-8"))}
    new = [r for r in scout_rows if r.get("url") not in have]
    if new:
        exists = os.path.exists("coord/source_registry.csv")
        with open("coord/source_registry.csv", "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(new[0].keys()))
            if not exists:
                w.writeheader()
            w.writerows(new)
    report["new_sources"] += len(new)
verify = collections.defaultdict(list)
for k, b in buyers.items():
    if any(e["verification"] == "verified" for e in b["evidence"]):
        continue
    for e in b["evidence"]:
        if e["verification"] == "unverified_page_unavailable":
            verify[OTHER.get(e["found_by"], "gemini")].append((k, e))
            break
hdr = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website", "known_general_email", "known_procurement_email", "contracts_in_dataset"]
for lane, items in verify.items():
    os.makedirs("coord/tasks/%s" % lane, exist_ok=True)
    with open("coord/tasks/%s/%s_verify_buyer_ap_batch01.csv" % (lane, lane), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        for i, (k, e) in enumerate(items, 1):
            w.writerow(["%s-VF-%05d" % (lane[:2].upper(), i), "", k, "", "", "", e.get("page_url") or "", e.get("email") or "", "",
                        "verify: %s found %s on %s but the verifier could not open the page; confirm or correct it" % (e["found_by"], e.get("email") or e.get("invoice_portal"), e.get("page_url"))])
    report["verify_tasks_" + lane] += len(items)
qa = collections.Counter()
for r in qa_rows:
    for c in ("buyer_match", "vendor_match", "title_match", "value_match", "dates_match", "status_supported"):
        qa[c + "=" + (r.get(c) or "").strip()] += 1
with open("coord/INGEST_REPORT.md", "w", encoding="utf-8") as f:
    f.write("# Ingest report — %s\n\n" % now)
    f.write("- buyers with team findings: %d (with at least one verified e-mail/portal: %d)\n" % (len(buyers), sum(1 for b in buyers.values() if any(e["verification"] == "verified" for e in b["evidence"]))))
    f.write("- vendors with team findings: %d\n- QA rows: %d\n- counters: %s\n- QA tallies: %s\n" % (len(vendors), len(qa_rows), dict(report), dict(qa)))
print(open("coord/INGEST_REPORT.md").read())

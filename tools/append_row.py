#!/usr/bin/env python3
"""Append one validated result row to a results CSV (creates it with the right header).
Usage: python3 tools/append_row.py <kind> <file.csv> '<json object>'
kind: buyer_ap | vendor_contact | qa | source_scouting
Exit 0 = row saved; exit 1 = rejected (message says why). Safe for agents: never rewrites existing rows.
"""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_returns import FORMATS, STATUS, EMAIL, PERSONAL, ROLE_HINT

kind, path, obj = sys.argv[1], sys.argv[2], sys.argv[3]
if kind not in FORMATS:
    sys.exit("kind must be one of " + ", ".join(FORMATS))
cols = FORMATS[kind].split(",")
try:
    row = json.loads(obj)
except Exception as e:
    print("REJECTED: not valid JSON (%s). Escape quotes inside values." % e); sys.exit(1)
unknown = [k for k in row if k not in cols]
if unknown:
    print("REJECTED: unknown columns %s. Allowed: %s" % (unknown, cols)); sys.exit(1)
row = {c: ("" if row.get(c) is None else str(row.get(c)).strip()) for c in cols}
errs = []
if kind in STATUS and row.get("status") not in STATUS[kind]:
    errs.append("status must be one of %s" % sorted(STATUS[kind]))
for col in ("ap_email", "general_email", "billing_or_ar_email"):
    e = row.get(col, "")
    if not e:
        continue
    if not EMAIL.match(e):
        errs.append("%s is not a single valid e-mail" % col)
    elif PERSONAL.match(e.split("@")[0]) and not ROLE_HINT.search(e.split("@")[0]):
        errs.append("%s looks like a personal mailbox; role mailboxes only" % col)
    if not row.get("evidence_url", "").startswith("http"):
        errs.append("evidence_url required with an e-mail")
    if e.lower() not in row.get("evidence_quote", "").lower():
        errs.append("evidence_quote must contain %s exactly as on the page" % e)
if row.get("invoice_portal_url") and not row["invoice_portal_url"].startswith("http"):
    errs.append("invoice_portal_url must be a full URL")
if "evidence_quote" in row and len(row["evidence_quote"]) > 300:
    row["evidence_quote"] = row["evidence_quote"][:300]
if row.get("retrieved_date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["retrieved_date"]):
    errs.append("retrieved_date must be YYYY-MM-DD")
if errs:
    print("REJECTED: " + "; ".join(errs)); sys.exit(1)
os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
new = not os.path.exists(path) or os.path.getsize(path) == 0
with open(path, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    if new:
        w.writeheader()
    w.writerow(row)
print("SAVED %s row for %s" % (kind, row.get("task_id") or row.get("qa_id") or row.get("source_name")))

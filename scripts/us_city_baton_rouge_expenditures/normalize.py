#!/usr/bin/env python3
"""Baton Rouge / East Baton Rouge Parish 'City-Parish Expenditures' (vwa8-ps2a), Canadian vendor address.
De-duplicates against normalized/us_city_baton_rouge.jsonl (POs) by PO number (read-only).
usage: python3 -I normalize.py <expenditures_ca.jsonl> <us_city_baton_rouge.jsonl> <out.jsonl>"""
import sys, json, collections
sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *
ep, prior, op = sys.argv[1:4]
prior_po = set()
for r in read_jsonl(prior):
    prior_po.add(r["record_id"].split(":", 1)[1])
SRC = {"key": "us_city_baton_rouge_expenditures", "name": "City-Parish Expenditures (Baton Rouge / East Baton Rouge Parish)",
       "publisher": "City of Baton Rouge / Parish of East Baton Rouge (data.brla.gov)", "dataset_url": "https://data.brla.gov/d/vwa8-ps2a",
       "record_url": None, "retrieved_at": "2026-10-26T03:40:59Z"}
G = collections.defaultdict(list)
for r in read_jsonl(ep):
    G[(s(r.get("vendor_name_1")), s(r.get("department_id")), s(r.get("source_document_number")) or "NODOC")].append(r)
out = Out(op)
for (vn, dept, doc), rows in G.items():
    r0 = rows[0]
    ok, basis = canadian(region=r0.get("vendor_state"), postal=r0.get("vendor_zip"), region_field="vendor_state", postal_field="vendor_zip", country_field=None)
    if not ok: out.exclude("not_canadian " + basis); continue
    if doc != "NODOC" and doc in prior_po: out.exclude("duplicate_of_us_city_baton_rouge " + doc); continue
    rows.sort(key=lambda r: r.get("check_date") or "")
    last = d(rows[-1].get("check_date")); first = d(rows[0].get("check_date"))
    st, sb = status_activity(last, "payment (check)")
    if not st: out.exclude("stale " + sb); continue
    paid = [r for r in rows if (s(r.get("payment_status")) or "").upper() not in ("VOID", "VOIDED", "CANCELLED")]
    val = round(sum(amt(r.get("invoice_line_item_amount")) or 0 for r in paid), 2)
    c = contract({"source_document_number": None if doc == "NODOC" else doc, "source_document_type": s(r0.get("source_document_type")),
                  "invoice_numbers": ";".join(sorted({s(r.get("invoice_number")) or "" for r in rows}))},
                 title=s(r0.get("source_document_description")) or s(r0.get("invoice_line_item_description")),
                 description="; ".join(sorted({s(r.get("invoice_line_item_description")) or "" for r in rows}))[:1000],
                 instrument_type="purchase order payments" if doc != "NODOC" else "direct payment (no purchase order)",
                 commodity={"brla_commodity": s(r0.get("commodity_code")), "brla_commodity_description": s(r0.get("commodity_description")),
                            "expense_category": s(r0.get("expense_category"))},
                 value=val, value_detail={"sum_invoice_line_item_amount": val, "payments": len(rows)},
                 dates={"start": first, "amended_last": last}, related={"first_payment": first, "last_payment": last})
    b = buyer(f"City of Baton Rouge / Parish of East Baton Rouge - {s(r0.get('department'))}", "city-parish department",
              identifiers={"department_id": dept, "division": s(r0.get("division")), "purchasing_department": s(r0.get("purchasing_department"))})
    v = vendor(vn, basis, line1=None, city=r0.get("vendor_city"), region=r0.get("vendor_state"), postal=r0.get("vendor_zip"))
    out.write(rec(SRC, sid(doc, vn, dept), st, sb, c, b, v, {"rows": rows, "dataset_id": "vwa8-ps2a"}))
print(json.dumps(out.close()))

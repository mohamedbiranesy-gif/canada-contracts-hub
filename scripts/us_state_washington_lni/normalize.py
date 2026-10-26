#!/usr/bin/env python3
"""WA L&I prevailing-wage Intents (t9je-9qwa) + Affidavits (9ncw-tqjn), Canadian contractor address.
usage: python3 -I normalize.py <intents.jsonl> <affidavits.jsonl> <out.jsonl>"""
import sys, json, collections, re
sys.path.insert(0, "scripts/us_discovery_sweep")
from sweeplib import *
ip, ap, op = sys.argv[1:4]
I = list(read_jsonl(ip)); A = list(read_jsonl(ap))
aff = collections.defaultdict(list)
for a in A: aff[str(a.get("intent"))].append(a)
RET = "2026-10-26T03:35:37Z"
SRC = {"key": "us_state_washington_lni", "name": "Washington State L&I prevailing wage - Intent Project Details (t9je-9qwa) with Affidavit Project Details (9ncw-tqjn)",
       "publisher": "Washington State Department of Labor & Industries (data.wa.gov)", "dataset_url": "https://data.wa.gov/d/t9je-9qwa",
       "record_url": None, "retrieved_at": RET}
def btype(n):
    u = (n or "").upper()
    for k, v in (("SCHOOL DISTRICT", "school district"), ("UNIVERSITY", "university"), ("COLLEGE", "college"), ("PORT OF", "port authority"),
                 (", PORT", "port authority"), ("PUBLIC UTILITY", "public utility district"), ("COUNTY", "county"), ("CITY OF", "city"),
                 (", CITY", "city"), ("TOWN OF", "town"), ("SOUND TRANSIT", "regional transit authority"), ("TRANSIT", "transit agency"),
                 ("HOUSING AUTHORITY", "housing authority"), ("WASH STATE", "state agency"), ("WASHINGTON STATE", "state agency"),
                 ("STATE DEPT", "state agency"), ("DEPT OF", "state agency"), ("DISTRICT", "special district")):
        if k in u: return v
    return "public body"
out = Out(op); seen = set()
for i in I:
    iid = str(i.get("intent_id"))
    if iid in seen: continue
    seen.add(iid)
    ok, basis = canadian(region=i.get("companystate"), postal=i.get("companyzip"), country=None,
                         text=" ".join(x for x in [i.get("companyaddress1"), i.get("companyaddress2"), i.get("companycity"), i.get("companystate")] if x),
                         region_field="companystate", postal_field="companyzip", country_field=None)
    if not ok: out.exclude("not_canadian " + basis); continue
    app = d(i.get("application_received_date")); start = d(i.get("expected_start_dt")); award = d(i.get("cntrct_award_dt"))
    affs = aff.get(iid, [])
    if affs:
        comp = max((d(a.get("projectcompletiondate")) or "") for a in affs) or None
        if comp and comp >= REF_S:
            status, sb = "ongoing", f"Affidavit of Wages Paid filed but its project completion date {comp} >= {REF_S}; work start {start or award}"
        else:
            out.exclude(f"ended affidavit_completion_{comp}"); continue
    else:
        if start and start > REF_S: out.exclude(f"not_started {start}"); continue
        if not app or app < STALE_S: out.exclude(f"stale intent_filed_{app}"); continue
        status = "ongoing_inferred"
        sb = (f"Intent to Pay Prevailing Wages filed {app} (expected start {start or 'n/a'}, contract award {award or 'n/a'}); no Affidavit of "
              f"Wages Paid (the closure record a contractor must file after completing its work) exists for intent {iid} in 9ncw-tqjn as of "
              f"{RET[:10]} -> work presumed in progress (no-closure-record convention, intents filed within 3 years only)")
    prime = str(i.get("primeintent") or "") == iid
    comp_amt = amt(i.get("cntrct_amt")); prime_amt = amt(i.get("amount"))
    c = contract({"intent_id": iid, "project_id": s(i.get("project_id")), "contract_number": s(i.get("contractnumber")),
                  "prime_intent_id": s(i.get("primeintent")), "prime_contractor_registration": s(i.get("prime_contractor_reg_number")),
                  "prime_ubi": s(i.get("prime_ubi_number"))},
                 title=s(i.get("contractname")), description=s(i.get("contractname")),
                 instrument_type="public works contract (prime)" if prime else f"public works subcontract (hired by {s(i.get('hiringcompanyname')) or s(i.get('prime_company_name'))})",
                 procurement_method=None, value=comp_amt,
                 value_detail={"company_contract_amount": comp_amt, "prime_contract_amount": prime_amt},
                 dates={"published": app, "signed": award, "start": start or award, "end": None},
                 related={"prime_contractor": s(i.get("prime_company_name")), "hiring_company": s(i.get("hiringcompanyname")),
                          "bid_due_date": d(i.get("bid_due_date")), "project_location": s(i.get("projectlocation")),
                          "affidavits": [s(a.get("id")) for a in affs]})
    b = buyer(s(i.get("agencyname")), btype(i.get("agencyname")),
              address={"full": s(i.get("awarding_agency_address")), "region": "WA", "country": "US"},
              contact={"phone": s(i.get("agencyphone"))})
    v = vendor(i.get("companyname"), basis, identifiers={"wa_ubi": s(i.get("ubi")), "wa_lni_contractor_registration": s(i.get("license"))},
               line1=i.get("companyaddress1"), line2=i.get("companyaddress2"), city=i.get("companycity"), region=i.get("companystate"),
               postal=i.get("companyzip"), country="CA", contact={"phone": s(i.get("phone"))})
    raw = {"intent": i, "affidavits": affs, "dataset_ids": ["t9je-9qwa", "9ncw-tqjn"]}
    out.write(rec(SRC, sid(iid), status, sb, c, b, v, raw))
print(json.dumps(out.close()))

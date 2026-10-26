"""Build normalized sec_edgar records from curated facts + docs_index."""
import json, re, sys, os, datetime
TODAY = datetime.date(2026,10,25)
OUT = "normalized/sec_edgar.jsonl"
idx = {json.loads(l)["_id"]: json.loads(l) for l in open("downloads/sec_edgar/docs_index.jsonl")}
hits = {json.loads(l)["_id"]: json.loads(l) for l in open("downloads/sec_edgar/hits.jsonl")}
existing=set()
if os.path.exists(OUT):
    for l in open(OUT): existing.add(json.loads(l)["record_id"])
def add_years(d, y):
    try: return d.replace(year=d.year+int(y))
    except ValueError: return d.replace(year=d.year+int(y), day=28)
def status_for(c, filed):
    start = c.get("start") or c.get("signed"); end = c.get("end"); dur = c.get("duration_years")
    sd = datetime.date.fromisoformat(start) if start else datetime.date.fromisoformat(filed)
    if end:
        ed = datetime.date.fromisoformat(end)
        if ed >= TODAY: return "ongoing", f"Exhibit states term end {end} (contract.dates.end) >= 2026-10-25; effective/signed {sd.isoformat()} <= 2026-10-25."
        return "expired", f"Stated end {end} < 2026-10-25."
    if dur:
        ed = add_years(sd, dur)
        if ed >= TODAY: return "ongoing_inferred", f"No fixed end date; exhibit states {dur}-year initial term. {sd.isoformat()} + {dur} years = {ed.isoformat()} >= 2026-10-25."
        return "expired", f"{sd.isoformat()} + {dur}y = {ed.isoformat()} < 2026-10-25."
    if c.get("term"):
        return "ongoing_inferred", f"No fixed end date; exhibit term clause: {c['term'][:160]} (evergreen/condition-based term, agreement in force as of filing {filed})."
    return "end_date_unknown", f"Exhibit filed {filed}; no usable term/end date extracted."
cur = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
out = open(OUT, "a", encoding="utf-8"); n=0; counts={}
for c in cur:
    if c.get("subject")=="skip": continue
    d = idx[c["_id"]]; h = hits.get(c["_id"], {}); s = h.get("_source", {})
    adsh = d["adsh"]; ex = c.get("exhibit") or d["file_type"]
    rid = f"sec_edgar:{adsh}:{ex}"
    if rid in existing: continue
    st, basis = status_for(c, d["file_date"])
    if st=="expired": print("expired skip", rid); continue
    v = c["vendor"]
    rec = {
      "record_id": rid,
      "source": {"key":"sec_edgar","name":"SEC EDGAR full-text search (material contracts / 8-K Item 1.01) - Canadian-located filers","publisher":"U.S. Securities and Exchange Commission",
                 "dataset_url":"https://efts.sec.gov/LATEST/search-index?q=%22agreement%22&dateRange=custom&startdt=2024-01-01&enddt=2026-10-25&locationCodes=A0,A1,A5,A6,A8,Z4",
                 "record_url": d["url"], "retrieved_at": d["retrieved_at"]},
      "status": st, "status_basis": basis,
      "contract": {"identifiers": {"accession_number": adsh, "exhibit": ex, "filer_cik": d["cik"], **(c.get("identifiers") or {})},
        "title": c.get("title") or d.get("file_description") or ex, "description": c.get("subject"),
        "instrument_type": c.get("instrument_type") or "contract", "procurement_method": None, "solicitation_procedure": None, "commodity": {},
        "value": c.get("value"), "currency": c.get("currency"), "value_detail": c.get("value_detail") or {},
        "dates": {"published": d["file_date"], "signed": c.get("signed"), "start": c.get("start"), "end": c.get("end"), "amended_last": None, "term_stated": c.get("term")},
        "related": {"filing_index_url": d["index_url"], "form": d["form"], **(c.get("related") or {})}},
      "buyer": {"name": c["buyer"]["name"], "country": c["buyer"].get("country"), "type": c["buyer"].get("type"), "identifiers": {}, "address": {}, "contact": {}},
      "vendor": {"name": v["name"], "country":"CA", "country_basis": v.get("country_basis") or f"EDGAR filer principal executive office location {s.get('biz_locations')} (biz_states {s.get('biz_states')}; locationCodes filter A0/A1/A5/A6/A8/Z4)",
                 "identifiers": {k:val for k,val in {"cik": d["cik"], "ticker": v.get("ticker"), "parent": v.get("parent")}.items() if val},
                 "address": {"line1": None, "city": v.get("city"), "region": v.get("region"), "postal_code": None, "country":"CA"}, "contact": {}},
      "raw": {"efts_hit": s, "efts_query_label": d.get("query"), "docs_index_row": {k:d[k] for k in ("kind","form","file_type","file_description","file_date","period_ending","items","biz_locations","biz_states","display_name","chars","file")},
              "evidence_snippet": c.get("evidence"), "curation_notes": c.get("notes"), "options": c.get("options"), "duration_years": c.get("duration_years"), "local_text_file": f"downloads/sec_edgar/docs/{d['file']}"}
    }
    out.write(json.dumps(rec, ensure_ascii=False)+"\n"); n+=1; counts[st]=counts.get(st,0)+1
print("wrote", n, counts)

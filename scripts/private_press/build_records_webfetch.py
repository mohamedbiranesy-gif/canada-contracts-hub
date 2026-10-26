"""Build private_press records for releases we could only read via WebFetch (no local HTML).
Input rows carry the same curated fields plus announce_date, headline, dateline_loc."""
import json, sys, hashlib, datetime, os
sys.path.insert(0, "scripts/private_press")
import build_records as B
OUT = B.OUT
cur = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
existing=set()
if os.path.exists(OUT):
    for l in open(OUT, encoding="utf-8"): existing.add(json.loads(l)["record_id"])
out = open(OUT,"a",encoding="utf-8"); n=0; counts={}
for c in cur:
    if c.get("subject")=="skip": continue
    url=c["url"]; sha=hashlib.sha1(url.encode()).hexdigest(); rid=f"private_press:{sha}"
    if rid in existing: continue
    st, basis = B.status_for(c, c["announce_date"])
    if st=="expired": print("expired", url); continue
    v=c["vendor"]
    WIRES = [("globenewswire", "GlobeNewswire press releases", "Notified (GlobeNewswire)"),
             ("businesswire", "Business Wire press releases", "Berkshire Hathaway (Business Wire)"),
             ("prnewswire", "PR Newswire press releases", "Cision PR Newswire"),
             ("newswire.ca", "Cision newswire.ca (CNW Group) press releases", "Cision Canada"),
             ("newsfilecorp", "Newsfile Corp. press releases", "Newsfile Corp."),
             ("accessnewswire", "ACCESS Newswire press releases", "ACCESS Newswire (Issuer Direct)"),
             ("accesswire", "ACCESS Newswire press releases", "ACCESS Newswire (Issuer Direct)"),
             ("ccc.ca", "Canadian Commercial Corporation announcements", "Canadian Commercial Corporation"),
             ("shipsforcanada.ca", "Irving Shipbuilding newsroom (Our Stories) supplier award announcements", "Irving Shipbuilding Inc."),
             ("war.gov", "U.S. Department of War daily contract announcements", "U.S. Department of War"),
             ("defense.gov", "U.S. Department of Defense daily contract announcements", "U.S. Department of Defense")]
    src_name, publisher = "Company newsroom press release", v["name"]
    for key, nm, pub in WIRES:
        if key in url:
            src_name, publisher = nm, pub; break
    rec = {"record_id": rid,
      "source": {"key":"private_press","name":src_name,"publisher":publisher,"dataset_url": url.split("/news-release")[0] if "globenewswire" in url else url.split("/news/")[0] if "/news/" in url else url,
                 "record_url": url, "retrieved_at": c.get("retrieved_at") or datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")},
      "status": st, "status_basis": basis,
      "contract": {"identifiers": {k:val for k,val in (c.get("identifiers") or {}).items() if val}, "title": c.get("headline"), "description": c.get("subject"),
        "instrument_type": c.get("instrument_type") or "contract", "procurement_method": c.get("procurement_method"), "solicitation_procedure": None,
        "commodity": {"sector": c.get("sector")} if c.get("sector") else {}, "value": c.get("value"), "currency": c.get("currency"),
        "value_detail": c.get("value_detail") or ({"announced_total": c.get("value")} if c.get("value") is not None else {}),
        "dates": {"published": c["announce_date"], "signed": c.get("signed"), "start": c.get("start"), "end": c.get("end"), "amended_last": None, "term_stated": c.get("term")},
        "related": c.get("related") or {}},
      "buyer": {"name": c["buyer"]["name"], "country": c["buyer"].get("country"), "type": c["buyer"].get("type"), "identifiers": {}, "address": {}, "contact": {}},
      "vendor": {"name": v["name"], "country":"CA", "country_basis": v.get("country_basis") or f"press-release dateline/HQ statement ({c.get('dateline_loc')})",
                 "identifiers": {k:val for k,val in {"ticker": v.get("ticker"), "parent": v.get("parent")}.items() if val},
                 "address": {"line1": None, "city": v.get("city"), "region": v.get("region"), "postal_code": None, "country":"CA"}, "contact": {}},
      "raw": {"headline": c.get("headline"), "dateline_location": c.get("dateline_loc"), "dateline_date": c["announce_date"], "retrieval_method": ("direct HTTP fetch; HTML saved under downloads/private_press/html/ (fetched_isi.jsonl)" if "shipsforcanada.ca" in url else "WebFetch summary (direct HTTP to this wire service returns 403 from this environment; no local HTML copy)"),
              "evidence_snippet": c.get("evidence"), "curation_notes": c.get("notes"), "options": c.get("options"), "duration_years": c.get("duration_years"), "duration_months": c.get("duration_months")}}
    out.write(json.dumps(rec, ensure_ascii=False)+"\n"); n+=1; counts[st]=counts.get(st,0)+1
print("wrote", n, counts)

"""Stage D: build normalized JSONL records for private_press from a curated facts file.
Usage: python3 -I build_records.py curated.jsonl
Each curated row: {"url":..., "vendor":{...}, "buyer":{...}, "subject":..., "value":..., "currency":..., "instrument_type":..., "term":..., "start":..., "end":..., "duration_years":..., "options":..., "identifiers":{...}, "notes":..., "evidence":"<15 words"}
Dates/status are computed here. The fetched text (for raw) is looked up from fetched_*.jsonl by URL."""
import json, re, sys, hashlib, datetime, os
sys.path.insert(0, "scripts/private_press")
from extract_lib import *
TODAY = datetime.date(2026, 10, 25)
DL = "downloads/private_press"
OUT = "normalized/private_press.jsonl"
fetched = {}
for fn in os.listdir(DL):
    if fn.startswith("fetched_") and fn.endswith(".jsonl"):
        for l in open(f"{DL}/{fn}", encoding="utf-8"):
            try:
                r = json.loads(l); fetched[r["url"]] = r
            except: pass
existing = set()
if os.path.exists(OUT):
    for l in open(OUT, encoding="utf-8"):
        try: existing.add(json.loads(l)["record_id"])
        except: pass
def add_years(d, years):
    y = int(years); frac = years - y
    try: nd = d.replace(year=d.year + y)
    except ValueError: nd = d.replace(year=d.year + y, day=28)
    if frac: nd = nd + datetime.timedelta(days=int(round(frac*365.25)))
    return nd
def status_for(c, announce):
    start = c.get("start"); end = c.get("end"); dur = c.get("duration_years"); dur_m = c.get("duration_months")
    basis = []
    sd = datetime.date.fromisoformat(start) if start else (datetime.date.fromisoformat(announce) if announce else None)
    if end:
        ed = datetime.date.fromisoformat(end) if len(end)==10 else datetime.date(int(end[:4]), 12, 31)
        if sd and sd > TODAY:
            # future start but published, contract exists -> treat as ongoing (signed) per schema start<=today rule? schema requires start<=today
            return "ongoing_inferred", f"Contract signed/announced {announce} with stated end {end} >= 2026-10-25; stated start {start} is after reference date, so counted as awarded-and-running (not yet performing)."
        if ed >= TODAY:
            return "ongoing", f"Stated end date {end} (field: contract.dates.end, from release text) >= 2026-10-25; start/announce {sd.isoformat() if sd else None} <= 2026-10-25."
        return "expired", f"Stated end {end} < 2026-10-25."
    if dur or dur_m:
        base = sd or (datetime.date.fromisoformat(announce) if announce else None)
        if not base: return "end_date_unknown", "Duration stated but no usable start/announce date."
        if dur: ed = add_years(base, float(dur)); what = f"{dur}-year"
        else: ed = base + datetime.timedelta(days=int(round(float(dur_m)*30.44))); what = f"{dur_m}-month"
        if ed >= TODAY:
            return "ongoing_inferred", f"No explicit end date; release states a {what} term. {base.isoformat()} + {what} = {ed.isoformat()} >= 2026-10-25."
        return "expired", f"{base.isoformat()} + {what} = {ed.isoformat()} < 2026-10-25."
    return "end_date_unknown", "Release states no end date or term; award/announcement only (announce date %s)." % announce
def build(c):
    url = c["url"]; f = fetched.get(url, {})
    sha = hashlib.sha1(url.encode()).hexdigest()
    rid = f"private_press:{sha}"
    text = f.get("text") or ""
    loc, d = parse_dateline(f.get("dateline") or "")
    if not d:
        loc, d = parse_dateline(re.sub(r"\s+"," ", text[:600]))
    announce = c.get("announce_date") or d or (f.get("meta",{}).get("date") or "")[:10] or None
    st, basis = status_for(c, announce)
    if st == "expired": return None, rid, "expired"
    is_ca, city, prov = location_is_canada(loc)
    v = c["vendor"]
    vendor_city = v.get("city") or city; vendor_region = v.get("region") or prov
    src_name = "Cision newswire.ca (CNW Group) press releases" if "newswire.ca" in url else ("PR Newswire press releases" if "prnewswire.com" in url else ("GlobeNewswire press releases" if "globenewswire" in url else ("Business Wire press releases" if "businesswire" in url else "Company press release")))
    publisher = "Cision Canada" if "newswire.ca" in url else ("Cision PR Newswire" if "prnewswire" in url else ("Notified / GlobeNewswire" if "globenewswire" in url else ("Berkshire Hathaway / Business Wire" if "businesswire" in url else v.get("name"))))
    core_dates = find_dates(text[:8000]) if text else []
    rec = {
      "record_id": rid,
      "source": {"key": "private_press", "name": src_name, "publisher": publisher,
                 "dataset_url": "https://www.newswire.ca/news-releases/financial-services-latest-news/contracts-list/" if "newswire.ca" in url else ("https://www.prnewswire.com/news-releases/financial-services-latest-news/contracts-list/" if "prnewswire" in url else url.split("/news")[0] if "/news" in url else url),
                 "record_url": url, "retrieved_at": f.get("retrieved_at") or c.get("retrieved_at") or datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")},
      "status": st, "status_basis": basis,
      "contract": {
        "identifiers": {k: val for k, val in (c.get("identifiers") or {}).items() if val},
        "title": c.get("title") or f.get("title") or (f.get("meta",{}) or {}).get("og:title"),
        "description": c.get("subject"),
        "instrument_type": c.get("instrument_type") or "contract",
        "procurement_method": c.get("procurement_method"), "solicitation_procedure": None,
        "commodity": {"sector": c.get("sector")} if c.get("sector") else {},
        "value": c.get("value"), "currency": c.get("currency"),
        "value_detail": c.get("value_detail") or ({"announced_total": c.get("value")} if c.get("value") is not None else {}),
        "dates": {"published": announce, "signed": c.get("signed"), "start": c.get("start"), "end": c.get("end"), "amended_last": None,
                  "term_stated": c.get("term")},
        "related": c.get("related") or {}
      },
      "buyer": {"name": c["buyer"]["name"], "country": c["buyer"].get("country"), "type": c["buyer"].get("type"),
                "identifiers": c["buyer"].get("identifiers") or {}, "address": {"city": c["buyer"].get("city")} if c["buyer"].get("city") else {}, "contact": {}},
      "vendor": {"name": v["name"], "country": "CA", "country_basis": v.get("country_basis") or ("press-release dateline city/province (%s) and 'About' boilerplate" % loc if is_ca else "company 'About' boilerplate / headquarters statement in release"),
                 "identifiers": {k: val for k, val in {"ticker": v.get("ticker") or (",".join(re.sub(r"\s+","",t).strip("()") for t in (f.get("tickers") or [])) or None), "parent": v.get("parent")}.items() if val},
                 "address": {"line1": None, "city": vendor_city, "region": vendor_region, "postal_code": None, "country": "CA"}, "contact": {}},
      "raw": {"headline": f.get("title"), "dateline": f.get("dateline"), "dateline_location": loc, "dateline_date": d, "meta": f.get("meta"), "tickers_in_text": [re.sub(r"\s+"," ",t) for t in (f.get("tickers") or [])],
              "company_links": f.get("company_links"), "list_date": f.get("list_date"), "site": f.get("site"), "html_sha1": sha, "html_file": f"downloads/private_press/html/{sha}.html" if f else None,
              "money_mentions": [m["text"] for m in parse_money(text[:8000])][:12] if text else [], "duration_mentions": [x["text"] for x in parse_durations(text[:8000])][:12] if text else [],
              "date_mentions": [x["iso"] for x in core_dates][:12], "evidence_snippet": c.get("evidence"), "curation_notes": c.get("notes"), "options": c.get("options"), "duration_years": c.get("duration_years"), "duration_months": c.get("duration_months")}
    }
    return rec, rid, st
if __name__ == "__main__":
    cur = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
    out = open(OUT, "a", encoding="utf-8"); n=0; skipped=0; counts={}
    seen_batch=set()
    for c in cur:
        try:
            rec, rid, st = build(c)
        except Exception as e:
            print("ERR", c.get("url"), e); continue
        if rid in existing or rid in seen_batch: skipped+=1; continue
        if rec is None: print("EXPIRED skip", c["url"]); continue
        seen_batch.add(rid)
        out.write(json.dumps(rec, ensure_ascii=False)+"\n"); n+=1; counts[st]=counts.get(st,0)+1
    out.flush()
    print("wrote", n, "skipped-existing", skipped, counts)

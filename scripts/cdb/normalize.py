#!/usr/bin/env python3
import json, re, collections, os, datetime
from dateutil import parser as dparser
REF = datetime.date(2026, 10, 25)
def doc_terms(url):
    if not url: return None
    fn = "downloads/cdb/docs/" + re.sub(r"[^A-Za-z0-9_.-]", "_", url.split("/")[-1])[:120] + ".txt"
    if not os.path.exists(fn): return None
    t = re.sub(r"[ \t]+", " ", open(fn).read())
    mc = re.search(r"Commencement Date of Contract\s*:?-?\s*(.+)", t, re.I); md = re.search(r"Duration of\s+Contract\s*:?-?\s*(.+)", t, re.I)
    if not mc or not md: return {"doc_text_file": fn}
    cs = re.sub(r"\s+", " ", mc.group(1)).strip(); ds = re.sub(r"\s+", " ", md.group(1)).strip()
    try:
        c = dparser.parse(re.sub(r"(?i)in accordance with.*?on or before", "", cs).replace(" ,", ","), fuzzy=True, default=datetime.datetime(2000, 1, 1)).date()
    except Exception: c = None
    dsn = re.sub(r"\s+", "", ds)
    n = re.search(r"\((\d+)\)", dsn) or re.search(r"(\d+)", dsn)
    u = re.search(r"(day|week|month|year)", dsn, re.I)
    end = None
    if c and n and u:
        k = int(n.group(1)); uu = u.group(1).lower()
        if uu == "day": end = c + datetime.timedelta(days=k)
        elif uu == "week": end = c + datetime.timedelta(weeks=k)
        elif uu == "month":
            mm = c.month - 1 + k; y2, m2 = c.year + mm // 12, mm % 12 + 1; import calendar; end = datetime.date(y2, m2, min(c.day, calendar.monthrange(y2, m2)[1]))
        else: end = datetime.date(c.year + k, c.month, min(c.day, 28))
    return {"doc_text_file": fn, "commencement_text": cs, "duration_text": ds, "commencement": c, "end_computed": end}
R = json.load(open("downloads/cdb/rows.json"))
can = [r for r in R if re.match(r"\s*Canada\s*-", r["winning_bid"], re.I)]
groups = collections.OrderedDict()
def amt(s):
    m = re.search(r"(USD|US\$|BSD|EUR|XCD|BBD)\s*([\d,\s]+(?:\.\s*\d+)?)", s)
    if not m: return None, None
    cur = {"US$": "USD"}.get(m.group(1), m.group(1))
    try: return float(re.sub(r"[,\s]", "", m.group(2))), cur
    except ValueError: return None, cur
for r in can:
    parts = [p.strip() for p in r["winning_bid"].split("|")]
    vendor = re.sub(r"^\s*Canada\s*-\s*", "", parts[0], flags=re.I).strip()
    value, cur = amt(r["winning_bid"])
    key = (re.sub(r"\W", "", vendor.lower())[:12], value)
    groups.setdefault(key, []).append((r, vendor, value, cur))
out = open("normalized/cdb.jsonl", "w", encoding="utf-8"); excluded = []
n = 0
for key, lst in groups.items():
    lst.sort(key=lambda x: -x[0]["year_filter"])
    r, vendor, value, cur = lst[0]
    corp = r["country"] in ("CDB", "Regional") or r["type"] == "Corporate"
    buyer = {"name": "Caribbean Development Bank", "country": "BB", "type": "IGO (regional development bank)"} if corp else \
            {"name": "Government of %s – executing agency of CDB-financed project '%s'" % (r["country"], r["project_name"].strip()), "country": None, "type": "borrower government / executing agency (CDB-financed project); agency named in the linked award notice"}
    dt = doc_terms(r["document_url"])
    status, sbasis, start, endc = "end_date_unknown", "CDB listing gives project, country, type, winning bid and amount, filed under award year %d; no contract dates or duration in the listing" % r["year_filter"], None, None
    if dt and dt.get("end_computed"):
        start, endc = dt["commencement"], dt["end_computed"]
        if endc < REF:
            excluded.append((r["project_name"], vendor, str(start), dt["duration_text"], str(endc))); continue
        status = "ongoing_inferred"; sbasis = "award notice: 'Commencement Date of Contract: %s' + 'Duration of Contract: %s' = %s → %s (contains 2026-10-25)" % (dt["commencement_text"], dt["duration_text"], start, endc)
    rid = "cdb:%d:%s" % (r["year_filter"], re.sub(r"\W+", "_", (r["document_url"] or r["project_name"]).split("/")[-1])[:70])
    rec = {"record_id": rid,
      "source": {"key": "cdb", "name": "Caribbean Development Bank – Contract Awards listing", "publisher": "Caribbean Development Bank (CDB)", "dataset_url": "https://www.caribank.org/work-with-us/procurement/contract-awards",
                 "record_url": r["document_url"], "retrieved_at": "2026-10-25T19:34:00Z"},
      "status": status, "status_basis": sbasis,
      "contract": {"identifiers": {"award_notice_document": r["document_url"]}, "title": r["project_name"], "description": r["project_name"], "instrument_type": "contract award (%s)" % r["type"],
                   "procurement_method": None, "solicitation_procedure": None, "commodity": {"cdb_sector_theme": r["sectors_themes"] or None, "cdb_type": r["type"]},
                   "value": value, "currency": cur, "value_detail": {"winning_bid_text": r["winning_bid"]}, "dates": {"published": None, "signed": None, "award_year_listing": r["year_filter"], "start": start.isoformat() if start else None, "end": endc.isoformat() if endc else None, "amended_last": None},
                   "related": {"award_notice_terms": {k: str(v) for k, v in (dt or {}).items()}, "listing_url": r["listing_url"], "beneficiary_country": r["country"]}},
      "buyer": {**buyer, "identifiers": {}, "address": {}, "contact": {}},
      "vendor": {"name": vendor, "country": "CA", "country_basis": "'Winning Bid' field is published as '<bidder country> - <firm>' and reads 'Canada - …'", "identifiers": {}, "address": {"country": "Canada"}, "contact": {}},
      "raw": {**r, "rows": [x[0] for x in lst] if len(lst) > 1 else []}}
    out.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
json.dump(excluded, open("downloads/cdb/excluded_ended.json", "w"), ensure_ascii=False, indent=0)
print(len(can), n, "excluded ended", len(excluded)); [print("  ", e) for e in excluded]

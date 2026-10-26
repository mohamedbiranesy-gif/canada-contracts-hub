#!/usr/bin/env python3
"""simap.ch award publications with a Canadian vendor -> schema records. For each match the referenced tender
publication (referencingPub) is fetched once to look for a contract period/duration."""
import json, urllib.request, time, datetime, re, os, collections
REF = datetime.date(2026, 10, 25)
UA = {"User-Agent": "contracts-research/1.0", "Accept": "application/json"}
dl = "downloads/ch_simap"
API = "https://www.simap.ch/api/publications"
cache = dl + "/ref_cache"; os.makedirs(cache, exist_ok=True)
def get(url, fn):
    if os.path.exists(fn): return json.load(open(fn))
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); json.dump(d, open(fn, "w")); time.sleep(0.4); return d
    except Exception as e:
        return {"_error": str(e)}
def ml(x):
    if isinstance(x, dict): return x.get("en") or x.get("de") or x.get("fr") or x.get("it")
    return x
def walk(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, p + "." + k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, p + "[%d]" % i)
    else: yield p, o
def d8(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(s or "")); return datetime.date(*map(int, m.groups())) if m else None
out = open("normalized/ch_simap.jsonl.tmp", "w", encoding="utf-8"); st = collections.Counter(); seen = set()
for l in open(dl + "/matches.jsonl"):
    m = json.loads(l); sr = m["search_row"]; det = m["details"]
    if sr["publicationId"] in seen: continue
    seen.add(sr["publicationId"])
    ref = det.get("referencingPub") or {}
    tender = get(API + "/v1/project/%s/publication-details/%s" % (sr["id"], ref.get("publicationId")), cache + "/%s.json" % ref.get("publicationId")) if ref.get("publicationId") else {}
    # contract period candidates from the tender publication
    per = {p: v for p, v in walk(tender) if v is not None and re.search(r"(contract|execution|delivery|service).*(period|duration|start|end|deadline)|(period|duration)\.", p, re.I)}
    start = end = None; dur = None
    for p, v in per.items():
        pl = p.lower()
        if pl.endswith(("periodfrom", ".start", ".startdate", ".from")) and d8(v): start = start or d8(v)
        if pl.endswith(("periodto", ".end", ".enddate", ".to", ".until")) and d8(v): end = end or d8(v)
    dec = det.get("decision") or {}
    vendors = [v for v in dec.get("vendors") or [] if ((v.get("vendorAddress") or {}).get("countryId") or "").upper() == "CA"]
    award = d8(dec.get("awardDecisionDate")); pub = d8((det.get("base") or {}).get("publicationDate")) or d8(sr.get("publicationDate"))
    for v in vendors:
        anchor = start or award or pub
        if end and end < REF: st["excluded_ended"] += 1; continue
        if anchor and anchor > REF: st["excluded_future"] += 1; continue
        if end: status, basis = "ongoing", "tender publication contract period %s → %s contains 2026-10-25" % (start, end)
        else: status, basis = "end_date_unknown", "award notice gives award decision date %s only; referenced tender publication %s gives no machine-readable contract end (period fields found: %s)" % (award, ref.get("publicationNumber") or ref.get("publicationId"), list(per.items())[:4])
        st[status] += 1
        va = v.get("vendorAddress") or {}; pi = det.get("project-info") or {}; po = pi.get("procOfficeAddress") or {}
        price = v.get("price") or {}
        rec = {"record_id": "ch_simap:%s:%s" % (sr["publicationNumber"], re.sub(r"\W+", "_", v.get("vendorName") or "")[:30]),
          "source": {"key": "ch_simap", "name": "simap.ch – Swiss public procurement platform, award publications (public API)", "publisher": "Verein simap.ch (Confederation, cantons and communes)",
                     "dataset_url": "https://www.simap.ch/ (API https://www.simap.ch/api/publications/v2/project/project-search ; spec https://www.simap.ch/api/specifications/simap.yaml)",
                     "record_url": "https://www.simap.ch/en/project-detail/%s#%s" % (sr["id"], sr["publicationId"]), "retrieved_at": m["retrieved_at"]},
          "status": status, "status_basis": basis,
          "contract": {"identifiers": {"project_id": sr["id"], "project_number": sr["projectNumber"], "publication_id": sr["publicationId"], "publication_number": sr["publicationNumber"], "tender_publication_id": ref.get("publicationId"), "vendor_id": v.get("vendorId")},
            "title": ml(sr.get("title")), "description": re.sub(r"<[^>]+>", " ", ml((det.get("procurement") or {}).get("orderDescription")) or "").strip() or None,
            "instrument_type": "contract award (%s / %s)" % (sr.get("projectType"), sr.get("projectSubType")), "procurement_method": sr.get("processType"), "solicitation_procedure": sr.get("processType"),
            "commodity": {"cpv": ((det.get("procurement") or {}).get("cpvCode") or {}).get("code"), "cpv_description": ml((((det.get("procurement") or {}).get("cpvCode") or {}).get("label")))},
            "value": price.get("price"), "currency": (price.get("currency") or "").upper() or None, "value_detail": {"vendor_price": price.get("price"), "vat_type": price.get("vatType"), "number_of_submissions": dec.get("numberOfSubmissions")},
            "dates": {"published": pub.isoformat() if pub else None, "signed": None, "award": award.isoformat() if award else None, "start": start.isoformat() if start else None, "end": end.isoformat() if end else None, "amended_last": None},
            "related": {"tender_publication": ref, "ted": det.get("ted")}},
          "buyer": {"name": ml(po.get("name")) or ml(sr.get("procOfficeName")), "country": "CH", "type": "Swiss contracting authority (procurement office)", "identifiers": {"proc_office_id": po.get("id")},
                    "address": {"line1": ml(po.get("street")), "city": ml(po.get("city")), "postal_code": po.get("postalCode"), "region": po.get("cantonId"), "country": po.get("countryId")}, "contact": {"phone": po.get("phone"), "email": po.get("email")}},
          "vendor": {"name": v.get("vendorName"), "country": "CA", "country_basis": "decision.vendors[].vendorAddress.countryId = 'CA'", "identifiers": {"simap_vendor_id": v.get("vendorId")},
                     "address": {"line1": va.get("street"), "city": va.get("city"), "region": None, "postal_code": va.get("postalCode"), "country": "CA"}, "contact": {}},
          "raw": {"search_row": sr, "award_publication_details": det, "tender_publication_details": tender}}
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
json.dump(st, open(dl + "/normalize_stats.json", "w")); print(dict(st))
out.close(); os.replace("normalized/ch_simap.jsonl.tmp", "normalized/ch_simap.jsonl")

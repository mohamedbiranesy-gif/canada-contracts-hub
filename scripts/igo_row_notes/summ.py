import json, sys, collections
for f in sys.argv[1:]:
    recs = [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
    st = collections.Counter(r["status"] for r in recs)
    cb = collections.Counter((r["vendor"].get("country_basis") or "")[:90] for r in recs)
    by = collections.Counter(r["buyer"].get("name") for r in recs)
    print("=====", f, len(recs), dict(st))
    print(" basis:", cb.most_common(5))
    print(" buyers:", by.most_common(6))
    print(" retrieved:", collections.Counter(r["source"].get("retrieved_at") for r in recs).most_common(3))
    print(" rec_url ex:", [r["source"].get("record_url") for r in recs[:2]])
    ends = collections.Counter((r["contract"]["dates"].get("end") or "none")[:4] for r in recs); print(" end years:", dict(ends))
    for r in recs[:5]:
        c = r["contract"]; d = c["dates"]
        print("  -", r["record_id"], "|", r["vendor"]["name"], "(", (r["vendor"].get("address") or {}).get("city"), ")|", r["buyer"]["name"], "|", (c.get("title") or "")[:70], "|", c.get("currency"), c.get("value"), "|", d.get("start") or d.get("signed") or d.get("award"), "->", d.get("end"), "|", r["status"], "|", r["source"].get("record_url"))

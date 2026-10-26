import json, sys, collections
for p in sys.argv[1:]:
    recs = [json.loads(l) for l in open(p)]
    st = collections.Counter(r["status"] for r in recs)
    vend = collections.Counter(r["vendor"]["name"] for r in recs)
    buy = collections.Counter(r["buyer"]["name"] for r in recs)
    tot = sum(r["contract"]["value"] or 0 for r in recs)
    print("==", p, len(recs), dict(st), "sum value", round(tot, 2))
    print("  top vendors:", vend.most_common(8))
    print("  top buyers:", buy.most_common(6))
    step = max(1, len(recs) // 5)
    for r in recs[::step][:5]:
        a = r["vendor"]["address"]
        print(f"  - `{r['record_id']}` | {r['vendor']['name']} ({a.get('city')}, {a.get('region')} {a.get('postal_code') or ''}) | {r['buyer']['name']} | {(r['contract']['title'] or '')[:70]} | USD {r['contract']['value']} | {r['contract']['dates'].get('start')}→{r['contract']['dates'].get('end')} | {r['status']}")

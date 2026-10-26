import json, sys, collections
for p in sys.argv[1:]:
    c = collections.Counter()
    try:
        for l in open(p):
            try:
                c[json.loads(l)["status"]] += 1
            except Exception:
                c["_bad"] += 1
    except FileNotFoundError:
        print(p, "missing"); continue
    print(p.split("/")[-1], sum(c.values()), dict(c))

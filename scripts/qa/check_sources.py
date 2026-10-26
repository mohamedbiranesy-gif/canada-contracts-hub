import sys, os, json, collections
d = sys.argv[1]; since = float(sys.argv[2])
for fn in sorted(os.listdir(d)):
    p = os.path.join(d, fn)
    if not fn.endswith('.jsonl') or os.path.getmtime(p) < since:
        continue
    n = bad = 0; st = collections.Counter(); vc = collections.Counter(); nourl = nobuyer = noraw = 0
    with open(p, encoding='utf-8', errors='replace') as f:
        for line in f:
            if not line.strip(): continue
            try: r = json.loads(line)
            except Exception: bad += 1; continue
            n += 1; st[r.get('status')] += 1; vc[(r.get('vendor') or {}).get('country')] += 1
            if not (r.get('source') or {}).get('record_url'): nourl += 1
            if not (r.get('buyer') or {}).get('name'): nobuyer += 1
            if not r.get('raw'): noraw += 1
    print(f"{fn[:-6]:42s} n={n:6d} bad={bad} status={dict(st)} vcountry={dict(vc.most_common(3))} no_url={nourl} no_buyer={nobuyer} no_raw={noraw}")

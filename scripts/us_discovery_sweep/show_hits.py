import json, re, sys
prior = {l.split('\t')[0]: l.split('\t')[1].strip() for l in open(sys.argv[2])}
FP = re.compile(r"LA CANADA|CANADA ST|CANADA AVE|CANADA RD|CANADA RAOD|CANADA WAY|CANADA DR|CANADAIGUA|CANADA BLVD|CANADA LN|CANADA CT|CANADA GOOSE|CANADAWAY|CANADA HOLLOW|TRANS.CANADA|CANADA TRUST|CANADAY|LITTLE CANADA|BOCA CANADA|CANADA HILL|CANADA RIDGE", re.I)
skip = int(sys.argv[3]) if len(sys.argv) > 3 else 0
for i, l in enumerate(open(sys.argv[1])):
    if i < skip: continue
    j = json.loads(l)
    if j['total_hits'] == 0: continue
    good = []
    for c in j['cols']:
        vals = [(v, n) for v, n in (c.get('values') or []) if v and not FP.search(str(v))]
        if vals: good.append((c['col'], c['kind'], sum(n for _, n in vals), vals[:5]))
    if not good: continue
    tag = 'PRIOR:' + prior[j['id']] if j['id'] in prior else ''
    print(j['domain'], j['id'], (j['name'] or '')[:55], tag, '|', str(good)[:400])

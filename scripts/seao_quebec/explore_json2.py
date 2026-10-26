import sys, json, collections, ijson, decimal
class E(json.JSONEncoder):
    def default(self,o):
        if isinstance(o, decimal.Decimal): return float(o)
        return super().default(o)
path = sys.argv[1]
shown=collections.Counter()
rel_per_ocid=collections.Counter()
contract_counts={}
shrink=0; grow=0; same=0
with open(path,'rb') as f:
    for rel in ijson.items(f, 'releases.item'):
        oc=rel['ocid']; rel_per_ocid[oc]+=1
        nc=len(rel.get('contracts') or [])
        if oc in contract_counts:
            if nc<contract_counts[oc]: shrink+=1
            elif nc>contract_counts[oc]: grow+=1
            else: same+=1
        contract_counts[oc]=nc
        cs=rel.get('contracts') or []
        if any(c.get('amendments') for c in cs) and shown['amend']<1:
            shown['amend']+=1; print('=== AMENDMENTS', json.dumps({k:rel[k] for k in ('ocid','date','tag','awards','contracts')}, cls=E, ensure_ascii=False)[:3000])
        if any('totalAmount' in (a.get('value') or {}) for a in rel.get('awards') or []) and shown['total']<1:
            shown['total']+=1; print('=== TOTALAMOUNT', json.dumps({k:rel[k] for k in ('ocid','date','tag','awards','contracts')}, cls=E, ensure_ascii=False)[:2000])
        if len(cs)>=2 and shown['multi']<1 and len(cs)<5:
            shown['multi']+=1; print('=== MULTI', json.dumps({k:rel[k] for k in ('ocid','date','tag','parties','awards','contracts')}, cls=E, ensure_ascii=False)[:5000])
        if 'implementation' in json.dumps(cs, cls=E) and shown['impl']<1:
            shown['impl']+=1; print('=== IMPL', json.dumps(cs, cls=E, ensure_ascii=False)[:2000])
        if (rel.get('tender') or {}).get('lots') and shown['lots']<1 and cs:
            shown['lots']+=1; print('=== LOTS', json.dumps({k:rel[k] for k in ('ocid','date','tag','awards','contracts')}, cls=E, ensure_ascii=False)[:1500], json.dumps(rel['tender']['lots'], cls=E, ensure_ascii=False)[:800])
print('releases', sum(rel_per_ocid.values()), 'ocids', len(rel_per_ocid), 'multi-release ocids', sum(1 for v in rel_per_ocid.values() if v>1))
print('contract count changes across releases: shrink', shrink, 'grow', grow, 'same', same)

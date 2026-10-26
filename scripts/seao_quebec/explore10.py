import sys, json, collections, ijson, re, datetime
path=sys.argv[1]
dist=collections.Counter(); k=0
examples=[]
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        old = int(rel['ocid'].rsplit('-',1)[1])<19000000
        for c in rel.get('contracts') or []:
            if c.get('status')!='active': continue
            ed=(c.get('period') or {}).get('endDate')
            if not ed: continue
            ed=ed[:10]; sd=(c.get('dateSigned') or '')[:10]; rd=rel['date'][:10]
            dist[(old, 'end>=today' if ed>='2026-10-25' else 'end<today', 'end>=signed' if ed>=sd else 'end<signed')]+=1
            if len(examples)<10 and ed<'2026-10-25' and old:
                examples.append((rel['ocid'], rel['tag'], 'rel', rd, 'signed', sd, 'end', ed, rel['tender'].get('title','')[:60], c.get('value')))
for k_,v in sorted(dist.items()): print(v,k_)
for e in examples: print(e)

import sys, json, collections, ijson, re
# amendments / implementation / lots presence in a big monthly; relation to depenses
path='downloads/seao_quebec/json/mensuel_20250901_20250930.json'
paths=collections.Counter(); k=0; n=0
with open(path,'rb') as f:
    for rel in ijson.items(f,'releases.item', use_float=True):
        n+=1
        for c in rel.get('contracts') or []:
            for key in c.keys(): paths['contracts/'+key]+=1
            if c.get('implementation'):
                for key in c['implementation'].keys(): paths['contracts/implementation/'+key]+=1
                if k<2:
                    k+=1; print('IMPL', rel['ocid'], json.dumps(c, ensure_ascii=False)[:1500])
        for key in rel.keys(): paths['/'+key]+=1
        for key in (rel.get('tender') or {}).keys(): paths['tender/'+key]+=1
        for a in rel.get('awards') or []:
            for key in a.keys(): paths['awards/'+key]+=1
            for key in (a.get('value') or {}).keys(): paths['awards/value/'+key]+=1
print(n); 
for p,c in sorted(paths.items()): print(c,p)

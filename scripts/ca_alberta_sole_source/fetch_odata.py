#!/usr/bin/env python3
"""Pull Alberta Sole-source service contracts OData collections completely, following __next (server pages of 25)."""
import json, sys, time, os, requests
OUT=sys.argv[1]
BASE="http://sole-source.dataservices.alberta.ca/SoleSourceDataService.svc/"
UA={"User-Agent":"contracts-research/1.0","Accept":"application/json"}
for coll in ["DisplayContracts","DisplaySpecialContracts"]:
    rows=[]; url=f"{BASE}{coll}?$format=json&$orderby=id"; n=0
    while url:
        for attempt in range(8):
            try:
                r=requests.get(url,headers=UA,timeout=120)
                if r.status_code==200: break
                print(coll,n,'HTTP',r.status_code,flush=True)
            except Exception as e:
                print(coll,n,'EXC',e,flush=True)
            time.sleep(3+3*attempt)
        else:
            print('GIVE UP',coll,n); break
        d=r.json().get('d')
        if isinstance(d,list): batch=d; nxt=None
        else: batch=d.get('results',[]); nxt=d.get('__next')
        rows.extend(batch); n+=1
        if n%20==0: print(coll,'pages',n,'rows',len(rows),flush=True)
        url=nxt
        if url and '$format=json' not in url: url+='&$format=json'
        time.sleep(0.25)
    json.dump(rows,open(os.path.join(OUT,coll+'.json'),'w'))
    print(coll,'DONE rows',len(rows),flush=True)
print('ALL DONE')

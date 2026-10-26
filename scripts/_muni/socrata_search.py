import json,sys,urllib.request,urllib.parse
dom=sys.argv[1]; q=sys.argv[2]
url=f"https://api.us.socrata.com/api/catalog/v1?domains={dom}&q={urllib.parse.quote(q)}&limit=40"
req=urllib.request.Request(url,headers={'User-Agent':'contracts-research/1.0'})
d=json.load(urllib.request.urlopen(req,timeout=60))
print('==',dom,q,'results',d.get('resultSetSize'))
for r in d.get('results',[]):
    res=r['resource']
    print(' ',res['id'],'|',res['name'],'|',res.get('type'),'|',(res.get('updatedAt') or '')[:10],'|',res.get('columns_name',[])[:14])

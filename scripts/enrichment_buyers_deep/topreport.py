import json,collections,sys
L=[json.loads(l) for l in open('enrichment/buyers_enriched.jsonl')]
B={json.loads(l)['buyer_key']:json.loads(l) for l in open('enrichment/buyer_master_input.jsonl')}
agg=collections.defaultdict(lambda:[0,None])
for x in L:
    key=x['canonical_name'] or x['name']
    agg[key][0]+=B[x['buyer_key']]['record_count_high_or_medium']
    if agg[key][1] is None or (x['ap_contact']['emails'] and not agg[key][1]['ap_contact']['emails']): agg[key][1]=x
n=int(sys.argv[1]); s=int(sys.argv[2]) if len(sys.argv)>2 else 0
for i,(k,(v,x)) in enumerate(sorted(agg.items(),key=lambda t:-t[1][0])[s:n]):
    print(i+s,v,k[:55],'|',x['official_website'][:45],'|',x['extras'].get('website_check',{}).get('status'),'| AP:',x['ap_contact']['emails'][:2],'| P:',x['procurement_contact']['emails'][:1], '| inv:', bool(x['ap_contact']['invoicing_requirements']))

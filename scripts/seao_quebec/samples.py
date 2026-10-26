import json, collections, random
path='normalized/seao_quebec.jsonl'
want = {'ongoing_json_only':None, 'ongoing_with_xml':None, 'inferred_xml_only_old':None, 'inferred_json_backed':None, 'inferred_with_depenses':None}
n=0
val_none=collections.Counter(); unit=collections.Counter()
for line in open(path, encoding='utf-8'):
    n+=1
    r=json.loads(line)
    raw=r['raw']
    if r['status']=='ongoing' and raw['avis'] is None and want['ongoing_json_only'] is None and r['contract']['value']: want['ongoing_json_only']=r
    if r['status']=='ongoing' and raw['avis'] is not None and want['ongoing_with_xml'] is None: want['ongoing_with_xml']=r
    if r['status']=='ongoing_inferred' and raw['ocds_release'] is None and r['contract']['dates']['signed'] and r['contract']['dates']['signed']<'2013' and want['inferred_xml_only_old'] is None and n%7==0: want['inferred_xml_only_old']=r
    if r['status']=='ongoing_inferred' and raw['ocds_release'] is not None and raw['avis'] is None and want['inferred_json_backed'] is None and n%5==0: want['inferred_json_backed']=r
    if r['status']=='ongoing_inferred' and raw['depenses_supplementaires'] and want['inferred_with_depenses'] is None and n%3==0: want['inferred_with_depenses']=r
    if r['contract']['value'] is None: val_none[(bool(raw['avis']), bool(raw['ocds_release']))]+=1
    u=r['contract']['related'].get('montantssoumisunite_code')
    if u: unit[u]+=1
print('value None breakdown (has_xml, has_json):', val_none)
print('non-$ unit codes:', unit)
out={}
for k,r in want.items():
    slim={kk:vv for kk,vv in r.items() if kk!='raw'}
    slim['raw_keys_present']={kk:(type(vv).__name__ if vv is not None else None) for kk,vv in r['raw'].items()}
    out[k]=slim
json.dump(out, open('downloads/seao_quebec/logs/samples.json','w'), ensure_ascii=False, indent=1)
for k,r in out.items(): print('==',k, r['record_id'], r['status'], r['contract']['dates'], r['contract']['value'])

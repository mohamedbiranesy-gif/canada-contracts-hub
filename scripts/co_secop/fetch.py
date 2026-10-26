#!/usr/bin/env python3
"""Colombia SECOP II: suppliers registered with pais=CA (qmzu-gj57) -> their contracts (jbjy-vk9h) via codigo_proveedor."""
import json, urllib.request, urllib.parse, time, sys, os
UA = {"User-Agent": "contracts-research/1.0"}
dl = "downloads/co_secop"
def soda(ds, params):
    url = "https://www.datos.gov.co/resource/%s.json?%s" % (ds, urllib.parse.urlencode(params))
    for i in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120))
        except Exception as e:
            print("ERR", e, url[:200], file=sys.stderr); time.sleep(3)
    return None
log = open(dl + "/fetch.log", "a")
sup = []
off = 0
while True:
    r = soda("qmzu-gj57", {"$where": "pais in('CA','CAN','Canada','CANADA','Canadá','CANADÁ')", "$limit": 5000, "$offset": off, "$order": "codigo"})
    if not r: break
    sup += r; off += len(r)
    if len(r) < 5000: break
json.dump(sup, open(dl + "/proveedores_pais_CA_all.json", "w"), ensure_ascii=False)
log.write("%s proveedores pais CA: %d\n" % (time.strftime("%FT%TZ", time.gmtime()), len(sup)))
codes = sorted({s["codigo"] for s in sup if s.get("codigo")})
cons = []
for i in range(0, len(codes), 40):
    chunk = codes[i:i+40]
    w = "codigo_proveedor in(%s)" % ",".join("'%s'" % c for c in chunk)
    r = soda("jbjy-vk9h", {"$where": w, "$limit": 50000})
    if r: cons += r
    time.sleep(0.5)
json.dump(cons, open(dl + "/contratos_by_codigo_proveedor_CA.json", "w"), ensure_ascii=False)
log.write("%s contratos for those suppliers: %d\n" % (time.strftime("%FT%TZ", time.gmtime()), len(cons)))
print(len(sup), len(cons))

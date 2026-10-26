#!/usr/bin/env python3
"""Paginated ArcGIS REST layer query -> JSONL (attributes only), resumable by offset.
usage: python3 -I arcgis_pull.py <layer_url> <out.jsonl> "<where>" [page]"""
import sys, json, time, urllib.request, urllib.parse
UA = "contracts-research/1.0"
url, out, where = sys.argv[1], sys.argv[2], sys.argv[3]
page = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
log = open(out + ".log", "a")
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START {url} where={where}\n")
off = 0; n = 0
with open(out, "w", encoding="utf-8") as fo:
    while True:
        q = urllib.parse.urlencode({"where": where, "outFields": "*", "f": "json", "resultOffset": off, "resultRecordCount": page, "returnGeometry": "false"})
        for a in range(5):
            try:
                j = json.load(urllib.request.urlopen(urllib.request.Request(url + "/query?" + q, headers={"User-Agent": UA}), timeout=120)); break
            except Exception as e:
                log.write(f"retry {a} {e}\n"); time.sleep(3 * (a + 1))
        else:
            raise SystemExit("failed")
        if "error" in j:
            log.write(f"ERROR {j['error']}\n"); raise SystemExit(str(j["error"]))
        fs = j.get("features", [])
        for f in fs:
            fo.write(json.dumps(f["attributes"], ensure_ascii=False) + "\n"); n += 1
        off += len(fs)
        if not fs or not j.get("exceededTransferLimit") and len(fs) < page:
            break
        time.sleep(0.4)
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE rows={n}\n"); log.close()
print(n)

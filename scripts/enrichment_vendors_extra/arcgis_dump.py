#!/usr/bin/env python3
"""Dump all rows of an ArcGIS FeatureServer layer (paginated, attributes only) to <out>.jsonl.gz, ~1 request/second.
usage: python3 -I arcgis_dump.py <layer_url> <out_prefix>
Writes <out_prefix>.jsonl.gz (one JSON object = one feature's attributes, verbatim), <out_prefix>_layer.json (layer metadata)
and <out_prefix>_retrieved_at.txt."""
import sys, json, gzip, time, datetime, urllib.request, urllib.parse

URL, OUT = sys.argv[1].rstrip("/"), sys.argv[2]
UA = "contracts-research/1.0 (public-sector contract vendor enrichment)"


def get(u, params):
    q = u + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            return json.loads(urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": UA}), timeout=120).read())
        except Exception as e:
            print("retry", attempt, repr(e)[:150], file=sys.stderr, flush=True)
            time.sleep(10 * (attempt + 1))
    raise SystemExit("failed " + q)


started = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
meta = get(URL, {"f": "json"})
json.dump(meta, open(OUT + "_layer.json", "w"), indent=0)
page = min(int(meta.get("maxRecordCount") or 1000), 2000)
oid = meta.get("objectIdField") or "OBJECTID"
n, off = 0, 0
with gzip.open(OUT + ".jsonl.gz", "wt", encoding="utf-8") as f:
    while True:
        time.sleep(1.0)
        j = get(URL + "/query", {"where": "1=1", "outFields": "*", "returnGeometry": "false", "orderByFields": oid,
                                 "resultOffset": off, "resultRecordCount": page, "f": "json"})
        feats = j.get("features") or []
        for ft in feats:
            f.write(json.dumps(ft["attributes"], ensure_ascii=False) + "\n")
        n += len(feats)
        off += len(feats)
        print("rows", n, file=sys.stderr, flush=True)
        if not feats or not (j.get("exceededTransferLimit") or len(feats) == page):
            break
open(OUT + "_retrieved_at.txt", "w").write(started + "\n")
print("done", n, URL)

#!/usr/bin/env python3
"""Field inspection for a prioritized list of ArcGIS items (appends to fields file; skips items already inspected).
usage: python3 -I arcgis_fields2.py <items.jsonl> <priority_ids.json> <fields_out.jsonl>
Per-host throttle 0.5 s (<= 2 req/s per host)."""
import json, sys, re, time, threading, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
UA = "contracts-research/1.0"
locks = {}; last = {}; glock = threading.Lock()


def throttle(host, gap=0.5):
    with glock:
        if host not in locks:
            locks[host] = threading.Lock(); last[host] = 0
    with locks[host]:
        w = last[host] + gap - time.time()
        if w > 0:
            time.sleep(w)
        last[host] = time.time()


def getj(u, timeout=45, tries=2):
    host = urllib.parse.urlparse(u).netloc; err = None
    for a in range(tries):
        throttle(host)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            err = str(e)[:150]; time.sleep(2)
    return {"_error": err}


items = {}
for l in open(sys.argv[1]):
    j = json.loads(l); items[j["id"]] = j
pids = json.load(open(sys.argv[2]))
done = set()
try:
    for l in open(sys.argv[3]):
        done.add(json.loads(l)["item"])
except FileNotFoundError:
    pass
todo = [items[i] for i in pids if i in items and i not in done]
print("todo", len(todo), file=sys.stderr, flush=True)
fo = open(sys.argv[3], "a"); wl = threading.Lock()


def layers_for(url):
    url = url.rstrip("/")
    if re.search(r"/(FeatureServer|MapServer)/\d+$", url, re.I):
        return [url]
    j = getj(url + "?f=json")
    out = [f"{url}/{l['id']}" for key in ("layers", "tables") for l in (j.get(key) or []) if isinstance(l, dict) and "id" in l]
    return out[:15] or [url + "/0"]


def chk(it):
    try:
        for lu in layers_for(it["url"]):
            j = getj(lu + "?f=json")
            if "_error" in j or "error" in j:
                rec = {"item": it["id"], "layer": lu, "error": str(j.get("_error") or j.get("error"))[:200]}
            else:
                rec = {"item": it["id"], "layer": lu, "name": j.get("name"), "type": j.get("type"),
                       "fields": [(x.get("name"), x.get("alias"), x.get("type")) for x in (j.get("fields") or [])],
                       "lastEditDate": (j.get("editingInfo") or {}).get("lastEditDate")}
            with wl:
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush()
    except Exception as e:
        with wl:
            fo.write(json.dumps({"item": it["id"], "layer": it["url"], "error": str(e)[:200]}) + "\n")


with ThreadPoolExecutor(10) as ex:
    list(ex.map(chk, todo))
print("done", file=sys.stderr)

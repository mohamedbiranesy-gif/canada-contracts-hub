#!/usr/bin/env python3
"""Parallel PASS1 for fetch_by_vendor.py (added on resume): probe one CMS detail page per not-yet-probed vendor ID with prefix
'ue-' (unverified-entity IDs), appending to the same vendor_probe.jsonl. Vendors are ORDERED (not filtered) so that names with
company-form tokens typical of Canadian firms (LTD, LIMITED, CANADA, LTEE, ULC, CORP, INC.) are probed first; country is still
decided only from the address on the detail page. Global rate limit <= 2 req/s.
usage: [LBB_PROBE_PREFIXES=ue-] [LBB_STRONG_ONLY=1] python3 -I probe_parallel.py <lbb_download_csv> <out_dir> [threads]
On resume it was also run with LBB_PROBE_PREFIXES=1,7 LBB_STRONG_ONLY=1 (399 vendors whose names contain CANADA/CANADIAN/LTD/LIMITED/LTEE/ULC).
"""
import sys, csv, re, os, json, time, threading, urllib.request, http.cookiejar
sys.path.insert(0, "scripts/us_state_texas_lbb")
from fetch_details import parse_vendor, UA

path, out_dir = sys.argv[1], sys.argv[2]
NT = int(sys.argv[3]) if len(sys.argv) > 3 else 4
vp = os.path.join(out_dir, "vendor_probe.jsonl")
log = open(os.path.join(out_dir, "probe_parallel.log"), "a")
probed = set()
if os.path.exists(vp):
    for l in open(vp, encoding="utf-8"):
        probed.add(json.loads(l)["vid"])
byvid = {}
for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
    vid = r["Vendor ID"].strip('"')
    if vid.startswith(tuple(os.environ.get("LBB_PROBE_PREFIXES", "ue-").split(","))) and vid not in probed:
        byvid.setdefault(vid, []).append(r)
PRI = re.compile(r"\b(LTD|LIMITED|CANADA|CANADIAN|LTEE|LTÉE|ULC|INC\.|CORP\.?|CORPORATION|TECHNOLOGIES)\b", re.I)


def pri(v):
    n = byvid[v][0]["Vendor"]
    return 0 if PRI.search(n) and not re.search(r"\bL\.?L\.?C\b", n, re.I) else 1


order = sorted(byvid, key=lambda v: (pri(v), v))
if os.environ.get("LBB_STRONG_ONLY"):  # restrict to names with strong tokens (used for FEIN/SSN-prefixed IDs 1/7)
    STRONG = re.compile(r"\b(CANADA|CANADIAN|LTD|LIMITED|LTEE|LTÉE|ULC)\b", re.I)
    order = [v for v in order if STRONG.search(byvid[v][0]["Vendor"])]
lock = threading.Lock(); rl = threading.Lock(); last = [0.0]; idx = [0]; done = [0]
fo = open(vp, "a", encoding="utf-8")
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START todo={len(order)} priority={sum(1 for v in order if pri(v) == 0)} threads={NT}\n"); log.flush()


def worker():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders = [("User-Agent", UA)]
    while True:
        with lock:
            if idx[0] >= len(order):
                return
            vid = order[idx[0]]; idx[0] += 1
        rs = byvid[vid]
        url = re.search(r"href='([^']+)'", rs[0]["Contract-ID"]).group(1).replace(" ", "%20")
        htm = final = None
        for a in range(4):
            with rl:
                wait = 0.5 - (time.time() - last[0])
                if wait > 0:
                    time.sleep(wait)
                last[0] = time.time()
            try:
                with op.open(url, timeout=90) as resp:
                    htm = resp.read().decode("utf-8", errors="replace"); final = resp.geturl(); break
            except Exception as e:
                log.write(f"retry {a} {url} {e}\n"); log.flush(); time.sleep(3 * (a + 1))
        if htm is None:
            continue
        j = {"vid": vid, "probe_url": url, "final_url": final, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
             "vendor_block": parse_vendor(htm), "n_contracts": len(rs), "vendor_name_csv": rs[0]["Vendor"]}
        with lock:
            fo.write(json.dumps(j, ensure_ascii=False) + "\n"); fo.flush(); done[0] += 1
            if done[0] % 50 == 0:
                log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} probed {done[0]}/{len(order)}\n"); log.flush()


ts = [threading.Thread(target=worker) for _ in range(NT)]
[t.start() for t in ts]
[t.join() for t in ts]
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE probed={done[0]}\n"); log.close()

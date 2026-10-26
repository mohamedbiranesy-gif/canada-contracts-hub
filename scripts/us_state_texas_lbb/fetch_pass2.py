#!/usr/bin/env python3
"""PASS2 only (added on resume): for every probed vendor whose CMS address is Canadian (is_canadian_block), fetch the detail
page of each of its active contracts not yet in details_canadian.jsonl. Lets pass 2 run while the parallel 'ue-' probe is
still incomplete. usage: python3 -I fetch_pass2.py <lbb_download_csv> <out_dir>"""
import sys, csv, re, os, json, time, urllib.parse, urllib.request, http.cookiejar
sys.path.insert(0, "scripts/us_state_texas_lbb")
from fetch_details import parse_vendor, UA
from fetch_by_vendor import is_canadian_block, fetch

path, out_dir = sys.argv[1], sys.argv[2]
log = open(os.path.join(out_dir, "fetch_pass2.log"), "a")
probed = {}
for l in open(os.path.join(out_dir, "vendor_probe.jsonl"), encoding="utf-8"):
    j = json.loads(l); probed[j["vid"]] = j
ca = {v for v, j in probed.items() if is_canadian_block(j["vendor_block"])}
byvid = {}
for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
    vid = r["Vendor ID"].strip('"')
    if vid in ca:
        byvid.setdefault(vid, []).append(r)
dp = os.path.join(out_dir, "details_canadian.jsonl")
done = set()
for l in open(dp, encoding="utf-8"):
    j = json.loads(l); done.add((j["aid"], j["cid"]))
cj = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj)); op.addheaders = [("User-Agent", UA)]
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} PASS2 canadian vendors={len(ca)}\n"); log.flush()
n = 0
with open(dp, "a", encoding="utf-8") as fo:
    for vid, rs in byvid.items():
        for r in rs:
            url = re.search(r"href='([^']+)'", r["Contract-ID"]).group(1).replace(" ", "%20")
            q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            aid, cid = q.get("aid", [""])[0], q.get("cid", [""])[0]
            if (aid, cid) in done:
                continue
            htm, final = fetch(op, url, log)
            if htm is None:
                continue
            fn = os.path.join(out_dir, "html", re.sub(r"[^A-Za-z0-9_.-]", "_", f"{aid}_{cid}") + ".html")
            open(fn, "w", encoding="utf-8").write(htm)
            rec = {"aid": aid, "cid": cid, "url": url, "final_url": final, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "vendor_block": parse_vendor(htm), "csv_row": r, "html_file": fn}
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); fo.flush(); done.add((aid, cid)); n += 1
            time.sleep(0.4)
log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE new={n}\n"); log.close()
print("new", n)

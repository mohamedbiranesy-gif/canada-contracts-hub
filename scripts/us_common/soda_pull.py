#!/usr/bin/env python3
"""Paginated Socrata SODA puller -> JSONL (one row per line), resumable.
usage: python3 -I soda_pull.py <domain> <dataset_id> <out.jsonl> [where-clause]
Writes progressively; log to <out>.log; state in <out>.state
"""
import sys, json, time, os, urllib.parse, urllib.request

UA = "contracts-research/1.0"
PAGE = 50000

def fetch(url, tries=6):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(5 * (i + 1))
    raise last

def main():
    domain, ds, out = sys.argv[1], sys.argv[2], sys.argv[3]
    where = sys.argv[4] if len(sys.argv) > 4 else None
    log = open(out + ".log", "a")
    state_f = out + ".state"
    offset = 0
    if os.path.exists(state_f):
        offset = int(open(state_f).read().strip() or 0)
    mode = "a" if offset else "w"
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} START domain={domain} ds={ds} offset={offset} where={where}\n"); log.flush()
    with open(out, mode, encoding="utf-8") as fo:
        while True:
            q = {"$limit": PAGE, "$offset": offset, "$order": ":id"}
            if where:
                q["$where"] = where
            url = f"https://{domain}/resource/{ds}.json?" + urllib.parse.urlencode(q)
            rows = fetch(url)
            for r in rows:
                fo.write(json.dumps(r, ensure_ascii=False) + "\n")
            fo.flush()
            offset += len(rows)
            open(state_f, "w").write(str(offset))
            log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} got {len(rows)} total {offset}\n"); log.flush()
            if len(rows) < PAGE:
                break
    log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} DONE total={offset}\n"); log.close()

if __name__ == "__main__":
    main()

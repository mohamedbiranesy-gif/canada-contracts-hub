#!/usr/bin/env python3
"""Crawl Alberta Purchasing Connection (APC) awarded opportunities.

Phase 1: search API (POST /api/opportunity/search) filtered to statusCode AWARD,
         sliced by postDate windows (API rejects offsets >= ~1000 and the UI uses
         limit<=1000), writes all search hits to search_hits.jsonl.
Phase 2: for each reference number AB-YYYY-NNNNN fetch
         GET /api/opportunity/public/{year}/{id} (public, no auth) -> details/AB-YYYY-NNNNN.json
Resumable: skips details already on disk. Writes a log and a state file.
Usage: python3 -I crawl_apc.py <download_dir>
"""
import json, os, sys, time, datetime as dt
import requests

BASE = "https://purchasing.alberta.ca/api"
UA = {"User-Agent": "contracts-research/1.0", "Accept": "application/json"}
OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "details"), exist_ok=True)
LOG = open(os.path.join(OUT, "crawl.log"), "a")
SLEEP = 0.35  # ~3 req/s


def log(msg):
    line = f"{dt.datetime.utcnow().isoformat()}Z {msg}"
    LOG.write(line + "\n"); LOG.flush()
    print(line, flush=True)


def search(start, end, offset, limit=1000, status="AWARD"):
    body = {
        "query": "", "queryMode": "standard", "includeEnhancedMatchIds": False,
        "filter": {
            "solicitationNumber": "", "categories": [],
            "statuses": [{"value": status, "selected": True, "count": 0}],
            "agreementTypes": [], "solicitationTypes": [], "opportunityTypes": [],
            "deliveryRegions": [], "deliveryRegion": "", "organizations": [], "unspsc": [],
            "postDateRange": "$$custom", "postDateStart": start, "postDateEnd": end,
            "closeDateRange": "$$custom",
        },
        "limit": limit, "offset": offset,
        "sortOptions": [{"field": "PostDateTime", "direction": "asc"}],
    }
    for attempt in range(6):
        try:
            r = requests.post(BASE + "/opportunity/search", json=body, headers=UA, timeout=90)
            if r.status_code == 200:
                return r.json()
            log(f"search {start}..{end} off={offset} HTTP {r.status_code} {r.text[:200]}")
        except Exception as e:
            log(f"search {start}..{end} off={offset} EXC {e}")
        time.sleep(2 + 3 * attempt)
    return None


def month_windows(first="2010-01-01", last=None):
    last = last or (dt.date.today() + dt.timedelta(days=2)).isoformat()
    d = dt.date.fromisoformat(first)
    end = dt.date.fromisoformat(last)
    while d <= end:
        nm = (d.replace(day=1) + dt.timedelta(days=32)).replace(day=1)
        yield d.isoformat(), (nm - dt.timedelta(days=1)).isoformat()
        d = nm


def phase1():
    hits_path = os.path.join(OUT, "search_hits.jsonl")
    state_path = os.path.join(OUT, "phase1_state.json")
    state = json.load(open(state_path)) if os.path.exists(state_path) else {"done_windows": []}
    seen = set()
    if os.path.exists(hits_path):
        for line in open(hits_path):
            try:
                seen.add(json.loads(line)["referenceNumber"])
            except Exception:
                pass
    fh = open(hits_path, "a")
    total_reported = None
    for start, end in month_windows():
        key = f"{start}..{end}"
        if key in state["done_windows"]:
            continue
        offset = 0
        n_window = 0
        while True:
            res = search(start, end, offset)
            if res is None:
                log(f"GIVE UP window {key} offset {offset}")
                break
            vals = res.get("values") or []
            tc = res.get("totalCount")
            if offset == 0:
                log(f"window {key}: totalCount={tc}")
                if tc and tc > 1000:
                    # split into daily windows
                    d0 = dt.date.fromisoformat(start); d1 = dt.date.fromisoformat(end)
                    while d0 <= d1:
                        ds = d0.isoformat()
                        r2 = search(ds, ds, 0)
                        for v in (r2 or {}).get("values") or []:
                            if v["referenceNumber"] not in seen:
                                seen.add(v["referenceNumber"]); fh.write(json.dumps(v) + "\n"); n_window += 1
                        time.sleep(SLEEP)
                        d0 += dt.timedelta(days=1)
                    fh.flush()
                    vals = []
            for v in vals:
                if v["referenceNumber"] not in seen:
                    seen.add(v["referenceNumber"]); fh.write(json.dumps(v) + "\n"); n_window += 1
            fh.flush()
            if len(vals) < 1000:
                break
            offset += 1000
            if offset >= 1000:  # API refuses deeper offsets; windows > 1000 handled by daily split
                break
            time.sleep(SLEEP)
        state["done_windows"].append(key)
        json.dump(state, open(state_path, "w"))
        log(f"window {key}: wrote {n_window}, cumulative {len(seen)}")
        time.sleep(SLEEP)
    fh.close()
    log(f"PHASE1 DONE: {len(seen)} distinct awarded references")
    return hits_path


def phase2(hits_path):
    refs = []
    for line in open(hits_path):
        try:
            refs.append(json.loads(line)["referenceNumber"])
        except Exception:
            pass
    refs = sorted(set(refs), reverse=(len(sys.argv) > 2 and sys.argv[2] == "reverse"))
    if len(sys.argv) > 2 and sys.argv[2].startswith("from:"):
        k = int(sys.argv[2][5:]); refs = refs[k:] + refs[:k]
    log(f"PHASE2: {len(refs)} references (reverse={len(sys.argv) > 2})")
    n_ok = n_fail = n_skip = 0
    for i, ref in enumerate(refs):
        path = os.path.join(OUT, "details", ref + ".json")
        if os.path.exists(path) and os.path.getsize(path) > 10:
            n_skip += 1
            continue
        try:
            _, year, num = ref.split("-")
            url = f"{BASE}/opportunity/public/{int(year)}/{int(num)}"
        except Exception:
            log(f"bad ref {ref}"); n_fail += 1; continue
        ok = False
        for attempt in range(5):
            try:
                r = requests.get(url, headers=UA, timeout=90)
                if r.status_code == 200:
                    with open(path, "w") as f:
                        f.write(r.text)
                    ok = True
                    break
                elif r.status_code == 404:
                    log(f"{ref} 404"); break
                else:
                    log(f"{ref} HTTP {r.status_code}")
            except Exception as e:
                log(f"{ref} EXC {e}")
            time.sleep(2 + 3 * attempt)
        if ok:
            n_ok += 1
        else:
            n_fail += 1
        if (i + 1) % 200 == 0:
            log(f"progress {i+1}/{len(refs)} ok={n_ok} fail={n_fail} skip={n_skip}")
        time.sleep(SLEEP)
    log(f"PHASE2 DONE ok={n_ok} fail={n_fail} skip={n_skip}")


if __name__ == "__main__":
    if len(sys.argv) > 2 and (sys.argv[2] == "reverse" or sys.argv[2].startswith("from:")):
        hp = os.path.join(OUT, "search_hits.jsonl")
    else:
        hp = phase1()
    phase2(hp)
    log("ALL DONE")

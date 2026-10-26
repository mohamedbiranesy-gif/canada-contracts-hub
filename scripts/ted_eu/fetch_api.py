#!/usr/bin/env python3
"""Fetch TED notices (all retrievable fields) from the TED Search API v3.

Modes:
  python3 -I fetch_api.py eforms <out_dir> <fields_json>
      -> all notices matching (winner-country=CAN OR organisation-country-tenderer=CAN
         OR organisation-country-subcontractor=CAN), all fields, saved one JSON per notice.
  python3 -I fetch_api.py byid <out_dir> <fields_json> <ids_file>
      -> notices listed (one publication number per line) fetched via `ND IN (...)` batches.

Rate limit <= 3 req/s, retry with backoff, skip notices already on disk (checkpointing).
"""
import json, os, sys, time
import requests

API = "https://api.ted.europa.eu/v3/notices/search"
HEADERS = {"User-Agent": "contracts-research/1.0", "Content-Type": "application/json", "Accept": "application/json"}
EFORMS_QUERY = "(winner-country=CAN OR organisation-country-tenderer=CAN OR organisation-country-subcontractor=CAN)"
PAGE = 5  # 1830 fields * 5 notices = 9150 < 10000 fields/page limit


def post(body, tries=6):
    delay = 1.0
    for i in range(tries):
        try:
            r = requests.post(API, headers=HEADERS, json=body, timeout=180)
            if r.status_code == 200:
                time.sleep(0.35)
                return r.json()
            if r.status_code == 400:
                print("400:", r.text[:500], file=sys.stderr)
                return None
            print(f"HTTP {r.status_code}, retry in {delay}s", file=sys.stderr)
        except requests.RequestException as e:
            print(f"error {e}, retry in {delay}s", file=sys.stderr)
        time.sleep(delay)
        delay = min(delay * 2, 60)
    return None


def save_notices(out_dir, notices, retrieved_at, query):
    n = 0
    for nt in notices:
        pn = nt.get("publication-number")
        if not pn:
            continue
        nt["_retrieved_at"] = retrieved_at
        nt["_query"] = query
        with open(os.path.join(out_dir, pn + ".json"), "w", encoding="utf-8") as f:
            json.dump(nt, f, ensure_ascii=False)
        n += 1
    return n


def fetch_eforms(out_dir, fields):
    os.makedirs(out_dir, exist_ok=True)
    retrieved_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    # ITERATION mode for consistency
    token = None
    total = 0
    page_no = 0
    while True:
        body = {"query": EFORMS_QUERY, "fields": fields, "limit": PAGE, "scope": "ALL", "paginationMode": "ITERATION"}
        if token:
            body["iterationNextToken"] = token
        res = post(body)
        if res is None:
            print("giving up at page", page_no, file=sys.stderr)
            break
        notices = res.get("notices") or []
        if not notices:
            break
        total += save_notices(out_dir, notices, retrieved_at, EFORMS_QUERY)
        page_no += 1
        token = res.get("iterationNextToken")
        if page_no % 10 == 0:
            print(f"page {page_no}, saved {total}, totalNoticeCount={res.get('totalNoticeCount')}", flush=True)
        if not token:
            break
    meta = {"query": EFORMS_QUERY, "retrieved_at": retrieved_at, "saved": total, "pages": page_no}
    with open(os.path.join(out_dir, "_meta.json"), "w") as f:
        json.dump(meta, f, indent=1)
    print(json.dumps(meta))


def fetch_byid(out_dir, fields, ids_file):
    os.makedirs(out_dir, exist_ok=True)
    retrieved_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    ids = [l.strip() for l in open(ids_file) if l.strip()]
    todo = [i for i in ids if not os.path.exists(os.path.join(out_dir, i + ".json"))]
    print(f"{len(ids)} ids, {len(todo)} to fetch", flush=True)
    missing = []
    for i in range(0, len(todo), PAGE):
        batch = todo[i:i + PAGE]
        q = "ND IN (" + " ".join(batch) + ")"
        res = post({"query": q, "fields": fields, "limit": PAGE, "scope": "ALL"})
        if res is None:
            missing += batch
            continue
        got = {n.get("publication-number") for n in res.get("notices") or []}
        save_notices(out_dir, res.get("notices") or [], retrieved_at, q)
        missing += [b for b in batch if b not in got]
        if (i // PAGE) % 20 == 0:
            print(f"batch {i//PAGE}, missing so far {len(missing)}", flush=True)
    with open(os.path.join(out_dir, "_missing.json"), "w") as f:
        json.dump(missing, f)
    print("done; missing:", len(missing), missing[:20])


if __name__ == "__main__":
    mode = sys.argv[1]
    out_dir = sys.argv[2]
    fields = json.load(open(sys.argv[3]))
    if mode == "eforms":
        fetch_eforms(out_dir, fields)
    elif mode == "byid":
        fetch_byid(out_dir, fields, sys.argv[4])

#!/usr/bin/env python3
"""Download World Bank contract-award data for Canadian suppliers.

1. Finances One API (successor of the Socrata kdui-wcs3 "Major Contract Awards"):
   datasets DS01004/RS00934 (FY2001-2016), DS04691/RS03933 (FY2017-2019), DS00005/RS00005 (FY2020+),
   plus DS00028/RS00025 (Corporate Procurement Contract Awards - the Bank itself as buyer),
   filtered supplier_country='Canada'.
2. World Bank Projects API for every distinct project_id (status, closing date, borrower, implementing agency).
3. Procurement notices API (search.worldbank.org/api/v2/procnotices) - Contract Award notices whose text
   contains "Country: Canada" (awarded or evaluated firm), all rows.

Usage: python3 -I fetch_wb.py <out_dir>
"""
import json, os, sys, time
import requests

H = {"User-Agent": "contracts-research/1.0", "Accept": "application/json"}
FONE = "https://datacatalogapi.worldbank.org/dexapps/fone/api/apiservice"
DATASETS = [
    ("DS01004", "RS00934", "Contract Awards in Investment Project Financing (since FY 2001 - FY 2016)"),
    ("DS04691", "RS03933", "Contract Awards in Investment Project Financing (since FY 2017 - FY 2019)"),
    ("DS00005", "RS00005", "Contract Awards in Investment Project Financing (Since FY 2020)"),
    ("DS00028", "RS00025", "Corporate Procurement Contract Awards"),
]


def get(url, params=None, tries=6):
    delay = 1.0
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=H, timeout=120)
            if r.status_code == 200:
                time.sleep(0.35)
                return r
            print("HTTP", r.status_code, r.url[:200], r.text[:200], file=sys.stderr)
            if r.status_code in (400, 404, 417):
                return r
        except requests.RequestException as e:
            print("error", e, file=sys.stderr)
        time.sleep(delay)
        delay = min(delay * 2, 60)
    return None


def fetch_fone(out_dir):
    retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    meta = {}
    for ds, rs, title in DATASETS:
        rows = []
        skip = 0
        count = None
        while True:
            r = get(FONE, {"datasetId": ds, "resourceId": rs, "top": 1000, "skip": skip, "type": "json",
                           "filter": "supplier_country='Canada'"})
            if r is None or r.status_code != 200:
                print("failed", ds, skip, file=sys.stderr)
                break
            d = r.json()
            count = d.get("count")
            data = d.get("data") or []
            rows += data
            if not data or len(rows) >= (count or 0):
                break
            skip += 1000
        path = os.path.join(out_dir, f"fone_{ds}_{rs}_canada.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"datasetId": ds, "resourceId": rs, "title": title, "filter": "supplier_country='Canada'",
                       "count": count, "retrieved_at": retrieved, "url": FONE, "rows": rows}, f, ensure_ascii=False)
        meta[ds] = {"title": title, "count": count, "rows": len(rows), "path": path}
        print(json.dumps(meta[ds]), flush=True)
        # metadata record
        m = get("https://datacatalogapi.worldbank.org/dexapps/fone/api/metadata", {"assetId": ds})
        if m is not None and m.status_code == 200:
            with open(os.path.join(out_dir, f"meta_{ds}.json"), "w") as f:
                f.write(m.text)
    return meta


def fetch_projects(out_dir):
    pids = set()
    for fn in os.listdir(out_dir):
        if fn.startswith("fone_") and fn.endswith("_canada.json"):
            d = json.load(open(os.path.join(out_dir, fn)))
            for row in d["rows"]:
                if row.get("project_id"):
                    pids.add(row["project_id"])
    path = os.path.join(out_dir, "projects.json")
    projects = json.load(open(path)) if os.path.exists(path) else {}
    todo = sorted(p for p in pids if p not in projects)
    print(f"{len(pids)} project ids, {len(todo)} to fetch", flush=True)
    fl = "id,project_name,status,closingdate,boardapprovaldate,countryshortname,countrycode,totalamt,url,impagency,borrower,lendprojectcost,approvalfy,regionname,projectstatusdisplay,lendinginstr,envassesmentcategorycode,sector1,theme1,curr_total_commitment,ibrdcommamt,idacommamt,grantamt,last_stage_reached_name,proj_last_upd_date"
    retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for i in range(0, len(todo), 20):
        batch = todo[i:i + 20]
        r = get("https://search.worldbank.org/api/v2/projects", {"format": "json", "id": ",".join(batch), "fl": fl, "rows": 50})
        got = {}
        if r is not None and r.status_code == 200:
            try:
                got = r.json().get("projects") or {}
            except Exception as e:
                print("json err", e, file=sys.stderr)
        if not isinstance(got, dict):
            got = {}
        for p in batch:
            rec = got.get(p)
            if rec is None:
                # retry single
                r1 = get("https://search.worldbank.org/api/v2/projects", {"format": "json", "id": p, "fl": fl})
                try:
                    rec = (r1.json().get("projects") or {}).get(p) if r1 is not None and r1.status_code == 200 else None
                except Exception:
                    rec = None
            projects[p] = {"_retrieved_at": retrieved, "_found": rec is not None, "record": rec}
        if (i // 20) % 10 == 0:
            with open(path, "w") as f:
                json.dump(projects, f)
            print(f"projects {i+len(batch)}/{len(todo)}", flush=True)
    with open(path, "w") as f:
        json.dump(projects, f)
    print("projects done", len(projects), "found", sum(1 for v in projects.values() if v["_found"]))


def fetch_procnotices(out_dir):
    retrieved = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    base = "https://search.worldbank.org/api/v2/procnotices"
    params = {"format": "json", "notice_type": "Contract Award", "qterm": '"Country: Canada"', "rows": 100, "srt": "noticedate", "order": "desc"}
    rows = []
    os_ = 0
    total = None
    while True:
        p = dict(params)
        p["os"] = os_
        r = get(base, p)
        if r is None or r.status_code != 200:
            print("procnotices failed at", os_, file=sys.stderr)
            break
        d = r.json()
        total = int(d.get("total", 0))
        data = d.get("procnotices") or []
        rows += data
        if not data or len(rows) >= total:
            break
        os_ += 100
    path = os.path.join(out_dir, "procnotices_canada.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"url": base, "params": params, "total": total, "retrieved_at": retrieved, "rows": rows}, f, ensure_ascii=False)
    print(json.dumps({"procnotices_total": total, "rows": len(rows), "path": path}), flush=True)


if __name__ == "__main__":
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    steps = sys.argv[2:] or ["fone", "projects", "procnotices"]
    if "fone" in steps:
        fetch_fone(out_dir)
    if "procnotices" in steps:
        fetch_procnotices(out_dir)
    if "projects" in steps:
        fetch_projects(out_dir)

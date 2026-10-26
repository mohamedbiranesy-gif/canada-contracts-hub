#!/usr/bin/env python3 -I
"""Fetch UNDP contract awards (procurement-notices.undp.org/view_awards.cfm) year by year.
Usage: python3 -I fetch_undp.py <outdir> [year_from] [year_to]
Saves <outdir>/awards_<year>.html and a fetch log.
"""
import sys, os, time, datetime, json
import requests

out = sys.argv[1]
y0 = int(sys.argv[2]) if len(sys.argv) > 2 else 2008
y1 = int(sys.argv[3]) if len(sys.argv) > 3 else 2026
os.makedirs(out, exist_ok=True)
URL = "https://procurement-notices.undp.org/view_awards.cfm"
H = {"User-Agent": "contracts-research/1.0"}
log = []
for y in range(y1, y0 - 1, -1):
    # split the year in two halves to keep responses manageable
    for (a, b) in ((f"{y}-01-01", f"{y}-06-30"), (f"{y}-07-01", f"{y}-12-31")):
        data = {"date_from1": a, "date_to1": b, "cur_contract_title": "", "cur_contract_ref": "",
                "cur_contractor_name": "", "cur_proc_meth_id": "", "cur_ocloud_iso_code": ""}
        t = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
        for attempt in range(3):
            try:
                r = requests.post(URL, data=data, headers=H, timeout=300)
                break
            except Exception as e:
                print("retry", y, a, e, file=sys.stderr); time.sleep(10); r = None
        if r is None:
            log.append({"range": [a, b], "status": "failed", "retrieved_at": t}); continue
        fn = os.path.join(out, f"awards_{a}_{b}.html")
        with open(fn, "wb") as f:
            f.write(r.content)
        n = r.text.count('contractsTable__row')
        log.append({"range": [a, b], "status": r.status_code, "bytes": len(r.content), "rows": n, "retrieved_at": t, "file": fn})
        print(y, a, b, r.status_code, len(r.content), "rows", n, flush=True)
        with open(os.path.join(out, "fetch_log.json"), "w") as f:
            json.dump(log, f, indent=1)
        time.sleep(1)

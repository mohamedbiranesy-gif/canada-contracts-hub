#!/usr/bin/env python3
"""Smoke test: what the machine is, and whether the data sites the jobs use answer from it (one request each)."""
import json
import os
import platform
import shutil
import time
import urllib.request

OUT = os.environ.get("CCH_OUT", ".")
UA = "canada-contracts-hub-worker/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
SITES = ["https://api.usaspending.gov/api/v2/references/toptier_agencies/", "https://ted.europa.eu/robots.txt",
         "https://www.contractsfinder.service.gov.uk/robots.txt", "https://www.datos.gov.co/robots.txt",
         "https://open.canada.ca/robots.txt", "https://www.seao.gouv.qc.ca/robots.txt", "https://api.us.socrata.com/api/catalog/v1?limit=1",
         "https://search.worldbank.org/api/v2/procnotices?format=json&rows=1"]
checks = {}
for url in SITES:
    t = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30) as r:
            checks[url] = {"status": r.status, "seconds": round(time.time() - t, 2)}
    except Exception as e:  # noqa: BLE001 — a probe records what happened, it never stops the job
        checks[url] = {"error": repr(e)[:200], "seconds": round(time.time() - t, 2)}
    time.sleep(1)
du = shutil.disk_usage("/")
info = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "machine": platform.machine(), "python": platform.python_version(),
        "system": platform.platform(), "cpus": os.cpu_count(), "disk_free_gb": round(du.free / 1e9, 1), "checks": checks}
with open(os.path.join(OUT, "machine.json"), "w") as f:
    json.dump(info, f, indent=1)
print(json.dumps(info))

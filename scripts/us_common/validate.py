import json, sys, re
REQ = ["record_id", "source", "status", "status_basis", "contract", "buyer", "vendor", "raw"]
for p in sys.argv[1:]:
    ids = set(); bad = 0; n = 0
    for l in open(p):
        n += 1; j = json.loads(l)
        miss = [k for k in REQ if k not in j]
        errs = []
        if miss: errs.append(f"missing {miss}")
        if j.get("status") not in ("ongoing", "ongoing_inferred", "end_date_unknown"): errs.append("status")
        if j["vendor"].get("country") != "CA" or not j["vendor"].get("country_basis"): errs.append("vendor country")
        if not j["buyer"].get("name"): errs.append("buyer name")
        if j["record_id"] in ids: errs.append("dup id")
        ids.add(j["record_id"])
        for k in ("published", "signed", "start", "end", "amended_last"):
            v = j["contract"]["dates"].get(k)
            if v and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v): errs.append(f"date {k}={v}")
        if j["status"] == "ongoing" and not (j["contract"]["dates"].get("end") and j["contract"]["dates"]["end"] >= "2026-10-25"): errs.append("ongoing w/o end")
        if j["contract"]["dates"].get("end") and j["contract"]["dates"]["end"] < "2026-10-25": errs.append("ended")
        for k in ("key", "name", "publisher", "dataset_url", "retrieved_at"):
            if not j["source"].get(k): errs.append(f"source.{k}")
        if errs:
            bad += 1
            if bad <= 3: print(p, j["record_id"], errs)
    print(f"{p}: {n} records, {bad} with problems")

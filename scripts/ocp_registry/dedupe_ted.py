#!/usr/bin/env python3
"""Drop OpenTender records whose TED notice ids already appear in normalized/ted_eu.jsonl. usage: dedupe_ted.py <key>..."""
import json, re, sys
B = "."
ted = set()
for l in open(B + "/normalized/ted_eu.jsonl"):
    m = re.match(r"ted_eu:(\d+-\d{4})", json.loads(l)["record_id"])
    if m: ted.add(m.group(1))
for k in sys.argv[1:]:
    R = [json.loads(l) for l in open(B + "/normalized/%s.jsonl" % k)]
    keep, dup = [], []
    for r in R:
        ids = [re.sub(r"^0+", "", i) for i in re.findall(r"TED:NOTICE:(\d+-\d{4})", json.dumps(r["raw"]["latest_release"]))]
        r["contract"]["related"]["ted_notice_ids"] = sorted(set(ids))
        (dup if any(i in ted for i in ids) else keep).append(r)
    open(B + "/normalized/%s.jsonl" % k, "w").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep))
    json.dump([(r["record_id"], r["contract"]["related"]["ted_notice_ids"]) for r in dup], open(B + "/downloads/%s/dropped_as_ted_eu_duplicates.json" % k, "w"))
    print(k, len(R), "dup", len(dup), "kept", len(keep))

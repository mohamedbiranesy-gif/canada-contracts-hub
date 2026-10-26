#!/usr/bin/env python3
"""Validate contributed contract records (JSONL or JSONL.gz) against docs/SCHEMA.md and the hard rules.
Usage: python3 tools/validate_records.py [--allow-ended] <file> [more files]   Exit 0 when every record passes.
--allow-ended: records whose end date fell before the reference date are accepted (the rebuild moves them to "ended")."""
import gzip, json, re, sys, collections

REF = json.load(open("coord/config.json"))["reference_date"]
STATUSES = {"ongoing", "ongoing_inferred", "end_date_unknown"}
PLACEHOLDER = re.compile(r"^(n/?a|none|null|unknown|undisclosed|confidential|withheld|redacted|various|multiple|tbd|-+|\.+)$|undisclosed|confidential client|nom retenu", re.I)
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOW_ENDED = "--allow-ended" in sys.argv
bad_total = 0
for path in [a for a in sys.argv[1:] if not a.startswith("--")]:
    op = gzip.open if path.endswith(".gz") else open
    probs, n, ids = collections.Counter(), 0, set()
    examples = {}
    with op(path, "rt", encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            if not line.strip():
                continue
            n += 1
            def bad(code):
                probs[code] += 1
                examples.setdefault(code, ln)
            try:
                r = json.loads(line)
            except Exception:
                bad("invalid_json"); continue
            rid = r.get("record_id") or ""
            if not rid or ":" not in rid: bad("record_id_missing_or_no_source_prefix")
            if rid in ids: bad("duplicate_record_id")
            ids.add(rid)
            src = r.get("source") or {}
            if not src.get("key") or not src.get("name"): bad("source.key_or_name_missing")
            if not (src.get("record_url") or src.get("dataset_url")): bad("source_url_missing")
            v, b, c = r.get("vendor") or {}, r.get("buyer") or {}, r.get("contract") or {}
            if v.get("country") != "CA": bad("vendor.country_not_CA")
            if not v.get("country_basis"): bad("vendor.country_basis_missing (which source field says Canada?)")
            if not (v.get("name") or "").strip() or PLACEHOLDER.search((v.get("name") or "").strip()): bad("vendor.name_missing_or_placeholder")
            if not (b.get("name") or "").strip() or PLACEHOLDER.search((b.get("name") or "").strip()): bad("buyer.name_missing_or_placeholder")
            st = r.get("status")
            if st not in STATUSES: bad("status_not_allowed")
            if not r.get("status_basis"): bad("status_basis_missing")
            d = c.get("dates") or {}
            for k, val in d.items():
                if val and not (isinstance(val, str) and DATE.match(val)): bad("date_not_iso:" + k)
            start = d.get("start") or d.get("award") or d.get("signed")
            end = d.get("end")
            if st == "ongoing":
                if not end: bad("ongoing_without_end_date (use ongoing_inferred or end_date_unknown)")
                elif end < REF and not ALLOW_ENDED: bad("ended_before_reference_date")
                if start and start > REF: bad("starts_after_reference_date")
            if c.get("value") is not None and not isinstance(c.get("value"), (int, float)): bad("contract.value_not_number")
            if not r.get("link"): bad("link_missing")
            if not isinstance(r.get("raw"), dict) or not r.get("raw"): bad("raw_missing (keep every source field verbatim)")
    bad_total += sum(probs.values())
    print("%s: %d records, %d problems" % (path, n, sum(probs.values())))
    for k, cnt in probs.most_common():
        print("  - %s: %d (first at line %d)" % (k, cnt, examples[k]))
sys.exit(1 if bad_total else 0)

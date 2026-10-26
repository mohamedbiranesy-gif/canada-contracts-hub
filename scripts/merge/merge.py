#!/usr/bin/env python3
"""Merge all per-source normalized JSONL files into the deliverables.

Usage: python3 -I merge.py <normalized_dir> <out_dir>

Produces (in <out_dir>):
  canadian_vendor_contracts_normalized.jsonl   one line per record, raw removed,
                                               + status_confidence, + cross_source_matches
  summary.json                                 counts and aggregates
  sample_records.json                          a readable sample (with raw, trimmed)
Per-source full files (with raw) are gzipped separately by the shell wrapper.
"""
import sys, os, json, re, unicodedata, datetime, collections, random

TODAY = datetime.date(2026, 10, 25)
SRC_DIR, OUT_DIR = sys.argv[1], sys.argv[2]
os.makedirs(OUT_DIR, exist_ok=True)

LEGAL = re.compile(r"\b(inc|incorporated|ltd|ltee|ltée|limited|limitee|limitée|corp|corporation|co|company|compagnie|llc|lp|llp|plc|gmbh|ag|sa|s\.a|srl|bv|nv|pty|the|le|la|les|l|d|de|du|des|et|and|&|group|groupe|holdings|holding|international|intl|canada|canadian|canadienne|canadien)\b")
NONALNUM = re.compile(r"[^a-z0-9 ]+")
SPACES = re.compile(r"\s+")

def stem(name):
    if not name:
        return ""
    s = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode().lower()
    s = NONALNUM.sub(" ", s)
    s = LEGAL.sub(" ", s)
    s = SPACES.sub(" ", s).strip()
    return s

def year_of(d):
    try:
        return int(str(d)[:4])
    except Exception:
        return None

def confidence(rec):
    st = rec.get("status")
    basis = (rec.get("status_basis") or "").lower()
    key = rec.get("source", {}).get("key", "")
    dates = rec.get("contract", {}).get("dates", {}) or {}
    if st == "ongoing":
        if "> 2100" in basis or "placeholder" in basis or "data-entry error" in basis:
            return "high_flagged_date", "explicit end date >= 2026-10-25 but the source's end date looks like a placeholder/data-entry error (see status_basis)"
        return "high", "source publishes an explicit end date >= 2026-10-25 and a start/award date <= 2026-10-25"
    if st == "end_date_unknown":
        return "unknown", "source publishes the award/contract but no end date, duration or closure signal"
    if st == "ongoing_inferred":
        if key == "seao_quebec" or "no final-information" in basis or "no closure" in basis or "closure record" in basis:
            y = year_of(dates.get("signed") or dates.get("start") or dates.get("published"))
            if y is not None and y >= 2023:
                return "low", "only evidence is the absence of a closure (information finale) record; contract concluded in %d" % y
            return "very_low", "only evidence is the absence of a closure (information finale) record; contract concluded in %s, closure publication is known to be incomplete and late" % (y if y else "an unknown year")
        return "medium", "end date computed from a stated duration/term, framework or project period, or the parent award's period (see status_basis)"
    return "unknown", "unrecognised status"

def to_num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).replace(",", "").replace("$", "").strip())
    except Exception:
        return None

sources = sorted(f for f in os.listdir(SRC_DIR) if f.endswith(".jsonl"))
out_path = os.path.join(OUT_DIR, "canadian_vendor_contracts_normalized.jsonl")
counts = collections.Counter()
by_src_status = collections.defaultdict(collections.Counter)
by_src_conf = collections.defaultdict(collections.Counter)
by_buyer_country = collections.Counter()
by_buyer_country_high = collections.Counter()
value_by_currency_high = collections.Counter()
value_by_currency_all = collections.Counter()
vendors = collections.defaultdict(set)
buyers_by_source = collections.defaultdict(set)
bad = collections.Counter()
ids_seen = set()
dup_ids = []
groups = collections.defaultdict(list)   # (vendor_stem, buyer_stem) -> [(record_id, source_key, value, currency, start, end, idset)]
samples = collections.defaultdict(list)
random.seed(20261025)

with open(out_path, "w", encoding="utf-8") as out:
    for fn in sources:
        key = fn[:-6]
        with open(os.path.join(SRC_DIR, fn), encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception:
                    bad[key + ":invalid_json"] += 1
                    continue
                rid = rec.get("record_id")
                if not rid:
                    bad[key + ":no_record_id"] += 1
                    continue
                if rid in ids_seen:
                    bad[key + ":duplicate_record_id"] += 1
                    dup_ids.append(rid)
                    continue
                ids_seen.add(rid)
                src = rec.get("source") or {}
                skey = src.get("key") or key
                st = rec.get("status")
                conf, conf_basis = confidence(rec)
                rec["status_confidence"] = conf
                rec["status_confidence_basis"] = conf_basis
                c = rec.get("contract") or {}
                v = to_num(c.get("value"))
                cur = c.get("currency")
                b = rec.get("buyer") or {}
                vd = rec.get("vendor") or {}
                bc = b.get("country") or "unknown"
                counts["total"] += 1
                by_src_status[skey][st] += 1
                by_src_conf[skey][conf] += 1
                by_buyer_country[bc] += 1
                if conf in ("high", "high_flagged_date"):
                    by_buyer_country_high[bc] += 1
                    if v is not None and cur:
                        value_by_currency_high[cur] += v
                if v is not None and cur:
                    value_by_currency_all[cur] += v
                vendors[stem(vd.get("name"))].add(skey)
                buyers_by_source[skey].add(b.get("name"))
                dates = c.get("dates") or {}
                idvals = set()
                for k2, v2 in (c.get("identifiers") or {}).items():
                    if isinstance(v2, (str, int)) and len(str(v2)) >= 5:
                        idvals.add(str(v2).strip().lower())
                groups[(stem(vd.get("name")), stem(b.get("name")))].append(
                    (rid, skey, v, cur, dates.get("start"), dates.get("end"), idvals))
                if len(samples[skey]) < 40 and random.random() < 0.05:
                    samples[skey].append(rec)
                slim = {k: v2 for k, v2 in rec.items() if k != "raw"}
                slim["raw_available_in"] = "full/%s.jsonl.gz" % key
                out.write(json.dumps(slim, ensure_ascii=False) + "\n")
        print("done", key, counts["total"], file=sys.stderr, flush=True)

# ---- cross-source matching (same vendor stem + same buyer stem + corroborating value/dates/identifier) ----
matches = collections.defaultdict(list)
pairs_found = 0
for (vs, bs), items in groups.items():
    if not vs or not bs or len(items) < 2:
        continue
    if len({it[1] for it in items}) < 2:
        continue
    n = len(items)
    if n > 400:
        continue
    for i in range(n):
        for j in range(i + 1, n):
            a, b2 = items[i], items[j]
            if a[1] == b2[1]:
                continue
            reasons = []
            if a[2] and b2[2] and a[3] and a[3] == b2[3] and abs(a[2] - b2[2]) <= 0.01 * max(a[2], b2[2]):
                reasons.append("same value (%s %.2f vs %.2f)" % (a[3], a[2], b2[2]))
            if a[4] and a[5] and a[4] == b2[4] and a[5] == b2[5]:
                reasons.append("same start and end dates")
            common = a[6] & b2[6]
            if common:
                reasons.append("shared identifier(s): " + ", ".join(sorted(common)[:5]))
            if reasons:
                pairs_found += 1
                matches[a[0]].append({"record_id": b2[0], "source": b2[1], "evidence": "; ".join(reasons)})
                matches[b2[0]].append({"record_id": a[0], "source": a[1], "evidence": "; ".join(reasons)})

# second pass to attach matches
tmp = out_path + ".tmp"
with open(out_path, encoding="utf-8") as fin, open(tmp, "w", encoding="utf-8") as fout:
    for line in fin:
        rec = json.loads(line)
        rec["cross_source_matches"] = matches.get(rec["record_id"], [])
        fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
os.replace(tmp, out_path)

summary = {
    "reference_date": TODAY.isoformat(),
    "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "total_records": counts["total"],
    "records_by_source_and_status": {k: dict(v) for k, v in sorted(by_src_status.items())},
    "records_by_source_and_confidence": {k: dict(v) for k, v in sorted(by_src_conf.items())},
    "records_by_confidence": dict(sum((collections.Counter(v) for v in by_src_conf.values()), collections.Counter())),
    "records_by_buyer_country": dict(by_buyer_country.most_common()),
    "records_by_buyer_country_high_confidence": dict(by_buyer_country_high.most_common()),
    "distinct_vendor_name_stems": len([v for v in vendors if v]),
    "distinct_buyer_names_by_source": {k: len(v) for k, v in sorted(buyers_by_source.items())},
    "value_sum_by_currency_high_confidence": {k: round(v, 2) for k, v in value_by_currency_high.items()},
    "value_sum_by_currency_all": {k: round(v, 2) for k, v in value_by_currency_all.items()},
    "value_caveat": "Sums add contract ceilings, framework/standing-offer maxima and IDV ceilings as published; they are not spend. Treat as an upper bound.",
    "cross_source_match_pairs": pairs_found,
    "records_with_cross_source_matches": len(matches),
    "rejected_lines": dict(bad),
    "duplicate_record_ids_rejected_sample": dup_ids[:20],
    "confidence_levels": {
        "high": "explicit published end date >= reference date (and start <= reference date)",
        "high_flagged_date": "as high, but the end date looks like a placeholder (e.g. 9999-12-31) - see status_basis",
        "medium": "end date computed from a stated duration/term, framework/project period or parent award period",
        "low": "no closure record published (SEAO convention) and contract concluded 2023 or later",
        "very_low": "no closure record published (SEAO convention) and contract concluded before 2023; closure publication is incomplete/late so many of these are probably finished",
        "unknown": "award published, nothing usable about the end date",
    },
}
with open(os.path.join(OUT_DIR, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

def trim(o, depth=0):
    if isinstance(o, dict):
        return {k: trim(v, depth + 1) for k, v in list(o.items())[:60]}
    if isinstance(o, list):
        return [trim(v, depth + 1) for v in o[:5]] + (["... %d more" % (len(o) - 5)] if len(o) > 5 else [])
    if isinstance(o, str) and len(o) > 600:
        return o[:600] + "...[%d chars]" % len(o)
    return o

sample_out = {k: [trim(r) for r in v[:8]] for k, v in sorted(samples.items())}
with open(os.path.join(OUT_DIR, "sample_records.json"), "w", encoding="utf-8") as f:
    json.dump(sample_out, f, indent=1, ensure_ascii=False)
print(json.dumps({k: summary[k] for k in ("total_records", "records_by_confidence", "cross_source_match_pairs", "rejected_lines")}, indent=1))

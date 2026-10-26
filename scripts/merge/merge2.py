#!/usr/bin/env python3
"""Merge every per-source normalized JSONL into slim merged files (raw dropped).

Usage: python3 -I merge2.py <normalized_dir> <out_dir>
Writes:
  <out_dir>/merged_ca.jsonl          records whose vendor.country == CA
  <out_dir>/merged_unverified.jsonl  records whose source publishes no vendor location
  <out_dir>/merge_stats.json
Each slim record gets: status_confidence(+_basis), link, link_type, source_file,
cross_source_matches (filled in a second pass).
"""
import sys, os, json, re, unicodedata, datetime, collections

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
    return SPACES.sub(" ", s).strip()


def year_of(d):
    try:
        return int(str(d)[:4])
    except Exception:
        return None


def confidence(rec):
    st = rec.get("status")
    basis = (rec.get("status_basis") or "").lower()
    key = (rec.get("source") or {}).get("key", "")
    dates = (rec.get("contract") or {}).get("dates") or {}
    if st == "ongoing":
        if "> 2100" in basis or "placeholder" in basis or "data-entry error" in basis:
            return "high_flagged_date", "explicit end date >= 2026-10-25 but it looks like a placeholder/data-entry error (see status_basis)"
        return "high", "source publishes an explicit end date >= 2026-10-25 and a start/award date <= 2026-10-25"
    if st == "end_date_unknown":
        return "unknown", "source publishes the award/contract but no end date, duration or closure signal"
    if st == "ongoing_inferred":
        if key == "seao_quebec" or "no final-information" in basis or "closure record" in basis:
            y = year_of(dates.get("signed") or dates.get("start") or dates.get("published"))
            if y is not None and y >= 2023:
                return "low", "only evidence is the absence of a closure (information finale) record; contract concluded in %d" % y
            return "very_low", "only evidence is the absence of a closure (information finale) record; contract concluded in %s; closure publication is incomplete and late, so many of these have probably ended" % (y if y else "an unknown year")
        return "medium", "end date computed from a stated duration/term, framework or project period, or the parent award's period (see status_basis)"
    return "unknown", "unrecognised status"


def best_link(rec):
    src = rec.get("source") or {}
    if src.get("record_url"):
        return src["record_url"], "record_page"
    rel = (rec.get("contract") or {}).get("related") or {}
    for k in ("award_notice_url", "tender_notice_url", "notice_url", "contract_url", "project_url", "prime_award_url", "document_url", "release_url"):
        v = rel.get(k)
        if isinstance(v, str) and v.startswith("http"):
            return v, k
    for k, v in rel.items():
        if isinstance(v, str) and v.startswith("http") and "url" in k.lower():
            return v, k
    if src.get("dataset_url"):
        return src["dataset_url"], "dataset_page (source has no per-record page; use the identifiers to find the record)"
    return None, None


def to_num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).replace(",", "").replace("$", "").strip())
    except Exception:
        return None


files = sorted(f for f in os.listdir(SRC_DIR) if f.endswith(".jsonl") and os.path.getsize(os.path.join(SRC_DIR, f)) > 0)
paths = {"ca": os.path.join(OUT_DIR, "merged_ca.jsonl"), "unv": os.path.join(OUT_DIR, "merged_unverified.jsonl")}
outs = {k: open(p, "w", encoding="utf-8") for k, p in paths.items()}
stats = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(collections.Counter)))
bad = collections.Counter()
ids_seen = set()
groups = collections.defaultdict(list)

for fn in files:
    srcfile = fn[:-6]
    with open(os.path.join(SRC_DIR, fn), encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception:
                bad[srcfile + ":invalid_json"] += 1
                continue
            rid = rec.get("record_id")
            if not rid:
                bad[srcfile + ":no_record_id"] += 1
                continue
            if rid in ids_seen:
                bad[srcfile + ":duplicate_record_id"] += 1
                continue
            ids_seen.add(rid)
            vd = rec.get("vendor") or {}
            bucket = "ca" if (vd.get("country") or "").upper() in ("CA", "CAN", "CANADA") else "unv"
            conf, conf_basis = confidence(rec)
            rec["status_confidence"] = conf
            rec["status_confidence_basis"] = conf_basis
            link, link_type = best_link(rec)
            rec["link"] = link
            rec["link_type"] = link_type
            rec["source_file"] = srcfile
            rec["vendor_country_verified"] = bucket == "ca"
            st = stats[bucket][srcfile]
            st["status"][rec.get("status")] += 1
            st["confidence"][conf] += 1
            st["buyer_country"][(rec.get("buyer") or {}).get("country") or "unknown"] += 1
            c = rec.get("contract") or {}
            v = to_num(c.get("value"))
            cur = c.get("currency")
            if v is not None and cur:
                st["value_sum_" + ("high" if conf in ("high", "high_flagged_date") else "other")][cur] += v
            st["has_record_page"][link_type == "record_page"] += 1
            b = rec.get("buyer") or {}
            dates = c.get("dates") or {}
            idvals = set()
            for k2, v2 in (c.get("identifiers") or {}).items():
                if isinstance(v2, (str, int)) and len(str(v2)) >= 5:
                    idvals.add(str(v2).strip().lower())
            groups[(stem(vd.get("name")), stem(b.get("name")))].append((rid, srcfile, v, cur, dates.get("start"), dates.get("end"), idvals))
            slim = {k: v2 for k, v2 in rec.items() if k != "raw"}
            slim["raw_available_in"] = "full/%s.jsonl.gz (record_id %s)" % (srcfile, rid)
            outs[bucket].write(json.dumps(slim, ensure_ascii=False) + "\n")
    print("done", srcfile, len(ids_seen), file=sys.stderr, flush=True)
for o in outs.values():
    o.close()

matches = collections.defaultdict(list)
pairs = 0
for (vs, bs), items in groups.items():
    if not vs or not bs or len(items) < 2 or len({it[1] for it in items}) < 2 or len(items) > 400:
        continue
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
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
                pairs += 1
                ev = "same vendor and buyer name; " + "; ".join(reasons)
                matches[a[0]].append({"record_id": b2[0], "source_file": b2[1], "evidence": ev})
                matches[b2[0]].append({"record_id": a[0], "source_file": a[1], "evidence": ev})

for k, p in paths.items():
    tmp = p + ".tmp"
    with open(p, encoding="utf-8") as fin, open(tmp, "w", encoding="utf-8") as fout:
        for line in fin:
            rec = json.loads(line)
            rec["cross_source_matches"] = matches.get(rec["record_id"], [])
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
    os.replace(tmp, p)

out = {"reference_date": TODAY.isoformat(),
       "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "buckets": {b: {s: {k: dict(v) for k, v in d.items()} for s, d in sorted(src.items())} for b, src in stats.items()},
       "cross_source_match_pairs": pairs, "records_with_cross_source_matches": len(matches),
       "rejected_lines": dict(bad), "total_records": len(ids_seen)}
with open(os.path.join(OUT_DIR, "merge_stats.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False, default=str)
print("TOTAL", len(ids_seen), "pairs", pairs, "bad", dict(bad))

#!/usr/bin/env python3
"""The cloud leads as append-only shards (2026-11-10).

Until now three workflows (row factory, member directories, credit / DNS scan) each loaded data/incoming/claude/claude_buyer_leads_cc.csv and
claude_lead_details_cc.jsonl.gz whole, changed them and wrote them back whole. Measured: 168,154 leads = 58 MB of CSV (GitHub refuses a file
over 100 MB: that is ~290,000 leads) and a 30 MB compressed details file that git stores again in full at every merge.

From now on the two files are a frozen base. A writer loads the current state (base + shards), works on it as before, and saves only what it
changed, as one shard per kind in data/incoming/claude/lead_shards/:

    leads_<engine>_<stamp>.gz     CSV, LEAD_COLS — leads that are new or whose row changed (a later shard replaces an earlier row of the key)
    details_<engine>_<stamp>.gz   JSON lines — details that are new or changed (the newest record of a key wins)
    gone_<engine>_<stamp>.gz      "L<TAB>key" / "D<TAB>key" — leads / details withdrawn by a stricter rule

Shards are applied in the order of their stamps (UTC, YYYYMMDDTHHMMSS + an optional letter), so two workflows that merge at the same time never
touch the same file and a push retry writes the same names again. The engines that always wrote shards (bbb, rbq, lic) fit the same rule.

    import lead_store as LS
    leads, det = LS.load(exclude=("rf", stamp))   # {key: row}, {key: details}: base + shards, without this run's own shards (push retry)
    snap = LS.snapshot(leads, det)                # before changing them
    …
    LS.save("rf", stamp, leads, det, snap)        # writes the shards of this run; returns (rows written, details written, withdrawn)

    for row in LS.rows(): …                    # readers: every current lead row
CLI:  python3 tools/lead_store.py stats
"""
import csv, glob, gzip, hashlib, json, os, re, sys

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INC = os.path.join(ROOT, "data/incoming/claude")
SHARDS = os.path.join(INC, "lead_shards")
BASE_LEADS = os.path.join(INC, "claude_buyer_leads_cc.csv")
BASE_DET = os.path.join(INC, "claude_lead_details_cc.jsonl.gz")
LEAD_COLS = ["buyer_key", "buyer_name", "website", "canadian_vendor_rows", "example_vendor", "canada_field_value", "evidence_dataset", "latest_record_date"]
_NAME = re.compile(r"^(leads|details|gone)_(?:([A-Za-z0-9]+)_)?(\d{8}T\d{6}\w*)\.gz$")
_ORDER = {"gone": 0, "leads": 1, "details": 2}


def shard_files(kinds=("gone", "leads", "details")):
    """[(stamp, kind, path)] of the shards, oldest first (within one stamp: withdrawals, then rows, then details)"""
    ev = []
    for p in glob.glob(os.path.join(SHARDS, "*.gz")):
        m = _NAME.match(os.path.basename(p))
        if m and m.group(1) in kinds:
            ev.append((m.group(3), _ORDER[m.group(1)], m.group(1), p))
    ev.sort()
    return [(s, k, p) for s, _, k, p in ev]


def _read_gone(p):
    out = []
    with gzip.open(p, "rt", encoding="utf-8") as fh:
        for l in fh:
            q = l.rstrip("\n").split("\t")
            if len(q) == 2 and q[0] in ("L", "D") and q[1]:
                out.append((q[0], q[1]))
    return out


def load(details=True, base=True, exclude=None):
    """the current cloud leads and their details: the frozen base files, then every shard in the order of its stamp.
    exclude=(engine, stamp): a writer leaves out the shards of its own run (a push retry computes them again from the new state of main)"""
    leads, det = {}, {}
    _skip = ("_%s_%s.gz" % tuple(exclude)) if exclude else None
    if base and os.path.exists(BASE_LEADS):
        with open(BASE_LEADS, encoding="utf-8", errors="replace") as fh:  # opened the way every reader of this file always opened it
            for r in csv.DictReader(fh):
                if r.get("buyer_key"):
                    leads[r["buyer_key"]] = r
    if base and details and os.path.exists(BASE_DET):
        with gzip.open(BASE_DET, "rt", encoding="utf-8") as fh:
            for l in fh:
                try:
                    o = json.loads(l)
                    det[o["key"]] = o
                except (ValueError, KeyError, TypeError):
                    pass
    for _, kind, p in shard_files():
        if _skip and os.path.basename(p).endswith(_skip):
            continue
        if kind == "gone":
            for what, k in _read_gone(p):
                if what == "L":
                    leads.pop(k, None)
                else:
                    det.pop(k, None)
        elif kind == "leads":
            with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
                for r in csv.DictReader(fh):
                    if r.get("buyer_key"):
                        leads[r["buyer_key"]] = r
        elif details:
            with gzip.open(p, "rt", encoding="utf-8") as fh:
                for l in fh:
                    try:
                        o = json.loads(l)
                        det[o["key"]] = o
                    except (ValueError, KeyError, TypeError):
                        pass
    return leads, det


def rows():
    """every current lead row (base + shards, withdrawals applied)"""
    return load(details=False)[0].values()


def reader(path):
    """the rows of a leads file. For the cloud base file (claude_buyer_leads_cc.csv) that is the current cloud state: base + shards.
    Every tool that used to open that file reads it through here, so a lead that lives in a shard, or was withdrawn by one, is seen alike everywhere."""
    if os.path.abspath(path) == os.path.abspath(BASE_LEADS):
        return iter(list(rows()))
    return csv.DictReader(open(path, encoding="utf-8", errors="replace"))


def _h(o):
    return hashlib.md5(json.dumps(o, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")).digest()[:8]


def _row(r):
    return {c: ("" if r.get(c) is None else str(r.get(c))) for c in LEAD_COLS}


def snapshot(leads, det):
    """what is on file now, as one short hash per row and per details record"""
    return {k: _h(_row(r)) for k, r in leads.items()}, {k: _h(d) for k, d in det.items()}


def save(engine, stamp, leads, det, snap):
    """write the shards of this run: rows and details that are new or changed since `snap`, and the keys that are gone.
    Returns (rows written, details written, leads withdrawn)."""
    s_rows, s_det = snap
    os.makedirs(SHARDS, exist_ok=True)
    up = [k for k in sorted(leads) if s_rows.get(k) != _h(_row(leads[k]))]
    upd = [k for k in sorted(det) if s_det.get(k) != _h(det[k])]
    gone = [("L", k) for k in sorted(s_rows) if k not in leads] + [("D", k) for k in sorted(s_det) if k not in det]
    base = os.path.join(SHARDS, "%%s_%s_%s.gz" % (engine, stamp))
    for kind, n in (("leads", len(up)), ("details", len(upd)), ("gone", len(gone))):
        if not n and os.path.exists(base % kind):
            os.remove(base % kind)  # a retry of the same run (its state was loaded with exclude=(engine, stamp)) that has nothing of this kind any more
    if up:
        with gzip.open(base % "leads", "wt", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=LEAD_COLS)
            w.writeheader()
            for k in up:
                w.writerow(_row(leads[k]))
    if upd:
        with gzip.open(base % "details", "wt", encoding="utf-8") as fh:
            for k in upd:
                fh.write(json.dumps(det[k], ensure_ascii=False) + "\n")
    if gone:
        with gzip.open(base % "gone", "wt", encoding="utf-8") as fh:
            for what, k in gone:
                fh.write("%s\t%s\n" % (what, k))
    return len(up), len(upd), sum(1 for w, _ in gone if w == "L")


if __name__ == "__main__":
    import collections
    L, D = load()
    fam = collections.Counter()
    for r in L.values():
        c = r.get("canada_field_value") or ""
        fam["registry" if c.startswith("registry contract") else "member / licence" if "membership / statutory fee" in c else "tech (credit / DNS / service)" if "(tech)" in c else
            "listed on a Canadian vendor's page" if "vendor located in Canada" in c else "dated record"] += 1
    sh = shard_files()
    print("cloud leads: %d rows, %d details; base file %s; shards: %d files (%s)" % (
        len(L), len(D), ("%.1f MB" % (os.path.getsize(BASE_LEADS) / 1e6)) if os.path.exists(BASE_LEADS) else "absent", len(sh),
        ", ".join("%s %d" % kv for kv in collections.Counter(k for _, k, _ in sh).most_common())))
    print("by kind:", dict(fam.most_common()))

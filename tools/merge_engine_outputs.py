#!/usr/bin/env python3
"""Union of engine output files produced by parallel runners (GitHub Actions shards, the Mac) — one row per key, the newest
retrieval wins. Nothing is dropped: a row absent from one copy is kept from the other. Used by .github/workflows/claude-engines.yml.
  python3 tools/merge_engine_outputs.py ap_terms   OUT.csv  IN1.csv IN2.csv …     key = (email, evidence_url)
  python3 tools/merge_engine_outputs.py registry   OUT.csv  IN1.csv …             key = (kind, key)
  python3 tools/merge_engine_outputs.py pages      OUT.csv  IN1.csv …             key = (buyer_key, url)   (ap_pages_seen.csv)
  python3 tools/merge_engine_outputs.py tsv_done   OUT.tsv  IN1.tsv …             key = column 1          (ap_walk_done.tsv)
  python3 tools/merge_engine_outputs.py jsonl      OUT.jsonl.gz IN1.jsonl.gz …     key = domain            (org_extras / org_contacts)
"""
import csv, gzip, io, os, sys

csv.field_size_limit(1 << 30)
KEYS = {"ap_terms": ("email", "evidence_url"), "registry": ("kind", "key"), "pages": ("buyer_key", "url")}
DATE = {"ap_terms": "retrieved_date", "registry": "retrieved_date", "pages": "date"}


def read_csv(path):
    if not path or not os.path.exists(path) or os.path.getsize(path) == 0:
        return [], []
    with (gzip.open if path.endswith(".gz") else open)(path, "rt", encoding="utf-8", errors="replace") as fh:
        txt = fh.read().replace("\0", "")
    rd = csv.DictReader(io.StringIO(txt))
    rows = list(rd)
    return rd.fieldnames or [], rows


def main():
    kind, out, ins = sys.argv[1], sys.argv[2], sys.argv[3:]
    if kind == "tsv_done":
        best = {}
        for p in ins:
            if not os.path.exists(p):
                continue
            for l in open(p, encoding="utf-8"):
                f = l.rstrip("\n").split("\t")
                if len(f) >= 2 and (f[0] not in best or f[1] >= best[f[0]].split("\t")[1]):
                    best[f[0]] = l.rstrip("\n")
        with open(out, "w", encoding="utf-8") as f:
            for k in sorted(best):
                f.write(best[k] + "\n")
        print("tsv_done:", len(best), "keys from", len(ins), "files")
        return
    if kind == "jsonl":  # org_extras / org_contacts: one JSON object per domain; a successful read beats a failed one, then the newest date
        import json
        best = {}
        for p in ins:
            if not p or not os.path.exists(p) or os.path.getsize(p) == 0:
                continue
            with (gzip.open if p.endswith(".gz") else open)(p, "rt", encoding="utf-8", errors="replace") as fh:
                for l in fh:
                    try:
                        d = json.loads(l)
                    except Exception:
                        continue
                    k = d.get("domain")
                    if not k:
                        continue
                    o = best.get(k)
                    # 2026-11-10: on one date the record of the newer reader wins (every shard's file holds the whole state it started from: the copy
                    # another shard carried of a site, made by the older reader on the same day, used to come after the fresh record and put its
                    # version number and page list back)
                    rank = lambda r: (r.get("status") == "ok", r.get("date") or "", int(r.get("v") or 0))
                    if o is None or rank(d) >= rank(o):
                        if o and o.get("status") == "ok" and d.get("status") == "ok":
                            m = dict(o); m.update({kk: vv for kk, vv in d.items() if vv not in ("", None, [], {})}); d = m  # facts read earlier stay when the newer read has fewer
                        best[k] = d
        with (gzip.open if out.endswith(".gz") else open)(out + ".tmp", "wt", encoding="utf-8") as f:
            for k in sorted(best):
                f.write(json.dumps(best[k], ensure_ascii=False) + "\n")
        os.replace(out + ".tmp", out)
        print("jsonl:", len(best), "domains from", len(ins), "files")
        return
    kcols, dcol = KEYS[kind], DATE[kind]
    split = kind == "ap_terms" and out.endswith("claude_ap_terms.csv")  # mailbox rows stay in the CSV, buyer-key (walker / search) rows go to claude_ap_terms_pages.csv.gz
    cols, merged, n_in = [], {}, 0
    for p in ins:
        fn, rows = read_csv(p)
        for c in fn:
            if c not in cols:
                cols.append(c)
        n_in += len(rows)
        for r in rows:
            k = tuple((r.get(c) or "").strip() for c in kcols)
            if not all(k):
                continue
            old = merged.get(k)
            if old is None or (r.get(dcol) or "") >= (old.get(dcol) or ""):
                merged[k] = r
    outputs = [(out, merged)]
    if split:
        outputs = [(out, {k: v for k, v in merged.items() if "@" in k[0]}), (out[:-4] + "_pages.csv.gz", {k: v for k, v in merged.items() if "@" not in k[0]})]
    for path, part in outputs:
        with (gzip.open if path.endswith(".gz") else open)(path + ".tmp", "wt", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for k in sorted(part):
                w.writerow({c: (part[k].get(c) or "").replace("\0", "") for c in cols})
        os.replace(path + ".tmp", path)
    print("%s: %d rows in, %d unique keys out (%d files)" % (kind, n_in, len(merged), len(ins)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Measure a change to the owner's test before any build uses it: replay tools/relationship_rows.owner_test, as it stands in the working tree,
on every row of a table already built, and count the rows whose readiness would change, by reason, with examples.

Why (2026-11-14): a rule written against a handful of rows can reach hundreds more. The name test for rule 19, replayed on the table of
22:10Z, would have taken out 86 rows of "Liberty Utilities (CalPeco Electric) LLC" — a utility the owner counted under rule 18 — and an
address ending "00000" was taken for "no address". Both were caught here, before a build. GitHub Actions does not need to run for it.

  python3 tools/replay_owner_test.py ranked_buyers.csv.gz [--examples 4] [--top 60]

The replay reads the cells a build wrote; what rank.py does before the test (names, folds, amounts) is not replayed — that part is measured by
the build's own counters in rank.log. Nothing is written.
"""
import argparse, collections, csv, gzip, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import relationship_rows as RR  # noqa: E402

csv.field_size_limit(1 << 30)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("table")
    ap.add_argument("--examples", type=int, default=4)
    ap.add_argument("--top", type=int, default=60)
    a = ap.parse_args()
    c, ex, n = collections.Counter(), collections.defaultdict(list), 0
    op = gzip.open if a.table.endswith(".gz") else open
    with op(a.table, "rt", encoding="utf-8", errors="replace") as fh:
        for x in csv.DictReader(fh):
            n += 1
            old = (x.get("ship_ready") or "").startswith("yes")
            y = dict(x)
            try:
                kind, route, out = RR.owner_test(y)
            except Exception as e:  # a crash here is a crash in the next build: shown first
                c[("ERROR", type(e).__name__, str(e)[:80])] += 1
                continue
            if old == (not out):
                continue
            if old:
                for r in out:
                    k = ("ready -> not ready", kind, re.sub(r"\(.*", "", r)[:90])
                    c[k] += 1
                    if len(ex[k]) < a.examples:
                        ex[k].append(((x.get("buyer") or "")[:35], (x.get("vendor") or "")[:30], r[:160]))
            else:
                k = ("not ready -> ready", kind, re.sub(r"\(.*", "", x.get("ship_ready_missing") or "")[:90])
                c[k] += 1
                if len(ex[k]) < a.examples:
                    ex[k].append(((x.get("buyer") or "")[:35], (x.get("vendor") or "")[:30], (x.get("ship_ready_missing") or "")[:160]))
    print("rows replayed: %d" % n)
    for k, v in sorted(c.items(), key=lambda kv: (kv[0][0] != "ERROR", -kv[1]))[:a.top]:
        print(v, k)
    for k, l in ex.items():
        print("==", k)
        for e in l:
            print("    ", e)


if __name__ == "__main__":
    main()

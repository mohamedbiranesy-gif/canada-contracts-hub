#!/usr/bin/env python3
"""Write coord/NEXT.md: for every lane, the next batch with open rows and how many remain.
A row is done when any results file of that lane has its task id. Run from repo root."""
import csv, glob, os, re, collections, datetime

done = collections.defaultdict(set)
for p in glob.glob("data/incoming/*/*.csv"):
    lane = p.split(os.sep)[-2]
    try:
        for r in csv.DictReader(open(p, encoding="utf-8-sig", newline="")):
            t = (r.get("task_id") or r.get("qa_id") or "").strip()
            if t:
                done[lane].add(t)
    except Exception:
        pass
lines = ["# NEXT — open work per lane (auto-generated %s UTC; do not edit)\n" % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")]
for lane_dir in sorted(glob.glob("coord/tasks/*/")):
    lane = os.path.basename(os.path.normpath(lane_dir))
    by_kind = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(lane_dir, "*.csv"))):
        m = re.match(r"%s_(.+?)_batch(\d+)\.csv$" % lane, os.path.basename(p))
        if m:
            by_kind[m.group(1)].append((int(m.group(2)), p))
    lines.append("## lane `%s`" % lane)
    for kind, batches in sorted(by_kind.items()):
        total = open_rows = 0
        nxt = None
        for n, p in sorted(batches):
            ids = [(r.get("task_id") or r.get("qa_id") or "").strip() for r in csv.DictReader(open(p, encoding="utf-8-sig", newline=""))]
            rem = [i for i in ids if i and i not in done[lane]]
            total += len(ids)
            open_rows += len(rem)
            if rem and nxt is None:
                nxt = (p, rem)
        if nxt:
            p, rem = nxt
            res = "data/incoming/%s/%s_%s_results_batch%s.csv" % (lane, lane, kind, re.search(r"batch(\d+)", p).group(1))
            lines.append("- **%s**: next batch `%s` — %d open rows (first: %s). Write results to `%s`. Lane total open: %d / %d."
                         % (kind, p, len(rem), ", ".join(rem[:5]), res, open_rows, total))
        else:
            lines.append("- **%s**: all %d rows done." % (kind, total))
    lines.append("")
open("coord/NEXT.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))

#!/usr/bin/env python3
"""Merge staged result CSVs (written by engines OUTSIDE the git clone) into the clone's data/incoming/claude files as a
RECORD union, then leave the files for push_loop to commit. Also resolves a conflicted CSV left by a rebase the same way.

Why: engines that append into files inside the clone lose every row written after git rewrites the file (a rebase or an
autostash conflict replaces the inode; the open handle keeps writing into an orphan). 2026-11-04 02:00: 4,502 ap_pages rows
were lost that way. Stage dir: ~/cch-crawler-state/stage/<same file name>.csv.
  python3 tools/stage_merge.py [--repo ~/cch-crawler] [--stage ~/cch-crawler-state/stage]
"""
import argparse, csv, glob, io, os, re, sys


def read_records(path):
    """header, rows (as tuples) of a CSV; conflict markers from a failed merge are dropped"""
    if not os.path.exists(path):
        return None, []
    raw = open(path, encoding="utf-8", errors="replace", newline="").read().replace("\0", "")
    if "<<<<<<<" in raw[:200] or "\n<<<<<<< " in raw or "\n>>>>>>> " in raw:
        raw = "\n".join(l for l in raw.split("\n") if not re.match(r"^(<<<<<<< |=======$|>>>>>>> )", l))
    rows = list(csv.reader(io.StringIO(raw)))
    rows = [r for r in rows if r]
    if not rows:
        return None, []
    return rows[0], rows[1:]


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--stage", default=os.path.expanduser("~/cch-crawler-state/stage"))
    a = a.parse_args()
    os.makedirs(a.stage, exist_ok=True)
    for sp in sorted(glob.glob(os.path.join(a.stage, "*.csv"))):
        name = os.path.basename(sp)
        tp = os.path.join(a.repo, "data/incoming/claude", name)
        sh, srows = read_records(sp)
        th, trows = read_records(tp)
        if sh is None:
            continue
        header = th or sh
        if th and th != sh:
            # map staged columns onto the target header
            idx = {c: i for i, c in enumerate(sh)}
            srows = [[r[idx[c]] if c in idx and idx[c] < len(r) else "" for c in header] for r in srows]
        seen = set(tuple(r) for r in trows)
        new = [r for r in srows if tuple(r) not in seen and any(x.strip() for x in r)]
        if not new and th == header and not ("<<<<<<<" in open(tp, encoding="utf-8", errors="replace").read()[:200] if os.path.exists(tp) else False):
            continue
        tmp = tp + ".merge.tmp"
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(trows)
            w.writerows(new)
        os.replace(tmp, tp)
        print("%s: +%d rows (target now %d)" % (name, len(new), len(trows) + len(new)))
    # a conflicted file left by a rebase (no staged twin): keep every record of both sides
    for tp in glob.glob(os.path.join(a.repo, "data/incoming/claude", "*.csv")):
        raw = open(tp, encoding="utf-8", errors="replace").read(200000)
        if "\n<<<<<<< " in raw or raw.startswith("<<<<<<< "):
            h, rows = read_records(tp)
            seen, out = set(), []
            for r in rows:
                if tuple(r) not in seen:
                    seen.add(tuple(r)); out.append(r)
            with open(tp + ".merge.tmp", "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f); w.writerow(h); w.writerows(out)
            os.replace(tp + ".merge.tmp", tp)
            print("%s: conflict markers removed, %d records kept" % (os.path.basename(tp), len(out)))


if __name__ == "__main__":
    main()

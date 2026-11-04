#!/usr/bin/env python3
"""push_loop v3 helper: snapshot the engines' lane files from the LIVE clone into the push worktree.

Why: the engines append into ~/cch-crawler/data/incoming/claude around the clock, so git must never rewrite that working
tree (v1 autostash and v2 stash+rebase both lost rows when a file changed under git: 2026-11-04 02:00 4,502 rows,
06:00-06:40 three cycles failed with "does not match index" and nothing was pushed). v3 keeps a separate worktree
(~/cch-crawler-state/pushwt, branch pushwt reset to origin/main every cycle), copies the live files into it, commits and pushes.
Rules per file:
  - skipped when origin changed it AFTER the live copy was last written (the live copy is stale; e.g. a file edited from the cloud);
  - text files: a half-written last line is dropped;
  - result files (*_results_*.csv, append-only): lines present only on origin are kept (never lose a row); other files
    (leads, mx, jsonl.gz) are copied as they are, because their writers rewrite them whole and may legitimately remove rows.
  python3 tools/push_snapshot.py ~/cch-crawler/data/incoming/claude ~/cch-crawler-state/pushwt
"""
import glob, os, subprocess, sys

SRC = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/cch-crawler/data/incoming/claude")
WT = os.path.expanduser(sys.argv[2] if len(sys.argv) > 2 else "~/cch-crawler-state/pushwt")
DST = os.path.join(WT, "data/incoming/claude")
TEXT = (".csv", ".tsv", ".jsonl", ".txt", ".md")


def last_commit_time(rel):
    out = subprocess.run(["git", "-C", WT, "log", "-1", "--format=%ct", "--", rel], capture_output=True, text=True).stdout.strip()
    return int(out) if out.isdigit() else 0


def main():
    os.makedirs(DST, exist_ok=True)
    copied, skipped = [], []
    for p in sorted(glob.glob(os.path.join(SRC, "*"))):
        name = os.path.basename(p)
        if os.path.isdir(p) or name.startswith(".") or name.endswith((".tmp", ".merge.tmp", ".lock", ".part")):
            continue
        q = os.path.join(DST, name)
        rel = "data/incoming/claude/" + name
        if os.path.exists(q) and last_commit_time(rel) > os.path.getmtime(p):
            skipped.append(name)
            continue
        b = open(p, "rb").read()
        if name.endswith(TEXT):
            if b and not b.endswith(b"\n"):
                b = b[:b.rfind(b"\n") + 1]
            if os.path.exists(q) and "_results_" in name:
                have = set(b.split(b"\n"))
                extra = [l for l in open(q, "rb").read().split(b"\n") if l.strip() and l not in have]
                if extra:
                    b = b + b"\n".join(extra) + b"\n"
                    print("%s: %d lines only on origin kept" % (name, len(extra)), flush=True)
        if os.path.exists(q) and os.path.getsize(q) == len(b) and open(q, "rb").read() == b:
            continue
        with open(q + ".tmp", "wb") as f:
            f.write(b)
        os.replace(q + ".tmp", q)
        copied.append(name)
    print("snapshot: %s%s" % (", ".join(copied) if copied else "no change", ("; stale (origin newer): " + ", ".join(skipped)) if skipped else ""), flush=True)


if __name__ == "__main__":
    main()

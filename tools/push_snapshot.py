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
TEXT = (".csv", ".tsv", ".jsonl", ".txt", ".md")
# 2026-11-08 23:23Z: the Mac's ap_terms rewrote claude_ap_terms_pages.csv.gz from its own view and the snapshot replaced the runners' union on
# origin (50,895 → 40,405 page rows). Files that several writers (GitHub runners + this Mac) produce rows for are UNIONED by key with the
# origin copy (tools/merge_engine_outputs.py: newest retrieval wins, a successful read beats a failed one), never copied over it.
MERGE = {"claude_ap_terms.csv": "ap_terms", "claude_registry_lookup.csv": "registry", "claude_org_extras.jsonl.gz": "jsonl", "claude_org_contacts.jsonl.gz": "jsonl"}
MERGE_SKIP = {"claude_ap_terms_pages.csv.gz"}  # merged together with claude_ap_terms.csv


def merge_into(q, p, kind, name):
    """union origin's copy (q, in the worktree) with the live file (p) into q; the live file is the last input so its rows win ties"""
    tool = os.path.join(WT, "tools/merge_engine_outputs.py")
    ins = [q, p]
    if kind == "ap_terms":
        qp, pp = q[:-4] + "_pages.csv.gz", p[:-4] + "_pages.csv.gz"
        ins = [x for x in (q, qp, p, pp) if os.path.exists(x)]
    r = subprocess.run([sys.executable, tool, kind, q] + ins, capture_output=True, text=True)
    print("%s: %s" % (name, (r.stdout.strip() or r.stderr.strip())[-200:]), flush=True)
    return r.returncode == 0


def last_commit_time(rel):
    out = subprocess.run(["git", "-C", WT, "log", "-1", "--format=%ct", "--", rel], capture_output=True, text=True).stdout.strip()
    return int(out) if out.isdigit() else 0


def snapshot(src, lane):
    dst = os.path.join(WT, "data/incoming", lane)
    os.makedirs(dst, exist_ok=True)
    copied, skipped, too_big = [], [], []
    for p in sorted(glob.glob(os.path.join(src, "*"))):
        name = os.path.basename(p)
        if os.path.isdir(p) or name.startswith(".") or name.endswith((".tmp", ".merge.tmp", ".lock", ".part")):
            continue
        if lane != "claude" and "_results_" not in name:
            continue  # other lanes: only the result files the Claude-run research driver writes on this Mac
        q = os.path.join(dst, name)
        rel = "data/incoming/%s/%s" % (lane, name)
        if os.path.getsize(p) > 95 * 1024 * 1024:  # GitHub refuses files over 100 MB and one such file would block every push: skip it (writers gzip big outputs)
            if name not in too_big:
                print("%s: %d MB, over GitHub's file limit, not pushed (gzip it)" % (name, os.path.getsize(p) >> 20), flush=True)
            too_big.append(name)
            continue
        if name in MERGE_SKIP:
            continue
        if name in MERGE and os.path.exists(q) and os.path.exists(os.path.join(WT, "tools/merge_engine_outputs.py")):
            before = open(q, "rb").read()
            if merge_into(q, p, MERGE[name], name):
                if open(q, "rb").read() != before:
                    copied.append(name)
                if MERGE[name] == "ap_terms":
                    copied.append("claude_ap_terms_pages.csv.gz")
                continue
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
    return copied, skipped


def main():
    copied, skipped = snapshot(SRC, "claude")
    for lane in ("gemini", "chatgpt", "codex"):  # results the Claude-run research driver writes into the other lanes' folders on this Mac
        d = os.path.join(os.path.dirname(SRC.rstrip("/")), lane)
        if os.path.isdir(d):
            c, sk = snapshot(d, lane)
            copied += [lane + "/" + n for n in c]; skipped += [lane + "/" + n for n in sk]
    print("snapshot: %s%s" % (", ".join(copied) if copied else "no change", ("; stale (origin newer): " + ", ".join(skipped)) if skipped else ""), flush=True)


if __name__ == "__main__":
    main()

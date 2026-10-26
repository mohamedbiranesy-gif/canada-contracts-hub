#!/usr/bin/env python3
"""Commit an unattended run's output to main without merge conflicts.

Usage: python3 tools/commit_lane.py <lane> "<message>" [author]      (needs GH_TOKEN, GITHUB_REPOSITORY)

- Keeps only what the lane may write: data/incoming/<lane>/, contrib/<lane>/, notes/,
  and additions to coord/inbox/*.md and docs/PLAYBOOK.md. Everything else is discarded.
- Rebuilds the commit on top of the latest main every attempt (no rebase, so no conflicts):
  results CSVs are merged row by row with whatever is already on main; inbox / playbook additions are re-inserted
  after the same anchor line (or appended).
- Validates result CSVs (warnings only: the referee drops bad rows) and asks the referee to run afterwards.
"""
import csv, difflib, io, os, subprocess, sys, time

lane, msg = sys.argv[1], sys.argv[2]
author = sys.argv[3] if len(sys.argv) > 3 else lane + "-bot"
DIRS = ("data/incoming/%s/" % lane, "contrib/%s/" % lane, "notes/")
TEXTS = lambda p: p.startswith("coord/inbox/") and p.endswith(".md") or p == "docs/PLAYBOOK.md"


def git(*a, check=True):
    r = subprocess.run(["git"] + list(a), capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(a), r.stderr.strip()))
    return r.stdout


def show(rev, p):
    r = subprocess.run(["git", "show", "%s:%s" % (rev, p)], capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""


# 1. collect this run's output
files, inserts = {}, {}
for line in git("status", "--porcelain", "--untracked-files=all").splitlines():
    p = line[3:].strip().strip('"')
    if " -> " in p:
        p = p.split(" -> ")[-1]
    if not os.path.isfile(p):
        continue
    if p.startswith(DIRS):
        files[p] = open(p, "rb").read()
    elif TEXTS(p):
        old, new = show("HEAD", p).splitlines(), open(p, encoding="utf-8", errors="replace").read().splitlines()
        adds = []
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes():
            if tag in ("insert", "replace"):
                adds.append((old[i1 - 1] if i1 > 0 else None, new[j1:j2], i1 >= len(old)))
        if adds:
            inserts[p] = adds
print("output files: %d, text additions: %d" % (len(files), len(inserts)))
if not files and not inserts:
    print("nothing to commit")
    sys.exit(0)

git("config", "user.name", author)
git("config", "user.email", "%s@users.noreply.github.com" % author)
token, repo = os.environ.get("GH_TOKEN", ""), os.environ.get("GITHUB_REPOSITORY", "")
if token and repo:
    git("remote", "set-url", "origin", "https://x-access-token:%s@github.com/%s.git" % (token, repo))

for attempt in range(1, 7):
    # 2. start from the latest main
    git("fetch", "-q", "origin", "main")
    git("reset", "-q", "--hard", "origin/main")
    git("clean", "-q", "-fd")
    # 3. write files back; result CSVs are merged row by row
    for p, data in files.items():
        os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
        if p.endswith(".csv") and os.path.exists(p):
            remote = list(csv.reader(io.StringIO(open(p, encoding="utf-8-sig").read())))
            mine = list(csv.reader(io.StringIO(data.decode("utf-8-sig", "replace"))))
            have = {tuple(r) for r in remote}
            merged = remote + [r for r in mine[1:] if tuple(r) not in have]
            with open(p, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerows(merged)
        else:
            open(p, "wb").write(data)
    # 4. re-insert text additions
    for p, adds in inserts.items():
        lines = open(p, encoding="utf-8").read().splitlines() if os.path.exists(p) else []
        for anchor, new_lines, at_end in adds:
            if any(l in lines for l in new_lines if l.strip()):
                continue  # already there
            if not at_end and anchor is not None and anchor.strip() and anchor in lines:
                k = len(lines) - 1 - lines[::-1].index(anchor)
                lines[k + 1:k + 1] = new_lines
            else:
                lines += new_lines
        open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    # 5. validate result CSVs (warnings only)
    for p in files:
        if p.endswith(".csv") and "/data/incoming/" in "/" + p:
            subprocess.run([sys.executable, "tools/validate_returns.py", p])
    git("add", "-A", *[p for p in list(files) + list(inserts)])
    if not git("diff", "--cached", "--name-only").strip():
        print("nothing new after merging with main")
        break
    git("commit", "-q", "-m", msg)
    r = subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], capture_output=True, text=True)
    if r.returncode == 0:
        print("pushed on attempt %d" % attempt)
        try:
            subprocess.run(["gh", "workflow", "run", "verify-and-merge.yml", "--ref", "main"])
        except FileNotFoundError:
            pass
        break
    print("push rejected (attempt %d): %s" % (attempt, r.stderr.strip()[-200:]))
    time.sleep(5 * attempt)
else:
    sys.exit("could not push after 6 attempts")

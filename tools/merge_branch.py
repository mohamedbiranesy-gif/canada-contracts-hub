#!/usr/bin/env python3
"""Fold an agent's pushed branch into main without needing the agent to pull first.

Sandboxed agents (e.g. Gemini's task mode) can push but cannot fetch, so their pushes to main are rejected as soon as
main moves. They push a branch named <lane>/<anything> instead; this script (run by .github/workflows/agent-branch.yml)
takes the files that branch changed under the lane's allowed paths and commits them onto the latest main with
tools/commit_lane.py (CSV rows merged, inbox/playbook additions re-inserted), then the workflow deletes the branch.
Usage: python3 tools/merge_branch.py <branch>      (run from a checkout of main with full history)"""
import os, subprocess, sys

branch = sys.argv[1]
lane = branch.split("/")[0]


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True, check=True).stdout


git("fetch", "-q", "origin", "main", branch)
main_ref = git("rev-parse", "origin/main").strip() if subprocess.run(["git", "rev-parse", "-q", "--verify", "origin/main"], capture_output=True).returncode == 0 else git("rev-parse", "HEAD").strip()
br_ref = git("rev-parse", "origin/%s" % branch).strip()
base = git("merge-base", main_ref, br_ref).strip()
changed = [p for p in git("diff", "--name-only", base, br_ref).splitlines() if p]
allowed = ("data/incoming/%s/" % lane, "contrib/%s/" % lane, "notes/", "coord/inbox/", "docs/PLAYBOOK.md")
take = [p for p in changed if p.startswith(allowed)]
print("branch %s: %d changed, %d in allowed paths" % (branch, len(changed), len(take)))
git("checkout", "-q", main_ref)
for p in take:
    data = subprocess.run(["git", "show", "%s:%s" % (br_ref, p)], capture_output=True).stdout
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    open(p, "wb").write(data)
if take:
    subprocess.run([sys.executable, "tools/commit_lane.py", lane, "%s: merge agent branch %s" % (lane, branch), "%s-agent" % lane], check=True)

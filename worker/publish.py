#!/usr/bin/env python3
"""Publish what the jobs wrote (DATA/out) to the branch worker-results of the repository, at most every 20 minutes.

The branch holds one commit, the latest state, so the repository does not grow with every pass. A file over 90 MB
is cut into .partNN pieces (GitHub refuses files over 100 MB). The token is read from /etc/cch/token and given to
git only for the push; it is never written to the checkout or to a log.

usage: publish.py REPO DATA
"""
import os
import shutil
import subprocess
import sys
import time

REPO, DATA = sys.argv[1], sys.argv[2]
OUT, RES = os.path.join(DATA, "out"), os.path.join(DATA, "results")
STAMP = os.path.join(DATA, ".last_publish")
EVERY = 20 * 60
LIMIT = 90 * 1024 * 1024
ORIGIN = subprocess.run(["git", "remote", "get-url", "origin"], cwd=REPO, capture_output=True, text=True).stdout.strip()

if os.path.exists(STAMP) and time.time() - os.path.getmtime(STAMP) < EVERY:
    sys.exit(0)
try:
    token = open("/etc/cch/token").read().strip()
except OSError:
    token = ""
if not token or token.startswith("PASTE_"):
    print("publish: no GitHub token in /etc/cch/token; nothing pushed")
    sys.exit(0)


def git(*a, check=True):
    return subprocess.run(["git", *a], cwd=RES, check=check, capture_output=True, text=True)


if os.path.isdir(RES):
    shutil.rmtree(RES)
os.makedirs(RES)
git("init", "-q")
git("config", "user.name", "cch-worker")
git("config", "user.email", "cch-worker@users.noreply.github.com")
git("checkout", "-q", "--orphan", "worker-results")
for root, _, files in os.walk(OUT):
    for fn in files:
        src = os.path.join(root, fn)
        rel = os.path.relpath(src, OUT)
        dst = os.path.join(RES, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.getsize(src) <= LIMIT:
            shutil.copy2(src, dst)
            continue
        with open(src, "rb") as f:
            i = 0
            while True:
                chunk = f.read(LIMIT)
                if not chunk:
                    break
                i += 1
                with open("%s.part%02d" % (dst, i), "wb") as g:
                    g.write(chunk)
with open(os.path.join(RES, "README.md"), "w") as f:
    f.write("What the canada-contracts-hub worker (Oracle machine) has found so far; rewritten on every publish.\n"
            "Status of the machine and of each job: _status/status.json. One folder per job. Code: worker/ on main.\n")
git("add", "-A")
git("commit", "-q", "-m", "worker results %s" % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
url = ORIGIN.replace("https://", "https://x-access-token:%s@" % token, 1)
r = subprocess.run(["git", "push", "-q", "-f", url, "worker-results"], cwd=RES, capture_output=True, text=True, timeout=900)
msg = (r.stdout + r.stderr).replace(token, "***")
print("publish:", "pushed" if r.returncode == 0 else "push failed: " + msg[-500:])
if r.returncode == 0:
    open(STAMP, "w").close()

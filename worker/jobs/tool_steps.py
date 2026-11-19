#!/usr/bin/env python3
"""Run a repository tool's steps in the job's own copy of the code, then copy what they wrote to the published output.

  tool_steps.py --step "{py} tools/x.py pull --work {work}/x" --step "{py} tools/x.py build --work {work}/x" --copy "data/incoming/claude/x/*.csv.gz"

{py} is this Python (the machine's venv), {work} the job's CCH_WORK. A failing step stops the job (later steps would read its output).
"""
import argparse
import glob
import os
import shlex
import shutil
import subprocess
import sys
import time

ap = argparse.ArgumentParser()
ap.add_argument("--step", action="append", default=[])
ap.add_argument("--copy", action="append", default=[])
a = ap.parse_args()
repo, out, work = os.environ["CCH_REPO"], os.environ["CCH_OUT"], os.environ["CCH_WORK"]
for step in a.step:
    cmd = shlex.split(step.replace("{py}", sys.executable).replace("{work}", work))
    t = time.time()
    print("== step:", " ".join(cmd), flush=True)
    rc = subprocess.run(cmd, cwd=repo).returncode
    print("== step done in %ds, exit %d" % (time.time() - t, rc), flush=True)
    if rc != 0:
        sys.exit(rc)
for pattern in a.copy:
    for src in glob.glob(os.path.join(repo, pattern)):
        dst = os.path.join(out, os.path.relpath(src, repo))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst + ".tmp")
        os.replace(dst + ".tmp", dst)
        print("published", os.path.relpath(src, repo), os.path.getsize(dst), flush=True)

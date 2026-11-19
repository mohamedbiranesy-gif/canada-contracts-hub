#!/usr/bin/env python3
"""Start the due jobs of worker/jobs.json and write the machine's status.

Called once per pass (every 10 minutes) by worker/run.sh on the Oracle machine. Each job runs detached in its own
session, so a job may run for hours across many passes; a job is started again only after `every_hours` since its
last start, and never while it is still running. At most `max_parallel` jobs run at once. worker/STOP in the
repository stops new starts (running jobs finish).

Each job gets, in its environment:
  CCH_OUT    its own output folder (published to the branch worker-results)
  CCH_WORK   its own working folder (kept on the machine, never published: caches, state, downloads)
  CCH_CACHE  a cache shared by all jobs
  CCH_REPO   the checkout
and writes progress to its log (the last lines are published in _status/status.json).

usage: runner.py REPO DATA
"""
import json
import os
import shutil
import socket
import subprocess
import sys
import time

REPO, DATA = sys.argv[1], sys.argv[2]
PY = os.path.join(DATA, "venv", "bin", "python")
CONF = json.load(open(os.path.join(REPO, "worker", "jobs.json"), encoding="utf-8"))
STATE_P = os.path.join(DATA, "state.json")
for d in ("locks", "logs", "out", "work", "cache", os.path.join("out", "_status")):
    os.makedirs(os.path.join(DATA, d), exist_ok=True)
state = json.load(open(STATE_P, encoding="utf-8")) if os.path.exists(STATE_P) else {}
stop = os.path.exists(os.path.join(REPO, "worker", "STOP"))
now = time.time()


def alive(pid):
    try:
        os.kill(pid, 0)
        with open("/proc/%d/stat" % pid) as f:
            return f.read().rsplit(")", 1)[1].split()[0] != "Z"  # a zombie has finished
    except (OSError, IndexError):
        return False


def tail(path, n=15):
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - 8000))
            return f.read().decode("utf-8", "replace").splitlines()[-n:]
    except OSError:
        return []


running = 0
for job in CONF["jobs"]:
    name = job["name"]
    st = state.setdefault(name, {"runs": 0})
    pid_p = os.path.join(DATA, "locks", name + ".pid")
    rc_p = os.path.join(DATA, "locks", name + ".rc")
    if os.path.exists(pid_p):
        pid = int(open(pid_p).read().strip() or 0)
        if pid and alive(pid):
            st["state"] = "running"
            running += 1
            continue
        os.remove(pid_p)
        st["last_end"] = now
        st["last_rc"] = int(open(rc_p).read().strip()) if os.path.exists(rc_p) else None
        st["state"] = "finished"
for job in CONF["jobs"]:
    name = job["name"]
    st = state[name]
    if st.get("state") == "running" or not job.get("enabled", True) or stop:
        continue
    if now - st.get("last_start", 0) < float(job.get("every_hours", 24)) * 3600:
        continue
    if running >= int(CONF.get("max_parallel", 3)):
        break
    # the job runs in its own copy of the code, so the reset of the checkout every 10 minutes never touches a running job, and
    # files a tool writes inside its copy (progress, caches) stay there from one run to the next (the copy deletes nothing)
    code = os.path.join(DATA, "work", name, "code")
    shutil.copytree(REPO, code, dirs_exist_ok=True, symlinks=True, ignore=shutil.ignore_patterns(".git"))
    env = dict(os.environ, CCH_OUT=os.path.join(DATA, "out", name), CCH_WORK=os.path.join(DATA, "work", name),
               CCH_CACHE=os.path.join(DATA, "cache"), CCH_REPO=code, PYTHONUNBUFFERED="1")
    os.makedirs(env["CCH_OUT"], exist_ok=True)
    os.makedirs(env["CCH_WORK"], exist_ok=True)
    cmd = [PY if c == "{py}" else c for c in job["cmd"]]
    rc_p = os.path.join(DATA, "locks", name + ".rc")
    if os.path.exists(rc_p):
        os.remove(rc_p)
    log = open(os.path.join(DATA, "logs", name + ".log"), "ab")
    log.write(("\n== start %s\n" % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())).encode())
    log.flush()
    wrapper = 'timeout --kill-after=60 %dm "$@"; echo $? > "%s"' % (int(job.get("timeout_minutes", 60)), rc_p)
    p = subprocess.Popen(["bash", "-c", wrapper, "_"] + cmd, cwd=code, env=env, stdout=log, stderr=subprocess.STDOUT,
                         start_new_session=True)
    with open(os.path.join(DATA, "locks", name + ".pid"), "w") as f:
        f.write(str(p.pid))
    st.update(state="running", last_start=now, runs=st.get("runs", 0) + 1)
    running += 1
    print("started", name, "pid", p.pid)
with open(STATE_P + ".tmp", "w", encoding="utf-8") as f:
    json.dump(state, f, indent=1)
os.replace(STATE_P + ".tmp", STATE_P)

du = shutil.disk_usage(DATA)
try:
    mem = {l.split(":")[0]: int(l.split()[1]) for l in open("/proc/meminfo") if l.split(":")[0] in ("MemTotal", "MemAvailable")}
except OSError:
    mem = {}
status = {
    "pass_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
    "commit": subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip(),
    "stop_file": stop,
    "host": {"name": socket.gethostname(), "cpus": os.cpu_count(), "load": os.getloadavg(),
             "mem_total_mb": mem.get("MemTotal", 0) // 1024, "mem_available_mb": mem.get("MemAvailable", 0) // 1024,
             "disk_free_gb": round(du.free / 1e9, 1), "disk_total_gb": round(du.total / 1e9, 1)},
    "jobs": {j["name"]: dict(state.get(j["name"], {}), enabled=j.get("enabled", True), every_hours=j.get("every_hours"),
                            log_tail=tail(os.path.join(DATA, "logs", j["name"] + ".log"))) for j in CONF["jobs"]},
}
with open(os.path.join(DATA, "out", "_status", "status.json"), "w", encoding="utf-8") as f:
    json.dump(status, f, indent=1, default=str)

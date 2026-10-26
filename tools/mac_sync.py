#!/usr/bin/env python3
"""Upload the work of agents on the owner's Mac whose shells have no network (the Gemini app's Task mode), and give
them today's instructions, without ever disturbing them.

Run it from any shell on the Mac that can push (ChatGPT/Codex does it at the start of every run):
    python3 tools/mac_sync.py                          # default clone: /tmp/canada-contracts-hub, lane gemini
    python3 tools/mac_sync.py /path/to/clone:lane ...  # other sandboxed clones

For each sandboxed clone:
 0. Missing clone (macOS empties /tmp when it restarts): it is cloned again and put on the branch <lane>/work.
 1. Snapshot. The lane's files as they are on disk now (committed or not) are laid over the latest main and become
    one commit whose parent is main. It is built with a temporary index, so the agent's HEAD, index and files are
    not touched. Files the agent does not have are left as main has them (nothing is ever deleted).
 2. Upload. If the snapshot holds a CSV row or text line that main does not have yet, it is pushed to GitHub as the
    branch <lane>/sync-<UTC time>. Because it sits on top of main, the push itself starts the agent-branch workflow,
    which folds it into main (lane paths only, rows merged) and deletes the branch.
 3. Refresh. Main's current instructions are copied into the clone (AGENTS.md, GEMINI.md, docs/, prompts/, tools/,
    coord/inbox/, coord/tasks/<lane>/, coord/NEXT.md, ...), so the agent reads today's orders although it cannot pull.
    Its results in data/incoming/<lane>/ are never touched. Skipped when the upload failed.
Safe to run any number of times. It always exits 0: it only reports, so it never breaks the caller's run.
"""
import csv, hashlib, io, os, subprocess, sys, tarfile, time

REPO = "mohamedbiranesy-gif/canada-contracts-hub"
DEFAULT = ["/tmp/canada-contracts-hub:gemini"]
REFRESH = ["AGENTS.md", "GEMINI.md", "CLAUDE.md", "README.md", "docs", "prompts", "tools", "coord/inbox",
           "coord/NEXT.md", "coord/STATUS_BOARD.md", "coord/DECISIONS.md", "coord/config.json", "coord/INGEST_REPORT.md",
           "coord/results/verification_log.csv"]
MAIN = "refs/mac-sync/main"  # private ref, so the agent's own refs are left alone
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")


def git(clone, *args, env=None, check=True, binary=False):
    r = subprocess.run(["git", "-C", clone] + list(args), capture_output=True, env=env or ENV, timeout=300)
    if check and r.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), r.stderr.decode("utf-8", "replace").strip()[-300:]))
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def blob(clone, ref, path):
    r = subprocess.run(["git", "-C", clone, "show", "%s:%s" % (ref, path)], capture_output=True, env=ENV)
    return r.stdout if r.returncode == 0 else b""


def additions(clone, paths):
    """{path: content} for every lane file on disk that holds a row or line main lacks. The content is main's file
    plus those rows/lines appended, so the snapshot only ever adds to main (stale local copies never overwrite)."""
    out = {}
    for top in paths:
        full = os.path.join(clone, top)
        files = [full] if os.path.isfile(full) else [os.path.join(d, f) for d, _, fs in os.walk(full) for f in fs]
        for f in files:
            rel = os.path.relpath(f, clone)
            if rel.split(os.sep)[-1].startswith(".") or subprocess.run(
                    ["git", "-C", clone, "check-ignore", "-q", rel], env=ENV).returncode == 0:
                continue
            mine, main = open(f, "rb").read(), blob(clone, MAIN, rel)
            if mine == main or not mine.strip():
                continue
            if rel.endswith(".gz") or b"\0" in mine[:4096]:
                if not main:
                    out[rel] = mine
                continue
            if not main:
                out[rel] = mine
                continue
            eol = "\r\n" if b"\r\n" in main else "\n"
            base = main if main.endswith(b"\n") else main + eol.encode()
            if rel.endswith(".csv"):
                have = {tuple(r) for r in csv.reader(io.StringIO(main.decode("utf-8-sig", "replace")))}
                add = [r for r in csv.reader(io.StringIO(mine.decode("utf-8-sig", "replace"))) if r and tuple(r) not in have]
                if add:
                    buf = io.StringIO()
                    csv.writer(buf, lineterminator=eol).writerows(add)
                    out[rel] = base + buf.getvalue().encode("utf-8")
            else:
                have = set(main.decode("utf-8", "replace").splitlines())
                add = [l for l in mine.decode("utf-8", "replace").splitlines() if l.strip() and l not in have]
                if add:
                    out[rel] = base + (eol.join(add) + eol).encode("utf-8")
    return out


def refresh(clone, lane):
    want = [p for p in REFRESH + ["coord/tasks/%s" % lane] if git(clone, "ls-tree", "--name-only", MAIN, "--", p).strip()]
    data = git(clone, "archive", "--format=tar", MAIN, "--", *want, binary=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        safe = [m for m in tar.getmembers() if (m.isfile() or m.isdir()) and not m.name.startswith(("/", "data/"))
                and ".." not in m.name.split("/")]
        if hasattr(tarfile, "data_filter"):
            tar.extractall(clone, members=safe, filter="data")
        else:
            tar.extractall(clone, members=safe)
    return len([m for m in safe if m.isfile()])


def sync(clone, lane):
    notes = []
    if not os.path.isdir(os.path.join(clone, ".git")):
        if os.path.exists(clone) and os.listdir(clone):
            return "not a git clone, left alone"
        subprocess.run(["git", "clone", "-q", "https://github.com/%s.git" % REPO, clone], check=True, env=ENV,
                       capture_output=True, timeout=600)
        git(clone, "checkout", "-q", "-b", "%s/work" % lane)
        notes.append("re-created the clone on branch %s/work" % lane)
    gitdir = git(clone, "rev-parse", "--absolute-git-dir").strip()
    git(clone, "fetch", "-q", "origin", "+refs/heads/main:%s" % MAIN)
    # a branch uploaded earlier that is still waiting means its fold did not run (GitHub's timer is unreliable): ask again
    waiting = git(clone, "ls-remote", "--heads", "origin", "refs/heads/%s/*" % lane).split()
    if waiting:
        try:
            r = subprocess.run(["gh", "workflow", "run", "agent-branch.yml", "--ref", "main", "-R", REPO],
                               capture_output=True, timeout=60)
            notes.append("%d earlier upload(s) still waiting; %s" % (len(waiting) // 2, "asked GitHub to fold them"
                         if r.returncode == 0 else "could not start the fold (gh), GitHub's timer will"))
        except (OSError, subprocess.SubprocessError):
            notes.append("%d earlier upload(s) still waiting for the fold" % (len(waiting) // 2))
    paths = ["data/incoming/%s" % lane, "contrib/%s" % lane, "notes", "coord/inbox", "docs/PLAYBOOK.md"]
    # 1. snapshot: main plus every row/line the agent has on disk that main lacks (temporary index; the agent's own
    #    HEAD, index and files are not touched)
    add = additions(clone, paths)
    key = hashlib.sha1(repr(sorted((p, hashlib.sha1(c).hexdigest()) for p, c in add.items())).encode()).hexdigest()
    last_file = os.path.join(gitdir, "mac_sync.last")
    last = open(last_file).read().strip() if os.path.exists(last_file) else ""
    uploaded = True
    if not add:
        notes.append("nothing new to upload")
    elif key == last:
        notes.append("already uploaded, waiting for the agent-branch workflow to fold it")
    else:
        idx = os.path.join(gitdir, "mac_sync.index")
        env = dict(ENV, GIT_INDEX_FILE=idx)
        try:
            git(clone, "read-tree", MAIN, env=env)
            for rel, content in add.items():
                sha = subprocess.run(["git", "-C", clone, "hash-object", "-w", "--stdin"], input=content,
                                     capture_output=True, env=ENV, check=True).stdout.decode().strip()
                git(clone, "update-index", "--add", "--cacheinfo", "100644,%s,%s" % (sha, rel.replace(os.sep, "/")), env=env)
            tree = git(clone, "write-tree", env=env).strip()
        finally:
            if os.path.exists(idx):
                os.remove(idx)
        who = dict(ENV, GIT_AUTHOR_NAME="%s-agent" % lane, GIT_AUTHOR_EMAIL="%s-agent@users.noreply.github.com" % lane,
                   GIT_COMMITTER_NAME="mac-sync", GIT_COMMITTER_EMAIL="mac-sync@users.noreply.github.com")
        commit = git(clone, "commit-tree", tree, "-p", MAIN, "-m",
                     "[%s] snapshot of local work (uploaded by tools/mac_sync.py)" % lane, env=who).strip()
        branch = "%s/sync-%s" % (lane, time.strftime("%Y%m%d-%H%M%S", time.gmtime()))
        try:
            git(clone, "push", "-q", "origin", "%s:refs/heads/%s" % (commit, branch))
            open(last_file, "w").write(key + "\n")
            notes.append("uploaded %s (%d file(s) with new rows/lines: %s)" % (branch, len(add), ", ".join(sorted(add))[:200]))
        except RuntimeError as e:
            uploaded = False
            notes.append("UPLOAD FAILED, will retry next run: %s" % e)
        git(clone, "update-ref", "-d", "refs/remotes/origin/%s" % branch, check=False)
    # 3. refresh the instructions, only when nothing is left unuploaded
    if uploaded:
        notes.append("refreshed %d instruction files" % refresh(clone, lane))
    return "; ".join(notes)


def main():
    for t in sys.argv[1:] or DEFAULT:
        clone, _, lane = t.rpartition(":")
        clone = os.path.realpath(os.path.expanduser(clone))
        try:
            print("mac_sync %s (lane %s): %s" % (clone, lane, sync(clone, lane)))
        except Exception as e:  # report, never break the caller's run
            print("mac_sync %s (lane %s): ERROR %s" % (clone, lane, e))


if __name__ == "__main__":
    main()

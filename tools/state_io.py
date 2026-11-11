#!/usr/bin/env python3
"""Big state files as release assets instead of git blobs (2026-11-10).

A file that is rewritten on every run and is already compressed cannot be stored as a difference: git keeps every version whole.
Measured over 24 hours: coord/results/team_buyers.jsonl.gz 61 versions = 1.0 GB, claude_org_extras.jsonl.gz 0.3 GB, … in a repository that
reached 8.9 GB in ten days. Such a file now lives as an asset of a release (default: harvest-state, the engines' state release); git holds
one line about it in coord/STATE_ASSETS.json (asset name, size, SHA-256, time) so that every checkout knows which version is current.

Writer (a workflow step, with GH_TOKEN):   python3 tools/state_io.py publish coord/results/team_buyers.jsonl.gz [more files] [--tag harvest-state]
    uploads each file under a name of its own for every version (claude_org_extras.<first 12 of its SHA-256>.jsonl.gz) and updates
    coord/STATE_ASSETS.json; the caller commits the manifest and stops committing the file itself (.gitignore + `git rm --cached`).
    2026-11-11: until today a version replaced the one before under one name. Two merges of one file at the same time (a dispatched
    org_facts run and the scheduled one) then went: A uploads, pushes its manifest line; B, which had started from the version before A's,
    uploads over it, loses the push, fetches "the current asset" — its own — and publishes a file without A's records. With a name per
    version an upload replaces nothing: the push of the manifest line decides, and the one that loses the push starts again from the
    version the manifest on main names. Old versions are deleted by the writer: never the one the manifest it sees names, never one
    younger than three hours, never one of the three newest.
Reader (any tool):   import state_io; state_io.ensure("coord/results/team_buyers.jsonl.gz")
    the file is used as it is when its SHA-256 is the one the manifest names (or when the manifest does not know it: a file still in git);
    otherwise it is downloaded from the release — with `gh` when a token is there, else from the public download URL.
CLI:   python3 tools/state_io.py ensure <file> [...]     |     python3 tools/state_io.py list
"""
import calendar, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANIFEST = os.path.join(ROOT, "coord/STATE_ASSETS.json")
REPO = os.environ.get("GITHUB_REPOSITORY") or "mohamedbiranesy-gif/canada-contracts-hub"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"


def rel(path):
    return os.path.relpath(os.path.abspath(path), ROOT).replace(os.sep, "/")


def manifest():
    try:
        return json.load(open(MANIFEST, encoding="utf-8"))
    except Exception:
        return {}


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()


def ensure(path, quiet=True):
    """True when `path` holds the current version (downloaded if needed); False when it could not be had."""
    ap = os.path.abspath(path if os.path.isabs(path) else os.path.join(ROOT, path) if not os.path.exists(path) else path)
    m = manifest().get(rel(ap))
    if not m:
        return os.path.exists(ap)  # not a release asset (yet): whatever the checkout holds
    mark = ap + ".asset"
    try:
        seen = open(mark, encoding="utf-8").read().strip()
    except OSError:
        seen = ""
    if os.path.exists(ap) and (seen == m["sha256"] or sha256(ap) == m["sha256"]):
        return True
    os.makedirs(os.path.dirname(ap), exist_ok=True)
    tmp, ok = ap + ".dl", False
    if shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")):
        try:
            d = tmp + ".d"
            shutil.rmtree(d, ignore_errors=True)
            r = subprocess.run(["gh", "release", "download", m["tag"], "-R", REPO, "-p", m["asset"], "-D", d, "--clobber"], capture_output=True, text=True, timeout=1800)
            f = os.path.join(d, m["asset"])
            if r.returncode == 0 and os.path.exists(f):
                os.replace(f, tmp)
                ok = True
            shutil.rmtree(d, ignore_errors=True)
        except Exception:
            ok = False
    if not ok:
        try:
            req = urllib.request.Request("https://github.com/%s/releases/download/%s/%s" % (REPO, m["tag"], m["asset"]), headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=900) as r, open(tmp, "wb") as o:
                shutil.copyfileobj(r, o, 1 << 22)
            ok = os.path.getsize(tmp) > 0
        except Exception as e:
            if not quiet:
                print("state asset %s not downloaded: %s" % (m["asset"], str(e)[:160]), file=sys.stderr)
    if ok:
        os.replace(tmp, ap)
        with open(mark, "w", encoding="utf-8") as f:  # the version the manifest named when this copy was fetched (the asset may be a run newer: fine)
            f.write(m["sha256"])
        return True
    return os.path.exists(ap)


def versioned(name, h):
    """claude_org_extras.jsonl.gz, its SHA-256 -> claude_org_extras.0123456789ab.jsonl.gz"""
    stem, dot, ext = name.partition(".")
    return "%s.%s%s%s" % (stem, h[:12], dot, ext)


def prune(tag, name, keep, min_age_h=3.0, newest=3):
    """delete old versions of the state file `name` from release `tag`. Kept: the names in `keep`, every version younger than `min_age_h`
    hours (another run may have uploaded it and be about to push its manifest line), the `newest` newest. Never raises."""
    try:
        stem, dot, ext = name.partition(".")
        pat = re.compile(r"^%s\.[0-9a-f]{12}%s$" % (re.escape(stem), re.escape(dot + ext)))
        r = subprocess.run(["gh", "api", "repos/%s/releases/tags/%s" % (REPO, tag), "--jq", ".id"], capture_output=True, text=True, timeout=120)
        rid = r.stdout.strip()
        if r.returncode != 0 or not rid.isdigit():
            return 0
        r = subprocess.run(["gh", "api", "--paginate", "repos/%s/releases/%s/assets?per_page=100" % (REPO, rid), "--jq", ".[] | [.id, .name, .created_at] | @tsv"],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            return 0
        vers = []
        for l in r.stdout.splitlines():
            f = l.split("\t")
            if len(f) == 3 and pat.match(f[1]):
                vers.append((calendar.timegm(time.strptime(f[2][:19], "%Y-%m-%dT%H:%M:%S")), f[0], f[1]))
        vers.sort(reverse=True)
        n = 0
        for t, aid, an in vers[newest:]:
            if an in keep or time.time() - t < min_age_h * 3600:
                continue
            d = subprocess.run(["gh", "api", "-X", "DELETE", "repos/%s/releases/assets/%s" % (REPO, aid)], capture_output=True, text=True, timeout=120)
            n += d.returncode == 0
        if n:
            print("state asset %s: %d old version(s) deleted, %d kept" % (name, n, len(vers) - n))
        return n
    except Exception as e:
        print("state asset %s: old versions not looked at (%s)" % (name, str(e)[:120]))
        return 0


def publish(paths, tag="harvest-state", save=None):
    """upload each file as an asset of `tag` — a name of its own per version — and record it in the manifest; returns the files published.
    save: a JSON file that receives only the entries written by this call (a push-retry loop resets the tree and writes them back with `restore`)"""
    m, done = manifest(), []
    for p in paths:
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            print("state asset %s: no such file, skipped" % p)
            continue
        name, h = os.path.basename(p), sha256(p)
        vname = versioned(name, h)
        before = (m.get(rel(p)) or {}).get("asset") or ""
        with tempfile.TemporaryDirectory() as td:
            vp = os.path.join(td, vname)
            try:
                os.link(p, vp)
            except OSError:
                shutil.copyfile(p, vp)
            for attempt in range(3):
                r = subprocess.run(["gh", "release", "upload", tag, vp, "-R", REPO, "--clobber"], capture_output=True, text=True)
                if r.returncode == 0:
                    break
                time.sleep(8 * (attempt + 1))
            else:
                print("state asset %s: upload failed — %s" % (vname, (r.stderr or r.stdout).strip()[:300]))
                continue
        m[rel(p)] = {"tag": tag, "asset": vname, "bytes": os.path.getsize(p), "sha256": h, "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        with open(os.path.abspath(p) + ".asset", "w", encoding="utf-8") as f:
            f.write(h)
        done.append(p)
        print("state asset %s -> release %s (%.1f MB)" % (vname, tag, os.path.getsize(p) / 1e6))
        prune(tag, name, {vname, before})
    if done:
        with open(MANIFEST, "w", encoding="utf-8") as f:
            json.dump(dict(sorted(m.items())), f, indent=1)
            f.write("\n")
        if save:
            with open(save, "w", encoding="utf-8") as f:
                json.dump({rel(p): m[rel(p)] for p in done}, f)
    return done


def record(entries):
    """merge manifest entries produced on another checkout state (a push-retry loop resets the tree: the entries are kept aside and written back)"""
    m = manifest()
    m.update(entries)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(m.items())), f, indent=1)
        f.write("\n")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    args = sys.argv[2:]
    if cmd == "publish":
        tag, save = "harvest-state", None
        if "--tag" in args:
            i = args.index("--tag")
            tag = args[i + 1]
            args = args[:i] + args[i + 2:]
        if "--save" in args:
            i = args.index("--save")
            save = args[i + 1]
            args = args[:i] + args[i + 2:]
        ok = publish(args, tag, save)
        sys.exit(0 if len(ok) == len(args) else 1)
    elif cmd == "ensure":
        bad = [p for p in args if not ensure(p, quiet=False)]
        print("state assets: %d ready%s" % (len(args) - len(bad), ("; missing: " + ", ".join(bad)) if bad else ""))
        sys.exit(1 if bad else 0)
    elif cmd == "restore":  # write the entries of a saved manifest (JSON file) into the current one: used inside push-retry loops
        record(json.load(open(args[0], encoding="utf-8")))
    else:
        for k, v in sorted(manifest().items()):
            print("%-60s %s/%s %8.1f MB %s" % (k, v["tag"], v["asset"], v["bytes"] / 1e6, v["updated"]))

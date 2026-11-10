#!/usr/bin/env python3
"""Publish a rank build: the bulky files become RELEASE ASSETS (tag ranked-latest); git keeps what a person reads.

Why (measured 2026-11-10): 5.4 GB of new git objects in 24 hours — package CSVs 1.5 GB, the ranked table 1.0 GB, the contracts export 0.5 GB —
and a repository of 8.9 GB after ten days; the table is meant to grow tenfold. "Big data is in GitHub Releases, not git" (AGENTS.md §3) now
holds for the deliverable too.

  python3 tools/ranked_publish.py out/ranked --tag ranked-latest --git-dir coord/results/ranked

Release assets (same names every build, replaced in place):
  ranked_buyers.csv.gz        the whole table, one row per buyer              ranked_buyers.jsonl.gz   the same rows as JSON lines
  ranked_batches.zip          every package CSV (ranked_batches_2.zip … when one zip would pass 1.8 GB)
  ranked_contracts.zip        contracts of the delivered buyers               ranked_extras.zip        audit flags, DMARC list, rows changed
  BUILD.json                  build id, time, row counts, each asset's size and SHA-256
In git (--git-dir): the build's *.md / *.json reports, BUILD.json, WHERE.md (links), batches_head/<package>.csv (first 10 rows of each package).
Exit code 0 only when every asset was uploaded; the caller then commits --git-dir. Needs `gh` and GH_TOKEN (the workflow's own token).
"""
import argparse, collections, csv, glob, gzip, hashlib, json, os, re, shutil, subprocess, sys, time, zipfile

csv.field_size_limit(1 << 30)
REPO = os.environ.get("GITHUB_REPOSITORY") or "mohamedbiranesy-gif/canada-contracts-hub"
ZIP_LIMIT = 1_800_000_000
HEAD_ROWS = 10


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()


def run(*cmd, check=True):
    r = subprocess.run(list(cmd), capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("%s -> %s" % (" ".join(cmd)[:160], (r.stderr or r.stdout).strip()[:400]))
    return r


def zips(files, base, out):
    """files -> base.zip (or base.zip, base_2.zip … so that no archive passes ZIP_LIMIT of raw input / 5, a safe bound for CSV text)"""
    made, cur, size, k = [], None, 0, 1

    def start():
        nonlocal cur, size
        name = "%s%s.zip" % (base, "" if k == 1 else "_%d" % k)
        cur = zipfile.ZipFile(os.path.join(out, name), "w", zipfile.ZIP_DEFLATED, compresslevel=6)
        made.append(os.path.join(out, name))
        size = 0
    for f in files:
        if cur is None:
            start()
        elif size and size + os.path.getsize(f) > ZIP_LIMIT * 5:
            cur.close()
            k += 1
            start()
        cur.write(f, os.path.basename(f))
        size += os.path.getsize(f)
    if cur is not None:
        cur.close()
    return made


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--tag", default="ranked-latest")
    ap.add_argument("--git-dir", default="coord/results/ranked")
    ap.add_argument("--dry", action="store_true", help="build the assets and the git folder, upload nothing")
    a = ap.parse_args()
    src = a.src.rstrip("/")
    pub = os.path.join(os.path.dirname(os.path.abspath(src)), "ranked_pub")
    shutil.rmtree(pub, ignore_errors=True)
    os.makedirs(pub)
    table = os.path.join(src, "ranked_buyers.csv.gz")
    if not os.path.exists(table) or os.path.getsize(table) < 1000:
        raise SystemExit("no ranked table in %s" % src)
    assets = []
    shutil.copy(table, os.path.join(pub, "ranked_buyers.csv.gz"))
    assets.append(os.path.join(pub, "ranked_buyers.csv.gz"))
    if os.path.exists(os.path.join(src, "ranked_buyers.jsonl.gz")):
        shutil.copy(os.path.join(src, "ranked_buyers.jsonl.gz"), os.path.join(pub, "ranked_buyers.jsonl.gz"))
        assets.append(os.path.join(pub, "ranked_buyers.jsonl.gz"))
    batch_files = sorted(glob.glob(os.path.join(src, "batches", "*.csv")))
    assets += zips(batch_files, "ranked_batches", pub)
    contract_files = sorted(glob.glob(os.path.join(src, "contracts", "*")))
    if contract_files:
        assets += zips(contract_files, "ranked_contracts", pub)
    extras = [p for p in (os.path.join(src, n) for n in ("audit_flags.csv", "dmarc_no_enforcement.csv", "rows_changed.csv")) if os.path.exists(p)]
    if extras:
        assets += zips(extras, "ranked_extras", pub)
    # counts: rows, tiers, packages
    tiers, n_rows, n_mail = collections.Counter(), 0, 0
    with gzip.open(table, "rt", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            n_rows += 1
            if (r.get("email") or "").strip():
                n_mail += 1
                tiers[r.get("tier") or "?"] += 1
    packages = collections.OrderedDict()
    for p in batch_files:
        name = re.sub(r"_part\d+_of_\d+$", "", os.path.basename(p)[:-4])
        with open(p, encoding="utf-8", newline="") as f:
            packages[name] = packages.get(name, 0) + sum(1 for _ in csv.reader(f)) - 1
    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sha = (run("git", "rev-parse", "--short", "HEAD", check=False).stdout or "").strip()
    build = {"id": "%s-%s" % (stamp, sha), "built": stamp, "code": sha, "release": a.tag, "rows": n_rows, "rows_with_mailbox": n_mail, "by_tier": dict(sorted(tiers.items())),
             "packages": packages, "assets": [{"name": os.path.basename(p), "bytes": os.path.getsize(p), "sha256": sha256(p),
                                               "url": "https://github.com/%s/releases/download/%s/%s" % (REPO, a.tag, os.path.basename(p))} for p in assets]}
    with open(os.path.join(pub, "BUILD.json"), "w", encoding="utf-8") as f:
        json.dump(build, f, indent=1)
    assets.append(os.path.join(pub, "BUILD.json"))
    print("build %s: %d rows (%d with a mailbox); assets: %s" % (build["id"], n_rows, n_mail, ", ".join("%s %.0f MB" % (os.path.basename(p), os.path.getsize(p) / 1e6) for p in assets)), flush=True)
    if not a.dry:
        if run("gh", "release", "view", a.tag, "-R", REPO, check=False).returncode != 0:
            notes = ("The current build of the ranked buyers deliverable: the whole table, every package, the contracts export. Replaced in place by every run of the "
                     "rank-buyers workflow; coord/results/ranked/BUILD.json in the repository says which build this is.")
            run("gh", "release", "create", a.tag, "-R", REPO, "--title", "Ranked buyers — current build", "--notes", notes, "--latest=false")
        for p in assets:
            for attempt in range(3):
                r = run("gh", "release", "upload", a.tag, p, "-R", REPO, "--clobber", check=False)
                if r.returncode == 0:
                    break
                time.sleep(10 * (attempt + 1))
            else:
                raise SystemExit("upload failed: %s — %s" % (os.path.basename(p), (r.stderr or r.stdout).strip()[:300]))
        # assets of an earlier, larger build that this one no longer has (ranked_batches_3.zip …) would be stale: remove them
        try:
            cur = json.loads(run("gh", "api", "repos/%s/releases/tags/%s" % (REPO, a.tag)).stdout)
            keep = {os.path.basename(p) for p in assets}
            for x in cur.get("assets") or []:
                if x["name"] not in keep and re.fullmatch(r"ranked_(batches|contracts|extras)(_\d+)?\.zip", x["name"]):
                    run("gh", "api", "-X", "DELETE", "repos/%s/releases/assets/%s" % (REPO, x["id"]), check=False)
        except Exception as e:
            print("stale-asset check skipped: %s" % str(e)[:200])
        print("uploaded %d assets to release %s" % (len(assets), a.tag), flush=True)
    # ---- what git keeps
    g = a.git_dir.rstrip("/")
    shutil.rmtree(g, ignore_errors=True)
    os.makedirs(os.path.join(g, "batches_head"))
    for p in sorted(glob.glob(os.path.join(src, "*.md")) + glob.glob(os.path.join(src, "*.json"))):
        shutil.copy(p, g)
    if os.path.exists(os.path.join(src, "contracts", "CONTRACTS.md")):
        shutil.copy(os.path.join(src, "contracts", "CONTRACTS.md"), os.path.join(g, "CONTRACTS.md"))
    shutil.copy(os.path.join(pub, "BUILD.json"), os.path.join(g, "BUILD.json"))
    done = set()
    for p in batch_files:
        name = re.sub(r"_part\d+_of_\d+$", "", os.path.basename(p)[:-4])
        if name in done:
            continue
        done.add(name)
        with open(p, encoding="utf-8", newline="") as f, open(os.path.join(g, "batches_head", name + ".csv"), "w", encoding="utf-8", newline="") as o:
            w = csv.writer(o)
            for i, row in enumerate(csv.reader(f)):
                if i > HEAD_ROWS:
                    break
                w.writerow(row)
    L = ["# Where the deliverable is", "",
         "Build **%s** — %d rows, %d with a mailbox. Tiers (rows with a mailbox): %s." % (build["id"], n_rows, n_mail, ", ".join("%s %d" % kv for kv in sorted(tiers.items()))), "",
         "The files are **release assets**, not files of this folder (a build is several hundred MB; committing each one grew the repository by gigabytes a day):", "",
         "**https://github.com/%s/releases/tag/%s**" % (REPO, a.tag), "", "| File | Size | What |", "|---|---|---|"]
    what = {"ranked_buyers.csv.gz": "the whole table, one row per buyer", "ranked_buyers.jsonl.gz": "the same rows as JSON lines", "BUILD.json": "this build: counts, sizes, SHA-256 of every file"}
    for x in build["assets"]:
        w_ = what.get(x["name"]) or ("every package as CSV (%d files)" % len(batch_files) if x["name"].startswith("ranked_batches") else
                                     "contracts of the delivered buyers" if x["name"].startswith("ranked_contracts") else "audit flags, DMARC list, rows changed since the last build")
        L.append("| [%s](%s) | %.1f MB | %s |" % (x["name"], x["url"], x["bytes"] / 1e6, w_))
    L += ["", "## Packages in `ranked_batches.zip`", "", "| Package | Rows |", "|---|---|"] + ["| %s | %d |" % kv for kv in packages.items()]
    L += ["", "`batches_head/` in this folder holds the first %d rows of each package, to look at a package without downloading it. " % HEAD_ROWS +
          "Reports of this build: SUMMARY.md, VALIDATION.md, AUDIT.md, COVERAGE_VS_TARGETS.md, DMARC.md, CHANGELOG.md, CONTRACTS.md.",
          "Tools read the table through `tools/ranked_io.py` (it downloads `ranked_buyers.csv.gz` when a checkout does not have this build)."]
    with open(os.path.join(g, "WHERE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    # the working copy of the NEW table for the readers that run later in this job (untracked: .gitignore)
    shutil.copy(table, os.path.join(g, "ranked_buyers.csv.gz"))
    with open(os.path.join(g, "ranked_buyers.csv.gz.build"), "w", encoding="utf-8") as f:
        f.write(build["id"])
    print("git folder %s: %s" % (g, ", ".join(sorted(os.listdir(g)))), flush=True)


if __name__ == "__main__":
    main()

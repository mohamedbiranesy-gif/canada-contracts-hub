#!/usr/bin/env python3
"""The ranked table in parts (2026-11-10): coord/results/ranked/ranked_buyers.csv.gz was 70 MB at 68,910 rows; GitHub refuses any file over
100 MB, so the push of a build with ~98,000 rows would have failed — and the target is a million rows.

Committed: ranked_buyers.csv.gz.part01, .part02 … — each one a complete gzip member under 45 MB that holds a slice of the rows (the header is
in part 01 only). Concatenated in order they are one valid gzip file with one valid CSV inside, so
    python3 tools/ranked_io.py assemble        # parts -> coord/results/ranked/ranked_buyers.csv.gz (untracked, see .gitignore)
gives every existing reader the file it has always opened. Workflows run it right after checkout.

  split FILE [MB]   FILE -> FILE.part01 … (FILE itself is removed)
  assemble [DIR]    parts in DIR (default coord/results/ranked) -> the single file, when it is missing or older than the parts
  cat [DIR]         the CSV text on stdout (single file or parts)
Python: rows(path) yields dict rows from the single file or from its parts; lines(path) yields the text lines.
"""
import csv, glob, gzip, io, json, os, shutil, subprocess, sys, urllib.request

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT = os.path.join(ROOT, "coord/results/ranked/ranked_buyers.csv.gz")
# 2026-11-10 07:30Z: the build's bulky outputs are RELEASE ASSETS (tag ranked-latest), no longer committed — measured: 5.4 GB of new git objects in
# 24 hours (batches 1.5 GB, this table 1.0 GB, contracts 0.5 GB …) and a repository of 8.9 GB after ten days. git keeps the summaries, BUILD.json
# (which build the release holds) and the first rows of each package. Every reader gets the table through ensure() / lines() / rows() as before.
TAG = "ranked-latest"
REPO = os.environ.get("GITHUB_REPOSITORY") or "mohamedbiranesy-gif/canada-contracts-hub"
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"


def parts_of(path):
    return sorted(glob.glob(path + ".part[0-9][0-9]")) + sorted(glob.glob(path + ".part[0-9][0-9][0-9]"))


def build_id(d):
    try:
        return str(json.load(open(os.path.join(d, "BUILD.json"), encoding="utf-8")).get("id") or "")
    except Exception:
        return ""


def ensure(path=DEFAULT):
    """the single file at `path`: already there (same build as BUILD.json says), or assembled from committed parts (builds before 2026-11-10), or
    downloaded from the release. Only the table's standard place is ever downloaded; any other path is read as given."""
    d = os.path.dirname(path)
    if parts_of(path):
        return True
    if os.path.basename(path) != "ranked_buyers.csv.gz" or os.path.basename(d) != "ranked":
        return os.path.exists(path)
    want = build_id(d)
    try:
        have = open(path + ".build", encoding="utf-8").read().strip()
    except OSError:
        have = ""
    if os.path.exists(path) and os.path.getsize(path) > 1000 and (not want or want == have):
        return True
    if not want and not os.environ.get("RANKED_FETCH"):
        return os.path.exists(path)  # no release build recorded in this checkout: nothing to fetch
    os.makedirs(d, exist_ok=True)
    tmp = path + ".dl"
    ok = False
    if shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")):
        try:
            dl = tmp + ".d"
            shutil.rmtree(dl, ignore_errors=True)
            r = subprocess.run(["gh", "release", "download", TAG, "-R", REPO, "-p", "ranked_buyers.csv.gz", "-D", dl, "--clobber"], capture_output=True, text=True, timeout=1800)
            f = os.path.join(dl, "ranked_buyers.csv.gz")
            if r.returncode == 0 and os.path.exists(f):
                os.replace(f, tmp)
                ok = True
            shutil.rmtree(dl, ignore_errors=True)
        except Exception:
            ok = False
    if not ok:
        try:
            req = urllib.request.Request("https://github.com/%s/releases/download/%s/ranked_buyers.csv.gz" % (REPO, TAG), headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=600) as r, open(tmp, "wb") as o:
                shutil.copyfileobj(r, o, 1 << 22)
            ok = os.path.getsize(tmp) > 1000
        except Exception as e:
            print("ranked table not downloaded from the release: %s" % str(e)[:160], file=sys.stderr)
            ok = False
    if ok:
        os.replace(tmp, path)
        with open(path + ".build", "w", encoding="utf-8") as f:
            f.write(want)
    return os.path.exists(path)


def lines(path=DEFAULT):
    """text lines of the table: its parts when there are any (builds before 2026-11-10), else the single file (fetched from the release when needed)"""
    ps = parts_of(path)
    if not ps:
        ensure(path)
    for p in (ps or ([path] if os.path.exists(path) else [])):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for l in f:
                yield l


def rows(path=DEFAULT):
    return csv.DictReader(lines(path))


def split(path, mb=40):
    limit = int(mb * 1024 * 1024)
    for p in parts_of(path):
        os.remove(p)
    n, k, out, raw = 0, 0, None, None

    def start():
        nonlocal k, out, raw
        k += 1
        raw = open("%s.part%02d" % (path, k), "wb")
        out = gzip.GzipFile(fileobj=raw, mode="wb", compresslevel=6, mtime=0)
    start()
    with gzip.open(path, "rb") as f:
        buf, in_quote = [], False
        for l in f:  # a CSV record may span several lines (quoted newlines): cut only between records
            buf.append(l)
            if l.count(b'"') % 2:
                in_quote = not in_quote
            if in_quote:
                continue
            out.write(b"".join(buf))
            buf, n = [], n + 1
            if n % 500 == 0:
                out.flush()
                if raw.tell() > limit:
                    out.close(); raw.close()
                    start()
        if buf:
            out.write(b"".join(buf))
    out.close(); raw.close()
    os.remove(path)
    print("%s: %d records in %d parts (%s MB)" % (os.path.basename(path), n - 1, k, ", ".join("%.0f" % (os.path.getsize(p) / 2 ** 20) for p in parts_of(path))))


def assemble(path=DEFAULT):
    ps = parts_of(path)
    if not ps:
        return ensure(path)
    if os.path.exists(path) and os.path.getmtime(path) >= max(os.path.getmtime(p) for p in ps) and os.path.getsize(path) == sum(os.path.getsize(p) for p in ps):
        return True
    with open(path + ".tmp", "wb") as o:
        for p in ps:
            with open(p, "rb") as f:
                shutil.copyfileobj(f, o, 1 << 22)
    os.replace(path + ".tmp", path)
    return True


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "assemble"
    if cmd == "split":
        split(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 40)
    elif cmd == "cat":
        d = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(DEFAULT)
        for l in lines(os.path.join(d, "ranked_buyers.csv.gz")):
            sys.stdout.write(l)
    else:
        d = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(DEFAULT)
        ok = assemble(os.path.join(d, "ranked_buyers.csv.gz"))
        print("ranked table: %s" % ("ready" if ok else "not found"))

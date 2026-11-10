#!/usr/bin/env python3
"""Look at a few public pages from a runner (a measurement: nothing is written). The session that plans the engines cannot open arbitrary sites
itself; this prints what a page is before an engine is built for it: robots.txt verdict for our user agent, status, content type, size, the
final address, the start of the page (text of an HTML page, or the raw start with --raw), and the links that match --grep.

  python3 tools/probe.py [--chars 3000] [--raw] [--grep REGEX] URL [URL ...]

One request a second, robots.txt obeyed (a page it disallows is not read), identified user agent.
"""
import argparse, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser, os, gzip

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402


def get(url, limit=3_000_000, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": C.UA, "Accept-Language": "en-CA,en;q=0.9,fr;q=0.8", "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read(limit)
            if r.headers.get("content-encoding") == "gzip" or data[:2] == b"\x1f\x8b":
                try:
                    data = gzip.decompress(data)
                except Exception:
                    try:
                        import zlib
                        data = zlib.decompressobj(47).decompress(data)
                    except Exception:
                        pass
            return r.status, r.headers.get("content-type", ""), data, r.geturl(), ""
    except urllib.error.HTTPError as e:
        try:
            body = e.read(2000)
        except Exception:
            body = b""
        return e.code, e.headers.get("content-type", "") if e.headers else "", body, url, ""
    except Exception as ex:
        return 0, "", b"", url, "%s: %s" % (type(ex).__name__, str(ex)[:160])


_robots = {}


def allowed(url):
    p = urllib.parse.urlparse(url)
    root = "%s://%s/" % (p.scheme, p.netloc)
    if root not in _robots:
        st, _, data, _, err = get(root + "robots.txt", 500_000)
        time.sleep(1)
        rp = None
        if st in (401, 403):
            rp = False
        elif st == 200 and data:
            rp = urllib.robotparser.RobotFileParser()
            rp.parse(data.decode("utf-8", "replace").splitlines())
        _robots[root] = (rp, st, err)
    rp, st, err = _robots[root]
    if rp is False:
        return False, "robots.txt answered %s" % st
    if rp is None:
        return True, "no robots.txt (%s %s)" % (st, err)
    return rp.can_fetch(C.UA, url), "robots.txt read"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--chars", type=int, default=3000)
    ap.add_argument("--raw", action="store_true")
    ap.add_argument("--grep", default="")
    a = ap.parse_args()
    rx = re.compile(a.grep, re.I) if a.grep else None
    for url in a.urls:
        print("=" * 110)
        print(url)
        if url.rstrip("/").endswith("robots.txt"):
            ok, why = True, "the robots file itself"
        else:
            ok, why = allowed(url)
        print("robots:", "allowed" if ok else "DISALLOWED", "(%s)" % why)
        if not ok:
            continue
        st, ct, data, final, err = get(url)
        time.sleep(1)
        print("status %s | %s | %d bytes | final %s %s" % (st, ct, len(data), final, err))
        if not data:
            continue
        text = data.decode("utf-8", "replace")
        is_html = "html" in ct.lower() or "<html" in text[:3000].lower()
        if is_html and not a.raw:
            m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
            print("title:", re.sub(r"\s+", " ", m.group(1)).strip()[:200] if m else "")
            print(C.visible(text)[:a.chars])
        else:
            print(text[:a.chars])
        if rx:
            seen = []
            for m in re.finditer(r"""(?:href|src|content|loc)\s*[=>]\s*["']?([^"'<>\s]+)""", text, re.I):
                u = m.group(1)
                if rx.search(u) and u not in seen:
                    seen.append(u)
            for m in rx.finditer(text):
                s = text[max(0, m.start() - 80):m.end() + 160].replace("\n", " ")
                if len(seen) < 60 and s not in seen:
                    seen.append("… " + s)
            print("-- %d matches of --grep --" % len(seen))
            for u in seen[:60]:
                print("  ", u[:300])


if __name__ == "__main__":
    main()

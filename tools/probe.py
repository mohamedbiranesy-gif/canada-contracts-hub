#!/usr/bin/env python3
"""Look at a few public pages from a runner (a measurement: nothing is written). The session that plans the engines cannot open arbitrary sites
itself; this prints what a page is before an engine is built for it: robots.txt verdict for our user agent, status, content type, size, the
final address, the start of the page (text of an HTML page, or the raw start with --raw), and the links that match --grep.

  python3 tools/probe.py [--chars 3000] [--raw] [--grep REGEX] URL [URL ...]
  python3 tools/probe.py --vet DOMAIN [DOMAIN ...]     a vetting sheet for a software vendor: its home page, then up to five of the pages it
                                                       links itself (terms, legal, privacy, contact, about, pricing) — the passages that state who
                                                       the contracting company is, where it is (Canadian postal codes, governing law) and whether
                                                       a free plan exists. For the vendor table of tools/tech_relationships.py: each entry quotes
                                                       the vendor's own page.

One request a second, robots.txt obeyed (a page it disallows is not read), identified user agent.
"""
import argparse, collections, re, sys, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser, os, gzip

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
            rp.parse(data.decode("utf-8-sig", "replace").splitlines())
        _robots[root] = (rp, st, err)
    rp, st, err = _robots[root]
    if rp is False:
        return False, "robots.txt answered %s" % st
    if rp is None:
        return True, "no robots.txt (%s %s)" % (st, err)
    return rp.can_fetch(C.UA, url), "robots.txt read"


PC = r"[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ \u00a0-]?\d[ABCEGHJ-NPRSTV-Z]\d"
VET = (("address in Canada", re.compile(r"(?<![A-Za-z0-9])" + PC + r"(?![A-Za-z0-9])"), 170, 40),
       ("contracting company", re.compile(r"between you and|agreement between|contract (?:is )?(?:between|with)|(?:[\"“](?:we|us|our|company)[\"”],? ?){1,3}(?:means|refers? to|or)|operated by|"
                                          r"owned (?:and operated )?by|is a (?:corporation|company)|a (?:Canadian|British Columbia|Ontario|Qu[ée]bec|Alberta|Delaware|Nova Scotia) (?:corporation|company)|"
                                          r"doing business as|d/b/a|\bdba\b|entre vous et", re.I), 120, 220),
       ("governing law", re.compile(r"governed by|laws of (?:the )?(?:Province|State)|lois (?:de la province|du Qu[ée]bec)|courts of", re.I), 60, 200),
       ("free plan", re.compile(r"free plan|free forever|forever free|free tier|free account|free version|forfait gratuit|gratuit pour toujours|no credit card|\$0\b|0 ?\$ ?/|free for (?:up to|non)|always free", re.I), 80, 140),
       ("regional entities", re.compile(r"if you (?:are|reside|live) (?:located |based )?(?:in|outside)|customers? (?:located )?(?:in|outside) (?:the )?(?:United States|U\.S\.|Europe|EEA|European|Canada|UK|United Kingdom|Australia)", re.I), 60, 260))
VET_LINK = re.compile(r"terms|conditions|legal|l[ée]gal|tos\b|privacy|confidentialit|contact|about|a-propos|pricing|plans|tarif|prix", re.I)
VET_RANK = (re.compile(r"terms|conditions|tos\b|legal|l[ée]gal", re.I), re.compile(r"contact", re.I), re.compile(r"pricing|plans|tarif|prix", re.I), re.compile(r"privacy|confidentialit", re.I), re.compile(r"about|a-propos", re.I))


def vet_page(url, text):
    vis = C.visible(text)
    for what, rx, before, after in VET:
        seen = []
        for m in rx.finditer(vis):
            q = re.sub(r"\s+", " ", vis[max(0, m.start() - before):m.end() + after]).strip()
            if not any(q[:60] in x or x[:60] in q for x in seen):
                seen.append(q)
            if len(seen) >= (6 if what == "address in Canada" else 4):
                break
        for q in seen:
            print("   [%s] %s" % (what, q))


def vet(dom):
    print("=" * 110)
    print("VENDOR", dom)
    home = "https://%s/" % dom if "//" not in dom else dom
    ok, why = allowed(home)
    if not ok:
        print("robots: DISALLOWED (%s)" % why)
        return
    st, ct, data, final, err = get(home)
    time.sleep(1)
    print("home: status %s | %d bytes | final %s %s" % (st, len(data), final, err))
    if st != 200 or not data:
        return
    text = data.decode("utf-8", "replace")
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    d = re.search(r"""<meta[^>]+name=["']description["'][^>]+content=["']([^"']{10,300})""", text, re.I)
    print("title:", re.sub(r"\s+", " ", m.group(1)).strip()[:160] if m else "", "|", (d.group(1) if d else "")[:220])
    vet_page(final, text)
    host = (urllib.parse.urlparse(final).hostname or "").lower()
    reg = C.registrable(host)
    links = {}
    for mm in re.finditer(r"""(?is)<a\s[^>]*?href\s*=\s*["']([^"'#>]+)["'][^>]*>(.*?)</a>""", text[:2_000_000]):
        u = urllib.parse.urljoin(final, mm.group(1).strip())
        pu = urllib.parse.urlparse(u)
        label = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", mm.group(2))).strip()[:60]
        if pu.scheme not in ("http", "https") or C.registrable((pu.hostname or "").lower()) != reg or not VET_LINK.search(pu.path + " " + label) or re.search(r"\.(pdf|png|jpe?g|svg|zip)$", pu.path, re.I):
            continue
        key = u.split("#")[0].split("?")[0].rstrip("/")
        if key != final.rstrip("/"):
            links.setdefault(key, label)
    ranked = sorted(links.items(), key=lambda kv: (next((i for i, rx in enumerate(VET_RANK) if rx.search(kv[0] + " " + kv[1])), 9), len(kv[0])))
    picked, used = [], collections.Counter()
    for u, label in ranked:
        r = next((i for i, rx in enumerate(VET_RANK) if rx.search(u + " " + label)), 9)
        if used[r] >= (2 if r == 0 else 1):
            continue
        used[r] += 1
        picked.append((u, label))
        if len(picked) >= 5:
            break
    for u, label in picked:
        ok, why = allowed(u)
        if not ok:
            print("-- %s (%s): robots DISALLOWED" % (u, label))
            continue
        st, ct, data, fin, err = get(u)
        time.sleep(1)
        print("-- %s (%s): status %s, %d bytes %s" % (fin, label, st, len(data), err))
        if st == 200 and data:
            vet_page(fin, data.decode("utf-8", "replace"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--vet", action="store_true")
    ap.add_argument("--chars", type=int, default=3000)
    ap.add_argument("--raw", action="store_true")
    ap.add_argument("--grep", default="")
    a = ap.parse_args()
    rx = re.compile(a.grep, re.I) if a.grep else None
    if a.vet:
        for d in a.urls:
            try:
                vet(d)
            except Exception as e:
                print("error: %s %s" % (type(e).__name__, str(e)[:160]))
        return
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

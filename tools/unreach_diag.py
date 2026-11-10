#!/usr/bin/env python3
"""What is behind the home-page scan's verdict "unreachable"? A measurement, not a harvester: nothing is written to the dataset.

The scan (tools/credit_scan.py) asked 3.0 million home pages by 2026-11-10 and 1.29 million ended "unreachable" (1.25 million of them .ca).
Its reader asks https://<domain>/ and falls back to plain http only on a TLS error and to www. only on a DNS error: a domain whose port 443
is closed or silent, or whose bare name is dead while www. works, ends "unreachable" too. So does a name the runner's resolver could not
answer in time. This tool takes a random sample of those domains and, for each one:

  1. asks the resolver for the bare name and for www.            -> no_dns: neither has an address (the domain is gone)
  2. asks robots.txt on https://d/, http://d/, https://www.d/, http://www.d/ in that order, 10 s each, and stops at the first that ANSWERS
     (any HTTP status); robots.txt is obeyed
  3. reads the home page at that root once and puts the site in ONE class

Classes: no_dns | silent (no root answers; the error of the https request is counted) | robots | blocked | http_<code> | not_html |
other_domain (the page is another registrable domain's: a forward) | parked (a registrar's, a seller's or a host's placeholder, or under 25 words) |
site (a page of its own: with / without a role mailbox on the home page, postal address in Canada or not).

  python3 tools/unreach_diag.py --n 5000 [--minutes 30] [--workers 60] [--seed 1]
"""
import argparse, collections, gzip, os, random, re, socket, sys, threading, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C  # noqa: E402
import cc_clients as CCL  # noqa: E402
import credit_scan as CS  # noqa: E402
import lead_crawl as LC  # noqa: E402

PARKED = re.compile(r"domain (?:name )?(?:is|may be|might be) (?:for sale|available)|buy this domain|this domain (?:is|has been) (?:parked|registered|reserved|expired)|parked (?:free|domain|page)|"
                    r"domain parking|ce (?:nom de )?domaine est (?:à|a) vendre|nom de domaine (?:est )?(?:à|a) vendre|domaine (?:est )?stationn|related searches|recherches associ|"
                    r"future home of|website (?:is )?coming soon|site (?:is )?under construction|site web (?:à|a) venir|"
                    r"default web ?site page|apache2? (?:ubuntu |debian )?default page|welcome to nginx|index of /|account (?:has been )?suspended|"
                    r"renew (?:your|this) domain|domain (?:has )?expired", re.I)
# words of a hosting company's placeholder: they only count on a page of fewer than 120 words
PARKED_WEAK = re.compile(r"coming soon|under construction|en construction|bient[ôo]t disponible|it works!|web hosting|h[ée]bergement|plesk|cpanel|sedo|afternic|hugedomains|bodis|parkingcrew|godaddy", re.I)
PARK_HOST = re.compile(r"(?:^|\.)(?:sedo|sedoparking|afternic|hugedomains|dan|bodis|parkingcrew|above|uniregistry|godaddy|secureserver|namecheap|domainmarket|buydomains|undeveloped|"
                       r"squadhelp|atom|brandbucket|namebright|epik|domains?\.[a-z]+|webnames|rebel|hover|namespro|whois)\.[a-z.]+$", re.I)


def err_word(ex):
    m = (str(ex) + " " + type(ex).__name__).lower()
    for word, keys in (("dns_temp", ("temporary failure",)), ("dns", ("name or service", "nodename", "getaddrinfo", "no address")), ("timeout", ("timed out", "timeout")),
                       ("refused", ("refused",)), ("reset", ("reset by peer", "connection reset")), ("tls_cert", ("certificate", "hostname")),
                       ("tls_other", ("ssl", "handshake", "eof")), ("no_route", ("unreachable", "no route")), ("remote_closed", ("remote end closed", "remotedisconnected", "badstatusline"))):
        if any(k in m for k in keys):
            return word
    return "other:" + type(ex).__name__


def raw_get(url, limit=600_000, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": C.UA, "Accept-Language": "fr-CA,fr;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.headers.get("content-type", ""), r.read(limit), r.geturl(), ""
    except urllib.error.HTTPError as e:
        return e.code, "", b"", url, ""
    except Exception as ex:
        return 0, "", b"", url, err_word(ex)


def addrs(host):
    for attempt in (0, 1):
        try:
            return sorted({x[4][0] for x in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}), ""
        except socket.gaierror as e:
            if e.errno == socket.EAI_AGAIN and attempt == 0:
                time.sleep(1.5)
                continue
            return [], "temp" if e.errno == socket.EAI_AGAIN else "none"
        except Exception:
            return [], "none"
    return [], "none"


def home_mailbox(raw, fhost, name):
    text, best = C.visible(raw), ""
    for e in C.page_emails(raw[:600_000]):
        if e.rsplit(".", 1)[-1] in ("png", "jpg", "jpeg", "gif", "svg", "webp") or not LC.ok_mailbox(e):
            continue
        try:
            if not C.same_org(e, "https://%s/" % fhost, name or ""):
                continue
            i = C.find_tok(text, e)
            kind = C.classify(e, text[max(0, i - 400):i + 400] if i >= 0 else "", "any")
        except Exception:
            continue
        if kind and (not best or C.RANK[kind] < C.RANK[best]):
            best = kind
    return best, bool(CCL.ADDR.search(text)), len(text.split())


def one(dom):
    """dict: class, root that answered, error of the https request on the bare name, addresses"""
    out = {"d": dom, "cls": "", "root": "", "e0": "", "ip": "", "em": "", "ca": 0, "to": ""}
    ip_b, why_b = addrs(dom)
    ip_w, why_w = addrs("www." + dom) if not dom.startswith("www.") else ([], "none")
    out["ip"] = (ip_b or ip_w or [""])[0]
    if not ip_b and not ip_w:
        out["cls"] = "no_dns_temp" if "temp" in (why_b, why_w) else "no_dns"
        return out
    out["dns"] = "both" if ip_b and ip_w else "bare_only" if ip_b else "www_only"
    roots = [("https_bare", "https://%s/" % dom), ("http_bare", "http://%s/" % dom)] if ip_b else []
    roots += [("https_www", "https://www.%s/" % dom), ("http_www", "http://www.%s/" % dom)] if ip_w else []
    answered, allowed = None, True
    for tag, root in roots:
        st, _, data, _, err = raw_get(root + "robots.txt", 300_000)
        if tag == roots[0][0]:
            out["e0"] = err or ("http_%d" % st)
        if st == 0:
            time.sleep(0.5)
            continue
        answered = (tag, root)
        if st in (401, 403):
            allowed = False
        elif st == 200 and data:
            rp = urllib.robotparser.RobotFileParser()
            try:
                rp.parse(data.decode("utf-8", "replace").splitlines())
                allowed = rp.can_fetch(C.UA, root)
            except Exception:
                allowed = True
        break
    if not answered:
        out["cls"] = "silent"
        return out
    out["root"] = answered[0]
    if not allowed:
        out["cls"] = "robots"
        return out
    time.sleep(0.5)
    st, ctype, data, final, err = raw_get(answered[1], 1_500_000)
    head = data[:20000].decode("utf-8", "replace") if data else ""
    if st == 0:
        out["cls"] = "page_" + err
        return out
    if st in (401, 403, 429) or (st == 503 and C.BLOCK_RX.search(head)) or (C.BLOCK_RX.search(head) and len(data) < 30000):
        out["cls"] = "blocked"
        return out
    if st != 200 or not data:
        out["cls"] = "http_%d" % st
        return out
    if data[:5] == b"%PDF-" or "pdf" in (ctype or "").lower() or ("html" not in (ctype or "html").lower() and b"<html" not in data[:3000].lower()):
        out["cls"] = "not_html"
        return out
    fhost = (urllib.parse.urlparse(final).hostname or "").lower()
    raw = CS.html.unescape(CS.decode(data, ctype))
    if C.registrable(fhost) != C.registrable(dom):
        out["cls"], out["to"] = "other_domain_parking" if PARK_HOST.search(fhost) else "other_domain", C.registrable(fhost)
        return out
    try:
        em, ca, words = home_mailbox(raw, fhost, "")
    except Exception:
        em, ca, words = "", False, 0
    text = C.visible(raw)
    if words < 25 or (words < 400 and PARKED.search(text)) or PARKED.search(text[:300]) or (words < 120 and PARKED_WEAK.search(text)):
        out["cls"] = "parked"
        return out
    out["cls"], out["em"], out["ca"] = "site", em, int(ca)
    return out


def sample(n, seed, tld):
    last = {}
    for l in CS.state_lines("done"):
        q = l.split("\t")
        if len(q) > 2:
            last[q[0].strip()] = q[2]
    pool = sorted(d for d, st in last.items() if st == "unreachable" and d.endswith("." + tld) and not d.startswith("www."))
    random.Random(seed).shuffle(pool)
    return pool[:n], len(pool)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5000)
    ap.add_argument("--minutes", type=float, default=30)
    ap.add_argument("--workers", type=int, default=60)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tld", default="ca")
    a = ap.parse_args()
    from concurrent.futures import ThreadPoolExecutor
    doms, pool = sample(a.n, a.seed, a.tld)
    print("unreachable .%s domains on file: %d; sample: %d" % (a.tld, pool, len(doms)), flush=True)
    deadline, res, lock = time.time() + a.minutes * 60, [], threading.Lock()

    def run(d):
        if time.time() > deadline:
            return
        try:
            r = one(d)
        except Exception as ex:
            r = {"d": d, "cls": "error:" + type(ex).__name__, "root": "", "e0": "", "ip": "", "em": "", "ca": 0, "to": ""}
        with lock:
            res.append(r)

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(run, doms))
    n = len(res)
    print("\nread: %d" % n)
    pc = lambda k: "%6d  %5.1f %%" % (k, 100.0 * k / max(n, 1))
    cls = collections.Counter(r["cls"] for r in res)
    print("\n== class ==")
    for k, v in cls.most_common():
        print("  %-28s %s" % (k, pc(v)))
    sites = [r for r in res if r["cls"] == "site"]
    print("\n== sites of their own: %d (%.1f %% of the sample -> %d of the %d on file) ==" % (len(sites), 100.0 * len(sites) / max(n, 1), round(pool * len(sites) / max(n, 1)), pool))
    print("  with a role mailbox on the home page: %d   with a postal address in Canada: %d   both: %d" % (
        sum(1 for r in sites if r["em"]), sum(1 for r in sites if r["ca"]), sum(1 for r in sites if r["em"] and r["ca"])))
    print("  mailbox kinds:", dict(collections.Counter(r["em"] for r in sites if r["em"])))
    print("\n== root that answered first (all that answered) / (sites of their own) ==")
    ra, rs = collections.Counter(r["root"] for r in res if r["root"]), collections.Counter(r["root"] for r in sites)
    for k in ("https_bare", "http_bare", "https_www", "http_www"):
        print("  %-12s %6d  %6d" % (k, ra[k], rs[k]))
    print("\n== error of the https request on the first name, where a later root answered ==")
    for k, v in collections.Counter((r["root"], r["e0"]) for r in res if r["root"] and r["root"] != "https_bare").most_common(20):
        print("  %-12s %-16s %6d" % (k[0], k[1], v))
    print("\n== error of the https request on the first name, where nothing answered ==")
    for k, v in collections.Counter(r["e0"] for r in res if r["cls"] == "silent").most_common(12):
        print("  %-16s %6d" % (k, v))
    print("\n== DNS of the domains that resolve ==", dict(collections.Counter(r.get("dns") for r in res if r.get("dns"))))
    print("\n== most frequent first addresses (count: classes) ==")
    by_ip = collections.defaultdict(collections.Counter)
    for r in res:
        if r["ip"]:
            by_ip[r["ip"]][r["cls"]] += 1
    for ip, c in sorted(by_ip.items(), key=lambda kv: -sum(kv[1].values()))[:25]:
        print("  %-18s %5d  %s" % (ip, sum(c.values()), dict(c.most_common(4))))
    print("\n== forwards: most frequent target domains ==")
    for k, v in collections.Counter(r["to"] for r in res if r["to"]).most_common(25):
        print("  %-32s %5d" % (k, v))
    print("\n== 60 sites of their own (domain, root, error of the https request, mailbox kind, address in Canada) ==")
    for r in sites[:60]:
        print("  %-34s %-10s %-12s %-12s %s" % (r["d"], r["root"], r["e0"], r["em"] or "-", "CA" if r["ca"] else "-"))


if __name__ == "__main__":
    main()

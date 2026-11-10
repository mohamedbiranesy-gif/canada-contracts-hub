#!/usr/bin/env python3
"""Why does the sweep get no answer for half of its questions? One measurement on a runner (workflow dns-diag.yml), no result kept.

2026-11-10: the sweep (tools/dns_services.py sweep) asked 1.1 M domains in a run and got no answer for 600,235 of them (55 %; 61 % the run
before). The same kind of name asked of a public resolver from outside (1,500 two-label .com names of the web graph): 81 % have an address,
14 % do not exist, 1 % fail. So three of four stores in the list are missed. This asks slices of the same list through differently set
resolvers and prints the answer mix and the resolver's own counters for each, so the setting is chosen on a measurement.

    python3 tools/dns_diag.py slice --place 30000000 --n 90000 --out /tmp/slice.txt     # 90,000 names of the list, shuffled (fixed seed)
    python3 tools/dns_diag.py ask --names /tmp/slice.txt --skip 0 --n 12000 --qps 250 --resolver 127.0.0.1:5353 --label "ratelimit 300"
    python3 tools/dns_diag.py ask --names /tmp/slice.txt --skip 60000 --n 6000 --qps 100 --label "public resolvers"
"""
import argparse, collections, gzip, os, random, re, subprocess, sys, threading, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def slice_(a):
    import credit_scan as CS
    import cc_clients as CCL
    import dns_services as D
    rel = CS.newest_graph()
    url = "%sprojects/hyperlinkgraph/%s/domain/%s-domain-vertices.txt.gz" % (CCL.CC, rel, rel)
    vfile = os.path.join(os.environ.get("RUNNER_TEMP") or ".", "vertices.txt.gz")
    subprocess.run(["curl", "-sS", "-L", "--fail", "--retry", "10", "--retry-delay", "10", "--retry-all-errors", "-C", "-", "-A", CCL.UA, "-o", vfile, url], check=True)
    pref = tuple(t + "." for t in D.SWEEP_TLDS)
    ok_name = re.compile(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+")
    pos, out = 0, []
    with gzip.open(vfile, "rt", encoding="utf-8", errors="replace") as fh:
        for l in fh:
            q = l.split("\t")
            if len(q) < 2 or not q[1].startswith(pref):
                continue
            pos += 1
            if pos <= a.place:
                continue
            d = ".".join(reversed(q[1].strip().split(".")))
            if len(d) <= 80 and ok_name.fullmatch(d) and not CS.PLATFORM.search(d):
                out.append(d)
                if len(out) >= a.n:
                    break
    random.Random(7).shuffle(out)
    open(a.out, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("slice: %d names of graph %s after place %d (first: %s)" % (len(out), rel, a.place, ", ".join(out[:4])), flush=True)


def ask(a):
    import dns.exception
    import dns.resolver
    names = [l.strip() for l in open(a.names, encoding="utf-8") if l.strip()][a.skip:a.skip + a.n]
    local = None
    if a.resolver:
        host, _, port = a.resolver.partition(":")
        local = (host, int(port or 53))
    public = ["1.1.1.1", "8.8.8.8", "9.9.9.9", "1.0.0.1", "8.8.4.4", "149.112.112.112"]
    tl, gate, nxt = threading.local(), threading.Lock(), [0.0]

    def turn():
        with gate:
            t = max(time.time(), nxt[0])
            nxt[0] = t + 1.0 / a.qps
        w = t - time.time()
        if w > 0:
            time.sleep(w)
        r = getattr(tl, "r", None)
        if r is None:
            r = dns.resolver.Resolver(configure=False)
            if local:
                r.nameservers, r.port, r.timeout, r.lifetime = [local[0]], local[1], a.lifetime, a.lifetime
            else:
                r.nameservers, r.timeout, r.lifetime = random.sample(public, 3), 2.5, 5.0
            tl.r = r
        return r

    def one(d):
        r = turn()
        t0 = time.time()
        try:
            ans = r.resolve(d, "A", raise_on_no_answer=False)
            how = "ok" if ans.rrset is not None else "none"
        except dns.resolver.NXDOMAIN:
            how = "nx"
        except dns.resolver.NoNameservers:
            how = "servfail"
        except dns.exception.Timeout:
            how = "timeout"
        except dns.exception.DNSException as e:
            how = "other:" + type(e).__name__
        return how, time.time() - t0

    from concurrent.futures import ThreadPoolExecutor
    st, lat = collections.Counter(), collections.defaultdict(list)
    t0 = time.time()
    with ThreadPoolExecutor(a.workers) as ex:
        for how, dt in ex.map(one, names):
            st[how] += 1
            lat[how].append(dt)
    el = time.time() - t0
    n = max(1, len(names))
    med = lambda v: sorted(v)[len(v) // 2] if v else 0
    print("== %s: %d names in %.0f s (%.0f a second, asked for %d): %s" % (
        a.label, len(names), el, len(names) / el, a.qps, ", ".join("%s %.1f %% (median %.2f s)" % (k, 100 * v / n, med(lat[k])) for k, v in st.most_common())), flush=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("slice"); s.add_argument("--place", type=int, default=30_000_000); s.add_argument("--n", type=int, default=90000); s.add_argument("--out", required=True)
    s.set_defaults(fn=slice_)
    s = sub.add_parser("ask"); s.add_argument("--names", required=True); s.add_argument("--skip", type=int, default=0); s.add_argument("--n", type=int, default=12000)
    s.add_argument("--qps", type=float, default=250); s.add_argument("--workers", type=int, default=300); s.add_argument("--resolver", default="")
    s.add_argument("--lifetime", type=float, default=6.0); s.add_argument("--label", default="")
    s.set_defaults(fn=ask)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

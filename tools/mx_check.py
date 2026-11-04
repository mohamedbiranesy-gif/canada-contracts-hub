#!/usr/bin/env python3
"""Does the mailbox's domain publish a mail server? DNS only (MX, else A/AAAA per RFC 5321 §5.1) — never an SMTP probe.

Learning taken from the owner's earlier extract (contrib/claude/pool_audit/README.md): a delivered address whose domain
has no mail server cannot receive the survey. Reads the e-mail domains of coord/results/ranked/ranked_buyers.csv (and any
extra CSV/TSV given), writes <repo>/data/incoming/claude/claude_mx_check.tsv: domain, status (mx | a_only | none | error),
mail_hosts, checked_date. contrib/claude/rank_buyers/rank.py blanks the mailbox of a `none` domain (the row stays, as Z).
  python3 tools/mx_check.py [--repo ~/cch-crawler] [--workers 32] [--recheck-days 7] [extra.csv ...]
"""
import argparse, csv, os, subprocess, sys, threading, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

try:
    import dns.resolver as _dns
except Exception:
    _dns = None
TODAY = time.strftime("%Y-%m-%d")
lock = threading.Lock()


def dig(domain, rtype):
    try:
        out = subprocess.run(["dig", "+short", "+time=5", "+tries=2", rtype, domain], capture_output=True, text=True, timeout=20).stdout
        return [l.strip() for l in out.splitlines() if l.strip() and not l.startswith(";")]
    except Exception:
        return None


def lookup_via(domain, nameserver):
    """the same lookup through one public resolver (dnspython only; dig fallback uses @nameserver)"""
    if _dns:
        return lookup(domain, nameserver)
    mx = None
    try:
        out = subprocess.run(["dig", "+short", "+time=5", "+tries=2", "@" + nameserver, "MX", domain], capture_output=True, text=True, timeout=20).stdout
        mx = [l.strip() for l in out.splitlines() if l.strip()]
    except Exception:
        return "error", "dig failed"
    hosts = [l.split()[-1].rstrip(".") for l in mx if len(l.split()) == 2]
    if hosts and hosts not in ([""], ["."]):
        return "mx", ";".join(sorted(hosts)[:4])
    for t in ("A", "AAAA"):
        try:
            if subprocess.run(["dig", "+short", "+time=5", "@" + nameserver, t, domain], capture_output=True, text=True, timeout=20).stdout.strip():
                return "a_only", t
        except Exception:
            pass
    return "none", "no MX, A or AAAA"


def lookup(domain, nameserver=None):
    """(status, hosts)"""
    if _dns:
        res = _dns.Resolver(configure=nameserver is None); res.lifetime = 8; res.timeout = 4
        if nameserver:
            res.nameservers = [nameserver]
        try:
            mx = sorted(str(r.exchange).rstrip(".") for r in res.resolve(domain, "MX"))
            mx = [m for m in mx if m and m != ""]
            if mx:
                return ("none", "null MX") if mx == ["."] or all(m in ("", ".") for m in mx) else ("mx", ";".join(mx[:4]))
        except _dns.NXDOMAIN:
            return "none", "NXDOMAIN"
        except (_dns.NoAnswer, _dns.NoNameservers):
            pass
        except Exception as e:
            return "error", type(e).__name__
        for t in ("A", "AAAA"):
            try:
                if list(res.resolve(domain, t)):
                    return "a_only", t
            except _dns.NXDOMAIN:
                return "none", "NXDOMAIN"
            except Exception:
                pass
        return "none", "no MX, A or AAAA"
    mx = dig(domain, "MX")
    if mx is None:
        return "error", "dig failed"
    hosts = [l.split()[-1].rstrip(".") for l in mx if len(l.split()) == 2]
    if hosts and hosts != [""]:
        return ("none", "null MX") if hosts == [""] or hosts == ["."] else ("mx", ";".join(sorted(hosts)[:4]))
    for t in ("A", "AAAA"):
        if dig(domain, t):
            return "a_only", t
    return "none", "no MX, A or AAAA"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("files", nargs="*")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--workers", type=int, default=32)
    a.add_argument("--recheck-days", type=int, default=7)
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_mx_check.tsv")
    prev = {}
    if os.path.exists(out):
        for r in csv.DictReader(open(out, encoding="utf-8"), delimiter="\t"):
            prev[r["domain"]] = r
    files = a.files or [os.path.join(a.repo, "coord/results/ranked/ranked_buyers.csv")]
    domains = set()
    import io
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read().replace("\0", "")
        for r in csv.DictReader(io.StringIO(text), delimiter="\t" if f.endswith(".tsv") else ","):
            for col in ("email", "ap_email", "mailbox"):
                e = (r.get(col) or "").strip().lower()
                if "@" in e:
                    domains.add(e.split("@")[-1])
    cutoff = time.strftime("%Y-%m-%d", time.localtime(time.time() - a.recheck_days * 86400))
    todo = sorted(d for d in domains if d not in prev or prev[d]["checked_date"] < cutoff or prev[d]["status"] == "error")
    print("domains: %d, to check: %d" % (len(domains), len(todo)), flush=True)
    stats = {}
    def one(d):
        st, hosts = lookup(d)
        if st in ("none", "error"):  # owner 2026-11-04 ("what about false negatives"): a negative is confirmed by two public resolvers
            confirm = [lookup_via(d, ns) for ns in ("8.8.8.8", "1.1.1.1")]
            if any(c[0] in ("mx", "a_only") for c in confirm):
                st, hosts = next(c for c in confirm if c[0] in ("mx", "a_only"))
                hosts = hosts + " (public resolver)"
            elif all(c[0] == "none" for c in confirm):
                st, hosts = "none", hosts + "; confirmed by 8.8.8.8 and 1.1.1.1"
            else:
                st = "error"
        with lock:
            prev[d] = {"domain": d, "status": st, "mail_hosts": hosts, "checked_date": TODAY}
            stats[st] = stats.get(st, 0) + 1
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["domain", "status", "mail_hosts", "checked_date"], delimiter="\t")
        w.writeheader()
        for d in sorted(prev):
            w.writerow(prev[d])
    os.replace(out + ".tmp", out)
    print("wrote", out, len(prev), "domains", stats, flush=True)


if __name__ == "__main__":
    main()

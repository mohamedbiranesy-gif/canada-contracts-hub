#!/usr/bin/env python3
"""DMARC posture of every delivered mailbox domain (owner 2026-11-04 10:21: "which ones have no DMARC record or p=none").

DNS only (TXT record at _dmarc.<domain>; when the mailbox domain is a subdomain without its own record, the organizational
domain's record applies — its sp= tag for subdomains, else its p= tag). Negatives are confirmed through 8.8.8.8 before
being written as `no_record`. Reads the e-mail column of the CSVs given (default: coord/results/ranked/batches/*.csv) and
writes <repo>/data/incoming/claude/claude_dmarc_check.tsv:
  domain, policy (none | quarantine | reject | no_record | invalid | error), record_domain (where the record was found),
  record (the raw TXT, first 300 chars), pct, rua_present, checked_date
  python3 tools/dmarc_check.py [--repo ~/cch-crawler] [--workers 32] [--recheck-days 30] [file.csv ...]
"""
import argparse, csv, glob, io, os, re, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from ap_crawler import registrable
except Exception:
    def registrable(h):
        p = h.split(".")
        return ".".join(p[-2:]) if len(p) >= 2 else h
try:
    import dns.resolver as _dns
except Exception:
    _dns = None
TODAY = time.strftime("%Y-%m-%d")
lock = threading.Lock()
TAG = re.compile(r"\b(p|sp|pct|rua|v)\s*=\s*([^;]+)", re.I)


def txt(name, nameserver=None):
    """('ok', [records]) | ('none', reason) | ('error', reason)"""
    if not _dns:
        return "error", "dnspython missing"
    res = _dns.Resolver(configure=nameserver is None); res.lifetime = 8; res.timeout = 4
    if nameserver:
        res.nameservers = [nameserver]
    try:
        ans = res.resolve(name, "TXT")
        recs = []
        for r in ans:
            recs.append(b"".join(getattr(r, "strings", [])).decode("utf-8", "replace") if getattr(r, "strings", None) else str(r).strip('"'))
        return "ok", recs
    except (_dns.NXDOMAIN, _dns.NoAnswer):
        return "none", "no TXT"
    except _dns.NoNameservers:
        return "error", "no nameservers"
    except Exception as e:
        return "error", type(e).__name__


def parse(recs):
    """the DMARC record among the TXT strings → (policy, sp, pct, rua_present, raw) or None"""
    for r in recs:
        if re.match(r"\s*v\s*=\s*DMARC1\b", r, re.I):
            tags = {k.lower(): v.strip() for k, v in TAG.findall(r)}
            p = (tags.get("p") or "").lower()
            if p not in ("none", "quarantine", "reject"):
                return "invalid", "", tags.get("pct", ""), "rua" in tags, r
            return p, (tags.get("sp") or "").lower(), tags.get("pct", "100"), "rua" in tags, r
    return None


def check(domain):
    """policy that applies to mail from <domain>"""
    st, recs = txt("_dmarc." + domain)
    if st == "error":
        st2, recs2 = txt("_dmarc." + domain, "8.8.8.8")
        if st2 != "error":
            st, recs = st2, recs2
    if st == "error":
        return {"policy": "error", "record_domain": "", "record": recs, "pct": "", "rua_present": ""}
    found = parse(recs) if st == "ok" else None
    if found:
        pol, sp, pct, rua, raw = found
        return {"policy": pol, "record_domain": domain, "record": raw[:300], "pct": pct, "rua_present": "yes" if rua else "no"}
    org = registrable(domain)
    if org and org != domain:
        st, recs = txt("_dmarc." + org)
        found = parse(recs) if st == "ok" else None
        if found:
            pol, sp, pct, rua, raw = found
            return {"policy": sp or pol, "record_domain": org + " (organizational domain%s)" % ("; sp= applies" if sp else ""), "record": raw[:300], "pct": pct, "rua_present": "yes" if rua else "no"}
    # confirm the negative through a public resolver (owner: "what about false negatives")
    st2, recs2 = txt("_dmarc." + domain, "8.8.8.8")
    found = parse(recs2) if st2 == "ok" else None
    if found:
        pol, sp, pct, rua, raw = found
        return {"policy": pol, "record_domain": domain + " (via 8.8.8.8)", "record": raw[:300], "pct": pct, "rua_present": "yes" if rua else "no"}
    return {"policy": "no_record", "record_domain": "", "record": "no DMARC record at _dmarc.%s%s; confirmed by 8.8.8.8" % (domain, (" or _dmarc." + org) if org and org != domain else ""), "pct": "", "rua_present": ""}


def main():
    a = argparse.ArgumentParser()
    a.add_argument("files", nargs="*")
    a.add_argument("--repo", default=os.path.expanduser("~/cch-crawler"))
    a.add_argument("--workers", type=int, default=32)
    a.add_argument("--recheck-days", type=int, default=30)
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_dmarc_check.tsv")
    prev = {}
    if os.path.exists(out):
        for r in csv.DictReader(open(out, encoding="utf-8"), delimiter="\t"):
            prev[r["domain"]] = r
    files = a.files or sorted(glob.glob(os.path.join(a.repo, "coord/results/ranked/batches/*.csv")))
    domains = set()
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read().replace("\0", "")
        for r in csv.DictReader(io.StringIO(text), delimiter="\t" if f.endswith(".tsv") else ","):
            for col in ("email", "ap_email", "mailbox"):
                e = (r.get(col) or "").strip().lower()
                if "@" in e:
                    domains.add(e.split("@")[-1])
    cutoff = time.strftime("%Y-%m-%d", time.localtime(time.time() - a.recheck_days * 86400))
    todo = sorted(d for d in domains if d not in prev or prev[d]["checked_date"] < cutoff or prev[d]["policy"] == "error")
    print("domains: %d, to check: %d" % (len(domains), len(todo)), flush=True)
    stats = {}
    def one(d):
        try:
            r = check(d)
        except Exception as e:
            r = {"policy": "error", "record_domain": "", "record": type(e).__name__, "pct": "", "rua_present": ""}
        with lock:
            prev[d] = dict(domain=d, checked_date=TODAY, **r)
            stats[r["policy"]] = stats.get(r["policy"], 0) + 1
            if sum(stats.values()) % 2000 == 0:
                print(sum(stats.values()), stats, flush=True)
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["domain", "policy", "record_domain", "record", "pct", "rua_present", "checked_date"], delimiter="\t")
        w.writeheader()
        for d in sorted(prev):
            w.writerow(prev[d])
    os.replace(out + ".tmp", out)
    print("wrote", out, len(prev), "domains", stats, flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""DMARC posture of every delivered mailbox domain (owner 2026-11-04 10:21: "which ones have no DMARC record or p=none").

DNS only (TXT record at _dmarc.<domain>; when the mailbox domain is a subdomain without its own record, the organizational
domain's record applies — its sp= tag for subdomains, else its p= tag). Negatives are confirmed through 8.8.8.8 before
being written as `no_record`. Reads the e-mail column of the CSVs given (default: coord/results/ranked/batches/*.csv) and
writes <repo>/data/incoming/claude/claude_dmarc_check.tsv:
  domain, policy (none | quarantine | reject | no_record | invalid | error), record_domain (where the record was found),
  record (the raw TXT, first 300 chars), pct, rua_present, spf_policy (hard_fail | soft_fail | neutral | pass_all | no_all | no_record), spf_record, checked_date
  python3 tools/dmarc_check.py [--repo ~/cch-crawler] [--workers 32] [--recheck-days 30] [--minutes M] [file.csv | file.csv.gz ...]
The file is written in parts under 40 MB (claude_dmarc_check.tsv, claude_dmarc_check.part02.tsv … — tools/parted_csv.py): 143 bytes a domain,
21 MB at 150,000 domains, over GitHub's 100 MB limit at ~700,000. Readers: parted_csv.rows(path, delimiter="\t").
"""
import argparse, csv, glob, gzip, io, os, re, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parted_csv as PC  # noqa: E402
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
    res = _dns.Resolver(configure=False); res.lifetime = 5; res.timeout = 2.5
    res.nameservers = [nameserver or "1.1.1.1"]  # straight to a public resolver: the Mac's stub resolver serialises bulk lookups
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


SPF_ALL = re.compile(r"(?:^|\s)([-~?+]?)all(?:\s|$)", re.I)


def spf(domain):
    """(policy, record) of the domain's SPF: hard_fail (-all) | soft_fail (~all) | neutral (?all) | pass_all (+all) | no_all | no_record | error"""
    st, recs = txt(domain)
    if st == "error":
        st, recs = txt(domain, "8.8.8.8")
    if st == "error":
        return "error", ""
    rec = next((r for r in (recs if st == "ok" else []) if re.match(r"\s*v=spf1\b", r, re.I)), "")
    if not rec:
        st2, recs2 = txt(domain, "8.8.8.8")
        rec = next((r for r in (recs2 if st2 == "ok" else []) if re.match(r"\s*v=spf1\b", r, re.I)), "")
    if not rec:
        return "no_record", ""
    m = SPF_ALL.search(rec)
    pol = {"-": "hard_fail", "~": "soft_fail", "?": "neutral", "+": "pass_all", "": "pass_all"}[m.group(1)] if m else "no_all"
    return pol, rec[:300]


def txt_first(name, rx):
    st, recs = txt(name)
    if st == "error":
        st, recs = txt(name, "8.8.8.8")
    if st != "ok":
        return ""
    return next((r[:200] for r in recs if re.match(rx, r, re.I)), "")


def check(domain):
    """policy that applies to mail from <domain>, plus the DNS-only transport / brand records (MTA-STS, TLS-RPT, BIMI)"""
    sp, sr = spf(domain)
    r = dmarc(domain)
    r["spf_policy"], r["spf_record"] = sp, sr
    org = registrable(domain) or domain
    r["mta_sts"] = txt_first("_mta-sts." + domain, r"\s*v=STSv1") or (txt_first("_mta-sts." + org, r"\s*v=STSv1") if org != domain else "")
    r["tls_rpt"] = txt_first("_smtp._tls." + domain, r"\s*v=TLSRPTv1") or (txt_first("_smtp._tls." + org, r"\s*v=TLSRPTv1") if org != domain else "")
    r["bimi"] = txt_first("default._bimi." + domain, r"\s*v=BIMI1") or (txt_first("default._bimi." + org, r"\s*v=BIMI1") if org != domain else "")
    for k in ("mta_sts", "tls_rpt", "bimi"):
        r[k] = r[k] or "none"  # checked, no record ('' = not checked yet)
    return r


def dmarc(domain):
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
    a.add_argument("--workers", type=int, default=96)
    a.add_argument("--recheck-days", type=int, default=30)
    a.add_argument("--force", action="store_true", help="re-check every domain (new columns)")
    a.add_argument("--minutes", type=float, default=0, help="stop asking after this many minutes and write what was checked (0 = no limit); the rest is checked by the next run")
    a = a.parse_args()
    out = os.path.join(a.repo, "data/incoming/claude/claude_dmarc_check.tsv")
    prev = {}
    for r in PC.rows(out, delimiter="\t"):
        prev[r["domain"]] = r
    files = a.files or sorted(glob.glob(os.path.join(a.repo, "coord/results/ranked/batches/*.csv")))
    domains = set()
    csv.field_size_limit(1 << 30)
    for f in files:
        # read as a stream (2026-11-10: the whole file was read into memory, three copies of it — the ranked table of 169,769 rows is 2 GB of
        # text and the runner was shut down twice at this step)
        # a .gz file is read as it is (2026-11-10: the previous table was first written out as 2.6 GB of plain text for this step alone)
        with (gzip.open(f, "rt", encoding="utf-8", errors="replace", newline="") if f.endswith(".gz") else open(f, encoding="utf-8", errors="replace", newline="")) as fh:
            for r in csv.DictReader((l.replace("\0", "") for l in fh), delimiter="\t" if f.endswith((".tsv", ".tsv.gz")) else ","):
                for col in ("email", "ap_email", "mailbox"):
                    e = (r.get(col) or "").strip().lower()
                    if "@" in e:
                        domains.add(e.split("@")[-1])
    cutoff = time.strftime("%Y-%m-%d", time.localtime(time.time() - a.recheck_days * 86400))
    todo = sorted(d for d in domains if a.force or d not in prev or prev[d]["checked_date"] < cutoff or prev[d]["policy"] == "error" or "spf_policy" not in prev[d] or "mta_sts" not in prev[d])
    print("domains: %d, to check: %d" % (len(domains), len(todo)), flush=True)
    stats = {}
    deadline = time.time() + a.minutes * 60 if a.minutes else 0
    def one(d):
        if deadline and time.time() > deadline:
            return  # out of time: this domain stays "to check" for the next run
        try:
            r = check(d)
        except Exception as e:
            r = {"policy": "error", "record_domain": "", "record": type(e).__name__, "pct": "", "rua_present": "", "spf_policy": "error", "spf_record": ""}
        with lock:
            prev[d] = dict(domain=d, checked_date=TODAY, **r)
            stats[r["policy"]] = stats.get(r["policy"], 0) + 1
            n = sum(stats.values())
            if n % 2000 == 0:
                print(n, stats, flush=True)
            if n % 5000 == 0:
                write(out, prev)  # resumable: a killed run keeps what it did
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(one, todo))
    write(out, prev)
    left = len(todo) - sum(stats.values())
    print("wrote", out, len(prev), "domains", stats, ("| not reached in %g minutes, left for the next run: %d" % (a.minutes, left)) if left else "", flush=True)


COLS = ["domain", "policy", "record_domain", "record", "pct", "rua_present", "spf_policy", "spf_record", "checked_date", "mta_sts", "tls_rpt", "bimi"]


def write(out, prev):
    PC.write(out, COLS, ([prev[d].get(k, "") for k in COLS] for d in sorted(prev)), delimiter="\t")


if __name__ == "__main__":
    main()

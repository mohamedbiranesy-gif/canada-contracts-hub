#!/usr/bin/env python3
"""One table of every cloud lane, from the files on main (no network): what each engine has read, what it produced, where the funnel narrows.
Run after `git pull`:   python3 tools/lane_status.py [--write coord/LANES.md]
Funnel of a delivered row: site known -> home page read -> relationship (lead) -> role mailbox found -> referee confirms -> rank delivers."""
import argparse, collections, csv, glob, gzip, json, os, re, sys, time

csv.field_size_limit(1 << 30)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
INC = os.path.join(ROOT, "data/incoming/claude")
CS = os.path.join(INC, "credit_scan")


def gz_lines(path):
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for l in f:
            yield l.rstrip("\n")


def lead_kind(cfv, platform=""):
    if cfv.startswith("registry contract"):
        return "R .ca registration"
    if "credited on the buyer's own site" in cfv:
        return "T credit line on the buyer's site"
    if "seen in the buyer's public DNS" in cfv:
        return "T provider in the buyer's DNS"
    if "member badge on the buyer's own site" in cfv:
        return "M membership stated by the member"
    if "(tech)" in cfv:
        return "T vetted software service (store / portal)"
    if "membership / statutory fee relationship" in cfv:
        return "M member / regulated payer list"
    if "vendor located in Canada" in cfv:
        return "D/E listed on a Canadian vendor's page (client, member, dealer, sponsor)"
    return "B/L dated record (payment, subaward, release)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", default="")
    a = ap.parse_args()
    out = []
    P = lambda s="": out.append(s)
    P("# Cloud lanes — status from the files on main (%s UTC)" % time.strftime("%Y-%m-%d %H:%M", time.gmtime()))
    # ---- 1. sites known / read
    P("\n## 1. Sites")
    for name, f in (("`.ca` domains of the archive index", "ca_domains.csv.gz"), ("`.ca` domains of the web graph + public list", "graph_ca_domains.csv.gz"),
                    ("domains linking to a proven Canadian vendor / vetted portal", "graph_inlinks.csv.gz"), ("OpenStreetMap Canada sites", "osm_sites.csv.gz"),
                    ("domains linking to Shopify (store candidates)", "graph_shopify.csv.gz")):
        p = os.path.join(CS, f)
        if os.path.exists(p):
            P("- %s: **%d**" % (name, sum(1 for _ in gz_lines(p)) - 1))
    st, ver, em, cc = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    latest = {}
    for p in sorted(glob.glob(os.path.join(CS, "done_*.gz"))):
        for l in gz_lines(p):
            q = l.split("\t")
            if len(q) > 2:
                latest[q[0]] = q
    for q in latest.values():
        s = q[2].split(":")[0]
        st["http_error" if s.startswith("http_") else s] += 1
        v = next((x for x in q[5:] if re.fullmatch(r"t\d", x)), "t1")
        ver[v] += 1
        if v >= "t4" and s == "ok":
            em[next((x[3:] for x in q[6:] if x.startswith("em=")), "none")] += 1
            cc[next((x[3:] for x in q[6:] if x.startswith("cc=")), "none")] += 1
    P("- home pages read by the scan: **%d** (%s); by detector: %s" % (len(latest), ", ".join("%s %d" % kv for kv in st.most_common(6)), dict(sorted(ver.items()))))
    n4 = sum(em.values())
    if n4:
        with_em = n4 - em["none"]
        P("- detector 4 (readable pages: %d): **%d print a role mailbox of the organisation (%.1f %%)** — %s; printed address: %s"
          % (n4, with_em, 100.0 * with_em / n4, ", ".join("%s %d" % kv for kv in em.most_common(8) if kv[0] != "none"), ", ".join("%s %d" % kv for kv in cc.most_common(5))))
        ca_em = sum(1 for d, q in latest.items() if d.endswith(".ca") and any(x.startswith("em=") for x in q[6:]))
        P("- `.ca` sites whose home page prints a role mailbox (registry candidates, tier R): **%d**" % ca_em)
    # ---- 2. credit scan vendors
    vs = collections.Counter()
    vlatest = {}
    for p in sorted(glob.glob(os.path.join(CS, "vendors_*.gz"))):
        for l in gz_lines(p):
            try:
                o = json.loads(l)
                vlatest[o["dom"]] = o
            except (ValueError, KeyError):
                pass
    for o in vlatest.values():
        vs[(o.get("status") or "?").split(":")[0]] += 1
    P("\n## 2. Vendors and providers checked live (their own site's address)")
    P("- %d domains: %s" % (len(vlatest), ", ".join("%s %d" % kv for kv in vs.most_common(8))))
    # ---- 3. DNS
    dn, shop, cn = 0, 0, 0
    for p in sorted(glob.glob(os.path.join(CS, "dns_*.gz"))):
        for l in gz_lines(p):
            dn += 1
            shop += '"shop": 1' in l
            cn += '"cn": "' in l
    P("\n## 3. DNS lookups")
    P("- domains looked up in the cloud: **%d**; on Shopify's storefront addresses: **%d**; with a www alias: %d" % (dn, shop, cn))
    # ---- 4. leads
    kinds = collections.Counter()
    lead_site, lead_kind_of = {}, {}
    for p in (os.path.join(INC, "claude_buyer_leads_cc.csv"), os.path.join(INC, "claude_buyer_leads.csv")):
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8", errors="replace")):
                k = lead_kind(r.get("canada_field_value") or "")
                kinds[("cloud " if p.endswith("_cc.csv") else "Mac era ") + k] += 1
                lead_kind_of[r["buyer_key"]] = k
    for p in sorted(glob.glob(os.path.join(INC, "tenant_state/leads_*.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                kinds["cloud T vetted software service (store / portal) [shards]"] += 1
                lead_kind_of[r["buyer_key"]] = "T vetted software service (store / portal)"
    P("\n## 4. Relationship leads on file")
    for k, c in sorted(kinds.items()):
        P("- %s: **%d**" % (k, c))
    # ---- 5. mailbox crawl
    P("\n## 5. Mailbox crawl")
    p = os.path.join(INC, "claude_lead_crawl_done.tsv")
    if os.path.exists(p):
        res = collections.Counter()
        by_kind = collections.defaultdict(collections.Counter)
        for l in open(p, encoding="utf-8"):
            q = l.rstrip("\n").split("\t")
            if len(q) > 2:
                s = q[2].split(":")[0]
                res[s] += 1
                by_kind[lead_kind_of.get(q[0], "leads no longer on file (withdrawn by a stricter rule) and registry candidates")][s] += 1
        P("- lead sites read: **%d** (%s)" % (sum(res.values()), ", ".join("%s %d" % kv for kv in res.most_common(6))))
        for k, c in sorted(by_kind.items(), key=lambda kv: -sum(kv[1].values())):
            tot = sum(c.values())
            if tot >= 50:
                P("  - %s: %d read, mailbox on %d (%.0f %%), blocked %d" % (k, tot, c["found"], 100.0 * c["found"] / tot, c["blocked"]))
    td = collections.Counter()
    tl = {}
    lp = os.path.join(INC, "claude_tenant_crawl_done.tsv")
    for l in (open(lp, encoding="utf-8") if os.path.exists(lp) else []):
        q = l.rstrip("\n").split("\t")
        if len(q) > 5:
            tl[q[0]] = q
    for p in sorted(glob.glob(os.path.join(INC, "tenant_state/done_*.gz"))):
        for l in gz_lines(p):
            q = l.split("\t")
            if len(q) > 5:
                tl[q[0]] = q
    for q in tl.values():
        td[(q[5], q[2].split(":")[0])] += 1
    if td:
        P("- candidate sites (stores / portals) read: **%d**" % len(tl))
        for v in sorted({k[0] for k in td}):
            tot = sum(c for (vv, s), c in td.items() if vv == v)
            if tot >= 20:
                P("  - %s: %d read — %s" % (v, tot, ", ".join("%s %d" % (s, c) for (vv, s), c in sorted(td.items(), key=lambda kv: -kv[1]) if vv == v)))
    rows = 0
    for p in sorted(glob.glob(os.path.join(INC, "claude_buyer_ap_results_cccrawl*.csv"))):
        rows += sum(1 for _ in open(p, encoding="utf-8", errors="replace")) - 1
    P("- mailbox rows written by the cloud crawls (before the referee): **%d**" % rows)
    # ---- 6. delivered
    try:
        import ranked_io
        tiers = collections.Counter()
        n = 0
        for r in ranked_io.rows():
            if (r.get("email") or "").strip() and (r.get("email_check") or "").startswith(("confirmed", "cross")):
                tiers[r.get("tier") or "?"] += 1
                n += 1
        P("\n## 6. Delivered (last rank build on main)")
        P("- rows with a confirmed mailbox: **%d** — by tier: %s" % (n, ", ".join("%s %d" % kv for kv in sorted(tiers.items()))))
        P("- named-vendor relationships (A B T M C D L E): **%d** · registry contract R: **%d** · weaker / inferred (F I): **%d**"
          % (sum(c for t, c in tiers.items() if t in "ABTMCDLE"), tiers["R"], tiers["F"] + tiers["I"]))
    except Exception as e:
        P("\n(ranked table not read: %s)" % e)
    text = "\n".join(out) + "\n"
    print(text)
    if a.write:
        with open(os.path.join(ROOT, a.write), "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()

"""CrUX Canada top origins (github.com/zakird/crux-top-lists, data/country/ca/202609.csv.gz, in ~/cch-sources/crux_ca/)
restricted to .ca hosts (CIRA Canadian Presence Requirements) -> ~/cch-crawl-some/crux_ca_new.csv, a crawl_some list that
ap_crawler does NOT read (so it never delays the charity / school batches): one row per registrable .ca domain not yet
crawled / queued / with a mailbox, most popular first. Key crux:<registrable domain>; buyer_name = the domain (CrUX has no
names). Run from ~/cch-crawler: python3 -I contrib/claude/org_task_lists/crux_ca_tasks.py"""
import csv, glob, gzip, io, os, re, urllib.parse, collections
STATE = os.path.expanduser("~/cch-crawler-state")
HDR = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
SL = set("ab.ca bc.ca mb.ca nb.ca nf.ca nl.ca ns.ca nt.ca nu.ca on.ca pe.ca qc.ca sk.ca yk.ca gc.ca".split())
BAD = re.compile(r"porn|sex|xxx|escort|casino|bet|gambl|poker|slot|adult|cam(s|girl)|nude|erotic|dating|hookup|weed|vape|cbd|loan|payday|crypto|torrent", re.I)
def host_of(u):
    u = (u or "").strip()
    if not u or "@" in u.split("/")[0]: return ""
    if not re.match(r"https?://", u, re.I): u = "http://" + u
    try: h = (urllib.parse.urlparse(u).hostname or "").lower().strip(".")
    except ValueError: return ""
    return h[4:] if h.startswith("www.") else h
def reg(h):
    p = h.split(".")
    return ".".join(p[-3:]) if len(p) >= 3 and ".".join(p[-2:]) in SL else ".".join(p[-2:])
seen = set()
for line in open(os.path.join(STATE, "done.tsv"), encoding="utf-8", errors="replace"):
    p = line.rstrip("\n").split("\t")
    if len(p) >= 5 and host_of(p[4]): seen.add(reg(host_of(p[4])))
for path in glob.glob("data/incoming/*/*results*.csv"):
    for r in csv.DictReader(io.StringIO(open(path, encoding="utf-8", errors="replace").read().replace("\0", ""))):
        if host_of(r.get("evidence_url") or ""): seen.add(reg(host_of(r["evidence_url"])))
for path in glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv"):
    for r in csv.DictReader(open(path, encoding="utf-8-sig", errors="replace")):
        if host_of(r.get("known_website") or ""): seen.add(reg(host_of(r["known_website"])))
for r in csv.DictReader(io.StringIO(open("coord/results/org_mailboxes.csv", encoding="utf-8", errors="replace").read().replace("\0", ""))):
    m = (r.get("mailbox") or "").lower()
    if "@" in m: seen.add(reg(m.split("@")[-1].strip()))
out, n_ca, n_bad = {}, 0, 0
for r in csv.DictReader(io.TextIOWrapper(gzip.open(os.path.expanduser("~/cch-sources/crux_ca/202609.csv.gz")), encoding="utf-8")):
    h = host_of(r["origin"])
    if not h.endswith(".ca"): continue
    n_ca += 1
    d = reg(h)
    if d.endswith(".gc.ca") or d == "gc.ca": continue
    if BAD.search(d): n_bad += 1; continue
    if d in seen or d in out: continue
    out[d] = (int(r["rank"]), r["origin"])
rows = sorted(out.items(), key=lambda kv: (kv[1][0], kv[0]))
with open(os.path.expanduser("~/cch-crawl-some/crux_ca_new.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HDR); w.writeheader()
    for i, (d, (rk, origin)) in enumerate(rows):
        w.writerow({"task_id": "CL-CRUX-%06d" % (i + 1), "org_group": "website on a .ca domain (CIRA Canadian Presence Requirements); CrUX Canada top origins 2026-09, rank bucket %d" % rk,
                    "buyer_key": "crux:" + d, "buyer_name": d, "other_spellings": "", "country": "CA", "known_website": origin.rstrip("/") + "/",
                    "known_general_email": "", "known_procurement_email": "", "contracts_in_dataset": ""})
print(".ca origins %d, adult/gambling-like skipped %d, new registrable domains %d" % (n_ca, n_bad, len(rows)), dict(collections.Counter(rk for _, (rk, _) in rows)))

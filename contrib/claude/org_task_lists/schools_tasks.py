"""Ontario private schools (data.ontario.ca 'Private school contact information') + Alberta schools and authorities
(open.alberta.ca 'Alberta schools and authorities') -> coord/tasks/claude/claude_buyer_ap_batch914.csv, one row per
registrable website domain not yet crawled / queued / with a mailbox. Keys onps:<school number>, abed:s<code> / abed:a<code>.
Inputs in ~/cch-sources/schools_ca/ (on_private.csv, ab_schools.xlsx; URLs in contrib/claude/rank_buyers/org_places.py).
Run from ~/cch-crawler: python3 -I contrib/claude/org_task_lists/schools_tasks.py   (needs openpyxl)"""
import csv, glob, io, os, re, urllib.parse
import openpyxl
SRC = os.path.expanduser("~/cch-sources/schools_ca"); STATE = os.path.expanduser("~/cch-crawler-state")
HDR = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
SL = set("ab.ca bc.ca mb.ca nb.ca nf.ca nl.ca ns.ca nt.ca nu.ca on.ca pe.ca qc.ca sk.ca yk.ca gc.ca co.uk org.uk ac.uk com.au".split())
PLATFORM = re.compile(r"(^|\.)(facebook|instagram|twitter|linkedin|youtube|google|sites\.google|wixsite|weebly|blogspot|linktr)\.[a-z.]+$")
def clean(u): return re.sub(r"^www/", "www.", (u or "").strip().strip('"\'').strip().rstrip(".,;"), flags=re.I)
def host_of(u):
    u = clean(u)
    if not u or "@" in u.split("/")[0]: return ""
    if not re.match(r"https?://", u, re.I): u = "http://" + u
    try: h = (urllib.parse.urlparse(u).hostname or "").lower().strip(".")
    except ValueError: return ""
    return h[4:] if h.startswith("www.") else h
def reg(h):
    p = h.split(".")
    return ".".join(p[-3:]) if len(p) >= 3 and ".".join(p[-2:]) in SL else ".".join(p[-2:])
seen = set(); keys = set()
for line in open(os.path.join(STATE, "done.tsv"), encoding="utf-8", errors="replace"):
    p = line.rstrip("\n").split("\t"); keys.add(p[0])
    if len(p) >= 5 and host_of(p[4]): seen.add(reg(host_of(p[4])))
for path in glob.glob("data/incoming/*/*results*.csv"):
    for r in csv.DictReader(io.StringIO(open(path, encoding="utf-8", errors="replace").read().replace("\0", ""))):
        if host_of(r.get("evidence_url") or ""): seen.add(reg(host_of(r["evidence_url"])))
for path in glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv"):
    if path.endswith("batch914.csv"): continue
    for r in csv.DictReader(open(path, encoding="utf-8-sig", errors="replace")):
        if host_of(r.get("known_website") or ""): seen.add(reg(host_of(r["known_website"])))
for r in csv.DictReader(io.StringIO(open("coord/results/org_mailboxes.csv", encoding="utf-8", errors="replace").read().replace("\0", ""))):
    m = (r.get("mailbox") or "").lower()
    if "@" in m: seen.add(reg(m.split("@")[-1].strip()))
cand = []
for r in csv.DictReader(open(os.path.join(SRC, "on_private.csv"), encoding="latin1")):
    cand.append(("onps:" + r["School Number"].strip(), r["School Name"].strip(), r["School Website"],
                 "private school in Ontario (data.ontario.ca Private school contact information; %s ON %s)" % (r["City"].strip(), r["Postal Code"].strip())))
wb = openpyxl.load_workbook(os.path.join(SRC, "ab_schools.xlsx"), read_only=True)
rows = list(wb.worksheets[0].iter_rows(values_only=True)); hdr = rows[2]
auth = {}
for row in rows[3:]:
    d = dict(zip(hdr, row))
    if not d.get("School Code"): continue
    cand.append(("abed:s" + str(d["School Code"]).strip(), (d["School Name"] or "").strip(), d.get("School Website") or "",
                 "school in Alberta (open.alberta.ca Alberta schools and authorities; %s AB %s)" % ((d.get("School City") or "").strip(), (d.get("School Postal Code") or "").strip())))
    if d.get("Authority Code") and d["Authority Code"] not in auth:
        auth[d["Authority Code"]] = 1
        cand.append(("abed:a" + str(d["Authority Code"]).strip(), (d["Authority Name"] or "").strip(), d.get("Authority Website") or "",
                     "school authority in Alberta (open.alberta.ca Alberta schools and authorities; %s AB %s)" % ((d.get("Authority City") or "").strip(), (d.get("Authority Postal Code") or "").strip())))
out, n_web = {}, 0
for k, name, u, grp in cand:
    h = host_of(u)
    if not h or not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", h) or PLATFORM.search(h): continue
    n_web += 1
    d = reg(h)
    if k in keys or d in seen or d in out: continue
    url = clean(u); url = url if re.match(r"https?://", url, re.I) else "http://" + url
    if url == url.upper(): url = re.match(r"https?://[^/?#]+", url, re.I).group(0).lower() + "/"
    out[d] = {"org_group": grp, "buyer_key": k, "buyer_name": name, "other_spellings": "", "country": "CA", "known_website": url,
              "known_general_email": "", "known_procurement_email": "", "contracts_in_dataset": ""}
print("candidates %d, with website %d, new domains %d" % (len(cand), n_web, len(out)))
with open("coord/tasks/claude/claude_buyer_ap_batch914.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HDR); w.writeheader()
    for i, r in enumerate(out.values()): w.writerow(dict(r, task_id="CL-SCH-%05d" % (i + 1)))

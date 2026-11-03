"""CRA registered charities (open.canada.ca 'List of charities' 2022-2024: Identification + Charity Contact Web Addresses)
-> crawler task lists coord/tasks/claude/claude_buyer_ap_batch910.csv ... (one row per registrable website domain not yet crawled).
Key: cra:<BN9>. Inputs downloaded to ~/cch-sources/cra_charities/ (ident_YYYY.csv, weburl_YYYY.csv; URLs in
contrib/claude/rank_buyers/org_places.py). Run from ~/cch-crawler:  python3 -I contrib/claude/org_task_lists/cra_tasks.py [rows_per_batch]"""
import csv, glob, io, os, re, sys, urllib.parse, collections
SRC = os.path.expanduser("~/cch-sources/cra_charities")
STATE = os.path.expanduser("~/cch-crawler-state")
HDR = ["task_id", "org_group", "buyer_key", "buyer_name", "other_spellings", "country", "known_website",
       "known_general_email", "known_procurement_email", "contracts_in_dataset"]
SL = set("ab.ca bc.ca mb.ca nb.ca nf.ca nl.ca ns.ca nt.ca nu.ca on.ca pe.ca qc.ca sk.ca yk.ca gc.ca co.uk org.uk ac.uk com.au org.au net.au".split())
PLATFORM = re.compile(r"(^|\.)(facebook|fb|instagram|twitter|x|linkedin|youtube|youtu|tiktok|canadahelps|gofundme|linktr|eventbrite|google|goo|"
                      r"bit|tinyurl|wa|zeffy|paypal|square|squareup|givebutter|donorbox|blackbaud|flipcause|patreon|meetup|yelp|"
                      r"craigslist|kijiji|amazon|apple|microsoft|outlook|gmail|hotmail|yahoo|ow|t|bitly|forms|jotform|surveymonkey|"
                      r"mailchimp|list-manage|wordpress\.org)\.[a-z.]+$", re.I)
def clean(u):
    u = (u or "").strip().strip('"').strip().strip("'").strip().rstrip(".,;")
    u = re.sub(r"^www/", "www.", u, flags=re.I)
    return u
def host_of(u):
    u = clean(u)
    if not u or "@" in u.split("/")[0]:
        return ""
    if not re.match(r"https?://", u, re.I):
        u = "http://" + u
    try:
        h = (urllib.parse.urlparse(u).hostname or "").lower().strip(".")
    except ValueError:
        return ""
    return h[4:] if h.startswith("www.") else h
def reg(h):
    p = h.split(".")
    if len(p) >= 3 and ".".join(p[-2:]) in SL:
        return ".".join(p[-3:])
    return ".".join(p[-2:])
seen_keys, seen_dom = set(), set()
for line in open(os.path.join(STATE, "done.tsv"), encoding="utf-8", errors="replace"):
    parts = line.rstrip("\n").split("\t")
    seen_keys.add(parts[0])
    if len(parts) >= 5:
        h = host_of(parts[4])
        if h: seen_dom.add(reg(h))
n_done = len(seen_dom)
for path in glob.glob("data/incoming/*/*results*.csv"):
    raw = open(path, encoding="utf-8", errors="replace").read().replace("\0", "")
    for r in csv.DictReader(io.StringIO(raw)):
        h = host_of(r.get("evidence_url") or "")
        if h: seen_dom.add(reg(h))
n_res = len(seen_dom)
for path in glob.glob("coord/tasks/*/*_buyer_ap_batch*.csv"):
    for r in csv.DictReader(open(path, encoding="utf-8-sig", errors="replace")):
        h = host_of(r.get("known_website") or "")
        if h: seen_dom.add(reg(h))
n_tasks = len(seen_dom)
if os.path.exists("coord/results/org_mailboxes.csv"):
    raw = open("coord/results/org_mailboxes.csv", encoding="utf-8", errors="replace").read().replace("\0", "")
    for r in csv.DictReader(io.StringIO(raw)):
        m = (r.get("mailbox") or "").lower()
        if "@" in m: seen_dom.add(reg(m.split("@")[-1].strip()))
print("skip domains: done.tsv %d, +results %d, +queued tasks %d, +org mailboxes %d" % (n_done, n_res, n_tasks, len(seen_dom)))
ident = {}
for y in ("2024", "2023", "2022"):
    for r in csv.DictReader(open(os.path.join(SRC, "ident_%s.csv" % y), encoding="utf-8-sig", errors="replace")):
        bn = (r.get("BN") or "")[:9]
        if bn and bn not in ident:
            ident[bn] = dict(r, year=y)
web = {}
for y in ("2024", "2023", "2022"):
    for r in csv.DictReader(open(os.path.join(SRC, "weburl_%s.csv" % y), encoding="utf-8-sig", errors="replace")):
        bn = (r.get("BN/NE") or "")[:9]
        u = clean(r.get("Contact URL") or "")
        if bn and u and bn not in web and host_of(u):
            web[bn] = (u, y)
print("charities in ident 2022-24: %d; with a web address: %d" % (len(ident), len(web)))
st = collections.Counter()
bydom = {}
for bn, (u, y) in web.items():
    i = ident.get(bn)
    if not i:
        st["no ident row"] += 1; continue
    if (i.get("Country") or "").strip().upper() not in ("CA", ""):
        st["not CA"] += 1; continue
    h = host_of(u)
    if not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", h) or ".." in h:
        st["bad url"] += 1; continue
    if PLATFORM.search(h):
        st["platform"] += 1; continue
    d = reg(h)
    if "cra:" + bn in seen_keys:
        st["key done"] += 1; continue
    if d in seen_dom:
        st["domain already crawled/queued/has mailbox"] += 1; continue
    path = urllib.parse.urlparse(u if re.match(r"https?://", u, re.I) else "http://" + u).path.strip("/")
    cand = (len(path) > 0, h.count("."), bn)
    if d not in bydom or cand < bydom[d][0]:
        if d in bydom: st["same domain as another charity"] += 1
        bydom[d] = (cand, bn, u, h)
    else:
        st["same domain as another charity"] += 1
print("filter:", dict(st), "-> tasks:", len(bydom))
PRI = {"QC": 0, "MB": 0, "SK": 0, "NB": 0, "NU": 0, "BC": 1}  # provinces where P13 infers a utility (higher confidence) first
rows = []
for d, (cand, bn, u, h) in bydom.items():
    i = ident[bn]
    legal = (i.get("Legal Name") or "").strip()
    acct = (i.get("Account Name") or "").strip()
    name = acct or legal
    other = legal if legal and legal.lower() != name.lower() else ""
    url = u if re.match(r"https?://", u, re.I) else "http://" + u  # http: the crawler also tries https://host/
    if url == url.upper() or not re.sub(r"^https?://[^/]+", "", url).strip("/"):
        url = re.match(r"https?://[^/?#]+", url, re.I).group(0).lower() + "/"  # an all-caps path would 404: start at the home page
    else:
        url = re.sub(r"^(https?://)([^/]+)", lambda m: m.group(1).lower() + m.group(2).lower(), url)
    prov = (i.get("Province") or "").strip().upper()
    rows.append((PRI.get(prov, 2), name.lower(), {"org_group": "registered charity in Canada (CRA List of charities %s, Charity Contact Web Addresses; %s %s %s)"
                 % (web[bn][1], (i.get("City") or "").strip().title(), prov, (i.get("Postal Code") or "").strip()),
                 "buyer_key": "cra:" + bn, "buyer_name": name, "other_spellings": other, "country": "CA", "known_website": url,
                 "known_general_email": "", "known_procurement_email": "", "contracts_in_dataset": ""}))
rows.sort(key=lambda x: (x[0], x[1]))
N = int(sys.argv[1]) if len(sys.argv) > 1 else 7000
os.makedirs("coord/tasks/claude", exist_ok=True)
for b in range(0, len(rows), N):
    fn = "coord/tasks/claude/claude_buyer_ap_batch%d.csv" % (910 + b // N)
    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HDR); w.writeheader()
        for j, (_, _, r) in enumerate(rows[b:b + N]):
            w.writerow(dict(r, task_id="CL-CRA-%05d" % (b + j + 1)))
    print(fn, len(rows[b:b + N]))

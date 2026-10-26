#!/usr/bin/env python3
"""Crawl NBON (New Brunswick Opportunities Network, https://nbon-rpanb.gnb.ca/) public "Browse Bid Results" with
Results Type = "Awards Only", one search per date window, paging 30 rows at a time. Anonymous public browsing
(the site's own "Browse Tenders and Awards" link). 1 request/second.

Writes one JSON line per tender (all award rows) to <outdir>/awards.jsonl and the raw result pages (gzipped) to
<outdir>/pages/. Personal e-mail addresses of purchasing agents are NOT stored (project rule: role mailboxes only).
Usage: python3 -I crawl_awards.py <outdir> <YYYY/MM/DD start> <YYYY/MM/DD end> [window_days]
"""
import sys, os, re, json, time, html, gzip, datetime
import requests

outdir, beg, end = sys.argv[1], sys.argv[2], sys.argv[3]
win = int(sys.argv[4]) if len(sys.argv) > 4 else 92
B = "https://nbon-rpanb.gnb.ca/"
os.makedirs(os.path.join(outdir, "pages"), exist_ok=True)
LOG = open(os.path.join(outdir, "crawl.log"), "a")
last = [0.0]


def log(m):
    LOG.write(f"{datetime.datetime.utcnow().isoformat()}Z {m}\n"); LOG.flush()


def throttle():
    w = last[0] + 1.0 - time.time()
    if w > 0:
        time.sleep(w)
    last[0] = time.time()


def new_session():
    s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
    throttle(); r = s.get(B + "welcome", timeout=60)
    sid = re.search(r'id="sessionId" value="(\d+)"', r.text).group(1)
    throttle(); s.get(B + f"submitLogin?sessionID={sid}&User_Name=Anonymous&Language=En&cssStyle=ext/&validate_method=OPEN", timeout=60)
    throttle(); s.get(B + f"showBidResults?sessionID={sid}&fillDates=yes&searchType=Tender&menuName=ExtBrowseBidResultsTender", timeout=60)
    return s, sid


def clean(x):
    x = re.sub(r"<br\s*/?>", "\n", x)
    x = re.sub(r"<[^>]+>", " ", x)
    x = html.unescape(x).replace("\xa0", " ")
    x = re.sub(r"[ \t\r]+", " ", x)
    return "\n".join(l.strip() for l in x.split("\n") if l.strip())


EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
ROLE_RE = re.compile(r"^(procurement|purchasing|tenders?|bids?|info|contracts?|approvisionnement|achats?|appels?|nbon|accountspayable|ap)[\w.-]*@", re.I)


def scrub_contact(text):
    out = []
    for line in text.split("\n"):
        m = EMAIL_RE.search(line)
        if m and not ROLE_RE.match(m.group(0)):
            out.append("[personal e-mail omitted]")
        else:
            out.append(line)
    return out


def parse(page):
    total = re.search(r"<span class=boldText>(\d+)-(\d+)&nbsp;/&nbsp;(\d+)</span>", page)
    qid = re.search(r"queryObjectId=(\d+)", page)
    tenders = []
    # split on tender header rows
    parts = re.split(r'<td style="width:20px;text-align:center;" class="searchResultsNumber">(\d+)</td>\s*<td style="width:100px;" headers="Tender', page)
    # parts: [pre, num1, body1, num2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        num, body = parts[i], parts[i + 1]
        t = {"row_number": int(num)}
        m = re.search(r"disID=(\d+)", body); t["disID"] = m.group(1) if m else None
        m = re.search(r'alt="Open Closed Document Number ([^"]+)"', body) or re.search(r'alt="Open Document Number ([^"]+)"', body)
        t["tender_number"] = html.unescape(m.group(1)).strip() if m else None
        cells = re.findall(r'<td style="width:(\d+)px;" headers="([^"]+)" class="searchResultsBody">(.*?)</td>', body, re.S)
        for w, hdr, val in cells:
            h = re.sub(r"\d+$", "", html.unescape(re.sub(r"<[^>]+>", "", hdr))).strip()
            v = clean(val)
            if h == "Issuing Organization":
                t["issuing_organization"] = v
            elif h == "Purchasing Agent":
                t["purchasing_agent_lines"] = scrub_contact(v)
            elif h == "Closing Date":
                t["closing_date"] = v
        m = re.search(r'class="searchResultsTitle">(.*?)</td>', body, re.S)
        t["title"] = clean(m.group(1)) if m else None
        awards = []
        for vb, tot, dt in re.findall(r'headers="Successful Vendor\d*" class="searchResultsBody">(.*?)</td>\s*<td[^>]*headers="Award Total[^"]*"[^>]*class="searchResultsBody">(.*?)</td>\s*<td[^>]*headers="Date Awarded\d*"[^>]*class="searchResultsBody">(.*?)</td>', body, re.S):
            lines = clean(vb).split("\n")
            awards.append({"vendor_block_lines": lines, "award_total_incl_hst": clean(tot), "date_awarded": clean(dt)})
        t["awards"] = awards
        tenders.append(t)
    return (int(total.group(3)) if total else 0), (qid.group(1) if qid else None), tenders


def search(s, sid, b, e):
    data = {"sessionID": sid, "mode": "", "menuName": "ExtBrowseBidResultsTender", "searchResult": "True", "isChanged": "no", "language": "En",
            "isFirst": "Yes", "searchType": "Tender", "dllPage": "bid_results.html", "dllAnchor_pageLevel": "pageLevel", "results_type": "Awards",
            "docNum": "", "issuedForName": "", "issuedFor": "", "issuedByName": "", "issuedBy": "", "beg_date": b, "end_date": e}
    throttle(); r = s.post(B + "showBidResults", data=data, timeout=120)
    return r


done_windows = set()
wpath = os.path.join(outdir, "windows_done.txt")
if os.path.exists(wpath):
    done_windows = set(open(wpath).read().split())
seen = set()
apath = os.path.join(outdir, "awards.jsonl")
if os.path.exists(apath):
    for l in open(apath):
        try:
            seen.add(json.loads(l)["key"])
        except Exception:
            pass
fo = open(apath, "a"); fw = open(wpath, "a")
d0 = datetime.datetime.strptime(beg, "%Y/%m/%d").date(); d1 = datetime.datetime.strptime(end, "%Y/%m/%d").date()
s, sid = new_session()
cur = d0
while cur <= d1:
    we = min(cur + datetime.timedelta(days=win - 1), d1)
    b, e = cur.strftime("%Y/%m/%d"), we.strftime("%Y/%m/%d")
    key = f"{b}-{e}"
    if key in done_windows:
        cur = we + datetime.timedelta(days=1); continue
    try:
        r = search(s, sid, b, e)
        total, qid, tenders = parse(r.text)
        with gzip.open(os.path.join(outdir, "pages", f"{b.replace('/', '')}_{e.replace('/', '')}_p1.html.gz"), "wt") as g:
            g.write(r.text)
        pages = [tenders]
        rec = 31
        while rec <= total and qid:
            url = (B + f"showBidResults?sessionID={sid}&mode=&menuName=ExtBrowseBidResultsTender&searchResult=True&isChanged=no&language=En&isFirst=Yes&searchType=Tender&dllPage=bid_results.html&"
                   f"dllAnchor_pageLevel=pageLevel&results_type=Awards&docNum=&issuedForName=&issuedFor=&issuedByName=&issuedBy=&beg_date={b.replace('/', '%2F')}&end_date={e.replace('/', '%2F')}&queryObjectId={qid}&recordNum={rec}")
            throttle(); rr = s.get(url, timeout=120)
            _, _, tt = parse(rr.text)
            with gzip.open(os.path.join(outdir, "pages", f"{b.replace('/', '')}_{e.replace('/', '')}_r{rec}.html.gz"), "wt") as g:
                g.write(rr.text)
            pages.append(tt); rec += 30
        n = 0
        for tt in pages:
            for t in tt:
                k = f"{t.get('tender_number')}|{t.get('disID')}"
                if k in seen:
                    continue
                seen.add(k); n += 1
                t["key"] = k; t["search_window"] = key; t["retrieved_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                fo.write(json.dumps(t, ensure_ascii=False) + "\n")
        fo.flush()
        log(f"window {key} total {total} parsed {sum(len(x) for x in pages)} new {n}")
        fw.write(key + "\n"); fw.flush()
        cur = we + datetime.timedelta(days=1)
    except Exception as ex:
        log(f"window {key} error {ex!r}; new session")
        time.sleep(10)
        s, sid = new_session()
log("done")

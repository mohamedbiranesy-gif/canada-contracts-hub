#!/usr/bin/env python3
"""Organisations WE ALREADY KNOW (buyers of the dataset, crawled organisations, lead buyers) named as customers in a
Canada-located vendor's own dated news release. No AI: dictionary matching.

tools/vendor_news.py parsed release TITLES for "<Buyer> selects <Vendor>" shapes: 51,000 releases gave 22 leads. Most
releases name the customer in a different shape ("<Vendor> announces X as new customer", "… awarded by the City of Y",
"<Vendor> to deliver Z for <Buyer>"). This tool instead looks for the names (or linked websites) of organisations we
already have — ~60,000 of them, with their websites and often their confirmed invoicing mailbox — in the title and the
first paragraphs of each release, next to a buying cue (selected, awarded, contract, deploys, customer, renews, …) and
away from the dropped cues (financing, acquisition, prize, partnership, donation, grant received …).

A match is emitted as a lead (tools/lead_scanner.py --bridge picks it up): buyer = the known organisation (its own name
and website, so rank.py attaches its confirmed mailbox and upgrades its row to a dated relationship), vendor = the
release's publisher, record date = the release date, evidence = the release URL + the sentence naming the buyer.
Vendor in Canada: the vendor list's own basis (contract data country field, Wikidata country, Canada-HQ list) AND, for
sites that are not .ca / not on the HQ list, a Canadian place line in the release itself (dateline or "headquartered in").

Vendors: the newsrooms that tools/vendor_news.py found releases on (its *.done files), Canadian listed companies from
Wikidata (TSX / TSXV / CSE / NEO), the Canada-HQ list. Polite: robots.txt, 1 request / second / site, identified UA.
  python3 tools/news_match.py [--workers 24] [--per-vendor 60] [--limit N] [--min-urls 3] [--only tsx|done|hq]
Output ~/cch-leads/socrata_news_match.jsonl (+ .done progress, .stats).
"""
import argparse, collections, csv, datetime, glob, hashlib, html, json, os, re, sys, threading, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL
import vendor_news as VN
from customer_stories import VENDORS as HQ_VENDORS

TODAY = datetime.date.today()
OLDEST = (TODAY - datetime.timedelta(days=3 * 365)).isoformat()
RECENT = (TODAY - datetime.timedelta(days=365)).isoformat()
LEADS = os.path.expanduser("~/cch-leads")
STATE = os.path.expanduser("~/cch-crawler-state")
REPO = os.path.expanduser("~/cch-crawler")
OUT = os.path.join(LEADS, "socrata_news_match.jsonl")
UA = CL.UA if hasattr(CL, "UA") else "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
lock = threading.Lock()

BUY = re.compile(r"\b(select(?:s|ed)?|chooses|chose|chosen|picks|picked|taps|tapped|award(?:s|ed)?|contract(?:s|ed)?|agreement|"
                 r"deploy(?:s|ed|ment)?|implement(?:s|ed|ation)?|goes live|go live|went live|roll(?:s|ed)? out|rollout|adopt(?:s|ed)?|"
                 r"renew(?:s|ed|al)?|extend(?:s|ed)?|expan(?:ds|ded|sion)|purchas(?:e|es|ed)|order(?:s|ed)?|suppl(?:y|ies|ied)|"
                 r"deliver(?:s|ed|y)?|provid(?:e|es|ed|ing)|standardi[sz]e[sd]? on|customer|client|subscri(?:bes|ption)|licen[cs]e[sd]?|"
                 r"signs?|signed|wins?|won|secure[sd]?|engage[sd]?|retain(?:s|ed)?|mandate|tender|rfp|procure(?:s|d|ment)|"
                 r"choisi\w*|retenu\w*|s[ée]lectionn\w*|octroi\w*|attribu\w*|confi[ée]\w*|contrat|entente|commande|d[ée]ploie\w*|"
                 r"adopte\w*|renouvel\w*|fournir\w*|livrer\w*|client[eè]?l?e?|mandat|remport\w*|obtien\w*|d[ée]croch\w*)\b", re.I)
DROP_T = re.compile(r"financ|credit facilit|\bloan|\bprêt|invest(?!igat)|raises?\b|funding|\bfund\b|grant(?!ed a contract)|subvention|"
                    r"acqui|merger|\bmerge|fusion|\bmou\b|memorand|letter of intent|\bloi\b|lettre d.intention|distribut|reseller|"
                    r"resell|revendeur|dealer|franchis|\bprize|\bprix\b|laur[ée]at|finalist|ranked|ranking|\btop \d|recogni|"
                    r"named (a|one|to)|appoint|nomm|hires|\bceo\b|\bcfo\b|board of directors|dividend|earnings|results|quarter|"
                    r"trimestr|webinar|conference|congr[èe]s|\bipo\b|shares|sponsor|donat|\bdon\b|charit|scholarship|bourse|"
                    r"internship|career fair|job fair|hackathon|study|survey|report finds|research shows|white ?paper|podcast|"
                    r"opinion|editorial|holiday|season.s greetings", re.I)
GENERIC = {"the", "of", "and", "de", "du", "des", "la", "le", "les", "et", "l", "d", "for", "in", "a", "an", "inc", "ltd", "llc",
           "corp", "corporation", "co", "company", "limited", "ltee", "group", "groupe", "holdings", "international", "canada",
           "city", "town", "village", "county", "district", "municipality", "township", "region", "regional", "university",
           "college", "school", "schools", "board", "hospital", "health", "services", "service", "authority", "association",
           "society", "foundation", "centre", "center", "department", "ministry", "office", "government", "state", "county",
           "public", "national", "general", "community", "institute", "ville", "municipalite", "commission", "agency", "bank",
           "credit", "union", "federal", "province", "provincial", "council", "system", "systems", "solutions", "technologies"}
TYPE_WORD = re.compile(r"^(city|town|village|county|district|municipality|township|region|regional|ville|municipalite|rm|"
                       r"comte|mrc|conseil|county|parish|borough|hamlet|cree|first|nation)$")
PLATFORM_DOM = re.compile(r"(^|\.)(linkedin|facebook|twitter|x|instagram|youtube|vimeo|wikipedia|google|apple|amazon|bit|t|"
                          r"newswire|prnewswire|globenewswire|businesswire|cision|accesswire|marketwatch|yahoo|bloomberg|"
                          r"reuters|cnw|newsfilecorp|sedarplus|sec|tsx|nasdaq|nyse|crunchbase|zoominfo|glassdoor|indeed|"
                          r"wordpress|wix|squarespace|shopify|hubspot|mailchimp|eventbrite|zoom|microsoft|adobe|gov|canada|"
                          r"gc|quebec|ontario|alberta|bcgov|europa|un|who|w3|github|medium|substack|spotify|soundcloud)\.[a-z.]+$|"
                          r"^(gov\.uk|canada\.ca|gc\.ca|quebec\.ca|ontario\.ca|alberta\.ca|gov\.bc\.ca|europa\.eu|un\.org|who\.int)$")
norm = VN.norm


from ap_crawler import registrable as _reg


def registrable(host):
    h = CL.base(host) if host else ""
    return _reg(h) if h and "." in h else h


def sig_tokens(name):
    toks = [t for t in norm(name).split() if t not in GENERIC and len(t) > 1]
    return toks


# ----------------------------------------------------------------------------------------------------------------
# the dictionary of organisations we know
def load_orgs():
    """name tokens -> org; registrable domain -> org. org = {name, website, key, grade}"""
    orgs, by_dom = {}, {}
    def add(name, website, key, grade=""):
        name = (name or "").strip()
        h = registrable((urllib.parse.urlparse(website if "//" in (website or "") else "https://" + (website or "")).hostname or "").lower().removeprefix("www."))
        if not name and not h:
            return
        o = orgs.get(key) or {"name": name, "website": website, "key": key, "grade": grade, "dom": h}
        if grade and (not o["grade"] or grade > o["grade"]):
            o["grade"] = grade
        orgs[key] = o
        if h and not PLATFORM_DOM.search(h) and not re.search(r"^(gmail|hotmail|outlook|yahoo|live|icloud)\.", h):
            by_dom.setdefault(h, o)
    rb = os.path.join(REPO, "coord/results/ranked/ranked_buyers.csv")
    if os.path.exists(rb):
        for r in csv.DictReader(open(rb, encoding="utf-8", errors="replace")):
            add(r["buyer"], r["buyer_website"], (r["keys"] or "").split("|")[0] or "rb:" + hashlib.sha1(r["buyer"].encode()).hexdigest()[:12], r.get("grade") or "")
    lf = os.path.join(REPO, "data/incoming/claude/claude_buyer_leads.csv")
    if os.path.exists(lf):
        for r in csv.DictReader(open(lf, encoding="utf-8", errors="replace")):
            add(r["buyer_name"], r.get("website") or "", r["buyer_key"])
    for f in sorted(glob.glob(os.path.join(REPO, "coord/tasks/claude/claude_buyer_ap_batch9*.csv"))) + \
             sorted(glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch9*.csv"))):
        try:
            for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
                if r.get("buyer_key", "").startswith(("v:", "osm:")):
                    continue  # vendors and shops: not buyers we target
                add(r.get("buyer_name") or "", r.get("known_website") or "", r.get("buyer_key") or "")
        except Exception:
            pass
    # name index: first significant token -> [(token tuple, org)]
    index = collections.defaultdict(list)
    for o in orgs.values():
        n = o["name"]
        if not n or re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", n.lower()):
            continue  # a bare domain is matched through links, not words
        full = norm(n).split()
        toks = sig_tokens(n)
        if not toks:
            continue
        if len(toks) == 1 and (len(toks[0]) < 9 or toks[0].isdigit()):
            continue  # one short word (nelson, marathon …) is not a name match
        typed = any(TYPE_WORD.match(t) for t in full)  # "city of x": the whole phrase must appear
        phrase = tuple(full) if typed else tuple(toks)
        if len(phrase) > 9:
            continue
        index[phrase[0]].append((phrase, o, typed))
    return orgs, by_dom, index


def find_names(text, index, limit=6):
    """organisations whose name phrase occurs in text: [(org, start, end)] on the normalised token stream"""
    toks, pos = [], []
    for m in re.finditer(r"[a-z0-9]+", text.lower()):
        toks.append(m.group(0)); pos.append((m.start(), m.end()))
    hits = {}
    for i, t in enumerate(toks):
        for phrase, o, typed in index.get(t, ()):
            n = len(phrase)
            if typed:
                if tuple(toks[i:i + n]) == phrase:
                    hits.setdefault(o["key"], (o, pos[i][0], pos[i + n - 1][1]))
            else:  # the significant words, in order, within a window that allows the generic words between them
                j, k, ok = i, 0, True
                while k < n and ok:
                    if j < len(toks) and toks[j] == phrase[k]:
                        k += 1; j += 1
                    elif j < len(toks) and toks[j] in GENERIC and j - i < n + 4:
                        j += 1
                    else:
                        ok = False
                if ok and k == n:
                    hits.setdefault(o["key"], (o, pos[i][0], pos[j - 1][1]))
        if len(hits) >= limit:
            break
    return list(hits.values())


def sentence_at(text, a, b):
    s = max(text.rfind(". ", 0, a), text.rfind("! ", 0, a), text.rfind("? ", 0, a), text.rfind("\n", 0, a)) + 1
    e = min(x for x in (text.find(". ", b), text.find("! ", b), text.find("? ", b), len(text)) if x >= 0)
    sent = text[s:e + 1].strip()
    if len(sent) > 300:
        lo = max(0, a - s - 120)
        sent = sent[lo:lo + 300]
    return sent


# ----------------------------------------------------------------------------------------------------------------
def wikidata_listed():
    """Canadian companies listed on TSX / TSXV / CSE / NEO (or 300+ employees) with a website, cached for a week."""
    cp = os.path.join(STATE, "wikidata_listed.json")
    if os.path.exists(cp) and time.time() - os.path.getmtime(cp) < 7 * 86400:
        return json.load(open(cp))
    q = """SELECT DISTINCT ?c ?cLabel ?web ?exLabel WHERE {
      ?c wdt:P17 wd:Q16 ; wdt:P856 ?web .
      { ?c wdt:P414 ?ex . } UNION { ?c wdt:P1128 ?emp . FILTER(?emp >= 300) }
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en,fr". }
    } LIMIT 25000"""
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.loads(r.read().decode("utf-8"))
    out = {}
    for b in data["results"]["bindings"]:
        web, name = b["web"]["value"], b["cLabel"]["value"]
        ex = (b.get("exLabel") or {}).get("value", "")
        if ex and not re.search(r"Toronto|TSX|Venture|Canadian Securities|NEO|Aequitas|Cboe Canada|Montreal", ex):
            continue
        h = registrable((urllib.parse.urlparse(web).hostname or "").lower().removeprefix("www."))
        if h and h not in out:
            out[h] = {"buyer_key": "wd:" + b["c"]["value"].rsplit("/", 1)[-1], "buyer_name": name, "known_website": "https://%s/" % h,
                      "basis": "wd", "exchange": ex}
    os.makedirs(STATE, exist_ok=True)
    json.dump(list(out.values()), open(cp, "w"))
    return list(out.values())


def vendors_from_done(min_urls):
    """vendor sites whose newsroom tools/vendor_news.py found releases on (site, urls, rows)"""
    seen, out = set(), []
    names = {}
    for f in glob.glob(os.path.expanduser("~/cch-crawler/coord/tasks/claude/claude_buyer_ap_batch90[234].csv")):
        for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
            h = registrable((urllib.parse.urlparse(r.get("known_website") or "").hostname or "").lower().removeprefix("www."))
            if h:
                names.setdefault(h, (r.get("buyer_name") or "", r.get("buyer_key") or ""))
    for f in glob.glob(os.path.join(LEADS, "socrata_vnews_*.jsonl.done")):
        for line in open(f, encoding="utf-8", errors="replace"):
            p = line.rstrip("\n").split("\t")
            if len(p) < 2 or not p[1].isdigit() or int(p[1]) < min_urls:
                continue
            site = p[0]
            h = registrable((urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www."))
            if h in seen or not h:
                continue
            seen.add(h)
            nm, key = names.get(h, ("", ""))
            out.append({"buyer_key": key or "site:" + h, "buyer_name": nm, "known_website": site, "basis": (key.split(":")[0] if key else "site"), "urls": int(p[1])})
    out.sort(key=lambda v: -v["urls"])
    return out


def one(v, orgs, by_dom, index, cap, stats, done):
    site = v["known_website"]
    vhost = registrable((urllib.parse.urlparse(site).hostname or "").lower().removeprefix("www."))
    if not vhost or vhost in done or vhost in by_dom and v["basis"] not in ("v", "wd", "hq"):
        return
    basis = v.get("basis") or "site"
    vname = v.get("buyer_name") or vhost
    try:
        urls = VN.news_urls(site, cap) if CL.allowed(site) else []
    except Exception:
        urls = []
    rows, n_read = {}, 0
    for u in urls:
        if not CL.allowed(u):
            continue
        page, final = CL.fetch(u)
        if not page:
            continue
        n_read += 1
        title = VN.page_title(page)
        if not title or DROP_T.search(title):
            continue
        d = VN.page_date(page, final)
        if not d or d < OLDEST or d > TODAY.isoformat():
            continue
        text = VN.body_text(page)
        head = title + ". " + text[:2500]
        place = VN.CANADA_LINE.search(text[:4000]) or VN.CANADA_HQ.search(text)
        place = re.sub(r"\s+", " ", text[max(0, place.start() - 40):place.end() + 40]).strip()[:200] if place else ""
        if basis != "hq" and not vhost.endswith(".ca") and not place:
            stats["no_canada_line"] += 1
            continue
        cands = []
        for href, label in CL.anchors(page, final):  # organisations linked from the release
            h = registrable((urllib.parse.urlparse(href).hostname or "").lower().removeprefix("www."))
            if h and h != vhost and not h.endswith("." + vhost) and h in by_dom:
                o = by_dom[h]
                i = head.lower().find(norm(o["name"]).split()[0] if o["name"] else "\0")
                cands.append((o, "link", i if i >= 0 else 0, i + 10 if i >= 0 else 0))
        for o, a, b in find_names(head, index):
            cands.append((o, "name", a, b))
        for o, how, a, b in cands:
            od = o.get("dom") or ""
            if od and (od == vhost or od.endswith("." + vhost) or vhost.endswith("." + od)):
                continue  # the vendor itself
            if norm(o["name"]) and norm(o["name"]) in norm(vname):
                continue
            sent = sentence_at(head, a, b) if how == "name" else (sentence_at(head, a, b) if a else title[:300])
            cue_zone = title + " " + sent
            if not BUY.search(cue_zone):
                stats["no_buy_cue"] += 1
                continue
            if DROP_T.search(sent) and not BUY.search(title):
                continue
            if how == "name" and o["name"].lower() not in sent.lower() and norm(o["name"]) not in norm(sent):
                sent = head[max(0, a - 120):b + 160]
            k = o["key"]
            if k in rows and rows[k]["row"]["record_date"] >= d:
                continue
            rows[k] = {"platform": "news_match", "domain": od or registrable((urllib.parse.urlparse(final).hostname or "")), "dataset_id": final,
                       "dataset": "named as a customer in a Canada-located vendor's own news release (%s)" % d, "dataset_url": final,
                       "publisher": o["name"] or od, "buyer_unit": "", "website": o["website"] or ("https://%s/" % od if od else ""),
                       "vendor": vname, "canada_field": "own news release of the vendor (%s)" % VN.BASIS.get(basis, basis),
                       "canada_value": place or vhost,
                       "row": {"record_date": d, "news_date": d, "title": title[:300], "quote": sent[:300], "match": how,
                               "org_key": k, "org_grade": o.get("grade", ""), "vendor_key": v["buyer_key"], "vendor_site": site,
                               "retrieved": TODAY.isoformat()}}
            stats["recent" if d >= RECENT else "older"] += 1
            if o.get("grade") == "4":
                stats["ap_grade_org"] += 1
    with lock:
        if rows:
            with open(OUT, "a", encoding="utf-8") as f:
                for r in rows.values():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(OUT + ".done", "a", encoding="utf-8") as f:
            f.write("%s\t%d\t%d\t%d\n" % (site, len(urls), n_read, len(rows)))
        stats["vendors"] += 1; stats["releases"] += n_read; stats["leads"] += len(rows)
        if stats["vendors"] % 50 == 0:
            print("%s %s" % (datetime.datetime.now().strftime("%H:%M"), dict(stats)), flush=True)
            json.dump(dict(stats), open(OUT + ".stats", "w"))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--workers", type=int, default=24)
    a.add_argument("--per-vendor", type=int, default=60)
    a.add_argument("--limit", type=int, default=0)
    a.add_argument("--min-urls", type=int, default=3)
    a.add_argument("--only", default="")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    orgs, by_dom, index = load_orgs()
    print("organisations: %d (domains %d, name phrases %d)" % (len(orgs), len(by_dom), sum(len(v) for v in index.values())), flush=True)
    done = set()
    if os.path.exists(OUT + ".done"):
        for l in open(OUT + ".done", encoding="utf-8"):
            done.add(registrable((urllib.parse.urlparse(l.split("\t")[0]).hostname or "").lower().removeprefix("www.")))
    vendors, seen = [], set()
    groups = []
    if a.only in ("", "tsx"):
        try:
            groups.append(wikidata_listed())
        except Exception as ex:
            print("wikidata: %s" % ex, flush=True)
    if a.only in ("", "hq"):
        groups.append([{"buyer_key": "hq:" + h, "buyer_name": "", "known_website": "https://www.%s/" % h, "basis": "hq"} for h in dict.fromkeys(HQ_VENDORS)])
    if a.only in ("", "done"):
        groups.append(vendors_from_done(a.min_urls))
    for g in groups:
        for v in g:
            h = registrable((urllib.parse.urlparse(v["known_website"]).hostname or "").lower().removeprefix("www."))
            if h and h not in seen:
                seen.add(h); vendors.append(v)
    if a.limit:
        vendors = vendors[:a.limit]
    print("vendors: %d (%d done before)" % (len(vendors), len(done)), flush=True)
    stats = collections.Counter()
    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(lambda v: one(v, orgs, by_dom, index, a.per_vendor, stats, done), vendors))
    json.dump(dict(stats), open(OUT + ".stats", "w"))
    print("finished %s" % dict(stats), flush=True)


if __name__ == "__main__":
    main()

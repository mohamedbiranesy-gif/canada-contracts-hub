"""Stage C: filter fetched releases to Canadian-vendor contract candidates and emit a compact digest for review."""
import json, re, sys
sys.path.insert(0, "scripts/private_press")
from extract_lib import *
src = sys.argv[1]; outp = sys.argv[2]
rows = [json.loads(l) for l in open(src)]
TITLE_KW = re.compile(r"\b(award|awarded|awards|contract|contracts|agreement|agreements|selected|selects|select|purchase order|order|orders|renew|renews|renewal|renewed|extension|extends|extended|supply|supplies|MSA|framework|signs|signed|sign|secures|secured|wins|win|chooses|chose|partners with|partnership|deal|subcontract|mandate|engagement|deploy|deploys|implement|licens|licence|license|expands|expand|teams|adopts|taps|to provide|to supply|to deliver|to build|to design|collaborat)\b", re.I)
EXCL_TITLE = re.compile(r"\b(collective agreement|tentative agreement|ratif|union|strike|lockout|acquire|acquisition|acquires|to acquire|merger|merge|definitive agreement to (?:acquire|sell|combine)|private placement|bought deal|financing|offering|prospectus|debenture|credit facility|loan|warrants?|dividend|earnings|results|quarter|fiscal|annual meeting|AGM|appoints|appointment|names .* as|joins board|board of directors|CEO|CFO|webcast|conference call|investor (?:conference|day|presentation)|normal course issuer bid|NCIB|share consolidation|stock option|RSU|DSU|listing|uplist|delist|trading halt|change of auditor|shareholder|proxy|lawsuit|class action|settlement|bankruptcy|CCAA|creditor|receivership|MOU|memorandum of understanding|letter of intent|LOI|non-binding|term sheet|exploration (?:agreement|results)|drill results|drilling results|assay|mineral resource|option agreement|earn-in|joint venture|royalty|streaming|offtake|concession|licen[cs]e to operate|permit|approval|grant|funding|contribution agreement|investment|invests|interview|podcast|webinar|award-winning|wins award|awarded (?:the )?(?:prize|medal|recognition)|named (?:to|one of|a top)|recogni[sz]ed|ranked|certification|certified|accredit|opens|opening|launches|launch|unveils|introduces|celebrates|anniversary|donat|sponsor|scholarship|hiring|hires|expands (?:team|footprint|presence|office)|new office|relocat|rebrand|survey|study|report finds|white paper|guide|tips|statement|responds|comment|advisory|media advisory|photo|video|invitation|reminder|notice|correction|update on|provides update|operational update|production update|guidance|outlook|forecast)\b", re.I)
UNNAMED = re.compile(r"\b(undisclosed|unnamed|confidential (?:customer|client|buyer)|a (?:major|leading|large|global|Fortune \d+|top-tier|tier-?1|tier-?one|North American|U\.S\.|European|Canadian|international) (?:\w+ ){0,4}(?:customer|client|utility|operator|retailer|OEM|manufacturer|bank|insurer|carrier|airline|university|hospital|agency|company|firm|miner|producer|contractor|distributor|partner|government|municipality|school board|province|state))\b", re.I)
out = open(outp, "w", encoding="utf-8")
kept=0; drop={"err":0,"not_ca":0,"no_kw":0,"excl":0}
for r in rows:
    if r.get("error"): drop["err"]+=1; continue
    title = r.get("title") or r["meta"].get("og:title") or ""
    text = r.get("text") or ""
    loc, d = parse_dateline(r.get("dateline") or "")
    if not d: loc, d = parse_dateline(re.sub(r"\s+"," ", text[:600]))
    if not d: d = (r["meta"].get("date") or "")[:10] or None
    is_ca, city, prov = location_is_canada(loc)
    tickers = parse_tickers(text)
    ca_ticker = any(t.startswith(("TSX:","TSXV:","CSE:","NEO:","CBOE CA:","CBOE CANADA:")) for t in tickers)
    if not (is_ca or ca_ticker): drop["not_ca"]+=1; continue
    if not TITLE_KW.search(title): drop["no_kw"]+=1; continue
    if EXCL_TITLE.search(title): drop["excl"]+=1; continue
    # body: cut boilerplate
    body = text
    cut = re.search(r"\n(About [A-Z][^\n]{0,80}|ABOUT [^\n]{0,80}|Forward[- ]Looking|FORWARD[- ]LOOKING|Cautionary|For (?:further|more) information|Media Contact|Contacts?:|SOURCE )", body)
    core = body[:cut.start()] if cut else body[:6000]
    money = parse_money(core)
    durs = parse_durations(core)
    dates = find_dates(core)
    unnamed = bool(UNNAMED.search(title + " " + core[:1500]))
    sents = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+"," ", core))
    lead = " ".join(sents[:5])[:1100]
    about = text[cut.start():] if cut else ""
    hq = None
    mhq = re.search(r"(headquartered|head office|based|headquarters)\s+(?:is\s+)?(?:in|at)\s+([A-Z][\w\.\-' ]{2,40}(?:,\s*[A-Z][\w\.\-' ]{2,30}){0,2})", about)
    if mhq: hq = mhq.group(0)[:120]
    out.write(json.dumps({"url": r["url"], "sha1": r.get("sha1"), "title": title, "announce_date": d, "dateline_loc": loc, "vendor_city": city, "vendor_prov": prov,
        "is_ca_dateline": is_ca, "tickers": tickers, "company_links": r.get("company_links"), "lead": lead,
        "money": [m["text"] for m in money[:8]], "durations": [f'{x["n"]} {x["unit"]}: {x["context"]}' for x in durs[:5]],
        "dates": [f'{x["iso"]}: {x["context"][:120]}' for x in dates[:8]], "unnamed_flag": unnamed, "core_len": len(core), "about_hq": hq, "core": re.sub(r"\s+"," ", core)[:5000]}, ensure_ascii=False)+"\n")
    kept+=1
print("kept", kept, "dropped", drop)

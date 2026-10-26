"""sec_edgar round 2: build review digests for fetched EX-99 press releases (kind ex99_pr), filtered by headline
keywords, skipping releases whose headline already appears in private_press (records or fetched newswire titles).
usage: digest_ex99.py out.jsonl out.txt"""
import json, re, sys, os, glob
sys.path.insert(0, "scripts/private_press")
from extract_lib import parse_dateline, location_is_canada, parse_money, parse_durations
sys.path.insert(0, "scripts/private_press/round4")
B = "."
POS = re.compile(r"\b(award(?:ed|s)?|contract|agreement|select(?:s|ed)|chosen|signs?|signed|wins?|won|renew(?:s|al|ed)?|extend(?:s|ed)?|extension|supply|purchase order|orders?|deal|standing offer|framework|MSA|master services|licen[cs]e|offtake|subcontract|task order|deploy(?:s|ment)?|implement(?:s|ation)?)\b", re.I)
NEG = re.compile(r"\b(results|earnings|quarter(?:ly)?|Q[1-4]|dividend|financing|private placement|offering|bought deal|prospectus|acquisition|acquire[sd]?|merger|appoint|board of directors|conference call|webcast|annual (?:general )?meeting|AGM|shareholder|stock option|issuer bid|NCIB|credit facility|debenture|notes due|recogni[sz]ed|named (?:one of|to|a|as)|ranking|MOU|memorandum of understanding|letter of intent|LOI|non-binding|webinar|investor|closes|arrangement agreement|warrant|grant(?:s|ed)?|management cease trade|annual information form|filing|financial statements|exploration|drill(?:ing)? results|assay|mineral resource|preliminary economic|feasibility study)\b", re.I)
def n(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
# headlines already covered by private_press
seen_titles = set()
for l in open(f"{B}/normalized/private_press.jsonl", encoding="utf-8"):
    r = json.loads(l); seen_titles.add(n(r["contract"].get("title") or r["raw"].get("headline"))[:60])
for fn in glob.glob(f"{B}/downloads/private_press/fetched_*.jsonl"):
    for l in open(fn, encoding="utf-8"):
        try: d = json.loads(l)
        except Exception: continue
        if d.get("title"): seen_titles.add(n(d["title"])[:60])
CA_WORDS = re.compile(r"\b(Canada|Canadian|Ontario|Qu[eé]bec|British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland|Toronto|Montr[eé]al|Vancouver|Calgary|Ottawa|Edmonton|Winnipeg|Halifax|Mississauga|Waterloo|Kitchener|Markham|Burnaby|Laval|Longueuil|Saskatoon|Regina|Kanata|Oakville|Burlington)\b")
idx = [json.loads(l) for l in open(f"{B}/downloads/sec_edgar/docs_index.jsonl", encoding="utf-8")]
outj = open(sys.argv[1], "w", encoding="utf-8"); outt = open(sys.argv[2], "w", encoding="utf-8")
k = 0; stats = {"docs": 0, "no_text": 0, "neg_headline": 0, "no_pos": 0, "dup_private_press": 0, "kept": 0}
seen_here = set()
for d in idx:
    if d.get("kind") != "ex99_pr": continue
    stats["docs"] += 1
    if not d.get("file"): stats["no_text"] += 1; continue
    p = f"{B}/downloads/sec_edgar/docs/{d['file']}"
    if not os.path.exists(p): stats["no_text"] += 1; continue
    t = open(p, encoding="utf-8", errors="replace").read()
    lines = [x.strip() for x in t.split("\n") if x.strip()]
    # headline: first line with >= 5 words that is not 'Exhibit 99.1' / company name only
    head = ""
    for x in lines[:15]:
        if re.match(r"(?i)^(exhibit|ex-)\s*99", x) or len(x.split()) < 5 or re.match(r"(?i)^(news release|press release|for immediate release)", x): continue
        head = x[:220]; break
    if NEG.search(head): stats["neg_headline"] += 1; continue
    if not POS.search(head): stats["no_pos"] += 1; continue
    key = n(head)[:60]
    if key in seen_titles or key in seen_here: stats["dup_private_press"] += 1; continue
    seen_here.add(key)
    flat = re.sub(r"\s+", " ", t)
    m = re.search(r"([A-Z][A-Za-z\.\s,'\-]{2,60}),?\s+(?:[A-Z][a-z]+\.?\s+\d{1,2},?\s+\d{4})", flat[:3000])
    loc, dt = parse_dateline(flat[:1500])
    sents = re.split(r"(?<=[\.\!\?])\s+(?=[A-Z\"“])", flat[:9000])
    lead = " ".join(sents[:3])[:600]
    keys = [s[:230] for s in sents[3:] if re.search(r"(year|month|term|until|through|expir|valued|worth|\$|million|commenc|deliver)", s, re.I) and not re.search(r"\bsaid\b|forward-looking", s)][:4]
    about = ""
    am = re.search(r"(?i)about ([A-Z][^\.]{1,60})[\.:]?\s(.{0,400})", flat)
    if am: about = (am.group(1) + ": " + am.group(2))[:300]
    rec = {"i": k, "_id": d["_id"], "url": d["url"], "filer": d["display_name"], "biz_locations": d.get("biz_locations"), "file_date": d["file_date"], "form": d["form"],
           "headline": head, "dateline_loc": loc, "date": dt, "lead": lead, "keys": keys, "about": about,
           "money": [x["text"] for x in parse_money(flat[:8000])][:6], "durations": [x["text"] for x in parse_durations(flat[:8000])][:6]}
    outj.write(json.dumps(rec, ensure_ascii=False) + "\n")
    outt.write(f"#{k} {d['file_date']} {d['form']} | {head}\n  FILER: {d['display_name']} {d.get('biz_locations')} LOC: {loc}\n  LEAD: {lead}\n  KEY: {' | '.join(keys)[:700]}\n  ABOUT: {about[:220]}\n  $: {rec['money']} DUR: {rec['durations']}\n  ID: {d['_id']}\n\n")
    k += 1; stats["kept"] += 1
print(json.dumps(stats))

#!/usr/bin/env python3
"""Round 4 stage C: compact review digests for fetched releases (for human curation).
usage: digest.py candidates.jsonl out_digest.jsonl out_digest.txt"""
import json, re, sys, os
sys.path.insert(0, "scripts/private_press")
from extract_lib import parse_dateline, location_is_canada, parse_money, parse_durations
DL = "downloads/private_press"
fetched = {}
for fn in os.listdir(DL):
    if fn.startswith("fetched_") and fn.endswith(".jsonl"):
        for l in open(f"{DL}/{fn}", encoding="utf-8"):
            try:
                r = json.loads(l)
                if r.get("text"): fetched[r["url"]] = r
            except Exception: pass
CA_WORDS = re.compile(r"\b(Canada|Canadian|Ontario|Qu[eé]bec|British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia|New Brunswick|Newfoundland|Prince Edward Island|Yukon|Nunavut|Toronto|Montr[eé]al|Vancouver|Calgary|Ottawa|Edmonton|Winnipeg|Halifax|Mississauga|Waterloo|Kitchener|Markham|Burnaby|Laval|Longueuil|Gatineau|Saskatoon|Regina|Victoria, B\.?C|Oakville|Burlington|Brampton|Vaughan|Kanata|Richmond, B\.?C|Saint John|Moncton|Fredericton|St\. John's)\b")
KEY = re.compile(r"(\$|€|£|million|billion|year|month|term|until|through|expir|extend|option|renew|valued|worth|contract|agreement|order|award|select|deliver|period|duration|framework|standing offer|commenc|effective)", re.I)
def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return re.split(r"(?<=[\.\!\?])\s+(?=[A-Z\"“])", t)
cands = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8")]
outj = open(sys.argv[2], "w", encoding="utf-8"); outt = open(sys.argv[3], "w", encoding="utf-8")
n = 0
for i, c in enumerate(cands):
    f = fetched.get(c["url"])
    if not f: continue
    text = f.get("text") or ""
    loc, d = parse_dateline(f.get("dateline") or "")
    if not d: loc, d = parse_dateline(re.sub(r"\s+", " ", text[:600]))
    is_ca, city, prov = location_is_canada(loc)
    # About paragraphs
    abouts = []
    for m in re.finditer(r"(?i)\babout ([A-Z][^\n]{1,70}?)(?:\n|:|\s{2})(.{0,700})", text, re.S):
        abouts.append(("About " + m.group(1).strip(), re.sub(r"\s+", " ", m.group(2))[:500]))
    hq = []
    for h, body in abouts:
        mm = re.search(r"[^.]*\b(headquarter\w*|based in|head office|offices? in|located in|founded in)\b[^.]*\.", body, re.I)
        if mm and CA_WORDS.search(mm.group(0)): hq.append(h + ": " + mm.group(0).strip()[:220])
        elif CA_WORDS.search(body): hq.append(h + ": [mentions] " + "; ".join(sorted(set(x.group(0) for x in CA_WORDS.finditer(body))))[:150])
        elif not hq: hq.append(h + ": [no Canada mention] " + body[:120])
    body = text
    k = body.find("About ")
    main = body[:k] if k > 400 else body
    sents = sentences(main)
    lead = " ".join(sents[:3])[:520]
    keys = [s[:230] for s in sents[3:] if KEY.search(s) and not re.search(r"\bsaid\b|\bsays\b", s)][:4]
    dg = {"i": n, "url": c["url"], "title": f.get("title") or c.get("title"), "date": d, "dateline_loc": loc,
          "dateline_is_ca": is_ca, "city": city, "prov": prov, "tickers": f.get("tickers"), "hq": hq[:3], "lead": lead, "keys": keys,
          "money": [m["text"] for m in parse_money(main[:6000])][:6], "durations": [x["text"] for x in parse_durations(main[:6000])][:6]}
    hq_ca = any("[no Canada mention]" not in h for h in hq)
    if not is_ca and not hq_ca:
        dg["auto_skip"] = "dateline not Canadian and About has no Canadian HQ"
        outj.write(json.dumps(dg, ensure_ascii=False) + "\n")
        open(sys.argv[3] + ".skipped", "a", encoding="utf-8").write(f"{dg['date']} | {loc} | {dg['title']}\n")
        continue
    outj.write(json.dumps(dg, ensure_ascii=False) + "\n")
    outt.write(f"#{n} {dg['date']} | {dg['title']}\n  LOC: {loc} (CA={is_ca}) TICK: {', '.join(re.sub(chr(10),'',t) for t in (f.get('tickers') or [])[:3])}\n  HQ: {' || '.join(hq[:2])[:300]}\n  LEAD: {lead}\n  KEY: {' | '.join(keys)[:800]}\n  $: {dg['money']} DUR: {dg['durations']}\n  URL: {c['url']}\n\n")
    n += 1
print("digests", n, "of", len(cands))

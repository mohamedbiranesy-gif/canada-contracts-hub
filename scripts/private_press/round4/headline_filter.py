#!/usr/bin/env python3
"""Round 4, stage A2: keep backlog/new candidates whose headline (+summary) looks like a contract announcement
with a counterparty; drop obvious non-contract news. usage: headline_filter.py in.jsonl out.jsonl [existing_urls...]"""
import json, re, sys
POS = re.compile(r"\b(award(?:ed|s)?\b(?! (?:winner|recipient|finalist|nominee|ceremony))|contract|agreement|select(?:s|ed)\b|chosen|choose[s]?\b|signs?\b|signed|wins?\b|won\b|renew(?:s|al|ed)?|extend(?:s|ed)?|extension|supply|purchase order|orders?\b|deal\b|standing offer|framework|MSA|master services|licen[cs]e agreement|procure(?:s|d|ment)|tender|deploy(?:s|ment)?|implement(?:s|ation)|go(?:es)? live|rolls? out|taps\b|engage[sd]?\b|retain(?:s|ed)\b|commission(?:s|ed)\b|delivers?\b|deliveries|offtake|subcontract|task order|call-up|teaming)", re.I)
NEG = re.compile(r"\b(results|earnings|quarter(?:ly)?\b|Q[1-4]\b|dividend|financing|private placement|offering|bought deal|prospectus|acquisition|acquire[sd]?|to acquire|merger|amalgamation|appoint(?:s|ed|ment)|board of directors|conference call|webcast|annual (?:general )?meeting|AGM\b|shareholder|stock option|normal course issuer|NCIB|credit facility|debenture|notes due|award(?:s)? (?:for|at)\b|recogni[sz]ed|named (?:one of|to|a|as)|top employer|best (?:workplaces|employers)|ranking|honou?red|MOU\b|memorandum of understanding|letter of intent|\bLOI\b|non-binding|webinar|podcast|to present at|to participate|investor day|reports? (?:first|second|third|fourth|fiscal|annual)|announces? (?:date|pricing)|closes? (?:\$|US\$|C\$|private|offering|financing)|strike|labour|union|collective agreement|tentative agreement|bargaining|lawsuit|class action|settlement agreement|share purchase|arrangement agreement|amalgamation agreement|purchase agreement for the acquisition|warrant|grant(?:s|ed)? (?:of )?options|scholarship|donat(?:es|ion)|charit|celebrat|anniversary|holiday|flight(?:s)? to|new route|nonstop|seasonal service|schedule|fare sale|loyalty|aeroplan|travel advisory|weather|appointment|obituary)\b", re.I)
inp, outp = sys.argv[1], sys.argv[2]
existing = set()
for fn in sys.argv[3:]:
    for l in open(fn, encoding="utf-8"):
        try:
            d = json.loads(l); existing.add(d.get("source", {}).get("record_url") or d.get("url"))
        except Exception: pass
kept = []
seen = set()
for l in open(inp, encoding="utf-8"):
    c = json.loads(l)
    u = c["url"]
    if u in existing or u in seen: continue
    seen.add(u)
    head = (c.get("title") or "")
    text = head + " || " + (c.get("summary") or "")
    if NEG.search(head): continue
    if not POS.search(head) and not re.search(r"\b(award(?:ed)?|contract|agreement)\b", c.get("summary") or "", re.I): continue
    kept.append(c)
with open(outp, "w", encoding="utf-8") as f:
    for c in kept: f.write(json.dumps(c, ensure_ascii=False) + "\n")
print("kept", len(kept), "of", len(seen))

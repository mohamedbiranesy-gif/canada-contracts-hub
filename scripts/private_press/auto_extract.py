"""Stage C2: heuristic extraction of vendor/buyer/value/term from digest rows -> proposals file for curation."""
import json, re, sys
sys.path.insert(0, "scripts/private_press")
from extract_lib import *
src = sys.argv[1]; outp = sys.argv[2]
rows = [json.loads(l) for l in open(src)]
ORG = r"((?:[A-Z][\w&'’\.\-]*|de|du|of|the|and|for|la|le|des)(?:\s+(?:[A-Z][\w&'’\.\-]*|de|du|of|the|and|for|la|le|des|&)){0,7}(?:\s+(?:Inc\.?|Ltd\.?|Limited|LLC|L\.L\.C\.|Corp\.?|Corporation|Co\.|Company|plc|PLC|S\.A\.|SA|AG|GmbH|N\.V\.|NV|B\.V\.|Pty|S\.p\.A\.|SpA|LP|L\.P\.|ULC|Group|Authority|Agency|Department|Ministry|Commission|Council|University|Hospital|Trust|Board|City|County|Government|Région|Société))?)"
def first(regexes, text):
    for rx in regexes:
        m = re.search(rx, text)
        if m: return m.group(1).strip(" ,.;:()\"'“”")
    return None
out = open(outp, "w", encoding="utf-8")
for r in rows:
    core = r["core"]; title = r["title"]
    lead = r["lead"]
    # vendor guess: company with Canadian ticker or dateline company (first "X (TSX: ...)" or "X Inc. (...) today announced")
    vend = None
    m = re.search(r"([A-Z][\w&'’\.\-]+(?:\s+[A-Z][\w&'’\.\-]+){0,5}(?:\s+(?:Inc\.?|Ltd\.?|Limited|Corp\.?|Corporation|Group|Technologies|Systems|Solutions|Industries|International|Holdings|Co\.|Company|S\.A\.|SA|LP|Partners))?)\s*(?:\((?:\"|“)?[^)]{0,60}\))?\s*\((?:TSX|TSXV|TSX-V|CSE|NEO|Cboe CA|Nasdaq|NASDAQ|NYSE)[^)]*\)", core[:1200])
    if m: vend = m.group(1).strip()
    if not vend:
        m = re.search(r"/(?:CNW|PRNewswire)[^/]{0,20}/\s*-+\s*" + ORG, core[:1500])
        if m: vend = m.group(1).strip()
    # buyer guess
    buyer = first([
        r"(?:awarded|received|secured|won|wins|secures|receives)\s+(?:a |an |the |its |new |additional |follow-on |multi-year |multiyear |\$[\d\.,]+\s*(?:million|billion)?\s*)*(?:[\w\-]+\s+){0,4}(?:contract|order|orders|purchase order|agreement|subcontract|award)s?\s+(?:from|by|with)\s+(?:the\s+)?" + ORG,
        r"(?:contract|agreement|order|subcontract|mandate|purchase order)s?\s+(?:from|by|with)\s+(?:the\s+)?" + ORG,
        r"(?:selected|chosen|awarded|contracted|engaged|retained|appointed|tapped)\s+by\s+(?:the\s+)?" + ORG,
        r"^" + ORG + r"\s+(?:has\s+)?(?:selects?|selected|awards?|awarded|chooses|choose|taps|tapped|picks|renews|extends|signs|has signed|has selected|has awarded|has chosen)\b",
        r"(?:agreement|contract|partnership|deal)\s+with\s+(?:the\s+)?" + ORG,
        r"(?:to|for)\s+(?:supply|provide|deliver|support|build|design|power|equip|serve)\s+(?:the\s+)?" + ORG,
    ], title) or first([
        r"(?:awarded|received|secured|won|wins|secures|receives)\s+(?:a |an |the |its |new |additional |follow-on |multi-year |multiyear |\$[\d\.,]+\s*(?:million|billion)?\s*)*(?:[\w\-]+\s+){0,4}(?:contract|order|orders|purchase order|agreement|subcontract|award)s?\s+(?:from|by|with)\s+(?:the\s+)?" + ORG,
        r"(?:selected|chosen|awarded|contracted|engaged|retained|appointed|tapped)\s+by\s+(?:the\s+)?" + ORG,
        r"(?:contract|agreement|order|subcontract|mandate|purchase order)s?\s+(?:from|by|with)\s+(?:the\s+)?" + ORG,
    ], lead)
    money = parse_money(core[:3000]); durs = parse_durations(core[:4000])
    # end-year hints
    endy = re.findall(r"\b(?:through|until|to|expiring in|expires in|ending in|ends in|runs through|runs until|valid until|extends? to|extended to|up to|completed by|complete by|by the end of)\s+(?:the end of\s+)?(?:(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+)?(20[2-4]\d)\b", core[:4000])
    out.write(json.dumps({"url": r["url"], "announce_date": r["announce_date"], "title": title, "loc": r["dateline_loc"], "city": r["vendor_city"], "prov": r["vendor_prov"], "tickers": r["tickers"][:3],
        "vendor_guess": vend, "buyer_guess": buyer, "money": [(m["text"], m["value"], m["currency"]) for m in money[:4]],
        "durations": [(d["n"], d["unit"], d["context"][:100]) for d in durs[:4]], "end_years": endy[:4], "unnamed": r["unnamed_flag"], "lead": lead[:700]}, ensure_ascii=False)+"\n")
print("done", len(rows))

"""Pre-filter company-page crawl candidates to likely contract announcements (2024+)
so the follow-up fetch is bounded. Usage: python3 -I prefilter_candidates.py <candidates.jsonl> <out.jsonl>"""
import json, sys, re
sys.path.insert(0, "scripts/private_press")
from extract_lib import parse_date

src, dst = sys.argv[1], sys.argv[2]
KW = re.compile(r"\b(award|awarded|awards|contract|contracts|agreement|agreements|selected|selects|purchase order|"
                r"order|orders|renew|renews|renewal|extension|extends|supply|supplies|framework|signs|signed|secures|"
                r"secured|wins|win|chooses|subcontract|mandate|deploy|deploys|licen[cs]e|licensing|to provide|to supply|"
                r"to deliver|to build|to design|offtake|IDIQ|task order|delivery order|MSA|PPA|partner|partnership|"
                r"collaborat|teams? up|chosen|names|appointed|engaged|retained|implement)\b", re.I)
EXCL = re.compile(r"\b(collective agreement|tentative agreement|ratif|results|quarter|fiscal|dividend|earnings|"
                  r"annual meeting|AGM|appoint(s|ed|ment)? (of )?(chief|ceo|cfo|president|director|board|vp|vice)|webcast|"
                  r"conference call|normal course issuer bid|NCIB|private placement|bought deal|offering|prospectus|"
                  r"debenture|credit facility|financing|acqui|merger|investor day|share consolidation|stock option|RSU|DSU|"
                  r"trading halt|auditor|proxy|lawsuit|class action|memorandum of understanding|letter of intent|\bLOI\b|"
                  r"non-binding|drill results|assay|mineral resource|option grant|warrant|convertible|closes|closing of|"
                  r"grant of|TSX Venture|exchange approval|notice of|reminder|invitation|advisory|media advisory|statement)\b", re.I)

MULTI = re.compile(r"\b(multi-?year|long-?term|\d{1,2}-?\s?year|\d{1,2} years|decade|through 20[3-9]\d|until 20[3-9]\d|to 20[3-9]\d|framework|IDIQ|MSA|master service|PPA|offtake|concession|P3|DBFM|DBFOM|life-?cycle|in-service support|ISS)\b", re.I)

done = set()
for f in ["fetched_newswire.jsonl", "fetched_prnewswire.jsonl", "fetched_search.jsonl"]:
    try:
        for l in open(f"downloads/private_press/{f}", encoding="utf-8"):
            done.add(json.loads(l)["url"])
    except FileNotFoundError:
        pass

n = 0
seen = set()
with open(dst, "w", encoding="utf-8") as out:
    for l in open(src, encoding="utf-8"):
        r = json.loads(l)
        u = r.get("url")
        if not u or u in done or u in seen:
            continue
        d = parse_date((r.get("list_date") or "")[:14])
        if not d or d < "2021-01-01":
            continue
        t = r.get("title") or ""
        if not KW.search(t) or EXCL.search(t):
            continue
        if d < "2024-01-01" and not MULTI.search(t):
            # pre-2024 announcements only if the title signals a multi-year / long-term term still plausibly running
            continue
        seen.add(u)
        out.write(json.dumps(r, ensure_ascii=False) + "\n")
        n += 1
print("filtered candidates:", n)

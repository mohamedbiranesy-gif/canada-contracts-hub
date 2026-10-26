"""Build a compact review sheet of candidate EX-10 exhibits & 8-K 1.01 docs (non-financing)."""
import json, re, sys
idx = [json.loads(l) for l in open("downloads/sec_edgar/docs_index.jsonl")]
DOCS="downloads/sec_edgar/docs"
EXCL = re.compile(r"\b(credit agreement|loan agreement|loan and security|note purchase|securities purchase|subscription agreement|underwriting|employment|indemnity|indemnification|equity incentive|incentive plan|stock option|warrant|arrangement agreement|merger|share purchase|asset purchase|membership interest|unit purchase|registration rights|voting|escrow|lease|forward purchase|standby equity|at-the-market|at the market|placement agency|investor'?s? rights|shareholder|guarantee|guaranty|security agreement|pledge|promissory|convertible|debenture|financing|facility agreement|advisory services|consulting agreement|management services agreement|separation|severance|retention|transition services|settlement|release|waiver|intercreditor|royalty agreement|recapitalization|exchange agreement|equity distribution|common shares sales|common shares purchase|sales agreement f|interest payment|debt conversion|talent contract|independent contractor|digital marketing|advertising and promotional|asset management agreement|joint venture interest purchase|stock purchase|asset sale|option agreement|investment agreement|production payment|contribution agreement|sif agreement|employee matters|ground sublease|termination agreement|omnibus amendment|assignment|joinder|allocation agreement|court|monitor|plan of arrangement|limited liability company agreement|co-ownership|trademark license and marketing|purchase and sale agreement dated as of july 30, 2021)\b", re.I)
out = open("downloads/sec_edgar/review_sheet.jsonl","w",encoding="utf-8")
n=0
for d in idx:
    if not d["file"]: continue
    t = open(f"{DOCS}/{d['file']}", encoding="utf-8").read()
    flat = re.sub(r"\s+"," ", t)
    head = flat[:6000]
    m = re.search(r"([A-Z][A-Z0-9 ,&\-/()'’\.]{3,160}?(AGREEMENT|CONTRACT|ORDER FORM|STATEMENT OF WORK|PURCHASE ORDER)[A-Z0-9 ,&\-/()'’\.]{0,80})", head)
    title = (m.group(1).strip() if m else "")
    desc = d.get("file_description") or ""
    label = title + " | " + desc
    if d["kind"]=="ex10" and EXCL.search(label): continue
    if d["kind"]=="8k_101":
        # keep only if 1.01 text mentions commercial words and not financing
        sec = re.search(r"Item 1\.01[\s\S]{0,4000}", t)
        sec_t = re.sub(r"\s+"," ", sec.group(0)) if sec else flat[:4000]
        if not re.search(r"\b(supply|services agreement|master services|license|licence|distribution|manufactur|offtake|statement of work|purchase order|customer|collaboration|commercial agreement|hosting|colocation|subscription|framework|development agreement|teaming|contract award|awarded)\b", sec_t, re.I): continue
        if re.search(r"\b(credit agreement|loan|notes?|securities purchase|subscription agreement for|underwriting|warrant|placement agency|at-the-market|equity distribution|merger agreement|arrangement agreement|share purchase agreement|asset purchase agreement|employment)\b", sec_t[:1500], re.I) and not re.search(r"\b(supply agreement|master services agreement|license agreement|offtake|distribution agreement|services agreement|hosting)\b", sec_t[:1500], re.I): continue
        snippet = sec_t[:1500]
    else:
        snippet = head[:1500]
    pm = re.search(r"(?:by and between|between|among|by and among)\s+(.{20,500}?)(?:\s+\(the|\s+\(“|\s+\(\"|\s+WHEREAS|\s+RECITALS|\.\s)", flat[:10000], re.I)
    term_ctx = []
    for mm in re.finditer(r"\b(?:Initial Term|initial term|term of this Agreement|Term of Agreement|Term of the Agreement|shall remain in full force|shall commence on|expire on|Expiration Date|terminate on|anniversary of the Effective Date)\b", flat):
        term_ctx.append(flat[max(0,mm.start()-150):mm.end()+250])
        if len(term_ctx)>=5: break
    dates = re.findall(r"(?:dated as of|dated|effective as of|made as of|entered into (?:as of|on)|Effective Date[^.]{0,30}?)\s+((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})", flat[:8000])
    money = re.findall(r"(?:US\$|C\$|CAD\s?\$?|USD\s?\$?|\$)\s?\d[\d,\.]*\s*(?:million|billion)?", flat[:30000])[:8]
    out.write(json.dumps({"_id": d["_id"], "kind": d["kind"], "filer": d["display_name"], "file_date": d["file_date"], "form": d["form"], "file_type": d["file_type"],
        "biz_locations": d["biz_locations"], "biz_states": d["biz_states"], "url": d["url"], "index_url": d["index_url"], "desc": desc, "title": title[:200],
        "parties": pm.group(1)[:500] if pm else None, "dates": dates[:5], "term_ctx": [x[:400] for x in term_ctx], "money": money, "snippet": snippet[:1200], "chars": d["chars"]}, ensure_ascii=False)+"\n")
    n+=1
print("review rows:", n)

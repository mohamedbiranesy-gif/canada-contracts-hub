#!/usr/bin/env python3
"""Parse crawled SaskTenders 'Awarded' listing pages into one JSON object per competition.
Usage: python3 -I parse_sasktenders.py <download_dir> <out_jsonl>
"""
import re, os, sys, glob, json, html

DL, OUT = sys.argv[1], sys.argv[2]
TBODY_RE = re.compile(r"<tbody x-data=\"\{ myId: '([0-9a-f\-]+)' \}\"[^>]*>(.*?)</tbody>", re.S)
TD_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.S)


def clean(s):
    if s is None:
        return None
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</p>\s*<p>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s)
    return s.strip()


def cf_decode(code):
    try:
        k = int(code[:2], 16)
        return "".join(chr(int(code[i:i + 2], 16) ^ k) for i in range(2, len(code), 2))
    except Exception:
        return None


def parse_block(guid, block):
    rec = {"competition_guid": guid}
    # summary row = first <tr>
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", block, re.S)
    if not trs:
        return None
    tds = TD_RE.findall(trs[0])
    if len(tds) >= 7:
        rec["competition_name"] = clean(tds[1])
        rec["organization"] = clean(tds[2])
        rec["competition_number"] = clean(tds[3])
        rec["opens"] = clean(tds[4])
        rec["closes"] = clean(tds[5])
        rec["status"] = clean(tds[6])
    detail = trs[1] if len(trs) > 1 else ""
    m = re.search(r"<h3[^>]*>Synopsis:</h3>\s*<div[^>]*>(.*?)</div>\s*</section>", detail, re.S)
    rec["synopsis"] = clean(m.group(1)) if m else None
    for label in ["Competition Type", "Agreement Type", "Public Opening"]:
        m = re.search(r"<dt[^>]*>" + re.escape(label) + r":</dt>\s*<dd>(.*?)</dd>", detail, re.S)
        rec[label.lower().replace(" ", "_")] = clean(m.group(1)) if m else None
    # documents sections
    docs = []
    for sec in re.finditer(r"<h3[^>]*>(Competition Documents|Bid Result Documents):?</h3>(.*?)</section>", detail, re.S):
        kind = sec.group(1)
        for li in re.finditer(r"<li[^>]*>(.*?)</li>", sec.group(2), re.S):
            t = clean(li.group(1))
            if t:
                href = re.search(r'href="([^"]*)"', li.group(1))
                docs.append({"section": kind, "text": t, "href": href.group(1) if href else None})
        if not re.search(r"<li", sec.group(2)):
            t = clean(sec.group(2))
            if t:
                docs.append({"section": kind, "text": t, "href": None})
    rec["documents"] = docs
    # award details
    awards = []
    m = re.search(r"<h3[^>]*>Award Details</h3>(.*?)</section>", detail, re.S)
    if m:
        for card in re.finditer(r"<div class=\"rounded-lg border[^\"]*\"[^>]*>(.*?)</div>", m.group(1), re.S):
            ps = [clean(p) for p in re.findall(r"<p[^>]*>(.*?)</p>", card.group(1), re.S)]
            name = re.search(r'title="([^"]*)"', card.group(1))
            a = {"supplier": html.unescape(name.group(1)) if name else (ps[0] if ps else None), "lines": ps}
            # classify lines: location (contains comma + region), amount ($...), date (Mon dd, yyyy)
            for p in ps[1:] if name else ps[1:]:
                if re.match(r"^\$?-?[\d,]+(\.\d+)?$", p.replace("$", "").replace(",", "").strip()) or p.startswith("$"):
                    a.setdefault("amount", p)
                elif re.match(r"^[A-Z][a-z]{2} \d{1,2}, \d{4}$", p):
                    a.setdefault("award_date", p)
                else:
                    a.setdefault("location", p)
            awards.append(a)
    rec["award_details"] = awards
    m = re.search(r"<h3[^>]*>Response Address</h3>\s*<div[^>]*>(.*?)</div>\s*</section>", detail, re.S)
    rec["response_address"] = clean(m.group(1)) if m else None
    m = re.search(r"<h3[^>]*>Contact</h3>\s*<div[^>]*>(.*?)</div>\s*</section>", detail, re.S)
    rec["contact"] = clean(m.group(1)) if m else None
    for attr in ["contact-name", "contact-email", "contact-phone"]:
        mm = re.search(r'data-' + attr + r'="([^"]*)"', detail)
        rec[attr.replace("-", "_")] = html.unescape(mm.group(1)) if mm else None
    if rec.get("contact"):
        rec["contact"] = re.sub(r"\[email protected\]", rec.get("contact_email") or "[email protected]", rec["contact"])
    if rec.get("response_address"):
        rec["response_address"] = re.sub(r"\[email protected\]", rec.get("contact_email") or "[email protected]", rec["response_address"])
    rec["print_url"] = f"https://www.sasktenders.ca/Competitions/Print?id={guid}"
    return rec


def main():
    out = open(OUT, "w")
    seen = set(); n = 0; dup = 0
    for path in sorted(glob.glob(os.path.join(DL, "pages", "page_*.html"))):
        h = open(path, encoding="utf-8", errors="replace").read()
        page = int(re.search(r"page_(\d+)", path).group(1))
        for m in TBODY_RE.finditer(h):
            guid = m.group(1)
            if guid in seen:
                dup += 1; continue
            rec = parse_block(guid, m.group(2))
            if not rec:
                continue
            seen.add(guid); rec["_page"] = page
            out.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
    out.close()
    print(json.dumps({"competitions": n, "duplicates_across_pages": dup}))


if __name__ == "__main__":
    main()

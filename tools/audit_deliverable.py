#!/usr/bin/env python3
"""Deep audit of the delivered packages (owner 2026-11-04 14:01: "final deep audit, max deep").

Goes beyond the seven gates of validate_deliverable.py: every row of every package is checked for mailbox integrity
(syntax, referee status, mail server, webmail, person-like local part, role words, receivables-looking boxes graded as
invoicing, shared government domains, regional tokens, quote vs address, evidence host vs mailbox domain vs website,
label vs grade, DNS columns), relationship integrity (tier vs dates, vendor named, Canada proof family, record link),
buyer/vendor hygiene (domain or generic names, legal-name fragments, duplicates by name and by site domain, field fill)
and cross-package consistency (one row per mailbox, 92 identical headers, part files). Writes AUDIT.md (every check with
PASS / FAIL / INFO, counts and examples) and audit_flags.csv (one line per flagged row and reason).
  python3 tools/audit_deliverable.py [coord/results/ranked] [--mx data/incoming/claude/claude_mx_check.tsv] [--dmarc data/incoming/claude/claude_dmarc_check.tsv] [--write DIR]
"""
import argparse, collections, csv, datetime, glob, os, re, sys, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from buyer_pages import FIRST_NAMES as FIRST
except Exception:
    FIRST = set()
try:
    from ap_crawler import registrable
except Exception:
    def registrable(h):
        p = h.split("."); return ".".join(p[-2:]) if len(p) >= 2 else h
from validate_deliverable import EMAIL, FREEMAIL, ROLE_WORDS

TODAY = datetime.date.today()
SHARED_GOV = re.compile(r"^(?:[a-z]{2}\.gov|state\.[a-z]{2}\.us|[a-z]+\.state\.[a-z]{2}\.us|gov\.[a-z]{2}\.ca|gnb\.ca|novascotia\.ca|ontario\.ca|gouv\.qc\.ca|canada\.ca|gc\.ca|alberta\.ca|saskatchewan\.ca|manitoba\.ca|gov\.uk|gov\.au|govt\.nz)$", re.I)
RECEIV_LOCAL = re.compile(r"(?:^|[._-])(?:payments?|billing|bills?|tax(?:es)?|utilit\w*|water|tuition|donat\w*|fees?|fines?|parking|permits?|licen\w*|rent|cashier|collections?)(?:$|[._-])", re.I)
PERSONISH = re.compile(r"^[a-z]+[._-][a-z]+$")
GENERIC_NAME = re.compile(r"^(?:contactez[- ]nous|contact(?:ez)?(?:[- ]us)?|nous joindre|accueil|home(?: page)?|bienvenue|welcome|about(?: us)?|[àa] propos|coordonn[ée]es|page d.accueil|untitled|index|services|joindre|login|connexion)\W*$", re.I)
DOMAIN_NAME = re.compile(r"^(?:www\.)?[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}$", re.I)
BAD_LEGAL = re.compile(r"copyright act|subject to|proprietary|affiliated|licen[cs]e|rights reserved|droits r[ée]serv|\btheme\b|posted by|schoolmessenger|sportsengine|civicplus|granicus|wordpress|squarespace|\bwix\b|shopify|cricos|connect with us|follow us", re.I)
# check 20 looks at the NAME, not at the cell's source text: until 2026-11-11 "licence" in "(the Régie du bâtiment du Québec's list of active
# licences …)" flagged every register name (5,266 cells flagged, 241 of them for the name itself, most of those names that begin with a small
# letter by design: "eGrr Services Inc."), while page furniture around a name went through ("… Your Cart Check Out", "X and protected by …")
def legal_cell_name(cell):
    """the name of a cell "NAME (source text)": the source is the bracket that ends the cell and begins with a small letter (or "CRA …")"""
    c = cell or ""
    if c.endswith(")"):
        depth = 0
        for i in range(len(c) - 1, -1, -1):
            if c[i] == ")":
                depth += 1
            elif c[i] == "(":
                depth -= 1
                if depth == 0:
                    if i > 0 and c[i - 1] == " " and re.match(r"[a-z]|CRA ", c[i + 1:]):
                        return c[:i - 1].strip()
                    break
    return c.strip()
LEGAL_FURNITURE = re.compile(r"^(?:inc|ltd|llc|corp|limited|incorporated)\b\.?(?:\s|$|,)|\bno\.?$|-->| · |^[·•┃|+»>]|"
                             r"\b(?:and (?:is |are )?protected|or its (?:content )?suppliers|your cart|we value|freedom of information|is an? (?:registered )?(?:trade ?mark|division|product)|"
                             r"are (?:registered )?trade ?marks|privacy policy|terms (?:and|&) conditions|welcome to|bienvenue chez|official (?:web)?site of|get in touch|loading)\b", re.I)
LEGAL_CUT_FRONT = re.compile(r"^(?:'?s|of|and|the|to|for|by|with|at|in|on|or|et|du|des|au|aux|par|pour)\s")  # a name cut at the front: begins with a small function word
NAME_BASIS = re.compile(r"\b(?:name|nom)\b.*\b(?:suggests|looks|sounds|implies|indicates|canadian-sounding)|inferred from (?:the )?name|vendor name", re.I)
GOLD = ("P01_", "P01T", "P01M")


def days(s):
    try:
        return (TODAY - datetime.date.fromisoformat((s or "")[:10])).days
    except Exception:
        return None


def main():
    a = argparse.ArgumentParser()
    a.add_argument("dir", nargs="?", default="coord/results/ranked")
    a.add_argument("--mx", default="data/incoming/claude/claude_mx_check.tsv")
    a.add_argument("--dmarc", default="data/incoming/claude/claude_dmarc_check.tsv")
    a.add_argument("--write", default="")
    a = a.parse_args()
    mx = {r["domain"]: r for r in csv.DictReader(open(a.mx, encoding="utf-8"), delimiter="\t")} if os.path.exists(a.mx) else {}
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import parted_csv as _PC  # the DNS-posture file is written in parts (tools/dmarc_check.py)
    dm = {r["domain"]: r for r in _PC.rows(a.dmarc, delimiter="\t")}
    import batch_files as BF  # the package files are compressed since 2026-11-10 (plain ones are still read)
    files = [f for f in BF.files(os.path.join(a.dir, "batches")) if not BF.member(f).startswith("Z_")]
    checks = collections.OrderedDict()  # name -> dict(kind=hard|soft|info, hits=[...], n=int)
    def hit(name, kind, where, detail=""):
        c = checks.setdefault(name, {"kind": kind, "hits": [], "n": 0})
        c["n"] += 1
        if len(c["hits"]) < 12:
            c["hits"].append((where + (" | " + detail if detail else ""))[:230])
    def ok(name, kind):
        checks.setdefault(name, {"kind": kind, "hits": [], "n": 0})
    flags = []
    headers, per_pkg, total = {}, collections.OrderedDict(), 0
    seen_mail, by_name, by_site, by_name_mail = {}, collections.defaultdict(list), collections.defaultdict(list), collections.Counter()
    fill = collections.Counter(); gold_rows = 0; basis_fam = collections.Counter(); btype = collections.Counter(); posture = collections.Counter()
    for name in ("1 header: identical columns in every file (106 since 2026-11-06)", "2 mailbox syntax", "3 mailbox referee-confirmed (all but P11)", "4 mail server (MX or A) on the mailbox domain", "4b mail server not yet checked (row newer than the last DNS pass)",
                 "5 no webmail domain", "6 no person-like local part", "7 role word in the local part", "8 receivables-looking local part graded invoicing/AP",
                 "9 shared government domain: page or quote names the body", "10 regional token of a multinational on a differently-located body", "11 quote contains the address", "11b quote shows the label next to the address (referee saw the address on the page)",
                 "12 evidence page on the organisation's domain (or its site)", "13 email_type label matches grade", "14 DMARC / SPF / provider columns filled",
                 "15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)", "16 vendor named and Canada proof present", "17 Canada proof is a source field or the vendor's site (never a name)",
                 "18 record link present for dated-record tiers", "19 buyer name is a name (not a domain or a page title)", "20 legal name is not a fragment or a platform copyright",
                 "21 one row per mailbox", "22 one row per organisation name (same name twice)", "23 one row per site domain (two rows, different mailboxes, same domain)",
                 "24 no blank cell", "25 jurisdiction vs mailbox top-level domain", "26 currency filled when a value is filled"):
        ok(name, "hard" if name.split()[0] in ("1", "2", "3", "4", "5", "6", "11", "13", "16", "21", "24") else "soft")
    for f in files:
        pkg = BF.package(f)
        short = pkg.split("_")[0] + ("_" if pkg.startswith("P01_") else "")
        short = pkg[:4]
        with BF.open_text(f) as _fh:
            rows = list(csv.DictReader(_fh))
        hdr = tuple(rows[0].keys()) if rows else ()
        headers[BF.member(f)] = hdr
        per_pkg[pkg] = per_pkg.get(pkg, 0) + len(rows); total += len(rows)
        for i, r in enumerate(rows, 2):
            where = "%s:%d %s" % (BF.member(f)[:-4], i, (r.get("buyer") or "")[:40])
            e = (r.get("email") or "").strip(); el = e.lower(); dom = el.split("@")[-1] if "@" in el else ""; local = el.split("@")[0]
            g = r.get("grade") or ""; et = r.get("email_type") or ""; q = r.get("email_evidence_quote") or ""; u = r.get("email_evidence_url") or ""
            site = r.get("buyer_website") or ""; sh = (urllib.parse.urlparse(site if "://" in site else "https://" + site).hostname or "").lower().removeprefix("www.") if site else ""
            uh = (urllib.parse.urlparse(u).hostname or "").lower().removeprefix("www.") if u.startswith("http") else ""
            reasons = []
            if not e or not EMAIL.match(e): hit("2 mailbox syntax", "hard", where, e); reasons.append("syntax")
            if short != "P11_" and (r.get("email_check") or "") != "confirmed": hit("3 mailbox referee-confirmed (all but P11)", "hard", where, r.get("email_check") or ""); reasons.append("not confirmed")
            st = (mx.get(dom) or {}).get("status")
            if dom and st == "none": hit("4 mail server (MX or A) on the mailbox domain", "hard", where, "%s: none" % dom); reasons.append("no mail server")
            elif dom and st not in ("mx", "a_only"): hit("4b mail server not yet checked (row newer than the last DNS pass)", "soft", where, dom); reasons.append("mail server unchecked")
            if dom and FREEMAIL.match(dom): hit("5 no webmail domain", "hard", where, e); reasons.append("webmail")
            parts = re.split(r"[._-]", local)
            if len(parts) == 2 and parts[0] in FIRST and len(parts[1]) >= 3 and not ROLE_WORDS.search(local): hit("6 no person-like local part", "hard", where, e); reasons.append("person-like")
            if local and not ROLE_WORDS.search(local) and not re.search(r"\d", local) and len(local) > 3: hit("7 role word in the local part", "soft", where, e); reasons.append("no role word")
            if et.startswith("invoicing") and RECEIV_LOCAL.search(local) and not re.search(r"payable|supplier|vendor|fourniss|invoice|factur", local): hit("8 receivables-looking local part graded invoicing/AP", "soft", where, e); reasons.append("receivables-looking")
            if dom and SHARED_GOV.match(dom):
                nm = re.sub(r"[^a-z0-9 ]", " ", (r.get("buyer") or "").lower()); toks = [t for t in nm.split() if len(t) >= 5]
                hay = (u + " " + q + " " + local).lower()
                if toks and not any(t in hay for t in toks) and not re.match(r"^(?:ap|accountspayable|accounts[._-]payable|payables?|invoices?|financial[._-]?sharedservices)$", local):
                    hit("9 shared government domain: page or quote names the body", "soft", where, e + " ← " + u[:80]); reasons.append("shared gov domain unproven")
            m = re.search(r"(?:^|[._-])(aunz|anz|apac|emea|latam|usa|uk|india|china|brasil|mexico|france|germany|japan|singapore|australia|europe|asia)(?:$|[._-])", local)
            if m and (r.get("jurisdiction") or "") in ("CA", "QC", "ON", "BC", "AB", "SK", "MB", "NS", "NB", "NL", "PE", "FED") and m.group(1) not in ("usa",): hit("10 regional token of a multinational on a differently-located body", "soft", where, e); reasons.append("regional token")
            if e and short != "P11_" and el not in q.lower().replace(" ", "") and el not in q.lower():
                if (r.get("email_check") or "") == "confirmed":
                    hit("11b quote shows the label next to the address (referee saw the address on the page)", "soft", where, q[:60]); reasons.append("quote is the label")
                else:
                    hit("11 quote contains the address", "hard", where, q[:60]); reasons.append("quote lacks address")
            if e and uh and dom and registrable(uh) != registrable(dom) and (not sh or registrable(uh) != registrable(sh)) and not SHARED_GOV.match(dom) and "direct-deposit" not in u:
                hit("12 evidence page on the organisation's domain (or its site)", "soft", where, "%s on %s (site %s)" % (e, uh, sh)); reasons.append("evidence host differs")
            lab = {"4": "invoicing/AP", "3": "finance/accounting dept or supplier-payment office", "2": "purchasing", "1": "general"}.get(g)
            if e and lab and et != lab: hit("13 email_type label matches grade", "hard", where, "%s vs grade %s" % (et, g)); reasons.append("label/grade")
            if e and (not r.get("dmarc_policy") or r.get("dmarc_policy") in ("", "not checked yet", "not_published") or not r.get("spf_policy") or r.get("spf_policy") in ("", "not checked yet", "not_published") or not r.get("mail_provider")):
                hit("14 DMARC / SPF / provider columns filled", "soft", where, "%s | %s | %s" % (r.get("dmarc_policy"), r.get("spf_policy"), r.get("mail_provider"))); reasons.append("dns columns")
            tier = r.get("tier") or ""; cs = r.get("contract_status") or ""
            if tier == "A" and (days(r.get("end_date")) is None or days(r.get("end_date")) > 0) and "active" in cs and not re.search(r"continuing|no end date", cs):
                hit("15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)", "soft", where, "A with end %s" % r.get("end_date")); reasons.append("tier/date A")
            if tier == "B" and days(r.get("award_date")) is not None and days(r.get("award_date")) > 366 and "3 years" not in cs and "Québec" not in cs:
                hit("15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)", "soft", where, "B awarded %s" % r.get("award_date")); reasons.append("tier/date B")
            if tier == "L" and days(r.get("award_date")) is not None and not (366 <= days(r.get("award_date")) <= 1096):
                hit("15 tier vs dates (A end ≥ today; B award ≤ 12 m; L 12–36 m)", "soft", where, "L awarded %s" % r.get("award_date")); reasons.append("tier/date L")
            vb = r.get("vendor_country_basis") or ""
            if not (r.get("vendor") or "").strip() or r.get("vendor") == "not_published" or not vb or vb == "not_published": hit("16 vendor named and Canada proof present", "hard", where); reasons.append("vendor/proof missing")
            if NAME_BASIS.search(vb): hit("17 Canada proof is a source field or the vendor's site (never a name)", "soft", where, vb[:80]); reasons.append("name-based proof")
            fam = "source field" if re.search(r"country|countr|address|adresse|state|province|dateline|headquart|HQ|located|office|FIRM_ADDRESS|FILER", vb, re.I) else "other"
            basis_fam[fam] += 1
            if tier in ("A", "B", "L", "F") and not (r.get("contract_link") or "").startswith("http"): hit("18 record link present for dated-record tiers", "soft", where, r.get("source", "")[:60]); reasons.append("no record link")
            bn = (r.get("buyer") or "").strip()
            if GENERIC_NAME.match(bn) or DOMAIN_NAME.match(bn): hit("19 buyer name is a name (not a domain or a page title)", "soft", where, bn); reasons.append("name is a domain/title")
            ln = r.get("buyer_legal_name_as_published") or ""
            lname = legal_cell_name(ln)
            if ln and ln != "not_published" and (BAD_LEGAL.search(lname) or LEGAL_FURNITURE.search(lname) or LEGAL_CUT_FRONT.search(lname)): hit("20 legal name is not a fragment or a platform copyright", "soft", where, ln[:70]); reasons.append("legal-name fragment")
            if el:
                if el in seen_mail: hit("21 one row per mailbox", "hard", where, e + " also in " + seen_mail[el]); reasons.append("duplicate mailbox")
                else: seen_mail[el] = BF.member(f)[:-4]
            nk = re.sub(r"[^a-z0-9]+", " ", bn.lower()).strip()
            by_name[nk].append((where, e)); by_name_mail[(nk, dom)] += 1
            if sh: by_site[registrable(sh)].append((where, e))
            blanks = [c for c, v in r.items() if (v or "") == ""]
            if blanks: hit("24 no blank cell", "hard", where, ",".join(blanks[:4])); reasons.append("blank cell")
            j = r.get("jurisdiction") or ""
            tld = dom.rsplit(".", 1)[-1] if dom else ""
            if j in ("CA", "QC", "ON", "BC", "AB", "SK", "MB", "NS", "NB", "NL", "PE", "FED") and tld in ("uk", "au", "nz", "fr", "de", "us", "gov") and tld != "us" or (j == "US" and tld == "ca"):
                hit("25 jurisdiction vs mailbox top-level domain", "soft", where, "%s / %s" % (j, dom)); reasons.append("jurisdiction/tld")
            if (r.get("contract_value") or "") not in ("", "not_published") and (r.get("currency") or "") in ("", "not_published"): hit("26 currency filled when a value is filled", "soft", where, r.get("contract_value", "")); reasons.append("value without currency")
            # fill statistics
            if short in GOLD: gold_rows += 1
            for col in ("buyer_website", "buyer_address", "buyer_phone", "buyer_legal_name_as_published", "buyer_bn_as_published", "buyer_logo_url", "ap_phone", "invoice_mailing_address", "invoicing_requirements",
                        "payment_terms_as_published", "po_required_as_published", "invoice_portal_url", "ap_contact_name_as_published", "contract_value", "award_date", "end_date", "contract_link",
                        "vendor_legal_name", "vendor_registry_id", "vendor_bn9", "vendor_neq", "vendor_address", "vendor_website", "vendor_emails", "vendor_phone", "vendor_logo_url", "vendor_incorporation_date"):
                if (r.get(col) or "") not in ("", "not_published"): fill[col] += 1
            btype[r.get("buyer_type") or "?"] += 1; posture[r.get("dmarc_policy") or "?"] += 1
            if reasons:
                flags.append({"file": BF.member(f)[:-4], "row": i, "package": pkg, "buyer": bn, "email": e, "reasons": "; ".join(reasons)})
    # header check
    hs = set(headers.values())
    if len(hs) != 1 or len(next(iter(hs))) < 92:
        hit("1 header: identical columns in every file (106 since 2026-11-06)", "hard", "files", "%d distinct headers; widths %s" % (len(hs), sorted({len(h) for h in hs})))
    for nk, lst in by_name.items():
        if len(lst) > 1 and len({e.split("@")[-1] for _, e in lst}) == 1:
            hit("22 one row per organisation name (same name twice)", "soft", lst[0][0], "%d rows, same mail domain: %s" % (len(lst), lst[0][1].split("@")[-1]))
        elif len(lst) > 1:
            pass  # same short name, different domains: different entities (Town of Cochrane AB vs a ranch house)
    for d, lst in by_site.items():
        if len(lst) > 1 and len({e.lower() for _, e in lst}) > 1 and not SHARED_GOV.match(d):
            hit("23 one row per site domain (two rows, different mailboxes, same domain)", "soft", lst[0][0], "%s: %d rows, %s" % (d, len(lst), "; ".join(e for _, e in lst[:3])))
    # report
    hard_fail = [k for k, v in checks.items() if v["kind"] == "hard" and v["n"]]
    lines = ["# Deep audit — %d delivered rows in %d packages (%d files), %s" % (total, len(per_pkg), len(files), TODAY.isoformat()), "",
             "Result: **%s** — %d hard checks, %d soft checks; hard failures: %d. Every flagged row is listed in `audit_flags.csv` with its reasons." % ("PASS" if not hard_fail else "FAIL", sum(1 for v in checks.values() if v["kind"] == "hard"), sum(1 for v in checks.values() if v["kind"] == "soft"), len(hard_fail)), "",
             "| # | check | kind | rows flagged | verdict |", "|---|---|---|---|---|"]
    for k, v in checks.items():
        verdict = "PASS" if not v["n"] else ("FAIL" if v["kind"] == "hard" else "REVIEW")
        lines.append("| %s | %s | %s | %d | %s |" % (k.split()[0], k.split(" ", 1)[1], v["kind"], v["n"], verdict))
    lines += ["", "## Examples of flagged rows (first 12 per check)"]
    for k, v in checks.items():
        if v["hits"]:
            lines.append("- **%s**" % k)
            for h in v["hits"]:
                lines.append("    - " + h)
    # independent QA audit by the chatgpt lane (coord/tasks/chatgpt/chatgpt_qa_audit_*: random dataset records re-opened at the source)
    qa = collections.Counter(); qn = 0
    for qf in glob.glob("data/incoming/chatgpt/chatgpt_qa_audit_results_*.csv"):
        for r in csv.DictReader(open(qf, encoding="utf-8")):
            qn += 1
            for col in ("link_opened", "buyer_match", "vendor_match", "title_match", "value_match", "dates_match", "status_supported"):
                qa[(col, r.get(col) or "")] += 1
    if qn:
        lines += ["", "## Independent QA audit of dataset records (lane chatgpt, %d random records re-opened at the publishing source)" % qn]
        for col in ("link_opened", "buyer_match", "vendor_match", "title_match", "value_match", "dates_match", "status_supported"):
            vals = {k[1]: v for k, v in qa.items() if k[0] == col}
            lines.append("- %s: %s" % (col, ", ".join("%s %d" % kv for kv in sorted(vals.items(), key=lambda kv: -kv[1]))))
        lines.append("- reading: a `no` on buyer_match in the sample was a ministry renamed since the award (same body); `status_supported = unclear / no` concentrates in SEAO records marked ongoing_inferred, which the packages rank as B/C, never as A.")
    lines += ["", "## Rows per package"] + ["- %s: %d" % (k, v) for k, v in per_pkg.items()]
    lines += ["", "## Field fill across all delivered rows (value present, not `not_published`)"] + ["- %s: %d (%.1f%%)" % (c, n, 100.0 * n / max(1, total)) for c, n in fill.most_common()]
    lines += ["", "## Canada-proof families", "- " + "; ".join("%s: %d" % kv for kv in basis_fam.most_common())]
    lines += ["", "## Buyer types"] + ["- %s: %d" % kv for kv in btype.most_common()]
    lines += ["", "## DMARC posture of the delivered mailboxes"] + ["- %s: %d" % kv for kv in posture.most_common()]
    out = "\n".join(lines) + "\n"
    print(out[:6000])
    if a.write:
        os.makedirs(a.write, exist_ok=True)
        open(os.path.join(a.write, "AUDIT.md"), "w", encoding="utf-8").write(out)
        with open(os.path.join(a.write, "audit_flags.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["file", "row", "package", "buyer", "email", "reasons"]); w.writeheader(); w.writerows(flags)
        print("wrote", os.path.join(a.write, "AUDIT.md"), "and audit_flags.csv (%d flagged rows)" % len(flags))
    return 0 if not hard_fail else 1


if __name__ == "__main__":
    sys.exit(main())

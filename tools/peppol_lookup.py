#!/usr/bin/env python3
"""Invoicing mailboxes of foreign public buyers from the Peppol Directory (the e-invoicing network's public registry). No AI.

Public bodies in Australia, New Zealand, the UK (NHS), the Nordics, the Netherlands, Belgium, Germany ... register to
receive e-invoices on Peppol. Their entry ("business card") often names an e-invoicing contact mailbox on their own
domain, e.g. the Australian Department of Defence lists peppol.einvoices@defence.gov.au. For each buyer:
  1. search the directory by name and country (one request per second);
  2. keep entries whose name matches the buyer's name;
  3. keep contacts that are the buyer's own mailbox (tools/ap_crawler.py same_org), never the access point's technical
     contact; open the entry's own JSON page and quote the mailbox from it (that page is the evidence).

    python3 tools/peppol_lookup.py coord/tasks/claude/claude_peppol_targets.csv
Output: data/incoming/claude/claude_buyer_ap_results_peppol01.csv (pushed with the crawler's rows).
"""
import csv, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ap_crawler as C

API = "https://directory.peppol.eu/search/1.0/json?"
OUT = "data/incoming/claude/claude_buyer_ap_results_peppol01.csv"
INVOICE = re.compile(r"invoic|factur|faktur|rechnung|kreditor|crediteur|factuur|fattur|lasku|payable|accounts|ap[._-]|[._-]ap@|"
                     r"compta|leverant|einvoic|e-invoic|peppol|billing|finance|ekonomi|okonomi|regnskab|bogholderi", re.I)
TECH = re.compile(r"accesspoint|access-point|techsupport|tech[._-]support|helpdesk@|noreply|no-reply|servicedesk|peppol@|support@", re.I)
last = [0.0]


def get(url):
    wait = last[0] + 1.0 - time.time()
    if wait > 0:
        time.sleep(wait)
    last[0] = time.time()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": C.UA, "Accept": "application/json"}), timeout=40) as r:
            return r.read(5_000_000).decode("utf-8", "replace")
    except Exception:
        return ""


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(the|of|and|ltd|limited|plc|inc|gmbh|ag|as|a/s|ab|bv|nv|sa|srl|kommune|council)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def matches(buyer, entity):
    a, b = norm(buyer), norm(entity)
    if not a or not b:
        return False
    if a == b or a in b or b in a:
        return True
    ta, tb = set(a.split()), set(b.split())
    return len(ta & tb) >= max(2, int(0.8 * min(len(ta), len(tb))))


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    tasks = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
    done = set()
    if os.path.exists(OUT):
        done = {r["buyer_key"] for r in csv.DictReader(open(OUT, encoding="utf-8"))}
    stats = {"buyers": 0, "entries": 0, "rows": 0}
    for i, t in enumerate(tasks, 1):
        if t["buyer_key"] in done:
            continue
        stats["buyers"] += 1
        name = re.split(r"\s[-–—|(]\s?", t["buyer_name"])[0].strip()
        res = get(API + urllib.parse.urlencode({"q": name, "country": t["country"], "rpc": 20}))
        try:
            matches_ = json.loads(res or "{}").get("matches") or []
        except ValueError:
            matches_ = []
        rows = []
        for m in matches_:
            pid = m.get("participantID") or {}
            for ent in m.get("entities") or []:
                ename = " ".join(n.get("name", "") for n in ent.get("name") or [])
                if not matches(name, ename):
                    continue
                stats["entries"] += 1
                for ct in ent.get("contacts") or []:
                    e = (ct.get("email") or "").strip().lower()
                    loc = e.split("@")[0]
                    if not e or TECH.search(e) or "technical" in (ct.get("type") or "").lower() or not C.EMAIL.match(e) \
                            or (C.PERSONAL.match(loc) and not C.ROLE_HINT.search(loc)) or (not INVOICE.search(loc) and not C.GENERAL.search(loc)):
                        continue  # never a person's mailbox; only invoicing or general role mailboxes
                    if not C.same_org(e, t.get("website") or "https://unknown.invalid", t["buyer_name"]) and not C.same_org(e, "https://unknown.invalid", ename):
                        continue
                    page = API + urllib.parse.urlencode({"participant": "%s::%s" % (pid.get("scheme"), pid.get("value"))})
                    raw = get(page)
                    q = C.quote_for(e, re.sub(r"\s+", " ", raw), raw)
                    if not q:
                        continue
                    kind = "invoice_submission" if INVOICE.search(e.split("@")[0]) else "general"
                    rows.append({"task_id": "CL-PP-%05d" % i, "buyer_key": t["buyer_key"], "org_name_as_found": ename or t["buyer_name"],
                                 "ap_email": e, "ap_email_type": kind, "invoice_portal_url": "", "ap_phone": ct.get("phone") or "",
                                 "invoice_mailing_address": "", "invoicing_requirements_summary": "e-invoices accepted on the Peppol network "
                                 "(participant %s)" % pid.get("value"), "applies_to": "whole_organisation", "evidence_url": page,
                                 "evidence_quote": q, "retrieved_date": C.TODAY, "status": "found",
                                 "queries_tried": "Peppol Directory search: %s (%s)" % (name, t["country"]),
                                 "notes": "contact '%s' in the buyer's own Peppol Directory entry; found by tools/peppol_lookup.py, no AI" % (ct.get("type") or "")})
        seen = set()
        rows = [r for r in rows if not (r["ap_email"] in seen or seen.add(r["ap_email"]))][:3]
        if rows:
            new = not os.path.exists(OUT)
            with open(OUT, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=C.COLS)
                if new:
                    w.writeheader()
                w.writerows(rows)
            stats["rows"] += len(rows)
        if stats["buyers"] % 25 == 0:
            C.log("peppol", stats)
    C.log("peppol finished", stats)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Current member / participant / regulated-institution lists published by Canadian bodies that their members PAY
(annual premiums, market charges, assessments or dues), as leads for a package of their own (P01M / P06M in
rank_buyers: "member or regulated payer of a Canadian body", never mixed with P01 / P01T). No AI.

Each list is a page the body itself publishes (URL + retrieval date kept); each member's name is copied as printed;
the body's head office is quoted from its own site; the fee basis is quoted from its own site. Websites come with the
list when it links them, else tools/site_finder_names.py resolves the names later.
Lists (scoped 2026-11-03, research/members_lists.json): IESO registered participants (JSON), AESO pool participants
(HTML), OSFI federally regulated financial institutions (open-data CSV), CDIC members, Payments Canada members,
Colleges and Institutes Canada, Alberta Municipalities regular members, Canadian Credit Union Association credit unions,
Canadian Bankers Association member banks, CLHIA members, Insurance Bureau of Canada members, Electricity Canada
members. Blocked (bot checks, rule 6): CIRO, AMO, UBCM. No public list: OHA. FCM: province counts only.
Output ~/cch-leads/socrata_member_lists.jsonl ; python3 tools/member_lists.py [--only ieso,aeso,...]
"""
import argparse, csv, html, io, json, os, re, sys, time, urllib.parse, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import client_lists as CL

LEADS = os.path.expanduser("~/cch-leads")
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
TODAY = time.strftime("%Y-%m-%d")
FIELD = "membership / statutory fee relationship: current list published by the Canadian body (%s)"

BODIES = {
    "ieso": dict(legal="Independent Electricity System Operator", hq="Independent Electricity System Operator 1600-120 Adelaide Street West Toronto, ON M5H 1T1",
                 hq_url="https://www.ieso.ca/Corporate-IESO/Contact", list_url="https://ieso.ca/Sector-Participants/Registered-Participants",
                 data_url="https://ieso.ca/ieso/api/table/data?source=936CC413D1564B988F7770AB7C07719F&ctx=%7B7902D088-6AA6-465B-8C74-E3959D8DCB5B%7D",
                 fee="market participants pay the IESO's market fees and administration charges (IESO market rules); registered participants list 'Last Updated: June 19, 2026'",
                 fee_url="https://ieso.ca/Sector-Participants/Registered-Participants", kind="json"),
    "aeso": dict(legal="Alberta Electric System Operator", hq="3000, 240 - 4 Avenue S.W. Calgary, Alberta T2P 4H4",
                 hq_url="https://www.aeso.ca/market/market-and-system-reporting/pool-participant-lists/",
                 list_url="https://www.aeso.ca/market/market-and-system-reporting/pool-participant-lists/",
                 data_url="http://ets.aeso.ca/ets_web/ip/Market/Reports/ParticipantListReportServlet?contentType=html",
                 fee="The AESO recovers the costs of operating the real-time energy market through an energy market trading charge on all electricity traded.",
                 fee_url="https://www.aeso.ca/market/market-participation/energy-market-trading-charge/", kind="aeso"),
    "osfi": dict(legal="Office of the Superintendent of Financial Institutions", hq="255 Albert Street, Ottawa, Ontario K1A 0H2",
                 hq_url="https://www.osfi-bsif.gc.ca/en/about-osfi/contact-us", list_url="https://open.canada.ca/data/en/dataset/b27ec3ef-7338-4e76-a6fd-128339a92df5",
                 data_url="https://open.canada.ca/data/dataset/b27ec3ef-7338-4e76-a6fd-128339a92df5/resource/945045fa-2de0-47d4-aad2-144d69467824/download/who_we_regulate_fi_eng.csv",
                 fee="federally regulated financial institutions pay OSFI's costs through base assessments and service charges (OSFI Act s. 23; Assessment of Financial Institutions Regulations)",
                 fee_url="https://laws-lois.justice.gc.ca/eng/acts/O-2.7/section-23.html", kind="csv", name_col="Company Name", skip_groups=("Foreign Bank Representative Offices",)),
    "cdic": dict(legal="Canada Deposit Insurance Corporation", hq="50 O’Connor Street, 17 th floor Ottawa, ON K1P 6L2", hq_url="https://www.cdic.ca/about/contact-us/",
                 list_url="https://www.cdic.ca/depositors/list-of-members/", data_url="https://www.cdic.ca/depositors/list-of-members/",
                 fee="Each CDIC member institution must pay annual premiums on insured deposits as a condition of membership.",
                 fee_url="https://www.cdic.ca/financial-professionals/member-institutions/premiums/", kind="li"),
    "payments": dict(legal="Canadian Payments Association (Payments Canada)", hq="Ottawa Constitution Square, Tower II 350 Albert, Suite 800 Ottawa, ON K1R 1A4",
                     hq_url="https://www.payments.ca/connect/contact", list_url="https://www.payments.ca/about/our-members-stakeholders/members",
                     data_url="https://www.payments.ca/about/our-members-stakeholders/members",
                     fee="All Payments Canada members are subject to an annual membership fee or common services dues. This fee is $49,544 per member for 2026.",
                     fee_url="https://www.payments.ca/systems-services/payment-systems/payments-canada-fees", kind="payments"),
    "cican": dict(legal="Colleges and Institutes Canada", hq="Colleges and Institutes Canada, Ottawa, Ontario", hq_url="https://www.collegesinstitutes.ca/",
                  list_url="https://www.collegesinstitutes.ca/colleges-and-institutes-in-your-community/our-members/",
                  data_url="https://www.collegesinstitutes.ca/colleges-and-institutes-in-your-community/our-members/",
                  fee="member colleges and institutes pay annual membership dues", fee_url="https://www.collegesinstitutes.ca/colleges-and-institutes-in-your-community/our-members/", kind="cican"),
    "abmunis": dict(legal="Alberta Municipalities", hq="Alberta Municipalities, 300, 8616 - 51 Avenue, Edmonton, AB T6E 6E6", hq_url="https://www.abmunis.ca/membership/regular-members",
                    list_url="https://www.abmunis.ca/membership/regular-members", data_url="https://www.abmunis.ca/membership/regular-members",
                    fee="support for Alberta Municipalities through annual membership fees, helps ensure that we keep municipal issues and needs at the forefront of provincial agendas.",
                    fee_url="https://www.abmunis.ca/membership", kind="anchors", site_re=r"^https?://(?!www\.abmunis\.ca)"),
    "ccua": dict(legal="Canadian Credit Union Association", hq="World Exchange Plaza 45 O’Connor St. Suite 860 Ottawa, ON K1P 1A4", hq_url="https://ccua.com/contact-us/",
                 list_url="https://ccua.com/about-credit-unions/find-a-credit-union/", data_url="https://ccua.com/about-credit-unions/find-a-credit-union/",
                 fee="member credit unions pay CCUA membership dues", fee_url="https://ccua.com/about-ccua/membership/", kind="options"),
    "cba": dict(legal="Canadian Bankers Association", hq="Toronto Main Office Commerce Court West 199 Bay Street, 28th Floor Toronto, Ontario M5L 1G2",
                hq_url="https://cba.ca/article/member-banks", list_url="https://cba.ca/article/member-banks", data_url="https://cba.ca/article/member-banks",
                fee="member banks pay CBA membership dues", fee_url="https://cba.ca/article/member-banks", kind="anchors", site_re=r"^https?://(?!(?:www\.)?cba\.ca)"),
    "clhia": dict(legal="Canadian Life and Health Insurance Association", hq="Canadian Life and Health Insurance Association, Toronto, Ontario", hq_url="https://www.clhia.ca/",
                  list_url="https://www.clhia.ca/en-ca/about/membership-information/our-members", data_url="https://www.clhia.ca/en-ca/about/membership-information/our-members",
                  fee="member insurers pay CLHIA membership dues", fee_url="https://www.clhia.ca/en-ca/about/membership-information", kind="h3"),
    "ibc": dict(legal="Insurance Bureau of Canada", hq="Insurance Bureau of Canada, Toronto, Ontario", hq_url="https://www.ibc.ca/",
                list_url="https://www.ibc.ca/industry-resources/ibc-advantage/our-members", data_url="https://www.ibc.ca/industry-resources/ibc-advantage/our-members",
                fee="member insurers pay IBC membership dues", fee_url="https://www.ibc.ca/industry-resources/ibc-advantage", kind="anchors", site_re=r"^https?://(?!(?:www\.)?ibc\.ca)"),
    "elec": dict(legal="Electricity Canada", hq="Electricity Canada 275 Slater Street, Suite 1500 Ottawa, Ontario, Canada K1P 5H9",
                 hq_url="https://www.electricity.ca/membership/list-of-members/", list_url="https://www.electricity.ca/membership/list-of-members/",
                 data_url="https://www.electricity.ca/membership/list-of-members/", fee="member utilities pay Electricity Canada membership dues",
                 fee_url="https://www.electricity.ca/membership/join-electricity-canada/", kind="elec"),
}
NOT_MEMBER = re.compile(r"^(home|about|contact|members?|membership|join|login|search|privacy|terms|français|english|skip|menu|news|events?|"
                        r"careers?|sitemap|accessibility|donate|subscribe|view all|see all|back|next|previous|page \d+)$", re.I)


def get(url):
    if not CL.allowed(url):
        return ""
    page, final = CL.fetch(url, limit=20_000_000) if "limit" in CL.fetch.__code__.co_varnames else CL.fetch(url)
    return page or ""


def text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def members(key, b):
    out = []  # (name, website, as_printed)
    kind = b["kind"]
    if kind == "json":
        req = urllib.request.Request(b["data_url"], headers={"User-Agent": UA, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
        if isinstance(d, list) and d and isinstance(d[0], dict) and "TableRows" in d[0]:
            d = d[0]
        rows = d if isinstance(d, list) else (d.get("TableRows") or d.get("Rows") or d.get("rows") or d.get("data") or d.get("Data") or [])
        for row in rows:
            cells = row if isinstance(row, list) else (row.get("Cells") or row.get("cells") or list(row.values()))
            vals = []
            for c in cells:
                v = c.get("Value") if isinstance(c, dict) else c
                vals.append(text(str(v)) if v is not None else "")
            name = next((v for v in vals if v and len(v) > 2 and not re.fullmatch(r"[\d\s./-]+", v)), "")
            if name:
                out.append((name, "", " | ".join(v for v in vals if v)[:200]))
    elif kind == "aeso":
        page = get(b["data_url"])
        for tr in re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", page):
            tds = [text(x) for x in re.findall(r"(?is)<td[^>]*>(.*?)</td>", tr)]
            if len(tds) >= 2 and tds[0] and not re.match(r"(?i)pool participant name", tds[0]):
                out.append((tds[0], "", " | ".join(tds[:3])[:200]))
    elif kind == "csv":
        req = urllib.request.Request(b["data_url"], headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read().decode("utf-8-sig", "replace")
        for row in csv.DictReader(io.StringIO(body)):
            name = (row.get(b["name_col"]) or "").strip()
            grp = (row.get("FI Group Name") or "")
            if name and not any(s.lower() in grp.lower() for s in b.get("skip_groups", ())):
                out.append((name, "", " | ".join("%s: %s" % (k, v) for k, v in row.items() if v and k in ("Company Name", "FI Type Name", "FI Group Name", "Province"))[:200]))
    elif kind == "li":
        page = get(b["data_url"])
        sec = page[page.find("members-"):] if "members-" in page else page
        for li in re.findall(r"(?is)<li[^>]*>(.*?)</li>", sec):
            n = text(li)
            if 2 < len(n) < 120 and not NOT_MEMBER.match(n) and not re.search(r"https?://|@", n):
                out.append((n, "", n))
    elif kind == "payments":
        page = get(b["data_url"])
        t = text(page)
        m = re.search(r"Members\s*\(\s*As of ([^)]+)\)\s*:?\s*(.*?)(?:Stakeholders|$)", t)
        if m:
            blob = m.group(2)
            # 'ATB, Ryan Rabin Bank of America, Leslie Konecny Bank of Canada, ...': each member name follows a representative's
            # two-word name; take the text between a comma and the next capitalised two-word person name as the member
            parts = re.split(r",\s*", blob)
            for p in parts:
                p = p.strip()
                mm = re.match(r"^(?:[A-Z][a-z'’\-]+(?:\s+[A-Z]\.)?\s+[A-Z][a-zA-Z'’\-]+)\s+(.+)$", p)
                name = (mm.group(1) if mm else p).strip()
                if 2 < len(name) < 100 and not NOT_MEMBER.match(name):
                    out.append((name, "", p[:200]))
    elif kind == "cican":
        page = get(b["data_url"])
        for href, inner in re.findall(r'(?is)<a[^>]+href="(https://www\.collegesinstitutes\.ca/members/[^"]+)"[^>]*>(.*?)</a>', page):
            n = text(inner)
            if 2 < len(n) < 120:
                out.append((n, "", n))
    elif kind == "anchors":
        page = get(b["data_url"])
        for href, inner in re.findall(r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', page):
            n = text(inner)
            if re.match(b["site_re"], href) and 2 < len(n) < 120 and not NOT_MEMBER.match(n) and not re.search(r"facebook|twitter|linkedin|instagram|youtube|x\.com", href):
                out.append((n, href, n))
    elif kind == "options":
        page = get(b["data_url"])
        for inner in re.findall(r"(?is)<option[^>]*>(.*?)</option>", page):
            n = text(inner)
            if 3 < len(n) < 120 and not re.match(r"(?i)select", n):
                out.append((n, "", n))
    elif kind == "h3":
        page = get(b["data_url"])
        for inner in re.findall(r"(?is)<h3[^>]*>(.*?)</h3>", page):
            n = text(inner)
            if 2 < len(n) < 120 and not NOT_MEMBER.match(n):
                out.append((n, "", n))
    elif kind == "elec":
        for pg in range(1, 7):
            url = b["data_url"] + ("" if pg == 1 else "page/%d/" % pg)
            page = get(url)
            found = 0
            for href, inner in re.findall(r'(?is)<a[^>]+href="(https?://(?!www\.electricity\.ca)[^"]+)"[^>]*>(.*?)</a>', page):
                n = text(inner)
                if 5 < len(n) < 400 and re.search(r"[A-Z]\d[A-Z] ?\d[A-Z]\d", n):  # name + address + postal code
                    name = re.split(r"\s+\d", n, 1)[0].strip(" ,")
                    if 2 < len(name) < 120:
                        out.append((name, href, n[:200])); found += 1
            if not found:
                break
    seen, res = set(), []
    for n, w, ap in out:
        k = re.sub(r"[^a-z0-9]+", " ", n.lower()).strip()
        if k and k not in seen:
            seen.add(k); res.append((n, w, ap))
    return res


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--only", default="")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    keys = [k for k in BODIES if not a.only or k in a.only.split(",")]
    leads = []
    for k in keys:
        b = BODIES[k]
        try:
            ms = members(k, b)
        except Exception as e:
            print("%s: %s" % (k, e), flush=True)
            ms = []
        print("%-9s %4d members" % (k, len(ms)), flush=True)
        for n, w, ap in ms:
            host = (urllib.parse.urlparse(w).hostname or "").lower().removeprefix("www.") if w else ""
            leads.append({"platform": "member_list", "domain": host or ("member." + k), "dataset_id": "%s:%s" % (k, re.sub(r"[^a-z0-9]+", "-", n.lower())[:60]),
                          "dataset": "current %s list published by %s" % ({"ieso": "registered participant", "aeso": "pool participant", "osfi": "federally regulated financial institution",
                                                                           "cdic": "member institution"}.get(k, "member"), b["legal"]),
                          "dataset_url": b["list_url"], "publisher": n, "buyer_unit": "", "website": ("https://%s/" % host) if host else "", "vendor": b["legal"],
                          "canada_field": FIELD % b["legal"], "canada_value": b["hq"],
                          "row": {"record_date": TODAY, "member_as_printed": ap, "list_url": b["list_url"], "data_url": b["data_url"], "body_hq_url": b["hq_url"],
                                  "fee_basis": b["fee"], "fee_url": b["fee_url"], "retrieved": TODAY, "body": k}})
    path = os.path.join(LEADS, "socrata_member_lists.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for r in leads:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("wrote %d leads -> %s" % (len(leads), path), flush=True)


if __name__ == "__main__":
    main()

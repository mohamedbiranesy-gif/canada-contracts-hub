#!/usr/bin/env python3
"""New buyers that work with Canadian suppliers, from US federal SUBAWARD data (USAspending.gov). No AI.

Prime recipients of US federal contracts and grants (companies, universities, hospitals, non-profits, states) must
report the subcontracts and subgrants they give. When the subawardee's own reported country is Canada (CAN), the
prime is a buyer that pays a Canadian supplier: thousands of distinct private and institutional buyers that no
procurement portal shows. Prime awards made directly to Canadian recipients add the awarding US agencies.

  python3 tools/usaspending_scanner.py --group contracts|grants
Leads: ~/cch-leads/socrata_usasub_<group>.jsonl (same format as tools/lead_scanner.py; its --bridge turns them into
crawler tasks; tools/site_finder.py looks up the buyer's website; tools/ap_crawler.py finds the invoicing e-mail).
Polite: one request per second (2 groups = at most 2 per second on the host).
"""
import argparse, json, os, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lead_scanner import LEADS, UA

API = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
CODES = {"contracts": ["A", "B", "C", "D"], "grants": ["02", "03", "04", "05"]}
SUB_FIELDS = ["Sub-Award ID", "Sub-Awardee Name", "Sub-Award Date", "Sub-Award Amount", "Prime Recipient Name",
              "Prime Award ID", "Awarding Agency", "Awarding Sub Agency", "Sub-Award Description", "prime_award_recipient_id"]
PRIME_FIELDS = ["Award ID", "Recipient Name", "Start Date", "End Date", "Award Amount", "Awarding Agency",
                "Awarding Sub Agency", "Description"]


def post(body):
    time.sleep(1.0)
    req = urllib.request.Request(API, data=json.dumps(body).encode(), headers={"User-Agent": UA, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        return None, "%s %s" % (e.code, e.read()[:300])
    except Exception as e:
        return None, repr(e)


def run(group, sub):
    out = os.path.join(LEADS, "socrata_usasub_%s%s.jsonl" % (group, "" if sub else "_prime"))
    state = out + ".page"
    page = int(open(state).read()) if os.path.exists(state) else 1
    filters = {"award_type_codes": CODES[group], "recipient_locations": [{"country": "CAN"}],
               "time_period": [{"start_date": "2016-10-01", "end_date": "2026-09-30"}]}
    variants = [{"spending_level": "subawards"}, {"subawards": True}] if sub else [{}]
    while True:
        data = err = None
        for v in variants:
            body = dict({"filters": filters, "fields": SUB_FIELDS if sub else PRIME_FIELDS, "limit": 100, "page": page,
                         "sort": "Sub-Award Amount" if sub else "Award Amount", "order": "desc"}, **v)
            data, err = post(body)
            if data is not None:
                variants = [v]
                break
        if data is None:
            print(group, "sub" if sub else "prime", "page", page, "error", err, flush=True)
            time.sleep(60)
            continue
        rows = data.get("results") or []
        with open(out, "a", encoding="utf-8") as f:
            for r in rows:
                if sub:
                    buyer, vendor = r.get("Prime Recipient Name") or "", r.get("Sub-Awardee Name") or ""
                else:
                    buyer = " - ".join(x for x in (r.get("Awarding Agency"), r.get("Awarding Sub Agency")) if x)
                    vendor = r.get("Recipient Name") or ""
                if not buyer:
                    continue
                f.write(json.dumps({"platform": "usaspending", "domain": "usaspending.gov", "dataset_id": group,
                                    "dataset": "USAspending %s %s to recipients located in Canada" % (group, "subawards" if sub else "prime awards"),
                                    "dataset_url": "https://www.usaspending.gov/award/%s" % (r.get("generated_internal_id") or r.get("Prime Award ID") or r.get("Award ID") or ""),
                                    "publisher": buyer.strip().title(), "buyer_unit": "", "website": "", "vendor": vendor,
                                    "canada_field": "subawardee country" if sub else "recipient country", "canada_value": "CAN", "row": r},
                                   ensure_ascii=False) + "\n")
        print(group, "sub" if sub else "prime", "page", page, "rows", len(rows), flush=True)
        page += 1
        open(state, "w").write(str(page))
        if not (data.get("page_metadata") or {}).get("hasNext") or not rows:
            break
    print(group, "done", flush=True)


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--group", choices=["contracts", "grants"], default="contracts")
    a = a.parse_args()
    os.makedirs(LEADS, exist_ok=True)
    run(a.group, True)
    run(a.group, False)

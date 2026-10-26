"""Stage A (sec_edgar): run EDGAR full-text search queries restricted to Canadian
filer locations; save all hits to downloads/sec_edgar/hits.jsonl (dedup by _id)."""
import requests, json, time, urllib.parse, datetime, os, sys
UA = {"User-Agent": "contracts-research research@example.com", "Accept-Encoding": "gzip, deflate"}
OUT = "downloads/sec_edgar"
CA_CODES = "A0,A1,A5,A6,A8,Z4"   # codes with hits: AB, BC, NS, ON, QC, Canada(federal)
# (A2 MB, A3 NB, A4 NL, A7 PE, A9 SK, B0 YT returned 0 hits for 'agreement' 8-K 2024-2026)
seen = set()
if os.path.exists(f"{OUT}/hits.jsonl"):
    for line in open(f"{OUT}/hits.jsonl"):
        try: seen.add(json.loads(line)["_id"])
        except: pass
out = open(f"{OUT}/hits.jsonl", "a", encoding="utf-8")
log = open(f"{OUT}/harvest.log", "a")
def run(qtext, forms, label, max_pages=30):
    total_new = 0
    for page in range(1, max_pages+1):
        params = {"q": qtext, "dateRange":"custom","startdt":"2024-01-01","enddt":"2026-10-25","locationCodes": CA_CODES, "page": str(page), "from": str((page-1)*100)}
        if forms: params["forms"] = forms
        url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode(params)
        for attempt in range(3):
            try:
                r = requests.get(url, headers=UA, timeout=60)
                if r.status_code == 200: break
                time.sleep(2*(attempt+1))
            except Exception as e:
                time.sleep(3)
        else:
            log.write(f"FAIL {url}\n"); return
        j = r.json()
        hits = j["hits"]["hits"]
        total = j["hits"]["total"]["value"]
        if page == 1:
            log.write(f"{datetime.datetime.now(datetime.UTC).isoformat()} query={qtext!r} forms={forms} total={total}\n"); log.flush()
            print(f"[{label}] total={total}", flush=True)
        for h in hits:
            if h["_id"] in seen: continue
            seen.add(h["_id"])
            h["_query"] = label
            h["_retrieved_at"] = datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00","Z")
            out.write(json.dumps(h, ensure_ascii=False)+"\n"); total_new += 1
        out.flush()
        if len(hits) < 100 or page*100 >= min(total, 10000): break
        time.sleep(0.15)
    print(f"[{label}] new hits saved: {total_new}", flush=True)

QUERIES = [
 # (query text, forms, label)
 ('"master services agreement"', None, "msa"),
 ('"supply agreement"', None, "supply"),
 ('"master supply agreement"', None, "master_supply"),
 ('"services agreement"', "8-K,6-K", "services_8k6k"),
 ('"license agreement"', "8-K,6-K", "license"),
 ('"distribution agreement"', None, "distribution"),
 ('"collaboration agreement"', None, "collaboration"),
 ('"manufacturing agreement"', None, "manufacturing"),
 ('"offtake agreement"', None, "offtake"),
 ('"purchase agreement" supplier', "8-K,6-K", "purchase_supplier"),
 ('"statement of work"', None, "sow"),
 ('"subscription agreement" software', "8-K,6-K", "subscription_sw"),
 ('"development agreement"', "8-K,6-K", "development"),
 ('"commercial agreement"', None, "commercial"),
 ('"framework agreement"', None, "framework"),
 ('"contract award" OR "awarded a contract" OR "awarded contract"', None, "award"),
 ('"Entry into a Material Definitive Agreement"', "8-K", "item101"),
 ('"customer" agreement term years', "6-K", "customer_6k"),
 ('"long-term agreement"', None, "lta"),
 ('"power purchase agreement"', None, "ppa"),
 ('"tolling agreement"', None, "tolling"),
 ('"streaming agreement"', None, "streaming"),  # mining: usually financing -> will filter later
 ('"reseller agreement"', None, "reseller"),
 ('"co-promotion agreement" OR "commercialization agreement"', None, "commercialization"),
 ('"master agreement"', None, "master"),
 ('"service contract" OR "services contract"', None, "service_contract"),
 ('"teaming agreement"', None, "teaming"),
 ('"engineering, procurement and construction"', None, "epc"),
 ('"take-or-pay"', None, "takeorpay"),
 ('"minimum purchase" agreement', None, "minpurchase"),
]
if __name__ == "__main__":
    for qtext, forms, label in QUERIES:
        run(qtext, forms, label)
        time.sleep(0.3)
    print("DONE. unique hits:", len(seen))

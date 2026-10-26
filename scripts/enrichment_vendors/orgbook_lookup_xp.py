#!/usr/bin/env python3
"""Look up BC-located vendors in BC OrgBook (public API) to get registration number, status and Business Number.

Usage: python3 -I orgbook_lookup.py <vendor_master.jsonl> <out.jsonl> [max_vendors]
Resumable: vendor_keys already present in <out.jsonl> are skipped. ~2 requests/second.
"""
import sys, os, json, time, urllib.parse, urllib.request, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from normname import strict_key, loose_key, norm_prov  # noqa: E402

VM, OUT = sys.argv[1], sys.argv[2]
MAXV = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
SHARD = int(sys.argv[4]) if len(sys.argv) > 4 else 0
NSH = int(sys.argv[5]) if len(sys.argv) > 5 else 1
import glob
API = "https://orgbook.gov.bc.ca/api/v4/search/topic?q={}&inactive=any&revoked=false&page_size=20"
UA = {"User-Agent": "contracts-research/1.0 (vendor registry matching; polite, 2 req/s)"}
ENTITY_TYPES = {"A": "Extraprovincial company", "BC": "BC company", "ULC": "BC unlimited liability company", "CC": "BC community contribution company",
                "BEN": "BC benefit company", "SP": "Sole proprietorship", "GP": "General partnership", "LP": "Limited partnership", "LLP": "Limited liability partnership",
                "S": "Society", "XS": "Extraprovincial society", "CP": "Cooperative", "XP": "Extraprovincial limited partnership", "XL": "Extraprovincial LLP"}

done = set()
for _p in glob.glob(OUT.split('.shard')[0] + '.shard*'):
    with open(_p, encoding="utf-8") as f:
        for line in f:
            try:
                done.add(json.loads(line)["vendor_key"])
            except Exception:
                pass

nobn = set()
with open("enrichment/v2/vendors_registry_v3.jsonl", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        if not (d.get("tax") or {}).get("bn9"):
            nobn.add(d["vendor_key"])
todo = []
with open(VM, encoding="utf-8") as f:
    for line in f:
        v = json.loads(line)
        provs = set()
        for a in v.get("addresses") or []:
            val = a.get("value") or {}
            if isinstance(val, dict):
                p = norm_prov(val.get("region"))
                if p:
                    provs.add(p)
        if provs and "BC" not in provs and v["vendor_key"] in nobn and v["vendor_key"] not in done:
            todo.append((v.get("record_count_high_or_medium") or 0, v.get("record_count") or 0, v["vendor_key"], v.get("name"), v.get("name_variants") or [], sorted(provs)))
todo.sort(key=lambda t: (-t[0], -t[1]))
todo = todo[:MAXV][SHARD::NSH]
print("todo", len(todo), "already", len(done), file=sys.stderr, flush=True)


def get(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            err = str(e)
            if "403" in err or "429" in err:
                time.sleep(30 * (attempt + 1))
            else:
                time.sleep(3 * (attempt + 1))
    return None


with open(OUT, "a", encoding="utf-8") as out:
    for n, (hm, rc, vk, name, variants, provs) in enumerate(todo):
        names = [name] + [x for x in variants if x != name][:2]
        vs_strict = {strict_key(x) for x in names if x}
        vs_loose = {loose_key(x) for x in names if x}
        cands = {}
        for qi, q in enumerate(names[:2]):
            if not q or (qi > 0 and cands):
                continue
            d = get(API.format(urllib.parse.quote(q)))
            time.sleep(1.5)
            if not d:
                continue
            for r in d.get("results", []):
                ent_names = [x["text"] for x in r.get("names", []) if x.get("type") == "entity_name"]
                bns = [x["text"] for x in r.get("names", []) if x.get("type") == "business_number"]
                attrs = {a["type"]: a["value"] for a in r.get("attributes", [])}
                sk = {strict_key(x) for x in ent_names}
                lk = {loose_key(x) for x in ent_names}
                if not (sk & vs_strict or lk & vs_loose):
                    continue
                cands[r["source_id"]] = {"registry": "bc_orgbook", "legal_name": ent_names[0] if ent_names else None, "other_names": ent_names[1:],
                                         "registration_number": r.get("source_id"), "business_number_bn9": (bns[0][:9] if bns else None),
                                         "entity_type": ENTITY_TYPES.get(attrs.get("entity_type"), attrs.get("entity_type")),
                                         "status": {"ACT": "Active", "HIS": "Historical"}.get(attrs.get("entity_status"), attrs.get("entity_status")),
                                         "registration_date": attrs.get("registration_date"), "registered_jurisdiction": attrs.get("registered_jurisdiction"),
                                         "home_jurisdiction": attrs.get("home_jurisdiction"),
                                         "_strict": bool(sk & vs_strict), "source_url": "https://orgbook.gov.bc.ca/entity/%s" % r.get("source_id"),
                                         "dataset_url": "https://orgbook.gov.bc.ca/", "retrieved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                         "raw": r}
        cl = list(cands.values())
        strict_active = [c for c in cl if c["_strict"] and c["status"] == "Active" and (c.get("home_jurisdiction") or "") in provs]
        for c in cl:
            if c in strict_active and len(strict_active) == 1:
                c["match_confidence"] = "strong"
                c["match_basis"] = "name equal after normalisation; active extraprovincial registration in BC whose home jurisdiction (%s) equals the vendor's province; only such entity" % c.get("home_jurisdiction")
            else:
                c["match_confidence"] = "weak"
                c["match_basis"] = ("name equal after normalisation" if c["_strict"] else "name equal except legal-form suffix") + "; %d candidate(s); status %s" % (len(cl), c["status"])
            del c["_strict"]
        cl.sort(key=lambda c: (c["match_confidence"] != "strong", c["status"] != "Active"))
        out.write(json.dumps({"vendor_key": vk, "name": name, "queried": names[:2], "matches": cl[:6]}, ensure_ascii=False) + "\n")
        out.flush()
        if n % 200 == 0:
            print("orgbook", n, "/", len(todo), file=sys.stderr, flush=True)
print("done", file=sys.stderr)

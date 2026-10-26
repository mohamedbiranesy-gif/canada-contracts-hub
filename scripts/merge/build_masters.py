#!/usr/bin/env python3
"""Build vendor and buyer master lists from the merged normalized file.

Usage: python3 -I build_masters.py <normalized_jsonl> <out_dir>
Writes <out_dir>/vendor_master_input.jsonl and <out_dir>/buyer_master_input.jsonl
"""
import sys, os, json, re, unicodedata, collections, hashlib

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

LEGAL = re.compile(r"\b(inc|incorporated|ltd|ltee|ltée|limited|limitee|limitée|corp|corporation|co|company|compagnie|llc|lp|llp|plc|gmbh|ag|sa|s\.a|srl|bv|nv|pty|the|le|la|les|l|d|de|du|des|et|and|&|group|groupe|holdings|holding|international|intl|canada|canadian|canadienne|canadien)\b")
NONALNUM = re.compile(r"[^a-z0-9 ]+")
SPACES = re.compile(r"\s+")

def stem(name):
    if not name:
        return ""
    s = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode().lower()
    s = NONALNUM.sub(" ", s)
    s = LEGAL.sub(" ", s)
    return SPACES.sub(" ", s).strip()

def key(prefix, *parts):
    return prefix + ":" + hashlib.sha1("|".join(p or "" for p in parts).encode()).hexdigest()[:16]

vendors = {}
buyers = {}
HIGH = {"high", "high_flagged_date", "medium"}

with open(SRC, encoding="utf-8") as f:
    for line in f:
        r = json.loads(line)
        v = r.get("vendor") or {}
        b = r.get("buyer") or {}
        src = r["source"]["key"]
        conf = r.get("status_confidence")
        # ---- vendor ----
        vs = stem(v.get("name"))
        if vs:
            vk = key("v", vs)
            d = vendors.get(vk)
            if d is None:
                d = vendors[vk] = {"vendor_key": vk, "stem": vs, "names": collections.Counter(), "countries": collections.Counter(),
                                   "country_basis": collections.Counter(), "addresses": collections.Counter(), "identifiers": collections.defaultdict(collections.Counter),
                                   "contacts": collections.Counter(), "sources": collections.Counter(), "record_count": 0, "record_count_high_or_medium": 0,
                                   "example_record_ids": []}
            d["names"][v.get("name")] += 1
            d["countries"][v.get("country") or ""] += 1
            d["country_basis"][str(v.get("country_basis") or "")[:120]] += 1
            a = v.get("address") or {}
            addr = json.dumps({k: a.get(k) for k in ("line1", "line2", "city", "region", "postal_code", "country") if a.get(k)}, ensure_ascii=False, sort_keys=True)
            if addr != "{}":
                d["addresses"][addr] += 1
            for ik, iv in (v.get("identifiers") or {}).items():
                if iv not in (None, "", []):
                    d["identifiers"][ik][str(iv)[:80]] += 1
            c = v.get("contact") or {}
            if c:
                d["contacts"][json.dumps(c, ensure_ascii=False, sort_keys=True)] += 1
            d["sources"][src] += 1
            d["record_count"] += 1
            if conf in HIGH:
                d["record_count_high_or_medium"] += 1
            if len(d["example_record_ids"]) < 5:
                d["example_record_ids"].append(r["record_id"])
        # ---- buyer ----
        bs = stem(b.get("name"))
        if bs:
            bc = b.get("country") or ""
            bk = key("b", bs, bc)
            d = buyers.get(bk)
            if d is None:
                d = buyers[bk] = {"buyer_key": bk, "stem": bs, "country": bc, "names": collections.Counter(), "types": collections.Counter(),
                                  "identifiers": collections.defaultdict(collections.Counter), "addresses": collections.Counter(), "contacts": collections.Counter(),
                                  "sources": collections.Counter(), "record_count": 0, "record_count_high_or_medium": 0, "example_record_ids": []}
            d["names"][b.get("name")] += 1
            d["types"][b.get("type") or ""] += 1
            for ik, iv in (b.get("identifiers") or {}).items():
                if iv not in (None, "", []):
                    d["identifiers"][ik][str(iv)[:120]] += 1
            a = b.get("address") or {}
            if a:
                d["addresses"][json.dumps(a, ensure_ascii=False, sort_keys=True)] += 1
            c = b.get("contact") or {}
            if c:
                d["contacts"][json.dumps(c, ensure_ascii=False, sort_keys=True)] += 1
            d["sources"][src] += 1
            d["record_count"] += 1
            if conf in HIGH:
                d["record_count_high_or_medium"] += 1
            if len(d["example_record_ids"]) < 5:
                d["example_record_ids"].append(r["record_id"])

def finalize(d, namekey):
    out = dict(d)
    out["name"] = d["names"].most_common(1)[0][0]
    out["name_variants"] = [n for n, _ in d["names"].most_common(10)]
    del out["names"]
    for k in ("countries", "country_basis", "addresses", "contacts", "sources", "types"):
        if k in out:
            out[k] = [{"value": (json.loads(v) if k in ("addresses", "contacts") and v.startswith("{") else v), "count": c} for v, c in d[k].most_common(8)]
    out["identifiers"] = {ik: [{"value": v, "count": c} for v, c in cnt.most_common(5)] for ik, cnt in d["identifiers"].items()}
    return out

with open(os.path.join(OUT, "vendor_master_input.jsonl"), "w", encoding="utf-8") as f:
    for d in sorted(vendors.values(), key=lambda x: (-x["record_count_high_or_medium"], -x["record_count"])):
        f.write(json.dumps(finalize(d, "name"), ensure_ascii=False) + "\n")
with open(os.path.join(OUT, "buyer_master_input.jsonl"), "w", encoding="utf-8") as f:
    for d in sorted(buyers.values(), key=lambda x: (-x["record_count_high_or_medium"], -x["record_count"])):
        f.write(json.dumps(finalize(d, "name"), ensure_ascii=False) + "\n")
print("vendors", len(vendors), "buyers", len(buyers))

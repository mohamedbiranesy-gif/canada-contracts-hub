#!/usr/bin/env python3
"""Generic OCDS Data Registry harvester: streams a publication's jsonl.gz (one release per line) from
data.open-contracting.org, keeps only releases with a Canada-addressed supplier, writes docs/SCHEMA.md records.
Usage: python3 -I ocds_harvest.py <pub_id> <source_key> <ISO2 buyer country> <year-file>[,<year-file>...] <out.jsonl.gz> [--name NAME]
Year files are the registry's names, e.g. 2025.jsonl.gz or full.jsonl.gz. Streams via curl, stores nothing else.
"""
import sys, gzip, json, subprocess, re, datetime, zlib, collections
UA = "canada-contracts-hub-crawler/1.0 (+https://github.com/mohamedbiranesy-gif/canada-contracts-hub)"
REF = "2026-11-12"
CA = {"canada", "ca", "can", "canadá", "canada ", "canadà", "kanada", "канада", "canadá."}

def d10(s):
    if not s or not isinstance(s, str): return None
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else None

def is_ca(p):
    a = p.get("address") or {}
    for k in ("countryName", "country"):
        v = a.get(k)
        if isinstance(v, str) and v.strip().lower() in CA: return k
    return None

def stream(pub, fname):
    """Stream lines; on a curl error (e.g. HTTP/2 reset) restart and skip the lines already yielded."""
    done = 0
    for attempt in range(6):
        rc = None; n = 0
        for item in stream_once(pub, fname):
            if isinstance(item, tuple): rc = item[1]; break
            n += 1
            if n > done:
                done = n; yield item
        if rc == 0: break
        print("retry", fname, "rc", rc, "after", done, "lines", file=sys.stderr, flush=True)
    yield ("RC", rc)

def stream_once(pub, fname):
    url = "https://data.open-contracting.org/en/publication/%s/download?name=%s" % (pub, fname)
    p = subprocess.Popen(["curl", "-sSL", "--fail", "--http1.1", "--cacert", "/root/.ccr/ca-bundle.crt", "-A", UA, url], stdout=subprocess.PIPE)
    dec = zlib.decompressobj(16 + zlib.MAX_WBITS)
    buf = b""
    while True:
        chunk = p.stdout.read(1 << 20)
        if not chunk: break
        try: data = dec.decompress(chunk)
        except zlib.error: break
        buf += data
        *lines, buf = buf.split(b"\n")
        for l in lines:
            if l.strip(): yield l
    if buf.strip(): yield buf
    p.wait()
    yield ("RC", p.returncode)

def amt(x):
    if isinstance(x, dict) and isinstance(x.get("amount"), (int, float)): return x["amount"], x.get("currency")
    return None, None

def main():
    pub, key, bcountry, files, out = sys.argv[1:6]
    name = sys.argv[sys.argv.index("--name") + 1] if "--name" in sys.argv else key
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stats = collections.Counter(); buyers = set(); ca_buyers = set(); seen_ids = set()
    with gzip.open(out, "wt", encoding="utf-8") as fo:
        for fname in files.split(","):
            n0 = stats["releases"]
            for line in stream(pub, fname):
                if isinstance(line, tuple):
                    print("curl rc", fname, line[1], file=sys.stderr); continue
                stats["releases"] += 1
                try: rel = json.loads(line)
                except Exception: stats["bad_json"] += 1; continue
                parties = [x for x in (rel.get("parties") or []) if isinstance(x, dict)]
                cap = {}
                for p in parties:
                    k = is_ca(p)
                    if k and (p.get("id") is not None or p.get("name")): cap[str(p.get("id"))] = (p, k)
                if not cap: continue
                byid = {str(p.get("id")): p for p in parties}
                stats["releases_with_ca_party"] += 1
                buyer = rel.get("buyer") or {}
                bp = byid.get(str(buyer.get("id"))) or next((p for p in parties if "buyer" in (p.get("roles") or []) or "procuringEntity" in (p.get("roles") or [])), None) or {}
                bname = (buyer.get("name") or bp.get("name") or "").strip()
                tender = rel.get("tender") or {}
                contracts = rel.get("contracts") or []
                awards = rel.get("awards") or []
                any_linked = any(aw.get("suppliers") for aw in awards)
                units = []
                for aw in awards:
                    ca_s = []
                    for s in (aw.get("suppliers") or []):
                        if str(s.get("id")) in cap and "supplier" in (cap[str(s.get("id"))][0].get("roles") or ["supplier"]):
                            ca_s.append(cap[str(s.get("id"))] + ("awards[].suppliers",))
                    units.append((aw, ca_s))
                if not any_linked:
                    # eForms-style releases: awards carry no supplier list; the winner is the party with role "supplier"
                    fb = [cap[k] + ("parties[].roles contains supplier (award not linked)",) for k in cap if "supplier" in (cap[k][0].get("roles") or [])]
                    if fb: units = [(awards[0] if awards else {}, fb)]
                for aw, ca_s in units:
                    if not ca_s: continue
                    stats["awards_ca_supplier"] += 1
                    if not bname: stats["no_buyer_name"] += 1; continue
                    cons = [c for c in contracts if str(c.get("awardID")) == str(aw.get("id"))] or ([contracts[0]] if (not any_linked and contracts) else [])
                    c0 = cons[0] if cons else {}
                    end = d10((c0.get("period") or {}).get("endDate")) or d10((aw.get("contractPeriod") or {}).get("endDate"))
                    start = d10((c0.get("period") or {}).get("startDate")) or d10((aw.get("contractPeriod") or {}).get("startDate"))
                    adate = d10(c0.get("dateSigned")) or d10(aw.get("date")) or d10(rel.get("date"))
                    first = start or adate
                    if aw.get("status") in ("cancelled", "unsuccessful") or c0.get("status") in ("cancelled", "terminated"): stats["cancelled"] += 1; continue
                    if end:
                        if end < REF: stats["ended"] += 1; continue
                        if first and first > REF: stats["future_start"] += 1; continue
                        status, basis = "ongoing", "contract/award period end date %s >= %s and start/award date %s <= %s (OCDS %s)" % (end, REF, first, REF, "contracts[].period.endDate" if d10((c0.get("period") or {}).get("endDate")) else "awards[].contractPeriod.endDate")
                    else:
                        if not adate or adate < "2024-11-12": stats["no_end_old"] += 1; continue
                        status, basis = "end_date_unknown", "no end date published; award/contract date %s is on or after 2024-11-12" % adate
                    val, cur = amt(c0.get("value")); 
                    if val is None: val, cur = amt(aw.get("value"))
                    for sp, kf, via in ca_s:
                        sid = sp.get("id")
                        rid = "%s:%s:%s:%s" % (key, rel.get("ocid"), aw.get("id"), sid)
                        if rid in seen_ids: continue
                        seen_ids.add(rid)
                        a = sp.get("address") or {}
                        bi = {}
                        if bp.get("identifier"): bi = {"%s" % (bp["identifier"].get("scheme") or "id"): bp["identifier"].get("id")}
                        vi = {}
                        if sp.get("identifier"): vi = {"%s" % (sp["identifier"].get("scheme") or "id"): sp["identifier"].get("id")}
                        baddr = bp.get("address") or {}
                        link = None
                        for doc in (tender.get("documents") or []) + (aw.get("documents") or []) + (c0.get("documents") or []):
                            pass
                        for s in rel.get("sources") or []:
                            if isinstance(s, dict) and s.get("url"): link = s["url"]
                        link = link or "https://data.open-contracting.org/en/publication/%s" % pub
                        ids = {"ocid": rel.get("ocid"), "release_id": rel.get("id"), "award_id": aw.get("id")}
                        if c0.get("id") is not None: ids["contract_id"] = c0.get("id")
                        rec = {
                            "record_id": rid,
                            "source": {"key": key, "name": name, "publisher": "OCDS publication %s via OCP Data Registry" % pub,
                                       "dataset_url": "https://data.open-contracting.org/en/publication/%s" % pub, "record_url": link, "retrieved_at": now},
                            "status": status, "status_basis": basis,
                            "contract": {"identifiers": ids, "title": c0.get("title") or aw.get("title") or tender.get("title"),
                                         "description": c0.get("description") or aw.get("description") or tender.get("description"),
                                         "instrument_type": "contract" if c0 else "award",
                                         "procurement_method": tender.get("procurementMethod"), "solicitation_procedure": tender.get("procurementMethodDetails"),
                                         "commodity": {}, "value": val, "currency": cur, "value_detail": {},
                                         "dates": {"published": d10(rel.get("date")), "signed": d10(c0.get("dateSigned")) or d10(aw.get("date")), "start": start, "end": end},
                                         "related": {}},
                            "buyer": {"name": bname, "country": (baddr.get("countryName") and bcountry) or bcountry, "type": None, "identifiers": bi, "address": baddr, "contact": bp.get("contactPoint") or {}},
                            "vendor": {"name": (sp.get("name") or "").strip(), "country": "CA", "country_basis": "parties[].address.%s = %r (party roles %s; supplier link: %s)" % (kf, a.get(kf), sp.get("roles"), via),
                                       "identifiers": vi, "address": {"line1": a.get("streetAddress"), "city": a.get("locality"), "region": a.get("region"), "postal_code": a.get("postalCode"), "country": a.get(kf)}, "contact": sp.get("contactPoint") or {}},
                            "link": link,
                            "raw": {"release": rel},
                        }
                        cl = (tender.get("mainProcurementCategory"))
                        if cl: rec["contract"]["commodity"]["main_category"] = cl
                        fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
                        stats["records_" + status] += 1
                        buyers.add(bname)
                if stats["releases"] % 200000 == 0: print(fname, dict(stats), file=sys.stderr, flush=True)
            print("done", fname, stats["releases"] - n0, "releases", file=sys.stderr, flush=True)
    print(json.dumps({"stats": dict(stats), "distinct_buyers": len(buyers)}))
if __name__ == "__main__": main()

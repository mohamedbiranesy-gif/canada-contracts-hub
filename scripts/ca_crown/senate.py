#!/usr/bin/env python3
"""Senate of Canada - "Report on Administration Contracts" (proactive disclosure), quarterly tables served by
https://sencanada.ca/umbraco/surface/ProActiveAjax/GetProActiveData?displayFor=Contracts&Year=Y&Quarter=Q (the data
source of https://sencanada.ca/en/proactive/contract/). 1 request/second.
No supplier address/country is published -> normalized/ca_crown_senate_unverified_country.jsonl.
Usage: python3 -I senate.py <download_dir> <out_main.jsonl> <out_unverified.jsonl> <stats.json>
"""
import sys, os, re, json, time, html, gzip, hashlib, datetime, collections
import requests

D, OUT, OUTU, STATS = sys.argv[1:5]
os.makedirs(D, exist_ok=True)
REF = datetime.date(2026, 10, 25)
EP = "https://sencanada.ca/umbraco/surface/ProActiveAjax/GetProActiveData"
PAGE = "https://sencanada.ca/en/proactive/contract/"
s = requests.Session(); s.headers["User-Agent"] = "contracts-research/1.0"
stats = collections.Counter()


def clean(x):
    x = re.sub(r"<br\s*/?>", "\n", x); x = re.sub(r"<[^>]+>", " ", x)
    return re.sub(r"\s+", " ", html.unescape(x)).strip()


quarters = [(y, q) for y in range(2016, 2027) for q in (1, 2, 3, 4) if (y, q) >= (2016, 3) and (y, q) <= (2026, 4)]
rows = []
log = open(os.path.join(D, "download.log"), "a")
for y, q in quarters:
    f = os.path.join(D, f"senate_{y}_Q{q}.html.gz")
    if os.path.exists(f):
        txt = gzip.open(f, "rt").read(); ts = None
    else:
        time.sleep(1.0)
        r = s.get(EP, params={"displayFor": "Contracts", "isHashRouted": "true", "Year": y, "Quarter": q, "pageUrl": PAGE}, timeout=60)
        ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        log.write(f"{ts} {r.status_code} {len(r.text)} {r.url}\n"); log.flush()
        if r.status_code != 200:
            stats["http_not_200"] += 1; continue
        txt = r.text
        with gzip.open(f, "wt") as g:
            g.write(txt)
    per = re.search(r"Period:\s*</[^>]+>\s*([^<]*)", txt)
    title_period = re.search(r"from\s*(?:<[^>]+>\s*)*([A-Z][a-z]+ \d{2}, \d{4})\s*(?:<[^>]+>\s*)*to\s*(?:<[^>]+>\s*)*([A-Z][a-z]+ \d{2}, \d{4})", txt)
    tb = re.search(r"<table.*?</table>", txt, re.S)
    if not tb:
        stats["no_table"] += 1; continue
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", tb.group(0), re.S)
    hdr = [clean(h) for h in re.findall(r"<th[^>]*>(.*?)</th>", trs[0], re.S)] if trs else []
    for tr in trs[1:]:
        cells = [clean(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if not cells or len(cells) < 3:
            continue
        rec = dict(zip(hdr, cells))
        rec["_year"] = y; rec["_quarter"] = q
        rec["_period_title"] = f"{title_period.group(1)} to {title_period.group(2)}" if title_period else None
        rec["_retrieved_at"] = ts
        rows.append(rec)
    stats["quarters_parsed"] += 1
stats["rows"] = len(rows)


def pdate(x):
    x = (x or "").strip().rstrip(",")
    for fmt in ("%B %d, %Y", "%B %d %Y", "%b %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(x, fmt).date()
        except ValueError:
            pass
    return None


def period(p):
    m = re.split(r"\s+to\s+", (p or "").replace(",,", ","), maxsplit=1)
    if len(m) == 2:
        return pdate(m[0]), pdate(m[1])
    return pdate(p), None


def money(x):
    try:
        return float(re.sub(r"[^0-9.\-]", "", (x or "").replace(",", "")))
    except ValueError:
        return None


def nk(x):
    return re.sub(r"[^A-Z0-9]", "", (x or "").upper())


groups = collections.defaultdict(list)
for r in rows:
    st, en = period(r.get("Contract Period"))
    r["_start"] = st.isoformat() if st else None; r["_end"] = en.isoformat() if en else None
    key = (nk(r.get("Provider"))[:50], nk(r.get("Subject"))[:40], r["_start"] or "")
    groups[key].append(r)
fo = open(OUT, "w"); fu = open(OUTU, "w"); by_status = collections.Counter()
for key, rs in groups.items():
    rs.sort(key=lambda r: (r["_year"], r["_quarter"]))
    last = rs[-1]
    st = datetime.date.fromisoformat(last["_start"]) if last["_start"] else None
    en = datetime.date.fromisoformat(last["_end"]) if last["_end"] else None
    if en is None:
        ends = [r["_end"] for r in rs if r["_end"]]
        en = datetime.date.fromisoformat(ends[-1]) if ends else None
    if en and en < REF:
        stats["excluded_ended"] += 1; continue
    if st and st > REF:
        stats["excluded_future_start"] += 1; continue
    status = "ongoing" if en else "end_date_unknown"
    basis = (f"ongoing: Senate administration contracts report {last['_year']} Q{last['_quarter']} Contract Period '{last.get('Contract Period')}' ends {en.isoformat()} >= 2026-10-25 and starts {st.isoformat() if st else 'n/a'} <= 2026-10-25"
             if en else f"end_date_unknown: Contract Period '{last.get('Contract Period')}' has no parseable end date")
    h = hashlib.sha1("|".join(key).encode()).hexdigest()[:16]
    rec = {"record_id": f"ca_crown_senate:{h}",
           "source": {"key": "ca_crown_senate", "name": "Senate of Canada - Report on Administration Contracts (proactive disclosure)",
                      "publisher": "Senate of Canada (Senate Administration)", "dataset_url": PAGE,
                      "record_url": f"https://sencanada.ca/en/proactive/contract/#?Year={last['_year']}&Quarter={last['_quarter']}",
                      "retrieved_at": last.get("_retrieved_at") or rs[0].get("_retrieved_at")},
           "status": status, "status_basis": basis,
           "contract": {"identifiers": {"senate_group_key": "|".join(key), "reported_quarters": [f"{r['_year']}Q{r['_quarter']}" for r in rs]},
                        "title": last.get("Subject"), "description": last.get("Comment"), "instrument_type": "contract",
                        "procurement_method": None, "solicitation_procedure": None, "commodity": {"subject": last.get("Subject")},
                        "value": money(last.get("Current Contract Value")), "currency": "CAD",
                        "value_detail": {"original_contract_value": money(last.get("Original Contract Value")), "current_contract_value": money(last.get("Current Contract Value"))},
                        "dates": {"published": None, "signed": None, "start": st.isoformat() if st else None, "end": en.isoformat() if en else None, "amended_last": None},
                        "related": {}},
           "buyer": {"name": "Senate of Canada", "country": "CA", "type": "parliamentary body", "identifiers": {"administration": "Senate Administration"}, "address": {}, "contact": {}},
           "vendor": {"name": last.get("Provider"), "country": None, "country_basis": "not published: the Senate report lists the provider name only",
                      "identifiers": {}, "address": {}, "contact": {}},
           "raw": {"rows": rs}}
    if (last.get("Provider") or "").upper() in ("PWGSC", "PSPC", "PUBLIC SERVICES AND PROCUREMENT CANADA"):
        rec["vendor"]["country"] = "CA"; rec["vendor"]["country_basis"] = "provider is a Government of Canada department (PWGSC/PSPC), located in Canada by definition"
        fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); stats["main_records"] += 1
    else:
        fu.write(json.dumps(rec, ensure_ascii=False) + "\n")
    by_status[status] += 1
fo.close(); fu.close()
json.dump({"stats": stats, "by_status": by_status}, open(STATS, "w"), indent=1)
print(dict(stats), dict(by_status))
